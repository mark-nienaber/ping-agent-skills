---
title: About password policies
description: Reference for PingDS password policy attributes covering per-server and subentry policies, validators, and generators.
component: pingds
version: 8.1
page_id: pingds:security-guide:pwp-about
canonical_url: https://docs.pingidentity.com/pingds/8.1/security-guide/pwp-about.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Security", "Setup &amp; Configuration"]
section_ids:
  pwp-per-server: Per-server password policies
  pwp-replicated: DS subentry password policies
  table-ds-pwp-password-policy: Core policy attributes
  table-ds-pwp-attribute-value-validator: Value validator attributes
  table-ds-pwp-character-set-validator: Character set attributes
  table-ds-pwp-dictionary-validator: Dictionary attributes
  table-ds-pwp-length-based-validator: Password length attributes
  table-ds-pwp-repeated-characters-validator: Repeated characters attributes
  table-ds-pwp-similarity-based-validator: Similarity attributes
  table-ds-pwp-unique-characters-validator: Unique characters attributes
  table-ds-pwp-random-generator: Generator attributes
  pwp-i-d-support: Interoperable password policies
  table-pwdpolicy: Internet-Draft attributes
  pwp-i-d-vs-server: Overrides
  ignored_attributes: Ignored attributes
  inheritance: Inheritance
---

# About password policies

DS password policies govern passwords, account lockout *(tooltip: \<div class="paragraph">
\<p>The act of making an account temporarily or permanently inactive after successive authentication failures.\</p>
\</div>)*, and account status notification.

DS servers support per-server password policies stored in the configuration, and subentry password policies stored in the (replicated) directory data:

