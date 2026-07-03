---
title: Adding SSO to a connection
description: To enable single sign-on (SSO), modify the provisioning connection that you created in Creating a provisioning connection.
component: scim
page_id: scim:setup:pf_scim_connector_adding_sso_to_a_connection
canonical_url: https://docs.pingidentity.com/integrations/scim/setup/pf_scim_connector_adding_sso_to_a_connection.html
revdate: July 8, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding SSO to a connection

To enable single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*, modify the provisioning connection that you created in [Creating a provisioning connection](pf_scim_connector_creating_a_provisioning_connection.html).

## Steps

1. On the PingFederate administrative console, open your existing SP connection.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Select your connection.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Select your connection.

2. On the **Connection Type** tab select **Browser SSO Profiles**. Click **Next**.

3. On the **Browser SSO** tab, configure your SSO settings.

   You can find specific connection details in the documentation and administrative console provided by the target service.

   You can find configuration help in [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

4. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.
