---
title: Add an application in Aquera
description: Configure the target service as an application in Aquera and note the connection credentials.
component: aquera
page_id: aquera:setup:pf_aquera_connector_add_an_application_in_aquera
canonical_url: https://docs.pingidentity.com/integrations/aquera/setup/pf_aquera_connector_add_an_application_in_aquera.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Add an application in Aquera

Configure the target service as an application in Aquera and note the connection credentials.

## Steps

1. Sign on to the Aquera [Applications](https://admin.aquera.io/securehome/endpoints) page.

2. Click **Add Application** and select the target service.

3. Configure the application. Learn more by searching for the the target service configuration steps in [Connectors](https://support.aquera.com/hc/en-us/categories/115000284613-Connectors) in the Aquera documentation.

4. On the **Applications** page, select the application that you added.

5. On the **Configure Application** window, from the **Copy this URL** field, note your SCIM URL.

6. Note your application credentials.

   Credentials can be a bearer token or a username and password pair. If both types of credentials are provided, note the bearer token.

   On the application details page, the credentials can appear in the following locations:

   * Right sidebar, in the **Authorization** section:

     * **Bearer**

   * Main window, in the **Credential To Access *\<application name>*** section:

     * **Token**

     * **Username**, **Password**

       |   |                                                                               |
       | - | ----------------------------------------------------------------------------- |
       |   | Aquera shows tokens and passwords as dots, but you can still copy the values. |
