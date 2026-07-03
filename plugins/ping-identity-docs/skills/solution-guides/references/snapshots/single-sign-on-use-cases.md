---
title: Changing certificates from SHA-1 to SHA-2 in PingFederate
description: Use your Java Virtual Machine (JVM) to generate SHA-2 certificates and import them into PingFederate to replace default SHA-1 certificates for better security.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_change_certs_from_sha_1_to_sha_2_pf
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_change_certs_from_sha_1_to_sha_2_pf.html
revdate: February 16, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Changing certificates from SHA-1 to SHA-2 in PingFederate

Use your Java Virtual Machine (JVM) to generate SHA-2 certificates and import them into PingFederate to replace default SHA-1 certificates for better security.

## Before you begin

**Component**

* PingFederate earlier than version 8

Ensure that you have installed a JVM.

## About this task

PingFederate generates SHA-1 certificates by default prior to version 8. Use these instructions to create an SHA-2 certificate with `keytool` and import it into PingFederate.

## Steps

1. **If using JDK 1.9 or later, skip to step 4.** If using an earlier version, see <https://www.oracle.com/java/technologies/javase-jce-all-downloads.html>.

   |   |                                                                                           |
   | - | ----------------------------------------------------------------------------------------- |
   |   | Java versions 1.9 and later include the appropriate policy files and use them by default. |

2. Copy `local_policy.jar` and `US_export_policy.jar` to `$JAVA_HOME/jre/lib/security`. These .jar files already exist in the JCE, so you must overwrite them. If you have a cluster, do this for each node.

3. Restart PingFederate.

4. When signing keypairs, use `keytool` to generate a self-signed certificate in a `pkcs12` keystore instead of the default `.jks` type.

   ```
   keytool -genkeypair -alias sha256 -keyalg RSA -keysize 2048 -sigalg SHA256withRSA -keystore sha256.p12 -storepass 2Federate -storetype pkcs12
   ```

5. Import the `sha256.p12` file into the appropriate PingFederate keystore using the administration console. Replicate the configuration change to all nodes within a cluster by clicking **Cluster Management → Replicate Cluster Configuration**.

6. Export the public key certificate using either the administration console or the following command:

   ```
   keytool -exportcert -alias sha256 -keystore sha256.p12 -storepass 2Federate -storetype pkcs12 -file  cert_name.crt
   ```

7. To view the contents of the public key certificate, enter the following command:

   ```
   keytool -printcert -file  cert_name.crt
   ```

---

---
title: Configuring a PingFederate authentication policy using PingID MFA authentication for CyberArk PVWA
description: For CyberArk and Ping Identity best practices, deploy MFA for all single sign-on (SSO) requests to the CyberArk Password Vault Web Access (PVWA).
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_integrate_cyberark_sso_authn_pf_pid
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_integrate_cyberark_sso_authn_pf_pid.html
revdate: April 29, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  result-4: Result:
---

# Configuring a PingFederate authentication policy using PingID MFA authentication for CyberArk PVWA

For CyberArk and Ping Identity best practices, deploy MFA for all single sign-on (SSO) requests to the CyberArk Password Vault Web Access (PVWA).

## About this task

Integrate a PingFederate authentication policy with PingID multi-factor authentication (MFA).

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The following configuration steps assume you are creating a new authentication policy specifically for MFA to the CyberArk PVWA. If other existing authentication policies are in use, modify your policy tree to perform this task. |

## Steps

1. Go to **Authentication → Integration → IdP Adapters**.

   ### Result:

   The **Manage IdP Adapter Instances** page opens.

2. Click **Create New Instance**.

3. On the **Type** tab, enter a **Instance Name** and an**Instance ID**

4. In the **Type** list, select the **PingID Adapter 2.6** adapter type. Click **Next**.

5. On the **IdP Adapter** tab, select **Choose File** and upload the PingID properties file. Click **Next**.

6. On the **Extended Contract** tab, click **Next**.

7. On the **Adapter Attributes** tab, select the **Pseudonym** checkbox for the **subject** attribute. Click **Next**.

8. On the **Adapter Contract Mapping** tab, click **Next**.

9. On the **Summary** tab, click **Done** to return to the **Manage IdP Adapter Instances** page.

10. Click **Save**.

