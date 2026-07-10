---
title: PingCentral 1.10 (June 2022)
description: PingCentral release notes, June 2022
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_june2022
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_june2022.html
revdate: August 3, 2023
section_ids:
  update-oauth-and-oidc-template-grant-types-scopes-and-policy-contracts-and-revert-to-previous-versions: Update OAuth and OIDC template grant types, scopes, and policy contracts and revert to previous versions
  update-applications-with-the-latest-template-version-available: Update applications with the latest template version available
  use-sso-to-access-pingfederate-and-pingaccess-from-pingcentral: Use SSO to access PingFederate and PingAccess from PingCentral
  account-lockout-mechanisms-added-to-mitigate-password-guessing: Account lockout mechanisms added to mitigate password guessing
  cannot-update-or-revert-templates-created-in-version-1-2-or-earlier: Cannot update or revert templates created in version 1.2 or earlier
  resolved-a-potential-security-vulnerability: Resolved a potential security vulnerability
  configure-apc-mappings-for-oidc-applications-in-pingfederate: Configure APC mappings for OIDC applications in PingFederate
  sp-certificates-and-assertion-encryption-certificates-must-be-different: SP certificates and assertion encryption certificates must be different
  promoting-applications-with-authentication-challenge-policies: Promoting applications with authentication challenge policies
  update-truststore-path-if-pingcentral-fails-to-start: Update truststore path if PingCentral fails to start
  adding-saml-applications-through-the-api: Adding SAML applications through the API
  managing-environments-through-the-api: Managing environments through the API
---

# PingCentral 1.10 (June 2022)

For the best possible experience, review these notes before using PingCentral 1.10.

## Update OAuth and OIDC template grant types, scopes, and policy contracts and revert to previous versions

New PASS-2017

If you are an administrator, you can now update the grant types, scopes, and policy contracts in OAuth and OpenID Connect (OIDC) templates to further customize them to meet your needs.The history of these templates is also available to review and compare with previous versions. You can see which administrator modified the template configuration or policy contract, when it was modified, and details regarding these modifications. You can also revert templates to previous versions, if necessary. See [Managing templates](../pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html) for details.

## Update applications with the latest template version available

New PASS-6007

