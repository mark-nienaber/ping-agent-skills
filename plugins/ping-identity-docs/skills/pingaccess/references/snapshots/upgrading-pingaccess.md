---
title: Performing post-upgrade tasks
description: After upgrading your PingAccess deployment using the upgrade utility or the installer, you must perform several post-upgrade tasks to ensure that the target version works correctly.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_performing_post_upgrade_tasks
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_performing_post_upgrade_tasks.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  troubleshooting: Troubleshooting
---

# Performing post-upgrade tasks

After upgrading your PingAccess deployment using the upgrade utility or the installer, you must perform several post-upgrade tasks to ensure that the target version works correctly.

## About this task

To see details about the upgrade, examine `log/upgrade.log`. To see details about the migrated configuration data, examine `log/audit.log`.

## Steps

1. Review any warnings returned by the upgrade utility and take the actions indicated in the table below.

   At the end of an upgrade, the PingAccess upgrade utility or installer records any manual steps that require user intervention both in the command-line output and in `log/upgrade.log` at the WARN level. Information that does not require user intervention is added to the `log/upgrade.log` at the INFO level.

2. Review the HTTP requests configuration to ensure the use of the IP source settings is appropriate for the environment.

3. Stop the source version of PingAccess.

4. Start the target version of PingAccess.

## Troubleshooting

| Warning text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Steps to take                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Resource <ResourceName> contains an invalid path prefix and cannot be migrated to the target version. Manual intervention is required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This occurs when the 2.1 path prefix contains functionality supported through a Java regex, but not by the wild card support in 3.1. The user must manually migrate the regex to 1 or more path prefixes in 3.1. For example, consider the 2.1 prefix, ﻿ `/(app1\|app2)`. This can be translated to a single resource in 3.1.1 with path prefixes of `/app1` and `/app2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `Resource <ResourceName> requires a case-sensitive path. This conflicts with its containing application, which requires a case-insensitive path. Manual intervention may be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The upgrade utility identifies path prefixes in 2.1 that start with `/(?i)` as path prefixes that are case-insensitive, and sets the case-sensitivity flag on the application appropriately. However, if multiple resources in a new application use inconsistent case sensitivity settings, the utility cannot determine what the case sensitivity should be. 2.1 resources are case-sensitive by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `Resource <ResourceName> requires a case-insensitive path. This conflicts with its containing application, which requires a case-sensitive path. Manual intervention may be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | This is the same as the previous setting, but with the requirement being for a case-insensitive path rather than a case-sensitive one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Resource <ResourceName> is disabled in the source version. Resources can no longer be individually disabled. Application <ApplicationName> has been disabled due to this constraint.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | In 2.1, individual resources can be disabled. In 3.1, only applications can be enabled or disabled. The upgrade utility takes the approach of disabling the application if any related resources are disabled. Check the final configuration and make sure this is the desired outcome.  If it is not, the disabled resources need to be deleted, and the application needs to be enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `Path prefix for resource <ResourceName> contains a '.' character. This will be treated as a literal '.' in the target version.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | In a 2.1 setup, there might be resource names that accidentally contain a '.', assuming it is a literal '.' rather than part of a regex. For example, any file extension type resources will probably not be escaping the '.'. This message is intended to bring this change in semantics to the user's attention. This action item will not show up if the user has correctly escaped the '.' character with the '\\.' sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Resource <ResourceName> could not be migrated to the target version due to application context root conflicts. Manual intervention is required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | This message indicates that multiple resources that use the same virtual host, but a different web session or site must be mapped under the same context root in the same application to preserve semantics.  For example, consider the following configuration:- Resource A:

  * Path Prefix: /hr

  * Virtual Host: internal.example.com

  * Web Session: W

  * Site: Z

- Resource B:

  * Path Prefix: /sales

  * Virtual host: internal.example.com

  * Web Session: W

  * Site: Z

- Resource C:

  * Path Prefix: /payroll

  * Virtual Host: internal.example.com

  * Web Session: V

  * Site: ZThis configuration triggers this error because these resources cannot be grouped in the same application, but they would need to be to preserve the semantics in the internal.example.com address space. This issue could be fixed by using rewrite rules to place Resource C or Resources A and B under a different namespace. For example, use `/intranet/sales` and `/intranet/hr` on the front-end and rewrite out the `/intranet` on the backend. |
