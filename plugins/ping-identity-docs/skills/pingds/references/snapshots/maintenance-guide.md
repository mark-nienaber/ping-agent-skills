---
title: Accounts
description: Configure PingDS account lockout policies, manage account status, and send account status notifications by email.
component: pingds
version: 8.1
page_id: pingds:maintenance-guide:accounts
canonical_url: https://docs.pingidentity.com/pingds/8.1/maintenance-guide/accounts.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Authentication", "Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  configure-account-lockout: Account lockout
  manage-accounts: Account management
  disable-account: Disable an account
  reactivate-account: Activate a disabled account
  account-status-notification: Account status notifications
  mail-account-status-notifications: Send account status mail
  message_templates: Message templates
---

# Accounts

## Account lockout

Account lockout settings are part of password policy. The server locks an account after the specified number of consecutive authentication failures. For example, users are allowed three consecutive failures before being locked out for five minutes. Failures themselves expire after five minutes.

The aim of account lockout is not to punish users who mistype their passwords. It protects the directory when an attacker attempts to guess a user password with repeated attempts to bind.

|   |                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Account lockout is not transactional across a replication topology. Under normal circumstances, replication propagates lockout quickly. If replication is ever delayed, an attacker with direct access to multiple replicas could try to authenticate up to the specified number of times on each replica before being locked out on all replicas. |

The following command adds a replicated password policy to activate lockout:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: cn=Lock after three failures,dc=example,dc=com
objectClass: top
objectClass: subentry
objectClass: ds-pwp-password-policy
cn: Lock after three failures
ds-pwp-password-attribute: userPassword
ds-pwp-default-password-storage-scheme: PBKDF2-HMAC-SHA256
ds-pwp-lockout-failure-expiration-interval: 5 m
ds-pwp-lockout-duration: 5 m
ds-pwp-lockout-failure-count: 3
subtreeSpecification: { base "ou=people" }
EOF
```

Users with this policy are locked out after three failed attempts in succession.

1. Successfully authenticate:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword hifalutin \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Output

   ```
   dn: uid=bjensen,ou=People,dc=example,dc=com
   mail: bjensen@example.com
   ```

2. First failure:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword fatfngrs \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Output

   ```
   The LDAP bind request failed: 49 (Invalid Credentials)
   ```

3. Second failure:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword fatfngrs \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Output

   ```
   The LDAP bind request failed: 49 (Invalid Credentials)
   ```

4. Third failure:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword fatfngrs \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Output

   ```
   The LDAP bind request failed: 49 (Invalid Credentials)
   ```

5. Try to authenticate:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=people,dc=example,dc=com" \
    --bindPassword hifalutin \
    --baseDN dc=example,dc=com \
    uid=bjensen \
    mail
   ```

   Locked out

   ```
   The LDAP bind request failed: 49 (Invalid Credentials)
   ```

## Account management

### Disable an account

1. Make sure the user running the `manage-account` command has access to perform the appropriate operations.

   Kirsten Vaughan is a member of the Directory Administrators group. For this example, she must have the `password-reset` privilege, and access to edit user attributes and operational attributes:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: uid=kvaughan,ou=People,dc=example,dc=com
   changetype: modify
   add: ds-privilege-name
   ds-privilege-name: password-reset

   dn: ou=People,dc=example,dc=com
   changetype: modify
   add: aci
   aci: (target="ldap:///ou=People,dc=example,dc=com")(targetattr ="*||+")
    (version 3.0;acl "Admins can run amok"; allow(all)
     groupdn = "ldap:///cn=Directory Administrators,ou=Groups,dc=example,dc=com";)
   EOF
   ```

   Notice here that the directory superuser, `uid=admin`, assigns privileges. Any administrator with the `privilege-change` privilege can assign privileges. However, if the administrator can update administrator privileges, they can assign themselves the `bypass-acl` privilege. Then they are no longer bound by access control instructions, including both user data ACIs and global ACIs. For this reason, do not assign the `privilege-change` privilege to normal administrator users.

2. Set the account status to disabled:

   ```console
   $ manage-account \
    set-account-is-disabled \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
    --bindPassword bribery \
    --operationValue true \
    --targetDN uid=bjensen,ou=people,dc=example,dc=com \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin
   ```

   > **Collapse: Show output**
   >
   > ```
   > Account Is Disabled:  true
   > ```

### Activate a disabled account

Clear the disabled status:

```console
$ manage-account \
 set-account-is-disabled \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
 --bindPassword bribery \
 --operationValue false \
 --targetDN uid=bjensen,ou=people,dc=example,dc=com \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin
