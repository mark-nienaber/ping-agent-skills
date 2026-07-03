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
