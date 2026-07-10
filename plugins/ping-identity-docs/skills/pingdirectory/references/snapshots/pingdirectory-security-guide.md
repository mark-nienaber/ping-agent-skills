---
title: Access control
description: The server's access control subsystem provides a way to examine each request that a client issues to determine whether it should be allowed.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_access_control
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_access_control.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Access control

The server's access control subsystem provides a way to examine each request that a client issues to determine whether it should be allowed.

It can also examine each search result entry to determine whether the client should be permitted to retrieve it at all, and if so, which attributes or even attribute values should be permitted.

The server's access control policy is constructed from a set of access control instructions (ACIs), also called access control rules. ACIs can be defined in user data in the ACI operational attribute, and they can also be defined in the configuration in the `global-aci` property in the access control handler configuration.

The server's access control policy denies all access by default. Unless there is an ACI that allows something, then no user who is subject to access control is permitted to perform the requested operation or retrieve the specified data. It is also possible to explicitly deny access to something, which overrides any permission that would have otherwise granted access to it.

---

---
title: Account security considerations
description: There are several things to keep in mind when creating and managing user accounts.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_consids_acct_security
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_consids_acct_security.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Account security considerations

There are several things to keep in mind when creating and managing user accounts.

---

---
title: Account status notifications
description: Account status notifications are used to notify users (or administrators) about events that affect their accounts or potentially to invoke custom code if such events occur.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_acct_status_notifications
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_acct_status_notifications.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Account status notifications

Account status notifications are used to notify users (or administrators) about events that affect their accounts or potentially to invoke custom code if such events occur.

The types of events that can generate account status notifications include:

* The account has been locked after too many failed authentication attempts.

* A bind attempt failed because it has been too long since the user last authenticated.

* A bind attempt failed because the user did not choose a new password in a timely manner after an administrative reset.

* A bind attempt failed because the password was rejected by one or more bind password validators.

* The account has been unlocked by an administrator.

* The account has been disabled or enabled by an administrator.

* A bind attempt failed because the account is not yet active or has expired.

* A bind attempt failed because the password is expired.

* The user's password is about to expire.

* The user has changed their own password.

* The user's password has been reset by an administrator.

* The user's account has been created with an add request that matches a defined set of criteria.

* The user's account has been updated with a modify or modify distinguished name (DN) request that matches a defined set of criteria.

The following password policy configuration property can be used to configure one or more account status notification handlers for use with that policy:

* `account-status-notification-handler`

  The set of account status notification handlers that should be invoked for users associated with the password policy.

  The server offers support for a few types of account status notification handlers by default, including:

  * A multi-part email account status notification handler that can generate elaborate email messages (containing plain-text and HTML-formatted body text and an optional set of attachments) from customizable templates.

  * A legacy SMTP account status notification handler that can generate simple plain-text email messages.

  * An error log account status notification handler that can record a message in the server's error log when such events occur.

  You can also use the UnboundID Server SDK to create custom account status notification handlers if desired.

  |   |                                                                                                                                                                                                                                                                                                                                                  |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You can find details about configuring the multi-part email account status notification handler in the `config/sample-dsconfig-batch-files/enable-email-account-status-notifications.dsconfig` batch file and about the options for customizing the email templates in the `config/account-status-notification-email-templates/README.txt` file. |

---

---
title: Account status notifications
description: PingDirectory server can generate account status notifications whenever certain events occur in the server regarding an account's state.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_acct_status_notifs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_acct_status_notifs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Account status notifications

PingDirectory server can generate account status notifications whenever certain events occur in the server regarding an account's state.

These notifications are used to notify end users or administrators about that event, or potentially to invoke custom code in response to them. For more information, see the [Account status notifications](pd_sec_acct_status_notifications.html) section in the discussion on password policies.

---

---
title: ACI bind rules
description: Bind rules are used to identify the set of requesters to which an ACI applies.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_aci_bind_rules
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_aci_bind_rules.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  userdn: userdn
  groupdn: groupdn
  connectioncriteria: connectioncriteria
  secure: secure
  userattr: userattr
  authmethod: authmethod
  ip: ip
  dns: dns
  dayofweek: dayofweek
  timeofday: timeofday
  oauthscope: oauthscope
---

# ACI bind rules

Bind rules are used to identify the set of requesters to which an ACI applies.

ACIs can have multiple bind rules to specify multiple conditions that can be satisfied. Bind rules can be combined using either the `and` or the `or` keyword such as `userdn="ldap:///uid=admin,dc=example,dc=com` or `groupdn="ldap:///cn=administrators,ou=Groups,dc=example,dc=com`. The `not` keyword is also used to negate the result of a bind rule.

## `userdn`

The `userdn` bind rule is used to target a requester based on their authenticated identity. The value of this bind rule must be in the form of an Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* URL although in some cases it might not actually be a valid URL (for example, because the distinguished name (DN) element is not actually a valid DN). The LDAP URL can take several forms, including:

* It can have an LDAP URL that contains just a DN, without any wildcard, scope, or filter: `"ldap:///uid=admin,dc=example,dc=com"`.

* It can contain an LDAP URL that contains a DN that has a pattern with asterisks as wildcards. Wildcards can be used as follows:

  * In place of an entire attribute value: `userdn="ldap:///uid=*,ou=People,dc=example,dc=com`

  * In place of a portion of an attribute value: `userdn="ldap:///uid=admin-*,ou=People,dc=example,dc=com`

  * In place of an attribute type: `userdn="ldap:///*=jdoe,ou=People,dc=example,dc=com`

  * In place of a single entire RDN component: `userdn="ldap:///uid=admin,*,dc=example,dc=com`

  * Two consecutive asterisks in place of any number of entire RDN components: `userdn="ldap:///uid=admin,**,dc=example,dc=com`

* It can have an LDAP URL that contains a parameterized DN. See the [Parameterized ACIs](pd_sec_parameterized_acis.html) section for more information about this.

* It can have an LDAP URL in which the DN is the string `anyone`: `userdn="ldap:///anyone`. This indicates that the ACI applies to any client, regardless of whether they are authenticated.

* It can have an LDAP URL in which the DN is the string `all`: `userdn="ldap:///all`. This indicates that the ACI applies to any authenticated client (regardless of the authentication identity), but not to unauthenticated or anonymous clients.

* It can have an LDAP URL in which the DN is the string `self`: `userdn="ldap:///self`. This indicates that the ACI applies to any operation in which the authenticated user is targeting their own entry.

* It can have an LDAP URL in which the DN is the string `parent`: `userdn="ldap:///parent`. This indicates that the ACI applies to any operation that targets an entry whose immediate parent is the requester's own entry. That is, it allows a requester to perform operations on entries immediately below their own.

* It can be a full LDAP URL, including a base DN (without wildcards or parameterization), scope, and filter suh as `userdn="ldap:///dc=example,dc=com??sub?(objectClass=person)"`.

The `userdn` bind rule can also contain multiple LDAP URLs. In that case, each URL should be separated by two consecutive vertical bar characters `||`: `("userdn="ldap:///uid=jdoe,ou=People,dc=example, dc=com || uid=jpublic,ou=People,dc=example,dc=com"")`.

The `!=` operator can be used as an alternative to the `=` operator: `userdn!="ldap:///uid=admin,ou=People,dc=example,dc=com"`. In that case, the bind rule matches if the provided value does not match the authenticated identity.

## `groupdn`

The `groupdn` bind rule is used to target a requester based on their group membership. The value of this bind rule must be an LDAP URL, such as `groupdn="ldap:///cn=Admin Users,ou=Groups,dc=example,dc=com"`. Only the DN element of the URL is used, and that DN must not contain any wildcards or parameterization.

The `groupdn` bind rule considers both direct group membership and nested membership such as if the user is a member of a group that is itself a member of a group listed in the `groupdn` value.

As with the `userdn` bind rule, the value of the `groupdn` bind rule can include multiple LDAP URLs separated by two consecutive vertical bar characters.

The `!=` operator can be used as an alternative to the `=` operator: `groupdn!="ldap:///cn=Administrators,ou=Groups,dc=example,dc=com"`. In that case, the bind rule matches if authenticated user is not a member of the specified group.

## `connectioncriteria`

The `connectioncriteria` bind rule allows or denies an operation based on whether the client connection matches a given connection criteria definition.

If present in an access control rule, the operator must be either "`=`" or "`!=`". The value must be enclosed in quotation marks, and it must be the name or full DN of the configuration object that defines the desired connection criteria.

For example, you can use a modification like the following to allow any client matching the "Root Users and Topology Administrators" connection criteria to have full read and write access to entries below `dc=example,dc=com`:

```
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr="*")(version 3.0; acl "Full read and write access for
  administrators"; allow (read,search,compare,write)
  connectioncriteria="Root Users and Topology Administrators";)
```

## `secure`

The `secure` bind rule allows or denies an operation based on whether the client is communicating with the server over a secure connection; for example, using LDAPS or StartTLS over LDAP.

If present in an access control rule, the operator must be either "`=`" or "`!=`", and the value must be either `"true"` or `"false"` including the quotation marks. With this in mind, the `secure` bind rule takes the following forms:

* `secure="true"` indicates that the ACI will apply only if the connection was received over a secure connection.

* `secure="false"` indicates that the ACI will only apply if the connection was received over a non-secure connection.

* `secure!="true"` indicates that the ACI will apply only if the connection was received over a non-secure connection.

* `secure!="false"` indicates that the ACI will apply only if the connection was received over a secure connection.

For example, you can use a modification like the following to allow users below `dc=example,dc=com` to update their own passwords over a secure connection:

```
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr="userPassword")(version 3.0; acl "Allow users to update
  their own passwords over a secure connection"; allow (write)
  userdn="ldap:///self" and secure="true";)
```

## `userattr`

The userattr bind rule can be used to target a requester based on their relation to the value of an attribute in the target entry. The value of the bind rule should contain the name of an attribute followed by the octothorpe character (#) and a keyword or attribute value.

There are four forms that userattr values can take:

* An attribute name followed by an octothorpe and the keyword `USERDN`, which indicates that the specified attribute should have a value that matches the DN of the authenticated user. For example, `userattr="manager#USERDN"` can be used to allow an operation if it targets an entry whose manager attribute has a value that matches the DN of the authenticated user.

* An attribute name followed by an octothorpe and the keyword `GROUPDN`, which indicates that the specified attribute should have a value that matches the DN of a group in which the authenticated user is a member. For example, `userattr="allowedEditors#GROUPDN"` can be used to allow an operation if it targets an entry whose `allowedEditors` attribute has a value that matches the DN of a group that contains the authenticated user either directly or indirectly through a nested group.

* An attribute name followed by an octothorpe and the keyword `LDAPURL`, in which case the value of the specified attribute must be an LDAP URL that is compared against the authenticated user's entry. For example, `userattr="allowedEditorCriteria#LDAPURL"` can be used to allow an operation if it targets an entry whose `allowedEditorCriteria` attribute has a value that is an LDAP URL whose base, scope, and filter matches the authenticated user's entry.

* An attribute name followed by an octothorpe and any value that is not one of `USERDN`, `GROUPDN`, or `LDAPURL`. In this case, that value is assumed to be an attribute value, and the operation can be authorized if both the authenticated user's entry and the target user's entry have that attribute value for the specified attribute. For example, `userattr="ou#Sales"` can be used to allow a user with an ou value of `Sales` to process operations against other users with an ou value of `Sales`.

When using the `USERDN` keyword, you can optionally specify a parent component to indicate that the target entry can be up to four levels below the authenticated user's entry. In this case, the word parent should be followed by an opening square bracket (\[), a comma-delimited list of digits between 0 and 4 (inclusive), a closing square bracket (]), a period, and the rest of the value. A value of zero matches if the attribute value contains a DN that matches that of the authenticated user, while A value of four matches if the attribute value contains a DN that is exactly four levels below the authenticated user's entry. For example, `userattr="parent[0,1,2,3,4].manager#USERDN"` can be used to allow an operation if it targets a user whose manager attribute contains a value that matches the DN of the authenticated user or is up to four levels below that DN.

The `!=` operator can be used as an alternative to the `=` operator such as `userattr!="manager#USERDN"`. In that case, the bind rule matches if the provided value does not match for the authenticated user.

## `authmethod`

The `authmethod` bind rule is used to target a requester based on the mechanism that they used to authenticate to the server. The value for this element can take one of the following forms:

* `none`

  This matches if the requester is not authenticated; `authmethod="none"`.

* `simple`

  This matches if the requester authenticated using non-anonymous LDAP simple authentication; `authmethod="simple"`.

* `ssl`

  This matches if the requester authenticated using a client certificate; `authmethod="ssl"`. This is equivalent to `authmethod="SASL EXTERNAL"`.

* `sasl <mechanisimName>`

  This matches if the requester authenticated using the specified SASL mechanism: `authmethod="SASL PLAIN"`.

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `ssl` value does not necessarily match just because the client is communicating with the server over a secure connection. Instead, it only matches if the client authenticated to the server with a client certificate chain using the SASL EXTERNAL mechanism. |

The `!=` operator can be used as an alternative to the `=`operator: `authmethod!="simple"`. In that case, the bind rule matches if the client is not authenticated using the specified mechanism.

## `ip`

The ip bind rule can be used to target a requester based on the IP address of the client system. The value can be a comma-delimited list of any of the following IP address patterns:

* A specific IPv4 address: `ip="1.2.3.4"`.

* An IPv4 address that uses the asterisk as a wildcard character to specify a range of addresses: `ip="1.2.3.*"`.

* An IPv4 address is followed by a plus sign and a subnet mask to specify a range of addresses: `ip="1.2.3.0+255.255.255.0"`.

* An IPv4 address using CIDR notation to specify a range of addresses: `ip="1.2.3.0/24"`.

* An IPv6 address as described in [RFC 2373](https://www.ietf.org/rfc/rfc2373.txt): `ip="0:0:0:0:0:0:0:1"`. IPv6 shorthand notation is also allowed: `ip="::1"`.

The `!=` operator can be used as an alternative to the "=" operator: `ip!="1.2.3.0/24"`. In that case, the bind rule matches if the client does not match the given IP address pattern.

## `dns`

The `dns` bind rule can be used to target a requester based on a resolvable host name. The value can be a comma-delimited list of host names in either of the following forms:

* A complete resolvable host name: `dns="client.example.com"`.

* A host name that uses the asterisk as a wildcard in the leftmost component: `dns="*.example.com"`.

The `!=` operator can be used as an alternative to the `=` operator: `dns!="*.example.com"`. In that case, the bind rule matches if the client host name does not match the provided pattern.

In general, we do not recommend using the `dns` bind rule. DNS might be vulnerable to spoofing attacks, which could help an attacker gain unauthorized access to the system. Further, if name resolution is slow (for example, as a result of a network problem or an intentional denial of service attack), then that can adversely affect the performance of the PingDirectory server.

## `dayofweek`

The `dayofweek` bind rule is used to make access control decisions based on the current day of the week, as determined by the server's current time zone. The value should be a comma-delimited list containing one or more of the following values: `sun`, `mon`, `tue`, `wed`, `thu`, `fri`, `sat`. For example, `dayofweek="mon,tue,wed,thu,fri"`.

The `!=` operator can be used as an alternative to the `=` operator: `dayofweek!="sat,sun"`. In that case, the bind rule matches if the current day of the week is not included in the provided list.

## `timeofday`

The `timeofday` bind rule is used to make access control decisions based on the current time of the day, as determined by the server's current time zone.

The value of this bind rule must be a four-digit number. The first two digits must represent the hour, with a value between `00` and `23`. The last two digits must represent the minute, with a value between `00` and `59`. For example, a value of `0123` represents a time of 1:23 a.m. in the server's time zone.

The operator for this bind rule can be one of the following:

* `=`

  The bind rule matches if the current time has the same hour and minute as specified in the value: `timeofday="0123"`.

* `!=`

  The bind rule matches if the current time has a different hour or minute than specified in the value: `timeofday!="0123"`.

* `<`

  The bind rule matches if the current time is between midnight (inclusive) and the time specified in the value (exclusive). That is, if the current time is earlier in the day than the specified time: `timeofday<"0123"`.

* `⇐`

  The bind rule matches if the current time is between midnight (inclusive) and the time specified in the value (inclusive). That is, if the current time is earlier in the day or the same as the specified time: `timeofday⇐"0123"`.

* `>`

  The bind rule matches if the current time is between the time specified in the value (exclusive) and 11:59 p.m. (inclusive). That is, if the current time is later in the day than the specified time: `timeofday>"0123"`.

* `>=`

  The bind rule matches if the current time is between the time specified in the value (inclusive) and 11:59 p.m. (inclusive). That is, if the current time is later in the day or the same as the specified time: `timeofday>="0123"`.

## `oauthscope`

The `oauthscope` bind rule is used to make access control decisions based on the set of scopes associated with an OAuth 2.0 access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* that the client used to authenticate.

The value for this bind rule might have one of the following forms:

* It can be the name of a single scope to match: `oauthscope="admin_user"`.

* It can be a substring assertion that contains one or more asterisks to use as wildcards: `oauthscope="admin_*"`.

* It can be a single asterisk to indicate that any scope is sufficient: `oauthscope="*"`.

The `!=` operator can be used as an alternative to the `=` operator: `oauthscope!="admin_user"`. In that case, the bind rule matches if the user does not have the specified scope.

---

---
title: ACI rights
description: The rights section of an ACI defines the permissions that are granted or denied to requesters identified by the bind rule for operations against the data specified by the target.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_aci_rights
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_aci_rights.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2024
page_aliases: ["pd_ds_allow_add_aci.adoc"]
section_ids:
  read: read
  search: search
  compare: compare
  write: write
  selfwrite: selfwrite
  add_aci: add
  delete: delete
  import-and-export: import and export
  proxy: proxy
  all: all
  allow_add_aci: Changing the allow add ACI behavior for entries
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# ACI rights

The rights section of an ACI defines the permissions that are granted or denied to requesters identified by the bind rule for operations against the data specified by the target.

Every ACI must allow or deny one or more rights.

## `read`

The `read` right covers access to attributes within search result entries. If a client does not have the `read` right for an attribute in a search result entry, then it is stripped out of the entry when it is returned to the client.

## `search`

The `search` right covers permission to use attributes in a search filter. When performing a search (regardless of its scope), the requester must have `search` permission for all attributes in the filter.

If the requester has `search` permission for all attributes used in the filter, but only for a portion of the subtree used as the scope for the search, then only entries that reside in portions of the DIT where the search right is granted can be retrieved. For example, if a user has the search right for the `cn` attribute below `ou=People,dc=example,dc=com`, then a search based at `dc=example,dc=com` with a filter that contains the `cn` attribute only returns matching entries below `ou=People,dc=example,dc=com` even if there are other entries matching the filter below `dc=example,dc=com` but outside of `ou=People,dc=example,dc=com`.

## `compare`

The `compare` right covers permission to perform a compare assertion for a specified set of attributes.

A compare assertion includes an entry DN, an attribute name, and an assertion value. If the specified entry has the given attribute with the provided assertion value, then the server returns a result of `compareTrue` (result code 6). If the entry does not have the indicated attribute value, then the server returns a result of `compareFalse` (result code 5). However, if the requester does not have permission to perform that compare assertion, then the server returns a result of `insufficientAccessRights` (result code 50).

## `write`

The `write` right covers permission to update attributes in an entry. This includes modify operations, and it also includes modify DN operations that do not specify a newSuperior (that is, modify distinguished name (DN) operations that only attempt to rename an entry and do not attempt to move it beneath a new parent). This does not include adding new entries or deleting existing entries.

## `selfwrite`

The `selfwrite` right is a limited subset of the `write` permission. It covers permission for a user to add their own DN to the set of values for specified attributes or for a user to remove their own DN from the set of values for those attributes. This is typically used to allow a user to add themselves to or remove themselves from static groups.

The `selfwrite` right should only be used for attributes that have a syntax of either distinguished name or name and optional UID. Attempts to use it for attributes with other syntaxes can fail or result in unexpected behavior.

## `add`

The `add` right covers permission to add new entries to the server. The requester must have `add` permission for at least one attribute included in the entry to be added.

## `delete`

The `delete` right covers permission to remove entries from the server. For the delete operation, the requester only needs to have the `delete` right for the target entry and not for individual attributes within the entry. However, the server enforces any `targattrfilters` restrictions for attribute values contained in the entry to be deleted. If a `targattrfilters` restriction is used to limit the set of values that the requester can delete, then they are only allowed to delete entries containing those values.

## `import` and `export`

Although you might assume otherwise from their names, the `import` and `export` rights don't have any relation to importing data from LDIF or exporting data to LDIF. Instead, these rights cover permission to move entries within the DIT (using a modify DN operation that includes a newSuperior). The `import` right is required to move the entry below its new parent, and the `export` right is required to move an entry out from under its current parent.

These rights aren't required to perform a modify DN operation that doesn't attempt to move the entry below a new parent. That's covered by the `write` right.

## `proxy`

The `proxy` right covers the ability to process an operation under the authority of an alternate authorization identity. This includes:

* Requests that include a proxied authorization request control

* Requests that include an intermediate client request control with a userIdentity

* SASL bind requests that request an alternate authorization identity

Because the ability to impersonate another user is a very sensitive operation, the requester must have the `proxied-auth` privilege for the operation to be allowed.

## `all`

The `all` right is a shorthand notation that includes the capabilities of all of the other access control rights except for `import`, `export`, and `proxy`. Using the `all` right is equivalent to using `read`, `search`, `compare`, `write`, `selfwrite`, `add`, and `delete`.

## Changing the allow add ACI behavior for entries

You can require a bind user to have `allow add` permissions for all of an entry's attributes before allowing them to add the entry to PingDirectory.

### About this task

By default, a bind user can add an entry to PingDirectory if they have `allow add` permissions for at least one of the attributes in the entry. To increase your control over who is allowed to add entries to your PingDirectory datastore, you can enable the `evaluate-target-attribute-rights-for-add-operations` property.

Enabling this property causes PingDirectory to require a bind user to have an `allow add` access control instruction (ACI) *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)* for each attribute of the entry in the add request. If the bind user doesn't meet this condition, or has a `deny add` ACI *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)* for any target attributes of the entry to be added, PingDirectory denies the add operation.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `evaluate-target-attribute-rights-for-add-operations` property is disabled by default. Enabling this property causes PingDirectory to evaluate the `targetattr` portion of an access control rule for add operations.Before enabling this property in a production environment, you should thoroughly test your existing access control configuration. You might discover cases where you need to add or augment access control rules to ensure that your authorized bind users can continue to add entries as expected. |

### Steps

* Modify the `evaluate-target-attribute-rights-for-add-operations` property.

  #### Choose from:

  * Enable the property.

    ```shell
    $ bin/dsconfig set-access-control-handler-prop \
      --set evaluate-target-attribute-rights-for-add-operations:true
    ```

  * Disable the property.

    ```shell
    $ bin/dsconfig set-access-control-handler-prop \
      --set evaluate-target-attribute-rights-for-add-operations:false
    ```

---

---
title: ACI syntax
description: The access control instruction (ACI) syntax that the PingDirectory server uses is similar to that used by other types of directory servers and is designed to make it easy to migrate data containing access control rules from other servers.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_aci_syntax
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_aci_syntax.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# ACI syntax

The access control instruction (ACI) syntax that the PingDirectory server uses is similar to that used by other types of directory servers and is designed to make it easy to migrate data containing access control rules from other servers.

Each ACI has the following format:

1. A set of one or more targets. The targets specify the data, attributes and entries, to which the ACI applies. Each ACI target is enclosed in parentheses and has the form (`name="value"`). Defined target names include:

   * `extop`: Provides a list of extended request OIDs to which the ACI applies.

   * `requestcriteria`: Determines whether an access control rule applies to an operation based on whether that operation matches a given request criteria definition.

   * `target`: Provides an LDAP URL whose distinguished name (DN) identifies the base of the subtree to which the ACI applies.

   * `targetattr`: Provides a list of attributes to which the ACI applies.

   * `targetcontrol`: Provides a list of request control OIDs to which the ACI applies.

   * `targetfilter`: Specifies a filter used to restrict the set of entries to which the ACI applies within the scope.

   * `targattrfilters`: Provides criteria for identifying the values within an attribute to which the ACI applies.

   * `targetscope`: Specifies the scope, relative to the target base DN, to which the ACI applies.

2. An opening parenthesis.

3. The string `version 3.0` to indicate the ACI syntax version. The PingDirectory server only supports 3.0.

4. A semicolon followed by a space.

5. The keyword `acl` followed by a space and a description for the access control instruction surrounded by quotation marks, such as `acl``"Allow users to update their own entries"`.

6. A semicolon followed by a space.

7. The keyword `allow` or `deny` followed by a comma-delimited list of rights enclosed in parentheses. For example, `allow`(`read`,`search`,`compare`). Available rights include:

   * `read`: Indicates that the ACI grants or denies permission to retrieve attributes in search result entries.

   * `search`: Indicates that the ACI grants or denies permission to use attributes in a search filter.

   * `compare`: Indicates that the ACI grants or denies permission to request a compare assertion against target attributes.

   * `write`: Indicates that the ACI grants or denies permission to update attributes within target entries.

   * `selfwrite`: Indicates that the ACI grants or denies permission to allow the requester to update attributes to add or remove their own DN.

   * `add`: Indicates that the ACI grants or denies permission to add entries.

   * `delete`: Indicates that the ACI grants or denies permission to delete entries.

   * `import`: Indicates that the ACI grants or denies permission to move an entry beneath its proposed new parent.

   * `export`: Indicates that the ACI grants or denies permission to move an entry out from under its current parent.

   * `proxy`: Indicates that the ACI grants or denies permission for one user to request that an operation be authorized as a different user, such as using a proxied authorization request control or SASL alternate authorization.

   * `all`: Indicates that the ACI grants or denies permission to all of the previously listed rights except for `import`, `export`, and `proxy`.

8. A semicolon followed by a space.

9. The bind rule component for the ACI, which identifies the set of requesters to which the ACI applies. Multiple bind rules can be joined with the keywords `and` and `or`, and the keyword `not` can be used to negate the result of a rule. Available bind rules include:

   * `authmethod`: Identifies the requester by the type of authentication that they used.

   * `connectioncriteria`: Allows or denies an operation based on whether the client connection matches a given connection criteria definition.

   * `dayofweek`: Identifies the requester by the current day of the week.

   * `dns`: Identifies the requester by the resolved name of the client system.

   * `groupdn`: Identifies the requester by group membership.

   * `ip`: Identifies the requester by the IP address of the client system.

   * `oauthscope`: Identifies the requester by the set of OAuth scopes that they have.

   * `secure`: Allows or denies an operation based on whether the client is communicating with the server over a secure connection; for example, using LDAPS or StartTLS over LDAP.

   * `timeofday`: Identifies the requester by the current time of day.

   * `userattr`: Identifies the requester by their relation to the value of a specified attribute.

   * `userdn`: Identifies the requester by DN or by a predefined keyword that is interpreted by the server.

10. A semicolon followed by a closing parenthesis.

For example, the following ACI allows a user to update their own password.

```
(targetattr="userPassword")(version 3.0; acl "Allow a user to update their own password"; allow (write) userdn="ldap:///self";)
```

---

---
title: ACI targets
description: ACI targets specify the set of data to which an ACI applies.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_aci_targets
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_aci_targets.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  targetattr: targetattr
  target: target
  targetscope: targetscope
  targetfilter: targetfilter
  targattrfilters: targattrfilters
  requestcriteria: requestcriteria
  targetcontrol: targetcontrol
  extop: extop
---

# ACI targets

ACI targets specify the set of data to which an ACI applies.

Each ACI target should be surrounded by parentheses and should have the form `(name="<value>")`.

An access control instruction can have multiple targets by simply placing them one right after another, such as `(targetattr="userPassword")(target="ldap:///ou=People,dc=example,dc=com")(targetscope="sub")(targetfilter="(objectClass=person)")`. All of the ACI targets must appear at the beginning of the ACI.

## `targetattr`

The `targetattr` ACI target is used to grant or deny access to a specified set of attributes. If multiple attributes are specified, then they should be separated by two consecutive vertical bars. For example, `(targetattr="givenName||sn||cn")` indicates that the ACI applies to the givenName, sn, and cn attributes.

The token `*` can be used as a shorthand notation to indicate all user attributes, but it does not include operational attributes. The token `+` can be used as a shorthand notation to indicate all operational attributes, but does not include user attributes. If you want an ACI to apply to all user attributes and all operational attributes, then you can use `` `(targetattr="*||+") ``.

It is possible to use the `!=` operator to target all user attributes except a named set. For example, `(targetattr!="userPassword")` indicates that the ACI targets all userAttributes except `userPassword`. However, this is potentially dangerous because it is easy for two different ACIs using this construct to cancel each other out. For example, if one ACI includes `(targetattr!="userPassword")` and a second ACI includes `(targetattr!="socialSecurityNumber")`, then the net effect might be equivalent to `(targetattr="*")` because the first target implicitly includes the `socialSecurityNumber` attribute that you're trying to exclude with the second, while the second implicitly includes the `userPassword` attribute that you're trying to exclude with the first. When access to a specific attribute should not be allowed, it might be better to create an ACI that denies access to that attribute rather than one that grants all access to all attributes except that attribute.

## `target`

The `target` ACI target is used to indicate that the ACI applies to entries in specified portions of the DIT. The value should be provided as an LDAP URL, but only the DN portion of that URL is used. For example, `(target="ldap:///dc=example,dc=com")` indicates that the ACI applies to entries at or below "`dc=example,dc=com`".

Each ACI can have at most one target. If an ACI defined in the user data does not contain a target element, then the effective target for that ACI would be the DN of the entry in which that ACI is defined. If a global ACI does not contain a target element, then it applies to all entries in the server, including in backends containing non-user data, like the root DSE, configuration, changelog, schema, and monitor backends. The `target` element can only use the "`=`" operator. It cannot use the `!=` operator to apply to all portions of the DIT outside of the specified distinguished name (DN).

If an ACI defined in user data includes a target element, then the DN contained in that element must be at or below the DN of the entry that contains that ACI. For example, the `ou=People,dc=example,dc=com` entry cannot have an ACI that targets entries below `ou=Groups,dc=example,dc=com`.If an ACI should not apply to all entries within the target subtree, then the `targetscope` and `targetfilter` elements can be used to narrow down the set of applicable entries.

## `targetscope`

The `targetscope` ACI target is used to specify how much of the target subtree is covered by the ACI. These scopes exhibit the same behavior in ACIs as they do for search operations. Allowed scope values include:

* `base`

  Indicates that the ACI only applies to the entry specified by the target DN, and not to any of its subordinates.

* `onelevel`

  Indicates that the ACI only applies to entries that are immediate subordinates of the entry specified by the target DN. Neither the target entry, nor any entries that are more than one level below the target entry, are included.

* `subtree`

  Indicates that the ACI applies to the entry specified by the target DN, as well as all entries below it (to any depth).

* `subordinate`

  Indicates that the ACI applies to all entries below the entry specified by the target DN (to any depth), but does not include the target entry itself.

The `targetscope` element can only use the "`=`" operator. It cannot use the `!=` operator. If an ACI does not include a `targetscope` element, a default value of `subtree` is assumed.

## `targetfilter`

The `targetfilter` ACI target is used to identify the set of entries in the target subtree to which the ACI applies based on their content. The value of this element is the string representation of an LDAP search filter, such as "`(targetfilter="(objectClass=person)")`".The `targetfilter` element can only use the "`=`" operator; it cannot use the "`!=`" operator although you can use the "`!`" operator in the filter itself to negate its meaning. If an ACI does not include a `targetfilter` element, then all entries within the target subtree and scope are considered applicable.

## `targattrfilters`

The `targattrfilters` ACI target is used to identify individual attribute values to which the ACI applies. This target is used for write operations, and it can restrict which attributes can be added to or removed from an entry.

The value of this element can have either one or two components. It can specify a set of attribute values that can be added to the entry (which must start with `add=`), a set of attribute values that can be removed from the entry (which must start with "`del=`"), or both. If both clauses are present, then they should be separated by a comma.

The content of each clause should be in the form of an attribute name followed by a colon and a search filter that identifies which values will be allowed for that attribute You can target multiple attributes in the same add or delete clause by separating them with a double ampersand `&&`.

For example, `(targattrfilters="add=description:(description=allowedAddDescription) && displayName:(displayName=allowedAddDisplayName), del=description:(description=allowedDeleteDescription)")` indicates that the ACI applies to any attempt to add a value of `allowedAddDescription` to the description attribute, an attempt to add a value of `allowedAddDisplayName` to the `displayName` attribute, or an attempt to remove a value of `allowedDeleteDescription` from the description attribute.

The filters can use a variety of logic for identifying which values are allowed. For example, you can use substring filters that include wildcards to match values that start with, end with, or contain a given substring. You can use a presence filter to indicate that any value is allowed. You can use a greater-or-equal or less-or-equal to indicate a range of allowed values. You can use AND and OR filters to combine multiple filters. You can use a NOT clause to negate a filter.

When processing an add operation, the server requires that the requester have permission to add all of the attribute values. When processing a delete operation, the server requires that the requester have permission to delete all of the attribute values. When processing a modify or modify DN operation, the server requires that the requester have permission to add all values introduced in the update and to delete all values removed in the update.The `targattrfilters` element can only use the `=` operator; it cannot use the `!=` operator.

## `requestcriteria`

The `requestcriteria` ACI target determines whether an access control rule applies to an operation based on whether that operation matches a given request criteria.

If present in an access control rule, the operator must be either "=" or "!=". The value must be enclosed in quotation marks and it must be the name or full DN of the configuration object that defines the desired request criteria.

For example, let's say that you want to allow members of the `cn=Sales Administrators,ou=Groups,dc=example,dc=com` group to be able to read from and write to the entries for the users that are members of the `cn=Sales Employees,ou=Groups,dc=example,dc=com` group. To do this, you must first create a request criteria object that will match entries for users in the `cn=Sales Employees,ou=Groups,dc=example,dc=com` group. You can do this with the following configuration change:

```
dsconfig create-request-criteria \
     --criteria-name "Requests Targeting Sales Employees" \
     --type simple \
     --set "any-included-target-entry-group-dn:cn=Sales Employees,ou=Groups,dc=example,dc=com"
```

With that request criteria defined, you can use a modification like the following to create the corresponding access control rule:

```
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr="*")(requestcriteria="Requests Targeting Sales
  Employees")(version 3.0; acl "Allow sales administrators to manage
  sales employees"; allow (read,search,compare,write)
  groupdn="ldap:///cn=Sales Administrators,ou=Groups,dc=example,dc=com";)
