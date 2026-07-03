---
title: Add application to Azure AD
description: Add an application to Azure Active Directory to create and expose Microsoft Graph API endpoints for provisioning.
component: office365
page_id: office365:office_365_provisioner:pf_office365_connector_add_application_to_azure_ad
canonical_url: https://docs.pingidentity.com/integrations/office365/office_365_provisioner/pf_office365_connector_add_application_to_azure_ad.html
revdate: June 20, 2024
section_ids:
  steps: Steps
---

# Add application to Azure AD

Add an application to Azure Active Directory to create and expose Microsoft Graph API endpoints for provisioning.

## Steps

1. Complete the steps in [Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-integrating-applications) in the [Microsoft identity platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-developers-guide).

2. Note your Azure application ID and secret.

3. To allow the provisioner to manage all users, including deleting users or modifying administrators, assign the "User administrator" role to your Azure AD application.

   1. Complete the steps in ["Authorization\_RequestDenied" error message when you try to change a password if you use Graph API](https://support.microsoft.com/en-us/help/3004133/authorization-requestdenied-error-message-when-you-try-to-change-a-pas) in the Microsoft documentation.

4. Add the following application permissions to your application by completing the steps in .microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis//\[Add permissions to access web APIs]:

   * `Application.ReadWrite.All`

   * `Group.ReadWrite.All`

   * `Organization.Read.All`

   * `User.ReadWrite.All`
