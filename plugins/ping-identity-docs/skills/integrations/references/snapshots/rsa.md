---
title: Configuring an adapter instance
description: Configure the RSA SecurID IdP Adapter to determine how PingFederate communicates with the RSA Authentication Manager server.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_configuring_an_adapter_instance.html
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the RSA SecurID IdP Adapter to determine how PingFederate communicates with the RSA Authentication Manager server.

## Steps

1. If you are upgrading from version 2.x of the integration kit, note the configuration details of your existing adapter instance, and then delete the adapter instance. Restore your configuration as you complete the steps below.

2. In the PingFederate administrative console, go to **Authentication > Integration > IdP Adapters**. Click **Create new Instance**.

3. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. From the **Type** list, select **RSA SecurID IdP Adapter**. Click **Next**.

4. (Optional) On the **IdP Adapter** screen, configure additional RSA Authentication Manager servers to try, in order, in case the primary server fails to respond.

   1. In the **Failover Servers** section, click **Add a new row to 'Failover Servers'**.

   2. In the **RSA Base API URL** field, enter the complete URL and endpoint of the RSA Authentication Manager server.

   3. If you want to skip hostname verification to prevent errors, clear the **Verify HTTPS Hostname** checkbox.

   4. In the **Action** column, click **Update**.

   5. To add another property, repeat steps a - d.

5. On the **IdP Adapter** tab, configure the adapter instance by referring to [RSA SecurID IdP Adapter settings reference](pf_rsa_securid_ik_rsa_securid_idp_adapter_settings_reference.html). Click **Next**.

6. On the **Actions** screen, test your connection to the RSA Authentication API. Resolve any issues that are reported and then click **Next**.

7. On the **Extended Contract** tab, add any attributes that you want to include in the contract. Click **Next**.

8. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

9. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

10. On the **Summary** tab, check and save your configuration. Click **Save**.

11. Create or modify a connection to the service provider using the RSA SecurID IdP Adapter instance. Learn more in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

---

---
title: Customizing templates
description: The RSA SecurID Integration Kit includes templates that can display RSA SecurID authentication challenges and other messages. You can customize the HTML portions of these templates to suit your organization's branding and presentation needs.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_customizing_templates
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_customizing_templates.html
revdate: June 21, 2024
---

# Customizing templates

The RSA SecurID Integration Kit includes templates that can display RSA SecurID authentication challenges and other messages. You can customize the HTML portions of these templates to suit your organization's branding and presentation needs.

The following table lists the templates and their use. For more information about templates, see [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) in the PingFederate documentation.

**Template files included in the RSA SecurID Integration Kit**

| Template file                                       | Description                                                                                                    |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `RSASecurIDIdPAdapter.nexttoken.template.html`      | Form presented when the user is required to enter the next token.                                              |
| `RSASecurIDIdPAdapter.reauthenticate.template.html` | Login form asking the user to authenticate again after resetting their PIN.                                    |
| `RSASecurIDIdPAdapter.systempinreset.template.html` | Presents the user with a new, system-generated PIN.                                                            |
| `RSASecurIDIdPAdapter.userpinreset.template.html`   | Presents the user with a form to input a new PIN.                                                              |
| `RSASecurIDIdPAdapter.form.template.html`           | Main login form, presented under normal conditions.                                                            |
| `RSASecurIDIdPAdapter.cas.approve.template.html`    | Presents the user with the Cloud Authentication Service options that are available to them for authentication. |
| `RSASecurIDIdPAdapter.approve.template.html`        | Presents the user with a wait page while waiting for a push notification to complete on the user device.       |
| `RSASecurIDIdPAdapter.token.template.html`          | Presents the user with the form for the `TOKEN` authentication method for the Cloud Authentication Service.    |

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the RSA SecurID Integration Kit files to your PingFederate directory.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_deploying_the_integration_files.html
revdate: June 21, 2024
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the RSA SecurID Integration Kit files to your PingFederate directory.

## Steps

1. Download the RSA SecurID Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/rsa-securid-integration-kit).

2. Stop PingFederate.

