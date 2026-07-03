---
title: Configure a Connection
description: Use the following procedure to configure a quick connection for single sign-on (SSO) to Heroku.
component: heroku
page_id: heroku::pf_heroku_integration_configure_a_connection
canonical_url: https://docs.pingidentity.com/integrations/heroku/pf_heroku_integration_configure_a_connection.html
revdate: February 24, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configure a Connection

## About this task

Use the following procedure to configure a quick connection for single sign-on (SSO) to Heroku.

|   |                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure provides instructions for configuring minimum required connection settings. The instructions skip pages in which all necessary information is configured or defaults are used. You can add or change settings to suit your requirements. |

## Steps

1. If you have not already done so, use PingFederate to configure the identity provider (IdP) adapter you want to use.

   Learn more in [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html) in the PingFederate documentation.

2. On the **Main Menu**, select **Create New** under SP Connections in the **IdP Configuration** section.

3. On the **Connection Template** page, select the **Do not use a template for this connection** and click **Next**.

   ![A screenshot showing the Connection Template page. Do not use a template for this collection is selected.](_images/hwb1563995389314.jpg)

4. On the **Connection Type** page, ensure that the **Browser SSO** profile is selected and click **Next**.

5. On the **Connection Options** page, ensure **Browser SSO** is selected and click **Next**.

6. On the **Import Metadata** page, click **Choose file** and select the Heroku `saml-metadata.xml` file you created in [Obtain the Heroku SAML 2.0 Metadata XML](pf_heroku_integration_obtain_the_heroku_saml_20_metadata_xml.html).

   ![A screenshot of the Import Metadata page, with the heroku-saml-metadata.xml file uploaded.](_images/zal1563995390253.jpg)

7. On the **Metadata Summary** page, click **Next**.

8. On the **General Info** page, ensure that the **Partner's Entity ID (Connection ID)**, **Connection Name**, and **Base URL** are accurate. Change details if required and click **Next**.

   ![A screenshot of the General Info page, with https://sso.heroku.com entered into the Entity ID, Connection Name, and Base URL fields.](_images/cbz1563995390911.jpg)

9. On the **Browser SSO** page, click **Configure Browser SSO**.

   ![A screenshot of the Browser SSO page, showing the Configure Browser SSO button.](_images/qlp1563995391812.jpg)

10. On the **SAML Profiles** page, ensure that the **IdP-Initiated SSO** and **SP-Initiated SSO** profiles are selected and click **Next**.

    ![A screenshot of the SAML Profiles page, showing the IdP-Initiated SSO and SP-Initiated SSO checkboxes checked.](_images/yzj1563995392810.jpg)

11. On the **Assertion Creation** page, click **Configure Assertion Creation**.

    ![A screenshot of the Assertion Creation page, showing the Configure Assertion Creation button.](_images/nal1563995393601.jpg)

12. On the **Attribute Contract** page, ensure that the SAML\_SUBJECT name format is set to:

    ```
    following:urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
    ```

    ![A screenshot of the Attribute Contract page, showing the SAML\_SUBJECT field populated.](_images/hnm1563995394378.jpg)

13. On the **Authentication Source Mapping** page, click **Map New Adapter Instance** and map the IdP Adapter Instance you defined earlier in this procedure. When you return to the Authentication Source Mapping page, click **Done**.

    |   |                                                                                                                                                                                                                                                                                                                                                   |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | This configuration is site-dependent and cannot be pre-configured. You can find detailed information and instructions in [Managing authentication source mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_assertioncreationtasklet_idpadaptermappingstate.html) in the PingFederate documentation. |

    ![A screenshot of the Authentication Source Mapping page, showing the Map New Adapter Instance button.](_images/cte1563995395079.jpg)

14. When you return to the **Assertion Creation** page, click **Next**

15. On the **Protocol Settings** page, click **Configure Protocol Settings**.

16. On the **Allowable SAML Bindings** page, ensure that only the **POST** and **Redirect** profiles are selected and click **Next**.

    ![A screenshot of the Allowable SAML Bindings page, showing the POST and REDIRECT checkboxes checked.](_images/oyu1563995395836.jpg)

17. On the next page, ensure that the **Always sign the SAML Assertion** is selected and click **Next**.

18. On the **Browser SSO** page, click **Next** and on the **Credentials** page, click **Configure Credentials**.

    Learn more in [Configuring digital signatures for service provider connections](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_digital_signatures_service_provider_connections.html) in the PingFederate documentation.

19. If you have not yet created or imported a signing certificate, click **Manage Certificates** and do so now. Learn more in [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html) in the PingFederate documentation.

    ![A screenshot of the Digital Signature Settings page, showing a signing certificate imported.](_images/lyy1563995396473.jpg)

20. Click **Next**.

21. On the **Summary** page, click **Done**.

22. On the **Credentials** page, click **Next**.

23. On the **Activation & Summary** page, **Activate** the SP Connection.

24. On the **Activation & Summary** page, click **Save**.
