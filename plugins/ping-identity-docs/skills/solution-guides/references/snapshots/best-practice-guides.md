---
title: Best Practice Guides
description: "Best Practices: Session Management"
component: solution-guides
page_id: solution-guides:best_practice_guides:htg_best_practice_guides
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/htg_best_practice_guides.html
revdate: April 8, 2025
---

# Best Practice Guides

| Use case                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Best Practices: Session Management](bp_session_mgmt.html)                                            | Session management is the process of managing user sessions in a web application. A session is a series of interactions between users and a web application that take place over a period of time.                                                                                                                                                                                                                      |
| [Best Practices: Elevated Rights for PingDirectory](bp_pd_elevated_rights.html)                       | This document provides an overview of Ping Identity's recommendations for management of elevated rights in PingDirectory.                                                                                                                                                                                                                                                                                               |
| [Best Practices: Performance Testing PingDirectory](bp_pd_performance_testing.html)                   | PingDirectory ships with several tools that you can use for performance testing.                                                                                                                                                                                                                                                                                                                                        |
| [Best Practices: PingDirectory Operational Support](bp_pd_operational_support.html)                   | This document contains recommendations and best practices for the PingDirectory application onboarding process. Additionally, this document provides recommendations on supporting processes that could be used in conjunction with application integration.                                                                                                                                                            |
| [Best Practices: PingFederate SAML Signing Certificates](htg_best_practice_pf_saml_signing_cert.html) | The following reference guide details the best practices for managing PingFederate Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">&#xA;\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>&#xA;\</div>)* signing certificate settings, depending on your partners' preferences. |
| [Best Practices: Performance Testing for PingFederate](bp_pf_performance_testing.html)                | This document provides an overview as well as general guidelines related to performance testing methodology for testing a PingFederate server prior to that system entering a customer production environment.                                                                                                                                                                                                          |
| [Best Practices: Journey to Passwordless](bp_journey_to_passwordless.html)                            | Learn about how passwordless authentication reduces friction for users.                                                                                                                                                                                                                                                                                                                                                 |

---

---
title: "Best Practices: Elevated Rights for PingDirectory"
description: This document provides an overview of Ping Identity's recommendations for management of elevated rights in PingDirectory.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_pd_elevated_rights
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_pd_elevated_rights.html
revdate: April 14, 2025
page_aliases: ["best_practice_guides:bp_pd_elevated_rights_capabilities.adoc", "best_practice_guides:bp_pd_elevated_rights_aci_best_practices.adoc", "best_practice_guides:bp_pd_elevated_rights_privileges_best_practices.adoc", "best_practice_guides:bp_pd_elevated_rights_client_connection_policy_best_practices.adoc", "best_practice_guides:bp_pd_elevated_rights_examples.adoc"]
section_ids:
  capabilities: Capabilities
  privileges: Privileges
  access-control-instructions-aci: Access control instructions (ACI)
  client-connection-policy: Client connection policy
  aci-best-practices: ACI best practices
  group-based: Group based
  use-implicit-deny-not-explicit: Use implicit deny, not explicit
  use-names-with-identifiers-in-acis-and-document: Use names with identifiers in ACIs and document
  privileges-best-practices: Privileges best practices
  client-connection-policy-best-practices: Client connection policy best practices
  not-a-replacement-for-acis: Not a replacement for ACIs
  define-unauthenticatedinsecure-policy: Define unauthenticated/insecure policy
  set-restrictive-client-connection-criteria: Set restrictive client connection criteria
  examples: Examples
---

# Best Practices: Elevated Rights for PingDirectory

This document provides an overview of Ping Identity's recommendations for management of elevated rights in PingDirectory.

PingDirectory is designed as a security product and provides a number of mechanisms that can be used to provide fine-grained control over the elevated rights that can be assigned to an administrator or service account.

## Capabilities

### Privileges

PingDirectory has a number of defined privileges that are used for fine-grained control of privilege.

The capabilities of the Directory Manager account that is created by default during a PingDirectory install is granted by assignment of privileges. This default Directory Manager account itself does not possess any special privileges or capabilities beyond those assigned by privileges. Any account in the directory that is assigned the same privileges as that default Directory Manager will have exactly the same level of access as that Directory Manager account.

The privileges assigned to the Directory Manager account can be removed (or the account itself can be deleted) without impacting the functionality of the directory.

| Privilege name                               | Root privilege | Privilege description                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `audit-data-security`                        | Yes            | Provides the ability to audit the security of data in any backend. The user still needs access control permission to perform the requested operation                                                                                                                                                                         |
| `backend-backup`                             | Yes            | Provides the ability to perform a backup of one or more backends with the server online via the tasks interface. The user still needs access control permission to perform the requested operation.                                                                                                                          |
| `backend-restore`                            | Yes            | Provides the ability to perform a restore of a backend with the server online through the tasks interface. The user still needs access control permission to perform the requested operation.                                                                                                                                |
| `bypass-acl`                                 | Yes            | Provides the ability to bypass all access control evaluation for any type of operation.&#xA;&#xA;Users with the bypass-acl privilege can still be subject to other restrictions, such other privileges that might be required to process a particular operation.                                                             |
| `bypass-pw-policy`                           | No             | Provides the ability to exempt an administrator from certain types of password policy evaluation when performing an operation against another user.                                                                                                                                                                          |
| `bypass-read-acl`                            | No             | Provides the ability to bypass all access control evaluation, but only for bind, compare, and search operations. Normal access control evaluation is still performed for add, delete, extended, modify, and modify DN operations.                                                                                            |
| `collect-support-data`                       | Yes            | Allows the requester to invoke the collect-support-data tool using an administrative task or extended operation.                                                                                                                                                                                                             |
| `config-read`                                | Yes            | Provides the ability to perform search and compare operations in the server configuration. These operations are still subject to access control restrictions.                                                                                                                                                                |
| `config-write`                               | Yes            | Provides the ability to perform add, delete, and modify operations in the server configuration. These operations are still subject to access control restrictions.                                                                                                                                                           |
| `disconnect-client`                          | Yes            | Provides the ability to terminate an arbitrary client connection. The user still needs access control permission to perform the requested operation.                                                                                                                                                                         |
| `exec-task`                                  | No             | Allows the requester to schedule an exec task.                                                                                                                                                                                                                                                                               |
| `file-servlet-access`                        | Yes            | Indicates that the requester may be permitted access to the content exposed by file servlet instances that require this privilege.                                                                                                                                                                                           |
| `jmx-notify`                                 | No             | Provides the ability to subscribe to receive JMX notifications.                                                                                                                                                                                                                                                              |
| `jmx-read`                                   | No             | Provides the ability to perform read operations using JMX.                                                                                                                                                                                                                                                                   |
| `jmx-write`                                  | No             | Provides the ability to perform write operations using JMX.                                                                                                                                                                                                                                                                  |
| `ldif-export`                                | Yes            | Provides the ability to perform LDIF export operations with the server online through the tasks interface. The user still needs access control permission to perform the requested operation.                                                                                                                                |
| `ldif-import`                                | Yes            | Provides the ability to perform LDIF import operations with the server online through the tasks interface. The user still needs access control permission to perform the requested operation.                                                                                                                                |
| `lockdown-mode`                              | Yes            | Provides the ability to cause the server to enter and leave lockdown mode or to access the server while it is in lockdown mode. The user still needs access control permission to perform the requested operation.                                                                                                           |
| `manage-topology`                            | Yes            | Provides the ability to manage a topology of server instances, including adding servers to and removing servers from a topology. The user still needs access control permission to perform the requested operation.                                                                                                          |
| `metrics-read`                               | Yes            | Provides the ability to search or retrieve data in the metrics backend. The user still needs access control permission to perform the requested operation.                                                                                                                                                                   |
| `modify-acl`                                 | Yes            | Provides the ability to modify access control rules. The user still needs access control permission to perform the requested operation.                                                                                                                                                                                      |
| `password-reset`                             | Yes            | Provides the ability to change another user's password. The user still needs access control permission to perform the requested operation.                                                                                                                                                                                   |
| `permit-externally-processed-authentication` | No             | Provides the ability for the requester to issue a bind request that uses the `UNBOUNDID-EXTERNALLY-PROCESSED-AUTHENTICATION` Simple Authentication and Security Layer (SASL) mechanism.                                                                                                                                      |
| `permit-forwarding-client-connection-policy` | No             | Provides the ability to request that an operation be processed using a specified client connection policy.                                                                                                                                                                                                                   |
| `permit-get-password-policy-state-issues`    | Yes            | Provides the ability for the requester to issue a bind request that includes the get password policy state issues request control. The bind request must also include the retain identity request control.                                                                                                                   |
| `privilege-change`                           | Yes            | Provides the ability to alter the set of privileges assigned to an individual user or to change the set of privileges that can be automatically assigned to root users.                                                                                                                                                      |
| `proxied-auth`                               | No             | Provides the ability to request that an operation be processed using an alternate authorization identity, such as using the proxied authorization or intermediate client request control or using a SASL authorization identity.                                                                                             |
| `server-restart`                             | Yes            | Provides the ability to request a server restart using the tasks interface. The user still needs access control permission to perform the requested operation.                                                                                                                                                               |
| `server-shutdown`                            | Yes            | Provides the ability to request a server shutdown using the tasks interface. The user still needs access control permission to perform the requested operation.                                                                                                                                                              |
| `soft-delete-read`                           | Yes            | Provides the ability to retrieve, compare, modify, delete, or undelete soft-deleted entries. The user still needs access control permission to perform the requested operation.                                                                                                                                              |
| `stream-values`                              | Yes            | Provides the ability to use the stream directory values extended operation to obtain a list of all entry DNs or unique attribute values or to use the stream proxy values extended operation to obtain information from the global index. The user still needs access control permission to perform the requested operation. |
| `third-party-task`                           | Yes            | Provides the ability to invoke a third-party task in the server. The user still needs access control permission to perform the requested operation.                                                                                                                                                                          |
| `unindexed-search`                           | Yes            | Provides the ability to perform an expensive unindexed search in a local DB backend. The user still needs access control permission to perform the requested operation.                                                                                                                                                      |
| `unindexed-search-with-control`              | No             | Provides the ability to perform an unindexed search if the request also includes the permit unindexed search request control.                                                                                                                                                                                                |
| `update-schema`                              | Yes            | Provides the ability to alter the server schema. The user still needs access control permission to perform the requested operation.                                                                                                                                                                                          |
| `use-admin-session`                          | Yes            | Provides the ability to use an administrative session to request that operations be processed in a dedicated thread pool.                                                                                                                                                                                                    |

Privileges are granted to an account by adding the desired privilege to the accounts `ds-privilege-name` attribute.

This attribute can be explicitly populated, populated with a virtual attribute, or a combination of the two.

Privileges allow us to grant accounts the ability to perform basic administrative tasks, such as `server-shutdown`, without needing to grant more powerful privileges, such as `bypass-aci`.

### Access control instructions (ACI)

ACIs are used to define the level of access an account can have to entries and attributes in the directory. By default, PingDirectory is configured with an implicit deny, so read/write access to entries must be explicitly granted.

### Client connection policy

A number of different client connection policies may be defined on a server. A client connection policy can, among other things, determine:

* Which branches of the directory are accessible

* Allow operation types (for example, search, add, delete, and modify)

* Allowed filter types

* Search size and time restrictions

* Attributes to be excluded from search results

* Attributes that cannot be included in search filters

* Attributes that cannot be modified (even if ACIs would normally allow)

Which client connection policy applies to an authenticated account can be determined by:

* Included/excluded IP address or IP range

* Connection type (HTTPs, LDAPs, LDAP)

* Location of authenticated account in the directory

* Group membership of authenticated account

* Attribute value contained in the authenticated account

* Authenticated account privileges

A common use of client connection policies is creating a connection policy for insecure LDAP communications where only accounts in specific groups are allowed to connect insecurely and can only see a limited number of entries and attributes.

## ACI best practices

Best practices for the definition of ACIs in a PingDirectory environment include:

* Default to deny

  * Don't define any global permissive ACIs for all users.

  * Ensure that unless explicitly granted, all security decisions are a deny.

* Group-based ACI

  * All ACIs should be assigned through group membership.

  * Do not assign ACIs to specific user accounts.

* Implement ACI identifiers and document thoroughly

### Group based

Ping Identity highly recommends using a set of standardized, group-based ACIs to grant permissions to the directory. Managing the application of ACIs through group membership provides a number of benefits:

* Easier to understand

  * You only need to look at group membership to determine what a user has access to. You don't need to decode ACIs to see which ACIs apply to a user.

* Simplified auditing (just look at group membership)

* Greatly simplifies the granting of rights

* Reduces the total number of ACIs

  * ACIs always get evaluated, so keeping the number of defined ACIs relatively small can help performance.

* Reduce risk and ACI proliferation

  * Application-specific or user-specific ACIs can be difficult to maintain. It can be difficult to know if an ACI is safe to remove or if it grants too many rights to an application. Group-based ACIs transform this issue into a group management issue that administrators are much better equipped to deal with.

  * Creating generic, reusable ACIs greatly reduces or eliminates the need to create custom, application-specific ACIs for each new application or unique use case.

**Example**

For a specific user organizational unit (OU) in the directory, you could create a set of group-based ACIs that grant the following:

* Read/Search access to non-sensitive attributes

* Read/Search access to sensitive attributes, such as SSN or date of birth.

