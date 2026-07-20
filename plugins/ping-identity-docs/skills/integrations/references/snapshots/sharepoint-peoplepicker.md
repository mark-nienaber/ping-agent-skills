---
title: Activate features
description: Login to your SharePoint Central Administration site.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_activate_features
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_activate_features.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Activate features

## Steps

1. Login to your SharePoint Central Administration site.

2. Go to **Central Administration > System Settings > Manage farm features**.

3. Activate the **Ping Identity People Picker Claims Provider** feature if it is not already active:

   ![screen capture of manage farm features](_images/sdt1563995682130.jpg)

   |   |                                                                    |
   | - | ------------------------------------------------------------------ |
   |   | Activating the feature registers the claim provider in SharePoint. |

4. Click on the gear icon on the top right corner of the Central Admin site.

5. Click on **Site Settings > Site Actions > Manage site features**.

6. Activate the **Ping Identity People Picker Claims Administration** feature:

   ![screen capture of site features](_images/kyi1563995682901.jpg)

---

---
title: Add and deploy the solution
description: Download the SharePoint People Picker Integration Kit .zip archive from the Add-ons tab of the PingFederate downloads page or the Ping Identity Marketplace.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_add_and_deploy_the_solution
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_add_and_deploy_the_solution.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Add and deploy the solution

## Steps

1. Download the SharePoint People Picker Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/sharepoint-people-picker).

2. Extract the SharePoint People Picker Integration Kit distribution file, and then go to `dist/sharepoint<yourversion>`.

3. Copy the solution (WSP) file to the SharePoint server.

4. Open the SharePoint Management Shell (PowerShell) as Administrator and use the `Add- SPSolution` command to add the solution to the farm:

   ```
   Add-SPSolution -LiteralPath
   C:\path\PingIdentity.SharePoint.PPClaimsProvider.wsp
   ```

5. Deploy the solution using Central Administrator using the `Install-SPSolution` command:

   ```
   Install-SPSolution PingIdentity.SharePoint.PPClaimsProvider.wsp
   -GACDeployment
   ```

---

---
title: Assumptions and prerequisites
description: This document assumes:
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker::pf_sharepoint_peoplepicker_ik_assumptions_and_prerequisites
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/pf_sharepoint_peoplepicker_ik_assumptions_and_prerequisites.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
---

# Assumptions and prerequisites

This document assumes:

* A Trusted Identity Token Issuer, referred to hereon as the Partner STS, has been created and enabled as an Authentication Provider for at least one SharePoint web application.

* SAML token-based authentication has been successfully tested for the SharePoint web application using the Partner STS.

