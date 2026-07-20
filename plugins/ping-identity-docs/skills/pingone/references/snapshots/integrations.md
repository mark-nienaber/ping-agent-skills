---
title: Adding a RADIUS gateway
description: Add a RADIUS gateway in PingOne to bridge your on-premise VPN or remote access system with PingOne authentication flows.
component: pingone
page_id: pingone:integrations:p1_add_radius_gateway
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_radius_gateway.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 22, 2024
section_ids:
  steps: Steps
  result: Result:
  next-steps: Next steps
---

# Adding a RADIUS gateway

Add a RADIUS gateway to allow PingOne to communicate with your RADIUS clients.

## Steps

1. Go to **Integrations → Gateways**.

2. Click the **[icon: plus, set=fa]**icon.

3. Enter the following and click **Next**:

   * **Name**: A name for the gateway. The name must be unique within the environment.

   * **Gateway Type**: Select **RADIUS**.

   * **Description** (optional): A brief description of the gateway.

4. **Optional:** In the **Authentication Port** field, enter the relevant port number. The default is 1812.

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | You must stop all active gateway instances before modifying the authentication port. |

5. In the **DaVinci Policy ID** field, select the DaVinci Policy ID that you want to apply to the RADIUS gateway.

6. If you want to define a **Default Shared Secret**, enter it here.

   If no default is defined, you must enter a **Client Shared-Secret** for each **Client IP address** that you add.

   |   |                                                                                 |
   | - | ------------------------------------------------------------------------------- |
   |   | For security reasons, you should rotate the shared secret at least once a year. |

7. **Optional:** To incorporate a Network Policy Server (NPS), configure the following settings:

   1. Select the **Use RADIUS Remote Network Policy Server** check box.

   2. Enter the relevant NPS **Server IP** and **Server port**.

      |   |                                                                                                                                                                                                               |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Because validation of the client IP shared secret is performed on the RADIUS gateway side and the NPS side, you must make sure the shared secret on the client matches the shared secret on the endpoint NPS. |

