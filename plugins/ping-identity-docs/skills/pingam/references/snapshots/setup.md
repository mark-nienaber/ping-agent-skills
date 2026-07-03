---
title: Active Directory
description: Configure Active Directory as an identity store in PingAM by setting LDAP connection parameters, search filters, and attribute mappings
component: pingam
version: 8.1
page_id: pingam:setup:data-stores-active-directory
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/data-stores-active-directory.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Directory Server", "Identity Store", "LDAP"]
page_aliases: ["setup-guide:data-stores-active-directory.adoc"]
section_ids:
  all_tabs: All tabs
  load_schema: Load Schema
  server_settings_tab: Server Settings tab
  ldap_server: LDAP Server
  ldap_bind_dn: LDAP Bind DN
  ldap_bind_password: LDAP Bind Password
  ldap_organization_dn: LDAP Organization DN
  ldap_connection_mode: LDAP Connection Mode
  ldap_connection_pool_minimum_size: LDAP Connection Pool Minimum Size
  ldap_connection_pool_maximum_size: LDAP Connection Pool Maximum Size
  ldap_connection_heartbeat_interval: LDAP Connection Heartbeat Interval
  ldap_connection_heartbeat_search_base: LDAP Connection Heartbeat Search Base
  ldap_connection_heartbeat_search_filter: LDAP Connection Heartbeat Search Filter
  ldap_connection_heartbeat_time_unit: LDAP Connection Heartbeat Time Unit
  maximum_results_returned_from_search: Maximum Results Returned from Search
  search_timeout: Search Timeout
  ldapv3_plugin_search_scope: LDAPv3 Plugin Search Scope
  affinity-enabled: Affinity Enabled
  affinity_level: Affinity Level
  plug_in_configuration_tab: Plug-in Configuration tab
  ldapv3_repository_plugin_class_name: LDAPv3 Repository Plugin Class Name
  attribute_name_mapping: Attribute Name Mapping
  ldapv3_plugin_supported_types_and_operations: LDAPv3 Plugin Supported Types and Operations
  user_configuration_tab: User Configuration tab
  ldap_users_search_attribute: LDAP Users Search Attribute
  ldap_users_search_filter: LDAP Users Search Filter
  ldap_user_object_class: LDAP User Object Class
  ldap_user_attributes: LDAP User Attributes
  create_user_attribute_mapping: Create User Attribute Mapping
  attribute_name_of_user_status: Attribute Name of User Status
  user_status_active_value: User Status Active Value
  user_status_inactive_value: User Status Inactive Value
  ldap_people_container_naming_attribute: LDAP People Container Naming Attribute
  ldap_people_container_value: LDAP People Container Value
  knowledge_based_authentication_attribute_name: Knowledge Based Authentication Attribute Name
  knowledge_based_authentication_active_index: Knowledge Based Authentication Active Index
  knowledge_based_authentication_attempts_attribute_name: Knowledge Based Authentication Attempts Attribute Name
  authentication_configuration_tab: Authentication Configuration tab
  authentication_naming_attribute: Authentication Naming Attribute
  group_configuration_tab: Group Configuration tab
  ldap_groups_search_attribute: LDAP Groups Search Attribute
  ldap_groups_search_filter: LDAP Groups Search Filter
  ldap_groups_container_naming_attribute: LDAP Groups Container Naming Attribute
  ldap_groups_container_value: LDAP Groups Container Value
  ldap_groups_object_class: LDAP Groups Object Class
  ldap_groups_attributes: LDAP Groups Attributes
  attribute_name_for_group_membership: Attribute Name for Group Membership
  attribute_name_of_unique_member: Attribute Name of Unique Member
  ad_recursive_group_membership_evaluation: AD Recursive Group Membership Evaluation
  persistent_search_controls_tab: Persistent Search Controls tab
  persistent_search_base_dn: Persistent Search Base DN
  persistent_search_scope: Persistent Search Scope
  error_handling_configuration_tab: Error Handling Configuration tab
  the_delay_time_between_retries: The Delay Time Between Retries
  cache_control_tab: Cache Control tab
  dn_cache: DN Cache
  dn_cache_size: DN Cache Size