3. If you are upgrading an existing deployment, back up your customizations and delete older versions of the integration files.

   1. Back up any RSA SecurID Integration Kit files that you customized in `<pf_install>/pingfederate/server/default/conf/templates`:

      * `RSASecurIDIdPAdapter.form.template.html`

      * `RSASecurIDIdPAdapter.nexttoken.template.html`

      * `RSASecurIDIdPAdapter.reauthenticate.template.html`

      * `RSASecurIDIdPAdapter.systempinreset.template.html`

      * `RSASecurIDIdPAdapter.userpinreset.template.html`

      * `RSASecurIDIdPAdapter.approve.template.html`

      * `RSASecurIDIdPAdapter.cas.approve.template.html`

      * `RSASecurIDIdPAdapter.token.template.html`

   2. Delete the following from `<pf_install>/pingfederate/server/default/deploy`:

      * `pf-rsa-securid-idp-adapter-<version>.jar`

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If you have existing customizations, manually modify the new `rsa-securid-messages.properties` file based on your previous customizations.

   You can find more information on customizing messages in [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

6. If there is more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2 - 7 for each engine node.

---

---
title: Download manifest
description: The following files are included in the RSA SecurID Integration Kit .zip archive:
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_download_manifest.html
revdate: June 21, 2024
---

# Download manifest

The following files are included in the RSA SecurID Integration Kit `.zip` archive:

* `Legal.pdf`: Copyright and license information

* `dist/pingfederate/server/default`: Contains the integration files

  * `deploy`: Contains the Java libraries

    * `pf-rsa-securid-idp-adapter-<version>.jar` – JAR file that contains the RSA SecurID IdP Adapter.

  * `conf` – contains the HTML template that presents the RSA SecurID sign-on form.

    * `template`: Contains user-facing HTML template files

      * `RSASecurIDIdPAdapter.form.template.html` – main login form, presented under normal conditions.

      * `RSASecurIDIdPAdapter.nexttoken.template.html` – form presented when the user is required to enter the next token.

      * `RSASecurIDIdPAdapter.reauthenticate.template.html` – login form asking the user to authenticate again after resetting their PIN.

      * `RSASecurIDIdPAdapter.systempinreset.template.html` – presents the user with a new, system-generated PIN.

      * `RSASecurIDIdPAdapter.userpinreset.template.html` – presents the user with a form to input a new PIN.

      * `RSASecurIDIdPAdapter.cas.approve.template.html` - presents the user with the Cloud Authentication Service options that are available to them for authentication.

      * `RSASecurIDIdPAdapter.approve.template.html` - presents the user with a wait page while waiting for a push notification to complete on the user device.

      * `RSASecurIDIdPAdapter.token.template.html` - presents the user with the form for the `TOKEN` authentication method for the Cloud Authentication Service.

    * `assets`: Contains functional scripts and files used by the template

      * `css` – contains CSS files for the templates.

        * `rsa-securid.css` – a CSS file that customizes the appearance of the template files.

        * `end-user/<version>/end-user.css` – a CSS file that customizes the appearance of the template files.

      * `fonts/end-user/icons`: Contains template icons

  * `lib/pf-authn-api-sdk-<version>.jar`: A `.jar` file that contains the PingFederate Authentication API SDK

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_enabling_debug_logging.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. For general information about logging, see [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following.

   1. Find the following section.

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`.

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags.

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. If you want to log activity just for the RSA SecurID IdP Adapter, add the following line.

   ```html
   <Logger name="com.pingidentity.adapters.securid.idp" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Example OGNL expressions
description: The following examples show common ways you might want to customize your outgoing SAML assertion.
component: rsa
page_id: rsa:rsa_securid_cloud_authentication_integration_guide:pf_rsa_cloudauthentication_integration_example_ognl_expressions
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_cloud_authentication_integration_guide/pf_rsa_cloudauthentication_integration_example_ognl_expressions.html
revdate: July 5, 2024
section_ids:
  example-1-authncontextclassref-based-on-saml_authn_ctx: "Example 1: AuthnContextClassRef based on SAML_AUTHN_CTX"
  example-2-authncontextclassref-based-on-sp-entity-id: "Example 2: AuthnContextClassRef based on SP entity ID"
---

# Example OGNL expressions

The following examples show common ways you might want to customize your outgoing SAML assertion.

## Example 1: AuthnContextClassRef based on SAML\_AUTHN\_CTX

To send `AuthnContextClassRef` based on the `SAML_AUTHN_CTX` attribute from your PingFederate authentication policy, use the following expression:

```
#req = #AuthnRequestDocument.getAuthnRequest(),
#newctx = #ChainedAttributes.get("SAML_AUTHN_CTX"),
#newctx && (
#req.isSetRequestedAuthnContext() && #req.unsetRequestedAuthnContext(),
#ctx = #req.addNewRequestedAuthnContext(),
#ctx.addAuthnContextClassRef(#newctx.toString())
)
```

In this example, the value of the `SAML_AUTHN_CTX` attribute is "Password" and the expression sends the following:

```html
<AuthnRequest Version="2.0" ID="gjmkj6OVk9tVhd1kvno63j92pqb" IssueInstant="2021-05-11T21:36:42.953Z" xmlns="urn:oasis:names:tc:SAML:2.0:protocol" xmlns:urn="urn:oasis:names:tc:SAML:2.0:assertion">
 <urn:Issuer>localhost:default:entityId</urn:Issuer>
 <urn:Subject>
  <urn:NameID>rsa@demo.com</urn:NameID>
 </urn:Subject>
 <NameIDPolicy AllowCreate="true"/>
 <RequestedAuthnContext>
  <urn:AuthnContextClassRef>Password</urn:AuthnContextClassRef>
 </RequestedAuthnContext>
</AuthnRequest>
```

## Example 2: AuthnContextClassRef based on SP entity ID

To send `AuthnContextClassRef` based on the service provider (SP) entity ID, use the following expression:

```
#Salesforce = "salesforceSPConnection", // this would be the target
#req = #AuthnRequestDocument.getAuthnRequest(),

#newctx = #Salesforce == #FedHubSpConnPartnerId ? "urn:rsa:names:tc:SAML:2.0:ac:classes:spec:stepup:PingFed_Lev_Low": null,
#newctx && (
#req.isSetRequestedAuthnContext() && #req.unsetRequestedAuthnContext(),
#ctx = #req.addNewRequestedAuthnContext(),
#ctx.addAuthnContextClassRef(#newctx.toString())
)
```

In this example, the SP connection used is Salesforce. The value `urn:rsa:names:tc:SAML:2.0:ac:classes:spec:stepup:PingFed_Lev_Low` is sent as the AuthnContextClassRef. `#FedHubSpConnPartnerId` is the SP entity ID.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For other variables, see [Message types and available variables](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_message_types_and_avail_variables.html) in the PingFederate documentation. |

The expression sends the following:

```
<AuthnRequest Version="2.0" ID="gjmkj6OVk9tVhd1kvno63j92pqb" IssueInstant="2021-05-11T21:36:42.953Z" xmlns="urn:oasis:names:tc:SAML:2.0:protocol" xmlns:urn="urn:oasis:names:tc:SAML:2.0:assertion">
 <urn:Issuer>localhost:default:entityId</urn:Issuer>
 <urn:Subject>
  <urn:NameID>rsa@demo.com</urn:NameID>
 </urn:Subject>
 <NameIDPolicy AllowCreate="true"/>
 <RequestedAuthnContext>
  <urn:AuthnContextClassRef>urn:rsa:names:tc:SAML:2.0:ac:classes:spec:stepup:PingFed
  _Lev_Low</urn:AuthnContextClassRef>
 </RequestedAuthnContext>
</AuthnRequest>
```

---

---
title: Integrating PingFederate with RSA SecurID
description: RSA provides complete setup steps for both PingFederate and the RSA Cloud Authentication Service. After you finish the RSA instructions, you can customize the SAML assertion in PingFederate.
component: rsa
page_id: rsa:rsa_securid_cloud_authentication_integration_guide:pf_rsa_cloudauthentication_integration_integrating_pf_with_rsa_securid
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_cloud_authentication_integration_guide/pf_rsa_cloudauthentication_integration_integrating_pf_with_rsa_securid.html
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Integrating PingFederate with RSA SecurID

RSA provides complete setup steps for both PingFederate and the RSA Cloud Authentication Service. After you finish the RSA instructions, you can customize the SAML assertion in PingFederate.

## Steps

1. Follow the [Ping Identity PingFederate 9.3 - RSA Ready SecurID Access Implementation Guide](https://community.rsa.com/t5/rsa-securid-access-integrations/ping-identity-pingfederate-9-3-rsa-ready-securid-access/ta-p/566800) in the RSA documentation. Your integration type and use case determine which steps to follow.

2. (Optional) Modify the outgoing SAML assertion to suit your needs.

   1. [Enabling and disabling expressions](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enable_disable_express.html) in the PingFederate documentation.

   2. Open the connection to RSA that you created while following the RSA implementation guide.

   3. Go to **Browser SSO > Protocol Settings > Configure Protocol Settings**. On the **Assertion Consumer Service URL** tab, click **Show Advanced Customizations**.

   4. In the **Message Type** list, select **AuthnRequestDocument**.

   5. In the **Expression** field, enter your custom OGNL expression.

      Learn more in [Example OGNL expressions](pf_rsa_cloudauthentication_integration_example_ognl_expressions.html).

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the RSA SecurID Integration Kit.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_known_issues_and_limitations.html
revdate: June 21, 2024
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the RSA SecurID Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* The RSA SecurID Integration Kit is designed to work with the on-premises RSA Authentication Manager (AM).

  |   |                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | This integration kit works with the RSA AM when the AM is integrated with the RSA Cloud Authentication Service (CAS), but does not work directly with the RSA CAS. |

* When a push notification request that's triggered by the RSA CAS's `Approve` method times out on a registered device, the adapter automatically fails the authentication method.

* Only RSA AM 8.7 SP2 and later integrated with CAS supports the `Approve` method's `Selection` mode.

* The adapter requires you to set a specific JVM option if you're using PingFederate deployed in JDK 17 in BC FIPS mode. Update the `JAVA_OPTS` to set `--add-opens=java.base/sun.security.internal.spec=ALL-UNNAMED` in the `run.sh` and `run.bat` files.

  For example, in `<pf_install>/pingfederate/bin/run.sh`, add:

  ```
  # java 17 support
  if [[ $JAVA_MAJOR_VERSION -eq "17" ]]; then
  JAVA_OPTS="$JAVA_OPTS --add-opens=java.base/java.lang=ALL-UNNAMED"
  JAVA_OPTS="$JAVA_OPTS --add-opens=java.base/java.util=ALL-UNNAMED"
  JAVA_OPTS="$JAVA_OPTS --add-opens=java.base/sun.security.internal.spec=ALL-UNNAMED"
  JAVA_OPTS="$JAVA_OPTS --add-exports=java.base/sun.security.x509=ALL-UNNAMED"
  JAVA_OPTS="$JAVA_OPTS --add-exports=java.base/sun.security.util=ALL-UNNAMED"
  JAVA_OPTS="$JAVA_OPTS --add-exports=java.naming/com.sun.jndi.ldap=ALL-UNNAMED"
  JAVA_OPTS="$JAVA_OPTS --add-exports=java.base/sun.net.util=ALL-UNNAMED"
  JAVA_OPTS="$JAVA_OPTS --add-exports=java.base/sun.security.pkcs=ALL-UNNAMED"
  JAVA_OPTS="$JAVA_OPTS --add-exports=java.base/sun.security.pkcs10=ALL-UNNAMED"
  fi
  ```

  In `<pf_install>/pingfederate/bin/run.bat`, add:

  ```
  if %JAVA_PRODUCT_VERSION% == 17 (
  set "PF_ENDORSED_DIRS_FLAG="
  set JAVA_OPTS=%JAVA_OPTS% ^
  --add-opens=java.base/java.lang=ALL-UNNAMED ^
  --add-opens=java.base/java.util=ALL-UNNAMED ^
  --add-opens=java.base/sun.security.internal.spec=ALL-UNNAMED ^
  --add-exports=java.naming/com.sun.jndi.ldap=ALL-UNNAMED ^
  --add-exports=java.base/sun.net.util=ALL-UNNAMED ^
  --add-exports=java.base/sun.security.pkcs=ALL-UNNAMED ^
  --add-exports=java.base/sun.security.pkcs10=ALL-UNNAMED ^
  --add-exports=java.base/sun.security.x509=ALL-UNNAMED ^
  --add-exports=java.base/sun.security.util=ALL-UNNAMED
  )
  ```

---

---
title: Overview of the SSO flow
description: With the RSA SecurID Integration Kit, PingFederate includes an RSA Authentication Manager server in the sign-on flow.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_overview_of_the_sso_flow.html
revdate: June 21, 2024
section_ids:
  description: Description
---

# Overview of the SSO flow

With the RSA SecurID Integration Kit, PingFederate includes an RSA Authentication Manager server in the sign-on flow.

The following figure illustrates a single sign-on (SSO) scenario in which PingFederate authenticates users to an SP application using the RSA SecurID IdP Adapter.

![A flow diagram that shows the interaction between PingFederate and the RSA Authentication Manager server.](_images/uop1563995598690.jpg)

## Description

1. The user initiates SSO from an SP application through the PingFederate SP server.

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This SP-initiated scenario represents the optimal use case, where both the identity provider (IdP) and SP use PingFederate. If your SP partner does not support this scenario, however, PingFederate accepts any valid SAML authentication request.You can also enable IdP-initiated SSO. In this case, the SSO flow would not include this step or the next one. |

2. The PingFederate SP server generates a SAML `AuthnRequest` and sends it to the PingFederate IdP server.

3. The PingFederate IdP server requests user authentication using the RSA SecurID Adapter. The adapter challenges the user for a RSA SecurID passcode.

4. The adapter sends authentication credentials to RSA Authentication Manager.

5. The RSA Authentication Manager validates the credentials sent by the adapter and sends a response to PingFederate.

6. If the validation fails, user access is denied. If validation succeeds, the PingFederate IdP server generates a SAML assertion with the username as the Subject and passes it to the PingFederate SP server.

---

---
title: PingFederate Authentication API Support
description: The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in PingFederate authentication API in the PingFederate documentation.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_authentication_api_support.html
revdate: February 23, 2026
section_ids:
  models-objects-and-error-codes: Models, objects, and error codes
  state-models: State models
  securid_next_tokencode_required: SECURID_NEXT_TOKENCODE_REQUIRED
  securid_next_code_required: SECURID_NEXT_CODE_REQUIRED
  securid_token_required: SECURID_TOKEN_REQUIRED
  securid_reauthentication_required: SECURID_REAUTHENTICATION_REQUIRED
  securid_system_pin_reset_required: SECURID_SYSTEM_PIN_RESET_REQUIRED
  securid_credential_required: SECURID_CREDENTIAL_REQUIRED
  securid_user_pin_reset_required: SECURID_USER_PIN_RESET_REQUIRED
  challenge-method-required: SECURID_CAS_CHALLENGE_METHOD_REQUIRED
  securid_cas_approve_method_pending_verification: SECURID_CAS_APPROVE_METHOD_PENDING_VERIFICATION
  action-models: Action models
  cancel: cancel
  checknexttokencode: checkNextTokencode
  check-credential: checkCredential
  checkpasscode: checkPasscode
  checktokencode: checkTokencode
  continue: continue
  poll: poll
  resetpin: resetPin
  selectchallengemethod: selectChallengeMethod
  usealternatemethod: useAlternateMethod
  validatepasscode: validatePasscode
  objects: Objects
  authentication-method: AuthenticationMethod object
  authentication-method-version: AuthenticationMethodVersion object
  challenge-method-info: ChallengeMethodInfo object
  challenge-method-set: ChallengeMethodSet object
  method-prompt: MethodPrompt object
  name-value-pair: NameValuePair object
  error-codes: Error codes
  top-level-error-codes: Top level error codes
  detail-level-error-codes: Detail level error codes
---

# PingFederate Authentication API Support

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the RSA SecurID IdP Adapter into your authentication flow, configure your application based on the information in this section.

|   |                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also explore the process using the PingFederate Authentication API Explorer. Learn more in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation. |

## Models, objects, and error codes

When using the RSA SecurID Integration Kit through the PingFederate Authentication API, the adapter uses the following state models, action models, objects, and error codes.

### State models

#### `SECURID_NEXT_TOKENCODE_REQUIRED`

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > * `authFailed` (boolean)
> >
> >   Specifies whether the current attempt is the result of a failed authorization attempt.
> >
> > * `additionalErrorInfo` (string)
> >
> >   Additional error info if the current attempt resulted in failed authorization.
>
> > **Collapse: Actions**
> >
> > * `checkNextTokencode`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > The next tokencode is required for authentication.

#### `SECURID_NEXT_CODE_REQUIRED`

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | Relevant only when the Authentication Manager is integrated with the Cloud Authentication Service. |

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > * `authFailed` (boolean)
> >
> >   Specifies whether the current attempt is the result of a failed authorization attempt.
> >
> > * `additionalErrorInfo` (string)
> >
> >   Additional error info if the current attempt resulted in failed authorization.
>
> > **Collapse: Actions**
> >
> > * `checkNextTokencode`
> >
> > * `useAlternateMethod`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > The next tokencode is required for authentication.

#### `SECURID_TOKEN_REQUIRED`

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | Relevant only when the Authentication Manager is integrated with the Cloud Authentication Service. |

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > * `authFailed` (boolean)
> >
> >   Specifies whether the current attempt is the result of a failed authorization attempt.
> >
> > * `additionalErrorInfo` (string)
> >
> >   Additional error info if the current attempt resulted in failed authorization.
>
> > **Collapse: Actions**
> >
> > * `checkTokencode`
> >
> > * `useAlternateMethod`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > The SecurID Authenticate OTP is required for authentication.

#### `SECURID_REAUTHENTICATION_REQUIRED`

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > There is no model for this state.
>
> > **Collapse: Actions**
> >
> > * `checkPasscode`
> >
> > * `useAlternateMethod`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > A passcode is required for reauthentication.

#### `SECURID_SYSTEM_PIN_RESET_REQUIRED`

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > * `pin` (string)
> >
> >   A new pin the system generated for the user.
>
> > **Collapse: Actions**
> >
> > * `continue`
> >
> > * `useAlternateMethod`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > Generates a new pin for the user.

#### `SECURID_CREDENTIAL_REQUIRED`

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > * `username` (string)
> >
> >   The username used in first-factor authentication.
> >
> > * `remainingTries` (integer)
> >
> >   The number of tries left.
> >
> > * `allowUsernameEdits` (boolean)
> >
> >   The username isn't editable if the adapter is being used in second-factor authentication.
> >
> > * `authFailed` (boolean)
> >
> >   Specifies whether the current attempt is the result of a failed authorization attempt.
> >
> > * `resetFailed` (boolean)
> >
> >   Specifies whether this attempt is the result of a failed pin reset attempt.
>
> > **Collapse: Actions**
> >
> > * `checkCredential`
> >
> > * `validatePasscode`
> >
> > * `useAlternateMethod`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > The SecurID credential is required for authentication.

#### `SECURID_USER_PIN_RESET_REQUIRED`

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > * `pinMinLength` (integer)
> >
> >   The minimum length needed for the pin.
> >
> > * `pinMaxLength` (integer)
> >
> >   The maximum length needed for the pin.
> >
> > * `pinAlphabeticCharCount` (integer)
> >
> >   The minimum number of letters needed for the pin.
> >
> > * `pinNumericCharCount` (integer)
> >
> >   The minimum number of numbers needed for the pin.
> >
> > * `pinAlphaNumeric` (boolean)
> >
> >   Specifies whether the pin can be alphanumeric.
> >
> > * `pinResetMessage` (string)
> >
> >   Pin reset requirement.
> >
> > * `authFailed` (boolean)
> >
> >   Specifies whether this attempt is the result of failed authorization attempt.
>
> > **Collapse: Actions**
> >
> > * `resetPin`
> >
> > * `useAlternateMethod`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > The user needs to reset the pin.

#### `SECURID_CAS_CHALLENGE_METHOD_REQUIRED`

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > * `challengeMethodIds` (array) (deprecated)
> >
> >   The method IDs of challenge methods as received from Cloud Authentication Service.
> >
> >   |   |                                                                                                                                                                                                                                 |
> >   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> >   |   | `challengeMethodIds` was deprecated in the 4.0.1 release, but is still usable. In this case, deprecated just means that you can switch to `challengeMethods` when you want to find more information about the challenge method. |
> >
> > * `challengeMethods` (array\[ChallengeMethodInfo])
> >
> >   List of objects containing challenge method details as received from Cloud Authentication Service. The adapter supports the `APPROVE`, `SECURID` and `TOKEN` authentication methods only.
> >
> > * `authFailed` (boolean)
> >
> >   Specifies whether the previous auth attempt failed.
> >
> > * `resetFailed` (boolean)
> >
> >   Specifies whether the previous pin reset attempt failed.
> >
> > * `authenticationMethod` (AuthenticationMethod)
> >
> >   You can find more information in the [AuthenticationMethod object](#authentication-method) table.
> >
> > * `authenticationMethodVersion` (AuthenticationMethodVersion)
> >
> >   You can find more information in the [AuthenticationMethodVersion object](#authentication-method-version) table.
> >
> > * `challengeMethodInfo` (ChallengeMethodInfo)
> >
> >   You can find more information in the [ChallengeMethodInfo object](#challenge-method-info) table.
> >
> > * `challengeMethodSet` (AuthenticationMethodSet)
> >
> >   You can find more information in the [AuthenticationMethodSet object](#authentication-method-set) table.
> >
> > * `methodPrompt` (MethodPrompt)
> >
> >   You can find more information in the [MethodPrompt object](#method-prompt) table.
> >
> > * `nameValuePair` (NameValuePair)
> >
> >   You can find more information in the [NameValuePair object](#name-value-pair) table.
>
> > **Collapse: Actions**
> >
> > * `selectChallengeMethod`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > The user needs to select a Cloud Authentication Service challenge method.

#### `SECURID_CAS_APPROVE_METHOD_PENDING_VERIFICATION`

> **Collapse: State details**
>
> > **Collapse: Response model**
> >
> > * `responseCode` (string)
> >
> >   The response status code of the Approve method authentication request.
> >
> > * `reasonCode` (string)
> >
> >   The reason status code of the Approve method authentication request.
> >
> > * `selectionCode` (string)
> >
> >   The optional selection code needed to approve Selection-based Approve requests.
>
> > **Collapse: Actions**
> >
> > * `poll`
> >
> > * `useAlternateMethod`
> >
> > * `cancel`
>
> > **Collapse: Description**
> >
> > The SecurID Cloud Authentication Service Approve method request has been initiated and is pending verification.

### Action models

#### `cancel`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > There is no model for this action.
>
> > **Collapse: Description**
> >
> > Cancels the current operation.

#### `checkNextTokencode`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > * `tokencode` (string) (required)
> >
> >   The tokencode used for authentication.
>
> > **Collapse: Description**
> >
> > Wait until the tokencode changes, then enter the next tokencode.

#### `checkCredential`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > * `username` (string) (required)
> >
> >   Username for authentication.
> >
> > * `passcode` (string)
> >
> >   Passcode for authentication
> >
> >   |   |                                                                                                                                                                                                                                                          |
> >   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> >   |   | The `passcode` field was deprecated in the 4.0 release. In this context, deprecated just means that `passcode` is now an optional field when using the `checkCredential` action. However, best practice is to use the `validatePasscode` action instead. |
>
> > **Collapse: Errors**
> >
> > * Error: `VALIDATION_ERROR`
> >
> >   ErrorDetail: `USERNAME_REQUIRED`, `INVALID_USERNAME`
>
> > **Collapse: Description**
> >
> > Authenticate using your SecurID credential.

#### `checkPasscode`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > * `passcode` (string) (required)
> >
> >   Passcode used for authentication.
>
> > **Collapse: Description**
> >
> > Reauthenticate using the passcode. Wait until the passcode changes, then enter the next passcode.

#### `checkTokencode`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > * `tokencode` (string) (required)
> >
> >   The tokencode used for authentication.
>
> > **Collapse: Description**
> >
> > Enter the SecurID Authenticate OTP code.

#### `continue`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > There is no model for this action.
>
> > **Collapse: Description**
> >
> > Continue the current operation.

#### `poll`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > There is no model for this action.
>
> > **Collapse: Errors**
> >
> > * Error: `VALIDATION_ERROR`
> >
> > * Error: `REQUEST_ERROR`
>
> > **Collapse: Description**
> >
> > Poll for the status of the Approve method request.

#### `resetPin`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > * `newPin` (string) (required)
> >
> >   The new pin used for authentication.
> >
> > * `confirmPin` (string) (required)
> >
> >   Confirm the new pin used for authentication.
>
> > **Collapse: Errors**
> >
> > * Error: `VALIDATION_ERROR`
> >
> >   ErrorDetail: `PIN_MISMATCH`, `INVALID_PIN`
>
> > **Collapse: Description**
> >
> > Reset the pin used for getting passcode.

#### `selectChallengeMethod`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > * `input` (string)
> >
> >   The challenge method to proceed with authentication. Supported methods include `SECURID`, `APPROVE`, and `TOKEN`.
>
> > **Collapse: Errors**
> >
> > * Error: `VALIDATION_ERROR`
> >
> >   ErrorDetail: `UNEXPECTED_METHOD`
>
> > **Collapse: Description**
> >
> > Select the challenge method.

#### `useAlternateMethod`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > There is no model for this action.
>
> > **Collapse: Errors**
> >
> > * Error: `VALIDATION_ERROR`
> >
> > * Error: `INVALID_REQUEST`
>
> > **Collapse: Description**
> >
> > Use an alternate authentication method.

#### `validatePasscode`

> **Collapse: Action details**
>
> > **Collapse: Request model**
> >
> > * `passcode` (string) (required)
> >
> >   The passcode used for authentication.
>
> > **Collapse: Description**
> >
> > Authenticate using the passcode.

### Objects

#### AuthenticationMethod object

> **Collapse: Object details**
>
> | Parameter Name  | Type                                                                               | Description                                                 |
> | --------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------- |
> | **methodId**    | String                                                                             | The ID of the authentication method.                        |
> | **displayName** | String                                                                             | The authentication method's name, as displayed to the user. |
> | **priority**    | Integer                                                                            | The authentication method's priority.                       |
> | **versions**    | An array of [AuthenticationMethodVersion objects](#authentication-method-version). | The versions associated with this authentication method.    |

#### AuthenticationMethodVersion object

> **Collapse: Object details**
>
> | Parameter Name       | Type                                                   | Description                                                            |
> | -------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------- |
> | **versionId**        | String                                                 | The ID of the authentication method version.                           |
> | **methodAttributes** | An array of [NameValuePair objects](#name-value-pair). | The attributes associated with this authentication method version.     |
> | **valueRequired**    | Boolean                                                | Indicates whether the authentication method version must be specified. |
> | **referenceId**      | String                                                 | The ID used to refer to the authentication method.                     |
> | **prompt**           | A [MethodPrompt object](#method-prompt).               | The prompts associated with this authentication method version.        |

#### ChallengeMethodInfo object

> **Collapse: Object details**
>
> | Parameter Name              | Type                         | Description                                                                                                                                                                                                                                                      |
> | --------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **methodId**                | String                       | Specifies the method to verify.                                                                                                                                                                                                                                  |
> | **methodPromptDefaultText** | String                       | Provides a text prompt for the user to collect the data that must be provided to complete authentication.                                                                                                                                                        |
> | **methodAvailable**         | Boolean                      | Indicates whether the method is available. The value is `false` until the user registers a device or method.                                                                                                                                                     |
> | **challengeMethodSet**      | A ChallengeMethodSet object. | A [ChallengeMethodSet object](#challenge-method-set), as received from RSA Authentication Manager.You can find internal details in the [RSA Authentication API Developer's Guide](https://community.rsa.com/s/rsa-securid-documentation/mfa-authentication-api). |

#### ChallengeMethodSet object

> **Collapse: Object details**
>
> | Parameter Name      | Type                                                                | Description                                                                       |
> | ------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
> | **methodSetId**     | String                                                              | The ID of the ChallengeMethodSet object received from RSA Authentication Manager. |
> | **requiredMethods** | An array of [AuthenticationMethod objects](#authentication-method). | The methods that can be used to complete the authentication challenge.            |

#### MethodPrompt object

> **Collapse: Object details**
>
> | Parameter Name          | Type    | Description                                                                                          |
> | ----------------------- | ------- | ---------------------------------------------------------------------------------------------------- |
> | **promptResourceId**    | String  | The prompt ID.                                                                                       |
> | **defaultText**         | String  | The text displayed to the user regarding the data that must be collected to complete authentication. |
> | **formatRegex**         | String  | The Regex format of the prompt.                                                                      |
> | **defaultValue**        | String  | The default method.                                                                                  |
> | **valueBeingDefined**   | Boolean | Indicates whether the user must enter a value.                                                       |
> | **sensitive**           | Boolean | Indicates whether the prompt requires sensitive information.                                         |
> | **minLength**           | Integer | The minimum number of characters the user's response must contain.                                   |
> | **maxLength**           | Integer | The maximum number of characters the user's response can contain.                                    |
> | **promptArgs**          | Array   | The prompt arguments.                                                                                |
> | **subjectNameRequired** | Boolean | Indicates whether the subject name is required.                                                      |

#### NameValuePair object

> **Collapse: Object details**
>
> | Parameter Name | Type   | Description                                           |
> | -------------- | ------ | ----------------------------------------------------- |
> | **name**       | String | The attribute name.                                   |
> | **value**      | String | The attribute value.                                  |
> | **dataType**   | String | The type of data associated with the attribute value. |

### Error codes

The PingFederate Authentication API returns an error code if the call flow state hasn't reached a dead end and the user can still authenticate with a device.

#### Top level error codes

> **Collapse: Error code details**
>
> | Error code         | Message                                                                       | HTTP status |
> | ------------------ | ----------------------------------------------------------------------------- | ----------- |
> | `VALIDATION_ERROR` | One or more validation errors occurred.                                       | `400`       |
> | `REQUEST_FAILED`   | The request couldn't be completed. There was an issue processing the request. | `400`       |
> | `INVALID_REQUEST`  | The request was malformed or invalid.                                         | `400`       |

#### Detail level error codes

> **Collapse: Error code details**
>
> | Error code          | Message                                                                                        | Parent code        |
> | ------------------- | ---------------------------------------------------------------------------------------------- | ------------------ |
> | `USERNAME_REQUIRED` | Username is required.                                                                          | `VALIDATION_ERROR` |
> | `INVALID_USERNAME`  | Username isn't necessary for two-factor authentication.                                        | `VALIDATION_ERROR` |
> | `PIN_MISMATCH`      | The two entered pins don't match.                                                              | `VALIDATION_ERROR` |
> | `INVALID_PIN`       | The entered pin is invalid.                                                                    | `VALIDATION_ERROR` |
> | `UNEXPECTED_METHOD` | The provided authentication method is invalid, unavailable, or the adapter doesn't support it. | `VALIDATION_ERROR` |

---

---
title: Registering PingFederate as an agent in the RSA Security Console
description: To process sign-on requests, PingFederate requires access to the RSA Authentication API. You can grant access in the RSA Security Console.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_registering_pf_as_an_agent_in_the_rsa_security_console
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_registering_pf_as_an_agent_in_the_rsa_security_console.html
revdate: June 21, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Registering PingFederate as an agent in the RSA Security Console

To process sign-on requests, PingFederate requires access to the RSA Authentication API. You can grant access in the RSA Security Console.

## About this task

You can find more information about registering authentication agents in [Add an Authentication Agent](https://community.rsa.com/docs/DOC-77208) in the RSA Authentication Manager documentation.

## Steps

1. Sign on to the RSA Security Console.

2. Go to **Access > Authentication Agents > Add new**.

3. In the **Authentication Agent Basics** section, in the **Hostname** field, enter a unique name of your choosing, such as `MyPingFederate`. Click **Save**.

4. If your RSA Authentication Manager uses a self-signed certificate, add it as a trusted certificate authority (CA) in PingFederate.

   1. Export the certificate by following the steps in [How to export RSA SecurID Access Authentication Manager Root Certificate](https://community.rsa.com/docs/DOC-96422) in the RSA Authentication Manager documentation.

   2. In the PingFederate administrative console, on the **Security > Trusted CAs** screen, import the certificate. Click **Save**.

---

---
title: RSA SecurID Cloud Authentication Integration Guide
description: This guide describes how to configure PingFederate and the RSA SecurID Cloud Authentication Service for multi-factor authentication (MFA). Because this integration uses a standard SAML configuration, you don't need to download additional software.
component: rsa
page_id: rsa:rsa_securid_cloud_authentication_integration_guide:pf_rsa_cloudauthentication_integration
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_cloud_authentication_integration_guide/pf_rsa_cloudauthentication_integration.html
revdate: June 21, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# RSA SecurID Cloud Authentication Integration Guide

This guide describes how to configure PingFederate and the RSA SecurID Cloud Authentication Service for multi-factor authentication (MFA). Because this integration uses a standard SAML configuration, you don't need to download additional software.

## Features

* Supports MFA for users with RSA SecurID passcodes, hardware tokens, and software tokens

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* The following sections of the RSA SecurID documentation

  * [RSA SecurID Access Overview](https://community.rsa.com/t5/rsa-securid-access-cloud/rsa-securid-access-overview/ta-p/568875)

  * [Ping Identity Corporation - Technology Integrations](https://community.rsa.com/t5/rsa-ready-documentation/ping-identity-corporation-technology-integrations/ta-p/570037)

  * [Ping Identity PingFederate 10 - RSA SecurID Access Implementation Guide](https://community.rsa.com/s/article/Ping-Identity-PingFederate-10---RSA-Ready-SecurID-Access-Implementation-Guide)

  * [Video: PingFederate SAML Integration user experience](https://community.rsa.com/t5/rsa-ready-blog/ping-identity-pingfederate-rsa-securid-access-saml-integration/ba-p/580490)

## System requirements

* PingFederate 11.3 or later

* RSA SecurID with the Cloud Authentication Service

---

---
title: RSA SecurID IdP Adapter settings reference
description: Field descriptions for the RSA SecurID IdP Adapter configuration screen.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_rsa_securid_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_rsa_securid_idp_adapter_settings_reference.html
revdate: July 5, 2024
---

# RSA SecurID IdP Adapter settings reference

Field descriptions for the RSA SecurID IdP Adapter configuration screen.

**Standard Fields**

| Field                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RSA Authentication Agent** | The unique name that you entered in the **Hostname** field in [Registering PingFederate as an agent in the RSA Security Console](pf_rsa_securid_ik_registering_pf_as_an_agent_in_the_rsa_security_console.html) , such as `MyPingFederate`. PingFederate uses this to identify itself to the RSA Authentication Manager API.&#xA;&#xA;If you've integrated the Authentication Manager with the RSA Cloud Authentication Service (CAS), you can leave this field blank if you fill out the Assurance Policy ID field instead. |
| **RSA Base API URL**         | The base URL of the primary RSA Authentication Manager including the hostname, port number and REST URL root path.For example: `https://RSA_Authentication_Manager_Hostname:REST_API_Port/mfa/v1_1`.The default REST API port is `5555`.                                                                                                                                                                                                                                                                                     |
| **RSA Access ID**            | A unique string that the RSA Authentication Manager uses to identify individual REST API client. This is required if the security key type is HMAC.                                                                                                                                                                                                                                                                                                                                                                          |
| **RSA Access Key**           | A unique string that the RSA Authentication Manager generates and uses as a shared secret with REST API clients.                                                                                                                                                                                                                                                                                                                                                                                                             |

**Advanced Fields**

| Field                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use Custom Cipher Suites**     | Cipher suites are used to send information securely when the adapter makes TLS requests to RSA Authentication Manager.**Cleared** (default) – The adapter uses all cipher suites available to the adapter. You can find a complete list in [Enum CipherSuites](https://square.github.io/okhttp//2.x/okhttp/index.html?com/squareup/okhttp/CipherSuite.html) in the OkHttp documentation.**Selected** – Restricts the adapter to the cipher suites entered in the **Custom Cipher Suites** field. This allows your organization to use only cipher suites that meet your unique security standards. Select this if your environment has special requirements.This check box is cleared by default.                                                                                            |
| **Custom Cipher Suites**         | The cipher suites that the adapter uses when **Use Custom Cipher Suites** is selected.Separate multiple ciphers with a comma. For example, `TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_AES_128_CBC_SHA256`.You can find a complete list in [Enum CipherSuites](https://square.github.io/okhttp//2.x/okhttp/index.html?com/squareup/okhttp/CipherSuite.html) in the OkHttp documentation.This field is blank by default.                                                                                                                                                                                                                                                                                                                                  |
| **Challenge Retries**            | The number of failed user authentications after which the account locking service blocks future attempts.&#xA;&#xA;To enable this feature, follow the steps in Account lockout protection in the PingFederate documentation.The default value is `5`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Security Key Type**            | The method of security key authentication to use against the RSA Authentication REST API. If Access Key is enabled, the plain key will be used. If HMAC is enabled an HMAC calculated from the Access Key, a hash of the request body, the Access ID, and other request-specific information will be used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Assurance Policy ID**          | The access policy name that's configured in the Cloud Administration Console. You can get the access policy name from your Cloud Authentication Service Super Admin.&#xA;&#xA;If you're using the RSA Authentication Manager integrated with the Cloud Authentication Service, you must enter a valid value for either the Assurance Policy ID field or the RSA Authentication Agent field.                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Logout Path**                  | Path on the PingFederate server to end a user's IdP session. Must include the initial slash. For example, `/mylogoutpath`.The value is added to the following to create the logout URL: https\://*pf\_host*:*port*/extThis field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Logout Redirect**              | The URL that the adapter redirects the user to after they log out. Applies only when **Logout Path** is set above. When provided, this URL takes precedence over any **Logout Template** specified below\.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Logout Template**              | HTML template to render after the user logs out. Applies when **Logout Path** is set above and **Logout Redirect** is blank. The template file must be located in `<pf_home>/server/default/conf/template`.The default value is: `idp.logout.success.page.template.html`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Authentication Context Value** | Additional information provided to the SP to assess the level of confidence in the assertion. This value will override the default authentication context used by the adapter.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Verify HTTPS Hostname**        | When a connection is established with RSA Authentication Manager, PingFederate matches the target host name against the names stored inside the server's X.509 certificate. This security measure ensures that PingFederate is connecting to the correct server.This check box is selected by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Override Internal User ID**    | Allows you to specify a custom user identifier attribute for authentication with RSA SecurID.By default, the adapter takes the `username` attribute from the PingFederate authentication policy and uses it for both frontend display and backend authentication with RSA Authentication Manager.To use a different attribute for backend authentication, select this check box and enter the custom attribute in the **Internal User ID Attribute** field.- Not selected (default)

  Frontend display: `username`Backend authentication: `username`

- Selected

  Frontend display: `username`Backend authentication: *\<custom attribute>*&#xA;&#xA;In either case, if no username attribute is available, the user-facing template shows an error.This check box is cleared by default. |
| **Internal User ID Attribute**   | When **Override Internal User ID** is selected, this field determines the user identifer attribute used to authenticate the user with RSA Authentication Manager.The attribute must be available in the PingFederate authentication policy. The attribute name is case sensitive.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Test Username**                | The username that's used to test the configuration on the **Actions** tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **HTML Template Prefix**         | A file prefix that identifies the customizable HTML templates that the adapter instance uses. The template files must be located in `<pf_home>/server/default/conf/template`.&#xA;&#xA;If you customize the template file names in /server/default/conf/template, make sure to use the same prefix consistently and enter that new prefix in this field.The default value is:```
RSASecurIDIdPAdapter.
```                                                                                                                                                                                                                                                                                                                                                                                   |
| **Messages Files**               | Identifies the customizable language-pack file that the adapter uses.If you customize the `rsa-securid-messages.properties` file name in the `/server/default/conf/language-packs` directory, enter the new name here.The default value is `rsa-securid-messages`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Error Message Key Prefix**     | Prefix for error messages in the language pack.The default value is `rsa.securid.error`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **API Request Timeout**          | The amount of time in milliseconds that PingFederate allows when establishing a connection with RSA Authentication Manager or waiting for a response to a request. A value of 0 disables the timeout.The default value is `5000`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Proxy Settings**               | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Custom Proxy Host**            | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Custom Proxy Port**            | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

---

---
title: RSA SecurID Integration Kit
description: The RSA SecurID Integration Kit allows PingFederate to use the RSA Authentication Manager service for multi-factor authentication (MFA). This allows PingFederate to act as an RSA Authentication Agent for on-premises deployments of RSA SecurID.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik.html
revdate: July 5, 2024
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# RSA SecurID Integration Kit

The RSA SecurID Integration Kit allows PingFederate to use the RSA Authentication Manager service for multi-factor authentication (MFA). This allows PingFederate to act as an RSA Authentication Agent for on-premises deployments of RSA SecurID.

With the RSA SecurID Integration Kit, PingFederate can authenticate users that use SecurID passcodes, hardware tokens, and software tokens for multi-factor authentication (MFA).

|   |                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This integration is for the on-premises RSA Authentication Manager. To integrate with RSA Cloud Authentication, see the [RSA SecurID Cloud Authentication Integration Guide](../rsa_securid_cloud_authentication_integration_guide/pf_rsa_cloudauthentication_integration.html). |

## Components

* RSA SecurID IdP Adapter

  * Allows PingFederate to communicate with the RSA Authentication API to process sign-on requests and other user activities supported by the templates.

* Templates

  * Allow the adapter to present information and forms to the user during the sign-on process, such as token challenges and PIN changes. You can customize the HTML portions of the templates to suit your organization's needs.

  * Allow you to modify the appearance of pages shown to the user during authentication.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

* The following sections of the RSA SecurID documentation

  * [RSA SecurID Access Overview](https://community.rsa.com/t5/rsa-securid-access-cloud/rsa-securid-access-overview/ta-p/568875)

  * [RSA Authentication Manager](https://community.rsa.com/community/products/securid/authentication-manager) in the RSA Authentication Manager documentation

## System requirements

* PingFederate 11.3 or later

* RSA Authentication Manager 8.7 SP2 or later

* RSA SecurID authenticator hardware or software tokens

---

---
title: RSA SecurID Integration Kit Changelog
description: The following is the change history for the RSA SecurID Integration Kit.
component: rsa
page_id: rsa:rsa_securid_integration_kit:pf_rsa_securid_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/rsa/rsa_securid_integration_kit/pf_rsa_securid_ik_changelog.html
revdate: February 27, 2026
section_ids:
  version-4-1-1: Version 4.1.1
  version-4-1: Version 4.1
  version-4-0-1: Version 4.0.1
  version-4-0: Version 4.0
  version-3-2-2: Version 3.2.2
  version-3-2-1: Version 3.2.1
  version-3-2: Version 3.2
  version-3-1-1: Version 3.1.1
  version-3-1: Version 3.1
  version-3-0-1: Version 3.0.1
  version-3-0: Version 3.0
  version-2-1: Version 2.1
  version-2-0: Version 2.0
  version-1-2-2: Version 1.2.2
  version-1-2-1: Version 1.2.1
  version-1-2: Version 1.2
  version-1-1: Version 1.1
  version-1-0: Version 1.0
---

# RSA SecurID Integration Kit Changelog

The following is the change history for the RSA SecurID Integration Kit.

## Version 4.1.1

Released in December 2024.

* Fixed an issue that caused the `Approve` method's push notification template to render twice.

* Fixed an issue that caused the RSA SecurID IdP Adapter to fail when using PingFederate in BC FIPS mode.

## Version 4.1

Released in April 2024.

* Added support for the `Approve` method's `Selection` mode. Support for the `Approve` method was introduced in RSA SecurID Integration Kit 4.0.

  |   |                                                                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To use `Selection` mode, you must have RSA Authentication Manager 8.7 SP2 or later, integrated with the RSA Cloud Authentication Service (CAS). You must enable the `Selection` feature in RSA CAS, and use version 4.3 or later of the RSA mobile app. |

* Added the ability to define a template file prefix and customize the pages that the adapter displays per adapter instance.

  |   |                                                                                                                                                                                                                                |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you modify a template file, rename the template file to give it a new prefix. Make sure to enter the new prefix in the **[HTML Template Prefix](pf_rsa_securid_ik_rsa_securid_idp_adapter_settings_reference.html)** field. |

## Version 4.0.1

Released in February 2024.

* Fixed an issue that caused an unavailable authentication method to display incorrectly.

* Deprecated the `challengeMethodIds` field in the PingFederate Authentication API. Learn more in the [`SECURID_CAS_CHALLENGE_METHOD_REQUIRED` state](pf_rsa_securid_ik_authentication_api_support.html#challenge-method-required).

## Version 4.0

Released in October 2023.

* Added support for the RSA Authentication Manager integrated with the RSA Cloud Authentication Service (CAS). The adapter supports the `SecurID`, `Token`, and `Approve` methods.

* Deprecated the `passcode` field in the PingFederate Authentication API. Learn more in the [`checkCredential` action](pf_rsa_securid_ik_authentication_api_support.html#check-credential).

## Version 3.2.2

Released in December 2022.

* Updated the security dependencies used by the adapter to the latest available.

## Version 3.2.1

Released in September 2021.

* Fixed two issues that caused certain authentication attempts to be logged incorrectly in `audit.log` and `server.log`.

## Version 3.2

Released in June 2021.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Improved the template files to use the PingFederate localization framework. If you have existing customizations, you need to manually modify the new `rsa-securid-messages.properties` file. You can find help customizing messages in [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

* Fixed an issue that, after upgrading the adapter, caused an error when using the admin API to bulk import an earlier version of the adapter.

* Fixed an issue where the previous adapter wouldn't fail over to its replicas when the virtual machine was running but RSA services weren't.

* Fixed a user impersonation vulnerability. You can find more information in the [SECADV026](https://support.pingidentity.com/s/article/SECADV026-RSA-SecureID-Integration-Kit-User-Impersonation) security bulletin.

## Version 3.1.1

Released in March 2021.

* Fixed an issue that caused unexpected behavior when `LockoutPeriod` was set to `0` in the account lockout settings file.

* Improved the description for the **Challenge Retries** setting in the adapter configuration.

## Version 3.1

Released in November 2020.

* Added the ability to customize the ciphers used in outbound HTTP requests to RSA SecurID.

* Improved error handling for cases where the user leaves the username or passcode field blank.

* Fixed an issue that could cause the adapter to cancel some sign-on attempts.

## Version 3.0.1

Released in October 2019.

* Fixed a serialization issue that occurred when PingFederate was used in a cluster.

## Version 3.0

Released in August 2019.

* Added support for RSA Authentication Manager 8.4.

* Added support for Java 11 by updating the adapter to use the RSA SecurID Authentication API.

* Added the ability to override the user ID attribute that is sent to the authentication API without affecting the ID shown to the user.

* Added the ability to configure failover servers for the primary RSA Authentication API endpoint.

* Added proxy connection override settings.

* Added connection read and timeout settings.

* Improved templates to support multi-factor authentication and CSRF protection.

* Improved template usability and error messages.

## Version 2.1

Released in June 2018.

* Added support for RSA Authentication Manager 8.3.

* Improved variable names in the template pages.

* Added new variables available to the template pages.

* Added configuration field to set the log level of the RSA Authentication Agent SDK.

* Added validation for user-generated PINs in the adapter and template.

## Version 2.0

Released in May 2017.

* Added support for RSA Authentication Manager 8.2.

* Removed support for versions 6.x and 7.x of RSA Authentication Manager.

* Updated the RSA SecurID IdP Adapter to use RSA Authentication Agent SDK 8.6 for Java.

## Version 1.2.2

Released in January 2017.

* Fixed an issue with configuring RSA in a clustered Windows environment.

## Version 1.2.1

Released in December 2015.

* Security fixes.

* Fixed serialization issue when token is in new PIN mode.

## Version 1.2

Released in September 2015.

* Qualified for RSA Authentication Manager 7.1 SP4.

* Updated RSA SecurID IdP Adapter for use as a second authentication factor.

* Added session state management.

## Version 1.1

Released in November 2013.

* RSA Authentication Agent API 8.1 SP2.

## Version 1.0

Released in March 2010.

* Initial Release.

---

---
title: RSA SecurID integrations
description: You can integrate PingFederate with RSA SecurID for multi-factor authentication (MFA) both in the cloud and on-premises. Both integrations support users with SecurID passcodes, hardware tokens, and software tokens.
component: rsa
page_id: rsa::pf_is_overview_of_rsa_securid_integrations
canonical_url: https://docs.pingidentity.com/integrations/rsa/pf_is_overview_of_rsa_securid_integrations.html
revdate: August 12, 2024
section_ids:
  rsa-securid-cloud-authentication-integration-guide-cloud: RSA SecurID Cloud Authentication integration guide (cloud)
  rsa-securid-integration-kit-on-premises: RSA SecurID Integration Kit (on-premises)
---

# RSA SecurID integrations

You can integrate PingFederate with RSA SecurID for multi-factor authentication (MFA) both in the cloud and on-premises. Both integrations support users with SecurID passcodes, hardware tokens, and software tokens.

## RSA SecurID Cloud Authentication integration guide (cloud)

This guide describes how to configure PingFederate and the RSA SecurID Cloud Authentication Service for MFA.

Because this integration uses a standard SAML configuration, you don't need to download additional software.

## RSA SecurID Integration Kit (on-premises)

The RSA SecurID Integration Kit allows PingFederate to use the RSA Authentication Manager service for MFA. This allows PingFederate to act as an RSA Authentication Agent for on-premises deployments of RSA SecurID.