* The Partner STS is configured to send the user identity claim type that will be used by SharePoint (for example, http\://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn).

  |   |                                                                                                                                                                                                                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Make note of the name of the Partner STS. You will need it when associating the Custom Claims Provider with the Partner STS. You can view all Trusted Identity Token Issuers and their names by executing the following command from the Management Shell: *Get-SPTrustedIdentityTokenIssuer* and looking at the *Name* attribute. |

* Connectivity and trust (for LDAPS connections) exists to all domain controllers that are to be searched.

* A provisioned service account with read access for each domain controller to be searched is available.

* The SharePoint Administration service must be running prior to installing the solution (.wsp) file.

---

---
title: Changelog
description: Added support for SharePoint Server Subscription Edition.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:release_notes:pf_sharepoint_peoplepicker_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/release_notes/pf_sharepoint_peoplepicker_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
section_ids:
  sharepoint-people-picker-integration-kit-1-5-june-2026: SharePoint People Picker Integration Kit 1.5 - June 2026
  sharepoint-people-picker-integration-kit-1-4-december-2020: SharePoint People Picker Integration Kit 1.4 – December 2020
  sharepoint-people-picker-integration-kit-1-3-february-2019: SharePoint People Picker Integration Kit 1.3 – February 2019
  sharepoint-people-picker-integration-kit-1-2-1-july-2018: SharePoint People Picker Integration Kit 1.2.1 – July 2018
  sharepoint-people-picker-integration-kit-1-2-may-2017: SharePoint People Picker Integration Kit 1.2 – May 2017
  sharepoint-2013-people-picker-extension-integration-kit-1-1-september-2016: SharePoint 2013 People Picker Extension Integration Kit 1.1 – September 2016
  sharepoint-2013-people-picker-extension-1-0-1-integration-kit-august-2016: SharePoint 2013 People Picker Extension 1.0.1 Integration Kit – August 2016
  sharepoint-2013-people-picker-extension-1-0-integration-kit-feb-2016: SharePoint 2013 People Picker Extension 1.0 Integration Kit – Feb 2016
---

# Changelog

## SharePoint People Picker Integration Kit 1.5 - June 2026

* Added support for SharePoint Server Subscription Edition.

* Removed support for SharePoint 2013.

  Microsoft ended Extended Support for Sharepoint 2013 in April 2023, the `sharepoint2013` artifacts are no longer included in the release package.

* Fixed a defect in the SharePoint 2016 and SharePoint 2019 builds where a SharePoint update released after version 1.4 caused solution installation to fail.

## SharePoint People Picker Integration Kit 1.4 – December 2020

* Added support for selecting an authentication type for each LDAP connection.

* Added support for SharePoint 2013.

## SharePoint People Picker Integration Kit 1.3 – February 2019

* Added support for SharePoint 2019.

## SharePoint People Picker Integration Kit 1.2.1 – July 2018

* Addressed feature activation failures due to logging and null configuration reference.

## SharePoint People Picker Integration Kit 1.2 – May 2017

* Resolved issue when the Ping Identity Custom Claims Provider is enabled for a Trusted Identity Provider in the Intranet Zone.

* Added support for secure storage of LDAP credentials.

* Resolved issue when searching for group names that contain brackets.

* Security fixes.

## SharePoint 2013 People Picker Extension Integration Kit 1.1 – September 2016

* Added ability to specify a custom LDAP filter to find users and groups.

## SharePoint 2013 People Picker Extension 1.0.1 Integration Kit – August 2016

* SharePoint People Picker can now be used alongside the Windows NTLM Claim Picker.

## SharePoint 2013 People Picker Extension 1.0 Integration Kit – Feb 2016

* Initial Release.

---

---
title: Configuration
description: Use the following sections to configure the solution.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_configuration
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_configuration.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Configuration

Use the following sections to configure the solution.

* [People Picker configuration](pf_sharepoint_peoplepicker_ik_people_picker_configuration.html)

* [Configuration storage](pf_sharepoint_peoplepicker_ik_configuration_storage.html)

---

---
title: Configuration storage
description: "Configuration settings are stored in the web application properties collection with the key \"PingClaimsProviderConfig\". The configuration is stored in JSON format in plain text (unencrypted)."
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_configuration_storage
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_configuration_storage.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuration storage

## About this task

Configuration settings are stored in the web application properties collection with the key "PingClaimsProviderConfig". The configuration is stored in JSON format in plain text (unencrypted).

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | If using the *Secure Store Application Id* feature, the credentials will be encrypted (see below). |

```shell
$webApp = Get-SPWebApplication <web app URL>\$webApp.Properties["PingClaimsProviderConfig"]\
```

**Secure Storage Configuration**

Configuring a Secure Store Target Application encrypts the credentials necessary for the LDAP query used in the People Picker. To set up a Secure Store Target Application for the Ping Identity People Picker, use the following steps.

## Steps

1. Create a new **Secure Store Target Application** and populate: **Target Application ID**, **Display Name**, and **Contact E-mail**. Use *Group* for the **Target Application Type**. Click **Next**.

   ![screen capture of target application settings](_images/iux1563995689380.png)

2. Use the field types *Username* and *Password* for the **User Name** and **Password** fields, respectively. Click **Next**.

   ![screen capture of username and password fields](_images/uwy1563995691267.png)

3. Select an account to administer the application in the **Target Application Administrators** field. In the **Members** field, enter a list of users who will have access the target application. Click **OK** to complete the setup.

   ![screen capture of target application administrators field](_images/zau1563995692146.png)

---

---
title: Diagnostic logging
description: Verbose tracing can be enabled for the Ping Identity People Picker on the Diagnostic Logging page of the Monitoring section in Central Administration.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:troubleshooting:pf_sharepoint_peoplepicker_ik_diagnostic_logging
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/troubleshooting/pf_sharepoint_peoplepicker_ik_diagnostic_logging.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
---

# Diagnostic logging

Verbose tracing can be enabled for the Ping Identity People Picker on the Diagnostic Logging page of the Monitoring section in Central Administration.

1. Go to **Central Administration > Monitoring > Reporting > Configure diagnostic logging**.

2. Select the Custom Claims category.

   ![sez1563995695463](_images/sez1563995695463.jpg)

3. (Optional) Select SharePoint Foundation >> Monitoring to enable monitored scopes that will show LDAP queries.

   ![jmh1563995696210](_images/jmh1563995696210.jpg)

4. Select Verbose as the least critical event to report to the trace log.

   ![tfz1563995696886](_images/tfz1563995696886.jpg)

5. The default log directory is similar to `C:\Program Files\Common Files\Microsoft Shared\Web Server Extensions\15\LOGS` for older SharePoint Server versions.

   The default log directory is similar to `C:\Program Files\Common Files\Microsoft Shared\Web Server Extensions\16\LOGS\` for Sharepoint Server Subscription Edition.

6. If the SharePoint admin has changed the default log path, you can find it by going to **Central Admin > Monitoring > Reporting > Configure diagnostic logging**. Scroll down to Trace Log - the Path configured here is where your Sharepoint logs are being stored.

7. Use the ULS Viewer app to monitor the ULS logs. You can use the following filters to see just the output from the custom claims provider.

   ![nga1563995697459](_images/nga1563995697459.jpg)

You can download the ULS Viewer tool from Microsoft here: <https://www.microsoft.com/en-us/download/details.aspx?id=44020>

---

---
title: Download manifest
description: The distribution .zip archive for the SharePoint People Picker Integration Kit contains the following:
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:release_notes:pf_sharepoint_peoplepicker_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/release_notes/pf_sharepoint_peoplepicker_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
---

# Download manifest

The distribution `.zip` archive for the SharePoint People Picker Integration Kit contains the following:

* `ReadMeFirst.pdf`– contains links to this online documentation.

* `/dist`

  * `sharepoint-server-subscription-edition/PingIdentity.SharePoint.PPClaimsProvider.wsp` - SharePoint People Picker solution for SharePoint Server Subscription Edition

  * `sharepoint2016/PingIdentity.SharePoint.PPClaimsProvider.wsp` – SharePoint People Picker solution for SharePoint Server 2016

  * `sharepoint2019/PingIdentity.SharePoint.PPClaimsProvider.wsp` – SharePoint People Picker solution for SharePoint Server 2019

* `Legal.pdf`: Copyright and license information.

---

---
title: Installation and setup
description: Use the following sections for instructions to install the solution.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_installation_and_setup
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_installation_and_setup.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Installation and setup

Use the following sections for instructions to install the solution.

* [Upgrade from a previous version](pf_sharepoint_peoplepicker_ik_upgrade_from_a_previous_version.html)

* [Add and deploy the solution](pf_sharepoint_peoplepicker_ik_add_and_deploy_the_solution.html)

* [Activate features](pf_sharepoint_peoplepicker_ik_activate_features.html)

* [Set the default claims provider](pf_sharepoint_peoplepicker_ik_set_the_default_claims_provider.html)

---

---
title: Known issues and limitations
description: None.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:release_notes:pf_sharepoint_peoplepicker_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/release_notes/pf_sharepoint_peoplepicker_ik_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Known issues and limitations

* None.

---

---
title: People Picker configuration
description: Sign on to your SharePoint Central Administration site.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_people_picker_configuration
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_people_picker_configuration.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
section_ids:
  steps: Steps
---

# People Picker configuration

## Steps

1. Sign on to your SharePoint Central Administration site.

2. Go to **Central Administration > Security**.

3. Click **Configure People Picker** (under **Users**):

   ![A screen capture of the SharePoint Security menu](_images/pf_sharepoint_people_picker_security.png)

4. Select the web application that's configured to use the Partner STS (Trusted Identity Provider) for authentication from the list at the top of the page):

   ![A screen capture of the SharePoint configuration menu showing how to change the Web Application](_images/pf_sharepoint_people_picker_config_web_app.png)

5. Configure the Claim Settings by selecting the Partner STS and specifying the Identity Claim Type.

   * Identity Claim Type examples

     `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`

     `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn`

6. Add Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* connections by selecting **Add a new connection…** in the **LDAP Connection** list, then fill out the LDAP connection settings as described in the following table:

   ![A screen capture of the SharePoint configuration menu showing LDAP settings](_images/pf_sharepoint_people_picker_config_ldap_connections.png)

| Field                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                | The name of this LDAP connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Server**                              | The FQDN or IP address for the LDAP server. If using LDAPS, include the relevant port (for example, `ldap.domain.com:636`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Secure Store App Id**                 | The ID of your saved credentials in SharePoint's Secure Store Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Username**                            | The username of the LDAP account that will be used to bind to LDAP to query users or groups. If the Username field is left blank the LDAP query will be made using the SharePoint farm account.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Password**                            | The password for the LDAP account.&#xA;&#xA;Passwords are stored in plain text with the other configuration data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Search Root**                         | The root (BaseDN) for the LDAP search.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Identity Attribute**                  | The Identity Attribute refers to the LDAP attribute used to populate the **Identity Claim Type** (which you selected in the **Claim Settings** at the top of the page). The LDAP attribute configured here must match the LDAP attribute used in PingFederate to populate that WS-Fed attribute.For example, an Identity Attribute of `userPrincipalName` has an Identity Claim Type of `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn`                                                                                                                                                                                    |
| **Group Identifier**                    | Select either **SID** or **Distinguished Name (DN)** to be used as the group unique identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **DisplayName Attribute**               | LDAP attribute used to display user-friendly names in People Picker, such as `displayName` or `givenName`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Server Time Limit (seconds)**         | The maximum number of seconds that the server waits for a search to complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Client Timeout (seconds)**            | The maximum number of seconds that the client waits for the server to return results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Maximum number of objects to return** | This refers to the maximum number of search results you want the People Picker to return.You can set this to a number between 0 and 500. If you set this to 0, it uses the SharePoint default size limit of 1000 entries.                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Minimum characters to start search**  | This refers to the minimum number of characters (letters) an end user must type into the People Picker search window before the search starts to execute.You can set this to a number between 4 and 10. If you set this to 0, it uses the SharePoint default setting of 3 characters.&#xA;&#xA;Each LDAP connection you add here will only be enabled for the specific SharePoint web application you selected. If you want to add the same LDAP connection to multiple SharePoint web applications, you need to repeat the same configuration steps (4-5-6) for each SharePoint web application.                                      |
| **Filter to be used for search**        | Provide a custom LDAP query to be used for search. Leave this property blank to use the default query:`"(&(&(\|(objectCategory=person)(groupType=-2147483646))(\|(displayName={0}*)(sAMAccountName={0}*)(userPrincipalName={0}*)(cn={0}*)(mail={0}*))))"`                                                                                                                                                                                                                                                                                                                                                                              |
| **Authentication Type**                 | Specifies the authentication mechanism used when connecting to the LDAP server. This corresponds to the `System.DirectoryServices.AuthenticationTypes` enumeration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Include Secure Flag**                 | When selected, the Secure flag is applied in addition to the selected authentication type. This instructs the underlying Windows security provider to negotiate the most secure available authentication mechanism (typically Kerberos or NTLM).Enable this option when connecting over LDAPS (port 636) or when the directory server requires authenticated binds.&#xA;&#xA;If Encrypt Connection using SSL/TLS is also enabled and the connection isn't configured for trusted (pass-through) authentication, the Secure flag is automatically stripped to avoid incompatibility between Kerberos and explicit credentials over SSL. |
| **Encrypt Connection**                  | When selected, the connection to the LDAP server is encrypted using SSL/TLS by applying the SecureSocketLayer authentication flag.Use this option when the LDAP server is configured to accept SSL connections (typically on port 636). Before enabling this option, ensure that:- The LDAP server's certificate is trusted by the SharePoint server.

- The LDAP server's port configured above matches the server's SSL listener port.                                                                                                                                                                                               |

---

---
title: Search by group
description: The following image is an example of a successful search for a group by the group's name (cn, sAMAccountName):
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_search_by_group
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_search_by_group.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
section_ids:
  about-this-task: About this task
---

# Search by group

## About this task

The following image is an example of a successful search for a group by the group's name (cn, sAMAccountName):

![Screen capture of a search for group by group name](_images/pf_sharepoint_people_picker_group_search.png)

The following image is the corresponding log entry for the successful search:

![Screen capture of the log entry for the previous search](_images/pf_sharepoint_people_picker_group_search_log.png)

---

---
title: Search by user
description: The following image is an example of a successful search for a user by username (sAMAccountName):
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_search_by_user
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_search_by_user.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
section_ids:
  about-this-task: About this task
---

# Search by user

## About this task

The following image is an example of a successful search for a user by username (sAMAccountName):

![Screen capture of a search by username](_images/pf_sharepoint_people_picker_user_search.png)

The following image is the corresponding log entry for the successful search:

![Screen capture of the log entry for the previous search](_images/pf_sharepoint_people_picker_user_search_log.png)

---

---
title: Set the default claims provider
description: Once the claims provider is installed and activated you can set it as the default claims provider for your PingFederate Partner STS by doing the following:
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_set_the_default_claims_provider
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_set_the_default_claims_provider.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Set the default claims provider

## About this task

Once the claims provider is installed and activated you can set it as the default claims provider for your PingFederate Partner STS by doing the following:

## Steps

1. Open SharePoint Management Shell as an Administrator.

2. Execute each command listed below.

   ```shell
   $ti = Get-SPTrustedIdentityTokenIssuer "<Partner STS Name>"
   $ti.ClaimProviderName = "PingIdentityPeoplePickerProvider"
   $ti.Update()
   ```

   Replace "*\<PartnerSTSName>*" with the name of your configured Trusted Identity Token Issuer.

---

---
title: SharePoint log location
description: "The default log directory is: C:\\Program Files\\Common Files\\Microsoft Shared\\Web Server Extensions[.varname]_<version>_\\LOGS."
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:troubleshooting:pf_sharepoint_peoplepicker_ik_sharepoint_log_location
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/troubleshooting/pf_sharepoint_peoplepicker_ik_sharepoint_log_location.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# SharePoint log location

The default log directory is: `C:\Program Files\Common Files\Microsoft Shared\Web Server Extensions[.varname]_<version>_\LOGS`.

If the SharePoint administrator has changed the default log path, you can find it by going to **Central Admin > Monitoring Reporting > Configure diagnostic logging** scroll down to Trace Log - the Path configured here is where your Sharepoint Logs are being stored.

---

---
title: SharePoint People Picker Integration Kit
description: The People Picker control is a central component in Microsoft SharePoint Server that is used to search and select users and groups when a resource owner assigns permissions. By default, when a SharePoint web application is configured to use SAML token-based authentication or "SAML claims", all queries entered in the People Picker are automatically displayed as if they had been resolved, regardless of whether they are valid users or groups. This poses a significant usability problem for SharePoint users and administrators, particularly in collaboration-oriented deployments where potentially every user has the ability to edit file and library permissions using the People Picker.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker::pf_sharepoint_peoplepicker_ik
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/pf_sharepoint_peoplepicker_ik.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# SharePoint People Picker Integration Kit

The People Picker control is a central component in Microsoft SharePoint Server that is used to search and select users and groups when a resource owner assigns permissions. By default, when a SharePoint web application is configured to use SAML token-based authentication or "SAML claims", all queries entered in the People Picker are automatically displayed as if they had been resolved, regardless of whether they are valid users or groups. This poses a significant usability problem for SharePoint users and administrators, particularly in collaboration-oriented deployments where potentially every user has the ability to edit file and library permissions using the People Picker.

To address this issue, Microsoft recommends you build a custom claims provider to provide capabilities for custom search and name resolution. The Ping Identity Custom Claims Provider for SharePoint is an implementation capable of connecting to one or more LDAP user stores or domains to fulfill search and name resolution queries.

When this custom claims provider is associated with a Trusted Login Provider (referred to in the Management Shell as a Trusted Identity Token Issuer) in SharePoint, such as might be configured to accept inbound SAML claims from PingFederate for one or more SharePoint web applications, the People Picker will provide functionality similar to that seen with classic-mode authentication where users and groups in Active Directory are available for search, name resolution, and attribute listing.

---

---
title: Supported search attributes with examples
description: The solution by default enables search on the following LDAP attributes:
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_supported_search_attributes_with_examples
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_supported_search_attributes_with_examples.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Supported search attributes with examples

The solution by default enables search on the following LDAP attributes:

* cn

* displayName

* mail

* sAMAccountName

* userPrincipalName

---

---
title: System requirements
description: This version of the Ping Identity Custom Claims Provider for SharePoint requires the following:
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker::pf_sharepoint_peoplepicker_ik_system_requirements
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/pf_sharepoint_peoplepicker_ik_system_requirements.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
---

# System requirements

This version of the Ping Identity Custom Claims Provider for SharePoint requires the following:

* Microsoft SharePoint Server 2016, 2019, or Subscription Edition configured with PingFederate as the Trusted Identity Token Issuer.

* Connectivity to one or more backing LDAP user stores. Testing has been performed on Microsoft Active Directory 2016 and Microsoft Active Directory on Windows Server 2022.

|   |                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Microsoft has announced the end of extended support for [SharePoint Server 2016](https://learn.microsoft.com/en-us/lifecycle/products/sharepoint-server-2016) and [SharePoint Server 2019](https://learn.microsoft.com/en-us/lifecycle/products/sharepoint-server-2019) on July 14, 2026. |

---

---
title: Uninstall the solution
description: In Central Administration disable the Trusted Identity provider from the web application.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:troubleshooting:pf_sharepoint_peoplepicker_ik_uninstall_the_solution
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/troubleshooting/pf_sharepoint_peoplepicker_ik_uninstall_the_solution.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
section_ids:
  steps: Steps
---

# Uninstall the solution

## Steps

1. In Central Administration disable the Trusted Identity provider from the web application.

   This step must be completed for each web application that is using that Trusted Identity provider (also known as the Partner STS or Trusted Identity Token Issuer).

![qsz1563995703178](_images/qsz1563995703178.jpg)

1. In **Central Administration > System Settings > Farm Features** deactivate the Ping Identity People Picker Claims Provider farm feature.

   ![qzl1563995704583](_images/qzl1563995704583.jpg)

2. In **Central Administration > Site Settings > Site Features** deactivate the Ping Identity People Picker Claims Administration site feature.

   ![sok1563995705092](_images/sok1563995705092.jpg)

3. In **Central Administration > System Settings > Farm Solutions** retract the pingidentity.sharepoint.ppclaimsprovider.wsp solution.

   ![awz1563995705587](_images/awz1563995705587.jpg)

4. In **Central Administration > System Settings > Farm Solutions** retract the pingidentity.sharepoint.ppclaimsprovider.wsp solution.

   |   |                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------- |
   |   | During retraction, schedule 10 minutes to prevent timer issues that sometimes occur in SharePoint. |

   ![afs1563995706306](_images/afs1563995706306.jpg)

5. Open SharePoint Management Shell as an Administrator.

6. Make a backup copy of your configuration settings for your existing Trusted Identity Token Issuer. For example: use this command tor produce a file called partnersts.txt that contains your list of token issuers and their settings:

   ```
   Get-SPTrustedIdentityTokenIssuer >partnersts.txt
   ```

7. Use this command to delete your current Trusted Identity Token Issuer:

   ```
   Remove-SPTrustedIdentityTokenIssuer –Identity "<PartnerSTS>"
   ```

   Replace `<PartnerSTS>` with the Name of your Trusted Identity Token Issuer.

8. User PowerShell to recreate your SP Trusted Identity Token Issuer (without setting the default claims provider). You can refer to the partnersts.txt to review what settings you used previously.

9. In Central Administration reconfigure the web application to use the newly created SPTrustedIdentityTokenIssuer.

10. (Optional) For a complete cleanup, you may also wish to remove the People Picker configuration settings that were stored for each web application that you configured to use the People Picker. This can be done by running the following commands via the SharePoint Management Shell for each web application:

    * Identify the web application by replacing `<web app URL>` with the SharePoint Web Application's URL:

      ```shell
      $webApp = Get-SPWebApplication <web app URL>
      ```

    * To view the settings associated for the web application:

      ```shell
      $webApp.Properties["PingClaimsProviderConfig"]
      ```

    * To remove the settings associated for the web application:

      ```shell
      $webApp.Properties.Remove("PingClaimsProviderConfig")
      $webApp.Update()
      ```

---

---
title: Upgrade from a previous version
description: Use Update-SPSolution in a Sharepoint Management Shell to upgrade to a newer version:
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_upgrade_from_a_previous_version
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_upgrade_from_a_previous_version.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Upgrade from a previous version

Use Update-SPSolution in a Sharepoint Management Shell to upgrade to a newer version:

```
Update-SPSolution -Identity pingidentity.sharepoint.ppclaimsprovider.wsp
     -LiteralPath "C:\path_to_solution\PingIdentity.SharePoint.PPClaimsProvider.wsp"
     –GacDeployment
```

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | The remaining steps of the Installation and Setup section are not required when upgrading. |