---

# Active Directory

Use these attributes when configuring Active Directory identity stores:

`amster` service name: `IdRepository`

## All tabs

### Load Schema

Import the appropriate LDAP schema to the directory server before saving the configuration. The LDAP Bind DN service account must have the required privileges to perform this operation.

Learn more in [Prepare identity stores](../installation/prepare-identity-repository.html).

## Server Settings tab

### LDAP Server

An ordered list of directory servers. The format is `HOST:PORT[|SERVERID[|SITEID]]`, where `HOST:PORT` are the directory server FQDN and its port, and `SERVERID` and `SITEID` are optional parameters for deployments with multiple servers and sites.

Multiple servers must be comma-separated, for example, `ldap1.example.com:1636, ldap2.example.com:1636`.

AM uses the optional settings to determine which directory server to contact first. AM tries to contact directory servers in the following priority order, with highest priority first:

1. The first directory server in the list whose *serverID* matches the current AM server.

2. The first directory server in the list whose *siteID* matches the current AM server.

3. The first directory server in the remaining list.

If the directory server isn't available, AM proceeds to the next directory server in the list.

In production environments, you should specify more than one directory server for failover purposes.

Default: `host:port` of the initial directory server configured for this AM server.

### LDAP Bind DN

Bind DN of the service account AM uses to connect to the directory server. Some AM capabilities require write access to directory entries.

Default: `CN=Administrator,CN=Users,base-dn`

### LDAP Bind Password

Bind password for connecting to the directory server

### LDAP Organization DN

The base DN under which to find user and group profiles.

Ensure that the identity store is setup with the specified DN before making any changes to this property in AM.

Default: `base-dn`

### LDAP Connection Mode

Whether to use LDAP, LDAPS or StartTLS to connect to the directory server. When LDAPS or StartTLS are enabled, AM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where AM runs, or because you imported the certificates into the trust store.

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

### LDAP Connection Pool Minimum Size

Minimum number of connections to the directory server.

Default: `1`

### LDAP Connection Pool Maximum Size

Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

Default: `10`

### LDAP Connection Heartbeat Interval

How often to send a heartbeat request to the directory server to ensure that the connection doesn't remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0. To set the units for the interval use LDAP Connection Heartbeat Time Unit.

Default: `10`

### LDAP Connection Heartbeat Search Base

Defines the search base for:

* The heartbeat request that checks connections to the LDAP server are alive and prevents idle timeouts (keepalive).

* The load balancer availability check.

The keepalive and availability checks are only enabled if the heartbeat interval and timeout are set to a value greater than `0`.

The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.

If the search results in an error, AM fails to start up with an exception such as `org.forgerock.opendj.ldap.ConnectionException: Connect Error: No operational connection factories available`.

Default: `[Empty]`

### LDAP Connection Heartbeat Search Filter

Defines the search filter for:

* The heartbeat request that checks connections to the LDAP server are alive and prevents idle timeouts (keepalive).

* The load balancer availability check.

You can also use the absolute True and False filter (`&`).

The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.

If the search results in an error, AM fails to start up with an exception such as `org.forgerock.opendj.ldap.ConnectionException: Connect Error: No operational connection factories available`.

Default: `(objectClass=*)`

### LDAP Connection Heartbeat Time Unit

Time unit for the LDAP Connection Heartbeat Interval setting.

Default: `SECONDS`

### Maximum Results Returned from Search

A cap for the number of search results to return, for example, when viewing profiles under Identities. Rather than raise this number, consider narrowing your search to match fewer directory entries.

Default: `1000`

### Search Timeout

Maximum time to wait for search results in seconds. Doesn't apply to persistent searches.

