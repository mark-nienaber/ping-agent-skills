---
title: Adding PingOne as an authentication provider in Code42
description: To allow PingOne to coordinate authentication with Code42, upload your SAML metadata.
component: code42-pingone
page_id: code42-pingone:single_sign-on_setup:p1_code42_integration_adding_p1_as_an_authentication_provider_in_code42
canonical_url: https://docs.pingidentity.com/integrations/code42-pingone/single_sign-on_setup/p1_code42_integration_adding_p1_as_an_authentication_provider_in_code42.html
revdate: June 26, 2024
section_ids:
  steps: Steps
---

# Adding PingOne as an authentication provider in Code42

To allow PingOne to coordinate authentication with Code42, upload your SAML metadata.

## Steps

1. Sign on to Code42 as an administrator.

2. Navigate to **Integrations > Identity Management**.

3. On the **Authentication** tab, click **Add authentication provider**.

4. On the **Add authentication provider** dialog, enter a name and select **Upload file**. Select the `saml2-metadata-idp-***.xml` file that you downloaded in [Creating an SSO connection in PingOne](p1_code42_integration_creating_an_sso_connection_in_p1.html). Click **Create provider**.

5. In the **Attribute mapping** section, click the pencil icon.

6. Clear the **Use default mapping** checkbox.

7. In the **Username** field, enter `mail`.

   ![A screenshot that shows the Username attribute mapped to mail.](_images/npf1627424023450.jpg)

8. Click **Save**.

9. Go to **Environment > Organizations**.

10. Add a new organization, or select an existing one.

11. In the organization details, on the **Settings** list, select **Edit**.

    ![A screenshot that shows the Settings menu with Edit highlighted.](_images/qgd1627424715354.jpg)

12. On the **Security** tab, in the **Servers** section, clear the **Inherit security settings from parent** checkbox.

13. On the **Select an authentication method** list, select **SSO**, then select the authentication provider you added.

14. On the **Select a directory service** list, select **Local** for testing purposes.

15. Click **Save**.

16. If you see a prompt to enable single sign-on, enter `ENABLE`, then click **Enable**.