| `Application <ApplicationName> contains OAuth rules, but authenticates users with a web session. Unexpected results may occur.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Step 2.1 allows OAuth *(tooltip: \<div class="paragraph">&#xA;\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>&#xA;\</div>)* rules to be attached resources that use a web session. While this configuration is likely invalid in the first place, it would be possible to include both a PingAccess cookie and OAuth token in requests and PingAccess would apply policy to the requests as configured. In 3.1, however, an application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* application and web application are mutually exclusive so the semantics of this particular configuration cannot be preserved.                                                                                                                                      |
| `The resource order for virtual host <VirtualHostName> has changed in the target version.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The upgrade utility checks that the resource order is consistent before and after the upgrade. This message indicates that the resource order from 2.1 does not match 3.1. This is likely due to how context roots in applications are ordered in 3.1. For 3.1, applications are ordered based on their context root, where the longest context root is checked first during resource matching.One way to address this is to review and potentially change the application context root values associated with the virtual host to avoid Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">&#xA;\<p>Identifies a resource according to its internet location.\</p>&#xA;\</div>)* overlaps between applications.                                                                                                                                                                                                                                                                                                                                        |
| `Application <ApplicationName> is no longer associated with an identity mapping. A web session or an authorization server is required to use identity mappings.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Indicates a misconfiguration in the source version. Check whether you intended to use an identity mapping for the application and associate an appropriate web session or authorization server if necessary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `OAuth rule with id <RuleId> is no longer associated with application <ApplicationName> because application <ApplicationName> is not an OAuth application. Manual intervention might be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Indicates a misconfiguration in the source version. Check whether the OAuth rule is necessary to implement the desired access control policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `OAuth RuleSet with id <RuleSetId> is no longer associated with application <ApplicationName> because application <ApplicationName> is not an OAuth application. Manual intervention might be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Indicates a misconfiguration in the source version. Check whether the OAuth RuleSet is necessary to implement the desired access control policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `Resource <ResourceName> from application with id <ApplicationId> was not migrated because the application is a web application while the resource has OAuth rules. Manual intervention might be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Indicates a resource associated with the application is associated with OAuth rules. This is likely a misconfiguration, and it is necessary to evaluate whether this was intended or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `Upgrade created availability profile for site <SiteName>. A more descriptive name might be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Indicates that an availability profile was created for the site during the upgrade. You might want to give the availability profile a more descriptive name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `Application <ApplicationName> and associated resources were not migrated. The context root of /pa is reserved. Manual intervention might be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The /pa context root was allowed as a valid context root in PingAccess 3.0 and is no longer allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `Resource <ResourceName> from application with id <ApplicationId> was not migrated because the /pa prefix is reserved when the application context root is /. Manual intervention may be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The */pa* path prefix was allowed as a valid path prefix in PingAccess 3.0 and is no longer allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `The OAuth Groovy script rule no longer controls the realm in the response sent for an unauthorized OAuth request.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | With PingAccess 3.2, realms moved to the application. The *Realm* can still be set using the PingAccess admin API interface. With the change in context for how realms are applied, it is necessary to check existing OAuth Groovy rules to ensure that they behave as expected. This message is shown if any OAuth Groovy rules exist in the migrated configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `The property <PropertyName> was set to a blank value to maintain compatibility. Set this to <PropertyName>=<PropertyValue>.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | New security headers properties values are not set during an upgrade to preserve the behavior from the source release in the upgrade. If there is no reason not to in your environment, update the `run.properties` file with the recommended setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `As a security enhancement, the default value of <CipherList> has changed with this version of PingAccess. Your existing ciphers remain unchanged. Use the default value: <PropertyName>=<CipherList>.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | This message applies to the `admin.ssl.ciphers`, `engine.ssl.ciphers`, and `agent.ssl.ciphers` lists. This message is displayed if the upgrade source version cipher lists are changed from the defaults. Update the configuration with the new default value if possible.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `The property <PropertyName> was set to a blank value to maintain compatibility. Set this to <PropertyName>=<CipherList>.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | This message applies to the `site.ssl.protocols`, `site.ssl.ciphers`, `pf.ssl.protocols`, and `pf.ssl.ciphers` settings. The upgrade utility sets these values as empty values to maintain backwards compatibility, but the recommended value should be used if possible.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `The host for virtual host <VirtualHost>:<Port> already has a keypair associated with it. The keypair previously associated with this virtual host was removed. Only one keypair can be associated with a given host.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | If a virtual host has more than one key pair associated with it, only one key pair will be associated with it after the upgrade completes. This message displays to indicate which key pair was used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `Application with name <ApplicationName> not migrated as the context root <Path> was a reserved path.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | If an application's context root is a reserved PingAccess path, the application will not be migrated. The indicated application will need to be created with a context root that does not conflict with the reserved path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `Resource with name <ResourceName> not migrated as the path <Path> was a reserved path.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | If a resource path is a reserved PingAccess path, the application will not be migrated. The indicated application will need to be created with a context root that does not conflict with the reserved path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `The CIDR rule with name <RuleName> is associated with an agent application named <ApplicationName> and overrides the IP source configuration. A new Agent rule should be created that does not override the IP source.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | With changes in IP source header handling, additional options are available to override the headers used to identify the source address. When an agent is involved, the changes in IP source handling might cause the specified rule to not behave as expected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `Require HTTPS option on application <ApplicationName> was set to <Setting> as virtual host had port <Port>. Please verify this setting is correct.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | The upgrade utility attempts to set the `Require HTTPS` option based on the virtual host associated with an application during an upgrade. This message is an advisory to just verify that the setting was properly detected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `Virtual host <VirtualHost> was not migrated. An existing virtual host existed with the same logical name <VirtualHost>.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Virtual host names are now case-insensitive. During the upgrade, after making the names case-insensitive, a duplicate virtual host was identified. It will be necessary to either recreate the virtual host with a new name, or to modify the configuration so the proper virtual host is migrated to the upgraded system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `Renamed virtual host's hostname from <VirtualHost to <NewVirtualHost> due to virtual host spec compliance issue`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | If a virtual host name contains an underscore (*\_*) character, that does not conform to host naming requirements. In this instance, the underscore will be renamed to the string *a-z*. For example, if a virtual host named *\<my\_virtual\_host>* is migrated, the new name will be *\<mya-zvirtuala-zhost>*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `Removed HTTP request rule with name <RuleName>, this rule must be converted to a Groovy script rule. Manual intervention might be required.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | When an HTTP request *(tooltip: \<div class="paragraph">&#xA;\<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>&#xA;\</div>)* rule is migrated from an earlier release of PingAccess, rules that specify a source of *\<Body>* are not migrated. A Groovy script rule can be used to perform a similar match, but the details of such a Groovy script require administrator intervention.A simple Groovy script rule that would perform a similar function might be:```
requestBodyContains('value')
```A script should be constructed that performs additional validation to ensure the rule passes only when desired. A generic match like this could lead to unexpected results depending on what content might be in the request body.                                                                                                                                                                                               |
| `The property <PropertyName> uses a customized value. "Your original value has not been modified. You may encounter startup or connection problems if this value is not supported by the JVM."`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | When migrating SSL settings between versions of PingAccess that use different Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* or Java Development Kit (JDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A development environment for building applications and components using Java.\</p>&#xA;\</div>)* versions, custom settings might not be compatible. If the protocols or ciphers used are not compatible with the target JVM or JDK, this message indicates which settings need to be manually updated.The *PropertyName* value can be any of the following values:- `site.ssl.protocols`

- `site.ssl.ciphers`

- `pf.ssl.protocols`

- `pf.ssl.ciphers`

- `admin.ssl.protocols`

- `admin.ssl.ciphers`

- `engine.ssl.protocols`

- `engine.ssl.ciphers`

- `agent.ssl.protocols`

- `agent.ssl.ciphers`                                                                                           |
| `Rule with ID <RuleId> and name <RuleName> was not migrated as matcher was invalid for the Groovy rule type.``Invalid rules were removed from RuleSet <RuleSetName> which resulted in an empty set.`*The RuleSet was removed. Please check your policy configuration.*`Invalid rules were removed from RuleSet <RuleSetName>. Please check your policy configuration.``Invalid rules were removed from application <ApplicationName>. Please check your policy configuration.``Invalid RuleSets were removed from application <ApplicationName>. Please check your policy configuration.``Invalid rules were removed from resource <resource name> on application <ApplicationName>. Please check your policy configuration.``Invalid RuleSets were removed from Resource 'resource name' on Application 'ApplicationName'. Please check your policy configuration.` | These messages might appear if the source PingAccess installation has misconfigured Groovy Rules.This indicates that you are not permitted to add an OAuth rule to an Application of type Web by editing an existing rule set.Groovy or OAuth Groovy rules will not be migrated for the following reasons:- The OAuth Groovy rule was applied to a Web application.

- The Groovy or OAuth Groovy uses a matcher that is not appropriate for the application type.Check the policy configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Rule with name <RuleName> has been removed from RuleSet with name <RuleSetName>. Multiple rate limiting rules with the same policy granularity cannot be included in a RuleSet."``Rule with name <RuleName> has been removed from RuleSet with name <RuleSetName>. Multiple cross-Origin request rules cannot be included in a RuleSet."`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The upgrade utility supports migrating a rule set containing multiple cross-origin resource sharing (CORS) or rate limiting rules with the same policy granularity. The upgrade utility will generate new action items, indicating that rules were removed from a rule set.These messages indicate that if both rules exist, there is a restriction to a single rate limiting or CORS rule. Please check to confirm that you have applied the correct rule to the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `One or more notifications were issued while migrating from version <SOURCE> to version <TARGET>.``Setting clusterconfig.enabled to false``The new configuration query port feature has been disabled for backward compatibility. Please refer to the PingAccess clustering documentation before enabling this feature.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The new cluster config query port is enabled by default for new PingAccess 4.0 installations when running in CLUSTERED\_CONSOLE or CLUSTERED\_CONSOLE\_REPLICA mode.During the upgrade process to version 4.0, the new cluster config query port is disabled. Messages are written to `upgrade.log` and `audit.log` to indicate this cluster configuration change was made.See the PingAccess clustering documentation before enabling this feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `One or more notifications were issued while migrating from version <SOURCE> to version <TARGET>``For backward compatibility, when connecting to a protected, TLS SNI-enabled site, PingAccess will set the SNI server_name to the configured target host and not the HTTP request Host header value. Please refer to PingAccess' upgrade documentation for more information.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | During upgrades to release 4.0 and higher, the upgrade utility sets the value of `pa.site.tls.sni.legacyMode` to `true` to maintain compatibility with existing configurations. This property is controlled in the `run.properties` file and is not enabled on new installs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `Localization property <\{property name}> was added to pa-messages.properties. Any customized localization files should be updated.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This message appears if new language properties are added between the source and target PingAccess versions and you have added additional language files or modified the en or en\_US files. Update any customized files as required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `Localization property <\{property name}> in pa-messages.properties was modified. Any customized localization files should be updated.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | This message appears if the language properties have changed between the source and target PingAccess versions and you have added additional language files or modified the en or en\_US files. Update any customized files as required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `Localization property <\{property name}> was removed from pa-messages.properties. This property can be removed from any customized localization files.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This message appears if the language properties have been removed between the source and target PingAccess versions and you have added additional language files or modified the en or en\_US files. Update any customized files as required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `WebSessionManagement contained an invalid cookie name. Replaced <\{old cookie name}> with <\{new cookie name}>. Please validate your configuration.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | This message appears if the WebSessionManagement has an invalid cookie name. Invalid characters are replaced with an underscore. Update any references as required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Legacy authentication requirements policy evaluation has been enabled to maintain backward compatibility with earlier versions of PingAccess. To disable this setting, remove the pa.policy.eval.acr.v42 property from run.properties.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This message appears on upgrade to release 4.3 or later if you have one or more authentication requirements rules. You can make adjustments to configured rules so you can remove this property or you can maintain the property to leave existing rules unaffected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `Property pa.audit.log.applicationResourceIdsAsIntegers was set to true in run.properties to maintain existing behavior. In order to log the ID of Global Unprotected Resources, this property should be removed or should be set to false (default). However, a value of false (default) will result in resourceId and applicationId audit logging fields being logged as strings, not integers, which may require audit logging database schema changes if these values are currently being used.`                                                                                                                                                                                                                                                                                                                                                                 | This message appears on upgrade to release 5.1 or later to support the existing logging behavior of application resource IDs as integers. The default behavior of release 5.1 and later is to log these IDs as strings. You can choose to log application resource IDs as strings after the upgrade by removing, or setting to false, the applicable property in the `run.properties` file. This change might require a modification to the audit logging database schema.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `Invalid resource method <Method> was removed from resource <ResourceName> on application <ApplicationName>.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | This message appears on upgrade to release 5.3 or later if the source version has an application resource that contains a method with whitespace. The resource is preserved by the upgrade, but the method is removed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Invalid resource <{name}> on application <{name}> was removed because it did not have any valid methods.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | This message appears on upgrade to release 5.3 or later if all of the methods associated with a resource were removed with an `Invalid resource method` error. The resource is not migrated by the upgrade.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `As of PingAccess 6.0, runtime state clustering using JGroups has been deprecated. Deployments relying on runtime state clustering will continue to function but the functionality will be replaced in a future version.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | This message appears on an upgrade to release 6.0 or later. The runtime state clustering feature has been deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: PingAccess cluster upgrade parameters
description: The command-line parameters are the same regardless of the platform, and are defined as follows.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_cluster_upgrade_parameters
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_cluster_upgrade_parameters.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  parameter-definitions: Parameter definitions
  environment-variables: Environment variables
  java-virtual-machine-jvm-memory-options: Java virtual machine (JVM) memory options
  example: Example