| Type                                             | Notes                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Per-server password policies](#pwp-per-server)  | * Use for default policies, and policies for top-level administrative accounts.

* You must manually apply policy updates to each replica server configuration.

* Updates require write access to the server configuration.                                                                                                                                                   |
| [DS subentry password policies](#pwp-replicated) | - Use for all user accounts stored in application data.

- Replication applies each policy update to all replicas.

- Updates require the `subentry-write` privilege, and ACIs *(tooltip: \<div class="paragraph">&#xA;\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>&#xA;\</div>)* to write the policy. |

![Per-server policies are not replicated; subentry policies are.](../_images/pwd-policy-types.png)Figure 1. Per-Server and subentry password policies

## Per-server password policies

You manage per-server password policies with the `dsconfig` command. When changing a per-server policy, you must update each replica in your deployment.

By default, there are two per-server password policies:

* The `Default Password Policy` for users.

* The `Root Password Policy` for the directory superuser, `uid=admin`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure you keep per-server password policy settings aligned across replicated DS servers. When per-server password policy settings differ between replicas, the results can be surprising to end users.As an example, suppose the user's password policy depends on a password storage scheme enabled on the replica where the user changes their password and disabled on the replica where they later authenticate:* The user changes their password on the first replica.

  The password update succeeds.

  Replication replays the change.

* The user authenticates on the second replica.

  Authentication fails even though the second replica has the correct password hash. The password storage scheme is disabled in the local per-server configuration. |

The following example displays the default per-server password policy for users:

```console
$ dsconfig \
 get-password-policy-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --policy-name "Default Password Policy" \
 --advanced \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

> **Collapse: Show output**
>
> ```
> Property                                  : Value(s)
> ------------------------------------------:---------------------------------------------
> account-status-notification-handler       : -
> allow-expired-password-changes            : false
> allow-multiple-password-values            : false
> allow-pre-encoded-passwords               : false
> allow-user-password-changes               : true
> default-password-storage-scheme           : PBKDF2-HMAC-SHA256
> deprecated-password-storage-scheme        : -
> expire-passwords-without-warning          : false
> force-change-on-add                       : false
> force-change-on-reset                     : false
> grace-login-count                         : 0
> idle-lockout-interval                     : 0 s
> java-class                                : org.opends.server.core.PasswordPolicyFactory
> last-login-time-attribute                 : -
> last-login-time-format                    : -
> lockout-duration                          : 0 s
> lockout-failure-count                     : 0
> lockout-failure-expiration-interval       : 0 s
> max-password-age                          : 0 s
> max-password-reset-age                    : 0 s
> min-password-age                          : 0 s
> password-attribute                        : userPassword
> password-change-requires-current-password : false
> password-expiration-warning-interval      : 5 d
> password-generator                        : Random Password Generator
> password-history-count                    : 0
> password-history-duration                 : 0 s
> password-validator                        : At least 8 characters, Common passwords
> previous-last-login-time-format           : -
> require-change-by-time                    : -
> require-secure-authentication             : true
> require-secure-password-changes           : true
> skip-validation-for-administrators        : false
> state-update-failure-policy               : reactive
> ```

For detailed descriptions of each property, refer to [Password Policy](../configref/objects-password-policy.html).

These settings are configured by default:

* When granted access, users can change their passwords.

* DS servers use the standard `userPassword` attribute to store passwords.

  DS servers also support the alternative standard `authPassword` attribute.

* When you import LDIF with `userPassword` values, DS servers apply a one-way hash to the passwords before storing them.

  When a user provides a password value during a bind, for example, the server hashes the incoming password, and compares it with the stored value. This mechanism helps prevent even the directory superuser from recovering the plain text password:

  ```console
  $ ldapsearch \
   --hostname localhost \
   --port 1636 \
   --useSsl \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=admin \
   --bindPassword password \
   --baseDN dc=example,dc=com \
   "(uid=bjensen)" \
   userpassword
  ```

  > **Collapse: Show output**
  >
  > ```
  > dn: uid=bjensen,ou=People,dc=example,dc=com
  > userpassword: {PBKDF2-HMAC-SHA256}10:<hash>
  > ```

* The server can set a random password when a password administrator resets a user's password.

Many capabilities are not set by default:

* No lockout.

* No password expiration.

* No password validator to check that passwords contain the appropriate mix of characters.

If the directory service enforces password policy, configure at least the default password policy accordingly.

## DS subentry password policies

You manage password policies as LDAP subentries in the application data. Replication applies updates to subentry password policies to all other replicas. Password policy administrators do not need access to the server configuration.

The DS subentry password policy entries have the object classes:

* `ds-pwp-password-policy` for most password policy features.

* A set of password validator object classes for specific validators that derive from the abstract `ds-pwp-validator` class for password validation configuration.

* `ds-pwp-random-generator` for password generation on reset.

The following tables describe password policy attributes per object class:

### Core policy attributes

Object class: `ds-pwp-password-policy`

| Attribute                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ds-pwp-password-attribute` (required)              | The attribute type used to hold user passwords.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `ds-pwp-default-password-storage-scheme` (required) | Names of enabled password storage schemes used to encode plaintext passwords.Default: PBKDF2-HMAC-SHA256.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `cn`                                                | Name of the password policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `ds-pwp-allow-user-password-changes`                | Whether users can change their passwords, assuming access control allows it.Default: true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ds-pwp-account-status-notification-handler`        | Names of enabled account status notification handlers to use with this policy.Use the `dsconfig list-account-status-notification-handlers` command. The first column of the output shows the names. The third column shows whether the handler is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ds-pwp-allow-expired-password-changes`             | Whether the user can change an expired password with the password modify extended operation.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `ds-pwp-allow-multiple-password-values`             | Whether user entries can have multiple distinct passwords. Any password is sufficient to authenticate.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `ds-pwp-allow-pre-encoded-passwords`                | Whether users can change their passwords by providing a pre-encoded value.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `ds-pwp-deprecated-password-storage-scheme`         | Names of deprecated password storage schemes for this policy.On successful authentication, encode the password with the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `ds-pwp-expire-passwords-without-warning`           | Whether to allow a user's password to expire even if that user has never received an expiration warning notification.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ds-pwp-force-change-on-add`                        | Whether users are forced to change their passwords upon first authentication after their accounts are added.Use the `ds-pwp-max-password-reset-age` property to control how long users have to change their passwords.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `ds-pwp-force-change-on-reset`                      | Whether users are forced to change their passwords after password reset by an administrator. For this purpose, anyone with permission to change a given user's password other than that user is an administrator.Use the `ds-pwp-max-password-reset-age` property to control how long users have to change their passwords.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ds-pwp-grace-login-count`                          | Number of grace logins that a user is allowed after the account has expired so the user can update their password.Default: 0 (disabled).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ds-pwp-idle-lockout-interval`                      | Maximum number of seconds that an account may remain idle (the associated user does not authenticate to the server) before that user is locked out. Requires maintaining a last login time attribute.Default: 0 seconds (inactive).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `ds-pwp-last-login-time-attribute`                  | Name or OID of the attribute type that is used to hold the last login time for users.Default: The `last-login-time-attribute` setting from the default password policy. By default, `last-login-time-attribute` is not set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `ds-pwp-last-login-time-format`                     | Format string that is used to generate the last login time value for users.The format string must match the syntax of the `ds-pwp-last-login-time-attribute` attribute, and must be a valid format string for the `java.text.SimpleDateFormat` class.Default: `yyyyMMddHHmmss'Z'`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `ds-pwp-lockout-duration`                           | Duration that an account is locked after too many authentication failures.Default: 0 seconds (account remains locked until the administrator resets the password).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `ds-pwp-lockout-failure-count`                      | Maximum number of authentication failures that a user is allowed before the account is locked out.Default: 0 (disabled).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ds-pwp-lockout-failure-expiration-interval`        | Duration before an authentication failure is no longer counted against a user for the purposes of account lockout.Default: 0 seconds (never expire).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ds-pwp-max-password-age`                           | Duration that a user can continue using the same password before it must be changed (the password expiration interval).Default: 0 seconds (passwords never expire).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `ds-pwp-max-password-reset-age`                     | Maximum number of seconds that users have to change passwords after they have been reset by an administrator before they become locked.Users are only required to change their password after it is reset if `ds-pwp-force-change-on-add` or `ds-pwp-force-change-on-reset` is true.Default: 0 seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `ds-pwp-min-password-age`                           | Minimum duration after a password change before the user is allowed to change the password again.Default: 0 seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ds-pwp-password-change-requires-current-password`  | Whether user password changes must include the user's current password before the change is allowed. This can be done with either the password modify extended operation, or a modify operation using delete and add.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ds-pwp-password-expiration-warning-interval`       | Duration before a user's password actually expires that the server begins to include warning notifications in bind responses for that user.Default: 5 days.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `ds-pwp-password-history-count`                     | Maximum number of former passwords to maintain in the password history.A value of zero indicates that either no password history is to be maintained if the password history duration has a value of zero seconds, or that there is no maximum number of passwords to maintain in the history if the password history duration has a value greater than zero seconds.Default: 0.&#xA;&#xA;When modifying a password, DS checks the new password against each hashed password value in the entry.&#xA;&#xA;If the password policy specifies a computationally intensive password storage scheme, such as Argon2, Bcrypt, a PBKDF2-based scheme, PKCS5S2, or Scrypt, enabling password history multiplies the cost of changing the password.&#xA;&#xA;DS must calculate the computationally intensive hash from the new password separately for each comparison with a hashed password in the password history. As a result, if it takes 100 ms to calculate the hash for a new password, and the applicable password policy has a password history count of 7, the calculations to modify the password can take up to 700 ms. |
| `ds-pwp-password-history-duration`                  | Maximum number of seconds that passwords remain in the password history.Default: 0 seconds (inactive).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ds-pwp-previous-last-login-time-format`            | Format string(s) that might have been used with the last login time at any point in the past for users associated with the password policy.Default: `yyyyMMddHHmmss'Z'`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ds-pwp-require-change-by-time`                     | Time by which all users with the associated password policy must change their passwords. Specified in generalized time form.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `ds-pwp-require-secure-authentication`              | Whether users with the associated password policy are required to authenticate in a secure manner.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `ds-pwp-require-secure-password-changes`            | Whether users with the associated password policy are required to change their password in a secure manner that does not expose the credentials.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `ds-pwp-skip-validation-for-administrators`         | Whether passwords set by administrators are allowed to bypass the password validation process.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `ds-pwp-state-update-failure-policy`                | How the server deals with the inability to update password policy state information during an authentication attempt.One of the following:- `ignore`: If a bind attempt would otherwise be successful, then do not reject it if a problem occurs while attempting to update the password policy state information for the user.

- `proactive`: Proactively reject any bind attempt if it is known ahead of time that it would not be possible to update the user's password policy state information.

- `reactive` (default): Even if a bind attempt would otherwise be successful, reject it if a problem occurs while attempting to update the password policy state information for the user.                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Value validator attributes

Object class: `ds-pwp-attribute-value-validator`

| Attribute                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ds-pwp-attribute-value-test-reversed-password` | Whether this password validator should test the reversed value of the provided password as well as the order in which it was given.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ds-pwp-attribute-value-match-attribute`        | Name(s) of the attribute(s) whose values should be checked to determine whether they match the provided password.If no values are provided, then the server checks if the proposed password matches the value of any user attribute in the user's entry. The server does not check values of operational attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ds-pwp-attribute-value-check-substrings`       | Whether this password validator is to match portions of the password string against attribute values and portions of attribute values against the password string.When false, the server checks whether the entire password matches any user attribute values. When true, the server checks whether the password contains portions of attribute values and whether the attribute values contain portions of the password.Consider the case of Babs Jensen (`uid: bjensen`) changing her password. The following table describes the effects of the settings:Setting	New Password	Password Modification Result&#xA;&#xA;ds-pwp-attribute-value-check-substrings: false&#xA;&#xA;&#x9;&#xA;&#xA;bjense&#xA;&#xA;&#x9;&#xA;&#xA;Success&#xA;&#xA;&#xA;&#xA;&#xA;ds-pwp-attribute-value-check-substrings: false&#xA;&#xA;&#x9;&#xA;&#xA;bjensen&#xA;&#xA;&#x9;&#xA;&#xA;Failure: 19 (Constraint Violation)&#xA;&#xA;&#xA;&#xA;&#xA;ds-pwp-attribute-value-check-substrings: false&#xA;&#xA;&#x9;&#xA;&#xA;bjensens&#xA;&#xA;&#x9;&#xA;&#xA;Success&#xA;&#xA;&#xA;&#xA;&#xA;ds-pwp-attribute-value-check-substrings: true&#xA;&#xA;&#x9;&#xA;&#xA;bjense&#xA;&#xA;&#x9;&#xA;&#xA;Failure: 19 (Constraint Violation)&#xA;&#xA;&#xA;&#xA;&#xA;ds-pwp-attribute-value-check-substrings: true&#xA;&#xA;&#x9;&#xA;&#xA;bjensen&#xA;&#xA;&#x9;&#xA;&#xA;Failure: 19 (Constraint Violation)&#xA;&#xA;&#xA;&#xA;&#xA;ds-pwp-attribute-value-check-substrings: true&#xA;&#xA;&#x9;&#xA;&#xA;bjensens&#xA;&#xA;&#x9;&#xA;&#xA;Failure: 19 (Constraint Violation)In summary:- `bjense` is allowed when the setting is false because the password does not exactly match and rejected when the setting is true because Babs's user ID contains the password.

- `bjensen` is rejected in both cases because the password exactly matches and contains Babs's user ID.

- `bjensens` is allowed when the setting is false because the password does not exactly match and rejected when the setting is true because the password contains Babs's user ID.Default: false. |
| `ds-pwp-attribute-value-min-substring-length`   | The minimal length of the substring within the password when substring checking is enabled.Default: 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Character set attributes

Object class: `ds-pwp-character-set-validator`

| Attribute                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ds-pwp-character-set-allow-unclassified-characters` | Whether this password validator allows passwords to contain characters outside of any of the user-defined character sets and ranges.Default: false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ds-pwp-character-set-min-character-sets`            | Minimum number of character sets and ranges that a password must contain.Use in conjunction with optional character sets and ranges (those requiring zero characters). The value must include any mandatory character sets and ranges (those requiring greater than zero characters). This is useful in situations where a password must contain characters from mandatory character sets and ranges, and characters from at least N optional character sets and ranges. For example, it is quite common to require that a password contains at least one non-alphanumeric character as well as characters from two alphanumeric character sets (lower-case, upper-case, digits). In this case, this property should be set to 3. |
| `ds-pwp-character-set-character-set`                 | A character set containing characters that a password may contain, and a value indicating the minimum number of characters required from that set.Each value must be an integer (indicating the minimum required characters from the set which may be zero, indicating that the character set is optional) followed by a colon and the characters to include in that set. For example, `3:abcdefghijklmnopqrstuvwxyz` indicates that a user password must contain at least three characters from the set of lowercase ASCII letters.Multiple character sets can be defined in separate values, although no character can appear in more than one character set.                                                                   |
| `ds-pwp-character-set-character-set-ranges`          | A character range containing characters that a password may contain, and a value indicating the minimum number of characters required from that range. Each value must be an integer (indicating the minimum required characters from the range which may be zero, indicating that the character range is optional) followed by a colon and one or more range specifications.A range specification is 3 characters: the first character allowed, a minus, and the last character allowed. For example, `3:A-Za-z0-9`. The ranges in each value should not overlap, and the characters in each range specification should be ordered.                                                                                              |

### Dictionary attributes

Object class: `ds-pwp-dictionary-validator`

| Attribute                                     | Description                                                                                                                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ds-pwp-dictionary-data` (required)           | A gzipped password dictionary, one word per line.This is a single-valued attribute.                                                                                            |
| `ds-pwp-dictionary-case-sensitive-validation` | Whether this password validator should treat password characters in a case-sensitive manner.Default: false.                                                                    |
| `ds-pwp-dictionary-check-substrings`          | Whether this password validator is to match portions of the password string against dictionary words.Default: false (match only the entire password against dictionary words). |
| `ds-pwp-dictionary-min-substring-length`      | The minimal length of the substring within the password in case substring checking is enabled.Default: 0.                                                                      |
| `ds-pwp-dictionary-test-reversed-password`    | Whether this password validator should test the reversed value of the provided password as well as the order in which it was given.Default: false.                             |

### Password length attributes

Object class: `ds-pwp-length-based-validator`

| Attribute                                 | Description                                               |
| ----------------------------------------- | --------------------------------------------------------- |
| `ds-pwp-length-based-max-password-length` | Maximum plaintext password length.Default: 0 (undefined). |
| `ds-pwp-length-based-min-password-length` | Minimum plaintext password length.Default: 6.             |

### Repeated characters attributes

Object class: `ds-pwp-repeated-characters-validator`

| Attribute                                              | Description                                                                                                                            |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| `ds-pwp-repeated-characters-max-consecutive-length`    | The maximum number of times that any character can appear consecutively in a password value.Default: 0 (no maximum limit is enforced). |
| `ds-pwp-repeated-characters-case-sensitive-validation` | Whether this password validator should treat password characters in a case-sensitive manner.Default: false.                            |

### Similarity attributes

Object class: `ds-pwp-similarity-based-validator`

| Attribute                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ds-pwp-similarity-based-min-password-difference` | The minimum difference the new and old password.The implementation uses the Levenshtein Distance algorithm to determine the minimum number of changes (where a change may be inserting, deleting, or replacing a character) to transform one string into the other. It can prevent users from making only minor changes to their current password when setting a new password. Note that for this password validator to be effective, it must have access to the user's current password. Therefore, if this password validator is to be enabled, also set `ds-pwp-password-change-requires-current-password: true`.Default: 0 (no difference between passwords is acceptable). |

### Unique characters attributes

Object class: `ds-pwp-unique-characters-validator`

| Attribute                                            | Description                                                                                                                   |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `ds-pwp-unique-characters-case-sensitive-validation` | Whether this password validator should treat password characters in a case-sensitive manner.Default: false.                   |
| `ds-pwp-unique-characters-min-unique-characters`     | The minimum number of unique characters that a password will be allowed to contain.Default: 0 (no minimum value is enforced). |

### Generator attributes

Object class: `ds-pwp-random-generator`

| Attribute                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ds-pwp-random-password-character-set` (required) | Named character sets. The format of the character set is the name of the set followed by a colon and the characters that are in that set. For example, the value `alpha:abcdefghijklmnopqrstuvwxyz` defines a character set named `alpha` containing all of the lower-case ASCII alphabetic characters.                                                                                                                                                                                                                              |
| `ds-pwp-random-password-format` (required)        | The format to use for the generated password. The value is a comma-delimited list of elements in which each of those elements is comprised of the name of a character set defined in the password-character-set property, a colon, and the number of characters to include from that set. For example, a value of `alpha:3,numeric:2,alpha:3` generates an 8-character password in which the first three characters are from the `alpha` set, the next two are from the `numeric` set, and the final three are from the `alpha` set. |

## Interoperable password policies

DS servers support the Internet-Draft, [Password Policy for LDAP Directories](https://datatracker.ietf.org/doc/html/draft-behera-ldap-password-policy-09) (version 09). The password policies are expressed as LDAP subentries with `objectClass: pwdPolicy`. An Internet-Draft password policy effectively overrides settings in the default per-server password policy for users, inheriting settings that it does not support or does not include from the per-server password policy.

The following table describes Internet-Draft policy attributes:

### Internet-Draft attributes

Object class: `pwdPolicy`

| Attribute                 | Description                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `pwdAttribute` (required) | The attribute type used to hold user passwords.                                                                                                                                      |
| `pwdAllowUserChange`      | Whether users can change their passwords.Default: true.                                                                                                                              |
| `pwdExpireWarning`        | Maximum number of seconds before a user's password actually expires that the server begins to include warning notifications in bind responses for that user.Default: 432000 seconds. |
| `pwdFailureCountInterval` | Length of time before an authentication failure is no longer counted against a user for the purposes of account lockout.Default: 0 seconds (never expire).                           |
| `pwdGraceAuthNLimit`      | Number of grace logins that a user is allowed after the account has expired so the user can update their password.Default: 0 (disabled).                                             |
| `pwdInHistory`            | Maximum number of former passwords to maintain in the password history.Default: 0 (disabled).                                                                                        |
| `pwdLockoutDuration`      | Number of seconds that an account is locked after too many authentication failures.Default: 0 seconds (account remains locked indefinitely).                                         |
| `pwdMaxAge`               | Maximum number of seconds that a user can continue using the same password before it must be changed (the password expiration interval).Default: 0 seconds (disabled).               |
| `pwdMaxFailure`           | Maximum number of authentication failures that a user is allowed before the account is locked out.Default: 0.                                                                        |
| `pwdMinAge`               | Minimum number of seconds after a password change before the user is allowed to change the password again.Default: 0 seconds (disabled).                                             |
| `pwdMustChange`           | Whether users are forced to change their passwords after password reset by an administrator.Default: false.                                                                          |
| `pwdSafeModify`           | Whether user password changes must use the password modify extended operation, and must include the user's current password before the change is allowed.Default: false.             |

### Overrides

The following table lists Internet-Draft policy attributes that override the per-server policy properties:

| Internet-Draft policy attribute | Overrides this server policy property       |
| ------------------------------- | ------------------------------------------- |
| `pwdAllowUserChange`            | `allow-user-password-changes`               |
| `pwdMustChange`                 | `force-change-on-reset`                     |
| `pwdGraceAuthNLimit`            | `grace-login-count`                         |
| `pwdLockoutDuration`            | `lockout-duration`                          |
| `pwdMaxFailure`                 | `lockout-failure-count`                     |
| `pwdFailureCountInterval`       | `lockout-failure-expiration-interval`       |
| `pwdMaxAge`                     | `max-password-age`                          |
| `pwdMinAge`                     | `min-password-age`                          |
| `pwdAttribute`                  | `password-attribute`                        |
| `pwdSafeModify`                 | `password-change-requires-current-password` |
| `pwdExpireWarning`              | `password-expiration-warning-interval`      |
| `pwdInHistory`                  | `password-history-count`                    |

### Ignored attributes

DS servers *ignore* the following Internet-Draft password policy attributes:

* `pwdCheckQuality`, because DS servers have password validators.

* `pwdMinLength`, because you can use a length-based password validator instead.

* `pwdLockout`, because DS servers use other lockout-related password policy attributes.

### Inheritance

Internet-Draft based password policies inherit these settings from the default per-server policy for users:

* `account-status-notification-handlers`

* `allow-expired-password-changes`

* `allow-multiple-password-values`

* `allow-pre-encoded-passwords`

* `default-password-storage-schemes`

* `deprecated-password-storage-schemes`

* `expire-passwords-without-warning`

* `force-change-on-add`

* `idle-lockout-interval`

* `last-login-time-attribute`

* `last-login-time-format`

* `max-password-reset-age`

* `password-generator`

* `password-history-duration`

* `password-validators`

* `previous-last-login-time-formats`

* `require-change-by-time`

* `require-secure-authentication`

* `require-secure-password-changes`

* `skip-validation-for-administrators`

* `state-update-failure-policy`