Default: `10`

### LDAPv3 Plugin Search Scope

LDAP searches can apply to a single entry (`SCOPE_BASE`), entries directly below the search DN (`SCOPE_ONE`), or all entries below the search DN (`SEARCH_SUB`).

Default: `SCOPE_SUB`

### Affinity Enabled

Enables affinity-based load balanced access to identity stores.

Affinity-based load balancing means that each request for the same entry goes to the same directory server. The directory server used for a specific operation is determined by the DN of the identity involved.

List the directory server instances that form part of the affinity deployment in the LDAP Server field.

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | When you enable affinity, the value of the LDAP Server property **must be identical** for all AM instances in the deployment. |

Set the operations that use affinity (none, bind only, or all operations) in the Affinity Level property.

Default: `Disabled`

### Affinity Level

The affinity level AM uses to balance requests across identity stores.

|   |                                                                    |
| - | ------------------------------------------------------------------ |
|   | If the Affinity Enabled property is off, AM ignores this property. |

* `NONE` – no affinity

* `BIND` – affinity for BIND requests only

* `ALL` – affinity for all requests

Default: `ALL`

## Plug-in Configuration tab

### LDAPv3 Repository Plugin Class Name

AM identity store implementation.

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

### Attribute Name Mapping

Map of AM profile attribute names to directory server attribute names.

Default: `userPassword=unicodePwd`

### LDAPv3 Plugin Supported Types and Operations

Specifies the identity types supported by the datastore, such as `user`, `group`, or `realm`, and which operations can be performed on them.

The following table illustrates the identity types supported by this datastore, and the operations that can be performed on them:

**Supported Identity Types and Operations**

|         | read                   | create                                           | edit                                     | delete                                     | service                                                                  |
| ------- | ---------------------- | ------------------------------------------------ | ---------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------ |
| `realm` | ✔                      | ✔                                                | ✔                                        | ✔                                          | ✔                                                                        |
| `user`  | ✔                      | ✔                                                | ✔                                        | ✔                                          | ✔                                                                        |
| `group` | ✔                      | ✔                                                | ✔                                        | ✔                                          |                                                                          |
|         | Read the identity type | Create new identities of the given identity type | Edit entities of the given identity type | Delete entities of the given identity type | Read and write service settings associated with the given identity type. |

You can remove permissions based on your datastore needs. For example, if the datastore should not be written to, you can set the operations to `read` only for the identity types.

The `service` operation is only relevant to the `realm` and the `user` identity types. For example, the Session Service configuration can be stored by realm, and a user can have specific session timeout settings.

Default:\
`realm=read,create,edit,delete,service`\
`user=read,create,edit,delete,service`\
`group=read,create,edit,delete`

## User Configuration tab

### LDAP Users Search Attribute

When searching for a user by name, match values against this attribute.

Default: `cn`

|   |                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Don't modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. For example, if you configure the search attribute to `mail`, it could prevent users from being able to update their email addresses in their user profiles. |

### LDAP Users Search Filter

When searching for users, apply this LDAP search filter as well.

Default: `(objectclass=person)`

### LDAP User Object Class

User profiles have these LDAP object classes.

AM handles only those attributes listed in this setting. AM discards any such unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that AM execute a search that asks for the `mailAlternateAddress` attribute, AM does the search, but doesn't request `mailAlternateAddress`. In the same way, AM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

Default: `organizationalPerson`, `person`, `top`, `User`,

### LDAP User Attributes

User profiles have these LDAP attributes.

