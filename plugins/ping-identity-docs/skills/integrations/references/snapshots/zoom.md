---
title: Add the Zoom metadata URL in PingFederate
description: To provide PingFederate with information about Zoom as a SAML partner, register the Zoom metadata URL.
component: zoom
page_id: zoom:setup:pf_zoom_connector_add_zoom_metadata
canonical_url: https://docs.pingidentity.com/integrations/zoom/setup/pf_zoom_connector_add_zoom_metadata.html
revdate: June 5, 2025
section_ids:
  steps: Steps
---

# Add the Zoom metadata URL in PingFederate

To provide PingFederate with information about Zoom as a SAML partner, register the Zoom metadata URL.

## Steps

1. On the PingFederate administrative console, on the **Security > Partner Metadata URLs** tab, click **Add New URL**.

2. On the **URL** tab, in the **Name** field, enter a name.

3. In the **URL** field, enter `https://your_vanity_url.zoom.us/saml/metadata/sp`. Click **Load Metadata**, then **Next**.

4. On the **Certificate Summary** tab, click **Next**.

5. On the **Summary** tab, click **Done**.

6. On the **Partner Metadata URLs** tab, click **Save**.
