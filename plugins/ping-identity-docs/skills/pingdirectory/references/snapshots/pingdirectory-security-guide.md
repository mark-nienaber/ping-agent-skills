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
title: Defining resource limits in client connection policies
description: Use client connection policies to impose hard upper bounds on the values of some resource limit properties.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_define_resource_limits_policies
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_define_resource_limits_policies.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  tuning-rate-limits: Tuning rate limits
---

# Defining resource limits in client connection policies

Use client connection policies to impose hard upper bounds on the values of some resource limit properties.

If the client connection policy is configured with a resource limit that's lower than the limit that would otherwise be imposed for the associated client, then the client connection policy's lower limit is enforced (even for root accounts and other types of administrative accounts). However, the client connection policy never grants a client a higher limit than it would otherwise have.

The client connection policy properties that are used to define resource limits include the following.

| Property                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `maximum-concurrent-connections`               | The maximum number of client connections that can be associated with the client connection policy at any one time. If the maximum number of connections are already associated with the policy, any attempt to assign another connection to the policy causes that connection to be terminated. A value of zero (which is the default) indicates that no limit is enforced.                                                                                                                                                                                                                                                                                          |
| `maximum-connection-duration`                  | The maximum length of time that connections associated with the policy can be established, regardless of how active those connections are. Any connection that's established for longer than this period of time will be terminated. A value of zero seconds (which is the default) indicates that no maximum connection duration is enforced.                                                                                                                                                                                                                                                                                                                       |
| `maximum-idle-connection-duration`             | The maximum length of time that connections associated with the policy are allowed to remain idle (without issuing any new requests). Any client connection that's idle for longer than this period of time is terminated. A value of zero (which is the default) indicates that the policy doesn't impose a maximum idle connection duration for client connections, and they're subject to whatever limit is in place through the global configuration or operational attributes in the authenticated user's entry.                                                                                                                                                |
| `maximum-operation-count-per-connection`       | The maximum number of requests that connections associated with the policy are allowed to request over the life of that connection. After a connection has already requested the maximum number of operations, if it attempts to request any other operations, then that connection is terminated. A value of zero (which is the default) indicates that no maximum operation count is enforced.                                                                                                                                                                                                                                                                     |
| `maximum-concurrent-operations-per-connection` | The maximum number of operations that a client associated with the policy can request at any one time. After the maximum number of concurrent operations are already active for a connection, then any new requests can optionally block for a period of time (specified by the `maximum-concurrent-operation-wait-time-before-rejecting` property) to see if any of the outstanding operations complete. At that point, the request can be rejected or the connection can be terminated based on the value of the `maximum-concurrent-operations-per-connection-exceeded-behavior` property. By default, no maximum concurrent operation limit is imposed.          |
| `maximum-connection-operation-rate`            | The maximum rate at which a client can issue requests. If provided, then the value should be provided as a count followed by a slash and a time duration (for example, 100/s indicates a maximum rate of one hundred requests per second, while 10K/6h indicates a maximum rate of 10,000 requests over a six-hour period). If any connection exceeds this rate, subsequent requests within that time period can be rejected or the connection can be terminated, as controlled by the `connection-operation-rate-exceeded-behavior` property. By default, no maximum connection operation rate is enforced.Learn more in [Tuning rate limits](#tuning-rate-limits). |
| `maximum-policy-operation-rate`                | The maximum rate at which all clients associated with the client connection policy can issue requests. If provided, then the value should be provided as a count followed by a slash and a time duration. If the maximum policy operation rate is exceeded, then subsequent requests within that time period can be rejected or the connection can be terminated, as controlled by the `policy-operation-rate-exceeded-behavior` property. By default, no maximum connection operation rate is enforced.Learn more in [Tuning rate limits](#tuning-rate-limits).                                                                                                     |
| `maximum-search-size-limit`                    | The maximum number of entries that can be returned in response to any single search operation for clients associated with the client connection policy. A value of zero (which is the default) indicates that the policy doesn't impose a maximum size limit for client connections, and they're subject to whatever limit is in place through the global configuration or operational attributes in the authenticated user's entry.                                                                                                                                                                                                                                 |
| `maximum-search-time-limit`                    | The maximum length of time that the server can spend processing any single search operation for clients associated with the client connection policy. A value of zero seconds (which is the default) indicates that the policy doesn't impose a maximum time limit for client connections, and they're subject to whatever limit is in place through the global configuration or operational attributes in the authenticated user's entry.                                                                                                                                                                                                                           |
| `maximum-search-lookthrough-limit`             | The maximum number of entries that the server can examine when processing any single search operation for clients associated with the client connection policy. A value of zero (which is the default) indicates that the policy doesn't impose a maximum lookthrough limit for client connections, and they're subject to whatever limit is in place through the global configuration or operational attributes in the authenticated user's entry.                                                                                                                                                                                                                  |
| `maximum-ldap-join-size-limit`                 | The maximum LDAP join size limit that's enforced for clients associated with the client connection policy. A value of zero (which is the default) indicates that the policy doesn't impose a maximum join size limit for client connections, and they're subject to whatever limit is in place through the global configuration or operational attributes in the authenticated user's entry.                                                                                                                                                                                                                                                                         |
| `maximum-sort-size-limit-without-vlv-index`    | The maximum number of entries that the server attempts to sort without the benefit of a VLV index. If the client issues a search request that includes the server-side sort control and matches more than this number of entries, then the server either returns the results in unsorted form (if the sort request control isn't marked critical), or it rejects the search (if the control is critical). A value of zero (which is the default) indicates that no limit should be enforced.                                                                                                                                                                         |

## Tuning rate limits

To help you tune the server's rate-limiting operations, and to identify unusual client activity, you can allow operations to exceed the configured per-connection and per-policy operation rates by using log mode. The server adds information about the client connections that exceed those rates to the error log.

To enable log mode for the `connection-operation-rate-exceeded-behavior` or `policy-operation-rate-exceeded-behavior` properties, supply the `log-allow` value.

You can use log mode without impacting application traffic, which makes it suitable for tuning production environments. For example, you can:

* Determine your traffic patterns, and then use that data to tune the thresholds for rejecting operations.

* Identify outlier client applications that need to be investigated.

Learn more about tuning rate limits in the configuration documentation included with the server.

---

---
title: Defining resource limits in operational attributes
description: Although the global configuration defines default values for several resource limits, it's possible to override those default values on a per-user basis by adding an appropriate set of operational attributes to the user's entry.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_define_resource_limits_op_attrs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_define_resource_limits_op_attrs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Defining resource limits in operational attributes

Although the global configuration defines default values for several resource limits, it's possible to override those default values on a per-user basis by adding an appropriate set of operational attributes to the user's entry.

Resource limits set through operational attributes can grant a user a higher limit than is available by default in the global configuration or impose a lower limit than would otherwise be permitted by default.

These operational attributes include:

| Attribute                      | Description                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ds-rlim-size-limit`           | The maximum number of entries that the user is allowed to retrieve in any single search operation. A value of zero indicates that no size limit is enforced for the user. If this attribute is present in a user's entry, then it overrides the default `size-limit` value from the global configuration.                                                                              |
| `ds-rlim-time-limit`           | The maximum length of time in seconds that the server is allowed to spend processing any single search operation for the user. A value of zero indicates that no time limit is enforced for the user. If this attribute is present in a user's entry, then it overrides the default `time-limit` value from the global configuration.                                                  |
| `ds-rlim-lookthrough-limit`    | The maximum number of entries that the server is allowed to examine while processing any single search operation for the user. A value of zero indicates that no lookthrough limit is enforced for the user. If this attribute is present in a user's entry, then it overrides the default `lookthrough-limit` value from the global configuration.                                    |
| `ds-rlim-idle-time-limit`      | The maximum length of time in seconds that the user is allowed to have an idle connection (one in which no operations in progress) established. A value of zero indicates that no idle time limit is enforced for the user. If this attribute is present in a user's entry, then it overrides the default idle-time-limit value from the global configuration.                         |
| `ds-rlim-ldap-join-size-limit` | The maximum number of entries that are joined with any single search result entry when processing a search request that includes the LDAP join request control. A value of zero indicates that no LDAP join size limit is enforced for the user. If this attribute is present in the user's entry, then it overrides the default `ldap-join-size-limit` from the global configuration. |

Each of these attributes can be explicitly set in the entries for users who should have a value different from the corresponding property in the global configuration. You can also use virtual attributes to assign values dynamically for these attributes using criteria like the location or content of the user's entry, the groups in which that user is a member, or the client connection policy to which they're assigned.

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After changing the resource limits for an operational attribute, you need to reset any existing client connections for the changes to take effect. |

---

---
title: Defining resource limits in search requests
description: Each search request allows the client to specify the size limit and time limit that should be used for that operation.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_define_limits_search_requests
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_define_limits_search_requests.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Defining resource limits in search requests

Each search request allows the client to specify the size limit and time limit that should be used for that operation.

If the client requests a size limit of zero, then that indicates that the client does not want to impose any limit and the search request is processed using whatever size limit imposes for that client. If the client requests a nonzero size limit and that requested size limit is lower than what the server would otherwise impose, then the client-requested size limit is used. If the client requests a size limit that is higher than what the server would otherwise impose, then the server-imposed limit is used.

The same logic applies to the requested time limit. That is, the time limit from the search request is used if it is lower than what the server would have otherwise imposed. Otherwise, the server's limit is used.

---

---
title: Defining resource limits in the global configuration
description: Use the following global configuration properties to enforce resource limits and provide protection against denial-of-service attacks.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_define_resource_limits_global_config
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_define_resource_limits_global_config.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Defining resource limits in the global configuration

Use the following global configuration properties to enforce resource limits and provide protection against denial-of-service attacks.

| Property                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `size-limit`                                    | The default maximum number of entries that a client can retrieve in any single search operation. If the client attempts to process a search that matches more than 1000 entries, then the operation fails with a `sizeLimitExceeded` result (after returning all matching entries identified before the size limit was reached). This is set to 1000 by default. A value of zero indicates that no limit should be enforced.                                                                                                                                                                                                                                                |
| `time-limit`                                    | The default maximum length of time in seconds that the server is allowed to spend processing any single search operation. If the client requests a search operation that takes longer than this length of time to complete, then the operation fails with a `timeLimitExceeded` result (after returning any matching entries identified before the time limit was reached). This is set to one minute by default. A value of zero seconds indicates that no limit should be enforced.                                                                                                                                                                                       |
| `idle-time-limit`                               | The default maximum length of time that a client connection should be allowed to remain established after the server has completed processing on the most recent request issued on that connection. If the client remains idle for longer than this duration, the connection is terminated. A value of zero seconds (which is the default value) indicates that no idle time limit should be enforced.                                                                                                                                                                                                                                                                      |
| `lookthrough-limit`                             | The default maximum number of entries that the server can examine in the course of processing a search request, regardless of whether those entries actually match the search criteria. This is primarily useful for limiting resource consumption when processing unindexed searches, and if the client attempts to process a search operation in which the server needs to examine more than this number of entries, then the operation fails with an `adminLimitExceeded` result (after returning any matching entries identified before the lookthrough limit was reached). This is set to 5000 by default. A value of zero indicates that no limit should be enforced. |
| `ldap-join-size-limit`                          | The default maximum number of entries that can be joined with each search result entry when processing a search using the LDAP join request control. If an entry is joined with more than this number of entries, then the join result control for that entry has a sizeLimitExceeded result code (and might or might not include any matching entries). This is set to 10,000 by default. A value of zero indicates that no limit should be enforced.                                                                                                                                                                                                                      |
| `maximum-concurrent-connections`                | The maximum number of connections that can be established to the server at any one time. After this limit has been reached, then any subsequent connection attempts are rejected until an existing client connection has been closed. A value of zero (which is the default) indicates that no limit is imposed by the server, although the operating system can impose a limit (for example, based on the number of available file descriptors).                                                                                                                                                                                                                           |
| `maximum-concurrent-connections-per-ip-address` | The maximum number of connections that can be established to the server at any one time from the same client IP address. After this limit has been reached, then any subsequent attempts to establish a connection from that client are rejected until an existing connection from that client has been closed. A value of zero (which is the default) indicates that no limit is enforced.                                                                                                                                                                                                                                                                                 |
| `maximum-concurrent-connections-per-bind-dn`    | The maximum number of connections that can be established to the server at any one time while authenticated as the same user. After this limit has been reached, then any subsequent attempts to bind as that user cause the connection to be terminated until an existing connection authenticated as that user is closed or binds as a different user. A value of zero (which is the default) indicates that no limit is enforced.                                                                                                                                                                                                                                        |
| `maximum-concurrent-unindexed-searches`         | The maximum number of unindexed searches that can be in progress within the server at any one time. If an unindexed search is requested while the maximum number of searches are already in progress, then that search is rejected with an `unwillingToPerform` result. This is set to ten by default. A value of zero indicates that no limit is enforced.                                                                                                                                                                                                                                                                                                                 |

You can also configure the server to suppress duplicate error log messages and administrative alerts. This can help prevent flooding the log with repeated messages if the same condition keeps occurring. The global configuration properties used to control this are:

| Property                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `duplicate-error-log-limit` and `duplicate-error-log-time-limit` | The maximum number of error log messages of the same type that can be written within a given length of time. If that error log message rate is exceeded, then any additional error log messages of that type within that time period are suppressed, and the server writes a message at the end of that time indicating the number of messages that were suppressed. By default, the server starts suppressing error log messages after 200 messages of the same type in a five-minute period. |
| `duplicate-alert-limit` and `duplicate-alert-time-limit`         | The maximum number of administrative alerts of the same type that can be generated within a given length of time. If that alert rate is exceeded, then any additional alerts of that type within that time period are suppressed, and the server generates an additional alert at the end of that time period indicating the number of alerts that were suppressed. By default, the server starts suppressing alerts after 10 alerts of the same type are generated in a ten-minute period.    |

---

---
title: Delay bind responses after too many authentication failures
description: You should have some mechanism in place to protect against online password guessing attacks.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_delay_bind_responses_authn_failures
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_delay_bind_responses_authn_failures.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Delay bind responses after too many authentication failures

You should have some mechanism in place to protect against online password guessing attacks.

Traditionally, this is done by locking accounts (at least temporarily) after too many failed authentication attempts. However, this is undesirable because an attacker could use it to intentionally lock those accounts and deny access to its legitimate owner. While you might be willing to accept this possibility for regular user accounts, you don't want to risk the chance that administrative accounts can become locked and unusable.

A compelling alternative to actually locking user accounts is to delay bind responses after too many failed attempts. This can help limit the rate at which attackers might make guesses without significantly impeding the legitimate account owner. To do this, use the `failure-lockout-action` property in the password policy configuration to select a policy that delays bind responses rather than locking the account.

If you do need to actually lock accounts to prevent them from being used after too many failed attempts, then you should choose a high enough `lockout-failure-count` value to ensure that accounts are not inadvertently locked by legitimate users who know their passwords but just mistype it several times in a row.

---

---
title: Delaying responses to failed bind attempts
description: Configure PingDirectory server to delay the response to bind requests as a way of rate-limiting online password guessing attacks.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectory_security_guide:pd_sec_delay_resp_failed_bind
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectory_security_guide/pd_sec_delay_resp_failed_bind.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Delaying responses to failed bind attempts

Configure PingDirectory server to delay the response to bind requests as a way of rate-limiting online password guessing attacks.

This can be done in two different ways:

* The LDAP connection handler offers a `failed-bind-response-delay` configuration property. If this is set to a nonzero duration, then the server automatically delays the response to any failed bind attempt by the specified length of time. The server does not delay the response to successful bind attempts.

* The password policy offers a `failure-lockout-action` configuration property that can be used to indicate what action should be taken after too many failed authentication attempts, and one possible action is delaying the bind response. For more information, see This will be covered in more detail in the [Failure lockout](pd_sec_failure_lockout.html) section in the discussion on password policies.

The option to delay bind responses in the connection handler was available before the corresponding option in the password policy. However, the latter option is the recommended approach because it also delays the response to the first successful bind following several failed attempts, which makes it more difficult for an attacker to use the delay to identify a failed attempt and to abort early without waiting for the full failure duration. You can also configure the password policy approach to work for non-LDAP clients.