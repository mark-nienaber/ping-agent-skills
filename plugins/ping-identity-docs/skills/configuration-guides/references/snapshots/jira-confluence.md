---
title: Configuring SAML SSO with Jira/Confluence and PingFederate
description: Learn how to configure SAML single sign-on with Jira/Confluence on premise and PingFederate.
component: configuration_guides
page_id: configuration_guides:jira_confluence:config_saml_jira_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/jira_confluence/config_saml_jira_pf.html
revdate: May 15, 2024
section_ids:
  about-this-task: About this task
  create-a-pingfederate-sp-connection-for-jiraconfluence: Create a PingFederate SP Connection for Jira/Confluence
  configure-the-pingfederate-idp-connection-for-jiraconfluence-on-premise: Configure the PingFederate IdP connection for Jira/Confluence on premise
---

# Configuring SAML SSO with Jira/Confluence and PingFederate

Learn how to configure SAML single sign-on with Jira/Confluence on premise and PingFederate.

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name    | Description | Required / Optional |
| ----------------- | ----------- | ------------------- |
| **SAML\_SUBJECT** | Username    | Required            |

## Create a PingFederate SP Connection for Jira/Confluence

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

1. Sign on to Atlassian application as an administrator and go to **Administration → System → SAML Authentication**.

2. Select **SAML Single Sign On**and note the **Audience URL (Entity ID)** and **Assertion Consumer Service URL** values.

3. Download the signing certificate.

4. Sign on to the PingFederate administrative console.

5. Using the details retrieved from the Atlassian application UI:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Enable **IdP-Initiated SSO** and **SP Initiated SSO**.

   3. In **Assertion Creation: Attribute Contract**, set the Subject Name Format to `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`.

   4. In the **Assertion Creation: Attribute Contract Fulfilment**, map the attribute **SAML\_SUBJECT** to the attribute **username**.

   5. In **Protocol Settings: Allowable SAML Bindings**, enable **Post** and **Redirect**.

6. Export the metadata for the newly-created SP connection.

7. Export the signing certificate public key.

## Configure the PingFederate IdP connection for Jira/Confluence on premise

1. Sign on to Atlassian application as an administrator and go to **Administration → System → SAML Authentication**.

2. Select **SAML Single Sign-On**.

3. Configure the following.

   | Setting                                  | Value                                                                                                                                                         |
   | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Single sign-on issuer**                | The issuer ID for your PingFederate instance. You can retrieve this from the metadata that you downloaded.                                                    |
   | **Identity provider single sign-on URL** | The PingFederate **SingleSignOnService** URL. You can retrieve this from the metadata that you downloaded. For example, `https://hostname:port/idp/SSO.saml2` |
   | **X509 Certificate**                     | Upload the PingFederate signing public certificate.                                                                                                           |
   | **Login Mode**                           | Choose whether SAML is primary or secondary authentication.                                                                                                   |

   Configuration is complete.
