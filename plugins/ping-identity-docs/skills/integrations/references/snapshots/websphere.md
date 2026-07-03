---
title: Configuring service provider-initiated SSO
description: You can imitate a service provider (SP)-initiated single sign-on (SSO) experience by configuring your WebSphere Application Server (WAS) to redirect unauthenticated users to the PingFederate SSO page.
component: websphere
page_id: websphere:setup:pf_websphere_integration_configuring_service_provider_initiated_sso
canonical_url: https://docs.pingidentity.com/integrations/websphere/setup/pf_websphere_integration_configuring_service_provider_initiated_sso.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring service provider-initiated SSO

You can imitate a service provider (SP)-initiated single sign-on (SSO) experience by configuring your WebSphere Application Server (WAS) to redirect unauthenticated users to the PingFederate SSO page.

## About this task

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | This part of the configuration is optional. If you only want identity provider-initiated SSO, skip these steps. |

By default, when an unauthenticated user tries to access a protected resource, the WebSphere Application Server (WAS) captures the requested resource URL in a browser cookie, then directs the user to a default error page.

You can override this behavior to redirect the user to the PingFederate SSO page instead. After the user authenticates, the WebSphere Application Server redirects them to the original resource URL stored in the cookie.

This creates a sign on experience that is similar to SP-initated SSO. For a true SAML-based solution, see [Enabling SAML SP-Initiated web single sign-on (SSO)](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/tsec_enable_saml_sp_sso.html) in the WebSphere documentation.

## Steps

1. In your WebSphere trusted association interceptor (TAI) configuration, add filter properties to allow the WAS to identify requests that should be authenticated by PingFederate. Follow the guide in the **SAML TAI filter property** section of [SAML web single sign-on (SSO) trust association interceptor (TAI) custom properties](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/rwbs_samltaiproperties.html) in the WebSphere documentation.

2. In your TAI configuration, change the `sso_<id>.sp.login.error.page` property to the **SSO Application Endpoint** URL that you noted in [Creating a single sign-on connection](gnc1590516299053.html).

---

---
title: Configuring single sign-on in WebSphere
description: Configure a SAML trust association interceptor (TAI) on your WebSphere Application Server (WAS).
component: websphere
page_id: websphere:setup:pf_websphere_integration_configuring_single_sign_on_in_websphere
canonical_url: https://docs.pingidentity.com/integrations/websphere/setup/pf_websphere_integration_configuring_single_sign_on_in_websphere.html
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Configuring single sign-on in WebSphere

Configure a SAML trust association interceptor (TAI) on your WebSphere Application Server (WAS).

## Steps