* Write access to non-sensitive attributes

* Write access to sensitive attributes

* Create permission for specific entry types (create for `inetOrgPerson` or `groupOfUniqueNames`)

* Write access to specific attribute (for example, `uniqueMember` grants the ability to manage group membership separately from the ability to create/delete groups)

* Import/Export rights (to allow for `moddn` operations)

* Delete permission for specific entry types

This might initially look like a lot of ACIs to create for each OU in your directory. However, these ACIs greatly reduce or eliminate the need for the creation of future ACIs, as 95% of your conceivable use cases for granting of permissions can now be accomplished through group membership.

PingDirectory allows for the use of nested groups, so it is possible to create a Level1 Help Desk group and nest it into multiple ACI groups across multiple OUs to simplify administration.

### Use implicit deny, not explicit

Using the above methodology means an entry will by default have no access to any entries in the directory. Any access granted to an account will be an accumulation of explicitly granted permissions. Starting from a position of no privilege and only having permissive ACIs greatly simplifies the evaluation of privileges when troubleshooting or verifying that an account has the correct rights.

One of the biggest issues with a deny ACI is that the deny is being implemented as a security control to remove access that would otherwise be granted. This implies that the account in question would by default have access to data it should not unless action is explicitly taken to deny that access.

Having only permissive ACIs means that mistakes in granting rights to a user will usually result in a user not having enough access. Using a deny ACI opens us up to the possibility of a mistake granting a user rights they should not have.

If you don't grant a user enough privileges, the user will usually let you know. Detection of this type of mistake is usually easy (the user is motivated to let you know) and poses low security risk to the organization.

If you grant a user or account too many permissions, no one will likely notice. Even if a user or application owner notices, they might not consider this an issue and are unlikely to report it. Detection of this type of mistake is very difficult and can pose a high security risk to the organization.

### Use names with identifiers in ACIs and document

When an ACI has been in place for an extended period of time it might not be a simple process to determine why that ACI exists, what exactly it does, and if it's safe to modify or delete it. This presents a number of auditing and supportability concerns and can produce a directory whose security stance cannot be fully determined.

It is highly recommended when creating ACIs that each ACI contain a descriptive name with a unique identifier that can be cross-referenced with a version document containing:

* ACI Unique Identifier

* ACI High Level Description

* ACI Business Case

* Change order/request id used to implement the ACI

* Responsible party

* Parties to be informed if ACI needs to be deleted or changed

For example, we might have an ACI that looks like:

```
(target="ldap:///cn=changelog")(targetscope="subtree")(targetattr="*||+")(version
          3.0; acl "GL-SYNC-1: Allow Read access to changelog backend";allow(read,search,compare)
          groupdn="ldap:///cn=SyncReadGrp,ou=Groups,ou=Administrators,dc=example,dc=com";)
```

With a corresponding entry in the ACI document similar to the following.

**GL-SYNC-1**

|                     |                                                                                                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description         | Grants read access to cn=changelog for the PingDataSync service account so it can monitor for changes to user data                                                                              |
| Business case       | CRM Unit needs to monitor for new customer entries in the directory so they can retrieve application generated unique identifiers and associate those with customer entries in the CRM database |
| Change order        | Implemented 12/24/2020 under CR23423                                                                                                                                                            |
| Request ID          | Requested 6/15/2020 with REQ 1231254                                                                                                                                                            |
| Area owner          | US Customer Relations                                                                                                                                                                           |
| Responsible parties | Manager – Alice Smith (bob.smith\@company.com)BA – Bob Jones (bob.jones\@company.com)                                                                                                           |

## Privileges best practices

Privileges are assigned to an entry through the population of the `ds-privilege-name` attribute with a list of the privileges that entry should have.

Ongoing maintenance and auditing of privilege assignment can be challenging if privileges are assigned through direct population of the `ds-privilege-name` attribute. Ping Identity does not recommend direct population of this attribute except in special cases.

Ping Identity recommends the use of group-membership based virtual attributes to populate privileges.

For example, to assign the `pwd-reset` privilege a virtual attribute would be created similar to:

```shell
dsconfig create-virtual-attribute \
 --name ADM-Password-Reset-Priv --type constructed \
 --set enabled:true --set attribute-type:ds-privilege-name \
 --set enabled:true --set attribute-type:ds-privilege-name \
 --set group-dn:cn=ADM-PasswordReset,ou=groups,ou=admins,dc=example,dc=com \
 --set value-pattern:password-reset
```

Using this virtual attribute, an account can be granted the password reset privilege by adding the user to the `ADM-PasswordReset` group.

**Exception**

You might encounter a potential bug with applications that heavily use Proxy Auth privileges where security context changes multiple times over a single connection. This behavior is typically limited to applications such as PingFederate and Siteminder. An existing connection that's heavily used for Proxy Auth might forget what privileges it has unless they are explicitly assigned to the entry's `ds-privilege-name` attribute.

## Client connection policy best practices

Client connection policies can be used to control what a client can see or do at a very high level. You can use client connection policies to enforce a certain level of security that is not available through other mechanisms.

There are a number of common use cases for client connection policies:

* Allow exceptions to requirement for secure connections based on a service account's group membership

* Limit the subtrees viewable or accessible to a client

  * Useful when storing both employee and customer data on the same server to logically isolate the branches from each other for most applications

