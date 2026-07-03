---
title: Configuring SAML SSO with BambooHR and PingFederate
description: The following table details the required and optional attributes to be configured in the assertion attribute contract.
component: configuration_guides
page_id: configuration_guides:bamboohr:config_saml_bamboohr_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/bamboohr/config_saml_bamboohr_pf.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
  choose-from: Choose from:
---

# Configuring SAML SSO with BambooHR and PingFederate

## About this task

The following table details the required and optional attributes to be configured in the assertion attribute contract.

| Attribute Name                                           | Description            | Required / Optional |
| -------------------------------------------------------- | ---------------------- | ------------------- |
| `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` | Email address for user | Required            |

The following table details the references that are used within this guide which are environment specific. Replace these with the suitable value for your environment.

| Reference | Description          |
| --------- | -------------------- |
| *tenant*  | BambooHR Tenant name |

## Steps

1. Create the PingFederate service provider (SP) connection for BambooHR.

   1. Sign on to the PingFederate administrative console.

   2. Using the metadata from `https://tenant.bamboohr.com/saml/sp_metadata.php`, create an SP connection in PingFederate:

      * Configure using **Browser SSO** profile **SAML 2.0**

      * Enable the **IdP-Initiated SSO** SAML profile.

      * Enable the **SP initiated SSO** SAML profile.

      * In **Assertion Creation → Attribute Contract**, set the **Subject Name Format** to **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

      * In **Assertion Creation → Attribute Contract Fulfillment**, map the attribute **SAML\_SUBJECT** to the attribute **mail**.

      * In **Protocol Settings → Allowable SAML Bindings**, enable **Redirect**.

   3. Export the metadata for the newly-created SP connection.

   4. Export the signing certificate public key.

      ![Screen capture illustrating the Applications > SP Connections page on the PingFederate administrative console.](_images/xlq1619029597861.png)

2. Configure the PingFederate identity provider (IdP) connection for BambooHR.

   1. Sign on to BambooHR as a Full Admin administrator user.

   2. On the **Settings** page, click **Apps**.

   3. On the **SAML Single Sign-On** application published by BambooHR line, click **Install**.

      ![Screen capture illustrating the SAML SSO application available for installation.](_images/clh1619029740667.png)

   4. In the **SSO Login URL** field, enter the URL Location for **SingleSignOnService Location** retrieved from the PingFederate SP metadata that you downloaded from the BambooHR configuration.

      ### Example:

      `https://PingFederateHostname:PingFederatePort/idp/SSO.saml2`

   5. In a text editor, open the signing certificate that you downloaded in from PingFederate and paste the contents into the **x.509 Certificate** field.

      ![Screen capture illustrating the SAML SSO Login URL and the x.509 Certificate metadata.](_images/gji1619029838840.png)

   6. Click **Install**.

      ### Result:

      Your configuration is complete.

      From this point BambooHR will redirect to the configured IdP for authentication for all new sessions. You should complete testing in a private or incognito browser session while keeping the original admin session active. This allows you to change settings or remove the configuration if the integration testing fails.

      ![Screen capture illustrating the SAML SSO application installed on the BambooHR website.](_images/nfy1619029926655.png)

3. Test the integration.

   ### Choose from:

   * PingFederate IdP-initiated SSO

     1. Go to the **SSO Application** in the PingFederate Application configuration to perform IdP-initiated SSO, such as https\://*PingFederateHostname*:*PingFederatePort*/idp/startSSO.ping?PartnerSpId=BambooHR-SAML.

        ![Screen capture illustrating the IdP SSO sign-on window.](_images/gof1619030025224.png)

     2. Go to the SSO Application Endpoint in the BambooHR configuration

        ![Screen capture illustrating the SSO Application endpoint in the BambooHr configuration.](_images/kre1619030073899.png)

   * PingFederate SP-initiated SSO

     Go to the URL for your BambooHR tenant: https\://*tenant*.bamboohr.com

     ![Screen capture illustrating the BambooHR tenant URL.](_images/pat1619030364471.png)
