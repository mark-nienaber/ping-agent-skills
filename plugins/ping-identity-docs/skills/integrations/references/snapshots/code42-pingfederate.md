---
title: Adding PingFederate as an authentication provider in Code42
description: To allow PingFederate to coordinate authentication with Code42, upload your SAML metadata.
component: code42-pingfederate
page_id: code42-pingfederate:single_sign-on_setup:pf_code42_integration_adding_pf_as_an_authentication_provider_in_code42
canonical_url: https://docs.pingidentity.com/integrations/code42-pingfederate/single_sign-on_setup/pf_code42_integration_adding_pf_as_an_authentication_provider_in_code42.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Adding PingFederate as an authentication provider in Code42

To allow PingFederate to coordinate authentication with Code42, upload your SAML metadata.

## Steps

1. Sign on to Code42 as an administrator.

2. Navigate to **Integrations > Identity Management**.

3. On the **Authentication** tab, click **Add authentication provider**.

4. On the **Add authentication provider** dialog, enter a name and select **Upload file**. Select the file that you exported in [Exporting SAML metadata from PingFederate](pf_code42_integration_exporting_saml_metadata_from_pf.html). Click **Create Provider**.

5. On the provider detail page, note the **Code42 Service Provider Metadata URL**.