```

## `targetcontrol`

The `targetcontrol` ACI target is used to indicate which request controls a requester is allowed to use. The value for this element is the OID for the desired request control, and multiple request control OIDs can be separated by a double vertical bar `||`. For example, `(targetcontrol="1.2.840.113556.1.4.473||2.16.840.1.113730.3.4.9")` is used to target requests that use either or both the server-side sort request control whose OID is "`1.2.840.113556.1.4.473`" and the virtual list view request control whose OID is `2.16.840.1.113730.3.4.9`.

Regardless of the type of control and what action the server can take for requests that contain it, the read right is used when determining whether to allow an operation containing the request control. Although it is technically allowed to include other rights in an ACI that uses the `targetcontrol` target, only the read right is used in making the determination.The `targetcontrol` element can only use the `=` operator; it cannot use the `!=` operator.

## `extop`

The `extop` ACI target is very similar to the `targetcontrol` target, except that it is used to indicate which extended requests a requester is allowed to use. The value can be either a single OID or a list of multiple OIDs separated by double vertical bars.As with the `targetcontrol` element, only the read right is considered when determining whether to allow a client to request a given extended operation.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The server might impose additional access control rights based on the function that the extended operation is to perform. For example, for a client to use the password modify extended operation, the server requires an ACI with an `extop` target containing the OID `1.3.6.1.4.1.4203.1.11.1`, but it also requires that the requester have permission to update the `userPassword` attribute or whatever password attribute has been configured in the user's password policy in the target user's entry. |

---

---
title: Additional mechanisms for securing communication
description: TLS provides a strong way to ensure that unauthorized observers aren't able to interpret the network communication to and from the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_addl_mech_secure_comm
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_addl_mech_secure_comm.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sec_secure_name_service_config.adoc", "pd_sec_name_service_caching.adoc", "pd_sec_strong_tcp_seq_nums.adoc", "pd_sec_reject_source_routed_packets.adoc", "pd_sec_reject_icmp_redirects.adoc", "pd_sec_encrypt_inter_sys_comm.adoc"]
section_ids:
  secure-name-service-configuration: Secure name service configuration
  name-service-caching: Name service caching
  strong-tcp-sequence-numbers: Strong TCP sequence numbers
  reject-source-routed-packets: Reject source-routed packets
  reject-icmp-redirects: Reject ICMP redirects
  encrypt-all-inter-system-communication: Encrypt all inter-system communication
---

# Additional mechanisms for securing communication

TLS provides a strong way to ensure that unauthorized observers aren't able to interpret the network communication to and from the PingDirectory server.

It also includes a trust mechanism to help clients ensure that they are communicating with a legitimate server and not an impostor. However, there are additional steps you can take to secure network communication.

## Secure name service configuration

If possible, you should use a secure name service like DNS over TLS or DNS over HTTPS. Regular DNS, especially DNS over UDP connections, is vulnerable to hijacking attacks.

If an attacker is able to run their own DNS server, and if that server is able to respond more quickly than the legitimate DNS server, then clients can be tricked into establishing connections to the wrong server.

If a secure DNS option is not available, then another option can be to use host files for name resolution. However, this option can be difficult to maintain in dynamic environments in which server addresses might change. It is also not a feasible option if you do not have control over the client systems.

## Name service caching

If name resolution is slow, then it can adversely affect server performance.

If the server is unable to resolve a host name to the corresponding address, then it might be unable to establish a connection to an external system. In some cases, it can also affect the ability to accept client connections or evaluate access control rules.

The server logs a message if attempts to resolve a host name to an IP address fail or take a long time to complete. This can help make it easier to diagnose problems related to name resolution, but it would be better to prevent those problems in the first place.

The JVM provides its own address caching facility that can help with this. It maintains its own internal cache that maps host names to IP addresses, and each mapping is associated with a Time To Live (TTL) value that indicates how long it should be used. If the mapping between host names and IP addresses is stable in your environment, then you might want to configure the JVM to use a large TTL value to reduce its dependency on the underlying name service. From a security perspective, this is primarily useful for cases in which you cannot rely on a secure name service or host file, but it can also help mitigate the possibility of problems that could arise in the event of a name service outage. You can use the `network-address-cache-ttl` property in the global configuration to tune this value.

You might also want to consider running a caching name server on the same system as the server to provide an additional layer of protection against name service outages and to reduce network latency for name service requests.

## Strong TCP sequence numbers

Use strong TCP sequence numbers to prevent already-established TCP connections from being hijacked.

## Reject source-routed packets

Source-routed packets allow a packet's sender to specify which route it should take to its destination.

An attacker might be able to use this capability to trick the client into communicating with the wrong system. Source-routed packets are rarely used for legitimate communication.

## Reject ICMP redirects

The Internet Control Message Protocol (ICMP) offers features that can ensure that traffic gets from its source to its destination as efficiently as possible, but it can also help attackers hijack existing sessions.

ICMP redirects are intended to provide a mechanism for a router to let a client know about a better way to reach the target system, but they are rarely needed in private networks, and attackers can use them to trick the client into communicating with the wrong system.

## Encrypt all inter-system communication

Any communication that the PingDirectory server itself has with other systems should be encrypted to resist observation and interception.

This also applies to any communication that the underlying system needs to perform, including name service resolution, use of network-based filesystems, remote logging, shell access, and file transfer.

---

---
title: Administrative alerts
description: The PingDirectory server can generate administrative alerts to notify administrators of errors, warnings, and significant events that occur in the server. Each alert has a name, severity, and message.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_admin_alerts
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_admin_alerts.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Administrative alerts

The PingDirectory server can generate administrative alerts to notify administrators of errors, warnings, and significant events that occur in the server. Each alert has a name, severity, and message.

The `docs/admin-alerts-list.csv` and `docs/admin-alerts-list.html` files provide a listing of all alert types that are defined in the PingDirectory server. Some of these alert types include:

* Whenever the server begins or completes the startup process

* Whenever the server begins the shutdown process

* Whenever a change is made to the server configuration

* If the server detects that a configuration change was made with the server offline

* Whenever a change is made to the server's access control policy

* If a backend is disabled with the server online

* If an error occurs while attempting to enable a connection handler

* If an error occurs while attempting to enable a backend

* If an error occurs while trying to create or restore a backup

* If an error occurs while trying to retrieve or decode an entry from a backend database

* If the server detects that a backend was not cleanly shut down and it can take additional time to bring it back up while it performs recovery processing

* If a backend index needs to be built or is in the process of being built

* If replication has become backlogged, is missing changes, fails to replay a change, encounters a conflict that cannot be automatically resolved, or encounters some other problem

* If the server work queue has become backlogged or full

* If an attempt is made to assign a user an invalid privilege

* If available disk space becomes too low

* If debug logging is enabled

* Whenever the server executes a command on the underlying system

* Whenever the server enters or leaves lockdown mode

* Whenever an alarm is raised or cleared

* If the server detects an invalid or non-recommended Java Virtual Machine (JVM) configuration

* If the PingDirectoryProxy server changes the assessed health check state for any of its backend servers

* If the PingDirectoryProxy server encounters a problem while performing entry rebalancing processing

* If the PingDataSync server detects a backlog or encounters a problem during processing

Whenever an administrative alert is raised within the server, the server provides it to all alert handlers that are defined and enabled in the configuration. Alert handlers that are available in the PingDirectory server include:

* Error Log — Write a message about the alert to server error log.

* Exec — Execute a specified command on the underlying system.

* JMX — Emit a Java Management Extensions (JMX) notification with information about the alert.

* Output — Write a message about the alert to standard output or standard error.

* SMTP — Send an email message with information about the alert to a specified set of recipients.

* SNMP — Emit an SNMP trap with information about the alert.

* Twilio — Send an SMS text message with information about the alert using the [Twilio](https://www.twilio.com/) service.

The UnboundID Server SDK can also be used to create custom alert handler implementations.

Information about recent alerts generated by the server is also available in the `cn=alerts` backend. It is also included in the output of the `status` tool.

---

---
title: Administrative password reset
description: In most cases, if a user's account is in an unusable state, an administrative password reset can restore access.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_admin_password_reset
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_admin_password_reset.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Administrative password reset

In most cases, if a user's account is in an unusable state, an administrative password reset can restore access.

This includes:

* If a user has forgotten their password

* If the account has been locked after too many failed authentication attempts

* If the account has been locked because it has been too long since the user last authenticated

* If the account has been locked because the user failed to authenticate in a timely manner after an administrative reset

* If the account has been locked because the user attempted to bind with a password that failed validation

* If the user's password has expired

An administrative password reset does not restore access to an account under the following circumstances:

* If the account has been administratively disabled

* If the account has an activation time that is in the future

  If the account has an expiration time, not to be confused with the password expiration time, which is in the past

---

---
title: Administrative password reset
description: An administrative password reset occurs when one user changes the password for another user.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_admin_pw_reset
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_admin_pw_reset.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Administrative password reset

An administrative password reset occurs when one user changes the password for another user.

This requires the password-reset privilege, and it also requires access control permission to update the password attribute.

You can configure PingDirectory server to require users to choose a new password after their password has been reset by an administrator. This can be accomplished through the following configuration properties:

* `force-change-on-add`

  Indicates whether a user is required to choose a new password the first time they authenticate after their account has been created. This is false by default.

* `force-change-on-reset`

  Indicates whether a user is required to choose a new password the first time they authenticate after their password has been reset by an administrator. This is false by default.

* `max-password-reset-age`

  The maximum length of time that a user has to change their password after an administrative reset before their account is locked.

If a user is forced to change their password, then the server allows that user to authenticate with the new password provided by an administrator, but the bind response includes the password expired response control and a diagnostic message indicating that they must change their password. The server also rejects any operation attempted on that connection until the user has chosen a new password.

If a maximum password reset age is configured and the user does not choose a new password within that length of time after the password reset, then the account is locked and another password reset is required to restore access to it.

See the `config/sample-dsconfig-batch-files/configure-password-reset-constraints.dsconfig` batch file for more information about forcing users to change their password after an administrative reset.

---

---
title: Alarms and gauges
description: Each PingDirectory server includes a set of gauges for tracking various metrics over time.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_alarms_gauges
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_alarms_gauges.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Alarms and gauges

Each PingDirectory server includes a set of gauges for tracking various metrics over time.

Each gauge is associated with a monitor attribute and can be configured with warning, minor, major, and critical thresholds. If the monitor value crosses one of those threshold values, then the server raises an alarm condition that might indicate a problem such as low disk space or unavailability of an external server, and can optionally trigger administrative alerts.

Like alerts, alarms have a name, severity, and message. They also have a condition that is indicated by the alarm, like "Disk Usage," and they can be associated with a specific resource, such as which filesystem is running low on disk space. If alarm conditions are published using SNMP, then they can also include probable cause and alarm type properties.

Alarms are exposed in the `cn=alarms` backend. Their values can change over time, and they can be cleared whenever the monitored value returns to normal. Active alarms can be viewed using the `status` tool.

---

---
title: Assigning password policies to users
description: Each user is associated with a password policy that governs their activity in the server, and different users can have different password policies.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_assign_password_policy
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_assign_password_policy.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sec_maintain_password_policies.adoc"]
section_ids:
  maintaining-password-policies-in-user-data: Maintaining password policies in user data
---

# Assigning password policies to users

Each user is associated with a password policy that governs their activity in the server, and different users can have different password policies.

Whenever the server processes an operation that attempts to authenticate a user, change their password, or interact with their password policy state in some way, it needs to select an appropriate password policy to use for that processing.

A user can be associated with a password policy through the `ds-pwp-password-policy-dn` operational attribute. If this attribute exists in the user's entry and refers to a valid password policy, then the user is subject to that password policy. If that attribute exists but refers to a nonexistent policy, then that user is unable to authenticate or be used as an alternate authorization identity. If a user's entry does not include the `ds-pwp-password-policy-dn` operational attribute, then that user is subject to the server's default password policy, which is specified by the default-password-policy property in the global configuration.

The `ds-pwp-password-policy-dn` operational attribute can be either real or virtual. You can explicitly set a value for the attribute in a user's entry, but it is also possible to have the server generate a value for that attribute based on some criteria using the virtual attribute subsystem. For example, you could use a virtual attribute to automatically assign the same password policy to all members of a specified group or to all users in a specified portion of the DIT.

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A user should not be conditionally subjected to different password policies under different circumstances. While it is technically possible to use virtual attributes that assign different values to the same attribute under different conditions, this capability should not be used for the `ds-pwp-password-policy-dn` attribute. |

For example, you should not attempt to detect which application has issued a request and select a password policy based on that application. The server only maintains one set of password policy state for each user, and attempting to access the same user under different password policies might have unexpected adverse effects and can introduce security risks.

## Maintaining password policies in user data

While password policies are typically defined in the server configuration, it is also possible to define them in user data.

This is particularly useful when the PingDirectory server is used to back a multi-tenant application, in which information about many different organizations is maintained in the same server instance, typically with a separate branch for each organization. You can configure password policies on a per-organization basis.

Each password policy must be defined in an entry containing the `ds-cfg-password-policy` structural object class. The definition of this object class can be found by querying the server schema over LDAP, by retrieving the "`cn=schema`" entry, or by looking in the `config/schema/02-config.ldif` schema definition file. The names of the LDAP attribute types which should correspond to names of the password policy configuration properties that are available in dsconfig or the administration console with a "`ds-cfg-`" prefix.

For example, the following entry represents a minimal password policy that might be defined in user data:

```
dn: cn=Org X Password Policy,ou=Org X,ou=tenants,dc=example,dc=com
objectClass: top
objectClass: ds-cfg-password-policy
cn: Org X Password Policy
ds-cfg-password-attribute: userPassword
ds-cfg-default-password-storage-scheme: cn=Salted SHA-256,cn=Password Storage
  Schemes,cn=config