11. Create a new authentication policy.

    |   |                                                                                                                                                                                                                                                                                                                             |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | These steps will help you create a new authentication policy. For general information about configuring authentication policies, see [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation. |

    1. Go to **Authentication → → Policies** to open the **Authentication Policies** window.

    2. On the **Policies** tab, select the **IDP Authentication Policies** checkbox. Click **Add Policy**.

       ### Result:

       A new **Policy** configuration page opens.

    3. Enter an authentication policy name in the **Name** field and a description in the **Description** field.

    4. In the **Policy** list, select **HTMLForm - (Adapter)**.

    5. In the **Fail** list, click **Done**.

    6. In the **Success** list, select **PingID - (Adapter)**.

    7. In the **Fail** list, select **Done**.

    8. In the **Success** list, select **cyberark - (Policy Contract)**.

    9. In the **Success** list, where **PingID - (Adapter)** is selected, click **Options**.

       ### Result:

       A new **Incoming User ID** modal opens.

    10. In the **Source** list, select **Adapter (HTMLForm)**.

    11. In the **Attribute** list, select **username**. Click **Done** to close and exit the modal.

    12. On the **Policy** page, click **Done** to return to the **Authentication Policies** configuration page.

    13. In the **Policy Contracts** section, click **Contract Mapping** for the CyberArk policy contract.

        ### Result:

        A new **Authentication Policy Contract Mapping** page opens.

    14. On the **Attribute Sources & User Lookup** tab, click **Next**.

    15. On the **Contract Fulfillment** tab, in the **Source** list, select **Adapter (HTMLForm)**.

    16. In the **Value** list, select **username**. Click **Next**.

    17. On the **Issuance Criteria** tab, click **Next**.

    18. On the **Summary** tab, click **Done** to return to the **Authentication Policies** window configuration.

    19. Click **Save**. Click **Done**.

---

---
title: Configuring a PingFederate SAML connection for CyberArk PVWA
description: Set up a SAML connection using PingFederate for CyberArk Password Vault Web Access (PVWA).
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_integrate_cyberark_sso_authn_pf_saml
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_integrate_cyberark_sso_authn_pf_saml.html
revdate: April 29, 2024
section_ids:
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  choose-from: Choose from:
  result-4: Result:
  result-5: Result:
---

# Configuring a PingFederate SAML connection for CyberArk PVWA

Set up a SAML connection using PingFederate for CyberArk Password Vault Web Access (PVWA).

## Steps

1. Go to **Applications → Integration → SP Connections**, and click **Create Connection**.

   ### Result:

   The **SP Connection** page opens.

   ![Screen capture showing the Connection Template tab on the SP Connection page with the "Do not use a template for this connection" option selected](_images/tjz1621443454744.png)

2. On the **Connection Template** tab, select **Do not use a template for this connection**. Click **Next**.

3. On the **Connection Type** tab, select the **Browser SSO Profiles** checkbox. Click **Next**.

4. On the **Connection Options** tab, make sure that the **Browser SSO** checkbox is selected. Click **Next**.

5. On the **Import Metadata** tab, select **None**. Click **Next**.

6. On the **General Info** tab:

   1. In the **Partners Entity ID (Connection ID)** field, enter `PasswordVault`.

   2. Enter a **Connection Name** value.

   3. Click **Next**.

7. On the **Browser SSO** tab, click **Configure Browser SSO**.

   ### Result:

   The **Browser SSO** page opens.

   ![Screen capture showing the SAML Profiles tab on the Browser SSO page](_images/ggd1621443753261.png)

8. On the **SAML Profiles** tab, select the **IDP-Initiated SSO** and **SP-Initiated SSO** checkboxes. Click **Next**.

9. On the **Assertion Lifetime** tab, in the **Minutes Before** and **Minutes After** fields, either leave the default setting of `5` or enter a different parameter value. Click **Next**.

10. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

    ### Result:

    A new **Assertion Creation** page opens.

    ![Screen capture showing the Identity Mapping tab on the Assertion Creation page with the "Standard" option selected.](_images/fve1621444014402.png)

11. On the **Identity Mapping** tab, select **Standard** as the type of name identifier to send to the service provider. Click **Next**.

12. On the **Attribute Contract** tab, in the **SAML\_SUBJECT** row, in the **Subject Name Format** list, select an option. Click **Next**.

    |   |                                                   |
    | - | ------------------------------------------------- |
    |   | The **Extend the Contract** field isn't required. |

13. Add a policy contract:

    ### Choose from:

    * Select an existing policy contract by clicking on its name.

    * Create a new policy contract adapter for authentication:

      1. On the **Authentication Source Mapping** tab, click **Map New Authentication Policy**.

         The **Authentication Policy Mapping** page opens.

         ![Screen capture showing the Authentication Policy Contract tab on the Authentication Policy Mapping page](_images/eca1621444452387.png)

      2. On the **Authentication Policy Contract** tab, click **Manage Policy Contracts**.

      The **Policy Contracts** page opens.

      ![Screen capture showing the Policy Contracts page](_images/cpe1621444671094.png)

      1. Click **Create New Contract**.

    The **Authentication Policy Contract** page opens.

    ![Screen capture showing the Contract Info tab on the Authentication Policy Contract page](_images/gsq1621444842743.png)

    1. On the **Contract Info** tab, in the **Contract Name**field, enter a name. Click **Next**.

    2. On the **Contract Attributes** tab, click **Next**.

    3. On the **Summary** tab, click **Save**.

    4. Click **Done** to return to the **Authentication Policy Mapping** page.

14. Map the authentication policy:

    1. On the **Authentication Policy Contract** tab, in the **Authentication Policy Contract** list, select the desired policy contract. Click **Next**.

    2. On the **Mapping Method** tab, click **Next**.

    3. On the **Attribute Contract Fulfillment** tab, in the **Source** list, select an option.

    4. In the **Value** field, enter a value.

    5. Click **Next**.

    6. On the **Issuance Criteria** tab, click **Next**.

    7. On the **Summary** tab, click **Done** to return to the **Assertion Creation** page.

    8. On the **Authentication Source Mapping** tab, click **Next**.

    9. On the **Summary** tab, click **Done** to return to the **Browser SSO** page.

15. Configure the protocol settings:

    1. On the **Assertion Creation** tab, click **Next**.

    2. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

       ### Result:

       A new **Protocol Settings** page opens.

       ![Screen capture showing the Assertion Customer Service URL tab on the Protocol Settings page](_images/zdc1621445259348.png)

    3. On the **Assertion Consumer Service URL** tab, enter the values as described in the following table.

       | Value        | Entry                                                                                                                                                                              |
       | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       | Index        | `0`                                                                                                                                                                                |
       | Binding      | `POST`                                                                                                                                                                             |
       | Endpoint URL | * For PVWA version 9, enter `https://<your PVWA address>/passwordvault/auth/saml/`.

       * For PVWA version 10, enter `https://<your PVWA address>/passwordvault/api/auth/saml/logon`. |

    4. To set a particular assertion consumer URL as the default, select the **Default** checkbox in the applicable row and click **Add**. Click **Next**.

    5. On the **Allowable SAML Bindings** tab, clear the **Artifact** and **SOAP** checkboxes. Click **Next**.

    6. On the **Signature Policy** tab, make sure that all the checkboxes are cleared. Click **Next**.

       |   |                                         |
       | - | --------------------------------------- |
       |   | By default, no checkboxes are selected. |

    7. On the **Encryption Policy** tab,verify the **None** is selected. Click **Next**.

    8. On the **Summary** tab, click **Done** to return to the **Browser SSO** page.

    9. On the **Protocol Settings** tab, click **Next**.

    10. On the **Summary** tab, click **Done** to return to the **SP Connection** page.

16. On the **Browser SSO** tab, click **Next**.

17. Complete the credentials configuration:

    1. On the **Credentials** tab, click **Configure Credentials**.

       ### Result:

       The **Credentials** page opens.

       ![Screen capture showing the Digital Signature Settings tab on the Credentials window](_images/sma1621445724114.png)

    2. In the **Signing Certificate** list, select the option to use for CyberArk (RSA SAH256).

       |   |                                                                          |
       | - | ------------------------------------------------------------------------ |
       |   | This certificate is provided to CyberArk in the SAML validation process. |

    3. Click **Next**.

    4. On the **Summary** tab, click **Done** to return to the **SP Connection** page.

    5. On the **Credentials** tab, click **Next**.

18. On the **Activation & Summary** tab, from the **SSO Application Endpoint** field, copy the IdP-initiated URL.

19. Click **Save**.

---

---
title: Configuring a PingOne for Enterprise authentication policy for PingID MFA using CyberArk PVWA
description: For CyberArk and Ping Identity best practices, deploy multi-factor authentication (MFA) for all single sign-on (SSO) requests to the CyberArk Password Vault Web Access (PVWA).
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_integrate_cyberark_sso_authn_p14e_pid
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_integrate_cyberark_sso_authn_p14e_pid.html
revdate: April 29, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  resultpingid-mfa-is-enabled-for-saml-based-sso-authentication-to-the-cyberark-pvwa: Result:PingID MFA is enabled for SAML-based SSO authentication to the CyberArk PVWA.
---

# Configuring a PingOne for Enterprise authentication policy for PingID MFA using CyberArk PVWA

For CyberArk and Ping Identity best practices, deploy multi-factor authentication (MFA) for all single sign-on (SSO) requests to the CyberArk Password Vault Web Access (PVWA).

## About this task

Configure the PingOne for Enterprise authentication policy to invoke PingID MFA.

## Steps

1. Go to **Setup → Authentication Policy**.

2. In the **Authentication Providers** section, select the **Enable authentication policy** checkbox.

3. In the **Authentication Policy Context** section, in the **Apply on application launch** section, select the applicable CyberArk application checkboxes.

   ### Result:PingID MFA is enabled for SAML-based SSO authentication to the CyberArk PVWA.

---

---
title: Configuring a PingOne for Enterprise SAML Connection for CyberArk PVWA
description: Set up SAML using PingOne for Enterprise for CyberArk Password Vault Web Access (PVWA).
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_integrate_cyberark_sso_authn_p14e_saml
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_integrate_cyberark_sso_authn_p14e_saml.html
revdate: April 29, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Configuring a PingOne for Enterprise SAML Connection for CyberArk PVWA

Set up SAML using PingOne for Enterprise for CyberArk Password Vault Web Access (PVWA).

## Before you begin

You must have the following information from your CyberArk and PingID environments to configure a SAML connection in PingFederate or PingOne for Enterprise:

* CyberArk's SAML Entity ID (Audience Value).

  |   |                                                                               |
  | - | ----------------------------------------------------------------------------- |
  |   | In the step-by-step SAML configuration, the value of `PasswordVault` is used. |

* CyberArk's Assertion Consumer Service (ACS) URL (POST Method). In this step-by-step SAML configuration example, the following values are used:

  * `https://components.cyberark.local/PasswordVault/auth/saml/` for PVWA v9

  * `https://components.cyberark.local/PasswordVault/api/auth/saml/logon` for PVWA v10

* A PingID registered account.

* The PingID properties file. For more information, see [Managing the PingID properties file](https://docs.pingidentity.com/pingid/pingid_integrations/pid_managing_pid_properties_file.html).

## Steps

1. Go to **Applications → My Applications → SAML**.

2. In the **Add Application** list, select **New SAML Application** to open the **New Application** window configuration.

3. In the **Application Details** workflow:

   1. Complete the **Application Name**, **Application Description**, **Category**, and **Graphics** fields.

   2. Click **Continue to Next Step**.

4. In the **Application Configuration** workflow:

   1. Click **I have the SAML configuration**.

   2. Enter the **Assertion Consumer Service (ACS)** value.

   3. Enter the **Entity ID** value.

   4. Click **Continue to Next Step**.

5. In the **SSO Attribute Mapping** workflow:

   1. Enter the **Identity Bridge Attribute or Literal Value** value.

      |   |                                                         |
      | - | ------------------------------------------------------- |
      |   | This is the user value that identifies a CyberArk user. |

   2. Click **Save & Publish**.

---

---
title: Configuring a SAML Integration with PingFederate in NGFW
description: Configure the SAML IdP server profile in NGFW.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_sso_globalprotect_vpn_pf_saml_ngfw
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_sso_globalprotect_vpn_pf_saml_ngfw.html
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Configuring a SAML Integration with PingFederate in NGFW

## Steps

1. Configure the SAML IdP server profile in NGFW.

   1. Sign on to Palo Alto Networks NGFW as an administrator, and then go to the **Device** tab.

   2. To import the metadata from PingFederate, go to **Server Profiles → SAML Identity Provider**, and then click **Import**.

   3. Enter a name in the **Profile Name** field, and then click **Browse** and select the `metadata.xml` file from step 7 of [Exporting the SAML Metadata from PingFederate](htg_config_sso_globalprotect_vpn_pf_export_saml_metadata.html).

      ![A screen capture of the SAML Identity Provider Server Profile Import window in Palo Alto NGFW.](_images/jhe1593476209245.png)

   4. **Optional:** If you are using a self-signed certificate in PingFederate, clear the **Validate Identity Provider Certificate** checkbox.

      ![A screen capture of the SAML Identity Provider Server Profile Import window in Palo Alto NGFW.](_images/uen1597963918494.png)

   5. Click **OK**.

   6. Click on your newly-created profile to open it.

   7. Select the **Post** checkbox for both **SAML HTTP Binding for SSO Requests to IDP** and **SAML HTTP Binding for SLO Requests to IDP**.

      ![A screen capture of the SAML Identity Provider Server Profile window in Palo Alto NGFW.](_images/xoo1597964619772.png)

   8. **Optional:** Adjust the clock skew in the **Maximum Clock Skew (seconds)** field.

   9. Click **OK**.

2. Create the authentication profile in NGFW.

   1. In Palo Alto Networks NGFW, go to the **Device** tab, and then click **Authentication Profile**.

   2. Click **Add**, and enter a profile name in the **Name** field.

   3. From the **Type** list, select **SAML**.

   4. From the **IdP Server Profile** list, select the SAML profile.

   5. From the **Certificate for Signing Requests** list, select the certificate of your GlobalProtect portal that you have created prior to this configuration. This will be used to sign the SAML message to the IdP.

   6. From the **Certificate Profile** list, select the certificate profile that you have created prior to this configuration.

      |   |                                                                                                                                                 |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | When using a CA-signed certificate in PingFederate, import the root CA in **Device → Certificates**, and include it in the certificate profile. |

      ![A screen capture of the Authentication Profile window in Palo Alto NGFW.](_images/hdr1593539204670.png)

      |   |                                                                                                                            |
      | - | -------------------------------------------------------------------------------------------------------------------------- |
      |   | If you want to add multi-factor authentication (MFA), we recommend adding it from the PingFederate administrative console. |

   7. Go to the **Advanced** tab, and then click **Add**.

   8. Select the groups that you want to be included in this Authentication Profile, and then click **OK**.

      ![A screen capture of the Authentication window in Palo Alto NGFW.](_images/zwo1593539719142.png)

3. Add the authentication profile to the GlobalProtect Portal.

   1. In Palo Alto Networks NGFW, go to **Network → GlobalProtect → Portals**, and then select the portal that you want to configure.

      |   |                                                                                                                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | For information on creating a portal, see [Set Up Access to the GlobalProtect Portal](https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/globalprotect-portals/set-up-access-to-the-globalprotect-portal). |

   2. Under Server Authentication, select the ssl service profile to the portal.

   3. Under Client Authentication, click **Add**.

   4. In the **Client Authentication** window, enter a name in the **Name** field. From the **Authentication Profile** list, select the authentication profile.

      ![A screen capture of the Client Authentication window in Palo Alto NGFW.](_images/xej1593540104445.png)

   5. **Optional:** From the **Allow Authentication with User Credentials OR Client Certificate** list, select **Yes**.

   6. Click **OK**.

   7. Go to the **Agent** tab and set the trusted root CA.

   8. Under Agent, click **Add**.

   9. On the **Authentication** tab, enter a name in the **Name** field. From the **Save User Credentials** list, select **Save Username Only**.

      ![A screen capture of the Configs window in Palo Alto NGFW.](_images/fts1593540204970.png)

   10. Go to the **External** tab. Under External Gateways, click **Add**.

   11. Enter a name in the **Name** field, and then enter the FQDN or IP address for the agent.

       ![A screen capture of the External Gateway window in Palo Alto NGFW.](_images/tjs1593540477645.png)

   12. Go to the **App** tab and review your configuration. Make any changes if required, and then click **OK**.

       |   |                                                                                                                                                                                                                                        |
       | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | Make sure the Gateway is configured. For more information, see [Configure a GlobalProtect Gateway](https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/globalprotect-gateways/configure-a-globalprotect-gateway). |

4. Export the metadata file from NGFW.

   1. Click the **Metadata** link of the authentication profile.

      ![A screen capture showing the Metadata link alongside the authentication profile.](_images/ars1593541453709.png)

   2. From the **Service** list, select **global-protect**.

   3. From the **Virtual System** list, select the virtual system.

   4. In the **IP or Hostname** field, select the URL of your GlobalProtect portal, and then click **OK**.

      ![A screen capture of the SAML Metadata Export window in Palo Alto NGFW.](_images/qpb1593541555986.png)

---

---
title: Configuring a trusted certificate in PingDirectory
description: Configure a trusted certificate using components of PingDirectory such as the config directory and the dsconfig utility.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_sailpoint_identityiq_pd_pf_ldaps_cert
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_sailpoint_identityiq_pd_pf_ldaps_cert.html
revdate: May 1, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Configuring a trusted certificate in PingDirectory

Configure a trusted certificate using components of PingDirectory such as the `config` directory and the `dsconfig` utility.

## About this task

To configure a trusted certificate in PingDirectory, you must replace the default self-signed certificate in the keystore with the trusted certificate. You must ensure that the referenced certificate files are in PEM certificate format.

## Steps

1. On the PingDirectory server in the installed directory, execute the following command.

   ```
   bin/manage-certificates change-certificate-alias \
   > --keystore config/keystore \
   > --keystore-password-file config/keystore.pin \
   > --current-alias server-cert \
   > --new-alias server-cert-prev
   # Initializing the server's encryption framework...
   Successfully changed the alias from 'server-cert' to 'server-cert-prev'.
   ```

2. Import the new trusted certificate to the keystore with the server-cert alias.

   ```
   bin/manage-certificates import-certificate \
   > --keystore config/keystore \
   > --keystore-password-file config/keystore.pin \
   > --alias server-cert \
   > --private-key-file demo.ping-eng.key \
   > --certificate-file demo.ping-eng.pem \
   > --certificate-file intermediate.crt
   # Initializing the server's encryption framework...

   The following certificate chain will be imported into the keystore, along with
   a private key, into alias 'server-cert':

   < Certificate Displayed Here >

   Do you want to import this certificate chain into the keystore? yes
   Successfully imported the certificate chain and its associated private key.
   ```

## Result

The trusted certificate is installed for use by the PingDirectory LDAPS Listener. IdentityIQ can now connect to PingDirectory over LDAPS.

---

---
title: Configuring authentication request signing in PingOne for Enterprise
description: For service provider (SP)-initiated single sign-on (SSO), your identity provider (IdP) or company policy might require signing the SAML authentication request.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_authn_req_sign_p14e
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_authn_req_sign_p14e.html
revdate: February 16, 2022
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
---

# Configuring authentication request signing in PingOne for Enterprise

For service provider (SP)-initiated single sign-on (SSO), your identity provider (IdP) or company policy might require signing the SAML authentication request.

## Before you begin

* Ensure that you have internet access.

* If you do not already have a PingOne for Enterprise account, [create an account](https://admin.pingone.com/web-portal/register).

## Steps

1. Sign in to the PingOne for Enterprise [admin portal](https://admin.pingone.com/web-portal/login).

2. Click **Setup**.

3. Click the **Pencil** ([icon: pencil, set=fa]) icon.

4. Select **PingFederate**. Click **Next.**

5. If PingFederate is already installed:

   1. Click **Yes**, then click **Next**.

   2. Copy the provided activation key into PingFederate Bridge when prompted.

6. If PingFederate is not installed:

   1. Click **No**, then click **Next**.

   2. Click the appropriate server platform.

   3. Download and install PingFederate Bridge, then click **Next**.

   4. Copy the provided activation key into PingFederate Bridge when prompted.

      If PingOne for Enterprise is configured with PingFederate version 8.0 or later, no changes in PingOne for Enterprise are necessary.

      |   |                                                                                                                                                                                           |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If PingFederate is set to **Require AuthN Requests To be Signed When Received via The Post or Redirect Bindings**, PingOne for Enterprise automatically signs the authentication request. |

7. If PingOne for Enterprise is configured with custom SAML:

   1. Select the **Sign AuthnRequest From PingOne** checkbox. Click **Next**.

   2. Click **Manually Enter Your IDP Connection Information**. Click **Save**.

## Result

PingOne for Enterprise will sign authentication requests during the SP-initiated SSO process. The verification certificate is inside the PingOne for Enterprise metadata file, and gets loaded into the SAML product when the metadata is uploaded for configuration.

---

---
title: Configuring federation with SharePoint server
description: Create a WS-Federation connection, export the signing certificate, add a trusted identity provider to the SharePoint server, and assign the identity provider to the web application.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_fed_sharepoint
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_fed_sharepoint.html
revdate: July 18, 2022
page_aliases: ["single_sign-on_use_cases:htg_config_fed_sharepoint_wsfed_pf.adoc", "single_sign-on_use_cases:htg_config_fed_sharepoint_signing_cert.adoc", "single_sign-on_use_cases:htg_config_fed_sharepoint_trusted_ip.adoc", "single_sign-on_use_cases:htg_config_fed_sharepoint_trusted_ip_assign_web_app.adoc", "single_sign-on_use_cases:htg_config_fed_sharepoint_more_config.adoc"]
section_ids:
  component: Component
  creating-ws-federation-connection-on-the-pingfederate-server: Creating WS-Federation connection on the PingFederate server
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  result: Result:
  exporting-the-signing-certificate: Exporting the signing certificate
  steps-2: Steps
  adding-a-trusted-identity-provider-to-the-sharepoint-server: Adding a trusted identity provider to the SharePoint server
  steps-3: Steps
  assigning-the-created-pingfederate-trusted-identity-provider-to-the-web-application: Assigning the created PingFederate trusted identity provider to the web application
  steps-4: Steps
  enabling-additional-configuration-options: Enabling additional configuration options
  steps-5: Steps
---

# Configuring federation with SharePoint server

Create a WS-Federation connection, export the signing certificate, add a trusted identity provider to the SharePoint server, and assign the identity provider to the web application.

This document describes how to configure a WS-Federation connection on the PingFederate server to integrate with SharePoint Server 2013 or SharePoint Server 2016.

## Component

PingFederate 9.3

## Creating WS-Federation connection on the PingFederate server

Set up a WS-Federation connection with PingFederate to establish federation with the SharePoint server.

### Before you begin

* Have a fully created and functional Web Application with federated authentication.

### Steps

1. Open the PingFederate Admin console.

2. Go to **System → Server → Protocol Settings**.

3. On the **Roles & Protocols** tab, select the **Enable Service Provider (SP) Role and Support the Following**checkbox, and then select the **WS-Federation** checkbox below. Click **Save**.

4. Go to **Identity Provider → SP Connections**. Click **Create New**.

5. On the **Connection Template** tab, click **Do Not Use a Template for This Connection**. Click **Next**.

6. On the **Connection Type** tab, select the **Browser SSO Profiles** checkbox.

   1. From the **Protocol** list, select **WS-Federation**.

   2. From the **WS-Federation Token Type** list, select **SAML 1.1**. Click **Next**.

      ![The Connection Type tab of the admin console. The connection template enables browser SSO profiles, WS-Federation protocol, and SAML 1.1 token type.](_images/fpo1577738746206.png)

7. On the **Connection Options** tab, keep the default settings. Click **Next**.

8. Complete the **General Info** tab.

   ![The General Info tab of the admin console SP connection configuration. Information filled in for the Connection ID and Connection Name fields.](_images/jmg1577738870018.png)

   1. In the **Partner's Realm (Connection ID)** field, enter the partner's unique connection identifier.

   2. In the **Connection Name** field, enter a name for the connection. Click **Next**.

      |   |                                                |
      | - | ---------------------------------------------- |
      |   | The Partner's Realm can be an arbitrary value. |

9. On the **Browser SSO** tab, click **Configure Browser SSO**.

10. Complete the **Assertion Lifetime** tab.

    1. In the **Minutes Before** field, enter `15`.

    2. In the **Minutes After** field, enter `15`. Click **Next**.

11. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

12. On the **Identity Mapping** tab, click **User Principal Name**. Click **Next**.

    |   |                                                                                                                             |
    | - | --------------------------------------------------------------------------------------------------------------------------- |
    |   | Configure the identity claim type on the SharePoint server for different attributes like email address, UPN or common name. |

13. Complete the **Attribute Contract** tab.

    1. In the **Extend the Contract** field, enter `upn`.

    2. From the **Attribute Name Format** list, select **http\://schemas.xmlsoap.org/ws/2005/05/identity/claims**.

    3. Click **Add**, and then click **Next**.

       |   |                                                                                                                                                       |
       | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | The attribute names are case-sensitive. They should match the claim type names configured for the Trusted Identity Provider on the SharePoint server. |

14. On the **Authentication Source Mapping** tab, add a mapping of your choice. Choose one of the following options.

    #### Choose from:

    * **Map New Adapter Instance**

    * **Map New Authentication Policy**

15. Depending on your choice, from the **Authentication Policy Contract** list select an **authentication policy contract**, or from the **Adapter Instance** list select the **adapter instance**. Click **Next**.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you do not have an Authentication Policy Contract or an Adapter Instance created, click **Manage Authentication Policy Contracts** or **Manage Adapter Instance** and configure the authentication source mapping as needed.For more information, see [Policy contracts](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_policy_contracts.html) and [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html) in the PingFederate documentation. |

16. On the **Mapping Method** tab, select **Retrieve Additional Attributes From Multiple Data Stores Using One Mapping**.

    #### Result:

    This selection retrieves the UPN value from an LDAP Data Store.

17. On the **Attribute Sources & User Lookup** tab, click **Add Attribute Store** and select an existing data store under **Active Data Store** or create a new one.

    |   |                                                                                                                                                                                                                       |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | For more information, see [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html) in the PingFederate documentation. |

18. On the **LDAP Directory Search** tab, enter the base DN details in the **Base DN** field.

19. In the attribute list, add **userPrincipalName** to the list of attributes returned from search. Click **Next**.

20. In the **Filter**field, enter a name for the filter. Click **Next**.

21. Click **Done**.

22. On the **Attribute Contract Fulfillment** tab, select the attribute contract source from the **Source** list, and the value from the **Value** list for each attribute contract. Click **Next**.

    ![The Attribute Contract Fulfillment tab of the admin console, from configuring the SP connection.](_images/bma1577739622966.png)

23. If necessary, complete the **Issuance Criteria** tab. Click **Next**.

    |   |                                                            |
    | - | ---------------------------------------------------------- |
    |   | The **Issuance Criteria** tab is not required to continue. |

24. On the **Summary** tab, review the information and click **Done**.

25. On the **Authentication Source Mapping** tab, click **Next**.

26. On the **Summary** tab, click **Done**.

27. On the **Assertion Creation** tab, click **Next**.

28. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

29. On the **Service URL** tab, in the **Endpoint URL** field enter the **Endpoint URL**. Click **Next**.

    ![The SP connection configuration protocol settings summary.](_images/skp1577739742574.png)

    |   |                                                                                                                                                                                                               |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Construct the Endpoint URL by adding `/_trust/` at the end of the SharePoint Web Application URL. In order to support multiple web applications on the same connection, see Additional configuration options. |

30. On the **Summary** tab, click **Done**.

31. On the **Protocol Settings** tab, click **Next**.

32. On the **Summary** tab, click **Done**.

33. On the **Browser SSO** tab, click **Next**.

34. On the **Credentials** tab, click **Configure Credentials**.

    ![The admin console Summary tab for configuring the SP connection.](_images/tzl1577739817245.png)

35. On the **Digital Signature Settings** tab, from the **Signing Certificate**list, select your signing certificate.

36. From the **Signing Algorithm** list, select the **Signing Algorithm**. Click **Next**.

37. On the **Summary** tab, click **Done**.

38. On the **Credentials** tab, click **Next**.

39. On the **Activation & Summary** tab, review the connection settings and set the **Connection Status** to **Active**. Click **Save**.

## Exporting the signing certificate

Find and export the signing certificate created for the WS-Federation connection on the PingFederate server.

### Steps

1. In the PingFederate Admin Console, go to **Security → Certificate & Key Management → Signing & Decryption Keys & Certificates**.

2. In the row with the previously-created signing certificate for the WS-Federation connection, click **Select Action**.

3. Click **Export**.

4. On the **Export Certificate** tab, click **Certificate Only**. Click **Next**.

5. Verify the certificate is correct, and then click **Export**.

   |   |                                                                                  |
   | - | -------------------------------------------------------------------------------- |
   |   | A `.crt` file will be saved in the Downloads folder configured for your browser. |

## Adding a trusted identity provider to the SharePoint server

Run the following commands in the SharePoint Management Shell to add an identity provider.

### Steps

1. Open SharePoint Management Shell.

2. Update the following commands according to your environment and run them one by one. To run the commands as a PowerShell script, add them to a `.psl` file.

   ```
   #Path to the Signing Certificate exported from the PingFederate server.

   $certpath = "c:\<pf-cert-name>.crt"


    #Name the PingFederate will be represented within SharePoint as a Trusted Identity Provider (PingFederateSTS was used in this example).

   $stsname = "<PingFederate_Trusted_Identity_Provider_name>"

   #Description for PingFederate STS within SharePoint.

   $stsdesc = "PingFederate Claims Provider"


   #Entity ID of the SharePoint realm (in our example it is ektd:sp02).

   $stsrealm = "<SharePoint_Realm_Name>"


    #PingFederate WS-Federation Endpoint.

   $signinurl = "https://<PingFederate_host_name_or_FQDN>:<port_number>/idp/prp.wsf"


    #Importing PingFederate Certificate into SharePoint.

   $cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("$certpath")

   New-SPTrustedRootAuthority -Name "PingFederate Token Signing Cert" -Certificate $cert

   # Defining incoming Claim Types.
   # Note: It could be more than one incoming claim type specified here.

   $m1 = New-SPClaimTypeMapping -IncomingClaimType "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn" -IncomingClaimTypeDisplayName "UPN" -SameAsIncoming


   # Creating Trusted Identity Provider

   New-SPTrustedIdentityTokenIssuer -Name $stsname -Description $stsdesc -Realm $stsrealm -ImportTrustCertificate $cert -ClaimsMappings $m1 -SignInUrl $signinurl -IdentifierClaim $m1.InputClaimType
   ```

## Assigning the created PingFederate trusted identity provider to the web application

Assign the web application's authentication providers using the zone name, claims authentication types, and the sign in page redirect URL.

### Steps

1. Open SharePoint Central Administration console and go to **Application Management → Manage Web Applications**.

2. Select the Web Application, and then click **Authentication Providers**.

3. Click the desired **Zone** name.

4. To enable the PingFederateSTS trusted identity provider, go to **Claims Authentication Types**, and then select **PingFederateSTS**.

   ![Edit Authentication window in the administrative console.](_images/gxr1577729233864.png)

5. Go to **Sign In Page URL**, and then click **Custom Sign In Page**.

6. In the **Custom Sign In Page** field, enter `/_trust/?trust=<PingFederate_Trusted_Identity_Provider_name>`.

   ![Sign In Page URL step in the administrative console.](_images/nac1577734894303.png)

   |   |                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To automatically redirect users to PingFederate for authentication when other authentication providers are configured, you must enter a destination for Sign In page redirection. |

7. Save changes.

## Enabling additional configuration options

Use the same service endpoint connection to service all of the web applications hosted on SharePoint Server.

### Steps

1. Open the SharePoint Management Shell.

2. To enable the `wreply` parameter for the Trusted Identity Provider, run the following commands.

   ```shell
   $tit = Get-SPTrustedIdentityTokenIssuer
    <PingFederate_Trusted_Identity_Provider_Name>
   $tit.UseWReplyParameter = $true
   $tit.Update()
   ```

3. Configure Valid Domain Names.

   1. In the PingFederate Admin console, open the connection for your SharePoint server.

   2. Go to **Protocol Settings → Service URL**.

   3. In the **Valid Domain Name** field, enter the domain name.

      |   |                                                                                                                                                                                                                                                                                                                   |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you have several web applications with a common domain name, such as*sales.pingdemo.com* or *support.pingdemo.com*, and if you require extra security, add them to the list. Otherwise, to cover these and future URLs with a similar format, add the domain name with a leading wildcard (*\*.pingdemo.com*). |

   4. Select the **Require HTTPS** and **Allow Any Query/Fragment** checkboxes. Click **Add**.

   5. Click **Save**.

---

---
title: Configuring IdentityIQ for SAML-based SSO
description: Use IdentityIQ's settings to configure SAML-based single sign-on (SSO).
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_sailpoint_identityiq_pd_pf_saml_identityiq
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_sailpoint_identityiq_pd_pf_saml_identityiq.html
revdate: May 1, 2024
section_ids:
  steps: Steps
---

# Configuring IdentityIQ for SAML-based SSO

Use IdentityIQ's settings to configure SAML-based single sign-on (SSO).

## Steps

1. From the IdentityIQ Administration console settings menu, select **Global Settings**.

![Screenshot of IdentityIQ window showing the location of Global Settings in the menu beneath the wrench icon.](_images/lus1584135700663.png)

1. From the **Global Settings** menu, select **Login Configuration**.

2. Click the **SSO Configuration** tab and select the **Enable SAML-based single sign-on (SSO)** checkbox.

3. Enter the SAML-based SSO settings.

+\[caption=] .Identity Provider Settings

| Field                    | Description                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------ |
| EntityID / Issuer        | The PingFederate SAML 2.0 Entity ID or Virtual Server ID.                                        |
| SSO Login URL            | The PingFederate IdP SSO endpoint. The default value is https\://*\<domain>*:9031/idp/SSO.saml2. |
| Public X.509 Certificate | The public certificate used in the PingFederate IdentityIQ SP connection                         |

+\[caption=] .SP Provider (IdentityIQ) Settings

| Field                 | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| EntityID / Issuer     | The Partner's IdentityIQ/Connection ID setup in the PingFederate SP.      |
| SAML URL (ACS)        | The IdentityIQ application URL, /identityiq/home.jsf.                     |
| SAML Binding          | The HTTP method configured in the PingFederate SP connection.             |
| SAML Name ID Format   | The SAML Name ID Format configured in the PingFederate SP connection.     |
| SAML Correlation Rule | The correlation rule in IdentityIQ. The default value is IdentityNowSAML. |

1. Click **Save**.

   |   |                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | After configuration, the default IdentityIQ login page redirects to the PingFederate identity provider (IdP). If you are required to authenticate to IdentityIQ, use the following URL: https\://*\<domain>*/identityiq/login.jsf?prompt=true. |

---

---
title: Configuring PingOne for Enterprise SSO with PingFederate Bridge as the identity repository
description: To enable PingOne for Enterprise single sign-on (SSO) using PingFederate Bridge as a new identity repository, use the PingFederate administrative console and the PingOne for Enterprise admin portal. To integrate PingOne for Enterprise SSO with an existing PingFederate configuration, see Connecting to PingOne for Enterprise after initial setup.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_p14e_pfb_identity_repository
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_p14e_pfb_identity_repository.html
revdate: May 1, 2024
page_aliases: ["single_sign-on_use_cases:htg_config_p14e_pfb_identity_repository_p14e_portal.adoc", "single_sign-on_use_cases:htg_config_p14e_pfb_identity_repository_p14e_bridge.adoc", "single_sign-on_use_cases:htg_config_p14e_pfb_identity_repository_sso_bridge.adoc"]
section_ids:
  components: Components
  before-you-begin: Before you begin
  connecting-pingfederate-bridge-to-pingone-for-enterprise-through-the-pingone-for-enterprise-admin-portal: Connecting PingFederate Bridge to PingOne for Enterprise through the PingOne for Enterprise admin portal
  about-this-task: About this task
  steps: Steps
  result: Result:
  connecting-pingfederate-bridge-to-pingone-for-enterprise-through-pingfederate-bridge: Connecting PingFederate Bridge to PingOne for Enterprise through PingFederate Bridge
  about-this-task-2: About this task
  steps-2: Steps
  result-2: Result:
  result-3: Result:
  configuring-p1-sso-pf-bridge: Configuring PingOne for Enterprise SSO with PingFederate Bridge
  about-this-task-3: About this task
  steps-3: Steps
  result-4: Result
---

# Configuring PingOne for Enterprise SSO with PingFederate Bridge as the identity repository

To enable PingOne for Enterprise single sign-on (SSO) using PingFederate Bridge as a new identity repository, use the PingFederate administrative console and the PingOne for Enterprise admin portal. To integrate PingOne for Enterprise SSO with an existing PingFederate configuration, see [Connecting to PingOne for Enterprise after initial setup](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_connecttop1_connecttop1state.html).

## Components

* PingOne for Enterprise

* PingFederate Bridge (available through PingOne for Enterprise)

## Before you begin

You must have:

* A PingOne for Enterprise admin portal account

* An instance of PingFederate Bridge

## Connecting PingFederate Bridge to PingOne for Enterprise through the PingOne for Enterprise admin portal

Connect PingOne for Enterprise SSO to PingFederate Bridge through the PingOne for Enterprise admin portal.

### About this task

You can also connect PingOne for Enterprise SSO to PingFederate Bridge through PingFederate Bridge. To connect to PingOne for Enterprise SSO through the PingOne for Enterprise admin portal:

### Steps

1. In the PingOne for Enterprise admin portal, click **Setup**.

2. On the **Identity Repository** tab, click **Connect to an Identity Repository**.

   |   |                                                                                                                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you have previously configured an identity repository, **Change Identity Repository** appears. Contact support about changing your identity repository or making changes to your existing PingFederate identity repository configuration because making changes affects your PingOne for Enterprise configuration. |

3. From the **Connect to an Identity Repository** menu, select **PingFederate**. Click **Next**.

4. Select **No**, and click **Next**.

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | To integrate with an existing PingFederate implementation, see PingOne for Enterprise. |

5. To choose your server platform, follow the on-screen instructions.

6. To download PingFederate Bridge, follow the on-screen instructions.

7. To install and configure PingFederate Bridge, follow the on-screen instructions.

8. In the PingFederate administrative console, review the license agreement. Click **Accept**.

9. In the PingOne for Enterprise admin portal, from the **Complete Quick Start** section, copy the activation key.

   ![Screen capture of the Complete Quick Start section. The Activation Key field is highlighted with a red box. Below the activation key field reads: To connect to your account, copy this unique activation key into when prompted. This is a single-use activation key. A new key will be generated for each session.](../_images/ebu1602608416395.png)

10. In the PingFederate administrative console, click **Yes, Connect to PingOne for Enterprise**.

11. In the **Activation Key** field, paste the activation key you copied from the PingOne for Enterprise admin portal.

    ![Screen capture of the Yes, Connect to section. The Activation Key field is highlighted with a red box. Text reads To connect this node to your account, enter your activation key. A link below reads Sign on to PingOne to get your activation key.](_images/sxf1604599204570.png)

12. Click **Next**.

    #### Result:

    The PingFederate administrative console displays the **Identities** section.

13. Proceed to [Configuring PingOne for Enterprise SSO with PingFederate Bridge](#configuring-p1-sso-pf-bridge).

## Connecting PingFederate Bridge to PingOne for Enterprise through PingFederate Bridge

Connect PingOne for Enterprise SSO to PingFederate Bridge through PingFederate Bridge.

### About this task

You can also connect PingOne for Enterprise SSO to PingFederate Bridge through the PingOne for Enterprise admin portal. To connect to PingOne for Enterprise SSO through PingFederate Bridge:

### Steps

1. Install PingFederate from the [Ping Identity Downloads Page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. To start the PingFederate server in Linux, run the following script.

   ```
   <YOUR PING FEDERATE DIRECTORY>/pingfederate/bin/run.sh
   ```

   |   |                                                                 |
   | - | --------------------------------------------------------------- |
   |   | In Windows, the server starts automatically after installation. |

3. Open the PingFederate administrative console.

   1. Open a browser and enter `https://Your Server Domain:9999/pingfederate/app`.

      |   |                                                                  |
      | - | ---------------------------------------------------------------- |
      |   | *Your Server Domain* is your fully qualified domain name (FQDN). |

   2. To proceed, review the license agreement. Click **Accept**.

4. Click **Yes, Connect to PingOne for Enterprise**.

5. Click **Sign on to PingOne to get your activation key** and enter your credentials to sign on.

   ![A screen capture of the Yes, Connect to section. The link reading Sign on to PingOne to get your activation key is highlighted with a red box. Above the link the text reads To connect this node to your account, enter your activation key.](_images/dbj1604600235163.png)

   #### Result:

   The admin portal displays the activation key.

6. Copy the activation key from the PingOne for Enterprise admin portal to your clipboard.

   ![A screen capture of the PingOne admin portal Activation Key field. The field is highlighted with a red box and contains sample key text.](_images/usu1604601270700.png)

7. In the PingFederate administrative console, in the **Activation Key** field, paste the key value.

   ![Screen capture of the Yes, Connect to section. The Activation Key field is highlighted with a red box. Text reads To connect this node to your account, enter your activation key. A link below reads Sign on to PingOne to get your activation key.](_images/sxf1604599204570.png)

8. Click **Next**.

   #### Result:

   The PingFederate administrative console displays the **Identities** section.

9. Proceed to [Configuring PingOne for Enterprise SSO with PingFederate Bridge](#configuring-p1-sso-pf-bridge).

## Configuring PingOne for Enterprise SSO with PingFederate Bridge

### About this task

To configure PingOne for Enterprise SSO with PingFederate Bridge as the identity repository:

### Steps

1. From the PingFederate Bridge administrative console **Identities** section, select **Yes, Connect a Directory Server**.

2. Enter information in the fields that is appropriate for your directory server.

   | Field                  | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
   | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Directory Type**     | Select the type of directory server from the list.                                                                                                                                                                                                                                                                                                                                                                  |
   | **Data Store Name**    | Enter the name of the datastore.                                                                                                                                                                                                                                                                                                                                                                                    |
   | **Hostname**           | Enter the fully qualified domain name (FQDN) for your directory server.                                                                                                                                                                                                                                                                                                                                             |
   | **Service Account DN** | Enter the distinguished name (DN) of the service account that PingFederate Bridge can use to communicate with the directory server.                                                                                                                                                                                                                                                                                 |
   | **Password**           | Enter the password associated with the service account.                                                                                                                                                                                                                                                                                                                                                             |
   | **Search Base**        | Enter the DN of the location in the directory where PingFederate Bridge begins its datastore queries.                                                                                                                                                                                                                                                                                                               |
   | **Search Filter**      | Specify how the username provided by a user at sign-on is mapped to an attribute in your directory.The default value is either `sAMAccountName=${username}` or `uid=${username}`, depending on the selected directory type.If you require a more advanced search filter, enter the value in the following format: `<Your attribute Name>=${username}`. For more information, consult your directory administrators. |

3. Click **Next**.

   |   |                                                                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your directory server is SSL-enabled and presents an untrusted certificate, PingFederate Bridge prompts you to upload the server's certificate. Click **Choose Certificate**, select the appropriate certificate, and click **Next**. |

4. In the **Use Cases** section, select the **PingOne SSO** checkbox, leaving the **Additional SSO Features** checkbox unselected. Click **Next**.

5. In the **Basic Information** section, in the **Base URL** field, enter `https://Your Server Domain:9031`.

   |   |                                    |
   | - | ---------------------------------- |
   |   | *Your Server Domain* is your FQDN. |

6. Click **Next**.

7. In the **Confirmation** section, review your configuration. To apply the configuration to PingFederate Bridge, click **Next**.

8. Click **Done**.

### Result

PingOne for Enterprise SSO, using PingFederate Bridge as the identity repository, is enabled for your PingOne for Enterprise applications.

---

---
title: Configuring SailPoint IdentityIQ with PingDirectory and PingFederate
description: This document describes how to integrate PingDirectory and PingFederate with SailPoint IdentityIQ.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_sailpoint_identityiq_pd_pf
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_sailpoint_identityiq_pd_pf.html
revdate: July 18, 2022
page_aliases: ["single_sign-on_use_cases:htg_config_sailpoint_identityiq_pd_pf_ldaps.adoc", "single_sign-on_use_cases:htg_config_sailpoint_identityiq_pd_pf_saml.adoc"]
section_ids:
  components: Components
  implementing-saml-based-sso-with-pingfederate-and-identityiq: Implementing SAML-based SSO with PingFederate and IdentityIQ
  implementing-an-ldaps-connection-with-pingdirectory-and-identityiq: Implementing an LDAPS connection with PingDirectory and IdentityIQ
---

# Configuring SailPoint IdentityIQ with PingDirectory and PingFederate

This document describes how to integrate PingDirectory and PingFederate with SailPoint IdentityIQ.

## Components

* PingDirectory 7.3

* PingFederate 9.2

## Implementing SAML-based SSO with PingFederate and IdentityIQ

Configure PingFederate and IdentityIQ to implement SAML-based single sign-on (SSO).

The IdentityIQ integration to PingFederate acting as the identity provider (IdP) for SSO authentication is a straightforward standards integration with the following caveats:

* The IdentityIQ application requires that the assertion portion inside the SAML response message is always signed.

* This system is tested with PingFederate 9.2 and higher and with IdentityIQ 7.3.

## Implementing an LDAPS connection with PingDirectory and IdentityIQ

Configure PingDirectory and IdentityIQ to implement an LDAP over SSL (LDAPS) connection from IdentityIQ to PingDirectory.

The IdentityIQ LDAPS integration to PingDirectory is a straightforward integration with the following caveats:

* PingDirectory must use a trusted certificate.

* IdentityIQ only supports the simple authentication bind mechanism.

---

---
title: Configuring SP-initiated SSO in PingOne for Enterprise
description: Configure the URL assigned to your application in PingOne for Enterprise to enable service provider (SP)-initiated SSO.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_sp_init_sso_p14e
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_sp_init_sso_p14e.html
revdate: February 16, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring SP-initiated SSO in PingOne for Enterprise

Configure the URL assigned to your application in PingOne for Enterprise to enable service provider (SP)-initiated SSO.

## Before you begin

Acquire a single sign-on (SSO) URL from your SP.

## About this task

When you enable connection to an SP in PingOne for Enterprise, an initial SSO URL is assigned to your application's icon within the PingOne dock. This URL does not work if your SP only supports SP-initiated SSO. To change your URL to enable it to work with these settings:

## Steps

1. Log in to PingOne for Enterprise at [admin.pingone.com](https://admin.pingone.com).

2. Go to **Applications → My Applications**.

3. Select your application and then click **Edit**. Click **Continue to Next Step**.

4. In **PingOne dock URL**, select the **Use Custom URL** checkbox and enter the SP-provided SSO URL. ![Example of 'Use Custom URL' field within the 'PingOne dock URL' section](_images/kqv1574198240003.png)

5. Continue through the remaining configuration screens, then click **Finish**.

---

---
title: Configuring SSO and SCIM for Uber for Business
description: To set up single sign-on (SSO) for administrators and coordinators in your organization, create an SP connection in PingFederate and then work with your sales manager or business API support agent to enable SSO.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_uber_sso_scim_overview
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_uber_sso_scim_overview.html
revdate: December 14, 2023
page_aliases: ["single_sign-on_use_cases:htg_uber_config_sso.adoc", "single_sign-on_use_cases:htg_uber_config_scim.adoc"]
section_ids:
  before-you-begin: Before you begin
  configuring-sso: Configuring SSO
  about-this-task: About this task
  steps: Steps
  result: Result:
  configuring-scim: Configuring SCIM
  about-this-task-2: About this task
  steps-2: Steps
---

# Configuring SSO and SCIM for Uber for Business

To set up single sign-on (SSO) for administrators and coordinators in your organization, create an SP connection in PingFederate and then work with your sales manager or business API support agent to enable SSO.

Then, configure PingFederate for System for Cross-domain Identity Management (SCIM) with the service provider (SP) connection that you created.

## Before you begin

Ensure that PingFederate is correctly installed and configured. For more information, see the following:

* [Installing PingFederate](https://docs.pingidentity.com/pingfederate/latest/installing_and_uninstalling_pingfederate/pf_installing_pf.html)

* [Setting up PingFederate](https://docs.pingidentity.com/pingfederate/latest/getting_started_with_pingfederate/pf_setting_up_pf.html)

* [Specifying federation information](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_federationinfostate.html)

  |   |                                                                                                                                                    |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Ensure that the SAML 2.0 entity ID is specified. This ID is usually defined as an organization's URL or a DNS address, such as `pingidentity.com`. |

* [Manage digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

* [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html)

* [Password credential validators](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_passwordcredentialvalidatortasklet_passwordcredentialvalidatormgmtstate.html)

* [HTML Form Adapter](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_html_form_adapt.html)

## Configuring SSO

### About this task

Start by creating an SP connection in PingFederate.

### Steps

1. Go to **Applications → SP Connections** and click **Create Connection**.

2. Ensure that **Do not use a template for this connection** is selected. Click **Next**.

3. On the **Connection Template** tab, select **Browser SSO Profiles** and the **SAML 2.0** protocol. Click **Next**.

4. On the **Connection Options** tab, ensure that **Browser SSO** is selected. Click **Next**.

5. On the **Import Metadata** tab, ensure that **None** is selected. Click **Next**.

6. On the **General Info** tab, in the **Partner's Entity ID** and **Connection Name** fields, enter `uber.com`. Click **Next**.

7. On the **Browser SSO** tab, click **Configure Browser SSO**.

   1. On the **SAML Profiles** tab, select both **IdP-Initiated SSO** and **SP-Initiated SSO**. Click **Next**.

   2. On the **Assertion Lifetime** tab, specify the number of minutes for which the assertion will be valid before and after it's issued. Click **Next**.

   3. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

      1. On the **Identity Mapping** tab, ensure that **Standard** is selected. Click **Next**.

      2. On the **Attribute Contract** tab, set **SAML\_SUBJECT** to `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`. Click **Next**.

   4. On the **Authentication Source Mapping** tab, select **Map New Adapter Instance**.

      1. On the **Adapter Instance** tab, click **Manage Adapter Instances** and then click **Create New Instance**.

      2. On the **Type** tab, enter a unique name and ID (with no spaces) for the adapter, select **HTML Form IdP Adapter** from the **Type** field. Click **Next**.

      3. On the **IdP Adapter** tab, click **Add a new row to Credential Validator**, select the type of validator that you use for your datastore from the list, and click **Update**. Click **Next** at the bottom of the page.

      4. Click **Next** on the **Extended Contract** tab.

      5. On the **Adapter Attributes** tab, in the **Pseudonym** column, select **username**. Click **Next**.

      6. On the **Adapter Contract Mapping** tab. Click **Next** and then click **Save** at the bottom of the page.

         The identity provider (IdP) adapter that you just created displays in the list of available adapters.

      7. Click **Done**.

   5. On the **Adapter Instance** tab, select the instance that you just created. Click **Next**.

      1. Ensure that the **Use Only the Adapter Contract Values in the SAML Assertion** option is selected. Click **Next**.

      2. On the **Attribute Contract Fulfillment** tab, in the **Source**list, select **Adapter**, and in the **Value** list, select **username**. Click **Next**.

      3. On the**Issuance Criteria** tab, click**Next**.

      4. On the **Summary** tab, click **Done**.

   6. On the **Authentication Source Mapping** tab, click **Next**.

   7. On the **Summary** tab, click **Done**.

   8. On the **Assertion Creation** tab, click **Next**.

   9. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

      1. In the **Binding** list, select **Post**.

      2. In the **Endpoint URL** field, enter `https://auth.uber.com/v2/saml/acs/`.

      3. Click **Add**. Click **Next**.

      4. On the **Allowable SAML Bindings** tab, deselect **Artifact** and **SOAP**. Click **Next**.

      5. On the **Signature Policy** tab and the **Encryption Policy** tab, click **Next**.

      6. On the **Summary** tab, click **Done**.

         You return to the **Browser** SSO tab.

8. Click **Next**.

9. On the **Credentials** tab, click **Configure Credentials** and select your signing certificate in the **Signing Certificate** list. Click **Next** and then click **Done**.

10. On the **Credentials** tab, click **Next**.

11. On the **Activation and Summary** tab, click **Save**.

    #### Result:

    The SP connection you just created displays in the list of available SP connections.

## Configuring SCIM

### About this task

Next, configure PingFederate for SCIM using the SP connection that you created:

### Steps

1. Download the SCIM Provisioner files and deploy them to your PingFederate directory.

   See [Deploying the integration files](https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_deploying_the_integration_files.html) for instructions.

2. In PingFederate, go to the **SP Connections** page.

3. Select the SP connection that you created for SSO and click the **Connection Type** tab.

4. Select the **Outbound Provisioning** option, then in the **Type**list, select **SCIM Connector**. Click **Next**.

5. Click **Next** until you reach the **Outbound Provisioning** tab. Click **Configure Provisioning**.

6. Create a SCIM app, obtain the SCIM Base URL, and enter it in the **SCIM URL** field.

   See the [Custom SCIM app](https://developer.uber.com/docs/scim/idp/custom) instructions in the Uber Developers Guide for details.

7. In the **Authentication Method** field, select **OAuth 2.0 Bearer Token**.

8. In the **Access Token** field, enter the access token.

   Generate this token from your app on developer.uber.com.

9. Click **Next**.

10. On the **Manage Channels** tab, create a new channel:

    1. In the **Channel Name**field, enter a unique name for the channel.

    2. In the **Source** list, select your datastore.

    3. In the **Source Location** field, enter the base DN (CN=Users, DC=domain, DC=com).

    4. In the **Filter** field, enter the filters that you want to use to provision users or groups. For example, you can enter `objectClass=user` to provision all users and `objectClass=groups` to provision all user groups.

    5. On the **Activation and Summary** tab, switch the channel to **Active**.

11. Enable SCIM for your organization account on the Uber platform.

    See [Onboarding to SCIM Provisioning](https://developer.uber.com/docs/scim/introduction) in the Uber Developers Guide for details.

---

---
title: Configuring SSO for GlobalProtect VPN with PingFederate
description: Next-Generation Firewall (NGFW) supports the ability to enable single sign-on (SSO) through the admin UI.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_sso_globalprotect_vpn_pf
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_sso_globalprotect_vpn_pf.html
revdate: November 10, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  exporting-the-saml-metadata-from-pingfederate: Exporting the SAML Metadata from PingFederate
  steps: Steps
  configuring-a-saml-integration-with-pingfederate-in-ngfw: Configuring a SAML Integration with PingFederate in NGFW
  steps-2: Steps
  importing-the-ngfw-metadata-into-pingfederate: Importing the NGFW Metadata into PingFederate
  steps-3: Steps
  troubleshooting: Troubleshooting
---

# Configuring SSO for GlobalProtect VPN with PingFederate

Next-Generation Firewall (NGFW) supports the ability to enable single sign-on (SSO) through the admin UI.

## Before you begin

* PingFederate is installed and configured.

* NGFW is installed and configured.

* You have a GlobalProtect portal certificate.

* You have a Certificate Profile.

* You have an identity provider (IdP) certificate signed by a certificate authority (CA), and trusted by the NGFW device (recommended).

## About this task

You can combine GlobalProtect VPN with PingFederate for SSO as illustrated in the following diagram.

![A flowchart showing the relationship between GlobalProtect, , and .](_images/gnx1571327130738.png)Flow diagram that links to three tasks: Export the SAML Metadata from PingFederate, Configure a SAML integration with PingFederate in NGFW, and Import the NGFW metadata into PingFederate

## Exporting the SAML Metadata from PingFederate

### Steps

1. Sign on to the PingFederate administrative console and go to **System → Protocol Metadata → Metadata Export**.

2. On the **Metadata Role** tab, select **I am the Identity Provider (IdP)**, and then click **Next**.

   ![A screen capture of the Metadata Role tab in the administrative console.](../_images/zbi1593474042547.png)

3. On the **Metadata Mode** tab, select **Select Information to Include in Metadata Manually**, and then click **Next**.

   ![A screen capture of the Metadata Mode tab in the administrative console.](../_images/pvo1593474233350.png)

4. On the **Protocol** tab, click **Next** until you reach the **Signing Key** tab, accepting the default values.

5. On the **Signing Key** tab, select an available signing key from the **Digital Signature Keys/Certs** list, and then click **Next**. If none are available, click **Manage Certificates** to create a signing key, and then follow the on-screen instructions.

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | Although you can use a self-signed certificate, a CA-signed certificate is recommended. |

   ![A screen capture of Signing Key tab in the administrative console.](../_images/sga1593474593063.png)

6. Click **Next** until you reach the **Export & Summary** tab, accepting the default values on the **Metadata Signing** and **XML Encryption Certificate** tabs.

7. On the **Export & Summary** tab, click **Export** and save the `metadata.xml` file. You will upload this file to Palo Alto Networks NGFW in the next step.

   ![A screen capture of the Export & Summary tab in the administrative console.](../_images/lfe1593474764679.png)

## Configuring a SAML Integration with PingFederate in NGFW

### Steps

1. Configure the SAML IdP server profile in NGFW.

   1. Sign on to Palo Alto Networks NGFW as an administrator, and then go to the **Device** tab.

   2. To import the metadata from PingFederate, go to **Server Profiles → SAML Identity Provider**, and then click **Import**.

   3. Enter a name in the **Profile Name** field, and then click **Browse** and select the `metadata.xml` file from step 7 of [Exporting the SAML Metadata from PingFederate](htg_config_sso_globalprotect_vpn_pf_export_saml_metadata.html).

      ![A screen capture of the SAML Identity Provider Server Profile Import window in Palo Alto NGFW.](_images/jhe1593476209245.png)

   4. **Optional:** If you are using a self-signed certificate in PingFederate, clear the **Validate Identity Provider Certificate** checkbox.

      ![A screen capture of the SAML Identity Provider Server Profile Import window in Palo Alto NGFW.](_images/uen1597963918494.png)

   5. Click **OK**.

   6. Click on your newly-created profile to open it.

   7. Select the **Post** checkbox for both **SAML HTTP Binding for SSO Requests to IDP** and **SAML HTTP Binding for SLO Requests to IDP**.

      ![A screen capture of the SAML Identity Provider Server Profile window in Palo Alto NGFW.](_images/xoo1597964619772.png)

   8. **Optional:** Adjust the clock skew in the **Maximum Clock Skew (seconds)** field.

   9. Click **OK**.

2. Create the authentication profile in NGFW.

   1. In Palo Alto Networks NGFW, go to the **Device** tab, and then click **Authentication Profile**.

   2. Click **Add**, and enter a profile name in the **Name** field.

   3. From the **Type** list, select **SAML**.

   4. From the **IdP Server Profile** list, select the SAML profile.

   5. From the **Certificate for Signing Requests** list, select the certificate of your GlobalProtect portal that you have created prior to this configuration. This will be used to sign the SAML message to the IdP.

   6. From the **Certificate Profile** list, select the certificate profile that you have created prior to this configuration.

      |   |                                                                                                                                                 |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | When using a CA-signed certificate in PingFederate, import the root CA in **Device → Certificates**, and include it in the certificate profile. |

      ![A screen capture of the Authentication Profile window in Palo Alto NGFW.](_images/hdr1593539204670.png)

      |   |                                                                                                                            |
      | - | -------------------------------------------------------------------------------------------------------------------------- |
      |   | If you want to add multi-factor authentication (MFA), we recommend adding it from the PingFederate administrative console. |

   7. Go to the **Advanced** tab, and then click **Add**.

   8. Select the groups that you want to be included in this Authentication Profile, and then click **OK**.

      ![A screen capture of the Authentication window in Palo Alto NGFW.](_images/zwo1593539719142.png)

3. Add the authentication profile to the GlobalProtect Portal.

   1. In Palo Alto Networks NGFW, go to **Network → GlobalProtect → Portals**, and then select the portal that you want to configure.

      |   |                                                                                                                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | For information on creating a portal, see [Set Up Access to the GlobalProtect Portal](https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/globalprotect-portals/set-up-access-to-the-globalprotect-portal). |

   2. Under Server Authentication, select the ssl service profile to the portal.

   3. Under Client Authentication, click **Add**.

   4. In the **Client Authentication** window, enter a name in the **Name** field. From the **Authentication Profile** list, select the authentication profile.

      ![A screen capture of the Client Authentication window in Palo Alto NGFW.](_images/xej1593540104445.png)

   5. **Optional:** From the **Allow Authentication with User Credentials OR Client Certificate** list, select **Yes**.

   6. Click **OK**.

   7. Go to the **Agent** tab and set the trusted root CA.

   8. Under Agent, click **Add**.

   9. On the **Authentication** tab, enter a name in the **Name** field. From the **Save User Credentials** list, select **Save Username Only**.

      ![A screen capture of the Configs window in Palo Alto NGFW.](_images/fts1593540204970.png)

   10. Go to the **External** tab. Under External Gateways, click **Add**.

   11. Enter a name in the **Name** field, and then enter the FQDN or IP address for the agent.

       ![A screen capture of the External Gateway window in Palo Alto NGFW.](_images/tjs1593540477645.png)

   12. Go to the **App** tab and review your configuration. Make any changes if required, and then click **OK**.

       |   |                                                                                                                                                                                                                                        |
       | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | Make sure the Gateway is configured. For more information, see [Configure a GlobalProtect Gateway](https://docs.paloaltonetworks.com/globalprotect/10-1/globalprotect-admin/globalprotect-gateways/configure-a-globalprotect-gateway). |

4. Export the metadata file from NGFW.

   1. Click the **Metadata** link of the authentication profile.

      ![A screen capture showing the Metadata link alongside the authentication profile.](_images/ars1593541453709.png)

   2. From the **Service** list, select **global-protect**.

   3. From the **Virtual System** list, select the virtual system.

   4. In the **IP or Hostname** field, select the URL of your GlobalProtect portal, and then click **OK**.

      ![A screen capture of the SAML Metadata Export window in Palo Alto NGFW.](_images/qpb1593541555986.png)

## Importing the NGFW Metadata into PingFederate

To complete the integration, import the metadata file from NGFW and finish the service provider (SP) configuration in PingFederate.

### Steps

1. Create an SP in PingFederate, and import the NGFW metadata file.

   1. In the PingFederate administrative console, go to **Applications → Integration → SP Connections**, and then click **Create Connection**.

      ![A screen capture of the SP Connections window in the administrative console.](_images/amu1593553427790.png)

   2. On the **Connection Template** tab, select **Do Not Use a Template for This Connection**, and then click **Next**.

   3. On the **Connection Type** tab, select the **Browser SSO Profiles** checkbox, and select **SAML 2.0** from the **Protocol** list. Click **Next**.

   4. On the **Connection Options** tab, accept the default election and click **Next**.

   5. On the **Import Metadata** tab, select the **File** checkbox and then click **Choose File**. Select the NGFW metadata file and then click **Next**.

      ![A screen capture of the Import Metadata tab in the administrative console.](_images/wsg1593553769958.png)

   6. On the **Metadata Summary** tab, ensure the imported **EntityID** field is correct, and then click **Next**.

   7. On the **General Info** tab, review the imported **Base URL** field, and then click **Next**.

      ![A screen capture of the General Info tab in the administrative console.](_images/gur1593556103752.png)

   8. On the **Browser SSO** tab, click **Configure Browser SSO**.

      ![A screen capture of the Browser SSO tab in the administrative console.](_images/tcx1593556313243.png)

   9. On the **SAML Profiles** tab, select the **SP-Initiated SSO** checkbox, and then click **Next**.

      ![A screen capture of the SAML Profiles tab in the administrative console.](_images/kfm1593556401432.png)

   10. On the **Assertion Lifetime** tab, accept the default values and click **Next**.

   11. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

       ![A screen capture of the Assertion Creation tab in the administrative console.](_images/mdn1593556618758.png)

   12. Click **Next** until you reach the **Authentication Source Mapping** tab, accepting the default values.

   13. On the **Authentication Source Mapping** tab, an Adapter Instance or Authentication Policy Contract must exist. Click **Map New Adapter Instance**.

       ![A screen capture of the Authentication Source Mapping tab in the administrative console.](_images/ghg1593556757925.png)

   14. On the **Adapter Instance** tab, select **HTML Form Adapter** from the **Adapter Instance** list, and then click **Next**.

       ![A screen capture of the Adapter Instance tab in the administrative console.](_images/ngd1593556824004.png)

   15. On the **Mapping Method** tab, accept the default values and click **Next**.

   16. On the **Attribute Contract Fulfillment** tab, select **Adapter** from the **Source** list and select **username** from the **Value** list. Click **Next**.

       ![A screen capture of the Attribute Contract Fulfillment tab in the administrative console.](_images/zrm1593556923492.png)

   17. Click **Next** and **Done** until you return to the **Protocol Settings** tab, accepting the default values. Click **Configure Protocol Settings**.

   18. On the **Assertion Consumer Service URL** tab, ensure that the Endpoint URL is correct, and then click **Next**.

       ![A screen capture of the Assertion Consumer Service URL tab in the administrative console.](_images/yfn1593557000819.png)

   19. On the **Allowable SAML Bindings** tab, select **POST** and then click **Next**.

       ![A screen capture of the Allowable SAML Bindings tab in the administrative console.](_images/fku1593557072875.png)

   20. Click **Next** and **Done** until you return to the **Credentials** tab. Click **Configure Credentials**.

       ![A screen capture of the Credentials tab in the administrative console.](_images/npa1593557141604.png)

   21. On the **Digital Signature Settings** tab, select a signing certificate from the **Signing Certificate** list. Click **Done**.

       ![A screen capture of the Digital Signature Settings tab in the administrative console.](_images/rlr1593557207609.png)

   22. On the **Credentials** tab, click **Next**.

   23. On the **Activation & Summary** tab, ensure your connection is enabled with the green toggle switch, and then click **Save**.

       ![A screen capture of the Activation & Summary tab in the administrative console.](_images/gud1593557327097.png)

### Troubleshooting

* For basic troubleshooting, see PingFederate [Troubleshooting](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_troubleshooting.html).

  Additional resources include:

  * [PingFederate discussion forum](https://support.pingidentity.com/s/topic/0TO1W000000Q9o7WAC/pingfederate)

  * [PingFederate docs](https://docs.pingidentity.com/pingfederate)

  * [Community discussion forums](https://support.pingidentity.com/s/community-home/)

  * Ping Identity [Support portal](https://support.pingidentity.com/s/)

* For user sign-on issues, identify whether the problem is on PingFederate or GlobalProtect.

  * Sign-on issues with PingFederate might be related to incorrect credentials. For more information, see your PingFederate logs.

  * If authentication completes successfully on PingFederate server and the SAML assertion is sent back to GlobalProtect:

    1. Check the Palo Alto Networks support logs.

    2. Check if the certificate is valid and trusted by the NGFW instance.

    3. Check the clock on both NGFW and PingFederate server, and the clock skew on the SAML Identity Provider Server Profile.

---

---
title: Configuring SSO for GlobalProtect VPN with PingOne for Enterprise
description: Next-Generation Firewall (NGFW) supports the ability to enable Single Sign-On (SSO) through the PingOne for Enterprise admin UI.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_sso_globalprotect_vpn_p14e
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_sso_globalprotect_vpn_p14e.html
revdate: February 16, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Configuring SSO for GlobalProtect VPN with PingOne for Enterprise

Next-Generation Firewall (NGFW) supports the ability to enable Single Sign-On (SSO) through the PingOne for Enterprise admin UI.

## Before you begin

* To ensure the integrity of messages processed in a SAML transaction, use digital certificates to cryptographically sign all messages. For guidelines on certificate usage, see [Configure SAML Authentication](https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/authentication/configure-saml-authentication.html) in the Palo Alto Networks documentation.

* You have an identity provider (IdP) certificate signed by a certificate authority (CA) and trusted by the NGFW device (recommended).

## About this task

You can combine GlobalProtect VPN with PingOne for Enterprise for SSO as shown in the following diagram.![A flow chart showing the relationship between the user, GlobalProtect, and PingOne.](_images/kod1574273989501.png)

## Steps

1. Create a standard security certificate for GlobalProtect to use.

   |   |                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | GlobalProtect requires a certificate from a Certificate Authority (CA) and cannot use a self-signed certificate. Ensure that you have a standard certificate. |

2. Download the GlobalProtect certificate.

   1. Log in to the NGFW admin portal.

   2. Go to **Device → Certificate Management → Certificates**, and select the certificate that you created in step 1.

   3. Click **Export Certificate**. From the **File Format** list, select `Base64 Encoded Certificate (PEM)`.

   4. Clear the **Export private key** checkbox, and then click **OK**.

      |   |                                                                                                                      |
      | - | -------------------------------------------------------------------------------------------------------------------- |
      |   | You will use the CN of the certificate for the assertion consumer service (ACS) endpoint and EntityID URL in step 3. |

3. In PingOne, set up the GlobalProtect application.

   1. Log in to PingOne.

   2. Go to **Applications → Application Catalog**, and search for GlobalProtect.

   3. Expand the Palo Alto Networks GlobalProtect entry with the black arrow. Click **Setup** and then click **Continue to Next Step**.

   4. In the **ACS URL** and **Entity ID** fields, replace *$\\{GlobalProtect Portal}* with the GlobalProtect FQDN or IP as shown.

      ### Example:

      ACS URL: `https://<FQDN or IP>:443/SAML20/SP/ACS`

      Entity ID: `https://<FQDN or IP>:443/SAML20/SP`

   5. Click **Browse** next to Primary Verification Certificate, and then select the GlobalProtect certificate that you downloaded from NGFW.

   Ensure that you:

   * Clear the **Encrypt Assertion** checkbox, and select the **Sign Assertion** checkbox.

   * Keep the signing algorithm as `RSA_SHA256`.

     |   |                                         |
     | - | --------------------------------------- |
     |   | Select **Force MFA** to use PingID MFA. |

     1. Click **Continue to Next Step**.

     2. In the **Attribute Mapping** window, set the value of the `username *` application attribute to `SAML_SUBJECT`, unless a different value is required. Click **Continue to Next Step**.

     3. **Optional:** On the **PingOne App Customization** page, change the application's icon, name, description, and category. Click **Continue to Next Step**.

     4. In the **Group Access** window, add the required user groups for VPN authentication, and then click **Continue to Next Step**.

        |   |                                                       |
        | - | ----------------------------------------------------- |
        |   | Exclude any group that should not have access to VPN. |

     5. If you choose to verify the user in NGFW under User Identification against your directory, ensure that PingOne for Enterprise is connected to the same directory.

     6. Click **Download** next to SAML Metadata, and then click **Finish**.

4. Import the PingOne for Enterprise SAML metadata into GlobalProtect.

   1. Log in as administrator to the NGFW admin portal.

   2. Go to **Device → Server Profile → SAML Identity Provider**, and then click **Import**.

   3. In the **Profile Name** field, enter a name for the profile.

   4. In the **Identity Provider Metadata** field, click **Browse** and import the metadata file that you downloaded from PingOne.

   5. **Optional:** If you are using a self-signed certificate, clear the **Validate Identity Provider Certificate** checkbox.

   6. **Optional:** Set the **Maximum Clock Skew**.

   7. Review your configuration and then click **OK**.

5. Create an authentication profile in GlobalProtect.

   1. On the **Device** page, go to **Authentication Profile**, and click **Add**.

   2. In the **Name** field, enter a name for the authentication profile.

   3. From the **Type** list, select `SAML`.

   4. In the**IDP Server Profile**, choose the SAML profile that you created in step 4.

   5. In the **Certificate for Signing Request** field, choose the certificate that you created for GlobalProtect. This is the same certificate that you imported into PingOne for Enterprise.

   6. In the **Certificate Profile** field, choose the certificate profile that you created for GlobalProtect. For more information, see [Configure a Certificate Profile](https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-admin/certificate-management/configure-a-certificate-profile.html) in the Palo Alto Networks documentation.

      |   |                                                                                                                                                          |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | When using a CA-signed certificate in PingOne for Enterprise, import the root CA in **Device → Certificates** and include it in the certificate profile. |

   7. Leave the **Username Attribute** field as `username`.

   8. Leave the **Factors** tab empty.

      |   |                                                                     |
      | - | ------------------------------------------------------------------- |
      |   | If you need to use MFA, you can force PingID MFA from PingFederate. |

      Your configuration should be similar to the following example.

      ![A screen capture of the Authentication Profile window in the NGFW admin portal.](_images/fql1571868589204.png)

   9. Go to the **Advanced** tab and choose the group to which this authentication profile applies.

   10. Confirm your configuration and then click **OK**.

6. Add the authentication profile to the GlobalProtect portal.

   For information on configuring a GP portal, see [Set up access to the GlobalProtect Portal](https://docs.paloaltonetworks.com/globalprotect/9-0/globalprotect-admin/globalprotect-portals/set-up-access-to-the-globalprotect-portal) in the Palo Alto Networks documentation.

   1. Go to **Network → GlobalProtect → Portals**, and choose the portal that you want to modify.

   2. Select **Authentication**, and choose the SSL service profile.

   3. On the **Client Authentication** tab, click **Add**.

   4. Enter a name for the client authentication profile, and select the authentication profile that you created in step 5.

   5. Confirm your configuration and then click **OK**.

      Your configuration should look similar to the following example.

      ![A screen capture of the Client Authentication window in the NGFW admin portal.](_images/xxt1571868962758.png)

7. Go to the **Agent** tab, and set the trusted root CA.

   1. On the **Agent** tab, click **Add**.

   2. On the **Authentication** tab, enter a name for the agent in the **Name** field.

   3. From the **Save User Credentials** menu, select **Save username only**.

      Your configuration should look similar to the following example.

      ![A screen capture of the Authentication tab in NGFW.](_images/tel1571927574689.png)

8. Add an external gateway to your GlobalProtect configuration.

   1. Go to the **External** tab, and under External Gateways click **Add**.

   2. Give the gateway a name, and set the FQDN or IP for the agent.

      Your configuration should look similar to the following example.

      ![A screen capture of the External Gateway window in NGFW.](_images/zpm1571928373673.png)

      |   |                                                                                                                                                                                                                                                                                                              |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Make sure that the Gateway is configured. For instructions on configuring a gateway, see [Configure a GlobalProtect Gateway](https://docs.paloaltonetworks.com/globalprotect/9-0/globalprotect-admin/globalprotect-gateways/configure-a-globalprotect-gateway.html) in the Palo Alto Networks documentation. |

9. Go to the **App** tab. Review the configuration and make any required changes, then click **OK**.

10. Click **Commit**.

---

---
title: Configuring the IdentityNow application for PingDirectory
description: Use the IdentityNow configuration functionality to establish a successful connection to PingDirectory.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_sailpoint_identityiq_pd_pf_ldaps_identitynow
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_sailpoint_identityiq_pd_pf_ldaps_identitynow.html
revdate: July 10, 2025
section_ids:
  steps: Steps
  example: Example:
---

# Configuring the IdentityNow application for PingDirectory

Use the IdentityNow configuration functionality to establish a successful connection to PingDirectory.

## Steps

1. Sign in to the IdentityNow Administrator interface.

2. Under the **Admin** tab, go to **Connections → Sources**.

3. Click the **+New** button.

4. In the window that appears, choose **SunOne** from the **Source Type** dropdown list, fill in the remaining fields with your information, and select **Direct Connection** for **Connection Type**. Click **Continue**. ![The Create New Source pop-up window with example values in its fields](_images/eej1590164597957.png)

5. Select a Virtual Appliance Cluster from those already configured for your organization. See the [SailPoint Virtual Appliance Reference Guide](https://community.sailpoint.com/t5/Connectors/Virtual-Appliance-Reference-Guide/ta-p/74641) for more details.

6. Enter the following connection details.

   1. In the **Connection Credentials** section, enter the PingDirectory administrator account information into the **Service Account** and **Password** fields.

   2. In the **Server Host** section, enter the hostname of the PingDirectory server in the **Hostname or IP Address** field.

   3. In the **Server Host** section, enter the PingDirectory configured LDAPS port 636 or 1636 in the **Port** field.

![The Config tab with sections and fields mentioned in step 6](_images/krh1590171864118.png)

1. Ensure the Account, Group and Group Member Search DNs are valid for the configured PingDirectory topology.

   ### Example:

   In the demo environment the following values were used.

   * Account Search DN: `ou=people,dc=example,dc=com`

   * Group Search DN: `ou=Groups,dc=example,dc=com`

   * Group Membership DN: `ou=Groups,dc=example,dc=com`

2. Under the **Connections** tab, enable the **Advanced Options** and select **Enable** in the **Use TLS** section and **Simple** in the **Authorization Type** section. ![The Connections tab with fields marked in accordance with step 8](_images/bnk1590174208878.png)

3. Before making changes to the source configurations via RESTful requests, you must generate an access token. See [IdentityNow REST APIs](https://community.sailpoint.com/t5/IdentityNow-Wiki/IdentityNow-REST-APIs/ta-p/80132) for details on this process.

4. Retrieve the internal **Source ID** of the PingDirectory source defined previously.

   Do this by retrieving the full list of defined sources in IdentityNow, and then searching for the correct one. The first API call is

   ```
   GET https://<api-url>/cc/api/source/list
   ```

   where `<api-url>` is `https://<org_name>.api.identitynow.com`.

   This returns a JSON array, each element of which is a source from IdentityNow. Search this array for the **Source Name** that you chose. It should look similar to the following example.

   ```json
   {
           "id": "50959",
           "version": 5,
           "name": "PingDirectory",
           "description": "PingDirectory source",
           "owner": {
               "id": "1037426",
               "name": "Adam Creaney"
           },
           "lastUpdated": "2020-04-21T20:45:58Z",
   ….
   Rest of response deleted
   ….
   ```

   |   |                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------- |
   |   | The "id" entry is the value to save from this call. In the above example the "id" value is 50959. |

5. Make the following API call (using a RESTful client application is recommended to accomplish this) to retrieve an `.xml` output of the configuration for the newly created source.

   ```
   GET https://<api-url>/cc/api/source/export/<sourceID>
   ```

   where `<sourceID>` is the "id" value from step 10.

   1. Copy this output and paste into a text editor.

   2. Find the section below for the Group schema as shown in the following screenshot. ![Screenshot of the Group schema with relevant changes highlighted](_images/anx1590177904376.png)

   3. Modify the `nativeObjectType` to `"groupOfNames"`, as shown in the above image.

   4. Find the attribute definition for the "member" attribute and add `multi="true"` to this section, as shown in the above image.

   5. Change the 'groupMemberAttribute' entry by adding `value="member"`, as shown in the above image.

   6. Save the file as `ping_directory.xml` (the name doesn't matter). Do not modify any other elements of the `.xml`.

6. Import the changes back into IdentityNow using a tool such as Postman.

   Use the following Postman command to import the changes.

   ```
   POST https://<api-url>/cc/api/source/import/<sourceID>
   ```

   where `<sourceID>` is the "id" value from step 10.

   * The content-type of this request is multipart/form-data. boundary=\<calculated when request is sent>

   * The body of this request should be of type form-data.

   * The only entry key should be "file". For value, select the `.xml` file from earlier.

![POST window showing the .xml file from earlier](_images/ovc1590182441281.png)

1. Send the request. IdentityNow should return a success message.

2. Click the **Test Connection** button to ensure the connection is successful.

---

---
title: Configuring time synchronization between PingFederate and other servers
description: Some operations require time synchronization between guest servers and PingFederate. This task describes how to resolve time synchronization errors for various server platforms.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_time_sync_pf_others
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_time_sync_pf_others.html
revdate: February 16, 2022
page_aliases: ["single_sign-on_use_cases:htg_config_time_sync_pf_vmware.adoc", "single_sign-on_use_cases:htg_config_time_sync_pf_windows.adoc", "single_sign-on_use_cases:htg_config_time_sync_pf_unix.adoc"]
section_ids:
  component: Component
  configuring-time-synchronization-with-vmware-virtual-servers: Configuring time synchronization with VMware virtual servers
  before-you-begin: Before you begin
  steps: Steps
  troubleshooting: Troubleshooting
  configuring-time-synchronization-with-standalone-windows-servers: Configuring time synchronization with standalone Windows servers
  steps-2: Steps
  configuring-time-synchronization-with-linuxunix-servers: Configuring time synchronization with Linux/Unix servers
  steps-3: Steps
  choose-from: Choose from:
---

# Configuring time synchronization between PingFederate and other servers

Some operations require time synchronization between guest servers and PingFederate. This task describes how to resolve time synchronization errors for various server platforms.

The following PingFederate error message is caused by either network latency or a time synchronization error:

```
ERROR [com.pingidentity.adapters.opentoken.BaseAuthnAdapter] Error decoding token
com.pingidentity.opentoken.TokenException: Invalid token; token is not yet valid (not-before > now)
```

Some latency issues can be managed by configuring the OpenToken adapter. To learn more, refer to the [OpenToken adapter: Not-Before-Tolerance value](https://support.pingidentity.com/s/article/value-of-Not-Before-Tolerance-in-the-OpenToken-adapter-configuration) KnowledgeBase article and the [OpenToken settings reference](https://docs.pingidentity.com/integrations/opentoken/setup/pf_opentoken_token_processor_settings.html).

## Component

PingFederate 9.x

## Configuring time synchronization with VMware virtual servers

Synchronizing with PingFederate servers instead of the default internet time service can solve synchronization errors in Windows Virtual Machine servers.

### Before you begin

Install VMware Tools on your guest OS. For more information, see .

### Steps

1. Go to **Control Panel → Set the time and date → Internet Time tab → Change settings…​** and clear the **Synchronize with an Internet time server** checkbox.

2. Open Command Prompt as an administrator.

3. Enter `time` to verify that the host time is correct.

4. Set the following `.vmx` configuration option to enable periodic synchronization.

   ```
   tools.syncTime=true
   ```

   By default the server will synchronize time every minute. Use the following command to change the synchronization frequency.

   ```
   tools.syncTime.period=time in seconds
   ```

### Troubleshooting

VMware Tools time synchronization cannot correct the issue if the guest OS time is ahead of the server. In that case, use `NTP` or `w32time` to set your server clock.

## Configuring time synchronization with standalone Windows servers

Standalone Windows servers synchronize time with the W32Time service.

### Steps

1. Open Command Prompt as an administrator.

2. Start the W32Time service

   ```
   %windir%\system32\sc.exe start w32time task_started
   ```

   |   |                                             |
   | - | ------------------------------------------- |
   |   | This command requires administrator rights. |

3. Synchronize the server with the W32Time service.

   ```
   %windir%\system32\w32tm.exe /resync
   ```

   The registry can also be modified to resync and perform other time-related tasks. For more information, see [Windows Time Service Technical Reference](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tech-ref).

## Configuring time synchronization with Linux/Unix servers

Synchronize the time on most Linux/Unix servers using a simple `ntpdate` or `rdate` script.

### Steps

1. Before creating the cron job, test these commands as the root user using the following syntax:

   #### Choose from:

   * ```
     /usr/sbin/ntpdate -u  host
     ```

   * ```
     rdate  host  or rdate -u  host
     ```

     |   |                                                                  |
     | - | ---------------------------------------------------------------- |
     |   | See the man page on your specific system for additional options. |

2. Use the following command to synchronize your time server. This example sets the synchronization event to occur at 04:00:

   ```
   # crontab -e
   0 4***/usr/sbin/ntpdate -u  host
   ```

---

---
title: Configuring Workday SSO with PingOne for Enterprise or PingFederate
description: You must have:
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_config_workday_sso_p14e_pf
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_config_workday_sso_p14e_pf.html
revdate: December 4, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  troubleshooting: Troubleshooting
  related-links: Related links
---

# Configuring Workday SSO with PingOne for Enterprise or PingFederate

## Before you begin

You must have:

* PingOne for Enterprise for cloud integration or PingFederate 10.3 for on-premise integration

* A Workday tenant

## About this task

Follow these steps to configure Workday as a service provider (SP) through PingOne for Enterprise or PingFederate.

## Steps

1. Create a Workday public key and configure it for use in PingOne for Enterprise and PingFederate.

   When using single logout (SLO) or signed SP-Initiated single sign-on (SSO), you must create and configure an x509 key pair for the Workday tenant. Later in this task, you'll import the public key into PingOne for Enterprise or PingFederate.

   1. From the Workday tenant, search for the task `Create x509 Private Key Pair`.

   2. Enter a name for the key pair.

   3. Copy and paste the value for **Public Key** into a new text file.

   4. Assign **Key Pair** to **SAML Configuration**.

   5. From the Workday Tenant, search for the task `edit tenant setup - security`.

   6. Assign the **Key Pair** to the field **x509 Private Key Pair**, and click **OK**.

2. For on-premise integration, configure Workday as a service provider using PingFederate.

   |   |                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------- |
   |   | Because of the complexity of setting up an SP connection, only the key configuration options are noted below. |

   1. In PingFederate, go to **Applications → SP Connections**.

   2. Click **Create Connection**.

   3. On the **Connection Template** tab, leave the default selection and click **Next**.

   4. On the **Connection Type** tab, under **Connection Template**, select **Browser SSO Profiles**. Click **Next**.

   5. On the **Connection Options** tab, select **Browser SSO**. Click **Next**.

   6. On the **Import Metadata** tab, select **None**. Click **Next**.

   7. On the **General Info** tab, set the **Partner's Entity ID (Connection ID)** to `http://www.workday.com` and enter your desired value for **Connection Name**. Click **Next**.

   8. On the **Browser SSO** tab, click **Configure Browser SSO**.

   9. On the **SAML Profiles** tab, select your desired **Single Sign-On (SSO) Profiles** and **Single Logout (SLO) Profiles**. Click **Next**.

   10. On the **Assertion Lifetime** tab, leave the default values and click **Next**.

   11. On the **Assertion Creation** tab, click **Configure Assertion Creation**.

   12. Click **Next** until you reach the **Authentication Source Mapping** tab.

   13. To authenticate users to your SP, choose from:

       * Mapping a **New Adapter Instance**, as described in [Configuring an IdP adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_idp_adapter_instance.html).

       * Mapping a **New Authentication Policy**, as described in [Mapping an authentication policy](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapp_auth_policy.html).

   14. Click **Next** and on the **Summary** tab, click **Done**.

   15. On the **Assertion Creation** tab, click **Next**.

   16. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

   17. Configure the following protocols.

       |   |                                                    |
       | - | -------------------------------------------------- |
       |   | *workday-tenant-name* is your Workday tenant name. |

       | Tab                                | Binding  | Endpoint URL                                                      |
       | ---------------------------------- | -------- | ----------------------------------------------------------------- |
       | **Assertion Consumer Service URL** | **POST** | `https://impl.workday.com/workday-tenant-name/login-saml.flex`    |
       | **SLO Service URLs**               | **POST** | https\://impl.workday.com/*workday-tenant-name*/logout-saml.htmld |

   18. On the **Allowable SAML Bindings** tab, select **POST**. Click **Next**.

   19. On the **Signature Policy** tab, enable the following:

       * (Optional) **Require AuthN Requests to Be Signed When Received via the POST or Redirect Bindings**

       * **Always Sign Assertion**

       * **Sign Response As Required**

   20. On the **Encryption Policy** tab, leave the default values and click **Next**. Click **Done**.

   21. On the **Protocol Settings** tab, click **Next**. Click **Done**.

   22. On the **Credentials** tab, click **Configure Credentials** and provide the following credentials:

       1. On the **Digital Signature Settings** tab, in the **Signing Certificate** list, select your signing certificate.

       2. Select **Include the Certificate in the Signature \<keyinfo> Element**.

       3. (Optional) On the **Signature Verification Settings** tab, if you're using SP-initiated SSO or SLO, import the Workday public key that you created previously from the text file.

       4. Click **Done**.

   23. On the **Activation & Summary** tab, click **Save**.

3. For cloud integration, configure Workday as a service provider through PingOne for Enterprise. For general instructions, see [Add an application from the Application Catalog](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_add_application_application_catalog.html)

   1. In the PingOne for Enterprise admin console, go to **Applications**.

   2. In the **Application Catalog**, search for `Workday`.

   3. Select the **Workday** application, not the Sandbox or Preview application.

   4. Click **Setup** to configure SSO for the Workday tenant. Click **Continue to Next Step**.

   5. On the **Connection Configuration** page, enter the following values and click **Continue to Next Step**.

      | Parameter                            | Value                                                                                                                                      |
      | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
      | **ACS URL**                          | `https://myworkday.com/workday-tenant-name/login-saml.flex`                                                                                |
      | **Entity ID**                        | `http://www.workday.com`                                                                                                                   |
      | **Target Resource**                  | `https://www.myworkday.com/workday-tenant-name/fx/home.flex`                                                                               |
      | **Single Logout Endpoint**           | `https://www.myworkday.com/workday-tenant-name/logout-saml.htmld`                                                                          |
      | **Single Logout Response Endpoint**  | `https://www.myworkday.com/workday-tenant-name/logout-saml.htmld`                                                                          |
      | **Primary Verification Certificate** | If using signed SP-initiated SSO or SLO, import the Workday public key that you created previously from the text file where you stored it. |

   6. Map attributes as needed:

      * If the subject will contain the username that corresponds to the account within Workday, select **SAML\_SUBJECT**.

      * If the subject is the email address, click **Advanced** and select the function **GetLocalPartFromEmail**.

   7. Perform additional application customizations as needed, then click **Finish**.

4. Enable SAML and create an IdP provider in Workday:

   1. In the Workday tenant, search for `edit tenant setup - security`.

   2. Select **Enable SAML Authentication**.

   3. Under **SAML Identity Providers**, click the **[icon: plus, set=fa]**to add a new IdP.

      Provide the following information:

      | Parameter                  | Value                                                                                                                                                                                                                                                                                                                                                                                                 |
      | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **Identity Provider Name** | Enter a value that is useful within your environment.                                                                                                                                                                                                                                                                                                                                                 |
      | **Issuer**                 | * For PingOne for Enterprise, the URL is available from the Workday Application Configuration. For example:`https://pingone.com/idp/cd-nnn.pingidentity`

      * For PingFederate, use the SAML 2.0 Entity ID that you can find from (**Server Configuration → Server Settings → Federation Info**).                                                                                                       |
      | **x509 Certificate**       | Create a public key that will contain the key from your PingOne for Enterprise or PingFederate connection.                                                                                                                                                                                                                                                                                            |
      | **Certificate**            | Paste the contents of the PingOne for Enterpriseor PingFederate public certificate into the **Certificate** field.* For PingOne for Enterprise, download the Signing Certificate from the Workday Application Configuration.

      * For PingFederate, export the signing certificate that is used for the Workday SP Connection from **Server Configuration → Signing & Decryption Keys & Certificates**. |

   4. To enable SP-initiated SSO, continue to Step 5.

   5. To enable SLO, go to Step 7.

   6. In the PingOne for Enterprise admin console, edit the Workday Application and continue to the page **Configure your connection**.

   7. Upload the public key from your text file to the **Primary Verification Certificate** and save the configuration.

5. Enable SP-initiated SSO for Workday:

   1. In the Workday tenant, search for the task `edit tenant setup - security`.

   2. Under **SAML Identity Providers** for the desired IdP, select `SP Initiated`.

   3. In the **Service Provider ID** field, enter `http://www.workday.com`.

   4. Select `Do Not Deflate SP-initiated Request`.

   5. **Optional:** Select `Sign SP-initiated Request`. If checked, refer to the section Workday x509 Public Key.

   6. Enter a value for **IdP SSO Service URL**:

      * For PingOne for Enterprise: From the Workday Application Configuration: Initiate Single Sign-On (SSO) URL.

      * For PingFederate: https\://*host*:*port*/idp/SSO.saml2

6. To test SP-init, open the following link to trigger SP-Init from Workday: `https://impl.workday.com/workday-tenant-name/login-saml2.flex`.

7. Enable SLO for Workday:

   1. In the Workday tenant, search for the task `edit tenant setup - security`.

   2. Under **SAML Identity Providers** for the desired IdP, select **Enable IdP Initiated Logout**.

   3. Configure the following **Logout Response URLs**:

      * For PingOne for Enterprise: https\://sso.connect.pingidentity.com/sso/SLO.saml2

      * For PingFederate: https\://*host*:*port*/idp/SLO.saml2

   4. Under **SAML Identity Providers**for the desired IdP, select **Enable Workday Initiated Logout**.

   5. Configure the following Logout Request URLs:

      * For PingOne for Enterprise: https\://sso.connect.pingidentity.com/sso/SLO.saml2

      * For PingFederate: https\://*host*:*port*/idp/SLO.saml2

8. **Optional:** Redirect the Workday sign on page to PingOne for Enterprise or PingFederate, as appropriate.

   1. From the Workday tenant, search for the task `edit tenant setup - security`.

   2. In the **Single Sign-on** section, add a new **Redirection URL**.

   3. Enter the SSO URL for the following fields:

      * **Login Redirect URL**

      * **Mobile App Login Redirect URL**

      * **Mobile Browser Login Redirect URL**

        The SSO URL is: https\://impl.workday.com/*\<workday-tenant-name*/login-saml2.flex>

   4. Configure the **Login Redirect URL**:

      * For PingOne for Enterprise: `https://sso.connect.pingidentity.com/sso/SLO.saml2`

      * For PingFederate: `https://host:port/idp/SLO.saml2`

   5. Configure the environment as determined by the tenant URL:

      * If the subdomain for the Workday tenant URL starts with `impl`, then the **Environment** attribute is **Implementation**.

      * If the subdomain name starts with something else, contact the Workday support team to determine the **Environment** attribute.

## Troubleshooting

* If there is an issue with the login redirect URL, append `?redirect=n` to the Workday login URL. For example, `https://impl.workday.com/wday/authgwy/workday-tenant-name/login.htmld?redirect=n`.

* Workday provides a SAML message validator that can be used to debug SAML issues. Search for the task `Validate SAML Message`.

## Related links

* [PingFederate 9.2 Administrator's Manual](https://cdn-docs.pingidentity.com/archive/pdf/pingfederate/pingfederate-92.pdf#page=62)

* [PingID Administration Guide](https://docs.pingidentity.com/pingid/pid_landing_page.html)

* [Workday Community](https://resourcecenter.workday.com/en-us/wrc/home.html)

* [Workday Support](https://www.workday.com/en-us/services/support.html)

---

---
title: Connecting Okta as an IdP through SAML to PingFederate as an SP
description: This solution provides the steps to configure Okta as an identity provider (IdP) and PingFederate as a service provider (SP) using a SAML 2.0 connection for communications. This process doesn't address single logout (SLO) or provisioning for either side of the single sign-on (SSO) transaction.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_connect_okta_idp_saml_pf_sp
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_connect_okta_idp_saml_pf_sp.html
revdate: July 18, 2022
page_aliases: ["single_sign-on_use_cases:htg_connect_okta_idp_saml_pf_sp_okta_idp.adoc", "single_sign-on_use_cases:htg_connect_okta_idp_saml_pf_sp_config_pf.adoc", "single_sign-on_use_cases:htg_connect_okta_idp_saml_pf_sp_troubleshooting.adoc"]
section_ids:
  component: Component
  process-overview: Process overview
  configuring-okta-as-the-idp: Configuring Okta as the IdP
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result
  configuring-pingfederate-as-the-sp: Configuring PingFederate as the SP
  before-you-begin-2: Before you begin
  steps-2: Steps
  result-2: Result:
  result-3: Result
  troubleshooting: Troubleshooting
  sso-attempt-looping: SSO attempt looping
  pingfederate-error-in-server-log: PingFederate error in server.log
---

# Connecting Okta as an IdP through SAML to PingFederate as an SP

This solution provides the steps to configure Okta as an identity provider (IdP) and PingFederate as a service provider (SP) using a SAML 2.0 connection for communications. This process doesn't address single logout (SLO) or provisioning for either side of the single sign-on (SSO) transaction.

## Component

PingFederate 9.1

## Process overview

The process for Okta as the IdP using IdP-initiated SSO is:

1. The user goes to Okta, assuming the user has an existing Okta session.

2. The user clicks on the Chicklet, which sends a SAML response to the configured SP.

3. A session is established with the SP.

4. The user is authenticated.

In SP-initiated SSO, ​the process is:

1. The user goes to the target SP first. They don't have a session established with the SP.

2. The SP redirects the user to the configured sign-on URL, Okta's generated app instance URL, sending the SAML request.

3. Okta receives a SAML request, assuming the user has an existing Okta session.

4. Okta sends a SAML response to the configured SP.

5. The SP receives the SAML response and verifies that it is correct.

6. A session is established on the SP side.

7. The user is authenticated.

## Configuring Okta as the IdP

Configure Okta as an identity provider (IdP) and PingFederate as a service provider (SP) using a SAML 2.0 connection.

### Before you begin

You must have the following:

* PingFederate installed and operating with administrator access OS

* Okta with Workforce Identity Single sign-on, One-App, or Enterprise editions

This task also assumes that you have the following information from the SP:

* Assertion consumer service (ACS) URL

* Signing certificate (if required)

### About this task

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | With Okta as the IdP, only a one-to-one IdP to SP entityID relationship is supported. If the SP has more than one application, a new IdP connection with a unique entityID from Okta is required. This behavior can be overridden by Okta. |

### Steps

1. Sign on to Okta as an administrator.

2. Go to **Application → Add Application**.

3. On the **Add Application** page, click **Add Application**.

4. On the **Create a New Application Integration** page, in the **Platform** list, select **Web**.

5. Click **SAML 2.0**, and then click **Create**.

6. On the **General Settings** tab, in the **Create SAML Integration** section, enter a name for the application in the **App name** field. Click **Next**.

   You can also add a logo and set the app visibility.

7. On the **Configure SAML** tab, in the **Single Sign on URL** field, enter the PingFederate ACS URL.

8. In the **Audience URI** field, enter the PingFederate SAML entity ID or connection virtual server ID (VSID).

9. **Optional:** In the **Attribute Statements (Optional)** and **Group Attribute Statements (Optional)** sections, add attributes from the Okta user store to fulfill the attribute contract with the SP.

10. Click **Next**.

11. **Optional:** Complete the sections on the **Feedback** tab.

    The sections on this tab help the Ping Identity support team.

12. Click **Finish**.

13. To obtain the file needed to configure the PingFederate SP, in the **Summary** window, click the **Identity Provider metadata** link.

14. **Optional:** If you're creating your own portal, click the **General** tab, and then copy the **App Embed Link**.

### Result

Okta configuration as the IdP is complete.

## Configuring PingFederate as the SP

Configure PingFederate as a service provider (SP) with Okta as an identity provider (IdP) using a SAML 2.0 connection.

### Before you begin

You must have the following:

* PingFederate installed and operating with administrator access OS

* Okta Enterprise or Enterprise Plus active with administrative access

This task also assumes that you have the following information:

* A metadata XML file from the Okta IdP that is accessible to the PingFederate console application

* An adapter configured for the target SP application

### Steps

1. In the PingFederate administrative console, go to **Authentication → Integration → IdP Connections**, and then click **Create Connection**.

2. On the **Connection Type** tab, select **Browser SSO Profiles**, and in the **Protocol** list, select **SAML 2.0**. Click **Next**.

3. On the **Connection Options** tab, click **Next**.

4. On the **Import Metadata** tab, click **File**, and then click **Choose file**.

5. Go to the Okta IdP metadata file, and then click **Open**.

6. Click **Next**.

7. On the **Metadata Summary** tab, click **Next**.

8. On the **General Info** tab, review the **Partner's Entity ID** and **Connection Name**.

   The **General Info** tab is filled out by the metadata.

9. If using a virtual server ID (VSID) for this connection instead of the Systems SAML 2.0 entityID, enter it in the **Virtual Server IDS** field. Click **Next**.

10. On the **Browser SSO** tab, click **Configure Browser SSO**.

11. On the **SAML Profiles** tab, select the agreed upon profiles, at a minimum **IdP-Initiated SSO**. Click **Next**.

    Optionally, you can select SP-initiated single sign-on (SSO) and sinigle logout (SLO) if configured for this connection.

12. On the **User-Session Creation** tab, click **Configure User-Session Creation**.

13. On the **Identity Mapping** tab, click **Account Mapping** and then click **Next**.

14. On the **Attribute Contract** tab, add any required attributes for the contract. Click **Next**.

15. On the **Target Session Mapping** tab, click **Map New Adapter Instance.**.

16. On the **Adapter Instance** tab, select the previously configured adapter from the **Adapter Instance** list. Review the adapter contract, and then click **Next**.

    Optionally, you can click **Manage Adapter Instances** to create a new adapter that will map the inbound attributes from Okta into the PingFederate connection.

17. On the **Adapter Data Store** tab, keep the default selection of **Use only the Attributes Available in the SSO Assertion**, and then click **Next**.

18. On the **Adapter Contract Fulfillment** tab, map the attributes from the inbound assertion to the connection attributes. Click **Next**

19. On the **Issuance Criteria** tab, click **Next**.

20. To complete the adapter configuration, on the **Adapter Mapping Summary** tab, click **Done**, and then click **Next** on the **Target Session Mapping** tab.

    #### Result:

    You return to the **User-Session Creation** tabs.

21. Review the **User-Session Creation Summary** tab, and then click **Done**.

22. On the **User Session Creation** tab, click **Next**.

23. On the **Protocol Settings** tab, click **Configure Protocol Settings**.

    The **Protocol Settings** tab shows the currently configured values from the metadata.

24. On the **SSO Service URLs** tab, review the **Endpoint URLs** extracted from the metadata. Click **Next**.

25. On the **Allowable SAML Bindings** tab, ensure only **Post** and **Redirect** are selected, and then click **Next**.

26. **Optional:** On the **Overrides** tab, optionally specify a different Target URL and Authorization context. Click **Next**.

27. On the **Signature Policy** tab, use the default selection of **SAML Standard** where the IdP will sign the response. Click **Next**.

    This is the Okta default.

28. On the **Encryption Policy** tab, keep the default selection of **None**. Click **Next**.

29. On the **Protocol Settings Summary** tab, review and click **Done**.

30. On the**Protocol Settings** tab, click **Next**.

31. On the **Browser SSO Summary** tab, review the settings and click **Done**.

32. On the **Browser SSO** tab, click **Next**.

33. On the **Credentials** tab, verify the IdP signing certificate is available, and then click **Next**.

    Because you imported metadata, the signing public key from the Okta partner was included.

34. On the **Activation and Summary** tab, ensure that the connection is active.

35. Click **Save**.

### Result

PingFederate SP configuration is complete.

## Troubleshooting

You might encounter the following common issues after completing configuration.

### SSO attempt looping

Single sign-on (SSO) attempt locking happens if the following items in the Okta configuration aren't set to the PingFederate assertion consumer service (ACS) endpoint:

* Recipient

* Destination

* Postback URL

### PingFederate error in `server.log`

The following error implies that the entityID used for the Okta connection is incorrect.

```
Top level error (ref#ftpcge): Unable to lookup idp connection metadata for
entityid='http://www.okta.com/<string>
```

Check your metadata or check with the Okta account owner to verify the entityID.