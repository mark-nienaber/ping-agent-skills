---
title: Adding the OpenToken HTTP Module in IIS
description: The OpenToken HTTP module allows your IIS server to communicate with PingFederate using the OpenToken format.
component: microsoft-iis
page_id: microsoft-iis:setup:pf_iis_ik_adding_the_opentoken_http_module_in_iis
canonical_url: https://docs.pingidentity.com/integrations/microsoft-iis/setup/pf_iis_ik_adding_the_opentoken_http_module_in_iis.html
revdate: July 2, 2025
section_ids:
  steps: Steps
  example: Example:
---

# Adding the OpenToken HTTP Module in IIS

The OpenToken HTTP module allows your IIS server to communicate with PingFederate using the OpenToken format.

## Steps

1. In the Internet Information Services (IIS) Manager, select the IIS server.

2. On the **Features View** tab, double-click **Modules**.

3. On the **Modules** window, in the **Actions** section, click **Add Managed Module**.

4. On the **Add Managed Module** dialog, in the **Name** field, enter a name.

   ### Example:

   `OpenTokenHttpModule`

5. In the **Type** field, enter the following:

   `OpenTokenModule.HttpModule, OpenTokenModule, Version=3.5.0.0, Culture=neutral, PublicKeyToken=f5ed9639debbca65`

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | The OpenToken HTTP Module doesn't automatically appear in the module selection list. |

6. Click **OK**.
