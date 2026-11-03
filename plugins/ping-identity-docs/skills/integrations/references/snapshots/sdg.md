---
title: Changelog
description: The CoreBlox IdP Adapter is now the SDG CTS IdP Adapter, and the CoreBlox SP Adapter is now the SDG CTS SP Adapter. The configuration field labels and descriptions have been updated to refer to the SDG Conversion Token Service (CTS).
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
section_ids:
  sdg-cts-integration-kit-2-8-october-2026: SDG CTS Integration Kit 2.8 - October 2026
  sdg-cts-integration-kit-2-7-1-october-2021: SDG CTS Integration Kit 2.7.1 – October 2021
  sdg-cts-integration-kit-2-7-september-2020: SDG CTS Integration Kit 2.7 – September 2020
  sdg-cts-integration-kit-2-6-2-june-2020: SDG CTS Integration Kit 2.6.2 – June 2020
  sdg-cts-integration-kit-2-6-1-november-2018: SDG CTS Integration Kit 2.6.1 – November 2018
  sdg-cts-integration-kit-2-6-october-2018: SDG CTS Integration Kit 2.6 – October 2018
  sdg-cts-integration-kit-2-5-april-2018: SDG CTS Integration Kit 2.5 – April 2018
  sdg-cts-integration-kit-2-4-june-2017: SDG CTS Integration Kit 2.4 – June 2017
  sdg-cts-integration-kit-2-3-september-2016: SDG CTS Integration Kit 2.3 – September 2016
  sdg-cts-integration-kit-2-2-november-2015: SDG CTS Integration Kit 2.2 – November 2015
  sdg-cts-integration-kit-2-1-may-2015: SDG CTS Integration Kit 2.1 – May 2015
  sdg-cts-integration-kit-2-0-april-2014: SDG CTS Integration Kit 2.0 – April 2014
  sdg-cts-integration-kit-1-0-5-march-2014: SDG CTS Integration Kit 1.0.5 – March 2014
  sdg-cts-integration-kit-1-0-november-2012: SDG CTS Integration Kit 1.0 – November 2012
---

# Changelog

## SDG CTS Integration Kit 2.8 - October 2026

* The CoreBlox IdP Adapter is now the SDG CTS IdP Adapter, and the CoreBlox SP Adapter is now the SDG CTS SP Adapter. The configuration field labels and descriptions have been updated to refer to the SDG Conversion Token Service (CTS).

* Added support for custom proxy configuration for connections to the SDG Conversion Token Service.

  Learn more in [SDG CTS IdP Adapter settings reference](pf_sdg_cts_ik_idp_adapter_settings_reference.html).

* Added an **API Request Timeout** setting that controls how long the adapters wait for responses from the SDG Conversion Token Service.

  Learn more in [SDG CTS IdP Adapter settings reference](pf_sdg_cts_ik_idp_adapter_settings_reference.html).

* Fixed a defect that caused attribute filter expressions to fail on PingFederate servers running Java 17.

## SDG CTS Integration Kit 2.7.1 – October 2021

