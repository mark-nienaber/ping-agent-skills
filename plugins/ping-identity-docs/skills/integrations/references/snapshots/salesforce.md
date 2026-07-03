---
title: Add an SSO link in Salesforce (example)
description: Create a dynamic single sign-on (SSO) link and add it to your Salesforce page.
component: salesforce
page_id: salesforce:salesforce_login_integration_kit:pf_salesforce_cic_add_an_sso_link_in_salesforce_example
canonical_url: https://docs.pingidentity.com/integrations/salesforce/salesforce_login_integration_kit/pf_salesforce_cic_add_an_sso_link_in_salesforce_example.html
revdate: June 25, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Add an SSO link in Salesforce (example)

Create a dynamic single sign-on (SSO) link and add it to your Salesforce page.

## Steps

1. In the Salesforce administrative console, go to **Setup > Customize > Home > Custom Links**.

2. On the **Home** page, in the **Custom Links** section, click **New**.

3. Complete the **Label**, **Name**, and **Description** fields.

4. In the **Content Source** list, select **URL**.

5. In the text area, enter one of the following URLs:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can insert `{!API.Session_ID}` and `{!API.Partner_Server_URL_200}` or equivalent by selecting **$Api** from the **Select Field Type** list and then selecting the variable you want from the **Insert Field** list.Salesforce dynamically populates these variables when the user clicks the link. Learn more about [Global Variables](https://help.salesforce.com/articleView?id=sf.dev_understanding_global_variables.htm) in the Salesforce documentation. |

   ### **Choose from:**

   * For SSO through an SP-partner connection in PingFederate:

     ```shell
     https://pf_host:pf_port/idp/startSSO.ping?
     sid={!API.Session_ID}&apiendpoint={!API.Partner_Server_URL_200}&
     TargetResource=destination_URL&
     PartnerSpId=connection_ID
     ```

     Replace the variables as follows:

     * *pf\_host*: The host name or IP address of the PingFederate server.

     * *pf\_port*: The port number of the PingFederate server.

     * *destination\_URL*: The fully-qualified URL of the target application or other protected resource.

     * *connection\_ID*: The **Partner's Entity ID (Connection ID)** of the service provider (SP) connection that you configured.

       Example URL:

       ```shell
       https://pingfederate.example.com:9031/idp/startSSO.ping?sid={!API.Session_ID}&apiendpoint={!API.Partner_Server_URL_200}&TargetResource=https://portal.example.com/welcome&PartnerSpId=SFConnection1
       ```

   * For SSO through IdP-to-SP adapter mapping in PingFederate:

     ```shell
     https://pf_host:pf_port/pf/adapter2adapter.ping?
     sid={!API.Session_ID}&apiendpoint={!API.Partner_Server_URL_200}&
     TargetResource=destination_URL&
     IdpAdapterId=adapter_ID
     ```

     Replace the variables as follows:

     * *pf\_host*: The host name or IP address of the PingFederate server.

     * *pf\_port*: The port number of the PingFederate server.

     * *destination\_URL*: The fully-qualified URL of the target application or other protected resource.

     * *adapter\_ID*: The **Instance ID** of the Salesforce IdP Adapter that you configured.

       Example URL:

       ```shell
       https://pingfederate.example.com:9031/pf/adapter2adapter.ping?sid={!API.Session_ID}&apiendpoint={!API.Partner_Server_URL_200}&TargetResource=https://portal.example.com/welcome&IdpAdapterId=SFAdapter1
       ```

6. Click **Save**.

7. Go to **Setup > Customize > Home Page Components**.

8. Add a new link component using the custom link that you created.

9. Go to **Setup > Customize > Home Page Layout**.

10. Edit your existing layout or create a new layout to include the new link component.

11. Check that the user profile is configured to use the page layout that you modified.