Default:\
`assignedDashboard`\
`cn`\
`createTimestamp`\
`devicePrintProfiles`\
`displayName`\
`distinguishedName`\
`dn`\
`employeeNumber`\
`givenName`\
`iplanet-am-auth-configuration`\
`iplanet-am-session-destroy-sessions`\
`iplanet-am-session-get-valid-sessions`\
`iplanet-am-session-max-caching-time`\
`iplanet-am-session-max-idle-time`\
`iplanet-am-session-max-session-time`\
`iplanet-am-session-quota-limit`\
`iplanet-am-session-service-status`\
`iplanet-am-user-account-life`\
`iplanet-am-user-admin-start-dn`\
`iplanet-am-user-alias-list`\
`iplanet-am-user-auth-config`\
`iplanet-am-user-auth-modules`\
`iplanet-am-user-failure-url`\
`iplanet-am-user-federation-info`\
`iplanet-am-user-federation-info-key`\
`iplanet-am-user-login-status`\
`iplanet-am-user-password-reset-force-reset`\
`iplanet-am-user-password-reset-options`\
`iplanet-am-user-password-reset-question-answer`\
`iplanet-am-user-success-url`\
`kbaActiveIndex`\
`kbaInfo`\
`mail`\
`modifyTimestamp`\
`name`\
`oath2faEnabled`\
`oathDeviceProfiles`\
`objectGUID`\
`objectclass`\
`postalAddress`\
`preferredLocale`\
`preferredlanguage`\
`preferredtimezone`\
`pushDeviceProfiles`\
`sAMAccountName`\
`sn`\
`sun-fm-saml2-nameid-info`\
`sun-fm-saml2-nameid-infokey`\
`sunAMAuthInvalidAttemptsData`\
`sunIdentityMSISDNNumber`\
`sunIdentityServerDiscoEntries`\
`sunIdentityServerPPAddressCard`\
`sunIdentityServerPPCommonNameAltCN`\
`sunIdentityServerPPCommonNameCN`\
`sunIdentityServerPPCommonNameFN`\
`sunIdentityServerPPCommonNameMN`\
`sunIdentityServerPPCommonNamePT`\
`sunIdentityServerPPCommonNameSN`\
`sunIdentityServerPPDemographicsAge`\
`sunIdentityServerPPDemographicsBirthDay`\
`sunIdentityServerPPDemographicsDisplayLanguage`\
`sunIdentityServerPPDemographicsLanguage`\
`sunIdentityServerPPDemographicsTimeZone`\
`sunIdentityServerPPEmergencyContact`\
`sunIdentityServerPPEmploymentIdentityAltO`\
`sunIdentityServerPPEmploymentIdentityJobTitle`\
`sunIdentityServerPPEmploymentIdentityOrg`\
`sunIdentityServerPPEncryPTKey`\
`sunIdentityServerPPFacadeGreetSound`\
`sunIdentityServerPPFacadeMugShot`\
`sunIdentityServerPPFacadeNamePronounced`\
`sunIdentityServerPPFacadeWebSite`\
`sunIdentityServerPPFacadegreetmesound`\
`sunIdentityServerPPInformalName`\
`sunIdentityServerPPLegalIdentityAltIdType`\
`sunIdentityServerPPLegalIdentityAltIdValue`\
`sunIdentityServerPPLegalIdentityDOB`\
`sunIdentityServerPPLegalIdentityGender`\
`sunIdentityServerPPLegalIdentityLegalName`\
`sunIdentityServerPPLegalIdentityMaritalStatus`\
`sunIdentityServerPPLegalIdentityVATIdType`\
`sunIdentityServerPPLegalIdentityVATIdValue`\
`sunIdentityServerPPMsgContact`\
`sunIdentityServerPPSignKey`\
`telephoneNumber`\
`unicodePwd`\
`userAccountControl`\
`userPrincipalname`\
`userpassword`

### Create User Attribute Mapping

When creating a user profile, apply this map of AM profile attribute names to directory server attribute names.

The LDAP user profile entries require the Common Name (`cn`) and Surname (`sn`) attributes, so that LDAP constraint violations don't occur when performing an add operation.

The `cn` attribute gets its value from the `uid` attribute, which comes from the User Name field on the AM admin UI's login page. The `sn` attribute gets the value of the `givenName` attribute. Attributes not mapped to another attribute and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile.

