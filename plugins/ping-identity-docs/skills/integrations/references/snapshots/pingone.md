---
title: Adding an application in DaVinci
description: Create an application to associate your PingFederate integration with your flow.
component: pingone
page_id: pingone:pingone_davinci_integration_kit:pf_p1_davinci_ik_adding_an_application_in_davinci
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_davinci_integration_kit/pf_p1_davinci_ik_adding_an_application_in_davinci.html
revdate: June 19, 2024
section_ids:
  steps: Steps
---

# Adding an application in DaVinci

Create an application to associate your PingFederate integration with your flow.

## Steps

1. Sign on to the DaVinci admin portal.

2. Create a blank flow:

   1. Go to **Flows** and click **[icon: plus, set=fa]Add Flow**.

   2. Select **Blank Flow**.

   3. On the **Add Flow** dialog, enter a name for your flow. Click **Create**.

   4. Complete the flow as described in [Building a flow in DaVinci](pf_p1_davinci_ik_building_a_flow_in_davinci.html).

3. Add an application:

   1. Go to **Applications**.

   2. Click **[icon: plus, set=fa]Add Application**

   3. On the **Add Application** dialog, enter a name for your application. Click **Create**.

   4. Click your application.

4. Add a flow policy to your application:

   1. On the **Flow Policy** tab, click **[icon: plus, set=fa]Add Flow Policy**.

   2. Select the flow that you made in step 2. Select **Latest Version** or another version. Click **Create My Flow Policy**.

   3. On the **Edit Your Weight Distribution** dialog, in the **Analytics - Select Success Nodes** list, select your **Send success JSON response** node. Click **Save My Flow Policy**.

   4. On the **Flow Policy** tab, note your **Policy ID**. You'll use this to configure the DaVinciadapter.

5. On the **General** tab, note your **Company ID** and **API Key**. You'll use these to configure the DaVinci adapter.
