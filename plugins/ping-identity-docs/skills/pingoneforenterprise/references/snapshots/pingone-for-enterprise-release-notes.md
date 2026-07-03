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
