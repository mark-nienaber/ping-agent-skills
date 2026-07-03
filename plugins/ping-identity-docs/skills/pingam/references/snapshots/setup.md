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

---

---
title: Active Directory Lightweight Directory Services (AD LDS)
description: Configure Active Directory Lightweight Directory Services (AD LDS) as an identity store for PingAM by specifying LDAP server connection details, bind credentials, and attribute mappings
component: pingam
version: 8.1
page_id: pingam:setup:data-stores-adam
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/data-stores-adam.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Directory Server", "Identity Store", "LDAP"]
page_aliases: ["setup-guide:data-stores-adam.adoc"]
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

# Active Directory Lightweight Directory Services (AD LDS)

Use these attributes when configuring Active Directory Lightweight Directory Services (AD LDS) identity stores:

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

Bind password for connecting to the directory server.

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

How often to send a heartbeat request to the directory server to ensure that the connection doesn't remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0. To set the units for the interval, use LDAP Connection Heartbeat Time Unit.

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

Time unit for the LDAP Connection Heartbeat Interval setting

Default: `second`

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

AM handles only those attributes listed in this setting. AM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that AM execute a search that asks for the `mailAlternateAddress` attribute, AM does the search, but doesn't request `mailAlternateAddress`. In the same way, AM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

Default:\
`devicePrintProfilesContainer`\
`forgerock-am-dashboard-service`\
`iPlanetPreferences`\
`iplanet-am-auth-configuration-service`\
`iplanet-am-managed-person`\
`iplanet-am-user-service`\
`kbaInfoContainer`\
`oathDeviceProfilesContainer`\
`organizationalPerson`\
`person`\
`pushDeviceProfilesContainer`\
`sunAMAuthAccountLockout`\
`sunFMSAML2NameIdentifier`\
`sunFederationManagerDataStore`\
`sunIdentityServerLibertyPPService`\
`top`\
`User`

### LDAP User Attributes

User profiles have these LDAP attributes.

AM handles only those attributes listed in this setting. AM discards any unlisted attributes from requests and the request proceeds without the attribute.

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
`msDS-UserAccountDisabled`\
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
`userPrincipalname`\
`userpassword`

### Create User Attribute Mapping

When creating a user profile, apply this map of AM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves, (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

Default: `cn`, `sn`

### Attribute Name of User Status

Attribute to check/set user status.

Default: `msDS-UserAccountDisabled`

### User Status Active Value

Active users have the user status attribute set to this value.

Default: `FALSE`

### User Status Inactive Value

Inactive users have the user status attribute set to this value.

Default: `TRUE`

### LDAP People Container Naming Attribute

RDN attribute of the LDAP base DN which contains user profiles.

### LDAP People Container Value

RDN attribute value of the LDAP base DN which contains user profiles.

If specified, AM will limit searches for user profiles to the provided base DN. Otherwise, AM searches the entire directory.

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

Whether to evaluate Active Directory group membership recursively using the Active Directory specific extensible filter named LDAP\_MATCHING\_RULE\_IN\_CHAIN.

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

---

---
title: Advanced properties
description: Configure authorization policy and policy set caching, certificate validation, OAuth 2.0 request restrictions, and other advanced server properties in PingAM
component: pingam
version: 8.1
page_id: pingam:setup:server-advanced
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/server-advanced.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["setup-guide:server-advanced.adoc"]
---

# Advanced properties

Each server has a list of advanced properties that can be modified at Deployment > Servers > *server name* > Advanced. For a list of inherited advanced properties relevant to all servers, go to Configure > Server Defaults > Advanced.

* `am.authorization.policy.cache.expirationDurationSeconds`

  The time period, in seconds, before the policy cache expires. During this period, all policy evaluation requests are read from the policy cache.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The recommended value for this property depends on your specific deployment.The *policy cache* isn't updated when you update or delete a policy definition. Policy evaluation is based on the cached definition until the maximum cache duration is reached, or until you restart AM.Find more information in [Tune policy evaluation](../am-authorization/what-is-authz-decision.html#tune-policy-evaluation). |

  Default: `0` seconds (policy caching is disabled)

  |   |                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------- |
  |   | Policy caching remains disabled if *either* the maximum cache size *or* the expiry duration is set to `0`. |

- `am.authorization.policy.cache.maxSize`

  The maximum cache size for authorization policies.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The recommended value for this property depends on your specific deployment.The *policy cache* isn't updated when you update or delete a policy definition. Policy evaluation is based on the cached definition until the maximum cache duration is reached, or until you restart AM.Find more information in [Tune policy evaluation](../am-authorization/what-is-authz-decision.html#tune-policy-evaluation). |

  If your AM service handles a large number of policy evaluations per second, tuning this property can result in a performance improvement. Setting this value slightly higher than the maximum number of policies configured across all policy sets in all realms ensures all policies are cached.

  Default: `0` (policy caching is disabled)

  |   |                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------- |
  |   | Policy caching remains disabled if *either* the maximum cache size *or* the expiry duration is set to `0`. |

* `am.authorization.policySet.cache.expirationDurationSeconds`

  The time period, in seconds, before the policy set cache expires. During this timeframe, all policy sets are read from the policy set cache.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The recommended value for this property depends on your specific deployment.The *policy cache* isn't updated when you update or delete a policy definition. Policy evaluation is based on the cached definition until the maximum cache duration is reached, or until you restart AM.Find more information in [Tune policy evaluation](../am-authorization/what-is-authz-decision.html#tune-policy-evaluation). |

  Default: `0` seconds (policy caching is disabled)

  |   |                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------- |
  |   | Policy set caching remains disabled if *either* the maximum cache size *or* the expiry duration is set to `0`. |

- `am.authorization.policySet.cache.maxSize`

  The maximum cache size for authorization policy sets.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The recommended value for this property depends on your specific deployment.The *policy cache* isn't updated when you update or delete a policy definition. Policy evaluation is based on the cached definition until the maximum cache duration is reached, or until you restart AM.Find more information in [Tune policy evaluation](../am-authorization/what-is-authz-decision.html#tune-policy-evaluation). |

  If your AM service handles a large number of policy evaluations per second, tuning this property can result in a performance improvement. Setting this value to the maximum number of policy sets across all realms in your deployment ensures all policy sets are cached.

  Default: `0` (policy caching is disabled)

  |   |                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------- |
  |   | Policy set caching remains disabled if *either* the maximum cache size *or* the expiry duration is set to `0`. |

* `am.nodes.certificatechain.validation.enforced`

  If `true`, the [Certificate Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-collector.html) collects the entire chain of certificates from the request, and the [Certificate Validation node](https://docs.pingidentity.com/auth-node-ref/8.1/certificate-validation.html) validates all certificates in the chain. Otherwise, only the first certificate in the chain (the user certificate) is collected and validated.

  Default: `true`

- `am.cts.use.etag.assertion.on.update`

  When set to `true` (the default), AM uses ETag assertions to prevent parallel CTS updates for authentication journeys. The assertion checks that the state of the CTS token hasn't changed between the read and the update. This check applies only to CTS session updates related to journeys, when allowlisting is enabled and journey sessions are stored in the CTS token store.

To enable parallel updates on CTS sessions, set this parameter to `false`.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | Unless you use in-memory journey sessions, disabling the assertion check can expose your journey sessions to parallel CTS updates. |

* `am.oauth2.request.object.restrictions.enforced`

  Aligns AM behavior with the following specifications:

  * OAuth 2.0 Pushed Authorization Requests (PAR) ([RFC 9126](https://www.rfc-editor.org/rfc/rfc9126.html))

  * OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR) ([RFC 9101](https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2)).

  These specifications indicate the following:

  * The authorization server should ignore authorize parameters outside the `request_uri`.

  * When sending a JWT-Secured Authorization Request (JAR), the `request_uri` *must* be an `https` URI.

  To enforce this behavior in AM, set this property to `true`.

  Default: `false`

- `am.secrets.gsm.stableid.version.only`

  By default, for certificates stored in a [GSM secret store](../security/secret-stores.html#create-GSM-secret-stores), the public key published in the JWK\_URI has a Key-ID (`kid`) value that includes the name of the secret. To override the default `kid` value with only the GSM secret version, set this property to `true`.

  Default: `false`

  Find more information in [Overwrite default `kid` values](../am-oidc1/managing-jwk_uri.html#overwrite-default-kid-values).

- `bootstrap.file`

  File that contains the path to the AM configuration folder. By default, the `.openamcfg` directory is created in the home directory of the user that runs the web container. For example, `$HOME/.openamcfg/AMConfig_path_to_tomcat_webapps_am_`.

- `com.iplanet.am.cookie.c66Encode`

  Properly URL encode session tokens.

  Default: `true`

- `com.iplanet.am.daemons`

  This property was used only for authentication with modules and chains and is no longer documented.

- `com.iplanet.am.directory.ssl.enabled`

  If `true` AM connects to the configuration directory server over LDAPS.

  Default: `false`

- `com.iplanet.am.installdir`

  AM Configuration and log file location.

  Default: `~/openam/`, such as `~/am`

- `com.iplanet.am.jssproxy.checkSubjectAltName`

  When using JSS or JSSE, check whether the name values in the `SubjectAltName` certificate match the server FQDN.

  Default: `false`

- `com.iplanet.am.jssproxy.resolveIPAddress`

  When using JSS or JSSE, check that the IP address of the server resolves to the host name.

  Default: `false`

- `com.iplanet.am.jssproxy.SSLTrustHostList`

  When using JSS or JSSE, comma-separated list of server FQDNs to trust if they match the certificate CN, even if the domain name isn't correct.

- `com.iplanet.am.jssproxy.trustAllServerCerts`

  When using JSS or JSSE, set to `true` to trust whatever certificate is presented without checking.

  Default: `true`

- `com.iplanet.am.lbcookie.name`

  Used with sticky load balancers that can inspect the cookie value.

  Default: `amlbcookie`

- `com.iplanet.am.lbcookie.value`

  Used with sticky load balancers that can inspect the cookie value. The value of this property defaults to the unique AM server ID, although you can set your own unique value.

  To improve AM server performance, keep the value of the cookie set to the AM server ID when using Web Agents.

  If you have replaced the value of this property and you need to match the AM server URLs with their corresponding server IDs, query the `global-config/servers` endpoint. For example:

  ```bash
  $ curl \
  --request GET \
  --header "Accept: application/json" \
  --header "iPlanetDirectoryPro: AQIC5…​NDU1*" \
  'https://am.example.com:8443/am/json/global-config/servers?_queryFilter=true'
  {
    "result": [
      {
        "_id": "01",
        "_rev": "1372703177",
        "url": "https://am.example.com:8443/am",
        "siteName": null
      }
    ],
    "resultCount": 1,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
  }
  ```

  In the example, the server ID for server `https://am.example.com:8443/am` is `01`.

  Default: `01`

- `com.iplanet.am.pcookie.name`

  Persistent cookie name.

  Default: `DProPCookie`

- `com.iplanet.am.profile.host`

  Not used

  Default: *server-host*, such as `am.example.com`

- `com.iplanet.am.profile.port`

  Not used

  Default: *server-port*, such as `8080` or `8443`

- `com.iplanet.am.sdk.caching.enabled`

  Enables caching for configuration data and user data.

  Learn more in the [Overall server cache settings](../maintenance/caching.html#caching-server-settings) section.

  Changes to this property take effect immediately. No server restart is necessary.

  Default: `true`

- `com.iplanet.am.session.agentSessionIdleTime`

  Time in *minutes* after which a web or Java agent's [server-side](../am-sessions/cts-based-sessions.html) session expires. Note that this setting is ignored when AM creates a client-side session for a web or Java agent.

  Default: `1440` (session expires after one day). You can set this property to `0` (session never expires), or any integer higher than `30` (no maximum limit).

- `com.iplanet.am.session.client.polling.enable`

  If `true`, client applications such as web or Java agents poll for [server-side](../am-sessions/cts-based-sessions.html) session changes. If `false`, client applications register listeners for notifications about changes to server-side sessions.

  Default: `false`

- `com.iplanet.am.session.client.polling.period`

  If client applications poll for changes, number of seconds between polls.

  Default: `180`

- `com.iplanet.am.session.httpSession.enabled`

  Create an `HttpSession` for users on successful authentication.

  Default: `true`

- `com.iplanet.security.SSLSocketFactoryImpl`

  SSL socket factory implementation used by AM.

  Default: `com.sun.identity.shared.ldap.factory.JSSESocketFactory`, uses a pure Java provider

- `com.sun.identity.am.cookie.check`

  If `true`, AM checks for cookie support in the user agent and returns an error if cookies aren't supported.

  Default: `false`

- `com.sun.identity.appendSessionCookieInURL`

  If `true`, AM appends the session cookie to the URL for a zero page session.

  Default: `true`

- `com.sun.identity.auth.cookieName`

  Cookie used by the AM authentication service to handle the authentication process.

  Default: `AMAuthCookie`

- `com.sun.identity.authentication.client.ipAddressHeader`

  Set the name of the HTTP header that AM can examine to learn the client IP address when requests go through a proxy or load balancer. (When requests go through an HTTP proxy or load balancer, checking the IP address on the request alone returns the address of the proxy or load balancer rather than that of the client.) AM must be able to trust the proxy or load balancer to set the client IP address correctly in the header specified.

  Example: `com.sun.identity.authentication.client.ipAddressHeader=X-Forwarded-For`

- `com.sun.identity.authentication.multiple.tabs.used`

  If `true`, users can open many browser tabs to the login page at the same time without encountering an error.

  Default: `false`

- `com.sun.identity.authentication.setCookieToAllDomains`

  If `true`, AM allows multiple cookie domains.

  Default: `true`

- `com.sun.identity.authentication.special.users`

  List of special users always authenticated against the local directory server.

  Default: `cn=dsameuser,ou=DSAME Users,%ROOT_SUFFIX%|cn=amService-UrlAccessAgent,ou=DSAME Users,%ROOT_SUFFIX%`

- `com.sun.identity.authentication.super.user`

  Identifies an administrative user that replaces the `amAdmin` user. For example, `uid=superroot,ou=people,dc=example,dc=com`.

  You must manually create a user account for the new administrative user in the configuration datastore that has the same privileges as the `uid=admin` user.

  |   |                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The `amAdmin` account is "hard-coded" in the source of several files. The code in these files may affect the functionality of a top-level administrative user with a name other than `amAdmin`. |

  Default: `uid=amAdmin,ou=People,%ROOT_SUFFIX%`

- `com.sun.identity.authentication.uniqueCookieName`

  When cookie hijacking protection is configured, name of the cookie holding the URL to the AM server that authenticated the user.

  Default: `sunIdentityServerAuthNServer`

- `com.sun.identity.client.notification.url`

  Notification service endpoint for clients such as web and Java agents.

  Default: `server-protocol://server-host:server-port/server-uri/notificationservice`, such as `https://am.example.com:8443/am/notificationservice`

- `com.sun.identity.common.systemtimerpool.size`

  Number of threads in the shared system timer pool used to schedule operations such as session timeout.

  Default: `3`

- `com.sun.identity.cookie.httponly`

  When set to `true`, mark cookies as HTTPOnly to prevent scripts and third-party programs from accessing the cookies.

  This configuration option is used only in non-UI deployments. The UI can't set the HttpOnly name in a cookie.

  Default: `true`

- `com.sun.identity.cookie.samesite`

  Configures support for applying *SameSite* cookie rules, as per internet-draft [Cookies:HTTP State Management Mechanism](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-02#section-5.3.7).

  Available settings are as follows:

  * `strict`

    Requests originating from different domains won't have cookies sent with them.

    When this mode is enabled, any AM functionality that relies on requests being redirected back to the AM instance may not operate correctly. For example, OAuth 2.0 flows and SAML federation may not operate correctly if AM can't access the required cookies.

  * `lax`

    Cookies received from different domains can't be accessed unless the request is a *top-level* request and uses a "safe" HTTP method, such as GET, HEAD, OPTIONS, and TRACE.

  * `off`

    AM applies no restrictions on cookie domains.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | You must disable *SameSite* support if any of the following is true:- You must set `Access-Control-Allow-Credentials=true` in your CORS configuration.

      Learn more about configuring CORS in AM in [Configure CORS support](../security/enable-cors-support.html).

    - You are using SAML HTTP-POST bindings.

      For example, IdP-initiated single logout (SLO) functionality won't operate correctly if *SameSite* support is enabled, as the `iPlanetDirectoryPro` cookie wouldn't be accessible in cross-domain POST requests. Learn more in [Implement SSO and SLO](../am-saml2/saml2-sso-slo.html). |

    Default: `off`

- `com.sun.identity.enableUniqueSSOTokenCookie`

  If `true`, AM uses protection against cookie hijacking.

  Default: `false`

- `com.sun.identity.jss.donotInstallAtHighestPriority`

  If `false`, JSS takes priority over other providers.

  Default: `true`

- `com.sun.identity.monitoring`

  Activates AM monitoring.

  Default: `off`

- `com.sun.identity.monitoring.local.conn.server.url`

  URL for local connection to the monitoring service.

  Default: `service:jmx:rmi://`

- `com.sun.identity.password.deploymentDescriptor`

  Internal property used by AM.

  Default: *server-uri*, such as `am`

- `com.sun.identity.policy.Policy.policy_evaluation_weights`

  Weights of the cost of evaluating policy subjects, rules, and conditions. Evaluation is in order of the heaviest weight to the lightest.

  Default: `10:10:10`, meaning evaluation of rules, then conditions, then subjects

- `com.sun.identity.policy.resultsCacheMaxSize`

  Maximum number of policy decisions AM caches.

  Default: `10000`

- `com.sun.identity.security.checkcaller`

  If `true`, AM performs a Java security permissions check.

  Default: `false`

- `com.sun.identity.server.fqdnMap`

  Enables virtual hosts, partial hostname and IP address. Maps invalid or virtual name keys to valid FQDN values for proper redirection.

  To map `myserver` to `myserver.example.com`, set `com.sun.identity.server.fqdnMap[myserver]=myserver.example.com`.

- `com.sun.identity.session.repository.enableAttributeCompression`

  For additional compression of CTS token JSON binaries, beyond GZip, if desired.

  Default: `false`

- `com.sun.identity.session.repository.enableCompression`

  For GZip-based compression of CTS tokens, if desired.

  Default: `false`

- `com.sun.identity.session.repository.enableEncryption`

  Enables tokens to be encrypted when stored.

  Multi-instance deployments require consistent use of this property, which should be configured under Configure > Server Defaults > Advanced.

  The `am.encryption.pwd` property must also be the same for all deployed instances. You can set the Password Encryption Key property under Deployment > Servers > *server name* > Security. Verify that all servers have the same setting for this property.

  Default: `false`

- `com.sun.identity.sm.cache.enabled`

  Enables service configuration caching.

  Find important information about this property in [Overall server cache settings](../maintenance/caching.html#caching-server-settings).

  Changes to this property take effect immediately. No server restart is necessary.

  Default: `true`

- `com.sun.identity.sm.cache.ttl`

  When service configuration caching time-to-live is enabled, this sets the time to live in minutes.

  Changes to this property take effect immediately. No server restart is necessary.

  Default: `30`

- `com.sun.identity.sm.cache.ttl.enable`

  If service configuration caching is enabled, whether to enable a time-to-live for cached configuration.

  Changes to this property take effect immediately. No server restart is necessary.

  Default: `false`

- `com.sun.identity.sm.flatfile.root_dir`

  File system directory to hold file-based representation of AM configuration.

  Default: `/path/to/am/`

- `com.sun.identity.sm.sms_object_class_name`

  Class used to read and write AM service configuration entries in the directory.

  Default: `com.sun.identity.sm.SmsWrapperObject`

- `com.sun.identity.url.readTimeout`

  Used to set the read timeout in milliseconds for HTTP and HTTPS connections to other servers.

  Default: `30000`

- `com.sun.identity.urlchecker.dorequest`

  If `true`, AM sends an HTTP GET request to the `com.sun.identity.urlchecker.targeturl` as a health check against another server in the same site.

  If `false`, AM only checks the Socket connection and doesn't send an HTTP GET request.

  If each AM server runs behind a reverse proxy, then the default setting of `true` means the health check actually runs against the AM instance, rather than checking only the Socket to the reverse proxy.

  Default: `true`

- `com.sun.identity.urlchecker.targeturl`

  URL to monitor when `com.sun.identity.urlchecker.dorequest` is set to `true`.

  Default: URL to the `/am/namingservice` endpoint on the remote server

- `com.sun.identity.urlconnection.useCache`

  If `true`, AM caches documents for HTTP and HTTPS connections to other servers.

  Default: `false`

- `com.sun.identity.webcontainer`

  Name of the web container to correctly set character encoding, if necessary.

  Default: `WEB_CONTAINER`

- `console.privileged.users`

  Used to assign privileged console access to particular users. Set to a `|` separated list of users' Universal IDs, such as `console.privileged.users=uid=bjensen,ou=user,dc=am,dc=example,dc=com|uid=scarter,ou=user,dc=am,dc=example,dc=com`.

* `oauth2.provider.request.object.processing.enforced`

  Forces AM to use the specification set in the [Request Object Processing Specification](services-configuration.html#config-request-object-proc-spec) field of the OAuth 2.0 provider configuration for JWT requests.

  If set to `true`, this parameter overrides the default behavior, which is for AM to infer the request type from the contents of the request, if possible.

  Default: `false`

* `openam.auth.destroy_session_after_upgrade`

  Where to destroy the old session after a session is successfully upgraded.

  Default: `true`

* `openam.auth.session_property_upgrader`

  Class that controls which session properties are copied during session upgrade, where default is to copy all properties to the upgraded session.

  Default: `org.forgerock.openam.authentication.service.DefaultSessionPropertyUpgrader`

* `openam.auth.version.header.enabled`

  The X-DSAMEVersion http header provides detailed information about the version of AM currently running on the system, including the build and date/time of the build. AM will need to be restarted once this property is enabled.

  Default: `false`

* `openam.authentication.ignore_goto_during_logout`

  If `true`, AM ignores the `goto` query string parameter on logout and displays the logout page instead.

  Default: `false`

* `openam.cdm.default.charset`

  Character set used for globalization.

  Default: `UTF-8`

* `openam.forbidden.to.copy.headers`

  Comma-separated list of HTTP headers not to copy when the distributed authentication server forwards a request to another distributed authentication server.

  Default: `connection`

* `openam.forbidden.to.copy.request.headers`

  Comma-separated list of HTTP headers not to copy when the distributed authentication server forwards a request to another distributed authentication server.

  Default: `connection`

- `openam.private.key.jwt.encryption.algorithm.whitelist`

  Comma-separated list of encryption algorithms that the OpenID Connect clients of the Social Identity Provider service can configure in the *Private Key JWT Encryption Algorithm* field.

  You can find a list of algorithms that AM supports in the [JSON Web Algorithms (JWA)](https://datatracker.ietf.org/doc/html/draft-ietf-jose-json-web-algorithms-11#section-4.1) internet draft.

  You can find information on the Social Identity Provider service in [Social identity provider client configuration](../am-authentication/social-idp-client-reference.html).

  Unrecognized or unsupported algorithms will be saved, but not exposed in the *Private Key JWT Encryption Algorithm* field.

  This property is hot-swappable.

  Default: `RSA-OAEP,RSA-OAEP-256,ECDH-ES`

- `openam.retained.http.headers`

  Comma-separated list of HTTP headers to copy to the forwarded response when the server forwards a request to another server.

  Requests are forwarded when the server receiving the request isn't the server that originally initiated authentication. The server that originally initiated authentication is identified by a session ID stored in the `AMAuthCookie` cookie.

  On subsequent requests, the server receiving the request checks the cookie. If the cookie identifies another server, the current server forwards the request to that server.

  If a header such as `Cache-Control` has been included in the list of values for the property `openam.retained.http.request.headers` and the header must also be copied to the response, then add it to the list of values for this property.

  Example: `openam.retained.http.headers=X-DSAMEVersion,Cache-Control`

  Default: `X-DSAMEVersion`

* `openam.retained.http.request.headers`

  Comma-separated list of HTTP headers to copy to the forwarded request when the server forwards a request to another server.

  Requests are forwarded when the server receiving the request isn't the server that originally initiated authentication. The server that originally initiated authentication is identified by a session ID stored in the `AMAuthCookie` cookie.

  On subsequent requests, the server receiving the request checks the cookie. If the cookie identifies another server, the current server forwards the request to that server.

  When a reverse proxy is set up to provide the client IP address in the `X-Forwarded-For` header, if your deployment includes multiple AM servers, then this property must be set to include the header.

  Example: `openam.retained.http.request.headers=X-DSAMEVersion,X-Forwarded-For`

  AM copies the header when forwarding a request to the authoritative server where the client originally began the authentication process, so that the authoritative AM server receiving the forwarded request can determine the real client IP address.

  Use the `openam.retained.http.headers` property to retain headers to return in the response to the AM server that forwarded the request.

  Default: `X-DSAMEVersion`

* `openam.session.case.sensitive.uuid`

  If `true`, universal user IDs are considered case-sensitive when matching them.

  Default: `false`

- `org.forgerock.allow.http.client.debug`

  Specifies whether AM can output logging at the `Message` level for the `org.apache.http.wire` and `org.apache.http.headers` logging appenders.

  Possible values are:

  * `true`. The appenders' debug log level can take the same value as AM's, even `Message`.

    |   |                                                                                                                                                                                                                             |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | The appenders can log cleartext passwords or sensitive information related to client interactions. For example, scripted authentication or STS transactions.Enable this property for debugging purposes only when required. |

  * `false`. The appender's debug log level is always `warning`, unless debug is disabled.

  You can also set this property as a JVM option in the container where AM runs.\
  Default: `false`

- `org.forgerock.openam.http.ssl.connection.manager`

  The class that implements the [org.forgerock.openam.http.SslConnectionManager](../_attachments/apidocs/org/forgerock/openam/http/SslConnectionManager.html) interface, which controls both keystore and truststore settings, as well as hostname verification.

  If the container in which AM runs is configured with the `java.protocol.handler.pkgs` property set, then ensure this property is set to `com.sun.identity.protocol.AmSslConnectionManager`.

  |   |                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In previous versions of AM, this property was named `opensso.protocol.handler.pkgs`, and required a value of `com.sun.identity.protocol` if the `java.protocol.handler.pkgs` property was set by the container. |

- `org.forgerock.openam.audit.identity.activity.events.blacklist`

  A comma-separated list of audit events that won't be logged.

  For example, `AM-ACCESS-ATTEMPT,AM-GROUP-CHANGE`.

  Logging all events can impact performance. You should log only those events you intend to monitor.

  Changes to this property require a server restart.

  Default: `AM-ACCESS-ATTEMPT,AM-IDENTITY-CHANGE,AM-GROUP-CHANGE`

- `org.forgerock.openam.authLevel.excludeRequiredOrRequisite`

  This property was used only for authentication with modules and chains and is no longer documented.

- `org.forgerock.openam.auth.audit.nodes.enabled`

  When `true`, AM generates audit log messages for each authentication node reached during authentication tree flows.

  Possible values are `true` or `false`.

  Default: `true`

- `org.forgerock.openam.auth.audit.trees.enabled`

  When `true`, AM generates audit log messages with the outcome of authentication tree flows.

  Possible values are `true` or `false`.

  Default: `true`

* `org.forgerock.openam.auth.transactionauth.returnErrorOnAuthFailure`

  Specifies whether AM returns an HTTP 200 or HTTP 401 message when the user fails to complete the required actions to perform session upgrade during transactional authorization. Possible values are:

  * `false`. AM returns an HTTP 200 message with the original SSO token.

    For example:

    ```json
    {
        "tokenId": "AQIC5wM...TU3OQ*",
        "successUrl": "http://example.com/index.html",
        "realm": "/"
    }
    ```

    In this case, the user is redirected to the success URL and, when trying to access the protected resource, policy evaluation will fail since transactional authorization has failed.

  * `true`. AM returns an HTTP 401 message.

    For example:

    ```json
    {
        "code":401,
        "reason":"Unauthorized",
        "message":"Login failure",
        "detail":{
            "failureUrl":"http://example.com/unauthorized.html"
        }
    }
    ```

    In this case, the user is redirected to the failure URL.

  Default: `false`

* `org.forgerock.openam.authentication.accountExpire.days`

  Days until account expiration set after successful authentication by the account expiration post-authentication plugin.

  Default: `30`

* `org.forgerock.openam.authentication.forceAuth.enabled`

  This property was used only for authentication with modules and chains and is no longer documented.

* `org.forgerock.openam.console.autocomplete.enabled`

  Specifies whether input forms and password fields can be autocompleted. This property only affects end-user pages in the classic UI. Possible values are `true`, to enable autocomplete, and `false`, to disable it.

  Default: `true`

* `org.forgerock.openam.core.resource.lookup.cache.enabled`

  Controls whether the results of resource file lookup should be cached.

  While you are customizing the UI as described in [UI customization](../ui-customization/preface.html), set this property to `false` to allow AM immediately to pick up changes to the files as you customize them.

  Reset this to the default, `true`, when using AM in production.

  Default: `true`

* `org.forgerock.openam.core.sms.always.fail.on.invalid.attributes`

  Specifies whether the server should throw an exception, when it encounters an unknown attribute while parsing file-based configurations. By default, the server ignores any unknown attributes, and doesn't throw an exception. To override this behavior, set this property to `true`.

  Default: `false`

* `org.forgerock.openam.core.sms.placeholder_api_enabled`

  For file-based configurations, enables [property value substitution](property-value-substitution.html).

  Takes the following values:

  * `ON` enables property value substitution for all property types.

  * `STRING_ONLY` enables property value substitution for properties with string values only.

  * `OFF` disables property value substitution.

  Default: `OFF`

|   |                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The recommended way to enable property value substitution is through a Java system property, rather than with this advanced server property. |

* `org.forgerock.openam.cts.rest.enabled`

  Enables access to the CTS REST endpoint `/json/tokens`.

  Even when access to the CTS REST endpoint is enabled, only the AM global administrator has authorization to perform operations against `/json/tokens`.

  Default: `false`

  After changing this property, you must restart AM or the container in which it runs for the change to take effect.

* `org.forgerock.openam.encryption.key.digest`

  Determines the digest algorithm used along with PBKDF2 key derivation method for AES Key Wrap encryption. Possible values are `SHA1`, `SHA256`, `SHA384`, or `SHA512`.

  Set this property in AM's web container's startup script. Learn more in [Use stronger encryption algorithms](../installation/prepare-aeswrap.html).

  Default: `SHA1`

* `org.forgerock.openam.encryption.key.iterations`

  The number of iterations for the key derivation process specified in the `org.forgerock.openam.encryption.key.digest` advanced property.

  Set this property in AM's web container's startup script. Learn more in [Use stronger encryption algorithms](../installation/prepare-aeswrap.html).

  Default:\`10000\`

* `org.forgerock.openam.encryption.key.size`

  The size of the derived key for the AES Key Wrap encryption operations.

  Set this property in AM's web container's startup script. Learn more in [Use stronger encryption algorithms](../installation/prepare-aeswrap.html).

  Default: `128`

* `org.forgerock.openam.encryption.useextractandexpand`

  Enables the algorithm to reduce the performance cost of AES Key Wrap encryption even when high-iteration counts are used. Possible values are `true`, to enable it, and `false` to disable it.

  If you configure a large iteration count when this property is set to `false`, AM startup times may indicate a performance impact if there are many agents in your deployment.

  Set this property in AM's web container's startup script. Learn more in [Use stronger encryption algorithms](../installation/prepare-aeswrap.html).

  Default: `false`

* `org.forgerock.openam.httpclienthandler.system.clients.connection.timeout`

  The time new client connections using the client handler will wait before timing out.

  The value is a string specifying a number and a unit of time.

  Restart AM or the container in which it runs for the change to take effect.

  Default: `10 seconds`

* `org.forgerock.openam.httpclienthandler.system.clients.max.connections`

  The maximum number of connections allowed in the pool available for clients using the client handler.

  Use this property only when the `org.forgerock.openam.httpclienthandler.system.clients.reuse.connections.enabled` advanced server property is enabled.

  Restart AM or the container in which it runs for the change to take effect.

  Default: `64`

* `org.forgerock.openam.httpclienthandler.system.clients.pool.ttl`

  The maximum time-to-live, in milliseconds, for pooled client connections using the client handler.

  Restart AM or the container in which it runs for the change to take effect.

  Default: Not set

* `org.forgerock.openam.httpclienthandler.system.clients.response.timeout`

  The time a client using the client handler will wait for a response before timing out.

  The value is a string specifying a number and a unit of time.

  Restart AM or the container in which it runs for the change to take effect.

  Default: `10 seconds`

* `org.forgerock.openam.httpclienthandler.system.clients.retry.failed.requests.enabled`

  Specifies whether the client handler should retry failed connections. Possible values are `true` or `false`.

  Restart AM or the container in which it runs for the change to take effect.

  Default: `true`

* `org.forgerock.openam.httpclienthandler.system.clients.reuse.connections.enabled`

  When `true` the client handler pools and reuses connections. Possible values are `true` or `false`.

  Restart AM or the container in which it runs for changes to this property to take effect.

  Default: `true`

* `org.forgerock.openam.httpclienthandler.system.nonProxyHosts`

  Lists the target hosts for which requests shouldn't be proxied. Use commas to separate hostnames.

  This property supports wildcards at the start and end of any value. For example, `*.example.com` would result in a match for `customers.example.com` and `staff.example.com`, and requests wouldn't be proxied for those target hosts.

  Configure alongside the `org.forgerock.openam.httpclienthandler.system.proxy.uri` and `org.forgerock.openam.httpclienthandler.system.proxy.username` advanced server properties.

  Store the proxy password in a [secret store](../security/secret-stores.html), instead of in the configuration. Use the secret label `am.servers.httpclienthandler.proxy.secret` to map an alias for the password.

  If AM finds a matching secret for the `am.servers.httpclienthandler.proxy.secret` label in a secret store, AM ignores the `org.forgerock.openam.httpclienthandler.system.proxy.password` advanced server property.

  Default: `localhost,127.*,[::1],0.0.0.0,[::0]`

* `org.forgerock.openam.httpclienthandler.system.proxy.enabled`

  When set to `true`, AM routes outgoing [HttpClientHandler](../_attachments/apidocs/org/forgerock/http/handler/HttpClientHandler.html) requests through the HTTP proxy defined on the JVM.

  Restart AM or the container in which it runs for the change to take effect.

  |   |                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This setting can be overridden at the request level. Learn more in the [HTTP Client service settings](services-configuration.html#httpclient-secondary-config-proxy). |

  Default: Not set

* `org.forgerock.openam.httpclienthandler.system.proxy.password`

  The password of the proxy that AM uses to route outgoing client handler requests.

  For greater security, store the proxy password in a [secret store](../security/secret-stores.html), instead of in the configuration. Use the secret label `am.servers.httpclienthandler.proxy.secret` to map an alias for the password.

  If AM finds a matching secret for the `am.servers.httpclienthandler.proxy.secret` label in a secret store, AM ignores the `org.forgerock.openam.httpclienthandler.system.proxy.password` advanced server property.

  Configure alongside the `org.forgerock.openam.httpclienthandler.system.proxy.username`, `org.forgerock.openam.httpclienthandler.system.proxy.uri`, and `org.forgerock.openam.httpclienthandler.system.nonProxyHosts` advanced server properties.

  If you change this password in the configuration, you must restart AM or the container in which it runs for the change to take effect. If you store the proxy password in a secret store, you can rotate the secret without having to restart AM.

  |   |                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This setting can be overridden at the request level. Learn more in the [HTTP Client service settings](services-configuration.html#httpclient-secondary-config-proxy). |

  Default: Not set

* `org.forgerock.openam.httpclienthandler.system.proxy.uri`

  The URI of the proxy that AM will use to route outgoing client handler requests. The URI must be in the format `scheme://hostname:port`. For example, `https://myproxy.example.com:443`.

  If the proxy requires authentication, also configure the `org.forgerock.openam.httpclienthandler.system.proxy.username` and, optionally, the `org.forgerock.openam.httpclienthandler.system.nonProxyHosts` property.

  Store the proxy password in a [secret store](../security/secret-stores.html). and use the secret label `am.servers.httpclienthandler.proxy.secret` to map an alias for the password. If AM finds a matching secret for the `am.servers.httpclienthandler.proxy.secret` label in a secret store, AM ignores the `org.forgerock.openam.httpclienthandler.system.proxy.password` advanced server property.

  This property takes precedence over the `org.forgerock.openam.httpclienthandler.system.proxy.enabled` advanced server property and its related JVM properties.

  Learn more in [Configure AM for outbound communication](../security/reverse-proxy.html#outbound-communication).

  Restart AM or the container in which it runs for the change to take effect.

  |   |                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This setting can be overridden at the request level. Learn more in the [HTTP Client service settings](services-configuration.html#httpclient-secondary-config-proxy). |

  Default: Not set

* `org.forgerock.openam.httpclienthandler.system.proxy.username`

  The username of the proxy AM will use to route outgoing client handler requests.

  Configure alongside the `org.forgerock.openam.httpclienthandler.system.proxy.password` and `org.forgerock.openam.httpclienthandler.system.proxy.uri` advanced server properties.

  Restart AM or the container in which it runs for the change to take effect.

  |   |                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This setting can be overridden at the request level. Learn more in the [HTTP Client service settings](services-configuration.html#httpclient-secondary-config-proxy). |

  Default: Not set

* `org.forgerock.openam.idm.attribute.names.lower.case`

  Specifies whether the fields in JSON responses are always returned in lowercase. When `true`, AM converts the fields to lowercase.

  Default: `false`

- `org.forgerock.openam.introspect.token.query.param.allowed`

  Specifies whether AM allows HTTP GET requests, *and* the use of `token` as a query parameter in POST requests, on the [oauth2/introspect](../am-oauth2/oauth2-introspect-endpoint.html) endpoint.

  For security reasons, and in accordance with the [OAuth 2.0 Token Introspection specification](https://www.rfc-editor.org/info/rfc7662), AM disallows HTTP GET requests on the introspection endpoint, and requires HTTP POST requests instead. AM also disallows the use of `token` as a query parameter in a POST request on that endpoint; for example, `/oauth2/introspect?token=access-token`.

  If your clients in an existing deployment need to send a GET request or `token` as a query parameter to the `oauth2/introspect` endpoint, you can change this setting to `true`. However, it is recommended that you adjust your clients to use the more secure setting.

  Default: `false`

- `org.forgerock.openam.ldap.default.time.limit`

  Configures the client-side timeout, in milliseconds, applied to LDAP operations performed with the Netscape LDAP SDK.

  Default: `0` (no time limit)

- `org.forgerock.openam.ldap.dncache.expire.time`

  Sets the [DN cache](../maintenance/caching.html#caching) timeout, in milliseconds, after which an entry should be removed from the cache. A value of `0` means that the DN cache won't expire, and entries won't be removed automatically.

  |   |                                                                    |
  | - | ------------------------------------------------------------------ |
  |   | Setting this value too low can have a *severe* performance impact. |

  Default: `0` (no time limit)

- `org.forgerock.openam.ldap.heartbeat.timeout`

  The number of seconds AM should wait for a heartbeat operation to the DS server to complete, before considering the connection unavailable.

  Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to `0`.

  Default: `10`

* org.forgerock.openam.ldap.secure.protocol.version

  The protocols AM uses to connect to a secure LDAP server.

  Specify a single value, for example `TLSv1.2`, for AM to use only that protocol when connecting to affected external resources. Learn more in [Secure network communication](../security/securing-communications.html).

  Specify a comma-separated list with multiple protocols for AM to use the most secure protocol supported by the external resources.

  A value of `TLSv1.3,TLSv1.2` means that AM attempts to use the TLSv1.3 protocol to connect to the configuration and user \*s, but if a TLSv1.3 connection isn't supported, AM uses TLSv1.2.

  Default: `TLSv1.3,TLSv1.2`

* `org.forgerock.openam.notifications.agents.enabled`

  Controls whether to publish notifications for consumption by web agents and Java agents.

  Learn more about notifications in the [Web Agents Maintenance Guide](https://docs.pingidentity.com/web-agents/2025.3/maintenance-guide/notifications.html) and the [Java Agents Maintenance Guide](https://docs.pingidentity.com/java-agents/2025.3/maintenance-guide/notifications.html).

  Default: `true`

- `org.forgerock.openam.oauth2.checkIssuerForIdTokenInfo`

  If set to `true`, a query to the [/oauth2/idtokeninfo](../am-oidc1/rest-api-oidc-idtoken-validation.html) endpoint validates the `iss` (issuer) claim against the AM issuers. If the value of the `iss` claim differs from the AM issuer, AM returns the following error:

  `bad_request: Invalid id token issuer`

  Default: `false`

* `org.forgerock.openam.oauth2.tokenexpiry.skewAllowance`

  The period, in seconds, during which an OIDC ID token remains valid *after* its expiry time.

  This property allows for clock skews between servers.

  Default: `300` (5 minutes)

- `org.forgerock.openam.oauth2.client.graceperiod.disabled`

  Lets you override the default maximum refresh token grace period.

  By default, you cannot set a grace period that exceeds 120 seconds. Setting this server property to `true` disables the maximum and lets you set any grace period up to the maximum positive integer value. This value affects the refresh token grace period set in the [OAuth2.0 provider configuration](services-configuration.html#refresh-token-grace-period-provider) or on any [OAuth 2.0 clients](../am-oauth2/oauth2-register-client.html#refresh-token-grace-period-client).

  |   |                                                                                                                                                                                       |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Having a long grace period poses a security risk. You should therefore keep the grace period as small as possible. Exceeding the default maximum of 120 seconds is *not* recommended. |

  Default: `false`

* `org.forgerock.openam.oidc.SocialProvider.sub.claim.is.not.unique`

  By default, OIDC social authentication flows use the `sub` claim to identify the subject, in accordance with the [OIDC specification](https://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes), which mandates that the `sub` claim should uniquely identify the user.

  However, some identity providers don't provide a unique value for the `sub` claim. In this case, you can set this property to `true`. When set to `true`, AM uses the value of the `Auth ID Key` in the social provider configuration to identify the subject.

  Default: `false`

* `org.forgerock.openam.openidconnect.allow.open.dynamic.registration`

  Controls whether OpenID Connect clients can register dynamically without providing an access token.

  If you set this to `true` in production, take care to limit or throttle dynamic client registrations.

  Default: `false`

- `org.forgerock.openam.radius.server.context.cache.size`

  Maximum number of RADIUS client sessions that can be cached concurrently on the AM server.

  Default: `5000`

* `org.forgerock.openam.redirecturlvalidator.maxUrlLength`

  Specifies the maximum length of redirection URLs validated by AM. The Validation Service and other AM services perform redirection URL validation. Learn more in [Configure trusted URLs](../am-authentication/redirection-url-precedence.html#configure-trusted-urls).

  The default value should be adequate in most cases. Increase the default value as needed if messages similar to the following appear in your debug log files with message-level debugging enabled:

  ```
  RedirectUrlValidator.isRedirectUrlValid: The url was length 2015 which is longer than the allowed maximum of 2000
  ```

  Default: `2000`

* `org.forgerock.openam.request.max.bytes.entity.size`

  Specifies the maximum size of the body of any request made to AM. Learn more in [Limit the size of the request body](../security/limit-request-body-size.html).

  The property is hot-swappable. You don't need to restart AM for the changes to take effect.

  Default: 1 MB (1048576 bytes)

* `org.forgerock.openam.secrets.keystore.keyid.provider`

  Specifies the name of the `KeyStoreKeyIdProvider` implementation AM uses to provide key ID (`kids`) to public keys when AM is configured as an OAuth 2.0 authorization server.

  Learn more in [Customizing Public Key IDs](../am-oidc1/managing-jwk_uri.html#customizing-kids).

  Default: `org.forgerock.openam.secrets.DefaultKeyStoreKeyIdProvider`.

* `org.forgerock.openam.secrets.googlekms.decryptionkey`

  Specifies the fully qualified resource ID of the Google Cloud KMS secret used to decrypt secrets as they are read from the filesystem, environment variables, or system properties.

  This property may also specify the Google Cloud KMS secret used to decrypt the hash of the password of the `amAdmin` user, if the value of the `org.forgerock.openam.secrets.special.user.passwords.format` advanced server property is set to `GOOGLE_KMS_ENCRYPTED`.

  Only one key can be specified at a time.

  Learn more in [Using Google Cloud KMS Secrets to Decrypt AM Secrets](../security/secret-stores.html#KMS-secret-stores-for-encrypting-secrets) and [Store the amAdmin password in a secret store](../security/securing-administration.html#amadmin-password-secret-store).

  This property has no default.

* `org.forgerock.openam.secrets.special.user.passwords.format`

  The format used to store the hash of the `amAdmin` user password.

  Possible values are:

  * `ENCRYPTED_PLAIN`. The hash is encrypted with the AM encryption key.

  * `PLAIN`. The hash is unencrypted. The password **must** be randomly generated and have high entropy.

  * `GOOGLE_KMS_ENCRYPTED`. The hash is encrypted with the Google Cloud KMS secret specified in the `org.forgerock.openam.secrets.googlekms.decryptionkey` advanced server property.

  Learn more in [Store the amAdmin password in a secret store](../security/securing-administration.html#amadmin-password-secret-store).

  Default: `ENCRYPTED_PLAIN`

- `org.forgerock.openam.secrets.special.user.secret.refresh.seconds`

  The period, in seconds, after which the special administrator secret cache expires.

  Learn more in [Store the amAdmin password in a secret store](../security/securing-administration.html#amadmin-password-secret-store).

  Default: 900 (15 minutes)

- `org.forgerock.openam.session.stateless.encryption.method`

  Sets the encryption method for client-side sessions. Possible values are:

  * **A128CBC-HS256**. AES 128-bit in CBC mode using HMAC-SHA-256-128 hash (HS256 truncated to 128 bits)

  * **A192CBC-HS384**. AES 192-bit in CBC mode using HMAC-SHA-384-192 hash (HS384 truncated to 192 bits)

  * **A256CBC-HS512**. AES 256-bit in CBC mode using HMAC-SHA-512-256 hash (HS512 truncated to 256 bits)

  * **A128GCM**. AES 128-bit in GCM mode

  * **A192GCM**. AES 192-bit in GCM mode

  * **A256GCM**. AES 256-bit in GCM mode

  Default: `A128CBC-HS256`

- `org.forgerock.openam.session.stateless.logout.cache.expiryCheckIntervalSeconds`

  The period (in seconds) after which the logout token cache purges expired entries. Changes to this property require a server restart.

  Default: `60`

  Learn more in [Invalidate all sessions for a user](../am-sessions/managing-sessions-REST.html#invalidate-sessions-user).

- `org.forgerock.openam.session.stateless.rsa.padding`

  Sets the padding mode for RSA encryption of client-side sessions. Possible values are:

  * **RSA1\_5**. RSA with PKCS#1 v1.5 padding.

  * **RSA-OAEP**. RSA with OAEP and SHA-1.

  * **RSA-OAEP-256**. RSA with OAEP padding and SHA-256.

  Default: `RSA-OAEP-256`

- `org.forgerock.openam.session.stateless.signing.allownone`

  Specifies whether signing client-side sessions is enabled. When `true`, AM allows selecting `NONE` as the signing algorithm for client-side sessions under Configure > Global Services > Session > Client-Side Sessions.

- `org.forgerock.openam.smtp.system.connect.timeout`

  Specifies the amount of time, in milliseconds, that AM waits before considering that an outbound SMTP connection is unavailable.

  Default: `10000`

- `org.forgerock.openam.smtp.system.socket.read.timeout`

  Specifies the amount of time, in milliseconds, that AM waits for an SMTP read request to receive an acknowledgement before returning an error.

  Default: `10000`

- `org.forgerock.openam.smtp.system.socket.write.timeout`

  Specifies the amount of time, in milliseconds, that AM waits for an SMTP write request to receive an acknowledgement before returning an error.

  Default: `10000`

- `org.forgerock.openam.slf4j.enableTraceInMessage`

  Controls whether trace-level logging messages are generated when message-level debug logging is enabled in AM.

  Certain components that run in AM's JVM write a large volume of trace-level debug records that aren't required for troubleshooting in many cases. With this option set to `false`, trace-level debug records aren't written for these components.

  If you set this to `true` in production, take care to monitor the amount of disk space occupied by the AM debug logs.

  Default: `false`

- `org.forgerock.openam.sso.providers.list`

  Specifies an ordered list of SSO providers. AM chooses the first applicable provider depending on the context for the requested SSO operation.

  Default: `org.forgerock.openidconnect.ssoprovider.OpenIdConnectSSOProvider, org.forgerock.openam.sso.providers.stateless.StatelessSSOProvider`

- `org.forgerock.openam.trees.consumedstatedata.cache.size`

  Specifies the maximum number of trees in a realm for which to cache the results of "state" scans.

  AM recursively scans the nodes and paths in authentication trees to determine the state data that each node consumes. Caching this information for a number of trees in each realm means AM doesn't have to make multiple calls to get the tree's structure.

  If you have many complex authentication trees and a large number of realms, increasing this value may reduce the impact on performance of the consumed state scans.

  Default: `15`

- `org.forgerock.openam.xui.user.session.validation.enabled`

  Changes the UI's behavior when an authenticated session expires. Possible values are `false`, where the user notices that their session has expired when trying to interact with the UI and they are redirected to the login screen, or `true`, where AM redirects the user to a page with the session expired message when their session expires. This prevents the display of possible sensitive information on the screen after a session expires.

  This setting doesn't apply to those users that are global or realm administrators, for example, `amAdmin`.

  Default: `true`

- `org.forgerock.openidconnect.ssoprovider.maxcachesize`

  Maximum size in entries of the `OpenIdConnectSSOProvider` provider's cache. This cache is used to map OIDC tokens to SSO tokens for quick lookup.

  Default: `5000`

- `org.forgerock.policy.subject.evaluation.cache.size`

  Maintains a record of subject IDs matched or not matched in a given session. The cache is keyed on the token ID and the session is cleared when destroyed.

  Default: `10000`

* `org.forgerock.security.entitlement.enforce.realm`

  By default, calls to the `subjectattributes` endpoint are enforced per realm.

  Learn more in [Query subject attributes](../am-authorization/rest-api-authz-policies.html#rest-api-authz-subject-attributes).

  Default: `true`

- `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness`

  Specifies the format of the subject (`sub`) claim of an OAuth 2.0 access token, [logout token](../am-oidc1/backchannel-logout.html), and OIDC ID token.

  AM accepts tokens that use the old `sub` format, even if you enable this property. Before enabling this property, ensure that your clients can use the new `sub` claim format, or a combination of the `sub` and the `subname` claims.

  > **Collapse: About the subname Claim**
  >
  > The value of the `subname` claim matches the value of the `sub` claim used in versions of AM earlier than 7.1. It also matches the value of the `sub` claim if you disable the `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness` property.
  >
  > An example of the value of the `subname` claim is `bjensen`, or `myOauth2Client`.
  >
  > AM adds this claim to access and ID tokens by default.
  >
  > If you don't want the `subname` claim added by default, disable the Include subname claim in tokens issued by the OAuth2 Provider property in the OAuth2 Provider service configuration.

  Default: `true` for new installations, `false` for upgrades

  Possible values are:

  * `false`.

    The value of the `sub` claim is the username of the identity, or the name or the client that's the subject of the token.

    For example, `bjensen`, or `myOauth2Client`.

  * `true`.

    The subject claim is in the format `(type!subject)`, where:

    * `subject` is the identifier of the user/identity, or the name of the OAuth 2.0/OpenID Connect client that is the subject of the token.

    * `type` can be one of the following:

      * `age`. Indicates the *subject* is an OAuth 2.0/OpenID Connect-related user-agent or client. For example, an OAuth 2.0 client, a Remote Consent Service agent, and a Web and Java Agent internal client.

      * `usr`. Indicates the *subject* is a user/identity.

  For example, `(usr!bjensen)`, or `(age!myOAuth2Client)`.

- `org.forgerock.services.cts.reaper.cache.pollFrequencyMilliseconds`

  How often to poll the reaper cache for tokens that have expired, and delete them.

  By default, an AM instance will review its cache for tokens eligible for deletion every 100 milliseconds.

  Default: `100` (milliseconds)

  Learn more in [Tune the CTS](../cts/cts-tuning-considerations.html).

- `org.forgerock.services.cts.reaper.cache.size`

  The number of records an AM instance will store in its CTS reaper cache.

  Default: `500000`

  Learn more in [Tune the CTS](../cts/cts-tuning-considerations.html).

- `org.forgerock.services.cts.reaper.search.gracePeriodMilliseconds`

  Specifies a grace period used when searching for expired tokens. Any tokens that expired more than the specified duration ago are returned.

  Default: `300000` (milliseconds)

  Learn more in [Tune the CTS](../cts/cts-tuning-considerations.html).

- `org.forgerock.services.cts.reaper.search.pollFrequencyMilliseconds`

  How often to perform a search for expired tokens in the CTS persistence store.

  Default: `5000` (milliseconds)

  Learn more in [Tune the CTS](../cts/cts-tuning-considerations.html).

- `org.forgerock.services.cts.reaper.search.tokenLimit`

  The maximum number of expired tokens to return to the AM reaper when searching the CTS store.

  Default: `5000`

  Learn more in [Tune the CTS](../cts/cts-tuning-considerations.html).

- `org.forgerock.services.cts.store.ttlsupport.enabled`

  Specifies whether AM support for the DS entry expiration and deletion feature is enabled. Enabling this setting causes AM to clone the value of the `coreTokenExpirationDate` attribute to the `coreTokenTtlDate` attribute during token creation, which allows DS to index tokens using the `coreTokenTtlDate` attribute for the entry expiration and deletion feature.

  This property doesn't clone the values of tokens that were created before the setting was enabled.

  Set this property to `true` in conjunction with the `org.forgerock.services.cts.store.ttlsupport.exclusionlist` advanced server property when you need to configure the AM reaper to manage the expiration time for a subset of the tokens in the CTS store only.

  Learn more in [Manage expired CTS tokens](../cts/cts-reaper.html).

  Default: `false`

- `org.forgerock.services.cts.store.reaper.enabled`

  Specifies whether the AM reaper is enabled.

  |   |                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Don't disable the AM reaper unless you have a system in place to clean up expired tokens, such as the DS entry expiration and deletion feature. |

  Set this property to `true` in the following scenarios:

  * When the AM reaper must manage the expiration times for all the tokens in the CTS store.

  * When the AM reaper must manage the expiration time for a subset of the tokens in the CTS store.

  Learn more in [Manage expired CTS tokens](../cts/cts-reaper.html).

  Default: `true`

- `org.forgerock.services.cts.store.ttlsupport.exclusionlist`

  When the `org.forgerock.services.cts.store.ttlsupport.enabled` advanced server property is set to `true`, this property specifies a list of token types which won't have their `coreTokenExpirationDate` data cloned. For example, `SESSION`.

  The AM reaper will delete the excluded tokens when they expire.

  |   |                                                                       |
  | - | --------------------------------------------------------------------- |
  |   | The CTS token store lists the token types in use in your environment. |

  Learn more in [Manage expired CTS tokens](../cts/cts-reaper.html).\
  Default: Not set

- `org.forgerock.services.datalayer.connection.timeout`

  Timeout in seconds for LDAP connections to the configuration \*.

  Default: `10` (seconds)

  Find the suggested settings in [Tuning CTS Store LDAP Connections](../maintenance/tuning-ldap-settings.html#tuning-ldap-settings-cts).

- `org.forgerock.services.datalayer.connection.timeout.cts.async`

  Timeout in seconds for LDAP connections used for most CTS operations.

  Default: `10` (seconds)

  Find the suggested settings in [Tuning CTS Store LDAP Connections](../maintenance/tuning-ldap-settings.html#tuning-ldap-settings-cts).

- `org.forgerock.services.datalayer.connection.timeout.cts.reaper`

  Timeout in seconds for the LDAP connection used for CTS token cleanup.

  Default: None (don't time out)

  Find the suggested settings in [Tuning CTS Store LDAP Connections](../maintenance/tuning-ldap-settings.html#tuning-ldap-settings-cts).

- `org.forgerock.session.stateless.jwtcache.expiry.time`

  The maximum time, in seconds, that AM caches client-side session JWTs.

  Setting a long cache timeout may be more efficient, but AM won't detect if a client-side session JWT has expired or has become invalid until the cache expires.

  The property is hot-swappable. You don't need to restart AM for the changes to take effect.

  Default: `10`

- `org.forgerock.session.stateless.jwtcache.size`

  The size, in bytes, of the cache where AM stores client-side session JWTs.

  Default: `10000`

- `org.forgerock.openam.ldap.keepalive.search.base`

  Defines the search base for:

  * The heartbeat request that checks connections to the LDAP server are alive and prevents idle timeouts (keepalive).

  * The load balancer availability check.

  The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.

  If the search results in an error, AM fails to start up with an exception such as `org.forgerock.opendj.ldap.ConnectionException: Connect Error: No operational connection factories available`.

  Default: `[Empty]`

- `org.forgerock.openam.ldap.keepalive.search.filter`

  Defines the search filter for:

  * The heartbeat request that checks connections to the LDAP server are alive and prevents idle timeouts (keepalive).

  * The load balancer availability check.

    You can also use the absolute True and False filter (`&`).

  The LDAP server connection pool will be marked as unavailable if the search fails with an error, returns no entries, or if more than one entry is returned.

  If the search results in an error, AM fails to start up with an exception such as `org.forgerock.opendj.ldap.ConnectionException: Connect Error: No operational connection factories available`.

  Default: `(objectClass=*)`

* `org.forgerock.am.auth.trees.authenticate.identified.identity`

  During authentication, AM records the type of user identified in an identity store. When this setting is enabled, AM uses these stored identities to decide which user to log in.

  This lets the authentication trees engine correctly resolve identities that have the same username.

  Learn more in the [custom node documentation](../auth-nodes/core-action.html) and [scripted decision node API](../am-scripting/scripting-api-node.html#action-set-outcome).

  Default: `true`

- `org.forgerock.am.auth.node.versioning.enable.v1.audit.detail`

  The node version is logged in the [Authentication log](../monitoring/audit-logging-ref.html#authentication-log-format) under the `AM-NODE-LOGIN-COMPLETED` event. When this property is set to `true`, `version` is logged for all node versions.

  If `false`, `version` is logged only for node versions greater than `1.0`.

  Default: `false`

* `org.forgerock.am.oauth2.aiagents.enabled`

  Set this property to `true` to enable AI agents in AM.

  Learn more in [Enable AI agents](../am-oauth2/ai-agents.html#enable-ai-agents).

  Default: `false`

---

---
title: Amster command-line tool
description: Use the Amster command-line tool to install, configure, and manage PingAM servers in DevOps environments
component: pingam
version: 8.1
page_id: pingam:setup:amster-tool
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/amster-tool.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Administration", "Tools", "User Interface"]
page_aliases: ["setup-guide:cli-tools.adoc", "cli-tools.adoc", "install-guide:install-openam-admin-tools.adoc"]
---

# Amster command-line tool

The Amster command-line interface (CLI) lets you install and configure an AM server.

Amster provides a lightweight CLI, ideal for use in DevOps processes, such as continuous integration and deployment. Amster manages an AM configuration over REST, so you can store AM server configuration as an artifact and import a stored configuration to set up an AM server.

Learn more in [Amster](../amster/preface.html).

---

---
title: Configure AM services
description: Configure global and realm-level services in PingAM, including authentication, federation, OAuth, SAML, and session management defaults
component: pingam
version: 8.1
page_id: pingam:setup:services-configuration
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/services-configuration.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Administration", "Configuration"]
page_aliases: ["reference:global-services-configuration.adoc", "reference:services-configuration.adoc", "setup-guide:services-configuration.adoc"]
section_ids:
  realm-androidkeyattestation: Android Key Attestation Service
  global-androidkeyattestation-realm-defaults: Realm defaults
  global-audit: Audit logging
  global-audit-global-attributes: Global attributes
  global-audit-realm-defaults: Realm defaults
  global-audit-secondary-config: Secondary configurations
  global-audit-secondary-config-jms: JMS
  global-audit-secondary-config-jms-general-handler-configuration: General handler configuration
  global-audit-secondary-config-jms-audit-event-handler-factory: Audit event handler factory
  global-audit-secondary-config-jms-jms-configuration: JMS configuration
  global-audit-secondary-config-jms-batch-events: Batch events
  global-audit-secondary-config-jsonstdout: JSONStdout
  global-audit-secondary-config-jsonstdout-general-handler-configuration: General handler configuration
  global-audit-secondary-config-jsonstdout-audit-event-handler-factory: Audit event handler factory
  global-audit-secondary-config-jsonstdout-json-configuration: JSON configuration
  global-audit-secondary-config-elasticsearch: Elasticsearch
  global-audit-secondary-config-syslog: Syslog
  global-audit-secondary-config-syslog-general-handler-configuration: General handler configuration
  global-audit-secondary-config-syslog-audit-event-handler-factory: Audit event handler factory
  global-audit-secondary-config-syslog-syslog-configuration: Syslog configuration
  global-audit-secondary-config-syslog-buffering: Buffering
  global-audit-secondary-config-csv: CSV
  global-audit-secondary-config-csv-general-handler-configuration: General handler configuration
  global-audit-secondary-config-csv-audit-event-handler-factory: Audit event handler factory
  global-audit-secondary-config-csv-csv-configuration: CSV configuration
  global-audit-secondary-config-csv-file-rotation: File rotation
  global-audit-secondary-config-csv-file-retention: File retention
  global-audit-secondary-config-csv-buffering: Buffering
  global-audit-secondary-config-csv-tamper-evident-configuration: Tamper Evident Configuration
  global-audit-secondary-config-jdbc: JDBC
  global-audit-secondary-config-jdbc-general-handler-configuration: General handler configuration
  global-audit-secondary-config-jdbc-audit-event-handler-factory: Audit event handler factory
  global-audit-secondary-config-jdbc-database-configuration: Database Configuration
  global-audit-secondary-config-jdbc-buffering: Buffering
  global-audit-secondary-config-json: JSON
  global-audit-secondary-config-json-general-handler-configuration: General handler configuration
  global-audit-secondary-config-json-audit-event-handler-factory: Audit event handler factory
  global-audit-secondary-config-json-json-configuration: JSON configuration
  global-audit-secondary-config-json-file-rotation: File rotation
  global-audit-secondary-config-json-file-retention: File retention
  global-audit-secondary-config-json-buffering: Buffering
  global-audit-secondary-config-splunk: Splunk
  global-baseurl: Base URL source
  global-baseurl-realm-defaults: Realm defaults
  global-federation-common: Common federation configuration
  global-federation-common-general-configuration: General configuration
  global-federation-common-implementation-classes: Implementation classes
  global-federation-common-algorithms: Algorithms
  global-federation-common-monitoring: Monitoring
  global-configurationversionservice: Configuration Version service
  global-corsservice: CORS service
  global-corsservice-configuration: Configuration
  global-corsservice-secondary-config: Secondary configurations
  global-corsservice-secondary-config-configuration: configuration
  cachemanager-service: Cache Manager service
  global-cachemanager-global-attributes: Global attributes
  cachemanager-service-configuration: Configuration
  cachemanager-service-secondary: Secondary configurations
  global-dashboard: Dashboard
  global-dashboard-realm-defaults: Realm defaults
  global-dashboard-secondary-config: Secondary configurations
  global-dashboard-secondary-config-instances: instances
  global-devicebindingservice: Device Binding service
  global-devicebindingservice-realm-defaults: Realm defaults
  global-deviceidservice: Device ID service
  global-deviceidservice-realm-defaults: Realm defaults
  global-deviceprofilesservice: Device Profiles service
  global-deviceprofilesservice-realm-defaults: Realm defaults
  global-email: Email service
  global-email-realm-defaults: Realm defaults
  global-email-secondary-config: Secondary configurations
  global-email-secondary-config-ms: Microsoft Graph API
  global-email-secondary-config-smtp: SMTP
  global-datastoreservice: External datastores
  global-datastoreservice-realm-defaults: Realm defaults
  global-datastoreservice-secondary-config: Secondary configurations
  global-datastoreservice-secondary-config-config: config
  global-authenticatoroathservice: ForgeRock Authenticator (OATH) service
  global-authenticatoroathservice-realm-defaults: Realm defaults
  global-authenticatorpushservice: ForgeRock Authenticator (Push) service
  global-authenticatorpushservice-realm-defaults: Realm defaults
  global-globalization: Globalization settings
  global-globalization-global-attributes: Global attributes
  global-globalization-realm-defaults: Realm defaults
  global-googlecloudserviceaccountservice: Google Cloud platform service accounts
  global-googlecloudserviceaccountservice-secondary-config: Secondary configurations
  global-googlecloudserviceaccountservice-secondary-config-serviceaccounts: serviceAccounts
  global-httpclient: Http Client service
  global-httpclient-realm-defaults: Realm defaults
  global-httpclient-secondary-config: Secondary configurations
  global-httpclient-secondary-config-configuration: Configuration
  global-httpclient-secondary-config-tlsconfiguration: TLS Configuration
  httpclient-secondary-config-timeouts: Timeouts
  httpclient-secondary-config-proxy: Proxy Configuration
  global-identity-assertion: Identity Assertion service
  global-identity-assertion-realm-defaults: Realm defaults
  global-identity-assertion-secondary-config: Secondary configurations
  global-idm-integration: IDM Provisioning
  global-iot: IoT service
  global-iot-realm-defaults: Realm defaults
  global-security: Legacy User Self-Service
  global-security-realm-defaults: Realm defaults
  global-logging: Logging
  global-logging-general: General
  global-logging-file: File
  global-logging-database: Database
  global-logging-syslog: Syslog
  global-monitoring: Monitoring
  global-monitoring-configuration: Configuration
  global-monitoring-secondary-config: Secondary configurations
  global-monitoring-secondary-config-crest: crest
  global-monitoring-secondary-config-graphite: graphite
  global-monitoring-secondary-config-prometheus: prometheus
  global-federation-multi: Multi-federation protocol
  global-naming: Naming
  global-naming-general-configuration: General configuration
  global-naming-federation-configuration: Federation configuration
  global-naming-endpoint-configuration: Endpoint configuration
  global-oauth-oidc: OAuth2 provider
  global-oauth-oidc-global-attributes: Global attributes
  global-oauth-oidc-core: Core
  global-oauth-oidc-advanced: Advanced
  global-oauth-oidc-client-dynamic-registration: Client Dynamic Registration
  global-oauth-oidc-openid-connect: OpenID Connect
  global-oauth-oidc-advanced-openid-connect: Advanced OpenID Connect
  global-oauth-oidc-device-flow: Device Flow
  global-oauth-oidc-consent: Consent
  global-oauth-oidc-ciba: CIBA
  global-oauth-ai-agents: AI Agents
  global-oauth-oidc-plugins: Plugins
  realm-pingone-worker-service: PingOne Worker service
  configuration: Configuration
  realm-pingone-worker-service-secondary-config: Secondary Configurations
  test-connection: Test the connection
  global-platform: Platform
  global-policyconfiguration: Policy configuration
  global-policyconfiguration-global-attributes: Global attributes
  global-policyconfiguration-realm-defaults: Realm defaults
  global-pushnotification: Push Notification service
  global-pushnotification-realm-defaults: Realm defaults
  global-radiusserverservice: RADIUS server
  global-radiusserverservice-configuration: Configuration
  global-radiusserverservice-secondary-config: Secondary configurations
  global-radiusserverservice-secondary-config-radiusclient: radiusClient
  global-rest: REST APIs
  global-remoteconsentservice: Remote Consent service
  global-remoteconsentservice-realm-defaults: Realm defaults
  global-federation-saml2soapbinding: SAML 2.0 SOAP binding
  global-saml2: SAML 2.0 service configuration
  global-scripting: Scripting
  global-scripting-configuration: Configuration
  global-scripting-secondary-config: Secondary configurations
  global-scripting-secondary-config-configuration: Configuration
  global-scripting-secondary-config-defaultscripts: Default Scripts
  global-scripting-secondary-config-secondaryconfig: Secondary Configurations
  global-scripting-secondary-engineconfiguration: engineConfiguration
  global-session: Session
  global-session-general: General
  global-session-session-search: Session search
  global-session-session-property-change-notifications: Session property change notifications
  global-session-session-quotas: Session quotas
  global-session-client-based-sessions: Client-side sessions
  global-session-dynamic-attributes: Dynamic attributes
  global-amsessionpropertywhitelist: Session Property Whitelist service
  global-amsessionpropertywhitelist-realm-defaults: Realm defaults
  global-socialauthentication: Social authentication implementations
  global-socialidentityproviders: Social Identity Provider service
  global-socialidentityproviders-realm-defaults: Realm defaults
  global-socialidentityproviders-secondary-config: Secondary configurations
  global-transaction: Transaction Authentication service
  global-transaction-realm-defaults: Realm defaults
  global-uma: UMA provider
  global-uma-global: Global Attributes
  global-uma-general: General
  global-uma-claims-gathering: Claims gathering
  global-user: User
  global-user-dynamic-attributes: Dynamic attributes
  global-selfservice: User Self-Service
  global-selfservice-general-configuration: General configuration
  global-selfservice-user-registration: User registration
  global-selfservice-forgotten-password: Forgotten password
  global-selfservice-forgotten-username: Forgotten username
  global-selfservice-profile-management: Profile management
  global-selfservice-advanced-configuration: Advanced configuration
  global-selfservicetrees: Self-Service trees
  global-selfservicetrees-realm-defaults: Realm defaults
  global-validation: Validation service
  global-validation-global-attributes: Global attributes
  global-validation-realm-defaults: Realm defaults
  webauthn-metadata-service: WebAuthn Metadata service
  global-authenticatorwebauthnservice: WebAuthn Profile Encryption service
  global-authenticatorwebauthnservice-realm-defaults: Realm defaults
---

# Configure AM services

You can configure AM services in two places:

* Under Configure > Global Services, you can set defaults for a range of AM services. These services affect all the realms in AM.

* Under Realms > *realm name* > Services, you can enable, remove, or configure different services for the realm.

## Android Key Attestation Service

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Certificate revocation status list URL

  The URL to retrieve the certificate revocation status list (CRL).

  Keys are checked against the revocation status list to ensure they have not been revoked or suspended.

  Keys can be revoked for a number of reasons, including mishandling or suspected extraction by an attacker.

  Defaults to the list maintained by Google at <https://android.googleapis.com/attestation/status>.

* Google hardware attestation root certificate URL

  The URL for retrieving the Google hardware attestation root certificates.

  Refer to [Verifying hardware-backed key pairs with Key Attestation](https://developer.android.com/training/articles/security-key-attestation#root_certificate) in the Android developer documentation.

  If you don't provide a URL, you must map the certificate using the secret label `am.services.attestation.google.public.key`.

  For more information, refer to [Map and rotate secrets](../security/secret-mapping.html).

* Cache duration (hours)

  The number of hours to cache the certificate revocation status list and Google hardware attestation root certificate.

  Defaults to one day (`24`).

  Specify `0` to prevent caching.

## Audit logging

`amster` service name: `AuditLogging`

### Global attributes

The following settings appear on the Global Attributes tab:

* Audit logging

  Enable audit logging in AM.

  Default value: `true`

  `amster` attribute: `auditEnabled`

* Field whitelist filters

  AM has a predefined allowlist that only records values that do not contain sensitive information. Use this property to allowlist fields in addition to the built-in list.

  Each field filter should be provided using a JSON Pointer-like syntax which is prefixed with the event's topic. The topic will be one of `access`, `activity`, `authentication`, or `config`.

  For example, to record the values of the `Accept-Language` HTTP header in *access* events, the pointer is `/access/http/request/headers/accept-language`.

  `amster` attribute: `whitelistFieldFilters`

* Field blacklist filters

  Denylist filters can be used to remove audit event fields which are allowlisted by default. These are fields which are safe to log but which you have decided are not necessary for your requirements.

  Each field filter should be provided using a JSON Pointer-like syntax which is prefixed with the event's topic. The topic will be one of `access`, `activity`, `authentication`, or `config`.

  For example, you might want to filter out surnames by hiding the `sn` field from *activity* events. To do so, add the following pointers to the Field blacklist filters list:

  * `/activity/before/sn`

  * `/activity/after/sn`

  `amster` attribute: `blacklistFieldFilters`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Audit logging

  Enable audit logging in AM.

  Default value: `true`

  `amster` attribute: `auditEnabled`

* Field whitelist filters

  AM has a predefined allowlist that only records values that do not contain sensitive information. Use this property to allowlist fields in addition to the built-in list.

  Each field filter should be provided using a JSON Pointer-like syntax which is prefixed with the event's topic. The topic will be one of `access`, `activity`, `authentication`, or `config`.

  For example, to record the values of the `Accept-Language` HTTP header in *access* events, the pointer is `/access/http/request/headers/accept-language`.

  `amster` attribute: `whitelistFieldFilters`

* Field blacklist filters

  Denylist filters can be used to remove audit event fields which are allowlisted by default. These are fields which are safe to log but which you have decided are not necessary for your requirements.

  Each field filter should be provided using a JSON Pointer-like syntax which is prefixed with the event's topic. The topic will be one of `access`, `activity`, `authentication`, or `config`.

  For example, you might want to filter out surnames by hiding the `sn` field from *activity* events. To do so, add the following pointers to the Field blacklist filters list:

  * `/activity/before/sn`

  * `/activity/after/sn`

  `amster` attribute: `blacklistFieldFilters`

### Secondary configurations

This service has the following secondary configurations.

#### JMS

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | The JMS audit event handler is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

A configured secondary instance of the JMS type has the following tabs:

##### General handler configuration

The General Handler Configuration tab contains the following secondary configuration properties:

* Enabled

  Enables or disables an audit event handler.

  Default value: `true`

  `amster` attribute: `enabled`

* Topics

  List of topics handled by an audit event handler.

  Default value:

  ```
  access
  activity
  config
  authentication
  ```

  `amster` attribute: `topics`

##### Audit event handler factory

The Audit Event Handler Factory tab contains the following secondary configuration properties:

* Factory Class Name

  The fully qualified class name of the factory responsible for creating the Audit Event Handler. The class must implement `org.forgerock.openam.audit.AuditEventHandlerFactory`.

  Default value: `org.forgerock.openam.audit.events.handlers.JmsAuditEventHandlerFactory`

  `amster` attribute: `handlerFactory`

##### JMS configuration

The JMS Configuration tab contains the following secondary configuration properties:

* Delivery Mode

  Specifies whether JMS messages used to transmit audit events use persistent or non-persistent delivery.

  With persistent delivery, the JMS provider ensures that messages are not lost in transit in case of a provider failure by logging messages to storage when they are sent.

  Specify the delivery mode as persistent if it is unacceptable for delivery of audit events to be lost in JMS transit. If the possible loss of audit events is acceptable, choose non-persistent delivery, which provides better performance.

  Default value: `NON_PERSISTENT`

  `amster` attribute: `deliveryMode`

* Session Mode

  Specifies the JMS session acknowledgement mode.

  The following values are supported:

  * `AUTO`. Auto mode guarantees once-only delivery of JMS messages used to transmit audit events.

  * `CLIENT`. Client mode does not ensure delivery.

  * `DUPS_OK`. Duplicates OK mode ensures that messages are delivered at least once.

  Use the default setting unless your JMS broker implementation requires otherwise. See your broker documentation for more information.

  Default value: `AUTO`

  `amster` attribute: `sessionMode`

* JNDI Context Properties

  Specifies JNDI properties that AM uses to connect to the JMS message broker to which AM will publish audit events.

  AM acts as a JMS client, using a JMS connection factory to connect to your JMS message broker. In order for AM to connect to the broker, the JNDI context properties must conform to those needed by the broker. See the documentation for your JMS message broker for required values.

  The default properties are example properties for connecting to Apache ActiveMQ.

  Default value:

  ```
  {
      &quot;java.naming.factory.initial&quot;: &quot;org.apache.activemq.jndi.ActiveMQInitialContextFactory&quot;,
      &quot;topic.audit&quot;: &quot;audit&quot;,
      &quot;java.naming.provider.url&quot;: &quot;tcp://localhost:61616&quot;
  }
  ```

  `amster` attribute: `jndiContextProperties`

* JMS Topic Name

  JNDI lookup name for the JMS topic

  Default value: `audit`

  `amster` attribute: `jndiTopicName`

* JMS Connection Factory Name

  Specifies the JNDI lookup name for the connection factory exposed by your JMS message broker. AM performs a JNDI lookup on this name to locate your broker's connection factory.

  See the documentation for your JMS message broker for the required value.

  The default is the connection factory name for Apache ActiveMQ.

  Default value: `ConnectionFactory`

  `amster` attribute: `jndiConnectionFactoryName`

##### Batch events

The Batch Events tab contains the following secondary configuration properties:

* Capacity

  Maximum event count in the batch queue; additional events are dropped.

  Default value: `1000`

  `amster` attribute: `batchCapacity`

* Max Batched

  Maximum number of events per batch.

  Default value: `100`

  `amster` attribute: `maxBatchedEvents`

* Writing Interval

  The interval (in seconds) for reading events from the buffer to transmit via jms.

  Default value: `10`

  `amster` attribute: `pollTimeoutSec`

#### JSONStdout

A configured secondary instance of the JSONStdout type has the following tabs:

##### General handler configuration

The General Handler Configuration tab contains the following secondary configuration properties:

* Enabled

  Enables or disables an audit event handler.

  Default value: `true`

  `amster` attribute: `enabled`

* Topics

  List of topics handled by an audit event handler.

  Default value:

  ```
  access
  activity
  config
  authentication
  ```

  `amster` attribute: `topics`

##### Audit event handler factory

The Audit Event Handler Factory tab contains the following secondary configuration properties:

* Factory Class Name

  The fully qualified class name of the factory responsible for creating the Audit Event Handler. The class must implement `org.forgerock.openam.audit.AuditEventHandlerFactory`.

  Default value: `org.forgerock.openam.audit.events.handlers.JsonStdoutAuditEventHandlerFactory`

  `amster` attribute: `handlerFactory`

##### JSON configuration

The JSON Configuration tab contains the following secondary configuration properties:

* ElasticSearch JSON Format Compatible

  JSON format should be transformed to be compatible with ElasticSearch format restrictions.

  Default value: `false`

  `amster` attribute: `elasticsearchCompatible`

#### Elasticsearch

This configuration was used only for the deprecated Elasticsearch audit handler and is no longer documented.

#### Syslog

|   |                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Syslog audit event handler is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

A configured secondary instance of the `Syslog` type has the following tabs:

##### General handler configuration

The General Handler Configuration tab contains the following secondary configuration properties:

* Enabled

  Enables or disables an audit event handler.

  Default value: `true`

  `amster` attribute: `enabled`

* Topics

  List of topics handled by an audit event handler.

  Default value:

  ```
  access
  activity
  config
  authentication
  ```

  `amster` attribute: `topics`

##### Audit event handler factory

The Audit Event Handler Factory tab contains the following secondary configuration properties:

* Factory Class Name

  The fully qualified class name of the factory responsible for creating the Audit Event Handler. The class must implement `org.forgerock.openam.audit.AuditEventHandlerFactory`.

  Default value: `org.forgerock.openam.audit.events.handlers.SyslogAuditEventHandlerFactory`

  `amster` attribute: `handlerFactory`

##### Syslog configuration

The Syslog Configuration tab contains the following secondary configuration properties:

* Server hostname

  Host name or IP address of receiving syslog server.

  `amster` attribute: `host`

* Server port

  Port number of receiving syslog server.

  `amster` attribute: `port`

* Transport Protocol

  Default value: `TCP`

  `amster` attribute: `transportProtocol`

* Connection timeout

  Timeout for connecting to syslog server, in seconds.

  `amster` attribute: `connectTimeout`

* Facility

  Syslog facility value to apply to all events.

  Default value: `USER`

  `amster` attribute: `facility`

##### Buffering

The Buffering tab contains the following secondary configuration properties:

* Buffering Enabled

  Enables or disables audit event buffering.

  Default value: `true`

  `amster` attribute: `bufferingEnabled`

* Buffer Size

  Maximum number of events that can be buffered (default/minimum: 5000)

  Default value: `5000`

  `amster` attribute: `bufferingMaxSize`

#### CSV

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | The CSV audit event handler is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

A configured secondary instance of the CSV type has the following tabs:

##### General handler configuration

The General Handler Configuration tab contains the following secondary configuration properties:

* Enabled

  Enables or disables an audit event handler.

  Default value: `true`

  `amster` attribute: `enabled`

* Topics

  List of topics handled by an audit event handler.

  Default value:

  ```
  access
  activity
  config
  authentication
  ```

  `amster` attribute: `topics`

##### Audit event handler factory

The Audit Event Handler Factory tab contains the following secondary configuration properties:

* Factory Class Name

  The fully qualified class name of the factory responsible for creating the Audit Event Handler. The class must implement `org.forgerock.openam.audit.AuditEventHandlerFactory`.

  Default value: `org.forgerock.openam.audit.events.handlers.CsvAuditEventHandlerFactory`

  `amster` attribute: `handlerFactory`

##### CSV configuration

The CSV Configuration tab contains the following secondary configuration properties:

* Log Directory

  Directory in which to store audit log CSV files.

  Default value: `%BASE_DIR%/var/audit/`

  `amster` attribute: `location`

##### File rotation

The File Rotation tab contains the following secondary configuration properties:

* Rotation Enabled

  Enables and disables audit file rotation.

  Default value: `true`

  `amster` attribute: `rotationEnabled`

* Maximum File Size

  Maximum size, in bytes, which an audit file can grow to before rotation is triggered. A negative or zero value indicates this policy is disabled.

  Default value: `100000000`

  `amster` attribute: `rotationMaxFileSize`

* File Rotation Prefix

  Prefix to prepend to audit files when rotating audit files.

  `amster` attribute: `rotationFilePrefix`

* File Rotation Suffix

  Suffix to append to audit files when they are rotated. Suffix should be a timestamp.

  Default value: `-yyyy.MM.dd-HH.mm.ss`

  `amster` attribute: `rotationFileSuffix`

* Rotation Interval

  Interval to trigger audit file rotations, in seconds. A negative or zero value disables this feature.

  Default value: `-1`

  `amster` attribute: `rotationInterval`

* Rotation Times

  Durations after midnight to trigger file rotation, in seconds.

  `amster` attribute: `rotationTimes`

##### File retention

The File Retention tab contains the following secondary configuration properties:

* Maximum Number of Historical Files

  Maximum number of backup audit files allowed. A value of `-1` disables pruning of old history files.

  Default value: `1`

  `amster` attribute: `retentionMaxNumberOfHistoryFiles`

* Maximum Disk Space

  The maximum amount of disk space the audit files can occupy, in bytes. A negative or zero value indicates this policy is disabled.

  Default value: `-1`

  `amster` attribute: `retentionMaxDiskSpaceToUse`

* Minimum Free Space Required

  Minimum amount of disk space required, in bytes, on the system where audit files are stored. A negative or zero value indicates this policy is disabled.

  Default value: `-1`

  `amster` attribute: `retentionMinFreeSpaceRequired`

##### Buffering

The Buffering tab contains the following secondary configuration properties:

* Buffering Enabled

  Enables or disables buffering.

  Default value: `true`

  `amster` attribute: `bufferingEnabled`

* Flush Each Event Immediately

  Performance may be improved by writing all buffered events before flushing.

  Default value: `false`

  `amster` attribute: `bufferingAutoFlush`

##### Tamper Evident Configuration

The Tamper Evident Configuration tab contains the following secondary configuration properties:

* Is Enabled

  Enables the CSV tamper evident feature.

  Default value: `false`

  `amster` attribute: `securityEnabled`

* Certificate Store Location

  Path to Java keystore.

  Default value: `%BASE_DIR%/var/audit/Logger.jks`

  `amster` attribute: `securityFilename`

* Certificate Store Password

  Password for Java keystore.

  `amster` attribute: `securityPassword`

* Signature Interval

  Signature generation interval, in seconds.

  Default value: `900`

  `amster` attribute: `securitySignatureInterval`

#### JDBC

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | The JDBC audit event handler is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

A configured secondary instance of the JDBC type has the following tabs:

##### General handler configuration

The General Handler Configuration tab contains the following secondary configuration properties:

* Enabled

  Enables or disables an audit event handler.

  Default value: `true`

  `amster` attribute: `enabled`

* Topics

  List of topics handled by an audit event handler.

  Default value:

  ```
  access
  activity
  config
  authentication
  ```

  `amster` attribute: `topics`

##### Audit event handler factory

The Audit Event Handler Factory tab contains the following secondary configuration properties:

* Factory Class Name

  The fully qualified class name of the factory responsible for creating the Audit Event Handler. The class must implement `org.forgerock.openam.audit.AuditEventHandlerFactory`.

  Default value: `org.forgerock.openam.audit.events.handlers.JdbcAuditEventHandlerFactory`

  `amster` attribute: `handlerFactory`

##### Database Configuration

The Database Configuration tab contains the following secondary configuration properties:

* Database Type

  Select the database to use for logging audit events.

  Identifies the database in use, for example MySQL, Oracle, or SQL.

  Default value: `oracle`

  `amster` attribute: `databaseType`

* JDBC Database URL

  URL of the JDBC database.

  `amster` attribute: `jdbcUrl`

* JDBC Driver

  Fully qualified JDBC driver class name.

  `amster` attribute: `driverClassName`

* Database Username

  Specifies the username to access the database server.

  `amster` attribute: `username`

* Database Password

  Specifies the password to access the database server.

  `amster` attribute: `password`

* Connection Timeout (seconds)

  Specifies the maximum wait time before failing the connection, in seconds.

  Default value: `30`

  `amster` attribute: `connectionTimeout`

* Maximum Connection Idle Timeout (seconds)

  Specifies the maximum idle time before the connection is closed, in seconds.

  Default value: `600`

  `amster` attribute: `idleTimeout`

* Maximum Connection Time (seconds)

  Specifies the maximum time a JDBC connection can be open, in seconds.

  Default value: `1800`

  `amster` attribute: `maxLifetime`

* Minimum Idle Connections

  Specifies the minimum number of idle connections in the connection pool.

  Default value: `10`

  `amster` attribute: `minIdle`

* Maximum Connections

  Specifies the maximum number of connections in the connection pool.

  Default value: `10`

  `amster` attribute: `maxPoolSize`

##### Buffering

The Buffering tab contains the following secondary configuration properties:

* Buffering Enabled

  Enables or disables audit event buffering.

  Default value: `true`

  `amster` attribute: `bufferingEnabled`

* Buffer Size (number of events)

  Size of the queue where events are buffered before they are written to the database.

  This queue has to be big enough to store all incoming events that have not yet been written to the database.

  If the queue reaches capacity, the process will block until a write occurs.

  Default value: `100000`

  `amster` attribute: `bufferingMaxSize`

* Write Interval

  Specifies the interval (seconds) at which buffered events are written to the database.

  Default value: `5`

  `amster` attribute: `bufferingWriteInterval`

* Writer Threads

  Specifies the number of threads used to write the buffered events.

  Default value: `1`

  `amster` attribute: `bufferingWriterThreads`

* Max Batched Events

  Specifies the maximum number of batched statements the database can support per connection.

  Default value: `100`

  `amster` attribute: `bufferingMaxBatchedEvents`

#### JSON

A configured secondary instance of the JSON type has the following tabs:

##### General handler configuration

The General Handler Configuration tab contains the following secondary configuration properties:

* Enabled

  Enables or disables an audit event handler.

  Default value: `true`

  `amster` attribute: `enabled`

* Topics

  List of topics handled by an audit event handler.

  Default value:

  ```
  access
  activity
  config
  authentication
  ```

  `amster` attribute: `topics`

##### Audit event handler factory

The Audit Event Handler Factory tab contains the following secondary configuration properties:

* Factory Class Name

  The fully qualified class name of the factory responsible for creating the Audit Event Handler. The class must implement `org.forgerock.openam.audit.AuditEventHandlerFactory`.

  Default value: `org.forgerock.openam.audit.events.handlers.JsonAuditEventHandlerFactory`

  `amster` attribute: `handlerFactory`

##### JSON configuration

The JSON Configuration tab contains the following secondary configuration properties:

* Log Directory

  Directory in which to store audit log JSON files.

  Default value: `%BASE_DIR%/var/audit/`

  `amster` attribute: `location`

* ElasticSearch JSON Format Compatible

  JSON format should be transformed to be compatible with ElasticSearch format restrictions.

  Default value: `false`

  `amster` attribute: `elasticsearchCompatible`

* File Rotation Retention Check Interval

  Interval to check time-based file rotation policies, in seconds.

  Default value: `5`

  `amster` attribute: `rotationRetentionCheckInterval`

##### File rotation

The File Rotation tab contains the following secondary configuration properties:

* Rotation Enabled

  Enables and disables audit file rotation.

  Default value: `true`

  `amster` attribute: `rotationEnabled`

* Maximum File Size

  Maximum size, in bytes, which an audit file can grow to before rotation is triggered. A negative or zero value indicates this policy is disabled.

  Default value: `100000000`

  `amster` attribute: `rotationMaxFileSize`

* File Rotation Prefix

  Prefix to prepend to audit files when rotating audit files.

  `amster` attribute: `rotationFilePrefix`

* File Rotation Suffix

  Suffix to append to audit files when they are rotated. Suffix should be a timestamp.

  Default value: `-yyyy.MM.dd-HH.mm.ss`

  `amster` attribute: `rotationFileSuffix`

* Rotation Interval

  Interval to trigger audit file rotations, in seconds. A negative or zero value disables this feature.

  Default value: `-1`

  `amster` attribute: `rotationInterval`

* Rotation Times

  Durations after midnight to trigger file rotation, in seconds.

  `amster` attribute: `rotationTimes`

##### File retention

The File Retention tab contains the following secondary configuration properties:

* Maximum Number of Historical Files

  Maximum number of backup audit files allowed. A value of `-1` disables pruning of old history files.

  Default value: `1`

  `amster` attribute: `retentionMaxNumberOfHistoryFiles`

* Maximum Disk Space

  The maximum amount of disk space the audit files can occupy, in bytes. A negative or zero value indicates this policy is disabled.

  Default value: `-1`

  `amster` attribute: `retentionMaxDiskSpaceToUse`

* Minimum Free Space Required

  Minimum amount of disk space required, in bytes, on the system where audit files are stored. A negative or zero value indicates this policy is disabled.

  Default value: `-1`

  `amster` attribute: `retentionMinFreeSpaceRequired`

##### Buffering

The Buffering tab contains the following secondary configuration properties:

* Batch Size

  Maximum number of events that can be buffered (default/minimum: 100000)

  Default value: `100000`

  `amster` attribute: `bufferingMaxSize`

* Write interval

  Interval at which buffered events are written to a file, in milliseconds.

  Default value: `5`

  `amster` attribute: `bufferingWriteInterval`

#### Splunk

This configuration was used only for the deprecated Splunk audit handler and is no longer documented.

## Base URL source

`amster` service name: `BaseUrlSource`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Base URL Source

  Specifies how the base URL is generated.

  The following values are supported:

  * **Extension class** (`EXTENSION_CLASS`). The extension class returns a base URL from a provided HttpServletRequest. In the Extension class name field, enter `org.forgerock.openam.services.baseurl.BaseURLProvider`.

  * **Fixed value** (`FIXED_VALUE`). The base URL is retrieved from the value specified in the Fixed value base URL field.

  * **Forwarded header** (`FORWARDED_HEADER`). The base URL is retrieved from a forwarded header field in the HTTP request. The Forwarded HTTP header field is standardized and specified in [RFC7239](https://www.rfc-editor.org/info/rfc7239).

  * **Host/protocol from incoming request** (`REQUEST_VALUES`). The hostname, server name, and port are retrieved from the incoming HTTP request.

  * **X-Forwarded-\* headers** (`X_FORWARDED_HEADERS`). The base URL is retrieved from non-standard header fields, such as `X-Forwarded-For`, `X-Forwarded-By`, `X-Forwarded-Proto`, `X-Forwarded-Host` and `X-Forwarded-Port`.

    If the `X-Forwarded-Proto` header is not provided, the server uses a fallback scheme, based on the URI of the request.

    If multiple `X-Forwarded-Host` headers are specified, the outermost proxy host is used.

  Default value: `REQUEST_VALUES`

  `amster` attribute: `source`

* Fixed value base URL

  If `Fixed value` is selected as the Base URL source, enter the base URL in the Fixed value base URL field.

  `amster` attribute: `fixedValue`

* Extension class name

  If `Extension class` is selected as the Base URL source, enter `org.forgerock.openam.services.baseurl.BaseURLProvider` in the Extension class name field.

  `amster` attribute: `extensionClassName`

* Context path

  Specifies the context path for the base URL.

  If provided, the base URL includes the deployment context path appended to the calculated URL.

  For example, `/am`.

  Default value: `/openam`

  `amster` attribute: `contextPath`

## Common federation configuration

`amster` service name: `CommonFederationConfiguration`

### General configuration

The following settings appear on the General Configuration tab:

* Maximum allowed content length

  The maximum content length allowed in federation communications, in bytes.

  Default value: `20480`

  `amster` attribute: `maxContentLength`

* Check presence of certificates

  Enable checking of certificates against local copy

  Whether to verify that the partner's signing certificate included in the Federation XML document is the same as the one stored in that partner's metadata.

  The possible values for this property are:

  * `off`. Disabled

  * `on`. Enabled

  Default value: `on`

  `amster` attribute: `certificateChecking`

* SAML Error Page URL

  AM redirects users here when an error occurs in the SAML2 engine.

  Both relative and absolute URLs are supported. Users are redirected to an absolute URL using the configured HTTP Binding whereas relative URLs are displayed within the request.

  Default value: `/saml2/jsp/saml2error.jsp`

  `amster` attribute: `samlErrorPageUrl`

* SAML Error Page HTTP Binding

  The possible values are HTTP-Redirect or HTTP-POST.

  Default value: `HTTP-POST`

  `amster` attribute: `samlErrorPageHttpBinding`

### Implementation classes

The following settings appear on the **Implementation Classes** tab:

* Datastore SPI implementation class

  The Federation system uses this class to get/set user profile attributes.

  The default implementation uses the identity store APIs to access user profile attributes. A custom implementation must implement the `com.sun.identity.plugin.datastore.DataStoreProvider` interface.

  Default value: `com.sun.identity.plugin.datastore.impl.IdRepoDataStoreProvider`

  `amster` attribute: `datastoreClass`

* Root URL provider SPI implementation class

  The Federation system uses this class to get the root URL of the AM deployment.

  The default implementation uses the Root URL APIs to access the AM instance root url. A custom implementation must implement the `org.forgerock.openam.federation.plugin.rooturl.RootUrlProvider` interface.

  Default value: `org.forgerock.openam.federation.plugin.rooturl.impl.FmRootUrlProvider`

  `amster` attribute: `rootUrlProviderClass`

* ConfigurationInstance SPI implementation class

  The Federation system uses this class to fetch service configuration.

  The default implementation uses the SMS APIs to access service configuration. A custom implementation must implement the `com.sun.identity.plugin.configuration.ConfigurationInstance` interface.

  Default value: `com.sun.identity.plugin.configuration.impl.ConfigurationInstanceImpl`

  `amster` attribute: `configurationClass`

* Logger SPI implementation class

  The Federation system uses this class to record log entries.

  The default implementation uses the Logging APIs to record log entries. A custom implementation must implement the `com.sun.identity.plugin.log.Logger` interface.

  Default value: `com.sun.identity.plugin.log.impl.LogProvider`

  `amster` attribute: `loggerClass`

* SessionProvider SPI implementation class

  The Federation system uses this class to interface with the session service.

  The default implementation uses the standard authentication and SSO APIs to access the session service. A custom implementation must implement the `com.sun.identity.plugin.session.SessionProvider` interface.

  Default value: `com.sun.identity.plugin.session.impl.FMSessionProvider`

  `amster` attribute: `sessionProviderClass`

* PasswordDecoder SPI implementation class

  The Federation system uses this class to decode password encoded by AM.

  The default implementation uses the internal AM decryption API to decode passwords. A custom implementation must implement the `com.sun.identity.saml.xmlsig.PasswordDecoder` interface.

  Default value: `com.sun.identity.saml.xmlsig.FMPasswordDecoder`

  `amster` attribute: `passwordDecoderClass`

* SignatureProvider SPI implementation class

  The Federation system uses this class to digitally sign SAML documents.

  The default implementation uses the XERCES APIs to sign the documents. A custom implementation must implement the `com.sun.identity.saml.xmlsig.SignatureProvider` interface.

  Default value: `com.sun.identity.saml.xmlsig.AMSignatureProvider`

  `amster` attribute: `signatureProviderClass`

* KeyProvider SPI implementation class

  The Federation system uses this class to provide access to the underlying Java keystore.

  The default implementation uses the Java Cryptographic Engine to provide access to the Java keystore. A custom implementation must implement the `com.sun.identity.saml.xmlsig.KeyProvider` interface.

  Default value: `com.sun.identity.saml.xmlsig.JKSKeyProvider`

  `amster` attribute: `keyProviderClass`

### Algorithms

The following settings appear on the **Algorithms** tab:

* XML canonicalization algorithm

  The algorithm used to canonicalize XML documents.

  The possible values for this property are:

  * `http://www.w3.org/2001/10/xml-exc-c14n#`

  * `http://www.w3.org/2001/10/xml-exc-c14n#WithComments`

  * `http://www.w3.org/TR/2001/REC-xml-c14n-20010315`

  * `http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments`

  Default value: `http://www.w3.org/2001/10/xml-exc-c14n#`

  `amster` attribute: `cannonicalizationAlgorithm`

* XML signature algorithm

  The algorithm used to sign XML documents.

  The possible values for this property are:

  * `http://www.w3.org/2000/09/xmldsig#rsa-sha1`

  * `http://www.w3.org/2000/09/xmldsig#hmac-sha1`

  * `http://www.w3.org/2001/04/xmldsig-more#rsa-md5`

  * `http://www.w3.org/2001/04/xmldsig-more#rsa-ripemd160`

  * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`

  * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha384`

  * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha512`

  * `http://www.w3.org/2001/04/xmldsig-more#hmac-md5`

  * `http://www.w3.org/2001/04/xmldsig-more#hmac-ripemd160`

  * `http://www.w3.org/2001/04/xmldsig-more#hmac-sha256`

  * `http://www.w3.org/2001/04/xmldsig-more#hmac-sha384`

  * `http://www.w3.org/2001/04/xmldsig-more#hmac-sha512`

  Default value: `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`

  `amster` attribute: `signatureAlgorithm`

* XML digest algorithm

  The default digest algorithm to use in signing XML.

  The possible values for this property are:

  * `http://www.w3.org/2000/09/xmldsig#sha1`

  * `http://www.w3.org/2001/04/xmlenc#sha256`

  * `http://www.w3.org/2001/04/xmlenc#sha512`

  * `http://www.w3.org/2001/04/xmldsig-more#sha384`

  Default value: `http://www.w3.org/2001/04/xmlenc#sha256`

  `amster` attribute: `DigestAlgorithm`

* Query String signature algorithm (RSA)

  The default signature algorithm to use for RSA keys.

  The possible values for this property are:

  * `http://www.w3.org/2000/09/xmldsig#rsa-sha1`

  * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`

  * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha384`

  * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha512`

  Default value: `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`

  `amster` attribute: `QuerySignatureAlgorithmRSA`

* Query String signature algorithm (DSA)

  The default signature algorithm to use for DSA keys.

  This property can only take the following value:

  * `http://www.w3.org/2009/xmldsig11#dsa-sha256`

  Default value: `http://www.w3.org/2009/xmldsig11#dsa-sha256`

  `amster` attribute: `QuerySignatureAlgorithmDSA`

* Query String signature algorithm (EC)

  The default signature algorithm to use for EC keys.

  The possible values for this property are:

  * `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha1`

  * `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256`

  * `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384`

  * `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512`

  Default value: `http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512`

  `amster` attribute: `QuerySignatureAlgorithmEC`

* XML transformation algorithm

  The algorithm used to transform XML documents.

  The possible values for this property are:

  * `http://www.w3.org/2001/10/xml-exc-c14n#`

  * `http://www.w3.org/2001/10/xml-exc-c14n#WithComments`

  * `http://www.w3.org/TR/2001/REC-xml-c14n-20010315`

  * `http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments`

  * `http://www.w3.org/TR/1999/REC-xslt-19991116`

  * `http://www.w3.org/2000/09/xmldsig#base64`

  * `http://www.w3.org/TR/1999/REC-xpath-19991116`

  * `http://www.w3.org/2000/09/xmldsig#enveloped-signature`

  * `http://www.w3.org/TR/2001/WD-xptr-20010108`

  * `http://www.w3.org/2002/04/xmldsig-filter2`

  * `http://www.w3.org/2002/06/xmldsig-filter2`

  * `http://www.nue.et-inf.uni-siegen.de/~geuer-pollmann/#xpathFilter`

  Default value: `http://www.w3.org/2001/10/xml-exc-c14n#`

  `amster` attribute: `transformationAlgorithm`

* Mask Generation Function Algorithm

  Which MGF algorithm to use when encrypting the symmetric encryption key using RSA OAEP algorithm.

  The possible values for this property are:

  * `http://www.w3.org/2009/xmlenc11#mgf1sha1`

  * `http://www.w3.org/2009/xmlenc11#mgf1sha224`

  * `http://www.w3.org/2009/xmlenc11#mgf1sha256`

  * `http://www.w3.org/2009/xmlenc11#mgf1sha384`

  * `http://www.w3.org/2009/xmlenc11#mgf1sha512`

  Default value: `http://www.w3.org/2009/xmlenc11#mgf1sha256`

  `amster` attribute: `maskGenerationFunction`

* AES Key Wrap Algorithm

  The AES key wrap algorithm to use when the remote entity provider does not specify which key wrap algorithms it supports.

  The possible values for this property are:

  * `http://www.w3.org/2001/04/xmlenc#kw-aes128`

  * `http://www.w3.org/2001/04/xmlenc#kw-aes192`

  * `http://www.w3.org/2001/04/xmlenc#kw-aes256`

  Default value: `http://www.w3.org/2001/04/xmlenc#kw-aes256`

  `amster` attribute: `aesKeyWrapAlgorithm`

* RSA Key Transport Algorithm

  The possible values for this property are:

  * `http://www.w3.org/2001/04/xmlenc#rsa-1_5`

  * `http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p`

  * `http://www.w3.org/2009/xmlenc11#rsa-oaep`

  Default value: `http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p`

  `amster` attribute: `rsaKeyTransportAlgorithm`

### Monitoring

The following settings appear on the **Monitoring** tab:

* Monitoring Agent Provider Class

  The Federation system uses this class to gain access to the monitoring system.

  The default implementation uses the built-in AM monitoring system. A custom implementation must implement the `com.sun.identity.plugin.monitoring.FedMonAgent` interface.

  Default value: `com.sun.identity.plugin.monitoring.impl.AgentProvider`

  `amster` attribute: `monitoringAgentClass`

* Monitoring Provider Class for SAML2

  The SAML2 engine uses this class to gain access to the monitoring system.

  The default implementation uses the built-in AM monitoring system. A custom implementation must implement the `com.sun.identity.plugin.monitoring.FedMonSAML2Svc` interface.

  Default value: `com.sun.identity.plugin.monitoring.impl.FedMonSAML2SvcProvider`

  `amster` attribute: `monitoringSaml2Class`

## Configuration Version service

`amster` service name: `ConfigurationVersionService`

The following settings are available in this service:

* configurationCommit

  `amster` attribute: `configurationCommit`

* Configuration Version

  AM's configuration version

  Default value: `8.0.0.0`

  `amster` attribute: `configurationVersion`

## CORS service

`amster` service name: `CorsConfiguration`

### Configuration

The following settings appear on the Configuration tab:

* Enable the CORS filter

  If disable, no CORS headers will be added to responses.

  Default value: `true`

  `amster` attribute: `enabled`

### Secondary configurations

This service has the following secondary configurations.

#### configuration

* Enable the CORS filter

  If disable, no CORS headers will be added to responses.

  Default value: `false`

  `amster` attribute: `enabled`

* Accepted Origins

  The set of accepted origins.

  `amster` attribute: `acceptedOrigins`

* Accepted Methods

  The set of (non-simple) accepted methods, included in the pre-flight response in the header Access-Control-Allow-Methods.

  `amster` attribute: `acceptedMethods`

* Accepted Headers

  The set of (non-simple) accepted headers, included in the pre-flight response in the header Access-Control-Allow-Headers.

  `amster` attribute: `acceptedHeaders`

* Exposed Headers

  The set of headers to transmit in the header Access-Control-Expose-Headers.

  `amster` attribute: `exposedHeaders`

* Max Age

  The max age (in seconds) for caching, included in the pre-flight response in the header Access-Control-Max-Age.

  Default value: `0`

  `amster` attribute: `maxAge`

* Allow Credentials

  Whether to transmit the Access-Control-Allow-Credentials: true header in the response.

  Default value: `false`

  `amster` attribute: `allowCredentials`

## Cache Manager service

`amster` service name: `CacheManagerService`

### Global attributes

The following settings appear on the Global Attributes tab:

* Maximum memory per realm (MB)

  The maximum amount of memory (in megabytes) that the cache manager service can consume for each realm.

  Default: `20`

* Maximum memory per entry (KB)

  The maximum amount of memory (in kilobytes) that each cache entry can consume.

  Default: `5`

* Securely remove entries

  Enables or disables memory zeroization relating to cache entries on their removal. This ensures that entries are securely removed.

  Default: Enabled

### Configuration

* Enabled

  Enable the cache manager service. If not enabled, entries are computed but never stored, so that each entry is reloaded each time it's requested.

  Learn about using the cache manager service in [Cache script values](../am-scripting/cache-manager.html).

  Default value: Not enabled

### Secondary configurations

Configure instances of the cache manager service. You can create multiple caches within each realm. The total size for all caches in a realm is limited to 20MB, and each cache entry can't exceed 5KB.

* Loading Script

  The script that's used to load cache entries. The script type must be `Cache Loader`, and it should have a `load()` function, and optionally, a `reload()` function.

  Default value: `--- Select a script ---`

- Eviction Policy

  The eviction policy used to determine when to remove or reload entries from the cache.

  The possible values are as follows:

  * `Expire after access`: Entries expire and are removed from the cache after a period of inactivity determined by the Eviction Period. After this time, the cache `load()` function runs.

    Entries remain in the cache indefinitely if they're continuously accessed within this time.

  * `Expire after write`: After the eviction period, entries expire and are removed from the cache. If the cache entry is accessed again, the `load()` function runs.

  * `Refresh after write`: After the eviction period, the `reload()` function runs.

  * `Never`: The cache entry isn't set to expire.

  Default value: `Expire after write`

- Duration Unit

  The unit of time for the eviction period. Possible values are `Seconds`, `Minutes`, or `Hours`.

  This setting is ignored if the eviction policy is set to `Never`.

  Default value: `Hours`

- Eviction Period

  The period of time after which entries are evicted or reloaded from the cache.

  This setting is ignored if the eviction policy is set to `Never`.

  Default value: `1`

## Dashboard

`amster` service name: `DashboardUserService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Available Dashboard Apps

  List of application dashboard names available by default for realms with the Dashboard service configured.

  `amster` attribute: `assignedDashboard`

### Secondary configurations

This service has the following secondary configurations.

#### instances

* Dashboard Class Name

  Identifies how to access the application, for example `SAML2ApplicationClass` for a SAML 2.0 application.

  `amster` attribute: `className`

* Dashboard Name

  The application name as it will appear to the administrator for configuring the dashboard.

  `amster` attribute: `name`

* Dashboard Display Name

  The application name that displays on the dashboard client.

  `amster` attribute: `displayName`

* Dashboard Icon

  The icon name that will be displayed on the dashboard client identifying the application.

  `amster` attribute: `icon`

* Dashboard Login

  The URL that takes the user to the application.

  `amster` attribute: `login`

* ICF Identifier

  `amster` attribute: `icfIdentifier`

## Device Binding service

`amster` service name: `DeviceBindingService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Device Binding Attribute

  The user's attribute in which to store bound device data.

  The default attribute is added to the schema when you prepare a user store for use with AM. If you want to use a different attribute, you must add it to your user store schema prior to binding devices with AM. AM must be able to write to the attribute.

  Default value: `boundDevices`

  `amster` attribute: `deviceBindingAttrName`

* Device Binding Encryption Scheme

  Encryption scheme to use to secure device binding data stored on the server.

  AM encrypts the data for each bound device using a unique random secret key with the selected AES encryption standard in CBC mode with PKCS#5 padding. An HMAC-SHA of the selected strength (truncated to half-size) protects the integrity and authenticity of the encryption. AM encrypts the unique random key with the given RSA key pair and stores it with the bound device data.

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings** (value: `NONE`)

  Default value: `NONE`

  `amster` attribute: `deviceBindingSettingsEncryptionScheme`

* Encryption Key Store

  Path to the keystore from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * For greater security, store the encryption key information in a [secret store](../security/secret-stores.html), instead of in the configuration. Use the secret label `am.services.devicebinding.encryption` to map an alias for Device Binding service secrets.

  * If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the user's device profile from their entry in the identity store so that the user can create a new one when they next log in.

  * To use this service in a FIPS 140-3 compliant environment, you must map the `am.services.devicebinding.encryption` secret label to an alias in a [FIPS-compliant keystore](../security/fips.html#manage-bcfks-keystores). |

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.devicebinding.encryption` label in a secret store, this value is ignored. |

  Default value: `/path/to/openam/security/keystores/keystore.jks`

  `amster` attribute: `deviceBindingSettingsEncryptionKeystore`

* Key Store Type

  Type of keystore to load.

  |   |                                                                                                                                                    |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PKCS#11 key stores require hardware support such as a security device or smart card, which are not available by default in most JVM installations. |

  Learn more in the [PKCS#11 Reference Guide](https://docs.oracle.com/en/java/javase/25/security/pkcs11-reference-guide1.html).

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.devicebinding.encryption` label in a secret store, this value is ignored. |

  The possible values for this property are:

  * Label: **Java Key Store (JKS)** (value: `JKS`)

  * Label: **Java Cryptography Extension Key Store (JCEKS)** (value: `JCEKS`)

  * Label: **PKCS#11 Hardware Crypto Storage** (value: `PKCS11`)

  * Label: **PKCS#12 Key Store** (value: `PKCS12`)

  Default value: `JKS`

  `amster` attribute: `deviceBindingSettingsEncryptionKeystoreType`

* Key Store Password

  Password to unlock the key store. AM encrypts this password when you save it in the configuration. You should modify the default value.

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.devicebinding.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceBindingSettingsEncryptionKeystorePassword`

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt bound device data.

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.devicebinding.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceBindingSettingsEncryptionKeystoreKeyPairAlias`

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.devicebinding.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceBindingSettingsEncryptionKeystorePrivateKeyPassword`

## Device ID service

`amster` service name: `deviceIdService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Profile Storage Attribute

  The user's attribute in which to store Device ID profiles.

  The default attribute is added to the schema when you prepare a user store for AM. If you want to use a different attribute, make sure you add it to your user store schema before creating journeys that use device data. AM must be able to write to the attribute.

  Default value: `devicePrintProfiles`

  `amster` attribute: `deviceIdAttrName`

* Device Profile Encryption Scheme

  Encryption scheme to use to secure device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings** (value: `NONE`)

  Default value: `NONE`

  `amster` attribute: `deviceIdSettingsEncryptionScheme`

* Encryption Key Store

  Path to the keystore from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * For greater security, store encryption key information in a [secret store](../security/secret-stores.html), instead of in the configuration. Use the secret label `am.services.deviceid.encryption` to map an alias for Device ID service secrets.

  * If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the user's device profile from their entry in the identity store so that the user can create a new one when they next log in.

  * To use this service in a FIPS 140-3 compliant environment, you must map the `am.services.deviceid.encryption` secret label to an alias in a [FIPS-compliant keystore](../security/fips.html#manage-bcfks-keystores). |

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceid.encryption` label in a secret store, this value is ignored. |

  Default value: `/path/to/openam/security/keystores/keystore.jks`

  `amster` attribute: `deviceIdSettingsEncryptionKeystore`

* Key Store Type

  Type of keystore to load.

  |   |                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PKCS#11 key stores require hardware support such as a security device or smart card and is not available by default in most JVM installations. |

  Learn more in the [PKCS#11 Reference Guide](https://docs.oracle.com/en/java/javase/25/security/pkcs11-reference-guide1.html).

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceid.encryption` label in a secret store, this value is ignored. |

  The possible values for this property are:

  * Label: **Java Key Store (JKS)** (value: `JKS`)

  * Label: **Java Cryptography Extension Key Store (JCEKS)** (value: `JCEKS`)

  * Label: **PKCS#11 Hardware Crypto Storage** (value: `PKCS11`)

  * Label: **PKCS#12 Key Store** (value: `PKCS12`)

  Default value: `JKS`

  `amster` attribute: `deviceIdSettingsEncryptionKeystoreType`

* Key Store Password

  Password to unlock the key store. AM encrypts this password when you save it in the configuration. You should modify the default value.

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceid.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceIdSettingsEncryptionKeystorePassword`

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceid.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceIdSettingsEncryptionKeystoreKeyPairAlias`

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceid.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceIdSettingsEncryptionKeystorePrivateKeyPassword`

## Device Profiles service

`amster` service name: `DeviceProfilesService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Profile Storage Attribute

  The user's attribute in which to store Device profiles.

  The default attribute is added to the schema when you prepare a user store for AM. If you want to use a different attribute, make sure you add it to your user store schema before creating journeys that use device profiles. AM must be able to write to the attribute.

  Default value: `deviceProfiles`

  `amster` attribute: `deviceProfilesAttrName`

* Device Profile Encryption Scheme

  Encryption scheme to use to secure device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings** (value: `NONE`)

  Default value: `NONE`

  `amster` attribute: `deviceProfilesSettingsEncryptionScheme`

* Encryption Key Store

  Path to the keystore from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | * For greater security, store the encryption key information in a [secret store](../security/secret-stores.html), instead of in the configuration. Use the secret label `am.services.deviceprofile.encryption` to map an alias for Device Profiles service secrets.

  * If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the user's device profile from their entry in the identity store so that the user can create a new one when they next log in.

  * To use this service in a FIPS 140-3 compliant environment, you must map the `am.services.deviceprofile.encryption` secret label to an alias in a [FIPS-compliant keystore](../security/fips.html#manage-bcfks-keystores). |

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceprofile.encryption` label in a secret store, this value is ignored. |

  Default value: `/path/to/openam/security/keystores/keystore.jks`

  `amster` attribute: `deviceProfilesSettingsEncryptionKeystore`

* Key Store Type

  Type of keystore to load.

  |   |                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PKCS#11 key stores require hardware support such as a security device or smart card and is not available by default in most JVM installations. |

  Learn more in the [PKCS#11 Reference Guide](https://docs.oracle.com/en/java/javase/25/security/pkcs11-reference-guide1.html).

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceprofile.encryption` label in a secret store, this value is ignored. |

  The possible values for this property are:

  * Label: **Java Key Store (JKS)** (value: `JKS`)

  * Label: **Java Cryptography Extension Key Store (JCEKS)** (value: `JCEKS`)

  * Label: **PKCS#11 Hardware Crypto Storage** (value: `PKCS11`)

  * Label: **PKCS#12 Key Store** (value: `PKCS12`)

  Default value: `JKS`

  `amster` attribute: `deviceProfilesSettingsEncryptionKeystoreType`

* Key Store Password

  Password to unlock the key store. AM encrypts this password when you save it in the configuration. You should modify the default value.

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceprofile.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceProfilesSettingsEncryptionKeystorePassword`

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceprofile.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceProfilesSettingsEncryptionKeystoreKeyPairAlias`

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.deviceprofile.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `deviceProfilesSettingsEncryptionKeystorePrivateKeyPassword`

## Email service

The Email service supports AM's user self-service feature. You can configure the email service globally or by realm. Learn more in [Configure the email service](../user-self-service/configuring-email-service.html).

`amster` service name: `EmailService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Email From Address

  The address from which to send self-service email notifications.

  For example, you might set this property to: no-reply\@example.com

  For Microsoft Graph API transport configurations, this address must exist as a valid address in the Microsoft Exchange administration center.

  `amster` attribute: `from`

* Email Attribute Name

  The profile attribute from which to retrieve the end user's email address.

  Default value: `mail`

  `amster` attribute: `emailAddressAttribute`

* Email Subject

  A subject for notification messages. If you don't set this, self-service emails won't include a subject.

  `amster` attribute: `subject`

* Email Content

  The content for notification messages. If you don't set this, self-service emails include only the confirmation URL in the mail body.

  `amster` attribute: `message`

* Email Rate Limit

  The minimum number of seconds that must elapse between sending emails to a specific user.

  Default value: `1`

  `amster` attribute: `emailRateLimitSeconds`

* Transport Type

  The mail server transport type to use. This value must be set to one of the secondary configurations.

  `amster` attribute: `transportType`

### Secondary configurations

This service has the following secondary configurations.

#### Microsoft Graph API

* Email Message Implementation Class

  The class that sends email notifications, such as those sent for user registration and forgotten passwords.

  Default value: `org.forgerock.openam.services.email.rest.MicrosoftRestMailServer`

  `amster` attribute: `emailImplClassName`

* Email Rest Endpoint URL

  The REST endpoint for sending emails, in the format `https://graph.microsoft.com/v1.0/users/USER ID/sendMail`.

  Learn more in the [sendMail API reference](https://learn.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0\&tabs=http).

  `amster` attribute: `emailEndpoint`

* OAuth2 Token Endpoint URL

  The endpoint for OAuth 2.0 authentication, in the format `https://login.microsoftonline.com/TENANT ID/oauth2/v2.0/token`.

  `amster` attribute: `tokenEndpoint`

* OAuth2 Client Id

  The client ID for use in OAuth 2.0 authentication.

  This is the client ID or application ID provided by the Microsoft Application Registration portal.

  `amster` attribute: `clientId`

* OAuth2 Scopes

  The scopes to request as part of the OAuth 2.0 authentication.

  The value supported by Microsoft Graph API is `https://graph.microsoft.com/.default`.

  `amster` attribute: `scope`

#### SMTP

* Email Message Implementation Class

  The class that sends email notifications, such as those sent for user registration and forgotten passwords.

  Default value: `org.forgerock.openam.services.email.MailServerImpl`

  `amster` attribute: `emailImplClassName`

* Mail Server Host Name

  The fully qualified domain name of the SMTP mail server through which to send self-service email notifications.

  For example, you might set this property to: smtp.example.com

  `amster` attribute: `hostname`

  |   |                                                                                                                                     |
  | - | ----------------------------------------------------------------------------------------------------------------------------------- |
  |   | This is a *different* email server to the general mail server AM uses to send notification emails, for example, on account lockout. |

* Mail Server Host Port

  The port number for the SMTP mail server.

  Default value: `465`

  `amster` attribute: `port`

* Mail Server Authentication Username

  The username for the SMTP mail server.

  For example, you might set this property to: username

  `amster` attribute: `username`

* Mail Server Authentication Password

  The password for the SMTP user.

  `amster` attribute: `password`

* Mail Server Secure Connection

  Whether to connect to the SMTP mail server using SSL.

  The possible values for this property are:

  * `SSL`

  * `Non SSL`

  * `Start TLS`

  Default value: `SSL`

  `amster` attribute: `sslState`

## External datastores

`amster` service name: `DataStoreService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Policy Data Store

  Select a datastore configuration to be used for policy storage

  The possible values for this property are:

  * Label: **Default Data Store** (value: `fd270e31-1788-4193-8734-eb2d500c47f3`)

  Default value: `fd270e31-1788-4193-8734-eb2d500c47f3`

  `amster` attribute: `policyDataStoreId`

* Application Data Store

  Select a datastore configuration to be used for application storage

  The possible values for this property are:

  * Label: **Default Data Store** (value: `fd270e31-1788-4193-8734-eb2d500c47f3`)

  Default value: `fd270e31-1788-4193-8734-eb2d500c47f3`

  `amster` attribute: `applicationDataStoreId`

### Secondary configurations

This service has the following secondary configurations.

#### config

* Host Urls

  An ordered list of connection strings for LDAP directories.Each connection string is composed as follows: HOST:PORT. serverHostname = Host Name

  `amster` attribute: `serverUrls`

* Bind DN

  `amster` attribute: `bindDN`

* Bind Password

  `amster` attribute: `bindPassword`

* Minimum Connection Pool Size

  Default value: `1`

  `amster` attribute: `minimumConnectionPool`

* Maximum Connection Pool Size

  Default value: `10`

  `amster` attribute: `maximumConnectionPool`

* Use SSL

  `amster` attribute: `useSsl`

* Start TLS

  `amster` attribute: `useStartTLS`

* Affinity Enabled

  `amster` attribute: `affinityEnabled`

## ForgeRock Authenticator (OATH) service

`amster` service name: `AuthenticatorOath`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Profile Storage Attribute

  Attribute for storing ForgeRock Authenticator OATH profiles.

  The default attribute is added to the user store during AM installation. If you want to use a different attribute, you must make sure to add it to your user store schema prior to deploying two-step verification with a ForgeRock OATH authenticator app in AM. AM must be able to write to the attribute.

  Default value: `oathDeviceProfiles`

  `amster` attribute: `oathAttrName`

* Device Profile Encryption Scheme

  Encryption scheme for securing device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (Value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (Value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings.** (Value: `NONE`)

  Default value: `NONE`

  `amster` attribute: `authenticatorOATHDeviceSettingsEncryptionScheme`

* Encryption Key Store

  Path to the keystore from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * For greater security, store the encryption key information in a [secret store](../security/secret-stores.html), instead of in the configuration. Use the secret label `am.services.authenticatoroath.encryption` to map an alias for ForgeRock Authenticator OATH service secrets.

  * If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the user's device profile from their entry in the identity store so that the user can create a new one when they next log in.

  * To use this service in a FIPS 140-3 compliant environment, you must map the `am.services.authenticatoroath.encryption` secret label to an alias in a [FIPS-compliant keystore](../security/fips.html#manage-bcfks-keystores). |

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatoroath.encryption` label in a secret store, this value is ignored. |

  Default value: `/path/to/openam/openam/keystore.jks`

  `amster` attribute: `authenticatorOATHDeviceSettingsEncryptionKeystore`

* Key Store Type

  Type of encryption key store.

  |   |                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PKCS#11 keys tores require hardware support such as a security device or smart card and is not available by default in most JVM installations. |

  Learn more in the [PKCS#11 Reference Guide](https://docs.oracle.com/en/java/javase/25/security/pkcs11-reference-guide1.html).

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatoroath.encryption` label in a secret store, this value is ignored. |

  The possible values for this property are:

  * Label: **Java Key Store (JKS).** (Value: `JKS`)

  * Label: **Java Cryptography Extension Key Store (JCEKS).** (Value: `JCEKS`)

  * Label: **PKCS#11 Hardware Crypto Storage.** (Value: `PKCS11`)

  * Label: **PKCS#12 Key Store.** (Value: `PKCS12`)

  Default value: `JKS`

  `amster` attribute: `authenticatorOATHDeviceSettingsEncryptionKeystoreType`

* Key Store Password

  Password to unlock the key store. AM encrypts this password when you save it in the configuration. You should modify the default value.

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatoroath.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `authenticatorOATHDeviceSettingsEncryptionKeystorePassword`

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatoroath.encryption` label in a secret store, this value is ignored. |

  Default value: `pushDeviceProfiles`

  `amster` attribute: `authenticatorOATHDeviceSettingsEncryptionKeystoreKeyPairAlias`

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatoroath.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `authenticatorOATHDeviceSettingsEncryptionKeystorePrivateKeyPassword`

* ForgeRock Authenticator (OATH) Device Skippable Attribute Name

  The datastore attribute that holds the user's decision to enable or disable obtaining and providing a password obtained from an [authenticator app](../am-authentication/authenticator-app.html). This attribute must be writable.

  Default value: `oath2faEnabled`

  `amster` attribute: `authenticatorOATHSkippableName`

## ForgeRock Authenticator (Push) service

`amster` service name: `AuthenticatorPush`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Profile Storage Attribute

  The user's attribute in which to store Push Notification profiles.

  The default attribute is added to the schema when you prepare a user store for use with AM. If you want to use a different attribute, you must add it to your user store schema before deploying push notifications with an [authenticator app](../am-authentication/authenticator-app.html) in AM. AM must be able to write to the attribute.

  Default value: `pushDeviceProfiles`

  `amster` attribute: `pushAttrName`

* Device Profile Encryption Scheme

  Encryption scheme to use to secure device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings** (value: `NONE`)

  Default value: `NONE`

  `amster` attribute: `authenticatorPushDeviceSettingsEncryptionScheme`

* Encryption Key Store

  Path to the keystore from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * For greater security, store encryption key information in a [secret store](../security/secret-stores.html), instead of in the configuration. Use the secret label `am.services.authenticatorpush.encryption` to map an alias for ForgeRock Authenticator Push service secrets.

  * If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the user's device profile from their entry in the identity store so that the user can create a new one when they next log in.

  * To use this service in a FIPS 140-3 compliant environment, you must map the `am.services.authenticatorpush.encryption` secret label to an alias in a [FIPS-compliant keystore](../security/fips.html#manage-bcfks-keystores). |

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatorpush.encryption` label in a secret store, this value is ignored. |

  Default value: `/path/to/openam/openam/keystore.jks`

  `amster` attribute: `authenticatorPushDeviceSettingsEncryptionKeystore`

* Key Store Type

  Type of keystore to load.

  |   |                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PKCS#11 key stores require hardware support such as a security device or smart card and is not available by default in most JVM installations. |

  Learn more in the [PKCS#11 Reference Guide](https://docs.oracle.com/en/java/javase/25/security/pkcs11-reference-guide1.html).

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatorpush.encryption` label in a secret store, this value is ignored. |

The possible values for this property are:

* Label: **Java Key Store (JKS)** (value: `JKS`)

* Label: **Java Cryptography Extension Key Store (JCEKS)** (value: `JCEKS`)

* Label: **PKCS#11 Hardware Crypto Storage** (value: `PKCS11`)

* Label: **PKCS#12 Key Store** (value: `PKCS12`)

Default value: `JKS`

`amster` attribute: `authenticatorPushDeviceSettingsEncryptionKeystoreType`

* Key Store Password

  Password to unlock the key store. AM encrypts this password when you save it in the configuration. You should modify the default value.

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatorpush.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `authenticatorPushDeviceSettingsEncryptionKeystorePassword`

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatorpush.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `authenticatorPushDeviceSettingsEncryptionKeystoreKeyPairAlias`

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------- |
  |   | If AM finds a matching secret for the `am.services.authenticatorpush.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `authenticatorPushDeviceSettingsEncryptionKeystorePrivateKeyPassword`

* ForgeRock Authenticator (Push) Device Skippable Attribute Name

  The name of the attribute in a user's profile used to store their decision on skipping push authentication.

  Default value: `push2faEnabled`

  `amster` attribute: `authenticatorPushSkippableName`

## Globalization settings

`amster` service name: `Globalization`

### Global attributes

The following settings appear on the Global Attributes tab:

* Charsets Supported by Each Locale

  This table lets you configure the order of supported character sets used for each supported locale. Change the settings only if the defaults are not appropriate.

  Default value:

  ```
  locale=zh|charset=UTF-8;GB2312
  locale=ar|charset=UTF-8;ISO-8859-6
  locale=es|charset=UTF-8;ISO-8859-15
  locale=de|charset=UTF-8;ISO-8859-15
  locale=zh_TW|charset=UTF-8;BIG5
  locale=fr|charset=UTF-8;ISO-8859-15
  locale=ko|charset=UTF-8;EUC-KR
  locale=en|charset=UTF-8;ISO-8859-1
  locale=th|charset=UTF-8;TIS-620
  locale=ja|charset=UTF-8;Shift_JIS;EUC-JP
  ```

  `amster` attribute: `charsetMappings`

* Charset Aliases

  Use this list to map between different character set names used in Java and in MIME.

  Default value:

  ```
  mimeName=EUC-KR|javaName=EUC_KR
  mimeName=EUC-JP|javaName=EUC_JP
  mimeName=Shift_JIS|javaName=SJIS
  ```

  `amster` attribute: `sun-identity-g11n-settings-charset-alias-mapping`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Auto Generated Common Name Format

  Use this list to configure how AM formats names shown in the console banner.

  This setting allows the name of the authenticated user shown in the AM admin UI banner to be customised based on the locale of the user.

  Default value: `zh={sn}{givenname}`

  `amster` attribute: `commonNameFormats`

## Google Cloud platform service accounts

`amster` service name: `GoogleCloudServiceAccountService`

### Secondary configurations

This service has the following secondary configurations.

#### serviceAccounts

* Credentials Secret Label

  The secret label that contains the GCP service account credentials. Leave blank to use the default credentials from the environment. Credentials can be loaded from disk using a FileSystem Secret Store.

  `amster` attribute: `credentialsSecretId`

* Allowed Realms

  A list of realms that can use this service account. Realms should be specified in path form, such as `/subrealm/subsubrealm`.

  `amster` attribute: `allowedRealms`

* Allowed Secret Names

  A list of patterns of Google Secret Manager secret names that are allowed to be usedwith this service account. Patterns can include the wildcard "\*".

  Default value: `*`

  `amster` attribute: `allowedSecretNamePatterns`

* Disallowed Secret Names

  A list of patterns of Google Secret Manager secret names that are *not* allowed to be used with this service account. Patterns can include the wildcard "\*".

  `amster` attribute: `disallowedSecretNamePatterns`

## Http Client service

`amster` service name: `HttpClientService`

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use the Http Client service to send an HTTP request over mTLS from within a script, set timeouts, or route a connection through a proxy server.Find out how to configure a service instance as the `clientName` for the `httpClient` script binding in [Send a request using mTLS](../am-scripting/script-bindings.html#httpclient-mtls) and [Route a request through a proxy](../am-scripting/script-bindings.html#httpclient-proxy). |

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Enabled

  Enable this Http Client service to use the secondary configurations when making HTTP requests.

  If not enabled, HTTP requests use the default HTTP client handler configuration (`org.forgerock.openam.httpclienthandler.system.*`) set in [advanced properties](server-advanced.html).

  Default value: `false`

### Secondary configurations

This service has the following secondary configurations.

#### Configuration

* Enabled

  Enable this Http Client instance.

#### TLS Configuration

Configure instances of the Http Client service to control how and which certificates AM uses in TLS connections.

* Client Certificate Secret Label Identifier

  AM uses this identifier to create a specific secret label, using the template `am.services.httpclient.mtls.clientcert.identifier.secret` where identifier is the value of Client Certificate Secret Label Identifier.

  The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If this field is empty, the Http Client service doesn't attach a client certificate to HTTP requests that use mTLS to connect with a target server.

* Server Trust Certificates Secret Label Identifier

  AM uses this identifier to create a specific secret label, using the template `am.services.httpclient.mtls.servertrustcerts.identifier.secret` where identifier is the value of Server Trust Certificates Secret Label Identifier.

  The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If this field is empty, the system truststore is used when attempting to verify the target server's certificate during a TLS connection.

* Disable Certificate Revocation Check

  If enabled, AM doesn't check certificate revocation lists when performing a TLS connection with the target server.

* Trust All Certificates

  If enabled, AM trusts all certificates when performing a TLS connection with the target server.

  |   |                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------- |
  |   | Don't enable this setting in a production environment. It's intended for testing purposes only. |

#### Timeouts

* Use Instance Timeouts

  If enabled, AM uses the connection and response timeouts defined in this Http Client service instance.

* Connection Timeout (secs)

  The maximum time (in seconds) to wait for a connection to be established before failing.

  Default value: `10`

* Response Timeout (secs)

  The maximum time (in seconds) to wait for a response from the target server before failing.

  Default value: `10`

#### Proxy Configuration

* Use Instance Proxy

  If enabled, AM uses the proxy settings defined in this instance. Otherwise, AM routes HTTP Client requests using the proxy settings defined in the [advanced server properties](server-advanced.html).

* Proxy URI

  The URI of the proxy server to use for HTTP requests. The format of the URI must be `http://hostname:port` or `https://hostname:port`.

* Proxy Username

  The proxy authentication username, if required.

* Proxy Secret Label Identifier

  The identifier for the proxy authentication secret.

  AM uses this identifier to create a secret label for mapping to a secret in the secret store. The secret label takes the form `am.services.httpclient.proxy.identifier.secret`, where identifier is the value of Proxy Secret Label Identifier. The label can only contain characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If this field is empty, AM doesn't perform proxy authentication.

## Identity Assertion service

`amster` service name: `IdentityAssertionService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Enable

  Enables the Identity Assertion service that lets AM use PingGateway to manage authentication through a third party such as WDSSO or Kerberos.

  When enabled, the servers defined in the secondary configuration become available as options in the [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/8.1/identity-assertion-node.html) configuration.

  Default value: `true`

* Server cache duration (minutes)

  Supports caching of identity assertion server configurations. A value greater than `0` indicates the duration in minutes that the server configurations are cached. A value of `0` disables caching.

  Default value: `120`

### Secondary configurations

This service has the following secondary configurations.

* Identity Assertion server URL

  The identity assertion server URL, for example, `https://ig.example.com:8448`. Don't include the route in this URL because you define the route when you configure the [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/8.1/identity-assertion-node.html).

* Shared Encryption Secret

  AM uses this identifier to create a specific secret label, using the template `am.services.identityassertion.service.identifier.shared.secret` where identifier is the value of Shared Encryption Secret.

  The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  The secret is shared by AM and PingGateway to encrypt the assertion request JWT sent to PingGateway and then decrypt the result JWT.

  Learn about mapping secrets in [Map and rotate secrets](../security/secret-mapping.html).

* JWT TTL (seconds)

  The identity assertion request JWT time-to-live duration in seconds. This is the period until the JWT sent to the gateway expires.

  Default value: `30`

* Skew Allowance (seconds)

  The time difference skew allowance to use when validating the assertion result JWT's `issued-at` and `expiry` claims. This is to address time differences between the PingGateway host and the AM hosts.

  Default value: `0`

## IDM Provisioning

`amster` service name: `IDMProvisioning`

The following settings are available in this service:

* Enabled

  Default value: `false`

  `amster` attribute: `enabled`

* Deployment URL

  URL of the IDM deployment, for example, `https://localhost:8080`.

  `amster` attribute: `idmDeploymentUrl`

* Deployment Path

  Path of the IDM deployment, for example, `openidm`.

  `amster` attribute: `idmDeploymentPath`

* IDM Provisioning Client

  The name of the oauth client to be used for the client credentials flow.

  `amster` attribute: `idmProvisioningClient`

* Signing Key Alias

  Alias of the signing symmetric key in AM's default keystore. Must be a duplicate of the symmetric key used by IDM.

  `amster` attribute: `provisioningSigningKeyAlias`

* Encryption Key Alias

  Alias of the encryption asymmetric key in AM's default keystore. Must be a duplicate of the asymmetric key used by IDM.

  `amster` attribute: `provisioningEncryptionKeyAlias`

* Signing Algorithm

  JWT signing algorithm.

  `amster` attribute: `provisioningSigningAlgorithm`

* Signing Compatibility Mode

  This option was used only for compatibility with unsupported IDM versions and is no longer documented.

  Default value: `false`

  `amster` attribute: `jwtSigningCompatibilityMode`

* Encryption Algorithm

  JWT encryption algorithm.

  `amster` attribute: `provisioningEncryptionAlgorithm`

* Encryption Method

  JWT encryption method.

  `amster` attribute: `provisioningEncryptionMethod`

- Configuration Cache Duration

  Specify a duration in minutes for caching static IDM configuration to reduce calls to IDM endpoints and improve performance.

  Even a short cache duration of 1 minute (the default) can increase efficiency under load.

  The following values are cached for the specified duration: IDM schemas, consent mappings, validation requirements, KBA configuration, and the IDM active terms.

  If changes are made to the IDM Provisioning service in AM during this period, the configuration cache is immediately cleared. If, however, changes are made to IDM, the cache is only refreshed when the duration expires.

  A zero value disables this feature.

  Default value: `1`

  `amster` attribute: `configurationCacheDuration`

## IoT service

`amster` service name: `IoTService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Create OAuth 2.0 Client

  Create an OAuth 2.0 Client with the given name and default configuration required to serve as the client for the IoT Service. The client will be created without any scope(s).

  Default value: `false`

  `amster` attribute: `createOAuthClient`

* OAuth 2.0 Client Name

  The name of the default OAuth 2.0 Client used by the IoT Service to request access tokens for things.

  Default value: `forgerock-iot-oauth2-client`

  `amster` attribute: `oauthClientName`

* Create OAuth 2.0 JWT Issuer

  Create a Trusted JWT Issuer with the given name and default configuration required for the IoT Service to act as the Issuer when handling request for thing access tokens.

  Default value: `false`

  `amster` attribute: `createOAuthJwtIssuer`

* OAuth 2.0 JWT Issuer Name

  The name of the Trusted JWT Issuer used by the IoT Service to request access tokens for things.

  Default value: `forgerock-iot-jwt-issuer`

  `amster` attribute: `oauthJwtIssuerName`

* OAuth 2.0 Subject Attribute

  The name of the identity store attribute from which to read the OAuth 2.0 subject value. The subject is used in access tokens issued for things. This allows the thing's access token subject to have a value other than the thing's ID, which is the value used by default.

  `amster` attribute: `oauthSubjectAttribute`

* Readable Attributes

  Specifies the list of attributes that a thing is allowed to request from its identity.

  Default value: `thingConfig`

  `amster` attribute: `attributeAllowlist`

## Legacy User Self-Service

`amster` service name: `SecurityProperties`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Legacy Self-Service REST Endpoint

  Specify whether to enable the legacy self-service endpoint.

  AM supports two user self-service components: the Legacy User Self-Service, which is based on a Java SDK and is available in AM versions prior to AM 13, and a common REST-based/XUI-based User Self-Service available in AM 13 and later.

  The Legacy User Self-Service will be deprecated in a future release.

  Default value: `false`

  `amster` attribute: `selfServiceEnabled`

* Self-Registration for Users

  If enabled, new users can sign up using a REST API client.

  Default value: `false`

  `amster` attribute: `selfRegistrationEnabled`

* Self-Registration Token LifeTime (seconds)

  Maximum life time for the token allowing User Self-Registration using the REST API.

  Default value: `900`

  `amster` attribute: `selfRegistrationTokenLifetime`

* Self-Registration Confirmation Email URL

  This page handles the HTTP GET request when the user clicks the link sent by email in the confirmation request.

  Default value: `http://openam.example.com:8080/openam/XUI/confirm.html`

  `amster` attribute: `selfRegistrationConfirmationUrl`

* Forgot Password for Users

  If enabled, users can assign themselves a new password using a REST API client.

  Default value: `false`

  `amster` attribute: `forgotPasswordEnabled`

* Forgot Password Token Lifetime (seconds)

  Maximum life time for the token that allows a user to process a forgotten password using the REST API.

  Default value: `900`

  `amster` attribute: `forgotPasswordTokenLifetime`

* Forgot Password Confirmation Email URL

  This page handles the HTTP GET request when the user clicks the link sent by email in the confirmation request.

  Default value: `http://openam.example.com:8080/openam/XUI/confirm.html`

  `amster` attribute: `forgotPasswordConfirmationUrl`

* Destination After Successful Self-Registration

  Specifies the behavior when self-registration has successfully completed.

  The possible values for this property are:

  * Label: **User is sent to a 'successful registration' page, without being logged in** (value: `default`)

  * Label: **User is sent to the login page, to authenticate** (value: `login`)

  * Label: **User is automatically logged in and sent to the appropriate page within the system** (value: `autologin`)

  Default value: `default`

  `amster` attribute: `userRegisteredDestination`

* Protected User Attributes

  A list of user profile attributes. Users modifying any of the attributes in this list will be required to enter a password as confirmation before the change is accepted. This option applies to XUI deployments only.

  `amster` attribute: `protectedUserAttributes`

* Confirmation Id HMAC Signing Key

  256-bit key (base64-encoded) to use for HMAC signing of the legacy self-service confirmation email links.

  Default value: `Bn+TrDWLSv1E3ADHWxgqpv4fZnVmKLqwQcZvGdo/3jU=`

  `amster` attribute: `confirmationIdHmacKey`

## Logging

`amster` service name: `Logging`

### General

The following settings appear on the General tab:

* Log Status

  Enable the common REST-based audit logging service.

  The possible values for this property are:

  * `ACTIVE`

  * `INACTIVE`

  Default value: `INACTIVE`

  `amster` attribute: `status`

* Logging Type

  Specifies whether to log to a database, Syslog, or to the file system.

  If you choose database then be sure to set the connection attributes correctly, including the JDBC driver to use.

  The possible values for this property are:

  * `File`

  * `DB`

  * `Syslog`

  Default value: `File`

  `amster` attribute: `type`

* Configurable Log Fields

  Controls the fields that are logged by AM.

  This property is the list of fields that are logged by default. Administrators can choose to limit the information logged by AM.

  Default value:

  ```
  IPAddr
  LoggedBy
  LoginID
  NameID
  ModuleName
  ContextID
  Domain
  LogLevel
  HostName
  MessageID
  ```

  `amster` attribute: `fields`

* Log Verification Frequency

  The frequency (in seconds) that AM verifies security of the log files.

  When secure logging is enabled, this is the period that AM will check the integrity of the log files.

  Default value: `3600`

  `amster` attribute: `verifyPeriod`

* Log Signature Time

  The frequency (in seconds) that AM will digitally sign the log records.

  When secure logging is enabled, this is the period that AM will digitally signed the contents of the log files. The log signatures form the basis of the log file integrity checking.

  Default value: `900`

  `amster` attribute: `signaturePeriod`

* Secure Logging

  Enable or disable secure logging.

  If this setting is enabled, AM digitally signs and verifies the contents of log files, to help prevent and detect log file tampering. You must configure a certificate for this functionality to be enabled.

  The possible values for this property are:

  * `ON`

  * `OFF`

  Default value: `OFF`

  `amster` attribute: `security`

* Secure Logging Signing Algorithm

  Determines the algorithm used to digitally sign the log records.

  The possible values for this property are:

  * `MD2withRSA`. MD2 with RSA

  * `MD5withRSA`. MD5 with RSA

  * `SHA1withDSA`. SHA1 with DSA

  * `SHA1withRSA`. SHA1 with RSA

  Default value: `SHA1withRSA`

  `amster` attribute: `signingAlgorithm`

* Logging Certificate Store Location

  The path to the Java keystore containing the logging system certificate.

  The secure logging system will use the certificate alias of `Logger` to locate the certificate in the specified keystore.

  Default value: `%BASE_DIR%/var/audit/Logger.jks`

  `amster` attribute: `certificateStore`

* Number of Files per Archive

  Controls the number of logs files that will be archived by the secure logging system.

  Default value: `5`

  `amster` attribute: `filesPerKeystore`

* Buffer Size

  The number of log records held in memory before the log records will be flushed to the logfile or the database.

  Default value: `25`

  `amster` attribute: `bufferSize`

* Buffer Time

  The maximum time (in seconds) AM will hold log records in memory before flushing to the underlying repository.

  Default value: `60`

  `amster` attribute: `bufferTime`

* Time Buffering

  Enable or disable log buffering

  When enabled AM holds all log records in a memory buffer that it periodically flushes to the repository. The period is set in the `Buffer Time` property.

  The possible values for this property are:

  * `ON`

  * `OFF`

  Default value: `ON`

  `amster` attribute: `buffering`

* Logging Level

  Control the level of JDK logging within AM.

  The possible values for this property are:

  * `OFF`

  * `SEVERE`

  * `WARNING`

  * `INFO`

  * `CONFIG`

  * `FINE`

  * `FINER`

  * `FINEST`

  Default value: `INFO`

  `amster` attribute: `jdkLoggingLevel`

### File

The following settings appear on the File tab:

* Log Rotation

  Enable log rotation to cause new log files to be created when configured thresholds are reached, such as *Maximum Log Size* or *Logfile Rotation Interval*.

  Default value: `true`

  `amster` attribute: `rotationEnabled`

* Maximum Log Size

  Maximum size of a log file, in bytes.

  Default value: `100000000`

  `amster` attribute: `maxFileSize`

* Number of History Files

  Sets the number of history files for each log that AM keeps, including time-based histories.

  The previously live file is moved and is included in the history count, and a new log is created to serve as the live log file. Any log file in the history count that goes over the number specified here will be deleted.

  For time-based logs, a new set of logs will be created when AM is started because of the time-based file names that are used.

  Default value: `1`

  `amster` attribute: `numberHistoryFiles`

* Logfile Rotation Prefix

  The name of the log files will be prefixed with the supplied value.

  This field defines the log file prefix. The prefix will be added to the name of all logfiles.

  |   |                                                    |
  | - | -------------------------------------------------- |
  |   | Only used when time-based log rotation is enabled. |

  `amster` attribute: `prefix`

* Logfile Rotation Suffix

  The name of the log files will be suffixed with the supplied value.

  This field defines the log file suffix. If no suffix is provided, the following default suffix format is used: `-MM.dd .yy-kk.mm`. The suffix allows the use of Date and Time patterns defined in [SimpleDateFormat](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/text/SimpleDateFormat.html).

  |   |                                                            |
  | - | ---------------------------------------------------------- |
  |   | This field is only used if time-based rotation is enabled. |

  Default value: `-MM.dd.yy-kk.mm`

  `amster` attribute: `suffix`

* Logfile Rotation Interval

  The rotation interval (in minutes).

  The rotation interval determines the frequency of when the log files will be rotated. If the value is `-1`, then time-based rotation is disabled and log file size-based rotation is enabled.

  Default value: `-1`

  `amster` attribute: `rotationInterval`

* Log File Location

  The path to the location of the log files

  This property controls the location of the log files. The value depends on whether File or DB logging is used:

  * File: The full pathname to the directory containing the log files.

  * DB: The JDBC URL to the database used to store the log file database.

  Default value: `%BASE_DIR%/var/audit/`

  `amster` attribute: `location`

### Database

The following settings appear on the Database tab:

* Database User Name

  When logging to a database, set this to the username used to connect to the database. If this attribute is incorrectly set, AM performance suffers.

  Default value: `dbuser`

  `amster` attribute: `user`

* Database User Password

  When logging to a database, set this to the password used to connect to the database. If this attribute is incorrectly set, AM performance suffers.

  `amster` attribute: `password`

* Database Driver Name

  When logging to a database, set this to the class name of the JDBC driver used to connect to the database.

  The default is for Oracle. AM also works with the MySQL database driver.

  Default value: `oracle.jdbc.driver.OracleDriver`

  `amster` attribute: `driver`

* Maximum Number of Records

  The maximum number of records read from the logs through the logging API.

  Default value: `500`

  `amster` attribute: `maxRecords`

* DB Failure Memory Buffer Size

  Max number of log records held in memory if DB logging fails.

  This is the maximum number of log records that will be held in memory if the database is unavailable. When the buffer is full, new log records cause the oldest record in the buffer to be cleared. AM monitoring records the number of log entries cleared when the database was unavailable.

  If the value of this property is less than that of the *Buffer Size* then the buffer size value will take precedence.

  Default value: `2`

  `amster` attribute: `databaseFailureMemoryBufferSize`

### Syslog

The following settings appear on the Syslog tab:

* Syslog server host

  The URL or IP address of the syslog server, for example `http://mysyslog.example.com`, or `localhost`.

  Default value: `localhost`

  `amster` attribute: `host`

* Syslog server port

  The port number the syslog server is configured to listen to.

  Default value: `514`

  `amster` attribute: `port`

* Syslog transport protocol

  The protocol to use to connect to the syslog server.

  The possible values for this property are:

  * `UDP`

  * `TCP`

  Default value: `UDP`

  `amster` attribute: `protocol`

* Syslog facility

  Syslog uses the facility level to determine the type of program that is logging the message.

  The possible values for this property are:

  * `kern`

  * `user`

  * `mail`

  * `daemon`

  * `auth`

  * `syslog`

  * `lpr`

  * `news`

  * `uucp`

  * `cron`

  * `authpriv`

  * `ftp`

  * `local0`

  * `local1`

  * `local2`

  * `local3`

  * `local4`

  * `local5`

  * `local6`

  * `local7`

  Default value: `local5`

  `amster` attribute: `facility`

* Syslog connection timeout

  The period of time, in seconds, to wait when attempting to connect to the syslog server, before reporting a failure.

  Default value: `30`

  `amster` attribute: `timeout`

## Monitoring

`amster` service name: `Monitoring`

### Configuration

The following settings appear on the Configuration tab:

* Monitoring Status

  Enable the monitoring system in AM.

  Default value: `false`

  `amster` attribute: `enabled`

* Monitoring HTTP Port

  Port number for the HTTP monitoring interface.

  This attribute is *deprecated*.

  Default value: `8082`

  `amster` attribute: `httpPort`

* Monitoring HTTP interface status

  Enable / Disable the HTTP access to the monitoring system.

  This attribute is *deprecated*.

  Default value: `false`

  `amster` attribute: `httpEnabled`

* Monitoring HTTP interface authentication file path

  Path to the monitoring system authentication file

  The `openam_mon_auth` file contains the username and password of the account used to protect the monitoring interfaces. The default username is `demo` with a password of `changeit`.

  This attribute is *deprecated*.

  Default value: `%BASE_DIR%/security/openam_mon_auth`

  `amster` attribute: `authfilePath`

* Monitoring RMI Port

  Port number for the JMX monitoring interface

  This attribute is *deprecated*.

  Default value: `9999`

  `amster` attribute: `rmiPort`

* Monitoring RMI interface status

  Enable / Disable the JMX access to the monitoring system

  This attribute is *deprecated*.

  Default value: `false`

  `amster` attribute: `rmiEnabled`

* Policy evaluation monitoring history size

  Size of the window of most recent policy evaluations to record to expose via monitoring system. Valid range is 100 - 1000000.

  This attribute is *deprecated*.

  Default value: `10000`

  `amster` attribute: `policyHistoryWindowSize`

* Session monitoring history size

  Size of the window of most recent session operations to record to expose via monitoring system. Valid range is 100 - 1000000.

  This attribute is *deprecated*.

  Default value: `10000`

  `amster` attribute: `sessionHistoryWindowSize`

### Secondary configurations

This service has the following secondary configurations.

#### crest

* Enabled

  Default value: `false`

  `amster` attribute: `enabled`

#### graphite

* Hostname

  The hostname of the Graphite server to which metrics should be published.

  `amster` attribute: `host`

* Port

  The port of the Graphite server to which metrics should be published.

  Default value: `2004`

  `amster` attribute: `port`

* Frequency

  The frequency (in seconds) at which metrics should be published.

  Default value: `30`

  `amster` attribute: `frequency`

#### prometheus

* Enabled

  Default value: `false`

  `amster` attribute: `enabled`

* Authentication Type

  The type of authentication determines whether Prometheus needs to authenticate: `None` or `HTTP Basic`.

  Default value: `HTTP Basic`

  `amster` attribute: `authenticationType`

* Username

  If the authentication type is `HTTP Basic`, specify a username for Prometheus to use when accessing the endpoint.

  Default value: `prometheus`

  `amster` attribute: `username`

* Password

  If the authentication type is `HTTP Basic`, specify a password for Prometheus to use when accessing the endpoint.

  |   |                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------- |
  |   | If you set a Secret Label Identifier and AM finds a matching secret in a secret store, the Password is ignored. |

  `amster` attribute: `password`

* Secret Label Identifier

  AM uses this identifier to create a specific secret label, using the template `am.services.monitoring.prometheus.identifier.secret` where identifier is the value of Secret Label Identifier.

  The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If you set a Secret Label Identifier and AM finds a matching secret in a secret store, the Password is ignored.

  `amster` attribute: `password`

## Multi-federation protocol

`amster` service name: `MultiFederationProtocol`

The following settings are available in this service:

* Single Logout Handler List

  List of logout handlers for each supported federation protocol

  The multi-federation protocol engine supports single logout. Each federation protocol requires a different single logout handler. The logout handler must implement the `com.sun.identity.multiprotocol.SingleLogoutHandler` interface.

  Default value:

  ```
  key=WSFED|class=com.sun.identity.multiprotocol.WSFederationSingleLogoutHandler
  key=SAML2|class=com.sun.identity.multiprotocol.SAML2SingleLogoutHandler
  ```

  `amster` attribute: `singleLogoutHandlerList`

## Naming

`amster` service name: `Naming`

### General configuration

The following settings appear on the General Configuration tab:

* Profile Service URL

  Specifies the endpoint used by the profile service.

  This attribute is deprecated.

  Default value: `%protocol://%host:%port%uri/profileservice`

  `amster` attribute: `profileUrl`

* Session Service URL

  Specifies the endpoint used by the session service.

  Default value: `%protocol://%host:%port%uri/sessionservice`

  `amster` attribute: `sessionUrl`

* Logging Service URL

  Specifies the endpoint used by the logging service.

  Default value: `%protocol://%host:%port%uri/loggingservice`

  `amster` attribute: `loggingUrl`

* Policy Service URL

  Specifies the endpoint used by the policy service.

  Default value: `%protocol://%host:%port%uri/policyservice`

  `amster` attribute: `policyUrl`

* Authentication Service URL

  Specifies the endpoint used by the authentication service.

  Default value: `%protocol://%host:%port%uri/authservice`

  `amster` attribute: `authUrl`

### Federation configuration

The following settings appear on the **Federation Configuration** tab:

* SAML Web Profile/Artifact Service URL

  Specifies the SAML v1 endpoint.

  Default value: `%protocol://%host:%port%uri/SAMLAwareServlet`

  `amster` attribute: `samlAwareServletUrl`

* SAML SOAP Service URL

  Specifies the SAML v1 SOAP service endpoint.

  Default value: `%protocol://%host:%port%uri/SAMLSOAPReceiver`

  `amster` attribute: `samlSoapReceiverUrl`

* SAML Web Profile/POST Service URL

  Specifies the SAML v1 Web Profile endpoint.

  Default value: `%protocol://%host:%port%uri/SAMLPOSTProfileServlet`

  `amster` attribute: `samlPostServletUrl`

* SAML Assertion Manager Service URL

  Specifies the SAML v1 assertion service endpoint.

  Default value: `%protocol://%host:%port%uri/AssertionManagerServlet/AssertionManagerIF`

  `amster` attribute: `samlAssertionManagerUrl`

* JAXRPC Endpoint URL

  (Deprecated) Specifies the JAXRPC endpoint URL used by the remote IDM/SMS APIs.

  Default value: `%protocol://%host:%port%uri/jaxrpc/`

  `amster` attribute: `jaxrpcUrl`

### Endpoint configuration

The following settings appear on the **Endpoint Configuration** tab:

* Identity Web Services Endpoint URL

  Specifies the endpoint for the Identity WSDL services.

  Default value: `%protocol://%host:%port%uri/identityservices/`

  `amster` attribute: `jaxwsUrl`

* Identity REST Services Endpoint URL

  Specifies the endpoint for the Identity REST services.

  Default value: `%protocol://%host:%port%uri/identity/`

  `amster` attribute: `idsvcsRestUrl`

* Security Token Service Endpoint URL

  Specifies the STS endpoint.

  Default value: `%protocol://%host:%port%uri/sts`

  `amster` attribute: `stsUrl`

* Security Token Service MEX Endpoint URL

  Specifies the STS MEX endpoint.

  Default value: `%protocol://%host:%port%uri/sts/mex`

  `amster` attribute: `stsMexUrl`

## OAuth2 provider

`amster` service name: `OAuth2Provider`

### Global attributes

The following settings appear on the Global Attributes tab:

* Token Denylist Cache Size

  Number of denylisted tokens to cache in memory to speed up denylist checks and reduce load on the CTS.

  Default value: `10000`

  `amster` attribute: `blacklistCacheSize`

* Denylist Poll Interval (seconds)

  How frequently to poll for token denylist changes from other servers, in seconds.

  How often each server will poll the CTS for token denylist changes from other servers. This is used to maintain a highly compressed view of the overall current token denylist improving performance. A lower number will reduce the delay for denylisted tokens to propagate to all servers at the cost of increased CTS load. Set to `0` to disable this feature completely.

  Default value: `10`

  `amster` attribute: `blacklistPollInterval`

* Denylist Purge Delay (minutes)

  Length of time to denylist tokens beyond their expiry time.

  Allows additional time to account for clock skew to ensure that a token has expired before it is removed from the denylist.

  Default value: `1`

  `amster` attribute: `blacklistPurgeDelay`

* Client-Side Grant Token Upgrade Compatibility Mode

  Enable AM to consume and create client-side OAuth 2.0 tokens in two different formats simultaneously.

  Enable this option when upgrading AM to allow the new instance to create and consume client-side OAuth 2.0 tokens in both the previous format and the new format. Disable this option once all AM instances in the cluster have been upgraded.

  Default value: `false`

  `amster` attribute: `statelessGrantTokenUpgradeCompatibilityMode`

* CTS Storage Scheme

  Storage scheme to be used when storing OAuth 2.0 tokens to CTS.

  To support rolling upgrades, this should be set to the latest storage scheme supported by all AM instances within your cluster. Select the latest storage scheme once all AM instances in the cluster have been upgraded.

  The storage scheme can be one of the following:

  * **One-to-One Storage Scheme**

    Under this storage scheme, each OAuth 2.0 token maps to an individual CTS entry.

    *This storage scheme is inefficient - use the Grant-Set Storage Scheme after all servers have been upgraded to a version that supports it.*

    (Amster value: `CTS_ONE_TO_ONE_MODEL`)

  * **Grant-Set Storage Scheme**

    Under this storage scheme, multiple authorization codes, access tokens, and refresh tokens for a given OAuth 2.0 client and resource owner can be stored within a single CTS entry.

    (Amster value: `CTS_GRANT_SET_MODEL`)

  Default value: **One-to-One Storage Scheme**

  `amster` attribute: `storageScheme`

* Enforce JWT Unreasonable Lifetime

  Enable the enforcement of JWT token unreasonable lifetime during validation.

  The [JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/rfc/rfc7523.html#section-3) specification states that an authorization server can reject JWTs with an "exp" claim value that is unreasonably far in the future and an "iat" claim value that is unreasonably far in the past. This enforcement can be disabled, but should only be done if the security implications have been evaluated.

  Default value: `true`

  `amster` attribute: `jwtTokenLifetimeValidationEnabled`

* JWT Unreasonable Lifetime (seconds)

  Specify the lifetime (in seconds) of a JWT which should be considered unreasonable and rejected by validation.

  The [JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://www.rfc-editor.org/rfc/rfc7523.html#section-3) specification states that an authorization server can reject JWTs with an "exp" claim value that is unreasonably far in the future and an "iat" claim value that is unreasonably far in the past. During token validation AM enforces that the token must expire within the specified duration and if the "iat" claim value is present, the token must not be older than the specified duration.

  Default value: `86400`

  `amster` attribute: `jwtTokenUnreasonableLifetime`

* JWT Required Claims

  Specify a custom list of claims that will be treated as required during validation of an OAuth 2.0 authorization grant or client authentication JWT. This is in addition to the default mandatory claims, "iss", "aud", and "exp". AM will throw an error if any of the claims defined in this attribute are not present.

  |   |                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------- |
  |   | This attribute does *not* apply to a request object JWT, such as the JWT parameter used when invoking the PAR endpoint. |

  Default value: `[Empty]`

  `amster` attribute: `jwtTokenRequiredClaims`

- OAuth2 allow unauthenticated user code entry

  Whether a user must authenticate *before* they can proceed to the verification URL to enter a user code.

  If set to true, users can input a user code without first logging in.

  This setting is intended for backwards compatibility only. Only enable it on existing installations that require legacy functionality.

  Default value: `false`

  `amster` attribute: `allowUnauthorisedAccessToUserCodeForm`

### Core

The following settings appear on the Core tab:

* Use Client-Side Access & Refresh Tokens

  When enabled, AM issues access and refresh tokens that can be inspected by resource servers.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  Default value: `false`

  `amster` attribute: `statelessTokensEnabled`

* Use Macaroon Access and Refresh Tokens

  When enabled, AM will issue access and refresh tokens as Macaroons with caveats.

  Default value: `false`

  `amster` attribute: `macaroonTokensEnabled`

* Authorization Code Lifetime (seconds)

  The time an authorization code is valid for, in seconds.

  Default value: `120`

  `amster` attribute: `codeLifetime`

* Refresh Token Lifetime (seconds)

  The time in seconds a refresh token is valid for. If this field is set to `-1`, the refresh token will never expire.

  Default value: `604800`

  `amster` attribute: `refreshTokenLifetime`

* Access Token Lifetime (seconds)

  The time an access token is valid for, in seconds. Note that if you set the value to `0`, the access token will not be valid. A maximum lifetime of 600 seconds is recommended.

  Default value: `3600`

  `amster` attribute: `accessTokenLifetime`

* Issue Refresh Tokens

  Whether to issue a refresh token when returning an access token.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  Default value: `true`

  `amster` attribute: `issueRefreshToken`

* Issue Refresh Tokens on Refreshing Access Tokens

  Whether to issue a refresh token when refreshing an access token.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  Default value: `true`

  `amster` attribute: `issueRefreshTokenOnRefreshedToken`

* Use Policy Engine for Scope decisions

  With this setting enabled, the policy engine is consulted for each scope value that is requested.

  Scope decisions are made in the following way when based on the policy engine:

  * If a policy returns an action of GRANT=true, the scope is consented automatically, and the user is not consulted in a user-interaction flow.

  * If a policy returns an action of GRANT=false, the scope is not added to any resulting token, and the user will not see it in a user-interaction flow.

  * If no policy returns a value for the GRANT action:

    * For user-facing grant types, such as the authorization or device code flows, the user is asked for consent or saved consent is used.

    * For grant types that are not user-facing, such as those using password or client credentials, the scope is not added to any resulting token.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  Default value: `false`

  `amster` attribute: `usePolicyEngineForScope`

* Scopes Policy Set

  The policy set that defines the context in which policy evaluations occur when `Use Policy Engine for Scope decisions` is enabled on the OAuth 2.0 provider. Leave this field blank, or set it to `oauth2Scopes` to use the default policy set.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  Default value: `[Empty]`

* OAuth2 Access Token May Act Script

  The script that is executed when issuing an access token explicitly to modify the `may_act` claim placed on the token.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  The possible values for this property are:

  * Label: **OAuth2 May Act Script** (Value: `c735de08-f8f2-4e69-aa4a-2d8d3d438323`)

  * Label: **--- Select a script ---** (Value: `[Empty]`)

  Default value: `[Empty]`

  `amster` attribute: `accessTokenMayActScript`

* OIDC ID Token May Act Script

  The script that is executed when issuing an OIDC ID Token explicitly to modify the `may_act` claim placed on the token.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  The possible values for this property are:

  * Label: **OAuth2 May Act Script** (Value: `c735de08-f8f2-4e69-aa4a-2d8d3d438323`)

  * Label: **--- Select a script ---** (Value: `[Empty]`)

  Default value: `[Empty]`

  `amster` attribute: `oidcMayActScript`

### Advanced

The following settings appear on the Advanced tab:

* Custom Login URL Template

  Custom URL for handling login, to override the default AM login page.

  Supports Freemarker syntax, with the following variables:

  | Variable    | Description                                                                                                                    |
  | ----------- | ------------------------------------------------------------------------------------------------------------------------------ |
  | `gotoUrl`   | The URL to redirect to after login.                                                                                            |
  | `acrValues` | The Authentication Context Class Reference (acr) values for the authorization request.                                         |
  | `realm`     | The AM realm the authorization request was made on.                                                                            |
  | `service`   | The name of the authentication tree requested to perform resource owner authentication.                                        |
  | `locale`    | A space-separated list of locales, ordered by preference.                                                                      |
  | `ForceAuth` | Set to `true` when forced reauthentication is required. Use this variable to include `ForceAuth=true` in the custom login URL. |

  The following example template redirects users to a non-AM front end to handle login, which will then redirect back to the `/oauth2/authorize` endpoint with any required parameters:

  `http://mylogin.com/login?goto=${goto}<#if acrValues??>&acr_values=${acrValues}</#if><#if realm??>&realm=${realm}</#if><#if service??>&service=${service}</#if><#if locale??>&locale=${locale}</#if>`

  |   |                                                                               |
  | - | ----------------------------------------------------------------------------- |
  |   | The default AM login page is constructed using the "Base URL Source" service. |

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  `amster` attribute: `customLoginUrlTemplate`

* Persistent Claims

  Set of custom claims that can be persisted between token refreshes. This list should not include the RFC 123 OAuth2 specification defined list of claims.

  Default value:

  `amster` attribute: `persistentClaims`

* Response Type Plugins

  List of plugins that handle the valid `response_type` values.

  OAuth 2.0 clients pass response types as parameters to the OAuth 2.0 Authorization endpoint (`/oauth2/authorize`) to indicate which grant type is requested from the provider. For example, the client passes `code` when requesting an authorization code, and `token` when requesting an access token.

  Values in this list take the form `response-type|plugin-class-name`.

  Default value:

  ```
  code|org.forgerock.oauth2.core.AuthorizationCodeResponseTypeHandler
  id_token|org.forgerock.openidconnect.IdTokenResponseTypeHandler
  device_code|org.forgerock.oauth2.core.TokenResponseTypeHandler
  token|org.forgerock.oauth2.core.TokenResponseTypeHandler
  ```

  `amster` attribute: `responseTypeClasses`

- Additional Audience Values

  The additional audience values that will be permitted when verifying Client Authentication JWTs.

  These audience values will be in addition to the AS base, issuer and endpoint URIs.

  `amster` attribute: `allowedAudienceValues`

- Token Exchanger Plugins

  List of plugins that handle the valid `requested_token_type` values.

  When using the Token Exchange grant type, these handlers will be used to convert the provided `subject_token` and `actor_token` into the appropriate impersonation or delegation tokens for use with downstream services.

  Default value:

  ```
  urn:ietf:params:oauth:token-type:access_token=&gt;urn:ietf:params:oauth:token-type:access_token|org.forgerock.oauth2.core.tokenexchange.accesstoken.AccessTokenToAccessTokenExchanger
  urn:ietf:params:oauth:token-type:id_token=&gt;urn:ietf:params:oauth:token-type:id_token|org.forgerock.oauth2.core.tokenexchange.idtoken.IdTokenToIdTokenExchanger
  urn:ietf:params:oauth:token-type:access_token=&gt;urn:ietf:params:oauth:token-type:id_token|org.forgerock.oauth2.core.tokenexchange.accesstoken.AccessTokenToIdTokenExchanger
  urn:ietf:params:oauth:token-type:id_token=&gt;urn:ietf:params:oauth:token-type:access_token|org.forgerock.oauth2.core.tokenexchange.idtoken.IdTokenToAccessTokenExchanger
  ```

  `amster` attribute: `tokenExchangeClasses`

- Token Validator Plugins

  List of plugins that validate `subject_token` and `actor_token` values.

  When using the Token Exchange grant type, these handlers will be used to convert the validate `subject_token` and `actor_token` values to ensure they meet the required criteria to be exchanged.

  Default value:

  ```
  urn:ietf:params:oauth:token-type:id_token|org.forgerock.oauth2.core.tokenexchange.idtoken.OidcIdTokenValidator
  urn:ietf:params:oauth:token-type:access_token|org.forgerock.oauth2.core.tokenexchange.accesstoken.OAuth2AccessTokenValidator
  ```

  `amster` attribute: `tokenValidatorClasses`

- User Profile Attribute(s) the Resource Owner is Authenticated On

  Names of profile attributes that resource owners use to log in. You can add others to the default, for example `mail`.

  Default value: `uid`

  `amster` attribute: `authenticationAttributes`

- User Display Name attribute

  The profile attribute that contains the name to be displayed for the user on the consent page.

  Default value: `cn`

  `amster` attribute: `displayNameAttribute`

* Client Registration Scope Allowlist

  The set of scopes allowed when registering clients dynamically, with translations.

  Scopes can be entered as simple strings or pipe-separated strings representing the internal scope name, locale, and localized description.

  For example: `read|en|Permission to view email messages in your account`

  Locale strings are in the format: `language_country_variant`, for example `en`, `en_GB`, or `en_US_WIN`.

  If the locale and pipe is omitted, the description is displayed to all users that have undefined locales.

  If the description is also omitted, nothing is displayed on the consent page for the scope. For example, specifying `read|` would allow the scope read to be used by the client but would not display it to the user on the consent page when requested.

  `amster` attribute: `supportedScopes`

* Subject Types supported

  List of subject types supported. Valid values are:

  * `public` - Each client receives the same subject (`sub`) value.

  * `pairwise` - Each client receives a different subject (`sub`) value, to prevent correlation between clients.

    Default value:

    ```
    public
    pairwise
    ```

    `amster` attribute: `supportedSubjectTypes`

* Default Client Scopes

  List of scopes a client will be granted if they request registration without specifying which scopes they want. Default scopes are not auto-granted to clients created through the AM admin UI.

  `amster` attribute: `defaultScopes`

* OAuth2 Token Signing Algorithm

  Algorithm used to sign client-side OAuth 2.0 tokens in order to detect tampering.

  AM supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

    The possible values for this property are:

  * `HS256`

  * `HS384`

  * `HS512`

  * `RS256`

  * `RS384`

  * `RS512`

  * `ES256`

  * `ES384`

  * `ES512`

  * `PS256`

  * `PS384`

  * `PS512`

  Default value: `HS256`\
  `amster` attribute: `tokenSigningAlgorithm`

* Client-Side Token Compression

  Whether client-side access and refresh tokens should be compressed.

  Default value: `false`

  `amster` attribute: `tokenCompressionEnabled`

* Encrypt Client-Side Tokens

  Whether client-side access and refresh tokens should be encrypted.

  Enabling token encryption will disable token signing as encryption is performed using direct symmetric encryption.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  Default value: `false`

  `amster` attribute: `tokenEncryptionEnabled`

* Subject Identifier Hash Salt

  If *pairwise* subject types are supported, it is *STRONGLY RECOMMENDED* to change this value. It is used in the salting of hashes for returning specific `sub` claims to individuals using the same `request_uri` or `sector_identifier_uri`.

  |   |                                                                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you map `am.services.oauth2.provider.hash.salt.secret` to a secret in a secret store, AM ignores this value.Learn more about secret labels in [OAuth 2.0 default secret label mappings](../security/secret-mapping.html#oauth2-provider-default-secret-IDs). |

  Default value: `changeme`

  `amster` attribute: `hashSalt`

* Code Verifier Parameter Required

  If enabled, requests using the authorization code grant or device flow require a `code_challenge` attribute to comply with the PKCE standard.

  For more information, read the [PKCE specification](https://www.rfc-editor.org/info/rfc7636).

  Note that if a client specifies a `code_challenge` parameter in the authorization request, PKCE is enabled regardless of the value of this attribute.

  The possible values for this property are:

  * Label: **All requests** (Value: `true`)

  * Label: **Requests from all public clients** (Value: `public`)

  * Label: **Requests from all passwordless public clients** (Value: `passwordless`)

  * Label: **No requests** (Value: `false`)

  Default value: `false`

  `amster` attribute: `codeVerifierEnforced`

* Modified Timestamp Attribute Name

  The identity Data Store attribute used to return modified timestamp values.

  This attribute is paired together with the *Created Timestamp Attribute Name* attribute (`createdTimestampAttribute`). You can leave both attributes unset (default) or set them both. If you set only one attribute and leave the other blank, the access token fails with a 500 error.

  For example, when you configure AM as an OIDC provider (OP) in a Mobile Connect application and use DS as an identity store, the client accesses the `userinfo` endpoint to obtain the `updated_at` claim value in the ID token. The `updated_at` claim gets its value from the `modifiedTimestampAttribute` attribute in the user profile. If the profile has never been modified the `updated_at` claim uses the `createdTimestampAttribute` attribute.

  `amster` attribute: `modifiedTimestampAttribute`

* Created Timestamp Attribute Name

  The identity Data Store attribute used to return created timestamp values.

  `amster` attribute: `createdTimestampAttribute`

* Password Grant Authentication Service

  The tree used to authenticate the username and password for the resource owner password credentials grant type.

  `amster` attribute: `passwordGrantAuthService`

* Enable Auth Module Messages for Password Credentials Grant

  This property was used only for authentication with modules and chains and is no longer documented.

* Grant Types

  The set of Grant Types (OAuth 2.0 flows) that are permitted to be used by this client.

  If no Grant Types (OAuth 2.0 Flows) are configured, nothing is permitted.

  Default value:

  ```
  implicit
  urn:ietf:params:oauth:grant-type:saml2-bearer
  refresh_token
  password
  client_credentials
  urn:ietf:params:oauth:grant-type:device_code
  authorization_code
  urn:openid:params:grant-type:ciba
  urn:ietf:params:oauth:grant-type:uma-ticket
  urn:ietf:params:oauth:grant-type:token-exchange
  urn:ietf:params:oauth:grant-type:jwt-bearer
  ```

  `amster` attribute: `grantTypes`

* Trusted TLS Client Certificate Header

  HTTP Header to receive TLS client certificates when TLS is terminated at a proxy.

  Leave blank if not terminating TLS at a proxy. Ensure that the proxy is configured to strip this headerfrom incoming requests. Best practice is to use a random string.

  `amster` attribute: `tlsClientCertificateTrustedHeader`

* TLS Client Certificate Header Format

  Format of the HTTP header used to communicate a client certificate from a reverse proxy.

  The following formats are supported:

  * `BASE64_ENCODED_CERT`: For Base64-encoded, URL-encoded certificates in PEM or DER format.

    AM infers the certificate type from the contents of the certificate. For example, a certificate that starts with `-----BEGIN CERTIFICATE-----` and ends with `-----END CERTIFICATE-----` is inferred to be a PEM format certificate. A certificate that starts and ends with a colon (`:`) is inferred to be a DER format certificate.

    NGINX, Google GKE, and AWS provide certificates in this format.

  * `X_FORWARDED_CLIENT_CERT`: The proxy provides the certificate in the `X-Forwarded-Client-Cert` header.

    Istio/Envoy proxies provide certificates in this way. Find more information in the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#config-http-conn-man-headers-x-forwarded-client-cert).

  Default value: `BASE64_ENCODED_CERT`\
  `amster` attribute: `tlsClientCertificateHeaderFormat`

* Support TLS Certificate-Bound Access Tokens

  Whether to bind access tokens to the client certificate when using TLS client certificate authentication.

  Default value: `true`

  `amster` attribute: `tlsCertificateBoundAccessTokensEnabled`

* Check TLS Certificate Revocation Status

  Whether to check if TLS client certificates have been revoked.

  If enabled then AM will check if TLS client certificates used for client authentication have been revoked using either OCSP (preferred) or CRL. AM implements "soft fail" semantics: if the revocation status cannot be established due to a temporary error (for example, a network error) then the certificate is assumed to still be valid.

  Default value: `false`

  `amster` attribute: `tlsCertificateRevocationCheckingEnabled`

* OCSP Responder URI

  URI of the OCSP responder service to use for checking certificate revocation status.

  If specified this value overrides any OCSP or CRL mechanisms specified in individual certificates.

  `amster` attribute: `tlsOcspResponderUri`

* OCSP Responder Certificate

  PEM-encoded certificate to use to verify OCSP responses.

  If specified this certificate will be used to verify the signature on all OCSP responses. Otherwise the appropriate certificate will be determined from the trusted CA certificates.

  `amster` attribute: `tlsOcspResponderCert`

* Macaroon Token Format

  The format to use when serializing and parsing Macaroons. V1 is bulky and should only be used when compatibility with older Macaroon libraries is required.

  The possible values for this property are:

  * `V1`

  * `V2`

  Default value: `V2`\
  `amster` attribute: `macaroonTokenFormat`

* Require exp claim in Request Object

  If enabled, the `exp` claim must be included in JWT request objects specified at [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) or [/oauth2/par](../am-oauth2/oauth2-par-endpoint.html).

  The `exp` (expiration time) claim defines the lifetime of the JWT, after which the JWT is no longer valid.

  To comply with the [FAPI](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile, this setting must be enabled.

  Default value: `false`

  `amster` attribute: `expClaimRequiredInRequestObject`

* Require nbf claim in Request Object

  If enabled, the `nbf` claim must be included in JWT request objects specified at [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) or [/oauth2/par](../am-oauth2/oauth2-par-endpoint.html).

  The `nbf` (not before) claim defines the earliest time that the JWT can be accepted for processing.

  To comply with the [FAPI](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile, this setting must be enabled.

  Default value: `false`

  `amster` attribute: `nbfClaimRequiredInRequestObject`

* Max nbf and exp difference

  The maximum permitted difference, in minutes, between the `nbf` and `exp` claims, as defined in the request object JWT.

  A value of 0 indicates that there is no maximum time requirement.

  If set to a value greater than 0, and either `nbf` or `exp` is not defined, the JWT is validated successfully, providing the claims are not required.

  If set to a value greater than 0, and both claims are present, the JWT is validated accordingly, even when not required.

  To comply with the [FAPI](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile, this setting must be 60 (minutes) or less.

  Default value: `0`

  `amster` attribute: `maxDifferenceBetweenRequestObjectNbfAndExp`

* Max nbf age

  The maximum permitted age, in minutes, of the `nbf` claim.

  A value of 0 indicates that there is no maximum time requirement.

  If set to a value greater than 0, and `nbf` is neither required nor specified, the JWT is validated successfully.

  If set to a value greater than 0, and `nbf` is present, the JWT is validated accordingly, even when not required.

  To comply with the [FAPI](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile, this setting must be 60 (minutes) or less.

  Default value: `0`

  `amster` attribute: `maxAgeOfRequestObjectNbfClaim`

- Request Object Processing Specification

  This setting determines which specification AM uses to validate request object JWTs, provided in the `request` or `request_uri` parameters:

  * `OIDC`: AM uses the [OIDC specification](https://openid.net/specs/openid-connect-core-1_0.html) for JWT processing

  * `JAR`: AM uses the [JAR specification](https://www.rfc-editor.org/rfc/rfc9101.html) for JWT processing

  For example, the following OIDC request specifies a request object JWT. It could be validated according to the JAR specification *or* as a standard OIDC request:

  `/authorize?client_id=myClient&request={JWT with scope=openid, response_type=id_token}`

  This table summarizes how AM validates the request object JWT, depending on the specification:

  **Specification Rules**

  |                                      | OIDC specification                                                                                                                                                                                           | JAR specification                                                                                                                          |
  | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
  | **Request object**                   | *May* be unsigned.                                                                                                                                                                                           | *Must* be [signed](https://www.rfc-editor.org/rfc/rfc7515.html) and, optionally, [encrypted](https://www.rfc-editor.org/rfc/rfc7516.html). |
  | **Authorization request parameters** | AM assembles parameters from the request object *and* the query parameters.If the same parameter exists in the request object and in the authorization request, AM uses the parameter in the request object. | AM assembles parameters from the request object ONLY and ignores duplicates defined as query parameters.                                   |
  | **Required request parameters**      | * `client_id`

  * `response_type`

  * `scope`, including `openid` scope value The `response_type` and `scope` must be specified outside the request object.                                                    | - `client_id`

  - `request` OR `request_uri`                                                                                                |

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * By default, AM consults this field *only* if it can't determine the rules to apply based on the incoming request. To override this behavior and ***force*** AM to use the specification selected here, regardless of the request object contents, set the advanced server property `oauth2.provider.request.object.processing.enforced` to `true`.

  * If you set `oauth2.provider.request.object.processing.enforced` to `true`, AM uses the specification selected here to process all JWT requests, regardless of whether the requests are OIDC. |

  Find more information on JWT validation rules in the [`request`](../am-oauth2/oauth2-parameters.html#the-request-parameter) parameter.

  Default value: `OIDC`

  `amster` attribute: `requestObjectProcessing`

- PAR Request URI Lifetime (seconds)

  The length of time that the PAR Request URI is valid, in seconds.

  Set this value to a short interval (for example, between 5 and 150 seconds). Setting this attribute to a higher value increases the load on the CTS, and can even result in denial of service if the requests are large and consume the available storage capacity.

  Learn more about the PAR flow in [Authorization code grant with PAR](../am-oauth2/oauth2-authz-grant-par.html).

  Default value: `90`

  `amster` attribute: `parRequestUriLifetime`

- Require Pushed Authorization Requests

  If enabled, clients must use the PAR endpoint to initiate authorization requests, otherwise AM will throw an error indicating a missing or invalid request object.

  This applies to all clients, including clients that are not configured to require PAR. You can find details in [Advanced client properties](../am-oauth2/oauth2-register-client.html#configure-oauth2-oidc-client-advanced).

  Default value: `false`

  `amster` attribute: `requirePushedAuthorizationRequests`

* Refresh Token Grace Period (seconds)

  The time, in seconds, that a refresh token can be reused. This grace period lets OAuth 2.0 clients recover seamlessly if the response from an original refresh token request is not received because of a network problem or other transient issue. During the grace period, the refresh token can be reused multiple times if the network problem persists. When the grace period ends, the refresh token is revoked.

  The refresh token grace period applies only to tokens in a one-to-one storage scheme.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Having a long grace period poses a security risk. You should therefore keep the grace period as small as possible. By default, the grace period cannot exceed 120 seconds. You *can* override this default maximum by setting the [org.forgerock.openam.oauth2.client.graceperiod.disabled](deployment-configuration-reference.html#org.forgerock.openam.oauth2.client.graceperiod.disabled) advanced server property. Note, however, that exceeding the default maximum of 120 seconds is *not* recommended. |

  There is no grace period by default, so the default value is `0`.

- Allow Client Credentials in Token Endpoint Query Parameters

  When this setting is `true`, you can include client credentials in token endpoint requests as query parameters.

  Default value: `false`

  |   |                                                  |
  | - | ------------------------------------------------ |
  |   | Don't change this setting, for security reasons. |

  `amster` attribute: `allowClientCredentialsInTokenRequestQueryParameters`

* Include subname claim in tokens issued by the OAuth2 Provider

  When this setting is `true`, AM adds the `subname` claim to access and ID tokens by default.

  The value of the `subname` claim is the name of the token's subject, for example, `bjensen`, or `myOAuth2Client`.

  Default value: `true`

- Include Client ID Claim In Stateless Access & Refresh Tokens

  When this setting is enabled, AM includes the `client_id` claim in new stateless access and refresh tokens and reads it from existing tokens if present.

  Default value: `true`

* Enable Application Context

  When enabled, this setting makes the application context available in all OAuth 2.0 / OIDC flows through the `oauthApplication` binding in [Scripted Decision node scripts](../am-scripting/scripting-api-node.html#oauthapp-binding).

  This setting can be overridden at the [client level](../am-oauth2/oauth2-register-client.html#enable-application-context-override).

- Accept Audience Parameters in Token Exchange Requests

  If this setting is `false` (default), AM ignores audience parameter values in token exchange requests.

  If this setting is `true`, AM validates audience parameter values in token exchange requests against the values set in the Allowed Resource Server Audience Values property in the client configuration.

  If validation fails, the token exchange request is rejected.

  Find more information in [The `aud` claim](../am-oauth2/token-exchange.html#aud-claim).

  Default value: `false`

* Use token\_introspection claim for JWT

  Specifies whether AM wraps the introspected token's claims inside a `token_introspection` claim in the JWT introspection response, as required by RFC 9701.

  When enabled, AM separates the JWT's own top-level claims (`iss`, `aud`, `iat`) from the introspected token's claims, which appear inside `token_introspection`. The `aud` claim of the introspected token is always included.

  When disabled, AM returns a flat JWT structure and omits the `aud` claim from the response.

  Learn more in [RFC 9701 token\_introspection claim](../am-oauth2/oauth2-introspect-endpoint.html#rfc-9701-token-introspection-claim).

  Default value: `false`

- Allow audience members to introspect tokens

  When enabled, any client whose `client_id` appears anywhere in a token's `aud` (audience) claim can introspect that token, including clients that aren't the issuing client.

  Enable this setting if tokens can have multiple `aud` values, or if you use token exchange with the `audience` request parameter. Resource servers listed in the `aud` claim can then validate tokens presented to them.

  When not enabled, only the issuing client can introspect a token (unless the client has a [special introspection scope](../am-oauth2/oauth2-scopes.html#special-oauth2-scopes)).

  Default value: `false`

### Client Dynamic Registration

The following settings appear on the Client Dynamic Registration tab:

* Require Software Statement for Dynamic Client Registration

  When enabled, a software statement JWT containing at least the `iss` (issuer) claim must be provided when registering an OAuth 2.0 client dynamically.

  Default value: `false`

  `amster` attribute: `dynamicClientRegistrationSoftwareStatementRequired`

* Required Software Statement Attested Attributes

  The client attributes that are required to be present in the software statement JWT when registering an OAuth 2.0 client dynamically. Only applies if Require Software Statements for Dynamic Client Registration is enabled.

  Leave blank to allow any attributes to be present.

  Default value: `redirect_uris`

  `amster` attribute: `requiredSoftwareStatementAttestedAttributes`

* Allow Open Dynamic Client Registration

  Allow clients to register without an access token. If enabled, consider adding some form of rate limiting. For details, refer to [Client Registration](https://openid.net/specs/openid-connect-registration-1_0.html#ClientRegistration) in the OIDC specification.

  Default value: `false`

  `amster` attribute: `allowDynamicRegistration`

* Generate Registration Access Tokens

  Whether to generate Registration Access Tokens for clients that register by using open dynamic client registration. Such tokens let the client access the [Client Configuration Endpoint](https://openid.net/specs/openid-connect-registration-1_0.html#ClientConfigurationEndpoint) as per the OIDC specification. This setting has no effect if Allow Open Dynamic Client Registration is disabled.

  Default value: `true`

  `amster` attribute: `generateRegistrationAccessTokens`

* Scope to give access to dynamic client registration

  Mandatory scope required when registering a new OAuth 2.0 client.

  Default value: `dynamic_client_registration`

  `amster` attribute: `dynamicClientRegistrationScope`

* Dynamic Client Registration Script

  Provide a script to customize dynamic client registration after a successful create, update, or delete operation.

  Default value: `--- Select a script ---`

  `amster` attribute: `dynamicClientRegistrationScript`

### OpenID Connect

The following settings appear on the OpenID Connect tab:

* Overrideable Id\_Token Claims

  List of claims in the ID token that can be overridden in the OIDC Claims script. These should be the subset of the core OIDC claims, such as `aud` or `azp`.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * Learn more about the core OIDC claims in [ID Token data structure](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

  * You can find details about the OIDC script and how to implement a custom scripted plugin in [OIDC claims](../am-oauth2/plugins-user-info-claims.html).

    To override claims, follow the steps described in [Override the audience and issuer claims](../am-oauth2/plugins-user-info-claims.html#example-override-issuer-audience). |

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  `amster` attribute: `overrideableOIDCClaims`

* ID Token Signing Algorithms supported

  Algorithms supported to sign OIDC `id_tokens`.

  AM supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

  * `RS384` - RSASSA-PKCS-v1\_5 using SHA-384.

  * `RS512` - RSASSA-PKCS-v1\_5 using SHA-512.

  * `PS256` - RSASSA-PSS using SHA-256.

  * `PS384` - RSASSA-PSS using SHA-384.

  * `PS512` - RSASSA-PSS using SHA-512.

    Default value:

    ```
    PS384
    ES384
    RS384
    HS256
    HS512
    ES256
    RS256
    HS384
    ES512
    PS256
    PS512
    RS512
    ```

  `amster` attribute: `supportedIDTokenSigningAlgorithms`

* ID Token Encryption Algorithms supported

  Encryption algorithms supported to encrypt OIDC ID tokens to hide their contents.

  AM supports the following ID token encryption algorithms:

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * \` RSA-OAEP-256\` - RSA with OAEP with SHA-256 and MGF-1.

  * \` A128KW\` - AES Key Wrapping with 128-bit key derived from the client secret.

  * \` RSA1\_5\` - RSA with PKCS#1 v1.5 padding.

  * \` A256KW\` - AES Key Wrapping with 256-bit key derived from the client secret.

  * \` dir\` - Direct encryption with AES using the hashed client secret.

  * \` A192KW\` - AES Key Wrapping with 192-bit key derived from the client secret.

    Default value:

    ```
    ECDH-ES+A256KW
    ECDH-ES+A192KW
    RSA-OAEP
    ECDH-ES+A128KW
    RSA-OAEP-256
    A128KW
    A256KW
    ECDH-ES
    dir
    A192KW
    ```

    `amster` attribute: `supportedIDTokenEncryptionAlgorithms`

* ID Token Encryption Methods supported

  Encryption methods supported to encrypt OIDC ID tokens to hide their contents.

  AM supports the following ID token encryption algorithms:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

    Default value:

    ```
    A256GCM
    A192GCM
    A128GCM
    A128CBC-HS256
    A192CBC-HS384
    A256CBC-HS512
    ```

    `amster` attribute: `supportedIDTokenEncryptionMethods`

- Supported Claims

  Set of claims supported by the OIDC `/oauth2/userinfo` endpoint, with translations.

  Claims can be entered as simple strings or pipe separated strings representing the internal claim name, locale, and localized description.

  For example: `name|en|Your full name.`.

  Locale strings are in the format: `language + "" + country + "" + variant`, for example `en`, `en_GB`, or `en_US_WIN`. If the locale and pipe is omitted, the description is displayed to all users that have undefined locales.

  If the description is also omitted, nothing is displayed on the consent page for the claim. For example specifying `family_name|` would allow the claim `family_name` to be used by the client, but would not display it to the user on the consent page when requested.

  `amster` attribute: `supportedClaims`

- OpenID Connect JWT Token Lifetime (seconds)

  The period of time the JWT is valid, in seconds.

  Default value: `3600`

  |   |                                                                  |
  | - | ---------------------------------------------------------------- |
  |   | Don't set a token lifetime greater than 86400 seconds (one day). |

  `amster` attribute: `jwtTokenLifetime`

- OIDC Provider Discovery

  Turns on and off OIDC Discovery endpoint.

  Default value: `false`

  `amster` attribute: `oidcDiscoveryEndpointEnabled`

### Advanced OpenID Connect

The following settings appear on the Advanced OpenID Connect tab:

* Remote JSON Web Key URL

  The Remote URL where the providers JSON Web Key can be retrieved.

  If this setting is not configured, then AM provides a local URL to access the public key of the private key used to sign ID tokens.

  `amster` attribute: `jkwsURI`

* JWT Signing kid Header Mappings

  Map custom `kid` header values for JWTs signed with the signing key to the specified secret alias.

  * Key is the secret alias of the key used to sign the given JWT.

  * Value is the custom `kid` value.

  AM only applies custom `kid` mappings if you set a value for Remote JSON Web Key URL. Use these mappings to guarantee that the `kid` header of a signed JWT references the correct key in a remote JWKS.

  If you don't configure a custom `kid` for a JWT signing key, AM generates a default `kid` value.

  Find more information in [Map custom key IDs to secrets](../am-oidc1/managing-jwk_uri.html#map-custom-kids).

* Idtokeninfo Endpoint Requires Client Authentication

  When enabled, the `/oauth2/idtokeninfo` endpoint requires client authentication if the signing algorithm is set to `HS256`, `HS384`, or `HS512`.

  Default value: `true`

  `amster` attribute: `idTokenInfoClientAuthenticationEnabled`

* Enable "claims\_parameter\_supported"

  If enabled, clients will be able to request individual claims using the `claims` request parameter, as per [section 5.5 of the OIDC specification](http://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter).

  Default value: `false`

  `amster` attribute: `claimsParameterSupported`

* OpenID Connect acr\_values to Auth Chain Mapping

  Maps OIDC ACR values to authentication trees. You can find details in the [acr\_values parameter](http://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) in the OIDC authentication request specification.

  |   |                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Don't configure more than one ACR mapping to the same authentication tree. Doing so can result in misrepresentation of the ACR information in the issued ID token. |

  `amster` attribute: `loaMapping`

* Default ACR values

  Default requested Authentication Context Class Reference values.

  List of strings that specifies the default acr values that the OP is being requested to use for processing requests from this Client, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value in the issued ID Token. The acr Claim is requested as a Voluntary Claim by this parameter. The acr\_values\_supported discovery element contains a list of the acr values supported by this server. Values specified in the acr\_values request parameter or an individual acr Claim request override these default values.

  `amster` attribute: `defaultACR`

* OpenID Connect id\_token amr Values to Auth Module Mappings

  This property was used only for authentication with modules and chains and is no longer documented.

* Always Return Claims in ID Tokens

  If enabled, include scope-derived claims in the `id_token`, even if an access token is also returned that could provide access to get the claims from the `userinfo` endpoint.

  If not enabled, if an access token is requested the client must use it to access the `userinfo` endpoint for scope-derived claims, as they will not be included in the ID token.

  Default value: `false`

  `amster` attribute: `alwaysAddClaimsToToken`

- Enable Session Management

  If this setting is disabled, OIDC session management related endpoints are disabled. When enabled AM stores *ops* tokens corresponding to OIDC sessions in the CTS store and an OIDC session ID in the AM session.

  Default value: `true`

  `amster` attribute: `storeOpsTokens`

- Request Parameter Signing Algorithms Supported

  Algorithms supported to verify signature of Request parameter. AM supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

  Default value:

  ```
  PS384
  ES384
  RS384
  HS256
  HS512
  ES256
  RS256
  HS384
  ES512
  PS256
  PS512
  RS512
  ```

  `amster` attribute: `supportedRequestParameterSigningAlgorithms`

- Request Parameter Encryption Algorithms Supported

  Encryption algorithms supported to decrypt Request parameter.

  AM supports the following ID token encryption algorithms:

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  Default value:

  ```
  ECDH-ES+A256KW
  ECDH-ES+A192KW
  ECDH-ES+A128KW
  RSA-OAEP
  RSA-OAEP-256
  A128KW
  A256KW
  ECDH-ES
  dir
  A192KW
  ```

  `amster` attribute: `supportedRequestParameterEncryptionAlgorithms`

- Request Parameter Encryption Methods Supported

  Encryption methods supported to decrypt Request parameter.

  AM supports the following Request parameter encryption algorithms:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

  Default value:

  ```
  A256GCM
  A192GCM
  A128GCM
  A128CBC-HS256
  A192CBC-HS384
  A256CBC-HS512
  ```

  `amster` attribute: `supportedRequestParameterEncryptionEnc`

- Supported Token Endpoint JWS Signing Algorithms.

  Supported JWS Signing Algorithms for 'private\_key\_jwt' JWT-based authentication method.

  Default value:

  ```
  PS384
  ES384
  RS384
  HS256
  HS512
  ES256
  RS256
  HS384
  ES512
  PS256
  PS512
  RS512
  ```

  `amster` attribute: `supportedTokenEndpointAuthenticationSigningAlgorithms`

- Authorized OIDC SSO Clients

  Clients authorized to use OIDC ID tokens as SSO Tokens.

  Allows clients to act with the full authority of the user. Grant this permission only to trusted clients.

  `amster` attribute: `authorisedOpenIdConnectSSOClients`

- UserInfo Signing Algorithms Supported

  Algorithms supported to verify signature of the UserInfo endpoint. AM supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

  Default value:

  ```
  ES384
  HS256
  HS512
  ES256
  RS256
  HS384
  ES512
  ```

  `amster` attribute: `supportedUserInfoSigningAlgorithms`

- UserInfo Encryption Algorithms Supported

  Encryption algorithms supported by the UserInfo endpoint.

  AM supports the following UserInfo endpoint encryption algorithms:

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * \` RSA-OAEP-256\` - RSA with OAEP with SHA-256 and MGF-1.

  * \` A128KW\` - AES Key Wrapping with 128-bit key derived from the client secret.

  * \` RSA1\_5\` - RSA with PKCS#1 v1.5 padding.

  * \` A256KW\` - AES Key Wrapping with 256-bit key derived from the client secret.

  * \` dir\` - Direct encryption with AES using the hashed client secret.

  * \` A192KW\` - AES Key Wrapping with 192-bit key derived from the client secret.

  Default value:

  ```
  ECDH-ES+A256KW
  ECDH-ES+A192KW
  RSA-OAEP
  ECDH-ES+A128KW
  RSA-OAEP-256
  A128KW
  A256KW
  ECDH-ES
  dir
  A192KW
  ```

  `amster` attribute: `supportedUserInfoEncryptionAlgorithms`

- UserInfo Encryption Methods Supported

  Encryption methods supported by the UserInfo endpoint.

  AM supports the following UserInfo endpoint encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

  Default value:

  ```
  A256GCM
  A192GCM
  A128GCM
  A128CBC-HS256
  A192CBC-HS384
  A256CBC-HS512
  ```

  `amster` attribute: `supportedUserInfoEncryptionEnc`

- Token Introspection Response Signing Algorithms Supported

  Algorithms that are supported for signing the Token Introspection endpoint JWT response.

  AM supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

  * `RS384` - RSASSA-PKCS-v1\_5 using SHA-384.

  * `RS512` - RSASSA-PKCS-v1\_5 using SHA-512.

  * `EdDSA` - EdDSA with SHA-512.

  Default value:

  ```
  PS384
  RS384
  EdDSA
  ES384
  HS256
  HS512
  ES256
  RS256
  HS384
  ES512
  PS256
  PS512
  RS512
  ```

  `amster` attribute: `supportedTokenIntrospectionResponseSigningAlgorithms`

- Token Introspection Response Encryption Algorithms Supported

  Encryption algorithms supported by the Token Introspection endpoint JWT response.

  AM supports the following Token Introspection endpoint encryption algorithms:

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  Default value:

  ```
  ECDH-ES+A256KW
  ECDH-ES+A192KW
  RSA-OAEP
  ECDH-ES+A128KW
  RSA-OAEP-256
  A128KW
  A256KW
  ECDH-ES
  dir
  A192KW
  ```

  `amster` attribute: `supportedTokenIntrospectionResponseEncryptionAlgorithms`

- Token Introspection Response Encryption Methods Supported

  Encryption methods supported by the Token Introspection endpoint JWT response.

  AM supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

  Default value:

  ```
  A256GCM
  A192GCM
  A128GCM
  A128CBC-HS256
  A192CBC-HS384
  A256CBC-HS512
  ```

  `amster` attribute: `supportedTokenIntrospectionResponseEncryptionEnc`

* Authorization Response Signing Algorithms Supported

  Algorithms supported for signing the [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) endpoint JWT response.

  AM supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256

  * `HS384` - HMAC with SHA-384

  * `HS512` - HMAC with SHA-512

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256

  * `RS384` - RSASSA-PKCS1-v1\_5 using SHA-384

  * `RS512` - RSASSA-PKCS1-v1\_5 using SHA-512

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve

  * `PS256` - RSASSA-PSS using SHA-256 and MGF1 with SHA-256

  * `PS384` - RSASSA-PSS using SHA-384 and MGF1 with SHA-384

  * `PS512` - RSASSA-PSS using SHA-512 and MGF1 with SHA-512

  Default value:

  ```
  PS384
  ES384
  RS384
  HS256
  HS512
  ES256
  RS256
  HS384
  ES512
  PS256
  PS512
  RS512
  ```

  `amster` attribute: `supportedAuthorizationResponseSigningAlgorithms`

- Authorization Response Encryption Algorithms Supported

  Algorithms supported for encrypting the [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) JWT response.

  AM supports the following Token Introspection endpoint encryption algorithms:

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

  * `ECDH-ES` - Elliptic Curve Diffie-Hellman Ephemeral Static key agreement using Concat KDF.

  * `ECDH-ES+A128KW` - ECDH-ES using Concat KDF and CEK wrapped with `A128KW`.

  * `ECDH-ES+A192KW` - ECDH-ES using Concat KDF and CEK wrapped with `A192KW`.

  * `ECDH-ES+A256KW` - ECDH-ES using Concat KDF and CEK wrapped with `A256KW`.

  Default value:

  ```
  ECDH-ES+A256KW
  ECDH-ES+A192KW
  RSA-OAEP
  ECDH-ES+A128KW
  RSA-OAEP-256
  A128KW
  A256KW
  ECDH-ES
  dir
  A192KW
  ```

  `amster` attribute: `supportedAuthorizationResponseEncryptionAlgorithms`

* Authorization Response Encryption Methods Supported

  Methods supported for encrypting the [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) JWT response.

  AM supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

  Default value:

  ```
  A256GCM
  A192GCM
  A128GCM
  A128CBC-HS256
  A192CBC-HS384
  A256CBC-HS512
  ```

  `amster` attribute: `supportedAuthorizationResponseEncryptionEnc`

* Include all kty and alg combinations in jwks\_uri

  By default only distinct kid entries are returned in the jwks\_uri and the alg property is not included. Enabling this flag will result in duplicate kid entries, each one specifying a different kty and alg combination ([RFC7517 distinct key KIDs](https://www.rfc-editor.org/rfc/rfc7517.html#section-4.5)).

  Default value: `false`

  `amster` attribute: `includeAllKtyAlgCombinationsInJwksUri`

- Use Force Authentication for `prompt=login`

  If you specify the `prompt=login` parameter in the URL, AM forces the end user to authenticate even if they already have a valid session.

  If this property is `false` (default), AM destroys the existing session and creates a new session after reauthentication.

  If this property is `true`, AM performs a [session upgrade](../am-sessions/session-upgrade.html) on reauthentication.

  Default value: `false`

- Use Force Authentication for max\_age

  This property applies only to reauthentication triggered by the Default Max Age property of an OAuth 2.0 client.

  If this property is `false` and the user requests authorization after the `max_age` has passed, AM destroys the existing session and creates a new session after reauthentication.

  If this property is `true` and the user requests authorization after the `max_age` has passed, AM performs a [session upgrade](../am-sessions/session-upgrade.html) on reauthentication.

  Default value: `false`

### Device Flow

The following settings appear on the Device Flow tab:

* Verification URL

  The URL that the user will be instructed to visit to complete their OAuth 2.0 login and consent when using the device code flow.

  `amster` attribute: `verificationUrl`

* Device Completion URL

  The URL that the user will be sent to on completion of their OAuth 2.0 login and consent when using the device code flow.

  `amster` attribute: `completionUrl`

* Device Code Lifetime (seconds)

  The lifetime of the device code, in seconds.

  Default value: `300`

  `amster` attribute: `deviceCodeLifetime`

* Device Polling Interval

  The polling frequency for devices waiting for tokens when using the device code flow.

  Default value: `5`

  `amster` attribute: `devicePollInterval`

* User Code Character Length

  The number of characters in the generated user code.

  Default value: `8`

  `amster` attribute: `deviceUserCodeLength`

* User Code Character Set

  The set of characters to be used to generate a user code.

  Consider limitations of low resolution mobile devices when defining a character sets. For example, the OAuth 2.0 Device Grant specification recommends removing characters that can be easily confused, such as "0" and "O" or "1", "l" and "I". You can find additional examples in [RFC 8628](https://www.rfc-editor.org/rfc/rfc8628.html#section-6.1).

  Default value: `234567ACDEFGHJKLMNPQRSTWXYZabcdefhijkmnopqrstwxyz`

  `amster` attribute: `deviceUserCodeCharacterSet`

- Allow unauthenticated user code entry

  Realm-level setting that corresponds to the *global* [OAuth 2.0 allow unauthenticated user code entry](#global-allow-unauthenticate-user-code-entry) setting on the Global Attributes tab.

  If enabled, during an OAuth 2.0 device code authentication flow, users can access and input a user code without first logging in.

  If you set the value in the global service configuration (on the Global Attributes tab) *and* in the realm service configuration (on the Device Flow tab), the realm-level setting takes precedence. If AM can't determine the realm value (for example, if the realm isn't provided in the verification URL), it uses the value set on the Global Attributes tab.

  Default value: `false`

  `amster` attribute: `realmAllowUnauthorisedAccessToUserCodeForm`

### Consent

The following settings appear on the Consent tab:

* Saved Consent Attribute Name

  Name of a multi-valued attribute on resource owner profiles where AM can save authorization consent decisions.

  When the resource owner chooses to save the decision to authorize access for a client application, then AM updates the resource owner's profile to avoid having to prompt the resource owner to grant authorization when the client issues subsequent authorization requests.

  `amster` attribute: `savedConsentAttribute`

* Allow Clients to Skip Consent

  If enabled, clients can be configured so that the resource owner won't be asked for consent during authorization flows.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  Default value: `false`

  `amster` attribute: `clientsCanSkipConsent`

* Enable Remote Consent

  Enables consent to be gathered by a separate service.

  This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

  Default value: `false`

  `amster` attribute: `enableRemoteConsent`

* Remote Consent Service ID

  The ID of an existing remote consent service agent.

  The possible values for this property are:

  * `[Empty]`

    This setting can be overridden at the client level. Learn more in [client profile configuration](../am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

    `amster` attribute: `remoteConsentServiceId`

* Remote Consent Service Request Signing Algorithms Supported

  Algorithms supported to sign consent\_request JWTs for Remote Consent Services.

  AM supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

    Default value:

    ```
    PS384
    ES384
    RS384
    HS256
    HS512
    ES256
    RS256
    HS384
    ES512
    PS256
    PS512
    RS512
    ```

    `amster` attribute: `supportedRcsRequestSigningAlgorithms`

* Remote Consent Service Request Encryption Algorithms Supported

  Encryption algorithms supported to encrypt Remote Consent Service requests.

  AM supports the following encryption algorithms:

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

    Default value:

    ```
    ECDH-ES+A256KW
    ECDH-ES+A192KW
    RSA-OAEP
    ECDH-ES+A128KW
    RSA-OAEP-256
    A128KW
    A256KW
    ECDH-ES
    dir
    A192KW
    ```

    `amster` attribute: `supportedRcsRequestEncryptionAlgorithms`

* Remote Consent Service Request Encryption Methods Supported

  Encryption methods supported to encrypt Remote Consent Service requests.

  AM supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

    Default value:

    ```
    A256GCM
    A192GCM
    A128GCM
    A128CBC-HS256
    A192CBC-HS384
    A256CBC-HS512
    ```

    `amster` attribute: `supportedRcsRequestEncryptionMethods`

* Remote Consent Service Response Signing Algorithms Supported

  Algorithms supported to verify signed consent\_response JWT from Remote Consent Services.

  AM supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

    Default value:

    ```
    PS384
    ES384
    RS384
    HS256
    HS512
    ES256
    RS256
    HS384
    ES512
    PS256
    PS512
    RS512
    ```

    `amster` attribute: `supportedRcsResponseSigningAlgorithms`

* Remote Consent Service Response Encryption Algorithms Supported

  Encryption algorithms supported to decrypt Remote Consent Service responses.

  AM supports the following encryption algorithms:

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * \` RSA-OAEP\` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * \` RSA-OAEP-256\` - RSA with OAEP with SHA-256 and MGF-1.

  * \` A128KW\` - AES Key Wrapping with 128-bit key derived from the client secret.

  * \` A192KW\` - AES Key Wrapping with 192-bit key derived from the client secret.

  * \` A256KW\` - AES Key Wrapping with 256-bit key derived from the client secret.

  * \` dir\` - Direct encryption with AES using the hashed client secret.

    Default value:

    ```
    ECDH-ES+A256KW
    ECDH-ES+A192KW
    ECDH-ES+A128KW
    RSA-OAEP
    RSA-OAEP-256
    A128KW
    A256KW
    ECDH-ES
    dir
    A192KW
    ```

    `amster` attribute: `supportedRcsResponseEncryptionAlgorithms`

* Remote Consent Service Response Encryption Methods Supported

  Encryption methods supported to decrypt Remote Consent Service responses.

  AM supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

    Default value:

    ```
    A256GCM
    A192GCM
    A128GCM
    A128CBC-HS256
    A192CBC-HS384
    A256CBC-HS512
    ```

    `amster` attribute: `supportedRcsResponseEncryptionMethods`

### CIBA

The following settings appear on the CIBA tab:

* Back Channel Authentication ID Lifetime (seconds)

  The time back channel authentication request id is valid for, in seconds.

  Default value: `600`

  `amster` attribute: `cibaAuthReqIdLifetime`

* Polling Wait Interval (seconds)

  The minimum amount of time in seconds that the Client should wait between polling requests to the token endpoint

  Default value: `2`

  `amster` attribute: `cibaMinimumPollingInterval`

* Signing Algorithms Supported

  Algorithms supported to sign the CIBA request parameter.

  AM supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `PS256` - RSASSA-PSS using SHA-256.

    Default value:

    ```
    ES256
    PS256
    ```

    `amster` attribute: `supportedCibaSigningAlgorithms`

### AI Agents

The following settings appear on the AI Agents tab:

* Enable AI Agents

  Enable the [AI agents](../am-oauth2/ai-agents.html) functionality for this OAuth 2.0 provider.

  You must reload the page to display the AI Agents menu item under Applications > OAuth 2.0.

  Default value: `false`

* AI Agent Managed Object Name

  The name of the managed object that represents the AI agent in IDM, for example `managed/alpha_AIAgent`.

* AI Agent Privilege Managed Object Name

  The name of the managed object that represents the AI Agent Privileges in IDM, for example `managed/alpha_AIAgentPrivilege`.

* AI Agent DCR Managed Object Mapping

  Maps attributes of dynamically registered AI agent clients (DCR clients) to IDM managed object attributes.

  The mapped managed object is specified in AI Agent Managed Object Name.

  This mapping applies only to DCR clients. For manually registered clients, managed object attributes are explicitly provided in the `aiAgentIdentityAttributes` request attribute.

  The key must be a `Client Metadata` value, as defined in the OAuth 2.0 Dynamic Client Registration Protocol specification ([RFC 7591](https://www.rfc-editor.org/rfc/rfc7591.html)), for example, `client_name`, `client_id`.

  Locale-specific keys are only mapped if they're explicitly defined. For example, if `client_name` is mapped but the request contains `client_name#en`, the mapping isn't applied. To support localized values, you must define an explicit mapping for the tagged attribute, for example, `client_name#en`.

  You can map multiple client attributes to the same IDM object attribute. Provide the client attributes in order of priority because only the first identified attribute is used. For example, if you map `client_name#en`, `client_name`, and `client_id` to a `name` object attribute, AM maps the first attribute present.

  The mapping syntax is `key|value`, where `value` supports pointer-style syntax.

  Examples:

  ```
  client_name|name
  client_name#en|name
  client_id|name
  client_name|/customAttributes/name
  client_name#en|customAttributes/name/en
  ```

### Plugins

The Plugins settings are used to configure the following supported OAuth 2.0 plugin extension points:

* Access Token Modification

* OIDC Claims

* Scope Evaluation

* Scope Validation

* Authorize Endpoint Data Provider

Each plugin is configured using three different attributes:

* `Plugin Type`:

  This value can be either `SCRIPTED` to run a custom script, or `JAVA` for a custom implementation class.

* `Script`:

  The script that is run for `SCRIPTED` plugin types.

* `Implementation Class`:

  The class that is invoked for `JAVA` plugin types. The class must implement the appropriate Java interface in the `org.forgerock.oauth2.core.plugins` package for the plugin.

  |   |                                                                                                                                                                                             |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | These plugin settings can be overridden at the client level. Learn more in [OAuth 2.0 provider overrides](../am-oauth2/oauth2-register-client.html#configure-oauth2-oidc-client-overrides). |

The following settings appear on the Plugins tab:

* Access Token Modification Plugin Type

  Default value: `SCRIPTED`

  `amster` attribute: `accessTokenModificationPluginType`

* Access Token Modification Script

  This script is run when issuing an access token. The script lets you modify the token, for example, by altering the data fields, before it is persisted or returned to the client.

  The script is run if `Access Token Modification Plugin Type` is set to `SCRIPTED`.

  Learn more in [Access token modification](../am-oauth2/modifying-access-tokens-scripts.html).

  Default value: `OAuth2 Access Modification Script`

  `amster` attribute: `accessTokenModificationScript`

* Access Token Modifier Plugin Implementation Class

  The Java class that provides the custom implementation for the access token modifier plugin interface, `org.forgerock.oauth2.core.plugins.AccessTokenModifier`. This class is invoked when `Access Token Modification Plugin Type` is set to `JAVA`.

  Default value: `[Empty]`

  `amster` attribute: `accessTokenModificationClass`

* OIDC Claims Plugin Type

  Default value: `SCRIPTED`

  `amster` attribute: `oidcClaimsPluginType`

* OIDC Claims Script

  This script is run when issuing an ID token or during a request to the `/userinfo` OIDC endpoint. Use this script to retrieve claim values based on an issued access token.

  The script is run if `OIDC Claims Plugin Type` is set to `SCRIPTED`.

  Default value: `OIDC Claims Script`

  `amster` attribute: `oidcClaimsScript`

* OIDC Claims Plugin Implementation Class

  The Java class that provides the custom implementation for the OIDC claims plugin interface, `org.forgerock.oauth2.core.plugins.UserInfoClaimsPlugin`. This class is invoked when `OIDC Claims Plugin Type` is set to `JAVA`.

  Default value: `[Empty]`

  `amster` attribute: `oidcClaimsClass`

* Scope Evaluation Plugin Type

  Default value: `JAVA`

  `amster` attribute: `evaluateScopePluginType`

* Scope Evaluation Script

  This script retrieves and evaluates the scope information for an OAuth 2.0 access token.

  The script lets you populate the scopes with profile attribute values. For example, if one of the scopes is `mail`, AM sets `mail` to the resource owner's email address in the token information returned.

  Default value: `--- Select a script ---`

  `amster` attribute: `evaluateScopeScript`

* Scope Evaluation Plugin Implementation Class

  The Java class that provides the custom implementation for the evaluate scope plugin interface: org.forgerock.oauth2.core.plugins.ScopeEvaluator.

  Default value: `org.forgerock.oauth2.core.plugins.registry.DefaultScopeEvaluator`

  `amster` attribute: `evaluateScopeClass`

* Scope Validation Plugin Type

  Default value: `JAVA`

  `amster` attribute: `validateScopePluginType`

* Scope Validation Script

  This script validates and customizes the set of requested scopes for authorize, access token, refresh token, and back channel authorize requests.

  Default value: `--- Select a script ---`

  `amster` attribute: `validateScopeScript`

* Scope Validation Plugin Implementation Class

  The Java class that provides the custom implementation for the evaluate scope plugin interface: org.forgerock.oauth2.core.plugins.ScopeValidator.

  Default value: `org.forgerock.oauth2.core.plugins.registry.DefaultScopeValidator`

  `amster` attribute: `validateScopeClass`

* Authorize Endpoint Data Provider Plugin Type

  Default value: `JAVA`

  `amster` attribute: `authorizeEndpointDataProviderPluginType`

* Authorize Endpoint Data Provider Script

  Use this script to retrieve additional data from an authorization request, such as data from the user's session or from an external service.

  Default value: `--- Select a script ---`

  `amster` attribute: `authorizeEndpointDataProviderScript`

* Authorize Endpoint Data Provider Plugin Implementation Class

  The Java class that provides the custom implementation for the evaluate scope plugin interface: org.forgerock.oauth2.core.plugins.AuthorizeEndpointDataProvider.

  Default value: `org.forgerock.oauth2.core.plugins.registry.DefaultEndpointDataProvider`

  `amster` attribute: `authorizeEndpointDataProviderClass`

* Access Token Enricher Plugin Implementation Class

  The class that provides the custom implementation for the access token enricher plugin interface.

  The access token enricher plugin interface is deprecated and will be removed in a future release.

  Default value: `org.forgerock.oauth2.core.plugins.registry.DefaultAccessTokenEnricher`

  `amster` attribute: `accessTokenEnricherClass`

* Device Code Flow User Code Generator Implementation Class

  The class that provides the custom implementation for generating user codes for the device code flow.

  To override the default implementation, create a Java class that implements the `UserCodeGenerator` interface, and set this property to the fully qualified class name.

  Default value: `org.forgerock.oauth2.core.plugins.registry.DefaultUserCodeGenerator`

  `amster` attribute: `userCodeGeneratorClass`

## PingOne Worker service

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Worker Service requires a configured [OAuth2 provider](#global-oauth-oidc) service in your AM server.Learn more in [Authorization server configuration](../am-oauth2/oauth2-configure-authz.html). |

### Configuration

The following settings appear on the Configuration tab:

* Enabled

  Enables the service.

### Secondary Configurations

This service has the following Secondary Configurations:

* Client ID

  Client ID of the worker application in PingOne.

  Find more information in [Adding a worker application for the PingOne Authorize service](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_worker_app.html).

* Client Secret Label Identifier

  AM uses this identifier to create a specific secret label for the client secret of the worker application.

  The secret label uses the template `am.services.pingone.worker.identifier.clientsecret` where identifier is the Client Secret Label Identifier value.

  This field can only contain characters `a-z`, `A-Z`, `0-9`, and `.` and can't start or end with a period.

  Find information on mapping the client secret to the secret label in [Map and rotate secrets](../security/secret-mapping.html).

* Environment ID

  The environment that contains the worker application in PingOne.

* PingOne API Server URL

  The regional base URL of the PingOne ***API*** server.

  Enter one of the following:

  * `https://api.pingone.com/v1` - for the North America region (excluding Canada)

  * `https://api.pingone.ca/v1` - for the Canada region

  * `https://api.pingone.eu/v1` - for the European Union region

  * `https://api.pingone.asia/v1` - for the Asia-Pacific region

  Default: `https://api.pingone.com/v1`

* PingOne Authorization Server URL

  The regional base URL for the PingOne ***authorization*** server.

  Enter one of the following:

  * `https://auth.pingone.com` - for the North America region (excluding Canada)

  * `https://auth.pingone.ca` - for the Canada region

  * `https://auth.pingone.eu` - for the European Union region

  * `https://auth.pingone.asia` - for the Asia-Pacific region

  Default: `https://auth.pingone.com`

#### Test the connection

After you configure the worker service, test the connection from AM to PingOne to verify the details. When you test the connection, AM attempts to get an access token from PingOne using the worker service configuration.

There are two ways to test the connection:

* In the AM admin UI

  Click the Save and Test Connection button to test the connection from AM to PingOne.

  A Test Results window indicates whether the connection was successful or not, and displays the environment ID and URLs used in the test. If the connection fails, check the worker service configuration.

* Over REST

  Use the `testConnection` action on the `realm-config/services/pingOneWorkerService/workers/pingone-worker-service-name` endpoint to test the connection from AM to PingOne. If the connection fails, check the worker service configuration.

  For example:

  ```none
  $ curl \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Accept-API-Version: resource=1.0' \
  --header 'iPlanetDirectoryPro: AQIC5wM…​TU3OQ*' \
  'https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/services/pingOneWorkerService/workers/pingone-worker-service-name?_action=testConnection'
  ```

  * If you get a `200 OK` response, the connection is successful.

  * If you get the following `400 Bad Request` response, the connection has failed:

    ```json
    {
        "code": 400,
        "reason": "Bad Request",
        "message": "Failed to retrieve PingOne Worker access token"
    }
    ```

## Platform

`amster` service name: `Platform`

The following settings are available in this service:

* Platform Locale

  Set the fallback locale used when the user locale cannot be determined.

  Default value: `en_US`

  `amster` attribute: `locale`

- Cookie Domains

  Set the list of domains into which AM writes cookies.

  If you set multiple cookie domains, AM only sets the cookie in the domain the client uses to access AM. If you do not set a value here, the `Set-Cookie` response header will not include a `Domain` attribute. In this case, AM sets a host-only cookie rather than a domain cookie.

  |   |                                                                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Because host-only cookies are more secure than domain cookies, you *should* use host-only cookies unless you have a good business case for using domain cookies. In general, domain cookies are required only if your Web or Java agent uses an SSO tracking cookie for SSO. |

  Default value: `openam.example.com`

  `amster` attribute: `cookieDomains`

## Policy configuration

`amster` service name: `PolicyConfiguration`

### Global attributes

The following settings appear on the Global Attributes tab:

* Resource Comparator

  AM uses resource comparators to match resources specified in policy rules. When setting comparators on the command line, separate fields with `|` characters.

  Default value: `serviceType=iPlanetAMWebAgentService|class=com.sun.identity.policy.plugins.HttpURLResourceName|wildcard=|oneLevelWildcard=--|delimiter=/|caseSensitive=false`

  `amster` attribute: `resourceComparators`

* Continue Evaluation on Deny Decision

  If no, then AM stops evaluating policy as soon as it reaches a deny decision.

  Default value: `false`

  `amster` attribute: `continueEvaluationOnDeny`

* Realm Alias Referrals

  If yes, then AM allows creation of policies for HTTP and HTTPS resources whose FQDN matches the DNS alias for the realm even when no referral policy exists.

  Default value: `false`

  `amster` attribute: `realmAliasReferrals`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Primary LDAP Server

  Configuration directory server host:port that AM searches for policy information. The default value is the directory server specified during setup.

  |   |                                                                                                                                                                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Configure the directory server settings if you want to use an identity store in an LDAP filter condition in a policy.These LDAP settings are only applicable to the identity store of the LDAP accounts or groups used in the filter condition, and don't affect how other data, such as policies or policy subjects, is stored. |

  Format: `local AM server name | hostname:port`

  Multiple entries must be prefixed by local server name. Make sure to place the multiple entries on a single line and separate the hostname:port URLs with a space.

  For example, am.example.com|ds.example.com:1389 ds.example.com:2389

  `amster` attribute: `ldapServer`

* LDAP Users Base DN

  Base DN for LDAP Users subject searches.

  Default value: `ou=identities`

  `amster` attribute: `usersBaseDn`

* LDAP Bind DN

  Bind DN to connect to the directory server for policy information.

  If you enable mTLS, AM ignores this property. Default value: `uid=am-identity-bind-account,ou=admins,ou=identities`

  `amster` attribute: `bindDn`

* LDAP Bind Password

  Bind password to connect to the directory server for policy information.

  If you enable mTLS, AM ignores this property.

  `amster` attribute: `bindPassword`

* LDAP Organization Search Filter

  Search filter to match organization entries.

  Default value: `(objectclass=sunismanagedorganization)`

  `amster` attribute: `realmSearchFilter`

* LDAP Users Search Filter

  Search filter to match user entries.

  Default value: `(objectclass=inetorgperson)`

  `amster` attribute: `usersSearchFilter`

* LDAP Users Search Scope

  Search scope to find user entries.

  The possible values for this property are:

  * `SCOPE_BASE`

  * `SCOPE_ONE`

  * `SCOPE_SUB`

  Default value: `SCOPE_SUB`

  `amster` attribute: `usersSearchScope`

* LDAP Users Search Attribute

  Naming attribute for user entries.

  Default value: `uid`

  `amster` attribute: `usersSearchAttribute`

* Maximum Results Returned from Search

  Search limit for LDAP searches.

  Default value: `100`

  `amster` attribute: `maximumSearchResults`

* Search Timeout

  Time after which AM returns an error for an incomplete search, in seconds.

  Default value: `5`

  `amster` attribute: `searchTimeout`

* LDAP SSL/TLS

  If enabled, AM connects securely to the directory server. This requires that you install the directory server certificate.

  Default value: `true`

  `amster` attribute: `sslEnabled`

* LDAP Connection Pool Minimum Size

  Minimum number of connections in the pool.

  Default value: `1`

  `amster` attribute: `connectionPoolMinimumSize`

* LDAP Connection Pool Maximum Size

  Maximum number of connections in the pool.

  Default value: `10`

  `amster` attribute: `connectionPoolMaximumSize`

* Heartbeat Interval

  Specifies how often should AM send a heartbeat request to the directory.

  Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle.

  Default value: `10`

  `amster` attribute: `policyHeartbeatInterval`

* Heartbeat Unit

  Defines the time unit corresponding to the Heartbeat Interval setting.

  Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle.

  The possible values for this property are:

  * Label: **second** (Value: `SECONDS`)

  * Label: **minute** (Value: `MINUTES`)

  * Label: **hour** (Value: `HOURS`)

  Default value: `SECONDS`

  `amster` attribute: `policyHeartbeatTimeUnit`

* Subjects Result Time to Live

  Maximum time that AM caches a subject result for evaluating policy requests, in minutes. A value of `0` prevents AM from caching subject evaluations for policy decisions.

  Default value: `10`

  `amster` attribute: `subjectsResultTTL`

* User Alias

  If enabled, AM can evaluate policy for remote users aliased to local users.

  Default value: `false`

  `amster` attribute: `userAliasEnabled`

* Check resources exist when Resource Server is updated

  Check all registered resources exist when updating Resource Server.

  Policy Set will check each registered Resource Types one by one against config datastore if enabled. Consider disabling this option if you have large number of Resource Types registered to a Policy Set.

  Default value: `true`

  `amster` attribute: `checkIfResourceTypeExists`

* mTLS Enabled

  Enables mutual TLS (mTLS) authentication between AM and this datastore.

  When you enable mTLS, you must also:

  * Enable LDAP SSL/TLS.

  * Map the secret label `am.policy.configuration.serice.mtls.cert` to the alias you want to use for mTLS authentication to this store.

AM ignores the LDAP Bind DN and LDAP Bind Password when you enable mTLS.

## Push Notification service

`amster` service name: `PushNotification`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* SNS Access Key ID

  Amazon Simple Notification Service Access Key ID. Learn more in [Create an AWS (Push Auth) Credential](https://backstage.pingidentity.com/knowledge/backstagehelp/article/a92326771#aws) in the Knowledge Base. You must log into Backstage to read this article.

  For example, you might set this property to: AKIAIOSFODNN7EXAMPLE

  `amster` attribute: `accessKey`

* SNS Access Key Secret

  Amazon Simple Notification Service Access Key Secret. Learn more in [Create an AWS (Push Auth) Credential](https://backstage.pingidentity.com/knowledge/backstagehelp/article/a92326771#aws) in the Knowledge Base. You must log into Backstage to read this article.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For greater security, you can store this secret in a [secret store](../security/secret-stores.html), instead of in the configuration.Map the secret to the secret label `am.services.pushnotification.sns.accesskey.secret`.If a secret is mapped to this secret label, AM uses that secret and ignores the value of the SNS Access Key Secret property.If a secret is mapped to this secret label and AM can't locate the secret, it falls back to the value of the SNS Access Key Secret property. |

  `amster` attribute: `secret`

* SNS Endpoint for APNS

  The Simple Notification Service endpoint in Amazon Resource Name format, used to send push messages to the Apple Push Notification Service (APNS).

  For example, you might set this property to: arn:aws:sns:us-east-1:1234567890:app/APNS/production

  `amster` attribute: `appleEndpoint`

* SNS Endpoint for GCM

  The Simple Notification Service endpoint in Amazon Resource Name format, used to send push messages over Google Cloud Messaging (GCM).

  For example, you might set this property to: arn:aws:sns:us-east-1:1234567890:app/GCM/production

  `amster` attribute: `googleEndpoint`

* SNS Client Region

  Region of your registered Amazon Simple Notification Service client. For more information, see <https://docs.aws.amazon.com/general/latest/gr/rande.html>.

  The possible values for this property are:

  * `us-gov-west-1`

  * `us-east-1`

  * `us-west-1`

  * `us-west-2`

  * `eu-west-1`

  * `eu-west-2`

  * `eu-central-1`

  * `ap-southeast-1`

  * `ap-southeast-2`

  * `ap-southeast-3`

  * `ap-northeast-1`

  * `ap-northeast-2`

  * `sa-east-1`

  * `ca-central-1`

  * `cn-north-1`

  Default value: `us-east-1`

  `amster` attribute: `region`

* Message Transport Delegate Factory

  The fully qualified class name of the factory responsible for creating the PushNotificationDelegate. The class must implement `org.forgerock.openam.services.push.PushNotificationDelegate`.

  Default value: `org.forgerock.openam.services.push.sns.SnsHttpDelegateFactory`

  `amster` attribute: `delegateFactory`

* Response Cache Duration

  The minimum lifetime to keep unanswered message records in the message dispatcher cache, in seconds. To keep unanswered message records indefinitely, set this property to `0`.

  Default value: `120`

  `amster` attribute: `mdDuration`

* Response Cache Concurrency

  Level of concurrency to use when accessing the message dispatcher cache. Defaults to `16`, and must be greater than `0`. Choose a value to accommodate as many threads as will ever concurrently access the message dispatcher cache.

  Default value: `16`

  `amster` attribute: `mdConcurrency`

* Response Cache Size

  Maximum size of the message dispatcher cache, in number of records. If set to `0` the cache can grow indefinitely. If the number of records that need to be stored exceeds this maximum, then older items in the cache will be removed to make space.

  Default value: `10000`

  `amster` attribute: `mdCacheSize`

## RADIUS server

`amster` service name: `RadiusServer`

### Configuration

The following settings appear on the Configuration tab:

* Enabled

  Lets the AM RADIUS server listen for requests on the listener port, and handle the requests.

  The possible values for this property are:

  * `NO`

  * `YES`

  Default value: `NO`

  `amster` attribute: `radiusListenerEnabled`

* Listener Port

  The UDP port on which the AM RADIUS server listens for incoming `Access-Request` packets.

  According to the RADIUS Authentication Specification, [RFC 2865](https://www.rfc-editor.org/info/rfc2865), the officially assigned port number for RADIUS is `1812`. Specify a value from `1024` to `65535`. All client requests are handled through the same port.

  Default value: `1812`

  `amster` attribute: `radiusServerPort`

* Thread Pool Core Size

  When a RADIUS request is received and fewer than `corePoolSize` threads are running, a new thread is created to handle the request, even if other worker threads are idle. If there are more than Thread Pool Core Size but less than Thread Pool Max Size threads running, a new thread is created only if the queue is full. By setting Thread Pool Core Size and Thread Pool Max Size to the same value, you create a fixed-size thread pool. Specify a value from `1` to `100`.

  Default value: `1`

  `amster` attribute: `radiusThreadPoolCoreSize`

* Thread Pool Max Size

  Maximum number of threads allowed in the pool. This setting is used in conjunction with Thread Pool Core Size.

  Default value: `10`

  `amster` attribute: `radiusThreadPoolMaxSize`

* Thread Pool Keep-Alive Seconds

  If the pool currently has more than Thread Pool Core Size threads, excess threads are terminated if they've been idle for more than the Keep-Alive Seconds. Specify a value from `1` to `3600`.

  Default value: `10`

  `amster` attribute: `radiusThreadPoolKeepaliveSeconds`

* Thread Pool Queue Size

  The number of requests that can be queued for the pool before further requests are silently dropped. This setting is used in conjunction with Thread Pool Core Size and Thread Pool Max Size. Specify a value from `1` to `1000`.

  Default value: `20`

  `amster` attribute: `radiusThreadPoolQueueSize`

### Secondary configurations

Configure RADIUS clients that connect to the RADIUS server. You can create multiple client configurations.

#### radiusClient

* Client IP Address

  The IP Address of the client.

  [Section 5.4 of the RADIUS Authentication Specification, RFC 2865](https://www.rfc-editor.org/rfc/rfc2865.html#section-5.4), indicates that the source IP address of the `Access-Request` packet *MUST* be used to identify a configured client, and determine the shared secret to use for decrypting the User-Password field.

  This property should hold the source IP address of the client. This should match the value obtained from Java's `InetSocketAddress.getAddress().toString()` function.

  To verify the value, send an `Access-Request` packet to AM's RADIUS port and watch for a message stating: `"No Defined RADIUS Client matches IP address '/127.0.0.1'. Dropping request."`. The value used in this property should match the IP address returned in the single quotes.

  Default value: `/127.0.0.1`

  `amster` attribute: `clientIpAddress`

* Client Secret

  The secret shared between the RADIUS server and the client.

  AM uses this secret to decrypt the `User-Password` attribute in incoming `Access-Request` packets. Make sure the same secret is configured on the RADIUS client.

  `amster` attribute: `clientSecret`

* Log Packet Contents for this Client

  Indicates if full packet contents should be output to the log.

  When troubleshooting issues with RADIUS it is helpful to know what was received in a given packet. Enable this option to log packet contents in a human readable format. The USER\_PASSWORD field is obfuscated with asterisks in the logs. Only enable this option for troubleshooting because it adds significant content to logs and slows processing. Learn more in [Troubleshooting](../am-authentication/radius-troubleshooting.html).

  Default value: `NO`

  `amster` attribute: `clientPacketsLogged`

* Handler Class

  The fully qualified name of a class to handle incoming RADIUS `Access-Request` packets for this client.

  This class must implement the `org.forgerock.openam.radius.server.spi.AccessRequestHandler` interface. AM creates an instance of this class for each new request to handle the incoming packet and provide a response.

  Default value: `org.forgerock.openam.radius.server.spi.handlers.OpenAMAuthHandler`

  `amster` attribute: `handlerClass`

* Handler Class Configuration Properties

  Properties needed by the handler class for its configuration.

  Use these properties to specify the authentication journey for the RADIUS client.

  For example, to use an authentication tree named `RADIUS-ClientA-Journey` in the `alpha` realm, set the properties as follows:

  ```properties
  realm=/alpha
  tree=RADIUS-ClientA-Journey
  ```

  |   |                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------- |
  |   | You can only specify one tree. Additionally, if you specify both a tree and a chain, the tree always takes precedence. |

  These properties are provided to the handler through its `init` method. If these values change, the next handler instance created for an incoming request receives the updated values. Each entry should be a key-value pair separated by an equals sign (`=`).

  Default value: `realm=/` and `chain=ldapService`

  `amster` attribute: `handlerConfig`

* Require Message-Authenticator Attribute

  Indicates if the RADIUS server requires the `Message-Authenticator` attribute in the `Access-Request` request packet and whether the RADIUS server provides this attribute in the `Access-Accept`, `Access-Reject` and `Access-Challenge` responses.

  You can use this attribute to verify incoming RADIUS access requests to prevent spoofing.

  If you enable this property, the RADIUS server expects the `Access-Request` to contain a valid `Message-Authenticator` attribute (as defined in [RFC 3579](https://datatracker.ietf.org/doc/html/rfc3579#section-3.2)). If the attribute isn't present or is invalid, AM silently drops the `Access-Request`.

  Also, if you enable this property, the RADIUS server provides the `Message-Authenticator` attribute in its `Access-Accept`, `Access-Reject` and `Access-Challenge` responses.

  Default: Enabled

## REST APIs

`amster` service name: `RestApis`

The following settings are available in this service:

* Default Resource Version

  The API resource version to use when the REST request does not specify an explicit version.

  The possible values for this property are:

  * `Latest`. If an explicit version is not specified, the latest resource version of an API is used.

  * `Oldest`. If an explicit version is not specified, the oldest supported resource version of an API is used. Note that since APIs may be deprecated and fall out of support, the oldest *supported* version may not be the first version.

  * `None`. If an explicit version is not specified, the request will not be handled and an error status is returned.

  Default value: `Latest`

  `amster` attribute: `defaultVersion`

* Warning Header

  Whether to include a warning header in the response to a request which fails to include the `Accept-API-Version` header.

  Default value: `true`

  `amster` attribute: `warningHeader`

* API Descriptions

  Whether API Explorer and API Docs are enabled in AM and how the documentation for them is generated. Dynamic generation includes descriptions from any custom services and authentication nodes you have added. Static generation only includes services and authentication nodes that were present when AM was built. The dynamic documentation generation might not work in some application containers.

  The possible values for this property are:

  * Label: **Enabled with Dynamic Documentation** (Value: `DYNAMIC`)

  * Label: **Enabled with Static Documentation** (Value: `STATIC`)

  * `DISABLED`

  Default value: `STATIC`

  `amster` attribute: `descriptionsState`

* Default Protocol Version

  The API protocol version to use when a REST request does not specify an explicit version. Choose from:

  The possible values for this property are:

  * `Oldest`. If an explicit version is not specified, the oldest protocol version is used.

  * `Latest`. If an explicit version is not specified, the latest protocol version is used.

  * `None`. If an explicit version is not specified, the request will not be handled and an error status is returned.

  Default value: `Latest`

  `amster` attribute: `defaultProtocolVersion`

* Enable CSRF Protection

  If enabled, all non-read/query requests will require the X-Requested-With header to be present.

  Requiring a non-standard header ensures requests can only be made via methods (XHR) that have stricter same-origin policy protections in Web browsers, preventing Cross-Site Request Forgery (CSRF) attacks. Without this filter, cross-origin requests are prevented by the use of the application/json Content-Type header, which is less robust.

  Default value: `true`

  `amster` attribute: `csrfFilterEnabled`

## Remote Consent service

`amster` service name: `RemoteConsentService`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Client Name

  The name used to identify this OAuth 2.0 remote consent service when referencedin other services.

  `amster` attribute: `clientId`

* Authorization Server jwk\_uri

  The jwk\_uri for retrieving the authorization server signing and encryption keys.

  `amster` attribute: `jwksUriAS`

* JWK Store Cache Timeout (in minutes)

  The cache timeout for the JWK store of the authorization server, in minutes.

  Default value: `60`

  `amster` attribute: `jwkStoreCacheTimeout`

* JWK Store Cache Miss Cache Time (in minutes)

  The length of time a cache miss is cached, in minutes.

  Default value: `1`

  `amster` attribute: `jwkStoreCacheMissCacheTime`

* Consent Response Time Limit (in minutes)

  The time limit set on the consent response JWT before it expires, in minutes.

  Default value: `2`

  `amster` attribute: `consentResponseTimeLimit`

## SAML 2.0 SOAP binding

`amster` service name: `SamlV2SoapBinding`

The following settings are available in this service:

* Request Handler List

  List of handlers to deal with SAML 2.0 requests bound to SOAP.

  The required format is: `key=Meta Alias|class=Handler Class`

  Set the *key* property for a request handler to the meta alias, and the *class* property to the name of the class that implements the handler.

  For example: `key=/pdp|class=com.sun.identity.xacml.plugins.XACMLAuthzDecisionQueryHandler`

  `amster` attribute: `requestHandlers`

## SAML 2.0 service configuration

`amster` service name: `SamlV2ServiceConfiguration`

The following settings are available in this service:

* Cache cleanup interval (in seconds)

  The time, in seconds, that an AuthnRequest can remain in the CTS before it's removed. AuthnRequests are stored in the CTS when AM is acting as the SP and SAML 2.0 failover is enabled.

  Default value: `600`

  `amster` attribute: `cacheCleanupInterval`

* Attribute name for Name ID information

  The user entry attribute to store name identifier information.

  Default value: `sun-fm-saml2-nameid-info`

  `amster` attribute: `nameIDInfoAttribute`

* Attribute name for Name ID information key

  The user entry attribute to store the name identifier key.

  Default value: `sun-fm-saml2-nameid-infokey`

  `amster` attribute: `nameIDInfoKeyAttribute`

* Cookie domain for IdP Discovery Service

  The cookie domain for the IdP discovery service.

  Default value: `openam.example.com`

  `amster` attribute: `idpDiscoveryCookieDomain`

* Cookie type for IdP Discovery Service

  The cookie type to use.

  The possible values for this property are:

  * `PERSISTENT`

  * `SESSION`

  Default value: `PERSISTENT`

  `amster` attribute: `idpDiscoveryCookieType`

* URL scheme for IdP Discovery Service

  The URL scheme to use.

  The possible values for this property are:

  * `HTTP`

  * `HTTPS`

  Default value: `HTTPS`

  `amster` attribute: `idpDiscoveryUrlSchema`

* XML Encryption SPI implementation class

  The class used by the SAML2 engine to *encrypt* and *decrypt* documents.

  Default value: `com.sun.identity.saml2.xmlenc.FMEncProvider`

  `amster` attribute: `xmlEncryptionClass`

* Include xenc:EncryptedKey inside ds:KeyInfo Element

  Select this option to include the `xenc:EncryptedKey` property inside the `ds:KeyInfo` element.

  Default value: `true`

  `amster` attribute: `encryptedKeyInKeyInfo`

* XML Signing SPI implementation class

  The class used by the SAML2 engine to *sign* documents.

  Default value: `com.sun.identity.saml2.xmlsig.FMSigProvider`

  `amster` attribute: `xmlSigningClass`

* XML Signing Certificate Validation

  Select this option to validate the certificates used to sign documents.

  Default value: `false`

  `amster` attribute: `signingCertValidation`

* CA Certificate Validation

  Select this option to validate CA certificates.

  Default value: `false`

  `amster` attribute: `caCertValidation`

* Buffer length (in bytes) to decompress request

  The size of the buffer used for decompressing requests, in bytes.

  Default value: `2048`

  `amster` attribute: `bufferLength`

## Scripting

`amster` service name: `Scripting`

### Configuration

The following settings appear on the Configuration tab:

* Default Script Type

  The default script context type when creating a new script.

  The possible values for this property are:

  | Label                                           | Value                                     |
  | ----------------------------------------------- | ----------------------------------------- |
  | OAuth2 Access Token Modification                | `OAUTH2_ACCESS_TOKEN_MODIFICATION`        |
  | Saml2 SP Adapter                                | `SAML2_SP_ADAPTER`                        |
  | Scripted Decision Node                          | `SCRIPTED_DECISION_NODE`                  |
  | Client-side Authentication                      | `AUTHENTICATION_CLIENT_SIDE`              |
  | Decision node script for authentication trees   | `AUTHENTICATION_TREE_DECISION_NODE`       |
  | Device Match Node                               | `DEVICE_MATCH_NODE`                       |
  | OAuth2 Trusted JWT Issuer                       | `OAUTH2_SCRIPTED_JWT_ISSUER`              |
  | Server-side Authentication                      | `AUTHENTICATION_SERVER_SIDE`              |
  | Social Identity Provider Profile Transformation | `SOCIAL_IDP_PROFILE_TRANSFORMATION`       |
  | Library                                         | `LIBRARY`                                 |
  | OAuth2 Validate Scope                           | `OAUTH2_VALIDATE_SCOPE`                   |
  | Config Provider                                 | `CONFIG_PROVIDER_NODE`                    |
  | OAuth2 Dynamic Client Registration              | `OAUTH2_DYNAMIC_CLIENT_REGISTRATION`      |
  | OAuth2 Authorize Endpoint Data Provider         | `OAUTH2_AUTHORIZE_ENDPOINT_DATA_PROVIDER` |
  | OAuth2 Evaluate Scope                           | `OAUTH2_EVALUATE_SCOPE`                   |
  | Saml2 SP Account Mapper                         | `SAML2_SP_ACCOUNT_MAPPER`                 |
  | Policy Condition                                | `POLICY_CONDITION`                        |
  | OIDC Claims                                     | `OIDC_CLAIMS`                             |
  | Saml2 IDP Adapter                               | `SAML2_IDP_ADAPTER`                       |
  | PingOne Verify Completion Decision Node         | `PINGONE_VERIFY_COMPLETION_DECISION_NODE` |
  | Policy Condition (Next-Gen)                     | `POLICY_CONDITION_NEXT_GEN`               |
  | Saml2 NameID Mapper                             | `SAML2_NAMEID_MAPPER`                     |
  | Saml2 IDP Attribute Mapper                      | `SAML2_IDP_ATTRIBUTE_MAPPER`              |
  | OAuth2 May Act                                  | `OAUTH2_MAY_ACT`                          |
  | Config Provider Node (Next-Gen)                 | `CONFIG_PROVIDER_NODE_NEXT_GEN`           |
  | Node Designer                                   | `NODE_DESIGNER`                           |

  Default value: `Policy Condition`

  `amster` attribute: `defaultContext`

### Secondary configurations

Configure script engine parameters for running a particular script type in AM.

A secondary configuration instance has the following tabs:

#### Configuration

* Scripting languages

  Select the languages available for scripts on the chosen type. Either `GROOVY` or `JAVASCRIPT`.

* Default Script

  The source code that is presented as the default when creating a new script of this type.

#### Default Scripts

The default scripts for this secondary configuration.

#### Secondary Configurations

This service has the following secondary configurations.

##### engineConfiguration

The script engine configuration for scripts of this type.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | Supports server-side scripts only. AM can't configure engine settings for client-side scripts. |

* Property Name Prefix

  This prefix must match the property name prefix used in the script. For example, if the property name is `custom.script.property`, the prefix is `custom.script`.

* Server-side Script Timeout

  The maximum execution time any individual script should take on the server (in seconds). AM terminates scripts which take longer to run than this value.

* Core thread pool size

  The initial number of threads in the thread pool from which scripts operate. AM will ensure the pool contains at least this many threads.

* Maximum thread pool size

  The maximum number of threads in the thread pool from which scripts operate. If no free thread is available in the pool, AM creates new threads in the pool for script execution up to the configured maximum. It's recommended to set the maximum number of threads to 300.

  |   |                                                                                                                                                                                                                                                                                                                                                   |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You can monitor the current usage of the thread pool using the `active` state metric and the size of the scripting engine queue using the `blocked` state metric.Find information about the `scripting.threadpool.threads.count.state.script-context` metric in [Scripting metrics](../monitoring/monitoring-metrics.html#ref-scripting-metrics). |

* Thread pool queue size

  The size of the queue to use for buffering requests for script execution when all core threads are in use. When the core thread pool is at capacity, new script execution requests are queued up to this limit.

  For short, CPU-bound scripts, consider a small pool size and larger queue length. For I/O-bound scripts such as REST calls, consider a larger maximum pool size and a smaller queue.

  Not hot-swappable: restart server for changes to take effect.

* Thread idle timeout (seconds)

  Length of time (in seconds) for a thread to be idle before AM terminates created threads. If the current pool size contains the number of threads set in `Core thread pool size` idle threads aren't terminated, to maintain the initial pool size.

- Java class allowlist

  The list of class-name patterns allowed to be invoked by the script. Every class accessed by the script must match at least one of these patterns.

  You can specify the class name as-is or use a regular expression.

  Find more information about allowlisting Java classes in [Scripting environment](../am-scripting/scripting-env.html).

  |   |                                                                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This only applies to legacy scripts. You can't add classes to the allowlist for a [next-generation](../am-scripting/next-generation-scripts.html) script. |

- Java class denylist

  The list of class-name patterns that are NOT allowed to be invoked by the script. The denylist is applied AFTER the allowlist to exclude those classes. Access to a class specified in both the allowlist and the denylist will be denied.

  You can specify the class name to exclude as-is or use a regular expression.

  Find more information about denylisting Java classes in [Scripting environment](../am-scripting/scripting-env.html).

- Use system SecurityManager

  If enabled, AM makes a call to `System.getSecurityManager().checkPackageAccess(…​)` for each class that is accessed. The method throws `SecurityException` if the calling thread is not allowed to access the package.

  |   |                                                                                |
  | - | ------------------------------------------------------------------------------ |
  |   | This feature only takes effect if the security manager is enabled for the JVM. |

## Session

`amster` service name: `SessionUserService`

### General

The following settings appear on the General tab:

* Latest Access Time Update Frequency

  Defaults to `60` seconds. At most, AM updates an authenticated session's latest access time this often.

  Subsequent changes to the authenticated session that occur within the specified number of seconds after an update don't cause additional updates to the authenticated session's access time. Refreshing an authenticated session returns the idle time as the number of seconds since an update has occurred, which will be between `0` and the specified Latest Access Time Update Frequency.

  Default value: `60`

  `amster` attribute: `latestAccessTimeUpdateFrequency`

* DN Restriction Only Enabled

  If enabled, AM will not perform DNS lookups when checking restrictions in cookie hijacking mode.

  Default value: `false`

  `amster` attribute: `dnRestrictionOnly`

* Session Timeout Handler implementations

  Lists plugin classes implementing session timeout handlers. Specify the fully qualified name.

  `amster` attribute: `timeoutHandlers`

- Enable Cross Upgrade Session Reference

  If enabled, the session contains an additional session reference property whose value is persisted across a session upgrade.

  To access the cross-upgrade session reference—for example, from within a script or when getting session information—allowlist the property `XUSRef` in the [Session Property Whitelist service](#global-amsessionpropertywhitelist).

  Track the session reference in the [audit logs](../monitoring/audit-logging-ref.html) for session creation and session upgrade events.

  `amster` attribute: `crossUpgradeReferenceFlag`

### Session search

The following settings appear on the Session Search tab:

* Maximum Number of Search Results

  Maximum number of results from a session search. Do not set this attribute to a large value, for example more than 1000, unless sufficient system resources are allocated.

  Default value: `120`

  `amster` attribute: `maxSessionListSize`

* Timeout for Search

  Time after which AM sees an incomplete search as having failed, in seconds.

  Default value: `5`

  `amster` attribute: `sessionListRetrievalTimeout`

### Session property change notifications

The following settings appear on the Session Property Change Notifications tab:

* Enable Property Change Notifications

  If enabled, AM notifies other applications participating in SSO when a session property in the Notification Properties list changes on a server-side session.

  The possible values for this property are:

  * `ON`

  * `OFF`

  Default value: `OFF`

  `amster` attribute: `propertyChangeNotifications`

* Notification Properties

  Lists session properties for which AM can send notifications upon modification. Session notification applies to server-side sessions only.

  `amster` attribute: `notificationPropertyList`

### Session quotas

The following settings appear on the Session Quotas tab:

* Enable Quota Constraints

  If enabled, AM lets you set quota constraints on server-side sessions.

  The possible values for this property are:

  * `ON`

  * `OFF`

  Default value: `OFF`

  `amster` attribute: `iplanet-am-session-enable-session-constraint`

* Read Timeout for Quota Constraint

  Maximum wait time after which AM considers a search for live session count as having failed if quota constraints are enabled, in milliseconds.

  Default value: `6000`

  `amster` attribute: `quotaConstraintMaxWaitTime`

* Resulting behavior if session quota exhausted

  Specify the action to take if a session quota is exhausted:

  The possible values for this property are:

  * **Deny Access** (`org.forgerock.openam.session.service.DenyAccessAction`). New session creation requests are denied.

  * **Destroy Next Expiring** `org.forgerock.openam.session.service.DestroyNextExpiringAction`). The session that would expire next is destroyed.

  * **Destroy Oldest** (`org.forgerock.openam.session.service.DestroyOldestAction`). The oldest session is destroyed.

  * **Destroy All** (`org.forgerock.openam.session.service.DestroyAllAction`). All previous sessions are destroyed.

  Default value: `org.forgerock.openam.session.service.DestroyNextExpiringAction`

  `amster` attribute: `behaviourWhenQuotaExhausted`

* Deny user login when session repository is down

  This property only takes effect when the session quota constraint is enabled, and the session datastore is unavailable.

  The possible values for this property are:

  * `YES`

  * `NO`

  Default value: `NO`

  `amster` attribute: `denyLoginWhenRepoDown`

### Client-side sessions

The following settings appear on the Client-Side Sessions tab:

* Signing Algorithm Type

  The algorithm that AM uses to sign the JSON Web Token (JWT) containing the session content. Signing the JWT enables tampering detection.

  The possible values for this property are:

  * `NONE`

  * `HS256`. HMAC using SHA-256.

  * `HS384`. HMAC using SHA-384.

  * `HS512`. HMAC using SHA-512.

  * `RS256`. RSASSA-PKCS1-v1\_5 using SHA-256.

  * `ES256`. ECDSA using SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384`. ECDSA using SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512`. ECDSA using SHA-512 and NIST standard P-521 elliptic curve.

  Default value: `HS256`

  `amster` attribute: `statelessSigningType`

* Signing HMAC Shared Secret

  Specifies the shared secret that AM uses when performing HMAC signing on the session JWT.

  Specify a shared secret when using a "Signing Algorithm Type" of `HS256`, `HS384`, or `HS512`.

  `amster` attribute: `statelessSigningHmacSecret`

* Encryption Algorithm

  Specifies the algorithm that AM uses to encrypt the JSON Web Token (JWT) containing the session content.

  The possible values for this property are:

  * `NONE`. Session content is not encrypted.

  * `RSA`. Session content is encrypted with AES using a unique key. The key is then encrypted with an RSA public key and appended to the JWT.

    AM supports the following padding modes, which you can set using the `org.forgerock.openam.session.stateless.rsa.padding` advanced property:

    * `RSA1_5`. RSA with PKCS#1 v1.5 padding.

    * `RSA-OAEP`. RSA with optimal asymmetric encryption padding (OAEP) and SHA-1.

    * `RSA-OAEP-256`. RSA with OAEP padding and SHA-256.

  * `AES_KEYWRAP`. AES key wrapping.

    Session content is encrypted with AES using a unique key and is then wrapped using AES KeyWrap and the master key. This provides additional security, compared to RSA, at the cost of 128 or 256 bits (or 32 bytes) depending on the size of the master key. This method provides authenticated encryption, which removes the need for a separate signature and decreases the byte size of the JWT. See [RFC 3394](https://www.rfc-editor.org/info/rfc3394).

  * `DIRECT`. Direct AES encryption.

    Session content is encrypted with direct AES encryption, with a symmetric key. This method provides authenticated encryption, which removes the need for a separate signature and decreases the byte size of the JWT.

  |   |                                                                                                                                                                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Users can *accidentally* disable all authentication by disabling signing and not using an authenticated encryption mode. To prevent this, set the `org.forgerock.openam.session.stateless.signing.allownone` system property to `true` to turn off signing completely. |

  Default value: `DIRECT`

  `amster` attribute: `statelessEncryptionType`

* Encryption Symmetric AES Key

  AES key for use with Direct or AES KeyWrap encryption modes.

  The symmetric AES key is a base64-encoded random key.

  For direct encryption with `AES-GCM` or for `AES-KeyWrap` with any content encryption method, this should be 128, 192, or 256 bits.

  For direct encryption with `AES-CBC-HMAC`, the key should be double those sizes (one half for the AES key, the other have for the HMAC key).

  `amster` attribute: `statelessEncryptionAesKey`

* Compression Algorithm

  If enabled the session state is compressed before signing and encryption.

  |   |                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Enabling compression can compromise encryption. This may leak information about the content of the session state if encryption is enabled. |

  The possible values for this property are:

  * `NONE`

  * `DEF`. Deflate Compression.

  Default value: `NONE`

  `amster` attribute: `statelessCompressionType`

* Enable Session Denylisting

  Denylists client-side sessions that log out.

  Enable this setting if the maximum session time is high. The denylist state is stored in the Core Token Service (CTS) token store until the session expires, to ensure that sessions cannot continue to be used.

  Default value: `false`

  `amster` attribute: `openam-session-stateless-enable-session-blacklisting`

* Session Denylist Cache Size

  Number of denylisted sessions to cache in memory to speed up denylist checks and reduce load on the CTS. The cache size should be approximately the number of logouts expected in the maximum session time.

  Default value: `10000`

  `amster` attribute: `openam-session-stateless-blacklist-cache-size`

* Denylist Poll Interval (seconds)

  Specifies the interval at which AM polls the Core Token Service to update the list of signed out sessions, in seconds.

  The longer the polling interval, the more time a malicious user has to connect to other AM servers in a deployment and make use of a stolen session cookie. Shortening the polling interval improves security for signed-out sessions, but might incur a minimal decrease in overall AM performance due to increased network activity. Set to `0` to disable this feature completely.

  Default value: `10`

  `amster` attribute: `openam-session-stateless-blacklist-poll-interval`

* Denylist Purge Delay (minutes)

  When added to the maximum session time, specifies the amount of time that AM tracks logged out sessions.

  Increase the denylist purge delay if you expect system clock skews in your deployment to be greater than one minute. You don't need to increase the denylist purge delay for servers running a clock synchronization protocol, such as the Network Time Protocol.

  Default value: `1`

  `amster` attribute: `openam-session-stateless-blacklist-purge-delay`

- Enable Invalidation of Sessions Based on User Identifier

  Let AM permit logging out all client-side sessions for a specific user, through the `logoutByUser` action.

  Setting this to `true` causes AM to store logout user tokens in a local cache. For multi-server deployments, AM polls the CTS at a specified interval and populates the cache with the logout user tokens of all servers in the deployment.

  Default value: `false`

  `amster` attribute: `statelessLogoutByUser`

- Invalidated Sessions Poll Interval (seconds)

  When Enable Invalidation of Sessions Based on User Identifier is `true`, this setting specifies the frequency at which AM polls the CTS for changes to persisted logout tokens.

  Default value: `60`

  `amster` attribute: `openam-session-stateless-logout-poll-interval`

### Dynamic attributes

|   |                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configuring any of the following properties at the realm level (Realms > *realm name* > Services > Session) causes the values to be stored in the identity store configured in that realm.If you remove the identity store from the realm, the properties will use the values configured at the global level (Configure > Global Services > Session). |

The following settings appear on the Dynamic Attributes tab:

* Maximum Session Time

  Maximum time a session can remain valid before AM requires the user to authenticate again, in minutes.

  Default value: `120`

  `amster` attribute: `maxSessionTime`

* Maximum Idle Time

  Maximum time a server-side session can remain idle before AM requires the user to authenticate again, in minutes.

  Default value: `30`

  `amster` attribute: `maxIdleTime`

* Maximum Caching Time

  Maximum duration that external AM clients should cache the session, in minutes.

  Default value: `3`

  `amster` attribute: `maxCachingTime`

* Active User Sessions

  Maximum number of concurrent server-side authenticated sessions per user.

  Default value: `5`

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This value doesn't apply if `Enable Quota Constraints` is `OFF`. In other words, session quota constraints must be enabled for any configured maximum to apply. |

  `amster` attribute: `quotaLimit`

## Session Property Whitelist service

`amster` service name: `SessionPropertyWhiteList`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Allowlisted Session Property Names

  A list of properties that users may read, edit the value of, or delete from their session.

  Adding properties to sessions can impact AM's performance. There is no limit on the set of properties that you can add to sessions, and no limit on the number of session properties you can add.

  Adding session properties can increase the load on an AM deployment in the following areas:

  * AM server memory

  * LDAP server storage

  * LDAP server replication

  Protected attributes **can't** be set, edited or deleted, even if they are included in this allowlist.

  Default value: `AMCtxId`

  `amster` attribute: `sessionPropertyWhitelist`

* Session Properties to return for session queries

  A list of session properties that can be returned to admins in a REST session query response.

  This setting can impact REST query performance. When session properties are added, the CTS token must be retrieved, and can be decrypted and decompressed, if configured.

  Protected attributes **can't** be set, edited or deleted, even if they are included in this list.

  `amster` attribute: `whitelistedQueryProperties`

## Social authentication implementations

This service was used only for authentication with modules and chains and is no longer documented.

## Social Identity Provider service

`amster` service name: `SocialIdentityProviders`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Enabled

  Default value: `true`

  `amster` attribute: `enabled`

### Secondary configurations

Learn about the secondary configuration settings in [Social identity provider client configuration](../am-authentication/social-idp-client-reference.html).

## Transaction Authentication service

`amster` service name: `TransactionAuthentication`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Time to Live

  The number of seconds within which the transaction must be completed.

  Default value: `180`

  `amster` attribute: `timeToLive`

## UMA provider

`amster` service name: `UmaProvider`

### Global Attributes

The following settings appear on the Global Attributes tab:

* UMA Policy Upgrade Compatibility Mode

  When this setting is enabled, AM creates backward-compatible UMA policies. Enable this setting when you are upgrading from servers prior to AM 7.2.0, and when you are upgrading multiple servers in a deployment at different times. Disable this setting when you have completed the upgrade for all AM instances in your deployment.

  Default value: `false`

  `amster` attribute: `umaPolicyUpgradeCompatibilityMode`

### General

The following settings appear on the General tab:

* Permission Ticket Lifetime (seconds)

  The maximum life of a permission ticket before it expires, in seconds.

  Default value: `120`

  `amster` attribute: `permissionTicketLifetime`

* Delete user policies when Resource Server is removed

  Delete all user policies that relate to a Resource Server when removing the OAuth2 agent entry or removing the `uma_protection` scope from the OAuth2 agent.

  Default value: `true`

  `amster` attribute: `deletePoliciesOnDeleteRS`

* Delete resources when Resource Server is removed

  Delete all resources that relate to a Resource Server when removing the OAuth2 agent entry or removing the `uma_protection` scope from the OAuth2 agent.

  Default value: `true`

  `amster` attribute: `deleteResourceSetsOnDeleteRS`

* Pending Requests Enabled

  Use the Pending Requests subsystem to notify the resource owner that an attempt was made to access their resource.

  Default value: `true`

  `amster` attribute: `pendingRequestsEnabled`

* Email Resource Owner on Pending Request creation

  Send an email to the Resource Owner when a Pending Request is created, when a Requesting Party requests access to a resource.

  Default value: `true`

  `amster` attribute: `emailResourceOwnerOnPendingRequestCreation`

* Email Requesting Party on Pending Request approval

  Send an email to the Requesting Party when a Pending Request is approved by the Resource Owner.

  Default value: `true`

  `amster` attribute: `emailRequestingPartyOnPendingRequestApproval`

* Grant Resource Owner Implicit Consent

  Implicitly grant the resource owner consent to the resource, regardless of policy conditions.

  Default value: `true`

  `amster` attribute: `resourceOwnerImplicitConsent`

* User profile preferred Locale attribute

  User profile attribute storing the user's preferred locale.

  Default value: `inetOrgPerson`

  `amster` attribute: `userProfileLocaleAttribute`

* Re-Sharing Mode

  Specifies whether re-sharing is off or on implicitly for all users, allowing all users to re-share resources that have been shared with them.

  The possible values for this property are:

  * `Off`

  * `Implicit`

  Default value: `Implicit`

  `amster` attribute: `resharingMode`

* Grant RPTs…​

  In UMA, scope comes from both the permission ticket and from the token request. An RPT is always granted when all scopes match, and is never granted when no scope matches. You can configure when RPTs are granted for partial match conditions here. For more information, see [Assessment and Results Determination](https://docs.kantarainitiative.org/uma/wg/rec-oauth-uma-grant-2.0.html#authorization-assessmentAuthorization) in the *UMA 2.0 Grant Specification*.

  Default value:

  ```none
  When the scope from the request is partially matched.
  When none of the scope from the request is matched.
  When the scope from the ticket is partially matched.
  ```

  `amster` attribute: `grantRptConditions`

* Username attribute

  The name of the attribute whose value must be specified by end users when sharing resources. For example, if a user wants to share a resource with another user, based on that user's email address, set this value to `mail`.

  The attribute that you set here *must* contain unique values; otherwise, a resource share can grant access to multiple users unintentionally.

  If you leave this attribute empty, UMA policies are based on the attribute that the underlying datastore considers the `username` (for example, the LDAP user search attribute). This behavior is compatible with previous AM versions. The [UMA Postman Collection](../uma/uma-example.html#uma-postman-collection) sets this value to `uid`, which works in most deployments.

  |   |                                                                   |
  | - | ----------------------------------------------------------------- |
  |   | Changing this setting can invalidate existing UMA authorizations. |

  Default value: None

  `amster` attribute: `usernameAttribute`

### Claims gathering

The following properties can be set on the Claims Gathering tab:

* Interactive Claims Gathering Enabled

  If this setting is enabled, and no PCT *(tooltip: Persisted Claims Token)* is provided on the request, the UMA provider returns a *redirect\_user* hint to the client, where the requesting party can authenticate themselves.

  Default value: `false`

  `amster` attribute: `interactiveClaimsGatheringEnabled`

* Claims Gathering Authentication Tree

  The authentication tree to which the requesting party should be directed, in order to collect claims. This authentication tree should collect all claims necessary for successful UMA authorization.

  Default value: None

  `amster` attribute: `claimsGatheringTree`

* Persisted Claims Token Lifetime (seconds)

  During interactive claims gathering, AM can issue a PCT *(tooltip: Persisted Claims Token)*, that clients can use later during RPT *(tooltip: Requesting Party Token)* flows, so that users don't have to go through the interactive claims gathering process too frequently.

  If a PCT *(tooltip: Persisted Claims Token)* is issued, this setting determines the interval (in seconds) that the PCT should be considered valid.

  Default value: `604800` (7 days)

  `amster` attribute: `pctLifetime`

- Warn on confusable characters in username

  When enabled, the UI displays a warning on pending share requests or existing resource permissions if the username of the requesting party contains confusable characters from different unicode scripts, for example `𝝲` and `y`.

  The warning displayed is `Warning: This username contains confusable characters. Make sure this is the correct person before allowing them access.`

  Pending request and resource set REST responses can include an additional field to indicate that confusable characters are present.

  Default value: `false`

  `amster` attribute: `warnIfConfusablesInUsername`

## User

`amster` service name: `IdRepositoryUser`

### Dynamic attributes

The following settings appear on the Dynamic Attributes tab:

* User Preferred Timezone

  Time zone for accessing AM admin UI.

  `amster` attribute: `preferredTimezone`

* Administrator DN Starting View

  Specifies the DN for the initial screen when the AM administrator successfully logs in to the AM admin UI.

  `amster` attribute: `adminDNStartingView`

* Default User Status

  Inactive users cannot authenticate, although AM stores their profiles.

  The possible values for this property are:

  * `Active`

  * `Inactive`

  Default value: `Active`

  `amster` attribute: `defaultUserStatus`

## User Self-Service

`amster` service name: `UserSelfService`

### General configuration

The following settings appear on the General Configuration tab:

* Encryption Key Pair Alias

  An encryption key alias in the AM server's JCEKS keystore. Used to encrypt the JWT token that AM uses to track end users during User Self-Service operations.

  For example, you might set this property to: selfserviceenctest

  |   |                                                                                                                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This property is deprecated and will be removed in a future release. Enable Use Secret Store and map a secret to the `am.services.selfservice.token.encryption` secret ID instead. AM ignores this value if you enable Use Secret Store. |

  `amster` attribute: `encryptionKeyPairAlias`

* Signing Secret Key Alias

  A signing secret key alias in the AM server's JCEKS keystore. Used to sign the JWT token that AM uses to track end users during user self-service operations.

  For example, you might set this property to: selfservicesigntest

  |   |                                                                                                                                                                                                                                       |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This property is deprecated and will be removed in a future release. Enable Use Secret Store and map a secret to the `am.services.selfservice.token.signing` secret ID instead. AM ignores this value if you enable Use Secret Store. |

  `amster` attribute: `signingSecretKeyAlias`

* Use Secret Store

  If enabled, user self-service operations use the AM secret store to retrieve signing and encryption keys for snapshot tokens, and ignore the values set in the Signing Secret Key Alias and Encryption Key Pair Alias properties.

  Configure the following secret IDs in the secret store before enabling this option:

  * `am.services.selfservice.token.encryption`

  * `am.services.selfservice.token.signing`

  If disabled, self-service operations use the configured legacy Encryption Key Pair Alias and Signing Secret Key Alias.

  `amster` attribute: `use.secret.store.secrets`

* Google reCAPTCHA Site Key

  Google reCAPTCHA plugin site key.

  `amster` attribute: `captchaSiteKey`

* Google reCAPTCHA Secret Key

  Google reCAPTCHA plugin secret key.

  `amster` attribute: `captchaSecretKey`

* Google Re-captcha Verification URL

  Google reCAPTCHA plugin verification URL.

  Default value: `https://www.google.com/recaptcha/api/siteverify`

  `amster` attribute: `captchaVerificationUrl`

* Security Questions

  Specifies the default set of knowledge-based authentication (KBA) security questions. The security questions can be set for the User Self-Registration, forgotten password reset, and forgotten username services, respectively.

  Format is `unique key|locale|question`.

  Default value:

  ```
  4|en|What is your mother&#39;s maiden name?
  3|en|What was the name of your childhood pet?
  2|en|What was the model of your first car?
  1|en|What is the name of your favourite restaurant?
  ```

  `amster` attribute: `kbaQuestions`

* Minimum Answers to Define

  Specifies the minimum number of KBA answers that users must define.

  Default value: `1`

  `amster` attribute: `minimumAnswersToDefine`

* Minimum Answers to Verify

  Specifies the minimum number of KBA questions that users need to answer to be granted the privilege to carry out an action, such as registering for an account, resetting a password, or retrieving a username. Specify a value from `0` to `50`.

  Default value: `1`

  `amster` attribute: `minimumAnswersToVerify`

* Valid Query Attributes

  Specifies the valid query attributes used to search for the user. This is a list of attributes used to identify your account for forgotten password and forgotten username.

  Default value:

  ```
  uid
  mail
  givenName
  sn
  ```

  `amster` attribute: `validQueryAttributes`

### User registration

The following settings appear on the **User Registration** tab:

* User Registration

  If enabled, new users can sign up for an account.

  Default value: `false`

  `amster` attribute: `userRegistrationEnabled`

* Captcha

  If enabled, users must pass a Google reCAPTCHA challenge during user self-registration to mitigate against software bots.

  Default value: `false`

  `amster` attribute: `userRegistrationCaptchaEnabled`

* Email Verification

  If enabled, users who self-register must perform email address verification.

  Default value: `true`

  `amster` attribute: `userRegistrationEmailVerificationEnabled`

* Verify Email before User Detail

  If enabled, email address verification will be performed first before user details screen is displayed. This will take effect only if Verify Email is enabled.

  Default value: `false`

  `amster` attribute: `userRegistrationEmailVerificationFirstEnabled`

* Security Questions

  If enabled, users must set up their security questions during the self-registration process.

  Default value: `false`

  `amster` attribute: `userRegistrationKbaEnabled`

* Token Lifetime (seconds)

  Maximum lifetime of the token allowing User Self-Registration, in seconds.

  Default value: `300`

  `amster` attribute: `userRegistrationTokenTTL`

* Outgoing Email Subject

  Customize the User Self-Registration verification email subject text. Format is `locale|subject text`.

  Default value: `en|Registration email`

  `amster` attribute: `userRegistrationEmailSubject`

* Outgoing Email Body

  Customize the User Self-Registration verification email body text. Format is: `locale|body text`.

  Default value: `en|<h2>Click on this <a href="%link%">link</a> to register.</h2>`

  `amster` attribute: `userRegistrationEmailBody`

* Valid Creation Attributes

  Specifies an allowlist of user attributes that can be set during user creation.

  Default value:

  ```
  userPassword
  mail
  givenName
  kbaInfo
  inetUserStatus
  sn
  username
  ```

  `amster` attribute: `userRegistrationValidUserAttributes`

* Destination After Successful Self-Registration

  The action to be taken after a user successfully registers a new account.

  The possible values for this property are:

  * Label: **User sent to 'successful registration' page** (value: `default`). User is sent to a success page, without being logged in.

  * Label: **User sent to login page** (value: `login`). User is sent to the login page to authenticate.

  * Label: **User is automatically logged in** (value: `auto-login`). User is automatically logged in and sent to the appropriate page.

  Default value: `default`

  `amster` attribute: `userRegisteredDestination`

### Forgotten password

The following settings appear on the **Forgotten Password** tab:

* Forgotten Password

  If enabled, users can reset their forgotten password.

  Default value: `false`

  `amster` attribute: `forgottenPasswordEnabled`

* Captcha

  If enabled, users must pass a Google reCAPTCHA challenge during password reset to mitigate against software bots.

  Default value: `false`

  `amster` attribute: `forgottenPasswordCaptchaEnabled`

* Email Verification

  If enabled, users who reset passwords must perform email address verification.

  Default value: `true`

  `amster` attribute: `forgottenPasswordEmailVerificationEnabled`

* Security Questions

  If enabled, users must answer their security questions during the forgotten password process.

  Default value: `false`

  `amster` attribute: `forgottenPasswordKbaEnabled`

* Enforce password reset lockout

  If enabled, users will be prevented from resetting their password after the configured number of failed attempts.

  Default value: `false`

  `amster` attribute: `numberOfAttemptsEnforced`

* Lock Out After number of attempts

  Can be set to 1 or more attempts for a user to correctly answer all their security questions. After the number of configured attempts the user has not correctly answered them the password reset feature will be disabled.

  Default value: `1`

  `amster` attribute: `numberOfAllowedAttempts`

* Token Lifetime (seconds)

  Maximum lifetime for the token allowing forgotten password reset, in seconds.

  Specify a value from `0` to `2147483647`.

  Default value: `300`

  `amster` attribute: `forgottenPasswordTokenTTL`

* Outgoing Email Subject

  Customize the forgotten password email subject text. Format is `locale|subject text`.

  Default value: `en|Forgotten password email`

  `amster` attribute: `forgottenPasswordEmailSubject`

* Outgoing Email Body

  Customize the forgotten password email body text. Format is `locale|body text`.

  Default value: `en|<h2>Click on this <a href="%link%">link</a> to reset your password.</h2>`

  `amster` attribute: `forgottenPasswordEmailBody`

### Forgotten username

The following settings appear on the **Forgotten Username** tab:

* Forgotten Username

  If enabled, users can retrieve their forgotten username.

  Default value: `false`

  `amster` attribute: `forgottenUsernameEnabled`

* Captcha

  If enabled, users must pass a Google reCAPTCHA challenge during the forgotten username retrieval process to mitigate against software bots.

  Default value: `false`

  `amster` attribute: `forgottenUsernameCaptchaEnabled`

* Security Questions

  If enabled, users must answer their security questions during the forgotten username process.

  Default value: `false`

  `amster` attribute: `forgottenUsernameKbaEnabled`

* Email Username

  If enabled, users receive their forgotten username by email.

  Default value: `true`

  `amster` attribute: `forgottenUsernameEmailUsernameEnabled`

* Show Username

  If enabled, users see their forgotten username on the browser page.

  Default value: `false`

  `amster` attribute: `forgottenUsernameShowUsernameEnabled`

* Token LifeTime (seconds)

  Maximum lifetime for the token allowing forgotten username, in seconds.

  Default value: `300`

  `amster` attribute: `forgottenUsernameTokenTTL`

* Outgoing Email Subject

  Customizes the forgotten username email subject text. Format is `locale|subject text`.

  Default value: `en|Forgotten username email`

  `amster` attribute: `forgottenUsernameEmailSubject`

* Outgoing Email Body

  Customizes the forgotten username email body text. Format is `locale|body text`.

  Default value: `en|<h2>Your username is <span style="color:blue">%username%</span>.</h2>`

  `amster` attribute: `forgottenUsernameEmailBody`

### Profile management

The following settings appear on the **Profile Management** tab:

* Protected Update Attributes

  Specifies a profile's protected user attributes, which causes re-authentication when the user attempts to modify these attributes.

  `amster` attribute: `profileProtectedUserAttributes`

* Self readable attributes

  Specifies the list of attributes that users can view when accessing their user profile.

  Default value:

  ```
  uid
  telephoneNumber
  mail
  kbaInfo
  givenName
  sn
  cn
  ```

  `amster` attribute: `profileAttributeWhitelist`

### Advanced configuration

The following settings appear on the Advanced Configuration tab:

* User Registration Confirmation Email URL

  Specifies the confirmation URL that the user receives during the self-registration process. The `${realm}` string is replaced with the current realm.

  Default value: `http://openam.example.com:8080/openam/XUI/?realm=${realm}#register/`

  `amster` attribute: `userRegistrationConfirmationUrl`

* Forgotten Password Confirmation Email URL

  Specifies the confirmation URL that the user receives after confirming their identity during the forgotten password process. The `${realm}` string is replaced with the current realm.

  Default value: `http://openam.example.com:8080/openam/XUI/?realm=${realm}#passwordReset/`

  `amster` attribute: `forgottenPasswordConfirmationUrl`

* User Registration Service Config Provider Class

  Specifies the provider class to configure any custom plugins.

  Default value: `org.forgerock.openam.selfservice.config.flows.UserRegistrationConfigProvider`

  `amster` attribute: `userRegistrationServiceConfigClass`

* Forgotten Password Service Config Provider Class

  Specifies the provider class to configure any custom plugins.

  Default value: `org.forgerock.openam.selfservice.config.flows.ForgottenPasswordConfigProvider`

  `amster` attribute: `forgottenPasswordServiceConfigClass`

* Forgotten Username Service Config Provider Class

  Specifies the provider class to configure any custom plugins.

  Default value: `org.forgerock.openam.selfservice.config.flows.ForgottenUsernameConfigProvider`

  `amster` attribute: `forgottenUsernameServiceConfigClass`

## Self-Service trees

`amster` service name: `SelfServiceTrees`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Enabled

  Default value: `true`

  `amster` attribute: `enabled`

* Tree Mapping

  Maps the self service function name (the key) to an authentication tree (the value).

  Default value: `{}`

  `amster` attribute: `treeMapping`

## Validation service

`amster` service name: `ValidationService`

### Global attributes

The following settings appear on the Global Attributes tab:

* Valid goto URL Resources

  List of valid goto URL resources.

  Specifies a list of valid URLs for the `goto` and `gotoOnFail` query string parameters.

  After login or logout, AM can redirect a user to a URL in this list. If the URL is not in this list, AM redirects to the user profile page, the administration console, or the URL set in the [Success URL node](https://docs.pingidentity.com/auth-node-ref/8.1/success-url.html). If you don't set this property, AM only allows URLs that match its domain; for example, `domain-of-am-instance.com`. Use the `*` wildcard to match all characters except `?`.

  Examples:

  * `http://app.example.com:80/*`

  * `http://app.example.com:80/?`

  `amster` attribute: `validGotoDestinations`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Valid goto URL Resources

  List of valid goto URL resources.

  Specifies a list of valid URLs for the `goto` and `gotoOnFail` query string parameters. AM only redirects a user after log in or log out to a URL in this list. If the URL is not in the list, AM redirects to either the user profile page, or the administration console. If this property is not set, AM will only allow URLs that match its domain; for example, `domain-of-am-instance.com`. Use the `*` wildcard to match all characters except `?`.

  Examples:

  * `http://app.example.com:80/*`

  * `http://app.example.com:80/?`

  `amster` attribute: `validGotoDestinations`

## WebAuthn Metadata service

`amster` service name: `WebAuthnMetadataService`

The WebAuthn Metadata service lets you configure how AM obtains FIDO2 metadata at the journey level.

You can configure the [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/8.1/webauthn-registration.html)'s FIDO Certification Level setting to force AM to check the WebAuthn Metadata service for the device's accepted certification level.

The service has the following configurable attributes:

* Metadata service URIs

  The list of locations from which to download the [metadata blob](https://fidoalliance.org/specs/mds/fido-metadata-service-v3.0-ps-20210518.html#metadata-blob).

  AM verifies the blob signature against secrets mapped to the `am.authentication.nodes.webauthn.fidometadataservice.rootcertificate` secret label.

  If you don't want AM to connect to the internet, this location can be a local filesystem.

  |   |                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------- |
  |   | If you store the metadata blob in a local filesystem, it's your responsibility to keep it up to date. |

  `amster` attribute: `fidoMetadataServiceUris`

* Enforce revocation check

  This setting specifies whether AM must check revocation entries from certificates.

  The setting is disabled by default, so AM doesn't check presented certificates for revocation.

  If you enable this setting, AM must be able to verify any attestation certificate's trust chain with a CRL or OCSP entry during processing.

  |   |                                                                                            |
  | - | ------------------------------------------------------------------------------------------ |
  |   | Certificates downloaded from the FIDO Metadata Service might not have a CRL or OCSP entry. |

  `amster` attribute: `enforceRevocationCheck`

## WebAuthn Profile Encryption service

`amster` service name: `AuthenticatorWebAuthn`

### Realm defaults

The following settings appear on the Realm Defaults tab:

* Profile Storage Attribute

  The user's attribute in which to store WebAuthn profiles.

  The default attribute is added to the schema when you prepare a user store for use with AM. If you want to use a different attribute, you must make sure to add it to your user store schema prior to deploying webauthn with AM. AM must be able to write to the attribute.

  Default value: `webauthnDeviceProfiles`

  `amster` attribute: `webauthnAttrName`

* Device Profile Encryption Scheme

  Encryption scheme to use to secure device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings** (value: `NONE`)

  Default value: `NONE`

  `amster` attribute: `authenticatorWebAuthnDeviceSettingsEncryptionScheme`

* Encryption Key Store

  Path to the keystore from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * For greater security, store encryption key information in a [secret store](../security/secret-stores.html), instead of in the configuration. Use the secret label `am.services.authenticatorwebauthn.encryption` to map an alias for WebAuthn service secrets.

  * If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the user's device profile from their entry in the identity store so that the user can create a new one when they next log in.

  * To use this service in a FIPS 140-3 compliant environment, you must map the `am.services.authenticatorwebauthn.encryption` secret label to an alias in a [FIPS-compliant keystore](../security/fips.html#manage-bcfks-keystores). |

  |   |                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If AM finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in a secret store, this value is ignored. |

  Default value: `/path/to/openam/security/keystores/keystore.jceks`

  `amster` attribute: `authenticatorWebAuthnDeviceSettingsEncryptionKeystore`

* Key Store Type

  Type of keystore to load.

  |   |                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PKCS#11 key stores require hardware support such as a security device or smart card and is not available by default in most JVM installations. |

  Learn more in the [PKCS#11 Reference Guide](https://docs.oracle.com/en/java/javase/25/security/pkcs11-reference-guide1.html).

  |   |                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If AM finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in a secret store, this value is ignored. |

The possible values for this property are:

* Label: **Java Key Store (JKS)** (value: `JKS`)

* Label: **Java Cryptography Extension Key Store (JCEKS)** (value: `JCEKS`)

* Label: **PKCS#11 Hardware Crypto Storage** (value: `PKCS11`)

* Label: **PKCS#12 Key Store** (value: `PKCS12`)

Default value: `JCEKS`

`amster` attribute: `authenticatorWebAuthnDeviceSettingsEncryptionKeystoreType`

* Key Store Password

  Password to unlock the key store. AM encrypts this password when you save it in the configuration. You should modify the default value.

  |   |                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If AM finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `authenticatorWebAuthnDeviceSettingsEncryptionKeystorePassword`

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If AM finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `authenticatorWebAuthnDeviceSettingsEncryptionKeystoreKeyPairAlias`

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If AM finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in a secret store, this value is ignored. |

  `amster` attribute: `authenticatorWebAuthnDeviceSettingsEncryptionKeystorePrivateKeyPassword`

---

---
title: Configure identities and realms over REST
description: Use the REST API to create, read, update, delete, and list identities and realms in PingAM
component: pingam
version: 8.1
page_id: pingam:setup:sec-rest-realm-rest
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/sec-rest-realm-rest.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "REST", "Identities", "Realms"]
page_aliases: ["setup-guide:sec-rest-realm-rest.adoc"]
section_ids:
  rest-api-crud-identity: Manage identities
  rest-api-create-identity: Create an identity
  rest-api-read-identity: Read an identity
  rest-api-update-identity: Update an identity
  rest-api-delete-identity: Delete an identity
  rest-api-query-identity: List identities
  rest-api-retrieve-identity-using-session-cookie: Get identities with the session cookie
  rest-api-change-password: Change passwords
  rest-api-create-group: Create a group
  rest-api-add-user-to-group: Add a user to a group
  rest-api-crud-realm: Manage realms
  rest-api-parameters-realm: Required realm properties
  rest-api-create-realm: Create a realm
  rest-api-list-realm: List realms
  rest-api-read-realm: Read a realm
  rest-api-update-realm: Update a realm
  rest-api-delete-realm: Delete a realm
---

# Configure identities and realms over REST

This page shows how to use the [REST API](../am-rest/preface.html) to manage identities and realms.

Long URLs are wrapped to fit the printed page, and some output is formatted for easier reading.

Before making a REST API call to manage an identity or realm, make sure that you have:

* Authenticated successfully to AM as a user with sufficient privileges to make the REST API call.

* Obtained the session token returned after successful authentication.

When making the REST API call, pass the [session token](../am-authentication/rest-using-ssotokens.html) in the HTTP header.

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | To make REST requests to a specific realm, see [Specify realms in REST API calls](../am-rest/rest-realms.html). |

## Manage identities

This section shows how to create, read, update, delete, and list identities using the REST API.

|   |                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM is not primarily an identity store, nor is it provisioning software. For storing identity data, consider PingDS. For provisioning, consider PingIDM. Both of these products provide REST APIs as well. |

AM has the `/json/groups` and `/json/users` JSON-based APIs for managing identities. These APIs follow the common REST pattern for creating, reading, updating, deleting, and querying resources.

Examples in this section do not repeat the authentication shown in [Authenticate over REST](../am-authentication/authn-rest.html). For browser-based clients, you can rely on AM cookies rather than construct the header in your application. Managing agent profiles, groups, and users with these APIs requires authentication. The examples shown in this section were performed with the token ID gained after authenticating as an AM administrator, for example `amAdmin`.

Although the examples here show user management, you can use `/json/groups` in a similar fashion. See [Manage realms](#rest-api-crud-realm) for examples related to realms.

The following sections cover this JSON-based API:

* [Create an identity](#rest-api-create-identity)

* [Read an identity](#rest-api-read-identity)

* [Update an identity](#rest-api-update-identity)

* [Delete an identity](#rest-api-delete-identity)

* [List identities](#rest-api-query-identity)

* [Get identities with the session cookie](#rest-api-retrieve-identity-using-session-cookie)

* [Change passwords](#rest-api-change-password)

* [Create a group](#rest-api-create-group)

* [Add a user to a group](#rest-api-add-user-to-group)

### Create an identity

AM lets administrators create a user profile with an HTTP POST of the JSON representation of the profile to `/json/subrealm/users/?_action=create`. To add a user to the Top Level Realm, you do not need to specify the realm.

The following example shows an administrator creating a new user. The only required fields are `username` and `userpassword`. If no other name is provided, `_id`,`cn`, `sn`, and `uid` are all set to the value of `username`. Values provided for `uid` are not used.

```bash
$ curl \
--request POST \
--header "Accept-API-Version: protocol=2.1,resource=3.0" \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--data \
'{
    "username": "bjensen",
    "userpassword": "Ch4ng31t",
    "mail": "bjensen@example.com"
}' \
'https://am.example.com:8443/am/json/realms/root/users/?_action=create'
{
    "_id": "bjensen",
    "_rev": "-588258934",
    "username": "bjensen",
    "realm": "/",
    "uid": [
        "bjensen"
    ],
    "mail": [
        "bjensen@example.com"
    ],
    "universalid": [
        "id=bjensen,ou=user,dc=am,dc=example,dc=com"
    ],
    "objectClass": [
        "iplanet-am-managed-person",
        "inetuser",
        "sunFederationManagerDataStore",
        "sunFMSAML2NameIdentifier",
        "inetorgperson",
        "sunIdentityServerLibertyPPService",
        "devicePrintProfilesContainer",
        "iplanet-am-user-service",
        "iPlanetPreferences",
        "pushDeviceProfilesContainer",
        "forgerock-am-dashboard-service",
        "organizationalperson",
        "top",
        "kbaInfoContainer",
        "person",
        "sunAMAuthAccountLockout",
        "oathDeviceProfilesContainer",
        "iplanet-am-auth-configuration-service"
    ],
    "inetUserStatus": [
        "Active"
    ],
    "dn": [
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "cn": [
        "bjensen"
    ],
    "sn": [
        "bjensen"
    ],
    "createTimestamp": [
        "20180426120642Z"
    ]
}
```

When `LDAP User Search Attribute` and `Authentication Naming Attribute` are set to different attributes, AM treats `id` and `username` as distinct values. In this case, `_id` is mapped to `LDAP User Search Attribute`, which is autogenerated if not specified in the payload, and `username` is mapped to `Authentication Naming Attribute`.

For example, given the same payload as above, if `LDAP User Search Attribute` is set to `cn`, the user data is set using the generated UUID as follows:

```bash
{
  "_id":"f3377274-99e4-44f3-8578-0a09914368fc",
  "_rev":"-1",
  "realm":"/",
  "username":"bjensen",
  "uid":[
    "bjensen"
  ],
  "mail":["bjensen@example.com"],
  "universalid":[
    "id=f3377274-99e4-44f3-8578-0a09914368fc,ou=user,dc=am,dc=example,dc=com"
  ],
  "objectClass":[
    …​
  ],
  "inetUserStatus":[
    "Active"
  ],
  "dn":[
    "cn=f3377274-99e4-44f3-8578-0a09914368fc,ou=people,dc=am,dc=example,dc=com"],

  "cn":[
    "f3377274-99e4-44f3-8578-0a09914368fc"],
  "sn":[
    "bjensen"
  ],
  "createTimestamp":[
    "20220608100442Z"
  ]
}
```

Alternatively, administrators can create user profiles with specific user IDs by doing an HTTP PUT of the JSON representation of the changes to `/json/users/user-id`, as shown in the following example:

```bash
$ curl \
--request PUT \
--header "Accept-API-Version: protocol=2.1,resource=3.0" \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--header "Content-Type: application/json" \
--header "If-None-Match: *" \
--data \
'{
    "username": "janedoe",
    "userpassword": "Ch4ng31t",
    "mail": "janedoe@example.com"
}' \
'https://am.example.com:8443/am/json/realms/root/users/janedoe'
{
    "_id": "janedoe",
    "_rev": "-1686380958",
    "username": "janedoe",
    "realm": "/",
    "uid": [
        "janedoe"
    ],
    "mail": [
        "janedoe@example.com"
    ],
    "universalid": [
        "id=janedoe,ou=user,dc=am,dc=example,dc=com"
    ],
    "objectClass": [
        "iplanet-am-managed-person",
        "inetuser",
        "sunFederationManagerDataStore",
        "sunFMSAML2NameIdentifier",
        "inetorgperson",
        "sunIdentityServerLibertyPPService",
        "devicePrintProfilesContainer",
        "iplanet-am-user-service",
        "iPlanetPreferences",
        "pushDeviceProfilesContainer",
        "forgerock-am-dashboard-service",
        "organizationalperson",
        "top",
        "kbaInfoContainer",
        "person",
        "sunAMAuthAccountLockout",
        "oathDeviceProfilesContainer",
        "iplanet-am-auth-configuration-service"
    ],
    "dn": [
        "uid=janedoe,ou=people,dc=am,dc=example,dc=com"
    ],
    "inetUserStatus": [
        "Active"
    ],
    "cn": [
        "janedoe"
    ],
    "sn": [
        "janedoe"
    ],
    "createTimestamp": [
        "20180426121152Z"
    ]
}
```

As shown in the examples, AM returns the JSON representation of the profile on successful creation. On failure, AM returns a JSON representation of the error including the [HTTP status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html). For example, version 2.0 of the common REST `/json/users` and `/json/groups` endpoints return 403 if the user making the request is not authorized to do so.

The same HTTP POST and PUT mechanisms also work for other objects, such as groups:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--data '{
    "username":"newGroup"
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/groups?_action=create'
{
    "username":"newGroup",
    "realm":"/alpha",
    "uniqueMember":[
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "cn":[
        "newGroup"
    ],
    "dn":[
        "cn=newGroup,ou=groups,dc=am,dc=example,dc=com"
    ],
    "objectclass":[
        "groupofuniquenames",
        "top"
    ],
    "universalid":[
        "id=newGroup,ou=group,dc=am,dc=example,dc=com"
    ]
}
```

```bash
$ curl \
--request PUT \
--header "If-None-Match: " \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz" \
--header "Content-Type: application/json" \
--data '{
    "username":"anotherGroup",
    "uniquemember":["uid=bjensen,ou=people,dc=am,dc=example,dc=com"]
}' \
'https://am.example.com:8443/am/json/realms/root/groups/realms/alpha/anotherGroup'
{
    "username":"anotherGroup",
    "realm":"/alpha",
    "uniqueMember":[
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "cn":[
        "anotherGroup"
    ],
    "dn":[
        "cn=anotherGroup,ou=groups,dc=am,dc=example,dc=com"
    ],
    "objectclass":[
        "groupofuniquenames",
        "top"
    ],
    "universalid":[
        "id=anotherGroup,ou=group,dc=am,dc=example,dc=com"
    ]
}
```

### Read an identity

AM lets users and administrators read profiles by requesting an HTTP GET on `/json/subrealm/users/user-id`. This allows users and administrators to verify user data, status, and directory. If users or administrators see missing or incorrect information, they can write down the correct information and add it using [Update an identity](#rest-api-update-identity). To read a profile on the Top Level Realm, you do not need to specify the realm.

Users can review the data associated with their own accounts, and administrators can also read other user's profiles.

|   |                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If an administrator user is reading their own profile, an additional `roles` element, with a value of `ui-admin` is returned in the JSON response. The UI verifies this element to grant or deny access to the AM Console. |

The following example shows an administrator accessing user data belonging to `bjensen`:

```bash
$ curl \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
'https://am.example.com:8443/am/json/realms/root/users/bjensen'
{
    "_id":"bjensen",
    "_rev":"-320505756",
    "username":"bjensen",
    "realm":"/",
    "uid":[
        "bjensen"
    ],
    "universalid":[
        "id=bjensen,ou=user,dc=am,dc=example,dc=com"
    ],
    "objectClass":[
        "iplanet-am-managed-person",
        "inetuser",
        "sunFederationManagerDataStore",
        "sunFMSAML2NameIdentifier",
        "devicePrintProfilesContainer",
        "inetorgperson",
        "sunIdentityServerLibertyPPService",
        "iPlanetPreferences",
        "pushDeviceProfilesContainer",
        "iplanet-am-user-service",
        "forgerock-am-dashboard-service",
        "organizationalperson",
        "top",
        "kbaInfoContainer",
        "sunAMAuthAccountLockout",
        "person",
        "oathDeviceProfilesContainer",
        "iplanet-am-auth-configuration-service"
    ],
    "dn":[
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "inetUserStatus":[
        "Active"
    ],
    "sn":[
        "jensen"
    ],
    "cn":[
        "babs"
    ],
    "createTimestamp":[
        "20240105101638Z"
    ],
    "modifyTimestamp":[
        "20240110102632Z"
    ]
}
```

Use the `_fields` query string parameter to restrict the list of attributes returned. This parameter takes a comma-separated list of JSON object fields to include in the result. Note that the `_fields` argument is case-sensitive. In the following example, the returned value matches the specified argument, `uid`, whereas `UID` would not.

```bash
$ curl \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
'https://am.example.com:8443/am/json/realms/root/users/bjensen?_fields=username,uid'
{
    "username":"bjensen",
    "uid":[
        "bjensen"
    ]
}
```

As shown in the examples, AM returns the JSON representation of the profile on success. On failure, AM returns a JSON representation of the error including the [HTTP status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).

### Update an identity

AM lets users update their own profiles, and lets administrators update other users' profiles. To update an identity do an HTTP PUT of the JSON representation of the changes to `/json/subrealm/users/user-id`. To update a profile on the Top Level Realm, you do not need to specify the realm.

The following example shows how users can update their own profiles:

```bash
$ curl \
--request PUT \
--header "iPlanetDirectoryPro: AQIC5…​Y3MTAx*" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: protocol=2.1,resource=3.0" \
--header "If-Match: *" \
--data '{ "mail": "bjensen@example.com" }' \
'https://am.example.com:8443/am/json/realms/root/users/bjensen'
{
    "username":"bjensen",
    "realm":"/",
    "uid":[
        "bjensen"
    ],
    "mail":[
        "bjensen@example.com"
    ],
    "universalid":[
        "id=bjensen,ou=user,dc=am,dc=example,dc=com"
    ],
    "objectClass":[
        "iplanet-am-managed-person",
        "inetuser",
        "sunFederationManagerDataStore",
        "sunFMSAML2NameIdentifier",
        "devicePrintProfilesContainer",
        "inetorgperson",
        "sunIdentityServerLibertyPPService",
        "iPlanetPreferences",
        "pushDeviceProfilesContainer",
        "iplanet-am-user-service",
        "forgerock-am-dashboard-service",
        "organizationalperson",
        "top",
        "kbaInfoContainer",
        "sunAMAuthAccountLockout",
        "person",
        "oathDeviceProfilesContainer",
        "iplanet-am-auth-configuration-service"
    ],
    "dn":[
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "inetUserStatus":[
        "Active"
    ],
    "sn":[
        "jensen"
    ],
    "cn":[
        "babs"
    ],
    "createTimestamp":[
        "20170105101638Z"
    ],
    "modifyTimestamp":[
        "20170110105038Z"
    ],
    "roles":[
        "ui-self-service-user"
    ]
}
```

As shown in the example, AM returns the JSON representation of the profile on success. On failure, AM returns a JSON representation of the error including the [HTTP status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).

You can use HTTP PUT to update other objects as well, such as groups:

Notice in the following example, which updates `newGroup`, the object class value is not included in the JSON sent to AM:

```bash
$ curl \
--request PUT \
--header "iPlanetDirectoryPro: AQIC5…​Y3MTAx*" \
--header "Content-Type: application/json" \
--data '{
    "uniquemember":[
        "uid=newUser,ou=people,dc=am,dc=example,dc=com",
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ]
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/groups/newGroup'
{
    "name":"newGroup",
    "realm":"/alpha",
    "uniqueMember":[
        "uid=newUser,ou=people,dc=am,dc=example,dc=com",
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "cn":[
        "newGroup"
    ],
    "dn":[
        "cn=newGroup,ou=groups,dc=am,dc=example,dc=com"
    ],
    "objectclass":[
        "groupofuniquenames",
        "top"
    ],
    "universalid":[
        "id=newGroup,ou=group,dc=am,dc=example,dc=com"
    ]
}
```

### Delete an identity

AM lets administrators delete a user profile by making an HTTP DELETE call to `/json/subrealm/users/user-id`. To delete a user from the Top Level Realm, you do not need to specify the realm.

The following example removes a user from the top level realm. Only administrators should delete users. The user id is the only field required to delete a user:

```bash
$ curl \
--request DELETE \
--header "Accept-API-Version: protocol=2.1,resource=3.0" \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
'https://am.example.com:8443/am/json/realms/root/users/bjensen'
{
    "_id": "bjensen",
    "_rev": "-1870449267",
    "success": "true"
}
```

On success, AM returns a JSON object indicating success. On failure, AM returns a JSON representation of the error including the [HTTP status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).

You can use this same logic for other resources such as performing an HTTP DELETE on a group:

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--header  "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/groups/newGroup'
{
    "success":"true"
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deleting a user doesn't automatically remove any of their authenticated sessions. If you are using server-side sessions, you can remove authenticated sessions by checking for any sessions for the user and then removing them using the AM admin UI's Sessions page. If you're using client-side sessions, you can't remove authenticated sessions. You must wait for the sessions to expire. |

### List identities

AM lets administrators list identities by making an HTTP GET call to `/json/subrealm/users/?_queryId=*`. To query the Top Level Realm, you do not need to specify the realm:

```bash
$ curl \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
'https://am.example.com:8443/am/json/realms/root/users?_queryId=*'
{
    "result":[
        {
            "username":"amAdmin",
            "realm":"dc=am,dc=example,dc=com",
            "sunIdentityMSISDNNumber":[

            ],
            "mail":[

            ],
            "sn":[
                "amAdmin"
            ],
            "givenName":[
                "amAdmin"
            ],
            "universalid":[
                "id=amadmin,ou=user,dc=am,dc=example,dc=com"
            ],
            "cn":[
                "amAdmin"
            ],
            "iplanet-am-user-success-url":[

            ],
            "telephoneNumber":[

            ],
            "roles":[
                "ui-global-admin",
                "ui-realm-admin"
            ],
            "iplanet-am-user-failure-url":[

            ],
            "inetuserstatus":[
                "Active"
            ],
            "postalAddress":[

            ],
            "dn":[
                "uid=amAdmin,ou=People,dc=am,dc=example,dc=com"
            ],
            "employeeNumber":[

            ],
            "iplanet-am-user-alias-list":[

            ]
        },
        {
            "username":"bjensen",
            "realm":"dc=am,dc=example,dc=com",
            "uid":[
                "bjensen"
            ],
            "createTimestamp":[
                "20160108155628Z"
            ],
            "inetUserStatus":[
                "Active"
            ],
            "mail":[
                "bjensen@example.com"
            ],
            "sn":[
                "jensen"
            ],
            "cn":[
                "babs"
            ],
            "objectClass":[
                "devicePrintProfilesContainer",
                "person",
                "sunIdentityServerLibertyPPService",
                "sunFederationManagerDataStore",
                "inetorgperson",
                "oathDeviceProfilesContainer",
                "iPlanetPreferences",
                "iplanet-am-auth-configuration-service",
                "sunFMSAML2NameIdentifier",
                "organizationalperson",
                "inetuser",
                "kbaInfoContainer",
                "forgerock-am-dashboard-service",
                "iplanet-am-managed-person",
                "iplanet-am-user-service",
                "sunAMAuthAccountLockout",
                "top"
            ],
            "kbaInfo":[
                {
                    "questionId":"2",
                    "answer":{
                        "$crypto":{
                            "value":{
                                "algorithm":"SHA-256",
                                "data":"VXGtsnjJMC…​MQJ/goU5hkfF"
                            },
                            "type":"salted-hash"
                        }
                    }
                },
                {
                    "questionId":"1",
                    "answer":{
                        "$crypto":{
                            "value":{
                                "algorithm":"SHA-256",
                                "data":"cfYYzi9U…​rVfFl0Tdw0iX"
                            },
                            "type":"salted-hash"
                        }
                    }
                }
            ],
            "dn":[
                "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
            ],
            "universalid":[
                "id=bjensen,ou=user,dc=am,dc=example,dc=com"
            ],
            "modifyTimestamp":[
                "20160113010610Z"
            ]
        }
    ],
    "resultCount":2,
    "pagedResultsCookie":null,
    "totalPagedResultsPolicy":"NONE",
    "totalPagedResults":-1,
    "remainingPagedResults":-1
}
```

The `users` endpoint also supports the `_queryFilter` parameter to alter the returned results. For more information, see [Query](../am-rest/rest-intro.html#about-crest-query).

The `_queryId=*` parameter also works for other types of objects, such as groups:

```bash
$ curl \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/groups?_queryId=*'
{
    "result" : [ "newGroup", "anotherGroup" ],
    "resultCount" : 2,
    "pagedResultsCookie" : null,
    "remainingPagedResults" : -1
}
```

As the result lists include all objects, this capability to list identity names is mainly useful in testing.

As shown in the examples, AM returns the JSON representation of the resource list if successful. On failure, AM returns a JSON representation of the error including the [HTTP status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).

### Get identities with the session cookie

If you only have access to the `iPlanetDirectoryPro` session cookie, you can retrieve the user ID by performing an HTTP POST operation on the `/json/users` endpoint using the `idFromSession` action:

```bash
$ curl \
--verbose \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: protocol=2.1,resource=3.0" \
--header "iPlanetDirectoryPro: AQIC5wM2LY4Sfcz…​c5ODk4MjYzMzA2MQ..*" \
'https://am.example.com:8443/am/json/realms/root/users?_action=idFromSession'
{
    "id":"bjensen",
    "realm":"/",
    "dn":"id=bjensen,ou=user,dc=am,dc=example,dc=com",
    "successURL":"/am/console",
    "fullLoginURL":"/am/XUI/?realm=%2F"
}
```

### Change passwords

*Users* other than the top-level administrator can change their own passwords with an HTTP POST to `/json/subrealm/users/username?_action=changePassword` including the new password as the value of `userpassword` in the request data.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Changing the top-level administrator's password requires a more complex procedure. See [Changing the amAdmin Password (UI)](../security/securing-administration.html#amadmin-password-console) for more information. |

Users must provide the current password, which is set in the request as the value of the `currentpassword`.

If a user has forgotten their password, see [Retrieve forgotten usernames](../user-self-service/uss-forgotten-username.html) instead.

The following example shows a successful request to change ``bjensen's password to `M0r3Secur3!``:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: protocol=2.1,resource=3.0" \
--header "iPlanetDirectoryPro: AQIC5w…​NTcy*" \
--data '{
    "currentpassword":"Ch4ng31t",
    "userpassword":"M0r3Secur3!"
}' \
'https://am.example.com:8443/am/json/realms/root/users/bjensen?_action=changePassword'
{}
```

On success, the response is an empty JSON object {} as shown in the example. On failure, AM returns a JSON representation of the error including the [HTTP status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html). See also [HTTP Status Codes](../am-rest/rest-intro.html#about-crest-response-codes) for more information.

*Administrators* can change non-administrative users' passwords with an HTTP PUT to `/json/subrealm/users/username` including the new password as the value of `userpassword` in the request data.

Unlike users, administrators do not provide users' current passwords when changing passwords.

The following example shows a successful request by an administrator to change ``bjensen's password to `M0r3Secur3!``:

```bash
$ curl \
--request PUT \
--header "iPlanetDirectoryPro: AQIC5w…​NTcy*" \
--header "Accept-API-Version: protocol=2.1,resource=3.0" \
--header "Content-Type: application/json" \
--data '{
    "userpassword":"M0r3Secur3!"
}' \
'https://am.example.com:8443/am/json/realms/root/users/bjensen'
{
    "_id":"bjensen",
    "_rev":"-1942782480",
    "username":"bjensen",
    "realm":"/",
    "uid":[
        "bjensen"
    ],
    "mail":[
        "bjensen@example.com"
    ],
    "universalid":[
        "id=bjensen,ou=user,dc=am,dc=example,dc=com"
    ],
    "objectClass":[
        "iplanet-am-managed-person",
        "inetuser",
        "sunFederationManagerDataStore",
        "sunFMSAML2NameIdentifier",
        "devicePrintProfilesContainer",
        "inetorgperson",
        "sunIdentityServerLibertyPPService",
        "iPlanetPreferences",
        "pushDeviceProfilesContainer",
        "iplanet-am-user-service",
        "forgerock-am-dashboard-service",
        "organizationalperson",
        "top",
        "kbaInfoContainer",
        "sunAMAuthAccountLockout",
        "person",
        "oathDeviceProfilesContainer",
        "iplanet-am-auth-configuration-service"
    ],
    "dn":[
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "inetUserStatus":[
        "Active"
    ],
    "sn":[
        "jensen"
    ],
    "cn":[
        "babs"
    ],
    "modifyTimestamp":[
        "20240110105705Z"
    ],
    "createTimestamp":[
        "20240105101638Z"
    ]
}
```

As shown in the example, AM returns the JSON representation of the profile on success. On failure, AM returns a JSON representation of the error including the [HTTP status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html). Learn more in [HTTP Status Codes](../am-rest/rest-intro.html#about-crest-response-codes).

### Create a group

AM lets administrators create a group with an HTTP POST of the JSON representation of the group to the `/json/subrealm/groups?_action=create` endpoint.

The following example shows how to create a group called `newGroup` in the top level realm using the REST API after authenticating to AM:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--data '{
    "username":"newGroup"
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/groups?_action=create'
{
    "username":"newGroup",
    "realm":"/alpha",
    "uniqueMember":[
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "cn":[
        "newGroup"
    ],
    "dn":[
        "cn=newGroup,ou=groups,dc=am,dc=example,dc=com"
    ],
    "objectclass":[
        "groupofuniquenames",
        "top"
    ],
    "universalid":[
        "id=newGroup,ou=group,dc=am,dc=example,dc=com"
    ]
}
```

### Add a user to a group

AM lets administrators add a user to an existing group with an HTTP PUT to the JSON representation of the group to the `/json/subrealm/groups/groupName` endpoint.

The following example shows how to add users to an existing group by using the REST API. The example assumes that the DS backend is in use. Make sure to use the `uniquemember` attribute to specify the user using the DS server:

```bash
$ curl \
--request PUT \
--header "iPlanetDirectoryPro: AQIC5…​Y3MTAx*" \
--header "Content-Type: application/json" \
--data '{
    "uniquemember":[
        "uid=newUser,ou=people,dc=am,dc=example,dc=com",
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ]
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/groups/newGroup'
{
    "name":"newGroup",
    "realm":"/alpha",
    "uniqueMember":[
        "uid=newUser,ou=people,dc=am,dc=example,dc=com",
        "uid=bjensen,ou=people,dc=am,dc=example,dc=com"
    ],
    "cn":[
        "newGroup"
    ],
    "dn":[
        "cn=newGroup,ou=groups,dc=am,dc=example,dc=com"
    ],
    "objectclass":[
        "groupofuniquenames",
        "top"
    ],
    "universalid":[
        "id=newGroup,ou=group,dc=am,dc=example,dc=com"
    ]
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For Active Directory implementations, use the `member` attribute when adding a user to a group using the REST API:```bash
$ curl \
--request PUT \
--header "iPlanetDirectoryPro: AQIC5…​Y3MTAx*" \
--header "Content-Type: application/json" \
--data '{
    "member":[
        "cn=newUser,cn=users,dc=example,dc=com",
        "cn=bjensen,cn=users,dc=example,dc=com"
    ]
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/groups/newGroup'
{
    "username": "newGroup",
    "realm": "/alpha",
    "sAMAccountName": ["$FL2000-EP4RN8LPBKUS"],
    "universalid": ["id=newGroup,ou=group,dc=example,dc=com"],
    "sAMAccountType": ["268435456"],
    "member": ["cn=newUser,cn=users,dc=example,dc=com", "cn=bjensen,cn=users,dc=example,dc=com"],
    "name": ["newGroup"],
    "objectClass":    [
        "top",
        "group"
    ],
    "distinguishedName": ["CN=newGroup,CN=Users,dc=example,dc=com"],
    "dn": ["CN=newGroup,CN=Users,dc=example,dc=com"],
    "cn": ["newGroup"],
    "objectCategory": ["CN=Group,CN=Schema,CN=Configuration,dc=example,dc=com"]
}
``` |

## Manage realms

This section shows how to create, read, update, and delete realms using the `/json/global-config/realms` endpoint.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use the AM API Explorer for detailed information about this endpoint, and to test it against your deployed AM instance.In the AM admin UI, click the Help icon, and then go to API Explorer > /global-config > /realms. |

The following sections cover managing realms with the REST API:

* [Required realm properties](#rest-api-parameters-realm)

* [Create a realm](#rest-api-create-realm)

* [List realms](#rest-api-list-realm)

* [Read a realm](#rest-api-read-realm)

* [Update a realm](#rest-api-update-realm)

* [Delete a realm](#rest-api-delete-realm)

### Required realm properties

The following table shows the required properties when managing realms using the REST API:

**Realm Properties for JSON-based API**

| Realm Property | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | The name of the realm.&#xA;&#xA;Realm names can't match any of the following:&#xA;&#xA;Existing realm names.&#xA;&#xA;Existing realm aliases.&#xA;&#xA;Names of AM REST endpoints.&#xA;&#xA;List of names that can't be used for a new realm by default&#xA;agents&#xA;api&#xA;applications&#xA;applicationtypes&#xA;authenticate&#xA;cache&#xA;conditiontypes&#xA;dashboard&#xA;decisioncombiners&#xA;docs&#xA;email&#xA;global-audit&#xA;global-config&#xA;groups&#xA;health&#xA;metrics&#xA;policies&#xA;push&#xA;realm-audit&#xA;realm-config&#xA;realms&#xA;records&#xA;resourcetypes&#xA;scripts&#xA;selfservice&#xA;serverinfo&#xA;sessions&#xA;subjectattributes&#xA;subjecttypes&#xA;things&#xA;timetravel&#xA;token&#xA;tokens&#xA;users |
| `active`       | Whether the realm is to be active, or not.Specify either `true` or `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `parentPath`   | The path of the parent realm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `aliases`      | An array of any applicable aliases associated with the realm. Be aware that an alias can only be used once. Entering an alias used by another realm will remove the alias from that realm and you will lose configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

The following JSON object shows an example realm configuration:

```json
{
    "name": "mySubRealm",
    "active": true,
    "parentPath": "/",
    "aliases": [ "payroll.example.com" ]
}
```

### Create a realm

AM lets administrators create a realm by performing an HTTP POST of the JSON representation of the realm to `/json/global-config/realms`.

The following example creates a new, active subrealm in the top level realm, named `mySubRealm`:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--header  "Accept-API-Version: resource=1.0" \
--data '{
    "name": "mySubRealm",
    "active": true,
    "parentPath": "/",
    "aliases": [ "payroll.example.com" ]
}' \
https://am.example.com:8443/am/json/global-config/realms
{
    "_id": "L2Fub3RoZXJSZWFsbQ",
    "_rev": "-1054013208",
    "parentPath": "/",
    "active": true,
    "name": "mySubRealm",
    "aliases": [ "payroll.example.com" ]
}
```

AM returns a 201 HTTP status code and a JSON representation of the realm on success. The value returned in the `_id` field is used in subsequent REST calls relating to the realm. On failure, AM returns a JSON representation of the error including the HTTP status code. For more information, see [HTTP Status Codes](../am-rest/rest-intro.html#about-crest-response-codes).

### List realms

To list and query realms, perform an HTTP GET on the `/json/global-config/realms` endpoint, and set the `_queryFilter` query string parameter to `true` as in the following example, which lists all available realms:

```bash
$ curl \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header  "Accept-API-Version: resource=1.0, protocol=2.1" \
https://am.example.com:8443/am/json/global-config/realms?_queryFilter=true
{
    "result":[
        {
            "_id":"Lw",
            "_rev":"252584985",
            "parentPath":null,
            "active":true,
            "name":"/",
            "aliases":[
                "am.example.com",
                "am"
            ]
        },
        {
            "_id":"L215U3ViUmVhbG0",
            "_rev":"949061198",
            "parentPath":"/",
            "active":true,
            "name":"mySubRealm",
            "aliases":[
                "payroll.example.com"
            ]
        }
    ],
    "resultCount":2,
    "pagedResultsCookie":null,
    "totalPagedResultsPolicy":"NONE",
    "totalPagedResults":-1,
    "remainingPagedResults":-1
}
```

For more information about using the `_queryString` parameter in REST calls, see [Query](../am-rest/rest-intro.html#about-crest-query).

### Read a realm

To read a realm's details, send an HTTP GET to the `/json/global-config/realms/realm-id` endpoint, where `realm-id` is the value of `_id` for the realm.

The following example shows an administrator receiving information about a realm called `mySubRealm`, which has an `_id` value of `L215U3ViUmVhbG0`:

```bash
$ curl \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--header "Accept-API-Version: resource=1.0" \
https://am.example.com:8443/am/json/global-config/realms/L215U3ViUmVhbG0
{
    "_id": "L215U3ViUmVhbG0",
    "_rev": "949061698",
    "parentPath": "/",
    "active": true,
    "name": "mySubRealm",
    "aliases": [
        "payroll.example.com"
    ]
}
```

AM returns a 200 HTTP status code and a JSON representation of the realm on success. On failure, AM returns a JSON representation of the error including the HTTP status code. For more information, see [HTTP Status Codes](../am-rest/rest-intro.html#about-crest-response-codes).

### Update a realm

To update a realm's aliases or to toggle between active and inactive, send an HTTP PUT to the `/json/global-config/realms/realm-id` endpoint, where `realm-id` is the value of `_id` for the realm.

The request should include an updated JSON representation of the complete realm. Note that you cannot alter the `name` or `parent` properties of a realm.

The following example shows how to update a realm called `mySubRealm`, which has an `_id` value of `L215U3ViUmVhbG0`. The example changes the realm status to inactive:

```bash
$ curl \
--request PUT \
--header "iPlanetDirectoryPro: AQIC5…​Y3MTAx*" \
--header "Content-Type: application/json" \
--header  "Accept-API-Version: resource=1.0, protocol=1.0" \
--data '{
    "parentPath": "/",
    "active": false,
    "name": "mySubRealm",
    "aliases": [
        "payroll.example.com"
    ]
}' \
https://am.example.com:8443/am/json/global-config/realms/L215U3ViUmVhbG0
{
    "_id": "L215U3ViUmVhbG0",
    "_rev": "94906213",
    "parentPath": "/",
    "active": false,
    "name": "mySubRealm",
    "aliases": [
        "payroll.example.com"
    ]
}
```

AM returns a 200 HTTP status code and a JSON representation of the realm on success. On failure, AM returns a JSON representation of the error including the HTTP status code. For more information, see [HTTP Status Codes](../am-rest/rest-intro.html#about-crest-response-codes).

### Delete a realm

To delete a realm, perform an HTTP DELETE on the `/json/global-config/realms/realm-id` endpoint, where `realm-id` is the value of `_id` for the realm.

The following example shows how to delete a realm called `mySubRealm`, which has an `_id` value of `L215U3ViUmVhbG0`.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure that you do not have any information you need within a realm before deleting it. Once a realm is deleted, the only way to restore it is to return to a previously backed up deployment of AM. |

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--header  "Accept-API-Version: resource=1.0" \
https://am.example.com:8443/am/json/global-config/realms/L215U3ViUmVhbG0
{
    "_id": "L215U3ViUmVhbG0",
    "_rev": "949061708",
    "parentPath": "/",
    "active": false,
    "name": "mySubRealm",
    "aliases": [
        "payroll.example.com"
    ]
}
```

AM returns a 200 HTTP status code and a JSON representation of the deleted realm on success. On failure, AM returns a JSON representation of the error including the HTTP status code. For more information, [HTTP Status Codes](../am-rest/rest-intro.html#about-crest-response-codes).

---

---
title: Configure policy and application stores
description: Configure external policy and application stores by connecting PingAM to directory servers and enabling realms to use them
component: pingam
version: 8.1
page_id: pingam:setup:setting-up-policy-and-app-stores
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/setting-up-policy-and-app-stores.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Policy", "Application Store", "Directory Server"]
page_aliases: ["setup-guide:setting-up-policy-and-app-stores.adoc"]
section_ids:
  proc-connecting-am-to-external-stores: Connect AM to a policy or application store
  proc-enabling-external-stores: Configure a realm to use a policy or application store
  proc-removing-external-stores: Remove a policy or application store
---

# Configure policy and application stores

Setting up an external policy or application store involves the following steps:

1. Configuring the connection between AM and the directory server.

   Refer to [Connect AM to a policy or application store](#proc-connecting-am-to-external-stores).

2. Enabling a realm to use the newly configured directory server.

   Refer to [Configure a realm to use a policy or application store](#proc-enabling-external-stores).

## Connect AM to a policy or application store

1. These steps assume you have [installed and configured DS as a policy or application store](prepare-policy-and-application-store.html#prepare-ds-for-policy-and-application).

2. In the AM admin UI, go to Configure > Global Services > External Data Stores.

3. On the Secondary Configurations tab, click Add a Secondary Configuration.

4. Complete the form as follows:

   1. In the Name field, enter a name for the datastore; for example, `myPolicyStore`.

   2. If you're ready to use this datastore, select Enabled.

      If you enable an external datastore configuration, AM checks that it can connect to the server when you save the configuration.

      You can't select a datastore configuration for use (at the realm or global level) until you enable it.

      |   |                                                                                                                                                                                                                                                                                                                            |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you're configuring mTLS authentication to the datastore, don't enable the connection until you have added an mTLS Secret Label Identifier and the corresponding entry in the secret store. You can't do this on the create page. You must save the configuration, then edit it to add the mTLS Secret Label Identifier. |

   3. In the Host Urls field, enter one or more connection strings. The format for each connection string is `HOST:PORT`. For example `policies.example.com:1636` or `applications.example.com:1636`.

      Multiple connection strings must be comma-separated, for example, `policies1.example.com:1636, policies2.example.com:1636`.

      AM uses the first connection string in the list unless the server is unreachable. In this case, it tries the next connection strings in the order in which they're defined.

      In production environments, you should specify more than one connection string for failover purposes.

   4. Enter the Bind DN and Bind Password of the service account AM uses to authenticate to the data store.

   5. Select Use SSL to connect to the directory server over SSL.

   6. Select mTLS Enabled to authenticate to the directory server using mTLS instead of a bind DN and password.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you enable mTLS, you must also:- Set Use SSL to true.

      - Set secure ports in the Host Urls property.

      - Configure the directory server and mappings for mTLS, as described in [mTLS for policy and application stores](../security/secure-connections.html#mtls-policy-application-stores).

      - Set an mTLS Secret Label Identifier after you save the configuration. (Refer to [step 6](#mtls-secret-label) of this procedure.)AM ignores the values of the Bind DN and Bind Password when mTLS Enabled is `true`. |

   7. Specify whether the directory servers you're using as application and policy stores use affinity load balancing, rather than a single primary directory instance in an active/passive deployment.

      If you enable this option, specify each of the directory server instances that form the affinity deployment in the Host Urls field.

5. To save your changes, click Create.

   If the configuration is Enabled, AM attempts to connect to the datastore using the specified settings, saves the connection, and makes it available for use as a policy or application store.

   If the connection is unsuccessful, AM logs an error: `Failed to load resource: the server responded with a status of 400 ()`.

   On successful connection, AM attempts to change the schema and structure of the external directory server. If the specified Bind DN property doesn't have permission to change the schema and structure, you must apply the required settings manually. For details, refer to [Prepare datastores](../installation/prepare-ext-stores.html).

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | You can select an external datastore for use at the global or realm level *only* when it's Enabled. |

6. []()If you enabled mTLS authentication to the datastore, edit the configuration to set an mTLS Secret Label Identifier.

   To edit the connection settings:

   1. Click the Secondary Configuration tab and click the name of the datastore configuration.

   2. Add an mTLS Secret Label Identifier.

      AM uses this identifier to create a specific secret label for this policy or application store. It uses the secret label to map to the mTLS certificate in the secret store.

      The generated secret label takes the form `am.external.datastore.identifier.mtls.cert`, where `identifier` is the value of mTLS Secret Label Identifier. You can only view and map the secret label after you have set the identifier.

      The identifier can only contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and periods (`.`). It can't start or end with a period.

      All LDAP servers configured for this policy or application store share the same secret label identifier.

   3. Click Save Changes.

7. Repeat these steps for additional policy or application stores.

You can now [configure AM to use the new policy or application store](#proc-enabling-external-stores).

## Configure a realm to use a policy or application store

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Changing the policy or application store will cause any existing policies or applications to become unavailable to the realm. |

Either recreate the policies or applications manually, or use [Amster](../amster/preface.html) to export the existing instances, then import them back after changing the stores.

1. In the AM admin UI, go to Realms > *realm name* Services.

2. Configure the External Data Stores service in the realm:

   1. If the External Data Stores service has not yet been added to the realm, click Add a Service, and select External Data Stores.

   2. If the External Data Stores service has already been added to the realm, click External Data Stores to edit the configuration.

3. On the External Data Stores page, select the name of the store to use as the Policy Data Store and/or Application Data Store, and click Save Changes.

   |   |                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you choose the `Default Datastore` option for either property, AM uses the configuration datastore you specified during installation. |

   Changes take effect immediately. New policies or applications are created in the configured datastore.

## Remove a policy or application store

Follow these steps to remove a policy or application store from a realm, and to delete the store from the AM configuration.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | You can't remove a policy or application store a realm is currently using. |

1. For each realm that's using the store, in the AM admin UI, go to Realms > *realm name* > Services > External Data Stores, and change each of the drop-down menus to either `Default Datastore`, or an alternative datastore.

   Save your changes.

2. Go to Configure > Global Services > External Data Stores > Secondary Configurations. Click the name of the store to remove, and click the delete icon.

   If the datastore is still in use, AM returns the following error message:

   `Unable to modify data store instance because it is referenced by the data store service of realm /realm-name`

   In this case, repeat the first step to remove the unwanted store from the listed realm, then repeat this step.

---

---
title: Configure realms in the UI
description: Create and configure realms in PingAM through the admin UI, including setting up realm aliases and DNS aliases for multi-domain deployments
component: pingam
version: 8.1
page_id: pingam:setup:configure-realms-console
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/configure-realms-console.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Realms"]
page_aliases: ["setup-guide:configure-realms-console.adoc"]
section_ids:
  create-new-realm: Create a new realm
  configure-realm-dns-alias: Configure DNS aliases to access a realm
---

# Configure realms in the UI

To create and configure realms through the AM admin UI, start from the Realms page.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you use DNS aliases, AM requires cookies for all configured realms.For example, if you install AM in the domain, `am.example.net` and have realms, `identity.example.org` and `security.example.com`, you must configure cookie domains for `.example.net`, `.example.org`, and `.example.com`.You can set up cookie domains for each realm by following the procedure in [Configure DNS aliases to access a realm](#configure-realm-dns-alias). |

## Create a new realm

You can create a new realm through the AM admin UI as described below:

1. In the AM admin UI, go to Realms and click New Realm.

   On the New Realm page, configure the realm.

2. In the Name field, enter a descriptive name for the realm.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Realm names can't match any of the following:* Existing realm names.

   * Existing realm aliases.

   * Names of AM REST endpoints.> **Collapse: List of names that can't be used for a new realm by default**
   >
   > ```none
   > agents
   > api
   > applications
   > applicationtypes
   > authenticate
   > cache
   > conditiontypes
   > dashboard
   > decisioncombiners
   > docs
   > email
   > global-audit
   > global-config
   > groups
   > health
   > metrics
   > policies
   > push
   > realm-audit
   > realm-config
   > realms
   > records
   > resourcetypes
   > scripts
   > selfservice
   > serverinfo
   > sessions
   > subjectattributes
   > subjecttypes
   > things
   > timetravel
   > token
   > tokens
   > users
   > ``` |

3. The realm is active by default.

   |   |                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------- |
   |   | If you configure the realm to be inactive, users cannot use it to authenticate, or be granted access to protected resources. |

4. In the Parent field, enter the parent of your realm.

   Default: the Top Level Realm (`/`).

5. In the Realm Aliases field, enter a simple text alias to represent the realm.

6. In the DNS Aliases field, enter fully qualified domain names (FQDN) that can be used to represent the realm.

   A DNS alias is not related to the CNAME record used in DNS database zones. In other words, the option shown in the AM admin UI does not conform to the definition of DNS aliases described in [RFC 2219](https://datatracker.ietf.org/doc/html/rfc2219).

   |   |                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Entering a DNS alias in the AM admin UI also applies required changes to the advanced server property `com.sun.identity.server.fqdnMap`. |

   For more information, see [Configure DNS aliases to access a realm](#configure-realm-dns-alias).

7. To enable client-side sessions for the realm, toggle the Use Client-Side Sessions switch.

   Learn more in [Introduction to sessions](../am-sessions/about-sessions.html).

8. Click Create to save your configuration.

## Configure DNS aliases to access a realm

You can configure realms to be associated with specific fully qualified domain names (FQDN).

For example, consider a deployment with the following characteristics:

* The FQDN for AM and the top level realm is `am.example.com`.

* AM also services `realm1.example.com`, and `realm2.example.com`. In other words, AM receives all HTTP(S) connections for these host names. Perhaps they share an IP address, or AM listens on all interfaces.

Without applying DNS aliases to the relevant realm, when a user visits `https://realm1.example.com:8443/am`, AM redirects that user to the top level realm, `https://am.example.com:8443/am`. If the authenticating user is present only in `realm1`, then authentication fails even with correct credentials.

If no DNS alias is configured for a realm, `realm1` users must visit URLs such as `https://am.example.com:8443/am/XUI/?realm=/realm1#login`. This format of URL reveals the top level realm, and exposes extra information about the service.

Configure DNS aliases for realms to prevent redirection and having to expose the top level realm domain by performing the following steps:

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Realm aliases must be unique within an AM instance, and cannot contain the characters `"`, `#`, `$`, `%`, `&`, `+`, `,`, `/`, `:`, `;`, `<`, `=`, `>`, `?`, `@`, `\`, or spaces. |

1. Add the domains that AM services to the list of domains that created cookies will be applicable to, as follows:

   * In the AM admin UI, go to Configure > Global Services > Platform.

   * In Cookie Domains, enter the domains that AM will service.

     For example, if you install AM at `am.example.net`, and intend to have realms associated with the FQDNs `realm1.example.org` and `realm2.example.com`, the Cookie Domains list will include `example.net`, `example.org`, and `example.com`.

2. Set the FQDN for each realm as follows:

   * Go to Realms > *realm name* > Properties.

   * In DNS Aliases, enter one or more FQDN values for the realm.

   * Save your changes.

3. Adding DNS aliases by using the AM admin UI also adds FQDN mappings to the AM server.

   To verify these have been created perform the following steps:

   * Go to Configure > Server Defaults > Advanced.

   * For each FQDN DNS alias configured, verify the existence of a property named `com.sun.identity.server.fqdnMap[Realm FQDN]` with a property value of *Realm FQDN*.

     For example, the property may be called `com.sun.identity.server.fqdnMap[realm1.example.com]` with a value of `realm1.example.com`.

     If the property does not exist or needs to be changed, manually create the property for each FQDN DNS alias.

   * Save your changes.

   The new realm aliases take effect immediately, it is not necessary to restart AM. You can now use a URL such as `https://realm1.example.com:8443/am` to access `realm1`, rather than `https://am.example.com:8443/am/XUI/?realm=/realm1#login`.

---

---
title: CTS properties
description: Configure PingAM Core Token Service storage location, connection settings, and LDAP datastore properties for token management
component: pingam
version: 8.1
page_id: pingam:setup:server-cts
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/server-cts.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["setup-guide:server-cts.adoc"]
section_ids:
  cts-tokenstore: CTS token store
  cts-external-tokenstore: External store configuration
---

# CTS properties

You can configure the Core Token Service (CTS) to store tokens in the same LDAP directory as the AM configuration or in a separate external directory server. Take note of specific requirements for indexing and replication. In particular, manage WAN replication carefully for optimum performance.

Tune advanced properties related to token size correctly, for example:

* `com.sun.identity.session.repository.enableEncryption`

* `com.sun.identity.session.repository.enableCompression`

* `com.sun.identity.session.repository.enableAttributeCompression`

Find more information in [Advanced properties](server-advanced.html).

## CTS token store

Set the following properties on the CTS Token Store tab:

* Store Mode

  Specifies the datastore where AM stores CTS tokens. Possible values are:

  * `Default Token Store`: AM stores CTS tokens in the configuration datastore.

  * `External Token Store`: AM stores CTS tokens in an external datastore.

  If you specify `Default Token Store`, you can't access the configuration properties on the External Store Configuration tab.

* Root Suffix

  This property sets the base DN for CTS storage. For example, `cn=cts,ou=famrecords,ou=openam-session,ou=tokens`. The Root Suffix specifies a database that can be maintained and replicated separately from the standard user datastore.

* Max Connections

  The maximum number of remote connections to the external datastore. For affinity deployments, this property specifies the maximum number of remote connections to each directory server in the connection string.

  Default: `100`

  Find recommended settings in [Tune CTS store LDAP connections](../maintenance/tuning-ldap-settings.html#tuning-ldap-settings-cts).

* Page Size

  The number of results per page returned from the CTS datastore.

  If the result set is *smaller* than the page size, the number of results is never paginated. If the result set is *larger*, the number of pages returned is the result set size divided by the page size.

  Increasing the page size results in fewer round trips to the CTS datastore when retrieving large result sets.

  To return all results and disable pagination, set to `0`.

  Default: `0`

* VLV Page Size

  The number of results per page returned from the underlying CTS datastore when using virtual list views (VLVs). Larger values will result in fewer round trips to the datastore when retrieving large result sets, and VLVs are enabled on the datastore.

  Find more information on VLVs in [Virtual List View Index](https://docs.pingidentity.com/pingds/8.1/config-guide/indexing.html#configure-vlv) in the DS documentation.

  Default: `10`

## External store configuration

The External Store Configuration tab lets you set connection details to one or more external PingDS instances.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you can select `External Token Store` on the CTS Token Store tab, you *must* complete the connection details on this tab. |

* SSL/TLS Enabled

  Enables a secure connection to the directory server. Connections to PingDS *must* be secure.

* mTLS Enabled

  When enabled, AM uses mutual TLS (mTLS) to authenticate to the PingDS using trusted certificates.

  When you enable mTLS, AM ignores the values of the Login Id and Password properties.

  You must also:

  * Set SSL/TLS Enabled.

  * Set a secure port in the Connection String(s) property.

  Find information on configuring certificates and keystore mappings in [Secret stores](../security/secret-stores.html).

  |   |                                                                                                                                                                                                             |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You must configure the corresponding secret mapping *before* you enable an mTLS connection to the PingDS. If you try to save an mTLS configuration before configuring the mapping, the UI returns an error. |

* Start TLS

  When enabled, AM uses startTLS to secure the connection to the external directory server.

* Connection String(s)

  An ordered list of connection strings for external DS servers. The format is `HOST:PORT[|SERVERID[|SITEID]]`, where `HOST:PORT` are the DS FQDN and its port. `SERVERID` and `SITEID` are optional parameters to specify an AM instance that prioritizes the particular connection. This doesn't exclude other AM instances from using that connection, although they must have no remaining priority connections available to them before they use it.

  Multiple connection strings must be comma-separated, for example, `cts1.example.com:1636, cts2.example.com:1636`.

  AM uses the first connection string in the list unless the server is unreachable. In this case, it tries the next connection strings in the order in which they're defined.

  In production environments, you should specify more than one connection string for failover purposes.

  > **Collapse: Examples for active/passive deployments**
  >
  > * `cts-ds1.example.com:1636,cts-ds2.example.com:1636`
  >
  >   Every AM instance accesses `cts-ds1.example.com:1636` for all CTS operations. If that server goes down, they access `cts-ds2.example.com:1636`.
  >
  >   Each AM opens new connections to `cts-ds1.example.com:1636` when that directory server becomes available.
  >
  > * `cts-ds1.example.com:1636|1|1,cts-ds2.example.com:1636|2|1`
  >
  >   Server 1 site 1 gives priority to `cts-ds1.example.com:1636`. Server 2 site 1 gives priority to `cts-ds2.example.com:1636`. Any server not specified accesses the first server on the list, while it is available.
  >
  >   If `cts-ds1.example.com:1636` goes down, server 1 site 1 accesses `cts-ds2.example.com:1636`. Any server not specified accesses the second server on the list.
  >
  >   If `cts-ds2.example.com:1636` goes down, server 2 site 1 accesses `cts-ds1.example.com:1636`. Any server not specified still accesses the first server on the list.
  >
  >   Server 1 site 1 and any server not specified opens new connections to `cts-ds1.example.com:1636` when it becomes available. Only server 2 site 1 opens new connections to `cts-ds2.example.com:1636` when it becomes available.
  >
  > * `cts-ds1.example.com:1636|1|1,cts-ds2.example.com:1636|1|1,cts-ds3.example.com:1636|1|2`
  >
  >   Server 1 site 1 gives priority to `cts-ds1.example.com:1636`. Any server not specified accesses the first server on the list, while it is available.
  >
  >   If `cts-ds1.example.com` goes down, server 1 site 1 accesses `cts-ds2.example.com:1636`. Any server not specified accesses the second server on the list.
  >
  >   If both `cts-ds1.example.com` and `cts-ds2.example.com` go down, server 1 site 1 accesses `cts-ds3.example.com:1636` in site 2. Any server not specified accesses the third server on the list.
  >
  >   Server 1 site 1 and any server not specified opens new connections to any server in site 1 when they become available, with `cts-ds1.example.com` being the preferred server.

  > **Collapse: Example for affinity deployments**
  >
  > * `cts-ds1.example.com:1636,cts-ds2.example.com:1636,cts-ds3.example.com:1636,cts-ds4.example.com:1636`
  >
  >   Access CTS tokens from one of the four servers listed in the connection string. For any given CTS token, AM determines the token's affinity for one of the four servers, and always accesses the token from that same server. Tokens are distributed equally across the four servers.

* Login Id

  The DN of the user who authenticates to the external datastore. This user needs sufficient privileges to read and write to the root suffix of the external PingDS.

* Password

  The password associated with the login ID.

  If you enable mTLS, AM ignores the values of the Login Id and Password properties.

* Heartbeat

  The interval, in seconds, that AM should send a heartbeat request to the PingDS to ensure that the connection isn't idle. Configure the heartbeat to ensure that network hardware, such as routers and firewalls, doesn't drop the connection between AM and the directory server.

  Default: `10`

* Affinity Enabled

  When enabled, AM accesses the CTS token store in multiple DS instances in an affinity deployment rather than a single PingDS instance in an active/passive deployment.

  If you enable this option, make sure that the value of the Connection String(s) property is identical for every server in multi-server deployments.

  Default: Disabled

---

---
title: Customize identity stores
description: Extend PingAM identity stores with custom attributes and repository plugins to store additional information and customize user and group mapping
component: pingam
version: 8.1
page_id: pingam:setup:customizing-data-stores
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/customizing-data-stores.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Customization", "Identity Store", "LDAP"]
page_aliases: ["setup-guide:customizing-data-stores.adoc"]
section_ids:
  sec-maint-datastore-customattr: Add custom user profile attributes
  add-attr-to-identity-repository: Update the identity store for a custom attribute
  allow-users-to-update-attr: Use an LDAP browser to let users update custom attributes
  allow-users-to-update-attr-command-line: Use the command line to let users update custom attributes
  updating-XUI: Add custom attributes to the end-user UI
  sec-maint-datastore-plugin: Customize identity data storage with an IdRepo plugin
  idrepo-plugin-inheritance: IdRepo plugin inheritance
  idrepo-plugin-lifecycle: IdRepo plugin lifecycle
  idrepo-plugin-capabilities: IdRepo plugin capabilities
  getsupportedtypes: getSupportedTypes()
  getsupportedoperations: getSupportedOperations()
  supportsauthentication: supportsAuthentication()
  idrepo-plugin-implementation: IdRepo plugin implementation
  idrepo-plugin-deployment: IdRepo plugin deployment
  identity-repository-plugin-annotation: Register your plugin with AM
  use_your_new_idrepo_plugin: Use your new IdRepo plugin
---

# Customize identity stores

Your deployment might require additional functionality than that offered by the default AM identity store. Use these sections to create custom attributes to store additional information in identity stores, or to create identity repository plugins to customize how AM maps users and groups to a realm:

* [Add custom user profile attributes](#sec-maint-datastore-customattr)

* [Customize identity data storage with an IdRepo plugin](#sec-maint-datastore-plugin)

## Add custom user profile attributes

You can extend user profiles by adding custom attributes. This section shows how to add a custom attribute to user profiles stored in the LDAP directory.

Adding a custom attribute involves updating the identity store schema to hold the new attribute, and updating the UI. To give users write permissions to the custom attribute, you must also update the AM configuration store.

This section includes the following procedures:

* [Update the identity store for a custom attribute](#add-attr-to-identity-repository)

* [Use an LDAP browser to let users update custom attributes](#allow-users-to-update-attr)

* [Use the command line to let users update custom attributes](#allow-users-to-update-attr-command-line)

* [Add custom attributes to the end-user UI](#updating-XUI)

### Update the identity store for a custom attribute

These steps update the identity store schema for the custom attribute, then update AM to use the custom attribute and object class.

If you intend to use an existing attribute that is already allowed in user profile entries, you can skip these steps.

1. Prepare the attribute type object class definitions in LDIF format. For example:

   ```bash
   $ cat custom-attr.ldif
   dn: cn=schema
   changetype: modify
   add: attributeTypes
   attributeTypes: ( temp-custom-attr-oid NAME 'customAttribute' EQUALITY case
    IgnoreMatch ORDERING caseIgnoreOrderingMatch SUBSTR caseIgnoreSubstrings
    Match SYNTAX 1.3.6.1.4.1.1466.115.121.1.15 USAGE userApplications )
   -
   add: objectClasses
   objectClasses: ( temp-custom-oc-oid NAME 'customObjectclass' SUP top AUXILIARY
     MAY customAttribute )
   ```

   In this example, the attribute type is called `customAttribute` and the object class is called `customObjectclass`.

2. Add the schema definitions to the directory.

   ```
   $ /path/to/opendj/bin/ldapmodify \
   --hostname 'ds.example.com' \
   --port 1636 \
   --useSsl \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   /path/to/custom-attr.ldif
   Processing MODIFY request for cn=schema
   MODIFY operation successful for DN cn=schema
   ```

3. In the AM admin UI, go to Realms > *realm name* > Identity Stores > *identity store name* > User Configuration.

4. Add the object class, for example `customObjectclass`, to the LDAP User Object Class list.

5. Add the attribute type, for example `customAttribute`, to the LDAP User Attributes list.

6. Save your work.

7. Add the attribute type to the profile attribute allowlist.

   The profile attribute allowlist controls the information returned to non-administrative users when they send requests to `json/user` endpoints. For example, the allowlist controls the attributes shown in the user profile page.

   Common profile attributes are allowlisted by default. You must add any custom attributes that you want non-administrative users to see.

   The allowlist can be set globally, or per realm, in the user self-service service. To modify the list:

   * Globally

     Go to Configure > Global Services > User Self-Service > Profile Management, and edit the Self readable attributes field.

   * By realm

     Go to Realms > *realm name* > Services > User Self-Service > Profile Management, and edit the Self readable attributes field.

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must add the user self-service service to the realm if you have not done so already, but you don't need to configure anything other than the allowlist. |

### Use an LDAP browser to let users update custom attributes

Update the AM configuration store to give users write permission to the custom attribute.

This procedure assumes that you use an LDAP browser, for example, [Apache Directory Studio](http://directory.apache.org/studio/). If you use the command line, follow [Use the command line to let users update custom attributes](#allow-users-to-update-attr-command-line).

1. Connect to the AM configuration store.

   You can see the configuration store details at Deployment > Servers > Directory Configuration > Server.

2. Search for `ou=SelfWriteAttributes`.

   You should find DNs similar to the following. The DNs have been folded for legibility:

   * `dn:ou=SelfWriteAttributes,ou=Policies,ou=default,ou=OrganizationConfig,ou=1.0, ou=iPlanetAMPolicyService,ou=services,o=sunamhiddenrealmdelegationservicepermissions, ou=services,dc=am,dc=example,dc=com`

   * `dn:ou=SelfWriteAttributes,ou=default,ou=default,ou=OrganizationConfig,ou=1.0, ou=sunEntitlementIndexes,ou=services,o=sunamhiddenrealmdelegationservicepermissions, ou=services,dc=am,dc=example,dc=com`

3. In the entry under `iPlanetAMPolicyService`, edit the `sunKeyValue` attribute to add the custom attribute to the list of self-writable attributes.

   For example, `<Value>customAttribute</Value>`.

4. In the entry under `sunEntitlementIndexes`, edit the `sunKeyValue` attribute to add the custom attribute to the list of self-writable attributes.

   This example shows a custom attribute as the first element of the list:

   `\"attributes\": [\n \"customAttribute\",\n …​`.

5. Restart AM or the web container where it runs.

### Use the command line to let users update custom attributes

Update the AM configuration store to give users write permission to the custom attribute.

This procedure assumes that you use the command line. Follow [Use an LDAP browser to let users update custom attributes](#allow-users-to-update-attr) if you use an LDAP browser. Adapt the file paths to your configuration store.

1. Search for the value of `sunKeyValue` in `ou=SelfWriteAttributes` by running the following command:

   ```bash
   $ /path/to/opendj/bin/ldapsearch \
    --hostname am.example.com \
    --port 1636 \
    --useSSL \
    --usePkcs12TrustStore /path/to/opendj/config/keystore \
    --truststorepassword:file /path/to/opendj/config/keystore.pin \
    --bindDn uid=admin \
    --bindPassword myPassword \
    --baseDn "dc=am,dc=example,dc=com" "(ou=SelfWriteAttributes)" \
    sunKeyValue
   dn: ou=SelfWriteAttributes,ou=Policies,ou=default,ou=OrganizationConfig,ou=1.0,ou=iPlanetAMPolicyService,ou=services,
       o=sunamhiddenrealmdelegationservicepermissions,ou=services,dc=am,dc=example,dc=com
   sunKeyValue:: eG1scG9saWN5PTw…​…​..

   dn: ou=SelfWriteAttributes,ou=default,ou=default,ou=OrganizationConfig,ou=1.0,ou=sunEntitlementIndexes,ou=services,
       o=sunamhiddenrealmdelegationservicepermissions,ou=services,dc=am,dc=example,dc=com
   sunKeyValue: serializable={"eCondition":{"className":"com.sun…​..
   ```

   Note that the command returns two DNs, and the value of `sunKeyValue` in the first one is base64-encoded.

2. Decode the base64 string of the `iPlanetAMPolicyService` DN.

   For example:

   ```bash
   $ ./base64 decode --encodedData eG1scG9saWN5PTw…​…​..
   xmlpolicy=<?xml version="1.0" encoding="UTF-8"?>
   <Policy name="SelfWriteAttributes" createdby="cn=dsameuser,ou=DSAME Users,ou=am-config"
    lastmodifiedby="cn=dsameuser,ou=DSAME Users,ou=am-config" creationdate="1528296269883"
    lastmodifieddate="1528296269883" referralPolicy="false" active="true" >
    <Rule name="user-read-rule">
     <ServiceName name="sunAMDelegationService" />
     <ResourceName name="sms://dc=am,dc=example,dc=com/sunIdentityRepositoryService/1.0/application/" />
     <AttributeValuePair>
      <Attribute name="MODIFY" />
      <Value>allow</Value>
     </AttributeValuePair>
    </Rule>
    <Subjects name="Subjects" description="">
     <Subject name="delegation-subject" type="AuthenticatedUsers" includeType="inclusive">
     </Subject>
    </Subjects>
    <Conditions name="AttrCondition" description="">
     <Condition name="condition" type="UserSelfCheckCondition">
      <AttributeValuePair>
       <Attribute name="attributes"/>
        <Value>givenname</Value>
        <Value>sn</Value>
        <Value>cn</Value>
        <Value>userpassword</Value>
        <Value>mail</Value>
        <Value>telephonenumber</Value>
        <Value>postaladdress</Value>
        <Value>preferredlocale</Value>
        <Value>iplanet-am-user-password-reset-options</Value>
        <Value>iplanet-am-user-password-reset-question-answer</Value>
        <Value>description</Value>
        <Value>oath2faEnabled</Value>
        <Value>sunIdentityServerDeviceKeyValue</Value>
        <Value>sunIdentityServerDeviceStatus</Value>
      </AttributeValuePair>
     </Condition>
    </Conditions>
   </Policy>
   ```

3. Create a file with the decoded string, then add the custom attribute to the `<AttributeValuePair>` list. For example:

   ```bash
   $ vi to-encode.xml
   …​
      <Attribute name="attributes"/><Value>customAttribute</Value><Value>givenname</Value>…​</AttributeValuePair>
   …​
   ```

4. Base64-encode the content of the file.

   For example:

   ```bash
   $ ./base64 encode -f to-encode.xml
   EG1scG9saWN5PTw22…​..
   ```

5. Create an LDIF file, for example, `change.ldif`.

   The following excerpt is an example of the LDIF file:

   ```ldif
   dn: ou=SelfWriteAttributes,ou=Policies,ou=default,ou=OrganizationConfig,ou=1.0,ou=iPlanetAMPolicyService,
       ou=services,o=sunamhiddenrealmdelegationservicepermissions,ou=services,dc=am,dc=example,dc=com
   changetype: modify
   replace: sunKeyValue
   sunKeyValue: EG1scG9saWN5PTw22.....

   dn: ou=SelfWriteAttributes,ou=default,ou=default,ou=OrganizationConfig,ou=1.0,ou=sunEntitlementIndexes,
       ou=services,o=sunamhiddenrealmdelegationservicepermissions,ou=services,dc=am,dc=example,dc=com
   changetype: modify
   replace: sunKeyValue
   sunKeyValue: serializable={"eCondition":{"className": ...  \"properties\":
       {\"attributes\": [\n    \"customAttribute\",\n    \"givenname\",\n    \"sn\",\n  ... \"values\": []\n}"}
   }
   ```

   The file must contain the following:

   * The LDIF properties and rules required to modify the value of the `sunKeyValue` attribute for both DNs.

   * The base64-encoded string as the value of the `sunKeyValue` attribute of the `iPlanetAMPolicyService` DN. The string already contains the custom attribute.

   * The value of the `sunKeyValue` attribute of the `sunEntitlementIndexes` DN. You must add the custom attribute inside the `attributes` list.

6. Apply the changes in the LDIF file to the LDAP configuration store, as follows:

   ```
   $ /path/to/opendj/bin/ldapmodify \
   --hostname 'ds.example.com' \
   --port 1636 \
   --useSsl \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --bindDn uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --filename change.ldif
   # MODIFY operation successful for DN ou=SelfWriteAttributes,ou=Policies,ou=default,ou=OrganizationConfig,ou=1.0,
     ou=iPlanetAMPolicyService,ou=services,o=sunamhiddenrealmdelegationservicepermissions,ou=services,dc=am,dc=example,dc=com
   # MODIFY operation successful for DN ou=SelfWriteAttributes,ou=default,ou=default,ou=OrganizationConfig,ou=1.0,
     ou=sunEntitlementIndexes,ou=services,o=sunamhiddenrealmdelegationservicepermissions,ou=services,dc=am,dc=example,dc=com
   ```

7. Restart AM or the web container where it runs.

### Add custom attributes to the end-user UI

To ensure the new attribute shows up in the user profile, you must download the UI source code, edit it, then rebuild the UI.

1. [Download the UI source](../ui-customization/downloading-ui.html).

2. Modify the UI as follows:

   * Edit the `openam-ui-user/src/resources/locales/en/translation.json` file and add a new line with the description for the custom attribute. This description will show in the UI user's profile page. For example:

     ```json
     {
         "profile": "Profile",
         "username" : "Username",
         "emailAddress" : "Email address",
         "givenName" : "First Name",
         "customAttribute" : "My Custom Attribute",
         "sn" : "Last Name",
         "changePassword" : "Change password"
     }
     ```

     Note that the example adds the custom attribute under the `common.user` JSON path.

     |   |                                                                                                              |
     | - | ------------------------------------------------------------------------------------------------------------ |
     |   | If you have translated the UI pages, remember to edit all the `translation.json` files in your installation. |

   * Edit the `openam-ui-user/src/resources/themes/default/templates/user/UserProfileTemplate.html` file and add a new line for the custom attribute. Consider the following points:

     * `property` must contain the name of the custom attribute created in the LDAP. For example, `customAttribute`.

     * `label` must contain the path to the label created in the `translation.json` file. In this case, `common.user.customAttribute`.

       For example:

       ```none
       {{#user}}
         {{> form/_basicInput property="username" label="common.user.username" readonly=true}}
         {{> form/_basicInput property="givenName" label="common.user.givenName"}}
         {{> form/_basicInput property="sn" label="common.user.sn" required="true"}}
         {{> form/_basicInput type="email" property="mail" label="common.user.emailAddress"
         extraAttributes='data-validator="validEmailAddressFormat" data-validator-event="keyup"' }}
         {{> form/_basicInput type="tel" property="telephoneNumber" label="common.user.phoneNumber"
         extraAttributes='data-validator="validPhoneFormat" data-validator-event="keyup"'}}
         {{> form/_basicInput property="customAttribute" label="common.user.customAttribute"}}
       {{/user}}
       ```

   * Edit the `openam-ui-user/src/js/org/forgerock/openam/ui/user/UserModel.js` file and add the custom attribute on the `ServiceInvoker.restCall` function.

     Consider the following constraints when modifying this file:

     * The file does not support tab indentation. You must use space indentation.

     * The file does not support lines longer than 120 characters. If the line you are modifying exceeds this limit, break it into multiple lines.

       For example:

       ```js
       return ServiceInvoker.restCall(_.extend(
       {
           type: "PUT",
           data: JSON.stringify(
               _.chain(this.toJSON())
               .pick(["givenName", "sn", "mail", "postalAddress", "telephoneNumber", "customAttribute"])
               .mapValues((val) => {
                   ...
       }
       ```

3. Rebuild the UI by running the `yarn build` command.

4. Test the UI pages by following the steps detailed in [Test and deploy the UI](../ui-customization/ui-testing-deploying.html).

   The UI user profile page now shows the custom attribute, and users are able to read and write its values:

   ![Users are able to read and write the custom attribute value.](../_images/user-profile-custom-attribute.png)

5. Once you are satisfied with the changes, deploy the output in the `build` directory to the `/path/to/tomcat/webapps/am/XUI/` directory of your AM instances.

   You don't need to restart the AM instance. Subsequent visits to the UI pages will use the rebuilt files.

## Customize identity data storage with an IdRepo plugin

AM maps user and group identities to realms using datastores. Datastores rely on a Java identity repository (`IdRepo`) plugin to interact with the identity store that stores the users and groups.

This section describes how to create a custom IdRepo plugin. AM includes built-in support for LDAP identity stores. For most deployments, you don't need to create your own IdRepo plugin. Only create custom IdRepo plugins for deployments with particular requirements that aren't met by the built-in AM functionality.

### IdRepo plugin inheritance

Your IdRepo plugin class must extend the `com.sun.identity.idm.IdRepo` abstract class, and must include a constructor method that takes no arguments.

### IdRepo plugin lifecycle

When AM instantiates your IdRepo plugin, it calls the `initialize()` method.

```java
public void initialize(Map configParams)
```

`configParams` are service configuration parameters for the realm where the IdRepo plugin is configured. They set up communication with the underlying identity store. AM calls the `initialize()` method once, and considers the identity store ready for use.

If you encounter errors or exceptions during initialization, catch and store them in your plugin for use later when AM calls other plugin methods.

After initialization, AM calls the `addListener()` and `removeListener()` methods to register listeners that inform AM client code of changes to identities managed by your IdRepo.

```none
public int addListener(SSOToken token, IdRepoListener listener)
public void removeListener()
```

Your IdRepo plugin must handle listener registration, and return events to AM through the `IdRepoListener`.

When stopping, AM calls your IdRepo plugin `shutdown()` method.

```none
public void shutdown()
```

You don't need to implement the `shutdown()` method, unless your IdRepo plugin has shutdown work of its own to do, such as closing connections to the underlying identity store.

### IdRepo plugin capabilities

Your IdRepo plugin provides AM with a generic means to manage identities, and to create, read, update, delete, and search identities. *Identities* include users and groups, and special identity types such as roles, realms, and agents. In order for AM to determine your plugin's capabilities, it calls the methods described in this section.

#### getSupportedTypes()

```none
public Set getSupportedTypes()
```

The `getSupportedTypes()` method returns a set of `IdType` objects, such as `IdType.USER` and `IdType.GROUP`. You can either hard-code the supported types in your plugin, or make them configurable through the IdRepo service.

#### getSupportedOperations()

```none
public Set getSupportedOperations(IdType type)
```

The `getSupportedOperations()` method returns a set of `IdOperation` objects, such as `IdOperation.CREATE` and `IdOperation.EDIT`. You can either hard-code these operations, or make them configurable.

#### supportsAuthentication()

```none
public boolean supportsAuthentication()
```

The `supportsAuthentication()` method returns `true` if your plugin supports the `authenticate()` method.

### IdRepo plugin implementation

Your IdRepo plugin implements operational methods, depending on what you support. These methods perform the operations in your datastore.

* Create

  AM calls `create()` to provision a new identity in the repository, where `name` is the new identity's name, and `attrMap` holds the attributes names and values.

  ```none
  public String create(SSOToken token, IdType type, String name, Map attrMap)
    throws IdRepoException, SSOException
  ```

* Read

  AM calls the following methods to retrieve identities in the identity store, and to check account activity. If your datastore doesn't support binary attributes, return an empty `Map` for `getBinaryAttributes()`.

  ```none
  public boolean isExists(
    SSOToken token,
    IdType type,
    String name
  ) throws IdRepoException, SSOException

  public boolean isActive(
    SSOToken token,
    IdType type,
    String name
  ) throws IdRepoException, SSOException

  public Map getAttributes(
    SSOToken token,
    IdType type,
    String name
  ) throws IdRepoException, SSOException

  public Map getAttributes(
    SSOToken token,
    IdType type,
    String name,
    Set attrNames
  ) throws IdRepoException, SSOException

  public Map getBinaryAttributes(
    SSOToken token,
    IdType type,
    String name,
    Set attrNames
  ) throws IdRepoException, SSOException

  public RepoSearchResults search(
    SSOToken token,
    IdType type,
    String pattern,
    Map avPairs,
    boolean recursive,
    int maxResults,
    int maxTime,
    Set returnAttrs
  ) throws IdRepoException, SSOException

  public RepoSearchResults search(
    SSOToken token,
    IdType type,
    String pattern,
    int maxTime,
    int maxResults,
    Set returnAttrs,
    boolean returnAllAttrs,
    int filterOp,
    Map avPairs,
    boolean recursive
  ) throws IdRepoException, SSOException
  ```

* Edit

  AM calls the following methods to update a subject in the identity store.

  ```none
  public void setAttributes(
    SSOToken token,
    IdType type,
    String name,
    Map attributes,
    boolean isAdd
  ) throws IdRepoException, SSOException

  public void setBinaryAttributes(
    SSOToken token,
    IdType type,
    String name,
    Map attributes,
    boolean isAdd
  ) throws IdRepoException, SSOException

  public void removeAttributes(
    SSOToken token,
    IdType type,
    String name,
    Set attrNames
  ) throws IdRepoException, SSOException

  public void modifyMemberShip(
    SSOToken token,
    IdType type,
    String name,
    Set members,
    IdType membersType,
    int operation
  ) throws IdRepoException, SSOException

  public void setActiveStatus(
    SSOToken token,
    IdType type,
    String name,
    boolean active
  )
  ```

* Authenticate

  AM calls the `authenticate()` method with the credentials provided.

  ```none
  public boolean authenticate(Callback[] credentials)
    throws IdRepoException, AuthLoginException
  ```

* Delete

  The `delete()` method removes the subject from the identity store. The `name` specifies the subject.

  ```none
  public void delete(SSOToken token, IdType type, String name)
    throws IdRepoException, SSOException
  ```

* Service

  The `IdOperation.SERVICE` operation is rarely used in recent AM deployments.

### IdRepo plugin deployment

When you build your IdRepo plugin, include `openam-core-8.1.1.jar` in the classpath. This file is found under `WEB-INF/lib/` where AM is deployed.

You can either package your plugin as a `.jar` file, and add it to `WEB-INF/lib/`, or add the classes under `WEB-INF/classes/`.

#### Register your plugin with AM

The steps in this procedure use a number of AM API interfaces and annotations. Click the following links to view the *AM Public API JavaDoc*:

* [PluginTools](../_attachments/apidocs/org/forgerock/openam/plugins/PluginTools.html)

* [AmPlugin](../_attachments/apidocs/org/forgerock/openam/plugins/AmPlugin.html)

* [IdRepoConfig](../_attachments/apidocs/org/forgerock/openam/annotations/sm/IdRepoConfig.html)

Register your custom IdRepo plugin with the `PluginTools` interface as follows:

1. Use the `@IdRepoConfig` annotation on your configuration interface, as shown below:

   ```java
   package com.example.custom;

   import java.util.Optional;

   import org.forgerock.openam.annotations.sm.Attribute;
   import org.forgerock.openam.annotations.sm.IdRepoConfig;

   /**
    * Custom IdRepo config.
    */
   @IdRepoConfig(name = "MyIdRepo")
   public interface CustomIdRepoConfig {

       /**
        * The IdRepo implementation fully qualified class name.
        *
        * @return The implementation class name.
        */
       @Attribute(order = 10, requiredValue = true)
       default String sunIdRepoClass() {
           return CustomIdRepo.class.getCanonicalName();
       }

       /**
        * Sets the connection pool minimum size.
        *
        * @return The connection pool minimum size.
        */
       @Attribute(order = 20)
       default Optional<Integer> connectionPoolMinSize() {
           return Optional.of(1);
       }

       /**
        * Sets the connection pool max size.
        *
        * @return The connection pool max size.
        */
       @Attribute(order = 30)
       default Optional<Integer> connectionPoolMaxSize() {
           return Optional.of(10);
       }
   }
   ```

2. Create a `.properties` file based on the name you provided in the configuration interface; for example, `MyIdRepo.properties`.

   The contents of the file might resemble the following:

   ```properties
   CustomIdRepoConfig=Custom IdRepo
   sunIdRepoClass=LDAPv3 Repository Plug-in Class Name
   connectionPoolMinSize=LDAP Connection Pool Minimum Size
   connectionPoolMaxSize=LDAP Connection Pool Maximum Size
   ```

3. Create a class that implements `AmPlugin`, and uses the `PluginTools` interface to handle the following events:

   * `onInstall()`

     Call the `pluginTools.installIdRepo` function with your configuration class as the parameter.

   * `onStartup()`

     Call the `pluginTools.startService` function with your configuration class as the parameter.

   * `upgrade()`

     Call the `pluginTools.upgradeIdRepo` function with your configuration class as the parameter.

     A sample custom plugin class follows:

     ```java
     package com.example.custom;

     import javax.inject.Inject;

     import org.forgerock.openam.plugins.AmPlugin;
     import org.forgerock.openam.plugins.PluginException;
     import org.forgerock.openam.plugins.PluginTools;
     import org.forgerock.openam.plugins.StartupType;

     /**
      * A custom IdRepo plugin. This uses the plugin framework to install the custom identity store.
      */
     public class CustomIdRepoPlugin implements AmPlugin {

         private static final String CURRENT_VERSION = "1.0.0";
         private PluginTools pluginTools;

         /**
          * The constructor.
          *
          * @param pluginTools The PluginTools instance.
          */
         @Inject
         public CustomIdRepoPlugin(PluginTools pluginTools) {
             this.pluginTools = pluginTools;
         }

         @Override
         public String getPluginVersion() {
             return CustomIdRepoPlugin.CURRENT_VERSION;
         }

         @Override
         public void onInstall() throws PluginException {
             pluginTools.installIdRepo(CustomIdRepoConfig.class);
         }

         @Override
         public void onStartup(StartupType startupType) throws PluginException {
             pluginTools.startService(CustomIdRepoConfig.class);
         }

         @Override
         public void upgrade(String fromVersion) throws PluginException {
             pluginTools.upgradeIdRepo(CustomIdRepoConfig.class);
         }
     }
     ```

4. Create a file at the path `META-INF/services/org.forgerock.openam.plugins.AmPlugin` with the following contents:

   `com.example.custom.CustomIdRepoPlugin`

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | If you don't create this file, AM won't pick up the custom repository. |

#### Use your new IdRepo plugin

1. Restart AM or the container in which it runs.

2. Configure a new ID repo in AM using your plugin:

   * In the AM admin UI, go to Realms > *realm name* > Identity Stores.

   * Select Add Identity Store, enter an ID, and select the type of identity store corresponding to your custom IdRepo plugin.

   * You can now add values to any custom properties you configured to be visible in the UI.

3. Go to Realms > *realm name* > Identities, and create a new identity.

   If your plugin supports authentication, users can authenticate using a URL similar to the following:

   ```none
   https://am.example.com:8443/am/XUI/?realm=/myRealm&service=myTree#login
   ```

---

---
title: Dashboards
description: Set up a dashboard service to provide users with single sign-on access to their assigned cloud and internal applications
component: pingam
version: 8.1
page_id: pingam:setup:dashboard-service
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/dashboard-service.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Dashboard"]
page_aliases: ["setup-guide:dashboard-service.adoc"]
section_ids:
  dashboard-setup: Implement the Dashboard service
  dashboard-add: Set up the dashboard service and add applications
  dashboard-single-realm: Configure the Dashboard service for a realm
  assign-app-to-user: Enable an application for a user
  dashboard-remove-user-access: Remove user access to an application
  sec-maint-rest-dashboard: Displaying Dashboard Applications
---

# Dashboards

The Dashboard service gives the end user an interface to access applications secured by AM; both cloud-based applications like SalesForce, and internal applications protected by web or Java agents. The Dashboard service uses SSO to log in to the applications when the user clicks on the application icon. For some apps, like SalesForce, you should limit access to only a few users. Other apps, like Google Mail or Drive, will likely be available to all users.

![The user dashboard lets users quickly access their applications.](_images/user-dashboard.png)Figure 1. User dashboard

The Dashboard service gives users a single place to access their applications. Keep in mind that this does not limit user access, only what appears on the user dashboard.

There are three stages to setting up the Dashboard service:

* Set up the Dashboard service and add applications.

* Configure the service for the realms.

* Assign users applications so that they appear on the users' dashboards. This can be done manually or through a provisioning solution.

Once the Dashboard service is configured for a user, the user can access their dashboard after logging in through the XUI under `/XUI/?realm=/alpha#dashboard/`.

When making a request to the UI, specify the realm or realm alias as the value of a `realm` parameter in the query string, or the DNS alias in the domain component of the URL. If you don't use a realm alias, you must specify the entire hierarchy of the realm. For example: `https://am.example.com:8443/am/XUI/?realm=/customers/europe#login/`.

For example, the full URL depending on the deployment might be at `https://am.example.com:8443/am/XUI/?realm=/alpha#dashboard/`.

## Implement the Dashboard service

Making some applications universally available ensures that all users have the same basic applications. However, some of your applications should be protected from the majority of your users. You will need to single out which users will include the application on their dashboard.

There are three default applications in the Dashboard service: Google, SalesForce, and ZenDesk.

### Set up the dashboard service and add applications

You can add applications to the dashboard service with the following steps. All fields except the dashboard class name and ICF Identifier are required for the application to work properly from the dashboard:

1. In the AM admin UI, go to Configure > Global Services > Dashboard > Secondary Configurations, and click Add a Secondary Configuration to add an application to the dashboard service.

2. Provide a unique name for the application.

3. Add a Dashboard Class Name that identifies how the end user will access the app, such as `SAML2ApplicationClass` for a SAML 2.0 application.

4. Add a Dashboard Name for the application.

5. Add a Dashboard Display Name. This name is what the end user will see, such as Google.

6. Add the Dashboard Icon you would like the end user to see for the application. Either use a fully qualified URL or an appropriate relative URL so that the icon is rendered properly on the user dashboard.

7. Add the Dashboard Login URL to point to the location the end user will go to once they click on the icon.

8. Leave the ICF Identifier blank.

9. Click Add.

### Configure the Dashboard service for a realm

You must configure the Dashboard service and add applications to a realm before you can access them. The following instructions show you how to add an application to a single realm. Before you begin, make sure you have the name of the application (displayed in the Secondary Configuration Instance table under Configure > Global Services > Dashboard):

1. Select Realms > *realm name* > Services, and click Add a Service.

2. Select the Dashboard service, and click Create.

3. Add or remove the applications you would like to appear on the Dashboard service for the realm.

4. Save your changes.

### Enable an application for a user

Use the following steps to enable access to an application from the user's dashboard:

1. Select Realms > *realm name* > Identities and click the user identifier to edit the user's profile.

2. Under Services, click Dashboard.

3. Add the application to the user's Assigned Dashboard list.

4. Save your changes.

### Remove user access to an application

Removing user access to an application does not delete the user's identity profile. The following steps walk you through removing an application from a user's dashboard:

1. Select Realms > *realm name* > Identities and click the user identifier to edit the user's profile.

2. Under Services, click Dashboard.

3. Delete the application from the user's Assigned Dashboard list.

4. Save your changes.

### Displaying Dashboard Applications

AM lets administrators configure online applications to display applications on user Dashboards. You can used exposed REST API to display information about the online applications.

* `/dashboard/assigned`

  This endpoint retrieves the list of applications assigned to the authenticated user.

  ```
  $ curl \
  --header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
  --header "Accept-API-Version: resource=1.0" \
  https://am.example.com:8443/am/json/realms/root/realms/alpha/dashboard/assigned
  {
      "google":{
          "dashboardIcon":[
              "Google.gif"
          ],
          "dashboardName":[
              "Google"
          ],
          "dashboardLogin":[
              "http://www.google.com"
          ],
          "ICFIdentifier":[
              ""
          ],
          "dashboardDisplayName":[
              "Google"
          ],
          "dashboardClassName":[
              "SAML2ApplicationClass"
          ]
      }
  }
  ```

* `/dashboard/available`

  This endpoint retrieves the list of applications available in the authenticated user's realm. The example is based on two of the default Dashboard applications: Google and Salesforce.

  ```
  $ curl \
  --header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
  --header "Accept-API-Version: resource=1.0" \
  https://am.example.com:8443/am/json/realms/root/realms/alpha/dashboard/available
  {
      "google":{
          "dashboardIcon":[
              "Google.gif"
          ],
          "dashboardName":[
              "Google"
          ],
          "dashboardLogin":[
              "http://www.google.com"
          ],
          "ICFIdentifier":[
              ""
          ],
          "dashboardDisplayName":[
              "Google"
          ],
          "dashboardClassName":[
              "SAML2ApplicationClass"
          ]
      },
      "salesforce":{
          "dashboardIcon":[
              "salesforce.gif"
          ],
          "dashboardName":[
              "Salesforce"
          ],
          "dashboardLogin":[
              "http://salesforce.com"
          ],
          "ICFIdentifier":[
              ""
          ],
          "dashboardDisplayName":[
              "Salesforce"
          ],
          "dashboardClassName":[
              "SAML2ApplicationClass"
      }
  }
  ```

* `/dashboard/defined`

  This endpoint retrieves the list of all applications available defined for the AM Dashboard service. The example is based on the three default Dashboard applications: Google, Salesforce, and Zendesk.

  ```
  $ curl \
  --header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
  --header "Accept-API-Version: resource=1.0" \
  https://am.example.com:8443/am/json/realms/root/realms/alpha/dashboard/defined
  {
      "google":{
          "dashboardIcon":[
              "Google.gif"
          ],
          "dashboardName":[
              "Google"
          ],
          "dashboardLogin":[
              "http://www.google.com"
          ],
          "ICFIdentifier":[
              "idm magic 34"
          ],
          "dashboardDisplayName":[
              "Google"
          ],
          "dashboardClassName":[
              "SAML2ApplicationClass"
          ]
      },
      "salesforce":{
          "dashboardIcon":[
              "salesforce.gif"
          ],
          "dashboardName":[
              "SalesForce"
          ],
          "dashboardLogin":[
              "http://www.salesforce.com"
          ],
          "ICFIdentifier":[
              "idm magic 12"
          ],
          "dashboardDisplayName":[
              "Salesforce"
          ],
          "dashboardClassName":[
              "SAML2ApplicationClass"
          ]
      },
      "zendesk":{
          "dashboardIcon":[
              "ZenDesk.gif"
          ],
          "dashboardName":[
              "ZenDesk"
          ],
          "dashboardLogin":[
              "http://www.ZenDesk.com"
          ],
          "ICFIdentifier":[
              "idm magic 56"
          ],
          "dashboardDisplayName":[
              "ZenDesk"
          ],
          "dashboardClassName":[
              "SAML2ApplicationClass"
          ]
      }
  }
  ```

If your application runs in a user-agent such as a browser, you can rely on AM to handle authentication.

---

---
title: Directory configuration properties
description: Configure LDAP directory server connection settings and connection pool parameters for PingAM
component: pingam
version: 8.1
page_id: pingam:setup:server-directory-configuration
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/server-directory-configuration.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["setup-guide:server-directory-configuration.adoc"]
section_ids:
  directory-directory: Directory configuration
  sec-directory-config-server: Server
---

# Directory configuration properties

Configure connection settings and additional LDAP directory server instances by navigating to Deployment > Servers > *server name* > Directory Configuration.

## Directory configuration

The following properties are available under the Directory Configuration tab:

* Minimum Connection Pool

  Sets the minimum number of connections in the pool.

  Changes to this property take effect immediately. No server restart is necessary.

* Maximum Connection Pool

  Sets the maximum number of connections in the pool.

  Changes to this property take effect immediately. No server restart is necessary.

* Bind DN

  Sets the bind DN of the service account AM uses to connect to the configuration directory servers.

  Changes to this property take effect immediately. No server restart is necessary.

* Bind Password

  Set the bind password to connect to the configuration directory servers.

  Changes to this property take effect immediately. No server restart is necessary.

## Server

In the LDAP connection table, edit existing LDAP connections by selecting the pen icon to the right of the row you want to modify. To add a new entry, fill the NAME, HOST NAME, PORT NUMBER and CONNECTION TYPE columns using the following hints:

* **NAME**. The name of the LDAP connection.

* **HOST NAME**. The FQDN of the LDAP server.

* **PORT NUMBER**. The port number to connect to the LDAP server.

* **CONNECTION TYPE**. Whether the connection between the LDAP server and AM is `SIMPLE` (unsecured) or `SSL` (secured).

---

---
title: General properties
description: Configure general server properties including site assignment, installation directory, locale settings, debugging levels, and mail server details
component: pingam
version: 8.1
page_id: pingam:setup:server-general
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/server-general.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["setup-guide:server-general.adoc"]
section_ids:
  general-site: Site
  general-system: System
  general-debugging: Debugging
  general-mailserver: Mail server
---

# General properties

The General page provides access to properties, such as site configuration, server base installation directory, default locale, debug levels, and other properties.

## Site

The following properties are available under the Site tab:

* Parent Site

  The site the server belongs to. The drop-down list defaults to `[empty}` until there is at least one site created in the deployment.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | The Site tab is only available by navigating to Deployment > Servers > *server name* > General. |

## System

The following properties are available under the System tab:

* Base installation directory

  The directory where AM's configuration data and logs reside. For example, `/path/to/am/`.

  Property: `com.iplanet.services.configpath`

- Default Locale

  The default locale of the UI pages when the client doesn't request a locale by using the `locale` query string parameter or by setting the `Accept-Language` HTTP header.

  To set the locale when AM can't find UI files for the requested locale, set the JVM platform locale instead.

  Default: `en_GB`

  Property: `com.iplanet.am.locale`

- Notification URL

  The URL of the notification service endpoint. For example, `https://am.example.com:8443/am/notificationservice`.

  Default: `%SERVER_PROTO%://%SERVER_HOST%:%SERVER_PORT%/%SERVER_URI%/notificationservice`

  Property: `com.sun.identity.client.notification.url`

- XML Validation

  When enabled, AM validates any XML document it parses.

  Default: `Off`

  Property: `com.iplanet.am.util.xml.validating`

## Debugging

The following properties are available under the Debugging tab:

* Debug Level

  The log level shared across components for debug logging.

  Changes to this property take effect immediately. No server restart is necessary.

  Default: `Error`

  Property: `com.iplanet.services.debug.level`

* Merge Debug Files

  When enabled, AM writes debug log messages to a single file, `debug.out`. By default, AM writes a debug log per component.

  Changes to this property take effect immediately. No server restart is necessary.

  Default:`Off`

  Property: `com.iplanet.services.debug.mergeall`

* Debug Directory

  The path where AM writes debug logs. For example, `/path/to/am/var/debug`.

  Changes to this property do not take effect until you restart the AM server.

  Default: `%BASE_DIR%/%SERVER_URI%/var/debug`

  Property: `com.iplanet.services.debug.directory`

## Mail server

The properties under the Mail Server tab configure the email server AM uses to send notification emails, for example, on account lockout.

* Mail Server Host Name

  The hostname of the SMTP server.

  Default: `localhost`

  Property: `com.iplanet.am.smtphost`

* Mail Server Port Number

  The port of the SMTP server.

  Default: `25`

  Property: `com.iplanet.am.smtpport`

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a *different* email server to the [Email service](../user-self-service/configuring-email-service.html) you configure for user self-service. |

---

---
title: Generic LDAPv3
description: Configure Generic LDAPv3 compliant identity stores, including Oracle Unified Directory, by specifying LDAP server connection details, search parameters, and attribute mappings
component: pingam
version: 8.1
page_id: pingam:setup:data-stores-generic-ldapv3
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/data-stores-generic-ldapv3.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Directory Server", "Identity Store", "LDAP"]
page_aliases: ["setup-guide:data-stores-generic-ldapv3.adoc"]
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
  behera_support_enabled: Behera Support Enabled
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
  attribute_name_of_group_member_url: Attribute Name of Group Member URL
  default_group_members_user_dn: Default Group Member's User DN
  persistent_search_controls_tab: Persistent Search Controls tab
  persistent_search_base_dn: Persistent Search Base DN
  persistent_search_filter: Persistent Search Filter
  persistent_search_scope: Persistent Search Scope
  error_handling_configuration_tab: Error Handling Configuration tab
  the_delay_time_between_retries: The Delay Time Between Retries
  cache_control_tab: Cache Control tab
  dn_cache: DN Cache
  dn_cache_size: DN Cache Size
---

# Generic LDAPv3

Use these attributes when configuring Generic LDAPv3 compliant identity stores, including Oracle Unified Directory:

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

### LDAP Bind Password

Bind password for connecting to the directory server.

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

How often to send a heartbeat request to the directory server to ensure that the connection doesn't remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0. To set the units for the interval, use LDAP Connection Heartbeat Time Unit.

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

Default: `second`

### Maximum Results Returned from Search

A cap for the number of search results to return, for example, when viewing profiles under Identities. Rather than raise this number, consider narrowing your search to match fewer directory entries.

Default: `1000`

### Search Timeout

Maximum time to wait for search results in seconds. Doesn't apply to persistent searches.

Default: `10`

### LDAPv3 Plugin Search Scope

LDAP searches can apply to a single entry (`SCOPE_BASE`), entries directly below the search DN (`SCOPE_ONE`), or all entries below the search DN (`SEARCH_SUB`).

Default: `SCOPE_SUB`

### Behera Support Enabled

Enable this property to use Behera draft control in outgoing requests for operations that might modify password values.

Behera draft control allows AM to display password policy related error messages when password policies aren't met.

Default: `Enabled`

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

Default: `uid`

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Don't modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. |

### LDAP Users Search Filter

When searching for users, apply this LDAP search filter as well.

Default: `(objectclass=inetorgperson)`

### LDAP User Object Class

User profiles have these LDAP object classes.

AM handles only those attributes listed in this setting. AM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that AM execute a search that asks for the `mailAlternateAddress` attribute, AM does the search, but doesn't request `mailAlternateAddress`. In the same way, AM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

Default: `inetorgperson`, `inetUser`, `organizationalPerson`, `person`, `top`

### LDAP User Attributes

User profiles have these LDAP attributes.

AM handles only those attributes listed in this setting. AM discards any unlisted attributes from requests and the request proceeds without the attribute.

Default:\
`uid`\
`caCertificate`\
`authorityRevocationList`\
`inetUserStatus`\
`mail`\
`sn`\
`manager`\
`userPassword`\
`adminRole`\
`objectClass`\
`givenName`\
`memberOf`\
`cn`\
`telephoneNumber`\
`preferredlanguage`\
`userCertificate`\
`postalAddress`\
`dn`\
`employeeNumber`\
`distinguishedName`

### Create User Attribute Mapping

When creating a user profile, apply this map of AM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

Default: `cn`, `sn`

### Attribute Name of User Status

Attribute to check/set user status.

Default: `inetuserstatus`

### User Status Active Value

Active users have the user status attribute set to this value.

Default: `Active`

### User Status Inactive Value

Inactive users have the user status attribute set to this value.

Default: `Inactive`

### LDAP People Container Naming Attribute

RDN attribute of the LDAP base DN which contains user profiles.

### LDAP People Container Value

RDN attribute value of the LDAP base DN which contains user profiles.

If specified, AM will limit searches for user profiles to the provided base DN. Otherwise, AM searches the entire directory.

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

Default: `uid`

## Group Configuration tab

### LDAP Groups Search Attribute

When searching for a group by name, match values against this attribute.

Default: `cn`

### LDAP Groups Search Filter

When searching for groups, apply this LDAP search filter as well.

Default: `(objectclass=groupOfUniqueNames)`

### LDAP Groups Container Naming Attribute

RDN attribute of the LDAP base DN which contains group profiles.

Default: `ou`

### LDAP Groups Container Value

RDN attribute value of the LDAP base DN which contains group profiles.

If specified, AM will limit searches for group profiles to the provided base DN. Otherwise, AM searches the entire directory.

Default: `groups`

### LDAP Groups Object Class

Group profiles have these LDAP object classes.

Default: `groupofuniquenames`, `top`

### LDAP Groups Attributes

Group profiles have these LDAP attributes.

Default: `ou`, `cn`, `description`, `dn`, `objectclass`, `uniqueMember`

### Attribute Name for Group Membership

LDAP attribute in the member's LDAP entry whose values are the groups to which a member belongs.

### Attribute Name of Unique Member

Attribute in the group's LDAP entry whose values are the members of the group.

Default: `uniqueMember`

### Attribute Name of Group Member URL

Attribute in the dynamic group's LDAP entry whose value is a URL specifying the members of the group.

Default: `memberUrl`

### Default Group Member's User DN

DN of member added to all newly created groups.

## Persistent Search Controls tab

### Persistent Search Base DN

Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

Default: `base-dn`

### Persistent Search Filter

LDAP filter to apply when performing persistent searches.

Default: `(objectclass=*)`

### Persistent Search Scope

LDAP searches can apply to a single entry (`SCOPE_BASE`), entries directly below the search DN (`SCOPE_ONE`), or all entries below the search DN (`SEARCH_SUB`).

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

---

---
title: Identity stores
description: Configure identity stores in PingAM realms to authenticate users against persistent data repositories like PingDS, PingDirectory, or Active Directory
component: pingam
version: 8.1
page_id: pingam:setup:setting-up-identity-stores
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/setting-up-identity-stores.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Identity Store", "Repository"]
page_aliases: ["setup-guide:setting-up-identity-stores.adoc"]
section_ids:
  realm-data-store: Configure an identity store
---

# Identity stores

An identity store, also called an identity repository, is a persistent store of user data. For example, PingDS, PingDirectory, or Microsoft Active Directory. You can configure identity stores either when installing AM, or by adding them to an existing AM instance.

AM also uses other types of datastores, such as the configuration datastore, the UMA datastore, and the Core Token Service (CTS) datastore.

When you first set up a realm, the new realm inherits the identity store from the parent realm. For example, in an installation where the Top Level Realm has a DS server as the identity store, any new realm created would have the same DS instance as the identity store, by default.

If your administrators are in one realm and your users in another, your new child realm might retrieve users from a different identity store.

|   |                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You shouldn't configure more than one writable identity store in a single realm. AM will try to perform write operations on each identity store configured in a realm, and there is no way to configure which repository is written to.To manage identities and reconcile differences between multiple identity stores, use [PingIDM](https://docs.pingidentity.com/pingidm/8.1). |

**Tasks to connect identity stores**

| Task                                                                                                                                                                                           | Resources                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Prepare an identity store**You must prepare the identity store before AM can use it.                                                                                                         | [Prepare identity stores](../installation/prepare-identity-repository.html) |
| **Configure an identity store**Configure the store in a realm so that users can be authenticated.By default, AM re-uses your configuration store as the identity store of the Top Level realm. | [Configure an identity store](#realm-data-store)                            |
| **Customize an identity store**Create custom attributes for your users or custom identity plugins to change how AM maps users and groups to a realm.                                           | [Customize identity stores](customizing-data-stores.html)                   |

## Configure an identity store

1. Share the identity store certificate with the AM container to prepare for TLS/LDAPS. AM should communicate with identity stores over secure connections.

   DS is configured to require secure connections by default. Share the DS certificate with the AM container before continuing.

   > **Collapse: Share the DS certificate with AM**
   >
   > * On the DS host, export the DS CA certificate.
   >
   >   DS uses a deployment ID and password to generate a CA key pair. Learn more in [Deployment IDs](https://docs.pingidentity.com/pingds/8.1/security-guide/pki.html#about-deployment-ids).
   >
   >   Use the `dskeymgr` command to export the CA certificate:
   >
   >   ```bash
   >   $ /path/to/opendj/bin/dskeymgr \
   >   export-ca-cert \
   >   --deploymentId $DEPLOYMENT_ID \
   >   --deploymentIdPassword password \
   >   --outputFile /path/to/ca-cert.pem
   >   ```
   >
   > * Copy the `ca-cert.pem` file to an accessible location on the AM host.
   >
   > - Import the DS CA certificate into the AM truststore:
   >
   >   ```bash
   >   $ keytool \
   >   -importcert \
   >   -file /path/to/ca-cert.pem \
   >   -keystore /path/to/am/security/keystores/truststore
   >   -storepass truststore-password
   >   ```
   >
   > Learn more about configuring AM's truststore in [Prepare the truststore](../installation/prepare-trust-store.html).

2. In the AM admin UI, go to Realms > *realm name* > Identity Stores.

3. Click Add Identity Store, enter an ID, and select the type of identity store from one of the following:

   | Type                                       | Use for                                                                                                                                                               |
   | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `Active Directory Application Mode (ADAM)` | [Active Directory Lightweight Directory Services (AD LDS)](data-stores-adam.html)                                                                                     |
   | `Active Directory`                         | [Active Directory](data-stores-active-directory.html)                                                                                                                 |
   | `ForgeRock IAM Directory Server`           | [PingDS](data-stores-opendj.html)Only use this type if DS is the shared identity store in a Ping Advanced Identity Software deployment. Otherwise, use type `OpenDJ`. |
   | `OpenDJ`                                   | [PingDS](data-stores-opendj.html)                                                                                                                                     |
   | `Generic LDAPv3`                           | [Generic LDAPv3 compliant](data-stores-generic-ldapv3.html) identity stores, including Oracle Unified Directory                                                       |
   | `Ping Directory Server`                    | [PingDirectory](data-stores-ping-directory.html)                                                                                                                      |

   Don't select the following unsupported types: `Sun DS with OpenAM schema` or `Tivoli Directory Server`.

4. Click Create.

5. In the tabbed view, provide information on how to connect to your identity store.

   Read the configuration hints for your identity store:

   * [Active Directory](data-stores-active-directory.html)

   * [Active Directory Lightweight Directory Services (AD LDS)](data-stores-adam.html)

   * [Generic LDAPv3](data-stores-generic-ldapv3.html)

   * [PingDS](data-stores-opendj.html)

   * [PingDirectory](data-stores-ping-directory.html)

6. If you've not applied the schema configuration to your identity data, but the AM service account used to bind to the directory service has permission to alter schema, enable the Load Schema option.

7. Save your changes.

8. Test the connection as described in [Test identity store access](prepare-idrepo-testing.html).

---

---
title: Load balancing
description: Configure load balancing for PingAM by session storage location, enable sticky load balancing, and handle HTTP request headers
component: pingam
version: 8.1
page_id: pingam:setup:configure-lb
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/configure-lb.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Load Balancer", "Setup &amp; Configuration"]
page_aliases: ["setup-guide:configure-lb.adoc"]
section_ids:
  configure-lb-stateful: Configure site sticky load balancing
  lb-termination: Load balancer offloading
  lb-request-forwarding: Request forwarding caveats
  handle-request-headers: Handle HTTP request headers
---

# Load balancing

Load balancing configuration requirements differ depending on where you configure AM to [store journey and authenticated sessions](../am-sessions/preface.html), as shown in the following table:

**Load balancing requirements by session storage location**

| Storage location                       | Load balancing requirement                           | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CTS token store                        | None. Session stickiness recommended for performance | Although the CTS token store is the authoritative source for server-side journey and authenticated sessions, AM servers cache the journey or authenticated session when:- Authenticating a user

- Satisfying a session requestAn AM site configured to use server-side sessions achieves the best performance when the server that originally authenticated a user continually manages that authenticated session, as it doesn't need to retrieve it from the CTS token store.In the same way, an AM realm configured to use server-side journey sessions achieves the best performance when the same server manages every request in the journey. |
| Client                                 | None. Session stickiness recommended for performance | Although the journey or authenticated session resides in a JWT stored on the client which is passed to AM server along with the request, client-side sessions should be signed and/or encrypted for security reasons. Because decrypting and verifying the session on each request may be an expensive operation depending on the algorithms configured, AM caches the decrypt sequence in memory to improve performance.Therefore, an AM site configured to use client-side authenticated sessions achieves the best performance when the same server manages every request for the same journey or authenticated session.                         |
| In AM's memory (journey sessions only) | Session stickiness required                          | Deployments where AM stores journey sessions in memory require sticky load balancing to route all requests pertaining to a particular journey to the same AM server. If a request reaches a different AM server, the journey restarts.                                                                                                                                                                                                                                                                                                                                                                                                              |

Learn more in [Introduction to sessions](../am-sessions/about-sessions.html).

Session storage location can be heterogeneous within the same AM deployment to suit the requirements of each of your realms. If your deployment uses a substantial number of server-side sessions, follow the recommendations for deployments configured for server-side sessions.

## Configure site sticky load balancing

1. In the AM admin UI go to Deployment > Sites.

2. Ensure you have a site created and that your servers are part of it.

   Learn more in [Configure a site with the first server](../installation/configure-sites.html#configure-site-after-installation).

3. Ensure that the `amlbcookie` cookie has a unique value for each AM server:

   * Go to Deployment > Servers > *server name* > Advanced and review the value of the `com.iplanet.am.lbcookie.value` property. By default, the cookie value is set to the AM server ID.

     Keep the value of the `amlbcookie` cookie set to the AM server ID to improve server performance when using web agents.

     If you have changed the value of this property, and you need to match the AM server URLs with their corresponding server IDs, query the `global-config/servers` endpoint. For example:

     ```bash
     $ curl \
     --request GET \
     --header "Accept: application/json" \
     --header "iPlanetDirectoryPro: AQIC5…​NDU1*" \
     'https://am.example.com:8443/am/json/global-config/servers?_queryFilter=true'
     {
       "result": [
         {
           "_id": "01",
           "_rev": "1372703177",
           "url": "https://am.example.com:8443/am",
           "siteName": null
         }
       ],
       "resultCount": 1,
       "pagedResultsCookie": null,
       "totalPagedResultsPolicy": "NONE",
       "totalPagedResults": -1,
       "remainingPagedResults": -1
     }
     ```

     In the example, the server ID for server `https://am.example.com:8443/am` is `01`.

     Changes take effect only after you restart the AM server.

   * Restart the AM server. You can then check the cookie value by logging in to the AM admin UI, and examining the `amlbcookie` cookie in your browser.

     |   |                                                                                                                                                                           |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can find details on changing the name of the sticky load balancing cookie in [Change the sticky load balancing cookie name](../security/change-amlbcookie-name.html). |

4. Repeat the previous steps for each of the AM servers that should be part of the site.

5. Configure your load balancer to perform sticky load balancing based on the `amlbcookie` value.

   In other words, the load balancer layer must keep track of which `amlbcookie` cookie value corresponds to which AM server.

   When the load balancer receives a request, it inspects the value of the `amlbcookie` cookie, and then forwards the request to the corresponding AM server.

### Load balancer offloading

When traffic to and from the load balancer is protected with HTTPS, you must terminate the SSL connection on the load balancer. Decrypting the traffic in the load balancer makes it possible to use cookie-based session stickiness.

You then either re-encrypt the traffic from the load balancer to AM, or make connections from the load balancer to AM over HTTP.

If you configure the load balancer in passthrough mode instead, session stickiness wouldn't be possible.

### Request forwarding caveats

Sticky load balancing based on the value of the `amlbcookie` cookie doesn't guarantee request forwarding to the corresponding AM server in all cases. For example, common REST API calls typically don't use cookies. Therefore, load balancers can't route these calls to the AM server on which the authenticated session is cached.

The AM server that doesn't hold the authenticated session in cache must locate the authenticated session by retrieving it from the CTS token store.

## Handle HTTP request headers

HTTP requests can include information needed for access management, such as the client IP address used for adaptive risk-based authentication.

Configure your load balancer or proxy to pass the information to AM by using request headers. For example, the load balancer or proxy can send the client IP address by using the `X-Forwarded-For` HTTP request header.

Also configure AM to consume and to forward the headers as necessary. For example, to configure AM to look for the client IP address in the `X-Forwarded-For` request header, set the advanced configuration property `com.sun.identity.authentication.client.ipAddressHeader` to `X-Forwarded-For` under Deployment > Servers > *server name* > Advanced.

In a site configuration where one AM server can forward requests to another AM server, you can retain the header by adding it to the advanced configuration property `openam.retained.http.request.headers`. If `X-Forwarded-For` is the only additional header to retain, set `openam.retained.http.request.headers` to `X-DSAMEVersion,X-Forwarded-For`, for example.

Configure these properties under Deployment > Servers > *server name* > Advanced.

---

---
title: Manage deployment configuration
description: Manage PingAM server and site configurations for single or multiple server instances, including default properties, per-server overrides, and multi-server site setup
component: pingam
version: 8.1
page_id: pingam:setup:deployment-configuration-reference
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/deployment-configuration-reference.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Install", "Configuration"]
page_aliases: ["reference:deployment-configuration-reference.adoc", "setup-guide:deployment-configuration-reference.adoc"]
section_ids:
  servers-configuration: Configure servers
  sites-configuration: Configure sites
---

# Manage deployment configuration

Under Deployment, you can manage different configurations for AM server instances, and site configurations when using multiple AM server instances.

## Configure servers

AM server properties reside in two places:

* The default configuration, under Configure > Server Defaults.

* Per-server basis configuration, under Deployment > Servers > *server name*.

Default server properties are applied to all server instances, and can be overridden on a per-server basis. Changes to the value of a default server property are applied to all servers that are not overriding that property. The ability to set default properties and override them for an individual server lets you keep a set of properties with identical configuration across the environment, while providing the flexibility to change properties on specific servers when required.

![A closed lock means inherited, an open lock means localized.](_images/inherited-properties.png)Figure 1. Inherited properties

* A closed lock means the property is inherited from the defaults. To change an inherited value click on the lock, and the property will become localized for that server.

* An open lock means the property is localized for this server. To return to the inherited values, click on the lock.

The Advanced section also takes values from the defaults, but the properties do not have locks for inheritance. Instead, if you want to override a particular advanced property value on a per-server basis, you need to add that property with its new value under Deployment > Servers > *server name* > Advanced.

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | After changing server configurations, restart AM or the web application container where AM runs for the changes to take effect unless otherwise noted. |

## Configure sites

Sites involve multiple AM servers working together to provide services. You can use sites with load balancers and session high availability to configure pools of servers capable of responding to client requests in highly available fashion.

* Name

  Sets the name of the site.

* Primary URL

  Sets the primary entry point to the site, such as the URL, to the load balancer for the site configuration.

* Secondary URLs

  Sets alternate entry points to the site.

---

---
title: PingDirectory
description: Configure PingAM to connect to PingDirectory as an identity store using LDAP, LDAPS, or StartTLS with options for proxied authorization and connection pooling
component: pingam
version: 8.1
page_id: pingam:setup:data-stores-ping-directory
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/data-stores-ping-directory.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Directory Server", "Identity Store", "LDAP"]
section_ids:
  all_tabs: All tabs
  load_schema: Load Schema
  server_settings_tab: Server Settings tab
  ldap_server: LDAP Server
  ldap_bind_dn: LDAP Bind DN
  ldap_bind_password: LDAP Bind Password
  proxied_authorization_using_bind_dn: Proxied Authorization using Bind DN
  fallback_using_bind_dn_if_proxied_authorization_denied: Fallback using Bind DN if Proxied Authorization denied
  ldap_organization_dn: LDAP Organization DN
  ldap_connection_mode: LDAP Connection Mode
  trust_all_server_certificates: Trust All Server Certificates
  ldap_connection_pool_minimum_size: LDAP Connection Pool Minimum Size
  ldap_connection_pool_maximum_size: LDAP Connection Pool Maximum Size
  ldap_connection_heartbeat_interval: LDAP Connection Heartbeat Interval
  ldap_connection_heartbeat_search_base: LDAP Connection Heartbeat Search Base
  ldap_connection_heartbeat_search_filter: LDAP Connection Heartbeat Search Filter
  ldap_connection_heartbeat_time_unit: LDAP Connection Heartbeat Time Unit
  maximum_results_returned_from_search: Maximum Results Returned from Search
  search_timeout: Search Timeout
  ldapv3_plugin_search_scope: LDAPv3 Plugin Search Scope
  behera_support_enabled: Behera Support Enabled
  affinity-enabled: Affinity Enabled
  affinity_level: Affinity Level
  mtls_enabled: mTLS Enabled
  mtls_secret_label_identifier: mTLS Secret Label Identifier
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
  attribute_name_of_group_member_url: Attribute Name of Group Member URL
  persistent_search_controls_tab: Persistent Search Controls tab
  persistent_search_base_dn: Persistent Search Base DN
  persistent_search_filter: Persistent Search Filter
  persistent_search_scope: Persistent Search Scope
  error_handling_configuration_tab: Error Handling Configuration tab
  the_delay_time_between_retries: The Delay Time Between Retries
  cache_control_tab: Cache Control tab
  dn_cache: DN Cache
  dn_cache_size: DN Cache Size
---

# PingDirectory

Use these attributes when configuring PingDirectory identity stores:

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

### LDAP Bind Password

Bind password for connecting to the directory server.

### Proxied Authorization using Bind DN

When the `force-change-on-reset` password policy is configured on the PingDirectory user datastore, users resetting their passwords using AM's forgotten password feature might be required to reset their passwords twice (prompted by both AM's User Self-Service and PingDirectory's password policy).

If you enable Proxied Authorization using Bind DN, AM uses PingDirectory's [proxied authorization](https://docs.pingidentity.com/pingdirectory/10.3/managing_access_control/pd_ds_work_with_proxied_authn.html) to reset user passwords. This means AM performs the password reset as the user, so users don't have to reset their passwords again.

Before enabling this setting, ensure that the service account configured in the LDAP Bind DN property has the `proxied-auth` privilege granted. If the service account doesn't have the required privilege, users won't be able to reset their passwords and AM and PingDirectory will log an error message.

Enable this property only if:

* The `force-change-on-reset` password policy is configured in the PingDirectory user datastore.

* The forgotten password user self-service feature is configured in AM.

* Users are being forced to reset their passwords twice.

Default: `Disabled`

### Fallback using Bind DN if Proxied Authorization denied

Enable this setting to fallback and retry using non-proxied authorization (without the PingDirectory `proxied-auth` privilege) when proxied authorization is denied.

Enabling this property causes AM to attempt to make LDAP changes as the LDAP Bind DN service account if proxied authorization was unsuccessful. For example, if the user account attempting the changes originally is locked or the password has expired.

This setting is effective only when Proxied Authorization using Bind DN is also enabled.

Default: `Disabled`

### LDAP Organization DN

The base DN under which to find user and group profiles.

Ensure that the identity store is set up with the specified DN before making any changes to this property in AM.

Default: `base-dn`

### LDAP Connection Mode

Whether to use LDAP, LDAPS or StartTLS to connect to the directory server. When LDAPS or StartTLS are enabled, AM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where AM runs, or because you imported the certificates into the trust store.

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

### Trust All Server Certificates

Whether AM trusts all server certificates when LDAPS or StartTLS are used to connect to the directory server.

Only enable this property if you completely trust the directory server.

Default: `Disabled`

### LDAP Connection Pool Minimum Size

Minimum number of connections to the directory server.

Default: `1`

### LDAP Connection Pool Maximum Size

Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

Default: `10`

### LDAP Connection Heartbeat Interval

How often to send a heartbeat request to the directory server to ensure that the connection doesn't remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0. To set the units for the interval, use LDAP Connection Heartbeat Time Unit.

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

Default: `second`

### Maximum Results Returned from Search

A cap for the number of search results to return, for example, when viewing profiles under Identities. Rather than raise this number, consider narrowing your search to match fewer directory entries.

Default: `1000`

### Search Timeout

Maximum time to wait for search results in seconds. Doesn't apply to persistent searches.

Default: `10`

### LDAPv3 Plugin Search Scope

LDAP searches can apply to a single entry (`SCOPE_BASE`), entries directly below the search DN (`SCOPE_ONE`), or all entries below the search DN (`SEARCH_SUB`).

Default: `SCOPE_SUB`

### Behera Support Enabled

Enable this property to use Behera draft control in outgoing requests for operations that might modify password values.

Behera draft control allows AM to display password policy related error messages when password policies aren't met.

Default: `Enabled`

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

### mTLS Enabled

Enables mutual TLS (mTLS) between AM and the directory server.

When mTLS is enabled, AM ignores the values for LDAP Bind DN and LDAP Bind Password.

If you enable this property, you must:

* Set the LDAP Connection Mode to `LDAPS`.

* Provide an mTLS Secret Label Identifier.

Default: `Disabled`

### mTLS Secret Label Identifier

Identifier used to create a secret label for mapping to the mTLS certificate in the secret store. AM uses this identifier to create a specific secret label for this identity store. The secret label takes the form `am.identity.repository.label.cert` , where `label` is the value of mTLS Secret Label Identifier. The identifier can only contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and periods (`.`). It can't start or end with a period.

When you configure mTLS, you must map the secret label based on this identifier to the correct certificate alias. To avoid a temporarily "broken" mTLS connection, add the mTLS Secret Label Identifier first, without enabling mTLS. Then [configure the mapping](../security/secure-data-stores.html#configure-mtls-mappings-id-store) to the certificate alias, then enable mTLS.

For more security, you should rotate certificates periodically. When you rotate a certificate, update the corresponding mapping in the realm secret store configuration to reflect this identifier. When you rotate a certificate, AM closes any existing connections using the old certificate. AM selects a new connection from the connection pool and no server restart is required.

## Plug-in Configuration tab

### LDAPv3 Repository Plugin Class Name

AM identity store implementation.

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

### Attribute Name Mapping

Map of AM profile attribute names to directory server attribute names.

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

Default: `uid`

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Don't modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. |

### LDAP Users Search Filter

When searching for users, apply this LDAP search filter as well.

Default: `(objectclass=inetorgperson)`

### LDAP User Object Class

User profiles have these LDAP object classes.

AM handles only those attributes listed in this setting. AM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that AM execute a search that asks for the `mailAlternateAddress` attribute, AM does the search, but doesn't request `mailAlternateAddress`. In the same way, AM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

Default:\
`iplanet-am-managed-person`\
`inetuser`\
`sunFMSAML2NameIdentifier`\
`inetorgperson`\
`devicePrintProfilesContainer`\
`pushDeviceProfilesContainer`\
`iPlanetPreferences`\
`iplanet-am-user-service`\
`forgerock-am-dashboard-service`\
`organizationalperson`\
`top`\
`kbaInfoContainer`\
`oathDeviceProfilesContainer`\
`person`\
`sunAMAuthAccountLockout`\
`iplanet-am-auth-configuration-service`

### LDAP User Attributes

User profiles have these LDAP attributes.

AM handles only those attributes listed in this setting. AM discards any unlisted attributes from requests and the request proceeds without the attribute.

Default:\
`iplanet-am-user-password-reset-question-answer`\
`mail`\
`iplanet-am-user-alias-list`\
`iplanet-am-auth-configuration`\
`assignedDashboard`\
`authorityRevocationList`\
`dn`\
`iplanet-am-user-password-reset-options`\
`createTimestamp`\
`employeeNumber`\
`kbaActiveIndex`\
`caCertificate`\
`iplanet-am-session-quota-limit`\
`iplanet-am-user-auth-config`\
`sun-fm-saml2-nameid-infokey`\
`sunIdentityMSISDNNumber`\
`devicePrintProfiles`\
`sunAMAuthInvalidAttemptsData`\
`iplanet-am-user-password-reset-force-reset`\
`givenName`\
`iplanet-am-session-get-valid-sessions`\
`objectClass`\
`adminRole`\
`inetUserHttpURL`\
`iplanet-am-user-account-life`\
`userCertificate`\
`postalAddress`\
`preferredtimezone`\
`iplanet-am-user-admin-start-dn`\
`oath2faEnabled`\
`preferredlanguage`\
`sun-fm-saml2-nameid-info`\
`userPassword`\
`iplanet-am-session-service-status`\
`telephoneNumber`\
`iplanet-am-session-max-idle-time`\
`distinguishedName`\
`iplanet-am-session-destroy-sessions`\
`modifyTimestamp`\
`uid`\
`iplanet-am-user-success-url`\
`kbaInfo`\
`iplanet-am-user-auth-modules`\
`sn`\
`memberOf`\
`preferredLocale`\
`manager`\
`iplanet-am-session-max-session-time`\
`cn`\
`oathDeviceProfiles`\
`iplanet-am-user-login-status`\
`pushDeviceProfiles`\
`inetUserStatus`\
`iplanet-am-user-failure-url`\
`iplanet-am-session-max-caching-time`

### Create User Attribute Mapping

When creating a user profile, apply this map of AM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

Default: `cn`, `sn`

### Attribute Name of User Status

Attribute to check/set user status.

Default: `inetuserstatus`

### User Status Active Value

Active users have the user status attribute set to this value.

Default: `Active`

### User Status Inactive Value

Inactive users have the user status attribute set to this value.

Default: `Inactive`

### LDAP People Container Naming Attribute

RDN attribute of the LDAP base DN which contains user profiles.

### LDAP People Container Value

RDN attribute value of the LDAP base DN which contains user profiles.

If specified, AM will limit searches for user profiles to the provided base DN. Otherwise, AM searches the entire directory.

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

Default: `uid`

## Group Configuration tab

### LDAP Groups Search Attribute

When searching for a group by name, match values against this attribute.

Default: `cn`

### LDAP Groups Search Filter

When searching for groups, apply this LDAP search filter as well.

Default: `(objectclass=groupOfUniqueNames)`

### LDAP Groups Container Naming Attribute

RDN attribute of the LDAP base DN which contains group profiles.

Default: `ou`

### LDAP Groups Container Value

RDN attribute value of the LDAP base DN which contains group profiles.

If specified, AM will limit searches for group profiles to the provided base DN. Otherwise, AM searches the entire directory.

Default: `groups`

### LDAP Groups Object Class

Group profiles have these LDAP object classes.

Default: `groupofuniquenames`, `top`

### LDAP Groups Attributes

Group profiles have these LDAP attributes.

Default: `dn`, `cn`, `uniqueMember`, `objectclass`

### Attribute Name for Group Membership

LDAP attribute in the member's LDAP entry whose values are the groups to which a member belongs.

### Attribute Name of Unique Member

Attribute in the group's LDAP entry whose values are the members of the group.

Default: `uniqueMember`

### Attribute Name of Group Member URL

Attribute in the dynamic group's LDAP entry whose value is a URL specifying the members of the group.

Default: `memberUrl`

## Persistent Search Controls tab

### Persistent Search Base DN

Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

Default: `base-dn`

### Persistent Search Filter

LDAP filter to apply when performing persistent searches.

Default: `(!(objectclass=frCoreToken))`

### Persistent Search Scope

LDAP searches can apply to a single entry (`SCOPE_BASE`), entries directly below the search DN (`SCOPE_ONE`), or all entries below the search DN (`SEARCH_SUB`).

Default: `SCOPE_SUB`

## Error Handling Configuration tab

### The Delay Time Between Retries

The number of milliseconds to wait between retry attempts when an LDAP operation fails with a retryable error.

Default: `1000`

## Cache Control tab

### DN Cache

Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when AM uses persistent searches to obtain notification of such updates.

Default: `true`

### DN Cache Size

Maximum number of DNs cached when caching is enabled.

Default: `1500`

---

---
title: PingDS
description: Configure PingDS identity stores in PingAM by specifying LDAP server addresses, bind credentials, connection settings, and schema options
component: pingam
version: 8.1
page_id: pingam:setup:data-stores-opendj
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/data-stores-opendj.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Directory Server", "Identity Store", "LDAP"]
page_aliases: ["setup-guide:data-stores-opendj.adoc"]
section_ids:
  all_tabs: All tabs
  load_schema: Load Schema
  server_settings_tab: Server Settings tab
  ldap_server: LDAP Server
  ldap_bind_dn: LDAP Bind DN
  ldap_bind_password: LDAP Bind Password
  proxied_authorization_using_bind_dn: Proxied Authorization using Bind DN
  fallback_using_bind_dn_if_proxied_authorization_denied: Fallback using Bind DN if Proxied Authorization denied
  ldap_organization_dn: LDAP Organization DN
  ldap_connection_mode: LDAP Connection Mode
  trust_all_server_certificates: Trust All Server Certificates
  ldap_connection_pool_minimum_size: LDAP Connection Pool Minimum Size
  ldap_connection_pool_maximum_size: LDAP Connection Pool Maximum Size
  ldap-conn-heartbeat-interval: LDAP Connection Heartbeat Interval
  ldap_connection_heartbeat_search_base: LDAP Connection Heartbeat Search Base
  ldap_connection_heartbeat_search_filter: LDAP Connection Heartbeat Search Filter
  ldap_connection_heartbeat_time_unit: LDAP Connection Heartbeat Time Unit
  maximum_results_returned_from_search: Maximum Results Returned from Search
  search_timeout: Search Timeout
  ldapv3_plugin_search_scope: LDAPv3 Plugin Search Scope
  behera_support_enabled: Behera Support Enabled
  affinity-enabled: Affinity Enabled
  affinity_level: Affinity Level
  mtls_enabled: mTLS Enabled
  mtls_secret_label_identifier: mTLS Secret Label Identifier
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
  attribute_name_of_group_member_url: Attribute Name of Group Member URL
  persistent_search_controls_tab: Persistent Search Controls tab
  persistent_search_base_dn: Persistent Search Base DN
  persistent_search_filter: Persistent Search Filter
  persistent_search_scope: Persistent Search Scope
  error_handling_configuration_tab: Error Handling Configuration tab
  the_delay_time_between_retries: The Delay Time Between Retries
  cache_control_tab: Cache Control tab
  dn_cache: DN Cache
  dn_cache_size: DN Cache Size
---

# PingDS

Use these attributes when configuring PingDS identity stores:

`amster` service name: `IdRepository`

## All tabs

### Load Schema

Import the appropriate LDAP schema to the directory server before saving the configuration. The LDAP Bind DN service account must have the required privileges to perform this operation.

Learn more in [Prepare identity stores](../installation/prepare-identity-repository.html).

## Server Settings tab

### LDAP Server

An ordered list of directory servers. The format is `HOST:PORT[|SERVERID[|SITEID]]`, where `HOST:PORT` are the directory server FQDN and its port, and `SERVERID` and `SITEID` are optional parameters for deployments with multiple servers and sites.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find the `serverID` and `siteID` by querying the `global-config/servers` and `global-config/sites` endpoints respectively. For example:> **Collapse:&#x20;**
>
> ```bash
> $ curl \
> --request GET \
> --header "Accept: application/json" \
> --header "iPlanetDirectoryPro: AQIC5…​NDU1*" \
> 'https://am.example.com:8443/am/json/global-config/servers?_queryFilter=true'
> {
>   "result": [
>     {
>       "_id": "01",
>       "_rev": "1372703177",
>       "url": "https://am.example.com:8443/am",
>       "siteName": null
>     }
>   ],
>   "resultCount": 1,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": -1
> }
> ```
>
> In the example, the server ID for server `https://am.example.com:8443/am` is `01`.> **Collapse:&#x20;**
>
> ```bash
> $ curl \
> --request GET \
> --header "Accept: application/json" \
> --header "iPlanetDirectoryPro: AQIC5…​NDU1*" \
> 'https://am.example.com:8443/am/json/global-config/sites?_queryFilter=true'
> {
>   "result": [
>     {
>       "_id": "site-name",
>       "_rev": "1372703177",
>       "id": "02",
>       "url": "https://am.example.com:8443/am",
>       "secondaryURLs": [],
>       "servers": []
>     }
>   ],
>   "resultCount": 1,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": -1
> }
> ```
>
> In the example, the site ID is `02`. |

Multiple servers must be comma-separated, for example, `ds1.example.com:1636, ds2.example.com:1636`.

AM uses the optional settings to determine which directory server to contact first. AM tries to contact directory servers in the following priority order, with the highest priority first:

1. The first directory server in the list whose *serverID* matches the current AM server.

2. The first directory server in the list whose *siteID* matches the current AM server.

3. The first directory server in the remaining list.

If the directory server isn't available, AM proceeds to the next directory server in the list.

In production environments, you should specify more than one directory server for failover purposes.

Default: `host:port` of the initial directory server configured for this AM server.

### LDAP Bind DN

Bind DN of the service account AM uses to connect to the directory server. Some AM capabilities require write access to directory entries.

If you enable mTLS authentication, this value is ignored.

### LDAP Bind Password

Bind password for connecting to the directory server.

If you enable mTLS authentication, this value is ignored.

### Proxied Authorization using Bind DN

When the `force-change-on-reset` password policy is configured on the DS user datastore, users resetting their passwords using AM's forgotten password feature might be required to reset their passwords twice (prompted by both AM's User Self-Service and DS's password policy).

If you enable Proxied Authorization using Bind DN, AM uses DS's [proxied authorization](https://docs.pingidentity.com/pingds/8.1/ldap-guide/proxied-authz.html) to reset user passwords. This means AM performs the password reset as the user, so users don't have to reset their passwords again.

Before enabling this setting, ensure that the service account configured in the LDAP Bind DN property has the `proxied-auth` privilege granted. If the service account doesn't have the required privilege, users would not be able to reset their passwords and AM and DS will log an error message.

You can find examples for setting the privileges required for the password reset feature in [Installing and Configuring PingDS for Identity Data](../installation/prepare-identity-repository.html#prepare-idrepo).

Enable this property only if:

* The `force-change-on-reset` password policy is configured in the DS user datastore.

* The forgotten password user self-service feature is configured in AM.

* Users are being forced to reset their passwords twice.

Default: `Disabled`

### Fallback using Bind DN if Proxied Authorization denied

Enable this setting to fallback and retry using non-proxied authorization (without the PingDS `proxied-auth` privilege) when proxied authorization is denied.

Enabling this property causes AM to attempt to make LDAP changes as the LDAP Bind DN service account if proxied authorization was unsuccessful; for example, if the user account attempting the changes originally is locked or the password has expired.

This setting is effective only when Proxied Authorization using Bind DN is also enabled.

Default: `Disabled`

### LDAP Organization DN

The base DN under which to find user and group profiles.

Ensure that the identity store is set up with the specified DN before making any changes to this property in AM.

Default: `base-dn`

### LDAP Connection Mode

Whether to use LDAP, LDAPS or StartTLS to connect to the directory server. If you enable LDAPS or StartTLS, AM must be able to trust server certificates, either because the server certificates were signed by a CA whose certificate is already included in the trust store used by the container where AM runs, or because you imported the certificates into the trust store.

Possible values: `LDAP`, `LDAPS`, and `StartTLS`

### Trust All Server Certificates

Whether AM trusts all server certificates when LDAPS or StartTLS are used to connect to the directory server.

Only enable this property if you completely trust the directory server.

Default: `Disabled`

### LDAP Connection Pool Minimum Size

Minimum number of connections to the directory server.

Default: `1`

### LDAP Connection Pool Maximum Size

Maximum number of connections to the directory server. Make sure the directory service can cope with the maximum number of client connections across all servers.

Default: `10`

### LDAP Connection Heartbeat Interval

How often to send a heartbeat request to the directory server to ensure that the connection doesn't remain idle. Some network administrators configure firewalls and load balancers to drop connections that are idle for too long. You can turn this off by setting the value to 0.

To set the units for the interval, use `LDAP Connection Heartbeat Time Unit`.

Note that setting this property to `0` will disable the heartbeat (keepalive) requests and load balancer availability checks.

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

Time unit for the `LDAP Connection Heartbeat Interval` setting.

Default: `second`

### Maximum Results Returned from Search

A cap for the number of search results to return, for example, when viewing profiles under Identities. Rather than raise this number, consider narrowing your search to match fewer directory entries.

Default: `1000`

### Search Timeout

Maximum time to wait for search results in seconds. Doesn't apply to persistent searches.

Default: `10`

### LDAPv3 Plugin Search Scope

LDAP searches can apply to a single entry (`SCOPE_BASE`), entries directly below the search DN (`SCOPE_ONE`), or all entries below the search DN (`SEARCH_SUB`).

Default: `SCOPE_SUB`

### Behera Support Enabled

Enable this property to use Behera draft control in outgoing requests for operations that might modify password values.

Behera draft control allows AM to display password policy related error messages when password policies aren't met.

Default: `Enabled`

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

### mTLS Enabled

Enables mutual TLS (mTLS) between AM and the directory server.

When mTLS is enabled, AM ignores the values for LDAP Bind DN and LDAP Bind Password.

If you enable this property, you must:

* Set the LDAP Connection Mode to `LDAPS`.

* Provide an mTLS Secret Label Identifier.

Default: `Disabled`

### mTLS Secret Label Identifier

Identifier used to create a secret label for mapping to the mTLS certificate in the secret store. AM uses this identifier to create a specific secret label for this identity store. The secret label takes the form `am.identity.repository.label.cert` , where `label` is the value of mTLS Secret Label Identifier. The identifier can only contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and periods (`.`). It can't start or end with a period.

When you configure mTLS, you must map the secret label based on this identifier to the correct certificate alias. To avoid a temporarily "broken" mTLS connection, add the mTLS Secret Label Identifier first, without enabling mTLS. Then [configure the mapping](../security/secure-data-stores.html#configure-mtls-mappings-id-store) to the certificate alias, then enable mTLS.

For more security, you should rotate certificates periodically. When you rotate a certificate, update the corresponding mapping in the realm secret store configuration to reflect this identifier. When you rotate a certificate, AM closes any existing connections using the old certificate. AM selects a new connection from the connection pool and no server restart is required.

## Plug-in Configuration tab

### LDAPv3 Repository Plugin Class Name

AM identity store implementation.

Default: `org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo`

### Attribute Name Mapping

Map of AM profile attribute names to directory server attribute names.

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

Default: `uid`

|   |                                                                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Don't modify the value of the search attribute in user profiles. Modifying this attribute value can result in incorrectly cached identity data. For example, if you configure the search attribute to `mail`, it could prevent users from being able to update their email addresses in their user profiles. |

### LDAP Users Search Filter

When searching for users, apply this LDAP search filter as well.

Default: `(objectclass=inetorgperson)`

### LDAP User Object Class

User profiles have these LDAP object classes.

AM handles only those attributes listed in this setting. AM discards any unlisted attributes from requests and the request proceeds without the attribute.

For example, with default settings, if you request that AM execute a search that asks for the `mailAlternateAddress` attribute, AM does the search, but doesn't request `mailAlternateAddress`. In the same way, AM does perform an update operation with a request to set the value of an unlisted attribute like `mailAlternateAddress`, but it drops the unlisted attribute from the update request.

Default:\
`iplanet-am-managed-person`\
`inetuser`\
`sunFMSAML2NameIdentifier`\
`inetorgperson`\
`devicePrintProfilesContainer`\
`pushDeviceProfilesContainer`\
`iPlanetPreferences`\
`iplanet-am-user-service`\
`forgerock-am-dashboard-service`\
`organizationalperson`\
`top`\
`kbaInfoContainer`\
`oathDeviceProfilesContainer`\
`person`\
`sunAMAuthAccountLockout`\
`iplanet-am-auth-configuration-service`

### LDAP User Attributes

User profiles have these LDAP attributes.

AM handles only those attributes listed in this setting. AM discards any unlisted attributes from requests and the request proceeds without the attribute.

Default:\
`iplanet-am-user-password-reset-question-answer`\
`mail`\
`iplanet-am-user-alias-list`\
`iplanet-am-auth-configuration`\
`assignedDashboard`\
`authorityRevocationList`\
`dn`\
`iplanet-am-user-password-reset-options`\
`createTimestamp`\
`employeeNumber`\
`kbaActiveIndex`\
`caCertificate`\
`iplanet-am-session-quota-limit`\
`iplanet-am-user-auth-config`\
`sun-fm-saml2-nameid-infokey`\
`sunIdentityMSISDNNumber`\
`devicePrintProfiles`\
`sunAMAuthInvalidAttemptsData`\
`iplanet-am-user-password-reset-force-reset`\
`givenName`\
`iplanet-am-session-get-valid-sessions`\
`objectClass`\
`adminRole`\
`inetUserHttpURL`\
`iplanet-am-user-account-life`\
`userCertificate`\
`postalAddress`\
`preferredtimezone`\
`iplanet-am-user-admin-start-dn`\
`oath2faEnabled`\
`preferredlanguage`\
`sun-fm-saml2-nameid-info`\
`userPassword`\
`iplanet-am-session-service-status`\
`telephoneNumber`\
`iplanet-am-session-max-idle-time`\
`distinguishedName`\
`iplanet-am-session-destroy-sessions`\
`modifyTimestamp`\
`uid`\
`iplanet-am-user-success-url`\
`kbaInfo`\
`iplanet-am-user-auth-modules`\
`sn`\
`memberOf`\
`preferredLocale`\
`manager`\
`iplanet-am-session-max-session-time`\
`cn`\
`oathDeviceProfiles`\
`iplanet-am-user-login-status`\
`pushDeviceProfiles`\
`inetUserStatus`\
`iplanet-am-user-failure-url`\
`iplanet-am-session-max-caching-time`

### Create User Attribute Mapping

When creating a user profile, apply this map of AM profile attribute names to directory server attribute names.

Attributes not mapped to another attribute (for example, `cn`) and attributes mapped to themselves (for example, `cn=cn`) take the value of the username unless the attribute values are provided when creating the profile. The object classes for user profile LDAP entries generally require Common Name (cn) and Surname (sn) attributes, so this prevents an LDAP constraint violation when performing the add operation.

Default: `cn`, `sn`

### Attribute Name of User Status

Attribute to check/set user status.

Default: `inetuserstatus`

### User Status Active Value

Active users have the user status attribute set to this value.

Default: `Active`

### User Status Inactive Value

Inactive users have the user status attribute set to this value.

Default: `Inactive`

### LDAP People Container Naming Attribute

RDN attribute of the LDAP base DN which contains user profiles.

Default: `ou`

### LDAP People Container Value

RDN attribute value of the LDAP base DN which contains user profiles.

If specified, AM will limit searches for user profiles to the provided base DN. Otherwise, AM searches the entire directory.

Default: `people`

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

Default: `uid`

## Group Configuration tab

### LDAP Groups Search Attribute

When searching for a group by name, match values against this attribute.

Default: `cn`

### LDAP Groups Search Filter

When searching for groups, apply this LDAP search filter as well.

Default: `(objectclass=groupOfUniqueNames)`

### LDAP Groups Container Naming Attribute

RDN attribute of the LDAP base DN which contains group profiles.

Default: `ou`

### LDAP Groups Container Value

RDN attribute value of the LDAP base DN which contains group profiles.

If specified, AM will limit searches for group profiles to the provided base DN. Otherwise, AM searches the entire directory.

Default: `groups`

### LDAP Groups Object Class

Group profiles have these LDAP object classes.

Default: `groupofuniquenames`, `top`

### LDAP Groups Attributes

Group profiles have these LDAP attributes.

Default: `dn`, `cn`, `uniqueMember`, `objectclass`

### Attribute Name for Group Membership

LDAP attribute in the member's LDAP entry whose values are the groups to which a member belongs.

### Attribute Name of Unique Member

Attribute in the group's LDAP entry whose values are the members of the group.

Default: `uniqueMember`

### Attribute Name of Group Member URL

Attribute in the group's LDAP entry whose values are LDAP URLs which define dynamic members of the group.

Default: `memberUrl`

## Persistent Search Controls tab

### Persistent Search Base DN

Base DN for LDAP-persistent searches used to receive notification of changes in directory server data.

Default: `base-dn`

### Persistent Search Filter

LDAP filter to apply when performing persistent searches.

Default: `(!(objectclass=frCoreToken))`

### Persistent Search Scope

LDAP searches can apply to a single entry (`SCOPE_BASE`), entries directly below the search DN (`SCOPE_ONE`), or all entries below the search DN (`SEARCH_SUB`).

Default: `SCOPE_SUB`

## Error Handling Configuration tab

### The Delay Time Between Retries

The number of milliseconds to wait between retry attempts when an LDAP operation fails with a retryable error.

The DS datastore uses this setting only for persistent searches.

Default: `1000`

## Cache Control tab

### DN Cache

Whether to enable the DN cache, which is used to cache DN lookups that can happen in bursts during authentication. As the cache can become stale when a user is moved or renamed, enable DN caching when the directory service allows move/rename operations (Mod DN), and when AM uses persistent searches to obtain notification of such updates.

Default: `true`

### DN Cache Size

Maximum number of DNs cached when caching is enabled.

Default: `1500`

---

---
title: Policy and application stores
description: Configure separate datastores for UMA data, Core Token Service sessions and tokens, policy data, and application data in PingAM
component: pingam
version: 8.1
page_id: pingam:setup:setting-up-data-stores
canonical_url: https://docs.pingidentity.com/pingam/8.1/setup/setting-up-data-stores.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Setup &amp; Configuration", "Policy", "Application Store"]
page_aliases: ["setup-guide:setting-up-data-stores.adoc"]
---

# Policy and application stores

In addition to the identity store, you can configure datastores for different types of data.

You might want to store these data types separately from other data types, depending on their characteristics; for example, to allow specific tuning of the indexes in the directory server.

You can configure datastores for the following data types:

* **UMA data**.

  Provides storage for UMA-related data, such as resources, labels, and pending requests.

* **Core Token Service (CTS) data**.

  Provides highly available storage for sessions and tokens used by AM.

* **Policy data**.

  Provides storage for policy-related data, such as policies, policy sets, and resource types. Policy stores also store [delegated realm administration privileges](../security/securing-administration.html#delegating-realm-administration-privileges).

  |   |                                                                                                                                                                                                                                                                                                                                     |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you change the policy datastore, any existing policy sets and resource types will no longer be available to the realm where you made the change. Either recreate these items manually, or use [Amster](../amster/preface.html) to export them from the old datastore, then import them back after changing to the new datastore. |

* **Application data**.

  Provides storage for application-related data, such as web and Java agent configuration, federation entities and configuration, and OAuth 2.0 clients definitions.

**Tasks to configure policy and/or application stores**

| Task                                                                                                                                                                                                                                             | Resources                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| **Prepare the store(s)**You must install new DS servers for the store(s). If you are configuring an AM instance that already has policy or application data in its configuration store, you might want to migrate that data to the new store(s). | [Prepare policy and application stores](prepare-policy-and-application-store.html) |
| **Configure the store(s)**Configure the newly-installed store(s) so that AM can use them.                                                                                                                                                        | [Configure policy and application stores](setting-up-policy-and-app-stores.html)   |