Default: `cn`, `sn`

### Attribute Name of User Status

Attribute to check/set user status.

Default: `userAccountControl`

### User Status Active Value

Active users have the user status attribute set to this value.

Default: `544`

### User Status Inactive Value

Inactive users have the user status attribute set to this value.

Default: `546`

### LDAP People Container Naming Attribute

RDN attribute of the LDAP base DN which contains user profiles.

Default: `cn`

### LDAP People Container Value

RDN attribute value of the LDAP base DN which contains user profiles.

If specified, AM will limit searches for user profiles to the provided base DN. Otherwise, AM searches the entire directory.

Default: `users`

### Knowledge Based Authentication Attribute Name

Profile attribute in which knowledge-based authentication information is stored.

Default: `kbaInfo`

### Knowledge Based Authentication Active Index

Profile attribute in the which knowledge-based authentication index is stored.

Default: `kbaActiveIndex`

### Knowledge Based Authentication Attempts Attribute Name

Profile attribute in which the number of failed attempts by a user when completing knowledge-based authentication information is stored.

Default: `kbaInfoAttempts`

## Authentication Configuration tab

### Authentication Naming Attribute

RDN attribute for building the bind DN when given a username and password to authenticate a user against the directory server.

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you change this value after you have deployed and configured AM, you must update or recreate all existing identities to refresh user DNs.Failure to do so could result in unsuccessful authentication or risk of impersonation attacks. |

Default: `cn`

## Group Configuration tab

### LDAP Groups Search Attribute

When searching for a group by name, match values against this attribute.

Default: `cn`

### LDAP Groups Search Filter

When searching for groups, apply this LDAP search filter as well.

Default: `(objectclass=group)`

### LDAP Groups Container Naming Attribute

RDN attribute of the LDAP base DN which contains group profiles.

Default: `cn`

### LDAP Groups Container Value

RDN attribute value of the LDAP base DN which contains group profiles.

If specified, AM will limit searches for group profiles to the provided base DN. Otherwise, AM searches the entire directory.

Default: `users`

### LDAP Groups Object Class

Group profiles have these LDAP object classes.

Default: `Group`, `top`

### LDAP Groups Attributes

Group profiles have these LDAP attributes.

Default:\
`cn`\
`distinguishedName`\
`dn`\
`member`\
`name`\
`objectCategory`\
`objectclass`\
`sAMAccountName`\
`sAMAccountType`

### Attribute Name for Group Membership

LDAP attribute in the member's LDAP entry whose values are the groups to which a member belongs.

### Attribute Name of Unique Member

Attribute in the group's LDAP entry whose values are the members of the group.

Default: `member`

### AD Recursive Group Membership Evaluation

Whether to evaluate Active Directory group membership recursively using the Active Directory specific extensible filter named `LDAP_MATCHING_RULE_IN_CHAIN`.

When enabled, AM evaluates nested group memberships when determining whether a user is a member of a group.

This option adds a performance overhead on the Active Directory server, and you might need additional indexes.

## Persistent Search Controls tab

### Persistent Search Base DN

Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

Default: `base-dn`

### Persistent Search Scope

LDAP searches can apply to a single entry (`SCOPE_BASE`), entries directly below the search DN (`SCOPE_ONE`), or all entries below the search DN (`SEARCH_SUB`).

Specify either `SCOPE_BASE` or `SCOPE_ONE`. Don't specify `SCOPE_SUB`, as it can have a severe impact on Active Directory performance.

Default: `SCOPE_SUB`

## Error Handling Configuration tab

### The Delay Time Between Retries

The number of milliseconds to wait between retry attempts when an LDAP operation fails with a retryable error.

Default: `1000`

## Cache Control tab

### DN Cache

Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when AM uses persistent searches to obtain notification of such updates.

Default: `false`

### DN Cache Size

Maximum number of DNs cached when caching is enabled.

Default: `1500`