---

# PingAccess cluster upgrade parameters

The command-line parameters are the same regardless of the platform, and are defined as follows.

## Parameter definitions

| Parameter                          | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -r \| --disable-config-replication | Disables configuration replication on the admin node. For more information about using this parameter in an upgrade, see the [Zero Downtime Upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html).                                                                                                                                                                                                                                                                                                                                                                |
| -p *\<admin\_port>*                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -i *\<directory>*                  | An optional directory containing additional library JAR files, such as plugins, Java Database Connectivity (JDBC) drivers to be copied into the target installation.Beginning in version 6.0, `JAR` files are stored in the `<PA HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party `JAR` files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA HOME>/deploy` folder if no directory is specified. |
| *\<sourcePingAccessRootDir>*       | The PA\_HOME for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -l *\<newPingAccessLicense>*       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -j *\<jvm\_memory\_options\_file>* | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* memory options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                                                      |
| -s \| --silent                     | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Environment variables

You can specify the username and password for the source version using these environment variables:

* `PA_SOURCE_API_USERNAME` – The username for the source version's Admin API. This should be set to Administrator.

* `PA_SOURCE_API_PASSWORD` – The basic authorization password for the Administrator in the source version's Admin API.

## Java virtual machine (JVM) memory options

These options can be included in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

* `-Xms<amount>` – Minimum heap size.

* `-Xmx<amount>` – Maximum heap size.

* `-XX:NewSize=<amount>` – Minimum size for the Young Gen space.

* `-XX:MaxNewSize=<amount>` – Maximum size for the Young Gen space.

