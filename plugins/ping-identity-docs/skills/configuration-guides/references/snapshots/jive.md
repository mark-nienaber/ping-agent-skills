---
title: Configuring SAML SSO with Jive and PingFederate
description: Learn how to configure SAML SSO with Jive and PingFederate.
component: configuration_guides
page_id: configuration_guides:jive:config_saml_jive_pf
canonical_url: https://docs.pingidentity.com/configuration_guides/jive/config_saml_jive_pf.html
revdate: May 15, 2024
section_ids:
  about-this-task: About this task
  create-the-pingfederate-sp-connection-for-jive: Create the PingFederate SP Connection for Jive
  configure-the-pingfederate-idp-connection-for-jive: Configure the PingFederate IdP connection for Jive
---

# Configuring SAML SSO with Jive and PingFederate

Learn how to configure SAML SSO with Jive and PingFederate.

## About this task

The following table details the references that are used within this guide that are environment specific. Replace these with the suitable value for your environment.

| Reference      | Description                              |
| -------------- | ---------------------------------------- |
| *jiveinstance* | The host and port for the Jive instance. |

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The following configuration is untested and is provided as an example. Additional steps might be required. |

## Create the PingFederate SP Connection for Jive

1. Sign on to the Jive Admin Console and enable single sign-on:

   1. Go to **People → Settings → Single Sign-On → SAML**.

   2. Check **Enabled**.

   3. Click **Save**.

   4. Restart Jive.

      |   |                                                                                                                                   |
      | - | --------------------------------------------------------------------------------------------------------------------------------- |
      |   | Until SAML configuration is complete, you'll need to sign on by going directly to the admin console, `http://jiveinstance/admin`. |

2. Download the Jive metadata from `http://jiveinstance/saml/metadata`.

3. Sign on to the PingFederate administrative console.

4. Using the metadata that you downloaded, create an SP connection in Ping Federate:

   1. Configure using **Browser SSO** profile **SAML 2.0**.

   2. Enable the following **SAML Profiles**:

      * **IdP-Initiated SSO**

      * **SP-Initiated SSO**

   3. In **Assertion Creation: Attribute Contract**, set the **Subject Name Format** to `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`.

   4. In the **Assertion Creation: Attribute Contract Fulfilment**, map the attribute **SAML\_SUBJECT** to the attribute `username`.

   5. Add any additional attributes required into the attribute contract and contract fulfillment.

   6. In **Protocol Settings: Allowable SAML Bindings**, enable **POST**, and **Redirect**.

5. Export the metadata for the newly-created SP connection.

6. Export the signing certificate public key.

## Configure the PingFederate IdP connection for Jive

1. Sign on to the Jive Admin Console and go to **People → Settings → Single Sign-On → SAML**.

2. On the **IdP Metadata** tab, copy the contents of the metadata file into the metadata field.

3. Click **Save All SAML Settings**.

4. On the **User Attribute Mapping** tab, map the user attributes in the Jive profile to the attributes that you configured in PingFederate.

5. **Optional:** Select **Group Mapping Enabled** if you want to assign users to groups with a group attribute passed in the assertion.

6. Click **Save Settings**.