If an application is based on an outdated template, an **Outdated Template** icon now displays next to its name in the applications list. Edit the template and click the **Update Template** button. See [Updating applications](../pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html#pingcentral_iam_updating_apps) for details.

## Use SSO to access PingFederate and PingAccess from PingCentral

New PASS-5202 and PASS-6018

You can now use SSO to access PingFederate and PingAccess from PingCentral. For details, see [Configuring PingFederate and PingAccess for SSO](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pf_pa_sso.html).

## Account lockout mechanisms added to mitigate password guessing

Improved PASS-6388

Account lockout mechanisms that prevent users from accessing the application or API after a specified number of failed sign-on attempts were added to this release. Specify the number of failed attempts that are allowed before users are locked out and the lockout period in the `application.yaml` file.

## Cannot update or revert templates created in version 1.2 or earlier

Issue PASS-6466

Templates created in version 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

## Resolved a potential security vulnerability

Security PASS-6387 and PASS-6378

Resolved a potential security vulnerability that is described in security bulletin [SECBL022](https://support.pingidentity.com/s/article/SECBL022-PingCentral-Overly-Permissive-Actuator) (requires sign-on).

## Configure APC mappings for OIDC applications in PingFederate

Issue PASS-6316 PingFederate

PingCentralpromotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.To resolve these issues, configure the APC mappings within PingFederate.

## SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingFederate

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:`Environment'staging': PingFederate. This certificate either has the same ID or the same content as the certificate with index 0.`To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

## Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral, but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

## Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, or 1.10, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

## Adding SAML applications through the API

Issue PASS-5009

If you attempt to add a SAML application to PingCentral from an existing application through the API, and the connection JSON contains identity attribute names and placeholders, you receive an error message advising you to nullify the **Names** field. However, even if you nullify this field, you still receive an error message because the JSON contains placeholders. Remove these placeholders before you proceed.

## Managing environments through the API

Issue PASS-5001 and PASS-5002

When creating, updating, or validating an environment through the API, you receive a server error message if the environment **Name** or **Password** fields are null or missing. API requests cannot be processed without this information, so ensure that these fields contain valid values.You will also receive a misleading error message if the **PingAccess Password** field is null. Rather than informing you that the information in this field is invalid, it informs you that you cannot connect to the PingFederateadministrative console, which is misleading.Requests to connect PingAccess to a PingCentral environment cannot be processed without this information, so ensure that this field contains a valid value.

---

---
title: PingCentral 1.11 (March 2023)
description: PingCentral release notes, March 2023
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_march2023
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_march2023.html
revdate: August 3, 2023
section_ids:
  updated-client-secret-generation-to-produce-client-secrets-compatible-with-pingfederate: Updated client secret generation to produce client secrets compatible with PingFederate
  multiple-acs-urls: Multiple ACS URLs
  set-application-name: Set application name
  deleting-an-application-in-pingcentral-also-deletes-it-in-other-environments: Deleting an application in PingCentral also deletes it in other environments
  configure-oauth-credentials-for-use-instead-of-username-and-password-to-connect-to-pingfederate-or-pingaccess: Configure OAuth credentials for use instead of username and password to connect to PingFederate or PingAccess
  upgraded-from-v1-h2-database-to-v2: Upgraded from v1 H2 database to v2
  configure-apc-mappings-for-oidc-applications-in-pingfederate: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier: Cannot update or revert templates created in 1.2 or earlier
  cannot-migrate-the-h2-database-if-the-installation-path-has-any-spaces: Cannot migrate the H2 database if the installation path has any spaces
---

# PingCentral 1.11 (March 2023)

For the best possible experience, review these notes before using PingCentral 1.11.

## Updated client secret generation to produce client secrets compatible with PingFederate

New

When creating a new client, PingCentral now generates OAuth client secrets compatible with PingFederate. For more information, see [Promoting OAuth and OIDC applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html#oauth).

## Multiple ACS URLs

New

You can now configure multiple Assertion Consumer Service (ACS) URLs during SAML application creation. This new feature simplifies application development since the same application can use different URLs simultaneously. For more information, see [Using SAML 2.0 templates](../pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html#saml_template).

## Set application name

New

When promoting an application between environments, you can now configure an application name for OAuth and OpenID Connect (OIDC) clients, SAML connections, and PingAccess applications. For more information, see [Promoting applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html).

## Deleting an application in PingCentral also deletes it in other environments

Improved

You can now choose to delete applications from PingFederate or PingAccess in addition to PingCentral. This feature is flexible because you can select which environments to delete the application from. For more information, see [Managing applications](../pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html).

## Configure OAuth credentials for use instead of username and password to connect to PingFederate or PingAccess

Improved

Instead of using administrator credentials for basic authentication, you can now configure PingCentral to use OAuth client credentials to connect to PingFederate or PingAccess. will request an `access_token` to use whenever it connects to PingFederate or PingAccess. For more information, see [Configuring PingFederate and PingAccess for SSO](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pf_pa_sso.html).

## Upgraded from v1 H2 database to v2

Security

Along with other dependencies (libraries), we've upgraded the H2 database from v1 to v2. For more information, see [Upgrading PingCentral](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_upgrading/pingcentral_upgrading_pc.html).

## Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

## Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

## SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

`Environment'staging': PingFederate. This certificate either has the same ID or the same content as the certificate with index 0.`

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

## Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

## Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

## Cannot migrate the H2 database if the installation path has any spaces

Issue PASS-6591

If the installation path has any spaces in the existing or new instance, the H2 database is not migrated during upgrade. Upon removing the spaces from the file path, the migration is successful.

---

---
title: PingCentral 1.12 (June 2023)
description: PingCentral release notes, June 2023
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_june2023
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_june2023.html
revdate: September 15, 2023
section_ids:
  approval-workflow: Approval workflow
  client-secret-management-enhancements: Client secret management enhancements
  multiple-slo-service-urls: Multiple SLO Service URLs
  jdk-17-support: JDK 17 support
  saml-metadata-export: SAML metadata export
  configure-apc-mappings-for-oidc-applications-in-pingfederate: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier: Cannot update or revert templates created in 1.2 or earlier
---

# PingCentral 1.12 (June 2023)

New features and improvements in PingCentral 1.12.

## Approval workflow

New PASS-6479

Previously, PingCentral did not allow an administrator to require approval for a non-administrator to promote an application to an environment. As of now, administrators can use Spring Expression Language (SpEL) based rules to trigger an approval requirement if an expression is or isn't met. Administrators will find a bell icon indicating active approval requests, and developers are informed when their requests are approved. For more information, see xref:pingcentral\_for\_iam\_administrators:

Learn more in [Managing approvals (administrators)](../pingcentral_for_iam_administrators/pingcentral_mng_approvals/pingcentral_manage_approvals.html).

## Client secret management enhancements

Improved PASS-6500

Administrators can now enforce a strong client secret for applications by requiring that PingCentral generate the client secret. With this feature enabled, when developers promote an application, they won't be able to create a client secret manually. This avoids the usage of weak client secrets. For more information, see [Managing environments](../pingcentral_for_iam_administrators/pingcentral_mng_environments/pingcentral_mng_environments.html).

## Multiple SLO Service URLs

New PASS-6609

When promoting SAML applications, developers can adjust and configure single logout (SLO) URLs. This adds flexibility and removes the need to manage multiple SAML applications only because different SLO URLs are required. For more information, see [Promoting SAML applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html#saml).

## JDK 17 support

New

We added support for Java Development Kit (JDK) 17.

## SAML metadata export

Fixed PASS-5630

To set up a service provider (SP) connection, PingCentral now accepts SAML metadata files exported from other SP connections. These files are used to extract the following information: entity IDs, ACS URLs, SLO service URLs, certificates, and attributes.

## Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

## Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

## SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

```
Environment'staging':  {pingfed}. This certificate either has the same ID or the same content as the certificate with index 0.
```

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

## Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

## Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

---

---
title: PingCentral 1.13
description: PingCentral 1.13 was skipped.
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_version_113
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_version_113.html
revdate: May 3, 2024
---

# PingCentral 1.13

PingCentral 1.13 was skipped.

---

---
title: PingCentral 1.14 (September 2023)
description: PingCentral release notes, September 2023
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_sept2023
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_sept2023.html
revdate: December 13, 2023
section_ids:
  disable-environments-when-down-for-maintenance-or-offline: Disable environments when down for maintenance or offline
  import-saml-connection-to-pingcentral-from-pingfederate-with-attributes-mapped-to-data-source: Import SAML Connection to PingCentral from PingFederate with attributes mapped to data source
  additional-synchronization-capabilities: Additional synchronization capabilities
  other-improvements: Other improvements
  h2-database-migration-when-the-installation-path-has-any-spaces: H2 database migration when the installation path has any spaces
  sso-inactivity-sign-off: SSO inactivity sign off
  multi-apc-connection-synchronization: Multi-APC connection synchronization
  configure-apc-mappings-for-oidc-applications-in-pingfederate: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier: Cannot update or revert templates created in 1.2 or earlier
---

# PingCentral 1.14 (September 2023)

New features and improvements in PingCentral 1.14.

## Disable environments when down for maintenance or offline

New PASS-6666 and PASS-6683

PingCentral administrators can now disable referenced PingFederate environments for any reason, such as PingFederate being unavailable due to maintenance tasks. Additionally, we added a new environment status bar that indicates if an environment is offline. In such cases, application owners will receive a notification indicating that the environment is disabled or offline rather than encountering a UI error. For more information, see step 1 of the Updating environments tab in [Managing environments](../pingcentral_for_iam_administrators/pingcentral_mng_environments/pingcentral_mng_environments.html).

## Import SAML Connection to PingCentral from PingFederate with attributes mapped to data source

New PASS-6667

All attributes defined in a SAML SP connection are now integrated into the PingCentral application. This enhancement eliminates a limitation and is expected to enhance usability significantly. For more information, see step 3 in [Using SAML 2.0 templates](../pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html#saml_template).

## Additional synchronization capabilities

New PASS-6696

We added the ability to effortlessly initiate an application synchronization in PingCentral. Now, when you make external modifications to an application configuration, you can seamlessly update the application information within PingCentral. This removes the need to manually update application information and introduces a more streamlined and efficient process. For more information, see step 2 in [Updating applications](../pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html#pingcentral_iam_updating_apps).

## Other improvements

New

* We also updated the following bundled components and third-party dependencies:

  * Apache Commons Text 1.10

## H2 database migration when the installation path has any spaces

Fixed PASS-6591

We resolved an issue where H2 database migration fails during an upgrade if there are spaces in the installation path for the existing or new instance.

## SSO inactivity sign off

Fixed PASS-6690

We fixed an issue where utilizing single sign-on (SSO) to access the PingCentral console incorrectly triggered a timeout based on an ID token's lifetime.

## Multi-APC connection synchronization

Issue PASS-6705

Previously, PingCentral was unable to handle a service provider (SP) connection with multiple Authentication Policy Contracts (APC) mapped within it. The PingCentral 1.14 release enables users to select from multiple mapped contracts when adding an application as a managed application or a template.

However, due to a known synchronization limitation, if you update an existing single APC SP connection already managed by PingCentral to include a second APC and subsequently synchronize the application, you won't find an option to specify your preferred APC.

To simplify your workflow and mitigate potential challenges, we recommend refraining from using synchronization to modify multi-APC connections. Instead, consider creating a new SP connection that aligns with your desired APC configuration. This approach grants you control over APC selection, ensuring a smoother and more efficient process.

## Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

## Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

## SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

```
Environment'staging':  {pingfed}. This certificate either has the same ID or the same content as the certificate with index 0.
```

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

## Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

## Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

---

---
title: PingCentral 1.14.1 (November 2023)
description: PingCentral release notes, November 2023
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_nov2023
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_nov2023.html
revdate: December 13, 2023
section_ids:
  forbidden-error-when-loading-api-documentation: Forbidden error when loading API documentation
---

# PingCentral 1.14.1 (November 2023)

Enhancements and resolved issues in PingCentral 1.14.1.

## Forbidden error when loading API documentation

Fixed PASS-6820

We fixed an error that prevented API documentation from loading when using OIDC single sign-on (SSO) with PingCentral.

---

---
title: PingCentral 2.0 (December 2023)
description: New features and improvements in PingCentral 2.0.
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_dec2023
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_dec2023.html
revdate: December 19, 2023
section_ids:
  template-synchronization-now-available-for-saml-and-pingaccess-applications: Template synchronization now available for SAML and PingAccess applications
  application-owners-can-now-edit-application-json-themselves: Application owners can now edit application JSON themselves
  prevent-application-owners-from-deleting-applications: Prevent application owners from deleting applications
  hide-inactive-promotion-approvals: Hide inactive promotion approvals
  approval-expressions-drag-and-drop-enhancement: Approval expressions drag and drop enhancement
  multi-apc-connection-synchronization: Multi-APC connection synchronization
  configure-apc-mappings-for-oidc-applications-in-pingfederate: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier: Cannot update or revert templates created in 1.2 or earlier
---

# PingCentral 2.0 (December 2023)

New features and improvements in PingCentral 2.0.

## Template synchronization now available for SAML and PingAccess applications

New PASS-6730

Administrators can now synchronize OAuth, OIDC, SAML, and PingAccess templates to ensure that their templates are based on the most up-to-date configurations available. Applications based on out-of-date templates have **Outdated Template** icons displayed next to them, which inform application owners that newer versions of the templates are available.

Administrators can also now revert SAML SP connections and PingAccess application templates to previous versions. You can find details on the **Reverting templates to previous versions** tab on the [Managing templates](../pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html).

Note that when you upgrade to PingCentral 2.0, SAML and PingAccess application templates will have base revisions created for them. OAuth and OIDC templates created prior to version 2.0 cannot be synced with the most recent configurations available. Recreate the template in version 2.0 to use the sync feature going forward.

## Application owners can now edit application JSON themselves

New PASS-6670

To accommodate a wide variety of promotion needs, application owners can now edit the application JSON for their applications when they promote them.

Note that providing application owners with this ability can be risky, so it's highly recommended that approvals are enabled for the environment. Administrators can review the submitted application JSON and compare it to the original application JSON before approving the promotion request.

Also note that:

* This functionality is not yet available for PingAccess applications.

* Applications cannot be reverted to a promotion that uses JSON editing.

* Be aware that the JSON review window compares against the original application JSON and not the most recently promoted JSON.

## Prevent application owners from deleting applications

New PASS-6731

To prevent application owners from accidentally deleting applications from PingFederate (and PingAccess, when applicable) environments, you can enable a new option that allows only administrators to delete applications from the environment.

## Hide inactive promotion approvals

Improved PASS-6733

To help manage promotion approvals, both administrators and application owners can now hide promotion approvals that are in a **canceled**, **promoted**, or **rejected** status that display on the **Promotion Approvals** page. The **Visible** filter is enabled by default.

## Approval expressions drag and drop enhancement

Improved PASS-6732

Administrators can add multiple approval expressions for an environment, which are evaluated sequentially from top to bottom in an IF/ELSE chain. Now, administrators can change the order in which these expressions display in the list by dragging and dropping them into different locations within the list instead of copying and pasting them between fields.

## Multi-APC connection synchronization

Issue PASS-6705

Previously, PingCentral was unable to handle a service provider (SP) connection with multiple Authentication Policy Contracts (APC) mapped within it. The PingCentral 1.14 release enables users to select from multiple mapped contracts when adding an application as a managed application or a template.

However, due to a known synchronization limitation, if you update an existing single APC SP connection already managed by PingCentral to include a second APC and subsequently synchronize the application, you won't find an option to specify your preferred APC.

To simplify your workflow and mitigate potential challenges, we recommend refraining from using synchronization to modify multi-APC connections. Instead, consider creating a new SP connection that aligns with your desired APC configuration. This approach grants you control over APC selection, ensuring a smoother and more efficient process.

## Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

## Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

## SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

```
Environment'staging':  {pingfed}. This certificate either has the same ID or the same content as the certificate with index 0.
```

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

## Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

## Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

---

---
title: PingCentral 2.0.1 (January 2024)
description: PingCentral release notes, January 2024
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_jan2024
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_jan2024.html
revdate: April 23, 2024
section_ids:
  approval-window-now-displays-most-recently-promoted-version: Approval window now displays most recently promoted version
  updated-json-for-oidc-applications-now-displays-in-pingfederate-after-promotion: Updated JSON for OIDC applications now displays in PingFederate after promotion
  application-synchronization-now-works-as-expected-for-oidc-applications: Application synchronization now works as expected for OIDC applications
---

# PingCentral 2.0.1 (January 2024)

## Approval window now displays most recently promoted version

Fixed PASS-6865

Previously, when administrators reviewed application promotion requests and compared the submitted JSON to the most recently promoted version, the original version was displayed instead of the most recently promoted version. This issue has been resolved, and the most recently promoted version now displays in the approval window.

## Updated JSON for OIDC applications now displays in PingFederate after promotion

Fixed PASS-6900

Previously, if application owners updated the underlying application JSON in their OIDC applications, and administrator approval was required to promote them, the updated JSON was not reflected in PingFederate. This issue has been resolved and the updated JSON now displays in PingFederate as expected.

## Application synchronization now works as expected for OIDC applications

Fixed PASS-6901

Previously, when OIDC applications were synchronized to the most up-to-date configurations available, they were saved as OAuth applications. This issue has been resolved, and the synchronization process now works as expected.

---

---
title: PingCentral 2.0.2 (April 2024)
description: PingCentral release notes, April 2024
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_april2024
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_april2024.html
revdate: April 24, 2024
section_ids:
  upgrade-processes-now-work-as-expected: Upgrade processes now work as expected
  expressions-can-now-be-added-or-updated-in-saml-applications: Expressions can now be added or updated in SAML applications
  saml-application-templates-can-now-be-updated: SAML application templates can now be updated
  database-errors-no-longer-occur-during-upgrade: Database errors no longer occur during upgrade
---

# PingCentral 2.0.2 (April 2024)

## Upgrade processes now work as expected

Fixed PASS-6905

Previously, if PingCentral had at least one (service provider) SP connection or one PingAccess template, upgrades from version 1.14 to 2.0 would fail. This issue has been resolved and upgrades now work as expected.

## Expressions can now be added or updated in SAML applications

Fixed PASS-6906

Previously, if applications were created from SAML templates that contained at least 1 OGNL expression, the expressions could not be updated, nor could new expressions be added for attribute mapping. This issue has been resolved, and expressions can now be added and updated as needed.

## SAML application templates can now be updated

Fixed PASS-6907

Previously, when administrators tried to change the templates associated with SAML applications, the change would not be saved. This issue has been resolved, and SAML applications can now be updated with new templates.

## Database errors no longer occur during upgrade

Fixed PASS-6940

Previously, if PingCentral had a SAML template with expressions or PingAccess templates, database errors would occur when upgrading from version 1.14 to 2.0. The issue has been resolved and upgrade processes now work as expected.

---

---
title: PingCentral 2.1 (June 2024)
description: New PASS-6911
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_june2024
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_june2024.html
revdate: October 10, 2025
section_ids:
  more-control-over-client-secrets: More control over client secrets
  mtls-is-now-supported: mTLS is now supported
  rocky-linux-is-now-supported: Rocky Linux is now supported
  new-email-parameter-added-to-all-user-accounts: New email parameter added to all user accounts
  performance-improvements: Performance improvements
  application-owners-limited-to-whom-they-can-assign-as-owners: Application owners limited to whom they can assign as owners
  certificates-management-usability-improvement: Certificates management usability improvement
  application-owners-list-is-now-easier-to-navigate: Application owners list is now easier to navigate
  change-template-button-fixed: Change Template button fixed
  json-editor-promotion-issues-resolved: JSON editor promotion issues resolved
  keystore-password-issues-resolved: Keystore password issues resolved
  assertion-encryption-certificate-issues-resolved: Assertion encryption certificate issues resolved
---

# PingCentral 2.1 (June 2024)

## More control over client secrets

New PASS-6911

Application owners now have more control over which client secrets are used when promoting OAuth and OIDC applications from PingCentral to PingFederate. If the application is configured to use a client secret for authentication, and the environment to which the application is being promoted requires that a random secret be used, users can choose to either generate a new client secret or retain the existing client secret. See [Promoting OAuth and OIDC applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html#oauth) for details.

## mTLS is now supported

New PASS-6915

Mutual TLS (mTLS) can now be used for admin API authentication from PingCentral to PingFederate. To set up this connection, access the new **Client TLS Key Pair** page, import the key pair that you want to use for authentication, and configure the environment to use the client certificate you specify. The **TLS Key Pair** page has also been renamed to **Server TLS Key Pair** to clearly differentiate between them. See [Configuring MTLS](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_config_mtls.html) for details.

## Rocky Linux is now supported

New PASS-6918

Rocky Linux version 9.3 and later is now a supported enterprise operating system.

## New email parameter added to all user accounts

New PASS-6967

The email parameter has been added to all PingCentral user accounts, which will let you extract users' email addresses and notify them about important events, such as upgrades, and maintenance windows. The **Email Address** field now displays on the **Add** and **Edit User** pages, an email property has been added to the API, and for SSO configurations, PingCentral will derive the user's email from the email claim defined by the email scope.

## Performance improvements

Improved PASS-6904 and PASS-6910

If you have many different applications in many different environments, or if you have many groups using SSO to access PingCentral, you will notice that performance has been greatly improved with this release. Now, when you filter your applications, you will only see managed applications (created from or promoted to PingCentral environments) by default, which improves page loading speeds. The application owner search functionality has also been improved, which makes it faster and easier to configure owners for applications.

## Application owners limited to whom they can assign as owners

Improved PASS-6913

Previously, when application owners used SSO to sign on to PingCentral and group memberships were also supplied, application owners could select any group as an owner of their application, which gave all group members the ability to manage it. Now, application owners can only select a group as an owner if the application owner is a member of the group.

## Certificates management usability improvement

Improved PASS-6917

When promoting SAML applications, the names of the signing certificates available now include the valid date range, which makes it easier to discern between certificates.

## Application owners list is now easier to navigate

Fixed PASS-2114

Previously, all application owners were listed on the application **Summary** tab, regardless of the number of owners. If an application had a large number of owners, the list would be long and difficult to read. Now, if the list is large, **Show More** and **Show Less** buttons are available to help you navigate the list.

## Change Template button fixed

Fixed PASS-6941

Previously, when importing metadata for a SAML application, the **Change Template** button would disappear. This issue has been fixed, and the **Change Template** button continually displays as expected.

## JSON editor promotion issues resolved

Fixed PASS-6966

Previously, under certain circumstances, server errors were encountered when JSON-based promotions occurred. This issue has been resolved.

## Keystore password issues resolved

Fixed PASS-6970

Previously, when configuring an environment and uploading a signing certificate, if an existing keystore file (\*.p12) was selected, the matching password provided could be too long for PingCentral to accept. This password limit has been increased.

## Assertion encryption certificate issues resolved

Fixed PASS-6985

Previously, if an application was configured with an assertion encryption certificate, the certificate would disappear from the **Promote to Environment** modal when the application was being promoted, and users had to upload the certificate again. This issue has been resolved.

---

---
title: PingCentral 2.2 (December 2024)
description: PingCentral release notes, December 2024
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_dec2024
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_dec2024.html
revdate: December 20, 2024
section_ids:
  trusted-ognl-expression-usability-improvement: Trusted OGNL expression usability improvement
  signing-and-encryption-certificates-can-now-be-the-same: Signing and encryption certificates can now be the same
  spring-security-upgrade: Spring Security upgrade
  cve-issues-fixed: CVE issues fixed
  upgrade-issues-fixed: Upgrade issues fixed
  saml-application-deletion-issue-resolved: SAML application deletion issue resolved
  pingcentral-and-pingfederate-application-sync-issue-resolved: PingCentral and PingFederate application sync issue resolved
---

# PingCentral 2.2 (December 2024)

## Trusted OGNL expression usability improvement

Improved PASS-7028

Previously, trusted OGNL expressions could only be assigned to applications one at a time. Now, a **Select All** checkbox is available to select all applications and assign the selected trusted OGNL expression to them.

## Signing and encryption certificates can now be the same

Improved PASS-7029

Previously, PingCentral did not allow the signing and encryption certificate the same, which is allowed in PingFederate. When application owners tried to promote and upload the same certificate and use it for both the signing and encryption certificate, users received validation errors. Now, the same certificates can be used in PingCentral.

## Spring Security upgrade

Improved PASS-7019

Spring Security has been upgraded from version 5.7.11 to prevent future false-positive scan alerts. Learn more about this upgrade in [CVE-2024-22257: Possible Broken Access Control in Spring Security With Direct Use of AuthenticatedVoter](https://spring.io/security/cve-2024-22257) in the Spring documentation.

## CVE issues fixed

Fixed PASS-7020

A number of third-party libraries have been updated to address Common Vulnerabilities and Exposures (CVEs) reported in these libraries. These CVEs were not exploitable, but they were updated to avoid unnecessary concerns.

## Upgrade issues fixed

Fixed PASS-7023

Previously, when upgrading from PingCentral 2.0.2 to 2.1.0, users received a warning message regarding their APIs. This issue has been resolved, and this message no longer displays when the upgrade is performed.

## SAML application deletion issue resolved

Fixed PASS-7026

Previously, when users tried to delete SAML applications, either through the PingCentral UI or API, and they selected the **Delete from PingFederate in all environments** option, the application was not deleted in PingFederate. This issue has been resolved and now works as expected.

## PingCentral and PingFederate application sync issue resolved

Fixed PASS-7027

Previously, when syncing a PingCentral application with a server-side PingFederate application, data within the **advancedEditPromotionJson** field was being deleted. This issue has been resolved, and the data within that field is now preserved.

---

---
title: PingCentral 2.3 (April 2025)
description: PingCentral release notes, April 2025
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_april2025
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_april2025.html
revdate: March 27, 2025
section_ids:
  fips-compliant-mode-now-available: FIPS-compliant mode now available
  spring-security-upgrade: Spring Security upgrade
  d3-color-upgrade: d3-color upgrade
  promotion-approval-requests-enhanced: Promotion approval requests enhanced
  updated-scripts: Updated scripts
  jdk-21-support-added: JDK 21 support added
---

# PingCentral 2.3 (April 2025)

## FIPS-compliant mode now available

New PASS-7036

Administrators can now enable PingCentral to run in FIPS-compliant mode, which guarantees that all cryptographic algorithms and protocols meet the U.S. federal standard for security compliance.

To enable this option, access the `<PingCentral_install>/conf/application.properties` file and set the `pingcentral.fips.enabled` property value to `true`. Learn more in [Configuring PingCentral to run in FIPS-compliant mode](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_fips_mode.html).

PingCentral is currently running FIPS 140-3. Learn more about this version in [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final).

## Spring Security upgrade

Improved PASS-7022

Spring Security has been upgraded from version 5.3.31 to 5.3.39 to prevent future false-positive scan alerts. You can find more information in [CVE-2024-38816: Path traversal vulnerability in functional web frameworks](https://spring.io/security/cve-2024-38816^) in the Spring documentation.

## d3-color upgrade

Improved PASS-7031

The d3-color package has been upgraded from version 1.4.1 to 3.1.0, where the security vulnerability was fixed.

## Promotion approval requests enhanced

Improved PASS-7033

Those who approve promotions can now determine if a promotion approval request is for a new or existing application by viewing the newly added detail on the **Promotion Approvals** page. **Last Promoted** or **Last Updated** now displays next to the date and timestamp that indicates when the application was last promoted or updated.

## Updated scripts

Improved PASS-7037

All PingCentral scripts have been updated to be DevOps-friendly.

## JDK 21 support added

New PASS-7038

Support was added for Java Development Kit (JDK) 21 using language level 11.

---

---
title: PingCentral 3.0 (November 2025)
description: New PASS-7124
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_nov2025
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_nov2025.html
section_ids:
  pingfederate-extended-properties-are-now-available-in-pingcentral: PingFederate extended properties are now available in PingCentral
  entire-urls-now-visible: Entire URLs now visible
  opencsv-upgrade: Opencsv upgrade
  spring-security-upgrade: Spring Security upgrade
  java-runtime-environment-update: Java runtime environment update
  nimbus-jose-jwt-libraries-updated: Nimbus JOSE + JWT libraries updated
  safeguards-are-now-available-for-overwriting-pingfederate-entity-ids: Safeguards are now available for overwriting PingFederate entity IDs
  strict-transport-security-hsts-header-issue-resolved: Strict-Transport-Security (HSTS) header issue resolved
  cve-issues-fixed: CVE issues fixed
  pingcentral-now-prevents-users-from-creating-apps-with-the-same-name: PingCentral now prevents users from creating apps with the same name
  client-secret-size-increased: Client secret size increased
---

# PingCentral 3.0 (November 2025)

## PingFederate extended properties are now available in PingCentral

New PASS-7124

PingFederate extended properties are single or multi-value fields that are used to store additional information about connections or OAuth clients. These properties are now displayed in PingCentral templates. Administrators can set these property values when they configure templates, and the applications created from these templates inherit those values. Application owners can also update these values unless the extended property is designated as read-only.

## Entire URLs now visible

Improved PASS-7098

Several UI modifications have been made that allow you to see entire URLs within text fields. This new functionality makes it easier for users to verify URLs, and helps prevent copy and paste errors.

## Opencsv upgrade

Improved PASS-7099

Opencsv has been upgraded from version 5.8 to 5.11.2 to prevent future false-positive scan alerts. You can find more information about the [CVE-2025-48734 vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-48734) on the National Vulnerability Database site.

## Spring Security upgrade

Improved PASS-7100

Spring Security has been upgraded from version 5.3.39 to 6.2.8 to prevent future false-positive scan alerts. You can find more information in [CVE-2024-22243: Spring Framework URL Parsing with Host Validation](https://spring.io/security/cve-2024-22243) in the Spring documentation.

## Java runtime environment update

Improved PASS-7106

You can now use either Java 17 or Java 21 as the PingCentral runtime environment. Java 11 is no longer supported.

## Nimbus JOSE + JWT libraries updated

Improved PASS-7134

The Nimbus JOSE + JWT libraries have been upgraded. You can find more information about the [CVE-2025-53864 vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-53864) on the National Vulnerability Database site.

## Safeguards are now available for overwriting PingFederate entity IDs

Fixed PASS-7105

Previously, it was possible to overwrite a connection in PingFederate if you created a PingCentral application with an entity ID that already exists in PingFederate. This issue has been resolved, and it's no longer possible to create new applications using an entity ID that is already used by a PingFederate connection.

## Strict-Transport-Security (HSTS) header issue resolved

Fixed PASS-7097

Previously, if OIDC single sign-on (SSO) was enabled, PingCentral stopped sending the HSTS header and administrators couldn't sign on. This issue has been resolved and SSO now works as expected.

## CVE issues fixed

Fixed PASS-7101

A number of third-party libraries have been updated to address Common Vulnerabilities and Exposures (CVEs) reported in these libraries. These CVEs weren't exploitable, but they were updated to avoid unnecessary concerns.

## PingCentral now prevents users from creating apps with the same name

Fixed PASS-7133

PingCentral now enforces consistent validation to ensure that new applications cannot have the same name as existing applications.

## Client secret size increased

Fixed PASS-7135

Previously, when users attempted to configure a PingCentral environment connection to PingFederate and PingAccess using PingOne OAuth app credentials, the database column wasn't large enough to store the client secret and an error message displayed. The column limit was increased, which resolved the issue.

---

---
title: PingCentral 3.0.1 (March 2026)
description: Fixed PASS-7151
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_march_2026
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_march_2026.html
section_ids:
  bc-fips-and-java-17-issue-resolved: BC FIPS and Java 17 issue resolved
  obfuscated-password-issue-resolved: Obfuscated password issue resolved
  template-issue-resolved: Template issue resolved
  sql-errors-resolved: SQL errors resolved
  pingaccess-application-creation-issue-resolved: PingAccess application creation issue resolved
---

# PingCentral 3.0.1 (March 2026)

## BC FIPS and Java 17 issue resolved

Fixed PASS-7151

Previously, if you were using Java 17 and BC FIPS was enabled, PingCentral failed to start. This issue has been resolved.

## Obfuscated password issue resolved

Fixed PASS-7153

Previously, the `obfuscate.sh <password>` command line utility (CLI) did not work out-of-the-box unless you modified the script. Once modified, the script was able to generate an obfuscated password, but if you tried to use this password to connect to an external database, PingCentral would fail to start. The CLI has been fixed and now works as expected.

## Template issue resolved

Fixed PASS-7156

Previously, after upgrading from version 2.3 to 3.0, administrators using a PostgreSQL database received a server error message when they tried to create a new template. This issue has been resolved.

## SQL errors resolved

Fixed PASS-7164

Previously, when users attempted to promote new applications and IDs were created with MySQL 8, SQL errors occurred. This issue has been resolved.

## PingAccess application creation issue resolved

Fixed PASS-7169

Previously, users could not create PingAccess applications if the `ApplicationResources` property was set to `null`. This issue has been resolved.

---

---
title: PingCentral 3.1 (April 2026)
description: PingCentral release notes, March 2026
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_april2026
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_april2026.html
revdate: April 2, 2026
section_ids:
  administrators-can-now-configure-signature-policies-for-saml-sp-connections: Administrators can now configure signature policies for SAML SP connections
  openjdk-version-requirements-if-using-fips-compliant-mode: OpenJDK version requirements if using FIPS-compliant mode
  security-vulnerability-fixed: Security vulnerability fixed
  apache-commons-compress-updated: Apache Commons Compress updated
  moment-js-updated: Moment.js updated
  option-to-download-saml-idp-metadata-issue-fixed: Option to download SAML IdP metadata issue fixed
  swagger-ui-library-updated: Swagger UI library updated
  swagger-json-fixed: Swagger.json fixed
  api-loading-issues-resolved: API loading issues resolved
  h2-database-updated: H2 database updated
  hibernate-library-updated: Hibernate library updated
  socket-appender-in-apache-log4j-updated: Socket Appender in Apache Log4j updated
  sso-issue-resolved: SSO issue resolved
  outdated-uri-issue-resolved: Outdated URI issue resolved
---

# PingCentral 3.1 (April 2026)

## Administrators can now configure signature policies for SAML SP connections

New PASS-7155

Administrators can now configure signature policies for SP connections when they create templates and applications, and promote applications to PingCentral environments.

Previously, PingFederate administrators had to configure the signature policies after the applications were promoted to PingFederate, which interrupted their workflow and caused unnecessary delays in the process.

Note that signature policy configurations are only visible if the corresponding profiles and artifact binding are enabled in the underlying PingFederate SP connection. To learn more, refer to step 8 in [Adding SAML application templates](../pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html#_adding_saml_application_templates).

## OpenJDK version requirements if using FIPS-compliant mode

Info PASS-7204

If the FIPS-compliant mode is enabled and OpenJDK 21 is being used, OpenJDK version 21.0.10 or higher is required.

## Security vulnerability fixed

Fixed PASS-1323

We've fixed the client-side security vulnerability in DOM-based XSS in redirect URI definitions.

## Apache Commons Compress updated

Fixed PASS-5852

The Apache Commons Compress has been updated to version 1.26, which resolved the security vulnerability that affected versions 1.0 to 1.21. You can find more information about the [CVE-2021-36090 vulnerability](https://nvd.nist.gov/vuln/detail/cve-2021-36090) on the National Vulnerability Database site.

## Moment.js updated

Fixed PASS-6410

Moment.js has been updated to version 2.29.4, which resolved the path traversal vulnerability that affected versions 1.0.1 to 2.29.1. You can find more information about the [CVE-2022-24785 vulnerability](https://nvd.nist.gov/vuln/detail/cve-2022-24785) on the National Vulnerability Database site.

## Option to download SAML IdP metadata issue fixed

Fixed PASS-7017

We've fixed the **Promotion Details** page so that it now displays the option to download the SAML IdP metadata if the application was promoted directly from the JSON file.

## Swagger UI library updated

Fixed PASS-7021

The Swagger UI library has been updated from version 2.9.2 to 3.23.11 to prevent future false-positive scan alerts. You can find more information about the [CVE-2019-17495 vulnerability](https://nvd.nist.gov/vuln/detail/cve-2019-17495) on the National Vulnerability Database site.

## Swagger.json fixed

Fixed PASS-7132

We've fixed the swagger.json endpoint, and it now returns information about the Admin API as expected.

## API loading issues resolved

Fixed PASS-7163

We've fixed the issue where users encountered a continuous loading screen when they tried to access the API. The API now works as expected and returns a response.

## H2 database updated

Fixed PASS-7070

The H2 database has been updated to version 2.2.220, which resolved the security vulnerability that affected version 2.1.210. You can find more information about the [CVE-2022-45868 vulnerability](https://nvd.nist.gov/vuln/detail/cve-2022-45868) on the National Vulnerability Database site.

## Hibernate library updated

Fixed PASS-7172

The `hibernate-ehcache` library is no longer used, which resolved the security vulnerability. You can find more information about the [CVE-2026-0603 vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-0603) on the National Vulnerability Database site.

## Socket Appender in Apache Log4j updated

Fixed PASS-7174

The Socket Appender in Apache Log4j has been updated to version 2.25.3, which resolved the security vulnerability that affected versions 2.0-beta9 through 2.25.2. You can find more information about the [CVE-2025-68161 vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-68161) on the National Vulnerability Database site.

## SSO issue resolved

Fixed PASS-7176

We've fixed an issue with SSO, and users are now redirected to the PingFederate sign-on page instead of the PingCentral home page when they sign on.

## Outdated URI issue resolved

Fixed PASS-7187

We've fixed an issue where redirect URIs were still displayed in OAuth or OIDC applications after the environment referenced in the URI was deleted.

---

---
title: PingCentral 3.1.1 (May 2026)
description: PingCentral release notes, January 2024
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_may2026
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_may2026.html
section_ids:
  pingfederate-extended-properties-fixed: PingFederate extended properties fixed
---

# PingCentral 3.1.1 (May 2026)

## PingFederate extended properties fixed

Fixed PASS-7205

Starting with PingCentral version 3.0, PingFederate extended properties are displayed in PingCentral templates. Administrators can set these values when they configure templates, and the applications created from these templates inherit them. Application owners can also update these values, unless the extended property is designated as read-only.

We've fixed the issues users experienced when promoting applications created from templates that were configured prior to version 3.0. Because PingCentral applications and templates did not include extended properties in earlier versions, empty values could overwrite the existing values in the PingFederate client or connection.

PingFederate extended property values are no longer overwritten, and the extended property values are visible in PingCentral templates and applications when you refresh the page.

---

---
title: Previous Releases
description: PingCentral release notes for 2022 and earlier
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_prev_relnotes
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_prev_relnotes.html
revdate: August 3, 2023
section_ids:
  2022-release-notes: 2022 release notes
  2021-release-notes: 2021 release notes
  2020-release-notes: 2020 release notes
  2019-release-notes: 2019 release notes
---

# Previous Releases

## 2022 release notes

* [PingCentral 1.10 (June 2022)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_June2022)

* [PingCentral 1.9.3 (February 2022)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_193)

## 2021 release notes

* [PingCentral 1.9.2 (December 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_192)

* [PingCentral 1.9.1 (December 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_191)

* [PingCentral 1.9 (October 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_19)

* [PingCentral 1.8.2 (December 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_182)

* [PingCentral 1.8.1 (December 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_181)

* [PingCentral 1.8 (June 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_18)

* [PingCentral 1.7 (March 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_17)

## 2020 release notes

* [PingCentral 1.6 (December 2020)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_16)

* [PingCentral 1.5 (September 2020)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_15)

* [PingCentral 1.4 (July 2020)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_14)

* [PingCentral 1.3 (March 2020)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_13)

## 2019 release notes

* [PingCentral 1.2 (November 2019)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_12)

* [PingCentral 1.01 (October 2019)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_101)

* [PingCentral 1.0 (August 2019)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_one_point_o)

---

---
title: Release Notes
description: The home page for PingCentral release notes.
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_home
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_home.html
revdate: November 4, 2025
section_ids:
  pingcentral-3-1-1-may-2026: PingCentral 3.1.1 (May 2026)
  pingfederate-extended-properties-fixed: PingFederate extended properties fixed
  pingcentral-3-1-april-2026: PingCentral 3.1 (April 2026)
  administrators-can-now-configure-signature-policies-for-saml-sp-connections: Administrators can now configure signature policies for SAML SP connections
  openjdk-version-requirements-if-using-fips-compliant-mode: OpenJDK version requirements if using FIPS-compliant mode
  security-vulnerability-fixed: Security vulnerability fixed
  apache-commons-compress-updated: Apache Commons Compress updated
  moment-js-updated: Moment.js updated
  option-to-download-saml-idp-metadata-issue-fixed: Option to download SAML IdP metadata issue fixed
  swagger-ui-library-updated: Swagger UI library updated
  swagger-json-fixed: Swagger.json fixed
  api-loading-issues-resolved: API loading issues resolved
  h2-database-updated: H2 database updated
  hibernate-library-updated: Hibernate library updated
  socket-appender-in-apache-log4j-updated: Socket Appender in Apache Log4j updated
  sso-issue-resolved: SSO issue resolved
  outdated-uri-issue-resolved: Outdated URI issue resolved
  pingcentral-3-0-1-march-2026: PingCentral 3.0.1 (March 2026)
  bc-fips-and-java-17-issue-resolved: BC FIPS and Java 17 issue resolved
  obfuscated-password-issue-resolved: Obfuscated password issue resolved
  template-issue-resolved: Template issue resolved
  sql-errors-resolved: SQL errors resolved
  pingaccess-application-creation-issue-resolved: PingAccess application creation issue resolved
  pingcentral-3-0-november-2025: PingCentral 3.0 (November 2025)
  pingfederate-extended-properties-are-now-available-in-pingcentral: PingFederate extended properties are now available in PingCentral
  entire-urls-now-visible: Entire URLs now visible
  opencsv-upgrade: Opencsv upgrade
  spring-security-upgrade: Spring Security upgrade
  java-runtime-environment-update: Java runtime environment update
  nimbus-jose-jwt-libraries-updated: Nimbus JOSE + JWT libraries updated
  safeguards-are-now-available-for-overwriting-pingfederate-entity-ids: Safeguards are now available for overwriting PingFederate entity IDs
  strict-transport-security-hsts-header-issue-resolved: Strict-Transport-Security (HSTS) header issue resolved
  cve-issues-fixed: CVE issues fixed
  pingcentral-now-prevents-users-from-creating-apps-with-the-same-name: PingCentral now prevents users from creating apps with the same name
  client-secret-size-increased: Client secret size increased
  pingcentral-2-3-april-2025: PingCentral 2.3 (April 2025)
  fips-compliant-mode-now-available: FIPS-compliant mode now available
  spring-security-upgrade-2: Spring Security upgrade
  d3-color-upgrade: d3-color upgrade
  promotion-approval-requests-enhanced: Promotion approval requests enhanced
  updated-scripts: Updated scripts
  jdk-21-support-added: JDK 21 support added
  pingcentral-2-2-december-2024: PingCentral 2.2 (December 2024)
  trusted-ognl-expression-usability-improvement: Trusted OGNL expression usability improvement
  signing-and-encryption-certificates-can-now-be-the-same: Signing and encryption certificates can now be the same
  spring-security-upgrade-3: Spring Security upgrade
  cve-issues-fixed-2: CVE issues fixed
  upgrade-issues-fixed: Upgrade issues fixed
  saml-application-deletion-issue-resolved: SAML application deletion issue resolved
  pingcentral-and-pingfederate-application-sync-issue-resolved: PingCentral and PingFederate application sync issue resolved
  pingcentral-2-1-june-2024: PingCentral 2.1 (June 2024)
  more-control-over-client-secrets: More control over client secrets
  mtls-is-now-supported: mTLS is now supported
  rocky-linux-is-now-supported: Rocky Linux is now supported
  new-email-parameter-added-to-all-user-accounts: New email parameter added to all user accounts
  performance-improvements: Performance improvements
  application-owners-limited-to-whom-they-can-assign-as-owners: Application owners limited to whom they can assign as owners
  certificates-management-usability-improvement: Certificates management usability improvement
  application-owners-list-is-now-easier-to-navigate: Application owners list is now easier to navigate
  change-template-button-fixed: Change Template button fixed
  json-editor-promotion-issues-resolved: JSON editor promotion issues resolved
  keystore-password-issues-resolved: Keystore password issues resolved
  assertion-encryption-certificate-issues-resolved: Assertion encryption certificate issues resolved
  pingcentral-2-0-2-april-2024: PingCentral 2.0.2 (April 2024)
  upgrade-processes-now-work-as-expected: Upgrade processes now work as expected
  expressions-can-now-be-added-or-updated-in-saml-applications: Expressions can now be added or updated in SAML applications
  saml-application-templates-can-now-be-updated: SAML application templates can now be updated
  database-errors-no-longer-occur-during-upgrade: Database errors no longer occur during upgrade
  pingcentral-2-0-1-january-2024: PingCentral 2.0.1 (January 2024)
  approval-window-now-displays-most-recently-promoted-version: Approval window now displays most recently promoted version
  updated-json-for-oidc-applications-now-displays-in-pingfederate-after-promotion: Updated JSON for OIDC applications now displays in PingFederate after promotion
  application-synchronization-now-works-as-expected-for-oidc-applications: Application synchronization now works as expected for OIDC applications
  pingcentral-2-0-december-2023: PingCentral 2.0 (December 2023)
  template-synchronization-now-available-for-saml-and-pingaccess-applications: Template synchronization now available for SAML and PingAccess applications
  application-owners-can-now-edit-application-json-themselves: Application owners can now edit application JSON themselves
  prevent-application-owners-from-deleting-applications: Prevent application owners from deleting applications
  hide-inactive-promotion-approvals: Hide inactive promotion approvals
  approval-expressions-drag-and-drop-enhancement: Approval expressions drag and drop enhancement
  multi-apc-connection-synchronization: Multi-APC connection synchronization
  configure-apc-mappings-for-oidc-applications-in-pingfederate: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier: Cannot update or revert templates created in 1.2 or earlier
  pingcentral-1-14-1-november-2023: PingCentral 1.14.1 (November 2023)
  forbidden-error-when-loading-api-documentation: Forbidden error when loading API documentation
  pingcentral-1-14-september-2023: PingCentral 1.14 (September 2023)
  disable-environments-when-down-for-maintenance-or-offline: Disable environments when down for maintenance or offline
  import-saml-connection-to-pingcentral-from-pingfederate-with-attributes-mapped-to-data-source: Import SAML Connection to PingCentral from PingFederate with attributes mapped to data source
  additional-synchronization-capabilities: Additional synchronization capabilities
  other-improvements: Other improvements
  h2-database-migration-when-the-installation-path-has-any-spaces: H2 database migration when the installation path has any spaces
  sso-inactivity-sign-off: SSO inactivity sign off
  multi-apc-connection-synchronization-2: Multi-APC connection synchronization
  configure-apc-mappings-for-oidc-applications-in-pingfederate-2: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies-2: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different-2: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start-2: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier-2: Cannot update or revert templates created in 1.2 or earlier
  pingcentral-1-13: PingCentral 1.13
  pingcentral-1-12-june-2023: PingCentral 1.12 (June 2023)
  approval-workflow: Approval workflow
  client-secret-management-enhancements: Client secret management enhancements
  multiple-slo-service-urls: Multiple SLO Service URLs
  jdk-17-support: JDK 17 support
  saml-metadata-export: SAML metadata export
  configure-apc-mappings-for-oidc-applications-in-pingfederate-3: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies-3: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different-3: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start-3: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier-3: Cannot update or revert templates created in 1.2 or earlier
  pingcentral-1-11-march-2023: PingCentral 1.11 (March 2023)
  updated-client-secret-generation-to-produce-client-secrets-compatible-with-pingfederate: Updated client secret generation to produce client secrets compatible with PingFederate
  multiple-acs-urls: Multiple ACS URLs
  set-application-name: Set application name
  deleting-an-application-in-pingcentral-also-deletes-it-in-other-environments: Deleting an application in PingCentral also deletes it in other environments
  configure-oauth-credentials-for-use-instead-of-username-and-password-to-connect-to-pingfederate-or-pingaccess: Configure OAuth credentials for use instead of username and password to connect to PingFederate or PingAccess
  upgraded-from-v1-h2-database-to-v2: Upgraded from v1 H2 database to v2
  configure-apc-mappings-for-oidc-applications-in-pingfederate-4: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies-4: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different-4: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start-4: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier-4: Cannot update or revert templates created in 1.2 or earlier
  cannot-migrate-the-h2-database-if-the-installation-path-has-any-spaces: Cannot migrate the H2 database if the installation path has any spaces
  pingcentral-1-10-june-2022: PingCentral 1.10 (June 2022)
  update-oauth-and-oidc-template-grant-types-scopes-and-policy-contracts-and-revert-to-previous-versions: Update OAuth and OIDC template grant types, scopes, and policy contracts and revert to previous versions
  update-applications-with-the-latest-template-version-available: Update applications with the latest template version available
  use-sso-to-access-pingfederate-and-pingaccess-from-pingcentral: Use SSO to access PingFederate and PingAccess from PingCentral
  account-lockout-mechanisms-added-to-mitigate-password-guessing: Account lockout mechanisms added to mitigate password guessing
  cannot-update-or-revert-templates-created-in-version-1-2-or-earlier: Cannot update or revert templates created in version 1.2 or earlier
  resolved-a-potential-security-vulnerability: Resolved a potential security vulnerability
  configure-apc-mappings-for-oidc-applications-in-pingfederate-5: Configure APC mappings for OIDC applications in PingFederate
  sp-certificates-and-assertion-encryption-certificates-must-be-different-5: SP certificates and assertion encryption certificates must be different
  promoting-applications-with-authentication-challenge-policies-5: Promoting applications with authentication challenge policies
  update-truststore-path-if-pingcentral-fails-to-start-5: Update truststore path if PingCentral fails to start
  adding-saml-applications-through-the-api: Adding SAML applications through the API
  managing-environments-through-the-api: Managing environments through the API
  previous-releases: Previous Releases
  2022-release-notes: 2022 release notes
  2021-release-notes: 2021 release notes
  2020-release-notes: 2020 release notes
  2019-release-notes: 2019 release notes
---

# Release Notes

These release notes summarize the changes in current and previous PingCentral product updates.

Subscribe to get automatic updates: [icon: rss-square, set=fa][PingCentral Release Notes RSS feed](pingcentral_relnotes_home.xml)

## PingCentral 3.1.1 (May 2026)

### PingFederate extended properties fixed

Fixed PASS-7205

Starting with PingCentral version 3.0, PingFederate extended properties are displayed in PingCentral templates. Administrators can set these values when they configure templates, and the applications created from these templates inherit them. Application owners can also update these values, unless the extended property is designated as read-only.

We've fixed the issues users experienced when promoting applications created from templates that were configured prior to version 3.0. Because PingCentral applications and templates did not include extended properties in earlier versions, empty values could overwrite the existing values in the PingFederate client or connection.

PingFederate extended property values are no longer overwritten, and the extended property values are visible in PingCentral templates and applications when you refresh the page.

## PingCentral 3.1 (April 2026)

### Administrators can now configure signature policies for SAML SP connections

New PASS-7155

Administrators can now configure signature policies for SP connections when they create templates and applications, and promote applications to PingCentral environments.

Previously, PingFederate administrators had to configure the signature policies after the applications were promoted to PingFederate, which interrupted their workflow and caused unnecessary delays in the process.

Note that signature policy configurations are only visible if the corresponding profiles and artifact binding are enabled in the underlying PingFederate SP connection. To learn more, refer to step 8 in [Adding SAML application templates](../pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html#_adding_saml_application_templates).

### OpenJDK version requirements if using FIPS-compliant mode

Info PASS-7204

If the FIPS-compliant mode is enabled and OpenJDK 21 is being used, OpenJDK version 21.0.10 or higher is required.

### Security vulnerability fixed

Fixed PASS-1323

We've fixed the client-side security vulnerability in DOM-based XSS in redirect URI definitions.

### Apache Commons Compress updated

Fixed PASS-5852

The Apache Commons Compress has been updated to version 1.26, which resolved the security vulnerability that affected versions 1.0 to 1.21. You can find more information about the [CVE-2021-36090 vulnerability](https://nvd.nist.gov/vuln/detail/cve-2021-36090) on the National Vulnerability Database site.

### Moment.js updated

Fixed PASS-6410

Moment.js has been updated to version 2.29.4, which resolved the path traversal vulnerability that affected versions 1.0.1 to 2.29.1. You can find more information about the [CVE-2022-24785 vulnerability](https://nvd.nist.gov/vuln/detail/cve-2022-24785) on the National Vulnerability Database site.

### Option to download SAML IdP metadata issue fixed

Fixed PASS-7017

We've fixed the **Promotion Details** page so that it now displays the option to download the SAML IdP metadata if the application was promoted directly from the JSON file.

### Swagger UI library updated

Fixed PASS-7021

The Swagger UI library has been updated from version 2.9.2 to 3.23.11 to prevent future false-positive scan alerts. You can find more information about the [CVE-2019-17495 vulnerability](https://nvd.nist.gov/vuln/detail/cve-2019-17495) on the National Vulnerability Database site.

### Swagger.json fixed

Fixed PASS-7132

We've fixed the swagger.json endpoint, and it now returns information about the Admin API as expected.

### API loading issues resolved

Fixed PASS-7163

We've fixed the issue where users encountered a continuous loading screen when they tried to access the API. The API now works as expected and returns a response.

### H2 database updated

Fixed PASS-7070

The H2 database has been updated to version 2.2.220, which resolved the security vulnerability that affected version 2.1.210. You can find more information about the [CVE-2022-45868 vulnerability](https://nvd.nist.gov/vuln/detail/cve-2022-45868) on the National Vulnerability Database site.

### Hibernate library updated

Fixed PASS-7172

The `hibernate-ehcache` library is no longer used, which resolved the security vulnerability. You can find more information about the [CVE-2026-0603 vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2026-0603) on the National Vulnerability Database site.

### Socket Appender in Apache Log4j updated

Fixed PASS-7174

The Socket Appender in Apache Log4j has been updated to version 2.25.3, which resolved the security vulnerability that affected versions 2.0-beta9 through 2.25.2. You can find more information about the [CVE-2025-68161 vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-68161) on the National Vulnerability Database site.

### SSO issue resolved

Fixed PASS-7176

We've fixed an issue with SSO, and users are now redirected to the PingFederate sign-on page instead of the PingCentral home page when they sign on.

### Outdated URI issue resolved

Fixed PASS-7187

We've fixed an issue where redirect URIs were still displayed in OAuth or OIDC applications after the environment referenced in the URI was deleted.

## PingCentral 3.0.1 (March 2026)

### BC FIPS and Java 17 issue resolved

Fixed PASS-7151

Previously, if you were using Java 17 and BC FIPS was enabled, PingCentral failed to start. This issue has been resolved.

### Obfuscated password issue resolved

Fixed PASS-7153

Previously, the `obfuscate.sh <password>` command line utility (CLI) did not work out-of-the-box unless you modified the script. Once modified, the script was able to generate an obfuscated password, but if you tried to use this password to connect to an external database, PingCentral would fail to start. The CLI has been fixed and now works as expected.

### Template issue resolved

Fixed PASS-7156

Previously, after upgrading from version 2.3 to 3.0, administrators using a PostgreSQL database received a server error message when they tried to create a new template. This issue has been resolved.

### SQL errors resolved

Fixed PASS-7164

Previously, when users attempted to promote new applications and IDs were created with MySQL 8, SQL errors occurred. This issue has been resolved.

### PingAccess application creation issue resolved

Fixed PASS-7169

Previously, users could not create PingAccess applications if the `ApplicationResources` property was set to `null`. This issue has been resolved.

## PingCentral 3.0 (November 2025)

### PingFederate extended properties are now available in PingCentral

New PASS-7124

PingFederate extended properties are single or multi-value fields that are used to store additional information about connections or OAuth clients. These properties are now displayed in PingCentral templates. Administrators can set these property values when they configure templates, and the applications created from these templates inherit those values. Application owners can also update these values unless the extended property is designated as read-only.

### Entire URLs now visible

Improved PASS-7098

Several UI modifications have been made that allow you to see entire URLs within text fields. This new functionality makes it easier for users to verify URLs, and helps prevent copy and paste errors.

### Opencsv upgrade

Improved PASS-7099

Opencsv has been upgraded from version 5.8 to 5.11.2 to prevent future false-positive scan alerts. You can find more information about the [CVE-2025-48734 vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-48734) on the National Vulnerability Database site.

### Spring Security upgrade

Improved PASS-7100

Spring Security has been upgraded from version 5.3.39 to 6.2.8 to prevent future false-positive scan alerts. You can find more information in [CVE-2024-22243: Spring Framework URL Parsing with Host Validation](https://spring.io/security/cve-2024-22243) in the Spring documentation.

### Java runtime environment update

Improved PASS-7106

You can now use either Java 17 or Java 21 as the PingCentral runtime environment. Java 11 is no longer supported.

### Nimbus JOSE + JWT libraries updated

Improved PASS-7134

The Nimbus JOSE + JWT libraries have been upgraded. You can find more information about the [CVE-2025-53864 vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2025-53864) on the National Vulnerability Database site.

### Safeguards are now available for overwriting PingFederate entity IDs

Fixed PASS-7105

Previously, it was possible to overwrite a connection in PingFederate if you created a PingCentral application with an entity ID that already exists in PingFederate. This issue has been resolved, and it's no longer possible to create new applications using an entity ID that is already used by a PingFederate connection.

### Strict-Transport-Security (HSTS) header issue resolved

Fixed PASS-7097

Previously, if OIDC single sign-on (SSO) was enabled, PingCentral stopped sending the HSTS header and administrators couldn't sign on. This issue has been resolved and SSO now works as expected.

### CVE issues fixed

Fixed PASS-7101

A number of third-party libraries have been updated to address Common Vulnerabilities and Exposures (CVEs) reported in these libraries. These CVEs weren't exploitable, but they were updated to avoid unnecessary concerns.

### PingCentral now prevents users from creating apps with the same name

Fixed PASS-7133

PingCentral now enforces consistent validation to ensure that new applications cannot have the same name as existing applications.

### Client secret size increased

Fixed PASS-7135

Previously, when users attempted to configure a PingCentral environment connection to PingFederate and PingAccess using PingOne OAuth app credentials, the database column wasn't large enough to store the client secret and an error message displayed. The column limit was increased, which resolved the issue.

## PingCentral 2.3 (April 2025)

### FIPS-compliant mode now available

New PASS-7036

Administrators can now enable PingCentral to run in FIPS-compliant mode, which guarantees that all cryptographic algorithms and protocols meet the U.S. federal standard for security compliance.

To enable this option, access the `<PingCentral_install>/conf/application.properties` file and set the `pingcentral.fips.enabled` property value to `true`. Learn more in [Configuring PingCentral to run in FIPS-compliant mode](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_fips_mode.html).

PingCentral is currently running FIPS 140-3. Learn more about this version in [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final).

### Spring Security upgrade

Improved PASS-7022

Spring Security has been upgraded from version 5.3.31 to 5.3.39 to prevent future false-positive scan alerts. You can find more information in [CVE-2024-38816: Path traversal vulnerability in functional web frameworks](https://spring.io/security/cve-2024-38816^) in the Spring documentation.

### d3-color upgrade

Improved PASS-7031

The d3-color package has been upgraded from version 1.4.1 to 3.1.0, where the security vulnerability was fixed.

### Promotion approval requests enhanced

Improved PASS-7033

Those who approve promotions can now determine if a promotion approval request is for a new or existing application by viewing the newly added detail on the **Promotion Approvals** page. **Last Promoted** or **Last Updated** now displays next to the date and timestamp that indicates when the application was last promoted or updated.

### Updated scripts

Improved PASS-7037

All PingCentral scripts have been updated to be DevOps-friendly.

### JDK 21 support added

New PASS-7038

Support was added for Java Development Kit (JDK) 21 using language level 11.

## PingCentral 2.2 (December 2024)

### Trusted OGNL expression usability improvement

Improved PASS-7028

Previously, trusted OGNL expressions could only be assigned to applications one at a time. Now, a **Select All** checkbox is available to select all applications and assign the selected trusted OGNL expression to them.

### Signing and encryption certificates can now be the same

Improved PASS-7029

Previously, PingCentral did not allow the signing and encryption certificate the same, which is allowed in PingFederate. When application owners tried to promote and upload the same certificate and use it for both the signing and encryption certificate, users received validation errors. Now, the same certificates can be used in PingCentral.

### Spring Security upgrade

Improved PASS-7019

Spring Security has been upgraded from version 5.7.11 to prevent future false-positive scan alerts. Learn more about this upgrade in [CVE-2024-22257: Possible Broken Access Control in Spring Security With Direct Use of AuthenticatedVoter](https://spring.io/security/cve-2024-22257) in the Spring documentation.

### CVE issues fixed

Fixed PASS-7020

A number of third-party libraries have been updated to address Common Vulnerabilities and Exposures (CVEs) reported in these libraries. These CVEs were not exploitable, but they were updated to avoid unnecessary concerns.

### Upgrade issues fixed

Fixed PASS-7023

Previously, when upgrading from PingCentral 2.0.2 to 2.1.0, users received a warning message regarding their APIs. This issue has been resolved, and this message no longer displays when the upgrade is performed.

### SAML application deletion issue resolved

Fixed PASS-7026

Previously, when users tried to delete SAML applications, either through the PingCentral UI or API, and they selected the **Delete from PingFederate in all environments** option, the application was not deleted in PingFederate. This issue has been resolved and now works as expected.

### PingCentral and PingFederate application sync issue resolved

Fixed PASS-7027

Previously, when syncing a PingCentral application with a server-side PingFederate application, data within the **advancedEditPromotionJson** field was being deleted. This issue has been resolved, and the data within that field is now preserved.

## PingCentral 2.1 (June 2024)

### More control over client secrets

New PASS-6911

Application owners now have more control over which client secrets are used when promoting OAuth and OIDC applications from PingCentral to PingFederate. If the application is configured to use a client secret for authentication, and the environment to which the application is being promoted requires that a random secret be used, users can choose to either generate a new client secret or retain the existing client secret. See [Promoting OAuth and OIDC applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html#oauth) for details.

### mTLS is now supported

New PASS-6915

Mutual TLS (mTLS) can now be used for admin API authentication from PingCentral to PingFederate. To set up this connection, access the new **Client TLS Key Pair** page, import the key pair that you want to use for authentication, and configure the environment to use the client certificate you specify. The **TLS Key Pair** page has also been renamed to **Server TLS Key Pair** to clearly differentiate between them. See [Configuring MTLS](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_config_mtls.html) for details.

### Rocky Linux is now supported

New PASS-6918

Rocky Linux version 9.3 and later is now a supported enterprise operating system.

### New email parameter added to all user accounts

New PASS-6967

The email parameter has been added to all PingCentral user accounts, which will let you extract users' email addresses and notify them about important events, such as upgrades, and maintenance windows. The **Email Address** field now displays on the **Add** and **Edit User** pages, an email property has been added to the API, and for SSO configurations, PingCentral will derive the user's email from the email claim defined by the email scope.

### Performance improvements

Improved PASS-6904 and PASS-6910

If you have many different applications in many different environments, or if you have many groups using SSO to access PingCentral, you will notice that performance has been greatly improved with this release. Now, when you filter your applications, you will only see managed applications (created from or promoted to PingCentral environments) by default, which improves page loading speeds. The application owner search functionality has also been improved, which makes it faster and easier to configure owners for applications.

### Application owners limited to whom they can assign as owners

Improved PASS-6913

Previously, when application owners used SSO to sign on to PingCentral and group memberships were also supplied, application owners could select any group as an owner of their application, which gave all group members the ability to manage it. Now, application owners can only select a group as an owner if the application owner is a member of the group.

### Certificates management usability improvement

Improved PASS-6917

When promoting SAML applications, the names of the signing certificates available now include the valid date range, which makes it easier to discern between certificates.

### Application owners list is now easier to navigate

Fixed PASS-2114

Previously, all application owners were listed on the application **Summary** tab, regardless of the number of owners. If an application had a large number of owners, the list would be long and difficult to read. Now, if the list is large, **Show More** and **Show Less** buttons are available to help you navigate the list.

### Change Template button fixed

Fixed PASS-6941

Previously, when importing metadata for a SAML application, the **Change Template** button would disappear. This issue has been fixed, and the **Change Template** button continually displays as expected.

### JSON editor promotion issues resolved

Fixed PASS-6966

Previously, under certain circumstances, server errors were encountered when JSON-based promotions occurred. This issue has been resolved.

### Keystore password issues resolved

Fixed PASS-6970

Previously, when configuring an environment and uploading a signing certificate, if an existing keystore file (\*.p12) was selected, the matching password provided could be too long for PingCentral to accept. This password limit has been increased.

### Assertion encryption certificate issues resolved

Fixed PASS-6985

Previously, if an application was configured with an assertion encryption certificate, the certificate would disappear from the **Promote to Environment** modal when the application was being promoted, and users had to upload the certificate again. This issue has been resolved.

## PingCentral 2.0.2 (April 2024)

### Upgrade processes now work as expected

Fixed PASS-6905

Previously, if PingCentral had at least one (service provider) SP connection or one PingAccess template, upgrades from version 1.14 to 2.0 would fail. This issue has been resolved and upgrades now work as expected.

### Expressions can now be added or updated in SAML applications

Fixed PASS-6906

Previously, if applications were created from SAML templates that contained at least 1 OGNL expression, the expressions could not be updated, nor could new expressions be added for attribute mapping. This issue has been resolved, and expressions can now be added and updated as needed.

### SAML application templates can now be updated

Fixed PASS-6907

Previously, when administrators tried to change the templates associated with SAML applications, the change would not be saved. This issue has been resolved, and SAML applications can now be updated with new templates.

### Database errors no longer occur during upgrade

Fixed PASS-6940

Previously, if PingCentral had a SAML template with expressions or PingAccess templates, database errors would occur when upgrading from version 1.14 to 2.0. The issue has been resolved and upgrade processes now work as expected.

## PingCentral 2.0.1 (January 2024)

### Approval window now displays most recently promoted version

Fixed PASS-6865

Previously, when administrators reviewed application promotion requests and compared the submitted JSON to the most recently promoted version, the original version was displayed instead of the most recently promoted version. This issue has been resolved, and the most recently promoted version now displays in the approval window.

### Updated JSON for OIDC applications now displays in PingFederate after promotion

Fixed PASS-6900

Previously, if application owners updated the underlying application JSON in their OIDC applications, and administrator approval was required to promote them, the updated JSON was not reflected in PingFederate. This issue has been resolved and the updated JSON now displays in PingFederate as expected.

### Application synchronization now works as expected for OIDC applications

Fixed PASS-6901

Previously, when OIDC applications were synchronized to the most up-to-date configurations available, they were saved as OAuth applications. This issue has been resolved, and the synchronization process now works as expected.

## PingCentral 2.0 (December 2023)

New features and improvements in PingCentral 2.0.

### Template synchronization now available for SAML and PingAccess applications

New PASS-6730

Administrators can now synchronize OAuth, OIDC, SAML, and PingAccess templates to ensure that their templates are based on the most up-to-date configurations available. Applications based on out-of-date templates have **Outdated Template** icons displayed next to them, which inform application owners that newer versions of the templates are available.

Administrators can also now revert SAML SP connections and PingAccess application templates to previous versions. You can find details on the **Reverting templates to previous versions** tab on the [Managing templates](../pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html).

Note that when you upgrade to PingCentral 2.0, SAML and PingAccess application templates will have base revisions created for them. OAuth and OIDC templates created prior to version 2.0 cannot be synced with the most recent configurations available. Recreate the template in version 2.0 to use the sync feature going forward.

### Application owners can now edit application JSON themselves

New PASS-6670

To accommodate a wide variety of promotion needs, application owners can now edit the application JSON for their applications when they promote them.

Note that providing application owners with this ability can be risky, so it's highly recommended that approvals are enabled for the environment. Administrators can review the submitted application JSON and compare it to the original application JSON before approving the promotion request.

Also note that:

* This functionality is not yet available for PingAccess applications.

* Applications cannot be reverted to a promotion that uses JSON editing.

* Be aware that the JSON review window compares against the original application JSON and not the most recently promoted JSON.

### Prevent application owners from deleting applications

New PASS-6731

To prevent application owners from accidentally deleting applications from PingFederate (and PingAccess, when applicable) environments, you can enable a new option that allows only administrators to delete applications from the environment.

### Hide inactive promotion approvals

Improved PASS-6733

To help manage promotion approvals, both administrators and application owners can now hide promotion approvals that are in a **canceled**, **promoted**, or **rejected** status that display on the **Promotion Approvals** page. The **Visible** filter is enabled by default.

### Approval expressions drag and drop enhancement

Improved PASS-6732

Administrators can add multiple approval expressions for an environment, which are evaluated sequentially from top to bottom in an IF/ELSE chain. Now, administrators can change the order in which these expressions display in the list by dragging and dropping them into different locations within the list instead of copying and pasting them between fields.

### Multi-APC connection synchronization

Issue PASS-6705

Previously, PingCentral was unable to handle a service provider (SP) connection with multiple Authentication Policy Contracts (APC) mapped within it. The PingCentral 1.14 release enables users to select from multiple mapped contracts when adding an application as a managed application or a template.

However, due to a known synchronization limitation, if you update an existing single APC SP connection already managed by PingCentral to include a second APC and subsequently synchronize the application, you won't find an option to specify your preferred APC.

To simplify your workflow and mitigate potential challenges, we recommend refraining from using synchronization to modify multi-APC connections. Instead, consider creating a new SP connection that aligns with your desired APC configuration. This approach grants you control over APC selection, ensuring a smoother and more efficient process.

### Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

### Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

### SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

```
Environment'staging':  {pingfed}. This certificate either has the same ID or the same content as the certificate with index 0.
```

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

### Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

### Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

## PingCentral 1.14.1 (November 2023)

Enhancements and resolved issues in PingCentral 1.14.1.

### Forbidden error when loading API documentation

Fixed PASS-6820

We fixed an error that prevented API documentation from loading when using OIDC single sign-on (SSO) with PingCentral.

## PingCentral 1.14 (September 2023)

New features and improvements in PingCentral 1.14.

### Disable environments when down for maintenance or offline

New PASS-6666 and PASS-6683

PingCentral administrators can now disable referenced PingFederate environments for any reason, such as PingFederate being unavailable due to maintenance tasks. Additionally, we added a new environment status bar that indicates if an environment is offline. In such cases, application owners will receive a notification indicating that the environment is disabled or offline rather than encountering a UI error. For more information, see step 1 of the Updating environments tab in [Managing environments](../pingcentral_for_iam_administrators/pingcentral_mng_environments/pingcentral_mng_environments.html).

### Import SAML Connection to PingCentral from PingFederate with attributes mapped to data source

New PASS-6667

All attributes defined in a SAML SP connection are now integrated into the PingCentral application. This enhancement eliminates a limitation and is expected to enhance usability significantly. For more information, see step 3 in [Using SAML 2.0 templates](../pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html#saml_template).

### Additional synchronization capabilities

New PASS-6696

We added the ability to effortlessly initiate an application synchronization in PingCentral. Now, when you make external modifications to an application configuration, you can seamlessly update the application information within PingCentral. This removes the need to manually update application information and introduces a more streamlined and efficient process. For more information, see step 2 in [Updating applications](../pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html#pingcentral_iam_updating_apps).

### Other improvements

New

* We also updated the following bundled components and third-party dependencies:

  * Apache Commons Text 1.10

### H2 database migration when the installation path has any spaces

Fixed PASS-6591

We resolved an issue where H2 database migration fails during an upgrade if there are spaces in the installation path for the existing or new instance.

### SSO inactivity sign off

Fixed PASS-6690

We fixed an issue where utilizing single sign-on (SSO) to access the PingCentral console incorrectly triggered a timeout based on an ID token's lifetime.

### Multi-APC connection synchronization

Issue PASS-6705

Previously, PingCentral was unable to handle a service provider (SP) connection with multiple Authentication Policy Contracts (APC) mapped within it. The PingCentral 1.14 release enables users to select from multiple mapped contracts when adding an application as a managed application or a template.

However, due to a known synchronization limitation, if you update an existing single APC SP connection already managed by PingCentral to include a second APC and subsequently synchronize the application, you won't find an option to specify your preferred APC.

To simplify your workflow and mitigate potential challenges, we recommend refraining from using synchronization to modify multi-APC connections. Instead, consider creating a new SP connection that aligns with your desired APC configuration. This approach grants you control over APC selection, ensuring a smoother and more efficient process.

### Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

### Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

### SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

```
Environment'staging':  {pingfed}. This certificate either has the same ID or the same content as the certificate with index 0.
```

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

### Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

### Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

## PingCentral 1.13

PingCentral 1.13 was skipped.

## PingCentral 1.12 (June 2023)

New features and improvements in PingCentral 1.12.

### Approval workflow

New PASS-6479

Previously, PingCentral did not allow an administrator to require approval for a non-administrator to promote an application to an environment. As of now, administrators can use Spring Expression Language (SpEL) based rules to trigger an approval requirement if an expression is or isn't met. Administrators will find a bell icon indicating active approval requests, and developers are informed when their requests are approved. For more information, see xref:pingcentral\_for\_iam\_administrators:

Learn more in [Managing approvals (administrators)](../pingcentral_for_iam_administrators/pingcentral_mng_approvals/pingcentral_manage_approvals.html).

### Client secret management enhancements

Improved PASS-6500

Administrators can now enforce a strong client secret for applications by requiring that PingCentral generate the client secret. With this feature enabled, when developers promote an application, they won't be able to create a client secret manually. This avoids the usage of weak client secrets. For more information, see [Managing environments](../pingcentral_for_iam_administrators/pingcentral_mng_environments/pingcentral_mng_environments.html).

### Multiple SLO Service URLs

New PASS-6609

When promoting SAML applications, developers can adjust and configure single logout (SLO) URLs. This adds flexibility and removes the need to manage multiple SAML applications only because different SLO URLs are required. For more information, see [Promoting SAML applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html#saml).

### JDK 17 support

New

We added support for Java Development Kit (JDK) 17.

### SAML metadata export

Fixed PASS-5630

To set up a service provider (SP) connection, PingCentral now accepts SAML metadata files exported from other SP connections. These files are used to extract the following information: entity IDs, ACS URLs, SLO service URLs, certificates, and attributes.

### Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

### Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

### SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

```
Environment'staging':  {pingfed}. This certificate either has the same ID or the same content as the certificate with index 0.
```

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

### Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

### Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

## PingCentral 1.11 (March 2023)

For the best possible experience, review these notes before using PingCentral 1.11.

### Updated client secret generation to produce client secrets compatible with PingFederate

New

When creating a new client, PingCentral now generates OAuth client secrets compatible with PingFederate. For more information, see [Promoting OAuth and OIDC applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html#oauth).

### Multiple ACS URLs

New

You can now configure multiple Assertion Consumer Service (ACS) URLs during SAML application creation. This new feature simplifies application development since the same application can use different URLs simultaneously. For more information, see [Using SAML 2.0 templates](../pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html#saml_template).

### Set application name

New

When promoting an application between environments, you can now configure an application name for OAuth and OpenID Connect (OIDC) clients, SAML connections, and PingAccess applications. For more information, see [Promoting applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html).

### Deleting an application in PingCentral also deletes it in other environments

Improved

You can now choose to delete applications from PingFederate or PingAccess in addition to PingCentral. This feature is flexible because you can select which environments to delete the application from. For more information, see [Managing applications](../pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html).

### Configure OAuth credentials for use instead of username and password to connect to PingFederate or PingAccess

Improved

Instead of using administrator credentials for basic authentication, you can now configure PingCentral to use OAuth client credentials to connect to PingFederate or PingAccess. will request an `access_token` to use whenever it connects to PingFederate or PingAccess. For more information, see [Configuring PingFederate and PingAccess for SSO](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pf_pa_sso.html).

### Upgraded from v1 H2 database to v2

Security

Along with other dependencies (libraries), we've upgraded the H2 database from v1 to v2. For more information, see [Upgrading PingCentral](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_upgrading/pingcentral_upgrading_pc.html).

### Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

### Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

### SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

`Environment'staging': PingFederate. This certificate either has the same ID or the same content as the certificate with index 0.`

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

### Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

### Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

### Cannot migrate the H2 database if the installation path has any spaces

Issue PASS-6591

If the installation path has any spaces in the existing or new instance, the H2 database is not migrated during upgrade. Upon removing the spaces from the file path, the migration is successful.

## PingCentral 1.10 (June 2022)

For the best possible experience, review these notes before using PingCentral 1.10.

### Update OAuth and OIDC template grant types, scopes, and policy contracts and revert to previous versions

New PASS-2017

If you are an administrator, you can now update the grant types, scopes, and policy contracts in OAuth and OpenID Connect (OIDC) templates to further customize them to meet your needs.The history of these templates is also available to review and compare with previous versions. You can see which administrator modified the template configuration or policy contract, when it was modified, and details regarding these modifications. You can also revert templates to previous versions, if necessary. See [Managing templates](../pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html) for details.

### Update applications with the latest template version available

New PASS-6007

If an application is based on an outdated template, an **Outdated Template** icon now displays next to its name in the applications list. Edit the template and click the **Update Template** button. See [Updating applications](../pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html#pingcentral_iam_updating_apps) for details.

### Use SSO to access PingFederate and PingAccess from PingCentral

New PASS-5202 and PASS-6018

You can now use SSO to access PingFederate and PingAccess from PingCentral. For details, see [Configuring PingFederate and PingAccess for SSO](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pf_pa_sso.html).

### Account lockout mechanisms added to mitigate password guessing

Improved PASS-6388

Account lockout mechanisms that prevent users from accessing the application or API after a specified number of failed sign-on attempts were added to this release. Specify the number of failed attempts that are allowed before users are locked out and the lockout period in the `application.yaml` file.

### Cannot update or revert templates created in version 1.2 or earlier

Issue PASS-6466

Templates created in version 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

### Resolved a potential security vulnerability

Security PASS-6387 and PASS-6378

Resolved a potential security vulnerability that is described in security bulletin [SECBL022](https://support.pingidentity.com/s/article/SECBL022-PingCentral-Overly-Permissive-Actuator) (requires sign-on).

### Configure APC mappings for OIDC applications in PingFederate

Issue PASS-6316 PingFederate

PingCentralpromotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.To resolve these issues, configure the APC mappings within PingFederate.

### SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingFederate

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:`Environment'staging': PingFederate. This certificate either has the same ID or the same content as the certificate with index 0.`To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

### Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral, but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

### Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, or 1.10, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

### Adding SAML applications through the API

Issue PASS-5009

If you attempt to add a SAML application to PingCentral from an existing application through the API, and the connection JSON contains identity attribute names and placeholders, you receive an error message advising you to nullify the **Names** field. However, even if you nullify this field, you still receive an error message because the JSON contains placeholders. Remove these placeholders before you proceed.

### Managing environments through the API

Issue PASS-5001 and PASS-5002

When creating, updating, or validating an environment through the API, you receive a server error message if the environment **Name** or **Password** fields are null or missing. API requests cannot be processed without this information, so ensure that these fields contain valid values.You will also receive a misleading error message if the **PingAccess Password** field is null. Rather than informing you that the information in this field is invalid, it informs you that you cannot connect to the PingFederateadministrative console, which is misleading.Requests to connect PingAccess to a PingCentral environment cannot be processed without this information, so ensure that this field contains a valid value.

## Previous Releases

Release notes for previous releases are available here.

### 2022 release notes

* [PingCentral 1.10 (June 2022)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_June2022)

* [PingCentral 1.9.3 (February 2022)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_193)

### 2021 release notes

* [PingCentral 1.9.2 (December 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_192)

* [PingCentral 1.9.1 (December 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_191)

* [PingCentral 1.9 (October 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_19)

* [PingCentral 1.8.2 (December 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_182)

* [PingCentral 1.8.1 (December 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_181)

* [PingCentral 1.8 (June 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_18)

* [PingCentral 1.7 (March 2021)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_17)

### 2020 release notes

* [PingCentral 1.6 (December 2020)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_16)

* [PingCentral 1.5 (September 2020)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_15)

* [PingCentral 1.4 (July 2020)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_14)

* [PingCentral 1.3 (March 2020)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_13)

### 2019 release notes

* [PingCentral 1.2 (November 2019)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_12)

* [PingCentral 1.01 (October 2019)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_101)

* [PingCentral 1.0 (August 2019)](https://docs.pingidentity.com/csh?Product=pingcentral\&context=pingcentral_relnotes_one_point_o)

---

---
title: PingCentral 1.10 (June 2022)
description: PingCentral release notes, June 2022
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_june2022
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_june2022.html
revdate: August 3, 2023
section_ids:
  update-oauth-and-oidc-template-grant-types-scopes-and-policy-contracts-and-revert-to-previous-versions: Update OAuth and OIDC template grant types, scopes, and policy contracts and revert to previous versions
  update-applications-with-the-latest-template-version-available: Update applications with the latest template version available
  use-sso-to-access-pingfederate-and-pingaccess-from-pingcentral: Use SSO to access PingFederate and PingAccess from PingCentral
  account-lockout-mechanisms-added-to-mitigate-password-guessing: Account lockout mechanisms added to mitigate password guessing
  cannot-update-or-revert-templates-created-in-version-1-2-or-earlier: Cannot update or revert templates created in version 1.2 or earlier
  resolved-a-potential-security-vulnerability: Resolved a potential security vulnerability
  configure-apc-mappings-for-oidc-applications-in-pingfederate: Configure APC mappings for OIDC applications in PingFederate
  sp-certificates-and-assertion-encryption-certificates-must-be-different: SP certificates and assertion encryption certificates must be different
  promoting-applications-with-authentication-challenge-policies: Promoting applications with authentication challenge policies
  update-truststore-path-if-pingcentral-fails-to-start: Update truststore path if PingCentral fails to start
  adding-saml-applications-through-the-api: Adding SAML applications through the API
  managing-environments-through-the-api: Managing environments through the API
---

# PingCentral 1.10 (June 2022)

For the best possible experience, review these notes before using PingCentral 1.10.

## Update OAuth and OIDC template grant types, scopes, and policy contracts and revert to previous versions

New PASS-2017

If you are an administrator, you can now update the grant types, scopes, and policy contracts in OAuth and OpenID Connect (OIDC) templates to further customize them to meet your needs.The history of these templates is also available to review and compare with previous versions. You can see which administrator modified the template configuration or policy contract, when it was modified, and details regarding these modifications. You can also revert templates to previous versions, if necessary. See [Managing templates](../pingcentral_for_iam_administrators/pingcentral_mng_templates/pingcentral_mng_templates.html) for details.

## Update applications with the latest template version available

New PASS-6007

If an application is based on an outdated template, an **Outdated Template** icon now displays next to its name in the applications list. Edit the template and click the **Update Template** button. See [Updating applications](../pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html#pingcentral_iam_updating_apps) for details.

## Use SSO to access PingFederate and PingAccess from PingCentral

New PASS-5202 and PASS-6018

You can now use SSO to access PingFederate and PingAccess from PingCentral. For details, see [Configuring PingFederate and PingAccess for SSO](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pf_pa_sso.html).

## Account lockout mechanisms added to mitigate password guessing

Improved PASS-6388

Account lockout mechanisms that prevent users from accessing the application or API after a specified number of failed sign-on attempts were added to this release. Specify the number of failed attempts that are allowed before users are locked out and the lockout period in the `application.yaml` file.

## Cannot update or revert templates created in version 1.2 or earlier

Issue PASS-6466

Templates created in version 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

## Resolved a potential security vulnerability

Security PASS-6387 and PASS-6378

Resolved a potential security vulnerability that is described in security bulletin [SECBL022](https://support.pingidentity.com/s/article/SECBL022-PingCentral-Overly-Permissive-Actuator) (requires sign-on).

## Configure APC mappings for OIDC applications in PingFederate

Issue PASS-6316 PingFederate

PingCentralpromotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.To resolve these issues, configure the APC mappings within PingFederate.

## SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingFederate

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:`Environment'staging': PingFederate. This certificate either has the same ID or the same content as the certificate with index 0.`To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

## Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral, but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

## Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, or 1.10, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

## Adding SAML applications through the API

Issue PASS-5009

If you attempt to add a SAML application to PingCentral from an existing application through the API, and the connection JSON contains identity attribute names and placeholders, you receive an error message advising you to nullify the **Names** field. However, even if you nullify this field, you still receive an error message because the JSON contains placeholders. Remove these placeholders before you proceed.

## Managing environments through the API

Issue PASS-5001 and PASS-5002

When creating, updating, or validating an environment through the API, you receive a server error message if the environment **Name** or **Password** fields are null or missing. API requests cannot be processed without this information, so ensure that these fields contain valid values.You will also receive a misleading error message if the **PingAccess Password** field is null. Rather than informing you that the information in this field is invalid, it informs you that you cannot connect to the PingFederateadministrative console, which is misleading.Requests to connect PingAccess to a PingCentral environment cannot be processed without this information, so ensure that this field contains a valid value.

---

---
title: PingCentral 1.11 (March 2023)
description: PingCentral release notes, March 2023
component: pingcentral
version: 3.1.1
page_id: pingcentral:release_notes:pingcentral_relnotes_march2023
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/release_notes/pingcentral_relnotes_march2023.html
revdate: August 3, 2023
section_ids:
  updated-client-secret-generation-to-produce-client-secrets-compatible-with-pingfederate: Updated client secret generation to produce client secrets compatible with PingFederate
  multiple-acs-urls: Multiple ACS URLs
  set-application-name: Set application name
  deleting-an-application-in-pingcentral-also-deletes-it-in-other-environments: Deleting an application in PingCentral also deletes it in other environments
  configure-oauth-credentials-for-use-instead-of-username-and-password-to-connect-to-pingfederate-or-pingaccess: Configure OAuth credentials for use instead of username and password to connect to PingFederate or PingAccess
  upgraded-from-v1-h2-database-to-v2: Upgraded from v1 H2 database to v2
  configure-apc-mappings-for-oidc-applications-in-pingfederate: Configure APC mappings for OIDC applications in PingFederate
  promoting-applications-with-authentication-challenge-policies: Promoting applications with authentication challenge policies
  sp-certificates-and-assertion-encryption-certificates-must-be-different: SP certificates and assertion encryption certificates must be different
  update-truststore-path-if-pingcentral-fails-to-start: Update truststore path if PingCentral fails to start
  cannot-update-or-revert-templates-created-in-1-2-or-earlier: Cannot update or revert templates created in 1.2 or earlier
  cannot-migrate-the-h2-database-if-the-installation-path-has-any-spaces: Cannot migrate the H2 database if the installation path has any spaces
---

# PingCentral 1.11 (March 2023)

For the best possible experience, review these notes before using PingCentral 1.11.

## Updated client secret generation to produce client secrets compatible with PingFederate

New

When creating a new client, PingCentral now generates OAuth client secrets compatible with PingFederate. For more information, see [Promoting OAuth and OIDC applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html#oauth).

## Multiple ACS URLs

New

You can now configure multiple Assertion Consumer Service (ACS) URLs during SAML application creation. This new feature simplifies application development since the same application can use different URLs simultaneously. For more information, see [Using SAML 2.0 templates](../pingcentral_for_application_owners/pingentral_adding_apps/pingcentral_adding_apps.html#saml_template).

## Set application name

New

When promoting an application between environments, you can now configure an application name for OAuth and OpenID Connect (OIDC) clients, SAML connections, and PingAccess applications. For more information, see [Promoting applications](../pingcentral_for_application_owners/pingcentral_promoting_apps/pingcentral_promoting_apps.html).

## Deleting an application in PingCentral also deletes it in other environments

Improved

You can now choose to delete applications from PingFederate or PingAccess in addition to PingCentral. This feature is flexible because you can select which environments to delete the application from. For more information, see [Managing applications](../pingcentral_for_iam_administrators/pingcentral_mng_applications/pingcentral_manage_apps.html).

## Configure OAuth credentials for use instead of username and password to connect to PingFederate or PingAccess

Improved

Instead of using administrator credentials for basic authentication, you can now configure PingCentral to use OAuth client credentials to connect to PingFederate or PingAccess. will request an `access_token` to use whenever it connects to PingFederate or PingAccess. For more information, see [Configuring PingFederate and PingAccess for SSO](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_pf_pa_sso.html).

## Upgraded from v1 H2 database to v2

Security

Along with other dependencies (libraries), we've upgraded the H2 database from v1 to v2. For more information, see [Upgrading PingCentral](../pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_upgrading/pingcentral_upgrading_pc.html).

## Configure APC mappings for OIDC applications in PingFederate

Issue PASS-3613 PingFederate

PingCentral promotes access token mappings and authentication policy contracts (APCs) with OIDC applications, but the APC mappings that link the APCs to the access token managers are not currently promoted with them. If the APC mappings do not already exist in the target PingFederate environments, applications do not function as expected.

When new APCs are promoted in PingCentral, access token mapping referencing the APC is created, but persistent grant mapping is not established, so the configurations are invalid.

To resolve these issues, configure the APC mappings within PingFederate.

## Promoting applications with authentication challenge policies

Issue PASS-4948 PingAccess

Customized authentication challenge responses, which support single-page applications, are available in PingAccess 6.2 or later. Applications with this type of policy can be added to PingCentral but cannot be promoted to another environment unless the authentication challenge policy, with the same UUID, also exists in the target environment.

## SP certificates and assertion encryption certificates must be different

Issue PASS-5663 PingAccess

When promoting SAML applications, PingFederate does not allow you to use the same certificate as both a service provider (SP) certificate and an assertion encryption certificate. Instead of preventing the promotion to continue, you receive a message similar to the following:

`Environment'staging': PingFederate. This certificate either has the same ID or the same content as the certificate with index 0.`

To continue the promotion, ensure that the SP certificate and the assertion encryption certificate are different.

## Update truststore path if PingCentral fails to start

Issue PASS-5977

After upgrading to 1.8, 1.9, 1.10, or 1.11, PingCentral fails to start if `$\{pingcentral.home}` is used in the trust store path. To prevent this from happening, change the home path to be the absolute trust store path and delete the **Certificates** table in the database.

## Cannot update or revert templates created in 1.2 or earlier

Issue PASS-6466

Templates created in 1.2 or earlier do not store the environment ID, so you cannot update their grant types, scopes, or policy contracts, nor can you revert them to previous versions.

## Cannot migrate the H2 database if the installation path has any spaces

Issue PASS-6591

If the installation path has any spaces in the existing or new instance, the H2 database is not migrated during upgrade. Upon removing the spaces from the file path, the migration is successful.