```

> **Collapse: Show output**
>
> ```
> Account Is Disabled:  false
> ```

## Account status notifications

DS servers can send mail about account status changes. The DS server needs an SMTP server to send messages, and needs templates for the mail it sends. By default, message templates are in English, and found in the `/path/to/opendj/config/messages/` directory.

DS servers generate notifications only when the server writes to an entry or evaluates a user entry for authentication. A server generates account enabled and account disabled notifications when the user account is enabled or disabled with the `manage-account` command. A server generates password expiration notifications when a user tries to bind.

For example, if you configure a notification for password expiration, that notification gets triggered when the user authenticates during the password expiration warning interval. The server does not automatically scan entries to send password expiry notifications.

DS servers implement controls that you can pass in an LDAP search to determine whether a user's password is about to expire. Refer to [Supported LDAP controls](../ldap-reference/controls.html) for a list. Your script or client application can send notifications based on the results of the search.

### Send account status mail

1. Configure an SMTP server to use when sending messages:

   ```console
   $ dsconfig \
    create-mail-server \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --server-name "SMTP server" \
    --set enabled:true \
    --set auth-username:mail.user \
    --set auth-password:password \
    --set smtp-server:smtp.example.com:587 \
    --set trust-manager-provider:"JVM Trust Manager" \
    --set use-start-tls:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Prepare the DS server to mail users about account status.

   The following example configures the server to send text-format mail messages:

   ```console
   $ dsconfig \
    set-account-status-notification-handler-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --handler-name "SMTP Handler" \
    --set enabled:true \
    --set email-address-attribute-type:mail \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   Notice that the server finds the user's mail address on the attribute on the user's entry, specified by `email-address-attribute-type`. You can also configure the `message-subject` and `message-template-file` properties. Use interactive mode to make the changes.

   You find templates for messages by default under the `config/messages` directory. Edit the templates as necessary.

   If you edit the templates to send HTML rather than text messages, then set the advanced property, `send-email-as-html`:

   ```console
   $ dsconfig \
    set-account-status-notification-handler-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --handler-name "SMTP Handler" \
    --set enabled:true \
    --set send-email-as-html:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

3. Adjust applicable password policies to use the account status notification handler you configured:

   ```console
   $ dsconfig \
    set-password-policy-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --policy-name "Default Password Policy" \
    --set account-status-notification-handler:"SMTP Handler" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   When configuring a subentry password policy, set the `ds-pwp-account-status-notification-handler` attribute, an attribute of the `ds-pwp-password-policy` object class.

## Message templates

When editing the `config/messages` templates, use the following tokens, which the server replaces with text:

* `%%notification-type%%`

  The name of the notification type.

* `%%notification-message%%`

  The message for the notification.

* `%%notification-user-dn%%`

  The string representation of the user DN that is the target of the notification.

* `%%notification-user-attr:attrname%%`

  The value of the attribute specified by attrname from the user's entry.

  If the specified attribute has multiple values, then this is the first value encountered. If the specified attribute does not have any values, then this is an empty string.

* `%%notification-property:propname%%`

  The value of the specified property.

  If the specified property has multiple values, then this is the first value encountered. If the specified property does not have any values, then this is an empty string.

  Valid propname values include the following:

  * `account-unlock-time`

  * `new-password`

  * `old-password`

  * `password-expiration-time`

  * `password-policy-dn`

  * `seconds-until-expiration`

  * `seconds-until-unlock`

  * `time-until-expiration`

  * `time-until-unlock`