```

Assign users to password policies contained in the user data in the same way that you assign them to policies in the configuration. Include the `ds-pwp-password-policy-dn` operational attribute in their entry as either a real or a virtual attribute.

|   |                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While password policies can reside in user data, any other configuration elements that they reference, including password storage schemes, password validators, password generators, account status notification handlers, and failure lockout actions, must reside within the configuration. |

For improved performance, the PingDirectory server maintains a cache of password policy entries that are defined in the user data. This cache holds up to 500 policies by default, but you can tune that through the `maximum-user-data-password-policies-to-cache` property in the global configuration.

---

---
title: Auditing
description: It is important to regularly audit the PingDirectory server and its content to ensure that the data remains secure.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_auditing
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_auditing.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Auditing

It is important to regularly audit the PingDirectory server and its content to ensure that the data remains secure.

---

---
title: Auditing configuration changes
description: Proper server configuration is critical to maintaining security. Be aware of all changes to the server configuration and understand whether the configuration in its current state matches what you intend and expect it to be.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_audit_config_changes
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_audit_config_changes.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  administrative-alerts: Administrative alerts
  the-configuration-audit-log: The configuration audit log
  the-configuration-archive: The configuration archive
  the-config-diff-tool: The config-diff tool
---

# Auditing configuration changes

Proper server configuration is critical to maintaining security. Be aware of all changes to the server configuration and understand whether the configuration in its current state matches what you intend and expect it to be.

## Administrative alerts

The PingDirectory server generates an administrative alert whenever a configuration change is made with the server online. It also generates an alert during startup if it detects unauthorized changes to the `dsconfig` tool in offline mode or the `manage-profile` tool.

You should make sure that an appropriate set of alert handlers are in place so that administrators are notified of configuration changes as soon as they occur.

## The configuration audit log

The PingDirectory server maintains a `logs/config-audit.log` file that contains a record of all authorized configuration changes made within the server. This includes:

* Changes made through the `dsconfig` command-line tool with the server online

* Changes made through the `dsconfig` command-line tool running in offline mode

* Changes made through the web administration console

* Changes made through the `manage-profile` tool

* Changes made through the configuration API

* Changes made by clients updating configuration entries over LDAP

The configuration audit log will not include a record of any changes made by directly editing the `config.ldif` file with the server offline, but the server should detect any such changes at startup and generate an administrative alert in response to them.

Each record in the configuration audit log should include the following information:

* A timestamp indicating when the change occurred

* The connection ID and operation ID for the request that was used to make the change

* The DN of the user who made the change and the type of authentication they used

* The address of the client system used to request the change

* A command that is used to undo the change

* The change that was applied

## The configuration archive

The PingDirectory server also maintains a configuration archive, in the `config/archived-configs` directory. This directory should contain a compressed and timestamped copy of every version of the configuration that the server has used. It also includes a version of the configuration as it existed when setup completed and a "clean" baseline configuration for the current version of the server without any customization applied.

## The `config-diff` tool

The PingDirectory server provides a `config-diff` tool to compare different versions of the server configuration and identify differences between them. This tool can compare different versions of the configuration from the same server, or it can be used to compare configurations between different servers. Any differences will be written in the form of a `dsconfig` batch file that can update the source server so that its configuration matches that of the target.

---

---
title: Auditing data access
description: It's also important to understand the kinds of requests that clients make. This can help you identify requests that are out of the ordinary, which might be evidence of a potential attack.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_audit_data_access
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_audit_data_access.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  log-analysis: Log analysis
  account-status-notification-handlers: Account status notification handlers
---

# Auditing data access

It's also important to understand the kinds of requests that clients make. This can help you identify requests that are out of the ordinary, which might be evidence of a potential attack.

## Log analysis

The primary way to accomplish this is through log analysis. It is important to regularly examine (or at least summarize) the log files to classify the types and frequency of operations being performed. A sudden increase in any one kind of traffic can be a red flag, but situations like the following might be of particular interest:

* Connections from unusual client addresses, or a spike in requests from certain clients.

* Operations that fail with invalidCredentials (49) or insufficientAccessRights (50) results.

* Search operations that fail with a timeLimitExceeded (3), sizeLimitExceeded (4), or adminLimitExceeded (11) results.

* Search operations that do not return any entries.

* Search operations that return large numbers of entries.

* Search or compare operations that explicitly attempt to retrieve or target the userPassword attribute (or another password attribute).

* Search operations that might represent attempts to exfiltrate data from the server through trawling. This can include things like repeated substring filters with subInitial filters in sequential order, such as searches with filters like `(cn=aa*)`, `(cn=ab*)`, `(cn=aa*)`, and so on. It can also include greater-or-equal and less-or-equal filters with similar patterns.

* Unindexed search attempts.

If you regularly characterize the types of operations that clients request, then you might be able to more easily identify anomalous requests.

There might be other specific events that you always want to know about. For example, you might want to know whenever clients retrieve search result entries that contain encoded passwords, or whenever a client alters the server's access control definitions or the set of privileges granted to an account. In such cases, you can create criteria to specifically identify those types of operations, and then you can use that criteria to create a logger that only records those types of events.

If you want to know about these kinds of events right away, then you could create an admin alert access logger using that criteria. This causes the server to generate an administrative alert (with an alert type of `access-log-criteria-matched`) whenever it processes an operation matching that criteria.

## Account status notification handlers

You might want to audit certain events related to password policy processing. For example, if the server is configured to lock accounts after too many failed attempts, then you might want to have a record of any time that happens. You might also want to have a record of all administrative password resets and self password changes.

This can be accomplished with account status notification handlers, and the server provides implementations that can either record messages about these kinds of events in the server error log or that can send email messages about them. If you would like to handle them in other ways, then you can use the UnboundID Server SDK to create a custom account status notification handler that implements the desired behavior.

---

---
title: Auditing data content
description: It's also a good idea to keep track of the data itself and identify any potential security-related issues that affect user entries or other data.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_audit_data_content
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_audit_data_content.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  data-security-auditors: Data security auditors
  soft-deletes: Soft deletes
---

# Auditing data content

It's also a good idea to keep track of the data itself and identify any potential security-related issues that affect user entries or other data.

## Data security auditors

One way to do this would be to regularly export the data to LDIF (ideally in encrypted form so that it is not exposed in the clear) and examine its content for unusual or undesirable conditions. You could also do this with search operations. However, in large data sets, such searches can be expensive and time consuming.

The server also provides an "audit data security" administrative task and an associated audit-data-security command-line tool that can help with this. When invoked, the task causes the server to efficiently iterate through all entries in the configured set of backends, comparing each one against a configured set of data security auditors.

The report is written into a directory structure on the server filesystem. There is a `summary.ldif` file that provides a summary of all of the processing that was performed. There is also a subdirectory for each of the backends that were examined with a set of LDIF files containing more detailed output from each of those auditors.

Data security auditors included with the PingDirectory server do the following:

* Identify all entries that contain ACIs.

* Identify administratively disabled users.

* Identify users with passwords that are expired or are about to expire.

* Identify users whose accounts are locked because of too many failed authentication attempts because it's been too long since the user authenticated or because the user did not change their password in a timely manner after an administrative reset.

* Identify users who have multiple passwords.

* Identify users who have explicitly configured privileges or root users or topology administrators who inherit the default set of root privileges.

* Identify users who have passwords encoded with password storage schemes that are considered weak.

* Identify all accounts with password policy state issues that can currently or soon affect their usability.

* Identify all accounts with activation times in the future, expiration times in the past, or expiration times in the near future.

* Identify accounts with passwords encoded using a deprecated password storage scheme.

* Identify accounts for users that have not authenticated in longer than a specified length of time.

* Identify accounts that are configured to use a nonexistent password policy (and are therefore unable to authenticate).

* Identify accounts that match a specified search filter.

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | You can also use the PingDirectory server SDK to develop custom data security auditors for identifying other kinds of issues. |

The `audit-data-security` tool offers the provided set of command-line arguments in addition to the usual options for connecting and authenticating to the server and scheduling tasks:

* `--outputDirectory`

  The directory (on the server filesystem) where the report files are created. If this is not specified, then it defaults to a directory whose name reflects the current time in the reports/audit-data-security subdirectory.

* `--reportFilter`

  An optional filter that can be used to indicate which entries should be examined. If this is provided, then only entries matching that filter are audited. Otherwise, all entries are examined. This can be provided multiple times if multiple filters should be specified, and only entries matching at least one of those filters are examined.

* `--backendID`

  An optional set of backend IDs for the backends to examine. If this is not provided, then all supported backends, including local DB backends and the server configuration, are examined.

* `--includeAuditor`

  An optional set of the names for the data security auditors that are invoked. By default, all data security auditors defined in the configuration are included, except for those excluded by the `--excludeAuditor` argument.

* `--excludeAuditor`

  An optional set of the names for the data security auditors that are not invoked.

## Soft deletes

Normally, when an authorized client deletes an entry, it is completely removed from the server. However, the PingDirectory server provides support for soft deletes, in which the server preserves the entry instead of removing it. When an entry is soft-deleted, the server makes the following changes to it:

* The server adds the ds-soft-delete-entry auxiliary object class to the entry, which causes it to be hidden from normal search results.

* The server renames the entry to add the entry's entryUUID attribute to the set of RDN attributes. This allows a new entry to be created with the same distinguished name (DN) as the former entry without conflicting with the soft-deleted form of the entry.

* The server adds the following additional operational attributes to the entry:

  * `ds-soft-delete-from-dn`: The original DN for the entry.

  * `ds-soft-delete-timestamp`: The time that the entry was soft-deleted.

  * `ds-soft-delete-requester-dn`: The DN of the user that requested the delete.

  * `ds-soft-delete-requester-ip-address`: The IP address of the client that requested the delete.

There are two ways that regular deletes can be turned into soft deletes. The first is to include the [soft delete request control](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/controls/SoftDeleteRequestControl.html) in the delete request, such as using the `--softDelete` argument to `ldapmodify`.

However, it is also possible to have the server automatically convert regular deletes into soft deletes. This can be done by creating a soft-delete policy, which can include the following properties:

* `auto-soft-delete-connection-criteria`

  Connection criteria that can identify client connections whose deletes should be converted to soft deletes.

* `auto-soft-delete-request-criteria`

  Request criteria that can identify delete requests that should be converted to soft deletes.

* `soft-delete-retention-time`

  The maximum length of time that soft-deleted entries should be retained in the server.

* `soft-delete-retain-number-of-entries`

  The maximum number of soft-deleted entries that should be retained in the server.

After a soft delete policy has been created, the global configuration can be updated to use it with the following property:

* `soft-delete-policy`

  The soft-delete policy that should be used by the server. If this is not configured, then soft deletes are disabled in the server, even for delete requests that use the soft delete request control.

Only soft-delete policies that contain values for at least one of the `auto-soft-delete-connection-criteria` and `auto-soft-delete-request-criteria` properties can automatically convert regular deletes to soft deletes. If the server has a soft delete policy without criteria, then soft deletes are only allowed with the soft delete request control.

Turning deletes into soft deletes provides a way to verify the content of deleted entries. Even though soft-deleted entries are excluded from search results by default, users with the soft-delete-read privilege can retrieve them by including the [soft-deleted entry access request control](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/controls/SoftDeletedEntryAccessRequestControl.html) in the search request, such as by providing the `--includeSoftDeletedEntries` argument to `ldapsearch`.

If necessary, `soft-deleted` entries can be resurrected with the [undelete request control](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/controls/UndeleteRequestControl.html) in an add request, such as using the `--allowUndelete` argument to `ldapmodify`. The attributes of the add request can be used to provide the details of the undelete. In particular, the DN from the add request specifies the DN to use for the resurrected entry, and the `ds-undelete-from-dn` attribute specifies the DN of the soft-deleted entry to undelete.

---

---
title: Authentication
description: Authentication is the process that a client uses to identify themselves to the server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_authentication
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_authentication.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Authentication

Authentication is the process that a client uses to identify themselves to the server.

This includes three basic components:

* Identify the account that is trying to authenticate. This is often provided in the form of a DN or username, but it can come in other forms like a Kerberos principal or information in a certificate or OAuth bearer token.

* Provide proof of that identity. This can include a password, optionally combined with a second factor like a one-time password, a certificate, or interaction with a trusted system like a Kerberos KDC or an OAuth introspection endpoint.

* Optionally specify an alternate authorization identity. Usually, when a client authenticates, subsequent operations on that connection are processed using the authority of the authenticated user. However, in some cases, it might be possible for the client to request that subsequent operations be processed under the authority of a different user.

For LDAP clients, the PingDirectory server supports both simple authentication and several SASL mechanisms. For HTTP clients, the server supports basic authentication and OAuth 2.0.

This section covers the set of authentication mechanisms that the PingDirectory server supports. It also provides information about its extensive support for password policy functionality, some of which also applies to non-password-based authentication.

---

---
title: Authentication-related controls
description: The PingDirectory server provides support for several additional controls that can be used when authenticating or interacting with password policy-related operations.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_authn_ctrls
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_authn_ctrls.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sec_authn_ctrls_ext_ops.adoc", "pd_sec_authr_id_request_ctrl.adoc", "pd_sec_get_authr_entry_ctrl.adoc", "pd_sec_acct_usable_control.adoc", "pd_sec_pw_policy_control.adoc", "pd_sec_pw_expire_controls.adoc", "pd_sec_get_pw_policy_state.adoc", "pd_sec_pw_validation_details_ctrl.adoc", "pd_sec_generate_pw_request_ctrl.adoc"]
section_ids:
  the-authorization-identity-request-control: The authorization identity request control
  the-get-authorization-entry-request-control: The get authorization entry request control
  the-account-usable-control: The account usable control
  the-password-policy-control: The password policy control
  the-password-expiring-and-password-expired-controls: The password expiring and password expired controls
  the-get-password-policy-state-issues-control: The get password policy state issues control
  the-password-validation-details-control: The password validation details control
  the-generate-password-request-control: The generate password request control
---

# Authentication-related controls

The PingDirectory server provides support for several additional controls that can be used when authenticating or interacting with password policy-related operations.

## The authorization identity request control

The authorization identity request control is described in [RFC 3829](https://www.ietf.org/rfc/rfc3829.txt) and can be included in a bind request to indicate that the server should include the resulting authorization identity in the successful bind response.

In the PingDirectory server, this authorization identity is always in the form of a distinguished name (DN), prefixed by `dn:` (for example, `dn:uid=jdoe`,`ou=People`,`dc=example`,`dc=com`).

This control is useful to determine the DN of the authenticated user entry, especially when the bind request does not identify the user by a DN, such as if the client was identified by a username, a Kerberos *(tooltip: \<div class="paragraph">
\<p>A network authentication protocol to provide strong authentication for client/server applications using symmetric key cryptography and a trusted authentication service (Key Distribution Center). The KDC authenticates the client and issues tickets allowing access to the server. Kerberos is the default authentication technology used by Microsoft.\</p>
\</div>)* principal, a client certificate, or an OAuth access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)*.

## The get authorization entry request control

While the authorization identity request control can be helpful, it only provides the distinguished name (DN) of the authenticated user and the specification does not even require that.

The PingDirectory server offers a more useful alternative in the form of the proprietary [get authorization entry request control](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/controls/GetAuthorizationEntryRequestControl.html).

This control can also be included in a bind request, and if the bind is successful, then the server can return a corresponding response control with the DN and a requested set of attributes from the authenticated user's entry. If the bind request also used an alternate authorization identity, then the response control can also include information about that user.

## The account usable control

Include the [account usable request control](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/controls/AccountUsableRequestControl.html) in a search request to indicate that matching entries should include a corresponding response control with a minimal set of information about whether the server considers the associated account to be usable.

This includes:

* Whether the account is usable

* The length of time until the user's password expires

* Whether the account is inactive

* Whether the user must change their password

* Whether the password is expired

* The number of remaining grace logins

* The length of time until the account is unlocked

This control is maintained for compatibility with a legacy system. While it is still useful, it is not updated to support new features.

## The password policy control

PingDirectory server supports the password policy request control, as described in [draft-behera-ldap-password-policy-10](https://docs.ldap.com/specs/draft-behera-ldap-password-policy-10.txt).

This control can be included in add, bind, compare, modify, and password modify extended requests to obtain information about the associated user's password policy state. This includes:

* The length of time until the user's password expires

* The number of remaining grace logins

* Whether the password is expired

* Whether the account is locked

* Whether the user must change their password

* Whether an update attempt failed because the user is not allowed to change their password

* Whether an update attempt failed because the user is required to provide their current password

* Whether an operation failed because the password is considered too weak

* Whether the proposed password is too short

* Whether the proposed password already exists in the user's password history

* Whether a user cannot change their password because there has not been enough time since the previous password change

Because this control is based on a public specification, its format is fixed and it is not updated to support additional features.

## The password expiring and password expired controls

PingDirectory server supports the password expiring and password expired controls, as described in [draft-vchu-ldap-pwd-policy-00](https://docs.ldap.com/specs/draft-vchu-ldap-pwd-policy-00.txt).

The password expiring control can be included in the response to a successful bind attempt to indicate that the user's password is about to expire. Its value indicates the length of time until the password actually expires.

The password expired control can be included in the response to a successful or failed bind attempt to indicate that the user's password has expired and must be changed. If the bind operation was successful, then it means that the user must change their password before they are allowed to request any other operations. If the bind operation failed, then it means that the password must be reset before the user can access their account.

## The get password policy state issues control

By default, PingDirectory server returns a minimal amount of information in the response to a failed bind attempt. This is intentional because revealing too much can give an attacker useful information that could allow them to improve their tactics.

Yet, it's useful in some circumstances to provide an application with a way to obtain information about the reason for a failed authentication attempt. As such, PingDirectory server offers a [get password policy state issues request control](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/controls/GetPasswordPolicyStateIssuesRequestControl.html) that can be included in a bind request to indicate that the server should include a control in the bind response with information about any error, warning, or notice conditions in the user's password policy state that might currently or soon interfere with their ability to authenticate. If the bind attempt fails, then it might also include specific information about the reason for that failure.

To prevent this control from being misused, PingDirectory server only allows it to be requested under a limited set of circumstances:

* The bind request must be issued on a connection that is currently authenticated as a user with the `permit-get-password-policy-state-issues` privilege.

* The requester must have access control permission to use the get password policy state issues request control.

The bind request must also include the [retain identity request control](pd_sec_retain_id_request_ctrl.html) in the bind request.

## The password validation details control

PingDirectory server provides support for a [password validation details request control](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/controls/PasswordValidationDetailsRequestControl.html) that can be included in an add request, modify request, or password modify extended request.

It indicates that the server should return a corresponding response control with a list of each of the requirements that the password must satisfy and an indication as to whether the proposed password satisfied.

## The generate password request control

You can include the proprietary [generate password request control](https://docs.ldap.com/ldap-sdk/docs/javadoc/index.html?com/unboundid/ldap/sdk/unboundidds/controls/GeneratePasswordRequestControl.html) in an add request to indicate that the server should automatically generate a password for the user.

The add response includes a corresponding response control that contains the generated password, along with an indication as to whether the user is required to choose a new password and how long the generated password is valid.

The password is generated using the password generator defined in the password policy that governs the new entry. Although the server might attempt to re-generate the password multiple times if previous attempts do not satisfy the configured set of password validators for the user, it might end up setting a password that does not pass validation. We recommend configuring the password generator to ensure that it is capable of generating passwords of acceptable strength.