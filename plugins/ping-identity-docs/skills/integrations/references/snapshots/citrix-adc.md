---
title: Citrix ADC Integration Guide
description: This guide describes how to configure PingFederate and Citrix ADC to enable single sign-on (SSO).
component: citrix-adc
page_id: citrix-adc::pf_citrix_adc_integration
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/pf_citrix_adc_integration.html
revdate: June 26, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Citrix ADC Integration Guide

This guide describes how to configure PingFederate and Citrix ADC to enable single sign-on (SSO).

This allows you to use PingFederate as an identity provider (IdP) for Citrix ADC and Gateway.

The integration uses a standard SAML configuration and does not require any additional software.

## Features

* Browser-based SSO initiated by the IdP or service provider (SP).

## Intended audience

This document is intended for PingFederate administrators. Before you start, you should be familiar with the following:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html) in the PingFederate documentation

* The following sections of the Citrix documentation:

  * [SAML authentication](https://docs.citrix.com/en-us/citrix-adc/13/aaa-tm/saml-authentication.html)

  * [Authentication, authorization, and auditing Application Traffic](https://docs.citrix.com/en-us/citrix-adc/13/aaa-tm)

## System requirements

* Citrix ADC 13.0 or later

* A DNS configuration that routes authentication requests to a Citrix ADC virtual IP address

* An SSL certificate installed on the Citrix ADC appliance

---

---
title: Configuring an adapter instance
description: Create an adapter instance to make the username attribute available in your service provider connection to Citrix Gateway.
component: citrix-adc
page_id: citrix-adc:creating_a_single_sign-on_connection:pf_citrix_adc_integration_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/creating_a_single_sign-on_connection/pf_citrix_adc_integration_configuring_an_adapter_instance.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Create an adapter instance to make the username attribute available in your service provider connection to Citrix Gateway.

## Steps

1. Click **Map New Adapter Instance**.

2. On the **Adapter Instance** tab, in the **Adapter Instance** list, select an adapter instance that can access the username in your user store, such as **HTML Form Adapter**. Click **Next**.

3. On the **Mapping Method** tab, click **Next**.

4. On the **Attribute Contract Fulfillment** tab, on the **SAML\_SUBJECT** line, in the **Source** list, select **Adapter**.

5. On the **SAML\_SUBJECT** line, in the **Value** list, select **username**. Click **Next**.

6. On the **Issuance Critera** tab, click **Next**.

7. On the **Summary** tab, check that the configuration is correct, and then click **Done**.

---

---
title: Creating a SAML policy in Citrix
description: Create a SAML authentication policy and associate it with the authentication server that you created.
component: citrix-adc
page_id: citrix-adc::pf_citrix_adc_integration_creating_a_saml_policy_in_citrix
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/pf_citrix_adc_integration_creating_a_saml_policy_in_citrix.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a SAML policy in Citrix

Create a SAML authentication policy and associate it with the authentication server that you created.

## About this task

Learn more in [NetScaler as a SAML SP](https://docs.citrix.com/en-us/netscaler/12/aaa-tm/saml-authentication/netscaler-saml-sp.html) in the Citrix documentation.

## Steps

1. In Citrix ADC, go to **Configuration > Security > AAA - Application Traffic > Policies > Authentication > Basic > Policies > SAML**. Click **Add**.

2. In the **Create Authentication SAML Policy** window, in the **Name** field, enter a name, such as `PF_Policy`.

3. In the **Server** list, select the server that you created in [Creating an authentication server in Citrix](pf_citrix_adc_integration_creating_an_authentication_server_in_citrix.html).

4. In the **Expression** section, in the **Saved Policy Expressions** list, select **ns\_true**. Click **Create**.

---

---
title: Creating a single sign-on connection
description: To allow PingFederate to handle single sign-on (SSO) to Citrix, create a service provider (SP) connection.
component: citrix-adc
page_id: citrix-adc:creating_a_single_sign-on_connection:pf_citrix_adc_integration_creating_a_single_sign_on_connection
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/creating_a_single_sign-on_connection/pf_citrix_adc_integration_creating_a_single_sign_on_connection.html
revdate: June 26, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Creating a single sign-on connection

To allow PingFederate to handle single sign-on (SSO) to Citrix, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. If you see the **Connection Template** tab, select **Do not use a template for this connection**. Click **Next**.

3. On the **Connection Type** tab, select only **Browser SSO Profiles**. Click **Next**.

4. On the **Connection Options** tab, select only **Browser SSO**. Click **Next**.

5. On the **Import Metadata** tab, select **None**. Click **Next**.

6. On the **General Info** tab, enter the basic connection information. Click **Next**.

   1. In the **Partner's Entity ID** field, enter the **Issuer Name** that you chose in [Creating an authentication server in Citrix](../pf_citrix_adc_integration_creating_an_authentication_server_in_citrix.html).

   2. In the **Connection Name** field, enter the connection ID portion of the **Redirect URL** that you entered in [Creating an authentication server in Citrix](../pf_citrix_adc_integration_creating_an_authentication_server_in_citrix.html).

   3. In the **Base URL** field, enter the base URL for your Citrix Gateway server.

7. On the **Browser SSO** tab, configure browser SSO. Click **Next**.

   Learn more in [Configure IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

   1. On the **Browser SSO > SAML Profiles** tab, select **IdP-Initiated SSO** and **SP-Initiated SSO**. Click **Next**.

   2. On the **Browser SSO > Assertion Creation > Authentication Source Mapping** tab, complete the steps in [Configuring an adapter instance](pf_citrix_adc_integration_configuring_an_adapter_instance.html). Click **Next**.

   3. On the **Browser SSO > Protocol Settings > Assertion Consumer Service** tab, in the **Binding** list, select **POST**.

   4. In the **Endpoint URL** field, enter `/cgi/samlauth`, and then click **Add**. Click **Next**.

   5. On the **Browser SSO > Protocol Settings > Allowable SAML Bindings** tab, select only **POST**. Click **Next**.

8. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.

10. Note the **SSO Application Endpoint** URL. Click **Save**.

    The **SSO Application Endpoint** URL should match the **Redirect URL** that you entered in [Creating an authentication server in Citrix](../pf_citrix_adc_integration_creating_an_authentication_server_in_citrix.html). If it doesn't, update the URL in Citrix ADC.

11. To test the integration, make sure your test credentials exist in both the PingFederate data store and Citrix, then go to your Citrix ADC URL in a browser and sign on.

---

---
title: Creating an authentication server in Citrix
description: To allow PingFederate to handle authentication requests, add your PingFederate signing certificate and sign-on URL.
component: citrix-adc
page_id: citrix-adc::pf_citrix_adc_integration_creating_an_authentication_server_in_citrix
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/pf_citrix_adc_integration_creating_an_authentication_server_in_citrix.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Creating an authentication server in Citrix

To allow PingFederate to handle authentication requests, add your PingFederate signing certificate and sign-on URL.

## Steps

1. In Citrix ADC, complete the steps in [Enabling authentication, authorization, and auditing](https://docs.citrix.com/en-us/citrix-adc/13/aaa-tm/ns-aaa-setup-enabling-tsk.html) in the Citrix documentation.

2. Go to **Configuration > Authentication > Dashboard**. Click **Add**.

3. In the **Create Authentication Server** window, in the **Choose Server Type** list, select **SAML**.

4. In the **Name** field, enter a name to represent your PingFederate server, such as `PF_Auth_Server`.

5. Clear the **Import Metadata** checkbox.

6. In the **Redirect URL** field, enter the following PingFederate sign-on URL. Substitute your hostname and port, and choose a connection ID.

   `https://pf_host:pf_port/idp/startSSO.ping?PartnerSpId=connectionID`

   You will use the connection ID again in [Creating a single sign-on connection](creating_a_single_sign-on_connection/pf_citrix_adc_integration_creating_a_single_sign_on_connection.html).

7. In the **SAML Binding** and **Logout Binding** lists, select **POST**.

8. Add your PingFederate signing certificate.

   1. Under **IDP Certificate Name**, click **Add**.

   2. In the **Certificate-Key Pair Name** field, enter a name, such as `PF_Certificate`.

   3. In the **Certificate File Name** section, upload the certificate that you saved in [Exporting your PingFederate signing certificate](pf_citrix_adc_integration_exporting_your_pf_signing_certificate.html). Click **Install**.

9. In the **Issuer Name** field, enter a name to represent Citrix, such as `CitrixSAML`.

10. In the **Reject Unsigned Assertion** list, select **OFF**. Click **More**.

11. In the **Signature Algorithm** section, click **RSA-SHA256**.

12. In the **Digest Method** section, click **SHA256**. Click **Create**.

---

---
title: Creating an authentication virtual server in Citrix
description: Configure a virtual server to direct authentication requests to PingFederate.
component: citrix-adc
page_id: citrix-adc::pf_citrix_adc_integration_creating_an_authentication_virtual_server_in_citrix
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/pf_citrix_adc_integration_creating_an_authentication_virtual_server_in_citrix.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating an authentication virtual server in Citrix

Configure a virtual server to direct authentication requests to PingFederate.

## About this task

Learn more in [Setting up an authentication virtual server](https://docs.citrix.com/en-us/citrix-adc/13/aaa-tm/authentication-virtual-server.html) in the Citrix documentation.

## Steps

1. In Citrix ADC, go to **Configuration > Security > AAA - Application Traffic > Virtual Servers**. Click **Add**.

2. In the **Authentication Virtual Server** window, in the **Basic Settings** section, enter the basic server information.

   1. In the **Name** field, enter a name, such as `PF_Auth_VServer`.

   2. In the **IP Address** field, enter the IP address of your PingFederate server. Click **OK**.

3. In the **Certificates** section, select your PingFederate certificate.

   1. Click **No Server Certificate**.

   2. In the **Server Certificate Binding** pane, in the **Select Server Certificate** section, click **Click to select**.

   3. In the **Server Certificates** pane, select the certificate that you added in [Creating an authentication server in Citrix](pf_citrix_adc_integration_creating_an_authentication_server_in_citrix.html). Click **Select**.

   4. In the **Server Certificate Binding** pane, click **Bind**. Click **Continue**.

4. In the **Advanced Authentication Policies** section, click **Continue**.

5. In the **Basic Authentication Policies** section, add a policy.

   1. Click **Add (+)**.

   2. In the **Choose Type** pane, in the **Policies** section, in the **Choose Policy** list, select **SAML**.

   3. In the **Choose Type** list, select **Primary**. Click **Continue**.

   4. In the **Policy Binding** section, in the **Select Policy** list, select the policy that you created in [Creating a SAML policy in Citrix](pf_citrix_adc_integration_creating_a_saml_policy_in_citrix.html).

   5. Click **Bind**. Click **Continue**.

6. Click **Done**.

---

---
title: Enabling SAML policy on the Gateway virtual server
description: Set the SAML policy you create as the default for the Gateway virtual server.
component: citrix-adc
page_id: citrix-adc::pf_citrix_adc_integration_enabling_saml_policy_on_the_gateway_virtual_server
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/pf_citrix_adc_integration_enabling_saml_policy_on_the_gateway_virtual_server.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Enabling SAML policy on the Gateway virtual server

Set the SAML policy you create as the default for the Gateway virtual server.

## Steps

1. In Citrix ADC, go to **Configuration > Citrix Gateway > Virtual Servers**. Select your virtual server.

2. In the **Basic Authentication Policies** section, select the policy that you created in [Creating a SAML policy in Citrix](pf_citrix_adc_integration_creating_a_saml_policy_in_citrix.html).

   1. Click **Add (+)**.

   2. In the **Choose Type** pane, in the **Policies** section, in the **Choose Policy** list, select **SAML**.

   3. In the **Choose Type** list, select **Primary**. Click **Continue**.

   4. In the **Policy Binding** section, in the **Select Policy** list, select the policy that you created in [Creating a SAML policy in Citrix](pf_citrix_adc_integration_creating_a_saml_policy_in_citrix.html).

   5. Click **Bind**.

3. Click **Done**.

---

---
title: Enabling single sign-on in PingFederate
description: Before you can configure single sign-on in Citrix, you need to set a SAML entity ID in PingFederate.
component: citrix-adc
page_id: citrix-adc:enabling_single_sign-on_in_pingfederate:pf_citrix_adc_integration_enabling_single_sign_on_in_pf
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/enabling_single_sign-on_in_pingfederate/pf_citrix_adc_integration_enabling_single_sign_on_in_pf.html
revdate: June 26, 2024
section_ids:
  enabling-single-sign-on-in-pingfederate-10-1-or-later: Enabling single sign-on in PingFederate 10.1 or later
  steps: Steps
  enabling-single-sign-on-in-pingfederate-10-0-or-earlier: Enabling single sign-on in PingFederate 10.0 or earlier
  steps-2: Steps
---

# Enabling single sign-on in PingFederate

Before you can configure single sign-on in Citrix, you need to set a SAML entity ID in PingFederate.

## Enabling single sign-on in PingFederate 10.1 or later

### Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Federation Info**.

2. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

3. Click **Save**.

## Enabling single sign-on in PingFederate 10.0 or earlier

### Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Roles & Protocols**.

2. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

3. Select the **SAML 2.0** checkbox. Click **Next**.

4. Go to the **Federation Info** tab.

5. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

6. Click **Save**.

---

---
title: Enabling single sign-on in PingFederate 10.0 or earlier
description: On the PingFederate administrative console, go to System > Protocol Settings > Roles & Protocols.
component: citrix-adc
page_id: citrix-adc:enabling_single_sign-on_in_pingfederate:pf_citrix_adc_integration_enabling_single_sign_on_in_pf_100_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/enabling_single_sign-on_in_pingfederate/pf_citrix_adc_integration_enabling_single_sign_on_in_pf_100_or_earlier.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Enabling single sign-on in PingFederate 10.0 or earlier

## Steps

1. On the PingFederate administrative console, go to **System > Protocol Settings > Roles & Protocols**.

2. Select the **Enable Identity Provider IdP Role and Support the Following** checkbox.

3. Select the **SAML 2.0** checkbox. Click **Next**.

4. Go to the **Federation Info** tab.

5. In the **SAML 2.0 Entity ID** field, enter a name for PingFederate to use to identify itself to SAML partners.

6. Click **Save**.

---

---
title: Enabling single sign-on in PingFederate 10.1 or later
description: On the PingFederate administrative console, go to System > Protocol Settings > Federation Info.
component: citrix-adc
page_id: citrix-adc:enabling_single_sign-on_in_pingfederate:pf_citrix_adc_integration_enabling_single_sign_on_in_pf_101_or_later
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/enabling_single_sign-on_in_pingfederate/pf_citrix_adc_integration_enabling_single_sign_on_in_pf_101_or_later.html
revdate: June 26, 2024
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
title: Exporting your PingFederate signing certificate
description: To allow Citrix to communicate with PingFederate, export your PingFederate signing certificate.
component: citrix-adc
page_id: citrix-adc::pf_citrix_adc_integration_exporting_your_pf_signing_certificate
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/pf_citrix_adc_integration_exporting_your_pf_signing_certificate.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Exporting your PingFederate signing certificate

To allow Citrix to communicate with PingFederate, export your PingFederate signing certificate.

## Steps

1. On the PingFederate administrative console, go to **Security > Signing & Decryption Keys & Certificates**.

2. If you do not have a certificate, create one.

   Learn more in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

3. For the certificate that you want to use, in the **Action** column, click **Export**.

4. On the **Export Certificate** tab, click **Next**.

5. On the **Export & Summary** tab, click **Export**.