* Restrict access or disallow access to PingDirectory based on client IP address (for example, don't allow adds/mod/writes from the Internet even if the account has ACIs granting those permissions)

* Place restrictions on allowable search filters

* Enforce limits on poorly behaving applications or applications that are yet to be vetted by the directory administrators

* The calculation of expensive virtual attributes can be restricted so that they only occur over a specific connection policy

The client connection policy associated with a particular connection can change over time. The client connection policy will be determined:

* When the connection is initially established

* After any successful Bind operation

* After a StartTLS request is received

### Not a replacement for ACIs

Care should be taken not to rely too heavily on connection policies to enforce security that can be addressed at a lower level by ACIs or Privileges.

If you don't want a particular user to have access to `ou=Customers`, for example, you could create a connection policy that prevents that user from seeing `ou=Customers`. However, ACIs should also be created to ensure that the user does not have access to those entries if a client connection policy mistake is made.

|   |                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Creating new client connection policies can easily introduce issues in the client connection policy evaluation order and process a more permissive policy before the more restrictive policies. |

### Define unauthenticated/insecure policy

When clients connect to PingDirectory, the initial connection is almost always unauthenticated.

If you are deleting the default client connection policy (or modifying it), make sure that there is at least one client connection policy that allows for a connection to transition from an unauthenticated state to an authenticated state or to allow an unauthenticated connection to send a StartTLS control.

### Set restrictive client connection criteria

The evaluation order defined for a client connection policy will determine which client connection policy a client receives if it meets the criteria for more than one client connection policy. This has the potential to create unexpected scenarios if a valid client connection state is not considered or tested during the design of the client connection criteria and client connection policies.

Best practice is to implement mutually exclusive client connection criteria where possible to reduce or eliminate reliance on the evaluation order index when a connection's client connection policy is determined.

## Examples

The following is a sample list of group based ACIs that might be created for an OU that contains employee accounts:

```shell
dn: ou=people,ou=internal,dc=example,dc=com

aci: (target =
"ldap:///ou=people,ou=internal,dc=example,dc=com")(targetattr = "* || +") (version 3.0; acl "IP1 read internal people ou"; allow
(search,read,compare)
(groupdn="ldap:///cn=ADM-InternalPeopleRead,ou=groups,ou=admins,dc=example,dc=com");)

aci: (target =
"ldap:///ou=people,ou=internal,dc=example,dc=com")(targetattr != "userpassword || authpassword") (version 3.0; acl "IP2 write internal people"; allow (write) (groupdn="ldap:///cn=ADM-InternalPeopleUpdate,ou=groups,ou=admins,dc=example,dc=com");)

aci: (target = "ldap:///ou=people,ou=internal,dc=example,dc=com")(targetattr = "userpassword || authpassword") (version 3.0; acl "IP3 password update internal people"; allow (write)
(groupdn="ldap:///cn=ADM-InternalPeoplePwdReset,ou=groups,ou=admins,dc=example,dc=com");)

aci: (target = "ldap:///ou=people,ou=internal,dc=example,dc=com") (version 3.0; acl "IP4 add internal people"; allow (add)
(groupdn="ldap:///cn=ADM-InternalPeopleAdd,ou=groups,ou=admins,dc=example,dc=com");)

aci: (target = "ldap:///ou=people,ou=internal,dc=example,dc=com") (version 3.0; acl "IP5 delete internal people"; allow (delete)
(groupdn="ldap:///cn=ADM-InternalPeopleDel,ou=groups,ou=admins,dc=example,dc=com");)

aci: (target = "ldap:///ou=people,ou=internal,dc=example,dc=com") (version 3.0; acl "IP6 move branch internal people"; allow
(import,export)
(groupdn="ldap:///cn=ADM-InternalPeopleModDN,ou=groups,ou=admins,dc=example,dc=com");)
```

In this example, if we wanted to give the help desk the ability to search for user accounts, read user accounts, and reset passwords, we would place the help desk users into the following groups (either directly or, more likely, by creating a help desk group and nesting it into these groups):

* `ADM-InternalPeopleRead`

* `ADM-InternalPeoplePwdReset`

With descriptive group names, this makes the determination of a user's rights to the directory intuitively obvious.

One further item to note is that the ACI that grants write access to `userPassword` (IP3) will need to be used in conjunction with the `password-reset` privilege before the help desk user can reset an employee's password. In the Privileges best practices section, there is an example virtual attribute that is used to assign the `password-reset` privilege to users that are direct or indirect members of the group `ADM-PasswordReset`.

To enable help desk users to reset the passwords of employees, those help desk users would need to be added to `ADM-InternalPeoplePwdReset`, which grants write access to `userPassword`. Then you would need to nest the `ADM-InternalPeoplePwdReset` group into the `ADM-PasswordReset` group that is used by that virtual attribute, which will grant those help desk users the `password-reset` privilege.

---

---
title: "Best Practices: Journey to Passwordless"
description: Learn about how passwordless authentication reduces friction for users.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_journey_to_passwordless
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_journey_to_passwordless.html
revdate: October 13, 2022
---

# Best Practices: Journey to Passwordless

Learn about how passwordless authentication reduces friction for users.

Your enterprise is more than likely taking advantage of using multi-factor authentication (MFA). This enables step-up authentication by providing a second factor with authentication. The second factors have multiple methods an administrator can configure, which include but are not limited to:

* Authenticator applications

* Email

* SMS

* Voice

* One-time passcodes (OTPs)

* Hard tokens

* FIDO

When using PingID, you might have a similar experience using first and second factors together as shown in the following image.

![A diagram with a series of screen captures showing a sign-on page (first factor) to an Authentication window for an OTP (second factor).](_images/fuw1662484655539.png)

The goal is to reduce passwords and to evolve the experience into a frictionless experience, as seen in the following image showing the passwordless experience using Touch ID.

![A diagram with a pair of screen captures showing a sign-on page and options to sign on with an arrow pointing to a Touch ID prompt window for passwordless sign-on.](_images/fmy1662484802718.png)

The number of steps for a passwordless experience decreases compared to the MFA experience:

* Reduce footprint:

  * Single sign-on (SSO) and MFA

  * Authentication authority

  * Standards

  * Risk signals

* Reduce friction:

  * First factor FIDO

  * Continuous AuthN

  * Zero login

You can balance security and experience by managing risk.

* Passwordless has many different definitions, depending on who you ask.

* Passwordless boils down to either reducing passwords or eliminating them altogether.

* People agree that, when done right, passwordless offers a better experience and better security compared to traditional sign-on experiences.

---

---
title: "Best Practices: Performance Testing for PingFederate"
description: This document provides an overview as well as general guidelines related to performance testing methodology for testing a PingFederate server prior to that system entering a customer production environment.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_pf_performance_testing
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_pf_performance_testing.html
revdate: April 1, 2025
section_ids:
  audience: Audience
  why-do-performance-testing: Why do performance testing?
  lesson-1-load-generation: "Lesson 1: Load generation"
  lesson-2-results-validation: "Lesson 2: Results validation"
  lesson-3-warm-up-your-server: "Lesson 3: Warm up your server"
  lesson-4-things-to-keep-in-mind-when-monitoring-performance: "Lesson 4: Things to keep in mind when monitoring performance"
  lesson-5-did-the-test-return-expected-results: "Lesson 5: Did the test return expected results?"
  lesson-6-tools-of-the-trade: "Lesson 6: Tools of the trade"
  lesson-7-understand-and-tune-the-infrastructure: "Lesson 7: Understand and tune the infrastructure"
  summary: Summary
---

# Best Practices: Performance Testing for PingFederate

This document provides an overview as well as general guidelines related to performance testing methodology for testing a PingFederate server prior to that system entering a customer production environment.

Many PingFederate deployments are still rolled out into production without any performance and scalability testing. This document shows you how Ping Professional Services approaches performance testing and can assist in identifying and thinking through potential bottlenecks so that you can deploy your servers with confidence.

## Audience

This is intended as a starting point for anyone interested in learning or expanding their knowledge of PingFederate performance testing. Performance testing should always be undertaken with a consistent methodology and well-known tooling. This article will not make you a seasoned performance tester because that can take many years of experience. Instead, the basic skills explained here will give you some familiarity with the testing techniques and approaches Ping Identity takes when approaching such an important topic.

## Why do performance testing?

Low-performing PingFederate applications do not deliver their intended benefits to an enterprise. Slow authentication performance or minimal scalability result in a net loss of time and money. If PingFederate is not delivering in a highly performant manner, this reflects poorly on all of the architects and consultants that delivered the solution to the customer.

## Lesson 1: Load generation

Before you embark on your performance testing journey, you must ensure there is sufficient hardware for load/traffic generation.

A common misconception of performance testing efforts is that a load generator is a piece of software that can generate massive amounts of load on very little hardware. Always keep in mind that the load generator must have sufficient access to hardware in order to generate the load required in order to test an enterprise-scale system.

A customer could purchase a load generator such as Loadrunner and incorrectly assume that they can install it on a couple of modestly-sized PingFederate instance and expect it to generate thousands of concurrent users.

Remember, load generators are software, and they should be treated as such. All software is bound by resource use and design. Everything has performance limitations.

For anyone doing performance testing, size your client hardware like you would your target system. For testing PingFederate, the testing hardware should almost always overpower the PingFederate servers because PingFederate transactions are very fast. If your load testing system is not able to generate requests at a sufficiently high rate, you can mistakenly assume that you've hit the peak of PingFederate's capability, when in reality your load generator is not able to sufficiently stress PingFederate.

Make sure that if you or your customer is starting a performance and load testing endeavor, you are using adequate testing hardware.

Use a large system to test a small system. Use a 12-core load generator to performance test a quad-core PingFederate system. Make sure your load generator has at least two to three times the performance of the test system. You need power to test power. The faster the response times are for your load tests, the more powerful the hardware that you need to pump through those requests.

Ask yourself:

* Are you connected to a network segment that can handle that load/amount of network traffic?

* What about proxy servers that can introduce delay and have scalability issues themselves? Could that be interfering with your test?

## Lesson 2: Results validation

Don't use intrusive validation in your test cases. For example, when you have a test case, you want to make sure that the validation of the actual result is as lightweight as possible. When you validate the result, you want to make sure that you pick the simplest and fastest way to do so.

For example, if you get a sign on page back from a request and you want to validate whether the sign on page is there, don't look through the entire body of the HTML to make sure it's exactly the same as the previous one that came in. Instead, look for specific key information in the request that comes back. If you are testing identity provider (IdP)-initiated single sign-on (SSO), use a simple, lightweight adapter on the service provider (SP) side that returns a simple, small, static HTML page.

If you have too heavy of a validation approach, it slows you down overall. This in turn means you might not really understand where the bottleneck is located.

## Lesson 3: Warm up your server

As far as the backend goes, tune and warm up the system. When you deploy PingFederate out-of-the-box on a server with 8 GB RAM/multi-core system, understand it is not fully tuned. Make sure that you go through some sort of tuning process so that PingFederate can use the resources that are available to it.

Don't test a cold system because cold systems don't yield typical results. Don't just restart a PingFederate server and immediately hit it with load, as this is not a valid approach. Java by nature improves over time with the just-in-time (JIT) compilation. Hot spots in the code are compiled rather than interpreted after a certain amount of time and if they are really hot, they can be inlined. You want to make sure that you warm the system up.

A server is typically running all the time, and it is reasonable to say that JIT compilation will have occurred. Because you want to make sure that you test a system that would otherwise be in that state, warm it up before you test it.

## Lesson 4: Things to keep in mind when monitoring performance

Performance monitoring or resource monitoring is an act of non-intrusively collecting or observing performance data from an operating or running application. As with any Java application, enterprise applications are affected by garbage collection performance.

In contrast, performance profiling is an act of collecting performance data from an operating or running application that might be intrusive on application throughput or responsiveness.

Profiling is rarely done in production environments. You want to avoid the use of profiling system, as they will affect your test.

Do not use excessive logging or harsh monitoring tools that affect the overall performance of the product. Just attaching JConsole monitoring to the system can affect runtime performance and give you results that are not usable because the system is spending part of its time responding to requests from the monitoring tools. Doing this results in additional load on the system that you are not yet accounting for.

* CPU

  For an application to reach its highest performance or scalability, it needs to not only take full advantage of the CPU cycles available to it, but also to use them in a non-wasteful manner. Making efficient use of CPU cycles can be challenging for multithreaded applications running on multiprocessor and multicore systems. Additionally, it is important to note that an application that can saturate CPU resources does not necessarily imply it has reached its maximum performance or scalability. To identify how an application is utilizing CPU cycles, monitor CPU utilization at the operating system level with tools such as perfmon or typeperf (command-line tool) or System Manager, with top being the command-line example.

  Linux has vmstat, which shows combined CPU utilization across all virtual processors. Vmstat can optionally take a reporting interval, in seconds, as a command-line argument. If no reporting interval is given to vmstat, the reported output is a summary of all CPU use data collected since the system has last been booted. When a reporting interval is specified, the first row of statistics is a summary of all data collected since the system was last booted.

* Disk

  PingFederate disk operations/disk I/O should be monitored for possible performance issues. Application logs write important information about the state or behavior of the application as various events occur. Disk I/O utilization is the most useful monitoring statistic for understanding application disk usage because it is a measure of active disk I/O time. Disk I/O utilization along with system or kernel CPU utilization can be monitored using iostat.

  When monitoring applications for an extended period of time, such as several hours or days, or in a production environment, many performance engineers and system administrators of Linux systems use sar to collect performance statistics. With sar, you can select which data to collect, such as user CPU utilization, system or kernel CPU utilization, number of system calls, memory paging, and disk I/O statistics. Data collected from sar is usually looked at after the fact, as opposed to while it is being collected.

  Observing data collected over a longer period of time can help identify trends that may provide early indications of pending performance concerns. You can find additional information on what performance data can be collected and reported with sar in the Linux sar man pages.

  In summary, just remember the "observer effect" and that seeing is changing.

## Lesson 5: Did the test return expected results?

Do you get the expected results when running your tests? A performance test is based on a functional test and therefore must perform functionally first. The key metrics for performance and reliability result analysis are response time and throughput. Generally speaking, these two metrics will always be the most important, and they are offset by resource use.

You want to look at:

1. What is the response time for a given request?

2. How much data can you push through the system?

3. How many requests can you process of a given type?

After you have this information, some pass and fail criteria can be handed down from product managers. If product managers have specific criteria that must be met for those response time targets and resource use targets, those must be taken into account by the performance tester, and those are usually the ones that have to be met before you can consider something to be ready for production.

## Lesson 6: Tools of the trade

A useful tool that is HTTPS based is Apache JMeter, which you can use to send HTTPS requests to any given PingFederate server.

Tune JMeter for optimal performance where appropriate. JMeter is just software and is subject to the same resource constraints as any application. The [PingFederate Capacity Planning Guide](https://support.pingidentity.com/s/article/PingFederate-9-x-Capacity-Planning-Guide) has recommendations on this, so be sure to review it.

## Lesson 7: Understand and tune the infrastructure

PingFederate is only one part of the data center infrastructure, and it has a great deal of reliance on other systems performing properly.

Ensure PingFederate is the only application running on the test systems, or at least be aware of the fact that other applications might be running on the PingFederate server. Network latency between test systems can affect results, so ensure that network infrastructure is robust, and don't take for granted bandwidth or latency. Be aware of any firewalls or proxy servers because these can cause issues with data transfer latencies between systems. Before conducting performance tests, make sure that you have a uniform configuration across all PingFederate servers. A non-uniform configuration often manifests itself as a single cluster member that has higher CPU use and a higher latency because it is garbage collecting more frequently.

Lastly, don't forget disk latency. Make sure that if you must log information for audit purposes or other reasons, you are writing to a fast disk.

## Summary

This document has given general guidelines related to performance testing methodologies for testing a PingFederate service prior to running in a real production environment. It's shown some of the common reasons why failure to do effective performance testing can lead to a system that does not perform up to expectations.

Our next installment of this series will move into a discussion of how to set up an actual performance test and give some common examples of scripts and tools used for that.

---

---
title: "Best Practices: Performance Testing PingDirectory"
description: PingDirectory ships with several tools that you can use for performance testing.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_pd_performance_testing
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_pd_performance_testing.html
revdate: April 14, 2025
section_ids:
  performance-testing: Performance testing
  creating-test-entries: Creating test entries
  searchrate-testing: Searchrate testing
  authrate-testing: Authrate testing
  modrate-testing: Modrate testing
---

# Best Practices: Performance Testing PingDirectory

PingDirectory ships with several tools that you can use for performance testing.

## Performance testing

The following table explains what each tool does.

| Tool name    | Description                             |
| ------------ | --------------------------------------- |
| `searchrate` | Test search performance                 |
| `authrate`   | Test authentication performance         |
| `modrate`    | Test modification and write performance |

## Creating test entries

Before testing, you should create some entries to test with. The easiest way to do this is by creating a template that can be used with the `make-ldif` utility.

1. Create a template file called `templateTest.tmp`:

   ```text
   define suffix=dc=example,dc=com
   define maildomain=example.com
   define numusers=5001

   branch: ou=PerfTest,[suffix]
   subordinateTemplate: person:[numusers]

   template: person
   rdnAttr: uid
   objectClass: top
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   givenName:  <first>
   sn:  <last>
   cn: {givenName} {sn}
   initials: {givenName:1}<random:chars:ABCDEFGHIJKLMNOPQRSTUVWXYZ:1>{sn:1}
   employeeNumber:  <sequential:0>
   uid: user.{employeeNumber}
   mail: {uid}@[maildomain]
   userPassword: Password_123
   telephoneNumber:  <random:telephone>
   homePhone:  <random:telephone>
   pager:  <random:telephone>
   mobile:  <random:telephone>
   street:  <random:numeric:5>  <file:streets>  Street
   l:  <file:cities>
   st:  <file:states>
   postalCode:  <random:numeric:5>
   postalAddress: {cn}${street}${l}, {st} {postalCode}
   description: This is the description for {cn}.
   ```

2. To create an LDIF file that can be used to create test users, run `make-ldif` with the template file:

   ```shell
   bin/make-ldif --templatefile templateTest.tmp --ldiffile testUser.ldif
   ```

3. To create the `testuser` organizational unit (OU) and the test users in the directory, apply the LDIF:

   ```shell
   bin/ldapmodify -a -f testUser.ldif
   ```

## Searchrate testing

Now you can run `searchrate`. Running this utility on the same server hosting the directory being tested will have some impact on performance results.

```shell
bin/searchrate --hostname [server name] --port [LDAP port] \
--bindDN "cn=directory manager" \
--bindPassword [directory manager password] \
--baseDN dc=example,dc=com \
--scope sub --filter "(uid=user.[1-5000])" \
--attribute givenName --attribute sn --attribute mail \
--numThreads 10
```

The output will look similar to:

```text
      Recent      Recent         Recent      Recent       Overall     Overall
Searches/Sec  Avg Dur ms   Entries/Srch  Errors/Sec  Searches/Sec  Avg Dur ms
------------ ------------  ------------ ------------ ------------ ------------
    9703.655       0.204          1.000       0.000      8261.414       0.239
    9867.418       0.201          1.000       0.000      8796.509       0.225
```

Increasing the thread count will improve throughput for lower values. Higher thread counts will have diminishing returns on performance.

## Authrate testing

You should test authentication rate. `Authrate` testing will be similar to `searchrate` testing.

The following command issues a search request to find a user and then a bind request to authenticate that user:

```shell
bin/authrate --hostname [server name] --port [LDAP port] \
--bindDN "cn=directory manager" --bindPassword [password] \
--baseDN dc=example,dc=com --scope sub --filter "(uid=user.[1-5000])" \
--credentials Password_123 --numThreads 10
```

The thread count should be varied to get an idea of how thread count (connection count) will impact performance. Test results will look similar to:

```text
    Recent        Recent       Recent      Overall      Overall
 Auths/Sec    Avg Dur ms   Errors/Sec    Auths/Sec   Avg Dur ms
------------ ------------ ------------ ------------ ------------
  4131.452         0.482        0.000     3634.848        0.547
  4097.089         0.486        0.000     3789.004        0.525
  3829.309         0.520        0.000     3799.079        0.524
```

## Modrate testing

The `modrate` tool tests the rate at which the directory can process modify operations. The arguments and output format will be similar to the other rate tools.

```shell
bin/modrate --hostname [server name] --port [LDAP port] \
--bindDN "cn=directory manager" \
--bindPassword [directory manager password] \
--entryDN "uid=user.[1-5000],ou=perftest,dc=example,dc=com" \
--attribute description --valueLength 12 \
--numThreads 10
```

Output will look similar to:

```text
     Recent       Recent       Recent      Overall      Overall
   Mods/Sec   Avg Dur ms   Errors/Sec     Mods/Sec   Avg Dur ms
------------ ------------ ------------ ------------ ------------
   6505.814        1.530        0.000     6505.811        1.530
   8270.312        1.206        0.000     7387.366        1.349
   9295.419        1.073        0.000     8023.173        1.242
```

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | Remember, varying the thread or connection count will impact performance results. |

---

---
title: "Best Practices: PingDirectory Operational Support"
description: This document contains recommendations and best practices for the PingDirectory application onboarding process. Additionally, this document provides recommendations on supporting processes that could be used in conjunction with application integration.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_pd_operational_support
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_pd_operational_support.html
revdate: April 14, 2025
section_ids:
  schema-dictionary: Schema dictionary
  attributes: Attributes
  syntax: Syntax
  example: Example
  ownership-and-change-process: Ownership and change process
  attribute-metadata: Attribute metadata
  application-onboarding: Application onboarding
  application-profiling: Application profiling
  schema-modification: Schema modification
  json-attributes: JSON attributes
---

# Best Practices: PingDirectory Operational Support

This document contains recommendations and best practices for the PingDirectory application onboarding process. Additionally, this document provides recommendations on supporting processes that could be used in conjunction with application integration.

## Schema dictionary

The schema dictionary is an often overlooked portion of running a well-managed directory. It can be time-consuming to create from scratch, but you'll get that time investment back.

### Attributes

A schema dictionary does not need to contain all of the attributes that you have defined in the schema. It should only contain those attributes that will get used by applications and other consumers of the directory and whose documentation is beneficial. You don't need to thoroughly document operational attributes or attributes that are never used.

### Syntax

A schema dictionary should contain a thorough description of the attribute syntax and format in both the directory and in any data sources that feed that data into the directory.

For example, for `HRemployeeID` you might have something like this:

```
HRemployeeid
Directory: Multi-valued, Case-Insensitive Unicode, Min. Length 5,
Max. Length 90
Peoplesoft: Single-valued, VARCHAR(30)
ContractorDB: Single-valued, NUM(45)
```

It can save a lot of time if you can get your developers to look at this document when they write their code. Having an attribute that is always a five-digit number can be dangerous if the source definition is VARCHAR. Documenting the real data format prevents developers from using an implied data format and hard coding something that will cause problems later.

### Example

Let's say you have an attribute called `HRemployeeID` that is used as a user's uid. In this example, it has always been a six-digit number. Then you hire your millionth employee. You're faced with what could be a difficult decision: how many of your application entitlement databases are using `HRemployeeID` as the key field? How many of these have that field defined as being six characters long because IDs are never longer than that? And how many of those have defined that field as an integer because it's always been an integer? Keeping the six character length and moving to alphanumeric will probably break some of your apps, but so will moving to a seven-digit integer.

The schema dictionary provides an easy means of preventing programmers and database administrators from making simple mistakes like this. It's not going to solve all of your issues, but most coders, database administrators, and application architects will read the document.

It's easy for a programmer to make a mistake with implied formats. Recovering from that mistake after it's been in production for a few years is hard. Just making sure app designers are aware that many of your attributes are case-insensitive all by itself will fully return your time investment.

## Ownership and change process

Most of the data that's stored in your directory is not owned or managed by you, and you're probably the only person in your organization who knows that.

Adding some verbiage into the schema dictionary as to who the owner is for each attribute and what the change process is for that attribute will save you a lot of time.

This is also an opportunity to keep your directory clean. On a regular basis, you should reach out the data owners for each attribute and have them certify the information that you have recorded about that attribute.

If you can't find an owner for an attribute, you should remove it from your directory (after giving advance notice first to your app owners, especially the ones that might be using that attribute). The default owner of an unowned attribute that remains in your directory is you, which can lead to issues such as governance difficulties and audit compliance if you don't have accurate information about the attribute.

Once a year, you should provide attribute owners with a list of groups and accounts in the directory that have read and write access to their attributes. It's critical that access decisions to potentially sensitive attribute information are approved by the owners of that data and not by an area (the directory support team) that does not own that data.

## Attribute metadata

Directory users are constantly getting themselves into trouble by thinking they understand what the attributes stored in your directory mean.

For example, with a `streetAddress` attribute, you know that a user has at least two business addresses in HR: a physical location and a physical mailing address. And you know that about 5% of the time, those two are different. You also know which of those two got mapped to `streetAddress` in our directory, but not everyone using the attribute is aware of that.

The schema dictionary is a great place to store information about your attributes that your users need. Initially, you won't have much metadata to worry about, but as identities get more complicated and start coming from a larger and larger number of disparate sources, the volume of metadata (and the importance of having it easily available) will grow.

Metadata can include:

* A description of what the attribute is

* Level of assurance

* Data classification

* Appropriate usage (for example, `streetAddress` sourced from Database A was collected under a EULA that prohibits usage for advertising)

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To understand more about metadata documentation, you should reading up on Master Data Management (MDM) methodologies. If you've been doing IDM for a while, you'll realize fairly rapidly that IDM is essentially MDM for identity. |

## Application onboarding

About the only time an application team will feel motivated to answer your questions and provide documentation about their application is while they're waiting for you to approve creation of their service account. While they're waiting, here is some of the data you will want to collect:

* Expected SLAs

  You'll want to collect data about how responsive they expect the directory to be. This can be used later as business requirements or justification when you want to request more server resources.

* Change windows

  Knowing the change windows for your consuming applications can help you identify the best time to perform maintenance. When asking the application areas for this, it should be made clear that staying in their change windows will not be guaranteed and is just best effort.

* Financial impact

  How much revenue an application generates and how much money is lost when it is not available is very useful information to have when you are building a business case for funding and resources.

  * Revenue generated per year

  * Revenue lost for 1 minute / 10 minute / 30 minute / 1 hour / full day outage.

* Service account password change process

  Application support teams rotate into and out of their areas all of the time. If you ever get into a situation where you want to mandate a password change after an application has been in place for more than a couple of years you might discover that no one knows how to safely change that password.

* Contact information

  This can be useful to have documented somewhere if you notice that a specific application is creating issues in the directory (especially if the issues are only moderately impactful and don't rise to the level of an incident).

  You should send an email to all of your application contacts a few times a year so that you can keep the contact list updated.

## Application profiling

PingDirectory provides the ability to filter the data written to access logs based on connection criteria (see the appendix for a configuration example). This provides us with a mechanism to create a custom access log that only contains operations performed by specific accounts.

This can be used with new or existing applications to collect data about how the application behaves. The bin/summarize-access-log utility can be used against this application-specific log file to generate an overview of the types of searches that are run by the application, index utilization, errors, and an operation response time histogram.

Having this information documented provides a useful comparison if the application begins to experience production issues and can greatly simplify troubleshooting.

## Schema modification

The ability to extend the schema should not be delegated to any groups outside of the directory administrators.

If an application area needs to extend the schema they will need to document their requirements. Their documentation should include:

* Attribute names

* objectclass definitions

* Single or multi-valued

* Attribute syntaxes

* Attribute indexing requirements

* Who owns the data in the attribute

* How the data is stored in the system of record (if the directory will not be the system of record)

The application area might need some help and guidance to answer these questions.

Before extending the schema, the data owners associated with this new data should be contacted and their approval granted and documented.

### JSON attributes

If an application's data storage requirements cannot easily be met by a defined, structured schema (for example, largely non-homogeneous data), consider creating application specific JSON attributes for the application.

Because JSON attributes can contain any JSON-formatted set of data, they're an ideal candidate for storing complex data and relationships that cannot be easily defined or stored in a traditional hierarchical data model.

Because there could be little enforcement as to what gets populated, care should be taken with JSON attributes, and their usage should be reviewed on an annual basis.

Optionally, you can place restrictions on JSON attributes to restrict things such as allowable keys, must and may keys, and syntaxes. You can find more information in [Configuring JSON attribute constraints](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_config_json_attr_constraints.html) for details on how to implement JSON restrictions and JSON key indexing.

---

---
title: "Best Practices: PingFederate SAML Signing Certificates"
description: "The following reference guide details the best practices for managing PingFederate Security Assertion Markup Language (SAML) signing certificate settings, depending on your partners' preferences."
component: solution-guides
page_id: solution-guides:best_practice_guides:htg_best_practice_pf_saml_signing_cert
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/htg_best_practice_pf_saml_signing_cert.html
revdate: April 14, 2025
section_ids:
  component: Component
  what-are-the-best-practices-for-signing-certificate-administration: What are the best practices for signing certificate administration?
  when-all-of-your-partners-accept-a-self-signed-signing-certificate: When all of your partners accept a self-signed signing certificate
  when-your-partners-require-a-signing-certificate-issued-by-a-trusted-certificate-authority: When your partners require a signing certificate issued by a trusted Certificate Authority
---

# Best Practices: PingFederate SAML Signing Certificates

The following reference guide details the best practices for managing PingFederate Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)* signing certificate settings, depending on your partners' preferences.

## Component

PingFederate 10.1

## What are the best practices for signing certificate administration?

There is no cryptographic difference between self-signed or certificate authority (CA) *(tooltip: \<div class="paragraph">
\<p>An entity that issues digital certificates.\</p>
\</div>)*-signed certificates that use the same algorithm and key-length. From a security perspective, they're the same, and many customers use self-signed certificates for SAML signing.

The following are some benefits to using self-signed certificates:

* You can set a longer lifetime, decreasing the amount of update maintenance required.

* You can use PingFederate's automatic certificate rotation feature: a new key and certificate pair are periodically generated based on your policy, and active connections in PingFederate using the policy rotate to the new certificate without intervention.

* If your partners have the ability to monitor and automatically reload your metadata, they are automatically updated. For partners that cannot monitor a metadata URL that you provide, it can require coordination to update.

For more information on managing certificates and certificate rotation, see [Manage digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate Server documentation.

Although there is no security benefit, your partners might require you to use a certificate issued from a Certificate Authority (CA) for trust reasons. Self-signed certificates do not have a trust chain. If the owner of the CA-signed certificate can have their recipient partners agree to an anchored trust model, this can be a great way to ease the administrative burden. In an anchored trust model, the recipient partner validates that the signing certificate was issued by an expected issuer they trust and that the subject distinguished name matches what is expected. Because the recipient partners validate the trust chain and the expected values, rather than the specific certificate, when a newly-issued certificate is used for signing that meets the same criteria, it passes validation.

Choosing between an anchored or unanchored trust model depends on what your partners support. There is no benefit to partitioning separate certificates for internal or external partners, unless the intention is to use a stronger algorithm or key-length for external partners. One certificate is acceptable if it meets your organization's security guidelines.

For more information on whether you need a CA-signed certificate for SAML signatures, see [Do I need a trusted CA-signed certificate for SAML signatures?](https://support.pingidentity.com/s/article/Do-I-need-a-trusted-CA-signed-certificate-for-SAML-signatures) in Ping Identity's support community.

## When all of your partners accept a self-signed signing certificate

1. Create a new self-signed certificate in PingFederate.

2. Set the validity period for as long as your security team allows. For example, three to five years.

3. Configure the certificate for certificate rotation with a creation buffer threshold of at least six months before the activation buffer threshold.

   |   |                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
   |   | While the next new certificate approaches its expiration, you have six months to coordinate the new certificate transition with partners. |

4. Send your partners the new certificate and document which ones can add it as a secondary decryption key or which ones need a coordinated cutover.

   |   |                                                    |
   | - | -------------------------------------------------- |
   |   | Inventory any unused service provider connections. |

5. Plan to stagger your cutovers in advance of the existing certificate expiry.

   |   |                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Schedule your cutovers so that they all do not transition on the same day. This gives you time to test and troubleshoot while managing any amount of connections and minimizes the impact on the users of those applications. |

6. Schedule enough downtime for you and partner to update the changing connection on both sides and to test and roll back, if needed. This ensures your users are not surprised that they cannot access an application and helps them plan accordingly.

   |   |                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on your certificate rotation policy time settings, a new certificate is created before the current certificate expires, which gives you time to coordinate again. |

7. When the activation buffer threshold is reached, all of your partner connections in PingFederate using that certificate are automatically updated to use the new one, and you do not need to edit each connection yourself.

## When your partners require a signing certificate issued by a trusted Certificate Authority

1. Obtain a new CA-issued certificate with a validity period for as long as the issuer allows.

2. Send your partners the new certificate and document which ones can add it as a secondary or which ones need a coordinated cutover.

   |   |                                                               |
   | - | ------------------------------------------------------------- |
   |   | Take an inventory of any unused service provider connections. |

3. Discuss with your partners if they can and want to use the anchored trust model.

   |   |                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Document which partners support and configure the anchored trust model. The next time you need to update the CA-issued certificate, there is no action needed from your partners. |

4. Plan to stagger your cutovers in advance of the existing certificate expiry.

   |   |                                                                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Schedule the cutovers so that they all do not transition on the same day. This gives you time to test and troubleshoot while managing any amount of connections and minimizes the impact on the users of those applications. |

5. Schedule enough downtime for you and partner to update the changing connection on both sides and to test and roll back, if needed. This ensures your users are not surprised that they cannot access an application and can plan accordingly.

|   |                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Certificate rotation is not possible with CA-signed certificates, so when the new certification expires, repeat this process. You need to manually update each connection in PingFederate and coordinate with your partners that do not use the anchored trust model. |

---

---
title: "Best Practices: Planning your upgrade"
description: Upgrading your software is essential to maintaining a secure environment that responds to your business needs. This planning guide is intended to supplement your internal upgrade protocols.
component: solution-guides
page_id: solution-guides:best_practice_guides:htg_plan_software_upgrade
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/htg_plan_software_upgrade.html
revdate: July 25, 2025
page_aliases: ["best_practice_guides:htg_upgrade_planning_guide.adoc", "best_practice_guides:htg_plan_upgrade_process.adoc", "best_practice_guides:erj1574373609467.adoc", "best_practice_guides:htg_product_specific_upgrades.adoc"]
section_ids:
  upgrade-planning-guide: Upgrade planning guide
  before-you-begin: Before you begin
  steps: Steps
  upgrade-process: Upgrade process
  steps-2: Steps
  general-upgrade-best-practices: General upgrade best practices
  product-specific-upgrade-guides: Product-specific upgrade guides
  pingfederate: PingFederate
  pingaccess: PingAccess
  pingdirectory-suite-of-products: PingDirectory suite of products
  pingauthorize: PingAuthorize
  pingcentral: PingCentral
---

# Best Practices: Planning your upgrade

Upgrading your software is essential to maintaining a secure environment that responds to your business needs. This planning guide is intended to supplement your internal upgrade protocols.

If you have questions about your upgrade, post them to our [Support Community](https://support.pingidentity.com/s/community-home) for expert answers from other Ping users. Tag your questions with the "Upgrade" topic. If you're new to the community, check out [Getting Started with Ping Community](https://support.pingidentity.com/s/question/0D51W00006POG7ASAX/welcome-to-the-online-community-for-ping-identity).

If you have an urgent upgrade request, please open a support ticket in the [Support portal](https://support.pingidentity.com/s/).

If this is your first time upgrading Ping products, or if your environment has grown in complexity, we recommend connecting with your account team to ensure you have the right resources in place. Ping Identity and our partners are available to consult on upgrades or even perform them for you as part of a Professional Services engagement.

|   |                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity products are designed using open standards and can be upgraded in any order. However, we recommend that you upgrade one product at a time. Use the following templates to create a separate upgrade plan for each Ping product you use. |

## Upgrade planning guide

Use the following checklist to assess the scope of the upgrade process before beginning.

### Before you begin

Note the product name, current version, and upgrade version for each product that you're upgrading.

| Product name | Current version | Upgrade version |
| ------------ | --------------- | --------------- |
|              |                 |                 |

### Steps

1. Validate upgrade scope requirements:

   | Pre-upgrade task                                                                                                                                                                                                                                                                                                                                         | Assignees | Completion Date |
   | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------- |
   | Identify the number of deployed environments.                                                                                                                                                                                                                                                                                                            |           |                 |
   | Identify the number of nodes (admin plus runtime) per deployed environment.                                                                                                                                                                                                                                                                              |           |                 |
   | Read the upgrade guide and release notes for your target upgrade version.&#xA;&#xA;If you skip versions (for example, if you're upgrading from version 2.0 to version 5.0) we recommend reviewing the upgrade guides, release notes, and system requirements for versions 3.0 and 4.0, as well as version 5.0, to ensure that your upgrades go smoothly. |           |                 |
   | Review the differences between current and target versions. Note any incompatibilities or dependencies.                                                                                                                                                                                                                                                  |           |                 |
   | Read the tuning guides for your target upgrade version to ensure that you're aware of significant changes and new tuning recommendations, especially when Java versions have been upgraded.                                                                                                                                                              |           |                 |
   | Review the new JDK defaults and make and relevant changes.                                                                                                                                                                                                                                                                                               |           |                 |
   | Collect and review the deployment requirements, use cases, and architecture and design documents.                                                                                                                                                                                                                                                        |           |                 |
   | Accept the changes and features from the release notes.                                                                                                                                                                                                                                                                                                  |           |                 |
   | Obtain a new license key for upgraded version.                                                                                                                                                                                                                                                                                                           |           |                 |

2. Identify external services that might be affected by the upgrade:

   | External Service Type    | External Service Name |
   | ------------------------ | --------------------- |
   | Directories              |                       |
   | Databases                |                       |
   | Application integrations |                       |
   |                          |                       |
   |                          |                       |
   |                          |                       |
   |                          |                       |

3. Assess upgrade readiness.

   Do you have the team and tools to complete this upgrade successfully? If not, please reach out to your Ping Account Team to discuss resources.

## Upgrade process

This upgrade process is recommended for all Ping products.

### Steps

1. Identify the key contacts:

   | Ping primary contacts  | Contact phone or email                                                                    |
   | ---------------------- | ----------------------------------------------------------------------------------------- |
   | Account executive      |                                                                                           |
   | Ping Technical Support | * North America: 1-855-355-PING (7464)

   * EMEA: 44 0 808 196 0788

   * APJ: 61 1800 370 672 |
   | Other                  |                                                                                           |

   | Internal primary contacts |         |
   | ------------------------- | ------- |
   | Project manager           |         |
   | Technical team            |         |
   | Technical team            |         |
   | Additional stakeholders   |         |

2. Review the release notes for the upgrade version:

   | Pre-upgrade task                                                                                                                                                                                                                                                                                                  | Completion date | Assignee |
   | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------- |
   | Review release notes for upgrade.&#xA;&#xA;If you skip versions (for example, if you're upgrading from version 2.0 to version 5.0) we recommend reviewing the upgrade guides, release notes, and system requirements for versions 3.0 and 4.0, as well as version 5.0, to ensure that your upgrade goes smoothly. |                 |          |
   | Perform any pre-upgrade tasks.                                                                                                                                                                                                                                                                                    |                 |          |
   | Define your rollback plan.                                                                                                                                                                                                                                                                                        |                 |          |
   | Review the post-upgrade requirements and note any applicable tasks.                                                                                                                                                                                                                                               |                 |          |

3. Perform a trial upgrade:

   | Trial upgrade task                                                                                                                                                                                                                                                                                                                                                                                                    | Completion date | Assignee |
   | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------- |
   | Schedule a trial upgrade on a duplicate image or staging environment..&#xA;&#xA;If your staging upgrade environment differs significantly from your production upgrade environment, making a copy of the production environment (for PingFederate and PingAccess, at a minimum, the admin server and one runtime server) can help you find any anomalies that you need to address prior to a full production upgrade. |                 |          |
   | Review the upgrade log. Note the anomalies, differences, and results.                                                                                                                                                                                                                                                                                                                                                 |                 |          |
   | Review your custom templates, compare them to the original versions, and determine if these customizations need to be carried over to the templates in the new version. This review is especially important if adapter templates were added or updated.                                                                                                                                                               |                 |          |
   | Migrate your custom `.jar` files.                                                                                                                                                                                                                                                                                                                                                                                     |                 |          |
   | Migrate your HTML templates.                                                                                                                                                                                                                                                                                                                                                                                          |                 |          |
   | Migrate your velocity templates.                                                                                                                                                                                                                                                                                                                                                                                      |                 |          |
   | Verify upgrade reliability according to your company standards.                                                                                                                                                                                                                                                                                                                                                       |                 |          |
   | Create the timeline and tasks for your production upgrade.                                                                                                                                                                                                                                                                                                                                                            |                 |          |

4. Perform your production platform upgrade:

   | Production upgrade task                                                                                                                                                                                                                                                    | Completion date | Assignee |
   | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------- |
   | Create the upgrade task list for your production environment.                                                                                                                                                                                                              |                 |          |
   | Schedule your upgrade to minimize downtime.                                                                                                                                                                                                                                |                 |          |
   | Notify Ping support of scheduled upgrade.Create a case in the Support Portal with the type = "Upgrade" and include important details such as the date and time of your move, which products you are upgrading, the old and new version, and helpful architectural details. |                 |          |

## General upgrade best practices

These tips will help you avoid common pitfalls, no matter which Ping product you are upgrading.

1. If you are migrating to a new server platform/operating system, copy the engines and consoles from the original servers to the new ones.

2. If your new environment needs unlimited Java Cryptography Extension (JCE):

   * Install the new Java and unlimited JCE on the new servers.

   * Upgrade the old console installations on the new servers.

   * Upgrade the old engines on the new servers.

   * Update the `run.properties` file to reflect new IP addresses on the new servers.

3. Configure load balancers for the new clusters:

   * Validate that the new configuration is working by updating a few host files on desktops using the new load balancer address.

     |   |                                                                                                       |
     | - | ----------------------------------------------------------------------------------------------------- |
     |   | Reference adapters and OAuth aren't very testable in any scenario other than on the cutover platform. |

   * Switch DNS to the new clusters after you've successfully unit tested the configurations.

## Product-specific upgrade guides

These links go to the upgrade pages and release notes for each Ping Identity product. These pages are updated with each product release.

### PingFederate

* [PingFederate release notes](https://docs.pingidentity.com/pingfederate/latest/release_notes/pf_release_notes.html)

* [PingFederate upgrade guide](https://docs.pingidentity.com/pingfederate/latest/upgrading_pingfederate/pf_upgrade_pf.html)

* [PingFederate system requirements](https://docs.pingidentity.com/pingfederate/latest/installing_and_uninstalling_pingfederate/pf_sys_requirements.html)

* [PingFederate performance tuning guide](https://docs.pingidentity.com/pingfederate/latest/performance_tuning_guide/pf_pf_performance_tuning_guide.html)

### PingAccess

* [PingAccess release notes](https://docs.pingidentity.com/pingaccess/latest/release_notes/pa_release_notes.html)

* [PingAccess upgrade guide](https://docs.pingidentity.com/pingaccess/latest/upgrading_pingaccess/pa_upgrading_pa_landing_topic.html)

* [PingAccess zero-downtime upgrade guide](https://docs.pingidentity.com/pingaccess/latest/pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html)

* [PingAccess system requirements](https://docs.pingidentity.com/pingaccess/latest/installing_and_uninstalling_pingaccess/pa_installation_requirements.html)

* [PingAccess performance tuning guide](https://docs.pingidentity.com/pingaccess/latest/reference_guides/pa_performance_tuning.html)

### PingDirectory suite of products

* [PingDirectory suite of products release notes](https://docs.pingidentity.com/pingdirectory/latest/release_notes/pd_release_notes.html)

* [PingDirectory and PingDirectoryProxy server upgrade guide](https://docs.pingidentity.com/pingdirectory/latest/installing_the_pingdirectory_suite_of_products/pd_ds_upgrade_server.html)

* [Delegated Admin upgrade guide](https://docs.pingidentity.com/pingdirectory/latest/installing_the_pingdirectory_suite_of_products/pd_da_upgrade_application.html)

* [PingDataSync upgrade guide](https://docs.pingidentity.com/pingdirectory/latest/installing_the_pingdirectory_suite_of_products/pd_ds_upgrade_server.html)

* [PingDirectory system requirements](https://docs.pingidentity.com/pingdirectory/latest/installing_the_pingdirectory_suite_of_products/pd_ds_system_requirements.html)

* [PingDirectory performance tuning guide](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_tune_server.html)

### PingAuthorize

* [PingAuthorize release notes](https://docs.pingidentity.com/pingauthorize/latest/release_notes/paz_release_notes_legacy_home.html)

* [PingAuthorize upgrade guide](https://docs.pingidentity.com/pingauthorize/latest/upgrading_pingauthorize/paz_upgrade_pingauthorize.html)

* [PingAuthorize system requirements](https://docs.pingidentity.com/pingauthorize/latest/installing_and_uninstalling_pingauthorize/paz_system_requirements.html)

### PingCentral

* [PingCentral release notes](https://docs.pingidentity.com/pingcentral/latest/release_notes/pingcentral_relnotes_home.html)

* [PingCentral upgrade guide](https://docs.pingidentity.com/pingcentral/latest/pingcentral_for_iam_administrators/pingcentral_upgrading_pc.html)

* [PingCentral system requirements](https://docs.pingidentity.com/pingcentral/latest/pingcentral_for_iam_administrators/pingcentral_system_requirements.html)

---

---
title: "Best Practices: Session Management"
description: Session management is the process of managing user sessions in a web application. A session is a series of interactions between users and a web application that take place over a period of time.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_session_mgmt
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_session_mgmt.html
revdate: April 8, 2025
page_aliases: ["best_practice_guides:bp_session_mgmt_keyfindings.adoc", "best_practice_guides:bp_session_mgmt_recommendations.adoc"]
section_ids:
  key-findings: Key findings
  session-hijacking: Session hijacking
  man-in-the-middle-attacks: Man-in-the-middle attacks
  fixation-attacks: Fixation attacks
  recommendations: Recommendations
  planning-and-implementation-recommendations: Planning and implementation recommendations
  session-configuration-recommendations: Session configuration recommendations
  related-links: Related links
---

# Best Practices: Session Management

Session management is the process of managing user sessions in a web application. A session is a series of interactions between users and a web application that take place over a period of time.

When sessions are well-managed, users can securely interact with the application and exchange sensitive information without having to frequently re-authenticate. The type of session management that organizations use depends on the sensitivity of the information being exchanged:

* Short-lived sessions last as long as the user interacts with the application. Sessions end when the user signs out of the application or when the session lifetime limit is reached.

* Long-lived sessions keep users signed on to the application even if they leave. These sessions store session IDs on user devices, which allows users to reopen an application and use it without needing to re-authenticate, and are most often used on mobile applications.

While long-lived sessions often provide users with a better experience, it can become a security risk if someone else obtains access to the device and the session is still active.

The challenge is finding the right balance between keeping application sessions safe and providing users with the best possible experience. If a session timeout is too short, it can frustrate users because they'll be required to sign on again, but if it's too long, sensitive information can be exposed that hackers can acquire. Failure to find this balance can either result in users abandoning their sessions and not returning to the application, or sessions being attacked, both of which can result in losing customers and revenue.

The specific challenges you might face depend on the type of application you're protecting. For example, with workforce applications, because you understand who your users are and where they're located, configuring application sessions might seem to be a simple task. However, when employees travel and occasionally work from different locations, session configuration becomes more complicated.

With retail applications, users are not always authenticated until purchases and other transactions occur, so it's even more difficult to determine if a returning user is the same person. You can use long-lived cookies with unique values that identify specific visits and returns, but many users don't want to be tracked and remove the cookies. Additionally, because other users might reside in locations where cookies aren't allowed, relying on persistent cookies is not always possible.

Fortunately, there are a wide variety of ways to configure retail and workforce application sessions to ensure that authentication occurs at the appropriate time and place, using methods deemed appropriate for the risk level detected.

## Key findings

You can prevent the most common types of session attacks by ensuring that session IDs and session cookies are protected:

* Session IDs are unique identifiers that the web applications create and assign to users for the duration of their visit. The session ID remains the same for a period of time, but a new one should be created for each stage of the session.

* Session cookies are files that contain the session ID. When users initially sign on to an application, a session ID and a session cookie containing that ID are created and sent to the user's browser to provide access. The browser then sends the cookie with every request to the server, which verifies the session ID and retrieves the requested object. Session cookies are temporarily stored on the user's device during a session and are typically destroyed when the session ends.

Session cookies are different from persistent cookies because persistent cookies exist after users close their browsers. Persistent cookies are used to recognize users and their devices, track their activity, display personalized ads, and create a better browsing experience by showing users other items that might interest them based on their browsing activities. The most common types of attacks, which are session hijacking attacks, man-in-the-middle attacks, and fixation attacks, occur when either the session ID or session cookies have been compromised.

### Session hijacking

Session hijacking occurs when attackers eavesdrop on network traffic and steal or predict the target's session ID, which enables them to impersonate the user, gain access to their sensitive information, and commit fraud and theft.

In this diagram, the attacker uses sniffer tools to obtain valid session IDs.

![A diagram showing the attacker intercepting the session ID as the user is interacting with the application.](_images/rpf1695396852062.png)

Then, attackers use these session IDs to access the application by impersonating the user.

![This diagram shows the attacker using the session ID to access the application.](_images/zkp1695396742226.png)

It is especially easy for attackers to eavesdrop on open, unencrypted wireless networks, such as the free WiFi offered at coffee shops and other businesses. Laptops or mobile devices broadcast a request to the WiFi device in the room that receives the signal, but these broadcasts are also visible to any other device in the room, including eavesdropping attackers.

### Man-in-the-middle attacks

Man-in-the-middle attacks occur when attackers impersonate either the user or the application and make it appear as though normal communication is in progress. Their goal is to steal sensitive information, such as sign-on credentials, credit card numbers, and financial account details.

First, they find a way to impersonate the original connection, then they communicate with the user, and finally, they access user accounts. These types of attacks can be compared to your mailman opening your bank statement, obtaining your account information, resealing the envelope, and delivering it to your door.

![This diagram shows the attacker impersonating the original connection.](_images/rau1695396896143.png)

### Fixation attacks

Fixation attacks occur when attackers steal valid session IDs that have not yet been authenticated. Attackers send users a link that contains the session ID and tricks them into clicking on it. When they authenticate with what they think is the application, the attacker uses the same session ID to access user accounts.

![This diagram shows the attacker sending the user a link. The user clicks on the link to access what they think is the application. The attacker uses that session to access the application.](_images/iek1695396954692.png)

## Recommendations

Because the ways in which application sessions are handled can affect the user experience, it's important to get it right. You want to keep session data safe from attackers, but you also want to ensure that users enjoy interacting with your applications and aren't unnecessarily interrupted during their journeys with authentication requests. The more your users enjoy their experiences, the more likely they are to become loyal customers, have stronger emotional connections to your brand, and refer other customers, which will ultimately increase your revenue.

For example, most people understand why financial institutions require multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* and have shorter timeout sessions and expirations, and they appreciate the fact that protection efforts are in place. However, many other types of organizations are not concerned with protecting sensitive information until purchases and other transactions are made or relationships are established. They are focused on engaging their users and making applications easy to access and use, which usually means that their sessions are much longer-lived and more complicated to protect.

While no solution is perfect and some level of risk will always exist, we've created a list of best practice planning and implementation recommendations, and provided some session configuration suggestions, to help you keep your sessions as secure as possible.

### Planning and implementation recommendations

Many tend to overlook the importance of the planning process when large amounts of time, effort, and energy can be saved if session management is appropriately planned and implemented. We recommend the following:

* Include the appropriate stakeholders in your decision-making processes. Often, identity and access management (IAM) administrators and engineers begin defining session parameters without consulting others who will be affected by configuration decisions, such as product managers, marketing and support representatives, and application owners.

  It's best to work closely with these stakeholders from the beginning to ensure that you all understand the current and future state of user journeys and that you're all involved in the decisions made regarding these journeys. Consider using an orchestration tool to help you visualize each path users can take.

* Review process flows to ensure that authentication occurs at the appropriate time and place. Consider the sensitivity of the data involved in each interaction and determine what type of security is needed.

  There are many ways you can configure application sessions to best meet your needs. For example, you can create rules that drive authentication and determine what users can see and do in an application, or you can map re-authentication methods to actions taken based on risk tolerance and levels of identity assurance.

* Continually monitor your sessions to determine whether they can still be trusted. Track as many interactions as you can and obtain data feeds from as many systems as possible. This data can help you identify patterns in normal behavior so that you can more easily detect abnormal activity. You can use API detection solutions to identify suspicious activity, monitor user behavior, and compare it to known patterns. You might also consider using telemetry monitoring to help you detect irregularities.

* Use risk-based authentication, which requires users to provide additional authentication information if risk signals are detected. The risk level is determined by several unique factors including location, time of day, device and browser information, IP address, user information, and the context of the request.

* Determine what will happen when abnormal activity is detected. Will you end the session? Require users to re-authenticate? Require users to authenticate using a different method? Map out these remediation processes during the planning process and test them before implementation. Orchestration tools are also helpful in mapping out these processes.

* Use passkeys, if appropriate. Passkeys are a safer and easier alternative to passwords. With passkeys, users can sign on to apps and websites with a biometric sensor (such as a fingerprint or facial recognition), PIN, or pattern, freeing them from having to remember and manage passwords.

After you and your team implement your session configurations, the real work begins. Continue to review the data you collect and revisit your authentication processes on a regular basis. The threat landscape is constantly evolving, and it's important that you evolve with it. Technologies change quickly and new attack techniques will continue to emerge, so the session configurations that you establish today might work well, but might not work quite as well tomorrow.

### Session configuration recommendations

Hijacking attacks, man-in-the-middle attacks, and fixation attacks most often occur when either the session ID or session cookies have been compromised. To protect them as much as possible:

* **Use HTTPS instead of HTTP**

  When HTTPS is used, all communication between the user's browser and the application is encrypted, which means that even if an attacker manages to intercept the traffic, they cannot read or tamper with the data. HTTPS also provides authentication, which ensures that users are communicating with the real application and not a fake application set up by an attacker. To protect cookies, we also recommend enabling the following attributes:

  * The `Secure` attribute so that they will only be sent over HTTPS.

  * The `HttpOnly` attribute so that JavaScript cannot access the cookies, which prevents attackers from stealing them using cross-site scripting (XSS).

* **Create secure session IDs and cookies**

  To ensure that attackers can't predict session IDs, it's considered an industry best practice to randomly generate session IDs that are a unique combination of letters and numbers at least 128 bits (16 bytes) long. This ID is simply an identifier and shouldn't contain sensitive information. When the session ID is created, a session cookie is also created to store the ID. It's a good idea to store session IDs in a different cookie from other sensitive information, such as a username. That way, even if an attacker manages to obtain the cookie, they won't be able to hijack a session without knowing the username. It's also a good idea to encrypt session IDs so that attackers can't read them without having the encryption key.

* **Limit the number of simultaneous sessions per user**

  If an attacker were to gain access to a user's account, they could do whatever they want. However, if you limit the number of simultaneous sessions available to each user, the application will only be available from one device at a time. This doesn't mean that users can only access the application from one device. It means that users can only be signed on to one device at a time.

* **Regenerate session IDs**

  To protect session IDs, we recommend regenerating them after users sign on to the application because it makes it much more difficult for hackers to exploit session IDs. It's also important to regenerate session IDs when users' privileges change. If a hacker hijacks a user's session, they will have access to the user's account with all of the privileges that the user has. However, if the session ID is regenerated after a significant privilege change, the hacker will no longer have a valid session ID, which makes it more difficult for them to access the user's account and escalate their privileges within the application. There are two ways to regenerate session IDs:

  * The first is to invalidate the old session ID and create a new one. This approach is the most secure, but it can cause problems if the user has multiple tabs open because they will be signed out of all of them.

  * The second is to change the secret key associated with the session ID. This approach is less secure but provides a better user experience because it doesn't sign the user out of other open tabs.

Destroying the session ID when users sign off is also highly recommended, as you invalidate the session ID and make it much more difficult for an attacker to hijack the session.

* **Invalidate all open sessions when passwords change**

  If an attacker obtains a user's password, they could use it to access the user's account. However, if all open sessions are invalidated when the password change occurs, the attacker will be locked out of the session.

* **Expire sessions based on user inactivity and risk tolerance**

  The longer sessions last, the more vulnerable they can become. The amount of time sessions should last depends on the sensitivity of the information exchanged between the user and the application and the level of identity assurance. For example, an e-commerce retail company might not have any concern about their users being signed on for long periods of time, especially if the user is just browsing and hasn't authenticated with the application. However, most financial institutions don't allow their users to be inactive for longer than 15 or 20 minutes before the session expires because the risk of fraud and theft increases.

### Related links

To learn more about session management and authentication, see:

* [PingAccess server-side session management configuration](https://docs.pingidentity.com/pingaccess/7.3/configuring_and_customizing_pingaccess/pa_server_side_session_management_config.html)

* [PingFederate session configuration](https://docs.pingidentity.com/pingfederate/11.3/administrators_reference_guide/pf_sessions.html)

* [PingOne Platform API Reference](https://apidocs.pingidentity.com/pingone/platform/v1/api/)

To learn more about monitoring solutions, see:

* [PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_overview.html)

* [PingOne Protect API Reference](https://apidocs.pingidentity.com/pingone/platform/v1/api/#pingone-protect)

* [PingOne Authorize](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_overview.html)

---

---
title: Enabling passwordless authentication in a PingFederate authentication policy
description: To enable passwordless authentication in a PingFederate authentication policy:
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_enabling_passwordless_pf_authentication_policy
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_enabling_passwordless_pf_authentication_policy.html
revdate: September 7, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling passwordless authentication in a PingFederate authentication policy

## About this task

To enable passwordless authentication in a PingFederate authentication policy:

## Steps

1. **Optional:** Create a policy contract:

   1. Go to **Authentication → Policies → Policy Contracts**.

   2. Click **Create New Contract.**

   3. Give the policy contract an appropriate name for the storage of attribute data. Click **Next**.

   4. Specify any additional attributes if required outside of the `subject` attribute to be reused later within OAuth-OpenID Connect (OIDC) or SAML-WS-Federation processing. Click **Next**.

   5. On the **Summary** page, click **Save**.

2. Create a local identity profile (LIP):

   1. Go to **Authentication → Policies → Local Identity Profiles**.

   2. Click **Create New Profile**.

   3. On the **Profile Info** tab, in the **Local Identity Profile Name** field, enter an appropriate name for the passwordless authentication processing.

   4. In the **Authentication Policy Contract** list, select an appropriate policy contract. If you created a new one, specify the policy contract from step 1. Click **Next**.

   5. For **Authentication Sources**, select **Security Key** and click **Add**. Click **Next**.

   6. On the **Summary** page, click **Save**.

3. Add the LIP to an available HTML Form IdP Adapter:

   1. Go to **Authentication → Integration → IdP Adapters** and select an available **HTML Form IdP Adapter** to use within PingFederate's authentication policy that will contain a **Passwordless Security Key** option.

   2. Click **IdP Adapter**.

   3. Scroll down to the **Local Identity Profile** section, and in the list, select the LIP that you created in step 2.

   4. Click **Save**.

4. Create an authentication policy:

   1. Go to **Authentication → Policies → Policies**.

   2. Click **Add Policy**.

   3. Give the authentication policy an appropriate name for the passwordless authentication process that will be performed.

   4. In the **Policy** list, select the **HTML Form IDP Adapter** that you added the LIP to in step 3.

   5. Under the **HTML Form IDP Adapter** that you selected, click **Rules** and specify the appropriate values.

      |   |                                |
      | - | ------------------------------ |
      |   | Case sensitivity is important. |

   6. Click **Done**.

   7. For the **Fail** branch off of the **HTML Form IDP Adapter**, click **Done**.

   8. For the **Security Key**branch, select the **PingID Adapter**.

   9. In the **Fail** branch off of the **PingID Adapter**, click **Done**.

   10. For the **Success** branch of the **PingID Adapter**, select the policy contract that you specified in step 2d.

   11. Perform the **Contract Mapping** to fulfill the **Policy Contract Attributes**. Click **Done** to return to the **Policy** tree when complete.

   12. In the last **Success** branch (the branch where **Security Key** is not selected), select the **PingID Adapter**.

   13. Under **PingID Adapter**, click **Options**.

   14. Select the appropriate attribute to provide to PingID to verify the registration status of the user performing the transaction. Click **Done.**

   15. For the **Fail** branch, click **Done**.

   16. For the **Success** branch of the non-passwordless PingID flow, select the **Policy Contract** that you specified in step 2d.

   17. Perform the **Contract Mapping** to fulfill the **Policy Contract Attributes**. Click **Done** to return to the **Policy** tree when complete.

   18. Click **Done** to return to the main **Policy** list selection.

   19. Move the authentication policy to the desired location in the list.

   20. Click **Save**.

---

---
title: Enabling passwordless authentication in the PingID cloud service
description: To enable passwordless authentication in the PingID cloud service, add a security key factor as an additional option to leverage for MFA:
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_enabling_passwordless_pid_cloud_service
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_enabling_passwordless_pid_cloud_service.html
revdate: September 7, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling passwordless authentication in the PingID cloud service

## About this task

To enable passwordless authentication in the PingID cloud service, add a security key factor as an additional option to leverage for MFA:

## Steps

1. Go to **Setup → PingID Configuration**.

2. Scroll down to **Alternate Authentication Methods**.

3. Select the **Security Key** checkbox.

4. Scroll down to the **Security Key** section.

5. Click the **Resident Key - Required** radio button.

   |   |                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When **Resident Key – Required** is selected, **User Verification** is automatically set to **Required**. If user verification was previously set to **Preferred**, all security keys that have not previously undergone user verification will be automatically disabled. |

6. Click **Save**.

---

---
title: PingID passwordless use cases
description: Windows login - passwordless makes it possible for users to sign on to their Windows computer without a password, using only one of the PingID authentication methods, such as the PingID mobile app.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_pid_passwordless_usecases
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_pid_passwordless_usecases.html
revdate: April 14, 2025
section_ids:
  windows-passwordless-login: Windows passwordless login
  overview-of-windows-passwordless-login: Overview of Windows passwordless login
---

# PingID passwordless use cases

Windows login - passwordless makes it possible for users to sign on to their Windows computer without a password, using only one of the PingID authentication methods, such as the PingID mobile app.

## Windows passwordless login

Learn more in [Integrating PingID with Windows login (passwordless)](https://docs.pingidentity.com/pingid/pingid_integrations/pid_integrating_with_windows_login_passwordless.html) in the PingID documentation.

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the initial version of Windows login - passwordless, the only supported authentication method is the PingID mobile app 1.15 or later. |

Consider the following into account before setting up Windows login - passwordless:

* For users to use the passwordless login, they must already have a device that has been paired with PingID.

* Windows login - passwordless includes support for Run as Admin.

* Windows login - passwordless includes support for remote desktop (RDP). If you plan on using RDP, you must install Windows login - passwordless on both the accessing client and the remote computer.

## Overview of Windows passwordless login

These are the main steps the administrator must do to set up the PingID integration with passwordless Windows login:

1. Create a new environment in PingOne and connect it to your existing PingID account.

2. Configure identity store provisioners.

3. Create an issuance certificate in PingOne.

4. Create an authentication policy in PingOne.

5. Create and configure a passwordless Windows login application in PingOne.

6. Generate a Key Distribution Center (KDC) certificate if necessary.

7. Install the Windows login - passwordless integration software on the individual Windows client computers.

---

---
title: Setting up Windows passwordless login
description: You can use Windows login - passwordless so that users can sign on to their Windows computer without a password.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_setting_up_windows_passwordless_login
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_setting_up_windows_passwordless_login.html
revdate: April 14, 2025
page_aliases: ["best_practice_guides:bp_setting_up_windows_passwordless_login_connect_pid_p1.adoc", "best_practice_guides:bp_setting_up_windows_passwordless_login_config_id_store.adoc", "best_practice_guides:bp_setting_up_windows_passwordless_login_create_issuance_cert.adoc", "best_practice_guides:bp_setting_up_windows_passwordless_login_create_authn_policy.adoc", "best_practice_guides:bp_setting_up_windows_passwordless_login_windows_app_p1.adoc", "best_practice_guides:bp_setting_up_windows_passwordless_login_kdc_cert.adoc", "best_practice_guides:bp_setting_up_windows_passwordless_login_install_on_client.adoc", "best_practice_guides:bp_setting_up_windows_passwordless_login_powershell.adoc", "best_practice_guides:bp_setting_up_windows_passwordless_login_troubleshooting.adoc"]
section_ids:
  before-you-begin: Before you begin
  creating-a-pingone-environment-and-connecting-it-to-a-pingid-account: Creating a PingOne environment and connecting it to a PingID account
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  configuring-identity-store-provisioners: Configuring identity store provisioners
  about-this-task-2: About this task
  creating-an-issuance-certificate-in-pingone: Creating an issuance certificate in PingOne
  about-this-task-3: About this task
  steps-2: Steps
  creating-an-authentication-policy-windows-passwordless: Creating an authentication policy (Windows passwordless)
  steps-3: Steps
  result: Result:
  creating-and-configuring-a-passwordless-windows-login-application-in-pingone: Creating and configuring a passwordless Windows login application in PingOne
  about-this-task-4: About this task
  steps-4: Steps
  generating-a-kdc-certificate: Generating a KDC certificate
  about-this-task-5: About this task
  steps-5: Steps
  installing-the-windows-login-passwordless-integration-on-client-computers: Installing the Windows login - passwordless integration on client computers
  before-you-begin-2: Before you begin
  about-this-task-6: About this task
  steps-6: Steps
  using-the-powershell-script-for-setting-up-windows-login-passwordless: Using the PowerShell script for setting up Windows login - passwordless
  about-this-task-7: About this task
  steps-7: Steps
  troubleshooting-windows-login-passwordless: Troubleshooting Windows login - passwordless
---

# Setting up Windows passwordless login

You can use Windows login - passwordless so that users can sign on to their Windows computer without a password.

## Before you begin

To set up and use the PingID integration for passwordless Windows login, the following system requirements must be met:

* Microsoft Active Directory is running on Windows Server 2016 or later

* Users' computers must be running Windows 10 (64-bit), and must support TPM 2.0.

You must have:

* Admin rights for the domain controller

* A PingOne account

* A PingID account

Users must have the PingID mobile app installed on their devices and must have already paired the device.

## Creating a PingOne environment and connecting it to a PingID account

### About this task

Create a new environment in PingOne and connect it to an existing PingID account (to allow syncing of the PingID data) or to a newly-created PingID account.

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You must create a new PingOne environment even if you have an existing environment because you cannot connect a PingID account to an existing PingOne environment. |

### Steps

1. In the PingOne admin console, click **Add Environment**.

2. Select **Build your own solution**.

3. Hover over the **PingOne SSO** element and click **Select**.

4. Hover over the **PingID** element and click **Select**.

5. Click **Next**.

6. When you are presented with the two options for PingID, you can either:

   #### Choose from:

   * Connect to an existing PingID account.

     After you select this option, enter the credentials that you use for the PingID account.

   * Create a new PingID account.

7. Click **Next**.

8. Enter a name for the new environment.

9. Select the relevant license.

10. Click **Finish**.

## Configuring identity store provisioners

### About this task

To use passwordless Windows login, user attributes must be mapped to attributes in PingOne.

If you have been using PingFederate with the PingID connector for user provisioning, you must make the transition to using PingFederate with the PingOne Provisioning connector for user provisioning.

You can find more information on using this integration in [Provisioning connector](https://docs.pingidentity.com/integrations/pingone/pingone_integration_kit/pf_p1_ik_provisioning_connector.html) in the PingOne Integration Kit documentation.

|   |                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When mapping attributes, keep in mind that the `ObjectSID` attribute must be mapped to a unique attribute in PingOne. You can find more information on passing binary attributes in [Passing binary attributes to PingOne](https://docs.pingidentity.com/integrations/pingone/pingone_integration_kit/pf_p1_ik_passing_binary_attributes_to_p1.html) in the PingOne Intergration Kit documentation.. |

## Creating an issuance certificate in PingOne

### About this task

The PingID Windows login - passwordless solution uses certificate-based authentication (CBA), so a certificate is required for each user that will be signing on. This requires that you create an issuance certificate in PingOne and then publish the certificate.

### Steps

1. Create an issuance certificate in PingOne.

   Learn more in [Adding a certificate and key pair](https://docs.pingidentity.com/pingone/settings/p1_addcertificate.html) in the PingOne documentation.

2. Publish the issuance (CA) certificate to Active Directory (AD):

   ```
   certutil -dspublish -f  <CA certificate filename>  NTAuthCA
   ```

3. To verify that the certificate was published, run the following command and make sure that you see the CA certificate in the list:

   ```
   certutil -viewstore "ldap:///CN=NTAuthCertificates,CN=Public Key Services,CN=Services,CN=Configuration,DC=<domain name>"
   ```

4. Import the CA certificate in the Group Policy Management Console (GPMC) to publish the CA certificate to end users' computers:

   1. Open the Group Policy Management Console (GPMC).

   2. Locate the relevant domain.

   3. Locate the group policy that you'll be using.

   4. In the **Public Key Policies** section, select **Trusted Root Certification Authorities** and import the CA certificate.

## Creating an authentication policy (Windows passwordless)

### Steps

1. In the PingOne admin console, open the environment you are using for Windows login - passwordless.

2. Click the **Identities** icon.

3. Click **Attributes**.

4. In the list of attributes, locate the PingOne attribute that you mapped to `ObjectSID`.

5. Click the **Pencil** ([icon: pencil, set=fa]) icon to edit the attribute properties.

6. Select the **Enforce Unique Values**checkbox. Confirm the choice if prompted to do so.

7. Click **Save**.

8. Click the **Experiences** icon.

9. Click **Authentication Policies**.

10. Click **Add Policy**.

    #### Result:

    The policy definition page opens.

11. Enter a name for the policy.

12. For **Step Type**, select **Windows Login Passwordless**.

13. In the **Match Attributes** list, select the attribute that you mapped to `ObjectSID`.

    |   |                                                                                                                        |
    | - | ---------------------------------------------------------------------------------------------------------------------- |
    |   | This list includes any attributes that you have specified as unique by selecting the **Enforce Unique Values** option. |

14. **Optional:** Select the **Offline Mode** option if you want to allow users to sign on when PingOne or PingID are not available.

15. Click **Save**.

## Creating and configuring a passwordless Windows login application in PingOne

### About this task

After creating the authentication policy, you can now create the application for passwordless Windows login:

### Steps

1. Go to the PingOne admin console and open the environment that you are using for Windows login - passwordless.

2. Click the **Connections** icon.

3. Click **Applications**.

4. Click the **[icon: plus, set=fa]**icon to add a new application.

5. For the **Application Type**, select **Native App**.

6. Click **Configure**.

7. Enter a name and description for the application. **Click Next**.

8. Enter the redirect URL, `winlogin.pingone.com://callbackauth`, and then click **Save and Continue**.

   |   |                                                                             |
   | - | --------------------------------------------------------------------------- |
   |   | You can skip the **Grant Resource Access** and **Attribute Mapping** steps. |

9. In the **Certificated Based Authentication** section, click the **Enabled** toggle.

   ![Screen capture of the Certificate Based Authentication section. The Enable toggle is selected.](_images/wut1662490785475.png)

10. Select an existing issuance certificate.

11. Go to the application's **Policies** tab and drag the passwordless policy that you created from the **All Policies** list to the **Applied Policies** list.

    ![Screen capture of the Policies tab. Applied Policy has passwordless\_policy added to it](_images/mlk1662490521899.png)

## Generating a KDC certificate

### About this task

If there is not yet a certificate for the KDC server that you will be using, you will need to generate one.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The KDC certificate is used as part of the Kerberos PKINIT mutual authentication mechanism. If you already have a KDC certificate installed on your Active Directory Domain Controllers, you don't need to perform this task |

### Steps

1. Create an `.inf` file containing the following information:

   ```
   [newrequest]
         subject = "CN=<hostname>"
         KeyLength = 2048
         MachineKeySet = TRUE
         Exportable = FALSE
         RequestType = PKCS10
         SuppressDefaults = TRUE
         [Extensions]
         ;Note 2.5.29.17 is the OID for a SAN extension.
         2.5.29.17 = "{text}"
         continue = "dns=<DNS hostname>"
   ```

   |   |                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | For more information on the contents of `.inf` files for the `certreq` command, see [Certreq](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certreq_1) in the Microsoft documentation. |

2. Generate a certificate signing request from your KDC server by running `certreq -new '<path to the .inf file>' 'kdc.req'`.

3. In the PingOne admin console, open the application that you created for passwordless Windows login.

4. Click the **Configuration** tab of the application.

5. Scroll down to the **Certificate Based Authentication** section.

   ![Screen capture of the Certificate Based Authentication section](_images/tqi1662489533655.png)

6. For the KDC certificate signing request that you created previously with the `certreq` command:

   1. Set the number of days until the certificate should expire.

   2. Click **Upload request** and **Issue Certificate** to have the certificate issued.

      |   |                                                                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The KDC certificate does not have to be signed by the issuance certificate that you created with PingOne. Any valid certification path will work. |

7. Install the KDC certificate on your server:

   ```
   certreq -accept -machine -f  <KDC certificate filename>
   ```

## Installing the Windows login - passwordless integration on client computers

### Before you begin

* To use the Windows login - passwordless feature, users' computers must be running Windows 10 and must support TPM 2.0.

* The first time that a user carries out passwordless Windows login, they must be online and connected to the organizational network because certificate enrollment requires a connection to Active Directory. Afterward, there is no need for a connection to the network, and authentication can be carried out online or offline for as long as the certificate is valid.

### About this task

To install the integration for Windows login - passwordless on your users' computers using the UI-based method:

### Steps

1. Run the provided executable, and when the welcome page is displayed, click **Next**.

   ![Screen capture of the Setup -Windows Login - Passwordless window that opens after you run the executable](_images/czx1662487688997.png)

2. Accept the license agreement and click **Next**.

   ![Screen capture of the EULA page with I accept the agreement selected](_images/arp1662487791403.png)

3. The settings that must be entered on the **Passwordless Sign-on Settings** page should be copied from the **Configuration** tab of the application that you created for Windows login - passwordless in PingOne. If your organization uses a proxy, click **Configure Proxy**. Otherwise, click **Next**.

   ![Screen capture of the Windows login - passwordless Password Sign-on Settngs page](_images/zza1662488031520.png)

4. If you clicked **Configure Proxy** in the previous step, enter the proxy information, click **Apply**, and when you are returned to the **Passwordless Sign-on Settings** page, click **Next**.

   ![Screen capture of the Windows login - passwordsless Proxy Configuration page](_images/fbd1662488173862.png)

5. When the **Ready to Install** page is open, click **Install** to start the installation.

   ![Screen capture of the Windows login - passwordless Ready to Install page](_images/osk1662487534585.png)

## Using the PowerShell script for setting up Windows login - passwordless

### About this task

You can use the `Configure-Passwordless.ps1` PowerShell script to quickly perform the steps required to set up Windows login - passwordless.

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | Only use this for purposes such as informal testing or demonstrations. Do not use for a production instance. |

### Steps

* Run `Configure-Passwordless.ps1`.

  The script carries out the following steps:

  * Creates and installs the CA certificate, also to the group policy

  * Sets `externalId` to be a unique attribute

  * Creates the authentication policy

  * Creates and configures the passwordless Windows login application

  * Creates a KDC certificate: request creation, issuing of certificate from request, installation of certificate

    You can download the script from [GitHub](https://github.com/pingidentity/pingid-windows-passwordless-configuration-script).

## Troubleshooting Windows login - passwordless

If you encounter any issues with Windows login - passwordless, review the information that is recorded in the log files and the event information that is displayed in the **Audit** window in PingOne.

You can find detailed activity information regarding Windows login - passwordless in the log files that are located in the `logs` folder under the folder that you specified during installation (the default location is `C:\Program Files\Ping Identity\PingID\Windows Passwordless\logs`). To include a greater level of detail in the log files, contact customer support for instructions on how to set the logging level to **Debug**.

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For some of the log files, there is no mechanism to limit the file size. You shouldn't leave the logging at **Debug** level for an extended period of time. |

The **Audit** window in PingOne includes information on events, such as certificate creation and user authentication. You can find more information in [Audit section](https://docs.pingidentity.com/pingone/monitoring/p1_reporting.html) in the PingOne documentation.

---

---
title: Workforce passwordless journey
description: The journey to passwordless is comprised of many phases and goals.
component: solution-guides
page_id: solution-guides:best_practice_guides:bp_workforce_passwordless_journey
canonical_url: https://docs.pingidentity.com/solution-guides/best_practice_guides/bp_workforce_passwordless_journey.html
revdate: April 14, 2025
page_aliases: ["best_practice_guides:bp_planning_workforce_passwordless_journey.adoc", "best_practice_guides:bp_lessons_learned_workforce_passwordless_journey.adoc", "best_practice_guides:bp_deploying_product.adoc"]
section_ids:
  planning-the-workforce-passwordless-journey: Planning the workforce passwordless journey
  change-management: Change management
  communication: Communication
  decide-passwordless-methods: Decide passwordless methods
  rethink-policies-and-processes: Rethink policies and processes
  testing-and-qa: Testing and QA
  planning-rollout: Planning rollout
  onboarding: Onboarding
  lost-devices: Lost devices
  lessons-learned-from-the-workforce-passwordless-journey: Lessons learned from the workforce passwordless journey
  web-browsers: Web browsers
  deploying-products: Deploying products
  before-you-begin: Before you begin
  about-this-task: About this task
---

# Workforce passwordless journey

The journey to passwordless is comprised of many phases and goals.

![A basic flow showing the journey to passwordless from centralized authentication through phasing out passwords, adding platform support, and finally reaching true passwordless](_images/dmj1662491613094.png)

The following diagrams show each step of the passwordless journey and its goals.

![A diagram of Step #1 goals to centralize SSO and MFA on an Authentication Authority Foundation and to add Risk-based MFA](_images/qld1662491310734.png)

The goals of step 1 are to centralize SSO and MFA on an authentication authority foundation.

![A diagram of Step #2 goals to reduce password use and rely on adaptive authentication to enforce the right methods as needed](_images/qpp1662491700492.png)

The goals of step 2 are to reduce password use and rely on adaptive authentication to enforce the right methods as needed.

![A diagram of Step #3 goals to implement machine passwordless control and remove the need for re-authentication with a browser](_images/tww1662492429018.png)

The goals of step 3 are to implement machine passwordless control and remove the need for re-authentication with a browser.

![A diagram of step #4 goals to eliminate passwords with ID verification at account creation and to cover all use cases](_images/slg1662493237766.png)

The goals of step 4 are to eliminate passwords with ID verification at account creation and to cover all use cases.

## Planning the workforce passwordless journey

Passwordless authentication provides technologies, such as FIDO security keys, FIDO biometrics, and Ping Risk, that eliminate the use of passwords.

Because lost and stolen passwords create security risks, passwordless authentication helps mitigate security risks associated with passwords and removes friction from the authentication process.

The following planning diagram breaks the implementation process apart into separate phases:

1. Planning the journey

2. Communicating the upcoming changes

3. Deciding on authentication methods

4. Testing the implementation

5. Preparing your help desk for passwordless

6. Rolling out the passwordless experience

![A planning diagram dividing the implementation into planning, communication, decision, testing, preparing help desk, and rolling out to support a frictionless experience.](_images/sga1662564645722.png)

### Change management

The most important step to begin discussing and planning with your organization. This helps to define the change that is coming, prepare for communication, and begin working with the internal channels that the enterprise is shifting to passwordless.

As an administrator, understand you are eliminating friction in the authentication process and improving security posture by eliminating passwords. Achieving frictionless authentication requires introducing friction at the start of the process, such as when you're planning change management, training, and implementing a deployment. The end result is a frictionless authentication experience.

When working with many internal teams through your change management processes there will be friction introduced in the beginning until this is complete.  This is the part where you introduce more friction before going frictionless.

1. Understand that you are aiming to mitigate password risks currently present and introducing a frictionless experience, improved end user experience.

2. Take advantage of biometrics and FIDO2 compliant devices.

3. Deploy adaptive authentication with passwordless using intelligent behavior analysis of user activity to determine authentication requirements:

   * Low-risk authentication requests

   * High-risk authentication requests that require re-authentication or block

When dealing with change management, understand what devices and technologies are available for the organization.  Work with the departments that handle inventory and the preferred choice of software used on workstations, and list what is available today for testing.  Ensure internal teams are aligned as you prepare for implementation.

The different changes you have planned not only determine your timelines and goals, but affect the tools and strategies that you will need going forward. Team alignment helps leaders identify whether they must provide any additional resources before rolling out passwordless authentication.

|                                                                                                                                                          |                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| What is being used with MFA today?- Are registered devices FIDO compliant?

- If not, begin introducing FIDO compliant devices allowed to be registered. | What is your current inventory?- Google, Apple, Microsoft, and so on

- Safari, Chrome, Edge

- Mac and Windows

- Windows Hello |
| Default timelines- Make sure they're realistic

- Determine testing period

- Determine rollout period

- Determine backup methods                       | Test with user groups- Seek opinions and feedback

- Hold regular product management meetings                                    |

### Communication

When planning this step, understand and determine who are the internal stakeholders including who will own what from the help desk, other departments, vendors, and application teams:

* Communicate timelines.

* Design marketing material and knowledge management articles.

* Establish the guidelines for these changes.

* Documentation and KMs.

* Prepare and train the help desk.

* Create a communication plan to update Workforce changes that are coming in the future.

### Decide passwordless methods

![An image of different types of passwordless methods, including biometrics FIDO, and phone or tablet](_images/tyg1662495558097.png)

As you decide on passwordless methods, keep the following in mind:

* Does your organization use Windows, Apple, Linux, or a combination of those?

* Are you using MFA?

* Ensure backup authentication methods are in place, such as:

  * TouchID, FaceID, FIDO2 compliant Security Key

  * Phone, tablet, laptop, and similar hardware.

    |   |                                                                                                                                                                                               |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Always register more than one device or technology. Biometric authentication is slightly more secure than a PIN, but if biometric authentication fails, it can be set up to fail back to PIN. |

* What adaptive authentication capabilities does your organization use, such as PingOne Protect?

### Rethink policies and processes

When you rethink your authentication policies, consolidate them to simplify.

When you rethink procedures, consider:

* Help desk policies

* Lost device policies

* How to test for your use cases

### Testing and QA

Before you plan for rollout, make sure you perform sufficient testing on different browsers and operating systems to prevent delays in implementation.

To test:

* Take into account third-party implementers for the standard.

  Chrome, Safari, Edge, and Firefox might have different requirements and behaviors that you must take into account.

* Involve diverse departments to help choose authentication factors and to test.

* Register a device on different operating systems.

  Some devices require updating the operating system. Updating the operating system for security requirements could create a delay with your planned timeline.

* Continue to test whenever browser and operating system updates occur.

### Planning rollout

As you plan for rollout, consider the following priorities:

* Prevent disrupting business.

* What groups or apps are already using MFA?

  Start here.

* Rollout to end users.

  What departments and groups are best-equipped for the first wave?

* Deploy in a small volume, then ramp it up:

  * 10 users with 5 or 10 applications

  * Increase to 100 users for 10 apps and so on

  * Increase to 500 users with 10 apps and so on

### Onboarding

As you prepare to onboard individuals with your passwordless authentication experience, consider the following:

* Self-service is the goal.

* Who is your user population?

  * What groups are best-equipped to be first adopters?

  * What considerations do you need to take into account for global users?

    * Not all can use MFA today.

    * Might not own smartphones.

  * What considerations do you need to take into account for seasonal employees?

    * You might not want to give them a security key.

    * You might need a policy for these groups.

* Are you using MFA?

  * What are those devices?

  * Is more than one registered?

  * How many of those would fall into biometric, security keys, Windows Hello, or others?

The following diagram shows the onboarding cycle.

![A diagram showing the new hire cycle.](_images/cjo1662496661914.png)

1. A new hire receives their Mac or Windows laptop. Include a FIDO2 compliant key for back up.

2. The user undergoes verification for the first time through PingOne Verify and a temporary password.

3. The user registers their devices, adding more than one device.

4. The user manages their devices, including adding device and reporting lost or stolen devices.

5. The user moves into a more secure, frictionless experience through passwordless authentication.

### Lost devices

How are you handling lost or stolen devices? The following can all help you plan for what to do about these devices.

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | Remember to have more than one device registered. For example, have an iPhone, iPad, and a laptop registered. |

* User verification.

* PingID mobile application.

* What's easier to get back on network?

  FIDO keys should be the second-to-last resort.

* HelpDesk can come into play through using a temporary method.

  The PingID desktop application with a lost or stolen Yubikey or phone should be your last resort.

## Lessons learned from the workforce passwordless journey

* Passwordless takes time:

  * Having an MFA deployment prior to adoption into passwordless will ease the process.

  * Setting up and testing takes time. There is a high upfront cost with time, planning, and testing. You need to understand the different behavior when interacting with different software and then test and determine what's best for your users before rolling out passwordless. Stay with the guidelines you've set to simplify the onboarding and support process moving forward.

* You are now in the hands of the implementers for the standard:

  * Chrome, Safari, Edge, and Firefox might have different behaviors that you must take into account.

  * Client browser or OS updates could change the experience.

  * Using different browsers requires multiple registrations.

* User experience:

  * Format for selecting registered devices

* User verification and adaptive authentication:

  * Risk-based authentication

### Web browsers

Different clients will provide a slightly different passwordless experience, as shown in the following example of the differences between a prompt in Chrome and a prompt in Safari.

![A pair of screen captures showing example push notifications in different browsers](_images/azo1662497971238.png)

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | FIDO must be registered twice if you are using two clients. Your organization should support at least two clients in case one encounters an issue from an update or similar. |

## Deploying products

### Before you begin

You must have:

* FIDO2 capable Security Key

  The example below leverages Yubikey 5.

* PingID Adapter 2.8.

* A browser that supports WebAuthn.

* PingFederate 10.2 or later, which provides native support for adding a passwordless authentication flow icon for the HTML Form Adapter along with only showing the **Security Key** button on the HTML Form when the browser in use supports WebAuthn.

### About this task

This document makes the following assumptions:

* The organization has a functioning HTML Form IdP Adapter that passwordless authentication processes can be added to.

* A new PingFederate authentication policy is being built as opposed to adding to an existing authentication policy, which should also be possible.

* The authentication policy built within the example is at a global level as opposed to an application-specific one. An admin determines the authentication flow that will be best suited for passwordless experience.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As of this writing, Firefox for Mac does not support PIN code user verification, resulting in the registered security key that has an associated PIN not being recognized. |