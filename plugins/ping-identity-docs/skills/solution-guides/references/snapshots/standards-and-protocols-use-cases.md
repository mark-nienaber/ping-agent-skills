---
title: Changing the federation protocol in Office 365 from WS-Federation to SAML2P
description: Office 365 can use either SAML2P or WS-Federation to authenticate passive profiles or web-based clients. This task details changing the federation protocol configuration of your Office 365 domain from WS-Federation to SAML2P.
component: solution-guides
page_id: solution-guides:standards_and_protocols_use_cases:htg_change_from_ws_fed_to_saml2p_office365
canonical_url: https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/htg_change_from_ws_fed_to_saml2p_office365.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

---

---
title: Configuring browsers for Kerberos and NTLM
description: The PingFederate Integrated Windows Authentication (IWA) adapter uses the Simple and Protected GSS-API Negotiation Mechanism (SPNEGO) for Kerberos and NTLM authentication.
component: solution-guides
page_id: solution-guides:standards_and_protocols_use_cases:htg_config_browsers_for_kerberos_and_ntlm
canonical_url: https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/htg_config_browsers_for_kerberos_and_ntlm.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2025
page_aliases: ["standards_and_protocols_use_cases:htg_config_browsers_for_kerberos_and_ntlm_safari.adoc", "standards_and_protocols_use_cases:htg_config_browsers_for_kerberos_and_ntlm_edge.adoc", "standards_and_protocols_use_cases:htg_config_browsers_for_kerberos_and_ntlm_ie_chrome_windows.adoc", "standards_and_protocols_use_cases:htg_config_browsers_for_kerberos_and_ntlm_chrome_macos.adoc", "standards_and_protocols_use_cases:htg_config_browsers_for_kerberos_and_ntlm_firefox.adoc"]
section_ids:
  configuring-apple-safari: Configuring Apple Safari
  configuring-microsoft-edge: Configuring Microsoft Edge
  configuring-internet-explorer-and-google-chrome-on-windows-for-kerberos-and-ntlm: Configuring Internet Explorer and Google Chrome on Windows for Kerberos and NTLM
  about-this-task: About this task
  steps: Steps
  result: Result
  configuring-google-chrome-on-mac-os-for-kerberos-and-ntlm: Configuring Google Chrome on Mac OS for Kerberos and NTLM
  about-this-task-2: About this task
  steps-2: Steps
  result-2: Result:
  configuring-mozilla-firefox-for-kerberos-and-ntlm: Configuring Mozilla Firefox for Kerberos and NTLM
  about-this-task-3: About this task
  steps-3: Steps
  result-3: Result
---

# Configuring browsers for Kerberos and NTLM

The PingFederate Integrated Windows Authentication (IWA) adapter uses the Simple and Protected GSS-API Negotiation Mechanism (SPNEGO) for Kerberos and NTLM authentication.