8. In the **RADIUS clients** area, for each client that you want to add:

   1. Click **Add Client**.

   2. In the new row, enter the **Client IP address** of the VPN server or remote access system and the **Client Shared Secret**.

      If the **Client Shared Secret** field is left empty, the **Default Shared Secret** is used.

   3. (Optional) To mitigate the risk of a Blast-RADIUS attack, select the **RADIUS Security Enhancement** checkbox and then select either:

      * **Require Message-Authenticator**: RADIUS gateway requires this attribute in every client request, and also includes it as the first attribute in every RADIUS response.

      * **Limit Proxy-State**: RADIUS Gateway ignores requests that contain one or more Proxy-State attribute if they do not include the **Message-Authenticator** attribute. This option should only be used for legacy clients that don't support sending the **Message-Authenticator** attribute and are not acting as a proxy client.

        |   |                                                                                                                                                                                                                                                                                                                                                                  |
        | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Learn more about Blast RADIUS mitigations in the IETF article [Deprecating Insecure Practices in RADIUS](https://datatracker.ietf.org/doc/draft-ietf-radext-deprecating-radius/) and [RADIUS vulnerability CVE-2024-3596](https://support.pingidentity.com/s/article/RADIUS-Vulnerability-CVE-2024-3596) in the Ping Identity Knowledge Base (requires sign-on). |

9. Click **Save**.

   ### Result:

   The new gateway displays in the **Gateways** list. PingOne generates a gateway credential, which the gateway uses to authenticate with PingOne.

   |   |                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | A gateway credential is like a password, so keep it protected. For security reasons, PingOne does not store the generated gateway credentials, but you can always create a new one in the PingOne console. Multiple gateway instances can use the same gateway credential. |

10. Copy the credential and paste it to a secure location.

    You'll use the credential later when starting a gateway instance.

11. **Optional:** Click **Show me the Docker command** and copy it to a secure location.

12. Click **Done**.

## Next steps

[Start a gateway instance](p1_starting_gateway_instance_radius.html)

---

---
title: Adding a user type
description: A user type in PingOne identifies categories of users in the external directory.
component: pingone
page_id: pingone:integrations:p1_add_a_user_type
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_a_user_type.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 20, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding a user type

A user type identifies categories of users in the external directory. You must define a user type in the gateway to use external authentication as part of your authentication policy.

## About this task

You can bulk migrate users from an external directory and continue to have those PingOne users authenticate with the external directory as the password authority. In other words, password checks and password changes would still go through the external directory. See the **Select Password Authority** option in the following procedure.

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can pre-populate the fields with default values for the directory type you chose when you created the gateway. Click the **Use default values** button. |

## Steps

1. In the PingOne admin console, go to **Integrations > Gateways**.

2. Locate the appropriate gateway and then click the gateway name to expand the gateway details.

3. Click the **Lookup** tab.

4. Next to **User Types**, click the **[icon: plus, set=fa]**icon.

5. To use the default values based on the type of LDAP directory that you selected when you created the gateway, click the **Use default values** button.

6. Enter or edit the following:

   * **User Type**: Enter a name for the set of users you're trying to look up. This field is a label for the user type you're creating, and typically identifies the category of users you are trying to import, such as `Employees`.

   * **Select Password Authority**: Select **PingOne** or **LDAP** for authentication. If you choose **PingOne**, PingOne will authenticate with the external directory the first time and then authenticate with PingOne for all subsequent sign-ons. Click **Help me decide** for more information.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | * If you change the password authority from LDAP to PingOne for an existing user type, the user's password is migrated from the LDAP directory to PingOne the next time the user signs on.

     * If you change the password authority from PingOne to LDAP for an existing user type, the user's password is removed from PingOne. Going forward, PingOne sends credential validation requests to the LDAP directory through the LDAP gateway. |

   * **Push password changes to LDAP**: If you selected **PingOne** as the password authority, select this option to have PingOne update the LDAP directory with the new password if a user changes their password in PingOne.

   * **Enable password changes from PingOne**: If you selected LDAP as the password authority, select this option to allow users to change their password in PingOne. PingOne will update the LDAP directory with the new password.

     If you are running an Active Directory server, PingOne can change a user's password if the user's password expires or the **User must change password at next logon** option is selected. Enable this option to allow PingOne to change a user's password.

   * **User Search LDAP Base DN**: Specify a path to the directory for the users that you want to authenticate. The LDAP gateway searches the entire subtree.

   * **User Link Attributes**: Define the LDAP attributes that PingOne uses to link PingOne users with LDAP users when they sign on. For example, `dn` and `sAMAccountName`.

   You can define multiple attributes if all users don't have the same unique attributes populated in the LDAP directory. PingOne searches for each defined attribute individually as an "OR" query from top to bottom until the correlating user is found. If multiple users are found for one user attribute, then PingOne searches for the next defined attribute.

   * **Enable migration of new users upon first authentication**: Select this option to enable users without a PingOne user record to sign on based on the applicable authentication policy. When users sign on for the first time, PingOne creates user records based on the attribute mapping configuration.

   * **LDAP Filter**: Specify an LDAP filter to identify the users that should be migrated to the PingOne directory.

   * **Population**: When importing the identity to PingOne, add the identity to the specified population.

   * **Update PingOne user attributes as users sign on**: Select this option to update user attributes in PingOne when users sign on successfully through the LDAP gateway client and when attribute changes are detected based on the LDAP server response. If an update fails for at least one user attribute, no attributes will be updated, and authentication will fail. Successes and failures are recorded in the PingOne audit log.

     You can find a complete list of events logged in PingOne in [Audit Reporting Events](https://developer.pingidentity.com/pingone-api/platform/reference/audit-reporting-events.html) in the PingOne API documentation.

     |   |                                                                                                                                                             |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | * User attributes are not updated if the user authenticates with Kerberos.

     * This option is only available when **Password Authority** is set to **LDAP**. |

   * **Map Attributes**: Map LDAP user attributes to PingOne attributes. For example, you could map the `mail` attribute in the LDAP directory to the `Email` attribute in PingOne. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

7. Click **Save**.

---

---
title: Adding a vendor-specific identity provider in PingOne
description: Add a vendor-specific external identity provider in PingOne to allow users to sign on to your application using their existing credentials from third-party vendors.
component: pingone
page_id: pingone:integrations:p1_adding_vendor_specific_idps
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_adding_vendor_specific_idps.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 24, 2025
page_aliases: ["p1_enable_idp.adoc"]
---

# Adding a vendor-specific identity provider in PingOne

Add a vendor-specific external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* in PingOne to allow users to sign on to your applications using their existing credentials from services like Google, Apple, or LinkedIn. Adding an external IdP for a third-party vendor includes mapping PingOne user attributes to attributes from the IdP.

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | To enable or disable an IdP, click the toggle in the **External IdPs** list. |

---

---
title: Adding an Authorize gateway
description: Use an Authorize gateway to deploy authorization policy versions to gateway instances in your infrastructure and keep them up-to-date.
component: pingone
page_id: pingone:integrations:p1_add_authz_gateway
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_authz_gateway.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
  result: Result
  next-steps: Next steps
---

# Adding an Authorize gateway

Use an Authorize gateway to deploy authorization policy versions to gateway instances in your infrastructure and keep them up-to-date.

Adding an Authorize gateway creates the PingOne cloud component that manages communication with your gateway instances and generates the credential those instances use to authenticate with PingOne. After adding a gateway, you can copy the Docker command required to start gateway instances.

You can use separate Authorize gateways to represent your development, testing, and production environments.

## Steps

1. In the PingOne admin console, go to **Integrations > Gateways** and click the **[icon: plus, set=fa]**icon to add a gateway.

   ![A screen capture of the Add Gateway page with the name set to Dev Gateway, Authorize selected as the Gateway Type, and a Description entered.](_images/p1-az-gateway-add.png)

2. Enter the following:

   * **Name**: A name for the gateway. The name must be unique in this environment.

   * **Gateway Type**: Select **Authorize**.

   * **Description** (optional): A brief description of the gateway.

3. Click **Next**.

4. Select an **Authorization Version**.

   This is the policy and Trust Framework configuration that will be published to gateway instances and used to make authorization decisions. Each gateway instance associated with this Authorize gateway will use this authorization policy version.

   If you haven't set up policies and the Trust Framework yet, select **Bootstrap**.

   ![A screen capture of the Authorization Version page as part of the Add Gateway process, with the Boostrap version selected.](_images/p1-az-gateway-add-version.png)

5. Click **Save**.

   PingOne generates a gateway credential. The gateway instance in your organization's infrastructure uses this credential to authenticate with PingOne.

   |   |                                                                                                                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | A gateway credential is like a password, so keep it protected. For security reasons, PingOne does not store generated gateway credentials, but you can always create a new one in PingOne.Multiple gateway instances can use the same gateway credential, and the credential doesn't expire.To revoke a credential, click the **Delete** icon. |

6. Copy the credential and save it in a secure location for later use.

   You'll use the credential later to connect gateway instances to PingOne.

   ![A screen capture of the New Credential Created message showing the credential and the Docker command link.](_images/p1-az-gateway-credential.png)

7. Click **Show me the Docker command** and copy the command to a secure location.

   You'll use the Docker command later to start a gateway instance.

8. Click **Done**.

   Your new Authorize gateway displays an alert reminding you that no gateway instances are connected yet.

   ![A screen capture of an Authorize gateway showing an alert.](_images/p1-az-gateway-alert.png)

## Result

Explore the settings available for your new gateway:

* Header area: The toggle next to the gateway name allows you to enable or disable the gateway. Use the **More Options** (⋮) icon to edit gateway settings or delete the gateway.

* **Overview** tab: Allows you to add or delete gateway credentials. After you start a gateway instance, this tab also shows you the status and version of your gateway instances.

  ![A screen capture of the gateway Overview tab showing the gateway credential.](_images/p1-az-gateway-overview-tab.png)

* **Configuration** tab: Allows you to edit the policy and Trust Framework version deployed to gateway instances.

  ![A screen capture of the gateway Configuration tab showing the authorization policy version name and ID.](_images/p1-az-gateway-configuration-tab.png)

* **Download** tab: Provides instructions and a command for running the gateway as a Docker container.

  ![A screen capture of the gateway Download tab showing download instructions and the Docker command.](_images/p1-az-gateway-download-tab.png)

* **Roles** tab: Allows you to assign collections of permissions to the Authorize gateway by granting roles. Learn more in [Managing Authorize gateway roles](p1_manage_authz_gateway_roles.html).

  ![A screen capture of the gateway Roles tab showing the roles assigned to the gateway and the Grant Roles button.](_images/p1-az-gateway-roles-tab.png)

## Next steps

[Starting an Authorize gateway instance](p1_start_authz_gateway_instance.html).

---

---
title: Adding an identity provider - Amazon
description: Add Amazon as an external identity provider in PingOne to allow users to sign on with Amazon when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_amazon_overview
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_amazon_overview.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
page_aliases: ["p1_create_security_profile_amazon.adoc", "p1_enable_login_with_amazon.adoc", "p1_get_clientid_amazon.adoc", "p1_add_idp_amazon.adoc", "p1_add_callback_url_amazon.adoc"]
section_ids:
  before-you-begin: Before you begin
  creating-a-security-profile-with-amazon: Creating a security profile with Amazon
  before-you-begin-2: Before you begin
  steps: Steps
  enabling-login-with-amazon: Enabling Login with Amazon
  steps-2: Steps
  result: Result:
  getting-the-client-id-and-client-secret: Getting the client ID and client secret
  steps-3: Steps
  adding-amazon-as-an-identity-provider-in-pingone: Adding Amazon as an identity provider in PingOne
  before-you-begin-3: Before you begin
  steps-4: Steps
  adding-the-callback-url-to-the-amazon-developer-console: Adding the callback URL to the Amazon Developer Console
  steps-5: Steps
  next-steps: Next steps
---

# Adding an identity provider - Amazon

Adding Amazon as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with Amazon when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* An Amazon account.

## Creating a security profile with Amazon

Before you can set up Amazon as an external IdP, you must create a security profile for your application. Learn more in [Register for Login with Amazon](https://developer.amazon.com/docs/login-with-amazon/register-web.html).

### Before you begin

Ensure that you have the following information for your application:

* Name

* Description

* Privacy notice URL

* Logo (optional)

### Steps

1. Go to the [Amazon Developer Console](https://login.amazon.com) and sign on to your account.

   If you don't have an account you can create one now.

2. Click **Create a New Security Profile**.

3. Enter the following:

   * **Security Profile Name**: A unique identifier for the application, which will appear on the consent page when users agree to sign on with Amazon.

   * **Security Profile Description**: A brief description of the application.

   * **Privacy Notice URL**: The location of the privacy notice for your application.

   * **Consent Logo Image** (optional): The image that appears on the consent page to represent your application.

4. Click **Save**.

## Enabling Login with Amazon

If you created a new security profile, `Login with Amazon` should be enabled by default. If you are adding an application to an existing security profile, enable `Login with Amazon`.

### Steps

1. Go to the [Amazon Developer Console](https://developer.amazon.com/loginwithamazon/console/site/lwa/overview.html).

   ### Result:

   You are asked to sign on to the Developer Console.

2. Click **Select a security profile**, then choose your security profile in the menu.

3. Click **Confirm**.

4. In the form that opens, enter a **Consent Privacy Notice URL**.

   This is the location of your application's privacy policy.

5. Click **Save**.

## Getting the client ID and client secret

Copy the client ID and client secret from the Amazon Developer Console. You'll need these values when you add the application to PingOne.

### Steps

1. Go to the [Amazon Developer Console](https://login.amazon.com) and locate the appropriate security profile.

2. Click **Web Settings**.

3. Copy the **Client ID** and **Client secret** to a secure location.

   You can always access these values on the Amazon Developer Console.

## Adding Amazon as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

You should have the following information ready:

* Client ID

* Client secret

Ensure that registration is enabled in the authentication policy. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **Amazon**.

3. Click **Next**.

4. On the **Add External Identity Provider** page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the IdP.

     |   |                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on Button**, in accordance with the provider's brand standards. |

5. Click **Next**.

6. Configure the connection and enter the following information:

   * **Client ID**: The application ID that you copied earlier from the IdP. You can find this information on the [Amazon Developer Console](https://login.amazon.com).

   * **Client secret**: The application secret that you copied earlier from the IdP. You can find this information on the [Amazon Developer Console](https://login.amazon.com).

   * **Callback URL**: Copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

7. Click **Next**.

8. Define how the PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

       |   |                                                                                                           |
       | - | --------------------------------------------------------------------------------------------------------- |
       |   | You can map the following attributes provided by Amazon:- `email`

       - `name`

       - `user_id`

       - `postal_code` |

9. Click **Save**.

10. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Adding the callback URL to the Amazon Developer Console

Copy the callback URL from the PingOne admin console and paste it in the Amazon Developer Console.

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the appropriate IdP.

2. Click the IdP to open the details panel.

3. On the **Connection** tab, copy the **Callback URL** to a secure location.

4. Go to the [Amazon Developer Console](https://login.amazon.com).

5. Select the appropriate profile.

6. Go to the **Web Settings** section.

7. For **Allowed Return URLs**, paste the value that you copied from the the PingOne admin console.

8. Click **Save**.

### Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html).

---

---
title: Adding an identity provider - Apple
description: Add Apple as an external identity provider in PingOne to allow users to sign on with Apple when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_apple_prereqs
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_apple_prereqs.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
page_aliases: ["p1_create_app_id.adoc", "p1_create_services_id.adoc", "p1_create_private_key.adoc", "p1_configure_email_communication.adoc", "p1_add_idp_apple.adoc", "p1_add_return_url_to_apple.adoc"]
section_ids:
  before-you-begin: Before you begin
  apple_create_app_id: Creating an App ID
  steps: Steps
  apple_create_private_key: Creating a Services ID
  steps-2: Steps
  creating-a-private-key: Creating a private key
  steps-3: Steps
  configuring-email-communication: Configuring email communication
  steps-4: Steps
  adding-apple-as-an-identity-provider-in-pingone: Adding Apple as an identity provider in PingOne
  before-you-begin-2: Before you begin
  steps-5: Steps
  adding-the-return-url-to-the-apple-developers-site: Adding the return URL to the Apple Developers site
  steps-6: Steps
  next-steps: Next steps
---

# Adding an identity provider - Apple

Adding Apple as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with Apple when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* An Apple account.

## Creating an App ID

When you register your application, Apple generates an App ID to identify the application. You'll need this value to connect the application to PingOne.

### Steps

1. Go to the [Apple Developer site](https://developer.apple.com) and sign on to your Apple Developer account.

   If you don't have an Apple Developer account, you'll need to create one.

2. Click **Certificates, Identifiers & Profiles**.

3. On the left, click **Identifiers** and then click the **[icon: plus, set=fa]**icon.

4. In the **Register a New Identifier** section, select **App IDs**.

5. In the **Register an App ID** section, enter a value for the **Bundle ID**.

6. Copy the following values to a secure location:

   * **App ID prefix** (Team ID): Identifies your team or organization.

   * **Bundle ID**: Identifies a group of applications.

7. In the list of available capabilities, select **Sign in with Apple**.

8. Click **Continue and Register**.

## Creating a Services ID

The Services ID identifies the particular instance of your application. The Services ID is equivalent to a client ID in PingOne.

### Steps

1. On the [Apple Developer site](https://developer.apple.com), sign on to your Apple Developer account and then click **Certificates, Identifiers & Profiles**.

2. In the **Register a New Identifier** section, select **Services ID**.

3. Enter the following information:

   * **Description**: A brief description of the application.

   * **Identifier**: The path to the application. This value will be used as the client ID in PingOne.

4. Click **Continue and Register**.

5. In the list, select the service you just created.

6. Select **Sign in with Apple** and click **Configure**.

7. Select the primary App ID and click the **[icon: plus, set=fa]**icon.

8. Enter a value for **Domains and subdomains**.

   This is the top-level domain for your application.

9. Leave the **Return URLs** blank for now.

   This is the path in your application that users are redirected to after they have authenticated with Apple. This value is equivalent to a callback URI. You'll enter this value after you set up your application in PingOne.

10. Click **Next**, and then click **Done**.

11. Click **Continue**, and then click **Save**.

## Creating a private key

When you register your application, Apple generates a private key for client authentication. You'll need this value when you add the application to PingOne.

### Steps

1. On the Apple Developer site, click **Certificates, Identifiers & Profiles**.

2. On the left, click **Keys**.

3. To register a new key, click the **[icon: plus, set=fa]**icon.

4. Enter a value for **Key Name**.

5. Select **Sign in with Apple** and click **Configure**.

6. Select the primary App ID you created earlier.

7. Click **Save** and then click **Continue**.

8. Click **Register**.

9. Copy the **Key ID** to a secure location.

   You'll use this value when you add the IdP in PingOne.

10. To save the key to the local file system, click **Download**.

    The key is saved as a text file with a `.p8` file extension. The key will be used as the client secret signing key and its identifier will be used as the private key in PingOne.

    |   |                                                                                                                                                                                                                                                    |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | You can download the key only once. Save the file to a secure location because the key is not saved in your developer account, and you won't be able to download it again. If the **Download** button is disabled, you already downloaded the key. |

## Configuring email communication

Configuring Apple for email communication allows users to set up an account and sign on to applications with their existing Apple ID, which is required for PingOne to communicate with users and for users to receive updates from Apple. Learn more in [Configure private email relay service](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service/) in the Apple Developer documentation.

### Steps

1. On the Apple Developer site, click **Certificates, Identifiers & Profiles**.

2. On the left, click **More** and then click **Configure**.

3. Next to **Email Sources**, click the **[icon: plus, set=fa]**icon.

4. For **Domains and subdomains**, enter `pingidentity.com`.

5. Click **Next**.

6. Click **Register** and then click **Done**.

## Adding Apple as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

Ensure that registration is enabled in the authentication policy. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

You should have the following information ready:

* App ID (Client ID)

* Client secret signing key

* Team ID

* Private key ID

Learn more in [Creating an App ID](#apple_create_app_id) and [Creating a Services ID](#apple_create_private_key).

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **Apple**.

3. Click **Next**.

4. On the **Add External Identity Provider** page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the IdP.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on Button** in accordance with the provider's brand standards. |

5. Click **Next**.

6. Configure the connection and enter the following information:

   * **Service ID** (App ID): The application ID that you copied earlier from the IdP. You can find this information on the [Apple Developer site](https://developer.apple.com).

   * **Private key**: The application secret that you copied earlier from the IdP. You can find this information on the [Apple Developer site](https://developer.apple.com).

   * **Team ID**: A unique 10-character string generated by Apple that identifies your organization. The team ID is the prefix of the app ID.

   * **Private key ID**: Identifies the private key in the JSON Web Token (JWT). This JSON object is the client secret in PingOne.

   * **Callback URL**: Copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

7. Click **Next**.

8. Map the following PingOne attributes to Apple attributes:

   |                       |                                   |
   | --------------------- | --------------------------------- |
   | **PingOne attribute** | **Apple attribute**               |
   | Given Name            | providerAttributes.name.firstName |
   | Family Name           | providerAttributes.name.lastName  |

   |   |                                                                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Apple only sends an ID token with the first authentication using Sign in with Apple.Learn more about Sign in with Apple in [Authenticating users with Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/authenticating-users-with-sign-in-with-apple) in the Apple documentation. |

9. Map additional attributes as needed.

   Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can map additional attributes if they are in the ID token from Apple, such as `iss`, `iat`, `exp`, `aud`, `sub`, `nonce`, `nonce_supported`, `email`, and `email_verified`. Learn more about the JSON structure generated by Apple in [Configuring your webpage for Sign in with Apple](https://developer.apple.com/documentation/signinwithapple/configuring-your-webpage-for-sign-in-with-apple/) in the Apple documentation. |

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

10. Click **Save**.

11. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Adding the return URL to the Apple Developers site

Copy the callback URL from the PingOne admin console and paste it in the [Apple Developers site](https://developer.apple.com).

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the appropriate IdP.

2. Click the IdP to open the details panel.

3. Click the **Connection** tab.

4. Copy the callback URL to a secure location.

5. On the Apple Developer site, click **Certificates, Identifiers & Profiles**.

6. Select **Sign in with Apple** and click **Configure**.

7. Select the primary app ID and click the **[icon: plus, set=fa]**icon.

8. For **Return URLs**, paste the **Callback URL** value that you copied earlier.

9. Click **Next**, and then click **Done**.

### Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html).

---

---
title: Adding an identity provider - Facebook
description: Add Facebook as an external identity provider in PingOne to allow users to sign on with Facebook when accessing your application.
component: pingone
page_id: pingone:integrations:p1_addidentityproviderfacebook
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_addidentityproviderfacebook.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
page_aliases: ["p1_register_app_with_facebook.adoc", "p1_enable_facebook_login.adoc", "p1_add_idp_in_p1.adoc", "p1_add_callback_url.adoc"]
section_ids:
  before-you-begin: Before you begin
  registering-your-application-with-facebook-for-developers: Registering your application with Facebook for Developers
  steps: Steps
  result: Result:
  next-steps: Next steps
  enabling-facebook-login: Enabling Facebook login
  steps-2: Steps
  adding-facebook-as-an-identity-provider-in-pingone: Adding Facebook as an identity provider in PingOne
  before-you-begin-2: Before you begin
  steps-3: Steps
  adding-the-callback-url-to-facebook-for-developers: Adding the callback URL to Facebook for Developers
  steps-4: Steps
  next-steps-2: Next steps
---

# Adding an identity provider - Facebook

Adding Facebook as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with Facebook when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* A Facebook account.

## Registering your application with Facebook for Developers

Facebook generates an app ID and app secret for your application. You'll need these values to connect the application to PingOne.

### Steps

1. Sign on to your [Facebook Developer Account](https://developers.facebook.com).

   If you haven't created a Facebook Developer Account, you can do so now.

2. At the top of the page, click **My Apps** and then click **Create app**.

3. Select the appropriate application type and then click **Continue**.

4. Enter the following information:

   * **App Display name**: The name you want to associate with this application ID.

   * **App Contact email**: The primary contact information for the application.

5. Click **Create app**, and then complete the security check, if required.

   ### Result:

   The application dashboard is displayed.

6. On the left side of the page, go to **Settings** > **Basic** and enter the following information:

   * **App domains**: The path in your application that users are redirected to after they have authenticated with Facebook.

     Leave **App domains** blank for now.

   * **Privacy policy URL** (optional): The URL that contains your privacy policy.

   * **Terms of service URL** (optional): The URL that contains your terms of service.

7. At the top of the page, locate the **App ID** and **App secret** and copy their values to a secure location.

8. Click **Save changes**.

### Next steps

Learn more in [Meta App Development](https://developers.facebook.com/docs/apps).

## Enabling Facebook login

You must enable Facebook login for your application if it's not enabled already.

### Steps

1. Go to [Facebook for Developers](https://developers.facebook.com).

2. At the top of the page, click **My Apps**, and then select the appropriate app.

3. On the left side of the page, click **Products**

4. Locate the **Facebook login** card and click **Set up**.

5. Follow the instructions to set up Facebook login.

## Adding Facebook as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

Ensure that registration is enabled in the appropriate authentication policy. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

You should have the following information ready:

* App ID

* App secret

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **Facebook**.

3. Click **Next**.

4. On the **Add External Identity Provider** page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the IdP.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on button** in accordance with the provider's brand standards. |

5. Click **Next**.

6. Configure the connection and enter the following information:

   * **App ID**: The application ID that you copied earlier from the IdP. You can find this information on the **Basic settings** page in the [Facebook for Developers portal](https://developers.facebook.com).

   * **App Secret**: The application secret that you copied earlier from the IdP. You can find this information on the **Basic settings** page on the [Facebook for Developers portal](https://developers.facebook.com).

   * **Callback URL**: Copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

7. Click **Next**.

8. Define how the PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

9. Click **Save**.

10. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Adding the callback URL to Facebook for Developers

Copy the callback URL from the PingOne admin console and paste it in the Facebook for Developers login settings.

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the appropriate IdP.

2. Click the IdP to open the details panel.

3. On the **Connection** tab, copy the **Callback URL** to a secure location.

4. Go to [Facebook for Developers](https://developers.facebook.com).

5. At the top of the page, click **My Apps**, and then select the appropriate app.

6. Go to **Facebook Login > Settings**.

7. For **Valid OAuth Redirect URIs**, paste the value that you copied from the PingOne admin console.

### Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html).

---

---
title: Adding an identity provider - GitHub
description: Add Github as an external identity provider in PingOne to allow users to sign on with Github when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_github_overview
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_github_overview.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
page_aliases: ["p1_add_app_github.adoc", "p1_add_idp_github.adoc", "p1_finish_creating_app_github.adoc", "p1_finish_adding_idp_github.adoc"]
section_ids:
  before-you-begin: Before you begin
  creating-your-application-on-github: Creating your application on GitHub
  steps: Steps
  adding-github-as-an-identity-provider-in-pingone: Adding GitHub as an identity provider in PingOne
  before-you-begin-2: Before you begin
  steps-2: Steps
  finishing-creating-the-application-on-github: Finishing creating the application on GitHub
  before-you-begin-3: Before you begin
  steps-3: Steps
  finishing-adding-the-identity-provider-in-pingone: Finishing adding the identity provider in PingOne
  before-you-begin-4: Before you begin
  steps-4: Steps
  next-steps: Next steps
---

# Adding an identity provider - GitHub

Adding GitHub as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with GitHub when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* A GitHub account.

## Creating your application on GitHub

Before you can set up GitHub as an external IdP, you must create an application on GitHub. GitHub generates a client ID and client secret for the application. Learn more in [Creating an OAuth app](https://docs.github.com/en/developers/apps/creating-an-oauth-app) in the GitHub documentation.

### Steps

1. Go to [GitHub](https://github.com/) and sign on to your account.

   If you don't have a GitHub account, you can create one now.

2. In the upper right, click your profile photo, and then click **Settings**.

3. On the left, click **Developer Settings**.

4. On the left, click **OAuth Apps**.

5. Click the **New OAuth App** button.

   |   |                                                                                                |
   | - | ---------------------------------------------------------------------------------------------- |
   |   | If you haven't created an app before, you'll see the button as **Register a new application**. |

6. Enter the following:

   * **Application name**: The display name for the application.

   * **Homepage URL**: The full URL to your application home page.

   * **Application description**: A description for your application that all users will see.

   * **Authorization callback URL**: The path in your application that users are redirected to after they have authenticated with GitHub. Leave this value blank for now.

7. Leave the GitHub page open to return later and enter the `Authorization callback URL` after you have created the application in PingOne.

## Adding GitHub as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

Ensure that registration is enabled in the authentication policy you want to use. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **GitHub**.

3. Click **Next**.

4. On the **Add External Identity Provider** page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the IdP.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on Button** in accordance with the provider's brand standards. |

5. Click **Next**.

6. Copy the value for **Callback URL** to a secure location.

7. Leave the PingOne page open to return and enter the `Client ID` and `Client Secret` after you have created the application on GitHub.

## Finishing creating the application on GitHub

Add the callback URL from the PingOne admin console to your application on GitHub.

### Before you begin

Ensure you have copied the **Callback URL** from PingOne.

### Steps

1. Go to the **Register a new OAuth application** page on GitHub.

2. For **Authorization callback URL**, enter the value for **Callback URL** that you copied from PingOne.

3. Click **Register application**.

## Finishing adding the identity provider in PingOne

After you have registered the application with GitHub, copy the values for client ID and client secret and enter them into PingOne.

### Before you begin

Ensure that you have copied the values for client ID and client secret from GitHub.

### Steps

1. Return to [GitHub](https://github.com/) and, in the **OAuth Apps** section, select the appropriate application.

2. Locate the **Client ID** and **Client Secret** and copy the values to a secure location.

3. In the PingOne admin console, configure the connection and enter the following information:

   * **Client ID**: The application identifier that you copied from the IdP. You can find this information on GitHub.

   * **Client Secret**: The application secret that you copied from the IdP. You can find this information on GitHub.

   * **Callback URL**: The URL to which the user will be redirected after authenticating.

4. Click **Next**.

5. Define how the PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

       You can map the following attributes provided by GitHub:

   * `Avatar URL`

   * `Blog`

   * `Company`

   * `Email`

   * `HTML URL`

   * `User ID`

   * `Location`

   * `Login`

   * `Name`

   * `Node ID`

   * `Site Admin`

   * `Type`

   * `URL`

6. Click **Save**.

7. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

   |   |                                                                    |
   | - | ------------------------------------------------------------------ |
   |   | You can disable the IdP by clicking the toggle to the left (gray). |

### Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Add the authentication policy to your application](../applications/p1_auth_policies_for_applications.html).

---

---
title: Adding an identity provider - Google
description: Add Google as an external IdP in PingOne.
component: pingone
page_id: pingone:integrations:p1_addidentityprovidergoogle
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_addidentityprovidergoogle.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 30, 2025
page_aliases: ["p1_register_app_with_google.adoc", "p1_enable_google_people_api.adoc", "p1_add_idp_in_p1_g.adoc", "p1_add_callback_google.adoc"]
section_ids:
  before-you-begin: Before you begin
  registering-the-application-with-google: Registering the application with Google
  steps: Steps
  next-steps: Next steps
  enabling-the-google-people-api: Enabling the Google People API
  steps-2: Steps
  next-steps-2: Next steps
  adding-google-as-an-identity-provider-in-pingone: Adding Google as an identity provider in PingOne
  before-you-begin-2: Before you begin
  steps-3: Steps
  adding-the-callback-url-to-the-google-api-console: Adding the callback URL to the Google API Console
  steps-4: Steps
  next-steps-3: Next steps
---

# Adding an identity provider - Google

Adding Google as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with Google when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* A Google account.

## Registering the application with Google

When you register your application, Google generates an app ID and app secret for the application. You'll need these values to connect the application to PingOne.

### Steps

1. Go to the [Google API Console](https://console.developers.google.com).

   If you haven't created a Google account, you can do so now.

2. In the **Projects** list, select a project or create a new one.

3. On the left, click **Credentials**.

4. Click **Create credentials**, then select **OAuth client ID**.

   If you're prompted to configure an OAuth consent screen with information about your application, you can do that now.

5. Select the appropriate application type for your project and enter the following information:

   * **Name**: The name of the OAuth client ID, not the display name of the application.

   * **Authorized JavaScript origins**: The origin URI of the client application, for use with requests from a browser.

   * **Authorized redirect URIs**: The path in your application that users are redirected to after they authenticate with Google. Leave this value blank for now.

6. Click **Create**.

7. On the **OAuth client** page, copy the client ID and client secret to a secure location.

   You can always access the client ID and client secret from the **Credentials** page in the API Console.

### Next steps

Learn more in [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257?sjid=17163377939720277440-NC) in the Google Cloud Platform Console Help documentation.

## Enabling the Google People API

You must enable the Google People API if it's not enabled already.

### Steps

1. Go to the [Google API Console](https://console.developers.google.com).

2. In the **Projects** list, select a project or create a new one.

3. On the left, click **Library**.

4. Locate the **Google People API**.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | If you need help finding the API, use the search bar. |

5. Click **Enable**.

### Next steps

Learn more in [Enable and disable APIs](https://support.google.com/googleapi/answer/6158841) in the Google API Console Help documentation.

## Adding Google as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

Ensure that registration is enabled in the authentication policy. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

You should have the following information ready:

* Client ID

* Client secret

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **Google** for **Identity Provider Type** and click **Next**.

3. In the **Create Profile** step, enter the following:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: Select a population to enable just-in-time registration from the IdP. This overrides the registration population defined in the authentication policy.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on Button** in accordance with the provider's brand standards. |

4. Click **Next**.

5. In the **Configure Connection** step, enter the following:

   * **Client ID**: The client ID that you copied earlier from the IdP. You can find this information on the **Credentials** page in the [Google API Console](https://console.developers.google.com).

   * **Client Secret**: The client secret that you copied earlier from the IdP. You can find this information on the **Credentials** page in the [Google API Console](https://console.developers.google.com).

   * **Callback URL**: Click the **Copy** icon ([icon: copy, set=fa]) to copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

6. Click **Next**.

7. Map PingOne user attributes to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To use the advanced expression builder, click the **Gear** icon ([icon: gear, set=fa]). Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the **Update Condition**, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty Only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   The following attributes can be mapped from Google:

   | Attribute                       | Required scope                | Description                                                                                                                                        |
   | ------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Age Range**                   | `auth/profile.agerange.read`  | The age range of the user, such as `TWENTY_ONE_OR_OLDER`                                                                                           |
   | **Birthday Day**                | `auth/user.birthday.read`     | The user's birthday date                                                                                                                           |
   | **Birthday Month**              | `auth/user.birthday.read`     | The user's birthday month                                                                                                                          |
   | **Birthday Text**               | `auth/user.birthday.text`     | A free text string for the user's birthday&#xA;&#xA;This attribute is deprecated.                                                                  |
   | **Birthday Year**               | `auth/user.birthday.read`     | The user's birthday year                                                                                                                           |
   | **Display Name**                | `auth/userinfo.profile`       | The user's display name, such as their full name                                                                                                   |
   | **Email**                       | `auth/userinfo.email`         | The user's email address                                                                                                                           |
   | **ETag**                        | None                          | A unique identifier assigned by the server the last time the resource was changed                                                                  |
   | **Family Name**                 | `auth/userinfo.profile`       | The user's surname                                                                                                                                 |
   | **Gender**                      | `auth/user.gender.read`       | The user's gender                                                                                                                                  |
   | **Gender Formatted Value**      | `auth/user.gender.read`       | The user's gender formatted in the administrator's local language                                                                                  |
   | **Given Name**                  | `auth/userinfo.profile`       | The user's first name                                                                                                                              |
   | **Locale**                      | `auth/profile.language.read`  | The user's language                                                                                                                                |
   | **Middle Name**                 | `auth/userinfo.profile`       | The user's middle name                                                                                                                             |
   | **Nickname**                    | `auth/userinfo.profile`       | A user's nickname                                                                                                                                  |
   | **Nickname Type**               | `auth/userinfo.profile`       | The type of nickname, such as an alternate name the user is known by                                                                               |
   | **Phone Number**                | `auth/user.phonenumbers.read` | The user's phone number                                                                                                                            |
   | **Phone Number Canonical Form** | `auth/user.phonenumbers.read` | The user's phone number in the canonical [international standard E.164](https://www.itu.int/rec/T-REC-E.164/en) format with a maximum of 15 digits |
   | **Phone Number Formatted Type** | `auth/user.phonenumbers.read` | The user's phone number translated and formatted to the administrator's locale                                                                     |
   | **Phone Number Type**           | `auth/user.phonenumbers.read` | The type for the user's phone number, such as home, mobile, or work                                                                                |
   | **Photo URL**                   | `auth/userinfo.profile`       | The URL for the user's photo from their Google profile                                                                                             |
   | **Resource Name**               | None                          | An identifier for a specific entity type, such as `Person` or `ContactGroup`                                                                       |

   Learn more about the required scopes in the [Google People API reference](https://developers.google.com/people/api/rest/v1/people/get) and [OAuth 2.0 scopes](https://developers.google.com/identity/protocols/oauth2/scopes#people) in the Google API documentation.

8. Click **Save**.

9. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

   |   |                                                                    |
   | - | ------------------------------------------------------------------ |
   |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Adding the callback URL to the Google API Console

After copying the callback URL from PingOne, you'll paste it in the Google API Console.

### Steps

1. Go to the [Google API Console](https://console.developers.google.com).

2. In the **Projects** list, select the appropriate project.

3. Click **Credentials**.

4. In the **Application** list, click the appropriate application.

5. In the **Authorized redirect URIs** section, click **Add URI** and paste the callback URL that you copied from PingOne.

## Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html).

---

---
title: Adding an identity provider - LinkedIn
description: Add LinkedIn as an external identity provider in PingOne to allow users to sign on with LinkedIn when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_linkedin_prereqs
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_linkedin_prereqs.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
section_ids:
  before-you-begin: Before you begin
  registering-the-application-with-linkedin: Registering the application with LinkedIn
  steps: Steps
  learn-more: Learn more
  adding-linkedin-as-an-identity-provider-in-pingone: Adding LinkedIn as an identity provider in PingOne
  before-you-begin-2: Before you begin
  steps-2: Steps
  adding-the-callback-url-to-the-linkedin-developer-page: Adding the callback URL to the LinkedIn Developer page
  steps-3: Steps
  next-steps: Next steps
---

# Adding an identity provider - LinkedIn

Adding LinkedIn as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* allows your users to sign on with LinkedIn when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* A LinkedIn account.

## Registering the application with LinkedIn

LinkedIn generates a client ID and client secret for your application. You'll need these values to connect the application to PingOne.

### Steps

1. Go to the [LinkedIn Developers page](https://developer.linkedin.com).

2. Click **Create app**.

   You'll be prompted to sign on to your LinkedIn account.

3. Enter the following information:

   * **App name**: A unique name for the application. It must be fewer than 50 characters.

   * **LinkedIn Page**: The LinkedIn company page to be associated with your application.

   * **App logo**: The logo users see when they authenticate to your application.

4. Click **Create app**.

5. On the **Product** tab, locate **Sign In with LinkedIn using OpenID Connect** in the list of products and click **Request access**.

6. On the **Auth** tab, copy the **Client ID** and **Primary Client Secret** to a secure location.

7. In the **OAuth 2.0 Settings** section, you'll see an empty field for **Redirect URLs**, which is the path in your application that users are redirected to after they have authenticated with LinkedIn. Leave this value blank for now.

### Learn more

Learn more in [Sign in with LinkedIn using OpenID Connect](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2) in the Microsoft LinkedIn documentation.

## Adding LinkedIn as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

Ensure that registration is enabled in the authentication policy. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

You should have the following information ready:

* Client ID

* Client secret

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **LinkedIn**.

3. Click **Next**.

4. On the **Add External Identity Provider **page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the identity provider.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on button** in accordance with the provider's brand standards. |

5. Click **Next**.

6. Configure the connection and enter the following information:

   * **Client ID**: The client ID that you copied earlier from the IdP. You can find this information on the **Auth** page on the [LinkedIn Developers page](https://developer.linkedin.com).

   * **Client secret**: The application secret that you copied earlier from the IdP. You can find this information on the **Auth** tab on the [LinkedIn Developers page](https://developer.linkedin.com).

   * **Callback URL**: Copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

7. Click **Next**.

8. Define how the PingOne user attributes are mapped to identity provider attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

9. Click **Save**.

10. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Adding the callback URL to the LinkedIn Developer page

Copy the callback URL from the PingOne admin console and paste it into the LinkedIn Developers page.

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the appropriate IdP.

2. Click the IdP to open the details panel.

3. Click the **Connection** tab.

4. Copy the **Callback URL** to a secure location.

5. Go to the [LinkedIn Developers page](https://developer.linkedin.com).

6. In the **My Apps** list, select the appropriate application.

7. On the **Auth** tab, click the **Pencil** icon in the **OAuth 2.0 settings** section.

8. Click **[icon: plus, set=fa]Add redirect URL**.

9. Paste the callback URL that you copied from the PingOne admin console.

10. Click **Update**.

## Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html).

---

---
title: Adding an identity provider - LinkedIn (legacy)
description: Add LinkedIn as an external identity provider in PingOne to allow users to sign on with LinkedIn when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_linkedin_prereqs_legacy
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_linkedin_prereqs_legacy.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
section_ids:
  before-you-begin: Before you begin
  registering-the-application-with-linkedin: Registering the application with LinkedIn
  steps: Steps
  learn-more: Learn more
  adding-linkedin-as-an-identity-provider-in-pingone: Adding LinkedIn as an identity provider in PingOne
  before-you-begin-2: Before you begin
  steps-2: Steps
  adding-the-callback-url-to-the-linkedin-developer-page: Adding the callback URL to the LinkedIn Developer page
  steps-3: Steps
  next-steps: Next steps
---

# Adding an identity provider - LinkedIn (legacy)

Adding LinkedIn as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* allows your users to sign on with LinkedIn when accessing your application.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The legacy LinkedIn IdP has been deprecated, so you might be unable to connect with LinkedIn using a legacy connection. Consider using the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)*-based LinkedIn IdP connection. Learn more in [Adding an identity provider - LinkedIn](p1_add_idp_linkedin_prereqs.html). |

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* A LinkedIn account.

## Registering the application with LinkedIn

LinkedIn generates a client ID and client secret for your application. You'll need these values to connect the application to PingOne.

### Steps

1. Go to the [LinkedIn Developers page](https://developer.linkedin.com).

2. Click **Create app**.

   You'll be prompted to sign on to your LinkedIn account.

3. Enter the following information:

   * **App name**: A unique name for the application. It must be fewer than 50 characters.

   * **LinkedIn Page**: The LinkedIn company page to be associated with your application.

   * **App logo**: The logo users see when they authenticate to your application.

4. Click **Create app**.

5. On the **Auth** tab, copy the **Client ID** and **Primary Client Secret** to a secure location.

6. In the **OAuth 2.0 Settings** section, you'll see an empty field for **Redirect URLs**, which is the path in your application that users are redirected to after they have authenticated with LinkedIn. Leave this value blank for now.

### Learn more

Learn more in [Sign in with LinkedIn](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin) in the Microsoft LinkedIn documentation.

## Adding LinkedIn as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

Ensure that registration is enabled in the authentication policy. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

You should have the following information ready:

* Client ID

* Client secret

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **LinkedIn (Legacy)**.

3. Click **Next**.

4. On the **Add External Identity Provider **page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the identity provider.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on button** in accordance with the provider's brand standards. |

5. Click **Next**.

6. Configure the connection and enter the following information:

   * **Client ID**: The client ID that you copied earlier from the IdP. You can find this information on the **Auth** page on the [LinkedIn Developers page](https://developer.linkedin.com).

   * **Client secret**: The application secret that you copied earlier from the IdP. You can find this information on the **Auth** tab on the [LinkedIn Developers page](https://developer.linkedin.com).

   * **Callback URL**: Copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

7. Click **Next**.

8. Define how the PingOne user attributes are mapped to identity provider attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

9. Click **Save**.

10. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Adding the callback URL to the LinkedIn Developer page

Copy the callback URL from the PingOne admin console and paste it into the LinkedIn Developers page.

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the appropriate IdP.

2. Click the IdP to open the details panel.

3. Click the **Connection** tab.

4. Copy the **Callback URL** to a secure location.

5. Go to the [LinkedIn Developers page](https://developer.linkedin.com).

6. In the **My Apps** list, select the appropriate application.

7. On the **Auth** tab, click the **Pencil** icon in the **OAuth 2.0 settings** section.

8. Click **[icon: plus, set=fa]Add redirect URL**.

9. Paste the callback URL that you copied from the PingOne admin console.

10. Click **Update**.

## Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html).

---

---
title: Adding an identity provider - Microsoft
description: Add Microsoft as an external identity provider in PingOne to allow users to sign on with Microsoft when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_microsoft
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_microsoft.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2025
---

# Adding an identity provider - Microsoft

Adding Microsoft as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with their Microsoft accounts when accessing your application. Learn more in [OIDC authentication](p1_add_idp_microsoft_oidc.html).

To connect PingOne as the external authentication provider for multi-factor authentication (MFA) in Microsoft Entra ID, you'll need to add a Microsoft identity provider. Learn more in [Entra ID external MFA](p1_add_idp_microsoft_entra.html).

---

---
title: Adding an identity provider - OIDC
description: Use the generic OIDC configuration to add an external identity provider in PingOne that follows the OIDC standard.
component: pingone
page_id: pingone:integrations:p1_add_idp_oidc
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_oidc.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2025
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Adding an identity provider - OIDC

You can use the generic OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* configuration to add any external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* that follows the OIDC standard.

## Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. In the **Select Identity Provider Type** step, click **OpenID Connect** and click **Next**.

3. In the **Create Profile** step, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: Select a population in the list that overrides the authentication policy's registration population and enables just-in-time (JIT) registration from the IdP.

   * **Sign-on Button** (optional): An image to use for the login button displayed to the end user. Use a 300 x 42 pixel image.

   * **Icon** (optional): An image to represent the IdP. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format. Use a 90 x 90 pixel image.

4. Click **Next**.

5. In the **Configure Connection** step:

   1. Enter the **Connection Details**:

      * **Client ID**: The application ID generated by the external IdP to which you're connecting.

      * **Client Secret**: The application secret generated by the external IdP to which you're connecting.

      * **Callback URL**: Copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

   2. Enter the **Discovery Details**:

      * **Discovery Document URI** (optional): The discovery endpoint from the external IdP. Enter the URL and then click **Use Discovery Document** to populate the remaining settings in **Discovery Details** automatically. Learn more in [Discovery document URI](p1_discovery_document_uri.html).

      * **Issuer**: The issuer to which the authentication is sent for the external IdP. This URL must use the `https` protocol.

      * **JWKS Endpoint**: The URL that specifies the JSON Web Key Set (JWKS) endpoint for the external IdP. The JWKS endpoint includes public keys that can be used to verify JSON Web Keys (JWKs) from the IdP. This URL must use the `https` protocol.

      * **Authorization Endpoint**: The URL that specifies the authorization endpoint for the external IdP. PingOne requests an authorization grant from the authorization endpoint. This URL must use the `https` protocol.

      * **Token Endpoint**: The URL that specifies the token endpoint for the external IdP. PingOne presents its authorization grant to the token endpoint to obtain an access token and a refresh token when needed. This URL must use the `https` protocol.

      * **User Information Endpoint** (optional): The URL that specifies the `userInfo` endpoint for the external IdP. When defined for the IdP, PingOne always sends a request to the `userInfo` endpoint to retrieve additional information about the user after successful authentication. This URL must use the `https` protocol.

        To obtain claims about the authenticated user:

        1. PingOne sends a token request to the IdP.

        2. The IdP returns a token response to PingOne containing an access token and ID token.

        3. PingOne then presents the access token returned in the IdP token response to the `userInfo` endpoint to retrieve user attributes, profile information, preferences, and other user-specific information, such as `name`, `email`, and `sub`.

        4. The external IdP returns a JSON object containing user claims. PingOne can only receive claims in the `userInfo` endpoint that correspond to scopes configured in the **Requested Scopes** field.

        5. Before applying any attribute mappings, PingOne merges the ID token claims with any results from the `userInfo` endpoint.

           If the same claim exists in both places, such as both containing the `email` attribute, PingOne gives precedence to the ID token claim over the `userInfo` endpoint response.

        6. PingOne then applies any defined attribute mappings.

      * **Token Endpoint Authentication Method**: The authentication method to use for authenticating the external IdP. Select **None**, **Client Secret Basic**, or **Client Secret Post**.

      * **Requested Scopes**: The scopes to include in the authentication request to the `userInfo` endpoint for the external IdP to return specific data. Scope values are case sensitive. You can provide multiple scopes by separating them with a space.

      * **Proof Key for Code Exchange (PKCE)**: Select the **Enable** checkbox to use PKCE to secure communication with the IdP and help prevent authorization code interception attacks.

        This option is selected by default if **Discovery Document URI** is configured and if the metadata from the provider includes the following:

        ```
        "code_challenge_methods_supported": [
        "plain",
        "S256"
        ]
        ```

        If **Discovery Document URI** isn't configured or if the `code_challenge_methods_supported` metadata from the provider doesn't include `S256`, this option is cleared by default.

        Learn more about PKCE in [RFC7636: Proof Key for Code Exchange by OAuth Public Clients](https://tools.ietf.org/html/rfc7636) on the Internet Engineering Task Force (IETF) website.

   3. Click **Next**.

6. In the **Map Attributes** step, define how the PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon ([icon: gear, set=fa]). Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP:

     * **Empty Only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

7. Click **Save**.

8. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

   |   |                                                                    |
   | - | ------------------------------------------------------------------ |
   |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Next steps

[Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

---

---
title: Adding an identity provider - PayPal
description: Add PayPal as an external identity provider in PingOne to allow users to sign on with PayPal when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_paypal
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_paypal.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
page_aliases: ["p1_register_app_paypal.adoc", "p1_configure_scopes_paypal.adoc", "p1_add_the_idp_p1.adoc", "p1_register_return_url_paypal.adoc"]
section_ids:
  before-you-begin: Before you begin
  registering-your-application-with-paypal: Registering your application with PayPal
  before-you-begin-2: Before you begin
  steps: Steps
  configuring-scopes-and-options: Configuring scopes and options
  steps-2: Steps
  adding-paypal-as-an-identity-provider-in-pingone: Adding PayPal as an identity provider in PingOne
  steps-3: Steps
  registering-the-callback-url-with-paypal: Registering the callback URL with PayPal
  before-you-begin-3: Before you begin
  steps-4: Steps
  next-steps: Next steps
---

# Adding an identity provider - PayPal

Adding PayPal as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with PayPal when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* A Paypal account

## Registering your application with PayPal

Create your application with PayPal, and then copy the client ID and client secret.

### Before you begin

Ensure that you have a PayPal account with an active subscription.

### Steps

1. Go to [PayPal for Developers](https://developer.paypal.com) and sign on to your account.

   If you don't have a PayPal account, you can create one now.

2. In the **My apps and credentials** section, click **Sandbox**.

3. In the **Rest API apps** section, click **Create app**.

4. In the **Application details** field, enter a name for the application, and then click **Create app**.

5. In the **Sandbox API credentials** section, copy the **Client ID** to a secure location.

6. In the **Secret** section, click **Show**.

7. Copy the client secret to a secure location.

8. In the **App feature options** section, select **Connect with PayPal**.

   You can clear the other options, unless your organization has a specific need for them.

9. Click **Save**.

## Configuring scopes and options

On the PayPal for Developers site, configure the options for scope attributes, permissions, and customer consent.

### Steps

1. Go to [PayPal for Developers](https://developer.paypal.com).

2. In the **Rest API apps** section, click your application name.

3. In the **Connect with PayPal** section, click **Advanced options**.

4. Select the following scope attributes:

   * `Full name`

   * `Email`

   * `Street address`

   * `City`

   * `State`

   * `Country`

   * `Postal code`

   * `Account verification status`

   * `PayPal account ID`

5. Under **Links shown on customer consent page**, enter the following:

   * **Privacy policy URL**: (Optional). The location of your organization's privacy policy.

   * **User agreement URL**: (Optional). The location of your organization's user agreement.

6. In the **Additional PayPal permissions** section, select **Enable customers who have not yet confirmed their email with PayPal to log in to your app**.

7. Click **Save**.

## Adding PayPal as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **PayPal**.

3. Click **Next**.

4. On the **Add External Identity Provider** page, enter the following information:

   * **Name**: A unique identifier for the IdP

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the IdP.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on Button** in accordance with the provider's brand standards. |

5. Click **Next**.

6. Configure the connection and enter the following information:

   * **Client ID**: The application ID from the IdP that you copied earlier. You can find this information on the [PayPal for Developers site](https://developer.paypal.com).

   * **Client secret**: The application secret from the IdP that you copied earlier. You can find this information on the [PayPal for Developers site](https://developer.paypal.com).

   * **Environment**: The environment the configuration connects to. Click **live** or **sandbox**

   * **Callback URL**: Copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

7. Click **Next**.

8. Define how the PingOne user attributes are mapped to identity provider attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

9. Click **Save**.

10. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Registering the callback URL with PayPal

Copy the callback URL value from the PingOne admin console and enter it into the PayPal for Developers site.

### Before you begin

Ensure that you have the callback URL from the PingOne admin console.

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the appropriate IdP.

2. Click the IdP to open the details panel.

3. Click the **Connection** tab.

4. Copy the **Callback URL** and paste it in a secure location.

5. Go to [PayPal for Developers](https://developer.paypal.com).

6. In the **Rest API apps** section, click your application name.

7. In the **Sandbox app settings** section, locate **Return URL**.

8. Click **Show**.

9. For **Return URL**, enter the callback URL value that you copied from the PingOne admin console.

10. Click **Save**.

### Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html) and ensure that registration is enabled in the authentication policy.

---

---
title: Adding an identity provider - SAML
description: Use the generic SAML configuration in PingOne to add an external identity provider that follows the SAML standard.
component: pingone
page_id: pingone:integrations:p1_add_identity_provider_saml
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_identity_provider_saml.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 2, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# Adding an identity provider - SAML

You can use the generic SAML configuration to add an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* that follows the SAML standard.

## Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **SAML**.

3. Click **Next**.

4. On the **Create Profile** page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the IdP.

   * **Sign-on Button** (optional): An image used for the sign-on button that the end user sees. Use a 300 x 42 pixel image.

   * **Icon** (optional): An image that represents the IdP. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

5. Click **Next**.

6. On the **Configure PingOne Connection** page, enter the following:

   * **PingOne (SP) Entity ID**: The entity ID for the service provider (SP), which is used as the `Issuer` when PingOne sends a request to the external IdP. The IdP can also use this value to ensure that requests from the SP are valid. By default, this ID is based on the value you entered for **Name**.

   * **ACS Endpoint**: Shows the Assertion Consumer Service (ACS) URL. The ACS endpoint is where the single sign-on (SSO) *(tooltip: \<div class="paragraph">
     \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
     \</div>)* tokens are sent. Copy this value and enter it into the IdP configuration.

   * **Signing Certificate**: The certificate confirming that SAML authentication requests and single logout (SLO) messages came from PingOne as the SP. Select the appropriate certificate in the list of available RSA or EC certificates. Learn more about adding a certificate in [Adding a certificate](../settings/p1_addcertificate.html).

   * **Signing Algorithm**: Select the algorithm to use for signing metadata.

     If you selected an RSA signing certificate, the options are:

     * **RSA\_SHA256**

     * **RSA\_SHA384**

     * **RSA\_SHA512**

     If you selected an EC signing certificate, the options are:

     * **SHA256\_ECDSA**

     * **SHA384\_ECDSA**

     * **SHA512\_ECDSA**

   * **Enable Signed Authentication Request**: Specifies whether the SAML authentication request will be signed when sending it to the IdP. Select this option if the external IdP is included in an authentication policy used by applications that are accessed by a combination of default URLs and custom domains URLs.

7. Click **Next**.

8. On the **Configure IDP Connection** page, specify the details of the connection between the IdP and PingOne.

   You can enter values manually or import them from a file.

   ### Choose from:

   * **Import Metadata**: Click **Select a file** and then select an XML metadata file on your file system. Click **Open**.

     |   |                                                                                                                   |
     | - | ----------------------------------------------------------------------------------------------------------------- |
     |   | If the metadata file doesn't specify all of the configuration values, you must enter the missing values manually. |

   * **Import from URL**: Enter the **Idp Metadata URL** and then click **Import**.

     |   |                                       |
     | - | ------------------------------------- |
     |   | The URL must be a valid absolute URL. |

   * **Manually Enter**:

     * **SSO Endpoint**: The SSO endpoint for the authentication request. Only authentication requests can be sent to the SSO endpoint.

     * **IDP Entity ID**: The IdP's entity ID.

     * **SSO Binding**: The binding to use for the authentication request. Select **HTTP Post** or **HTTP Redirect**.

     * **SLO Endpoint**: The URL of the SLO service. PingOne redirects the browser to this location when it needs to send an SLO message to the SP. Learn more in [SAML 2.0 single logout](p1_saml_slo_externalidp.html).

     * **SLO Response Endpoint**: The URL of the SLO. You can use this option if you have a separate service for SLO responses. If this value is blank, PingOne sends responses to the SLO endpoint.

     * **SLO Binding**: The SAML binding used by the application. The default is `HTTP POST`. Select `HTTP Redirect` as needed.

     * **SLO Window (in hours)**: Specify how long PingOne can exchange logout messages with the IdP, specifically a `LogoutRequest` from the IdP, after the initial request. PingOne can also send a `LogoutRequest` to the IdP when SLO is initiated by the user from other session participants, such as an application or another IdP. This setting is per IdP. The SLO logout is separate from the user session logout that revokes all tokens. The minimum value is 1 hour, and the maximum is 24 hours. You should start with a value of 2 hours and then fine-tune as needed.

     * **Verification Certificate**: A certificate that confirms that the SAML assertions came from the external IdP. Select one of the following:

       * **[icon: plus, set=fa]Import**: Upload the appropriate certificate from your local files.

       * **[icon: plus, set=fa]Add**: Select a certificate in the list of available certificates. You can view certificates in **Settings > Certificates and Key Pairs**. Learn more in [Adding a certificate](../settings/p1_addcertificate.html).

9. Click **Next**.

10. Define how PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

    * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

    * To add an attribute, click **[icon: plus, set=fa]Add**.

    * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

    * Select the update condition, which determines how PingOne updates its user directory with values from the IdP. The options are:

      * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

      * **Always**: Always update the PingOne directory attribute.

11. Click **Save**.

12. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Next steps

[Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

---

---
title: Adding an identity provider - X
description: Add X as an external identity provider in PingOne to allow users to sign on with X when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_x_prereqs
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_x_prereqs.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 29, 2025
page_aliases: ["p1_add_idp_twitter_prereqs.adoc", "p1_register_app_x.adoc", "p1_enable_email_x.adoc", "p1_get_api_key_x.adoc", "p1_add_idp_x.adoc", "p1_add_callback_url_x.adoc"]
section_ids:
  before-you-begin: Before you begin
  registering-the-application-with-x: Registering the application with X
  steps: Steps
  enabling-email-communication: Enabling email communication
  steps-2: Steps
  getting-the-api-key-and-api-secret: Getting the API key and API secret
  steps-3: Steps
  adding-x-as-an-identity-provider-in-pingone: Adding X as an identity provider in PingOne
  before-you-begin-2: Before you begin
  steps-4: Steps
  adding-the-callback-url-to-the-x-developer-site: Adding the callback URL to the X Developer site
  steps-5: Steps
  next-steps: Next steps
---

# Adding an identity provider - X

Adding X as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with X when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* An X account

## Registering the application with X

To enable signing on with X, you must register your application with X.

### Steps

1. Go to the [X Developer site](http://developer.x.com) and sign on to your account.

   If you haven't created an X Developer account, you can do so now.

2. Click **Create an app**.

3. Enter the appropriate information.

4. Select **Enable sign in with X**.

5. Click **Create**.

## Enabling email communication

Enable email communication to retrieve a user's email address from X.

### Steps

1. Go to the [X Developer site](http://developer.x.com).

2. Select your application.

3. Click **Edit**, then click **Edit details**.

4. On the **Permissions** tab, click **Edit**.

5. Enable the **Request email addresses from users** option.

6. Click **Save**.

## Getting the API key and API secret

When you register your application, X generates an API key to identify the application.

### Steps

1. Go to the [X Developer site](http://developer.x.com).

2. Select your application.

3. On the **Keys and tokens** tab, copy the following values to a secure location:

   * **API key**: The consumer key that identifies the application.

   * **API secret key**: The consumer secret that secures the application.

## Adding X as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

Ensure that registration is enabled in the authentication policy. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

You should have the following information ready:

* API key

* API secret key

Learn more in [Adding an identity provider - X](p1_add_idp_x_prereqs.html).

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **X**.

3. Click **Next**.

4. On the **Add External Identity Provider** page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the IdP.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on Button** in accordance with the provider's brand standards. |

5. Click **Next**.

6. Configure the connection and enter the following information:

   * **API key**: The consumer key that you copied earlier from the IdP. You can find this information on the [X Developer site](http://developer.x.com).

   * **API secret key**: The consumer secret that you copied earlier from the IdP. You can find this information on the [X Developer site](http://developer.x.com).

   * **Callback URL**: Copy the **Callback URL** to a secure location. You'll provide this value to the IdP later.

7. Click **Next**.

8. Define how the PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

9. Click **Save**.

10. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

## Adding the callback URL to the X Developer site

Copy the callback URL from the PingOne admin console and paste it in the X Developer site.

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and browse or search for the appropriate IdP.

2. Click the IdP to open the details panel.

3. On the **Connection** tab, copy the **Callback URL** to a secure location.

4. On the [X Developer site](https://developer.x.com/), select your application.

5. On the **App details** tab, for **Callback URL**, paste the value that you copied earlier.

6. Click **Save**.

### Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html).

---

---
title: Adding an identity provider - Yahoo
description: Add Yahoo as an external identity provider in PingOne to allow users to sign on with Yahoo when accessing your application.
component: pingone
page_id: pingone:integrations:p1_add_idp_yahoo_prereqs
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_idp_yahoo_prereqs.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2025
page_aliases: ["p1_create_app_yahoo.adoc", "p1_add_idp_yahoo.adoc", "p1_finish_app_yahoo.adoc", "p1_finish_adding_idp_yahoo.adoc"]
section_ids:
  before-you-begin: Before you begin
  creating-the-application-with-yahoo: Creating the application with Yahoo
  steps: Steps
  adding-yahoo-as-an-identity-provider-in-pingone: Adding Yahoo as an identity provider in PingOne
  before-you-begin-2: Before you begin
  steps-2: Steps
  finishing-creating-the-application-with-yahoo: Finishing creating the application with Yahoo
  before-you-begin-3: Before you begin
  steps-3: Steps
  finishing-adding-the-identity-provider-in-pingone: Finishing adding the identity provider in PingOne
  steps-4: Steps
  next-steps: Next steps
---

# Adding an identity provider - Yahoo

Adding Yahoo as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* gives your users the option to sign on with Yahoo when accessing your application.

## Before you begin

Ensure that you have:

* A PingOne organization with an environment added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Added your application to PingOne. Learn more in [Adding an application](../applications/p1_applications_add_applications.html).

* A Yahoo account

## Creating the application with Yahoo

To enable signing on with Yahoo, create the application on the Yahoo Developers page. Yahoo generates a client ID and client secret to identify the application. Learn more in [Getting Started](https://developer.yahoo.com/oauth2/guide/openid_connect/getting_started.html) in the OpenID Connect section of the Yahoo Developer site.

### Steps

1. Go to the [Yahoo Developer site](http://developer.yahoo.com/apps) and sign on to your account.

   If you haven't created a Yahoo Developer account, you can do so now.

2. Click the **Create an App** button.

3. Enter a name for the application.

4. For **Application type**, select **Web application**.

5. Leave **Redirect URI** blank for now.

   You will get this value from PingOne and enter it later.

6. In the **API Permissions** section, select **OpenID Connect Permissions**, and then select **Email** and **Profile**.

7. Leave the page open so you can return later to enter the **Redirect URI**.

## Adding Yahoo as an identity provider in PingOne

Configure the IdP connection in PingOne.

### Before you begin

Ensure that registration is enabled in the authentication policy. Learn more in [Editing an authentication policy](../authentication/p1_edit_auth_policy.html).

### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click **[icon: plus, set=fa]**.

2. Click **Yahoo**.

3. Click **Next**.

4. On the **Add External Identity Provider** page, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: A population that overrides the authentication policy's registration population and enables just-in-time registration from the IdP.

     |   |                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on Button** in accordance with the provider's brand standards. |

5. Click **Next**.

6. Copy the value for **Callback URL** to a secure location.

7. Leave the page open so you can return later to enter the values for **Client ID** and **Client secret**.

## Finishing creating the application with Yahoo

Add the callback URL from the PingOne admin console to your Yahoo application.

### Before you begin

Ensure you have the callback URL from the PingOne admin console that you copied in [Adding an identity provider - Yahoo](p1_add_idp_yahoo_prereqs.html).

### Steps

1. Go to the [Yahoo Developers page](http://developer.yahoo.com/apps).

2. For **Callback URL**, enter the value that you copied from the PingOne admin console on the **Configure Connection** page.

3. Click **Create App**.

## Finishing adding the identity provider in PingOne

After you have created the application with Yahoo, copy the values for client ID and client secret and enter them into PingOne.

### Steps

1. Go to the [Yahoo Developers page](http://developer.yahoo.com/apps).

2. Copy the values for **Client ID** and **Client Secret** to a secure location.

3. In the PingOne admin console, finish configuring the Yahoo connection and enter the following information:

   * **Client ID**: The application ID that you copied from the IdP. You can find this information on the Yahoo Developers site.

   * **Client Secret**: The application secret that you copied from the IdP. You can find this information on the Yahoo Developers site.

   * **Callback URL**: The URL to which the user will be redirected after authenticating.

4. Click **Next**.

5. Define how the PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Enter the PingOne user profile attribute and the external IdP attribute. Learn more about attribute syntax in [Identity provider attributes](p1_idp_attributes.html).

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon. Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

       You can map the following attributes provided by Yahoo:

       * `sub`

       * `name`

       * `given_name`

       * `family_name`

       * `email`

       * `picture`

       * `nickname`

       * `locale`

6. Click **Save**.

7. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

   |   |                                                                    |
   | - | ------------------------------------------------------------------ |
   |   | You can disable the IdP by clicking the toggle to the left (gray). |

### Next steps

* [Add the IdP to your authentication policy](../authentication/p1_edit_auth_policy.html).

* [Apply the authentication policy to your application](../applications/p1_apply_auth_policy_to_applications.html).

---

---
title: Adding an LDAP gateway
description: An LDAP gateway connection allows PingOne to communicate with the LDAP directory.
component: pingone
page_id: pingone:integrations:p1_add_ldap_gateway
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_ldap_gateway.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Adding an LDAP gateway

An Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* gateway connection allows PingOne to communicate with the LDAP directory.

## About this task

|   |                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For gateway provisioning, PingOne supports only Active Directory or PingDirectory user stores. Learn more in [Provisioning](p1_provisioning.html).To avoid connectivity issues when adding an LDAP gateway, you shouldn't use a load balancer hostname or IP address. |

## Steps

1. In the PingOne admin console, go to **Integrations → Gateways**.

2. Click the **[icon: plus, set=fa]**icon.

3. Enter the following:

   * **Name**: A name for the gateway. The name must be unique within the environment.

   * (Optional) **Description**: A brief characterization of the gateway.

   * **Gateway Type**: Click **LDAP**.

4. Click **Next**.

5. Enter connection information:

   * **LDAP Directory Type**: Specify the type of directory that the gateway connects to. PingOne supports any LDAP v3-compliant directory server.

     |   |                                                                                                                                                                          |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | If you select **Microsoft Active Directory**, you'll have the option to use Kerberos for authentication. See [Kerberos authentication](p1_kerberos_authentication.html). |

   * **LDAP Host Name**: Specify the IP address or hostname for the external directory server. Click **[icon: plus, set=fa]Add LDAP Host** to configure multiple servers for failover. PingOne tries to connect to the servers in the order they're listed. If the first server is unavailable, then PingOne tries to connect to the next server in the list.

   * **Port**: Specify the port that the external directory is located on. For standard LDAP connections, the default port is 389. For connections with Transport Layer Security (TLS) security, the default port is 636.

   * **Follow LDAP Referrals**: Determines whether the LDAP Gateway client follows referrals it receives from LDAP servers.

   * **Connection Security**: Select **TLS**, **StartTLS,** or **None** to configure the security options for the connection. **TLS** is the default selection and is recommended for better security.

   * **Allow TLS connections with untrusted certificates**: Allow certificates that are signed by a certificate authority (CA) that isn't well-known or trusted. A certificate could be untrusted if the certificate is expired, the hostname doesn't match what's specified in the certificate, or a certificate is self-signed.

   * **Bind DN**: Specify the service account credential used to access the external directory. You can query the directory to get this value.

   * **Bind Password**: Specify the password for the selected `Bind DN`.

     |   |                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------- |
     |   | The following options appear only if you selected **Microsoft Active Directory** for **Directory type**. |

   * **Enable Kerberos Authentication**: Determines whether to use Kerberos for authentication.

   * **Service Account User Principal Name**: The Kerberos service account configured as the Service Principal Name (SPN). The value must be in User Principal Name (UPN) format and is case sensitive. Learn more in [Creating SPNs](p1_creating_spns.html) and in [UPN format](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/plan-connect-userprincipalname#upn-format) in the Active Directory documentation.

     |   |                                                                                                                                                                                                                                                                                                                      |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | For additional protection, we recommend adding MFA to the associated authentication policy. Learn more in [Creating an authentication policy that uses the gateway](p1_create_auth_policy_using_the_gateway.html) and [Adding a multi-factor authentication or PingID step](../authentication/p1_add_mfa_step.html). |

   * **Service Account Password**: The password for the Kerberos service account.

   * **Retain Previous Credentials**: Determines whether PingOne remembers credentials that were previously used to authenticate. If you change the Kerberos service account credentials, PingOne saves the previous five service account credentials. This allows Kerberos requests issued with previous service account credentials to be validated for the specified amount of time. Learn more in [Retaining credentials](p1_retaining_credentials.html).

   * **Retention Duration (Minutes)**: Specifies how long to keep the previous credentials, in minutes. The default value is 610.

6. Click **Save**.

   ### Result:

   PingOne generates a gateway credential, which the gateway uses to authenticate with PingOne.

   |   |                                                                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | A gateway credential is like a password, so keep it protected. For security reasons, PingOne doesn't store the generated gateway credentials, but you can always create a new one in the PingOne console. Multiple gateway instances can use the same gateway credential. |

7. Copy the credential and paste it to a secure location.

   You'll use the credential later when creating a gateway instance.

8. (Optional) Click **Show me the Docker command** and copy it to a secure location.

9. Click **Done**.

---

---
title: Adding the authentication policy to an application
description: Associate a gateway-based authentication policy with an application in PingOne to enforce LDAP user migration on sign-on.
component: pingone
page_id: pingone:integrations:p1_add_the_auth_policy_to_an_application
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_the_auth_policy_to_an_application.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2024
section_ids:
  steps: Steps
---

# Adding the authentication policy to an application

Associate the authentication policy with an application so that users accessing the application will use the specified authentication policy. For more information, see [Authentication policies for applications](../applications/p1_auth_policies_for_applications.html).

## Steps

1. Go to **Applications → Applications**.

2. Locate the application you want to edit by browsing or searching for it.

3. Click the application entry to open the **Details** panel.

4. Click the **Policies** tab, and then click the **Pencil** icon.

5. Select the check box for the authentication policy that you want to apply for the application.

   The policies are applied in the order in which they appear in the list. PingOne evaluates the first policy in the list first. If the requirements of the policy are not met, PingOne moves to the next policy in the list.

6. Click **Save**.

7. (Optional) To verify that your policy migrates LDAP users upon authentication, sign on to the application as a user that matches the user type you selected when you [created an authentication policy that uses the gateway](p1_create_auth_policy_using_the_gateway.html).

---

---
title: Adding the LDAP gateway service
description: Download and install the PingOne LDAP gateway bundle as a Windows service on the computer that will run the gateway.
component: pingone
page_id: pingone:integrations:p1_add_gateway_windows_service
canonical_url: https://docs.pingidentity.com/pingone/integrations/p1_add_gateway_windows_service.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 22, 2024
section_ids:
  steps: Steps
  result: Result:
---

# Adding the LDAP gateway service

Download the `.zip` archive and extract it to the computer that will run the gateway.

## Steps

1. In the PingOne admin console, go to **Integrations > Gateways** and locate the appropriate gateway.

2. Click the gateway name to expand the gateway details.

3. Click the **Download** tab.

4. In the **Standalone** section, review the prerequisites and instructions.

5. In the **Instructions** section, click the download link for the gateway bundle.

   |   |                                            |
   | - | ------------------------------------------ |
   |   | If prompted, complete the sign-on process. |

   ### Result:

   The download begins.

6. Extract the `.zip` archive to the computer that will run the gateway.

   We recommend that you use a common location as the parent directory, such as `C:\Program Files\Ping Identity`.

7. Follow the instructions in the `README.txt` file to:

   1. Configure the `run.properties` file, including providing the gateway credential information.

      The `run.properties` file is located in the `config` directory. For example, `C:\Program Files\Ping Identity\pingone-ldap-gateway-2.3.0\config`.

   2. (Optional) To configure an LDAP Gateway client application to use a forward web proxy server to handle traffic between the gateway and PingOne, in the `run.properties` file provide the relevant access information.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * To add the web proxy details after installing the LDAP gateway client application as a Windows service, update the `run.properties` file, and then run the `bin/windows/reinstall-service.bat` file using an account with administrator privileges.

      * You must also configure the web proxy settings locally per each running instance. For example, if you're running two gateway client applications, you must configure web proxy settings in both instances.

      * Digest authentication does not support international characters.

      * Basic authentication requires configuration in the proxy server to support international characters. |

8. Sign on to Windows with administrator privileges.

9. Start a command prompt or PowerShell.

10. Run the `install-service.bat` file without any parameters.

    By design, the `install-service.bat` file does not start the service automatically after completion. However, the service is configured to start automatically at the next and subsequent restarts of the Windows operating system.

11. In the Services system application, start the PingOne LDAP Gateway service.

12. Go to **Integrations > Gateways** to verify that the gateway can connect to PingOne. Learn more in [Verifying a gateway instance](p1_verifying_gateway_instance_ldap.html).