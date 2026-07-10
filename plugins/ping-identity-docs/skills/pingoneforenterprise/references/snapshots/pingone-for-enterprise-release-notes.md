---
title: PingOne for Enterprise Release Notes
description: New features and improvements in PingOne for Enterprise, PingOne for Enterprise for Managed Service Providers, PingOne SSO for SaaS Apps, PingOne SSO for SaaS Apps with Managed Accounts, and AD Connect.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_release_notes:p14e_release_notes
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_release_notes/p14e_release_notes.html
revdate: December 26, 2025
section_ids:
  may-2025: May 2025
  users-tab-restored-after-migrating-pingid: Users tab restored after migrating PingID
  february-2025: February 2025
  filter-users-by-service-search: Filter Users by Service search
  january-2025: January 2025
  users-tab-remains-after-pingid-integration-with-pingone: Users tab remains after PingID integration with PingOne
  sub-tenant-admin-access-lock: Sub-tenant admin access lock
  october-2024: October 2024
  aws-iam-identity-center-provisioner: AWS IAM Identity Center Provisioner
  pingone-connector: PingOne Connector
  may-2024: May 2024
  scim-saas-provisioner: SCIM SaaS Provisioner
  pingone-connector-2: PingOne Connector
  march-2024: March 2024
  country-data-for-sso-report: Country data for SSO report
  november-2023: November 2023
  servicenow-connector-2-3: ServiceNow Connector 2.3
  july-2023: July 2023
  webex-connector-2-3-0: Webex Connector 2.3.0
  zoom-connector-1-3-3: Zoom Connector 1.3.3
  may-2023: May 2023
  manual-pingone-for-enterprise-connections: Manual PingOne for Enterprise connections
  april-2023: April 2023
  users-by-service-search: Users by Service search
  servicenow-tokyo: ServiceNow Tokyo
  march-2023: March 2023
  email-communications: Email communications
  february-2023: February 2023
  pingid-license-management-for-customer-accounts: PingID license management for customer accounts
  google-workspace-connector-3-2-1: Google Workspace Connector 3.2.1
  december-2022: December 2022
  improved-messaging-for-expired-user-invitations: Improved messaging for expired user invitations
  scim-saas-provisioner-1-5: SCIM SaaS Provisioner 1.5
  zoom-connector-1-2: Zoom Connector 1.2
  november-2022: November 2022
  export-a-report-of-applications-by-group-access: Export a report of applications by group access
  september-2022: September 2022
  managed-accounts-certificate-notifications: Managed accounts certificate notifications
  august-2022: August 2022
  custom-application-and-customer-connection-secrets: Custom application and customer connection secrets
  pingone-for-enterprise-directory-self-registration: PingOne for Enterprise Directory self-registration
  custom-entity-id: Custom Entity ID
  july-2022: July 2022
  servicenow-connector-2-3-2: ServiceNow Connector 2.3
  march-2022: March 2022
  pingid-admins-multi-factor-authentication-mfa-bypass: PingID admins multi-factor authentication (MFA) bypass
  google-workspace-provisioner-improvements: Google Workspace Provisioner improvements
  new-report-type: New report type
  new-report-type-2: New report type
  application-integration-testing-change: Application integration testing change
  rest-application-customization: REST application customization
---

# PingOne for Enterprise Release Notes

New features and improvements in PingOne for Enterprise, PingOne for Enterprise for Managed Service Providers, PingOne SSO for SaaS Apps, PingOne SSO for SaaS Apps with Managed Accounts, and AD Connect.

Subscribe for automatic updates: [icon: rss-square, set=fa][PingOne for Enterprise Release Notes RSS feed](p14e_release_notes.xml)

## May 2025

### **Users** tab restored after migrating PingID

Info PingOne for Enterprise

We've restored the SSO functionality in the **Users** tab for accounts that have migrated their PingID tenant to PingOne. We've also added a banner linking you to the PingOne admin console where you can manage your migrated PingID tenant.

## February 2025

### Filter Users by Service search

New PingOne for Enterprise

We've added a feature that allows you to filter your search results by user attribute in the **Users by Service** window. You can now search by Subject, Email, or Name across all available services. The default attribute is Subject.

To search by Name, the input string must be in the format "last name, first name".

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use the search filter, your account must not have the `SERVICE_USER_LEGACY` feature flag, which preserves legacy search behavior from before a PingOne for Enterprise update in [April 2023](#april-2023).Your account only has this feature flag enabled if you requested it. If you're not sure whether you have this feature flag, or if you want it removed so you can access this new behavior, open a support case.The email and name filters can only filter user data that was newly created or updated after this feature was deployed (February 2025). |

Learn more in [Temporarily hiding a user's service](../pingone_for_enterprise/p14e_temporarily_hide_users_service.html), [Bypassing a user's service](../pingone_for_enterprise/p14e_bypass_users_service.html), and [Removing service users](../pingone_for_enterprise/p14e_remove_service_users.html).

## January 2025

### Users tab remains after PingID integration with PingOne

Fixed PingOne for Enterprise

We've fixed a defect that caused the **Users** tab to remain available to the Service User Admin role after you integrate your PingID tenant with PingOne.

Integrating PingID with PingOne moves user management from PingOne for Enterprise to the PingOne admin console.

Learn more in the [Users](https://docs.pingidentity.com/pingone/directory/p1_aboutusers.html) section of the PingOne documentation.

### Sub-tenant admin access lock

Fixed PingOne for Enterprise PingOne SSO for SaaS Apps

We've fixed a defect in PingOne for Enterprise for Managed Service Providers and PingOne SSO for SaaS Apps with Managed Accounts that allowed administrative users to permanently lock their access to read-only when impersonating a sub-tenant.

## October 2024

### AWS IAM Identity Center Provisioner

Improved PingOne for Enterprise

We added the ability to update the `nickname` attribute for existing provisioned Amazon Web Services (AWS) single sign-on (SSO) users.

Learn more in [Amazon Web Services](../pingone_for_enterprise_app_catalog/p14eapps_aws.html).

### PingOne Connector

Fixed PingOne for Enterprise

We fixed a defect that could cause delays in fetching an updated user schema.

The following known limitations apply:

* Clearing fields on updates is not supported.

* Multivalued attributes (e.g. emails or addresses) are not supported. Multiple values appear as a single array value in PingOne.

* Custom attributes are set when the user is initially created and are never updated.

## May 2024

### SCIM SaaS Provisioner

Fixed PingOne for Enterprise

Fixed a defect that caused a JSON parsing error when non-standard fields are present in the SCIM 2.0 Enterprise User Schema Extension.

The following known limitations apply:

* User attributes cannot be cleared after they have been set. They can only be updated.

* Outbound Group Provisioning and Memberships are not supported.

* Patch updates to SCIM-enabled target applications are not supported.

* There is a limit of one value per type (such as home, work, or other) for multivalue attributes such as `email`, `phone`, and `address`.

* Unexpected behavior may occur if the SaaS does not specify either type and primary information, or both type and primary information for multivalue attribute such as such as `email`, `phone`, and `address`. Also, existing SaaS attributes might not be removed during an Update, and the desired value might not be correctly set as primary.

* SCIM-compliant service providers can implement or interpret SCIM standards differently, which can result in behavior that is not consistent with the intended use of the SCIM SaaS Provsioner.

### PingOne Connector

New PingOne for Enterprise

Added support for the Australia region.

The following known limitations apply:

* Clearing fields on updates is not supported.

* Multivalued attributes (e.g. emails or addresses) are not supported. Multiple values appear as a single array value in PingOne.

* Custom attributes are set when the user is initially created, and are never updated.

## March 2024

### Country data for SSO report

New PingOne for Enterprise

Added a new column to the SSO report listing the country where the SSO event originated.

To learn more, see [PingOne for Enterprise report event reference](../pingone_for_enterprise/p14e_report_event_reference.html).

## November 2023

### ServiceNow Connector 2.3

New PingOne for Enterprise

Added support for the Utah and Vancouver versions of ServiceNow.

The following known limitations apply:

* Outbound Group Provisioning and Memberships are not supported.

* User attributes cannot be cleared after they have been set. They can only be updated.

* When provisioning to ServiceNow, all user accounts in ServiceNow must have a `username` (User ID).

  This is not a required field in ServiceNow, but it is required for provisioning to work due to the provisioner using this field to sync with preexisting users in ServiceNow. If a user in ServiceNow resolves to `sAMAccountName` (the "standard" mapping in the provisioning channel), then the accounts will be linked.

  Currently if users exist in ServiceNow without a `username` that will cause errors in provisioning, resolve this by ensuring every user has this field populated even if they are not intended to be managed by the provisioner.

* When provisioning users, the `username` attribute must only contain URL-safe characters.

* When synchronizing roles with users, the role attribute must contain only URL-safe characters.

* If a new user is created with the same `username` as an existing user, a duplicate user will not be created. Instead, the existing user will be updated with any information in the create.

* Due to limitations with the ServiceNow API, a role can be added to a user, but not removed. This may cause a user's role in the source datastore to become out-of-sync with the user's role in ServiceNow.

  For more information, see [Enable User Role Removal](https://docs.pingidentity.com/bundle/integrations/page/pzq1563995052451.html).

* When mapping the `roles` attribute, multiple additional calls to ServiceNow must be made to sync user role. This may impact provisioning performance.

* For departments that contain the `^` character in the name, the ServiceNow API causes the creation of multiple departments with the same name.

* For the `department` and `location` parameters, the ServiceNow API ignores capitalization. When provisioning a user that matches multiple departments or locations in ServiceNow (such as Accounting and accounting), PingFederate provisions the user with an empty department or location attribute and logs an error in `provisioner.log`.

* The `city` attribute mapping is not supported for the local repository.

For more information, see [Adding ServiceNow to Your PingOne for Enterprise Dock](../pingone_for_enterprise_app_catalog/p14eapps_servicenow.html).

## July 2023

### Webex Connector 2.3.0

New PingOne for Enterprise

Updated the **SiteID** configuration field to be optional.

For more information, see [Adding WebEx to Your PingOne for Enterprise Dock](../pingone_for_enterprise_app_catalog/p14eapps_webex.html).

### Zoom Connector 1.3.3

New PingOne for Enterprise

Added support for Server-to-Server OAuth applications. This is an alternative method to create a connection to Zoom due to the deprecation of JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
\</div>)* applications.

For more information, see [Adding Zoom to Your PingOne for Enterprise Dock](../pingone_for_enterprise_app_catalog/p14eapps_zoom.html).

## May 2023

### Manual PingOne for Enterprise connections

Info PingOne SSO for SaaS Apps

It is no longer possible to connect a PingOne for Enterprise tenant and a PingOne SSO for SaaS Apps tenant by manually exchanging metadata. This kind of connection was never supported, and can cause duplicate entity ID errors.

You should always use an [invited connection](../pingone_sso_for_saas_apps/p14saas_creating_invited_sso_connection.html) to connect your PingOne SSO for SaaS Apps application to PingOne for Enterprise.

## April 2023

### Users by Service search

Info PingOne for Enterprise

The Users by Service search behavior has changed from returning results that contain the search string to returning results that begin with the username.

For more information, see [Monitoring service activity](../pingone_for_enterprise/p14e_monitor_service_activity.html).

### ServiceNow Tokyo

Improved PingOne for Enterprise

Added support for the Tokyo version of ServiceNow.

The following known limitations apply:

* Outbound Group Provisioning and Memberships are not supported.

* User attributes cannot be cleared after they have been set. They can only be updated.

* When provisioning to ServiceNow, all user accounts in ServiceNow must have a `username` (User ID).

  This is not a required field in ServiceNow, but it is required for provisioning to work due to the provisioner using this field to sync with preexisting users in ServiceNow. If a user in ServiceNow resolves to `sAMAccountName` (the "standard" mapping in the provisioning channel), then the accounts will be linked.

  Currently if users exist in ServiceNow without a `username` that will cause errors in provisioning, resolve this by ensuring every user has this field populated even if they are not intended to be managed by the provisioner.

* When provisioning users, the `username` attribute must only contain URL-safe characters.

* When synchronizing roles with users, the role attribute must contain only URL-safe characters.

* If a new user is created with the same `username` as an existing user, a duplicate user will not be created. Instead, the existing user will be updated with any information in the create.

* Due to limitations with the ServiceNow API, a role can be added to a user, but not removed. This may cause a user's role in the source datastore to become out-of-sync with the user's role in ServiceNow.

  For more information, see [Enable User Role Removal](https://docs.pingidentity.com/bundle/integrations/page/pzq1563995052451.html).

* When mapping the `roles` attribute, multiple additional calls to ServiceNow must be made to sync user role. This may impact provisioning performance.

* For departments that contain the `^` character in the name, the ServiceNow API causes the creation of multiple departments with the same name.

* For the `department` and `location` parameters, the ServiceNow API ignores capitalization. When provisioning a user that matches multiple departments or locations in ServiceNow (such as Accounting and accounting), PingFederate provisions the user with an empty department or location attribute and logs an error in `provisioner.log`.

## March 2023

### Email communications

Info PingOne for Enterprise, PingOne SSO for SaaS Apps

Updated our email communications to change the product name from "PingOne" to "PingOne for Enterprise".

This change affects both PingOne for Enterprise and PingOne SSO for SaaS Apps licenses, and will include all emails from Ping, including certificate expiration and password expiration messages.

Email templates that you have customized for your customer accounts are not affected by this change.

If you have any email filters in place, update them to reflect this change.

## February 2023

### PingID license management for customer accounts

New PingOne for Enterprise

Added the ability to manage PingID licensing for your PingOne for Enterprise for Managed Service Providers customer accounts.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | This feature is in limited release. To request access to this feature, open a support case. |

For more information, see [Administer customer accounts](../pingone_for_enterprise/p14e_administer_customer_accounts.html).

### Google Workspace Connector 3.2.1

Improved PingOne for Enterprise

* Added support for the `addressFormatted` user attribute.

  `addressFormatted` is a full and unstructured postal address. This single-string attribute can include any values like: PO Box, city, state/province, ZIP/postal code, or country/region.

* Fixed an issue that caused new users not to be provisioned with group membership.

* Fixed an issue that caused users not to be disabled by a disable deprovision action.

Learn more in [Google Workspace Provisioner](https://docs.pingidentity.com//integrations/google/google_workspace_provisioner/pf_google_workspace_connector.html).

## December 2022

### Improved messaging for expired user invitations

Improved PingOne for Enterprise

Updated the messaging for the following PingOne for Enterprise Directory invited user scenarios:

If an invited user clicks on an expired invitation link, they are redirected to the PingOne for Enterprise sign-on page with an error message directing them to request a new invitation from an administrator. For more information, see [Add directory users](../pingone_for_enterprise/p14e_add_p1d_users.html).

If an invited user has not yet been approved, and they try to use the **Forgot Password** link, they will see an error message that their account is still awaiting approval.

### SCIM SaaS Provisioner 1.5

Improved PingOne for Enterprise

Added the `homeEmail` and `otherEmail` attributes.

The following known limitations apply:

* Clearing fields on updates is not supported.

* Outbound Group Provisioning and Memberships are not supported.

* Patch updates to SCIM-enabled target applications are not supported.

* There is a limit of one value per type (such as home, work, or other) for multivalue attributes such as `email`, `phone`, and `address`.

* Unexpected behavior may occur if the SaaS does not specify either type and primary information, or both type and primary information for multivalue attribute such as such as `email`, `phone`, and `address`. Also, existing SaaS attributes might not be removed during an Update, and the desired value might not be correctly set as primary.

* SCIM-compliant service providers can implement or interpret SCIM standards differently, which can result in behavior that is not consistent with the intended use of the SCIM SaaS Provsioner.

Learn more in [SCIM Provisioner](https://docs.pingidentity.com//integrations/scim/pf_scim_connector.html).

### Zoom Connector 1.2

Improved PingOne for Enterprise

We added a feature to restore the user's Zoom license when the user is re-enabled.

The following known issues apply:

* The Zoom Provisioner does not support group provisioning.

* User attributes cannot be cleared once set. They can only be updated.

* Zoom only allows a single value for the `Roles` attribute.

* Deleting the administrative user that is set up for provisioning may lead to undesired consequences. The provisioner makes the administrative user the owner and member of each group that is created by the provisioner. We recommend not deleting the administrative user and not managing this user through the provisioner.

* Zoom does note allow attribute updates for users with a "disabled" status. To update attributes, re-enable the user first.

* Zoom does not allow users with the admin role to be disabled or deleted. Change the user's role first.

Learn more in [Zoom Provisioner](https://docs.pingidentity.com//integrations/zoom/pf_zoom_connector.html).

## November 2022

### Export a report of applications by group access

Improved PingOne for Enterprise

You can now export a `.csv` report of configured applications and the user groups assigned to access them. This can be useful for filtering purposes if you have a large number of active applications.

For more information, see [Exporting a report of applications by group](../pingone_for_enterprise/p14e_export_apps_by_group.html).

## September 2022

### Managed accounts certificate notifications

Improved PingOne for Enterprise, PingOne SSO for SaaS Apps

If you have a PingOne for Enterprise for Managed Service Providers or PingOne SSO for SaaS Apps with Managed Accounts license, you can now enable your administrators to receive email notifications when your customer accounts have certificates that are about to expire or have expired.

For more information, see [Editing administrative roles, permissions, and notifications](../pingone_for_enterprise/p14e_editing_administrative_roles_permissions_notifications.html).

## August 2022

### Custom application and customer connection secrets

New PingOne SSO for SaaS Apps

You can now generate client secret values for each application and customer connection API connection.

This ability improves security over using a single set of client credentials for all connections.

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | This feature is currently in limited release. To request access to this feature, open a support case. |

For more information, see [Creating or editing application-specific credentials](../pingone_sso_for_saas_apps/p14saas_application_credentials.html) and [Creating or editing additional Connection API credentials](../pingone_sso_for_saas_apps/p14saas_customer_connection_api_credentials.html).

### PingOne for Enterprise Directory self-registration

Improved PingOne for Enterprise

You can now configure how long the email invitation remains valid for new self-registering PingOne for Enterprise Directory users.

You can set the duration between 1 hour and 168 hours. The default duration is 24 hours.

For more information, see [Allow self registration for new directory users](../pingone_for_enterprise/p14e_allow_self_registration_p1d_users.html).

### Custom Entity ID

Info PingOne SSO for SaaS Apps

The ability to define a custom entity ID for applications that are enabled through PingOne SSO for SaaS Apps is now available to all customers.

If a custom entity ID is in use by a non-multiplexed connection, it cannot be changed.

For more information, see [Add or update other applications](../pingone_sso_for_saas_apps/p14saas_add_update_other_app.html).

## July 2022

### ServiceNow Connector 2.3

Improved PingOne for Enterprise

Added support for the Rome and San Diego versions of ServiceNow.

The following known issues apply:

* Outbound Group Provisioning and Memberships are not supported.

* User attributes cannot be cleared once set. They can only be updated.

* When provisioning to ServiceNow, all user accounts in ServiceNow must have a `username` (User ID). This is not a required field in ServiceNow, but it is required for provisioning to work due to the provisioner using this field to sync with pre-existing users in ServiceNow. If a user in ServiceNow resolves to `sAMAccountName` (the "standard" mapping in the provisioning channel), then the accounts will be linked. Currently, if users exist in ServiceNow without a `username` that will cause errors in provisioning. You can resolve this by ensuring every user has the `username` field populated even if they are not intended to be managed by the provisioner.

* When provisioning users, the `username` attribute must only contain URL-safe characters.

* When synchronizing roles with users, the role attribute must contain only URL-safe charcters.

* If a new user is created with the same `username` as an existing user, a duplicate user will not be created. Instead, the existing user will be updated with any information in the create.

* Due to limitations with the ServiceNow API, a role can be added to a user, but not removed, which may cause a user's role in the source datastore to become out-of-sync with the user's role in ServiceNow. Learn more in [ServiceNow Provisioner](https://docs.pingidentity.com//integrations/servicenow/pf_servicenow_connector.html).

* When mapping the roles attribute multiple additional calls to ServiceNow must be made to sync user role. This may impact provisioning performance.

* For departments that contain the `^` character in the name, the ServiceNow API causes the creation of multiple departments with the same name.

* For the department and location objects, the ServiceNow API ignores capitalization. When provisioning a user that matches multiple departments or locations in ServiceNow (such as `Accounting` and `accounting`), PingFederate provisions the user with an empty department or location attribute and logs an error in `provisioner.log`.

## March 2022

### PingID admins multi-factor authentication (MFA) bypass

New PingOne for Enterprise

Added an optional permission to allow PingID Device Administrators to grant temporary MFA bypass to users.

To enable this permission, go to **Account > Administrators > Permissions** and select **Allow Bypass**.

For more information, see [Administrative roles](../pingone_for_enterprise/p14e_administrative_roles.html).

### Google Workspace Provisioner improvements

Improved PingOne for Enterprise

Added the following improvements to the Google Workspace Provisioner:

* Added the ability to disable and delete users

* Added the ability to provision disabled users

* Added the ability to remove user actions

* Added support for Google Admin SDK 1.32.1

The following known issues apply:

* User attributes cannot be cleared once set.

* Google does not properly handle creating users with an invalid `addressCountry` value.

* The Provisioner sends the value of `work` for the `Organization` type. However Google does not retain this value. and as a result the *Organization* type has no value.

* Google treats certain user attributes as complex data sets:

  * Address (address\* attributes)

  * Organization (org\* attributes)

  * Phone (work\* attributes)

  Any unmapped or empty fields within a complex data set will be cleared in the corresponding Google account.

### New report type

New PingOne for Enterprise

Added a new report type for PingOne for Enterprise for Managed Service Providers accounts.

The **SSO Summary by Customer** report displays unique users and SSO transactions for each of your customer accounts.

For more information, see [PingOne for Enterprise report types](../pingone_for_enterprise/p14e_report_types.html).

### New report type

New PingOne for Enterprise

The **SSO User Summary** report displays a list of all unique users who have used SSO during the defined period.

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | This feature is currently in limited release. To request access to this feature, open a support case. |

For more information, see [PingOne for Enterprise report types](../pingone_for_enterprise/p14e_report_types.html).

### Application integration testing change

Info PingOne SSO for SaaS Apps

Changed the tenant used to generate test users from PingFederate to PingOne for Enterprise Directory.

Test user IDs and passwords will no longer automatically populate on the test IdP login site. You can find a complete list of test user IDs and their passwords in the documentation.

For more information, see [Testing your application using the built-in IdP](../pingone_sso_for_saas_apps/p14saas_test_application_integration.html).

### REST application customization

New PingOne SSO for SaaS Apps

Added an option to allow your customers to customize the **Default Application URL** and **Error URL** when they configure your REST application from the application catalog.

For more information, see [Add or update other applications](../pingone_sso_for_saas_apps/p14saas_add_update_other_app.html).

---

---
title: Previous AD Connect Releases
description: Resolved issues
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_release_notes:p14e_adc_relnotes_archive
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_release_notes/p14e_adc_relnotes_archive.html
revdate: July 10, 2024
section_ids:
  april-2020-release-version-5-0-3: "April 2020 Release: Version 5.0.3"
  february-2020-version-5-0-1: "February 2020: Version 5.0.1"
  fall-2019-version-4-0-10: "Fall 2019: Version 4.0.10"
  summer-2019-release-version-4-0-65: "Summer 2019 Release: Version 4.0.65"
  fall-2018-release-version-4-0-5: "Fall 2018 Release: Version 4.0.5"
  august-2018-version-4-0-3: "August, 2018: Version 4.0.3"
  march-2018-version-4-0-1: "March, 2018: Version 4.0.1"
  october-2017-version-3-0-60: "October, 2017: Version 3.0.60"
  july-2017-version-3-0-50: "July, 2017: Version 3.0.50"
  june-2017-version-3-0-49: "June, 2017: Version 3.0.49"
  june-2017-version-3-0-47: "June, 2017: Version 3.0.47"
  june-2017-version-3-0-44: "June, 2017: Version 3.0.44"
  may-2017-version-3-0-43: "May, 2017: Version 3.0.43"
  april-2017-version-3-0-42: "April, 2017: Version 3.0.42"
  march-2017-version-3-0-38: "March, 2017: Version 3.0.38"
  january-2017-version-3-0-37: "January 2017: Version 3.0.37"
  august-16-2016-version-3-0-31: "August 16, 2016: Version 3.0.31"
  august-30-2016-version-3-0-32: "August 30, 2016: Version 3.0.32"
  august-9-2016-version-3-0-22: "August 9, 2016: Version 3.0.22-→"
  may-17-2016-version-3-0-22: "May 17, 2016: Version 3.0.22"
  april-26-2016-version-3-0-20: "April 26, 2016: Version 3.0.20"
  march-15-2016-version-3-0-14: "March 15, 2016: Version 3.0.14"
  january-22-2016-version-3-0-12: "January 22, 2016: Version 3.0.12"
  january-12-2016-version-3-0-10: "January 12, 2016: Version 3.0.10"
  october-15-2015-version-3-0-8: "October 15, 2015: Version 3.0.8"
  september-16-2015-version-3-0: "September 16, 2015: Version 3.0"
  august-21-2015-version-2-1-17: "August 21, 2015: Version 2.1.17"
  july-21-2015-version-2-1-15: "July 21, 2015: Version 2.1.15"
  march-16-2015-version-2-1-10: "March 16, 2015: Version 2.1.10"
  february-25-2015-version-2-1-9: "February 25, 2015: Version 2.1.9"
  january-10-2015-version-2-1-4: "January 10, 2015: Version 2.1.4"
  october-28-2014-version-2-0-45: "October 28, 2014: Version 2.0.45"
  october-7-2014-version-2-0-44: "October 7, 2014: Version 2.0.44"
  august-26-2014-version-2-0-42: "August 26, 2014: Version 2.0.42"
  july-17-2014-version-2-0-39: "July 17, 2014: Version 2.0.39"
  june-24-2014-version-2-0-34: "June 24, 2014: Version 2.0.34"
---

# Previous AD Connect Releases

## April 2020 Release: Version 5.0.3

**Resolved issues**

| Ticket ID | Issue                                                                                                 |
| --------- | ----------------------------------------------------------------------------------------------------- |
| SSD-15239 | (AD Connect) Fixed an issue where AD Connect could not be installed on a non-Domain Controller sever. |

## February 2020: Version 5.0.1

**Enhancements**

| Feature     | Description                                                                                                                                                                                                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TLS Support | AD Connect 5.0.1 supports TLS 1.2 as we prepare to End of Life TLS 1.0. and 1.1.                                                                                                                                     |
|             | New installations and upgrades to AD Connect 5.0.1 require the installation of Microsoft .NET Framework 4.7.2. See [Installing AD Connect](../pingone_for_enterprise/p14e_installing_adc.html) for more information. |

## Fall 2019: Version 4.0.10

**Enhancements**

| Feature                         | Description                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Directory Global Catalog | (AD Connect only) You can now elect to use the Active Directory Global Catalog for lookups. The option to enable the Global Catalog is in the AD Connect Configuration section of the AD Connect setup (**Setup > Identity Repository > Connect to an Identity Repository > AD Connect**). See [AD Connect final setup](../pingone_for_enterprise/p14e_adc_final_setup.html) for more information. |

## Summer 2019 Release: Version 4.0.65

**Enhancements**

| Feature  | Description                                                                                                                                                                                                         |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Branding | (AD Connect) You can now assign branding for the login and password reset pages. See [Assign AD Connect branding and designs](../pingone_for_enterprise/p14e_assign_adc_branding_design.html) for more information. |

## Fall 2018 Release: Version 4.0.5

**Resolved issues**

| Ticket ID | Issue                                                                                                     |
| --------- | --------------------------------------------------------------------------------------------------------- |
| SSD-10054 | (AD Connect) Fixed an issue where AD Connect did not allow duplicate values in an Octet String attribute. |

## August, 2018: Version 4.0.3

**Enhancements**

| Feature                       | Description                                          |
| ----------------------------- | ---------------------------------------------------- |
| TLS 1.1 and 1.2 now supported | We've added support for TLS 1.1 and 1.2. (SSD-8913). |

## March, 2018: Version 4.0.1

**Resolved issues**

| Ticket ID | Issue                                                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| SSD-6889  | (AD Connect) Fixed an issue where AD Connect was prevented from reconnecting to PingOne if an error was encountered while attempting to connect. |

## October, 2017: Version 3.0.60

**Enhancements**

| Feature                                             | Description                                                                                                                       |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| (AD Connect) Added logging of authentication method | We updated AD Connect logging to distinguish the method a user employs to authenticate (such as, IWA or Forms-based). (SSD-6103). |

**Known issues and limitations**

| Subject | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-1289 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |

## July, 2017: Version 3.0.50

**Enhancements**

| Feature                   | Description                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Invalid credential errors | Invalid credential errors are now logged at the Debug level, rather than the Error level as previously. (SSD-5372, SSD-5501). |

**Resolved issues**

| Ticket ID                 | Issue                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| PINGONESTG-2489, SSD-5501 | (AD Connect with IIS only) Fixed an issue where communication issues with the DC were being masked by other error messages. |

**Known issues and limitations**

| Subject | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-1289 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |

## June, 2017: Version 3.0.49

**Enhancements**

| Feature                   | Description                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Invalid credential errors | (AD Connect with IIS only) Invalid credential errors are now logged at the Debug level, rather than the Error level as previously. (SSD-5372). |

**Resolved issues**

| Ticket ID                 | Issue                                                                                                                                                                                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PINGONESTG-2447, SSD-5372 | (AD Connect with IIS only) Fixed an issue in AD Connect with IIS where look ups for additional user information were sometimes incorrectly based on the user's email domain instead of the Windows domain, as expected.                                                       |
| PINGONESTG-2455, SSD-5372 | Fixed an issue where AD Connect could unintentionally be configured to strip the email domain from the username before trying to look up the user information based on their email (which would always fail). The Strip Email setting is now disabled for email-based lookup. |

**Known issues and limitations**

| Subject | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-1289 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |

## June, 2017: Version 3.0.47

**Enhancements**

| Feature       | Description                                     |
| ------------- | ----------------------------------------------- |
| Debug logging | We've improved debug logging (PINGONESTG-2292). |

**Resolved issues**

| Ticket ID       | Issue                                                                            |
| --------------- | -------------------------------------------------------------------------------- |
| PINGONESTG-2413 | Fixed an issue where a user's thumbnail photo attribute wasn't encoded properly. |

**Known issues and limitations**

| Subject | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-1289 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |

## June, 2017: Version 3.0.44

**Resolved issues**

| Ticket ID       | Issue                                                             |
| --------------- | ----------------------------------------------------------------- |
| PINGONESTG-2377 | Fixed an issue where the photo attribute wasn't encoded properly. |

**Known issues and limitations**

| Subject | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-1289 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |

## May, 2017: Version 3.0.43

**Resolved issues**

| Ticket ID       | Issue                                                                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-4726        | Fixed an issue when using Filter as the lookup method with "Strip mail" disabled. AD Connect was appending the domain name if the user didn't include it. |
| SSD-5013        | Fixed an issue where, under certain conditions, errors were being displayed without the proper styling.                                                   |
| PINGONESTG-2341 | Fixed issue where static resources weren't loaded correctly on some pages.                                                                                |

**Known issues and limitations**

| Subject | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-1289 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |

## April, 2017: Version 3.0.42

**Resolved issues**

| Ticket ID       | Issue                                                                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PINGONESTG-2251 | Fixed an issue with filter-based authentication where disabling the **Strip Email** resulted in appending the Windows domain to usernames during the lookup. |

**Known issues and limitations**

| Subject | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-1289 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |

## March, 2017: Version 3.0.38

**Enhancements**

* Support for TLS v1.1 & v1.0 following Salesforce removal of TLS v1.0 support

  From March 4, 2017, Salesforce is no longer supporting TLS v1.0. To minimize impact for PingOne customers that use PingOne to connect to Salesforce via delegated authentication for AD Connect with IIS, we've put together information and instructions. These show you how to ensure your IIS deployment running AD Connect for IIS supports the updated version of TLS (TLS v1.1 or v1.2).

**Resolved issues**

| Ticket ID | Issue                                                                                                                  |
| --------- | ---------------------------------------------------------------------------------------------------------------------- |
| SSD-4121  | (AD Connect) Fixed an issue where concurrent SSO requests using IWA were resulting in network collisions.              |
| ID-1357   | Fixed an issue that was causing some users to get an HTTP Error 400 when attempting to SSO to ZScalar from AD Connect. |

**Known issues and limitations**

| Subject | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-1289 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |

## January 2017: Version 3.0.37

**Known issues and limitations**

| Subject  | Issue/Limitation                                                                                                                                                                                                                                                                                                                      |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-3870 | If you import more than one signing certificate with the same subject name into the IIS host for AD Connect, you must first remove expired certificates with the same subject name directly through IIS Manager. If this is not done you may experience problems when removing an expired certificate and updating it with a new one. |
| SSD-4139 | Fixed an issue where a user's middle name attribute could not be used in a SAML assertion.                                                                                                                                                                                                                                            |

## August 16, 2016: Version 3.0.31

**Resolved issues**

| Ticket ID | Issue                                                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------------------------- |
| ID-5623   | Fixed an issue where AD Connect was providing PingOne with the computer name, rather than the fully qualified domain name (FQDN). |

## August 30, 2016: Version 3.0.32

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-5826   | Fixed an issue where the connection to PingOne can intermittently be lost under certain conditions.                                                                       |
| ID-5838   | When you use a custom theme.zip with AD Connect with IIS, the favicon is placed in the root directory. This prevents the custom theming from handling the state properly. |

## August 9, 2016: Version 3.0.22-→

**Enhancements**

* AD Connect installer

  We've added the ability to define a verification certificate as part of the AD Connect installation process. During installation, you have the option to:

  * Create a new self-signed certificate.

  * Select an existing certificate.

  * Upload a certificate file.The options available vary depending on whether you are performing a new installation or an upgrade.

## May 17, 2016: Version 3.0.22

**Enhancements**

* New configuration parameter for AD Connect

  We've add the Subject Attribute parameter to the AD Connect Configuration section when installing or reconfiguring AD Connect. Use this parameter to choose the value to use for SAML\_SUBJECT. The possible values are sAMAccountName and userPrincipalName.

**Resolved issues**

| Ticket ID | Issue                                                                                                                                    |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| ID-361    | Fixed an issue where AD Connect wasn't sending the address attributes in the SCIM User object if the StreetAddress attribute wasn't set. |

**Known issues and limitations**

| Subject      | Issue/Limitation                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Provisioning | For a single PingOne account, if you have two AD domains with two provisioners, do not modify groups on one domain while the other domain's provisioner is restarting. This can cause unpredictable behaviour to occur. Ticket ID: IX-315. |

## April 26, 2016: Version 3.0.20

**Enhancements**

* New configuration parameter for AD Connect

  We've add the Subject Attribute parameter to the AD Connect Configuration section when installing or reconfiguring AD Connect. Use this parameter to choose the value to use for SAML\_SUBJECT. The possible values are sAMAccountName and userPrincipalName.

**Resolved issues**

| Ticket ID | Issue                                                                                                              |
| --------- | ------------------------------------------------------------------------------------------------------------------ |
| ID-5012   | Fixed an issue where users had no access to applications until the AD Connect Configuration service was restarted. |
| ID-4705   | Fixed an issue where PingID needed to be re-enabled after upgrading AD Connect.                                    |

**Known issues and limitations**

| Subject      | Issue/Limitation                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Provisioning | For a single PingOne account, if you have two AD domains with two provisioners, do not modify groups on one domain while the other domain's provisioner is restarting. This can cause unpredictable behaviour to occur. Ticket ID: IX-315. |

## March 15, 2016: Version 3.0.14

**Enhancements**

* None

  (None to report for this release.)

**Resolved issues**

| Ticket ID | Issue                                                                                                                         |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ID-4668   | Fixed an issue where the AD Connect for IIS installation wasn't finding the required .NET version, although it was installed. |
| ID-4650   | Fixed an issue where provisioning for AD Connect was failing.                                                                 |

Known issues and limitations

| Subject      | Issue/Limitation                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Provisioning | For a single PingOne account, if you have two AD domains with two provisioners, do not modify groups on one domain while the other domain's provisioner is restarting. This can cause unpredictable behaviour to occur. Ticket ID: IX-315. |

## January 22, 2016: Version 3.0.12

**Enhancements**

* None

  (None to report for this release.)

**Resolved issues**

| Ticket ID | Issue                                                                                              |
| --------- | -------------------------------------------------------------------------------------------------- |
| ID-4010   | Fixed an issue where SSO wasn't working unless you restarted the AD Connect Configuration Service. |

Known issues and limitations

| Subject      | Issue/Limitation                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Provisioning | For a single PingOne account, if you have two AD domains with two provisioners, do not modify groups on one domain while the other domain's provisioner is restarting. This can cause unpredictable behaviour to occur. Ticket ID: IX-315. |

## January 12, 2016: Version 3.0.10

**Enhancements**

* None

  (None to report for this release.)

**Resolved issues**

| Ticket ID | Issue                                                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------ |
| ID-3995   | Fixed an issue where you weren't able to select the Provisioner Only option using a mouse or trackpad. |

Known issues and limitations

| Subject      | Issue/Limitation                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Provisioning | For a single PingOne account, if you have two AD domains with two provisioners, do not modify groups on one domain while the other domain's provisioner is restarting. This can cause unpredictable behaviour to occur. Ticket ID: IX-315. |

## October 15, 2015: Version 3.0.8

**Enhancements**

* None

  (None to report for this release.)

**Resolved issues**

| Ticket ID | Issue                                                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ID-3613   | Fixed an issue where the installation instructions in the header of the screen to select the installation type weren't being displayed properly. |
| ID-3501   | Fixed the naming of the AD Connect with IIS selection on the installation type screen.                                                           |

## September 16, 2015: Version 3.0

**Enhancements**

* Group Hierarchy Support

  We've added a configuration option to enable support for nested Active Directory groups. When this option is enabled, the nested groups will inherit the SSO permissions of their parent group or groups. See [Installing AD Connect](../pingone_for_enterprise/p14e_installing_adc.html) for instructions.

* Auto-Update Changes

  You can now use auto-update if your current installation is version 3.0 or higher. All prior versions of AD Connect require a manual update. See [Updating AD Connect](../pingone_for_enterprise/p14e_updating_adc.html) for instructions.

* .NET Requirements

  Microsoft Net 4.5.2 Framework is now required. The framework installation file is packaged with the AD Connect and AD Connect with IIS distributions.

**Resolved issues**

| Ticket ID | Issue                                                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| ID-2277   | Fixed issue where the option to require a password on an initial login wasn't enabled by default.                                     |
| ID-2222   | Fixed display of popup window to authorize an AD Connect update.                                                                      |
| ID-2117   | Fixed error when configuring IdP using a new account.                                                                                 |
| ID-2074   | Fixed error when switching to edit mode from the settings summary page after previously exiting edit mode without making any changes. |

Known issues and limitations

| Subject                                                                  | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AD Connect application requests redirected to the PingOne dock (ID-1441) | If you are using AD Connect and experiencing an issue where your application requests are being redirected to the PingOne dock when you aren't using the dock, enable the stateless option for AD Connect:1) Ensure that you're using AD Connect version 2.1.14 or higher. See [Updating AD Connect](../pingone_for_enterprise/p14e_updating_adc.html) for upgrade instructions.

2) Open the *installation\_path*Ping Identity\AdConnect\SSO\web.config file in a text editor.

3) Under the \<appSettings> section, add the following entry:

   ```
   <add key="stateless" value="true" />
   ```

4) Save the web.config file. Your changes will take affect immediately. |

## August 21, 2015: Version 2.1.17

**Enhancements**

* None

  (None to report for this release).

**Resolved issues**

| Ticket ID | Issue                                                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| ID-2277   | Fixed issue where the option to require a password on an initial login wasn't enabled by default.                                     |
| ID-2222   | Fixed display of popup window to authorize an AD Connect update.                                                                      |
| ID-2117   | Fixed error when configuring IdP using a new account.                                                                                 |
| ID-2074   | Fixed error when switching to edit mode from the settings summary page after previously exiting edit mode without making any changes. |

Known issues and limitations

| Subject                                                                  | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AD Connect application requests redirected to the PingOne dock (ID-1441) | If you are using AD Connect and experiencing an issue where your application requests are being redirected to the PingOne dock when you aren't using the dock, enable the stateless option for AD Connect:1) Ensure that you're using AD Connect version 2.1.14 or higher. See [Updating AD Connect](../pingone_for_enterprise/p14e_updating_adc.html) for upgrade instructions.

2) Open the *installation\_path*Ping Identity\AdConnect\SSO\web.config file in a text editor.

3) Under the \<appSettings> section, add the following entry:

   ```
   <add key="stateless" value="true" />
   ```

4) Save the web.config file. Your changes will take affect immediately. |

## July 21, 2015: Version 2.1.15

**Enhancements**

* None

  (None to report for this release).

**Resolved issues**

| Ticket ID | Issue                                                                         |
| --------- | ----------------------------------------------------------------------------- |
| ID-1306   | Fixed a misleading error message when attempting to communicate with PingOne. |

Known issues and limitations

| Subject                                                                  | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AD Connect application requests redirected to the PingOne dock (ID-1441) | If you are using AD Connect and experiencing an issue where your application requests are being redirected to the PingOne dock when you aren't using the dock, enable the stateless option for AD Connect:1) Ensure that you're using AD Connect version 2.1.14 or higher. See [Updating AD Connect](../pingone_for_enterprise/p14e_updating_adc.html) for upgrade instructions.

2) Open the *installation\_path*Ping Identity\AdConnect\SSO\web.config file in a text editor.