* `-XX:+UseParallelGC` – Specifies that the parallel garbage collector should be used.

You can copy the existing `<PA_HOME>/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

## Example

```
#Sample JVM Memory options file
-Xms512m
-Xmx1g
-XX:NewSize=256m
-XX:MaxNewSize=512m
-XX:+UseParallelGC
```

---

---
title: PingAccess standalone upgrade parameters
description: The command-line parameters are the same regardless of the platform and are defined in the following table.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_standalone_upgrade_parameters
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_standalone_upgrade_parameters.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  environment-variables: Environment variables
  java-virtual-machine-jvm-memory-options: Java virtual machine (JVM) memory options
  example: Example
---

# PingAccess standalone upgrade parameters

The command-line parameters are the same regardless of the platform and are defined in the following table.

| Parameter                          | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -p *\<admin\_port>*                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -i *\<directory>*                  | An optional directory containing additional library JAR files, such as plugins and Java Database Connectivity (JDBC) drivers, to be copied into the target installation.Beginning in version 6.0, JAR files are stored in the `<PA HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party JAR files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA HOME>/deploy` folder if no directory is specified. |
| *\<sourcePingAccessRootDir>*       | The `PA_HOME` for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -l *\<newPingAccessLicense>*       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -j *\<jvm\_memory\_options\_file>* | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                                                             |
| -s \| --silent                     | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Environment variables

You can specify the username and password for the source version using these environment variables:

* `PA_SOURCE_API_USERNAME` – The username for the source version's Admin API. This should be set to Administrator.

* `PA_SOURCE_API_PASSWORD` – The basic authorization password for the Administrator in the source version's Admin API.

## Java virtual machine (JVM) memory options

You can include these options in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

* `-Xms<amount>` – Minimum heap size

* `-Xmx<amount>` – Maximum heap size

* `-XX:NewSize=<amount>` – Minimum size for the Young Gen space

* `-XX:MaxNewSize=<amount>` – Maximum size for the Young Gen space

* `-XX:+UseParallelGC` – Specifies that the parallel garbage collector should be used

You can copy the existing `<PA_HOME>/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

## Example

```
#Sample JVM Memory options file
-Xms512m
-Xmx1g
-XX:NewSize=256m
-XX:MaxNewSize=512m
-XX:+UseParallelGC
```

---

---
title: Restoring a PingAccess configuration backup
description: If an upgrade fails, restore your PingAccess configuration using an automatically generated backup.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_restoring_a_pa_configuration_backup
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_restoring_a_pa_configuration_backup.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Restoring a PingAccess configuration backup

If an upgrade fails, restore your PingAccess configuration using an automatically generated backup.

## About this task

PingAccess automatically creates a backup `.zip` file each time an administrative user authenticates to the administrative console. These backups are stored in `<PA_HOME>/data/archive`, with a maximum number of backups configurable using the `pa.backup.filesToKeep` configuration parameter in `run.properties`.

|   |                                                                  |
| - | ---------------------------------------------------------------- |
|   | This operation will replace your current configuration settings. |

## Steps

1. Stop PingAccess.

2. Extract the backup file to `<PA_HOME>`.

3. Restart PingAccess.

   ### Result:

   Your PingAccess configuration is reverted to the state in the backup archive that was restored.

---

---
title: Upgrade considerations
description: The following changes between PingAccess versions might require additional steps during an upgrade.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrade_considerations
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrade_considerations.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  considerations-when-upgrading-to-6-0-or-later: Considerations when upgrading to 6.0 or later
  new-templates-for-error-and-logout-pages: New templates for error and logout pages
  using-a-proxied-pingfederate-deployment: Using a proxied PingFederate deployment
  spa-support: SPA support
  considerations-when-upgrading-to-7-0-or-later: Considerations when upgrading to 7.0 or later
  runtime-state-clustering-removal: Runtime state clustering removal
  upgrading-to-or-past-version-7-3-with-a-customized-log4j2-xml-file: Upgrading to or past version 7.3 with a customized log4j2.xml file
  elliptic-curve-key-pair-issues-with-aws-cloudhsm-client-sdk-5: Elliptic Curve key pair issues with AWS CloudHSM Client SDK 5
  improved-configuration-replication-compatibility: Improved configuration replication compatibility
  considerations-when-upgrading-to-8-0-or-later: Considerations when upgrading to 8.0 or later
  upgrading-to-or-past-version-8-0-from-version-6-2-or-below: Upgrading to or past version 8.0 from version 6.2 or below
  pa-keystore-pw-encryption-enforcement: pa.keystore.pw encryption enforcement
  considerations-when-upgrading-to-9-0-or-later: Considerations when upgrading to 9.0 or later
  java-11-removal: Java 11 removal
  rsa-1-5-with-pkcs1-removal: RSA 1.5 with PKCS#1 removal
  rotate: Automatically rotate the admin config query certificate
---

# Upgrade considerations

The following changes between PingAccess versions might require additional steps during an upgrade.

## Considerations when upgrading to 6.0 or later

### New templates for error and logout pages

In PingAccess 6.1, we updated several error and logout page template files to modernize their appearance and remove Ping branding:

* `general.loggedout.page.template.html`

* `general.error.page.template.html`

* `admin.error.page.template.html`

* `policy.error.page.template.html`

You can find more information about the templates in [User-facing page customization reference](../configuring_and_customizing_pingaccess/pa_user_facing_page_customization_ref.html). If you customized the template files previously, recustomize the new files.

### Using a proxied PingFederate deployment

PingAccess 6.2 introduced the ability to configure a proxied PingFederate deployment through PingAccess. If you configured a similar deployment in an earlier version of PingAccess manually, you can continue to use it.

However, if you plan to switch from a deployment that you configured manually to a proxied PingFederate deployment through PingAccess:

* Review the configuration options in the proxied PingFederate deployment admin console. Verify that it can support your current configuration's use cases.

* Remove any PingFederate-related applications before migrating the configuration.

### SPA support

We removed the single-page application (SPA) support checkbox from the admin UI for **Web** applications in PingAccess 6.2. Consequently, all **Web** applications created in PingAccess 6.2 and later have SPA support enabled by default.

