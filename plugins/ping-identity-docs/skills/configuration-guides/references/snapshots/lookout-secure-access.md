---
title: Configuring SAML SSO with Lookout Secure Access
description: The Ping Identity and Lookout SAML integration supports service provider (SP) and identity provider (IdP) initiated single sign-on (SSO).
component: configuration_guides
page_id: configuration_guides:lookout_secure_access:config_saml_sso_lookout_secure_access
canonical_url: https://docs.pingidentity.com/configuration_guides/lookout_secure_access/config_saml_sso_lookout_secure_access.html
revdate: June 7, 2024
section_ids:
  what-it-is: What it is
  what-youll-need: What you'll need
  what-youll-do: What you'll do
  step-1-gather-the-sp-metadata: "Step 1: Gather the SP metadata"
  step-2-configure-the-sp-in-pingone: "Step 2: Configure the SP in PingOne"
  step-3-configure-the-idp-in-lookout: "Step 3: Configure the IdP in Lookout"
  step-4-enable-sso-for-the-lookout-management-console-endpoint-client-and-proxy-authentication: "Step 4: Enable SSO for the Lookout management console, endpoint client, and proxy authentication"
  step-5-configure-idp-initiated-sign-on-for-lookout-management-console: "Step 5: Configure IdP-initiated sign-on for Lookout management console"
  step-6-test-sso-with-lookout-secure-access: "Step 6: Test SSO with Lookout Secure Access."
---

# Configuring SAML SSO with Lookout Secure Access

The Ping Identity and Lookout SAML integration supports service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* and identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* initiated single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

## What it is

Lookout Cloud Security (Lookout SSE platform) is a data-centric cloud security solution that protects users from internet-based threats and protects data stored in cloud applications, private applications, and websites.

Lookout Cloud Security supports the following cloud security components:

* Lookout Secure Internet Access

  Protection for web or non-web internet-based traffic.

* Lookout Secure Private Access

  Protection for private application traffic.

* Lookout Secure Cloud Access

  Protection for cloud application traffic.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Users must authenticate with your enterprise SSO provider during their initial access before accessing solutions such as Secure Internet Access and Secure Cloud Access. |

The Lookout Cloud Security platform leverages the user or user group context to enforce access and activity policies on cloud apps, private apps, and websites.

## What you'll need

* Have a PingOne account. Learn more in [Starting a PingOne trial](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_start_a_p1_trial.html).

* Verify that you can sign on to the PingOne admin console. Learn more in [Accessing the PingOne admin console](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_access_admin_console.html).

* Have a Lookout SSE platform account. To enroll in a Lookout SSE platform account, contact [Lookout](https://security.lookout.com/contact/enterprise-contact-us).

## What you'll do

To configure SAML SSO with Lookout Secure Access:

1. Gather the service provider (Lookout Secure Access) metadata.

2. Configure the service provider in PingOne.

3. Configure the identity provider (PingOne) in Lookout.

4. Enable SSO for the Lookout management console, endpoint client, and proxy authentication.

5. Configure IdP-initiated sign-on for Lookout management console.

6. Test SSO with Lookout Secure Access.

## Step 1: Gather the SP metadata

To use PingOne as an IdP, you'll capture SAML values from the Lookout Management console:

1. In the Lookout Management console, go to **Administration → Enterprise Integration**.

2. Go to **Configuration → Single Sign-On**.

3. On the **SSO Groups** tab, go to the default group.

4. In the **SP Metadata** column, click the **Download** icon.

   The **SP Metadata** window opens.

5. Copy the **Assertion Consumer Service (ACS) URL** and **Entity ID** values.

## Step 2: Configure the SP in PingOne

After you've captured the SAML values from Lookout Secure Access, you'll configure a SAML-based application in PingOne. This gives PingOne the information it needs to communicate with the Lookout Cloud Security Platform so that the platform can enforce policies based on user credentials.

1. In the PingOne admin console, go to **Applications → Application Catalog** and browse or search for `Lookout Secure Access`.

2. Click the **Lookout Secure Access** entry to open the details panel.

3. For **Quick Setup**, enter the following information:

   * **ACS URL**: Enter the **Assertion Consumer Service** value that you copied previously.

   * **Entity ID**: Enter the **Entity ID** value that you copied previously.

4. Click **Next**.

5. On the **Map Attributes** page, click **Next**.

6. On the **Select Groups** page, click **Save** without assigning groups.

   This allows users to have access to all applications by default.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | Assign groups to the application to restrict access to only those groups. |

7. In **Application Instances**, select the **Lookout Secure Access Application** entry to open the **Connection Details** page.

8. On the **Connection Details** page, copy the **IDP Metadata URL** to use when configuring the SP.

## Step 3: Configure the IdP in Lookout

Next, you'll link your PingOne instance to the Lookout Cloud Security Platform by configuring a new IdP instance. Lookout uses to retrieve user information from PingOne.

1. In the Lookout Management Console, go to **Administration → Enterprise Integration**.

2. Go to **Configuration → Single Sign-On**.

3. On the **SSO Providers** tab, click **New**.

4. Enter or select the following values:

   * **Name**: Enter a name that contains no more than 255 characters.

   * **Type**: Select **Identity Provider**.

   * **SSO Group**: Select **Default**.

   * **Metadata Link**: Enter the **IDP Metadata URL** value that you copied from the PingOne.

5. Click **Validate** and confirm that the Management Console populates the **Entity ID** field.

6. Click **Save**.

## Step 4: Enable SSO for the Lookout management console, endpoint client, and proxy authentication

After you've configured the service provider, you'll enable SSO for the Lookout Cloud Security Platform.

1. In the Lookout Management Console, go to **Administration → System Settings → Enterprise Authentication**.

2. In the **Identity Provider** list, choose the IdP that you created.

3. To enable the **Management SSO**, click the toggle.

4. To enable the **Endpoint**, click the toggle.

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | The **Native Proxy Authentication** toggle is enabled by default and cannot be disabled. |

5. Click **Save**.

## Step 5: Configure IdP-initiated sign-on for Lookout management console

Next, to set up IdP-initiated sign-on for the Lookout Management Console, you'll configure relay state on PingOne.

1. In the Lookout Management Console, go to **Administration → System Settings → Enterprise Authentication**.

2. In the **Enterprise Single Sign-on Settings** field, click **Copy** to copy the **Relay State** value.

3. In the PingOne admin console, go to **Applications → Applications**.

4. Click the **Lookout Secure Access** entry.

5. On the **Overview** tab, click **Enable Advanced Configuration**.

   The **Enable Advanced Configuration** window opens.

6. Click **Enable**.

7. On the **Configuration** tab, click on the **Pencil** icon to edit the **Connection Details**.

8. In the **Target Application URL** field, paste the **Relay State** value that you copied from the Lookout Management Console.

9. Click **Save**.

## Step 6: Test SSO with Lookout Secure Access.

After you've configured IdP-initiated sign-on, you'll verify that SSO works.

1. In the PingOne admin console, go to **Applications → Applications**.

2. Click the **Lookout Secure Access** entry.

3. On the **Configuration** tab, copy the **Initiate Single Sign-On URL** value.

4. Paste the URL in a new browser window and hit enter.

   You are successfully redirected to the Lookout Management Console.