3) Under the \<appSettings> section, add the following entry:

   ```
   <add key="stateless" value="true" />
   ```

4) Save the web.config file. Your changes will take affect immediately. |

## March 16, 2015: Version 2.1.10

**Enhancements**

* None

  (None to report for this release).

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-246    | Fixed an issue where the `distinguishedName` include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ad.adoc\[tags=AD]attribute wasn't being sent for provisioning. |
| ID-242    | Fixed an issue where the attribute were being converted to all lowercase.                                                                                           |

## February 25, 2015: Version 2.1.9

Enhancements

* ID-53

  We've added `immutableId` to the SCIM user object map in AD Connect outbound provisioning.

Resolved issues

| Ticket ID | Issue                              |
| --------- | ---------------------------------- |
| None      | (None to report for this release.) |

## January 10, 2015: Version 2.1.4

Enhancements

* include::pingone\_for\_enterprise:partial$p14e\_p1refs\_365.adoc\[tags=365]Active Profiles

  We've added support for Office 365 active profiles.

* Password Functionality

  We've added the ability to reset passwords for AD Connect.

Resolved issues

| Ticket ID | Issue                              |
| --------- | ---------------------------------- |
| None      | (None to report for this release.) |

## October 28, 2014: Version 2.0.45

Enhancements

* None

  (None to report for this release.)

Resolved issues

| Ticket ID | Issue                                                                     |
| --------- | ------------------------------------------------------------------------- |
| PINT-524  | Fixed exception when selecting CA signed certificate during installation. |

## October 7, 2014: Version 2.0.44

Enhancements

* None

  (None to report for this release.)

Resolved issues

| Ticket ID | Issue        |
| --------- | ------------ |
| Various   | Minor fixes. |

## August 26, 2014: Version 2.0.42

Enhancements

Resolved issues

| Ticket ID | Issue                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| PINT-277  | Fix an issue where the subject is missing when the user principal name (UPN) isn't specified for the user. |

## July 17, 2014: Version 2.0.39

Enhancements

* Authentication Lookup Parameters

  We've added support for configuration of authentication lookup parameters (such as attribute name and filter).

## June 24, 2014: Version 2.0.34

Enhancements

* New AD Connect

  AD Connect is now available without an IIS dependency. You now have the option to install "AD Connect" or "AD Connect with IIS".

* IWA Support

  We've added the option to use Integrated Windows Authentication (IWA) with AD Connect.

* SAML\_SUBJECT Value Changed

  The SAML\_SUBJECT value is changed to `userPrincipalName` rather than `sAMAccountName` as in previous AD Connect versions. You need to update your application attribute mappings if SAML\_SUBJECT is a source value for any of your application connections.

* SCIM Events

  We've added support for resending of user SCIM events on group monitoring changes.

* SCIM Attributes

  We now send only required SCIM attributes during provisioning.

* PingOne URL

  The new PingOne configuration URLs are now used.

* Certificate DN Parsing

  We've improved certificate DN parsing for AD Connect with IIS.

* Auto-Update

  We've improved the workflows for auto-update.

---

---
title: Previous PingOne for Enterprises releases
description: Enhancements
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_release_notes:p14e_relnotes_archive
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_release_notes/p14e_relnotes_archive.html
revdate: March 30, 2023
section_ids:
  february-2022: February 2022
  december-2021: December 2021
  october-2021: October 2021
  september-2021: September 2021
  august-2021: August 2021
  july-2021: July 2021
  june-2021: June 2021
  may-2021: May 2021
  april-2021: April 2021
  march-2021: March 2021
  december-2020: December 2020
  november-2020: November 2020
  october-2020: October 2020
  july-2020: July 2020
  july-2020-2: July 2020
  june-2020: June 2020
  may-2020: May 2020
  april-2020: April 2020
  march-2020: March, 2020
  january-2020: January, 2020
  november-2019: November, 2019
  september-2019: September, 2019
  july-2019: July, 2019
  june-2019: June, 2019
  may-2019: May, 2019
  april-2019: April, 2019
  march-2019: March, 2019
  february-2019: February, 2019
  january-2018: January, 2018
  december-2018: December, 2018
  november-2018: November, 2018
  october-2018: October, 2018
  september-2018: September, 2018
  august-2018: August, 2018
  july-2018: July, 2018
  june-2018: June, 2018
  may-2018: May, 2018
  april-2018: April, 2018
  march-2018: March, 2018
  january-february-2018: January - February, 2018
  december-2017: December, 2017
  november-2017: November, 2017
  october-2017: October, 2017
  september-2017: September, 2017
  august-2017: August, 2017
  july-2017: July, 2017
  june-2017: June, 2017
  april-may-2017: April-May, 2017
  march-2017: March, 2017
  february-2017: February, 2017
  january-2017: January, 2017
  december-2016-minor-release: "December, 2016: Minor Release"
  november-2016-minor-release: "November, 2016: Minor Release"
  october-2016-minor-release: "October, 2016: Minor Release"
  september-2016-minor-release: "September, 2016: Minor Release"
  august-30-2016-minor-release: "August 30, 2016: Minor Release"
  august-9-2016-minor-release: "August 9, 2016: Minor Release"
  july-19-2016-minor-release: "July 19, 2016: Minor Release"
  june-28-2016-minor-release: "June 28, 2016: Minor Release"
  june-15-2016-minor-release: "June 15, 2016: Minor Release"
  june-1-2016-major-release: "June 1, 2016: Major Release"
  may-17-2016-minor-release: "May 17, 2016: Minor Release"
  april-26-2016-minor-release: "April 26, 2016: Minor Release"
  april-19-2016-minor-release: "April 19, 2016: Minor Release"
  april-5-2016-minor-release: "April 5, 2016: Minor Release"
  march-15-2016-minor-release: "March 15, 2016: Minor Release"
  february-23-2016-minor-release: "February 23, 2016: Minor Release"
  february-2-2016-minor-release: "February 2, 2016: Minor Release"
  january-26-2016: January 26, 2016:
  january-19-2016: January 19, 2016:
  january-12-2016-minor-release: "January 12, 2016: Minor Release"