You can find IWA adapter system requirements in the [IWA documentation](https://cdn-docs.pingidentity.com/archive/pdf/integrations/pingfederate-iwa-ik.pdf).

Read the following sections for instructions specific to the browsers you want to configure.

## Configuring Apple Safari

Safari on Windows supports SPNEGO with no further configuration. SPNEGO supports Kerberos if the computer is domain-joined and logged in by a domain user, otherwise SPNEGO negotiates NTLM.

Safari on Mac OS X supports SPNEGO with Kerberos if Mac OS is joined to Active Directory (AD), otherwise SPNEGO negotiates NTLM.

For information on joining Mac OS to AD, see [Integrate Active Directory](https://support.apple.com/guide/directory-utility/integrate-active-directory-diru39a25fa2/5.0/mac/10.14).

## Configuring Microsoft Edge

Before configuring Microsoft Edge for Kerberos and NTLM, determine whether you have the legacy or Chromium version.

* Legacy

  To configure Microsoft Edge (Legacy), see [Kerberos Adapter does not work for Edge Browsers in Windows 10 for SSO](https://support.pingidentity.com/s/article/Kerberos-Adapter-does-not-work-for-Edge-Browsers-in-Windows-10) in the Ping Identity Knowledge Base.

* Chromium

  To configure Microsoft Edge (Chromium), see [Kerberos unconstrained double-hop authentication with Microsoft Edge (Chromium)](https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/iis/www-authentication-authorization/kerberos-double-hop-authentication-edge-chromium) in the Microsoft documentation.

## Configuring Internet Explorer and Google Chrome on Windows for Kerberos and NTLM

Add sites to the trusted zone to enable the Simple and Protected GSS-API Negotiation Mechanism (SPNEGO).

### About this task

By default, any IWA authentication request originating from an Internet host is not allowed. The default setting only allows clients to automatically provide credentials to hosts within the intranet zone. Sites are considered to be in the intranet zone if the connection was established using a Universal Naming Convention path (for example, `pingsso`), the site bypasses the proxy server, or host names don't contain periods (for example, `http://pingsso`).

Most PingFederate single sign-on (SSO) connections use the fully qualified domain name, so they won't be categorized as being in the intranet zone. Configure the browser to trust the host by adding the PingFederate hostname to the trusted sites zone.

The default setting, **Automatic logon with current user name and password**, uses Kerberos if available and NTLM if not. The setting **Prompt for user name and password** only uses NTLM.

If Internet Explorer Enhanced Security Configuration is enabled, a login prompt overrides the automatic login behavior. This prompt allows Kerberos and NTLM functionality, however it does not use the cached credentials from the user login.

To configure Internet Explorer and Google Chrome to support SPNEGO:

### Steps

1. From the Control Panel, go to **Network and Internet → Internet Options → Security**.

2. Click **Trusted Sites**, then click **Custom Level**.

3. Under User Authentication, select**Automatic logon with current user name and password**. Click **OK**.

4. On the **Security** tab, click **Trusted Sites**, then click **Sites**.

5. In the **Add this website to the zone** field, enter the PingFederate server's hostname and click **Add**. Click **Close**.

   |   |                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can include an asterisk in front of the domain suffix to trust any host name within the AD domain (for example,*\*.ADdomain.pingidentity.com*). |

### Result

SPNEGO supports Kerberos if the computer is domain-joined and logged in with an AD user account.

SPNEGO negotiates NTLM on non-domain-joined computers. You are prompted for credentials, for which you would enter *\<ADdomain>\\\<username>* and the password.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The NetBIOS domain name (*\<ADdomain>* in the above example) must qualify the username if:- The computer is not joined to an AD domain, or

- There are multiple AD domains or forests and you are authenticating over a cross-domain trust. |

You can add the PingFederate URL to the local intranet zone as an alternative to adding it to the trusted sites zone. Reasons for this vary based on the network design of the environment, but setting **Automatic logon with current user name and password** for the trusted sites zone implies that negotiate/authorization credentials might be sent in requests to sites outside of the intranet zone.

## Configuring Google Chrome on Mac OS for Kerberos and NTLM

Authorize hosts for the Simple and Protected GSS-API Negotiation Mechanism (SPNEGO) using the terminal.

### About this task

SPNEGO works on Chrome without configuration, but only negotiates NTLM. To enable Kerberos, you must authorize host or domain names for SPNEGO protocol message exchanges. Do this from Terminal or by joining Mac OS to AD. For information on joining Mac OS to AD, see [Integrate Active Directory](https://support.apple.com/guide/directory-utility/integrate-active-directory-diru39a25fa2/5.0/mac/10.14). For iOS, only NTLM via SPNEGO has been tested. Kerberos has not been verified.

Configure `AuthServerWhitelist` from the Terminal:

### Steps

1. Within your Mac OS Terminal, run `kinit` to get an initial ticket-granting ticket from your Kerberos domain controller to request service tickets for the IWA adapter.

   ```
   >kinit  <joe@ADdomain.com>
   joe@ADdomain.com's Password:  <YourPassword>
   ```

2. Go to the Chrome directory and start Chrome with the `AuthServerWhitelist` parameter.

   ```
   >cd  </Applications/Google Chrome.app/Contents/MacOS>
   >./"Google Chrome" --auth-server-whitelist="<*.addomain.com>"
   ```

   |   |                                                                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Some services require delegation of the users identity. By default, Chrome does not allow this.The `AuthNegotiateDelegateWhitelist` policy points Chrome to a server to delegate credentials. Add this parameter to the above command by specifying `--auth-negotiate-delegate-whitelist="*.adexample.com"`. |

   #### Result:

   This setting persists every time Chrome is launched.

3. Run `kinit` every 10 hours for Chrome to request service tickets for the IWA adapter.

## Configuring Mozilla Firefox for Kerberos and NTLM

Configure a list of trusted sites for the Simple and Protected GSS-API Negotiation Mechanism (SPNEGO).

### About this task

Firefox rejects all SPNEGO challenges from any web server by default. You must configure a whitelist of sites permitted to exchange SPNEGO messages with the browser.

### Steps

1. In the Firefox address bar, enter `about:config`. Click **I accept the risk!**

2. Search for the following preferences:

   * `network.negotiate-auth.trusted-uris`

   * `network.automatic-ntlm-auth.trusted-uris`

3. Double-click each of the preferences and enter any host or domain names in the **Enter string value** field, separated by commas. Click **OK**.

   |   |                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can add a period in front of the domain suffix to trust any hostname within the domain (for example, *.adexample.pingidentity.com*). |

### Result

SPNEGO supports Kerberos if the computer is joined to Active Directory (AD) and logged on with a domain user account, otherwise SPNEGO negotiates NTLM.

Firefox on Mac OS supports both Kerberos and NTLM if the computer is joined to AD, otherwise only NTLM negotiates.

---

---
title: Integrated Windows Authentication Group Policy browser settings
description: Apply browser settings using Group Policy.
component: solution-guides
page_id: solution-guides:standards_and_protocols_use_cases:htg_integrated_windows_authn_group_policy_browser_setting
canonical_url: https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/htg_integrated_windows_authn_group_policy_browser_setting.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 8, 2025
---

# Integrated Windows Authentication Group Policy browser settings

Apply browser settings using Group Policy.

The PingFederate Integrated Windows Authentication (IWA) adapter supports the Kerberos and NTLM authentication protocols, though some browsers must be configured to use them. These settings are configured manually on each computer, except in a Windows Enterprise environment, where they are managed by Group Policy.

Within Group Policy there are two configuration subsets available: policies and preferences. Policies and preferences are applied through Group Policy Objects (GPOs) for the following browser configurations:

* Internet Explorer

* Google Chrome

* Mozilla Firefox

Policies typically configure system-specific settings such as Windows operating system, security, and software settings. When the GPO falls out of scope, Group Policy Preference settings remain the same. In Policies, the defined settings supersede the local system or user settings. When they fall out of scope, the local settings revert to the previous settings.

---

---
title: Providing a persistent SAML NameID format in PingFederate
description: Use a custom SAML NameID format by defining a hidden attribute in the PingFederate attribute contract.
component: solution-guides
page_id: solution-guides:standards_and_protocols_use_cases:htg_provide_persistent_saml_nameid_format_in_pf
canonical_url: https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/htg_provide_persistent_saml_nameid_format_in_pf.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 8, 2025
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
  related-links: Related links
---

# Providing a persistent SAML NameID format in PingFederate

Use a custom SAML NameID format by defining a hidden attribute in the PingFederate attribute contract.

## Before you begin

You must have the following product versions:

* PingFederate 10.3

## About this task

Some SAML federation partner software requires a SAML NameID format of `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`. Provide this format by using `SAML_NAME_FORMAT`.

## Steps

1. In PingFederate, go to **Applications → SP Connections**.

2. In the **SP Connections** list, select your connection.

3. Click the **Browser SSO** tab, and then click **Configure Browser SSO**.

4. Click the **Assertion Creation** tab, and then click **Configure Assertion Creation**.

5. Click the **Attribute Contract** tab.

6. Extend the contract using the following table as a guide.

   | Attribute Contract | Subject Name Format                                         |
   | ------------------ | ----------------------------------------------------------- |
   | `SAML_SUBJECT`     | **urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified**   |
   | `SAML_NAME_FORMAT` | **urn:oasis:names:tc:SAML:1.1:attrname-format:unspecified** |

7. Click **Next**.

8. Click the **Authentication Source Mapping** tab and then click **Map New Adapter Instance**.

9. On the **Adapter Instance** tab, in the **Adapter Instance** list, select your adapter. Click **Next**.

10. On the **Mapping Method** tab, leave the default settings and click **Next**.

11. On the **Attribute Contract Fulfillment** tab, fulfill the contract using the following table as a guide.

    | Attribute Contract | Source    | Value                                                  |
    | ------------------ | --------- | ------------------------------------------------------ |
    | `SAML_SUBJECT`     | `Adapter` | `username`                                             |
    | `SAML_NAME_FORMAT` | `Text`    | `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` |

12. Click **Next** until you reach the **Summary** tab. Click **Save**.

## Result

This produces a `SAML_SUBJECT` similar to the following example.

```text
<saml:Subject>
<saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:persistent">joe</saml:NameID>
<saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
```

The new `SAML_NAME_FORMAT` value overrides the original SAML NameID.

## Related links

* [Assertions and Protocols for the OASIS Security Assertion Markup Language](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

---

---
title: Standards and Protocols Use Cases
description: Changing the federation protocol in Office 365 from WS-Federation to SAML2P
component: solution-guides
page_id: solution-guides:standards_and_protocols_use_cases:htg_standards_and_protocols
canonical_url: https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/htg_standards_and_protocols.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 8, 2025
---

# Standards and Protocols Use Cases

| Use case                                                                                                                          | Description                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Changing the federation protocol in Office 365 from WS-Federation to SAML2P](htg_change_from_ws_fed_to_saml2p_office365.html)    | Office 365 can use either SAML2P or WS-Federation to authenticate passive profiles or web-based clients. This task details changing the federation protocol configuration of your Office 365 domain from WS-Federation to SAML2P. |
| [Configuring browsers for Kerberos and NTLM](htg_config_browsers_for_kerberos_and_ntlm.html)                                      | The PingFederate Integrated Windows Authentication (IWA) adapter uses the Simple and Protected GSS-API Negotiation Mechanism (SPNEGO) for Kerberos and NTLM authentication.                                                       |
| [Integrated Windows Authentication Group Policy browser settings](htg_integrated_windows_authn_group_policy_browser_setting.html) | Apply browser settings using Group Policy.                                                                                                                                                                                        |
| [Providing a persistent SAML NameID format in PingFederate](htg_provide_persistent_saml_nameid_format_in_pf.html)                 | Use a custom SAML NameID format by defining a hidden attribute in the PingFederate attribute contract.                                                                                                                            |
| [Using OpenSSL s\_client commands to test SSL connectivity](htg_use_openssl_to_test_ssl_connectivity.html)                        | Test SSL connectivity with `s_client` commands to check whether the certificate is valid, trusted, and complete.                                                                                                                  |

---

---
title: Using OpenSSL s_client commands to test SSL connectivity
description: Use OpenSSL s_client commands to evaluate and troubleshoot certificates and secure connections.
component: solution-guides
page_id: solution-guides:standards_and_protocols_use_cases:htg_use_openssl_to_test_ssl_connectivity
canonical_url: https://docs.pingidentity.com/solution-guides/standards_and_protocols_use_cases/htg_use_openssl_to_test_ssl_connectivity.html
llms_txt: https://docs.pingidentity.com/solution-guides/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 8, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  related-links: Related links
---

# Using OpenSSL s\_client commands to test SSL connectivity

Test SSL connectivity with `s_client` commands to check whether the certificate is valid, trusted, and complete.

## Before you begin

Install OpenSSL software from <http://www.openssl.org/>.

## Steps

1. In the command line, enter `openssl s_client -connect` *\<hostname>*`:<port>`.

   ### Result:

   This opens an SSL connection to the specified hostname and port and prints the SSL certificate.

2. Check the availability of the domain from the connection results.

   The following table includes some commonly used `s_client` commands. For more information, see [OpenSSL s\_client commands man page](https://docs.openssl.org/master/man1/openssl-cmds/) in the OpenSSL toolkit.

   To view a complete list of `s_client` commands in the command line, enter `openssl -?`.

   | Command Options | Description                                                                                                                                                       | Example                                                                  |
   | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
   | `-connect`      | Tests connectivity to an HTTPS service.                                                                                                                           | `openssl s_client -connect pingfederate.<YourDomain>.com:443`            |
   | `-showcerts`    | Prints all certificates in the certificate chain presented by the SSL service. Useful when troubleshooting missing intermediate CA certificate issues.            | `openssl s_client -connect <hostname>:<port> -showcerts`                 |
   | `-tls, -dtls1`  | Forces TLSv1 and DTLSv1 respectively.                                                                                                                             | `openssl s_client -connect <hostname>:<port> -tls1`                      |
   | `-cipher`       | Forces a specific cipher. This option is useful in testing enabled SSL ciphers. Use the `openssl ciphers` command to see a list of available ciphers for OpenSSL. | `openssl s_client -connect <hostname>:<port> -cipher DHE-RSA-AES256-SHA` |

3. Troubleshooting:

   For troubleshooting connection and SSL handshake problems, see the following:

   * If there is a connection problem reaching the domain, the OpenSSL `s_client -connect` command waits until a timeout occurs and prints an error, such as `connect: Operation timed out`.

   * If you use the OpenSSL client to connect to a non-SSL service, the client connects but the SSL handshake doesn't happen. `CONNECTED (00000003)` prints as soon as a socket opens, but the client waits until a timeout occurs and prints an error message, such as `44356:error:140790E5:SSL routines:SSL23_WRITE:ssl handshake failure:/SourceCache/OpenSSL098/OpenSSL098-47.1/src/ssl/s23_lib.c:182:`.

     After disabling a weak cipher, you can verify if it has been disabled or not with the following command.

     ```shell
     openssl s_client -connect google.com:443 -cipher EXP-RC4-MD5
     ```

## Related links

* [SSL Labs](https://www.ssllabs.com/ssltest/)