* Verified that the SDG CTS IdP Adapter is compliant with US Federal Information Processing Standards (FIPS). Learn more about usage in [Integrating with Bouncy Castle FIPS provider](https://docs.pingidentity.com/pingfederate/latest/getting_started_with_pingfederate/pf_set_up_java8_java11.html) in the PingFederate documentation.

* Updated internal components to better support certificate revocation checks in PingFederate 11.0 and later.

## SDG CTS Integration Kit 2.7 – September 2020

* Fixed an issue that could cause a query string to be encoded incorrectly.

* Fixed an issue that could sometimes cause a redirect loop.

* Added the **Session Cookie Prefix** and **Remove Session Cookie Prefix** settings to accommodate a change in the way SDG Conversion Token Service provides tokens.

## SDG CTS Integration Kit 2.6.2 – June 2020

* Fixed an issue that occurred when a user left the sign-on page, then tried to open the sign-on page again elsewhere.

## SDG CTS Integration Kit 2.6.1 – November 2018

* Improved PingFederate node reliability when making REST calls to the SDG Conversion Token Service by changing to a bundled HTTP client.

## SDG CTS Integration Kit 2.6 – October 2018

* Added the ability to ignore session cookies from inbound requests to the PingFederate SP server. Refer to the **Ignore Session Cookie** field on the SDG CTS SP Adapter **Instance Configuration** page.

## SDG CTS Integration Kit 2.5 – April 2018

* Added the **Send Session Attributes** field to the SP adapter. Use this field to send attribute contract to the SDG Conversion Token Service (CTS) for inclusion in the created session.

## SDG CTS Integration Kit 2.4 – June 2017

* PingFederate 8.4 compatibility updates.

* Optionally, prevent an update to the session cookie after sign on.

* User is redirected for authentication if the session is invalid.

* Session cookie is retained and set to the logged off value after SLO.

* Session cookie isn't modified on SLO error.

## SDG CTS Integration Kit 2.3 – September 2016

* Made the **Login URL** field optional to support multiple SDG environments.

* Improved error logging in both the IdP and SP adapters.

## SDG CTS Integration Kit 2.2 – November 2015

* Added support for cookie provider functionality

* Added support for authentication context in the SP Adapter.

## SDG CTS Integration Kit 2.1 – May 2015

* Added the ability to download a configuration file for the OpenToken agent in the SDG SP adapter.

* Bug fixes.

## SDG CTS Integration Kit 2.0 – April 2014

* Added additional UI configuration validation, notably for the fields required for authorization and for the **Cookie Domain** field in the SP adapter.

* Fixed an issue that caused the adapter to use `userId-qualifier` as the attribute to link accounts instead of the `usesrId` attribute.

* Added the ability to specify an **Authentication Context** for the IdP adapter. Anything entered into this field is included in the SAML assertion. Learn more in the [SDG CTS IdP Adapter settings reference](pf_sdg_cts_ik_idp_adapter_settings_reference.html).

* You can now configure both the IdP and SP adapters to authorize a user before redirecting them to the target resource.

* You can now use the keyword `token` to add the `token` attribute returned in the JSON object from the CTS to the extended contract.

## SDG CTS Integration Kit 1.0.5 – March 2014

* Added support for authorization functionality, enabling review of users' authorization level before they can access a protected resource.

## SDG CTS Integration Kit 1.0 – November 2012

* Initial release.

---

---
title: Changelog
description: The following is the change history for the CoreBlox Token Translator.
component: sdg
page_id: sdg:coreblox_token_translator:pf_coreblox_tt_changelog
canonical_url: https://docs.pingidentity.com/integrations/sdg/coreblox_token_translator/pf_coreblox_tt_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
section_ids:
  coreblox-token-translator-1-3-august-2017-current-release: CoreBlox Token Translator 1.3 - August 2017 (current release)
  coreblox-token-translator-1-2-august-2016: CoreBlox Token Translator 1.2 - August 2016
  coreblox-token-translator-1-1-may-2016: CoreBlox Token Translator 1.1 – May 2016
  coreblox-token-translator-1-0-april-2014: CoreBlox Token Translator 1.0 – April 2014
---

# Changelog

The following is the change history for the CoreBlox Token Translator.

## CoreBlox Token Translator 1.3 - August 2017 (current release)

* PingFederate 8.4 compatibility updates.

## CoreBlox Token Translator 1.2 - August 2016

* Added configuration option to Base64-encode the CoreBlox token.

## CoreBlox Token Translator 1.1 – May 2016

* Added authentication context support for the Token Generator.

## CoreBlox Token Translator 1.0 – April 2014

* Initial release.

---

---
title: Configuring a SDG CTS SP Adapter instance
description: Configure the SDG CTS SP Adapter to determine how PingFederate communicates with your service provider (SP) application.
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_configuring_sp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_configuring_sp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  steps: Steps
---

# Configuring a SDG CTS SP Adapter instance

Configure the SDG CTS SP Adapter to determine how PingFederate communicates with your service provider (SP) application.

## Steps

1. In the PingFederate admin console, go to **Applications > Integration > SP Adapters**.

2. Click **Create New Instance**.

3. On the **Type** tab, set the basic adapter instance attributes.

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **SDG CTS SP Adapter**. Click **Next**.

4. (Optional) On the **Instance Configuration** tab, in the **Protected Resource Mapping Table** section, define conditions that the SAML assertion has to meet for the user to get access to a protected resource.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The SDG Conversion Token Service allows you to grant permissions to specific realms in specific domains by defining the resource, instance, and action fields. These values are defined in your CTS Agent Config Object (ACO) settings.Learn more in the SDG Conversion Token Service Install and Configuration Guide included in the [Conversion Token Service Overview](https://sdgc.com/conversion-token-service/) download. |

   1. Click **Add a new row to 'Protected Resource Mapping Table'**.

   2. In the **Auth Context** field, enter the authentication context that has to exist in the SAML assertion, such as `Password` or `MobileTwoFactorContract`.

      You can find the complete list of authentication contexts in the [Authentication Context for the OASIS Security Assertion Markup Language (SAML) 2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-authn-context-2.0-os.pdf) \[PDF] in the OASIS Open documentation.

   3. (Optional) In the **Attribute Filter** field, enter an attribute that has to exist in the assertion, such as `${organization}='WidgetCo'`.

      |   |                                                                                                                                                                         |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can use `AND` and `OR` operators to include multiple attributes or create simple rules. For example, `${organization}='WidgetCo' OR ${organization}='WidgetCoLtd'`. |

   4. In the **Resource** field, enter the name of the resource that the user can access when the assertion meets the **Auth Context** and **Attribute Filters** conditions.

      For example, `/partner_application/partner_landing.html`.

   5. In the **Instance** field, enter the value of the `AgentName` parameter associated with the default CTS Agent Config Object.

      For example, `partner_site_agent`.

   6. In the **Action** field, enter the action, such as `GET`, `POST`, or `PUT`.

   7. In the **Action** column, click **Update**.

   8. To add more attributes, repeat steps a - g.

5. On the **Instance Configuration** tab, configure the adapter instance by referring to [SDG CTS SP Adapter settings reference](pf_sdg_cts_ik_sp_adapter_settings_reference.html).

6. Click **Next**.

7. (Optional) On the **Actions** tab, if you set **Send Extended Attributes** to **OpenToken**, click **Download**, and then click **Export**. Save `agent-config.txt`.

   You can use this file to decode the OpenToken token that contains the extended attributes.

8. On the **Extended Contract** tab, add any attributes that you expect to retrieve other than the SAML subject. Click **Next**.

9. On the **Target App Info** tab, enter the basic information about your SP application. Click **Next**.

10. On the **Summary** tab, click **Save**.

11. Create an IdP connection using this SDG CTS SP Adapter instance.

    Learn more in the [Service provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_servic_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring a SDG IdP Adapter instance
description: Configure the SDG CTS IdP Adapter to determine how PingFederate communicates with SDG Conversion Token Service. You can configure the adapter to direct authentication requests, authorization consent requests, or both to your application.
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_configuring_idp_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_configuring_idp_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  steps: Steps
---

# Configuring a SDG IdP Adapter instance

Configure the SDG CTS IdP Adapter to determine how PingFederate communicates with SDG Conversion Token Service. You can configure the adapter to direct authentication requests, authorization consent requests, or both to your application.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**.

2. Click **Create New Instance**.

3. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **SDG CTS IdP Adapter**. Click **Next**.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [SDG CTS IdP Adapter settings reference](pf_sdg_cts_ik_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Extended Contract** screen, add any attributes that you want to include in the assertion. Click **Next**.

   |   |                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The SDG Conversion Token Service returns a `userAttributes` key that lists a set of attributes. You can use any of these attributes to extend the attribute contract.You can also include the `token` key in the extended attribute contract. |

6. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

7. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Defining the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation.

8. Click **Next**.

9. On the **Summary** tab, click **Save**.

10. Create an SP connection using this SDG CTS IdP Adapter instance. Learn more about [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html) in the PingFederate documentation.

---

---
title: Configuring the IdP token processor
description: This section describes how to configure the CoreBlox Token Processor.
component: sdg
page_id: sdg:coreblox_token_translator:pf_coreblox_tt_configuring_the_idp_token_processor
canonical_url: https://docs.pingidentity.com/integrations/sdg/coreblox_token_translator/pf_coreblox_tt_configuring_the_idp_token_processor.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
section_ids:
  steps: Steps
---

# Configuring the IdP token processor

This section describes how to configure the CoreBlox Token Processor.

## Steps

1. Sign on to the PingFederate admin console and click **Token Processors** under **IdP Configuration** on the main menu.

   |   |                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you don't see Token Processors on the main menu, enable **WS-Trust** under **Server Settings** on the **Roles and Protocols** screen by selecting **WS-Trust** for the IdP role. |

2. On the **Manage Token Processor Instances** page, click **Create New Instance**.

3. On the **Type** tab:

   1. In the **Instance Name** field, enter a name of your choice for the token processor instance.

   2. In the **Instance ID** field, enter a unique identifier for the token processor instance.

      |   |                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **Instance ID** is used internally. It can't contain any spaces or non-alphanumeric characters, and it must be uniquely named. |

4. In the **Type** list, select **CoreBlox Token Processor**. Click **Next**.

5. On the **Instance Configuration** page, complete the following fields:

   > **Collapse: Standard fields**
   >
   > | Field                                      | Description                                                                                                                    |
   > | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
   > | **CoreBlox URL**                           | The base URL for CTS requests.                                                                                                 |
   > | **Validate CoreBlox Certificate Hostname** | If selected, the hostname of the server certificate presented by the CTS must match the hostname of the **CoreBlox URL**.      |
   > | **Client Certificate**                     | The certificate used for authentication calls to the CTS.                                                                      |
   > | **CoreBlox Tokentype**                     | The `tokentype` to be returned from the CTS.&#xA;&#xA;The only permissible value is SMSESSION. This is also the default value. |

6. (Optional) Click **Show Advanced Fields** to specify the token processor's authorization configuration settings.

   > **Collapse: Advanced fields**
   >
   > | Field                         | Description                                                                                                                                                                                                     |
   > | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **Perform Authorize Request** | If selected, the token processor makes an authorize request to the CTS before accessing the protected resource.&#xA;&#xA;The following three fields are required for the adapter to make the authorize request. |
   > | **Resource**                  | The resource that the agent protects.                                                                                                                                                                           |
   > | **Instance**                  | Refers to the name of the agent instance.                                                                                                                                                                       |
   > | **Action**                    | The action to take when evaluating requests against the policy server.                                                                                                                                          |

7. Click **Next**.

8. (Optional) On the **Extended Contract** tab, configure additional attributes for the adapter.

   Learn more about key concepts in the [Administrator's reference guide](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_administrators_reference_guide.html) in the PingFederate documentation.

9. Click **Next**.

10. On the **Token Attributes** page, select the **Pseudonym** checkbox for the `userId` attribute.

    |   |                                                                                                           |
    | - | --------------------------------------------------------------------------------------------------------- |
    |   | You can also select this checkbox for any extended attributes specified on the **Extended Contract** tab. |

    Learn more in [Setting pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation.

11. Click **Next**.

12. On the **Summary** tab, verify that everything is correct, then click **Done**.

13. On the **Manage Token Processor Instances** page, click **Save** to complete the token generator configuration.

---

---
title: Configuring the SP token generator
description: This section describes how to configure the CoreBlox SP Token Generator.
component: sdg
page_id: sdg:coreblox_token_translator:pf_coreblox_tt_configuring_the_sp_token_generator
canonical_url: https://docs.pingidentity.com/integrations/sdg/coreblox_token_translator/pf_coreblox_tt_configuring_the_sp_token_generator.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
section_ids:
  steps: Steps
---

# Configuring the SP token generator

This section describes how to configure the CoreBlox SP Token Generator.

## Steps

1. Sign on to the PingFederate admin console. In the **SP Configuration** section, click **Token Generators**.

2. On the **Manage Token Generator Instances** page, click **Create New Instance**.

3. On the **Type** tab:

   1. In the **Instance Name** field, enter a name of your choice for the token processor instance.

   2. In the **Instance ID** field, enter a unique identifier for the token processor instance.

      |   |                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **Instance ID** is used internally. It can't contain any spaces or non-alphanumeric characters, and it must be uniquely named. |

4. In the **Type** list, select **CoreBlox Token Generator *\<version>***. Click **Next**.

5. On the **SP Adapter** page, click **Add a new row to 'Protected Resource Mapping Table'** and enter the following information into the table:

   > **Collapse: Protected resource mapping table fields**
   >
   > | Field                  | Description                                                                                                                                                                                                              |
   > | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **Auth Context**       | The attribute containing authentication context.&#xA;&#xA;The name of this attribute needs to be specified in the Context Attribute Name advanced field in step 7 if you're using advanced fields in your configuration. |
   > | **Attribute Filter**   | The names and values of attributes that the assertion must contain for this protected resource.                                                                                                                          |
   > | **Protected Resource** | The protected resource to be accessed if the authentication context and attribute filters in the assertion match the provided values.                                                                                    |

   1. Click **Update** in the **Action** column.

      |   |                             |
      | - | --------------------------- |
      |   | Repeat step 5 as necessary. |

6. On the **Instance Configuration** tab, complete the following fields:

   > **Collapse: Standard fields**
   >
   > | Field                                      | Description                                                                                                                  |
   > | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
   > | **CoreBlox URL**                           | The URL for the CTS.                                                                                                         |
   > | **Validate CoreBlox Certificate Hostname** | If selected, the hostname of the server certificate presented by the CTS must match the hostname of the **CoreBlox URL**.    |
   > | **Client Certificate**                     | The certificate used for authentication calls to the CTS.                                                                    |
   > | **CoreBlox Tokentype**                     | The tokentype to be returned from the CTS.&#xA;&#xA;The only permissible value is SMSESSION. This is also the default value. |
   > | **Base64 Decode The Token**                | If selected, the token the CTS returns will be base64-decoded. This prevents the token from being encoded twice.             |

7. (Optional) Click **Show Advanced Fields** to specify the token processor's authorization configuration settings.

   > **Collapse: Advanced fields**
   >
   > | Field                         | Description                                                                                                                                                                                                                    |
   > | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **Context Attribute Name**    | The name of the attribute containing the **Auth Context** used for mapping protected resources.&#xA;&#xA;This value is required if Perform Authorize Request is selected and the Protected Resource Mapping Table isn't empty. |
   > | **Perform Authorize Request** | If selected, the adapter will make an authorize request to the CTS before accessing the protected resource.&#xA;&#xA;The following three fields are required for the adapter to make the authorize request.                    |
   > | **Resource**                  | The resource that is protected by the agent.                                                                                                                                                                                   |
   > | **Instance**                  | Refers to the name of the agent instance.                                                                                                                                                                                      |
   > | **Action**                    | The action to take when evaluating requests against the policy server.                                                                                                                                                         |

8. Click **Next**.

9. (Optional) On the **Extended Contract** tab, configure additional attributes for the Token Generator.

   Any attributes configured in this step are added to the request header.

10. Click **Next**.

11. On the **Summary** screen, verify that everything is correct, then click **Done**.

12. On the **Manage Token Generator Instances** page, click **Save**.

---

---
title: CoreBlox Token Translator
description: The PingFederate CoreBlox Token Translator provides a token processor and token generator for use with the PingFederate's WS-Trust Security Token Service (STS).
component: sdg
page_id: sdg:coreblox_token_translator:pf_coreblox_tt
canonical_url: https://docs.pingidentity.com/integrations/sdg/coreblox_token_translator/pf_coreblox_tt.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 1, 2026
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# CoreBlox Token Translator

The PingFederate CoreBlox Token Translator provides a token processor and token generator for use with the PingFederate's WS-Trust Security Token Service (STS).

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The CoreBlox Token Translator was created before Coreblox became SDG. The configuration fields and documentation will be updated to use the new name during the next token translator release. |

## Components

* Token processor

  Allows an identity provider (IdP) STS to validate and authorize a CoreBlox session token from a Web Service Client (WSC), and then map user attributes into a SAML token to a Web Service Provider (WSP).

* Token Generator

  Allows a service provider (SP) STS to issue a CoreBlox session token for a WSP, including mapped attributes from an incoming SAML token.

## Intended audience

This document is intended for PingFederate administrators and web application developers.

If you need help during the setup process, learn more about available resources in:

* The following section of the PingFederate documentation:

  * [WS-Trust STS configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_wstrust_sts_config.html)

* The following CoreBlox resources:

  * [CoreBlox Token Service](https://sdgc.com/conversion-token-service/)

## System requirements

* PingFederate 11.3 or later

* A CoreBlox Token Service (CTS) installation, either local or remote

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the SDG CTS Integration Kit files to your PingFederate directory.
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_deploying_integration_files
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_deploying_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the SDG CTS Integration Kit files to your PingFederate directory.

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the SDG CTS Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/coreblox-integration-kit).

2. Stop PingFederate, if it's running.

3. If you're upgrading an existing deployment, delete `pf-sdg-cts-adapter-<version>.jar` from `<pf_install>/PingFederate/server/default/deploy`.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each engine node.

---

---
title: Deploying the integration files
description: If you operate PingFederate in a cluster, the following steps refer to the console node.
component: sdg
page_id: sdg:coreblox_token_translator:pf_coreblox_tt_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/sdg/coreblox_token_translator/pf_coreblox_tt_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
section_ids:
  steps: Steps
---

# Deploying the integration files

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | If you operate PingFederate in a cluster, the following steps refer to the console node. |

## Steps

1. Download the CoreBlox Token Translator `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/coreblox-token-translator).

2. Stop PingFederate, if it's running.

3. If you're upgrading an existing deployment, delete any existing CoreBlox Token Translator files (`coreblox-token-translator-*.jar`) from the `<pf_install>/PingFederate/server/default/deploy` directory.

4. Extract the `zip` archive and copy the `CoreBlox-token-translator-<version>.jar` file from the `dist` directory to the `<pf_install>/PingFederate` directory.

5. Start the PingFederate server.

6. If you operate PingFederate in a cluster, repeat steps 2 - 5 for each engine node.

---

---
title: Download manifest
description: The following files are included in the SDG CTS Integration Kit .zip archive.
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
---

# Download manifest

The following files are included in the SDG CTS Integration Kit `.zip` archive.

* `Legal.pdf`: Copyright and license information.

* `dist/pingfederate/server/default`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-sdg-cts-adapter-<version>.jar`: The SDG CTS IdP Adapter and SDG CTS SP Adapter.

---

---
title: Download manifest
description: The following files are included in the CoreBlox Token Translator .zip archive:
component: sdg
page_id: sdg:coreblox_token_translator:pf_coreblox_tt_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/sdg/coreblox_token_translator/pf_coreblox_tt_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
---

# Download manifest

The following files are included in the CoreBlox Token Translator `.zip` archive:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `/dist`: Contains libraries needed to run the adapter.

  * `CoreBlox-token-translator-<version>.jar`: The CoreBlox Token Translator `.jar` file.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 23, 2026
section_ids:
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

These steps are optional. Learn more about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. If you want to log activity for PingFederate and all adapters, do the following:

   1. Find the following section:

      ```xml
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`:

      ```xml
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. If you want to see the adapter activity in the console, remove the comment tags:

      ```xml
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. If you want to log activity just for the SDG CTS IdP Adapter, add the following line:

   ```xml
   <Logger name="com.pingidentity.clientservices.product.coreblox" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the SDG CTS Integration Kit.
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_known_issues_limitations
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_known_issues_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the SDG CTS Integration Kit.

## Known issues

There are no known issues.

## Known limitations

* Can't delete all characters of an attribute on the **Extended Contract** page during an `update` action.

* If you're running SDG Conversion Token Service (CTS) inside PingFederate and have deployed the PingID RADIUS PCV, you must use PingID RADIUS PCV 1.3 or later.

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the CoreBlox Token Translator.
component: sdg
page_id: sdg:coreblox_token_translator:pf_coreblox_tt_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/sdg/coreblox_token_translator/pf_coreblox_tt_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the CoreBlox Token Translator.

## Known issues

* When configuring STS clients in PingFederate 6.0 or later, there's a common issue with libraries parsing XML. You can find more information on how to resolve this issue in [Invalid XML Errors While Loading STS Client Libraries](https://support.pingidentity.com/s/article/Invalid-XML-Errors-While-Loading-STS-Client-Libraries) in the Ping Identity Knowledge Base.

## Known limitations

There are no known limitations.

---

---
title: Overview of the IdP SSO flow
description: With the SDG CTS Integration Kit, PingFederate allows the identity provider (IdP) to access user attributes from SDG Conversion Token Service (CTS).
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_overview_idp_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_overview_idp_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  description: Description
---

# Overview of the IdP SSO flow

With the SDG CTS Integration Kit, PingFederate allows the identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* to access user attributes from SDG Conversion Token Service (CTS).

The following figure illustrates an IdP-initiated single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* scenario where PingFederate generates an assertion using a SDG CTS IdP Adapter session cookie.

![A diagram showing an example SSO flow using the SDG CTS IdP Adapter and the CTS.](_images/pf_coreblox_ik_idp_sso_flow_overview.jpg)

## Description

1. A user initiates an SSO transaction by authenticating with the IdP.

2. The login service authenticates the user with the CTS.

3. The IdP sets a session cookie in the browser and redirects the browser to PingFederate.

4. PingFederate uses the session cookie to query the CTS for user attributes associated with the session. The CTS returns the user attributes.

5. The adapter wraps the user attributes in an assertion. PingFederate redirects the browser to the service provider with the assertion.

---

---
title: Overview of the SP SSO flow
description: With the SDG CTS Integration Kit, PingFederate allows a service provider (SP) to start a SDG session with user attributes from the identity provider (IdP).
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_overview_sp_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_overview_sp_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  description: Description
---

# Overview of the SP SSO flow

With the SDG CTS Integration Kit, PingFederate allows a service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* to start a SDG session with user attributes from the identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*.

The following figure illustrates an IdP-initiated single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* scenario where PingFederate uses the SDG CTS SP Adapter to parse an assertion and create an SDG session cookie.

![A diagram showing an example SSO flow using the SDG CTS SP Adapter and the CTS.](_images/pf_coreblox_ik_sp_sso_flow_overview.jpg)

## Description

1. The PingFederate SP server receives an assertion from the IdP.

2. PingFederate parses the assertion.

3. The SDG CTS SP Adapter uses the user attributes to create and authorize a session with the CTS.

4. The adapter redirects the browser with a request that contains the session cookie.

---

---
title: SDG CTS IdP Adapter settings reference
description: Field descriptions for the SDG CTS IdP Adapter configuration page.
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  standard-fields: Standard fields
  advanced-fields: Advanced fields
---

# SDG CTS IdP Adapter settings reference

Field descriptions for the SDG CTS IdP Adapter configuration page.

## Standard fields

| Field Name                                                     | Description                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SDG Conversion Token Service URL**                           | The URL for the SDG Conversion Token Service (CTS).This field is blank by default.                                                                                                                                                                                                                                                                                                    |
| **Validate SDG Conversion Token Service Certificate Hostname** | The hostname of the server certificate presented by SDG Conversion Token Service must match the hostname in the **SDG Conversion Token Service URL** field.This checkbox is selected by default.                                                                                                                                                                                      |
| **Client Certificate**                                         | The certificate that the adapter uses to authentication calls to SDG Conversion Token Service.                                                                                                                                                                                                                                                                                        |
| **SDG Conversion Token Service TokenType**                     | The token type that SDG Conversion Token Service is configured to provide to the adapter.The default and only value is `SMSESSION`.                                                                                                                                                                                                                                                   |
| **Cookie Name**                                                | The name of the cookie that contains the token used with SDG Conversion Token Service.This field is blank by default.                                                                                                                                                                                                                                                                 |
| **Cookie Domain**                                              | The domain name that the adapter uses when creating cookies. The browser compares this value to the domain of subsequent requests to determine whether the cookie should be submitted.If this field is blank, the adapter uses the domain name of the request. When sharing cookie across subdomains, this value must be prefixed with a period (`.`).This field is blank by default. |
| **Cookie Path**                                                | The path that the adapter uses when creating cookies. The browser compares this value to the path of subsequent requests to determine whether the cookie should be submitted.The default value is `/`.                                                                                                                                                                                |
| **Cookie Secure Flag**                                         | The adapter writes cookies with the Secure flag. The browser only submits Secure cookies on subsequent HTTPS requests.This checkbox is selected by default.                                                                                                                                                                                                                           |
| **Error URL**                                                  | When an error occurs in the adapter, PingFederate redirects the browser to this URL instead of to the default error page. This URL can contain query parameters. The URL has an `errorMessage` appended to it, which contains a brief description of the error that has occurred.This field is blank by default.                                                                      |
| **Logged-Out Cookie Value**                                    | The expected value of the cookie when the user has been signed off.The default value is `LOGGEDOFF`.                                                                                                                                                                                                                                                                                  |
| **HTTP Only Flag**                                             | The adapter sets a flag for the cookie. The flag indicates that the cookie should only be read through HTTP requests and disallows Javascript from accessing the cookie.This checkbox is selected by default.                                                                                                                                                                         |
| **Login URL**                                                  | An optional URL for the authentication service.If the cookie isn't found in the request, PingFederate redirects the request to this URL along with the relative resume path.This field is blank by default.                                                                                                                                                                           |
| **Authentication Context**                                     | This can be any value agreed upon with your SP partner that indicates how the user was authenticated. The value is included in the SAML assertion.This field is blank by default.                                                                                                                                                                                                     |

## Advanced fields

| Field Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Perform Authorize Request**        | The adapter makes an authorize request to SDG Conversion Token Service before accessing the protected resource.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Resource**                         | The resource that is protected by the agent.This field is required if **Perform Authorize Request** is selected.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Instance**                         | Refers to the name of the agent instance.This field is required if **Perform Authorize Request** is selected.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Action**                           | The action to take when evaluating requests against the policy server.This field is required if **Perform Authorize Request** is selected.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **PingFederate Base URL**            | The base URL for PingFederate, such as `https://pf_host:pf_port/`.The adapter uses this value to create the return URL **Cookie Provider URL** to create the return URL.Complete this field if you're using a cookie provider to enable single sign-on (SSO) across multiple domains.This field is blank by default.                                                                                                                                                                                                                                                                                                  |
| **Cookie Provider URL**              | The URL of the cookie provider. PingFederate redirects the request to this URL if the session cookie is in a separate domain.Complete this field if you're using a cookie provider to enable SSO across multiple domains.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                              |
| **Cookie Provider Target Parameter** | The name of parameter that contains the PingFederate return URL in the redirect to the cookie provider.Complete this field if you're using a cookie provider to enable SSO across multiple domains.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                    |
| **Session Cookie Prefix**            | The prefix to remove when **Remove Session Cookie Prefix** is selected.Complete this field if you're using a cookie provider to enable SSO across multiple domains.When using a cookie provider to enable SSO across multiple domains, tokens are prepended with the security zone name. This field works with the **Remove Session Cookie Prefix** setting to remove the security name prefix and to allow the adapter to process the token.Enter the **SSOZoneName** from your Agent Configuration Object (ACO) surrounded by `-`. For the default security zone name, enter `-SM-`.This field is blank by default. |
| **Remove Session Cookie Prefix**     | The adapter removes the **Session Cookie Prefix** from the beginning of the session cookie.Select this check box if you're using a cookie provider to enable SSO across multiple domains.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                         |
| **Disable Refresh Session Cookie**   | The adapter doesn't refresh session cookies when validating them. This allows other dependent applications to manage the session cookie.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **API Request Timeout**              | The time in milliseconds that PingFederate waits for SDG CTS to respond to requests and allows to establish a connection with SDG CTS. A value of `0` disables the timeout.The default value is `5000`.                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Proxy Settings**                   | Defines proxy settings for outbound HTTP requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Custom Proxy Host**                | The proxy server host name name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Custom Proxy Port**                | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

---

---
title: SDG CTS Integration Kit
description: The SDG CTS Integration Kit allows PingFederate to integrate with applications that are protected by SDG Conversion Token Service (CTS).
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# SDG CTS Integration Kit

The SDG CTS Integration Kit allows PingFederate to integrate with applications that are protected by SDG Conversion Token Service (CTS).

## Components

* SDG CTS IdP Adapter

  * Allows an identity provider enterprise to extend the SDG domain to include partner applications with a variety of protocols, such as SAML, WS-Federation, OAuth, and OpenID Connect.

  * Uses the CTS to validate and authorize tokens for use with PingFederate.

* SDG CTS SP Adapter

  * Allows a service provider enterprise to accept SAML or WS-Federation assertions and provide single sign-on (SSO) to applications that require a SDG-issued token.

  * Uses the CTS to create a SDG token based on the attributes in the assertion.

  * Can be configured to authorize the token against a specific resource.

## Intended audience

This document is intended for PingFederate administrators. If you need help during the setup process, you can find more information in:

* The following sections of the PingFederate documentation:

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Managing SP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html)

* The following SDG resources:

  * [SDG Token Service](https://www.sdgc.com/products-old/sdg-token-services/)

## System requirements

* PingFederate 11.3 or later

* SDG Token Service 1.5.4 (or later), acting as a secure token service between PingFederate and a policy server.

  * Available to download at no cost from [SDG Token Service](https://www.sdgc.com/products-old/sdg-token-services/).

---

---
title: SDG CTS SP Adapter settings reference
description: Field descriptions for the SDG CTS SP Adapter configuration page.
component: sdg
page_id: sdg:sdg_cts_integration_kit:pf_sdg_cts_ik_sp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/sdg/sdg_cts_integration_kit/pf_sdg_cts_ik_sp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  standard-fields: Standard fields
  advanced-fields: Advanced fields
---

# SDG CTS SP Adapter settings reference

Field descriptions for the SDG CTS SP Adapter configuration page.

## Standard fields

| Field Name                                                     | Description                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SDG Conversion Token Service URL**                           | The URL for the SDG Conversion Token Service.This field is blank by default.                                                                                                                                                                                                                                                                                                            |
| **Validate SDG Conversion Token Service Certificate Hostname** | The hostname of the server certificate presented by the SDG Conversion Token Service must match the hostname in the **SDG Conversion Token Service URL** field.This checkbox is selected by default.                                                                                                                                                                                    |
| **Client Certificate**                                         | The certificate that the adapter uses to authentication calls to SDG Conversion Token Service.                                                                                                                                                                                                                                                                                          |
| **SDG Conversion Token Service TokenType**                     | The token type that SDG Conversion Token Service is configured to provide to the adapter.The default and only value is `SMSESSION`.                                                                                                                                                                                                                                                     |
| **Cookie Name**                                                | The name of the cookie that contains the token used with SDG Conversion Token Service.This field is blank by default.                                                                                                                                                                                                                                                                   |
| **Cookie Domain**                                              | The domain name that the adapter uses when creating cookies. The browser compares this value to the domain of subsequent requests to determine whether the cookie should be submitted.If this field is blank, the adapter uses the domain name of the request. When sharing a cookie across subdomains, this value must be prefixed with a period (`.`).This field is blank by default. |
| **Cookie Path**                                                | The path that the adapter uses when creating cookies. The browser compares this value to the path of subsequent requests to determine whether the cookie should be submitted.The default value is `/`.                                                                                                                                                                                  |
| **Cookie Secure Flag**                                         | The adapter writes cookies with the Secure flag. The browser only submits Secure cookies on subsequent HTTPS requests.This checkbox is selected by default.                                                                                                                                                                                                                             |
| **SDG Conversion Token Service URL**                           | The URL for SDG Conversion Token Service.This field is blank by default.                                                                                                                                                                                                                                                                                                                |
| **Error URL**                                                  | When an error occurs in the adapter, PingFederate redirects the browser to this URL instead of to the default error page. This URL can contain query parameters. The URL has an `errorMessage` appended to it, which contains a brief description of the error that has occurred.This field is blank by default.                                                                        |
| **Logged-Out Cookie Value**                                    | The expected value of the cookie when the user has been signed off.The default value is `LOGGEDOFF`.                                                                                                                                                                                                                                                                                    |
| **HTTP Only Flag**                                             | When selected, the adapter sets a flag for the cookie. The flag indicates that the cookie should be read only through http requests and disallows Javascript from accessing the cookie.This checkbox is selected by default.                                                                                                                                                            |
| **Account Link URL**                                           | The URL to redirect the user to for account linking.This field is blank by default.                                                                                                                                                                                                                                                                                                     |

## Advanced fields

| Field Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Resource**                         | The resource that is protected by the agent.This field is required if **Perform Authorize Request** is selected.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Instance**                         | Refers to the name of the agent instance.This field is required if **Perform Authorize Request** is selected.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Action**                           | The action to take when evaluating requests against the policy server.This field is required if **Perform Authorize Request** is selected.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **PingFederate Base URL**            | The base URL for PingFederate, such as `https://pf_host:pf_port/`.The adapter uses this value to create the return URL **Cookie Provider URL** to create the return URL.Complete this field if you are using a cookie provider to enable single sign-on (SSO) across multiple domains.This field is blank by default.                                                                                                                                                                                                                                                                                                 |
| **Cookie Provider URL**              | The URL of the cookie provider. PingFederate redirects the request to this URL if the session cookie is in a separate domain.Complete this field if you're using a cookie provider to enable SSO across multiple domains.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                              |
| **Cookie Provider Target Parameter** | The name of parameter that contains the PingFederate return URL in the redirect to the cookie provider.Complete this field if you're using a cookie provider to enable SSO across multiple domains.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                    |
| **Session Cookie Prefix**            | The prefix to remove when **Remove Session Cookie Prefix** is selected.Complete this field if you're using a cookie provider to enable SSO across multiple domains.When using a cookie provider to enable SSO across multiple domains, tokens are prepended with the security zone name. This field works with the **Remove Session Cookie Prefix** setting to remove the security name prefix and to allow the adapter to process the token.Enter the **SSOZoneName** from your Agent Configuration Object (ACO) surrounded by `-`. For the default security zone name, enter `-SM-`.This field is blank by default. |
| **Remove Session Cookie Prefix**     | The adapter removes the **Session Cookie Prefix** from the beginning of the session cookie.Select this checkbox if you're using a cookie provider to enable SSO across multiple domains.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                          |
| **Disable Refresh Session Cookie**   | The adapter doesn't refresh session cookies when validating them. This allows other dependent applications to manage the session cookie.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **API Request Timeout**              | The time in milliseconds that PingFederate waits for SDG CTS to respond to requests and allows to establish a connection with SDG CTS. A value of `0` disables the timeout.The default value is `5000`.                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Proxy Settings**                   | Defines proxy settings for outbound HTTP requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Custom Proxy Host**                | The proxy server host name name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Custom Proxy Port**                | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Perform Authorize Request**        | The adapter makes an authorize request to SDG Conversion Token Service before accessing the protected resource.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Send Extended Attributes**         | The method that the adapter uses to send extended attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Send Session Attributes**          | Includes the attribute contract as session attributes in the call to SDG Conversion Token Service.The default selection is `None`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **OpenToken Transfer Method**        | The method that the adapter uses to transport the OpenToken.The default selection is `Query Parameter`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **OpenToken Name**                   | The name of the cookie or request attribute that contains the OpenToken.This name should be unique for each adapter instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **OpenToken Password**               | The password that the adapter uses when encrypting extended attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Send Session Attributes**          | When selected, the adapter includes the attribute contract as session attributes in the call to SDG Conversion Token Service.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Ignore Session Cookie**            | When selected, the adapter ignores any existing session cookie on the request and creates a new one.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

---

---
title: SDG integrations
description: The PingFederate SDG CTS Integration Kit allows PingFederate administrators to integrate their applications protected by a SDG Conversion Token Service (CTS) with a PingFederate server acting as either an identity provider (IdP) or as a service provider (SP).
component: sdg
page_id: sdg::pf_is_overview_sdg_integrations
canonical_url: https://docs.pingidentity.com/integrations/sdg/pf_is_overview_sdg_integrations.html
llms_txt: https://docs.pingidentity.com/integrations/sdg/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 22, 2026
section_ids:
  pingfederate-sdg-cts-integration-kit: PingFederate SDG CTS Integration Kit
  pingfederate-sdg-token-translator: PingFederate SDG Token Translator
---

# SDG integrations

## PingFederate SDG CTS Integration Kit

The PingFederate SDG CTS Integration Kit allows PingFederate administrators to integrate their applications protected by a SDG Conversion Token Service (CTS) with a PingFederate server acting as either an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* or as a service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)*.

## PingFederate SDG Token Translator

The PingFederate SDG Token Translator provides a token processor and token generator for use with the PingFederate's WS-Trust Security Token Service (STS) *(tooltip: \<div class="paragraph">
\<p>An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.\</p>
\</div>)*.