The SPA support checkbox is still available for **API** applications and **Web + API** applications. You can find more information in [Application field descriptions](../pingaccess_user_interface_reference_guide/pa_application_field_descriptions.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If the default settings for SPA support with **Web** applications aren't compatible with your environment or with a specific application, you can [change the default authentication policy](../pingaccess_user_interface_reference_guide/pa_changing_the_default_authentication_challenge_policy.html) or [create a new authentication challenge policy](../pingaccess_user_interface_reference_guide/pa-managing-acps.html). |

PingAccess 7.1 added a system-provided authentication challenge policy that disables SPA support by default. This policy is useful if you aren't onboarding any new SPAs and don't have many SPAs in your current environment. Learn more in [Authentication](../pingaccess_user_interface_reference_guide/pa_authentication.html).

## Considerations when upgrading to 7.0 or later

### Runtime state clustering removal

Support for runtime state clustering was removed in PingAccess 7.0. However, one benefit of runtime state clustering was that it enabled [rate limiting rules](../pingaccess_user_interface_reference_guide/pa_adding_rate_limiting_rules.html) to behave more consistently in a clustered environment. This was because runtime state clustering enabled all of the engines in a cluster to know the total number of requests for a resource, not just the requests which that engine received.

If you're using runtime state clustering with rate limiting rules, before upgrading to PingAccess 7.0 or later, you should either:

* Configure a load balancer sitting in front of a PingAccess cluster to stick the session to a specific engine. This ensures that a single PingAccess engine node applies the rate limiting rule. Learn more in [Managing load balancing strategies](../pingaccess_user_interface_reference_guide/pa_load_balancing_strategies.html).

* Tune down the **Max Burst Requests** interval on the rate limiting rule, following the *\<current max burst requests interval>*/*\<number of engines in cluster>* ratio.

### Upgrading to or past version 7.3 with a customized `log4j2.xml` file

PingAccess 7.3 introduced a new `log4j-categories.xml` file to enable adjustment of the amount of detail included in PingAccess's logs. Learn more in [Configuring verbose logging in the admin console](../pingaccess_user_interface_reference_guide/pa_configuring_verbose_logging.html).

If you have customized your `log4j2.xml` file, you must merge this file with the `log4j-categories.xml` file the first time you upgrade to PingAccess 7.3 or a later version.

### Elliptic Curve key pair issues with AWS CloudHSM Client SDK 5

As of PingAccess 7.3, PingAccess offers support for Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)* CloudHSM Client SDK 5 instead of Client SDK 3.

Client SDK 5 introduces an issue with elliptic curve (EC) key pairs for all TLS handshakes, similar to the extant issue with TLS 1.3 for EC and RSA keys. As a result, you can create EC key pairs in PingAccess, but you can't assign them to a listener.

### Improved configuration replication compatibility

PingAccess 7.3 introduced the ability for engine nodes and the replica administrative node to connect to an administrative node that's running a later version of PingAccess. This ability was backported to PingAccess 7.2.2 as well.

Nodes running PingAccess 7.2.2 or later can replicate data that's relevant for the version of PingAccess that they're running from the administrative node. You can find more information on clustering and configuration data replication in [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html).

This ability to maintain compatibility reduces the possibility for outages caused by outdated information, providing more flexibility during the upgrade process for those with large scale or hybrid environments. It also improves stability for containerized deployments because clustered engine nodes don't need to maintain their replication data throughout a restart.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You should still finish upgrading the engine nodes as soon as possible and avoid making configuration changes until all engines have been upgraded. |

## Considerations when upgrading to 8.0 or later

### Upgrading to or past version 8.0 from version 6.2 or below

If you have PingAccess 6.2 or below, you cannot upgrade directly to PingAccess 8.0. You must upgrade to a version above 6.2 first, and then upgrade to 8.0.

This is because in PingAccess 8.0, an outdated H2 JAR file was removed, and PingAccess 6.2 and below use an H2 embedded database.

### `pa.keystore.pw` encryption enforcement

PingAccess 8.3 and later enforce encryption of the `pa.keystore.pw` property in the `run.properties` file as follows:

* In non-FIPS mode, if you don't obfuscate `pa.keystore.pw`, PingAccess logs a warning during startup.

* If you try to enable FIPS mode without obfuscating `pa.keystore.pw`, PingAccess terminates startup and logs an error message.

## Considerations when upgrading to 9.0 or later

### Java 11 removal

Ping Identity removed Java 11 support from PingAccess in December 2025. You must upgrade to a supported Java version before installing PingAccess 9.0 or later. Learn more about supported java versions in [PingAccess system requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html#system-reqs).

### RSA 1.5 with PKCS#1 removal

Ping Identity removed support for RSA 1.5 with PKCS#1 in PingAccess 9.0.

### Automatically rotate the admin config query certificate

PingAccess 9.1 now uses a two-port certificate rotation approach for the admin config query listener. Engine nodes poll the [`/engines/rest/config-query-certificate` endpoint](../reference_guides/pa_api_endpoints.html) to retrieve new certificates and add them to the engine node's truststore.

After upgrading to PingAccess 9.1 or later:

* Consider whether you need to change the rotation window or the temporary rotation port. Learn more in the [PingAccess configuration file reference](../reference_guides/pa_config_file_ref.html#pa-cluster-config-settings) and [Port requirements](../installing_and_uninstalling_pingaccess/pa_installation_requirements.html#port-reqs).

* If using Linux, make sure any clustered PingAccess engine nodes have the write permission so they can modify the `bootstrap.properties` file. If these nodes don't have the correct file permissions, making updates to the config query listener can cause unexpected behavior.

---

---
title: Upgrade Troubleshooting
description: This table lists some potential problems and resolutions you might encounter while upgrading PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrade_troubleshooting
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrade_troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Upgrade Troubleshooting

This table lists some potential problems and resolutions you might encounter while upgrading PingAccess.

| Issue                                                                 | Resolution                                                                                                                                                                                                              |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upgrade from version 4.3 or earlier fails due to Groovy rule changes. | To verify your Groovy scripts are prepared for the upgrade, review the [Groovy development reference guide](../reference_guides/pa_groovy_in_pa.html) and the [Upgrade considerations](pa_upgrade_considerations.html). |
| Custom plugins are missing after upgrade.                             | Manually add the custom plugins to the `<PA Home>/deploy` directory.                                                                                                                                                    |

---

---
title: Upgrade utility configuration file reference
description: This configuration file reference provides an overview of configurable parameters used by the upgrade utility. These parameters are configured in the <UU_HOME>/conf/run.properties file.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrade_utility_config_file_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrade_utility_config_file_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Upgrade utility configuration file reference

This configuration file reference provides an overview of configurable parameters used by the upgrade utility. These parameters are configured in the `<UU_HOME>/conf/run.properties` file.

* pa.upgrade.source.ssl.ciphers

  Defines the type of cryptographic ciphers available for use with the source PingAccess

* pa.upgrade.source.ssl.protocols

  Defines the protocols available for use with the source PingAccess

* pa.upgrade.target.ssl.ciphers

  Defines the type of cryptographic ciphers available for use with the target PingAccess. If not specified, the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
  \<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
  \</div>)* default values are used.

* pa.upgrade.target.ssl.protocols

  Defines the protocols available for use with the target PingAccess. If not specified, the JVM default values are used.

* pa.upgrade.http.client.connection.timeout.ms

  Defines, in milliseconds, the amount of time to wait before timing out the connection to the HTTP client. The default value is 3600000.

* pa.upgrade.http.client.socket.timeout.ms

  Defines, in milliseconds, the HTTP client socket timeout. The default value is 3600000.

---

---
title: Upgrading a PingAccess cluster using the incremental update package
description: Upgrade a PingAccess cluster to a newer version using the incremental update package.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_a_pa_cluster_using_the_incremental_upgrade_package
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_a_pa_cluster_using_the_incremental_upgrade_package.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Upgrading a PingAccess cluster using the incremental update package

Upgrade a PingAccess cluster to a newer version using the incremental update package.

## Before you begin

* Make a backup copy of the PingAccess home directory. If the upgrade fails, use the backup copy to restore PingAccess.

* Review the release notes for every version between your current version and the target version.

* Verify that each node is using the same PingAccess version. You can check the version by viewing the `<PA_HOME>/lib/pingaccess-admin-ui-<version number>.jar` file.

* Verify that the PingAccess administrative node is running.

* Verify that basic authentication is configured and enabled for the running PingAccess administrative node.

* Download the PingAccess incremental update `.zip` file for the target version.

## About this task

Use the PingAccess incremental update bundle to upgrade a cluster from PingAccess 6.3 or later, the source version, to the most recent maintenance release for that version of PingAccess, the target version. For example, upgrade PingAccess 6.3 to the most recent maintenance release for 6.3.

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This upgrade procedure causes some downtime. To upgrade a cluster with no downtime, see the [Zero Downtime Upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html) guide. |

## Steps

1. Upgrade the administrative node.

   1. Extract the `.zip` file for the target version of PingAccess.

   2. Open the `readme` file included in the extracted `.zip` bundle.

   3. Make the file changes specified in the `readme` file.

2. Upgrade the replica administrative node.

   1. Extract the `.zip` file for the target version of PingAccess.

   2. Open the `readme` file included in the extracted `.zip` bundle.

   3. Make the file changes specified in the `readme` file.

3. Upgrade each engine node.

   1. Extract the `.zip` file for the target version of PingAccess.

   2. Open the `readme` file included in the extracted `.zip` bundle.

   3. Make the file changes specified in the `readme` file.

4. Shut down the entire cluster.

5. Start the upgraded administrative node.

6. Start the upgraded replica administrative node.

7. Start each upgraded engine node.

## Next steps

After you complete the upgrade, see [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).

---

---
title: Upgrading a PingAccess cluster using the upgrade utility
description: Upgrade a PingAccess cluster to a newer version.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_a_pa_cluster_using_the_upgrade_utility
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_a_pa_cluster_using_the_upgrade_utility.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  next-steps: Next steps
  pingaccess-cluster-upgrade-parameters: PingAccess cluster upgrade parameters
  parameter-definitions: Parameter definitions
  environment-variables: Environment variables
  java-virtual-machine-jvm-memory-options: Java virtual machine (JVM) memory options
  example: Example
---

# Upgrading a PingAccess cluster using the upgrade utility

Upgrade a PingAccess cluster to a newer version.

## Before you begin

* If you are using PingAccess 3.2 or earlier, upgrade to PingAccess 4.3 or 5.3 before upgrading to the latest version.

* Create a backup of your existing PingAccess configuration. If the upgrade fails, you can restore your environment from this backup.

* Review the release notes for every version between your current version and the target version.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In PingAccess 5.0 or later, there are potentially breaking changes to the Software Development Kit (SDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.\</p>&#xA;\</div>)* for Java, Groovy scripts, and the administrative SDK. For information on these changes and the actions administrators might need to take, see the [Upgrade considerations](pa_upgrade_considerations.html) and the [PingAccess 5.0](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-50.pdf#page=263) release notes. |

* Verify the following:

  * Each node is using the same PingAccess version. You can check the version by viewing the `<PA_HOME>/lib/pingaccess-admin-ui-<version number>.jar` file.

  * The PingAccess administrative node is running.

  * Basic authentication is configured and enabled for the running PingAccess administrative node.

  * You have the `.zip` bundle for the target version of PingAccess.

* Verify that you are using the same account normally used to run PingAccess.

## About this task

Use the PingAccess upgrade utility to upgrade a cluster from PingAccess 4.0 or later, the source version, to the most recent version, the target version.

|   |                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The upgrade procedure causes some downtime. To upgrade a cluster with no downtime, see the [Zero Downtime Upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html) guide. |

The upgrade utility starts an instance of PingAccess with an administrative listener on port 9001. You can change this port number using the `upgrade.bat` or `upgrade.sh` `-p` parameter. This port configuration is only used for the upgrade. The configured port is used by the upgraded server when the upgrade is complete.

Any warnings or errors encountered are recorded in `log/upgrade.log`, as well as on-screen while the utility is being run. The upgrade uses an exit code of 0 to indicate a successful upgrade and an exit code of 1 to indicate failure.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you are upgrading from version 4.3 or earlier, and your installation uses custom plugins, they must be rebuilt using the SDK version included in PingAccess 5.0 or later. Run the upgrade utility manually with the new `-i` command-line option to specify a directory containing the custom plugin JAR files and only the custom plugin JAR files. To migrate your custom plugins, see the [PingAccess Addon SDK for Java Migration Guide](../agents_and_integrations/pa_add_on_sdk_for_java_migration_guide.html). |

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | During the upgrade, do not make any changes to the running PingAccess environment. |

## Steps

1. On the administrative node, extract the `.zip` file for the target version of PingAccess.

2. Go to the new version's `/upgrade/bin` directory.

3. Run the PingAccess upgrade utility:

   ### Choose from:

   * On Windows: `upgrade.bat [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

   * On Linux: `./upgrade.sh [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

4. Review the upgrade log. If it records any manual post-upgrade tasks:

   1. Stop the source administrative console.

   2. Start the target administrative console using the `<PA_HOME>/bin/run.sh` command on Linux systems or the `<PA_HOME>\bin\run.bat` command on Windows systems.

   3. Perform any manual post-upgrade tasks recorded in the upgrade log.

   4. Shut down the upgraded administrative console.

5. Run the upgrade utility on the replica administrative node.

   ### Choose from:

   * On Windows: `upgrade.bat [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

   * On Linux: `./upgrade.sh [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

6. Run the upgrade utility on each engine node.

   ### Choose from:

   * On Windows: `upgrade.bat [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

   * On Linux: `./upgrade.sh [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

7. Shut down the entire cluster.

8. Start the upgraded administrative node.

9. Start the upgraded replica administrative node.

10. Start each upgraded engine node.

## Next steps

After you complete the upgrade, see [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).

## PingAccess cluster upgrade parameters

The command-line parameters are the same regardless of the platform, and are defined as follows.

### Parameter definitions

| Parameter                          | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -r \| --disable-config-replication | Disables configuration replication on the admin node. For more information about using this parameter in an upgrade, see the [Zero Downtime Upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html).                                                                                                                                                                                                                                                                                                                                                                |
| -p *\<admin\_port>*                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -i *\<directory>*                  | An optional directory containing additional library JAR files, such as plugins, Java Database Connectivity (JDBC) drivers to be copied into the target installation.Beginning in version 6.0, `JAR` files are stored in the `<PA HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party `JAR` files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA HOME>/deploy` folder if no directory is specified. |
| *\<sourcePingAccessRootDir>*       | The PA\_HOME for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -l *\<newPingAccessLicense>*       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -j *\<jvm\_memory\_options\_file>* | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* memory options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                                                      |
| -s \| --silent                     | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Environment variables

You can specify the username and password for the source version using these environment variables:

* `PA_SOURCE_API_USERNAME` – The username for the source version's Admin API. This should be set to Administrator.

* `PA_SOURCE_API_PASSWORD` – The basic authorization password for the Administrator in the source version's Admin API.

### Java virtual machine (JVM) memory options

These options can be included in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

* `-Xms<amount>` – Minimum heap size.

* `-Xmx<amount>` – Maximum heap size.

* `-XX:NewSize=<amount>` – Minimum size for the Young Gen space.

* `-XX:MaxNewSize=<amount>` – Maximum size for the Young Gen space.

* `-XX:+UseParallelGC` – Specifies that the parallel garbage collector should be used.

You can copy the existing `<PA_HOME>/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

### Example

```
#Sample JVM Memory options file
-Xms512m
-Xmx1g
-XX:NewSize=256m
-XX:MaxNewSize=512m
-XX:+UseParallelGC
```

---

---
title: Upgrading a PingAccess standalone version using the incremental update package
description: Upgrade a standalone PingAccess deployment to a newer version using the incremental update package.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_a_pa_standalone_version_using_the_incremental_update_package
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_a_pa_standalone_version_using_the_incremental_update_package.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Upgrading a PingAccess standalone version using the incremental update package

Upgrade a standalone PingAccess deployment to a newer version using the incremental update package.

## Before you begin

* Make a backup copy of the PingAccess home directory. If the upgrade fails, use the backup copy to restore PingAccess.

* Review the release notes for every version between your current version and the target version.

* Verify that you have the following:

  * The PingAccess incremental update `.zip` file for the target version

  * Administrator credentials for the running PingAccess instance

* Verify that basic authentication is configured and enabled for the running PingAccess instance.

* Verify that the PingAccess host is running.

## About this task

Use the PingAccess incremental update bundle to upgrade from PingAccess 6.3 or later, the source version, to the most recent maintenance release for that version of PingAccess, the target version. For example, upgrade PingAccess 6.3 to the most recent maintenance release for 6.3.

## Steps

1. Stop PingAccess.

2. Open the `readme` file included in the extracted `.zip` bundle.

3. Make the file changes specified in the `readme` file.

4. Restart PingAccess.

## Next steps

After you complete the upgrade, see [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).

---

---
title: Upgrading a PingAccess standalone version using the upgrade utility
description: Upgrade a standalone PingAccess deployment to a newer version.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_a_pa_standalone_version_using_the_upgrade_utility
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_a_pa_standalone_version_using_the_upgrade_utility.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  example: Example:
  next-steps: Next steps
  pingaccess-standalone-upgrade-parameters: PingAccess standalone upgrade parameters
  environment-variables: Environment variables
  java-virtual-machine-jvm-memory-options: Java virtual machine (JVM) memory options
  example-2: Example
---

# Upgrading a PingAccess standalone version using the upgrade utility

Upgrade a standalone PingAccess deployment to a newer version.

## Before you begin

* If you are using PingAccess 3.2 or earlier, upgrade to PingAccess 4.3 or 5.3 before upgrading to the current version of PingAccess.

* Create a backup of your existing PingAccess configuration. If the upgrade fails, restore your environment from this backup.

* Review the release notes for every version between your current version and the target version.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In release 5.0, there are potentially breaking changes to the Software Development Kit (SDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A set of tools that allows a developer to build a custom application that integrates with or connects to a platform or service.\</p>&#xA;\</div>)* for Java, Groovy scripts, and the administrative application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*. For information on these changes and the actions administrators might need to take, review the [Upgrade considerations](pa_upgrade_considerations.html) and the [PingAccess 5.0](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-50.pdf#page=263) release notes. |

* Verify that you have the following:

  * The PingAccess distribution `.zip` file

  * Your new PingAccess license file, if you plan to switch to a new license file

  * Sign on access to the PingAccess host, as the utility is run on the host

  * Administrator credentials for the running PingAccess instance

* Verify that basic authentication is configured and enabled for the running PingAccess instance.

* Verify that the PingAccess host is running.

* Verify that you are using the same account normally used to run PingAccess.

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you have set `security.overridePropertiesFile=false` in `$JAVA_HOME/jre/lib/java.security`, the upgrade utility might fail because the PingAccess upgrade utility uses an override to enable deprecated ciphers and protocols during the upgrade process. |

## About this task

Use the PingAccess upgrade utility to upgrade from PingAccess 4.0 or later, the source version, to the most recent version, the target version.

The upgrade utility starts an instance of PingAccess with an administrative listener on port 9001. This port number can be changed using the `upgrade.bat` or `upgrade.sh` `-p` parameter. This port configuration is only used for the upgrade. The configured port is used by the upgraded server when the upgrade is complete.

Any warnings or errors encountered are recorded in `log/upgrade.log`, as well as on-screen while the utility is being run. The upgrade uses an exit code of 0 to indicate a successful upgrade and an exit code of 1 to indicate failure.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you are upgrading from version 4.3 or earlier, and your installation uses custom plugins, they must be rebuilt using the SDK version included in PingAccess 5.0 or later. Run the upgrade utility manually with the new `-i` command-line option to specify a directory containing the custom plugin JAR files and only the custom plugin JAR files. To migrate your custom plugins, see the [PingAccess Addon SDK for Java Migration Guide](../agents_and_integrations/pa_add_on_sdk_for_java_migration_guide.html). |

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | During the upgrade, do not make any changes to the running PingAccess environment. |

## Steps

1. Copy the `.zip` file for the new PingAccess version to the PingAccess host and extract it.

2. Change to the new version's `/upgrade/bin` directory.

3. Run the PingAccess upgrade utility:

   ### Choose from:

   * On Windows: `upgrade.bat [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

   * On Linux: `./upgrade.sh [-p <admin_port>] [-i <directory>] [-j <jvm_memory_options_file>] [-l <newPingAccessLicense>] [-s | --silent] <sourcePingAccessRootDir>`

     ### Example:

     For example: `./upgrade.sh -p 9002 -i MyJARDir pingaccess-5.3`

## Next steps

After you complete the upgrade, see [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).

## PingAccess standalone upgrade parameters

The command-line parameters are the same regardless of the platform and are defined in the following table.

| Parameter                          | Value description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -p *\<admin\_port>*                | Optional port to be used by the temporary PingAccess instance run during the upgrade. The default is 9001.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -i *\<directory>*                  | An optional directory containing additional library JAR files, such as plugins and Java Database Connectivity (JDBC) drivers, to be copied into the target installation.Beginning in version 6.0, JAR files are stored in the `<PA HOME>/deploy` folder.During an upgrade from versions earlier than 6.0, third-party JAR files are migrated from the `lib` folder to the `deploy` folder if no directory is specified.During an upgrade from version 6.0 or later, the contents of the `deploy` folder are migrated to the new `<PA HOME>/deploy` folder if no directory is specified. |
| *\<sourcePingAccessRootDir>*       | The `PA_HOME` for the source PingAccess version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -l *\<newPingAccessLicense>*       | An optional path to the PingAccess license file to use for the target version. If not specified, the existing license is reused.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -j *\<jvm\_memory\_options\_file>* | An optional path to a file with Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* options to use for the new PingAccess instance during the upgrade.                                                                                                                                                                                                                                                                             |
| -s \| --silent                     | Run the upgrade with no user input required. To use this option, specify the source version's credentials using environment variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Environment variables

You can specify the username and password for the source version using these environment variables:

* `PA_SOURCE_API_USERNAME` – The username for the source version's Admin API. This should be set to Administrator.

* `PA_SOURCE_API_PASSWORD` – The basic authorization password for the Administrator in the source version's Admin API.

### Java virtual machine (JVM) memory options

You can include these options in the JVM memory options file. Memory amounts use `m` or `g` to specify the unit.

* `-Xms<amount>` – Minimum heap size

* `-Xmx<amount>` – Maximum heap size

* `-XX:NewSize=<amount>` – Minimum size for the Young Gen space

* `-XX:MaxNewSize=<amount>` – Maximum size for the Young Gen space

* `-XX:+UseParallelGC` – Specifies that the parallel garbage collector should be used

You can copy the existing `<PA_HOME>/conf/jvm-memory.options` file to create a JVM memory options file for the upgrade.

### Example

```
#Sample JVM Memory options file
-Xms512m
-Xmx1g
-XX:NewSize=256m
-XX:MaxNewSize=512m
-XX:+UseParallelGC
```

---

---
title: Upgrading PingAccess
description: Learn how to upgrade your PingAccess server to a more recent target version.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_pa_landing_topic
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_pa_landing_topic.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 11, 2026
---

# Upgrading PingAccess

Learn how to upgrade your PingAccess server to a more recent target version. After reviewing the [Upgrade considerations](pa_upgrade_considerations.html), complete the procedure relevant to your environment:

* [Upgrading a PingAccess standalone version using the upgrade utility](pa_upgrading_a_pa_standalone_version_using_the_upgrade_utility.html)

* [Upgrading a PingAccess cluster using the upgrade utility](pa_upgrading_a_pa_cluster_using_the_upgrade_utility.html)

* [Upgrading PingAccess using the Windows installer](pa_upgrading_pa_using_the_windows_installer.html)

* [Upgrading a PingAccess standalone version using the incremental update package](pa_upgrading_a_pa_standalone_version_using_the_incremental_update_package.html)

* [Upgrading a PingAccess cluster using the incremental update package](pa_upgrading_a_pa_cluster_using_the_incremental_upgrade_package.html)

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have a clustered environment and want to upgrade PingAccess without impacting resource availability, learn more in [PingAccess zero downtime upgrade](../pingaccess_zero_downtime_upgrade/pa_zero_downtime_upgrade.html). |

You can find more information about what to do during or after your upgrade in:

* [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html)

* [Restoring a PingAccess configuration backup](pa_restoring_a_pa_configuration_backup.html)

* [Upgrade Troubleshooting](pa_upgrade_troubleshooting.html)

* [Upgrade utility configuration file reference](pa_upgrade_utility_config_file_ref.html)

---

---
title: Upgrading PingAccess using the Windows installer
description: Upgrade PingAccess if you installed PingAccess using the Windows installer.
component: pingaccess
version: 9.1
page_id: pingaccess:upgrading_pingaccess:pa_upgrading_pa_using_the_windows_installer
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/upgrading_pingaccess/pa_upgrading_pa_using_the_windows_installer.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Upgrading PingAccess using the Windows installer

Upgrade PingAccess if you installed PingAccess using the Windows installer.

## Before you begin

* If you are using PingAccess 3.2 or earlier, you must upgrade to PingAccess 4.3 or 5.3 before upgrading to PingAccess 6.0.

* Review the [Upgrade considerations](pa_upgrade_considerations.html).

## About this task

|   |                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If additional JAR files, such as custom plugins and Java database connectivity (JDBC) drivers, have been added to the existing PingAccess `/lib` directory, the 5.0-Beta installer cannot be used to perform the upgrade. Instead, run the upgrade utility manually, using the `-i` command-line option to specify the JAR files to be included. |

## Steps

1. Download the installer.

2. Start the installer.

   ### Result:

   The existing installation is detected.

3. To upgrade the installation, click **Yes**.

4. If you are switching to a new license, select a license file and specify a temporary admin port.

   |   |                                                                         |
   | - | ----------------------------------------------------------------------- |
   |   | The temporary admin port is not required when upgrading a cluster node. |

5. Click **Next**.

6. Specify the administrator credentials. Click **Next**.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | Administrator credentials are not required when upgrading a cluster node. |

7. Click **Finish**.

## Next steps

After completing the upgrade, [Performing post-upgrade tasks](pa_performing_post_upgrade_tasks.html).