---

# Previous PingOne for Enterprises releases

## February 2022

**Enhancements**

| Feature                          | Description                                                                                                                                                                                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PingFederate Connection          | The latest version of PingFederate available for download through PingOne for Enterprise is 10.3.You can download later versions of PingFederate from [the Ping Identity main download site](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).                             |
| PingOne Connector                | * Fixed an issue that caused an error when trying update the population ID attribute.See **Known Issues and Limitations** below for important information.                                                                                                                                       |
| PingOne for Enterprise Directory | Notification emails sent to administrators when new users self-register now include a link to the **Users > User Directory > Users** menu where you can approve the new user.For more information, see [Approve new directory users](../pingone_for_enterprise/p14e_approve_new_p1d_users.html). |

## December 2021

**Enhancements**

| Feature                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Azure Conditional Access | Added the `MFA_SUBJECT` attribute to the Microsoft Azure AD identity repository configuration.If you're using PingID for Azure Conditional Access, the `MFA_SUBJECT` attribute in PingOne for Enterprise can be mapped the same as the `username` attribute in PingID.For more information, see [Connect to Azure](../pingone_for_enterprise/p14e_connect_azure.html) and [Configuring PingID MFA for Microsoft Azure AD Conditional Access](https://docs.pingidentity.com//pingid/pingid_integrations/pid_cfg_azure_conditional_access.html) in the PingID documentation. |
| Office 365 Connector     | Migrated the Office 365 Connector from the Azure AD Graph API 1.6 to the Microsoft Graph API 1.0See **Known Issues and Limitations** below\.Learn more in the [Office 365 Connector](https://docs.pingidentity.com//integrations/office365/pf_is_overview_of_office_365_integrations.html) documentation.                                                                                                                                                                                                                                                                  |
| SSO Admins               | Updated the **Account > Administrators** page to display all single sign-on (SSO) administrative users.Previously, SSO admins who were also registered in other PingOne for Enterprise accounts did not display.For more information, see [Assign administrative roles](../pingone_for_enterprise/p14e_assign_administrative_roles.html).                                                                                                                                                                                                                                  |

**Known issues and limitations**

| Subject              | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Office 365 Connector | * Opting out of license management for users is not supported. The connector will clear existing licenses even when the attribute is unmapped.

* Updating mobile attribute requires that the service principal representing the connector be assigned a role with Company Administrator privileges using Powershell. See [this KB article](https://support.pingidentity.com/s/article/O365-Connector-Mobile-attribute-updates) for more information.

* Updating the `Password` attribute is not supported.

* User updates containing a manager that has not yet been provisioned or updated by the new version will fail. Older version updates will not have the new extended attribute with their distinguished name (DN) from Active Directory.

* If the **DoBase64Conversion** field is switched to `false`, conflicts or failures will likely result on federated domains containing pre-existing users provisioned by dirsync/V1.0.

* Only outbound provisioning is supported.

* Group provisioning is not supported.

* Automatic licensing of users is not supported. |

## October 2021

**Enhancements**

| Feature           | Description                                                                                                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Connector | * Changed the **North America** region to **North America (US)**

* Added the **North America (Canada)** regionSee **Known Issues and Limitations** below for important information.                      |
| SSO/SLO           | Increased the `max-age` parameter of the `strict-transport-security` header for the `https://sso.connect.pingidentity.com/sso/` endpoint.The previous `max-age` was 1 year. The new `max-age` is 2 years. |

**Known issues and limitations**

| Subject           | Issue/Limitation                                                                                                                                                                                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Connector | * Clearing fields on updates is not supported.

* Multivalued attributes such as email or address are not supported. Multiple values appear as a single array on PingOne.

* Custom attributes are set when the user is initially created, and cannot be updated afterward. |

## September 2021

**Enhancements**

| Feature                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Custom Application Categories | Added the ability to create custom application categories.Custom application categories let you organize applications in ways that work best for your organization.For more information, see [Creating a custom application category](../pingone_for_enterprise/p14e_creating_custom_application_category.html).                                                                                                                                                                                                                                                                                                                                                                                                       |
| PingOne Connector             | * Added support for group provisioning

* Added the ability to select a default MFA device during user creation

* Added voice as an option for offline device pairing

* Fixed an issue that prevented all of a user's authentication methods from being provisioned if any of them were invalid.

* Fixed an issue that allowed duplicate local attributes to be defined when configuring an adapter.

* Fixed an issue that could cause an attribute containing an array of objects to be returned in the incorrect format.

* Fixed an issue that caused password validation to fail intermittently when the user's access token had expired.See **Known Issues and Limitations** below for important information. |
| Single Logout                 | Added support for the optional `idpid` parameter to all single logout (SLO) endpoints.If you specify the `idpid` value, the SLO operation is restricted only to sessions with the specified `idpid` value.For more information, see [PingOne for Enterprise and SLO](../pingone_for_enterprise/p14e_slo.html).                                                                                                                                                                                                                                                                                                                                                                                                         |
| SSO Admins                    | Updated the **Account > Administrators** page to display all single sign-on (SSO) administrative users.Previously, SSO admins who were also registered in other PingOne for Enterprise accounts did not display.For more information, see [Assign administrative roles](../pingone_for_enterprise/p14e_assign_administrative_roles.html).                                                                                                                                                                                                                                                                                                                                                                              |

**Known issues and limitations**

| Subject             | Issue/Limitation                                                                                                                                                                                                                                                                        |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Provisioner | Clearing fields on updates is not supported.Multivalued attributes, such as emails and addresses, are not supported. Multiple values appear as a single-array value in PingOne.Custom attributes are set when the user is initially created. They cannot be updated after they are set. |

## August 2021

**Enhancements**

| Feature             | Description                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------ |
| PingOne Provisioner | Added support for custom string attributes.See Known Issues and Limitations below for important information. |

**Known issues and limitations**

| Subject             | Issue/Limitation                                                                                                                                                                                                                                                                        |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Provisioner | Clearing fields on updates is not supported.Multivalued attributes, such as emails and addresses, are not supported. Multiple values appear as a single-array value in PingOne.Custom attributes are set when the user is initially created. They cannot be updated after they are set. |

## July 2021

**Enhancements**

| Feature             | Description                                                                                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin Portal Banner | Added a feature allowing you to display a banner message in the administrative portal.For more information, see [Adding a logo and banner message](../pingone_for_enterprise/p14e_adding_logo_banner_message.html). |

## June 2021

**Enhancements**

| Feature                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single Logout Flow               | Added a feature allowing administrators to choose how PingOne for Enterprise handles single logout (SLO) requests.For more information, see [Configure the dock when using PingOne for Enterprise Directory](../pingone_for_enterprise/p14e_configure_dock_when_using_p14e_directory.html) and [Configuring the dock when using an identity bridge](../pingone_for_enterprise/p14e_configuring_dock_when_using_identity_bridge.html). |
| PingID Device Administrator Role | Added a new administrative role to manage user PingID Device settings.For more information, see [Assign administrative roles](../pingone_for_enterprise/p14e_assign_administrative_roles.html).                                                                                                                                                                                                                                       |
| Read-Only Administrative Roles   | Added a feature allowing you to assign user groups to read-only versions of administrative roles.Read-only roles allow administrators to access the areas of the admin portal normally allowed by that role, but not to change settings.For more information, see [Configuring SSO to the PingOne for Enterprise admin portal](../pingone_for_enterprise/p14e_configuring_sso_p14e_admin_portal.html).                                |
| Password Policy                  | Changed the default password requirements for new accounts.Previous default settings required a minimum password length of 6 characters, with no requirement for special characters.New default settings require a minimum password length of 8 characters, and a minimum of one special character.This change only applies to new accounts.                                                                                          |

**Known issues and limitations**

| Subject            | Issue/Limitation                                                                                                                                                                                                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single Logout Flow | Single logout from the admin portal does not currently support redirect SLO flow\.If you select **Redirect** SLO flow for your users, your SSO admins should use the **Sign Off** button at the top right of the admin portal rather than signing off through the PingOne Dock. |

## May 2021

**Enhancements**

| Feature                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin-API Client              | Removed the ability to use special characters in the **Client Name** and **Description** fields when creating API clients.Special characters in these fields can present a security risk.If you have existing API clients that include special characters, you will be forced to remove the characters the next time you edit the client.For more information, see [Creating an Admin-API client](../pingone_for_enterprise/p14e_creating_admin_api_client.html). |
| Password Policy Customization | Added a feature giving PingOne for Enterprise for Managed Service Providers administrators the ability to permit their customer accounts to customize password policies.For more information, see [Configuring customer account service settings](../pingone_for_enterprise/p14e_configuring_customer_account_service_settings.html).                                                                                                                             |

## April 2021

**Enhancements**

| Feature                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin-API Client              | Removed the ability to use special characters in the **Client Name** and **Description** fields when creating API clients.Special characters in these fields can present a security risk.If you have existing API clients that include special characters, you will be forced to remove the characters the next time you edit the client.For more information, see [Creating an Admin-API client](../pingone_for_enterprise/p14e_creating_admin_api_client.html). |
| Password Policy Customization | Added a feature giving PingOne for Enterprise for Managed Service Providers administrators the ability to permit their customer accounts to customize password policies.For more information, see [Configuring customer account service settings](../pingone_for_enterprise/p14e_configuring_customer_account_service_settings.html).                                                                                                                             |

## March 2021

**Enhancements**

| Feature                           | Description                                                                                                                                                                                                                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OAuth Access Token                | Increased the allowed number of trusted origins for OAuth access token Cross-Origin Resource Sharing. The previous limit was 10. The current limit is 100.For more information, see [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html). |
| PingOne for Customers Provisioner | Added a new provisioner for PingOne for Customers.This provisioner includes:- Authoritative IdP attribute

- Default nicknames for email and SMSLearn more in [PingOne Integration Kit](https://docs.pingidentity.com//integrations/pingone/pf_p1_ik.html).                          |
| Self-Service Password Reset       | Reduced the lifetime of self-service user password reset from the sign on screen.Previously the password reset link was valid for 3 days. Currently the password reset link is valid for 24 hours.                                                                                   |

**Known issues and limitations**

| Subject                           | Issue/Limitation                               |
| --------------------------------- | ---------------------------------------------- |
| PingOne for Customers Provisioner | * Clearing fields on updates is not supported. |

## December 2020

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Aquera Provisioner     | Added a new provisioner for Aquera Connector. This is the initial release for this provisioner.This provisioner includes:- Support for user provisioning

- Support for SCIM core and enterprise attributes

- Support for bearer token and HTTP basic authentication

- configuration options for deprovisioning actionsLearn more in [Aquera Provisioner](https://docs.pingidentity.com//integrations/aquera/pf_aquera_connector.html) |
| SCIM SaaS Provisioner  | Fixed application/JSON headers for SCIM 1.1 requests.Added logic to avoid sending an empty `FormattedName` attribute.Learn more in [SCIM Provisioner](https://docs.pingidentity.com//integrations/scim/pf_scim_connector.html).                                                                                                                                                                                                          |
| ServiceNow Provisioner | Added support for the Orlando and Paris versions of Service Now\.Learn more in [ServiceNow Provisioner](https://docs.pingidentity.com//integrations/servicenow/pf_servicenow_connector.html).                                                                                                                                                                                                                                            |

**Known issues and limitations**

| Subject                | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ServiceNow Provisioner | * Outbound Group Provisioning and Memberships is not supported.

* Once set, user attributes cannot be cleared, only updated

* When provisioning to ServiceNow, all user accounts in ServiceNow must have a `UserName` (User ID). This is not a required field in ServiceNow, but it is required for provisioning to work due to the provisioner using this field to sync with pre-existing users in ServiceNow. If a user in ServiceNow resolves to `sAMAccountName` (the "standard" mapping in the provisioning channel), then the accounts will be linked.Users in ServiceNow without a `UserName` will cause errors in provisioning. Resolve this by ensuring every user has this field populated, even if they are not intended to be managed by the provisioner.

* When provisioning users, the `UserName` attribute must only contain URL-safe characters.

* When synchronizing roles with users, the role attribute must contain only URL-safe characters.

* If a new user is created with the same `UserName` as an existing user, a duplicate user will not be created. Instead, the existing user will be updated with any information in the creation.

* Due to limitations with the ServiceNow API, a role can be added to a user but not removed. This may cause a user's role in the source datastore to become out-of-sync with the user's role in ServiceNow. Learn more in [ServiceNow Provisioner](https://docs.pingidentity.com//integrations/servicenow/pf_servicenow_connector.html).

* When mapping the `roles` attribute, multiple additional calls to ServiceNow must be made to sync user role. This may impact provisioning performance.

* For department names that contain the ^ character, the ServiceNow API causes the creation of multiple departments with the same name.

* For the `department` object, the ServiceNow API ignores capitalization. When provisioning a user that matches multiple departments in ServiceNow (such as Accounting and accounting), PingFederate provisions the user with an empty department attribute and logs an error in `provisioner.log`. |
| SCIM SaaS Provisioner  | - Clearing fields on updates is not supported.

- Outbound Group Provisioning and Memberships is not supported.

- Patch updates to SCIM-enabled target applications are not supported.

- Multivalue attributes such as email, phone, and address have a limit of one value per type, such as home, work, or other.

- For multivalue attributes such as email, phone, and address, if the SaaS does not specify either type and primary information, or both type and primary information, the provisioner may behave in unexpected ways.Also, existing attributes on the SaaS might night be removed during an updated, and the desired value might not be correctly set as primary. \* SCIM-compliant service providers may implement or interpret the SCIM standards differently. This can result in behavior that is not consistent with the intended use of the SCIM SaaS Provisioner. \* The SCIM provisioner will not provision users until the users are updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## November 2020

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication Policy  | Added a feature that allows you to choose whether to authenticate SSO admins using their email or their SSO username.For more information, see [Create or update an authentication policy](../pingone_for_enterprise/p14e_create_update_authentication_policy.html).                                                                                                                                        |
| Administrator Settings | Added a feature that allows you to change the certificate expiration notification settings for Global and SaaS administrators.For more information, see [Editing administrative roles, permissions, and notifications](../pingone_for_enterprise/p14e_editing_administrative_roles_permissions_notifications.html) and [Manage your user profile](../pingone_for_enterprise/p14e_manage_user_profile.html). |
| Subscription API       | Added a new result status to PingID audit events.`UNSUCCESSFUL_ATTEMPT` represents an invalid one-time passcode (OTP) attempt that did not result in failed authentication.For more information about audit events, see [Get the audit events for a Poll subscription](../pingone_for_enterprise/p14e_get_audit_events_poll_subscription.html).                                                             |

**Known issues and limitations**

| Subject       | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single Logout | PingOne for Enterprise's single logout (SLO) implementation relies on the ability to send cookies within an iframe. [Safari now blocks this function by default](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/), which causes SLO to fail in most scenarios.We are working to accommodate this new behavior.This issue impacts SLO on the following browsers:- Safari 13.1+ on MacOS

- Safari on iOS and iPadOS 13.4+

- Any browser where the user has disabled third party cookiesYou can solve this problem by enabling third-party cookies in the browser settings. |

## October 2020

**Enhancements**

| Feature                        | Description                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin-API Clients              | Added a feature that allows you to create Admin-API clients to access subscription endpoints without the need for additional administrator accounts.For more information, see [Creating an Admin-API client](../pingone_for_enterprise/p14e_creating_admin_api_client.html)                                                                                             |
| AWS Single Sign-On Provisioner | Added a new provisioner for AWS Single Sign-On. This is the initial release for this provisioner.This provisioner includes:- Included support for user provisioning

- Included configuration for deprovisioning actionsSee Known Issues and Limitations below for important information.                                                                               |
| PingOne Directory              | Added a feature that directs a user to the specified redirect URL if they click on the registration URL after completing the registration process.For more information about self-registration, see [Allow self registration for new directory users](../pingone_for_enterprise/p14e_allow_self_registration_p1d_users.html).                                           |
| Signing Certificates           | Added a feature that allows administrators to designate a signing certificate as the default certificate for newly added application connections.For more information, see [Create a signing certificate](../pingone_for_enterprise/p14e_create_signing_certificate.html) and [View certificate details](../pingone_for_enterprise/p14e_view_certificate_details.html). |

**Known issues and limitations**

| Subject                        | Issue/Limitation                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| AWS Single Sign-On Provisioner | * This integration does not support group provisioning

* Once set, user attributes cannot be cleared, only updated |

## July 2020

**Enhancements**

| Feature             | Description                                                                                                                                                                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Directory   | Added a feature that allows administrators to enable additional directory attributes for use in attribute mapping for IdP, dock, and application configuration.For more information, see [Manage directory attributes](../pingone_for_enterprise/p14e_manage_p1d_attributes.html). |
| PingOne Provisioner | * Changed name from PingOne for Customers Provisioner to PingOne Provisioner

* Added the ability to manage PingOne MFA Email and SMS devices                                                                                                                                      |

**Known issues and limitations**

| Subject             | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Provisioner | * Clearing fields on updates is not supported.

* Outbound Group Provisioning and Memberships is not supported.

* Patch updates to SCIM-enabled target applications are not supported.

* There is a limit of one value per type (such as, home, work, other) for multivalue attributes (email, phone, address).

* Unexpected behavior may occur if the SaaS application does not specify either type and primary information, or both type and primary information for multivalue attributes (email, phone, address). Also, existing attributes on the application may not be removed during an update, and the desired value may not be correctly set as primary.

* SCIM-compliant service providers may implement or interpret the SCIM standards differently. This can result in behavior that is not consistent with the intended use of the SCIM SaaS provisioner. |

## July 2020

**Enhancements**

| Feature      | Description                                                                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Concur 1.0.1 | * Fixed an issue that prevented users from being updated in Concur. Learn more in [Concur Provisioner](https://docs.pingidentity.com//integrations/concur/pf_concur_connector.html). |

## June 2020

**Enhancements**

| Feature                     | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Atlassian Cloud Provisioner | * Initial release

* Includes SAML 2.0 support for IdP- and SP-initiated SSO

* Included support for user provisioning

* Included configuration for deprovisioning actions

* Learn more in [Atlassian Cloud Provisioner](https://docs.pingidentity.com//integrations/atlassian/atlassian_cloud_provisioner/pf_atlassian_cloud_connector.html).                                                |
| ServiceNow Connector 2.2    | - Added the ServiceNow URL field and removed the ServiceNow Instance Name field

- Fixed an issue that caused an error when assigning a role that was not also assigned to the provisioning user account

- Added support for the Orlando version of ServiceNow

- Learn more in [ServiceNow Provisioner](https://docs.pingidentity.com//integrations/servicenow/pf_servicenow_connector.html). |

**Known issues and limitations**

| Subject                     | Issue/Limitation                                                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Atlassian Cloud Provisioner | * Clearing fields on updates is not supported

* This integration does not support group provisioning

* Once set, user attributes can only be updated, not cleared |

## May 2020

**Enhancements**

| Feature                            | Description                                                                                                                                                                                                                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Code42 Provisioner                 | * Initial release.

* Included support for user provisioning.

* Learn more in [Code42 Integration Guide for PingFederate](https://docs.pingidentity.com//integrations/code42-pingfederate/pf_code42_integration.html).                                                                          |
| ZScaler Private Access Provisioner | - Initial release.

- Included support for user provisioning.

- Included configuration for deprovisioning actions.

- Learn more in [Zscaler Private Access Provisioner](https://docs.pingidentity.com//integrations/zscaler/zscaler_private_access_provisioner/pf_zscaler_zpa_connector.html). |

**Known issues and limitations**

| Subject                            | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code42 Provisioner                 | * User attributes cannot be cleared once set. They can only be updated.

* This integration does not support group provisioning.

* Deleting the administrative user that is set up for provisioning may lead to undesired consequences. The provisioner makes the administrative user the owner and member of each group that is created by the provisioner. We recommend not deleting the administrative user and not managing this user through the provisioner. |
| Zscaler Private Access Provisioner | - This integration does not support group provisioning.

- Once set, user attributes can only be updated, not cleared.

- Deleting the administrative user that is set up for provisioning may lead to undesired consequences. The provisioner makes the administrative user the owner and member of each group that is created by the provisioner. We recommend not deleting the administrative user and not managing this user through the provisioner.           |

## April 2020

**Enhancements**

| Feature                     | Description                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AD Connect agent management | * Added a feature allowing administrators to view and manage AD Connect nodes from PingOne portal. See [View and manage AD Connect agent nodes](../pingone_for_enterprise/p14e_view_manage_adc_agent_nodes.html) for more information.                                                                                                               |
| Metadata Download URL       | - Added a feature to generate a shareable metadata URL for applications and the configured SAML IdP. See [Adding or updating a SAML application](../pingone_for_enterprise/p14e_add_update_saml_application.html) and [Connecting to a custom SAML provider](../pingone_for_enterprise/p14e_connect_custom_saml_provider.html) for more information. |
| Session Idle Timeout        | * Added a setting to the **Setup > Dock** menu allowing administrators to set the time that a user session can be idle before the session is automatically signed out.                                                                                                                                                                               |
| Slack Connecter             | - Added Support for handling rate-limiting responses from Slack.                                                                                                                                                                                                                                                                                     |
| Zoom Connector 1.0          | * Initial release.

* Included support for user provisioning.

* Included support for Zoom attributes.

* Included support for API key and secret authentication.

* Included configuration options for deprovisioning actions.

* Learn more in [Zoom Provisioner](https://docs.pingidentity.com//integrations/zoom/pf_zoom_connector.html).        |

**Known issues and limitations**

| Subject            | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zoom Connector 1.0 | * This integration does not support group provisioning.

* Once set, user attributes can only be updated, not cleared.

* Zoom only allows a single value for the `Roles` attribute.

* Deleting the administrative user that is set up for provisioning may lead to undesired consequences. The provisioner makes the administrative user the owner and member of each group created by the provisioner. We recommend not deleting the administrative user and not managing the user through the provisioner.

* Due to a limitation in Zoom, if a user's attributes change at the same they are enabled or disabled, only the `disabled` status is updated in Zoom. The attributes are updated the next time a change is made to that user.

* Zoom does not allow users with the admin role to be disabled or deleted. Change the user's role first. |

## March, 2020

**Enhancements**

| Feature                     | Description                                                                                                                                                                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SCIM Provisioner            | * Added support for the application/scim+json HTTP header type

* Improved the SCIM URL field in the connection configuration to work either with or without a trailing slash (/) in the URL                                                  |
| Zscaler ZIA Provisioner 1.1 | - Renamed the integration to "Zscaler Internet Access" to match official branding

- Added the ability to update the username attribute in Zscaler

- Improved error handling and reporting when encountering a user that does not have an ID |

**Known issues and limitations**

| Subject                     | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zscaler ZIA Provisioner 1.1 | The following limitations apply:- Clearing fields on updates is not supported.

- Deleting the administrative user that is set up for provisioning may lead to undesired consequences. The provisioner makes the administrative user the owner and member of each group that is created by the provisioner. We recommend not deleting the adminstrative user and not managing this user through the provisioner. |

## January, 2020

**Enhancements**

| Feature  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Branding | We've expanded the branding options for the PingOne dock as well as the AD Connect and PingOne Directory login screens. We have also added new branding options for intermediate SSO screens including error, SLO, and IdP Discovery screens. Finally we have reorganized the branding screens in the PingOne admin portal. See [Assign branding and design](../pingone_for_enterprise/p14e_assign_branding_designn.html) for more information. |

**Resolved issues**

| Ticket ID | Issue                                                                        |
| --------- | ---------------------------------------------------------------------------- |
| SSD-12791 | Fixed an issue to allow non-HTTPS URI redirects in OIDC mobile applications. |

## November, 2019

**Enhancements**

| Feature                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OAuth refresh tokens                        | We've added support for OAuth refresh tokens with OpenID Connect applications. See [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html) and [Adding or updating an OIDC application](../pingone_for_enterprise/p14e_add_update_oidc_application.html) for more information.                                                                                                                                                                                                                                                                                                                      |
| Updated provisioner for ServiceNow          | We've updated the provisioner for Salesforce. The update to this provisioner includes support for:- Added support for the London, Madrid, and New York versions of ServiceNow.

- Added support for mapping users to departments in ServiceNow.

- Improved user ID validation when updating and deleting users.

- Removed support for the Jakarta and Istanbul versions of ServiceNow.	This is an update to the existing ServiceNow provisioner (Kingston, Jakarta, Istanbul). It has also been rebranded from "ServiceNow (Kingston, Jakarta, Istanbul)" to "ServiceNow".See **Known Issues and Limitations** for important information. |
| Delegated administration of applications    | We've added an Application Administrator role and the ability for you to delegate administration of applications to an Application Administrator. See [Assign Application Administrator applications](../pingone_for_enterprise/p14e_assign_application_administrator_applications.html) for more information.                                                                                                                                                                                                                                                                                                                              |
| SLO for OpenID Connect applications         | We've added single logout (SLO) support for OpenID Connect (OIDC) applications. See the **Logout URI** when adding an OIDC application, or [Adding or updating an OIDC application](../pingone_for_enterprise/p14e_add_update_oidc_application.html) for more information.                                                                                                                                                                                                                                                                                                                                                                  |
| Disable inactive users in PingOne directory | We've added the ability for you to disable users who've been inactive for an extended period of time. See [Disable directory users](../pingone_for_enterprise/p14e_disable_p1d_users.html) for more information.                                                                                                                                                                                                                                                                                                                                                                                                                            |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                             |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| IO-5615   | (Slack provisioner) Fixed an issue that caused the connector to update the wrong phone number attribute as a result of a change in the Slack API. |
| SSD-12509 | Fixed an issue in Google Chrome where a SameSite=none setting in cookies was affecting SSO.                                                       |
| SSD-12579 | Fixed an issue where PingOne directory error messages weren't displaying single quotes.                                                           |

**Known issues and limitations**

| Subject                | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ServiceNow provisioner | The following limitations apply:- For departments that contain the "^" (caret) character in the name, the ServiceNow API causes the creation of multiple departments with the same name.

- For the department object, the ServiceNow API ignores capitalization. When provisioning a user that matches multiple departments in ServiceNow (such as, Accounting and accounting), PingOne provisions the user with an empty department attribute and logs an error in the Dashboard Report.

- `Outbound Group Provisioning` and `Memberships` are not supported.

- User attributes cannot be cleared once set. They can only be updated.

- When provisioning to ServiceNow, all user accounts in ServiceNow must have an assigned `username` (User ID) value. This is not a required field in ServiceNow. However, because the provisioner must use this field to sync with pre-existing users in ServiceNow, it is required for provisioning to function. If a user in ServiceNow resolves to sAMAccountName (the "standard" mapping in the provisioning channel), the accounts will be linked. Currently, if users exist in ServiceNow without an assigned UserName value, this will cause errors in provisioning. In this case, you can resolve the issue by ensuring every user has an assigned UserName, even if they are not intended to be managed by the provisioner.

- When provisioning users, the `username` attribute must contain only URL-safe characters.

- When synchronizing roles with users, the `role` attribute must contain only URL-safe characters.

- If a new user is created with the same `username` as an existing user, a duplicate user will not be created. Instead, the existing user will be updated with any information assigned.

- Due to limitations with the ServiceNow API, a role can be added to a user but not removed, which may cause a user's role in the source data store to become out of sync with the user's role in ServiceNow. For more information, see [Adding the Ping Identity provisioning role in ServiceNow](https://docs.pingidentity.com/bundle/integrations/page/pzq1563995052451.html).

- When mapping the `roles` attribute, multiple calls to ServiceNow must be made to sync the user role information. This may impact provisioning performance. |

## September, 2019

**Enhancements**

| Feature                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adding OIDC applications           | We've updated the selection and configuration of OIDC applications, streamlining this process based on the type of OIDC application connection you want to add. See [Adding or updating an OIDC application](../pingone_for_enterprise/p14e_add_update_oidc_application.html) for more information.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Encryption certificates            | We've added management of encryption certificates to the certificate management page (**Setup > Certificates**). You can choose the encryption certificate used for an application. See [Update an encryption certificate](../pingone_for_enterprise/p14e_update_encryption_certificate.html) for more information.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Administrators and SSO             | We've updated the Administrators page so that when an assigned administrator first signs on (SSO) to the admin portal, they're automatically added to the list of administrators displayed on the **Account > Administrators** page. See [Assign administrative roles](../pingone_for_enterprise/p14e_assign_administrative_roles.html) for more information.                                                                                                                                                                                                                                                                                                                                                        |
| Browser extension updated          | The browser extension (used for Basic SSO password vaulting) has been updated to version 2.54.9. This update included a fix for an unexpected prompt to restart the browser extension.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Updated provisioner for Salesforce | We've updated the provisioner for Salesforce. The update to this provisioner includes support for:- Provisioning to Salesforce Community Cloud (customer, partner, and custom communities).

- Provisioning to custom Salesforce domains.

- Version 46.0 of the Salesforce REST API.

- Configuring options to manage permission sets by merging or overwriting.

- Additional salesforce attributes.

- Improved error handling and reporting for cases where users in the target application do not have an ID.

- Improved error handling and reporting for cases where groups are updated or deleted but do not exist in the target application.See **Known Issues and Limitations** for important information. |

**Resolved issues**

| Ticket ID                        | Issue                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| (Browser extension) Staging-8549 | Fixed an issue where users were unexpectedly prompted to restart the browser extension.                                                |
| IO-5467                          | Fixed an issue that prevented users with certain special characters from being provisioned to Salesforce.                              |
| SSD-12043                        | Fixed an issue where the SAML\_SUBJECT attribute was not appearing in the attributes dropdown list in Advanced Attribute Mapping mode. |

**Known issues and limitations**

| Subject                | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Salesforce provisioner | The following limitations apply:- The provisioner cannot clear user attributes once they have been set.

- This provisioner does not support custom attributes.

- The Salesforce provisioner does not support hard deleting users in Salesforce. When users are enabled/disabled or deleted in your user store, the user will only be soft deleted (enabled/disabled) accordingly in Salesforce.

- The `username` attribute must be in an email format.

- The `alias` attribute can be no more than 8 characters.

- Group provisioning is not supported.

- Deprovisioning:

  * When deprovisioning a Salesforce customer or partner user, the provisioning connector does not unlink the user from the associated contact.

  * If a customer or partner user is unlinked in Salesforce from the associated contact, any changes to the user in the data store will cause the provisioner to create a new user in Salesforce and link it to the existing contact.

  * Guest users in Salesforce cannot be frozen. If **Freeze users** instead of **Disable** is selected in your provisioning options, the guest user will not be disabled or frozen.

- Salesforce Communities:

  * The provisioner can link users to "customer" and "partner" business accounts, but not to "person" accounts. See *Accounts* in the Salesforce documentation. |

## July, 2019

**Enhancements**

| Feature                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne directory user passwords            | We've updated the PingOne directory user password process for new users. Now after you create a new user, the user must change their assigned password when they first sign on. See [Add directory users](../pingone_for_enterprise/p14e_add_p1d_users.html) for more information.                                                                                                                                                                                                                                                                    |
| Updated provisioner for WebEx®              | We've updated the provisioner for WebEx. The update to this provisioner includes:- Fixed an issue that prevented users with special characters from being provisioned to WebEx.

- Improved error handling and reporting for cases where users in the target application do not have an ID.

- Improved error logging security.

- Fixed an issue that caused a user to be recreated when the provisioning engine tried to delete or disable a user that was already deleted in WebEx.See **Known Issues and Limitations** for important information. |
| Updated provisioner for Amazon Web Services | We've updated the provisioner for Amazon Web Services (AWS). The update to this provisioner includes:- Support for the AWS 2.0 API.

- Support for the Password and PasswordResetRequired attributes.

- Support for updating the UserName attribute.

- Improved error-handling and reporting behavior.See **Known Issues and Limitations** for important information.                                                                                                                                                                               |
| PingFederate                                | PingFederate is now the default PingFederate identity bridge for PingOne. It's a light-weight version of PingFederate designed for quick and easy configuration with PingOne. See .pingidentity.com/pingfederatebridge/pf93///\[Introduction to PingFederate] and [Connect to PingFederate](../pingone_for_enterprise/p14e_connect_pf.html) for more information.                                                                                                                                                                                     |
| Admin portal SSO for multiple groups        | You can now assign multiple groups to administrative roles for the purpose of SSO to the PingOne admin portal from the PingOne dock. We've also created a new page for this assignment: **Setup > Dock > Admin Portal SSO**. See [Configure SSO from the dock to the admin portal](../pingone_for_enterprise/p14e_configure_sso_from_the_dock_to_the_admin_portal.html) for more information.                                                                                                                                                         |
| Ping directory branding                     | We've added the ability for you to brand PingOne directory pages for your organization. See [Assign directory branding and designs](../pingone_for_enterprise/p14e_assign_p1d_branding_design.html) for more information.                                                                                                                                                                                                                                                                                                                             |
| SSO reports                                 | You can now apply filtering to SSO reports based on specific applications. See [Run a predefined report](../pingone_for_enterprise/p14e_run_predefined_report.html) or [Run a custom report](../pingone_for_enterprise/p14e_run_custom_report.html) for more information.                                                                                                                                                                                                                                                                             |
| Supported languages                         | PingOne UI components now support the use of more languages. See [PingOne for Enterprise language support](../pingone_for_enterprise/p14e_language_support.html) for more information.                                                                                                                                                                                                                                                                                                                                                                |

**Known issues and limitations**

| Subject                         | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WebEx provisioner               | The following limitations apply:- The provisioner cannot re-enable user meeting types that have been disabled through the Webex administration console. If the provisioner tries to update the user's meeting types in this scenario, it can cause all meeting types for that user to be disabled.

- The WebEx ID attribute is not updateable in PingOne.

- The MeetingType attribute is limited to one value in PingOne (not a multivalued attribute).

- Due to API Limitations, WebEx doesn't allow a user to be created in a suspended state. WebEx will automatically activate the user after it is created. |
| Amazon Web Services provisioner | The following limitations apply:- Group Provisioning is not supported.

- Deprovisioning:

  * AWS does not support disabled users. These users are deleted instead.

- Attributes:

  * When a user is created with a passwordResetRequired value other than "true" or "TRUE", the provisioning connector sets the value to "false" in AWS.

  * Clearing fields on updates is not supported.                                                                                                                                                                                                                      |

## June, 2019

**Enhancements**

| Feature                                         | Description                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingFederate                                    | PingFederate is now the default PingFederate identity bridge for PingOne for Enterprise. It's a light-weight version of PingFederate designed for quick and easy configuration with PingOne. See .pingidentity.com/pingfederatebridge/pf93///\[Introduction to PingFederate] and [Connect to PingFederate](../pingone_for_enterprise/p14e_connect_pf.html) for more information.              |
| Admin portal SSO for multiple groups            | You can now assign multiple groups to administrative roles for the purpose of SSO to the PingOne admin portal from the PingOne dock. We've also created a new page for this assignment: **Setup > Dock > Admin Portal SSO**. See [Configure SSO from the dock to the admin portal](../pingone_for_enterprise/p14e_configure_sso_from_the_dock_to_the_admin_portal.html) for more information. |
| Ping directory branding                         | We've added the ability for you to brand PingOne directory pages for your organization. See [Assign directory branding and designs](../pingone_for_enterprise/p14e_assign_p1d_branding_design.html) for more information.                                                                                                                                                                     |
| SSO reports                                     | You can now apply filtering to SSO reports based on specific applications. See [Run a predefined report](../pingone_for_enterprise/p14e_run_predefined_report.html) or [Run a custom report](../pingone_for_enterprise/p14e_run_custom_report.html) for more information.                                                                                                                     |
| Supported languages                             | PingOne UI components now support the use of more languages. See [PingOne for Enterprise language support](../pingone_for_enterprise/p14e_language_support.html) for more information.                                                                                                                                                                                                        |
| Basic SSO option                                | We've added an option for you to enable Basic SSO on the **Setup > Dock > Configurations** page in the admin portal. When enabled, you'll use the browser extension to add apps for Basic SSO. See [Basic SSO (password vaulting)](../pingone_for_enterprise/p14e_basic_sso.html) for more information.                                                                                       |
| Basic SSO browser extension new field available | We've updated the browser extension used for Basic SSO apps to support an additional field for use when training the browser extension to sign on to a Basic SSO app. The additional (third) field is optional and is supplied for those apps that require sign-on information in addition to the user name and password fields.                                                              |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IO-5262   | (Provisioning) Fixed an issue where disabling users in the user source without a synchronized user in a target SaaS could result in a new user being created in the SaaS. The affected PingOne apps are:- Amazon Web Services

- Box

- Concur

- Dropbox

- Egnyte

- Github

- Google

- Lucidchart

- Office 365

- Ping IDaaS Directory Provisioner

- PingOne for Customers Provisioner

- Ping IDaaS Generic Scim Provisioner

- Salesforce

- ServiceNow Jakarta

- Slack

- WebEx

- Workplace by Facebook

- Zendesk

- Zscaler |
| SSD-11699 | Fixed an issue in PingOne directory where a user having the same email address could not be recreated being deleted.                                                                                                                                                                                                                                                                                                                                                                                                                     |

## May, 2019

**Enhancements**

| Feature                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Basic SSO option                                | We've added an option for you to enable Basic SSO on the **Setup > Dock > Configurations** page in the admin portal. When enabled, you'll use the browser extension to add apps for Basic SSO. See [Basic SSO (password vaulting)](../pingone_for_enterprise/p14e_basic_sso.html) for more information.                                                                                                                                                                                                                    |
| Basic SSO browser extension new field available | We've updated the browser extension used for Basic SSO apps to support an additional field for use when training the browser extension to sign on to a Basic SSO app. The additional (third) field is optional and is supplied for those apps that require sign-on information in addition to the user name and password fields.                                                                                                                                                                                           |
| Updated provisioner for PingOne for Customers   | We've updated the provisioner for PingOne for Customers. This provisioner is intended for existing PingOne for Enterprise accounts using either PingOne directory or AD Connect who want to migrate their users to PingOne for Customers. The update to this provisioner includes:- Fixed an issue that prevented users with empty attributes from being provisioned to PingOne for Customers.

- Removed support for obsolete scopes from the provisioner.See **Known Issues and Limitations** for important information. |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                    |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BE-2752   | (Browser extension) Fixed an issue where the browser extension wasn't properly replaying an app in Chrome resulting in the Login button not functioning. |
| SSD-11636 | Fixed an issue where a CSR response could not be uploaded to PingOne.                                                                                    |
| SSD-11595 | Fixed an issue where the PingOne attribute mapping for PingFederate defaulted to `sub` instead of `SAML_SUBJECT` as expected.                            |
| SSD-11570 | Fixed an issue where the activation key for a PingOne 30 day trial account was not accepted by PingFederate.                                             |
| SSD-11351 | Fixed an issue where a routing for a PingFederate connection was being retained to a Ping data center that was no longer being used.                     |

**Known issues and limitations**

| Subject                           | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne for Customers provisioner | The following limitations apply:\* Clearing fields on updates is not supported. \* Outbound Group Provisioning and Memberships is not supported. \* Patch updates to SCIM-enabled target applications are not supported. \* There is a limit of one value per type (such as, home, work, other) for multivalue attributes (email, phone, address). \* Unexpected behavior may occur if the SaaS application does not specify either type and primary information, or both type and primary information for multivalue attributes (email, phone, address). Also, existing attributes on the application may not be removed during an update, and the desired value may not be correctly set as primary. \* SCIM-compliant service providers may implement or interpret the SCIM standards differently. This can result in behaviour that is not consistent with the intended use of the SCIM SaaS provisioner. |

## April, 2019

**Enhancements**

| Feature                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne registration page                                                                                | We've updated the UI for the registration page, administrator login, and password recovery. Most importantly, we've added the selection of the PingOne data center to use for the new account. See [Registering a PingOne for Enterprise account](../pingone_for_enterprise/p14e_register_p14e_account.html) for more information.                                                                |
| Identity repository setup                                                                                | We've updated the UI for identity repository setup and added an attribute mapping option enabling you to configure the attribute mapping from the identity provider to the standard set of PingOne SSO attributes.                                                                                                                                                                                |
| Microsoft include::pingone\_for\_enterprise:partial$p14e\_p1refs\_azure.adoc\[tags=Azure]identity bridge | We've added an identity bridge for Azure, with the option to synchronize groups from your Azure tenant to PingOne for Enterprise. See [Connect to Azure](../pingone_for_enterprise/p14e_connect_azure.html) for more information.                                                                                                                                                                 |
| Microsoft ADFS identity bridge                                                                           | We've added an identity bridge for Active Directory Federation Services (ADFS). See [Connect to ADFS](../pingone_for_enterprise/p14e_connect_adfs.html) for more information.                                                                                                                                                                                                                     |
| Group assignment                                                                                         | You can now authorize groups for application access as part of the application setup for SAML, OIDC, or Application Catalog applications.                                                                                                                                                                                                                                                         |
| Pingone directory self-registration                                                                      | If you're using PingOne directory as your identity repository, you can now assign the email domains that can be used for self-registration. If you choose not to assign the email domains, then all domains can be used for self-registration. See [Allow self registration for new directory users](../pingone_for_enterprise/p14e_allow_self_registration_p1d_users.html) for more information. |
| Cross-origin resource sharing (CORS) for OpenID Connect                                                  | If you're integrating OpenID Connect (OIDC) applications with PingOne, you can now configure one or more trusted origins to enable cross-origin resource sharing (CORS). See [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html) for more information.                                                                                                |
| SAML response signing                                                                                    | If you're integrating SAML applications with PingOne, you can now configure whether PingOne for Enterprise signs the SAML assertion or the SAML response that is sent to the application during SSO. See [Adding or updating a SAML application](../pingone_for_enterprise/p14e_add_update_saml_application.html) for more information.                                                           |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-10739 | (Ping directory) Fixed an issue where a user was invited and confirmed the email activation, but the user wasn't provisioned to Ping directory until another user was created or invited. |
| SSD-11230 | Fixed an issue where the SAML response signing selection for existing connections defaults to signing the assertion.                                                                      |

## March, 2019

**Enhancements**

| Feature               | Description                                                                                                                                                                                                                                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SCIM SaaS provisioner | We've updated the provisioner for SCIM SaaS applications. This provisioner includes:- Configuration options for the Unique User Identifier (userName or workEmail) which is used to search for users in the target application.See **Known Issues and Limitations** for important information. |

**Known issues and limitations**

| Subject                           | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PingOne for Customers provisioner | The following limitations apply:- Clearing fields on updates is not supported.

- Outbound Group Provisioning and Memberships is not supported.

- Patch updates to SCIM-enabled target applications are not supported.

- There is a limit of one value per type (such as, home, work, other) for multivalue attributes (email, phone, address).

- Unexpected behavior may occur if the SaaS application does not specify either type and primary information, or both type and primary information for multivalue attributes (email, phone, address). Also, existing attributes on the application may not be removed during an update, and the desired value may not be correctly set as primary.

- SCIM-compliant service providers may implement or interpret the SCIM standards differently. This can result in behaviour that is not consistent with the intended use of the SCIM SaaS provisioner. |

## February, 2019

**Enhancements**

| Feature                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New provisioner for PingOne for Customers | We've added a new provisioner for PingOne for Customers. This provisioner is intended for existing PingOne for Enterprise accounts using either PingOne directory or AD Connect who want to migrate their users to PingOne for Customers. This provisioner includes:\* Support for user provisioning. \* Support for user attributes: Username, Email, Population ID, Account ID, City, Country, External ID, First Name, Force Change Password, Full Name, Honorific Prefix, Honorific Suffix, Job Title, Last Name, Locale, Middle Name, Mobile Phone, Nickname, Password, Preferred Language, Primary Phone, Profile Image, State/Region, Street Address, Timezone, User Type and ZIP Code.See **Known Issues and Limitations** for important information. |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-10517 | Fixed an issue where user provisioning to PingOne directory failed when switching to the PingOne directory from either a PingFederate or AD Connect identity bridge. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

**Known issues and limitations**

| Subject                           | Issue/Limitation                                                               |
| --------------------------------- | ------------------------------------------------------------------------------ |
| PingOne for Customers provisioner | The following limitations apply:- Clearing fields on updates is not supported. |

## January, 2018

**Enhancements**

| Feature                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OpenID Connect custom scopes | We've added OAuth configuration settings for OpenID Connect applications to enable you to define custom scopes or to modify existing scopes with custom or standard claims. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Configure the access token].                                                                                                                                                                                                                                                                                                                              |
| PingOne redirect URI         | We've updated the PingOne redirect URI to include a verification code unique to your account. The redirect URI used by your OpenID Connect provider for PingOne must include the verification code for SSO to be successful. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Connect to OpenID Connect].                                                                                                                                                                                                                                                                              |
| Audit & Report administrator | We've added a dedicated administrator role for working with the audit event streaming and polling capabilities. The Audit & Report administrator is restricted to accessing the PingOne Dashboard and the Reporting and Subscriptions pages. The Audit & Report administrator can also access the API for polling audit events when audit subscriptions are configured as polling subscriptions. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Assign administrative roles] and .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Managing reports and subscriptions]. |
| SSO reporting                | We've added new report types and predefined reports for SSO transactions. For more information, see .pingidentity.com/pingone/saasSsoAdminGuide/index.shtml//\[Report types] and .pingidentity.com/pingone/saasSsoAdminGuide/index.shtml//\[Report event information].                                                                                                                                                                                                                                                                                                                                                         |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                                                                                                                                    |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-10353 | Fixed an issue where access to the PingOne admin portal generated an error when the PingOne authentication policy applied multi-factor authentication for SSO to the admin portal.                                                                                                                                                       |
| SSD-10402 | Fixed an issue that occurred while adding a new SAML application. The signing certificate selected during the configuration process was not being used for the signing certificate download link displayed on the summary page at the end of the configuration process. Instead, the download link used the default signing certificate. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

## December, 2018

**Enhancements**

| Feature                      | Description                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenID Connect custom scopes | We've added OAuth configuration settings for OpenID Connect applications to enable you to define custom scopes or to modify existing scopes with custom or standard claims. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Configure the access token].                                                 |
| PingOne redirect URI         | We've updated the PingOne redirect URI to include a verification code unique to your account. The redirect URI used by your OpenID Connect provider for PingOne must include the verification code for SSO to be successful. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Connect to OpenID Connect]. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

## November, 2018

**Enhancements**

| Feature                                | Description                                                                                                                                                                                                                                                                                                      |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenID Connect query parameters        | We've updated the OpenID Connect repository configuration to enable you to specify additional query parameters for the authentication request PingOne sends to the OpenID Connect provider. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Connect to OpenID Connect]. |
| PingOne dock and SSO session lifetimes | We've updated the PingOne dock to use the same session lifetime as the SSO session. The PingOne dock and SSO session can now be set to as low as 15 minutes. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Configure the dock when using an identity bridge].         |
| Turkish language support               | We've updated the PingOne user interface to include support for Turkish. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[PingOne language support].                                                                                                                     |

**Resolved issues**

| Ticket ID | Issue                                                                                                                              |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| SSD-9795  | Fixed an issue where users who are members of a large number of groups were unable to use SafeNet for multi-factor authentication. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

## October, 2018

**Enhancements**

| Feature                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include::partial$p14e\_p1refs\_github.adoc\[tags=Github]provisioner | We've a new provisioner for Github applications. This provisioner includes:- Added support for user provisioning.

- Added support for user attributes: Username, Email, First Name, Last Name and External ID.See **Known Issues and Limitations** for important information.                                                                                                                                                                                                                                                                                            |
| Administrative auditing (reports and subscriptions)                 | Administrative auditing is now available PingOne for Enterprise, PingID and PingOne SSO for SaaS Apps. You can utilize the administrative audit events through both the Reports and the Subscriptions facilities .                                                                                                                                                                                                                                                                                                                                                        |
| PKCE support for OpenID Connect (OIDC)                              | We've added support for Proof Key for Code Exchange (PKCE) to secure OIDC clients that cannot or choose not to use a client secret. We have therefore relaxed the requirement that a client secret must be specified when configuring an OIDC application with the authorization code flow. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Integrate an OIDC application, PKCE parameters]For more information, see .pingidentity.com/pingone/saasSsoAdminGuide/index.shtml//\[Integrate an OIDC application, PKCE parameters]. |
| SLO for OIDC identity providers                                     | We've added single logout (SLO) support for PingOne for Enterprise OIDC identity providers (IdPs). You can specify the end-session URL through the well-known metadata of the OpenID Connect provider (end\_session\_endpoint), or when you configure the PingOne connection for the OIDC IdP. When SLO is triggered, PingOne redirects the user logout process to the end-session URL for the OIDC IdP.                                                                                                                                                                  |
| Automatic IdP Discovery                                             | We've added automatic IdP discovery for all PingOne for Enterprise managed applications (applications managed by your account, rather than a service provider). For these applications, we no longer require that you specify the idpid for SP-initiated (SAML) requests or OIDC authorization requests.                                                                                                                                                                                                                                                                  |
| SAML assertion available in reports                                 | For SAML applications, we've added an enhancement to reports for you to display the SAML assertion for a failed SSO audit event included in a report. You can click on the failure code to display a popup containing the SAML assertion.                                                                                                                                                                                                                                                                                                                                 |
| PingOne directory enhancements                                      | We've added features to PingOne directory allowing you to:- Configure the reply-to email address used for PingOne Directory user invitations. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Allow self registration for new directory users].

- Enable or disable the password expiry and password lockout notification emails sent to PingOne Directory users. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Allow self registration for new directory users].                    |
| include::partial$p14e\_p1refs\_faw\.adoc\[tags=faw]provisioner      | We've updated the provisioner for Workplace by Facebook applications. This provisioner includes:- Improved error handling and reporting when Workplace by Facebook users contain no ID.

- Improved check connection call by not retrieving a list of users.See **Known Issues and Limitations** for important information.                                                                                                                                                                                                                                               |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

**Known issues and limitations**

| Subject                           | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Github provisioner                | The following limitations apply:- Clearing fields on updates is not supported.

- Enabling a previously deleted user in GitHub will trigger a create operation.

- When a user is deleted from GitHub they are removed from the organization. The user will still have a GitHub account but no access to the organization's resources.

- Due to GitHub API limitations, provisioning with multiple threads or making more than 5000 requests per hour may trigger GitHub's abuse detection mechanism, rate-limiting, or both. This will prevent requests from being completed. For more information, see .github.com/v3///\[Github rate-limiting].                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Workplace by Facebook provisioner | The following limitations apply:- Clearing fields on updates is not supported.

- Due to API limitations with matching a user's manager using the display name, if multiple matches occur the first match will be used. This could be an issue if multiple employees in the Workplace by Facebook account have the same first and last names. To avoid conflicts, you can use a custom attribute mapping to link the manager attribute to a manager's email.

- Due to LDAP limitations, when you update a manager's name it does not update their Distinguished Name (DN). The provisioner uses the distinguished name to match a manager in Workplace by Facebook and may not find the correct match. To avoid this, you can use a custom attribute mapping to link the manager attribute to a manager's email.

- Due to SaaS API limitations, adding a manger may require a search of all Workplace by Facebook users. This will impact provisioning performance. To avoid this, you can use a custom attribute mapping to link the manager attribute to a manager's email. |

## September, 2018

**Enhancements**

| Feature                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PKCE support for OpenID Connect (OIDC)                         | We've added support for Proof Key for Code Exchange (PKCE) to secure OIDC clients that cannot or choose not to use a client secret. We have therefore relaxed the requirement that a client secret must be specified when configuring an OIDC application with the authorization code flow. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Integrate an OIDC application, PKCE parameters] For more information, see .pingidentity.com/pingone/saasSsoAdminGuide/index.shtml//\[Integrate an OIDC application, PKCE parameters]. |
| SLO for OIDC identity providers                                | We've added single logout (SLO) support for PingOne for Enterprise OIDC identity providers (IdPs). You can specify the end-session URL through the well-known metadata of the OpenID Connect provider (end\_session\_endpoint), or when you configure the PingOne connection for the OIDC IdP. When SLO is triggered, PingOne redirects the user logout process to the end-session URL for the OIDC IdP.                                                                                                                                                                   |
| Automatic IdP Discovery                                        | We've added automatic IdP discovery for all PingOne for Enterprise managed applications (applications managed by your account, rather than a service provider). For these applications, we no longer require that you specify the idpid for SP-initiated (SAML) requests or OIDC authorization requests.                                                                                                                                                                                                                                                                   |
| PingOne directory enhancements                                 | We've added features to PingOne directory allowing you to:- Configure the reply-to email address used for PingOne Directory user invitations. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Allow self registration for new directory users].

- Enable or disable the password expiry and password lockout notification emails sent to PingOne Directory users. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Allow self registration for new directory users].                     |
| include::partial$p14e\_p1refs\_faw\.adoc\[tags=faw]provisioner | We've updated the provisioner for Workplace by Facebook applications. This provisioner includes:- Improved error handling and reporting when Workplace by Facebook users contain no ID.

- Improved check connection call by not retrieving a list of users.See **Known Issues and Limitations** for important information.                                                                                                                                                                                                                                                |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

**Known issues and limitations**

| Subject                           | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workplace by Facebook provisioner | The following limitations apply:- Clearing fields on updates is not supported.

- Due to API limitations with matching a user's manager using the display name, if multiple matches occur the first match will be used. This could be an issue if multiple employees in the Workplace by Facebook account have the same first and last names. To avoid conflicts, you can use a custom attribute mapping to link the manager attribute to a manager's email.

- Due to LDAP limitations, when you update a manager's name it does not update their Distinguished Name (DN). The provisioner uses the distinguished name to match a manager in Workplace by Facebook and may not find the correct match. To avoid this, you can use a custom attribute mapping to link the manager attribute to a manager's email.

- Due to SaaS API limitations, adding a manger may require a search of all Workplace by Facebook users. This will impact provisioning performance. To avoid this, you can use a custom attribute mapping to link the manager attribute to a manager's email. |

## August, 2018

**Enhancements**

| Feature                              | Description                                                                                                                                  |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Users by Service                     | We've added support for first and last name values for provisioned users on the **Users > Users By Service** page.                           |
| PingOne directory user registrations | We've added the ability for you to specify a reply-to email address for user registrations on the **Setup > Directory > Registration** page. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

## July, 2018

**Enhancements**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenID Connect applications         | PingOne for Enterprise and PingOne SSO for SaaS Apps now support the OpenID Connect (OIDC) protocol for application integration using code, implicit or hybrid flows. You can customize access tokens for your account or per application. Client authentication is done using client secrets.For PingOne for Enterprise, you can make PingOne OIDC applications available on the PingOne dock. The applications are also selectable in access and authentication policies.                                                                                                                                                                                     |
| Updated provisioner for Evernote®   | We have updated the provisioner for Evernote applications. The update includes:\* Support for user attributes: Display Name and External ID. \* Support for the Evernote SCIM 2.0 API. \* Removed support for hard delete (feature deprecated by Evernote). \* Removed support for reactivating a disabled user (feature deprecated by Evernote).See **Known Issues and Limitations** for important information.                                                                                                                                                                                                                                                |
| Updated SCIM SaaS provisioner       | We have updated the provisioner for SCIM SaaS applications. The updates include:\* Fixed issue where SCIM v2 requests included SCIM v1.1 schema URN's. \* Fixed issue where the NO\_CONTENT HTTP response code was not being handled. \* Fixed issue where the SERVER\_ERROR HTTP response code was not being handled. \* Fixed issue where the user's active status was not updated correctly on update requests. \* Fixed issue where SCIM v2 error descriptions were not logged correctly. \* Fixed issue where an empty return body on a user PUT operation caused a JSON parsing exception.See **Known Issues and Limitations** for important information. |
| New provisioner for Lucidchart®     | We have added a new provisioner for the Lucidchart applications. This provisioner includes:\* Support for user provisioning. \* Support for these user attributes: Username, Display Name, Email, External ID, First Name, Last Name and Roles.See **Known Issues and Limitations** for important information.                                                                                                                                                                                                                                                                                                                                                  |
| Updated provisioner for Office 365™ | We have updated the provisioner for Office 365 applications. The update includes:\* Support for hard-deleting users.See **Known Issues and Limitations** for important information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

**Known issues and limitations**

| Subject                | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evernote provisioner   | The following limitations apply:\* Clearing fields on updates is not supported. \* Provisioning disabled users from an LDAP user repository to Evernote is not supported. \* Due to Evernote API limitations, a deactivated user cannot be reactivated using SCIM. \* Due to Evernote API limitations, new users cannot be created with the same username as a previously deactivated user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SCIM SaaS provisioner  | The following limitations apply:\* Clearing fields on updates is not supported. \* Outbound Group Provisioning and Memberships is not supported. \* Patch updates to SCIM-enabled target applications are not supported. \* There is a limit of one value per type (such as, home, work, other) for multivalue attributes (email, phone, address). \* Unexpected behavior may occur if the SaaS application does not specify either type and primary information, or both type and primary information for multivalue attributes (email, phone, address). Also, existing attributes on the application may not be removed during an update, and the desired value may not be correctly set as primary. \* SCIM-compliant service providers may implement or interpret the SCIM standards differently. This can result in behaviour that is not consistent with the intended use of the SCIM SaaS provisioner.                                                                                                               |
| Lucidchart provisioner | The following limitations apply:\* Clearing fields on updates is not supported. \* Due to Lucidchart API limitations, there will be a performance impact to creating users when mapping External ID or Roles. Both External ID and Role may fail to be added to a user on the initial create. If this happens, an error will be logged and the update to External ID and Roles will be retried up to three times. \* Due to Lucidchart API limitations, attempting to update a user immediately after creating them may result in user not found exceptions. This is due to a delay in Lucidchart between creating a user and being able to modify the user. Failed attempts to update the user will be re-attempted up to three times.                                                                                                                                                                                                                                                                                     |
| Office 365 provisioner | The following limitations apply:\* Opting out of license management for users is not supported. The provisioner will clear existing licenses even when the attribute is unmapped. \* Updating the mobile attribute requires that the service principal representing the provisioner (where the user gets the client key and secret) be assigned a role with Company Administrator privileges (using Powershell). \* Updating the Password attribute is not supported. \* User updates containing a manager that has not yet been provisioned or updated by the new version will fail, because the manager will not have the new extended attribute holding their distinguished name from Active Directory. \* If the DoBase64Conversion field is switched to "false", expect conflicts or failures on federated domains containing pre-existing users provisioned by dirsync or V1.0. \* Only outbound provisioning is supported. \* Group provisioning is not supported. \* Automatic licensing of users is not supported. |

## June, 2018

**Enhancements**

| Feature                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New provisioner for Zscaler®     | We have added a new provisioner for the Zscaler applications. This provisioner includes:\* Support for user provisioning. \* Support for these user attributes: Username, Display Name, Department, Email, External ID, First Name and Last Name.See **Known Issues and Limitations** for important information.                                                                                                                                                                                                                                                                                               |
| Audit subscriptions              | We have added UI for you to configure subscriptions to audit events. You can now display a list of your audit subscriptions, create new Push or Poll subscriptions, and edit or delete existing subscriptions.Learn more in [Monitoring PingOne for Enterprise use](../pingone_for_enterprise/p14e_monitoring_use.html).                                                                                                                                                                                                                                                                                       |
| Service provider SAML encryption | We have added an option for you to configure encryption of the assertion in the outbound SAML response sent from PingOne to the service provider (SP). This functionality is available only for non-multiplexed SAML applications. You can assign the encryption algorithm to use. You can also upload your own certificate to use for encryption. NOTE: For enhanced security we will sign the SAML response rather than the assertion in the SAML response when encryption is enabled.Learn more in [Adding or updating a SAML application](../pingone_for_enterprise/p14e_add_update_saml_application.html) |
| Service provider SAML encryption | We have added an option for you to configure encryption of the assertion in the outbound SAML response sent from PingOne for an application. You can assign the encryption algorithm to use. You can also upload your own certificate to use for encryption. NOTE: For enhanced security we will sign the SAML response rather than the assertion in the SAML response when encryption is enabled.See [Adding or updating a SAML-enabled application](../pingone_sso_for_saas_apps/p14saas_add_update_saml_application.html) for more information.                                                             |
| Updated navigation design        | We have updated the design of the top-level navigation for the PingOne admin portal. There is no functional or behavioral impact. This is solely a style change.                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SSD-8111  | Fixed an issue where the Target Resource URL was limited to 128 characters.                                                                                                                                                    |
| SSD-8413  | Fixed an issue where changing the PingOne for Enterprise Target Resource URL for an application supplied by a service provider (SP) to the same Target Resource value as set by the SP resulted in the setting change failing. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

**Known issues and limitations**

| Subject             | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zscaler provisioner | The following limitations apply:\* Clearing fields on updates is not supported. \* Due to a Zscaler limitation, a user's username cannot be updated. \* Deleting the administrative user that is set up for provisioning may lead to undesired consequences. The provisioner makes the administrative user the owner and member of each group that is created by the provisioner. We recommend that this administrative user is not managed through the provisioner and is not deleted. |

## May, 2018

**Enhancements**

| Feature                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ServiceNow provisioner (Kingston, Jakarta, Istanbul) | We've added new capabilities for the ServiceNow applications:- Configuration options for the create/read/update/delete (CRUD) capabilities.

- Configuration options for provisioning disabled users.

- Support for Istanbul, Jakarta, and Kingston.See **Known Issues and Limitations** for important information. This is a new ServiceNow provisioner. We've rebranded the existing provisioner from ServiceNow to "ServiceNow (Fuji)". |
| Box provisioner                                      | We've added new capabilities for the Box applications:- An option to create personal folders on user creates.

- An option to force delete users with managed content.See **Known Issues and Limitations** for important information.	If you have an existing Box application, to take advantage of the new features you will need to click through to the last page and save the application.                                              |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| SSD-7486  | Fixed an issue when adding a new SAML application where changes to the signing algorithm were not being retained after saving the changes. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

**Known issues and limitations**

| Subject                                              | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ServiceNow provisioner (Kingston, Jakarta, Istanbul) | The following limitations apply:- `Outbound Group Provisioning` and `Memberships` are not supported.

- User attributes cannot be cleared once set. They can only be updated.

- When provisioning to ServiceNow, all user accounts in ServiceNow must have an assigned `username` (User ID) value. This is not a required field in ServiceNow. However, because the provisioner must use this field to sync with pre-existing users in ServiceNow, it is required for provisioning to function. If a user in ServiceNow resolves to sAMAccountName (the "standard" mapping in the provisioning channel), the accounts will be linked. Currently, if users exist in ServiceNow without an assigned UserName value, this will cause errors in provisioning. In this case, you can resolve the issue by ensuring every user has an assigned UserName, even if they are not intended to be managed by the provisioner.

- When provisioning users, the `username` attribute must contain only URL-safe characters.

- When synchronizing roles with users, the `role` attribute must contain only URL-safe characters.

- If a new user is created with the same `username` as an existing user, a duplicate user will not be created. Instead, the existing user will be updated with any information assigned.

- Due to limitations with the ServiceNow API, a role can be added to a user but not removed, which may cause a user's role in the source data store to become out of sync with the user's role in ServiceNow. Learn more in [ServiceNow Provisioner](https://docs.pingidentity.com//integrations/servicenow/pf_servicenow_connector.html).

- When mapping the `roles` attribute, multiple calls to ServiceNow must be made to sync the user role information. This may impact provisioning performance. |
| Box provisioner                                      | The following limitations apply:- Clearing fields on updates is not supported.

- The login attribute cannot be updated through provisioning.

- The `Inactive Status Default` user attribute has no effect if the Box connector is configured to delete (hard-delete) users instead of disable (soft-delete) users when de-provisioning. Additionally, deleting a user in an LDAP repository will always set the status for the user as "inactive" in the Box application.

- `Outbound Group Provisioning` and `Memberships` are not supported.

- A Box API limitation prevents login credentials from being updated by the provisioner when the character case differs. For example, "<USER@TEST.COM>", cannot be updated to "<user@test.com>". When the case differs, the Box API omits the login from the API operation. So, in an update operation, when the case differs, the login is omitted, but any other attributes that may have changed are provisioned and updated.

- Due to Box API requirements, only primary, validated email addresses can be used to sync users.

- Enabling Personal Folder functionality will diminish initial synchronization provisioning performance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## April, 2018

**Enhancements**

| Feature                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenID Connect identity repository | We've added support for OpenID Connect identity repositories. You can now authenticate users through any OpenID provider. See [Connect to OpenID Connect](../pingone_for_enterprise/p14e_connect_oidc.html) for more information.                                                                                                                                                                                                                                                                               |
| Force MFA option                   | If you have an authentication policy in place for your PingOne account, when you add an application to PingOne, you now have the option to require that each time a user accesses the application, they must use multi-factor authentication (MFA).                                                                                                                                                                                                                                                             |
| New attribute mapping settings     | When you add an application to PingOne and use advanced attribute mapping to map your identity provider attributes to service provider attributes, you will now find settings for `random` and `hash` functions. The hash function takes a literal string or attribute value. The random function generates a random string of a specified length. Both functions optionally hash the string using the selected algorithm (MD5, SHA-1, SHA-256) and encode the string using the selected encoder (hex, base64). |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                    |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SSD-6937  | Fixed an issue where the signing algorithm for a non-multiplexed application wasn't updating the signing algorithm for the connection.                                                                                   |
| SSD-6763  | Fixed an issue where administrative SSO to the PingOne admin portal for newly assigned administrators was failing when multi-factor authentication (MFA) for the admin portal was required in the authentication policy. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

## March, 2018

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                       |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-6751  | Fixed an issue where the `restAuthUsername` value wasn't always set when the integration page was loaded.                                                   |
| SSD-6627  | Fixed an issue where Basic SSO apps were being counted towards the application limit even though the setting to allow Basic SSO was disabled (the default). |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

## January - February, 2018

**Enhancements**

| Feature                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include::partial$p14e\_p1refs\_faw\.adoc\[tags=faw]provisioner | We've updated the Workplace by Facebook provisioner to add support for additional user attributes. See **Known Issues and Limitations** for important information. NOTE: If you've been using the Workplace by Facebook application (formerly known as Facebook at Work), you will need to edit the application by clicking through to the last page and saving the application. You will then be able to take advantage of the new provisioner features. |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SSD-6604  | Fixed an issue where you were unable to edit or delete duplicate groups.                                                                                                       |
| SSD-6599  | Fixed an issue where the PingOne was using the NA region authenticator for multi-factor authentication, rather than the proper regional authenticator for the PingOne account. |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

**Known issues and limitations**

| Subject                           | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workplace by Facebook provisioner | The following limitations apply:- Clearing fields on updates is not supported.

- Due to API limitations with matching a user's manager using the display name, if multiple matches occur, the first match will be used. This may be an issue if multiple employees in the Workplace by Facebook account have the same first and last names. To avoid conflicts, you can use a custom attribute mapping to link the Manager attribute to a manager's email address.

- Due to LDAP limitations, when you update a manager's name it does not update their Distinguished Name (DN). The provisioner uses the DN to match a manager name in Workplace by Facebook, so may not find the correct match. To avoid this, you can use a custom attribute mapping to link the Manager attribute to a manager's email address.

- Due to SaaS API limitations, adding a manger may require a search of all Workplace by Facebook users. This will impact provisioning performance. To avoid this, you can use a custom attribute mapping to link the Manager attribute to a manager's email address. |

## December, 2017

**Enhancements**

| Feature                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multi-factor authentication for the PingOne admin portal | We've added a feature on the Authentication Policy page in the admin portal to enable and require PingID multi-factor authentication (MFA) for PingOne administrators who access the PingOne admin portal. Included is an option to specify an administrator who can access the admin portal without requiring MFA.See [SSO to the PingOne for Enterprise admin portal with multi-factor authentication](../pingone_for_enterprise/p14e_sso_admin_portal_mfa.html) for more information.                                                                                                                                                                                                                    |
| SAML signature signing algorithm for SSO                 | We've added the ability for you to configure the signature signing algorithm for all authentication requests, assertion signing and single logout (SLO) between PingOne and SAML identity providers and between PingOne and SAML service providers. PingOne will continue to support the SHA-1 algorithm, but now allows you to select SHA-256, SHA-384 and SHA-512. New SAML connections default to SHA-256. See [Connect to PingFederate](../pingone_for_enterprise/p14e_connect_pf.html) for more information.&#xA;&#xA;If you're using PingFederate version 8.0 or greater, you will be automatically updated to use SHA-256 for authentication requests at a future date, with no interruption to SSO. |
| SAML signature signing algorithm                         | We've added the ability for you to configure the signature signing algorithm for all assertion signing to PingOne. PingOne will continue to support the SHA-1 algorithm, but now allows you to select SHA-256, SHA-384 and SHA-512. New SAML connections default to SHA-256. See [Adding or updating a SAML-enabled application](../pingone_sso_for_saas_apps/p14saas_add_update_saml_application.html) for more information.                                                                                                                                                                                                                                                                               |
| Session revocation for PingOne directory                 | We've implemented a session revocation service for the PingOne directory workflows: user deletion, user disablement and password reset. When you perform these workflows for a PingOne Directory user, the session revocation service will now terminate the PingOne session associated with that user and prevent them from performing new SSO requests through PingOne. See [Delete directory users](../pingone_for_enterprise/p14e_delete_p1d_users.html) for a description. NOTE: The session revocation service does not perform SLO to SaaS applications that the user may have in an active session.                                                                                                 |
| PingFederate summary information                         | We've added configuration summary information on the **Identity Repository Settings** page for identity repositories using PingFederate 8.0 or greater.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| New provisioner for Jive®                                | We've added a new provisioner for Jive applications. This provisioner includes:- Added support for user provisioning.

- Added support for the user attributes: userName, givenName, familyName, workEmail, password, locale, timeZone, workPhone, externalContributor, federated and location.See **Known Issues and Limitations** for important information.                                                                                                                                                                                                                                                                                                                                              |

**Deprecated features**

| Feature                             | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Basic SSO and the browser extension | Basic SSO and the PingOne browser extension are no longer offered for new PingOne accounts. Accounts that are currently utilizing Basic SSO or the browser extension can continue using these facilities without interruption. For accounts not currently using Basic SSO or the browser extension, availability of these facilities is no longer displayed. |

**Known issues and limitations**

| Subject          | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jive provisioner | The following limitations apply:- Clearing fields on updates is not supported.

- Outbound Group Provisioning and Memberships is not supported.

- Due to a Jive limitation, a user's `username` cannot be updated.

- Due to a Jive limitation, the `externalContributor` attribute cannot be updated.

- Due to a Jive limitation, when a user is created their email address must be unique. However, after creation their email address can be updated to match that of an existing user.

- Deleting the administrative user that is set up for provisioning can lead to undesired consequences, because the provisioner makes the admin user the owner and member of each group that is created by the provisioner. We recommend that this admin user is not managed through the provisioner and is not deleted. |

## November, 2017

## October, 2017

**Enhancements**

| Feature                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include::partial$p14e\_p1refs\_slack.adoc\[tags=Slack]provisioner | We've have added support for additional user attributes. See **Known issues and limitations** for important information. NOTE: Existing customers must edit their existing Slack application, click through to the end page and save to take advantage of the new features                                                                                                                                                                         |
| SCIM SaaS provisioner                                             | We've added a new provisioner for SCIM SaaS applications. This provisioner includes:- Support for SCIM 1.1 and 2.0

- Support for user provisioning

- SCIM core and enterprise attributes

- Support for Basic Authentication, OAuth 2 Bearer Token and OAuth 2 Client Credentials Authentication

- SCIM Overrides (Filter Expression, Authorization Header Type, Users API Path)See **Known issues and limitations** for important information. |
| Ping IDaaS Directory provisioner                                  | We've added a new provisioner for Ping IDaaS Directory.See **Known issues and limitations** for important information.                                                                                                                                                                                                                                                                                                                             |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                  |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-6063  | Fixed an issue where you were unable to preview the PingOne dock.                                                                                                                                                      |
| SSD-5879  | Fixed an issue where the number of connections displayed on the My Applications page for applications was incorrect when an application was disabled.                                                                  |
| SSD-3780  | Fixed an issue where no warning or confirmation prompt was displayed when saving an Attribute Policy that had no associated connection.                                                                                |
| SSD-3838  | Fixed an issue where the dropdown list on the search bar automatically displayed when opening the PingOne dock using include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ie.adoc\[tags=IE]10.                      |
| SSD-3838  | Fixed an issue when using include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ie.adoc\[tags=IE]and clicking the search bar, where an application description wasn't being displayed after clicking the down arrow. |

. Known issues and limitations

| Subject                             | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Slack provisioner                   | * Clearing fields on updates is not supported.

* Outbound Group Provisioning and Memberships is not supported.

* Due to an API limitation, a user name cannot be updated.

* Due to an API limitation, users cannot be created in a deactivated state. For example, if a user is disabled in your user store it will not be created in Slack by the provisioner.

* For more information on Slack provisioning limitations, see the .slack.com/scim//\[Slack API documentation].                                                                                                                                                                                                                                                                                                                                                                        |
| SCIM SaaS provisioner               | - Clearing fields on updates is not supported.

- Outbound Group Provisioning and Memberships is not supported.

- Patch updates to SCIM enabled target applications are not supported.

- There is a limit of one value per type (such as, home, work, other) for multivalue attributes (email, phone, address).

- Unexpected behavior may occur if the SaaS does not specify either type and primary information, or both type and primary information for multivalue attributes (email, phone, address). Also, existing attributes on the SaaS may not be removed during an Update, and the desired value may not be correctly set as primary.

- SCIM-compliant service providers may implement or interpret the SCIM standards differently which can result in behaviour that is not consistent with the intended use of the SCIM SaaS Provisioner. |
| Ping IDaaS Directory provisioner    | * Clearing fields on updates is not supported.

* Outbound Group Provisioning and Memberships is not supported.

* The password, external id, profilePhotoUrl, profileThumbnailUrl, role, certificates and entitlements attributes cannot be mapped from the source. A default literal value can be used for setting values in the target PingOne tenant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Multiplexing and manual connections | When configuring a manual connection to an application, currently it is possible to select for multiplexing not to be used for non-SAML applications. Multiplexing is used for all non-SAML applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## September, 2017

**Enhancements**

| Feature                     | Description                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------- |
| Deleting a customer account | We've added a confirmation dialog box when you choose to delete a customer account. (SSD-5867) |

**Resolved issues**

| Ticket ID      | Issue                                                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-5735       | Fixed an issue where changing the application category for a PingOne for Enterprise managed application did not update the application category on the PingOne dock. |
| SSD-5603, 5604 | Updated Ping logo, icon and favicon.                                                                                                                                 |

## August, 2017

**Enhancements**

| Feature                                                         | Description                                                                                                                                                                                                                             |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include::partial$p14e\_p1refs\_msedge.adoc\[tags=MsEdge]support | You can now use the Microsoft Edge browser (minimum EdgeHTML version: 15.15063) with the PingOne dock and the PingOne browser extension.                                                                                                |
| PingOne directory `phoneNumbers` attribute                      | We've expanded the `phoneNumbers` multivalued attribute to include more subattributes. See [PingOne for Enterprise Directory attributes](../pingone_for_enterprise/p14e_p1d_attributes.html) for the list of subattributes you can use. |
| PingID Standalone upgrade supported                             | Customers with an existing PingID Standalone account can now upgrade to a PingOne for Enterprise account (SSD-5464).                                                                                                                    |

**Resolved issues**

| Ticket ID          | Issue                                                                                                                                                                                                                   |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-5536           | Fixed an issue where the legacy UI was being displayed for Service User administrators.                                                                                                                                 |
| SSD-5297, SSD-3839 | (PingOne directory) Fixed an issue where the UI wasn't operating as expected when entering email addresses to share a certificate (**Setup > Certificates**, expand the details for a certificate and click **Share**). |
| SSD-5345           | Fixed an issue where the dropdown lists for setting attribute mappings in the **Dock > Configuration** page wasn't being displayed.                                                                                     |
| SSD-5633           | Fixed an issue when configuring a new custom SAML application where the list of attributes available for attribute mapping wasn't loading properly until you saved and refreshed the page.                              |

## July, 2017

**Enhancements**

| Feature                                                         | Description                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrators page                                             | We've redesigned the **Account > Administrators** page for clarity and ease of use.                                                                                                                                                                              |
| Users By Service Bypass option                                  | We've removed the Unlimited Time setting for the **Bypass** option for Users By Service for all administrators except Global Administrators. You must now be a Global Administrator to enable the **Bypass** option for a user for an unlimited time. (SSD-4983) |
| include::partial$p14e\_p1refs\_msedge.adoc\[tags=MsEdge]support | You can now use the Microsoft Edge browser (version 40) to access the PingOne admin portal.                                                                                                                                                                      |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                           |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-5358  | Fixed an issue on the My Applications page in the admin portal where the **Request Ping Identity add a new application to the application catalog** selection did not reference the proper URL. |
| SSD-5307  | Fixed an issue when adding a new private SAML application where the setting for the **Force Re-authentication** option wasn't being saved correctly.                                            |
| BE-2344   | (Browser extension) Fixed an issue where the locale setting for the browser extension didn't match the locale setting for the PingOne dock.                                                     |

## June, 2017

**Enhancements**

| Feature                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne universal certificate                                                              | A new PingOne universal certificate is now available. You need to update to the new PingOne universal certificate if you're using either PingFederate or a Third-Party SAML provider as your identity bridge and your configuration requires either:- Signed AuthN requests.

- SAML single logout (SLO), either IdP-initiated or SP-initiated.&#xA;&#xA;You do not need to update the PingOne universal certificate if you're using an identity repository other than PingFederate or Third-Party SAML.See [Check whether you need to update the PingOne for Enterprise universal certificate](../pingone_for_enterprise/p14e_check_whether_you_need_update_p14e_universal_certificate.html) for more instructions. |
| PingOne encryption certificate                                                             | We now include the PingOne encryption certificate in the PingOne metadata available when you're configuring a PingFederate or Third-Party SAML identity bridge. We've also added the option to separately download the PingOne encryption certificate if you intend to manually configure the IdP settings (rather than using the PingOne metadata).                                                                                                                                                                                                                                                                                                                                                                 |
| Custom entity IDs                                                                          | When configuring a PingFederate or Third-Party SAML identity bridge, you can now select to enable account-specific entity IDs and specify a custom entity ID for your account. We will validate the ID to ensure that it is unique across all PingOne accounts.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| include::pingone\_for\_enterprise:partial$p14e\_p1refs\_gapps.adoc\[tags=GApps]provisioner | We've updated the Google Apps for Work provisioner as follows:- Improved exception handling and reporting

- Added support for Google Admin SDK v1.22.0

- Updates to the password and includeInGlobalAddressList attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| include::partial$p14e\_p1refs\_zendesk.adoc\[tags=Zendesk]provisioner                      | We've updated the Zendesk provisioner as follows:- Added Support for updating user emails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PingOne universal certificate                                                              | A new PingOne universal certificate is now available. If you're using multiplexing, or using manually configured customer connections, you're using the PingOne universal certificate. In this case, it is imperative that you edit the application configuration to update the PingOne universal certificate. See [Update the PingOne SSO for SaaS Apps universal certificate](../pingone_sso_for_saas_apps/p14saas_update_universal_certificate.html) for instructions.                                                                                                                                                                                                                                            |
| PingOne encryption certificate                                                             | When you're adding a customer connection manually, we've added the option to separately download the PingOne encryption certificate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| IdP discovery                                                                              | When you edit a customer connection, you need only specify the domain or domains used for customer email addresses and we will use this information to discover the IdP for the connection. We've added the option to set the current connection as the default IdP connection used for all of your applications.We've also updated the IdP Discovery popup window to display the application logo and your corporate logo (if you've configured this).                                                                                                                                                                                                                                                              |
| Testing application integration                                                            | For security reasons, we've disabled connections to the PingOne Test IdP by default. This connection is enabled only when you select to test your application. We also ensure that you can disable the connection when you're done testing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                                                                                                     |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-4485  | Fixed an issue where selecting to use the PingOne universal certificate for a Third-Party SAML identity bridge configuration, then changing to use the PingOne directory as the identity repository, caused the Renewal Certificate to be selected for use rather than the PingOne universal certificate. |
| SSD-4450  | Fixed an issue that resulted in configuration updates not being used during SSO.                                                                                                                                                                                                                          |
| SSD-4298  | Fixed an issue where the Upload link was being displayed on top of the company logo icon when registering for a new account.                                                                                                                                                                              |
| SSD-3777  | Fixed an issue where the Signoff button was being displayed after closing the browser tab for an impersonated session, then going to the PingOne admin portal (the impersonated session) from the PingOne dock.                                                                                           |
| SSD-3721  | Fixed an issue on the My Devices page where pressing the Enter key did not correspond to clicking the Save button.                                                                                                                                                                                        |

## April-May, 2017

**Enhancements**

| Feature                                                                                                                  | Description                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include::partial$p14e\_p1refs\_box.adoc\[tags=Box]and include::partial$p14e\_p1refs\_webex.adoc\[tags=WebEx]provisioners | We've improved handling of look-up by Secondary ID, for instances when look-up by Primary ID fails to return a user.                                                                                                                                                   |
| Corporate branding                                                                                                       | We've added an **Account > Branding** page for you to assign branding to be used for your organization's account.                                                                                                                                                      |
| Corporate branding                                                                                                       | We've removed the **Setup > General** page and moved the account branding setting to a new **Account > Branding** page. On this page, you can assign branding to be used for your organization's account.                                                              |
| User support message                                                                                                     | The user support message setting that appeared on the (now removed) **Setup > General** page is displayed as one of the settings on the **Setup > Dock** page.The user support message is displayed to your users when they click the **Need Help?** link in the dock. |

**Resolved issues**

| Ticket ID      | Issue                                                                                                                                                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-4300       | Fixed an error message that was displaying repeatedly.                                                                                                                                                                                                  |
| SSD-4659       | Fixed an error message displayed when attempting to SSO to an application without the appropriate permissions.                                                                                                                                          |
| SSD-4671       | Fixed an issue where Application Catalog icons weren't being displayed consistently.                                                                                                                                                                    |
| SSD-3167       | Fixed an issue where Support Admins (Read-Only) were unable to view the Users tab when impersonating an account using PingOne directory as the identity repository.                                                                                     |
| SSD-4661       | Fixed an issue where the QR code wasn't being displayed when selecting to add a new device in the PingOne dock.                                                                                                                                         |
| SSD-4511       | Removed the (non-editable) corporate logo field from the **Account > Company** page. The corporate logo assignment is on the **Account > Branding** page.                                                                                               |
| SSD-4687       | Fixed an issue where selecting "Other" as the country on the Company page resulted in an error.                                                                                                                                                         |
| SSD-4806       | Fixed an issue where an error was thrown when mapping an advanced attribute using "As Literal", entering data, then clicking Save before the preview field updated.                                                                                     |
| SSD-4844       | Fixed an issue where the expiry date for the PingOne universal certificate shown after setting up an identity repository was different (by one day) from the expiry date shown in for the certificate in the list on the **Setup > Certificates** page. |
| SSD-4915       | Fixed an issue on the Company page when the country is France. The dropdown list for State/Province/Region displayed a second entry for "Limousin", rather than an entry for "Lorraine".                                                                |
| SSD-4425       | Fixed an issue where the Company ID value was no longer displayed in the PingOne dock. The **Company ID** value is now displayed on the bottom of the navigation pane in the dock.                                                                      |
| SSD-5064, 5065 | Fixed an issue where attempting to SSO to the admin portal from the PingOne dock fails when the prior SSO request was from the dock to PingFederate.                                                                                                    |
| SSD-3773       | Fixed an issue where a customer password reset was not also triggering the display of the license agreement if the license agreement had been updated.                                                                                                  |
| BE-2192        | Fixed an issue where an error wasn't being displayed when attempting to launch a Basic SSO application in the PingOne dock (without refreshing the page) after the application had been removed from the My Applications list.                          |
| BE-2228        | Fixed an issue where the PingOne browser extension training wizard wasn't able to complete for the Cloudpay Community application.                                                                                                                      |
| BE-2228        | Fixed issues where the PingOne browser extension training wizard wasn't able to complete for a number of applications.                                                                                                                                  |
| BE-2268        | Fixed an issue where the PingOne browser extension for include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ie.adoc\[tags=IE]was affecting the ability to load intranet sites.                                                                       |

## March, 2017

**Enhancements**

| Feature                        | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Directory settings permissions | We've expanded Identity Repository administrators permissions to include access to view and modify the directory settings when the identity repository is PingOne directory.                                                                                                                                                                                                                         |
| API Provisioning               | From March 4th 2017 Salesforce is no longer supporting TLS 1.0 protocol. PingOne has been updated to support OAuth for Provisioning communication to accommodate this change. See [How to Migrate the Salesforce Provisioner](https://support.pingidentity.com/s/article/How-to-Migrate-the-Salesforce-Provisioner) for instructions.JIT Provisioning (just-in-time) is not impacted by this change. |

**Resolved issues**

| Ticket ID | Issue                                                                                                                            |
| --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| SSD-3822  | Fixed an error message displayed when uploading an IdP metadata file that is missing necessary information for SP-initiated SSO. |
| SSD-3695  | Fixed an issue where the phone number wasn't being passed to the authentication provider (PingID).                               |

## February, 2017

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PingOne reporting      | We've added a new SSO summary report to the list of predefined reports included in the PingOne admin portal reporting. This report shows the number of unique users that are actively using PingOne, and which applications they are logging in to. It also shows the total number of SSO events for each application.                                                                                                                                                                     |
| Password change        | We've enhanced security to ensure that if a user fails to enter the correct password three times when changing their password on the User Profile page, they are automatically logged out.                                                                                                                                                                                                                                                                                                 |
| Salesforce provisioner | We've updated the Salesforce provisioner with the following changes and enhancements:- Support for approximately 150 additional user attributes.

- Support for Salesforce REST v37.0 API.

- Support for OAuth Authentication with the OAuth Configuration Service (OCS).

- Support for custom subdomains.

- You now have the option to freeze user accounts, rather than deactivating them.

- Improved exception handling and reporting.

- Support for Salesforce disabling TLS 1.0. |

**Resolved issues**

| Ticket ID       | Issue                                                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-4473        | Fixed an issue that was preventing an MSP administrator from impersonating an account to which only disabled administrators has access. |
| BE-2130         | Fixed an issue that was preventing the browser extension welcome message from displaying correctly in some browsers.                    |
| SSD-4316        | Fixed an issue that was prompting a user to activate OAuth when creating a connection for which provisioning was not selected.          |
| SSD-4289        | Fixed a security issue with an MSP administrator's ability to impersonate customer accounts.                                            |
| SSD-4282        | Fixed an issue that was preventing error message popups from closing correctly in the PingOne admin portal.                             |
| BE-2080/BE-1940 | Fixed an issue that was preventing characters from displaying correctly when training an app, if the language is not English.           |
| IO-2027         | We've improved the handling of different letter case logins and aliases for the Box provisioner.                                        |
| IO-2243         | Fixed an issue with the Microsoft Office 365 provisioner that was causing an error when trying to retrieve a user during provisioning.  |
| IO-2242         | Fixed an issue with the WebEx provisioner's handling of the timezones not listed in WebEx's timezone encoding list.                     |

**Known issues and limitations**

| Subject                | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Salesforce provisioner | * User attributes cannot be cleared once they have been set.

* You cannot delete permission set assignments.

* Custom attributes are not supported.

* If you enable/disable or delete a user in your user store, the Salesforce provisioner can only disable the corresponding user in Salesforce as it cannot perform a hard delete of the user entry in Salesforce.

* Username attribute must be entered in email format only.

* Alias attribute entries can be a maximum of 8 characters in length. |

## January, 2017

**Enhancements**

| Feature                | Description                                                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certificate Management | PingOne will now inform you if a verification certificate that has been configured on a connection is invalid when the connection is being edited.        |
| Reporting              | We've added the ability to navigate back to the Users by Service page if you clicked on the Latest Activity link for a user on the Users by Service page. |

**Resolved issues**

| Ticket ID               | Issue                                                                                                                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-4040                | Fixed an issue when filtering dashboard metrics, where filtering by "today" would return 0 results. Also fixed an issue with the mouse over popup on chart data that spanned a DST boundary where the time reported was offset by +1/-1 hour.                                          |
| SSD-4064                | Fixed an issue where viewing latest activity for a user on the Users by Service page was redirecting to the old report logging UI.                                                                                                                                                     |
| SSD-4144                | Fixed an issue that was preventing the first and last name from being displayed in the PingOne dock when using PingOne directory.                                                                                                                                                      |
| SSD-4116                | Fixed an issue that was preventing an administrator from accessing report entries if they occurred in a timezone and at a time that was considered the next day for the local timezone. Administrators can now select up to one day in the future for the end date of a report filter. |
| SSD-4071                | Fixed an issue that was preventing the propagation of SLO settings changed on an application in a PingOne for SaaS Apps account from being applied to all connections to that application.                                                                                             |
| SSD-4078                | Fixed an issue that was limiting the value that can be entered in each field on the Password Policy page to three digit numbers (i.e. a maximum value of 999). This limit is now removed.                                                                                              |
| SSD-4037                | Fixed an issue that was not clearing the filter criteria from the previous report, when running a predefined report in the **Reporting** tab.                                                                                                                                          |
| SSD-3718                | The dropdown box used to select fields when running a report has been fixed so that it now displays field names alphabetically.                                                                                                                                                        |
| SSD-3794/SSD-3784       | Fixed an issue when impersonating an account via the PingOne dock that was causing the navigation window to resize incorrectly.                                                                                                                                                        |
| ID-5209                 | Fixed an issue that was marking the SAML\_SUBJECT as an optional field when creating an application connection, rather than mandatory.                                                                                                                                                 |
| BE-2050                 | The browser extension can now handle language-based variations of the Eventzilla URL.                                                                                                                                                                                                  |
| BE-1943                 | Fixed an issue that was preventing the browser extension from detecting the **Password** and **Sign In** button for the Office 365 app.                                                                                                                                                |
| BE-1883                 | Fixed an issue displaying French language text when signing on to the browser extension.                                                                                                                                                                                               |
| BE-2003/BE-2005/BE-1995 | Fixed an issue that was preventing the browser extension from loading correctly after changing the privacy key on a different browser or machine.                                                                                                                                      |

## December, 2016: Minor Release

**Enhancements**

| Feature              | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne admin portal | We've made the following enhancements to the PingOne admin portal:- You can now use any Top Level Domain (TLD) URL as a connection configuration URL, in addition to those that are defined by Internet Assigned Numbers Authority (IANA).

- We've increased the number of records you can download from the report log, and added a progress bar to the **Reports** tab. You can now download up to 500,000 records to a .csv file. |
| Application catalog  | We've added support for the StartMeeting cloud application.                                                                                                                                                                                                                                                                                                                                                                           |
| Reporting            | The report log has been updated and enhanced.- You can now run detailed reports from the PingOne admin portal. PingOne provides a number of predefined reports, and also gives you the ability to run your own custom ad hoc report. You can view the results directly in the PingOne admin portal, or export the results in .csv format.

- We've also added the ability to view SSO activity per application, via the API.          |

**Resolved issues**

| Ticket ID       | Issue                                                                                                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BE-2003/BE-1995 | Fixed an issue that was preventing the browser extension from loading correctly after changing the privacy key on a different browser or machine.                                                                                             |
| BE-1994         | Fixed an issue that was preventing the sign in popup from being displayed in the PingOne dock following a browser refresh.                                                                                                                    |
| SSD-3630        | Fixed an issue that was preventing the system from saving the correct value for the **Account Specific Entity ID** field and the **Sign AuthRequest** field when uploading metadata for a third party SAML identity repository configuration. |
| ID-5966         | Fixed an issue when checking whether the Entity ID is unique during identity repository configuration.                                                                                                                                        |
| ID-6344         | Fixed an issue that was categorizing identity provider connections associated with a signing certificate incorrectly.                                                                                                                         |
| SSD-3572        | Fixed an issue that was preventing the removal of the **Identity Bridge Logout URL** value assigned in PingOne.                                                                                                                               |
| SSD-3543        | Fixed an issue where during configuration of an Invited PingOne SSO account, attempting to download a metadata file or a signing certificate generated an error.                                                                              |

## November, 2016: Minor Release

**Enhancements**

| Feature                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrator capabilities | A global or support administrator impersonating a customer account can now delete the last administrator on the account.                                                                                                                                                                                                                                                                                                                                        |
| PingOne admin portal       | We've added the ability for a Managed Service Provider (MSP) to delete a custom email template in the PingOne admin portal.                                                                                                                                                                                                                                                                                                                                     |
| PingOne admin portal       | We've reduced the idle timeout for an admin session to 15 minutes.We've added the ability for a Managed Service Provider (MSP) to delete a custom email template in the PingOne admin portal.                                                                                                                                                                                                                                                                   |
| Certificate Management     | We've made the following enhancements:- We've provided admins the ability to remove a verification certificate from a PingOne application connection.

- We've added the ability to promote a secondary verification certificate to a primary verification certificate when editing an application connection or a third party SAML identity repository.

- Primary and secondary certificates now display the common name and expiry date for the certificate. |
| Workplace by Facebook™     | We've renamed this feature (formerly known as Facebook at Work), and removed the suppressEmail attribute.                                                                                                                                                                                                                                                                                                                                                       |
| Box Provisioner            | We've added support for updating user emails in Box Provisioner. NOTE: Existing customers must remove their existing Box applications and then add the application connection to take advantage of the new feature.                                                                                                                                                                                                                                             |
|                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

**Resolved issues**

| Ticket ID         | Issue                                                                                                                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-3501          | Fixed an issue that was preventing a customer from creating an account when receiving an email invitation from a Managed Service Provider (MSP) administrator in PingOne.                                                 |
| SSD-3497/SSD-3394 | Fixed an issue that was preventing the use of "?" and "/" characters in advanced attribute mapping.                                                                                                                       |
| SSD-3480          | Fixed an issue that was preventing the validation error message from appearing when importing invalid metadata into the PingOne.                                                                                          |
| SSD-3464          | Fixed an issue that was causing an exception error when trying to save an application with an invalid ACS URL in PingOne.                                                                                                 |
| SSD-3441          | Fixed an issue that was displaying the administrator role incorrectly when sending an invitation to a new administrator to become the administrator of an existing PingOne account.                                       |
| ID-5882           | Fixed an issue that was causing PingOne to automatically insert default values into optional attribute mapping fields that were purposefully left blank.                                                                  |
| BE-1892           | Fixed issues with the following apps, and enabled them in the Application Catalog:- Glassdoor

- Wells Fargo CEO portal

- 8x8 Virtual Office

- 8x8 Account Manager                                                      |
| ID-6039           | We've hidden the ability to add primary and secondary verification certificates when creating an SAML 1.1 application connection, as verification certificates are not supported in SAML v1.1.                            |
| ID-6266           | Fixed an issue that was preventing a newly created certificate from appearing in the Certificate List when using Internet Explorer v10 and v11.                                                                           |
| ID-5714           | The **Single Logout Endpoint**, **Single Logout Response Endpoint**, and **Single Logout Binding Type** fields have been removed from SAML v1.1 managed applications. SAML v1.1 does not support Single Logout Endpoints. |
| SSD-3421          | Fixed an issue that was causing the admin account to be locked, if resetting a password in the PingOne admin portal using a password that does not meet the PingOne directory policy.                                     |
| SSD-3418          | Fixed an issue when resetting a password from the PingOne admin portal.                                                                                                                                                   |
| SSD-3294          | Fixed an issue when loading content from PingOne admin portal using Internet Explorer 10.                                                                                                                                 |

## October, 2016: Minor Release

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certificate management | We've now added email notifications to inform you when the primary verification certificate or secondary verification certificate associated with a conniction or identity bridge is expiring. Email notifications are sent two months before expiry, a week before expiry, and at the time of expiry.                                                                                               |
| Admin roles            | We've renamed the Directory Administrator role to Identity Repository Administrator, for clarity. The Identity Repository Administrator refers to an administrator who is responsible for the identity repository, regardless of whether it is PingFederate, AD Connect, a Third Party repository, or PingOne Directory.                                                                             |
| Dashboard              | We've enhanced the layout of data in the graphs displayed on the dashboard.                                                                                                                                                                                                                                                                                                                          |
| MSP administrator      | We've enhanced the Managed Service Provider (MSP) admin account capabilities. Now if an MSP account owns a PingOne SSO for SaaS Apps account and invites a customer or partner to create a connection to an application under that PingOne SSO for SaaS Apps account by registering an "Invited PingOne SSO" account, the Invited PingOne SSO account is now listed in the MSP's customer list page. |
| PingOne user accounts  | For any new identity provider that you set up, the lifetime of any user session is now set to 2 hours by default. You can change the duration from PingOne, if you need to do so.                                                                                                                                                                                                                    |
| Attribute mapping      | We've added the phone number attribute to the list of dock attribute mapping options for PingFederate, AD Connect, and third party SAML identity repositories.                                                                                                                                                                                                                                       |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-3356  | Restored the setting application logos on applications created in PingOne SSO for SaaS Apps accounts, as they were being removed incorrectly. The logos were removed when this capability was removed for PingOne for Enterprise when using the new PingOne for Enterprisedock. |
| BE-1812   | Fixed an issue that was preventing the **Go to PingOne**and **Sign Off**buttons from showing in the browser extension.                                                                                                                                                          |
| ID-5976   | Fixed an error handling issue on the PingOne for Enterprise password reset page.                                                                                                                                                                                                |
| ID-5993   | Fixed an issue that was preventing users changing the default signing certificate assigned to their managed application.                                                                                                                                                        |
| ID-6171   | Fixed an issue with the delete certificate feature.                                                                                                                                                                                                                             |
| SSD-3288  | Fixed an issue that was preventing a user from entering an email address that includes the '+' character, when inviting a customer from a Managed Service Provider (MSP) account in PingOne for Enterprise.                                                                     |
| SSD-3331  | Fixed an error displayed when adding Google Drive as a Basic SSO application in PingOne for Enterprise.                                                                                                                                                                         |
| SSD-3259  | Implemented a fix to make transaction processing more resilient to service configuration problems.                                                                                                                                                                              |
| SSD-3169  | Fixed a security issue with MSP Support Admin (read-only) roles.                                                                                                                                                                                                                |
| SSD-3108  | Fixed an issue updating login failures on the dashboard.                                                                                                                                                                                                                        |

## September, 2016: Minor Release

**Enhancements**

| Feature                     | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin log reporting         | We've added a new Administrator Login category to the reports log. The new report shows all login attempts by a PingOne administrator, the method of login used (username and password, or SSO) and whether the login attempt was successful.                                                                                                                                                        |
| SSO to PingOne Admin portal | We've added the ability for administrators having Identity Repository administrator or SaaS administrator roles to SSO directly to the PingOne admin portal. In previous versions this was only available for the Global administrator and the Service User administrator roles. This option is only available when using PingFederate, AD Connect, or Third Party SAML as your identity repository. |
| PingOne API                 | We've added support for PKCS7 formatted certificates.                                                                                                                                                                                                                                                                                                                                                |
| Certificate Management      | We've reorganized the layout of the connections that are listed in the certificate Connections tab. Connections are now listed by category (identity bridge or application). Identity bridge connections are listed by type (such as PingFederate, or Third Party SAML). The applications header shows the number of application connections associated with the certificate. .                      |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                  |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-3020  | Verification certificate tool tip text updated.                                                                                                                                                                        |
| SSD-3129  | Fixed an issue that was permitting users to upload expired or invalid certificates for third party SAML Identity Providers.                                                                                            |
| SSD-3112  | Fixed an issue when accessing the attribute mapping page for a SAML 2.0 connection. When exiting the page and then uploading metadata with a different attribute set, the attributes were not being updated correctly. |
| SSD-3161  | Fixed an issue with caching when trying to SSO with an account that was suspended and then re-enabled.                                                                                                                 |
| SSD-3168  | Fixed a security issue with Managed Service Provider (MSP) admin capabilities in PingOne.                                                                                                                              |

## August 30, 2016: Minor Release

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certificate management | Certificates that do not have a CN defined, now show the first 20 characters of the Subject DN as the certificate name.Performance enhancements were applied to the Certificate Management page.Certificate expiry dates are now displayed in a 4 digit format. |

**Resolved issues**

| Ticket ID        | Issue                                                                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-5718          | Fixed an issue when adding SAML v1.1 applications from the application catalog, where certificate management was not being supported.                                                                               |
| ID-5717          | Fixed an issue that was preventing a user from being able to add a multiplexed SAML app from the Application Catalog.                                                                                               |
| ID-5679          | Fixed an issue with the appearance of the **Select Image**button for the Application logo and icon. The appearance is now sized correctly and consistently in the UI.                                               |
| ID-5671          | Fixed a issue when clicking the **Active Download**link in Safari, that was causing it to be displayed, rather than downloaded.                                                                                     |
| ID-5846          | Fixed a bug that was causing an infinite loop when attempting to access the Devices page before completing first factor authentication using PingOne.                                                               |
| SSD-3136         | The option to define an application logo has been removed when creating or editing an application connection for users that have upgraded to the new dock. The option remains for users that are using legacy dock. |
| SSD-2993SSD-3121 | Fixed a bug when uploading metadata that included mappings that were already in the connection, and was causing these mappings to be lost.                                                                          |
| SSD-3036         | Fixed an issue that was causing an exception when loading the Certificate Management page if invalid certificates were present.                                                                                     |
| SSD-3017         | Fixed a bug where binary certificates that were uploaded were not saved correctly.                                                                                                                                  |

## August 9, 2016: Minor Release

**Enhancements**

| Feature                        | Description                                                                                                                                                                                                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| My Applications search         | We've enhanced the ability to search the My Applications list. You can now search by the:- Entity ID.

- Application description or part of the description.

- Application name.In previous versions it was only possible to search by the application name.          |
| PingOne certificate management | We've added the ability to view the SHA1 and SHA256 fingerprint in the certificate Properties tab.                                                                                                                                                                     |
| PingOne passwords              | When changing the administrator password in the PingOne admin portal, the administrator is now required to enter their current password, as well as their new password. If the administrator enters the wrong password three times, the account is temporarily locked. |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                                                                       |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-5685   | Fixed a broken link in the Invite IdP page.                                                                                                                                                                                                                                 |
| ID-5549   | Properties and connections associated with a verification certificate are now displayed in separate tabs. This matches the way this information is presented for signing certificates.                                                                                      |
| ID-4585   | Fixed an issue that was preventing the secondary instance of a certificate from being deleted when replacing a primary certificate with a secondary certificate.                                                                                                            |
| ID-5428   | When configuring a managed connection, the text for the Application Icon has been changed to 'For use on the dock'. As the Application Logo is not used on the new PingOne dock, the text for this field has been changed to 'For use on the previous version of the dock'. |
| BE-1642   | Fixed an issue that was making the browser extension unresponsive when clicking the username and then clicking **Learn** when training an app.                                                                                                                              |
| BE-1601   | Fixed an issue when training an app that was causing a loop when clicking the **Login** button.                                                                                                                                                                             |
| ID-5712   | Fixed an issue when editing an application that was preventing changes to the SLO or SLO Response Endpoint from being saved.                                                                                                                                                |
| ID-5689   | Fixed an issue in the Certificate Management page that was preventing the **Download** and **Export** buttons from working in some browsers.                                                                                                                                |
| ID-5691   | Fixed an issue on the Certificate Management page where applications sharing a connection (a multiplexed connection) were being displayed as disabled.                                                                                                                      |

## July 19, 2016: Minor Release

**Enhancements**

| Feature                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certificate management                              | We've added a new centralized certificate management UI. The new UI enables you to:- Create new signing certificates.

- Migrate individual connections to different signing certificates.

- Add certificate expiration notifications.

- Verify certification for failover and migration.

- Share certificates.See [Overview of signing and verification certificates](../pingone_for_enterprise/p14e_overview_signing_verification_certificates.html) for more information. |
| Additional language support for end user components | The following languages are now supported for all PingOne user subsystems (PingOne dock, transaction processing, browser extension, and authentication):Chinese, Dutch, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish, and Thai.                                                                                                                                                                                                             |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ID-5544   | Fixed an issue where the PingOne signing certificate wasn't showing up in the list of results when typing "Ping" in the certificate search field.                                                      |
| ID-5502   | Fixed an issue when setting up a connection to an application, that meant the PingOne default certificate was always selected even when a different signing certificate was chosen.                    |
| ID-5481   | Fixed an issue that caused the PingOne provided signing certificate to be downloaded for an application connection, even if a different singing certificate was selected for the connection.           |
| ID-5486   | Renamed the Connection Summary "Certificate" label to "Signing Certificate".                                                                                                                           |
| ID-5485   | Fixed an issue when promoting a secondary verification certificate to the primary verification certificate. The instance of the secondary verification certificate wasn't being automatically deleted. |
| ID-5482   | Fixed an issue that the certificate properties Issuer DN and Expiration Date fields were not updating accordingly when uploading a response to a certificate signing request (CSR).                    |
| ID-5343   | Fixed an issue importing the PingOne metadata file via a URL when setting up a Third-Party SAML identity bridge.                                                                                       |
| ID-5329   | Fixed an issue that was affecting the proper display of text when verifying AD Connect as an identity bridge.                                                                                          |
| BE-1569   | Fixed an issue for trained apps in PingOne browser extension v2.22.0 that was preventing the browser extension from signing in users automatically.                                                    |
| ID-5585   | Fixed a bug that was causing formatting issues in the PingOne dock search.                                                                                                                             |
| ID-5543   | Change the name of the link used to change an identity repository from "Change User Store Type" to "Change Identity Repository".                                                                       |
| ID-5508   | Fixed an issue that was preventing some users from editing an application.                                                                                                                             |

## June 28, 2016: Minor Release

**Enhancements**

| Feature                            | Description                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| New Application Catalog categories | We've added the following categories to the application catalog: benefits, training, and travel. |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-5444   | Fixed an issue when attempting to erase the identity bridge URL, the field was not updating correctly.                                                                                                            |
| ID-5385   | Fixed formatting of the applications listed in the application catalog.                                                                                                                                           |
| ID-5342   | Fixed an issue with editing an application, where Chrome and Firefox browsers were auto-populating the first two application configuration fields with autosaved username and password data.                      |
| ID-4503   | Fixed missing link that enables a user to log back into the admin web portal after they successfully logged out.                                                                                                  |
| BE-1493   | Fixed an issue when training a basic SSO app, that caused training to pause when clicking on the Login field.                                                                                                     |
| ID-5462   | Fixed an error when setting up a Third Party SAML identity bridge that prevented the list of connection information from being displayed.                                                                         |
| ID-5363   | Fixed an issue that custom app icons were not being displayed in the My Applications page, unless the entry was expanded. Custom app icons now app in the My Applications page, and when deleting an application. |
| ID-5356   | The browser extension install option now only appears if there is at least one Basic SSO application installed.                                                                                                   |
| ID-5361   | Fixed a security vulnerability associated with the application name on the legacy dock.                                                                                                                           |
| ID-5415   | Fixed a security vulnerability associated with the browser extension.                                                                                                                                             |
| SSD-2817  | Fixed an issue that was causing a mismatch between the total number of logins displayed in the Dashboard maps and the number of logins recorded in the Logins field.                                              |

## June 15, 2016: Minor Release

Resolved issues

| Ticket ID | Issue                                                                                                                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-5268   | Performance enhancements, to address customer issues when performing a search of Users by Service.                                                                                           |
| ID-4656   | Fixed a potential security vulnerability.                                                                                                                                                    |
| ID-5342   | Fixed an issue with editing an application, where Chrome and Firefox browsers were auto-populating the first two application configuration fields with autosaved username and password data. |
| ID-5334   | Fixed an issue that was causing an error when adding an application.                                                                                                                         |
| ID-5274   | Fixed an issue when clicking a Configuration page link it was landing on the Dashboard.                                                                                                      |
| ID-1671   | Fixed an issue on the Company Settings page when viewing company description the characters were not displaying correctly.                                                                   |
| ID-5332   | Fixed and issue that an application which had been updated to show a new icon displayed the old icon when trying to delete the application.                                                  |

## June 1, 2016: Major Release

**Enhancements**

| Feature                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New PingOne dock                                                | We've totally redesigned the PingOne dock:- There's a new user interface, with application categories, frequently used applications and quick access to account information.

- A new search bar to help you find applications and install new ones.

- More options for you to customize and brand the interface. This includes use of company logos, custom background images, definitions of application categories, and colors of navigation panes, fonts and the search bar.

- And improved display quality of application icons.See [Introducing the PingOne for Enterprise dock](../pingone_for_enterprise/p14e_introducing_p14e_dock.html) for more information. |
| include::partial$p14e\_p1refs\_faw\.adoc\[tags=faw]provisioning | We've updated Facebook at Work provisioning to support provisioning user manager details.See Known Limitations for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Known issues and limitations

| Subject                       | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Facebook at Work provisioning | * Clearing fields on updates is not supported.

* Due to API limitations with matching a user's manager using the display name, if multiple matches occur the first match will be used. This could be an issue if multiple employees in the Facebook at Work account have the same first and last names. To avoid conflicts, you can use a custom attribute mapping to link the manager attribute to a manager's email.

* Due to LDAP limitations, when you update a manager's name it does not update their Distinguished Name (DN). The provisioner uses the distingushed name to match a manager in Facebook At Work and may not find the correct match. To avoid this, you can use a custom attribute mapping to link the manager attribute to a manager's email.

* Due to SaaS API limitations, adding a manger may require a search of all Facebook At Work users. This will impact provisioning performance. To avoid this, you can use a custom attribute mapping to link the manager attribute to a manager's email. |

## May 17, 2016: Minor Release

Enhancements

| Feature                                                            | Description                                                                                                                                                                                  |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include::partial$p14e\_p1refs\_webex.adoc\[tags=WebEx]Provisioning | We've updated WebEx provisioning to support:\* Additional user attributes. \* WebEx API v10.0 SP3. \* Improvements to error handling and logging.See Known Limitations for more information. |

Resolved issues

| Ticket ID | Issue                                                                                                                                                                                                           |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-4842   | Fixed an issue on the PingID Configuration page where choosing to discard changes when attempting to exit this page didn't exit the page.                                                                       |
| ID-5135   | Fixed an issue where a new token wasn't being generated when a PingOne for Enterprise administrator clicked the Invite SaaS Admin link to send an email to the PingOne for SaaS Apps application administrator. |
| ID-5128   | Fixed an issue where some users were not being removed from the PingID service when selecting Remove on the Users by Service page.                                                                              |
| ID-5020   | Fixed an issue with removing customers from the customers listing. The last customer displayed in the listing wasn't being removed.                                                                             |
| BE-1300   | (Browser extension) Fixed an issue causing an include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ie.adoc\[tags=IE]installation error (1603) when attempting to install the browser extension.              |

Deprecated features

| Feature                   | Description                                                                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingID Standalone account | The registration option for a PingID Standalone account has been removed. All of the functionality offered by this account is now included in a PingOne for Enterprise account. |

Known issues and limitations

| Subject            | Issue/Limitation                                                                                                                                                                                                                                                                                                 |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WebEx provisioning | \* The WebEx ID attribute is not updateable in PingOne. \* The MeetingType attribute is limited to one value in PingOne (not a multivalued attribute). \* Due to API Limitations, WebEx doesn't allow a user to be created in a suspended state. WebEx will automatically activate the user after it is created. |

## April 26, 2016: Minor Release

Resolved issues

| Ticket ID | Issue                                                                                                                                                                                                                   |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-4842   | Fixed an issue where a Managed Service Provider (MSP) was unable to log in to an Invited PingOne SSO account as a Directory Admin.                                                                                      |
| ID-3881   | Fixed an issue where downloading the PingOne metadata file for a Third-Party SAML identity bridge wasn't working properly in Safari.                                                                                    |
| ID-5134   | Fixed an issue where user were unable to add applications to their personal dock.                                                                                                                                       |
| SSD-2627  | Fixed a security issue with an error message.                                                                                                                                                                           |
| BE-1084   | (Browser extension) Fixed an issue when using include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ie.adoc\[tags=IE]version 11 where the browser extension wasn't capturing and supplying user credentials properly. |
| BE-1222   | (Browser extension) Fixed an issue where Basic SSO wasn't working properly when using Internet Explorer for some applications not in the Application Catalog.                                                           |
| BE-1279   | (Browser extension) Fixed an in Internet Explorer 11 when signing on to a Basic SSO application from the PingOne dock.                                                                                                  |

Deprecated features

| Feature                   | Description                                                                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingID Standalone account | The registration option for a PingID Standalone account has been removed. All of the functionality offered by this account is now included in a PingOne for Enterprise account. |

## April 19, 2016: Minor Release

Enhancements

| Feature                                                        | Description                                                                                                                                                       |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include::partial$p14e\_p1refs\_box.adoc\[tags=Box]Provisioning | We've updated Box provisioning to support:- Additional user attributes.

- Improvements to error handling and logging.See Known Limitations for more information. |

Resolved issues

| Ticket ID | Issue                              |
| --------- | ---------------------------------- |
| None      | (None to report for this release.) |

Known issues and limitations

| Subject          | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Box provisioning | * Once set, you cannot clear user attributes.

* The login attribute cannot be updated through provisioning.

* The `Inactive Status Default` user attribute has no effect if the Box connector is configured to delete (hard-delete) users instead of disable (soft-delete) users when de-provisioning. Additionally, deleting a user in an LDAP repository will always set the status for the user as "inactive" in Box. |

## April 5, 2016: Minor Release

Enhancements

| Feature | Description                        |
| ------- | ---------------------------------- |
| None    | (None to report for this release.) |

Resolved issues

| Ticket ID | Issue                                                                                                                                                                   |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| None      | (None to report for this release.)                                                                                                                                      |
| SSD-2572  | Added new application categories for Benefits, Training and Travel.                                                                                                     |
| ID-4819   | Fixed an issue where an error occurred when you attempted to change your password using AD Connect with the Password Change option enabled and the IWA option disabled. |
| ID-4839   | Fixed an issue where Basic SSO transactions weren't being logged.                                                                                                       |

Known issues and limitations

| Subject                                            | Issue/Limitation                                                                                                                                                             |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Browser extension installation in Mozilla Firefox® | After installing the PingOne browser extension in Firefox, you need to refresh the page. Otherwise, the browser extension installation will begin again. Ticket ID: ID-4248. |

## March 15, 2016: Minor Release

Enhancements

| Feature | Description                        |
| ------- | ---------------------------------- |
| None    | (None to report for this release.) |

Resolved issues

| Ticket ID | Issue                                                                                                                                                                                                                                                                                                                   |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| None      | (None to report for this release.)                                                                                                                                                                                                                                                                                      |
| ID-4658   | Fixed an issue where the number of applications displayed in the Dashboard page didn't match the number of applications displayed in the My Applications page.                                                                                                                                                          |
| ID-4650   | Fixed an issue where provisioning for AD Connect was failing.                                                                                                                                                                                                                                                           |
| ID-4422   | Fixed an issue where the PingID settings file had an extraneous escape character.                                                                                                                                                                                                                                       |
| BE-1142   | (Browser extension) Fixed an issue where the PingOne browser extension was interfering with display rendering in include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ie.adoc\[tags=IE]version 10 or 11 when using include::partial$p14e\_p1refs\_oracle.adoc\[tags=Oracle]Business Intelligence Enterprise Edition. |

Known issues and limitations

| Subject                                            | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dropbox provisioning                               | * Clearing fields on updates is not supported.

* Due to API limitations, a user's email cannot be updated until the user has activated their account.

* Due to API limitations, a user cannot be suspended or unsuspended until the user has activated their account.

* Due to API limitations, if a user's given name or surname fails to update due to the new value containing unsupported characters (\* \| : " < > ?), an error may not be reported in the provisioning logs. |
| Browser extension installation in Mozilla Firefox® | After installing the PingOne browser extension in Firefox, you need to refresh the page. Otherwise, the browser extension installation will begin again. Ticket ID: ID-4248.                                                                                                                                                                                                                                                                                                          |

## February 23, 2016: Minor Release

Enhancements

| Feature                                                                | Description                                                                                                                                                 |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| include::partial$p14e\_p1refs\_dropbox.adoc\[tags=Dropbox]Provisioning | We've updated Dropbox provisioning to support additional user attributes. See Known Limitations for more information.                                       |
| Invited PingOne SSO Accounts                                           | We've add an Administrators page to the PingOne admin portal for Invited PingOne SSO accounts. You can now assign multiple administrators for your account. |

Resolved issues

| Ticket ID | Issue                                                                                                                                                                                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| None      | (None to report for this release.)                                                                                                                                                         |
| SSD-2267  | Fixed an issue for multi-factor authentication with include::partial$p14e\_p1refs\_safenet.adoc\[tags=SafeNet]where users needed to authenticate a second time when logging in to Safenet. |
| ID-4278   | Fixed an issue in the Reports page display where the Category values was removed whenever the report results were expanded.                                                                |
| ID-1682   | Fixed an issue on the User Groups page where the Deprovision all users checkbox wasn't displayed when you cleared a selected checkbox next to the application name.                        |
| BE-976    | (Browser extension) Fixed an issue where the Save Learning popup wasn't displaying properly for include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ie.adoc\[tags=IE]version 9.        |

Known issues and limitations

| Subject                                            | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dropbox provisioning                               | * Clearing fields on updates is not supported.

* Due to API limitations, a user's email cannot be updated until the user has activated their account.

* Due to API limitations, a user cannot be suspended or unsuspended until the user has activated their account.

* Due to API limitations, if a user's given name or surname fails to update due to the new value containing unsupported characters (\* \| : " < > ?), an error may not be reported in the provisioning logs. |
| Browser extension installation in Mozilla Firefox® | After installing the PingOne browser extension in Firefox, you need to refresh the page. Otherwise, the browser extension installation will begin again. Ticket ID: ID-4248.                                                                                                                                                                                                                                                                                                          |

## February 2, 2016: Minor Release

Resolved issues

| Ticket ID | Issue                                                                                                                                                         |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-4216   | Fixed an issue where the Save button wasn't working in the application credentials dialog box for Basic SSO applications.                                     |
| ID-4213   | Fixed an issue where the step to configure provisioning for a PingFederate identity bridge displayed in the existing tab/window rather than a new tab/window. |
| ID-4145   | Fixed an issue where the browser extension wasn't automatically signing in after you install your first Basic SSO application.                                |
| ID-3883   | Fixed an issue where errors weren't being displayed properly when installing an identity bridge.                                                              |
| ID-3398   | Fixed an issue for PingID Standalone accounts, where an extraneous warning was being displayed when clicking the Setup tab.                                   |
| ID-3031   | Fixed an issue where you were unable to upload a JPG image file for your profile picture.                                                                     |
| ID-3030   | Fixed an issue where invited PingOne directory users were unable to upload a JPG image file for their profile picture during the registration process.        |
| BE-12     | (Browser extension) Fixed an issue where the browser extension wasn't working properly when login fields displayed in an iFrame.                              |
| BE-747    | (Browser extension) Fixed an issue where sign on for Basic SSO applications wasn't working properly when the application login required text input.           |
| BE-623    | (Browser extension) Fixed an issue where browser extension wasn't working properly when the PingOne dock tab wasn't the current tab.                          |
| ID-1656   | Fixed an issue where the instruction steps for creating or editing an application displayed HTML tags and encoded characters.                                 |
| ID-4214   | Fixed an issue where the SSO endpoint was being truncated. Now extended to 2048 characters.                                                                   |

Known issues and limitations

| Subject                                            | Issue/Limitation                                                                                                                                                             |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Browser extension installation in Mozilla Firefox® | After installing the PingOne browser extension in Firefox, you need to refresh the page. Otherwise, the browser extension installation will begin again. Ticket ID: ID-4248. |

## January 26, 2016:

include::partial$p14e\_p1refs\_faw\.adoc\[tags=faw]Provisioning

Enhancements

| Feature                       | Description                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| Facebook at Work Provisioning | We've updated Facebook at Work provisioning to support additional user attributes. |

Known issues and limitations

| Subject                             | Issue/Limitation                                                                                                                                   |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Known limitations for this release: | * Making attributes create-only isn't supported.

* Clearing fields on updates isn't supported.

* The `roles` field supports only a single value. |

## January 19, 2016:

include::pingone\_for\_enterprise:partial$p14e\_p1refs\_365.adoc\[tags=365]Provisioning

Enhancements

| Feature                 | Description                                                                                                                                                                                                                                         |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Office 365 Provisioning | We've updated Office 365 provisioning to support:- Provisioning additional user attributes.

- Azure Active Directory Graph API v1.6 (updated from version v1.5).

- Clearing of licenses on updates.

- Improved exception handling and reporting. |

Known issues and limitations

| Subject                             | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Known limitations for this release: | * Opting out of license management for users is not supported. The provisioner will clear existing licenses even when the attribute is unmapped.

* User delete is not supported. However, you can disable users.

* Users cannot be created in a disabled state. They must first be created in an active state and then disabled.

* Updating the mobile attribute requires that the service principal representing the provisioner (the place the user gets the Client ID and Secret) be assigned a role with Company Administrator privileges (using PowerShell).

* Updating the ImmutableID and Password attributes is not supported.

* User updates containing a manager that has not yet been provisioned or updated by the new version will fail because the manager will not have the new extended attribute holding their Active Directory distinguished name.

* If the DoBase64Conversion field is set to "false", expect conflicts or failures on federated domains containing pre-existing users provisioned by Dirsync or a Ping product.

* Only outbound provisioning is supported.

* Automatic licensing of users is not supported. |

## January 12, 2016: Minor Release

Resolved issues

| Ticket ID | Issue                                                                                                                                                                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID-3828   | Fixed a misleading error message.                                                                                                                                                                                                                    |
| ID-3758   | Fixed an issue regarding lapse of synchronization between PingOne directory administrators and directory users.                                                                                                                                      |
| SSD-1956  | Fixed an issue where meaningful information wasn't being displayed in the Logout Confirmation screen.                                                                                                                                                |
| ID-3904   | Fixed an issue where some pages were displaying an error saying the domains wasn't set, when the domain had already been set for the PingOne session.                                                                                                |
| ID-3504   | Fixed an issue where you were unable to remove validation certificates assigned to Third-Party SAML identity bridges.                                                                                                                                |
| ID-1656   | Fixed an issue where the instruction steps for creating or editing an application displayed HTML tags and encoded characters.                                                                                                                        |
| BE-656    | (Browser extension) Fixed an issue during adding an application where the prompt to sign in normally for the application site was being displayed a second time after you'd already successfully signed in.                                          |
| BE-623    | (Browser extension) Fixed an issue where the Save popup wasn't being displayed when adding the include::partial$p14e\_p1refs\_netflix.adoc\[tags=netflix]application in include::pingone\_for\_enterprise:partial$p14e\_p1refs\_ie.adoc\[tags=IE]10. |

---

---
title: Previous PingOne SSO for SaaS Apps releases
description: Enhancements
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise_release_notes:p14saas_relnotes_archive
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise_release_notes/p14saas_relnotes_archive.html
revdate: March 30, 2023
section_ids:
  february-2022: February 2022
  october-2021: October 2021
  september-2021: September 2021
  july-2021: July 2021
  june-2021: June 2021
  may-2021: May 2021
  april-2021: April 2021
  march-2021: March 2021
  january-2021: January 2021
  november-2020: November 2020
  october-2020: October 2020
  april-2020: April 2020
  september-november-2019: September-November 2019
  june-2019: June, 2019
  april-2019: April, 2019
  january-2019: January, 2019
  november-2018: November, 2018
  october-2018: October, 2018
  september-2018: September, 2018
  july-2018: July, 2018
  june-2018: June, 2018
  march-2018: March, 2018
  december-2017: December, 2017
  november-2017: November, 2017
  october-2017: October, 2017
  june-2017: June, 2017
  april-may-2017: April-May, 2017
  february-2017: February, 2017
  january-2017: January, 2017
---

# Previous PingOne SSO for SaaS Apps releases

## February 2022

**Enhancements**

| Feature                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Manual Connection IdPID | Removed the ability to change the *idpid* value for an existing manual customer connection.The *idpid* value acts as the identifier for an IdP connection, and changing it can cause unexpected behavior.If you need to change the *idpid* value, you can [create a new manual connection](../pingone_sso_for_saas_apps/p14saas_create_saml_connection.html).For more information, see [What is an idpId?](../pingone_sso_for_saas_apps/p14saas_what_is_idpid.html). |

## October 2021

**Enhancements**

| Feature | Description                                                                                                                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSO/SLO | Increased the `max-age` parameter of the `strict-transport-security` header for the `https://sso.connect.pingidentity.com/sso/` endpoint.The previous `max-age` was 1 year. The new `max-age` is 2 years. |

## September 2021

**Enhancements**

| Feature            | Description                                                                                                                                                                                                                                                                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Custom Entity ID   | Added the ability to define a custom entity ID for applications that are enabled through PingOne.If a custom entity ID is in use by a non-multiplexed connection, it cannot be changed.For more information, see [Add or update other applications](../pingone_sso_for_saas_apps/p14saas_add_update_other_app.html).                       |
| SSO Summary Report | Added a new **SSO User Count** report type.The **SSO User Count** report counts the total number of unique users for a customer during the specified period. You can run the report either by customer name or `IdP ID`.For more information, see [PingOne for Enterprise report types](../pingone_for_enterprise/p14e_report_types.html). |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-16877 | Fixed an issue that reassigned the signing certificate to the default signing certificate when the `signingCertFingerprint` parameter was not specified when updating a customer connection. |

## July 2021

**Enhancements**

| Feature                 | Description                                                                                                                                                                                                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Connection API | Added a feature allowing you to delete customer connections and application connections using the customer connection API.For more information, see [PingOne SSO for SaaS Apps Customer Connection API](../pingone_sso_for_saas_apps/p14saas_customer_connection_api.html). |
| Admin Portal Banner     | Added a feature allowing you to display a banner message in the administrative portal.For more information, see [Assign branding and design](../pingone_sso_for_saas_apps/p14saas_assign_branding_design.html).                                                             |

## June 2021

**Enhancements**

| Feature                        | Description                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Read-Only Administrative Roles | Added a feature allowing you to assign user groups to read-only versions of administrative roles.Read-only roles allow administrators to access the areas of the admin portal normally allowed by that role, but not to change settings.For more information, see [Configure SSO to the admin portal](../pingone_sso_for_saas_apps/p14saas_configure_sso_admin_portal.html). |
| Verbose Reporting              | Added a feature allowing more detailed reports and subscriptions for partner accounts with OIDC identity providers.For more information, see [Creating and administering a partner account](../pingone_sso_for_saas_apps/p14saas_creating_administering_partner_account.html).                                                                                               |

## May 2021

**Enhancements**

| Feature    | Description                                                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Account ID | Added a feature allowing administrative users to look up their unique account ID.To find your account ID, go to **Account > Properties**. |

## April 2021

**Enhancements**

| Feature                          | Description                                                                                                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Invited Connection Contact Email | Added a feature allowing administrators to change the contact email for invited accounts.For more information, see [Edit an invited customer connection](../pingone_sso_for_saas_apps/p14saas_edit_invited_customer_connection.html). |

## March 2021

**Enhancements**

| Feature                       | Description                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Connections REST API | Added request parameters to the Customer Connection Rest API. These optional parameters give you the same control over application connections using the API that you would have using the admin console.For more information, see [PingOne SSO for SaaS Apps Customer Connection API](../pingone_sso_for_saas_apps/p14saas_customer_connection_api.html) |
| OAuth Access Token            | Increased the allowed number of trusted origins for OAuth access token Cross-Origin Resource Sharing. The previous limit was 10. The current limit is 100.For more information, see [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html).                                                                      |

## January 2021

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin Console SSO      | Added the ability to configure your IdP connection to allow administrative users to SSO into the admin console.See **Known issues and limitations** below for important limitations to this feature.For more information, see [Configure SSO to the admin portal](../pingone_sso_for_saas_apps/p14saas_configure_sso_admin_portal.html) |
| PingOne Token Lifetime | Reduced the lifetime of the PingOne user token from ten minutes to five minutes.For more information, see [Process the PingOne SSO for SaaS Apps token exchange](../pingone_sso_for_saas_apps/p14saas_process_p1_token_exchange.html).                                                                                                  |

**Known issues and limitations**

| Subject       | Issue/Limitation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single Logout | PingOne's single logout (SLO) implementation relies on the ability to send cookies within an iframe. Some browsers now block this ability by default, which causes problems with SLO.SLO does not function on browsers where third-party cookies are disabled.This issue impacts SLO on the following browsers:- Safari 13.1+ on MacOS

- Safari on iOS and iPadOS 13.4+

- Any browser where the user has disabled third party cookiesIdP-initiated SLO does not terminate the admin portal session in browsers that enforce SameSite.We are working to accommodate this new behavior. |

## November 2020

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrator Settings | Added a feature that allows you to change the certificate expiration notification settings for Global and SaaS administrators.For more information, see [Editing administrative roles, permissions, and notifications](../pingone_for_enterprise/p14e_editing_administrative_roles_permissions_notifications.html) and [Manage your user profile](../pingone_for_enterprise/p14e_manage_user_profile.html). |

## October 2020

**Enhancements**

| Feature              | Description                                                                                                                                                                                                                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Connections | Added a feature that allows you to filter the list of existing customer connections by status or type.For more information, see [Edit an invited customer connection](../pingone_sso_for_saas_apps/p14saas_edit_invited_customer_connection.html) and [Edit a managed customer connection](../pingone_sso_for_saas_apps/p14saas_edit_managed_customer_connection.html). |

## April 2020

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certificate management | We've added a new certificate management UI. The new UI enables you to:- Create new signing certificates

- View usage of configured certificates

- Migrate individual applications and identity providers to different signing certificates, or change the configured verification certificate

- Automatically receives email notifications when certificates are expiring or have expiredSee [Certificate management](../pingone_sso_for_saas_apps/p14saas_managing_certificates.html) for more information. |

## September-November 2019

**Enhancements**

| Feature                              | Description                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Adding OIDC applications             | We've updated the selection and configuration of OIDC applications, streamlining this process based on the type of OIDC application connection you want to add. See [Adding or updating an OIDC application](../pingone_sso_for_saas_apps/p14saas_add_update_oidc_app.html) for more information.                                                 |
| OpenID Connect login\_hint parameter | We've added the ability for you to pass the `idpid` or email domain in the OpenID Connect (OIDC) login\_hint parameter when adding an OIDC application. See the Default User Profile Attribute Contract settings in [Adding or updating an OIDC application](../pingone_sso_for_saas_apps/p14saas_add_update_oidc_app.html) for more information. |

## June, 2019

**Enhancements**

| Feature                              | Description                                                                                                                                                                                                        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Customer connection email invitation | You can now select the PingOne data center region for invited customers. See [Creating an invited SSO connection](../pingone_sso_for_saas_apps/p14saas_creating_invited_sso_connection.html) for more information. |

## April, 2019

**Enhancements**

| Feature                                                 | Description                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cross-origin resource sharing (CORS) for OpenID Connect | If you're integrating OpenID Connect (OIDC) applications with PingOne, you can now configure one or more trusted origins to enable cross-origin resource sharing (CORS). See [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html) for more information. |

## January, 2019

**Enhancements**

| Feature       | Description                                                                                                                                                                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSO reporting | We've added new report types and predefined reports for SSO transactions. For more information, see .pingidentity.com/pingone/saasSsoAdminGuide/index.shtml//\[Report types] and .pingidentity.com/pingone/saasSsoAdminGuide/index.shtml//\[Report event information]. |

## November, 2018

**Enhancements**

| Feature                  | Description                                                                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Turkish language support | We've updated the PingOne user interface to include support for Turkish. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[PingOne language support]. |

## October, 2018

**Enhancements**

| Feature                                             | Description                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrative auditing (reports and subscriptions) | Administrative auditing is now available PingOne for Enterprise, PingID and PingOne SSO for SaaS Apps. You can utilize the administrative audit events through both the Reports and the Subscriptions facilities.                                                                           |
| PKCE support for OpenID Connect (OIDC)              | We've added support for Proof Key for Code Exchange (PKCE) to secure OIDC clients that cannot or choose not to use a client secret. We have therefore relaxed the requirement that a client secret must be specified when configuring an OIDC application with the authorization code flow. |

## September, 2018

**Enhancements**

| Feature                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PKCE support for OpenID Connect (OIDC) | We've added support for Proof Key for Code Exchange (PKCE) to secure OIDC clients that cannot or choose not to use a client secret. We have therefore relaxed the requirement that a client secret must be specified when configuring an OIDC application with the authorization code flow. For more information, see .pingidentity.com/pingone/employeeSsoAdminGuide/index.shtml//\[Integrate an OIDC application, PKCE parameters] For more information, see .pingidentity.com/pingone/saasSsoAdminGuide/index.shtml//\[Integrate an OIDC application, PKCE parameters]. |

## July, 2018

**Enhancements**

| Feature                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenID Connect applications | PingOne for Enterprise and PingOne SSO for SaaS Apps now support the OpenID Connect (OIDC) protocol for application integration using code, implicit or hybrid flows. You can customize access tokens for your account or per application. Client authentication is done using client secrets.For PingOne for Enterprise, you can make PingOne OIDC applications available on the PingOne dock. The applications are also selectable in access and authentication policies. |

## June, 2018

**Enhancements**

| Feature                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service provider SAML encryption | We have added an option for you to configure encryption of the assertion in the outbound SAML response sent from PingOne for an application. You can assign the encryption algorithm to use. You can also upload your own certificate to use for encryption. NOTE: For enhanced security we will sign the SAML response rather than the assertion in the SAML response when encryption is enabled.See [Adding or updating a SAML-enabled application](../pingone_sso_for_saas_apps/p14saas_add_update_saml_application.html) for more information. |
| Updated navigation design        | We have updated the design of the top-level navigation for the PingOne admin portal. There is no functional or behavioural impact. This is solely a style change.                                                                                                                                                                                                                                                                                                                                                                                  |

## March, 2018

**Resolved issues**

| Ticket ID | Issue                                                                                                     |
| --------- | --------------------------------------------------------------------------------------------------------- |
| SSD-6751  | Fixed an issue where the `restAuthUsername` value wasn't always set when the integration page was loaded. |

## December, 2017

**Enhancements**

| Feature                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SAML signature signing algorithm | We've added the ability for you to configure the signature signing algorithm for all assertion signing to PingOne. PingOne will continue to support the SHA-1 algorithm, but now allows you to select SHA-256, SHA-384 and SHA-512. New SAML connections default to SHA-256. See [Adding or updating a SAML-enabled application](../pingone_sso_for_saas_apps/p14saas_add_update_saml_application.html) for more information. |

## November, 2017

**Known issues and limitations**

| Subject                             | Issue/Limitation                                                                                                                                                                                          |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multiplexing and manual connections | When configuring a manual connection to an application, currently it is possible to select for multiplexing not to be used for non-SAML applications. Multiplexing is used for all non-SAML applications. |

## October, 2017

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                 |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-5879  | Fixed an issue where the number of connections displayed on the My Applications page for applications was incorrect when an application was disabled. |
| SSD-3780  | Fixed an issue where no warning or confirmation prompt was displayed when saving an Attribute Policy that had no associated connection.               |

. Known issues and limitations

| Subject                             | Issue/Limitation                                                                                                                                                                                          |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multiplexing and manual connections | When configuring a manual connection to an application, currently it is possible to select for multiplexing not to be used for non-SAML applications. Multiplexing is used for all non-SAML applications. |

## June, 2017

**Enhancements**

| Feature                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne universal certificate   | A new PingOne universal certificate is now available. If you're using multiplexing, or using manually configured customer connections, you're using the PingOne universal certificate. In this case, it is imperative that you edit the application configuration to update the PingOne universal certificate. See [Update the PingOne SSO for SaaS Apps universal certificate](../pingone_sso_for_saas_apps/p14saas_update_universal_certificate.html) for instructions. |
| PingOne encryption certificate  | When you're adding a customer connection manually, we've added the option to separately download the PingOne encryption certificate.                                                                                                                                                                                                                                                                                                                                      |
| IdP discovery                   | When you edit a customer connection, you need only specify the domain or domains used for customer email addresses and we will use this information to discover the IdP for the connection. We've added the option to set the current connection as the default IdP connection used for all of your applications.We've also updated the IdP Discovery popup window to display the application logo and your corporate logo (if you've configured this).                   |
| Testing application integration | For security reasons, we've disabled connections to the PingOne Test IdP by default. This connection is enabled only when you select to test your application. We also ensure that you can disable the connection when you're done testing.                                                                                                                                                                                                                               |

## April-May, 2017

**Enhancements**

| Feature            | Description                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Corporate branding | We've added an **Account > Branding** page for you to assign branding to be used for your organization's account. |

## February, 2017

**Enhancements**

| Feature                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Salesforce provisioner | We've updated the Salesforce provisioner with the following changes and enhancements:- Support for approximately 150 additional user attributes.

- Support for Salesforce REST v37.0 API.

- Support for OAuth Authentication with the OAuth Configuration Service (OCS).

- Support for custom subdomains.

- You now have the option to freeze user accounts, rather than deactivating them.

- Improved exception handling and reporting.

- Support for Salesforce disabling TLS 1.0. |

**Resolved issues**

| Ticket ID | Issue                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-4316  | Fixed an issue that was prompting a user to activate OAuth when creating a connection for which provisioning was not selected.         |
| IO-2027   | We've improved the handling of different letter case logins and aliases for the Box provisioner.                                       |
| IO-2243   | Fixed an issue with the Microsoft Office 365 provisioner that was causing an error when trying to retrieve a user during provisioning. |
| IO-2242   | Fixed an issue with the WebEx provisioner's handling of the timezones not listed in WebEx's timezone encoding list.                    |

## January, 2017

**Resolved issues**

| Ticket ID | Issue                                                                                                                                                                                                                                         |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSD-4040  | Fixed an issue when filtering dashboard metrics, where filtering by "today" would return 0 results. Also fixed an issue with the mouse over popup on chart data that spanned a DST boundary where the time reported was offset by +1/-1 hour. |
| SSD-4071  | Fixed an issue that was preventing the propagation of SLO settings changed on an application in a PingOne for SaaS Apps account from being applied to all connections to that application.                                                    |