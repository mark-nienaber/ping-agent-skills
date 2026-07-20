---
title: Choose persistent or transient federation
description: Decide between persistent federation for permanent account links or transient for temporary session links
component: pingoneaic
page_id: pingoneaic:am-saml2:choose-persistent-or-transient-federation
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/choose-persistent-or-transient-federation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["saml2-guide:persistent-or-transient-federation.adoc", "saml2-guide:choose-persistent-or-transient-federation.adoc"]
---

# Choose persistent or transient federation

In Advanced Identity Cloud, there are two ways to federate users with SAML 2.0:

* Permanently link identities with ***persistent federation***.

  Persistent federation requires an attribute value that is the same on the IdP and the SP; for example, an email address or another unique user identifier. Use this method to link accounts without user interaction.

  For more information, refer to [Link identities automatically based on an attribute value](auto-federation.html#auto-federate-based-on-attribute).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | When accounts are persistently linked, authentication is required **only** by the IdP. Authentication *is* required on the SP side if the SP is unable to map the identity in the assertion from the IdP to a local user account. This can happen the first time accounts are linked, for example, after which the persistent identifier establishes the mapping. When the mapping is established, authentication is required only by the IdP. |

* Maintain no user account on the SP with ***transient federation***.

  Transient federation can be useful when the SP needs no user-specific account to provide a service or when you do not want to retain a user profile on the SP, but you make authorization decisions based on attribute values from the IdP.

  When accounts are transiently linked, authentication to the SP might be required.

  The SP must authenticate the user for every SAML assertion received. This is due to the identifier being used to link identities in a transient way. It doesn't provide a repeatable, durable means to link the identities.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can prevent the ability to link accounts persistently.For an SP, set the `Disable NameID Persistence` property to `true` in the NameID Format section of the Assertion Content tab. For more information, refer to [SP assertion content](saml2-reference.html#sp-assertion-content).For an IdP, set the `Disable NameID Persistence` to `true` in the Account Mapper section of the Assertion processing tab. For more information, refer to [IdP assertion processing](saml2-reference.html#idp-assertion-processing). |

Once you choose how you federate users, enable [persistent](enable-persistent-federation.html) or [transient](enable-transient-federation.html) federation.

---

---
title: Configure IdPs and SPs with journeys
description: Configure IdPs and SPs to redirect to authentication journeys for SAML 2.0 flows
component: pingoneaic
page_id: pingoneaic:am-saml2:configure-providers
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/configure-providers.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["release-notes:rapid-channel/saml-idp-init-flows.adoc"]
section_ids:
  config-redirect-journey: Redirect to a journey on the hosted SP
  samlapp-journey: Configure a SAML 2.0 application journey for a remote SP
---

# Configure IdPs and SPs with journeys

After you've set up the entity providers, you can tailor the SAML 2.0 flow to your business needs by configuring the provider settings.

## Redirect to a journey on the hosted SP

For [IdP-initiated SSO in integrated mode](saml2-integrated-mode.html#idpinit-sso-integrated-mode), you must configure the hosted SP to send the user to an authentication journey after validating the SAML 2.0 assertion from the IdP. This lets you perform SAML 2.0 authentication on the SP side.

You can also define additional actions the user must fulfill, such as performing multi-factor authentication (MFA) or checking organizational details before accessing the SAML 2.0 application.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | Include a Scripted Decision node in the journey and query the `samlApplication` binding to access the assertion and response details. |

If a `local authentication URL` is configured, it takes precedence, but Advanced Identity Cloud doesn't validate that the specified journey exists on the hosted SP.

If you haven't configured a journey in either setting, an IdP-initiated SSO SAML flow results in an invalid request error.

For SP-initiated SSO, the flow continues in the originating journey, ignoring any redirect journey configured on the hosted SP.

To configure a redirect journey:

1. Under Native Consoles > Access Management, go to Applications > Federation > Entity Providers > *hosted SP*.

2. Under Assertion Processing > Redirect Tree, select the name of your authentication journey from the Redirect Tree Name list.

   Learn about the `Redirect Tree Name` property in the [hosted SP configuration](saml2-reference.html#config-redirect-tree).

3. Save your changes.

|   |                                                                                  |
| - | -------------------------------------------------------------------------------- |
|   | You can't delete a journey if it's set as the redirect journey in the hosted SP. |

## Configure a SAML 2.0 application journey for a remote SP

Configure the remote SP so that a specific authentication journey is always run for users authenticating with your SAML 2.0 app. The federation flow invokes the associated journey ignoring any existing sessions or authentication context requirements.

Learn about configuring application journeys in [Application journeys](../app-management/application-journeys.html).

---

---
title: Customize SAML 2.0
description: Customize SAML 2.0 functionality with attribute mapper, adapter, and account mapper scripts
component: pingoneaic
page_id: pingoneaic:am-saml2:customize-saml2-plugins
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/customize-saml2-plugins.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["saml2-guide:customize-saml2-plugins.adoc"]
---

# Customize SAML 2.0

Advanced Identity Cloud lets you extend SAML 2.0 functionality with scripts:

| Script type                                              | Description                                                                                         |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [IdP attribute mapper](custom-idp-attribute-mapper.html) | Customize the default IdP attribute mapper to specify the user attributes included in an assertion. |
| [IdP adapter](custom-idp-adapter.html)                   | Customize SAML responses and browser redirects.                                                     |
| [SP account mapper](custom-sp-account-mapper.html)       | Customize the mapping between user attributes and the SAML 2.0 assertion.                           |
| [SP adapter](custom-sp-adapter.html)                     | Customize configuration in the hosted SP adapter environment.                                       |
| [NameID mapper](custom-nameid-mapper.html)               | Customize the value of the NameID attribute in the SAML assertion.                                  |

---

---
title: Deployment considerations
description: SAML 2.0 deployment considerations including provider setup, attribute mapping, and session storage
component: pingoneaic
page_id: pingoneaic:am-saml2:saml2-configuration
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-configuration.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Setup &amp; Configuration", "Planning"]
page_aliases: ["saml2-guide:saml2-configuration.adoc"]
section_ids:
  saml2-and-session-state: SSO and session storage
  configure_saml_v2_0: Configure SAML v2.0
---

# Deployment considerations

Before you set up SAML 2.0 in Advanced Identity Cloud, you should:

* Know which providers will participate in circles of trust (CoTs).

* Know how tenants act as IdPs or SPs.

* Define how to map shared user attributes in identity information exchanged with other participants in a CoT. Advanced Identity Cloud user profile attribute names should map to user profile attribute names at other providers.

  For example, if you exchange user identifiers with a partner, and your Advanced Identity Cloud attribute is `uid`, but the partner's attribute is `userid`, you must map `uid` to the partner's `userid` attribute.

* Agree with other providers on a synchronized time service.

## SSO and session storage

SAML 2.0 functionality uses a combination of the backend token service and browser-based data to store the progress of SAML 2.0 single sign-on (SSO) operations.

SSO progress is stored in a JSON web token (JWT) in the browser's session storage.

The JWT created in the browser's session storage doesn't expire. Instead, the time allowed to complete the SSO flow is determined by the configurable [maximum duration](../am-authentication/suspended-auth.html#maximum-duration) of the journey session.

The browser must [support the sessionStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API#window.sessionstorage) to handle SSO without the need for sticky load balancing of the Advanced Identity Cloud tenant.

Session storage is similar to local storage but is more limited:

* Session storage exists only within the current browser tab.

* Another tab that displays the same page will have a different session storage.

* Session storage is shared between frames in the same tab (assuming they come from the same origin).

* Session storage data survives a page refresh, but not closing and opening the tab.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To enable session storage support in WebView components on Android, set the following property:```
settings.setDomStorageEnabled(true)
```You can't use session storage when using multiple WebView components simultaneously. Learn more in [WebSettings - setDomStorageEnabled](https://developer.android.com/reference/android/webkit/WebSettings#setDomStorageEnabled\(boolean\)) in the *Android Developers* documentation. |

## Configure SAML v2.0

The following table summarizes the high-level tasks required to configure SAML 2.0:

| Task                                                                                                                                                                                                                                                                                                                                                              | Resources                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Configure an SP, an IdP, and a CoT**Decide if Advanced Identity Cloud will be an SP, an IdP, or both, and determine what metadata you need to import from other providers.For example, if Advanced Identity Cloud is the IdP for another service, you must import the metadata of the remote SP.Ensure that SPs and IdPs that work together share the same CoT. | [Set up IdPs, SPs, and CoTs](saml2-providers-and-cots.html) |
| **Secure your providers**Configure signing and encryption secrets for your environment.                                                                                                                                                                                                                                                                           | [Sign and encrypt messages](saml2-encryption.html)          |
| **Configure your environment for SSO and SLO**Advanced Identity Cloud provides integrated and standalone modes for implementing SSO and SLO.Choose the mode that's most appropriate for your environment.                                                                                                                                                         | [Implement SSO and SLO](saml2-sso-slo.html)                 |
| **Decide how to federate identities**Advanced Identity Cloud supports different ways to federate identities, depending on the configuration and whether user profiles already exist in the SP.                                                                                                                                                                    | [Federate identities](saml2-linking-accounts.html)          |

---

---
title: Enable persistent federation
description: Enable permanent identity federation with persistent identifiers stored in user profiles
component: pingoneaic
page_id: pingoneaic:am-saml2:enable-persistent-federation
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/enable-persistent-federation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["saml2-guide:persistent-federation.adoc", "saml2-guide:enable-persistent-federation.adoc"]
section_ids:
  integrated_mode: Integrated mode
  standalone_mode: Standalone mode
  test_your_work: Test your work
  manage-persistent-federation: Manage persistent federation
  change-federation: Change federation
  initiate_change_from_the_sp: Initiate change from the SP
  initiate_change_from_the_idp: Initiate change from the IdP
  terminate_federation: Terminate federation
  initiate_termination_from_the_sp: Initiate termination from the SP
  initiate_termination_from_the_idp: Initiate termination from the IdP
---

# Enable persistent federation

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on persistent federation, refer to [Choose persistent or transient federation](choose-persistent-or-transient-federation.html). |

Both [integrated and standalone](saml2-sso-slo.html) SAML 2.0 implementations allow you to link accounts persistently.

Before you configure persistent federation, ensure you:

* Configure Advanced Identity Cloud for SAML 2.0.

* Create the [IdP](saml2-providers-and-cots.html#create-hosted-providers).

  * If Advanced Identity Cloud is the IdP, use the Advanced Identity Cloud admin console with [application management](../app-management/register-a-custom-application.html#custom-saml-app-setup-sso).

* Create [SPs](saml2-providers-and-cots.html#create-hosted-providers).

* Configure a [circle of trust (CoT)](saml2-providers-and-cots.html#create-cot).

* Configure Advanced Identity Cloud to support [SSO](saml2-sso-slo.html).

## Integrated mode

To enable persistent federation with [integrated mode](saml2-sso-slo.html):

1. Create a journey that contains the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html).

   Find an example in [SSO in integrated mode](saml2-integrated-mode.html).

2. In the NameID Format field of the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html), specify the value `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

   |   |                                                                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can link accounts using different *nameid* formats. For example, you could use the `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified` value, and receive the IdP user's e-mail address in the `NameID` value. The SP displays the login page to identify the local user account and persistently link the two accounts. |

3. Save your work.

4. Initiate SSO by accessing a URL that calls an journey that includes the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html).

   For example, `https://<tenant-env-sp-fqdn>/am/XUI/#login/&realm=alpha&service=mySAML2Tree`.

## Standalone mode

To enable persistent federation with [standalone mode](saml2-sso-slo.html):

1. Initiate SSO with `spssoinit` or `idpssoinit` URLs, including `NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` as a query parameter.

   For example, to initiate SSO from the SP, access a URL similar to the following:

   ```
   https://<tenant-env-sp-fqdn>/am/spssoinit
   ?idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fopenam
   &metaAlias=/sp
   &NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
   ```

   To initiate SSO from Advanced Identity Cloud acting as the IdP, access a URL similar to the following:

   ```
   https://<tenant-env-fqdn>/am/idpssoinit
   ?spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fopenam
   &metaAlias=/idp
   &NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
   ```

## Test your work

1. Authenticate to the IdP as the user you want to persistently link.

   On success, you are redirected to the SP.

   |   |                                                                                                                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If there was no login page displayed at the SP, you might have enabled auto-federation, or Advanced Identity Cloud was able to find a link between the two identities without requiring authentication at the SP.To ensure there are no existing links, create a new identity in the IdP, and initiate SSO again, authenticating to the IdP as the new user. |

2. Authenticate to the SP as the local user to link with.

   The accounts are persistently linked, with persistent identifiers stored in the user's profile on both the IdP and the SP.

   Subsequent attempts to access the SP only require that the user authenticates to the IdP, as the identities are now permanently linked.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can prevent the ability to persistently link accounts.For an SP, set the `Disable NameID Persistence` property to `true` in the NameID Format section of the Assertion Content tab. For more information, refer to [SP assertion content](saml2-reference.html#sp-assertion-content).For an IdP, set the `Disable NameID Persistence` to `true` in the Account Mapper section of the Assertion processing tab. For more information, refer to [IdP assertion processing](saml2-reference.html#idp-assertion-processing). |

## Manage persistent federation

When using persistent federation, you can configure and manage the federation of the persistently linked accounts.

Advanced Identity Cloud implements the SAML 2.0 Name Identifier Management profile. This lets you change a persistent identifier set to federate accounts and terminate federation for an account.

Name identifier information from identities is stored in the `sun-fm-saml2-nameid-info` and `sun-fm-saml2-nameid-infokey` attributes of a user's entry.

Advanced Identity Cloud provides two endpoints for managing persistently linked accounts:

* `IDPMniInit` for initiating changes from the IdP side

  > **Collapse: IDPMniInit parameters**
  >
  > | Parameter       | Description                                                                                                                                                                                                                                                                                                                    |
  > | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  > | `spEntityID`    | (Required) Indicate the remote SP. Make sure you URL-encode the value. For example, specify `spEntityID=\https://www.sp.com:8443/am` as `spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam`.                                                                                                                                     |
  > | `metaAlias`     | (Required) Local alias for the provider, such as `metaAlias=/myRealm/idp`. This parameter takes the format `/realm-name/provider-name` as described in [MetaAlias](saml2-reference.html#idp-metaalias).                                                                                                                        |
  > | `requestType`   | (Required) Type of manage name ID request, either `NewID` to change the ID, or `Terminate` to remove the information that links the accounts on the IdP and the SP.                                                                                                                                                            |
  > | `SPProvidedID`  | (Required if `requestType=NewID`) Name identifier in use as described previously.                                                                                                                                                                                                                                              |
  > | `affiliationID` | (Optional) Specify a SAML affiliation identifier.                                                                                                                                                                                                                                                                              |
  > | `binding`       | (Optional) Indicate which binding to use for the operation. The full, long name format is required for this parameter to work.The value must be one of the following:- `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`
  >
  > - `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect`
  >
  > - `urn:oasis:names:tc:SAML:2.0:bindings:SOAP` |
  > | `relayState`    | (Optional) Specify where to redirect the user when the process is complete. Make sure you URL-encode the value. For example, `relayState=http%3A%2F%2Fpingidentity.com` takes the user to `http://pingidentity.com`.                                                                                                           |

* `SPMniInit` for initiating changes from the SP side

  > **Collapse: SPMniInit parameters**
  >
  > | Parameter       | Description                                                                                                                                                                                                                                                                                                                    |
  > | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  > | `idpEntityID`   | (Required) Indicate the remote IdP. Make sure you URL-encode the value. For example, specify `idpEntityID=\https://www.idp.com:8443/am` as `idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam`.                                                                                                                                |
  > | `metaAlias`     | (Required) Specify the local alias for the provider, such as `metaAlias=/myRealm/sp`. This parameter takes the format `/realm-name/provider-name` as described in [MetaAlias](saml2-reference.html#sp-metaalias).                                                                                                              |
  > | `requestType`   | (Required) Type of manage name ID request, either `NewID` to change the ID, or `Terminate` to remove the information that links the accounts on the IdP and the SP.                                                                                                                                                            |
  > | `IDPProvidedID` | (Required if `requestType=NewID`) Name identifier in use as described above.                                                                                                                                                                                                                                                   |
  > | `affiliationID` | (Optional) Specify a SAML affiliation identifier.                                                                                                                                                                                                                                                                              |
  > | `binding`       | (Optional) Indicate which binding to use for the operation. The full, long name format is required for this parameter to work.The value must be one of the following:- `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`
  >
  > - `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect`
  >
  > - `urn:oasis:names:tc:SAML:2.0:bindings:SOAP` |
  > | `relayState`    | (Optional) Specify where to redirect the user when the process is complete. Make sure you URL-encode the value. For example, `relayState=http%3A%2F%2Fpingidentity.com` takes the user to `http://pingidentity.com`.                                                                                                           |

### Change federation

To change federation of persistently linked accounts, you must to get the name identifier value and initiate a change request using either the `IDPMniInit` or `SPMniInit` endpoint.

#### Initiate change from the SP

1. Get the name identifier value on the IdP side by checking the value of the `sun-fm-saml2-nameid-infokey` property.

   For example, if the user's entry in the directory shows:

   ```
   sun-fm-saml2-nameid-infokey:
     https://<tenant-env-fqdn>/am|
     https://<tenant-env-sp-fqdn>/am|
     XyfFEsr6Vixbnt0BSqIglLFMGjR2
   ```

   The name identifier on the IdP side is `XyfFEsr6Vixbnt0BSqIglLFMGjR2`.

2. Call the `/SPMniInit` endpoint to initiate a change request from the SP. Make sure you URL-encode the parameters. For example:

   ```
   https://<tenant-env-sp-fqdn>/am/SPMniInit
   ?idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fopenam
   &metaAlias=/sp
   &requestType=NewID
   &IDPProvidedID=XyfFEsr6Vixbnt0BSqIglLFMGjR2
   ```

#### Initiate change from the IdP

1. Get the name identifier value on the SP side by checking the value of `sun-fm-saml2-nameid-info`.

   For example, if the user's entry in the directory shows the following:

   ```
     sun-fm-saml2-nameid-info:
       https://<tenant-env-sp-fqdn>/am|
       https://<tenant-env-fqdn>/am|
       ATo9TSA9Y2Ln7DDrAdO3HFfH5jKD|
       https://<tenant-env-fqdn>/am|
       urn:oasis:names:tc:SAML:2.0:nameid-format:persistent|
       9B1OPy3m0ejv3fZYhlqxXmiGD24c|
       https://<tenant-env-sp-fqdn>/am|
       SPRole|false
   ```

   The name identifier on the SP side is `9B1OPy3m0ejv3fZYhlqxXmiGD24c`.

2. Call the `/IDPMniInit` endpoint to initiate a change request from the SP. Make sure you URL-encode the parameters. For example:

   ```
   https://<tenant-env-fqdn>/am/am/IDPMniInit
   ?spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam
   &metaAlias=/idp
   &requestType=NewID
   &SPProvidedID=9B1OPy3m0ejv3fZYhlqxXmiGD24c
   ```

### Terminate federation

Advanced Identity Cloud lets you terminate account federation, where the accounts have been linked with a persistent identifier, as described in [Enable persistent federation](enable-persistent-federation.html).

#### Initiate termination from the SP

Access the following URL with at least the query parameters shown.

```
https://<tenant-env-sp-fqdn>/am/SPMniInit
?idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam
&metaAlias=/sp
&requestType=Terminate
```

#### Initiate termination from the IdP

Access the following URL with at least the query parameters shown:

```
https://<tenant-env-fqdn>/am/IDPMniInit
?spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fopenam
&metaAlias=/idp
&requestType=Terminate
```

---

---
title: Enable transient federation
description: Enable temporary identity federation without maintaining user accounts on the SP
component: pingoneaic
page_id: pingoneaic:am-saml2:enable-transient-federation
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/enable-transient-federation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["saml2-guide:transient-federation.adoc", "saml2-guide:enable-transient-federation.adoc"]
section_ids:
  integrated_mode: Integrated mode
  standalone_mode: Standalone mode
  test_your_work: Test your work
---

# Enable transient federation

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on transient federation, refer to [Choose persistent or transient federation](choose-persistent-or-transient-federation.html). |

Both [integrated and standalone](saml2-sso-slo.html) SAML 2.0 implementations let you link accounts temporarily (transiently).

Before you configure transient federation, ensure you:

* Configure Advanced Identity Cloud for SAML 2.0.

* Create the [IdP](saml2-providers-and-cots.html#create-hosted-providers).

  * If Advanced Identity Cloud is the IdP, utilize the Advanced Identity Cloud admin console with [application management](../app-management/register-a-custom-application.html#custom-saml-app-setup-sso).

* Create [SPs](saml2-providers-and-cots.html#create-hosted-providers).

* Configure a [circle of trust (CoT)](saml2-providers-and-cots.html#create-cot).

* Configure Advanced Identity Cloud to support [SSO](saml2-sso-slo.html).

## Integrated mode

To enable transient federation with [integrated mode](saml2-sso-slo.html):

1. Create a journey that contains the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html).

   If you have not created one yet, refer to [SSO and SLO in Integrated Mode](saml2-integrated-mode.html) for an example.

2. In the NameID Format field, specify the value `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`.

3. Save your work.

4. Initiate SSO by accessing a URL that calls a journey that includes the SAML 2.0 node:

   For example, `https://<tenant-env-sp-fqdn>/am/XUI/#login/&realm=alpha&service=mySAMLTree`.

## Standalone mode

To enable transient federation with [standalone mode](saml2-sso-slo.html):

1. Initiate SSO with either the `/spssoinit` or `/idpssoinit` URLs, including `NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:transient` as a query parameter.

   For example, to initiate SSO from the SP, access a URL similar to the following:

   ```
   https://<tenant-env-sp-fqdn>/am/spssoinit
   ?idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fopenam
   &metaAlias=/sp
   &NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:transient
   ```

   To initiate SSO from the IdP, access a URL similar to the following:

   ```
   https://<tenant-env-fqdn>/am/idpssoinit
   ?spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fopenam
   &metaAlias=/idp
   &NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:transient
   ```

## Test your work

1. Authenticate to the IdP as the user you want to link temporarily.

   On success, you are redirected to the SP.

2. Authenticate to the SP as the local user.

   The accounts are only linked for the duration of the session. Once the user logs out, the accounts are no longer linked.

   Nothing is written in the user's profile on the IdP and the SP.

   Subsequent attempts to access the SP require the user to authenticate to the IdP *AND* the SP (assuming no existing session exists), as the identities aren't linked.

---

---
title: Federate identities
description: Federate identities through automatic linking, authentication, or shared account mapping
component: pingoneaic
page_id: pingoneaic:am-saml2:saml2-linking-accounts
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-linking-accounts.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:saml2-linking-accounts.adoc", "auto-federate-with-dynamic-creation.adoc"]
---

# Federate identities

Federation in SAML 2.0 is a necessary step that provides a seamless SSO experience to users. Federation is the agreement between an identity provider (IdP) and one or more service providers (SPs) to use the same standard. This allows the IdP and SP to share information in a trusted manner within a [circle of trust](saml2-providers-and-cots.html#create-cot).

Refer to the following table for a list of tasks to configure how Advanced Identity Cloud federates identities

| Task                                                                                                                                                                                                                                                                                                             | Resources                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Decide whether to permanently link identities**Advanced Identity Cloud lets you choose whether to maintain the link between federated entities after logout (persistent federation) or to create a new link each time the user logs in (transient federation).Also, learn how to manage persistent federation. | [Choose persistent or transient federation](choose-persistent-or-transient-federation.html) |
| **Link identities automatically**Configure Advanced Identity Cloud to link identities automatically when they exist in both the IdP and the SP.                                                                                                                                                                  | [Link identities automatically with auto-federation](auto-federation.html)                  |
| **Link identities using the authentication service**Configure Advanced Identity Cloud to link identities when the `NameID` that the IdP provides is not enough to unequivocally identify the identity.                                                                                                           | [Link identities for authentication](linking-auth-tree.html)                                |
| **Link identities in the IdP to a single, shared account on the SP**Configure Advanced Identity Cloud to link an identity in the IdP temporarily. For example, to link the `anonymous` user in the SP.                                                                                                           | [Link identities to a single, shared account](auto-federate-using-anonymous.html)           |

---

---
title: IdP adapter
description: IdP adapter scripts to customize SAML 2.0 authentication request processing and SAML responses
component: pingoneaic
page_id: pingoneaic:am-saml2:custom-idp-adapter
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/custom-idp-adapter.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Scripts"]
page_aliases: ["saml2-guide:plugins-idp-adapter.adoc", "plugins-idp-adapter.adoc"]
section_ids:
  example-idp-adapter-legacy: Redirect a journey using a legacy script
  idp-adapter-policy: Configure a policy
  create-idp-adapter: Create the script
  use-idp-adapter: Configure the IdP
  try-idp-adapter: Test the script
  example-idp-adapter-nextgen: Set a custom header using a next-generation script
  create-idp-adapter-ng: Create the script
  use-idp-adapter-ng: Configure the IdP
  try-idp-adapter-ng: Test the script
---

# IdP adapter

Use an IdP adapter script to alter the processing of the authentication request, such as to redirect the user before SSO or before sending a failure response.

* Next-generation example script

  [SAML2 IDP Adapter Script (Next Gen)](../am-scripting/sample-scripts.html#saml2-idp-adapter-nextgen-js)

* Legacy example script

  [SAML2 IDP Adapter Script](../am-scripting/sample-scripts.html#saml2-idp-adapter-js)

* Script bindings

  [IdP adapter scripting API](../am-scripting/saml2-idp-adapter-api.html)

The script provides hooks at the following points in assertion processing:

| Processing phase         | Description                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `preSingleSignOn`        | Invoked when Advanced Identity Cloud receives the authentication request. Only applicable to SP-initiated flows.                                         |
| `preAuthentication`      | Invoked before redirecting the request for authentication. Only applicable to SP-initiated flows.                                                        |
| `preSendResponse`        | Invoked after the user successfully authenticates or makes the request with an existing valid session, and before the response is sent.                  |
| `preSignResponse`        | Invoked after Advanced Identity Cloud prepares the response, but before it signs the response. This lets you customize the content of the SAML response. |
| `preSendFailureResponse` | Invoked before Advanced Identity Cloud returns a SAML error response. Only applicable to SP-initiated flows.                                             |

## Redirect a journey using a legacy script

Before you try the example, configure SSO using SAML 2.0 with Advanced Identity Cloud as the hosted IdP.

The following example determines whether to redirect the authentication journey based policy evaluation:

* [Configure a policy](#idp-adapter-policy)

* [Create the script](#create-idp-adapter)

* [Configure the IdP](#use-idp-adapter)

* [Test the script](#try-idp-adapter)

### Configure a policy

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Authorization > Resource Types and create a [new resource type](../am-authorization/resource-types-ui.html) with the following settings:

   * Name

     `SAML SP Access`

   * Pattern

     `*`

   * Action

     `Assert` (Default State: `Deny`)

2. Go to Policy Sets and create a [new policy set](../am-authorization/policy-sets-ui.html) with the following settings:

   * Id

     `saml`

   * Name

     `saml`

   * Resource Types

     `SAML SP Access`

3. Add a [new policy](../am-authorization/policies-ui.html) with the following settings:

   * Name

     `SAML Access Policy`

   * Resource Types

     `SAML SP Access`

   * Resources

     `*`

   * Actions

     `ASSERT:Denied`

   * Response Attributes

     `redirect_uri: https://example.com`

   * Subjects

     `"type": "AuthenticatedUsers"`

### Create the script

1. In the Advanced Identity Cloud admin console, [create a legacy script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type SAML2 IDP Adapter.

2. In the JavaScript field, paste the template [SAML2 IDP Adapter Script](../am-scripting/sample-scripts.html#saml2-idp-adapter-js).

3. Insert the following code in the `preSendResponse` function. The script causes Advanced Identity Cloud to redirect or send an error response if the policy for the SP evaluates to false:

   ```javascript
   function preSendResponse() {

     var frJava = JavaImporter(
       com.sun.identity.saml2.common.SAML2Exception);

     try {
       // set realm DN if you want to use an LDAP filter condition in the SAML access policy
       var env = new java.util.HashMap();
       var realmDn = new java.util.HashSet();
       realmDn.add("dc=am,dc=example,dc=com");
       env.put("am.policy.realmDN", realmDn);

       var subject = idpAdapterScriptHelper.getSubjectForToken(session);
       var resources = idpAdapterScriptHelper.getResourcesForToken(authnRequest);

       var ents = idpAdapterScriptHelper.getEntitlements(
         "saml", realm, subject, resources, env).iterator();

       while (ents.hasNext()) {
         var entitlement = ents.next();
         var isAllowed = entitlement.getActionValue("Assert");

         if (isAllowed != null && isAllowed == true) {
           return false;
         } else {
           var redirectUris = entitlement.getAttributes().get("redirect_uri");

           if (redirectUris == null || redirectUris.isEmpty()) {
             logger.error("No redirect_uri");
             response.sendError(403);
           } else {
             var redirectUri = redirectUris.iterator().next();
             response.sendRedirect(redirectUri);
           } return true;
         }
       }
     } catch (error) {
       logger.error("Error in preSend reponse. " + error);
       throw new frJava.SAML2Exception(error);
     }
   }
   ```

4. Save your changes and close the editor.

### Configure the IdP

1. Under Native Consoles > Access Management, go to Applications > Federation > Entity Providers > *Hosted IDP Name* > Advanced.

2. In the IDP Adapter Script field, select your script.

3. Save your changes.

### Test the script

1. Perform an SP-initiated flow.

2. Verify the user is redirected to the `redirect_uri` from the policy (`https://example.com`).

## Set a custom header using a next-generation script

The following example sets a custom header using the next-generation binding, `responseHelper`:

* [Create the script](#create-idp-adapter-ng)

* [Configure the IdP](#use-idp-adapter-ng)

* [Test the script](#try-idp-adapter-ng)

### Create the script

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type SAML2 IDP Adapter.

2. On the Choose Script Engine page, select Next Generation, enter a name for your script, and click Create.

3. In the JavaScript field, paste the template [SAML2 IDP Adapter Script (Next Gen)](../am-scripting/sample-scripts.html#saml2-idp-adapter-nextgen-js).

4. Replace the `preSendFailureResponse` function with the following script:

   ```java
   function preSendFailureResponse() {
     // set custom header in event of failure
     try {
       if (responseHelper) {
         responseHelper.setHeader("CUSTOM-SAML-FAILURE", "true");
       }
     } catch (e) {
       logger.error("Error in preSendFailureResponse: " + e.message);
     }

     logger.error("CUSTOM-SAML-FAILURE response header set");
   }
   ```

5. Validate and save your changes.

### Configure the IdP

1. Configure Advanced Identity Cloud to use the updated IdP adapter script:

   1. Go to Applications > Federation > Entity Providers > *hosted IdP* > Advanced.

   2. Select your custom next-generation script from the IDP Adapter Script list.

   3. Save your changes.

### Test the script

1. Test your changes using an SP-initiated flow that ends in failure.

2. Verify that the response contains the custom header, for example:

   ```bash
   HTTP/1.1 500
   X-Frame-Options: SAMEORIGIN
   ...
   CUSTOM-SAML-FAILURE: true
   ...
   ```

---

---
title: IdP attribute mapper
description: IdP attribute mapper scripts to customize SAML 2.0 attribute values in assertions
component: pingoneaic
page_id: pingoneaic:am-saml2:custom-idp-attribute-mapper
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/custom-idp-attribute-mapper.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Scripts"]
page_aliases: ["saml2-guide:plugins-idp-attribute-mapper.adoc", "plugins-idp-attribute-mapper.adoc"]
section_ids:
  example-idp-attribute-mapper: Modify SAML attributes using a legacy script
  create-idp-attr-mapper: Create the script
  use-idp-attr-mapper: Configure the IdP
  try-idp-attr-mapper: Test the script
  example-idp-attribute-mapper-nextgen: Update username with a next-generation script
  create-idp-attr-mapper-ng: Create the script
  use-idp-attr-mapper-ng: Configure the IdP
  try-idp-attr-mapper-ng: Test the script
---

# IdP attribute mapper

Use an IdP attribute mapper script to map user-configured attributes to SAML attributes in the generated SAML assertion.

The default implementation retrieves the mapped attribute values from the user profile first. If the attribute values are missing from the user's profile, then Advanced Identity Cloud attempts to retrieve them from the authenticated session.

* Next-generation example script

  [SAML2 IDP Attribute Mapper Script (Next Gen)](../am-scripting/sample-scripts.html#saml2-idp-attribute-mapper-next-gen-js)

* Legacy example script

  [SAML2 IDP Attribute Mapper Script](../am-scripting/sample-scripts.html#saml2-idp-attribute-mapper-js)

* Script bindings

  [IdP attribute mapper scripting API](../am-scripting/saml2-idp-attribute-mapper-api.html)

## Modify SAML attributes using a legacy script

Before you try the example, configure SSO using SAML 2.0 with Advanced Identity Cloud as the hosted IdP.

The following example modifies the SAML attributes in the assertion returned by the IdP:

* [Create the script](#create-idp-attr-mapper)

* [Configure the IdP](#use-idp-attr-mapper)

* [Test the script](#try-idp-attr-mapper)

### Create the script

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type SAML2 IDP Attribute Mapper.

2. In the JavaScript field, paste the template [SAML2 IDP Attribute Mapper Script](../am-scripting/sample-scripts.html#saml2-idp-attribute-mapper-js).

3. Insert one of the following example code snippets just before `return attributes;` around line 150 to return a custom static attribute:

   * Add a static single-value attribute:

     ```javascript
     var customSet = new java.util.HashSet();
     customSet.add("test");
     attributes.add(
       idpAttributeMapperScriptHelper.createSAMLAttribute(
         "customSAMLAttribute", null, customSet));
     ```

   * Add a static multi-value attribute:

     ```javascript
     var customSet = new java.util.HashSet();
     var attributes = new java.util.ArrayList();
     customSet.add("test1");
     customSet.add("test2");
     customSet.add("test3");
     attributes.add(
       idpAttributeMapperScriptHelper.createSAMLAttribute(
         "customMultiValueAttribute", null, customSet));
     ```

4. Save your changes and close the editor.

### Configure the IdP

1. Under Native Consoles > Access Management, go to Applications > Federation > Entity Providers > *Hosted IDP Name* > Assertion Processing.

2. In the Attribute Mapper Script field, select your custom script.

3. Save your changes.

### Test the script

1. Perform a SAML 2.0 flow.

2. Verify the `AttributeStatement` element in the SAML assertion contains the custom attribute.

   * Example single-value attribute assertion:

     ```xml
     <saml:AttributeStatement>
       <saml:Attribute Name="customSAMLAttribute">
         <saml:AttributeValue
           xmlns:xs="http://www.w3.org/2001/XMLSchema"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:type="xs:string"
         >test</saml:AttributeValue>
       </saml:Attribute>
     </saml:AttributeStatement>
     ```

   * Example multi-value attribute assertion:

     ```xml
     <saml:AttributeStatement>
       <saml:Attribute Name="customMultiValueAttribute">
         <saml:AttributeValue
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:type="xs:string">test1
         </saml:AttributeValue>
         <saml:AttributeValue
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:type="xs:string">test2
         </saml:AttributeValue>
         <saml:AttributeValue
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:type="xs:string">test3
         </saml:AttributeValue>
       </saml:Attribute>
     </saml:AttributeStatement>
     ```

## Update username with a next-generation script

Before you try the example, configure SSO using SAML 2.0 with Advanced Identity Cloud as the hosted IdP.

The following example updates the username to uppercase in the assertion returned by the IdP:

* [Create the script](#create-idp-attr-mapper-ng)

* [Configure the IdP](#use-idp-attr-mapper-ng)

* [Test the script](#try-idp-attr-mapper-ng)

### Create the script

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type SAML2 IDP Attribute Mapper.

2. On the Choose Script Engine page, select Next Generation, enter a name for your script, and click Create.

3. In the JavaScript field, add the following script:

   ```javascript
   // returns the list of attributes for the current session
   var attributes = idpAttributeMapperScriptHelper.getStandardAttributes();

   for (var attr of attributes) {
     if (attr.name === "username") {
       var upperCaseValues = [];
       for (var val of attr.values) {
         upperCaseValues.push(val.toUpperCase());
       }
       attr.values = upperCaseValues;
     }
   }
   // return the modified list of attributes
   attributes;
   ```

   |   |                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Always make sure the last line of your script is the list of the attributes to return. It must be in the following format:```json
   [
     {
       "name:": "...",
       "nameFormat": "...",
       "values": ["..."]
     },
     ...
   ]
   ``` |

4. Validate and save your changes.

### Configure the IdP

1. Configure Advanced Identity Cloud to use the updated IdP attribute mapper script:

   1. Go to Applications > Federation > Entity Providers > *hosted IdP* > Assertion Processing.

   2. Select your custom next-generation script from the Attribute Mapper Script list.

2. Map the required attributes:

   1. Add the following mapping to the Attribute Map:

      * SAML Attribute

        `username`

      * Local Attribute

        `uid`

3. Save your changes.

### Test the script

1. Test your changes using an SP-initiated flow.

2. Verify that the SAML assertion contains the updated `username` value. For example:

   ```xml
   <saml:AttributeStatement>
     <saml:Attribute Name="username">
     <saml:AttributeValue
       xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
       xmlns:xs="http://www.w3.org/2001/XMLSchema"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:type="xs:string">BJENSEN
       </saml:AttributeValue>
     </saml:Attribute>
   </saml:AttributeStatement>
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you run an [SP-initiated SSO integrated mode flow](saml2-integrated-mode.html#spinit-sso-integrated-mode), you can include a Scripted Decision node to output the assertion value using the `samlApplication` binding.Learn more in [Query SAML application and authentication request](../am-scripting/scripting-api-node.html#samlapp-binding). |

---

---
title: Implement SSO and SLO
description: Implement SAML 2.0 single sign-on and single logout using integrated and standalone modes
component: pingoneaic
page_id: pingoneaic:am-saml2:saml2-sso-slo
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-sso-slo.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:saml2-sso-slo.adoc"]
section_ids:
  integrated_and_standalone_mode: Integrated and standalone mode
---

# Implement SSO and SLO

Within SAML 2.0 you can implement single sign-on (SSO) and single logout (SLO). SLO is the ability to terminate multiple login sessions by logging out of one central place.

SSO can be initiated either from the SP or the IdP:

* SP-initiated SSO

  The SP initiates the login request.

  A common reason to choose SP-initiated SSO is the ability for end users to access specific URLs within the application immediately upon login.

  For example:

  * If a user navigates to the SP first, then the SP directs to the IdP for the login.

  * If the user already has a session on the IdP, then the IdP redirects the user back to the SP with a SAML assertion.

  * If the user doesn't have a session, they enter their credentials. After a successful login, the user is redirected back to the SP with a SAML assertion.

  * The user is allowed access to the SP application.

  Find an example use case in [Grant access to Google Workspace](saml2-introduction.html#saml2-use-case-spinit).

* IdP-initiated\_ SSO

  The IdP initiates the login to the SP.

  An IdP-initiated SSO flow can simplify the user experience by making an application appear part of the IdP's portal.

  For example:

  * The user is already logged into the IdP and clicks an application (SP) to access the application.

  * The IdP sends a SAML assertion to the SP.

  * The user is allowed access to the SP application.

  Find an example use case in [Grant access to a pension application through a workplace portal](saml2-introduction.html#saml2-use-case-idpinit).

## Integrated and standalone mode

Advanced Identity Cloud provides the following options for implementing SSO and SLO with SAML 2.0:

* Integrated mode

  This option uses nodes and journeys to integrate SAML 2.0 SSO into the Advanced Identity Cloud authentication process. SP-initiated SSO in integrated mode must use the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html).

* Standalone mode

  Access servlet URLs to initiate SSO and SLO.

  Use [standalone mode](saml2-standalone-mode.html) for any of the following reasons:

  * You want to use the SAML 2.0 Enhanced Client or Proxy (ECP) SSO profile.

  * Your IdP and SP instances are using the same domain name, for example, `mydomain.net`.

    Due to the way integrated mode tracks authentication status by using a cookie, it can't be used when both the IdP and SP share a domain name.

The following table summarizes support for SSO and SLO in integrated and standalone mode.

| Mode            | SSO          | SLO           |
| --------------- | ------------ | ------------- |
| Integrated mode | SSO only (1) | Not supported |
| Standalone mode | Supported    | Supported     |

(1) Only supported if IdP and SP instances are using different domain names.

---

---
title: Introduction to SAML 2.0
description: Introduction to SAML 2.0 federation covering identity providers, service providers, and SSO concepts
component: pingoneaic
page_id: pingoneaic:am-saml2:saml2-introduction
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-introduction.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)"]
page_aliases: ["saml2-guide:saml2-introduction.adoc"]
section_ids:
  saml_2_0_concepts: SAML 2.0 concepts
  saml2-use-case: Use cases
  saml2-use-case-spinit: Grant access to Google Workspace
  saml2-use-case-idpinit: Grant access to a pension application through a workplace portal
---

# Introduction to SAML 2.0

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | You configure and set up SAML 2.0 under Native Consoles > Access Management. |

SAML 2.0 helps organizations share, or *federate* identities and services, without having to manage the identities or credentials themselves. The credentials are managed by a single entity, known as the *identity provider* (IdP). The services are provided by *service providers* (SP). Both providers are configured to trust one another.

Advanced Identity Cloud can serve as the IdP for an SP **or** it can be the SP for an external IdP (such as Azure AD).

![A high-level overview of the SAML 2.0 participants in Advanced Identity Cloud.](_images/saml2-high-level.svg)Figure 1. Overview of SAML 2.0 in Advanced Identity Cloud

Advanced Identity Cloud uses the concept of the *circle of trust* to manage the relationship between IdPs and SPs.

## SAML 2.0 concepts

Security Assertion Markup Language (SAML) 2.0 is a standard that lets users access multiple services using only a single set of credentials. The services can be provided by different organizations, using multiple domains. In summary, SAML 2.0 provides cross-domain single sign-on (CDSSO).

**SAML 2.0 Terminology**

| Term                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **End user**                | The person who is attempting to access the resource or application. In SAML 2.0, the end user is often referred to as the *subject*.The end user uses a *user-agent*, usually a web-browser, when performing a SAML 2.0 flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Single sign-on (SSO)**    | The ability for an end user to authenticate once but gain access to multiple applications, without having to authenticate separately to each one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Single log out (SLO)**    | The ability for an end user to log out once but terminate sessions in multiple applications, without having to log out separately from each one.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Assertions**              | An assertion is a set of statements about an authenticated user that let services make authorization decisions, that is, whether to allow that user to access the service and what functionality they can use.SAML assertions are XML-formatted tokens. Assertions issued by Advanced Identity Cloud can contain the following information about an end user:1) Their attributes, such as pieces of information from the user's profile.

2) The level of authentication they have performed.                                                                                                                                                                                                                                                                                                                                                                                                |
| **Identity provider (IdP)** | The IdP is responsible for authenticating end users, managing their account, and issuing SAML assertions about them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Service provider (SP)**   | The provider of the service or application that the end user is trying to access.The SP has a trust relationship with the IdP, which enables the SP to rely on the assertions it receives from the IdP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Circle of trust (CoT)**   | A circle of trust is an Advanced Identity Cloud concept that groups at least one IdP and at least one SP who agree to share authentication information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Metadata**                | Providers in SAML 2.0 share *metadata*, which represents the configuration of the provider, as well as the mechanisms it can use to communicate with other providers.For example, the metadata may contain necessary certificates for signing verification, as well as which of the SAML 2.0 bindings are supported.Sharing metadata greatly simplifies the creation of SAML 2.0 providers in a circle of trust. Advanced Identity Cloud can import the XML-formatted metadata provided by other providers, which are referred to as *remote* providers. You can also export the metadata from providers created in your tenant, referred to as *hosted* providers.For more information about metadata, refer to [Metadata for the OASIS Security Assertion Markup Language (SAML) V2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf) in the *SAML 2.0 Standard*. |

For more information, refer to [Security Assertion Markup Language (SAML) 2.0](https://www.oasis-open.org/standards#samlv2.0).

SAML 2.0 depends on standards for describing how the providers interact and exchange information. The SAML 2.0 standards describe the messages sent between providers, how they are relayed, how they are exchanged, and common use cases.

When configuring Advanced Identity Cloud to provide single sign-on using SAML 2.0, you can:

* Map accounts from the IdP to accounts in the SP, including mapping to an anonymous user.

* Make assertions as the IdP to the SP, for example, to attest that the end user has authenticated with the IdP.

  The SP then consumes assertions from the IdP to make authorization decisions, for example to let an authenticated user complete a purchase that gets charged to the user's account at the IdP.

> **Collapse: SAML 2.0 example flow**
>
> ![A possible SAML 2.0 flow.](_images/saml2-flow.svg)
>
> Figure 2. SAML 2.0 Flow
>
> 1. An unauthenticated user attempts to access a SAML 2.0 SP.
>
> 2. The SP determines the IdP associated with the end user, and redirects the user's browser to the IdP, using an HTTP 302 Redirect message. A SAML 2.0 authentication request is included in the query string.
>
>    This is an example of *HTTP-Redirect* binding, and is the default when requesting SAML authentication by Advanced Identity Cloud. Advanced Identity Cloud also supports the *HTTP-POST* binding for processing SAML 2.0 authentication requests.
>
>    Advanced Identity Cloud provides two deployment models to support single sign-on (SSO) when contacting the SP initially. For details, refer to [Implement SSO and SLO](saml2-sso-slo.html).
>
> 3. The IdP validates the request, determines the authentication method that should be used, and authenticates the user.
>
>    The SP can include particular authentication requirements in the request, for example, to require the user to use multi-factor authentication.
>
> 4. The IdP creates a *SAML Artifact*, which contains a unique artifact ID for the SAML 2.0 response.
>
>    The IdP redirects the end user's browser to the SP, and includes the SAML Artifact in the query parameters.
>
>    |   |                                                                                                                               |
>    | - | ----------------------------------------------------------------------------------------------------------------------------- |
>    |   | The browser only has access to the artifact ID rather than the SAML response itself, reducing risk of malicious interference. |
>
> 5. The SP communicates directly with the IdP, using the SOAP protocol, to retrieve the SAML response relating to the artifact ID.
>
>    The IdP returns the SAML response, including the assertion, using the SOAP protocol, directly to the SP.
>
>    The information in the SAML response is not shared with the user agent. This is an example of *HTTP-Artifact* binding, and is the default when Advanced Identity Cloud is returning SAML assertions. Advanced Identity Cloud also supports the *HTTP-POST* binding for transmitting SAML 2.0 assertions.
>
> 6. The SP validates the SAML response and that the signature matches the public key it holds for the IdP.
>
>    Optionally, the SP can choose to create a new account locally for the user, or associate an identifier in the assertion with a user account it already has locally. Linked accounts are often referred to as a *federated identity*. For more information, refer to [Federate identities](saml2-linking-accounts.html).
>
>    |   |                                                                                                                                                                                                                                                     |
>    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | To link to an existing account, the SP might also need the end user to authenticate to the SP itself, to determine the matching local account. When the accounts are linked, the user only needs to authenticate to the IdP when requesting access. |
>
> 7. The SP can now use the information provided in the assertion, and any details in the local federated identity, to authorize the user, and decide whether to provide its services to the end user.

## Use cases

### Grant access to Google Workspace

A common use case for SAML 2.0 is to let your internal staff access and use the applications provided by Google Workspace, such as Google Docs and Google Sheets. This section highlights how Advanced Identity Cloud provides the solution.

In this scenario, Google acts as the SP, and Advanced Identity Cloud acts as the IdP for a hypothetical organization, Example.com.

1. An administrative user configures Advanced Identity Cloud as the IdP as a [custom application](../app-management/register-a-custom-application.html#custom-saml-app-template-sso).

2. The administrative user configures Google Workspace as a remote SP and provides the values that Google needs to use Advanced Identity Cloud as its IdP. For example, the login, logout, and profile management URLs, and the validation certificate.

3. The Google Workspace administrator enters the provided URLs and certificate into the Google Workspace Admin console for the domain being configured.

4. When the configuration is complete, users attempting to access a Google Workspace service are asked for their corporate email address:

   ![Provide Google with your corporate email address, so the relevant IdP can be determined.](_images/scenario-gsuite-identify-to-google.png)

5. Based on the domain of the email address, Google redirects the user to sign in to Advanced Identity Cloud, acting as the IdP.

6. After successfully authenticating with Advanced Identity Cloud, the user is redirected back to the Google Workspace application, for example, Google Docs.

   Google, acting as the SP, creates a federated identity in its systems to manage local account options, such as privacy settings. The user can now access any of the Google Workspace apps, by authenticating to Advanced Identity Cloud using their corporate Example.com account:

   ![Google Docs showing a federated identity authenticated by Advanced Identity Cloud, the trusted IdP.](_images/scenario-gsuite-federated-identity.png)

Learn more about this SAML flow in [SP-initiated SSO integrated mode flow](saml2-integrated-mode.html#spinit-sso-integrated-mode).

### Grant access to a pension application through a workplace portal

This scenario describes an employee who wants to check their pension details from their company website. The company, Example.com, provides an application dashboard to its employees, which includes an option to access their pension provider, MyPension.

An IdP-initiated SSO flow in integrated mode lets the employee authenticate with the third-party workplace portal and bypass the pension app's login page.

1. In Advanced Identity Cloud, the admin user configures MyPension as the hosted SP and imports the metadata for the remote IdP (Example.com) to create a circle of trust.

   The hosted SP configuration includes a login journey to handle the pension provider's authentication requirements, such as adding multi-factor authentication.

2. MyPension provides a URL for Example.com to embed in its website.

   Learn more about configuring this URL in [Assertion Consumer Service](saml2-reference.html#config-hosted-sp-acs).

3. The employee provides their credentials to Example.com and clicks the embedded link to the pension app in the dashboard.

4. As the IdP, Example.com authenticates the employee and redirects them to MyPension (the SP).

5. Advanced Identity Cloud, acting as the SP, validates the IdP, identifies the employee, and runs the authentication journey.

   The authentication journey verifies that the employee has the required authorization level for their organization.

6. The employee is redirected to the MyPension website and granted access to their pension details.

Learn more about this SAML flow in [IdP-initiated SSO integrated mode flow](saml2-integrated-mode.html#idpinit-sso-integrated-mode).

---

---
title: Link identities automatically with auto-federation
description: Link identities automatically based on shared attribute values between IdPs and SPs
component: pingoneaic
page_id: pingoneaic:am-saml2:auto-federation
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/auto-federation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:hosted-IDP-attribute-map-reference.adoc", "saml2-guide:auto-federation.adoc"]
section_ids:
  auto-federate-based-on-attribute: Link identities automatically based on an attribute value
  auto-federation-missing-nameid: Auto-federation when no NameID is present
---

# Link identities automatically with auto-federation

|   |                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before linking identities, you must first choose between [persistent or transient federation](choose-persistent-or-transient-federation.html). |

Advanced Identity Cloud lets you configure the SP to link identities automatically, based on an attribute value in the assertion returned from the IdP. This process is called *auto-federation*.

When the identities on both the IdP and the SP share a common attribute value, such as an email address or other unique user identifier, you can configure Advanced Identity Cloud to map the attributes to each other and link identities. The user doesn't authenticate to the SP.

## Link identities automatically based on an attribute value

You can automatically link identities based on an attribute value that is the same in both the IdP and the SP.

Before you configure auto-federation, you must perform the following tasks:

* Configure Advanced Identity Cloud for SAML 2.0.

* Create the [IdP](saml2-providers-and-cots.html#create-hosted-providers). If Advanced Identity Cloud is the IdP, use the Advanced Identity Cloud admin console with [application management](../app-management/register-a-custom-application.html#custom-saml-app-setup-sso).

* Create [SPs](saml2-providers-and-cots.html#create-hosted-providers).

* Configure a [circle of trust (CoT)](saml2-providers-and-cots.html#create-cot).

* Configure Advanced Identity Cloud to support [SSO](saml2-sso-slo.html).

Find information about these tasks in [Deployment considerations](saml2-configuration.html).

Perform the following steps on the hosted IdP(s), and again on the hosted SP(s):

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Applications > Federation > Entity Providers, and click on the name of the hosted provider.

   Advanced Identity Cloud only displays the configuration of a single role.

   To switch between an IdP and SP configuration for a given provider, select the role to view:

   ![saml-roles](_images/saml-roles.png)

2. On the hosted IdP:

   * Go to the Assertion Processing tab.

   * Review the Attribute Map configuration. If the attributes you want to use to link the accounts on the IdP and the SP are not in the map already, add them.

     The IdP sends these attributes in the assertion, and the SP maps them using its own attribute map.

     |   |                                                                                                                                                                                                                                                                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The default IdP mapping implementation lets you add static values in addition to values taken from the user profile. You add a static value by enclosing the profile attribute name in double quotes (`"`), as in the following example:![Example of Static Attribute Mapping. Notice that the static value is enclosed in double quotes.](_images/static-attr-mapping.png) |

   * Save your work.

3. On the hosted SP:

   * Go to the Assertion Processing tab.

   * Review the Attribute Map configuration, and ensure that the attribute mappings you created on the IdP are represented in the map.

     > **Collapse: Tips to configure the attribute map on the SP**
     >
     > The value of Key is a SAML attribute sent in an assertion. The value of Value is a property in the authenticated session or an attribute of the user's profile.
     >
     > By default, the SP maps the SAML attributes it receives to equivalent-named session properties. However, when the SP is configured to create identities during auto-federation and the identity doesn't exist yet, the SP maps the SAML attributes to their equivalents in the newly-created user profile.
     >
     > The special mapping `Key: *, Value: *` means that the SP maps each attribute it receives in the assertion to equivalent-named properties or attributes. For example, if the SP receives `mail` and `firstname` in the assertion, it maps them to `mail` and `firstname` respectively.
     >
     > Remove the special mapping and add key pairs to the map if:
     >
     > * During auto-federation the attributes in the IdP and SP's identity stores do not match.
     >
     > * You need control over the names of the session properties.
     >
     > * You need control over which attributes the SP should map, because the IdP adds too many to the assertion.
     >
     > For example, if the SAML attribute is `firstname` and you want the SP to map it to a session property/user profile attribute called `cn`, create a mapping similar to `Key: firstname, Value: cn`.

   * Under Auto Federation, click the Enabled toggle to enable auto-federation.

   * In the Attribute property, enter the SAML attribute name that the SP will use to link accounts, as configured in the Attribute Map.

   * Save your work.

4. To test your work, initiate SSO. Find an example described in [IdP-initiated SSO](saml2-standalone-mode.html#saml2-sso-standalone-idpssoinit).

   * Authenticate to the IdP as an existing user.

   * Attempt to access the SP.

   Notice that the user has an authenticated session and can access their profile page on the SP without having to authenticate again.

## Auto-federation when no NameID is present

By default, Advanced Identity Cloud can process SAML 2.0 assertions that don't contain a NameID.

When a NameID is absent, Advanced Identity Cloud uses the configured auto-federation attribute to resolve the user identity.

|   |                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | SLO isn't supported when NameID is missing from the assertion.The SAML 2.0 specification requires a stable subject identifier (NameID, BaseID, or EncryptedID) in a LogoutRequest. Without one, Advanced Identity Cloud can't terminate the federated session. |

If you use a scripted SP account mapper, update your script to handle a `null` NameID.

Learn more in [Handle a missing NameID in a script](custom-sp-account-mapper.html#handle-missing-nameid).

---

---
title: Link identities for authentication
description: Link SAML 2.0 identities using authentication journeys for users without auto-federation
component: pingoneaic
page_id: pingoneaic:am-saml2:linking-auth-tree
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/linking-auth-tree.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Authentication", "Accounts", "Journeys", "Scripts"]
page_aliases: ["saml2-guide:linking-auth-tree.adoc"]
section_ids:
  first_authentication_to_the_sp: First authentication to the SP
  subsequent_authentications_to_the_sp: Subsequent authentications to the SP
  saml2-integrated-mode-sso-persistent-platform: Link accounts persistently
---

# Link identities for authentication

IdPs and SPs must be able to communicate about users. In some cases, the IdP chooses to communicate a minimum of information about an authenticated user; for example, a generated, opaque `NameID` that cannot directly be used to locate to an identity in the SP identity store.

Advanced Identity Cloud can use these pseudonym identifiers for establishing links between otherwise unrelated accounts, by requiring that the user authenticates to the SP using a linking authentication mechanism.

## First authentication to the SP

The following flow shows the sequence of events that occurs when a user first attempts to authenticate to the Advanced Identity Cloud SP:

![Sequence diagram: first authentication to the SP](_images/linking-auth-tree-first-auth.svg)Figure 1. First authentication to the SP flow

1. **Accessing the SP**

   A user attempts to access a service and is redirected to Advanced Identity Cloud which acts as the SP, specifying the SAML 2.0 service in the login URL.

   For example, a journey containing the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html):

   `https://<tenant-env-sp-fqdn>/am/XUI/#login/&service=spSAMLJourney`

2. **Authentication at the IdP**

   Advanced Identity Cloud redirects the user to the IdP. The user authenticates successfully to the IdP. The IdP returns a SAML assertion to Advanced Identity Cloud.

3. **SP attempts to access a federated identity**

   Advanced Identity Cloud attempts to locate the identity in its user store but finds no link between the IdP identity and a local identity.

4. **Invocation of the linking authentication node(s)**

   Because no link is found, Advanced Identity Cloud uses the configured authentication journey to authenticate the user.

5. **Identity federation**

   After successfully authenticating the user, Advanced Identity Cloud writes the name ID from the assertion into the user's local profile, creating a permanent link between the two identities.

   For more information on creating permanent links between identities, refer to [Enable persistent federation](enable-persistent-federation.html).

   Find an example of a journey that links identities in [Create accounts dynamically during federation](saml2-integrated-mode.html#saml2-integrated-mode-sso-dynamic-platform).

## Subsequent authentications to the SP

The following flow shows the sequence of events that occurs during subsequent authentication attempts after the user's identities on the IdP and SP have been federated:

![Sequence diagram: subsequent authentications to the SP](_images/linking-auth-tree-subsequent-auth.svg)Figure 2. Subsequent authentications to the SP flow

1. **Accessing the SP**

   A returning user attempts to access their service and is redirected to Advanced Identity Cloud, which acts as the SP. Their login URL specifies the SAML 2.0 login service.

   For example, a journey containing the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html) and the [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/latest/write-federation-information.html):

   `https://<tenant-env-sp-fqdn>/am/XUI/#login/&service=spSAMLJourney`.

2. **Authentication at the IdP**

   Advanced Identity Cloud redirects the user to the IdP, and the user authenticates successfully at the IdP. The IdP returns a SAML assertion to Advanced Identity Cloud.

3. **SP attempts to access a federated identity**

   Advanced Identity Cloud attempts to locate the name ID in its user store. The search for the name ID succeeds.

   Because there's a match, the user doesn't need to authenticate to Advanced Identity Cloud and can access the service.

## Link accounts persistently

If you're not using auto-federation, perform the steps in this procedure to configure a journey, similar to the following, to link accounts persistently.

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure relies on [integrated mode SSO](saml2-sso-slo.html#integrated-mode-sso).SLO is *not* supported for this procedure. |

![Example journey to link accounts persistently](../am-authentication/_images/trees-node-write-federation-information-example.png)

1. Add a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html).

   Ensure the NameID Format specified is `persistent`.

   The node processes the assertion, makes its contents available to the journey's shared state in the `userInfo` object, and tries to map the assertion's nameID using the `uid` mapping in the SP's assertion map.

   If the node finds a match, the journey continues through the `Account Exists` output. Otherwise, the journey continues through the `No Account Exists` output.

   The attribute the node uses to map the nameID is not configurable, and this example adds nodes to process the `userInfo` object and match its contents to the managed user's schema instead.

2. Add a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) to copy the information from the assertion to the journey's shared state.

   > **Collapse: Example script**
   >
   > * Next-generation
   >
   > * Legacy
   >
   > ```javascript
   > if (nodeState.get("userInfo")) {
   >   if (nodeState.get("objectAttributes")) {
   >     nodeState.remove("objectAttributes");
   >   }
   >   var userName=null,sn=null,mail=null;
   >
   >   try {
   >     var attribs = nodeState.get("userInfo")["attributes"];
   >
   >     userName=attribs["uid"][0];
   >     sn=attribs["sn"][0];
   >     mail=attribs["mail"][0];
   >
   >   } catch (e) {
   >     logger.error("Error getting userInfo: " + e);
   >   }
   >   nodeState.putShared("username", userName);
   >   nodeState.putShared("objectAttributes", {"userName":userName,"sn":sn,"mail":mail, "givenName": userName});
   > }
   > action.goTo("true");
   > ```
   >
   > ```javascript
   > var fr = JavaImporter(org.forgerock.openam.auth.node.api.Action);
   >
   > if (nodeState.get("userInfo")) {
   >   if (nodeState.get("objectAttributes")) {
   >     nodeState.remove("objectAttributes");
   >   }
   >   var userName=null,sn=null,mail=null;
   >
   >   try {
   >     var attribs = nodeState.get("userInfo").get("attributes");
   >
   >     userName=attribs.get("uid").get(0).asString();
   >     sn=attribs.get("sn").get(0).asString();
   >     mail=attribs.get("mail").get(0).asString();
   >
   >   } catch (e) {
   >     logger.error("Error getting userInfo: " + e);
   >   }
   >   nodeState.putShared("username", userName);
   >   nodeState.putShared("objectAttributes", {"userName":userName,"sn":sn,"mail":mail, "givenName": userName});
   > }
   > action = fr.Action.goTo("true").build();
   > ```
   >
   > You can also query the `samlApplication` binding on the SP side to get the assertion.
   >
   > Learn more in the [Scripted Decision node API](../am-scripting/scripting-api-node.html).

3. Add an [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/latest/identify-existing-user.html) to search the user with the appropriate attribute.

   For example, `userName`.

4. Authenticate the user to the SP.

5. Add the [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/latest/write-federation-information.html) to the successful outcome of the authentication process to create the link between the accounts.

   If a transient link exists, it is converted into a persistent one.

---

---
title: Link identities to a single, shared account
description: Map identities to a single shared account on the SP without creating user-specific accounts
component: pingoneaic
page_id: pingoneaic:am-saml2:auto-federate-using-anonymous
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/auto-federate-using-anonymous.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Accounts"]
page_aliases: ["saml2-guide:auto-federate-using-anonymous.adoc"]
section_ids:
  link_identities_to_a_single_sp_account: Link identities to a single SP account
---

# Link identities to a single, shared account

Advanced Identity Cloud lets you map identities on the IdP temporarily to a single account on the SP (for example, the `anonymous` account). This lets you exchange attributes about the user without a user-specific account on the SP.

This approach is useful when the SP doesn't need a user-specific account to provide a service, or when you don't want to create or retain identity data on the SP, but you must make authorization decisions based on attribute values from the IdP.

## Link identities to a single SP account

Before you configure identities to link to a single account, ensure you:

* Configure Advanced Identity Cloud for SAML 2.0.

* Create the [IdP](saml2-providers-and-cots.html#create-hosted-providers).

  * If Advanced Identity Cloud is the IdP, use the Advanced Identity Cloud admin console with [application management](../app-management/register-a-custom-application.html#samlv2).

* Create [SPs](saml2-providers-and-cots.html#create-hosted-providers).

* Configure a [circle of trust (CoT)](saml2-providers-and-cots.html#create-cot).

* Configure Advanced Identity Cloud to support [SSO](saml2-sso-slo.html).

Perform the following steps:

1. On the hosted IdP:

   * Under Native Consoles > Access Management, go to Realms > *Realm Name* > Applications > Federation > Entity Providers > *Hosted IDP Name*.

   * On the Assertion Processing tab, if the attributes you want to access from the SP aren't included in the Attribute Map property, add the attribute mappings.

     Enter attribute map values using the following format: `SAML Attribute Name=Profile Attribute Name`.

   * Save your work.

2. On the hosted SP:

   * Under Native Consoles > Access Management, go to Realms > *Realm Name* > Applications > Federation > Entity Providers > *Hosted SP Name*.

   * On the Assertion Processing tab, if the attributes you want to access from the IdP are not included in the Attribute Map property, add the attribute mappings.

     Enter attribute map values using the following format: `SAML Attribute Name=Profile Attribute Name`.

     |   |                                                                                                                                                                   |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can use a special wildcard mapping of `*=*`, which maps each attribute in the assertion to an identically named attribute on the SP using the relevant value. |

   * In the Auto Federation section, ensure that Enabled is not selected.

   * In the Account Mapper > Transient User property, add the account name Advanced Identity Cloud will use to link all identities from the IdP, for example; `anonymous`.

   * Save your work.

3. To test your work:

   * Create a new user on the IdP, including values for any attributes you mapped in the providers.

   * Log out of the UI and initiate SSO using transient federation; for example, as described in [Enable transient federation](enable-transient-federation.html).

   * Authenticate to the IdP as the new user you created.

   * After successfully authenticating to the IdP, check that the identity is linked to a transient account by performing the following steps:

     * In a separate browser or private window, log in to the UI of the SP.

     * Go to Realms > *Realm Name* > Sessions.

     * Enter the transient username you configured earlier; for example, `anonymous`.

       The sessions of users who initiated SSO and who are temporarily linked to the transient user account display.

---

---
title: NameID mapper
description: NameID mapper scripts to customize the NameID attribute value in SAML 2.0 assertions
component: pingoneaic
page_id: pingoneaic:am-saml2:custom-nameid-mapper
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/custom-nameid-mapper.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Customization", "Java", "Scripts"]
page_aliases: ["release-notes:rapid-channel/custom-nameid-mapper.adoc"]
section_ids:
  demo-nameid-mapper: Demonstrate a NameID adapter
  create-nameid-mapper: Create the script
  configure-nameid-mapper: Configure the remote SP
  try-nameid-mapper: Test the script
---

# NameID mapper

Use a NameID mapper script to customize the value of the NameID attribute returned in the SAML assertion per SP.

* Next-generation example script

  [SAML2 NameID Mapper Script](../am-scripting/sample-scripts.html#saml2-nameid-mapper-js)

* Script bindings

  [NameID mapper scripting API](../am-scripting/saml2-nameid-mapper-api.html)

## Demonstrate a NameID adapter

Before you try the example, configure single sign-on using SAML 2.0 with Advanced Identity Cloud as the hosted IDP.

The following example modifies the NameID attribute in the assertion on the remote SP:

* [Create the script](#create-nameid-mapper)

* [Configure the remote SP](#configure-nameid-mapper)

* [Test the script](#try-nameid-mapper)

### Create the script

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type SAML2 NameID Mapper.

   |   |                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------- |
   |   | The NameID mapper script type is a [next-generation script](../am-scripting/next-generation-scripts.html) only. |

2. In the JavaScript field, write a script to set a custom value for the NameID attribute. For example, the following script replaces instances of `.com` with `.org` in a user's email address. Alternatively, uncomment the call to `getIdentityNameID` to set NameID to the user's first and last name.

   ```javascript
   /*
    * Retrieve nameID value from Java plugin and modify
   */
   function getModifiedNameID() {
     var nameIDValue = nameIDScriptHelper.getNameIDValue();

     if (nameIDValue.includes(".com")) {
         return nameIDValue.replace(".com", ".org");
     }
     return nameIDValue;
   }

   /*
    * Use identity binding to gather attributes
   */
   function getIdentityNameID() {
     var givenName = identity.getAttributeValues("givenName")[0];
     var lastName = identity.getAttributeValues("sn")[0];

     return givenName + "_" + lastName;
   }

   getModifiedNameID();
   //getIdentityNameID();
   ```

3. Save your changes and close the editor.

### Configure the remote SP

1. In the Advanced Identity Cloud admin console, go to Applications > *SAML App Name* > Sign On and click Show advanced settings.

2. In Application Username, select Custom.

3. Select your script from the NameId Script list.

4. Save your changes.

### Test the script

1. Test your changes using an SP-initiated flow.

2. Verify that the SAML 2.0 assertion shows an updated value, for example:

   ```xml
   <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
                NameQualifier="idp"
                SPNameQualifier="sp">bjensen@example.org</saml:NameID>
   ```

---

---
title: Reference
description: SAML 2.0 configuration reference for identity providers, service providers, and circles of trust
component: pingoneaic
page_id: pingoneaic:am-saml2:saml2-reference
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-reference.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Algorithm"]
page_aliases: ["saml2-guide:saml2-reference.adoc"]
section_ids:
  saml2-hosted-idp-configuration: Hosted IdP configuration
  idp-assertion-content: Assertion Content tab
  signing_and_encryption: Signing and Encryption
  nameid_format: NameID Format
  authentication_context: Authentication Context
  assertion_time: Assertion Time
  basic_authentication: Basic Authentication
  assertion_cache: Assertion Cache
  idp-assertion-processing: Assertion Processing tab
  attribute_mapper: Attribute Mapper
  account_mapper: Account Mapper
  local_configuration: Local Configuration
  idp-services: Services tab
  idp_service_attributes: IDP Service Attributes
  idp-advanced: Advanced tab
  sae_configuration: SAE Configuration
  ecp_configuration: ECP Configuration
  session_synchronization: Session Synchronization
  idp_finder_implementation: IDP Finder Implementation
  relay_state_url_list: Relay State URL List
  idp_adapter: IDP Adapter
  application_context: Application Context
  saml2-remote-idp-configuration: Remote IdP configuration
  remote-idp-assertion-content: Assertion Content
  signing_and_encryption_2: Signing and Encryption
  nameid_format_2: NameID Format
  secrets: Secrets
  basic_authentication_2: Basic Authentication
  client_authentication: Client Authentication
  remote-idp-services: Services tab
  idp_service_attributes_2: IDP Service Attributes
  nameid_mapping: NameID Mapping
  saml2-hosted-sp-configuration: Hosted SP configuration
  sp-assertion-content: Assertion Content tab
  signing_and_encryption_3: Signing and Encryption
  nameid_format_3: NameID Format
  authentication_context_2: Authentication Context
  assertion_time_2: Assertion Time
  basic_authentication_3: Basic Authentication
  sp-hosted-client-auth: Client Authentication
  sp-assertion-processing: Assertion Processing tab
  attribute_mapper_2: Attribute Mapper
  auto_federation: Auto Federation
  account_mapper_2: Account Mapper
  artifact_message_encoding: Artifact Message Encoding
  url: URL
  config-redirect-tree: Redirect Tree
  adapter: Adapter
  sp-services: Services tab
  sp_service_attributes: SP Service Attributes
  sp-advanced: Advanced tab
  sae_configuration_2: SAE Configuration
  ecp_configuration_2: ECP Configuration
  idp_proxy: IDP Proxy
  session_synchronization_2: Session Synchronization
  relay_state_url_list_2: Relay State URL List
  saml2-remote-sp-configuration: Remote SP configuration
  remote-sp-assertion-content: Assertion Content
  signing_and_encryption_4: Signing and Encryption
  nameid_format_4: NameID Format
  secrets_2: Secrets
  basic_authentication_4: Basic Authentication
  remote-sp-assertion-processing: Assertion Processing
  attribute_mapper_3: Attribute Mapper
  artifact_message_encoding_2: Artifact Message Encoding
  remote-sp-services: Services
  sp_service_attributes_2: SP Service Attributes
  remote-sp-advanced: Advanced settings
  request_processing: Request Processing
  sae_configuration_3: SAE Configuration
  idp_proxy_2: IDP Proxy
  config-treename: Tree Name
  application_context_2: Application Context
  saml2-cot-configuration: Circle of trust
---

# Reference

This reference covers the configuration settings for identity providers (IdPs), service providers (SPs), and circles of trust.

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can override certain global configuration settings for SAML 2.0 flows with ESVs. Learn more in [Use ESVs to override global configuration](../tenants/esvs-override-global-configuration.html). |

## Hosted IdP configuration

To edit hosted IdP settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > Federation > Entity Providers > *Provider Name*.

### Assertion Content tab

#### Signing and Encryption

* Request/Response Signing

  The parts of messages the IdP requires the SP to sign digitally.

* Encryption

  When NameID Encryption is selected, the SP must encrypt name identifier (NameID) elements.

* Secret ID and Algorithms

  * Secret ID Identifier

    By default, Advanced Identity Cloud uses the entity provider's role-specific, default global [secret IDs](../am-reference/secret-id-mappings.html). Alternatively, set an identifier for the secret ID Advanced Identity Cloud uses for this entity provider when resolving secrets. For example, when you set this to `demo`, the entity provider uses the following secret IDs:

    * `am.applications.federation.entity.providers.saml2.demo.signing`

    * `am.applications.federation.entity.providers.saml2.demo.encryption`

  * Signing Algorithm

    The algorithms the provider uses to sign the request and response attributes selected in the Request/Response Signing group.

    The provider's metadata extension lists these algorithms.

    This property has no default.

  * Digest Algorithm

    The digest algorithms the provider uses to sign the requests and responses selected in the Request/Response Signing group.

    The provider's metadata extension lists these algorithms.

    This property has no default.

  * Encryption Algorithm

    There are two types of encryption algorithms for the provider:

    * Symmetric algorithms; the provider uses these to encrypt the objects selected in the Encryption group. Select one or more AES algorithms from the drop-down list.

      Default: `http://www.w3.org/2001/04/xmlenc#aes128-cbc`

    * Asymmetric algorithms; the provider advertises this as the transport key algorithm. When SAML 2.0 token encryption is enabled, hosted providers should use the algorithm the remote provider advertises to encrypt symmetric encryption keys.

      Select one or more algorithms from the drop-down list:

      * `http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p` (default)

      * `http://www.w3.org/2009/xmlenc11#rsa-oaep`

        For this algorithm, Advanced Identity Cloud uses `http://www.w3.org/2009/xmlenc11#mgf1sha256` to create the transport key.

      * `http://www.w3.org/2001/04/xmlenc#rsa-1_5`

        For security reasons, do not use this option.

#### NameID Format

* NameID Format List

  Supported NameIDs for users shared between providers for single sign-on (SSO).

  The following diagram shows how the hosted IdP determines which NameID format to use:

  ![How the hosted IdP decides which NameID formats to use](_images/nameid-format-flow-hosted-idp.svg)

* NameID Value Map

  Maps a NameID format (Key) to a user profile attribute (Value). The `persistent` and `transient` NameID formats don't have to be mapped.

  The mapped user profile attribute must be one of the attributes listed in [User identity attributes and properties reference](../identities/user-identity-properties-attributes-reference.html). Make sure you use the AM attribute name.

  NameID mapping supports Base64-encoded binary values. Select the Binary option to Base64-encode the attribute's value before it's added to the assertion.

#### Authentication Context

* Mapper

  A class that implements the `IDPAuthnContextMapper` interface and sets up the authentication context.

  Don't edit this field.

  Default: `com.sun.identity.saml2.plugins.DefaultIDPAuthnContextMapper`

* Authentication Context

  The supported authentication context classes and any authentication mechanisms Advanced Identity Cloud uses when an SP specifies the class in a SAML 2.0 authentication request. For details, refer to [Authentication Context for the OASIS Security Assertion Markup Language (SAML) v2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-authn-context-2.0-os.pdf).

  Default: `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`

  * Context Reference

    Select from the following options to define a context reference:

    * Predefined Reference to choose from a list of supported context references.

    * Custom Reference to type your own reference to an authentication context.

  * Key

    Select an authentication mechanism from the list for Advanced Identity Cloud to use when the SP specifies an authentication context class in a SAML 2.0 request.

    > **Collapse: Authentication mechanisms**
    >
    > * Service
    >
    >   Set the Value to the authentication journey to use.
    >
    > * Module
    >
    >   Not supported.
    >
    > * User
    >
    >   Not supported.
    >
    > * Role
    >
    >   Not supported.
    >
    > * Authentication Level
    >
    >   Advanced Identity Cloud uses a method where the authentication level is greater than or equal to the Value. Match the Value field with the Level field to avoid requiring users to re-authenticate unnecessarily.
    >
    >   If more than one suitable method exists, Advanced Identity Cloud presents the available options with a `ChoiceCallback`.

  * Value

    Depends on the Key. For example, if you selected `Service`, enter the name of the journey.

  * Level

    The order of precedence for supported context reference classes as a numeric value.

    Higher numbers are stronger than lower numbers.

#### Assertion Time

* Not-Before Time Skew

  Grace period in seconds for the `NotBefore` time in assertions.

* Effective Time

  Assertion validity in seconds.

#### Basic Authentication

* Enabled, User Name, Password

  When enabled, authenticate with the specified credentials at SOAP endpoints.

#### Assertion Cache

* Enabled

  When enabled, cache assertions.

### Assertion Processing tab

#### Attribute Mapper

Extension point to map the IdP attributes included in the SAML assertion.

* Attribute Mapper

  The Java class for the default implementation, which retrieves attributes from the user profile. If the attributes are not present in the profile, retrieve attributes from the user session.

  Do not edit this field. It is not used if Attribute Mapper Script is set.

  Default: `com.sun.identity.saml2.plugins.DefaultIDPAttributeMapper`

* Attribute Mapper Script

  A JavaScript implementation of an attribute mapper.

  Select a `Saml2 IDP Attribute Mapper` script from this realm.

  For an example, refer to [saml2-idp-attribute-mapper.js](../am-scripting/sample-scripts.html#saml2-idp-attribute-mapper-js).

* Attribute Map

  Maps SAML attributes to user profile attributes or session properties.

  The default implementation also supports static values. Enclose the profile attribute name in double quotes (`"`):

  ![The static value is enclosed in double quotes.](_images/static-attr-mapping.png)

#### Account Mapper

* Account Mapper

  The Java class for the default implementation to map remote users to local user profiles.

* Disable NameID Persistence

  By default, Advanced Identity Cloud stores NameIDs the IDP issues when the NameID format is persistent (`urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`). When you set this, Advanced Identity Cloud no longer stores persistent NameIDs.

  Only enable this setting after configuring a NameID Value Mapping for persistent NameIDs; otherwise, the `ManageNameID` and the `NameIDMapping` SAML profiles no longer work with persistent NameIDs.

  Advanced Identity Cloud does not remove existing, stored account links when you enable this setting.

#### Local Configuration

* Auth URL

  If set, overrides the default UI login URL to authenticate users during federation.

  Use this setting, for example, if you have created a custom UI for federation.

  The application exposing the URL must authenticate federated users, establish their sessions, and return SSO tokens in the tenant session cookies.

  Advanced Identity Cloud must accept the cookie for the domain of the URL. If Advanced Identity Cloud uses host cookies, the FQDN of the URL must match your tenant's FQDN.

  Advanced Identity Cloud redirects users to the URL, appending a `goto` parameter. The parameter contains the URL to redirect to after authentication. The application must not override the `goto` parameter, as changing it causes federation to fail. For details, refer to [Success and failure redirection URLs](../am-authentication/redirection-url-precedence.html).

* Reverse Proxy URL

  The URL of the reverse proxy for SAML endpoints if one exists.

* External Application Logout URL

  The URL to send an HTTP POST with all cookies when receiving a logout request. Add a user session property by including it as a query string parameter named `appsessionproperty`.

### Services tab

* MetaAlias

  Read-only alias to locate the provider's entity identifier, specified as `/realm-name/provider-name`, for example: `/alpha/myIDP`.

#### IDP Service Attributes

* Artifact Resolution Service

  The endpoint to manage artifact resolution.

* Single Logout Service

  The endpoints to manage single logout (SLO) depending on the SAML binding.

* Manage NameID Service

  The endpoints to manage NameIDs depending on the SAML binding.

* Single SignOn Service

  The endpoints to manage SSO.

  These endpoints are used only for SP-initiated flows but are included as a requirement of the [SAML V 2.0 Metadata specification](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf).

* NameID Mapping

  The endpoint to manage NameID mapping.

* Assertion ID Request Service

  The endpoints to request a specific assertion by assertion ID.

### Advanced tab

#### SAE Configuration

* IDP URL

  The endpoint to manage Secure Attribute Exchange (SAE) requests.

* Application Security Configuration

  Encryption settings for SAE.

#### ECP Configuration

* IDP Session Mapper

  A Java class to find a valid session in an HTTP servlet request to an IdP with a SAML Enhanced Client or Proxy (ECP) profile.

  Do not edit this field.

#### Session Synchronization

* Enabled

  When enabled, the IdP sends backchannel SOAP logout requests to all SPs when an authenticated session times out. An authenticated session can time out after the maximum idle time or maximum session time, for example.

#### IDP Finder Implementation

* IDP Finder Implementation Class

  A Java class to find the preferred IdP for a proxied authentication request.

* IDP Finder JSP

  A JSP to present the list of IdPs to the user.

* Enable Proxy IDP Finder For All SPs

  When enabled, Advanced Identity Cloud applies the finder for all remote SPs.

#### Relay State URL List

* Relay State URL List

  List of accepted `RelayState` URLs.

  Advanced Identity Cloud validates the `RelayState` redirection URLs against this list during SLO. Advanced Identity Cloud only allows redirection to `RelayState` URLs in this list or matching the tenant domain; otherwise, a browser error occurs.

  This setting does not apply to IdP-initiated SSO as the SP validates the `RelayState` URL.

  Use the pattern matching rules in [Success and failure redirection URLs](../am-authentication/redirection-url-precedence.html) to specify URLs.

#### IDP Adapter

* IDP Adapter Class

  A Java class Advanced Identity Cloud invokes immediately before sending a SAML 2.0 response.

* IDP Adapter Script

  A JavaScript implementation of an IdP adapter.

  Select a `Saml2 IDP Adapter` script from this realm.

  Find an example script in [SAML2 IDP Adapter Script (Next Gen)](../am-scripting/sample-scripts.html#saml2-idp-adapter-js).

#### Application Context

* Enable Application Context

  When enabled, this setting makes the application context available in all SAML 2.0 flows through the `samlApplication` binding in [Scripted Decision node scripts](../am-scripting/scripting-api-node.html#samlapp-binding).

  You can override this value by setting [`Application Context Enabled`](#saml-sp-app-context-enabled) in the remote SP configuration.

## Remote IdP configuration

After you've set up a remote IdP, configure it under Native Consoles > Access Management > Realms > *Realm Name* > Applications > Federation > Entity Providers > *Provider Name*.

### Assertion Content

#### Signing and Encryption

* Request/Response Signing

  The parts of messages the IdP requires the SP to sign digitally.

* Encryption

  * NameID Encryption – When selected, the SP must encrypt NameID elements.

* Algorithms

  Select the signing, encryption and digest algorithms that the SP will use.

#### NameID Format

* NameID Format List

  Supported NameIDs for users shared between providers for single sign-on (SSO).

#### Secrets

* Secret Label Identifier – Identifier used to create a secret label for mapping to a secret in the secret store. Advanced Identity Cloud uses this label to create a specific secret label for this entity provider. The secret label takes the form `am.applications.federation.entity.providers.saml2.identifier.basicauth` where identifier is the value of Secret Label Identifier. The label can only contain characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If you change the Secret Label Identifier for a specific entity provider, any corresponding mappings are deleted, unless they're referenced by other entity providers.

#### Basic Authentication

* Enabled – Authenticate with the specified username and password when making requests to this entity provider's SOAP endpoints.

* User Name – The username with which to authenticate at SOAP endpoints.

* Password – The password with which to authenticate at SOAP endpoints.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you set a value for Secret Label Identifier, and Advanced Identity Cloud finds a mapping to this secret label in the secret store, the value of this Password field is ignored. For example, if you set the Secret Label Identifier to demo and Advanced Identity Cloud finds a secret mapping to `am.applications.federation.entity.providers.saml2.demo.basicauth`, Advanced Identity Cloud uses this secret and ignores the value of the Password field. For basic authentication, there is no *default* secret label for the realm, or globally. |

#### Client Authentication

These settings let an SP authenticate to the IdP using mutual TLS (mTLS).

When you enable client authentication for any request type in this section, you must configure a secret mapping from one of the following secret labels to a valid secret (ESV) in the secret store:

* `am.default.applications.federation.entity.providers.saml2.sp.mtls` – the global or realm-specific mapping for hosted SPs

* `am.applications.federation.entity.providers.saml2.identifier.mtls` – a mapping for a specific SP, where identifier is the value of the Secret Label Identifier you set in the Secrets panel in the SP configuration.

If you configure a global mapping, a realm-specific mapping, and a mapping for a specific SP, the order of precedence is as follows:

* Hosted SP-specific mapping

* Realm-level default

* Global default

The certificates mapped to these labels are included in the SP metadata export with `<KeyDescriptor use="signing">`.

Currently, you can enable mTLS for the following request:

* Artifact Resolve – For artifact resolution requests, the IdP instructs the SP to send a client certificate along with the request.

### Services tab

#### IDP Service Attributes

* Artifact Resolution Service

  The endpoint to manage artifact resolution.

* Single Logout Service

  The endpoints to manage SLO depending on the SAML binding.

  These endpoints are used only for SP-initiated flows but are included as a requirement of the [SAML V 2.0 Metadata specification](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf).

* Manage NameID Service

  The endpoints to manage NameIDs depending on the SAML binding.

* Single SignOn Service

  The endpoints to manage SSO.

#### NameID Mapping

* URL

  The endpoint to manage NameID mapping.

## Hosted SP configuration

To edit hosted SP settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > Federation > Entity Providers > *Provider Name*.

### Assertion Content tab

#### Signing and Encryption

* Request/Response Signing

  The parts of messages the SP requires the IdP to sign digitally.

* Encryption

  When selected, the IdP must encrypt the selected elements.

* Secret ID and Algorithms

  * Secret ID Identifier

    By default, Advanced Identity Cloud uses the entity provider's role-specific, default global secret IDs. Alternatively, set an identifier for the secret ID Advanced Identity Cloud uses for this entity provider when resolving secrets. For example, when you set this to `demo`, the entity provider uses the following secret IDs:

    * `am.applications.federation.entity.providers.saml2.demo.signing`

    * `am.applications.federation.entity.providers.saml2.demo.encryption`

  * Signing Algorithm

    The algorithms the provider uses to sign the request and response attributes selected in the Request/Response Signing group.

    The provider's metadata extension lists these algorithms.

    This property has no default.

  * Digest Algorithm

    The digest algorithms the provider uses to sign the requests and responses selected in the Request/Response Signing group.

    The provider's metadata extension lists these algorithms.

    This property has no default.

  * Encryption Algorithm

    The two types of encryption algorithms for the provider:

    * Symmetric algorithms; the provider uses these to encrypt the objects selected in the Encryption group. Select one or more AES algorithms from the drop-down list.

      Default: `http://www.w3.org/2001/04/xmlenc#aes128-cbc`

    * Asymmetric algorithms; the provider advertises this as the transport key algorithm. When SAML 2.0 token encryption is enabled, hosted providers should use the algorithm the remote provider advertises to encrypt symmetric encryption keys.

      Select one or more algorithms from the drop-down list:

      * `http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p` (default)

      * `http://www.w3.org/2009/xmlenc11#rsa-oaep`

        For this algorithm, Advanced Identity Cloud uses `http://www.w3.org/2009/xmlenc11#mgf1sha256` to create the transport key.

      * `http://www.w3.org/2001/04/xmlenc#rsa-1_5`

        For security reasons, don't use this option.

#### NameID Format

* NameID Format List

  Supported NameIDs for users shared between providers for SSO.

  The following diagram shows how the hosted SP determines which NameID format to use:

  ![How the hosted SP decides which NameID formats to use](_images/nameid-format-flow-hosted-sp.svg)

* Disable NameID Persistence

  By default, Advanced Identity Cloud stores NameIDs the IdP issues when the NameID format is persistent (`urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`) and the account manager matched a local user to the assertion. When you set this, Advanced Identity Cloud no longer stores persistent NameIDs.

  When you enable this setting, end users must authenticate locally for each SAML login.

#### Authentication Context

* Mapper

  A class that implements the `SPAuthnContextMapper` interface and maps the incoming request parameters to an authentication context.

  Don't edit this field.

  Default: `com.sun.identity.saml2.plugins.DefaultSPAuthnContextMapper`

* Authentication Context

  The authentication context maps the URI references to the IdP's supported authentication context classes to authentication levels set on the SP side.

  * Context Reference

    Select from the following options to define a context reference:

    * Predefined Reference to choose from a list of supported context references.

    * Custom Reference to type your own reference to an authentication context.

  * Level

    The order of precedence of the context reference classes as a numeric value.

    Classes with higher numbers are considered stronger than lower numbered classes. The values determine which authentication classes can be used when the SP makes an authentication request that uses a comparison attribute; for example, `minimum` or `better`.

  Learn about authentication context classes in [Authentication Context for the OASIS Security Assertion Markup Language (SAML) V2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-authn-context-2.0-os.pdf) in the *SAML V2.0 Standard*.

  Default value: `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`

* Comparison Type

  Used in conjunction with the default authentication context to specify the possible range of authentication mechanisms the IdP can choose from.

  For example, if the Comparison Type field is set to `better`, and the `PasswordProtectedTransport` authentication context class is selected in the Default Authentication Context field, the IdP must select an authentication mechanism with a higher level assigned.

  Default: `exact`

* Include Request Authentication Context

  When enabled, include the authentication context class as the requested authentication context in the SAML 2.0 authentication request.

  Default: Enabled

#### Assertion Time

* Assertion Time Skew

  Grace period in seconds for the `NotBefore` time in assertions.

#### Basic Authentication

* Enabled, User Name, Password

  When enabled, authenticate with the specified credentials at SOAP endpoints.

#### Client Authentication

* Exclude Client Certificate from Metadata

  When enabled, don't export the client certificate in the SP metadata.

### Assertion Processing tab

#### Attribute Mapper

Extension point to map the SP attributes included in the SAML assertion.

* Attribute Mapper

  The Java class for the default implementation, which sets attributes in the user profile or properties in the session.

  Don't edit this field.

  Default: `com.sun.identity.saml2.plugins.DefaultSPAttributeMapper`

* Attribute Map

  Maps SAML attributes to user profile attributes or session properties.

  The Key is a SAML attribute from the assertion. The Value is the profile attribute or session property.

  By default, the SP maps SAML attributes to session properties with the same names. When the SP creates a profile during auto-federation, the SP maps SAML attributes to the new user profile.

  The special mapping `Key: *, Value: *` maps each attribute in the assertion to a session property or profile attribute with the same name. For example, if the SP receives `mail` and `givenName` in the assertion, it maps them to `mail` and `givenName`.

  Remove the special mapping and add key pairs to the map if:

  * (Auto-federation) The attributes in the IdP's and the SP's identity stores do not match.

  * You need control over the names of the session properties.

  * You need control over the attributes to map because the IdP adds too many to the assertion.

#### Auto Federation

* Enabled

  When enabled, automatically federate the user's accounts at different providers based on the specified SAML attribute.

* Attribute

  The SAML attribute to match accounts at different providers.

#### Account Mapper

* Account Mapper

  The Java class for the default implementation to map remote users to local user profiles.

* Use Name ID as User ID

  When selected, fall back to the NameID from the assertion to find the user.

* Transient User

  When set, map all transient users from the IdP to this profile.

#### Artifact Message Encoding

* Artifact Message Encoding

  The message encoding format for artifacts.

#### URL

* Local Authentication URL

  If set, overrides the default redirect URL to use after validating the SAML 2.0 assertion from the IdP.

  Use this setting, for example, if you have created a custom UI for federation.

  In integrated mode, Advanced Identity Cloud appends query string parameters to this URL. The parameters contain details to let Advanced Identity Cloud continue the authentication journey.

  In standalone mode, Advanced Identity Cloud redirects users to the specified URL and appends a `goto` parameter, identifying the next redirect URL for the user.

  To make sure a valid tree is configured, use [Redirect Tree](#config-redirect-tree) instead. However, if configured, the value for `Local Authentication URL` overrides `Redirect Tree Name`.

* Intermediate URL

  A URL to redirect the user to after authentication but before the original URL requested.

* External Application Logout URL

  The URL to send an HTTP POST with all cookies when receiving a logout request. Add a user session property by including it as a query string parameter named `appsessionproperty`.

#### Redirect Tree

* Redirect Tree Name

  If specified, Advanced Identity Cloud redirects to this journey after validating the SAML2 assertion from the IdP.

  For IdP-initiated SSO, you must set either `Redirect Tree Name` or `Local Authentication URL`, otherwise the SP fails to process the assertion and returns an invalid request error.

  If you provide a value for both settings, Advanced Identity Cloud prioritizes `Local Authentication URL`.

  You can't delete a journey if it's set as the value for `Redirect Tree Name`.

  Find information about setting a redirect journey in [Redirect to a journey on the hosted SP](configure-providers.html#config-redirect-tree).

* Default Relay State URL

  The URL to redirect users to after completing the request. Advanced Identity Cloud uses this if the response does not specify the `RelayState`.

#### Adapter

* Adapter

  A Java class to perform application-specific processing during the federation process.

* Adapter Environment

  Environment variables Advanced Identity Cloud passes to the adapter class.

### Services tab

* MetaAlias

  Read-only alias to locate the provider's entity identifier, specified as `/realm-name/provider-name`; for example: `/alpha/mySP`.

#### SP Service Attributes

* Single Logout Service

  The endpoints to manage SLO depending on the SAML binding.

* Manage NameID Service

  The endpoints to manage NameIDs depending on the SAML binding.

- Assertion Consumer Service

  The endpoints to consume assertions, where the order corresponds to the index of the URL in the standard metadata.

  The scheme, FQDN, and port configured must exactly match the SPs settings in its metadata.

  If the base URL service is configured, Advanced Identity Cloud uses it to determine the SP's endpoint URL.

  If the URL doesn't match, the SAML 2.0 flow fails and Advanced Identity Cloud logs an `Invalid Assertion Consumer Location specified` message.

  Set the HTTP-Artifact and HTTP-POST service locations to `AuthConsumer` for [integrated mode](saml2-integrated-mode.html).

### Advanced tab

#### SAE Configuration

* SP URL

  The endpoint to manage SAE requests.

* SP Logout URL

  The SP endpoint to process global logout requests.

* Application Security Configuration

  Encryption settings for SAE.

#### ECP Configuration

* Request IDP List Finder Implementation

  A Java class to return a list of preferred IdPs trusted for the SAML ECP profile.

  Default: `com.sun.identity.saml2.plugins.ECPIDPFinder`

* Request IDP List Get Complete

  A URI reference to retrieve the complete list of IdPs if the `IDPList` element is not complete.

* Request IDP List

  A list of IdPs for the ECP client or proxy to contact. The default finder implementation uses this.

#### IDP Proxy

* IDP Proxy

  When enabled, Advanced Identity Cloud adds a `Scoping` element to the authentication request for proxying.

* Introduction

  When enabled, use introductions to find the proxy IDP.

* Proxy Count

  The maximum number of proxy identity providers.

* IDP Proxy List

  A list of URIs for preferred proxy IDPs.

#### Session Synchronization

* Enabled

  When enabled, the SP sends backchannel SOAP logout requests to all IDPs when an authenticated session times out. An authenticated session can time out after the maximum idle time or maximum session time, for example.

#### Relay State URL List

* Relay State URL List

  List of accepted `RelayState` URLs.

  Advanced Identity Cloud validates the `RelayState` redirection URLs against this list during SLO. Advanced Identity Cloud only allows redirection to `RelayState` URLs in this list or matching the tenant domain; otherwise, a browser error occurs.

  Use the pattern matching rules in [Success and failure redirection URLs](../am-authentication/redirection-url-precedence.html) to specify URLs.

## Remote SP configuration

After you've set up a remote SP, configure it under Native Consoles > Access Management > Realms > *Realm Name* > Applications > Federation > Entity Providers > *Provider Name*.

### Assertion Content

The following properties appear under the Assertion Content tab:

#### Signing and Encryption

* Request/Response Signing

  The requests and responses that the SP requires the IdP to sign digitally.

* Encryption

  The elements that the SP requires the IdP to encrypt.

  * Attribute Encryption – When selected, the IDP must encrypt SAML attributes.

  * Assertion Encryption – When selected, the IDP must encrypt SAML assertions.

  * NameID Encryption – When selected, IDP must encrypt NameID elements.

* Algorithms

  * Signing Algorithm – The signing algorithm the SP will use.

  * Digest Algorithm – The digest algorithm the SP will use.

  * Encryption Algorithm – The encryption algorithm the SP will use.

#### NameID Format

* NameID Format List – The supported name identifiers for users who are shared between providers for single sign-on.

* NameID Value Map – Map the NameID format to a user profile attribute, for example:

  `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress=mail` or `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent=objectGUID;binary`.

  * `Key` – The Name ID format to map, for example: `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`

  * `Value` – The profile attribute, for example: `mail`.

  * `Binary` – Indicates that the profile attribute is binary and should be Base64-encoded when used as the NameID value.

  If the specified NameID format is used in the protocol, the corresponding profile attribute value is used as the NameID in the Subject assertion element. This mapping overrides *all* the values defined in the NameID Value Map on the hosted IdP. For example, if a NameID Value Map is defined for the SP and a request is made with a specific NameID Format that only exists on the IdP, it will fail.

* Disable NameID Persistence Disables the storage of NameID values at the IdP when generating an assertion for this remote SP.

  Default value: `false`

#### Secrets

* Secret Label Identifier – Identifier used to create a secret label for mapping to a secret in the secret store.

  Advanced Identity Cloud uses this label to create a specific secret label for this entity provider. The secret label takes the form `am.applications.federation.entity.providers.saml2.identifier.basicauth` where identifier is the value of Secret Label Identifier. The label can only contain characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If you change the Secret Label Identifier for a specific entity provider, any corresponding mappings are deleted, unless they're referenced by other entity providers.

  |   |                                                                                                                                                                                                                                                                                |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you specify a value for Secret Label Identifier, and Advanced Identity Cloud finds a mapping to this secret label in the secret store, the value of the Password field is ignored. For basic authentication, there is no *default* secret label for the realm, or globally. |

#### Basic Authentication

* Enabled – Require authentication with the specified username and password at SOAP endpoints.

* User Name – The username used to authenticate at SOAP endpoints.

* Password – The password used to authenticate at SOAP endpoints.

  |   |                                                                                                                                                                                                                                                                                |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you specify a value for Secret Label Identifier, and Advanced Identity Cloud finds a mapping to this secret label in the secret store, the value of the Password field is ignored. For basic authentication, there is no *default* secret label for the realm, or globally. |

### Assertion Processing

#### Attribute Mapper

* Attribute Map

  Override mappings from assertion attributes to user profile attributes at the IdP.

#### Artifact Message Encoding

* Encoding

  The message encoding format for artifacts.

### Services

The following properties appear under the Services tab:

#### SP Service Attributes

* Single Logout Service

  The endpoints to manage SLO depending on the SAML binding.

* Manage NameID Service

  The endpoints to manage NameIDs depending on the SAML binding.

* Assertion Consumer Service

  The endpoints to consume assertions, where the order corresponds to the index of the URL in the standard metadata.

### Advanced settings

#### Request Processing

* Skip Endpoint Validation For Signed Requests

  When enabled, Advanced Identity Cloud doesn't verify assertion consumer service (ACS) URLs in SAML authentication requests. The ACS URL can contain dynamic query parameters, for example.

  The SAML 2.0 specification requires ACS URL verification. When you enable this, the SP must digitally sign the authentication request; in Assertion Content > Signing and Encryption > Request/Response Signing, enable Authentication Requests Signed. If Advanced Identity Cloud receives an unsigned authentication request, it returns an error.

#### SAE Configuration

* SP URL

  The endpoint to manage SAE requests.

* SP Logout URL

  The SP endpoint to process global logout requests.

#### IDP Proxy

* IDP Proxy enabled

  When enabled, authentication requests from the SP can be proxied.

* Proxy all requests

  When enabled, Advanced Identity Cloud proxies every authentication request from the SP, even if the `Scoping` element is missing.

  Set IDP Proxy enabled for this setting to take effect.

* Introduction enabled

  When enabled, use introductions to find the proxy IdP.

  This property requires a non-default *SAML2IDPProxyFRImpl* implementation.

* Use IDP Finder

  When enabled, Advanced Identity Cloud uses the IDP finder service to determine the proxy IDP.

* Proxy Count

  The maximum number of proxy identity providers. Advanced Identity Cloud sets the specified value in the `Scoping` element of proxied authentication requests.

  Enable Proxy all requests for this setting to take effect.

* IDP Proxy List

  A list of URIs for preferred proxy IdPs.

#### Tree Name

* Tree Name

  If configured, Advanced Identity Cloud redirects the remote SP to the specified journey, ignoring the configured authentication context mapper and existing sessions. The redirect contains a transaction condition advice to ensure the journey is run.

  You can access the requested authentication context and configured mappings by including a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) in the journey that queries the `samlApplication` script binding.

  |   |                                                                                                                                                                                                                                                                                                                                       |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To prevent users from authenticating directly through this journey, either for security reasons or because the journey is insufficient as a complete authentication service, configure it as a [transactional authentication journey](../am-authentication/configure-authentication-trees.html#configure-transactional-auth-journey). |

  Learn about SAML 2.0 application journeys in [Application journeys](../app-management/application-journeys.html).

#### Application Context

* Application Context Enabled

  This setting controls the availability of the application context in SAML 2.0 flows through the `samlApplication` binding in [Scripted Decision node scripts](../am-scripting/scripting-api-node.html#samlapp-binding).

  Choose from the following options:

  * Default: Inherits the value from [`Enable Application Context`](#saml-idp-enable-app-context) in the hosted IdP configuration.

  * Enabled: The application context is always available.

  * Disabled: The application context is never available.

## Circle of trust

To edit circle of trust settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > Federation > Circle of Trust > *Circle of Trust Name*.

* Name

  String to refer to the circle of trust.

  You can't change its Name after creation.

* Description

  Short description for the circle of trust.

* Status

  Whether this circle of trust is operational.

* Entity Providers

  Known hosted and remote IdPs and SPs participating in this circle of trust.

* SAML2 Writer Service URL

  SAML 2.0 service to write IdP entity identifiers to common domain cookies after successful authentication for IdP discovery; for example: `https://[.var]##_<tenant-env-fqdn>_##/am/saml2writer`.

* SAML2 Reader Service URL

  SAML 2.0 service to read ID entity identifiers from common domain cookies for IdP discovery; for example: `https://[.var]##_<tenant-env-fqdn>_##/am/saml2reader`.

---

---
title: SAML 2.0
description: SAML 2.0 concepts, configuration, and single sign-on procedures for identity federation
component: pingoneaic
page_id: pingoneaic:am-saml2:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["index.adoc", "saml2-guide:preface.adoc"]
---

# SAML 2.0

These topics cover concepts, configuration, and procedures for working with the Advanced Identity Cloud Security Assertion Markup Language (SAML) 2.0 features.

[icon: book, set=fas, size=3x]

#### [SAML 2.0](saml2-introduction.html)

Learn how Advanced Identity Cloud support SAML 2.0.

[icon: handshake, set=fas, size=3x]

#### [Configure SAML 2.0](saml2-configuration.html)

Configure Advanced Identity Cloud's SAML 2.0 support under Native Consoles > Access Management.

[icon: users, set=fas, size=3x]

#### [Configure single sign-on](saml2-sso-slo.html)

Enable SAML 2.0 single sign-on (SSO) and single logout (SLO).

---

---
title: Set up IdPs, SPs, and CoTs
description: Set up SAML 2.0 identity providers, service providers, and circles of trust with metadata management
component: pingoneaic
page_id: pingoneaic:am-saml2:saml2-providers-and-cots
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-providers-and-cots.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:saml2-providers-and-cots.adoc", "release-notes:rapid-channel/samlapp-journeys.adoc"]
section_ids:
  create-hosted-providers: Create a hosted IdP or SP
  saml2-metadata-export: Export provider metadata
  configure-remote-entity: Import a remote IdP or SP
  update-metadata: Update remote SP certificate
  create-cot: Create a circle of trust (CoT)
---

# Set up IdPs, SPs, and CoTs

To implement SAML 2.0 in Advanced Identity Cloud, you share metadata for your hosted providers with other remote providers in a circle of trust (CoT).

You must also configure remote providers by importing their metadata.

In Advanced Identity Cloud, a *hosted* provider is one served by the current Advanced Identity Cloud tenant, and a *remote* provider is one hosted elsewhere.

## Create a hosted IdP or SP

A hosted IdP or SP is a provider hosted within Advanced Identity Cloud. For example, if Advanced Identity Cloud is the authoritative source for users to a downstream application, then you would configure Advanced Identity Cloud to be a hosted IdP.

|   |                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | With [application management](../app-management/applications.html), Advanced Identity Cloud acts as a hosted IdP through intuitive screens. Learn more in [Create a custom SAML 2.0 application](../app-management/register-a-custom-application.html#samlv2). |

This procedure provides steps for creating a hosted IdP or SP:

1. In Native Consoles > Access Management, go to Realms > *Realm Name* > Dashboard, and click SAML Applications.

2. Click Add Entity Provider > Hosted.

3. Enter an Entity ID, and verify the Entity Provider Base URL value is correct.

   |   |                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Advanced Identity Cloud truncates sequences of whitespace with a single whitespace character in values such as entity IDs. For example, if `MyEntityID value` (with one space) exists already, and you add a new entity, `My Entity ID value` (same name but multiple spaces), then Advanced Identity Cloud will throw an error because the string values are treated as identical. |

   Advanced Identity Cloud uses the Entity Provider Base URL value for all SAML 2.0 related endpoints, so ensure other entities in your SAML deployment are able to access the specified URL.

4. In the Meta Aliases section, provide a URL-friendly value in either the Identity Provider Meta Alias, the Service Provider Meta Alias property, or both.

   The aliases for providers must be unique in a circle of trust and in the realm.

5. Click Create.

   The UI only displays the configuration of a single role. To switch between SP and IdP configuration for a given provider, click on the labels to select the role view:

   ![saml-roles](_images/saml-roles.png)

6. On the Assertion Processing tab, in the Attribute Mapper section, map SAML attribute names to local attribute names. The SAML attribute names are the names in an assertion.

   ![In this example, we map the SalesForce IDPEmail SAML attribute to the local mail attribute.](_images/ui-attribute-mapper-example.png)Figure 1. Mapping SAML attributes to local attributes

   The default mapping implementation has additional features beyond retrieving string attributes from the user profile:

   * Add an attribute that takes a static value by enclosing the profile attribute name in double quotes (`"`).

     For example, you can add a static SAML attribute called `partnerID` with a value of `staticPartnerIDValue` by adding `partnerID` as the SAML Attribute with `"staticPartnerIDValue"` as the Local Attribute name.

   * Select the binary option when dealing with binary attribute values; for example, values that are Base64 encoded.

   * Use the optional `Name Format Uri` property as required by the remote provider. For example, you may need to specify `urn:oasis:names:tc:SAML:2.0:attrname-format:uri`.

7. If you are adding a new attribute map, click Add. If you are updating an existing attribute map, click Update.

8. Customize any other properties as required, and click Save Changes at the bottom of the screen.

   For in-depth information about hosted IdP and SP properties, refer to:

   * [Hosted identity provider configuration properties](saml2-reference.html#saml2-hosted-idp-configuration)

   * [Hosted service provider configuration properties](saml2-reference.html#saml2-hosted-sp-configuration)

9. [Export the XML-based metadata](#saml2-metadata-export) from your hosted provider to share with other providers in your circle of trust.

## Export provider metadata

SAML 2.0 metadata is an XML document that contains the necessary information to transmit an agreement between identity providers (IdPs) and service providers (SPs). It contains information on setting up federation (through `NameID`) and specifies the locations of various services. The SAML 2.0 metadata contains settings such as endpoint URLs, supported bindings, identifiers, and public keys.

Exporting SAML 2.0 metadata from PingOne Advanced Identity Cloud lets you share metadata with other entity providers and can be useful for troubleshooting your configuration.

You can access the SAML 2.0 metadata for your entity provider in two ways:

* Over REST

  Run the following command, including an output filename, the entity provider ID, and the realm:

  ```bash
  $ curl \
  --output <metadata.xml> \
  "https://<tenant-env-fqdn>/am/ExportSamlMetadata?\
  entityid=<entityid>&realm=/<realm>"
  ```

* In a browser

  Open your tenant environment's metadata URL in a browser, specifying the entity provider ID and the realm in the following format:

  ```bash
  https://<tenant-env-fqdn>/am/ExportSamlMetadata?entityid=<entityid>&realm=/<realm>
  ```

## Import a remote IdP or SP

A remote IdP or SP is a provider outside of Advanced Identity Cloud. For example, Azure AD could be the authoritative source for a user profile in your organization. If that's the case, then Azure AD would be a remote IdP.

The following procedure provides steps for importing and configuring one or more remote IdP or SPs:

1. Get the remote IdP or SP metadata as an XML-formatted file.

2. Import the metadata in one of the following ways:

   * In the Advanced Identity Cloud admin console

     1. Go to Native Consoles > Access Management > Realms > *Realm Name* > Dashboard and click SAML Applications.

     2. Click the Add Entity Provider drop-down button, and click Remote.

     3. On the New Remote Entity Provider page, either:

        * Drag and drop the XML file into the box, or

        * Click the box to open a file browser and select the XML file.

     4. If you have already [created a circle of trust](#create-cot), you can add the remote providers into one or more of them by using the Circles of Trust property.

     5. Leave the Update Type as empty or set to `CREATE`.

     6. Click Create.

   * Over REST

     1. Convert the XML metadata to a base64url-encoded string.

     2. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).

     3. Run the following command, specifying the access token and the base64url-encoded metadata:

        ```bash
        $ curl \
        --request POST \
        --header 'authorization: Bearer <access-token>' \
        --header 'Content-Type: application/json' \
        --header 'Accept-API-Version: resource=1.0' \
        --data-raw '{"standardMetadata": "<base64url-encoded metadata>"}' \
        'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/saml2/remote?_action=importEntity'
        ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can import multiple remote entities in a single operation as long as the entity IDs are unique.Advanced Identity Cloud truncates sequences of whitespace with a single whitespace character in values such as entity IDs. For example, if `ID value` (with one space) exists already, a new entity with the same name but multiple spaces would result in an error because the string values are treated as identical. |

3. To edit the configuration of an entity provider, go to Realms > *Realm Name* > Applications > Federation > Entity Providers, and select the entity provider to edit.

   The UI only displays the configuration of a single role. To switch between SP and IdP configuration for a given provider, click on the labels to select the role view:

   ![saml-roles](_images/saml-roles.png)

   Learn more about remote entity provider properties in:

   * [Remote IdP configuration](saml2-reference.html#saml2-remote-idp-configuration)

   * [Remote SP configuration](saml2-reference.html#saml2-remote-sp-configuration)

### Update remote SP certificate

To update all the metadata for a remote IdP or SP, you can [import the metadata](#configure-remote-entity) again. Reimporting the metadata deletes and recreates the entity provider, overwriting all existing provider settings with the values in the metadata XML file.

However, if you only want to update the signing and encryption certificate used by the SP to sign the authentication request without losing existing settings, follow these steps:

1. Get the SAML 2.0 SP metadata with the updated signed certificate.

   You can find information about exporting provider metadata XML in [Export provider metadata](#saml2-metadata-export).

2. Update the certificate in one of the following ways:

   * In the AM native admin console

     1. [Import the metadata](#configure-remote-entity).

        On the New Remote Entity Provider page, make sure you choose `UPDATE_CERTIFICATES` as the Update Type.

     2. Click Create.

   * Over REST

     1. Convert the XML metadata to a base64url-encoded string.

     2. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).

     3. Run the following REST API command, specifying the access token and the base64url-encoded SP metadata XML.

        ```bash
        $ curl \
        --request POST \
        --header 'authorization: Bearer <access-token>' \
        --header 'Content-Type: application/json' \
        --header 'Accept-API-Version: resource=1.0' \
        --data-raw '{
            "standardMetadata": "<base64url-encoded metadata>",
            "updateType": "UPDATE_CERTIFICATES"
        }' \
        'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/saml2/remote?_action=importEntity'
        {"importedEntities":["myProvider"]}
        ```

## Create a circle of trust (CoT)

A CoT groups at least one IdP and at least one SP who agree to share authentication information.

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | With [application management](../app-management/applications.html), you can use intuitive screens to create trusted agreements between providers through SAML 2.0 applications.Learn more in [Create a custom SAML 2.0 application](../app-management/register-a-custom-application.html#samlv2). |

1. In Native Consoles > Access Management, go to Realms > *Realm Name* > Applications > Federation > Circles of Trust, and click Add Circle of Trust.

2. Enter a name, and click Create.

3. On the Circle of Trust page, in the Entity Providers property, select at least one IdP and one SP.

   |   |                                                                |
   | - | -------------------------------------------------------------- |
   |   | You can create IdPs and SPs at any time and add them later on. |

4. Customize any other properties as required, and click Save Changes.

   Learn about CoT configuration in [CoT configuration](saml2-reference.html#saml2-cot-configuration).

---

---
title: Sign and encrypt messages
description: Configure SAML 2.0 message signing and encryption algorithms for identity providers and service providers
component: pingoneaic
page_id: pingoneaic:am-saml2:saml2-encryption
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/saml2-encryption.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "SHA-256", "RSA", "Encryption", "Algorithms", "Certificates"]
page_aliases: ["saml2-guide:saml2-encryption.adoc"]
section_ids:
  how_signing_works: How signing works
  how_encryption_works: How encryption works
  saml-advertised-sign-encrypt-algs: Configure the advertised signing and encryption algorithms
  sign-assertion-content: Configure Advanced Identity Cloud to sign and encrypt SAML 2.0 assertion content
---

# Sign and encrypt messages

|   |                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | By default, IdPs and SPs don't sign or encrypt SAML 2.0 messages.Although this is useful for test and demo environments, secure your production and production-like environments with keys.Find information on how to create and configure keys for signing and encryption in [TLS, secrets, signing, trust, and encryption](../tenants/tls-secrets-signing-trust-encryption.html). |

## How signing works

When Advanced Identity Cloud needs to sign a SAML request or response for the consumption of a remote entity provider, it will determine the signing algorithm, and optionally, the digest method, based on the following logic, as recommended by the [SAML 2.0 Metadata Profile for AlgorithmSupport Version 1.0](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-metadata-algsupport-v1.0-cs01.pdf) specification:

1. Advanced Identity Cloud retrieves the remote entity provider's metadata, and examines the role-specific extensions for a configured digest method, or signing algorithm. These are extensions defined within the `IDPSSODescriptor` or `SPSSODescriptor` elements.

   > **Collapse: Example**
   >
   > The following example role-specific extensions define the digest method and signing algorithms applicable to the SP role only:
   >
   > ```xml
   > <SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
   > 	<Extensions xmlns:alg="urn:oasis:names:tc:SAML:metadata:algsupport">
   > 		<alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha512" />
   > 		<alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512" />
   > 	</Extensions>
   > 	<!-- Other SP specific information -->
   > </SPSSODescriptor>
   > ```

2. If there is no role-specific algorithm configured, Advanced Identity Cloud checks for algorithms configured in the entity provider-level extensions. These are extensions defined within the `EntityDescriptor` element.

   > **Collapse: Example**
   >
   > The following example entity provider-level extensions define the digest method and signing algorithms applicable to the whole entity provider:
   >
   > ```xml
   > <EntityDescriptor entityID="myProvider"
   > 	xmlns="urn:oasis:names:tc:SAML:2.0:metadata">
   > 	<Extensions xmlns:alg="urn:oasis:names:tc:SAML:metadata:algsupport">
   > 		<alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha512" />
   > 		<alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512" />
   > 	</Extensions>
   > 	<!-- Role specific information -->
   > </EntityDescriptor>
   > ```

3. If signing algorithms are specified at either role-specific level or entity provider-level, but Advanced Identity Cloud can't find a suitable key, it doesn't sign the element, and displays an error.

   Possible reasons include:

   * **Algorithm mismatch**: the signing algorithm can't be used with the private key configured in the relevant secret ID.

   * **Keysize mismatch**: the required key size and actual key size aren't equal.

4. If the entity provider doesn't specify supported signing and digest methods in the standard metadata, Advanced Identity Cloud uses the default algorithm settings.

5. Advanced Identity Cloud examines the configured signing key type, and uses `RSA-SHA256` for RSA keys, `DSA-SHA256` for DSA keys, and `ECDSA-SHA512` for EC keys.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Advanced Identity Cloud has different default signing algorithm settings for XML signatures, and for query signatures.Advanced Identity Cloud determines the correct default query signing algorithm based on the signing key's algorithm: RSA, DSA, or EC.Advanced Identity Cloud reverts to the same defaults for XML and query signing algorithms only if the settings aren't correctly defined. |

After determining the required algorithm, the sender uses their own private key to write the signature on the request. Then, the provider receiving the message uses the public key exposed in the sender's metadata to validate the signature.

## How encryption works

When encrypting SAML 2.0 messages, the sender uses the receiver's public key (exposed in the receiver's metadata) to encrypt the request. The receiver decrypts the request with their private key.

As with signing, providers also expose the algorithms that they allow to encrypt assertion content in their metadata.

Because SAML 2.0 messages are in XML format, the encryption requires an additional key to be transported with the message, as explained in the [XML Encryption Syntax and Processing Version 1.1](https://www.w3.org/TR/xmlenc-core/) specification. Advanced Identity Cloud refers to those keys as *transport keys*.

Consider the following example of an encryption/decryption flow:

1. The IdP generates a random symmetric transport key using the transport key algorithm exposed in the SP's metadata.

2. The IdP encrypts the assertion with the transport key.

3. The IdP encrypts the transport key with the public key of the SP (which is also exposed in its metadata).

4. The SP decrypts the transport key using its private key.

5. The SP uses the transport key to decrypt the assertion.

This scenario ensures only this SP can decrypt the message.

The following sections explore these topics in detail.

## Configure the advertised signing and encryption algorithms

[Hosted IdPs and SPs](saml2-providers-and-cots.html#create-hosted-providers) can advertise the algorithms they can use to sign assertion content. This information appears as part of the provider's metadata extension.

Configure the required signing algorithms and digests:

1. Under Native Consoles > Access Management, go to Applications > Federation > Entity Providers > *Hosted Entity Provider*.

2. In Assertion Content > Signing and Encryption > Secret ID And Algorithms:

   * In the Signing Algorithm list, select the signing algorithms this provider can use.

   * In the Digest Algorithm list, select the digest algorithms this provider can use.

     Signing/digest algorithm metadata example

     ```xml
     <Extensions>
     <alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
     <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256"/>
     </Extensions>
     ```

     There is no default for these properties.

Hosted SPs and IdPs advertise their encryption algorithms so that the remote providers know which ones they should use when sending encrypted data.

Configure the required encryption algorithms:

1. On the Assertion Content tab, in the Encryption Algorithm drop-down list, select the algorithms this provider can use.

   Encryption algorithm metadata example

   ```xml
   <!-- Enable RSA-OAEP key transport with AES-GCM data encryption: -->
   <KeyDescriptor use="encryption">
    <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#rsa-oaep"/>
    <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc11#aes128-gcm"/>
   </KeyDescriptor>
   ```

   Select one or more AES algorithms from the list to encrypt assertion content, and one or more asymmetric algorithms to encrypt the transport key.

   For assertion encryption algorithms, ForgeRock recommends AES-GCM over the older AES-CBC modes. GCM offers authenticated encryption, which protects better against an attacker tampering with an encrypted assertion. Also sign assertions to make such attacks harder to exploit.

   **Assertion encryption algorithms**

   | Algorithm Identifier                                    | Recommended |
   | ------------------------------------------------------- | ----------- |
   | `http://www.w3.org/2009/xmlenc11#aes128-gcm`            | ✔           |
   | `http://www.w3.org/2009/xmlenc11#aes192-gcm`            | ✔           |
   | `http://www.w3.org/2009/xmlenc11#aes256-gcm`            | ✔           |
   | `http://www.w3.org/2001/04/xmlenc#aes128-cbc` (default) |             |
   | `http://www.w3.org/2001/04/xmlenc#aes192-cbc`           |             |
   | `http://www.w3.org/2001/04/xmlenc#aes256-cbc`           |             |

   **Key transport algorithms**

   | Algorithm Identifier                                        | Recommended |
   | ----------------------------------------------------------- | ----------- |
   | `http://www.w3.org/2009/xmlenc11#rsa-oaep`                  | ✔           |
   | `http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p` (default) |             |
   | `http://www.w3.org/2001/04/xmlenc#rsa-1_5`(1)               | ✖           |

   (1) For security reasons, you shouldn't use this option.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you change the signing or encryption algorithms for the hosted entity provider, don't forget to update the algorithms on the remote entity provider to match. To do this in the Advanced Identity Cloud admin console, select Native Consoles > Access Management, go to Applications > Federation > Entity Providers > *Remote Entity Provider* and select the Assertion Content tab. Alternatively, [reimport the metadata](saml2-providers-and-cots.html#configure-remote-entity) to delete and recreate the entity provider with the new details. |

## Configure Advanced Identity Cloud to sign and encrypt SAML 2.0 assertion content

Advanced Identity Cloud can sign and encrypt the SAML 2.0 assertion content with the following caveats:

* Assertions

  HTTP-POST bindings require signed assertions.

  Failure to enable signing when using HTTP-POST bindings can result in errors such as the following:

  ```none
  ERROR: UtilProxySAMLAuthenticatorLookup.retrieveAuthenticationFromCache: Unable to do sso or federation.
  com.sun.identity.saml2.common.SAML2Exception: Provider's signing certificate alias is missing.
  ```

  Or:

  ```none
  ERROR: SAML2Utils.verifyResponse:Assertion is not signed or signature is not valid.
  ```

* SAML authentication requests

  Signing is **recommended** to verify the request's authenticity and when using the `ForceAuthn` flag.

* SAML assertion responses

  Signing **AND** encrypting is **recommended** because responses can contain user data.

* SAML logout requests

  Signing is **recommended** to verify the request's authenticity.

To configure signing and encryption:

1. Under Native Consoles > Access Management, go to Applications > Federation > Entity Providers > *Hosted Entity Provider*.

2. On the Assertion Content tab, in the Secret ID Identifier property, enter a string value to identify the secret IDs this provider will use.

   For example, `mySamlSecrets`.

   How secret identifiers work:

   * Advanced Identity Cloud using a secret identifier to know which secret IDs are relevant for a provider. You can reuse the identifier that another provider is already using if you want them to share the same secrets.

   * When a provider is removed from the Advanced Identity Cloud configuration, Advanced Identity Cloud automatically removes the secret IDs related to their identifier, unless they're being used by another provider.

   * If you don't specify a value for the secret ID identifier, Advanced Identity Cloud will use the global default secrets relative to the entity provider's role, *in the realm*. If they aren't mapped, Advanced Identity Cloud will search for the global default secrets in the global secret stores.

3. Save your changes.

   Advanced Identity Cloud creates two new secret IDs, at the realm level, based on the value you specified.

4. Under Native Consoles > Access Management, go to Applications > Federation > Entity Providers > *Hosted Entity Provider*.

5. On the Assertion Content tab, in the Signing and Encryption section, select the SAML 2.0 elements that Advanced Identity Cloud should sign and the elements to encrypt.

6. Save your changes.

   Advanced Identity Cloud now uses the key pairs you configured. Find more information on how to create and configure keys for signing and encryption in Advanced Identity Cloud in [TLS, secrets, signing, trust, and encryption](../tenants/tls-secrets-signing-trust-encryption.html).

---

---
title: SP account mapper
description: SP account mapper scripts to customize how SAML 2.0 assertions map to user profiles
component: pingoneaic
page_id: pingoneaic:am-saml2:custom-sp-account-mapper
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/custom-sp-account-mapper.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Customization", "Scripts"]
page_aliases: ["release-notes:rapid-channel/sp-account-mapper.adoc"]
section_ids:
  example-sp-account-mapper: Customize auto-federation using an SP account mapper
  prepare-profile-data: Prepare the user profiles
  configure-auto-fed: Configure auto-federation
  use-sp-account-mapper-script: Update the SP account mapper script
  test-sp-account-mapper-script: Try the script
  handle-missing-nameid: Handle a missing NameID in a script
---

# SP account mapper

Use the SP account mapper to customize how SAML 2.0 assertions are mapped to user profiles.

* Next-generation example script

  [SAML2 SP Account Mapper Script](../am-scripting/sample-scripts.html#saml2-sp-account-mapper-js)

* Script bindings

  [SP account mapper scripting API](../am-scripting/saml2-sp-account-mapper-api.html)

## Customize auto-federation using an SP account mapper

This section describes how to implement an example SP account mapper that uses a script to customize auto-federation of user accounts. It assumes that you have configured your environment for SSO using SAML 2.0, where Advanced Identity Cloud is the hosted SP. These example steps use a separate Advanced Identity Cloud tenant as the remote IdP.

* [Prepare the user profiles](#prepare-profile-data)

* [Configure auto-federation](#configure-auto-fed)

* [Update the SP account mapper script](#use-sp-account-mapper-script)

* [Try the script](#test-sp-account-mapper-script)

### Prepare the user profiles

1. Create a test user on the hosted SP, for example `bjensen`, with an email address set to `bjensen@example.com`.

2. Create a test user on the hosted IdP, for example `babsjensen`, with an email address also set to `bjensen@example.com`.

### Configure auto-federation

Under Native Consoles > Access Management, go to Applications > Federation > Entity Providers and click on the name of the hosted provider.

1. On the tenant configured as the **hosted SP**:

   1. Under Assertion Processing > Auto Federation:

      * Switch on Enabled.

      * Set Attribute to `mail`.

   2. Save your changes.

2. On the tenant configured as the **hosted IdP**:

   1. Under Assertion Processing > Attribute Mapper, add the following Attribute Map:

      * Name Format Uri

        `urn:oasis:names:tc:SAML:2.0:attrname-format:basic`

      * SAML Attribute

        `mail`

      * Local Attribute

        `mail`

   2. Save your changes.

### Update the SP account mapper script

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type SAML2 SP Account Mapper.

2. Update the script to implement any custom behavior for auto-federation. This example adds a logging statement to record the assertion map.

   |   |                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To handle a missing NameID in the assertion, update the script to check for a `null` NameID and fall back to auto-federation.Learn more in [Handle a missing NameID in a script](#handle-missing-nameid). |

   ```javascript
   ...
   userID = accountMapperHelper.getAutoFedUser(nameID["value"]);
       if (userID != null && userID.length > 0) {
           //
           // insert custom code here
           //
           // update logging to output assertion and userID
           logger.error("Assertion: " + assertion);
           logger.error(debugMethod + " use AutoFedUser as userID: " + userID);
           return userID;
       } else {
           ...
       }
   ```

   |   |                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The SP account mapper script type is a [next-generation script](../am-scripting/next-generation-scripts.html) only.Learn about the available bindings in the [SP account mapper scripting API](../am-scripting/saml2-sp-account-mapper-api.html). |

3. Still in the native console, go to Applications > Federation > Entity Providers > *Hosted SP Name* > Assertion Processing.

4. Under Account Mapper, select `SAML2 SP Account Mapper Script` from the Account Mapper Script list.

5. Save your changes.

### Try the script

1. To verify the script works as expected, test your changes using an SP-initiated flow.

   For example:

   ```none
   https://<tenant-env-sp-fqdn>/am/saml2/jsp/spSSOInit.jsp?realm=/alpha&idpEntityID=idp1&metaAlias=/alpha/sp1&binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-POST
   ```

2. Log into the IdP as `babsjensen`.

   After you've logged into the IdP successfully, you shouldn't need to log into the SP because the script auto-federates the `babsjensen` and `bjensen` accounts.

3. Verify that `bjensen` is logged into the SP.

   You can also check that the SP [debug logs](../tenants/audit-debug-logs.html) contain the customized logging output, for example:

   ```none
   Assertion:
   {
       "version": "2.0",
       "issueInstant": 1758805815000,
       "subject": {
           "subjectConfirmation": [
               {
       …​
   }
   ScriptedSPAccountMapper.getIdentity::  use AutoFedUser as userID: id=bjensen,ou=user,o=alpha,ou=services,ou=am-config
   ```

## Handle a missing NameID in a script

If your IdP doesn't always include a NameID in the assertion, update your SP account mapper script to check for a `null` NameID and fall back to auto-federation.

When `accountMapperHelper.getNameID()` returns `null`, call `accountMapperHelper.getAutoFedUser()` to resolve the user using the configured auto-federation attribute.

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If there's no NameID and the auto-federation lookup fails to find a user, the script should return `null`. Advanced Identity Cloud then rejects the assertion. |

The following example shows a `getIdentity()` function with the NameID `null` check:

```javascript
function getIdentity() {
    const debugMethod = "ScriptedSPAccountMapper.getIdentity:: ";
    var nameID = accountMapperHelper.getNameID();
    var userID = null;

    if (!nameID) {
        // No NameID in assertion — fall back to auto-federation attribute
        return accountMapperHelper.getAutoFedUser();
    }

    var isTransient = accountMapperHelper.isTransientNameId(nameID["format"]);
    if (isTransient) {
        userID = accountMapperHelper.getTransientUserForSP();
        accountMapperHelper.validateUserId(userID);
        if (userID != null && userID.length > 0) {
            logger.debug(debugMethod + " use Transient user as userID:" + userID);
            return userID;
        }
    }

    userID = accountMapperHelper.getAutoFedUser(nameID["value"]);
    if (userID != null && userID.length > 0) {
        logger.debug(debugMethod + " use AutoFedUser as userID:" + userID);
        return userID;
    } else {
        if (accountMapperHelper.useNameIDAsSPUserID() && !accountMapperHelper.isAutoFedEnabled()) {
            logger.debug(debugMethod + " use NameID value as userID:" + nameID["value"]);
            accountMapperHelper.validateUserId(nameID["value"]);
            return nameID["value"];
        } else {
            return null;
        }
    }
}

getIdentity();
```

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | SLO isn't supported when the NameID is missing from the assertion. Learn more in [Auto-federation when no NameID is present](auto-federation.html#auto-federation-missing-nameid). |