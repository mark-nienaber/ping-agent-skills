---
title: Changing the federation protocol in Office 365 from WS-Federation to SAML2P
description: Office 365 can use either SAML2P or WS-Federation to authenticate passive profiles or web-based clients. This task details changing the federation protocol configuration of your Office 365 domain from WS-Federation to SAML2P.
component: solution-guides
page_id: solution-guides:standards_and_protocols_use_cases:htg_change_from_ws_fed_to_saml2p_office365
canonical_url: https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/htg_change_from_ws_fed_to_saml2p_office365.html
revdate: April 8, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  troubleshooting: Troubleshooting
---

# Changing the federation protocol in Office 365 from WS-Federation to SAML2P

Office 365 can use either SAML2P or WS-Federation to authenticate passive profiles or web-based clients. This task details changing the federation protocol configuration of your Office 365 domain from WS-Federation to SAML2P.

## Before you begin

* [Connect PowerShell to Office 365](https://docs.microsoft.com/en-us/microsoft-365/enterprise/connect-to-microsoft-365-powershell?view=o365-worldwide)

## About this task

Change the federation protocol from WS-Federation to SAML2P in Office 365 using PowerShell.

## Steps

1. Sign on to Office 365 PowerShell as an administrator.

   ```powershell
   PS C:\Users\Administrator> Connect-MsolService
   ```

2. Show current settings.

   ```powershell
   PS C:\Users\Administrator> Get-MsolDomainFederationSettings -domainName  Office 365 domain name  | Format-List *

   ExtensionData                   : System.Runtime.Serialization.ExtensionDataObject
   ActiveLogOnUri                  : https://pf1.pinggcs.com:9031/idp/sts.wst
   FederationBrandName             : Ping Identity
   IssuerUri                       :  Office 365 domain name
   LogOffUri                       : https://pf1.pinggcs.com:9031/idp/prp.wsf
   MetadataExchangeUri             : https://pf1.pinggcs.com:9031/pf/sts_mex.ping?PartnerSpId=urn:federation:MicrosoftOnline
   NextSigningCertificate          :
   PassiveLogOnUri                 : https://pf1.pinggcs.com:9031/idp/prp.wsf
   PreferredAuthenticationProtocol : WsFed
   SigningCertificate              : MIICX...
   ```

3. Save the settings to a variable.

   ```powershell
   PS C:\Users\Administrator> $saml = Get-MsolDomainFederationSettings -DomainName  Office 365 domain name
   ```

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Save the old settings to a file for easy recovery.```powershell
   PS C:\Users\Administrator> Get-MsolDomainFederationSettings -DomainName  Office 365 domain name  | Export-Clixml dfs-pf-wsfed.xml
   ``` |

4. Update the variable to use SAML2P endpoints for the passive profile.

   ```powershell
   PS C:\Users\Administrator> $saml.PassiveLogOnUri = "https://pf1.pinggcs.com:9031/idp/SSO.saml2"
   PS C:\Users\Administrator> $saml.LogOffUri = "https://pf1.pinggcs.com:9031/idp/startSLO.ping"
   ```

5. Disable SSO from the domain.

   ```powershell
   PS C:\Users\Administrator> Set-MsolDomainAuthentication -DomainName  Office 365 domain name  -Authentication Managed
   ```

6. Use `Set-MsolDomainAuthentication` to set the `$saml` variable to enable federation.

   ```powershell
   PS C:\Users\Administrator> Set-MsolDomainAuthentication -DomainName  Office 365 domain name  -FederationBrandName $saml.FederationBrandName -Authentication Federated -PassiveLogOnUri $saml.PassiveLogOnUri -ActiveLogOnUri $saml.ActiveLogonUri -SigningCertificate $saml.SigningCertificate -IssuerUri $saml.IssuerUri -LogOffUri $saml.LogOffUri -PreferredAuthenticationProtocol "SAMLP"
   ```

7. Review the results.

   ```powershell
   PS C:\Users\Administrator> Get-MsolDomainFederationSettings -domainName  Office 365 domain name  | Format-List *

   ExtensionData                   : System.Runtime.Serialization.ExtensionDataObject
   ActiveLogOnUri                  : https://pf1.pinggcs.com:9031/idp/sts.wst
   FederationBrandName             : Ping GCS
   IssuerUri                       :  Office 365 domain name
   LogOffUri                       : https://pf1.pinggcs.com:9031/idp/startSLO.ping
   MetadataExchangeUri             : https://pf1.pinggcs.com:9031/pf/sts_mex.ping?PartnerSpId=urn:federation:MicrosoftOnline
   NextSigningCertificate          :
   PassiveLogOnUri                 : https://pf1.pinggcs.com:9031/idp/SSO.saml2
   PreferredAuthenticationProtocol : Samlp
   SigningCertificate              : MIICX...
   ```

8. Save the new settings to a different file.

   ```powershell
   PS C:\Users\Administrator> Get-MsolDomainFederationSettings -DomainName  Office 365 domain name  | Export-Clixml dfs-pf-samlp.xml
   ```

## Troubleshooting

For troubleshooting, see the following to restore the federation protocol settings back to WS-Federation from SAML2P:

1. Restore the saved settings to a variable.

   ```powershell
   PS C:\Users\Administrator> $wsfed = Import-Clixml dfs-pf-wsfed.xml
   ```

2. Disable SSO from the domain.

   ```powershell
   PS C:\Users\Administrator> Set-MsolDomainAuthentication -DomainName  Office 365 domain name  -Authentication Managed
   ```

3. Use `Set-MsolDomainAuthentication` to enable WS-Federation using the `$wsfed` variable.

   ```powershell
   PS C:\Users\Administrator> Set-MsolDomainAuthentication -DomainName  Office 365 domain name  -FederationBrandName $wsfed.FederationBrandName -Authentication Federated -PassiveLogOnUri $wsfed.PassiveLogOnUri -ActiveLogOnUri $wsfed.ActiveLogonUri -SigningCertificate $wsfed.SigningCertificate -IssuerUri $wsfed.IssuerUri -LogOffUri $wsfed.LogOffUri -PreferredAuthenticationProtocol "WSFED"
   ```
