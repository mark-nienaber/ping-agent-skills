---
title: Adding SSO to a connection
description: To enable single sign-on (SSO) to Workplace from Facebook, modify the provisioning connection that you created in Creating a provisioning connection.
component: facebook
page_id: facebook:workplace_from_facebook_provisioner:pf_workplace_connector_adding_sso_to_a_connection
canonical_url: https://docs.pingidentity.com/integrations/facebook/workplace_from_facebook_provisioner/pf_workplace_connector_adding_sso_to_a_connection.html
revdate: June 11, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Adding SSO to a connection

To enable single sign-on (SSO) to Workplace from Facebook, modify the provisioning connection that you created in [Creating a provisioning connection](pf_workplace_connector_creating_a_provisioning_connection.html).

## Steps

1. On the PingFederate administrator console, open your existing SP connection.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Select your connection.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Select your connection.

2. On the **Connection Type** tab select **Browser SSO Profiles**. Click **Next**.

3. On the **Browser SSO** tab, configure your SSO settings.

   1. Go to **Browser SSO > SAML Profiles** and select only **IdP-Initiated SSO** and **SP-Initiated SSO**.

   2. Go to **Browser SSO > Assertion Creation > Attribute Contract**. For **SAML\_SUBJECT**, select **urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress**.

   3. On the **Authentication Policy Mapping** tab, select or create an authentication source that maps `SAML_SUBJECT` to an email attribute that matches the email addresses used in Workplace from Facebook.

   For configuration help, see [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

4. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation.

   * On the **Digital Signature Settings** tab, from the **Signing Certificate** list, select the certificate that you want to use with Workplace from Facebook.

5. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.