1. Complete the steps in [Enabling your system to use the SAML web single sign-on (SSO) feature](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/twbs_enablesamlsso.html) in the WebSphere documentation. Add custom properties to your TAI based on the table below.

   **Trust association interceptor custom properties for PingFederate**

   | Property                            | Description                                                                                                                                                                                                 |
   | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `sso_<id>.sp.acsUrl`                | The assertion consumer service URL for the WebSphere SAML ACS servlet, such as `https://was_host:was_port/samlsps/applicationacs`.                                                                          |
   | `sso_<id>.sp.EntityID`              | Enter an entity ID of your choosing for your WAS. This is included in the SAML metadata file that you export in the next step.                                                                              |
   | `sso_<id>.idp_<id>.EntityID`        | The **SAML 2.0 Entity ID** that you entered in [Enabling single sign-on in PingFederate](pf_websphere_integration_enabling_single_sign_on_in_pf.html).                                                      |
   | `sso_<id>.idp_<id>.SingleSignOnUrl` | The PingFederate SSO URL, such as `https://pf_host:pf_port/idp/SSO.saml2`.                                                                                                                                  |
   | `sso_<id>.idp_<id>.certAlias`       | Enter a name of your choosing to identity the PingFederate signing certificate. You will use this when you import the certificate to WebSphere.                                                             |
   | `sso_<id>.sp.login.error.page`      | Your WAS authentication error page.This property is also used in the optional [Configuring service provider-initiated SSO](pf_websphere_integration_configuring_service_provider_initiated_sso.html) steps. |
   | `sso_<id>.sp.targetUrl`             | The URL of the target application.To test your configuration, you can enter `https://was_host:was_port/snoop`.                                                                                              |

   |   |                                                                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For detailed specifications for these properties, see [SAML web single sign-on (SS) trust association interceptor (TAI) custom properties](https://www.ibm.com/support/knowledgecenter/SS7K4U_9.0.5/com.ibm.websphere.zseries.doc/ae/rwbs_samltaiproperties.html) in the WebSphere documentation. |

2. Complete the steps in [Exporting SAML web service provider metadata using the wsadmin command-line utility](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/twbs_exportsamlspmetadata.html) in the WebSphere documentation. Save the metadata file to your PingFederate server. You will use it in [Creating a single sign-on connection](gnc1590516299053.html).

3. Complete the steps in [Importing SAML identity provider (IdP) partner metadata using the wsadmin command-line utility](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/twbs_importsamlidpmetadata.html) in the WebSphere documentation. Select the metadata file that you saved in [Exporting SAML metadata from PingFederate](pf_websphere_integration_exporting_saml_metadata_from_pf.html). Use the alias that you chose for the `sso_<id>.idp_<id>.certAlias` property.

4. Complete the steps in [Configuring single sign-on (SSO) partners](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/twbs_configuresamlssopartners.html) in the WebSphere documentation.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle single sign-on (SSO) authentication for WebSphere, create a service provider (SP) connection.
component: websphere
page_id: websphere:setup:gnc1590516299053
canonical_url: https://docs.pingidentity.com/integrations/websphere/setup/gnc1590516299053.html
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Creating a single sign-on connection

To allow PingFederate to handle single sign-on (SSO) authentication for WebSphere, create a service provider (SP) connection.

## Steps

1. Sign on to the PingFederate administrator console.

2. On the **Identity Provider** tab, in the **SP Connections** area, create a new connection.

   1. Click **Create new**.

   2. If you see the **Connection Template** tab, select **Do not use a template for this connection**. Click **Next**.

3. On the **Connection Type** tab, select only **Browser SSO Profiles**. Click **Next**.

4. On the **Connection Options** tab, select only **Browser SSO**. Click **Next**.

5. On the **Import Metadata** tab, select **File**. Click **Choose File**, select the `sp-metadata.xml` file that you saved in [Configuring single sign-on in WebSphere](pf_websphere_integration_configuring_single_sign_on_in_websphere.html), and then click **Open**. Click **Next**.

6. On the **General Info** tab, the basic connection information is populated by the metadata XML file. Click **Next**.

7. On the **Browser SSO** tab, configure browser SSO.

   For a complete guide, see [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select only **IdP-Initiated SSO**.

8. On the **Credentials** tab, configure the connection credentials. Click **Next**.

   For a complete guide, see [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

   * On the **Credentials > Digital Signature Settings** tab, select the **Include the certificate in the signature \<KeyInfo> element** check box.

9. On the **Activation and Summary** tab, above the **Summary** section, turn on the connection.

10. Note the **SSO Application Endpoint** URL. You can use this to enable SP-initiated single sign-on in [Configuring single sign-on in WebSphere](pf_websphere_integration_configuring_single_sign_on_in_websphere.html). Click **Save**.

---

---
title: Enabling single sign-on in PingFederate
description: Before you can configure single sign-on in WebSphere, you need to set a SAML entity ID in PingFederate.
component: websphere
page_id: websphere:setup:pf_websphere_integration_enabling_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/websphere/setup/pf_websphere_integration_enabling_single_sign_on_in_pf.html
revdate: July 5, 2024
section_ids:
  enabling-single-sign-on-in-pingfederate-10-1-or-later: Enabling single sign-on in PingFederate 10.1 or later
  steps: Steps
  enabling-single-sign-on-in-pingfederate-10-0-or-earlier: Enabling single sign-on in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling single sign-on in PingFederate

Before you can configure single sign-on in WebSphere, you need to set a SAML entity ID in PingFederate.

## Enabling single sign-on in PingFederate 10.1 or later

### Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Federation Info**.

2. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

3. Click **Save**.

## Enabling single sign-on in PingFederate 10.0 or earlier

### Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Roles & Protocols**.

2. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

3. Select the **SAML 2.0** check box. Click **Next**.

4. Go to the **Federation Info** tab.

5. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

6. Click **Save**.

---

---
title: Enabling single sign-on in PingFederate 10.0 or earlier
description: On the PingFederate administrative console, go to System > Protocol Settings > Roles & Protocols.
component: websphere
page_id: websphere:setup:pf_websphere_integration_enabling_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/websphere/setup/pf_websphere_integration_enabling_single_sign_on_in_pf_100_or_earlier.html
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Enabling single sign-on in PingFederate 10.0 or earlier

## Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Roles & Protocols**.

2. Select the **Enable Identity Provider IdP Role and Support the Following** check box.

3. Select the **SAML 2.0** check box. Click **Next**.

4. Go to the **Federation Info** tab.

5. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

6. Click **Save**.

---

---
title: Enabling single sign-on in PingFederate 10.1 or later
description: On the PingFederate administrative console, go to System > Protocol Settings > Federation Info.
component: websphere
page_id: websphere:setup:pf_websphere_integration_enabling_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/websphere/setup/pf_websphere_integration_enabling_single_sign_on_in_pf_101_or_later.html
revdate: July 5, 2024
section_ids:
  steps: Steps
---

# Enabling single sign-on in PingFederate 10.1 or later

## Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Federation Info**.

2. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

3. Click **Save**.

---

---
title: Exporting SAML metadata from PingFederate
description: Export a metadata file that describes your PingFederate identity provider configuration.
component: websphere
page_id: websphere:setup:pf_websphere_integration_exporting_saml_metadata_from_pf
canonical_url: https://docs.pingidentity.com/integrations/websphere/setup/pf_websphere_integration_exporting_saml_metadata_from_pf.html
revdate: July 5, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Exporting SAML metadata from PingFederate

Export a metadata file that describes your PingFederate identity provider configuration.

## About this task

For general information about these steps, see [Metadata export](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_metadata_export.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Metadata Export** window\..

   ### Choose from:

   * For PingFederate 10.1 or later: go to **System > Protocol Metadata > Metadata Export**.

   * For PingFederate 10.0 or earlier: go to **System > Metadata Export**.

2. If you see the **Metadata Role** tab, select **I am the identity provider (IdP)**. Click **Next**.

3. On the **Metadata Mode** tab, select **Select information to include in metadata manually**. Click **Next**.

4. On the **Protocol** tab, click **Next**.

5. On the **Attribute Contract** tab, click **Next**.

6. On the **Signing Key** tab, select a signing certificate. Click **Next**.

7. **Optional:** On the **Metadata Signing** tab, select a certificate to sign the metadata XML file. Click **Next**.

8. On the **XML Encryption Certificate** tab, select the certificate that you want to use to encrypt the XML content. Click **Next**.

9. On the **Export & Summary** tab, click **Export**.

10. Save `metadata.xml`.

11. Click **Done**.

---

---
title: WebSphere Integration Guide
description: This guide describes how to configure PingFederate and IBM WebSphere Application Server to enable single sign-on (SSO).
component: websphere
page_id: websphere::pf_websphere_integration
canonical_url: https://docs.pingidentity.com/integrations/websphere/pf_websphere_integration.html
revdate: July 5, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# WebSphere Integration Guide

This guide describes how to configure PingFederate and IBM WebSphere Application Server to enable single sign-on (SSO).

Because this integration uses a standard SAML configuration, you don't need to download additional software.

## Features

* Browser-based SSO initiated by the identity provider (IdP) or service provider (SP).

|   |                                           |
| - | ----------------------------------------- |
|   | WebSphere does not support single logout. |

## Intended audience

This document is intended for PingFederate administrators.

Before you start, you should be familiar with the following:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html) in the PingFederate documentation

* The following sections of the WebSphere documentation:

  * [SAML web single sign-on](https://www.ibm.com/support/knowledgecenter/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/cwbs_samlssoconcepts.html)

  * The **Trust association model** section of [Trust associations](https://www.ibm.com/support/knowledgecenter/SS7K4U_9.0.5/com.ibm.websphere.zseries.doc/ae/csec_trust.html)

## System requirements

* Administrator access to WebSphere 8.5 or later