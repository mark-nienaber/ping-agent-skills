---
title: Configuring SAML SSO with Microsoft 365 and PingFederate
description: Learn how to enable Microsoft 365 sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Microsoft 365 sign-on using PingFederate (SP-initiated sign-on).
component: configuration_guides
page_id: configuration_guides:microsoft_365:config_saml_o365_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/microsoft_365/config_saml_o365_pf.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  create-a-pingfederate-sp-connection-for-microsoft-365: Create a PingFederate SP connection for Microsoft 365
  add-the-pingfederate-connection-to-microsoft-365: Add the PingFederate connection to Microsoft 365
  test-the-pingfederate-idp-initiated-sso-integration: Test the PingFederate IdP-initiated SSO integration
  test-the-pingfederate-sp-initiated-sso-integration: Test the PingFederate SP-initiated SSO integration
---

# Configuring SAML SSO with Microsoft 365 and PingFederate

Learn how to enable Microsoft 365 sign-on from a PingFederate URL (IdP-initiated sign-on) and direct Microsoft 365 sign-on using PingFederate (SP-initiated sign-on).

## Before you begin

* Configure PingFederate to authenticate against an IdP or datastore containing the users requiring application access.

* Make sure Microsoft 365 has a valid, non-default domain and is populated with at least one AD synced user in that domain to test access.

* You must have administrative access to PingFederate and Microsoft 365.

* You must have access to run the Microsoft Azure Active Directory Module for Windows PowerShell.

## Create a PingFederate SP connection for Microsoft 365

1. Download the Microsoft 365 SAML metadata from <https://nexus.microsoftonline-p.com/federationmetadata/saml20/federationmetadata.xml>.

2. Sign on to the PingFederate administrative console.

3. Create an SP connection for Microsoft 365 in Ping Federate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Import the metadata from the downloaded Microsoft 365 metadata file.

   3. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

      * **SP Initiated SLO**

   4. In **Assertion Creation: Attribute Contract**, extend the contract to add the attributes **guid** and **SAML\_NAME\_FORMAT**.

   5. In **Assertion Creation: Authentication Source Mapping: Attribute Contract Fulfillment** map the following:

      * SAML\_SUBJECT to **guid** (**guid** should map to your attribute holding the Microsoft 365 user objectID and be in Base64 binary format)

      * **SAML\_NAME\_FORMAT** to **urn:oasis:names:tc:SAML:2.0:nameid-format:persistent**.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST** and **REDIRECT**.

   7. In **Protocol Settings: Signature Policy**, select **Always Sign Assertion**.

   8. In **Credentials: Digital Signature Settings**, select the PingFederate signing certificate.

4. Save the configuration.

5. Export the signing certificate.

6. Export and then open the metadata file and copy the values for the following:

   * entityID

   * Location entry for SSO (`https://your-value/idp/SSO.saml2`)

   * Location entry for SLO (`https://your-value/idp/SLO.saml2`)

## Add the PingFederate connection to Microsoft 365

1. Open an elevated Windows PowerShell Command Prompt window on any internet-connected computer and type:

   ```powershell
   $cred = Get-Credential
   ```

2. Enter the username and password of your Microsoft 365 administrator account in the pop-up.

   ![Screen capture of Windows Powershell credential request prompting for username and password.](_images/ntm1622072017171.png)

3. Connect with MsolService.

   ```powershell
   Connect-MsolService -Credential $cred
   ```

4. List your domains.

   ```powershell
   Get-MsolDomain
   ```

5. Select the domain for which you would like to enable SSO.

   ```powershell
   $dom = "your-O365-domain"
   ```

6. Set the `uri` parameter to the PingFederate **entityID** value.

   ```powershell
   $uri ="your-entityID"
   ```

7. Set the `url` parameter to the PingFederate **Location for SSO** value.

   ```powershell
   $url="your-Passive-Log-On-Uri"
   ```

8. Set the `logouturl` parameter to the PingFederate **Location for SLO** value.

   ```powershell
   $logouturl="your-Log-Off-Uri"
   ```

9. Open the downloaded signing certificate in Notepad, copy the encoded contents, and paste them into the command below to set the certificate parameter.

   ```powershell
   $cert="your-certificate-contents"
   ```

10. Run the following command to setup SAML SSO for your domain.

    ```powershell
    Set-MsolDomainAuthentication `
    -DomainName $dom `
    -FederationBrandName $dom `
    -Authentication Federated `
    -PassiveLogOnUri $url `
    -SigningCertificate $cert `
    -IssuerUri $uri `
    -LogOffUri $logouturl `
    -PreferredAuthenticationProtocol SAMLP
    ```

11. Run the following command to see the completed SSO settings.

    ```powershell
    Get-MSolDomainFederationSettings -DomainName "your-O365-domain" | Format-List *
    ```

## Test the PingFederate IdP-initiated SSO integration

1. Go to the PingFederate SSO application endpoint for the Microsoft 365 SP connection.

2. Complete PingFederate authentication.

   You're redirected to your Microsoft 365 domain.

## Test the PingFederate SP-initiated SSO integration

1. Go to <https://portal.office.com>.

2. Enter your email address.

3. After you're redirected to PingFederate, enter your PingFederate username and password.

   You're redirected back to Microsoft 365.
