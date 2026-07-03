---
title: Configuring Browser SSO
description: For the single sign-on (SSO) part of your connection to Contentful, use the details below.
component: contentful
page_id: contentful:configuring_single_sign-on:pf_contentful_integration_configuring_browser_sso
canonical_url: https://docs.pingidentity.com/integrations/contentful/configuring_single_sign-on/pf_contentful_integration_configuring_browser_sso.html
revdate: June 26, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring Browser SSO

For the single sign-on (SSO) part of your connection to Contentful, use the details below.

## About this task

|   |                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For all other settings, you can use the default or customize the configuration for your needs. Learn more in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation. |

## Steps

1. On the **Browser SSO** tab, click **Configure Browser SSO**.

2. On the **Browser SSO > SAML Profiles** tab, select only **IDP-Initiated SSO** and **SP-Initiated SSO**. Click **Next**.

3. On the **Assertion Lifetime** tab, click **Next**.

4. On the **Assertion Creation** tab, configure the assertion.

   1. Click **Configure Assertion Creation**.

   2. On the **Attribute Contract** tab, set the following name formats. Click **Next**.

      **Attribute name formats**

      | Attribute Contract | Subject Name format                                     |
      | ------------------ | ------------------------------------------------------- |
      | SAML\_SUBJECT      | `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified` |
      | email              | `urn:oasis:names:tc:SAML:2.0:attrname-format:uri`       |
      | givenname          | `urn:oasis:names:tc:SAML:2.0:attrname-format:basic`     |
      | surname            | `urn:oasis:names:tc:SAML:2.0:attrname-format:basic`     |

   3. On the **Authentication Source Mapping** tab, click **Map New Adapter Instance**.

   4. On the **IdP Adapter Mapping > Adapter Instance** tab, in the **Adapter Instance** list, select the adapter instance that you created in [Creating an HTML Form Adapter instance](pf_contentful_integration_creating_an_html_form_adapter_instance.html). Click **Next**.

   5. On the **Mapping Method** tab, click **Next**.

   6. On the **Attribute Contract Fulfillment** tab, select **Adapter** for all attributes. Click **Next**.

      ![A screenshot that shows the Attribute Contract Fulfillment tab with Adapter selected for every attribute.](_images/wqg1616516794672.jpg)

   7. On the **Issuance Criteria** tab, click **Next**.

   8. On the **Summary** tab, click **Done**.

   9. On the **Browser SSO > Assertion Creation > Authentication Source Mapping** tab, click **Next**.

   10. On the **Summary** tab, click **Done**.

5. On the **Protocol Settings** tab, configure the protocol settings.

   1. Click **Configure Protocol Settings**.

   2. On the **Assertion Consumer Service URL** tab, the default URL is populated by the Contentful `metadata.xml` file. Click **Next**.

   3. On the **Allowable SAML Bindings** tab, select only **POST** and **Redirect**. Click **Next**.

   4. On the **Signature Policy** tab, clear the **Require authn requests to be signed** check box. Click **Next**.

   5. On the **Encryption Policy** tab, click **Next**

   6. On the **Summary** tab, click **Done**.

   7. On the **Browser SSO > Protocol Settings** tab, click **Next**.

   8. On the **Summary** tab, click **Done**.

6. On the **SP Connection > Browser SSO** tab, click **Next**.
