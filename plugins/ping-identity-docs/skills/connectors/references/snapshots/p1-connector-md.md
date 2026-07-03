---
title: PingOne Connector
description: Use the PingOne DaVinci connector to add PingOne functionality for your DaVinci flow.
component: connectors
page_id: connectors::p1_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2025
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-pingone: Setting up PingOne
  setting-up-your-pingone-environment: Setting up your PingOne environment
  choosing-a-pingone-worker-app: Choosing a PingOne worker app
  assigning-roles-to-the-application: Assigning Roles to the application
  getting-your-application-credentials: Getting your application credentials
  getting-your-environment-details: Getting your environment details
  setting-up-the-pingone-connector-configuration: Setting up the PingOne connector configuration
  connector-configuration: Connector configuration
  environment-id: Environment ID
  client-id: Client ID
  client-secret: Client secret
  region: Region
  using-the-connector-in-a-flow: Using the connector in a flow
  authenticating-users-and-resetting-passwords: Authenticating users and resetting passwords
  registering-users-and-setting-up-mfa: Registering users and setting up MFA
  authenticating-users-with-protect-and-mfa: Authenticating users with Protect and MFA
  registering-users-with-agreements-and-verifying-email: Registering users with agreements and verifying email
  registering-users-and-verifying-email: Registering users and verifying email
  managing-group-memberships: Managing group memberships
  managing-user-groups: Managing user groups
  migrating-users-from-an-external-directory-to-pingone: Migrating users from an external directory to PingOne
  authenticating-users-through-kerberos: Authenticating users through Kerberos
  using-an-alternative-identifier: Using an alternative identifier
  updating-users-through-gateway: Updating users through gateway
  sending-account-creation-notifications: Sending account creation notifications
  sending-verification-code-notification: Sending verification code notifications
  sending-password-recovery-notifications: Sending password recovery notifications
  sending-password-change-notifications: Sending password change notifications
  capabilities: Capabilities
  userLookup: Find User
  usersLookup: Find Multiple Users
  checkPassword: Check Password
  createUser: Create User
  readUser: Read User
  updateUser: Update User
  deleteUser: Delete User
  enableUser: Update User Status
  sendVerificationCode: Send Email Verification Code
  verifyEmail: Validate Verification Code
  sendRecoveryCode: Send Password Recovery Code
  recoverPassword: Validate Password Recovery Code
  resetPassword: Change Password
  setPassword: Set Password
  createAccountLink: Create Account Link
  readAccountLinks: Read Account Links
  deleteAccountLink: Delete Account Link
  checkUserAgreement: Check User Agreement
  readUserAgreements: Read User Agreements
  revokeUserAgreement: Revoke User Agreement
  acceptAgreement: Accept User Agreement
  readAgreementContent: Read Agreement Content
  readPopulation: Read Population
  readUserGroupMemberships: Read User Group Memberships
  createUserGroupMembership: Create User Group Membership
  deleteUserGroupMembership: Delete User Group Membership
  migrateUserGateway: Migrate User through Gateway
  createGroup: Create Group
  readGroup: Read Group
  updateGroup: Update Group
  deleteGroup: Delete Group
  readGroupMembers: Read Group Members
  kerberosAuthentication: Authenticate User via Kerberos
  singleFactorSignOn: Single-Factor Sign On
  unlockUser: Unlock User
  updateUserGateway: Update User through Gateway
  readTheme: Read Theme
  limitations: Limitations
  livesync-operations: LiveSync operations
  troubleshooting: Troubleshooting
  username-is-immutable-and-cannot-be-updated-error: "\"Username is immutable and cannot be updated\" error"
---

# PingOne Connector

Use the PingOne DaVinci connector to add PingOne functionality for your DaVinci flow.

The PingOne connector has capabilities that you can tie together to achieve your desired outcome. The connector acts like a worker application with each capability calling one or more endpoints in PingOne using your application for authentication.

You can use the PingOne connector to:

* Create a sign-on flow for authentication.

* Reset a user's password.

* Register new users in the PingOne user store.

* Unlock a locked user account.

* Create, edit, and delete users in the PingOne user store.

* Verify a user's email address.

* View a user's population.

* Manage a user's group memberships.

* Manage user groups.

* View agreements and consents for a user.

* Migrate users from an LDAP datastore to PingOne.

* Authenticate users through Kerberos.

* Send users an email for successful account creation.

* Send users verification code notifications.

## Setup

### Resources

You can find information in, the following sections of the PingOne documentation:

* PingOne:

  * [Introduction to PingOne](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html)

  * [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html)

  * [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A PingOne license ([Try PingOne for free](https://www.pingidentity.com/en/try-ping.html))

* A PingOne environment with a configured Worker app

### Setting up PingOne

#### Setting up your PingOne environment

Learn more in [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html).

#### Choosing a PingOne worker app

Most environments include a preconfigured worker app that you can use with DaVinci connectors.

To add a worker app:

1. Decide whether to connect to the host PingOne tenant or a different PingOne tenant.

2. In the PingOne admin console, go to **Applications > Applications**.

3. Select the preconfigured **PingOne DaVinci Connection** worker app.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A small number of older environments might not have the preconfigured worker app. If that applies to your environment, you can:- Reuse a worker app you've already created.

- Create a new worker app.

  > **Collapse: Details**
  >
  > To create a new worker app for this connector:
  >
  > 1. Sign on to PingOne.
  >
  > 2. Create a worker app as described in the [PingOne documentation](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).
  >
  > 3. Make sure you set the authentication method as `Client secret basic`.
  >
  >    The PingOne connector receives a token using your application's credentials.
  >
  > 4. Assign the following roles to the worker app:
  >
  >    * **Identity Data Admin**
  >
  >    * **Environment Admin**
  >
  > 5. Note the **Client ID**, **Client Secret**, and **Environment ID** for the worker app.
  >
  > 6. Click **Finish**.
  >
  > 7. Go to **Applications > Applications**, click the application to open the application details, and click the toggle switch in the upper right to enable the application. |

#### Assigning Roles to the application

To use the appropriate capabilities, the Worker app used by the connector needs the **Environment Admin** and **Identity Data Admin** roles.

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The user that creates the Worker app must have the **Environment Admin** and **Identity Data Admin** roles to assign the roles to a Worker app. |

1. In the PingOne admin console, go to **Applications > Applications**.

   Learn more about [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation.

2. Locate the application you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app) and click it to open the details panel.

3. Click the **Roles** tab and then click the **Pencil** icon to edit the roles.

4. Review the assigned roles to ensure that they include **Environment Admin** and **Identity Data Admin** roles. If not, click **[icon: plus, set=fa]Add role** to assign them.

#### Getting your application credentials

Get the **Client ID** and **Client secret** from the PingOne admin console before setting up the PingOne connector in DaVinci.

1. In your PingOne environment, go to **Applications > Applications**.

   Learn more about [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation.

2. Locate the application you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app) and click it to open the details panel.

3. On the **Configuration** tab, expand **General** and locate the **Client ID** and **Client secret**. Copy these values to a secure location.

#### Getting your environment details

Get your **Environment ID** and **Region** before setting up the PingOne connector in DaVinci.

1. In your PingOne environment, go to **Settings > Environment Properties**.

2. Locate the **Environment ID** and **Region**. Copy these values to a secure location.

### Setting up the PingOne connector configuration

In DaVinci, add a PingOne connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html) in the DaVinci documentation.

#### Connector configuration

##### Environment ID

The unique identifier for the appropriate PingOne environment. Learn more about finding the environment ID in [Environment properties](https://docs.pingidentity.com/pingone/settings/p1_environments.html) in the PingOne documentation.

##### Client ID

The unique public identifier for the PingOne application you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). Learn more about finding the client ID in [Viewing application details](https://docs.pingidentity.com/pingone/applications/p1_viewapplications.html) in the PingOne documentation.

##### Client secret

The cryptographic secret that is known only to the application and the authorization server. Use the client secret of the application you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). Learn more about finding the client secret in [Viewing a client secret](https://docs.pingidentity.com/pingone/applications/p1_view_client_secret_application.html) in the PingOne documentation.

##### Region

The geographic region that hosts your PingOne tenant. Learn more about finding the region in [Environment properties](https://docs.pingidentity.com/pingone/settings/p1_environments.html) in the PingOne documentation.

## Using the connector in a flow

You can use sample flows as a starting point or create your own flows to satisfy your requirements. The following section shows some popular sample flows. Open the [Ping Identity Marketplace](https://marketplace.pingone.com/home) for a full list.

### Authenticating users and resetting passwords

Use this flow to create authentication flows that include the ability for users to reset or recover their passwords.

Search for **PingOne - Sign On and Password Reset** in the [Ping Identity Marketplace](https://marketplace.pingone.com/home)

Learn more in [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) in the DaVinci documentation.

### Registering users and setting up MFA

Use this flow to create registration flows with optional user enrollment to MFA.

Search for **PingOne - Register with verify email and MFA enrollment** in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

Learn more in [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) in the DaVinci documentation.

### Authenticating users with Protect and MFA

Use this flow to create sign-on flows that include a password check and a conditional step-up to second-factor authentication using the [PingOne Protect Connector](p1_protect_connector.html).

Search for **PingOne - Sign On and Adaptive MFA** in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

Learn more in [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) in the DaVinci documentation.

### Registering users with agreements and verifying email

Use this flow to create registration flows that include email address verification and agreement consent.

Search for **PingOne - Register with Agreements and Verify Email** in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

Learn more in [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) in the DaVinci documentation.

### Registering users and verifying email

Use this flow to create registration flows that include email address verification.

Search for **PingOne - Register with Verify Email** in the [Ping Identity Marketplace](https://marketplace.pingone.com/home).

Learn more in [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) in the DaVinci documentation.

### Managing group memberships

The connector has several capabilities that allow you to manage the groups that a user belongs to in PingOne:

* **Read User Group Membership**

* **Create User Group Membership**

* **Delete User Group Membership**

No special flow configuration is needed. Add the capability that you want and populate its properties according to the help text.

### Managing user groups

The connector has several capabilities that allow you to manage groups.

* **Create Group**

  * Create a new user group in PingOne and optionally set the metadata on the group. Only the **Group Name** is required.

    |   |                                                                                                                                         |
    | - | --------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Updating a group's metadata using the **Update Group** capability on a DaVinci flow overwrites any existing metadata on PingOne Groups. |

* **Read Group**

  * Read a user group. Only the **Group ID** is required.

* **Update Group**

  * Update an existing user group with the supplied information and optionally update a group's metadata. The **Group ID** is required to verify the group exists and the **Group Name** is required only when updating a group.

* **Delete Group**

  * Delete a specified group. Only the **Group ID** is required.

* **Read Group Members**

  * Read up to 100 users within a group. The list is filterable by match attributes and an identifier. Only the **Group ID** is required.

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

### Migrating users from an external directory to PingOne

The connector allows you to use your existing authentication flow to migrate users to the PingOne user store from an external directory.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about setting up a directory as a gateway in PingOne in [Gateways](https://docs.pingidentity.com/pingone/integrations/p1_gateways.html) in the PingOne documentation. |

In your authentication flow, add the PingOne connector with the **Migrate User Through Gateway** capability. This capability validates the user's credentials against the directory for authentication, then migrates the user account to PingOne.

The **Gateway User Type List** property allows you to filter by specific gateways and user types.

Unlike the **Authenticate User via Kerberos** capability, the **Migrate User Through Gateway** capability supports only user types with user migration, with the **Enable migration of new users upon first authentication** option enabled.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're building a flow to support LDAP authentication for users provisioned from Microsoft Active Directory into PingOne through an [LDAP gateway provisioning connection](https://docs.pingidentity.com/pingone/integrations/p1_create_provisioning_connection_gateway.html) and an [inbound rule](https://docs.pingidentity.com/pingone/integrations/p1_create_inbound_provisioning_rule_gateway.html), use the **Check Password** capability. |

### Authenticating users through Kerberos

Use the **Authenticate User via Kerberos** capability to seamlessly authenticate users whose user records reside in an on-premise Microsoft Active Directory.

|   |                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When adding this node to your flow, you must select at least one LDAP gateway and a user type.The PingOne admin console only shows LDAP gateways when the **LDAP Directory Type** is set to **Microsoft Active Directory**, the **Enable Kerberos Authentication** option is activated, and the service account credentials are provided. |

An authentication is considered `successful` if PingOne is able to validate the Kerberos ticket and find the user under the **User Search LDAP Base DN** as defined in the selected user type.

For user types:

* If users span multiple base DNs, such as `OU=employees,DC=example,DC=com` and `OU=contractors,DC=example,DC=com`, create two user types (one for each base DN) and add them to the node.

* If none of the selected user types are configured to migrate users upon their first authentication, the **Create PingOne User** toggle isn't applicable and not shown.

* If at least one of the selected user types is configured to migrate users upon their first authentication, the **Create PingOne User toggle** is shown and enabled.

  * When enabled, a PingOne user account is created using attributes from Active Directory (only if the user type used to find the user is configured to migrate users upon their first authentication).

  * Disable this option to support a legacy integration where DaVinci is configured as an external IdP in PingOne.

The [example flow](https://marketplace.pingone.com/item/pingone-kerberos-authentication) uses the `PingOne` node to authenticate the user through Kerberos and evaluates as follows:

* `Successful`: The `PingOne Authentication` node returns a success response.

* `Failure`: The `Username/Password Form` node asks for the user's username and password and the flow continues to the `Button Pressed` node. The user has the options to press:

  * Submit: The user submits login and the flow continues to the `Sign In` node, the `User Lookup` node, and `PingOne node` in which a user migrates through a gateway and lastly continues on to the `Check Password` node.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | If you are building a flow to support Kerberos authentication for users provisioned from Microsoft Active Directory into PingOne through an [LDAP gateway provisioning connection](https://docs.pingidentity.com/pingone/integrations/p1_create_provisioning_connection_gateway.html) and an [inbound rule](https://docs.pingidentity.com/pingone/integrations/p1_create_inbound_provisioning_rule_gateway.html), remove the `PingOne` node that migrates users and link the `False` branch of the `User Lookup` node to the `Invalid Username/Password` node.The `User Lookup` node should always return `True` unless provisioning fails to create the user record in PingOne, in which case you should review the provisioning audit events in **Event types** > **Provisioning** in the PingOne admin console. |

  * Forgot Password: Flow continues to `Forgot Password` node.

  * No match: Flow continues to the `An Unexpected Error` node which displays a custom error message.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Learn more about setting up Active Directory as a gateway in PingOne in the following:- [LDAP Gateways](https://docs.pingidentity.com/pingone/integrations/p1_ldap_gateways.html)

    - [Creating SPNs](https://docs.pingidentity.com/pingone/integrations/p1_creating_spns.html)

    - [Configuring end user browsers](https://docs.pingidentity.com/pingone/integrations/p1_configuring_end_user_browsers.html)

    - [Adding a Gateway](https://docs.pingidentity.com/pingone/integrations/p1_add_ldap_gateway.html)Learn more about using the connector in a flow in [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) in the DaVinci documentation. |

### Using an alternative identifier

An alternative identifier is a domain, ID, or custom value used to identify a population.

The following example shows a population with a domain alternative identifier used with the **Read Population** capability.

```
{
"id": "42fc7d8f-db37-4a42-8eb8-6664e7f62f79",
"environment": {
"id": "<env_id>"
},
"name": "Sample Population with an Alternative Identifier",
"userCount": 256,
"createdAt": "2024-10-17T19:16:09.272Z",
"updatedAt": "2024-11-17T15:23:33.272Z",
"alternativeIdentifiers": [
"pingidentity.com",
"another_alt_identifier"
],
"default": false
}
```

The following images show setting the alternative identifier value directly in the field and having the value pulled from a prior node's form value.

![alternative identifier field](_images/connector-images/dvc-p1-alt-id-url.png)![alternative identifier node value](_images/connector-images/dvc-p1-alt-id-variable.png)

### Updating users through gateway

Use this capability to retrieve a user's attributes through a PingOne gateway and update the PingOne user profile with them.

In the **PingOne Attribute** list, select the attribute that you want to match against the provided identifier to find a user. The default is **User ID**.

In the **Identifier** field, enter the user ID, username, or email address of the user that you want to find.

![A screen capture of the user through gateway configuration.](_images/connector-images/dvc-p1-sso-update-user-through-gateway-config.png)

The variable you enter in **Identifier** points to an outcome attribute from an earlier node, where the user is successfully authenticated, and the user and user identifier are known.

You can also use the **Authenticate User via Kerberos** capability, followed by the **Update User through Gateway** capability to have PingOne authenticate users using the Kerberos protocol and then update PingOne user attributes with attribute values from the on-premises Microsoft Active Directory (AD).

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **Update User through Gateway** capability configuration doesn't include which LDAP Gateway and user type to select to find a user, as the PingOne user's record contains the LDAP Gateway and user type. |

### Sending account creation notifications

You can use the **Create User** capability to create a user in PingOne and send an account creation notification email to that user. Notification templates are configured in the PingOne admin console in **User Experience > Notification Templates**.

To send an account creation notification:

1. Branch from a node that presents a user-facing form to collect user information to a PingOne node with the **Create User** capability.

2. In the **Create User** node, select **ACCOUNT\_OK** in the **Lifecycle status** field.

   |   |                                                                                                                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For the **ACCOUNT\_OK** option, user verification isn't required, and the user will be notified of successful account creation.For the **VERIFICATION\_REQUIRED** option, the account will be created when the user is verified. Learn more in the [Sending verification code notifications](#sending-verification-code-notification). |

3. Select a template from PingOne that will notify the user when their account is created. If you don't select a template, the user won't be notified.

4. You can also configure the following additional fields to customize the notification email:

   * **Notification Name**: Select the specific template configured in PingOne to use for the email notification.

   * **Notification Locale**: Localize the notification text for any of the languages enabled in PingOne for the chosen locale.

   * **Notification Variables**: Pass variables to personalize the template text. For example, you can pull a `username` variable to address in the email.

Learn more in [Notification templates](https://docs.pingidentity.com/pingone/user_experience/p1_notifications.html) in the PingOne documentation.

### Sending verification code notifications

You can use the **Create User** capability to send a verification code notification. Notification templates are configured in the PingOne admin console in **User Experience > Notification Templates**.

To send a verification code notification:

1. Branch from a node that presents a user-facing form to collect user information to a PingOne node with the **Create User** capability.

2. In the **Create User** node, select **VERIFICATION\_REQUIRED** in the **Lifecycle status** field.

3. Configure the following additional fields that display to customize the user-facing notification:

   * **Notification Name**: Select the specific template configured in PingOne to use for the email notification.

     |   |                                                                                                           |
     | - | --------------------------------------------------------------------------------------------------------- |
     |   | If you don't select an option here, the default notification template configured in PingOne will be used. |

   * **Notification Locale**: Localize the notification text for any of the languages enabled in PingOne for the chosen locale.

   * **Notification Variables**: Pass variables to personalize the template text. For example, you can pull a `username` variable to address in the email.

Learn more in [Notification templates](https://docs.pingidentity.com/pingone/user_experience/p1_notifications.html) in the PingOne documentation.

### Sending password recovery notifications

You can use the **Password Recovery - DaVinci** capability to ensure that users receive a recovery code via e-mail when they need to reset their password. Notification templates are configured in the PingOne admin console in **User Experience > Notification Templates**.

To send a password recovery notification:

1. Branch from a node that presents a user-facing form to a PingOne node with the **Send Password Recovery Code** capability.

2. Configure the following fields that display to customize the user-facing notification:

   * **Notification Name**: Select the specific template configured in PingOne to use for the notification.

     |   |                                                                                                           |
     | - | --------------------------------------------------------------------------------------------------------- |
     |   | If you don't select an option here, the default notification template configured in PingOne will be used. |

   * **Notification Locale**: Localize the notification text for any of the languages enabled in PingOne for the chosen locale.

   * **Notification Variables**: Pass variables to personalize the template text. For example, you can pull a `username` variable to address in the email.

Learn more in [Notification Templates](https://docs.pingidentity.com/pingone/user_experience/p1_notifications.html) in the PingOne documentation.

### Sending password change notifications

You can use the **Change Password** capability to notify the end user by email when their password changes. This capability uses notification templates that are created under **Password Change (End User) - DaVinci** in PingOne.

The **Set Password** capability uses notification templates created under **Password Change (Admin) - DaVinci** in PingOne. Use this capability when an administrator changes or resets a user's password. Configure notification templates in the PingOne console in **User Experience > Notification Templates**.

Learn more in [Notification Templates](https://docs.pingidentity.com/pingone/user_experience/p1_notifications.html).

To send a password change notification:

1. Branch from a node that presents a user-facing form to a PingOne node with the **Password Change - DaVinci** capability.

2. Configure the following additional fields that display to customize the user-facing notification:

   * **Notification Name**: Select the specific template configured in PingOne to use for the notification.

     |   |                                                                                                           |
     | - | --------------------------------------------------------------------------------------------------------- |
     |   | If you don't select an option here, the default notification template configured in PingOne will be used. |

   * **Notification Locale**: Localize the notification text for any of the languages enabled in PingOne for the chosen locale.

   * **Notification Variables**: Pass variables to personalize the template text. For example, you can pull a `username` variable to address in the email.

## Capabilities

### Find User

Find a user by identifier.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Custom SCIM Filter toggleSwitch
>   - SCIM Filter textField
>   - PingOne Attributes textFieldArrayView
>
>   Enter the PingOne attributes you want to use to find a user, such as username, userID, or email.
>
> - Identifier textField
>
>   Enter the identifier, which was captured earlier in the flow, that you want to use to find a user. For example, if the attributes specified are email and username, and the identifier is username, the system will search for users whose email or username match the value captured under username.
>
> - Return User Password Status toggleSwitch
>
>   The output will include a property named 'passwordStatus' which correlates to the user's password state status in PingOne.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttributes array uniqueItems: true
>
>     * userIdentifierForFindUser string
>
>       User attribute to match attributes.
>
>     * returnUserPasswordStatus boolean
>
>     * scimFilter string
>
>       SCIM filter to match users.
>
> - output object
>
>   * matchedUser object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * passwordStatus string
>
>   * userFilter string
>
>   * userCount integer
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "matchedUsers": {
>       "_embedded": {
>         "users": [
>           {
>             "environment": {
>               "id": "5007e871-f0e7-4fc9-9ab9-b23b3ae76069"
>             },
>             "id": "f442f27a-6d9c-4280-891f-bed26a9bd9ce",
>             "username": "johndoe"
>           }
>         ]
>       }
>     },
>     "passwordState": {
>       "status": "OK"
>     }
>   },
>   "responseStatus": 200,
>   "headers": {
>     "XPing": "X-Ping"
>   },
>   "passwordStatus": "OK|PASSWORD_EXPIRED|MUST_CHANGE_PASSWORD|NO_PASSWORD|PASSWORD_LOCKED_OUT|UNKNOWN",
>   "matchedUser": {
>     "environment": {
>       "id": "5007e871-f0e7-4fc9-9ab9-b23b3ae76069"
>     },
>     "id": "f442f27a-6d9c-4280-891f-bed26a9bd9ce",
>     "username": "johndoe"
>   }
> }
> ```

### Find Multiple Users

Find a set of users by an identifier.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Custom SCIM Filter toggleSwitch
>   - SCIM Filter textField
>   - PingOne Attributes textFieldArrayView
>
>   Enter the PingOne attributes you want to use to find a user, such as username, userID, or email.
>
> - Identifier textField
>
>   Enter the identifier, which was captured earlier in the flow, that you want to use to find a user. For example, if the attributes specified are email and username, and the identifier is username, the system will search for users whose email or username match the value captured under username.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttributes array uniqueItems: true
>
>     * userIdentifierForFindUser string
>
>       User attribute to match attributes.
>
>     * scimFilter string
>
>       SCIM filter to match users.
>
> - output object
>
>   * matchedUsers array
>
>   * count integer
>
>   * userFilter string
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * matchedUsers array
>
>       * count integer
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "matchedUsers": [
>         {
>           "_embedded": {
>             "user": {
>               "preferredLanguage": "EN",
>               "timezone": "EST",
>               "lastSignOn": {
>                 "at": "00:00:00:0000",
>                 "remoteIp": "127.0.0.1"
>               },
>               "title": "test",
>               "type": "Admin",
>               "locale": "EN",
>               "enabled": true,
>               "createdAt": "00:00:00:0000",
>               "verifyStatus": "NOT_VERIFIED",
>               "nickname": "test",
>               "mfaEnabled": false,
>               "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>               "email": "ping@pingidentity.com",
>               "username": "test"
>             }
>           }
>         }
>       ]
>     }
>   },
>   "matchedUsers": [
>     {
>       "_embedded": {
>         "user": {
>           "preferredLanguage": "EN",
>           "timezone": "EST",
>           "lastSignOn": {
>             "at": "00:00:00:0000",
>             "remoteIp": "127.0.0.1"
>           },
>           "title": "test",
>           "type": "Admin",
>           "locale": "EN",
>           "enabled": true,
>           "createdAt": "00:00:00:0000",
>           "verifyStatus": "NOT_VERIFIED",
>           "nickname": "test",
>           "mfaEnabled": false,
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>           "email": "ping@pingidentity.com",
>           "username": "test"
>         }
>       }
>     }
>   ]
> }
> ```

### Check Password

Validate a user's password.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Password textField
>
>   The user's password to validate.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * password string required minLength: 1
>
>       Password
>
> - output object
>
>   * passwordState object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * rawResponse object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "passwordState": {
>       "environment": {
>         "id": "5007e871-f0e7-4fc9-9ab9-b23b3ae76069"
>       },
>       "user": {
>         "id": "f442f27a-6d9c-4280-891f-bed26a9bd9ce"
>       },
>       "passwordPolicy": {
>         "id": "b91ef66e-2b21-449a-a158-afc2d870ab92"
>       },
>       "status": "OK",
>       "lastChangedAt": "2021-03-15T08:50:24.426Z"
>     }
>   }
> }
> ```

### Create User

Create a user with the attribute values provided.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Username textField required
>
>   The unique identifier for the user.
>
> - Population dropDown
>
>   The name of the population.
>
>   * Use Population ID (Default)
>
>   * Use Alternative ID
>
> - Population ID textField
>
>   The unique identifier for the population.
>
> - * Password textField
>   * Given Name textField
>   * Family Name textField
>   * Email textField
>   * Primary Phone textField
>   * Mobile Phone textField
>   * Preferred Language textField
>   * Locale textField
>   * Other Attributes variableInputList
>
>   Add other attributes and their values.
>
> - Lifecycle Status dropDown
>
>   Indicate whether new users must initially verify their identities through email. If they do, they will receive an email containing a verification code when their accounts are created.
>
>   * ACCOUNT\_OK (Default)
>
>   * VERIFICATION\_REQUIRED
>
> * default object
>
>   * properties object
>
>     * population string required minLength: 0 maxLength: 100
>
>       Population
>
>     * alternativeIdentifier string minLength: 0 maxLength: 255
>
>       Alternative Identifier
>
>     * populationId string minLength: 0 maxLength: 100
>
>       Population ID
>
>     * given string
>
>     * family string
>
>     * email string
>
>     * primaryPhone string
>
>     * mobilePhone string
>
>     * username string required
>
>     * preferredLanguage string
>
>     * locale string
>
>     * passwordForCreateUser string
>
>     * lifecycleStatus string required
>
> - output object
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * rawResponse object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * headers object
>
>   * statusCode integer

### Read User

Find user information.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
> - output object
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * rawResponse object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * headers object
>
>   * statusCode integer

### Update User

Update user attributes.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Username textField required
>
>   The unique identifier for the user.
>
> - * Given Name textField
>   * Family Name textField
>   * Email textField
>   * Primary Phone textField
>   * Mobile Phone textField
>   * Preferred Language textField
>   * Locale textField
>   * Other Attributes variableInputList
>
>   Add other attributes and their values.
>
> - User Attributes to Clear textFieldArrayView
>
>   Type the PingOne user attributes you want to clear for a user, such as name or primaryPhone, and hit enter after each one.
>
> - * PingOne User Attributes link
>   * Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * given string
>
>     * family string
>
>     * email string
>
>     * primaryPhone string
>
>     * mobilePhone string
>
>     * username string
>
>     * preferredLanguage string
>
>     * locale string
>
> - output object
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * rawResponse object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * headers object
>
>   * statusCode integer

### Delete User

Delete users.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer

### Update User Status

Enable or disable user accounts.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Enable User toggleSwitch
>
>   Enable or disable the user's account.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * enabled boolean required
>
>       Enable Status Of User
>
> - output object
>
>   * user object
>
>     * enabled boolean
>
>   * rawResponse object
>
>     * enabled boolean
>
>   * headers object
>
>   * statusCode integer

### Send Email Verification Code

Send a verification code to the user that can be used to verify their email.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
> - output object
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * rawResponse object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * headers object
>
>   * statusCode integer

### Validate Verification Code

Verifies the provided code that was sent to a user's email during account creation.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Verification Code textField
>
>   The code emailed to the user to verify their email address.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * verificationCode string required minLength: 0 maxLength: 100
>
>       Enter the code to verify a user's account.
>
> - output object
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer

### Send Password Recovery Code

Send recovery codes to users' email addresses to recover forgotten passwords.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
> - output object
>
>   * passwordState object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * rawResponse object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {}
> }
> ```

### Validate Password Recovery Code

Validate recovery codes and allow users to reset their passwords.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Recovery Code textField
>
>   The code to validate.
>
> - New Password textField
>
>   The user's new password.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * recoveryCode string required
>
>     * newPassword string required minLength: 1
>
> - output object
>
>   * passwordState object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * rawResponse object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {}
> }
> ```

### Change Password

Change a user's password to a new password using their current password for validation.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Current Password textField
>
>   The user's current password.
>
> - New Password textField
>
>   The user's new password.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * newPassword string minLength: 1
>
>     * currentPassword string minLength: 1
>
> - output object
>
>   * passwordState object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * rawResponse object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "passwordState": {
>       "environment": {
>         "id": "5da98f13-ad62-4234-ba04-2b6e2e85c8ca"
>       },
>       "user": {
>         "id": "c3042000-188f-4bc7-a269-dee1602cf7af"
>       },
>       "passwordPolicy": {
>         "id": "5da98f13-ad62-4234-86d3-01018f6ef0ad"
>       },
>       "status": "OK",
>       "lastChangedAt": "2019-01-08T20:18:31.264Z"
>     }
>   }
> }
> ```

### Set Password

Set a user's password, optionally forcing the user to change password at next login.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Password Value textField
>
>   The user's new password, which can be in a cleartext or pre-encoded format.
>
> - Force Change Password toggleSwitch
>
>   Indicate whether the user must change their password the next time they sign on.
>
> - Bypass PingOne Password Policy toggleSwitch
>
>   Indicate whether the password policy used to authenticate the user's population should be ignored.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * passwordValue string required minLength: 1
>
>     * forceChange boolean
>
>     * bypassPolicy boolean
>
> - output object
>
>   * passwordState object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * rawResponse object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "passwordState": {
>       "environment": {
>         "id": "5da98f13-ad62-4234-ba04-2b6e2e85c8ca"
>       },
>       "user": {
>         "id": "c3042000-188f-4bc7-a269-dee1602cf7af"
>       },
>       "passwordPolicy": {
>         "id": "5da98f13-ad62-4234-86d3-01018f6ef0ad"
>       },
>       "status": "OK",
>       "lastChangedAt": "2019-01-08T20:18:31.264Z"
>     }
>   }
> }
> ```

### Create Account Link

Create an account link for a user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - External ID textField
>
>   ID of a user at an identity provider.
>
> - Identity Provider dropDown
>
>   The name of the PingOne Identity Provider.
>
>   * Use Identity Provider ID (Default)
>
> - Identity Provider ID textField
>
>   ID of the PingOne Identity Provider.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * identityProvider string required minLength: 0 maxLength: 100
>
>       The id of the identity provider the account link is for
>
>     * identityProviderId string minLength: 0 maxLength: 100
>
>       The id of the identity provider the account link is for
>
>     * externalId string required minLength: 0 maxLength: 3000
>
>       The id of the account at the identity provider
>
> - output object
>
> - properties object
>
>   * id string
>
>   * environment object
>
>     * id string
>
>   * identityProvider object
>
>     * id string
>
>   * user object
>
>     * id string
>
>   * externalId string
>
> - rawResponse object
>
>   * id string
>
>   * environment object
>
>     * id string
>
>   * identityProvider object
>
>     * id string
>
>   * user object
>
>     * id string
>
>   * externalId string
>
> - headers object
>
> - statusCode integer

### Read Account Links

Read a user's account links.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
> - output object
>
>   * linkedAccounts array
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * linkedAccounts array
>
>     * count number
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Delete Account Link

Delete a user's account link.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Account link ID textField
>
>   ID of the account link.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * accountLinkId string required minLength: 0 maxLength: 100
>
>       Account link ID
>
> - output object
>
>   * headers object
>
>   * statusCode integer

### Check User Agreement

Indicate whether users need to accept or sign agreements before proceeding.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Agreement dropDown
>
>   The name of the agreement.
>
>   * Use Agreement ID (Default)
>
> - Agreement ID textField
>
>   A unique identifier for the agreement the user has accepted or signed.
>
> - Accept Language textField
>
>   The language in which the agreement is written and indicated by an IEFT BCP 47 language tag, such as "en-US" or "az-Arab".
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * agreementId string minLength: 0 maxLength: 100
>
>       Agreement ID
>
>     * acceptLanguage string minLength: 0 maxLength: 100
>
>       BCP 47 Language tag used as Accept-Language header
>
> - output object
>
>   * agreementPresentation object
>
>     * agreementPresentationId string
>
>     * agreementText string
>
>     * agreementTitle string
>
>     * agreementAcceptCheckboxText string
>
>     * agreementContinueButtonText string
>
>     * agreementDeclineButtonText string
>
>   * userAgreement object
>
>     * \_embedded object
>
>       * agreement object
>
>         * id string
>
>         * name string
>
>         * environment object
>
>           * id string
>
>         * reconsentPeriodDays number
>
>         * totalConsents number
>
>         * totalExpiredConsents number
>
>         * consentsAggregatedAt string
>
>         * enabled boolean
>
>       * revision object
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * effectiveAt string
>
>         * contentType string
>
>         * requireReconsent boolean
>
>       * language object
>
>         * userExperience object
>
>           * acceptCheckboxText string
>
>           * continueButtonText string
>
>           * declineButtonText string
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * displayName string
>
>         * locale string
>
>         * enabled boolean
>
>     * lastConsent object
>
>       * id string
>
>       * expiresAt string
>
>       * revision object
>
>         * id string
>
>       * language object
>
>         * id string
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * status string
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * agreement object
>
>         * id string
>
>         * name string
>
>         * environment object
>
>           * id string
>
>         * reconsentPeriodDays number
>
>         * totalConsents number
>
>         * totalExpiredConsents number
>
>         * consentsAggregatedAt string
>
>         * enabled boolean
>
>       * revision object
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * effectiveAt string
>
>         * contentType string
>
>         * requireReconsent boolean
>
>       * language object
>
>         * userExperience object
>
>           * acceptCheckboxText string
>
>           * continueButtonText string
>
>           * declineButtonText string
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * displayName string
>
>         * locale string
>
>         * enabled boolean
>
>     * lastConsent object
>
>       * id string
>
>       * expiresAt string
>
>       * revision object
>
>         * id string
>
>       * language object
>
>         * id string
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * status string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "agreement": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>         "environment": {
>           "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>         },
>         "name": "Agreement_1_UPDATED_1601679632",
>         "reconsentPeriodDays": 360,
>         "totalConsents": 0,
>         "totalExpiredConsents": 0,
>         "consentsAggregatedAt": "2021-01-15T20:45:17.463Z",
>         "enabled": false
>       },
>       "revision": {
>         "id": "aab73db4-9432-4149-9d24-daa8e6e1289b",
>         "environment": {
>           "id": "af2e0f45-d9cb-4aa1-a8e8-432e040ddc30"
>         },
>         "agreement": {
>           "id": "d462d436-cf80-421c-8c05-881e9958c4b4"
>         },
>         "language": {
>           "id": "7e156496-4e67-4adc-a139-ebbbbe2c1aea"
>         },
>         "effectiveAt": "2098-08-01T22:45:44.497Z",
>         "contentType": "text/plain",
>         "requireReconsent": false
>       },
>       "language": {
>         "id": "a00abf13-22fc-4d66-a89e-7f6abb1d323f",
>         "environment": {
>           "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>         },
>         "displayName": "Language_1601679509",
>         "agreement": {
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>         },
>         "enabled": true,
>         "locale": "en-US"
>       }
>     },
>     "lastConsent": {
>       "language": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>       },
>       "revision": {
>         "id": "90eb5621-eae8-4fa1-aafb-2a884d6848cb"
>       },
>       "at": "2021-08-01T22:45:44.497Z",
>       "expiresAt": "2098-08-01T22:45:44.497Z"
>     },
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "f880dacd-19d1-4d4e-9f2e-9d175bd03e1b"
>     },
>     "agreement": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>     },
>     "status": "ACCEPTED"
>   }
> }
> ```

### Read User Agreements

Find information about agreements users have accepted or signed.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Accept Language textField
>
>   The language in which the agreement is written and indicated by an IEFT BCP 47 language tag, such as "en-US" or "az-Arab".
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * acceptLanguage string minLength: 0 maxLength: 100
>
>       BCP 47 Language tag used as Accept-Language header
>
> - output object
>
>   * userAgreements array
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * userAgreements array
>
>     * count number
>
>     * size number
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "userAgreements": [
>         {
>           "_embedded": {
>             "agreement": {
>               "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>               "environment": {
>                 "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>               },
>               "name": "Agreement_1_UPDATED_1601679632",
>               "reconsentPeriodDays": 360,
>               "totalConsents": 0,
>               "totalExpiredConsents": 0,
>               "consentsAggregatedAt": "2021-01-15T20:45:17.463Z",
>               "enabled": false
>             },
>             "revision": {
>               "id": "aab73db4-9432-4149-9d24-daa8e6e1289b",
>               "environment": {
>                 "id": "af2e0f45-d9cb-4aa1-a8e8-432e040ddc30"
>               },
>               "agreement": {
>                 "id": "d462d436-cf80-421c-8c05-881e9958c4b4"
>               },
>               "language": {
>                 "id": "7e156496-4e67-4adc-a139-ebbbbe2c1aea"
>               },
>               "effectiveAt": "2098-08-01T22:45:44.497Z",
>               "contentType": "text/plain",
>               "requireReconsent": false
>             },
>             "language": {
>               "id": "a00abf13-22fc-4d66-a89e-7f6abb1d323f",
>               "environment": {
>                 "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>               },
>               "displayName": "Language_1601679509",
>               "agreement": {
>                 "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>               },
>               "enabled": true,
>               "locale": "en-US"
>             }
>           },
>           "lastConsent": {
>             "language": {
>               "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>             },
>             "revision": {
>               "id": "90eb5621-eae8-4fa1-aafb-2a884d6848cb"
>             },
>             "at": "2021-08-01T22:45:44.497Z",
>             "expiresAt": "2098-08-01T22:45:44.497Z"
>           },
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>           "environment": {
>             "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>           },
>           "user": {
>             "id": "f880dacd-19d1-4d4e-9f2e-9d175bd03e1b"
>           },
>           "agreement": {
>             "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>           },
>           "status": "ACCEPTED"
>         }
>       ]
>     },
>     "count": 1,
>     "size": 1
>   },
>   "userAgreements": [
>     {
>       "_embedded": {
>         "agreement": {
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>           "environment": {
>             "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>           },
>           "name": "Agreement_1_UPDATED_1601679632",
>           "reconsentPeriodDays": 360,
>           "totalConsents": 0,
>           "totalExpiredConsents": 0,
>           "consentsAggregatedAt": "2021-01-15T20:45:17.463Z",
>           "enabled": false
>         },
>         "revision": {
>           "id": "aab73db4-9432-4149-9d24-daa8e6e1289b",
>           "environment": {
>             "id": "af2e0f45-d9cb-4aa1-a8e8-432e040ddc30"
>           },
>           "agreement": {
>             "id": "d462d436-cf80-421c-8c05-881e9958c4b4"
>           },
>           "language": {
>             "id": "7e156496-4e67-4adc-a139-ebbbbe2c1aea"
>           },
>           "effectiveAt": "2098-08-01T22:45:44.497Z",
>           "contentType": "text/plain",
>           "requireReconsent": false
>         },
>         "language": {
>           "id": "a00abf13-22fc-4d66-a89e-7f6abb1d323f",
>           "environment": {
>             "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>           },
>           "displayName": "Language_1601679509",
>           "agreement": {
>             "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>           },
>           "enabled": true,
>           "locale": "en-US"
>         }
>       },
>       "lastConsent": {
>         "language": {
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>         },
>         "revision": {
>           "id": "90eb5621-eae8-4fa1-aafb-2a884d6848cb"
>         },
>         "at": "2021-08-01T22:45:44.497Z",
>         "expiresAt": "2098-08-01T22:45:44.497Z"
>       },
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>       "environment": {
>         "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>       },
>       "user": {
>         "id": "f880dacd-19d1-4d4e-9f2e-9d175bd03e1b"
>       },
>       "agreement": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>       },
>       "status": "ACCEPTED"
>     }
>   ]
> }
> ```

### Revoke User Agreement

Revoke agreements users have accepted or signed.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Agreement dropDown
>
>   The name of the agreement.
>
>   * Use Agreement ID (Default)
>
> - Agreement ID textField
>
>   A unique identifier for the agreement the user has accepted or signed.
>
> - Accept Language textField
>
>   The language in which the agreement is written and indicated by an IEFT BCP 47 language tag, such as "en-US" or "az-Arab".
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * agreementId string minLength: 0 maxLength: 100
>
>       Agreement ID
>
>     * acceptLanguage string minLength: 0 maxLength: 100
>
>       BCP 47 Language tag used as Accept-Language header
>
> - output object
>
>   * userAgreement object
>
>     * \_embedded object
>
>       * agreement object
>
>         * id string
>
>         * name string
>
>         * environment object
>
>           * id string
>
>         * reconsentPeriodDays number
>
>         * totalConsents number
>
>         * totalExpiredConsents number
>
>         * consentsAggregatedAt string
>
>         * enabled boolean
>
>       * revision object
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * effectiveAt string
>
>         * contentType string
>
>         * requireReconsent boolean
>
>       * language object
>
>         * userExperience object
>
>           * acceptCheckboxText string
>
>           * continueButtonText string
>
>           * declineButtonText string
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * displayName string
>
>         * locale string
>
>         * enabled boolean
>
>     * lastConsent object
>
>       * id string
>
>       * expiresAt string
>
>       * revision object
>
>         * id string
>
>       * language object
>
>         * id string
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * status string
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * agreement object
>
>         * id string
>
>         * name string
>
>         * environment object
>
>           * id string
>
>         * reconsentPeriodDays number
>
>         * totalConsents number
>
>         * totalExpiredConsents number
>
>         * consentsAggregatedAt string
>
>         * enabled boolean
>
>       * revision object
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * effectiveAt string
>
>         * contentType string
>
>         * requireReconsent boolean
>
>       * language object
>
>         * userExperience object
>
>           * acceptCheckboxText string
>
>           * continueButtonText string
>
>           * declineButtonText string
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * displayName string
>
>         * locale string
>
>         * enabled boolean
>
>     * lastConsent object
>
>       * id string
>
>       * expiresAt string
>
>       * revision object
>
>         * id string
>
>       * language object
>
>         * id string
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * status string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "agreement": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>         "environment": {
>           "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>         },
>         "name": "Agreement_1_UPDATED_1601679632",
>         "reconsentPeriodDays": 360,
>         "totalConsents": 0,
>         "totalExpiredConsents": 0,
>         "consentsAggregatedAt": "2021-01-15T20:45:17.463Z",
>         "enabled": false
>       },
>       "revision": {
>         "id": "aab73db4-9432-4149-9d24-daa8e6e1289b",
>         "environment": {
>           "id": "af2e0f45-d9cb-4aa1-a8e8-432e040ddc30"
>         },
>         "agreement": {
>           "id": "d462d436-cf80-421c-8c05-881e9958c4b4"
>         },
>         "language": {
>           "id": "7e156496-4e67-4adc-a139-ebbbbe2c1aea"
>         },
>         "effectiveAt": "2098-08-01T22:45:44.497Z",
>         "contentType": "text/plain",
>         "requireReconsent": false
>       },
>       "language": {
>         "id": "a00abf13-22fc-4d66-a89e-7f6abb1d323f",
>         "environment": {
>           "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>         },
>         "displayName": "Language_1601679509",
>         "agreement": {
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>         },
>         "enabled": true,
>         "locale": "en-US"
>       }
>     },
>     "lastConsent": {
>       "language": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>       },
>       "revision": {
>         "id": "90eb5621-eae8-4fa1-aafb-2a884d6848cb"
>       },
>       "at": "2021-08-01T22:45:44.497Z",
>       "expiresAt": "2098-08-01T22:45:44.497Z"
>     },
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "f880dacd-19d1-4d4e-9f2e-9d175bd03e1b"
>     },
>     "agreement": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>     },
>     "status": "ACCEPTED"
>   }
> }
> ```

### Accept User Agreement

Accept user agreements.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Agreement Presentation ID textField
>
>   The unique identifier for the agreement information to ensure the correct agreement revision and language is being accepted.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * agreementPresentationId string required
>
>       Read User Agreement and Read Agreement capabilities generate this id in their agreement presentation output.
>
> - output object
>
>   * userAgreement object
>
>     * \_embedded object
>
>       * agreement object
>
>         * id string
>
>         * name string
>
>         * environment object
>
>           * id string
>
>         * reconsentPeriodDays number
>
>         * totalConsents number
>
>         * totalExpiredConsents number
>
>         * consentsAggregatedAt string
>
>         * enabled boolean
>
>       * revision object
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * effectiveAt string
>
>         * contentType string
>
>         * requireReconsent boolean
>
>       * language object
>
>         * userExperience object
>
>           * acceptCheckboxText string
>
>           * continueButtonText string
>
>           * declineButtonText string
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * displayName string
>
>         * locale string
>
>         * enabled boolean
>
>     * lastConsent object
>
>       * id string
>
>       * expiresAt string
>
>       * revision object
>
>         * id string
>
>       * language object
>
>         * id string
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * status string
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * agreement object
>
>         * id string
>
>         * name string
>
>         * environment object
>
>           * id string
>
>         * reconsentPeriodDays number
>
>         * totalConsents number
>
>         * totalExpiredConsents number
>
>         * consentsAggregatedAt string
>
>         * enabled boolean
>
>       * revision object
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * effectiveAt string
>
>         * contentType string
>
>         * requireReconsent boolean
>
>       * language object
>
>         * userExperience object
>
>           * acceptCheckboxText string
>
>           * continueButtonText string
>
>           * declineButtonText string
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * displayName string
>
>         * locale string
>
>         * enabled boolean
>
>     * lastConsent object
>
>       * id string
>
>       * expiresAt string
>
>       * revision object
>
>         * id string
>
>       * language object
>
>         * id string
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * status string
>
>   * headers object
>
>   * statusCode integer

### Read Agreement Content

Find information about the agreement content.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Agreement dropDown
>
>   The name of the agreement.
>
>   * Use Agreement ID (Default)
>
> - Agreement ID textField
>
>   A unique identifier for the agreement the user has accepted or signed.
>
> - Accept Language textField
>
>   The language in which the agreement is written and indicated by an IEFT BCP 47 language tag, such as "en-US" or "az-Arab".
>
> - User Locale textField
>
>   The user's location, which determines the language in which the agreement is written and indicated by an IEFT BCP 47 language tag, such as "en-US" or "az-Arab".
>
> * default object
>
>   * properties object
>
>     * agreementId string minLength: 0 maxLength: 100
>
>       Agreement ID
>
>     * acceptLanguage string minLength: 0 maxLength: 100
>
>       BCP 47 Language tag used as Accept-Language header
>
>     * userLocale string minLength: 0 maxLength: 100
>
>       User Locale
>
> - output object
>
>   * agreementPresentation object
>
>     * agreementPresentationId string
>
>     * agreementText string
>
>     * agreementTitle string
>
>     * agreementAcceptCheckboxText string
>
>     * agreementContinueButtonText string
>
>     * agreementDeclineButtonText string
>
>   * userAgreement object
>
>     * \_embedded object
>
>       * agreement object
>
>         * id string
>
>         * name string
>
>         * environment object
>
>           * id string
>
>         * reconsentPeriodDays number
>
>         * totalConsents number
>
>         * totalExpiredConsents number
>
>         * consentsAggregatedAt string
>
>         * enabled boolean
>
>       * revision object
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * effectiveAt string
>
>         * contentType string
>
>         * requireReconsent boolean
>
>       * language object
>
>         * userExperience object
>
>           * acceptCheckboxText string
>
>           * continueButtonText string
>
>           * declineButtonText string
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * displayName string
>
>         * locale string
>
>         * enabled boolean
>
>     * lastConsent object
>
>       * id string
>
>       * expiresAt string
>
>       * revision object
>
>         * id string
>
>       * language object
>
>         * id string
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * status string
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * agreement object
>
>         * id string
>
>         * name string
>
>         * environment object
>
>           * id string
>
>         * reconsentPeriodDays number
>
>         * totalConsents number
>
>         * totalExpiredConsents number
>
>         * consentsAggregatedAt string
>
>         * enabled boolean
>
>       * revision object
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * effectiveAt string
>
>         * contentType string
>
>         * requireReconsent boolean
>
>       * language object
>
>         * userExperience object
>
>           * acceptCheckboxText string
>
>           * continueButtonText string
>
>           * declineButtonText string
>
>         * id string
>
>         * environment object
>
>           * id string
>
>         * displayName string
>
>         * locale string
>
>         * enabled boolean
>
>     * lastConsent object
>
>       * id string
>
>       * expiresAt string
>
>       * revision object
>
>         * id string
>
>       * language object
>
>         * id string
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * status string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "agreement": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>         "environment": {
>           "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>         },
>         "name": "Agreement_1_UPDATED_1601679632",
>         "reconsentPeriodDays": 360,
>         "totalConsents": 0,
>         "totalExpiredConsents": 0,
>         "consentsAggregatedAt": "2021-01-15T20:45:17.463Z",
>         "enabled": false
>       },
>       "revision": {
>         "id": "aab73db4-9432-4149-9d24-daa8e6e1289b",
>         "environment": {
>           "id": "af2e0f45-d9cb-4aa1-a8e8-432e040ddc30"
>         },
>         "agreement": {
>           "id": "d462d436-cf80-421c-8c05-881e9958c4b4"
>         },
>         "language": {
>           "id": "7e156496-4e67-4adc-a139-ebbbbe2c1aea"
>         },
>         "effectiveAt": "2098-08-01T22:45:44.497Z",
>         "contentType": "text/plain",
>         "requireReconsent": false
>       },
>       "language": {
>         "id": "a00abf13-22fc-4d66-a89e-7f6abb1d323f",
>         "environment": {
>           "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>         },
>         "displayName": "Language_1601679509",
>         "agreement": {
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>         },
>         "enabled": true,
>         "locale": "en-US"
>       }
>     },
>     "lastConsent": {
>       "language": {
>         "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>       },
>       "revision": {
>         "id": "90eb5621-eae8-4fa1-aafb-2a884d6848cb"
>       },
>       "at": "2021-08-01T22:45:44.497Z",
>       "expiresAt": "2098-08-01T22:45:44.497Z"
>     },
>     "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>     "environment": {
>       "id": "9ad15e9e-3ac6-43f7-a053-d46b87d6c4a7"
>     },
>     "user": {
>       "id": "f880dacd-19d1-4d4e-9f2e-9d175bd03e1b"
>     },
>     "agreement": {
>       "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb"
>     },
>     "status": "ACCEPTED"
>   }
> }
> ```

### Read Population

Find population information.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Population dropDown
>
>   The name of the population.
>
>   * Use Population ID (Default)
>
>   * Use Alternative ID
>
> - Alternative Identifier textField
>
>   Enter an Alternative Identifier to look for populations.
>
> - Population ID textField
>
>   The unique identifier for the population.
>
> * default object
>
>   * properties object
>
>     * population string required minLength: 0 maxLength: 100
>
>       Population
>
>     * alternativeIdentifier string minLength: 0 maxLength: 255
>
>       Alternative Identifier
>
>     * populationId string minLength: 0 maxLength: 100
>
>       Population ID
>
> - output object
>
>   * population object
>
>     * id string
>
>     * name string
>
>     * description string
>
>     * userCount number
>
>     * createdAt string
>
>     * updatedAt string
>
>     * passwordPolicy object
>
>       * id string
>
>     * preferredLanguage string
>
>     * defaultIdentityProvider object
>
>       * id string
>
>       * type string
>
>     * alternativeIdentifiers array
>
>     * theme object
>
>       * id string
>
>   * populations array
>
>   * rawResponse object
>
>     * id string
>
>     * name string
>
>     * description string
>
>     * userCount number
>
>     * createdAt string
>
>     * updatedAt string
>
>     * passwordPolicy object
>
>       * id string
>
>     * preferredLanguage string
>
>     * defaultIdentityProvider object
>
>       * id string
>
>       * type string
>
>     * alternativeIdentifiers array
>
>     * theme object
>
>       * id string
>
>   * headers object
>
>   * statusCode integer

### Read User Group Memberships

Find information about the groups to which users belong.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
> - output object
>
>   * groupMemberships array
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * groupMemberships array
>
>     * count number
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Create User Group Membership

Add a user to a group.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Group dropDown
>
>   The name of the group.
>
>   * Use Group ID (Default)
>
> - Group ID textField
>
>   The unique identifier for the group.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * groupId string minLength: 0 maxLength: 100
>
>       Group ID
>
>     * groupName string
>
>     * description string
>
>     * externalId string
>
>     * userFilter string
>
>       SCIM filter for users
>
>     * memberGroupRelationship boolean
>
>     * customData object
>
> - output object
>
>   * groupMembership object
>
>     * id string
>
>     * name string
>
>     * population object
>
>       * id string
>
>     * type string
>
>   * rawResponse object
>
>     * groupMembership object
>
>       * id string
>
>       * name string
>
>       * population object
>
>         * id string
>
>       * type string
>
>   * headers object
>
>   * statusCode integer

### Delete User Group Membership

Remove a user from a group.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Group dropDown
>
>   The name of the group.
>
>   * Use Group ID (Default)
>
> - Group ID textField
>
>   The unique identifier for the group.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * matchAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string required
>
>       User attribute to match attributes.
>
>     * groupId string minLength: 0 maxLength: 100
>
>       Group ID
>
>     * groupName string
>
>     * description string
>
>     * externalId string
>
>     * userFilter string
>
>       SCIM filter for users
>
>     * memberGroupRelationship boolean
>
>     * customData object
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer

### Migrate User through Gateway

Validate a user's credentials and, if valid, migrate the user from a PingOne gateway to PingOne.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Username textField required
>
>   The user's unique identifier in the PingOne gateway.
>
> - Password textField required
>
>   The user's password in the PingOne gateway.
>
> - Gateway User Type List variableInputList required
>
>   The gateway and user type to target when validating the user's credentials. These values are based on the gateways configured in your PingOne environment.
>
> * default object
>
>   * properties object
>
>     * usernameGateway string required
>
>       The user's unique identifier in the PingOne gateway.
>
>     * passwordGateway string required minLength: 4 maxLength: 100
>
>       The user's password in the PingOne gateway.
>
>     * gatewayUserTypeList array required
>
>       The gateway and user type to target when validating the user's credentials. These values are based on the gateways configured in your PingOne environment.
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer

### Create Group

Create a user group.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Group Name textField required
>
>   The name of the group.
>
> - Group Description textArea
>
>   The description of the group.
>
> - Dynamic User Filter textField
>
>   A filter to automatically assign users to the group.
>
> - Population dropDown
>
>   The name of the population.
>
>   * Use Population ID (Default)
>
>   * Use Alternative ID
>
> - Population ID textField
>
>   The unique identifier for the population.
>
> - * Edit Metadata Properties JSON toggleSwitch
>   * Metadata Properties keyValueList
>
>   This input will overwrite the current metadata for the group.
>
> - Metadata Properties textArea
>
>   This input will overwrite the current metadata for the group.
>
> * default object
>
>   * properties object
>
>     * groupId string
>
>     * groupName string required
>
>     * description string
>
>     * externalId string
>
>     * userFilter string
>
>       SCIM filter for users
>
>     * memberGroupRelationship boolean
>
>     * customData object
>
> - output object
>
>   * group object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * customData object
>
>     * population object
>
>       * id string
>
>     * name string
>
>     * description string
>
>     * isExternal string
>
>     * externalId string
>
>     * userFilter string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * customData object
>
>     * population object
>
>       * id string
>
>     * name string
>
>     * description string
>
>     * isExternal string
>
>     * externalId string
>
>     * userFilter string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * headers object
>
>   * statusCode integer

### Read Group

Read a user group.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Group ID textField
>
>   The unique identifier for the group.
>
> * default object
>
>   * properties object
>
>     * groupId string required minLength: 0 maxLength: 100
>
>       Group ID
>
> - output object
>
>   * group object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * customData object
>
>     * population object
>
>       * id string
>
>     * name string
>
>     * description string
>
>     * isExternal string
>
>     * externalId string
>
>     * userFilter string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * customData object
>
>     * population object
>
>       * id string
>
>     * name string
>
>     * description string
>
>     * isExternal string
>
>     * externalId string
>
>     * userFilter string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * headers object
>
>   * statusCode integer

### Update Group

Update a user group.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Group ID textField
>
>   The unique identifier for the group.
>
> - Group Name textField required
>
>   The name of the group.
>
> - Group Description textArea
>
>   The description of the group.
>
> - Dynamic User Filter textField
>
>   A filter to automatically assign users to the group.
>
> - * Edit Metadata Properties JSON toggleSwitch
>   * Metadata Properties keyValueList
>
>   This input will overwrite the current metadata for the group.
>
> - Metadata Properties textArea
>
>   This input will overwrite the current metadata for the group.
>
> * default object
>
>   * properties object
>
>     * groupId string required
>
>     * groupName string
>
>     * description string
>
>     * externalId string
>
>     * userFilter string
>
>       SCIM filter for users
>
>     * memberGroupRelationship boolean
>
>     * customData object
>
> - output object
>
>   * group object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * customData object
>
>     * population object
>
>       * id string
>
>     * name string
>
>     * description string
>
>     * isExternal string
>
>     * externalId string
>
>     * userFilter string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * customData object
>
>     * population object
>
>       * id string
>
>     * name string
>
>     * description string
>
>     * isExternal string
>
>     * externalId string
>
>     * userFilter string
>
>     * createdAt string
>
>     * updatedAt string
>
>   * headers object
>
>   * statusCode integer

### Delete Group

Delete a user group.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Group ID textField
>
>   The unique identifier for the group.
>
> * default object
>
>   * properties object
>
>     * groupId string required minLength: 0 maxLength: 100
>
>       Group ID
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer

### Read Group Members

Read up to 100 members of a group.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Group ID textField
>
>   The unique identifier for the group.
>
> - PingOne Attributes textFieldArrayView
>
>   Enter the PingOne attributes you want to use to find a user, such as username, userID, or email.
>
> - Identifier textField
>
>   Enter the identifier, which was captured earlier in the flow, that you want to use to find a user. For example, if the attributes specified are email and username, and the identifier is username, the system will search for users whose email or username match the value captured under username.
>
> - Direct Member Relationship toggleSwitch
>
>   The output will only include members that are directly assigned to the group, instead of including any members assigned by a filter.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * groupId string required minLength: 0 maxLength: 100
>
>       Group ID
>
> - output object
>
>   * matchedUsers array
>
>   * count integer
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * matchedUsers array
>
>       * count integer
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "_embedded": {
>       "matchedUsers": [
>         {
>           "_embedded": {
>             "user": {
>               "preferredLanguage": "EN",
>               "timezone": "EST",
>               "lastSignOn": {
>                 "at": "00:00:00:0000",
>                 "remoteIp": "127.0.0.1"
>               },
>               "title": "test",
>               "type": "Admin",
>               "locale": "EN",
>               "enabled": true,
>               "createdAt": "00:00:00:0000",
>               "verifyStatus": "NOT_VERIFIED",
>               "nickname": "test",
>               "mfaEnabled": false,
>               "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>               "email": "ping@pingidentity.com",
>               "username": "test"
>             }
>           }
>         }
>       ]
>     }
>   },
>   "matchedUsers": [
>     {
>       "_embedded": {
>         "user": {
>           "preferredLanguage": "EN",
>           "timezone": "EST",
>           "lastSignOn": {
>             "at": "00:00:00:0000",
>             "remoteIp": "127.0.0.1"
>           },
>           "title": "test",
>           "type": "Admin",
>           "locale": "EN",
>           "enabled": true,
>           "createdAt": "00:00:00:0000",
>           "verifyStatus": "NOT_VERIFIED",
>           "nickname": "test",
>           "mfaEnabled": false,
>           "id": "43eb5621-eae8-4fa1-aafb-2a884d6848cb",
>           "email": "ping@pingidentity.com",
>           "username": "test"
>         }
>       }
>     }
>   ]
> }
> ```

### Authenticate User via Kerberos

Authenticate Active Directory users seamlessly via the Kerberos protocol.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Gateway dropDown required
>
>   Select the gateway that connects to the Active Directory servers where the users are located.
>
> - User Type dropDown required
>
>   Select the user type through which the users can be found.
>
>   Default: `useUserTypeId`
>
> - Create PingOne User toggleSwitch
>
>   When enabled, DaVinci creates a PingOne user account using attributes from Active Directory. Disable this to support a legacy integration where DaVinci is configured as an External IdP in PingOne.
>
> * default object
>
>   * properties object
>
>     * gatewayId string required
>
>       Gateway Id
>
>     * userTypeId string required
>
>       User Type ID
>
>     * gatewayUserTypeList array
>
>       The gateway and user type to target when validating the user's credentials. These values are based on the gateways configured in your PingOne environment.
>
>     * createUserIfNotFound boolean
>
> - output object
>
>   * user object
>
>     * id string
>
>     * username string
>
>     * environment object
>
>       * id string
>
>     * population object
>
>       * id string
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Single-Factor Sign On

Sign on with a username and password.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Sign On Form dropDown required
>
>   Select the sign-on form for single-factor authentication.
>
> - Form Theme dropDown required
>
>   Choose from themes configured in the PingOne environment or use a theme ID. If no theme is selected, the default active theme is used.
>
>   * PingOne Active Theme (Default)
>
>   * Use Theme ID
>
> - Theme ID textField
>
>   The ID of the PingOne theme to use when rendering the form, such as `aa4b3e81-cf7e-8685-4b7b-7ec89cfcf7c8`.
>
> * default object
>
>   * properties object
>
>     * singleFactorSignOnFormId string required
>
>       Single-Factor Sign On Form ID
>
> - output object
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * passwordState object
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * passwordPolicy object
>
>       * id string
>
>     * warnings object
>
>       * expires string
>
>       * noChangeUntil string
>
>       * failuresRemaining number
>
>     * status string
>
>     * lastChangedAt string
>
>   * buttonValue string
>
>   * rawResponse object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * headers object
>
>   * statusCode integer

### Unlock User

Unlock a user by their user ID.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   Enter the ID of the user.
>
> * default object
>
>   * properties object
>
>     * userId string required
>
> - output object
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * rawResponse object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * headers object
>
>   * statusCode integer

### Update User through Gateway

Retrieve a user's attributes through a PingOne gateway and update the PingOne user profile with them.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Override User toggleSwitch
>
>   User ID is mapped automatically unless you override them here.
>
> - PingOne Attribute dropDown
>
>   Select the attribute that you want to match against the provided identifier to find a user.
>
>   * User ID (Default)
>
>   * Username
>
>   * Email
>
> - Identifier textField
>
>   Enter the User ID, Username, or Email address of the user that you want to find.
>
> - Search Special-Character Usernames toggleSwitch
>
>   A toggle switch to automatically escape the user attributes.
>
> * default object
>
>   * properties object
>
>     * overrideUser boolean
>
>       Override User
>
>     * matchAttribute string
>
>       PingOne user attribute to identify a user with.
>
>     * identifier string
>
>       User attribute to match attributes.
>
>   * authentication object
>
>     * userId string
>
>     * methods array
>
> - output object
>
>   * user object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * rawResponse object
>
>     * preferredLanguage string
>
>     * timezone string
>
>     * lastSignOn object
>
>       * at string
>
>       * remoteIp string
>
>     * title string
>
>     * type string
>
>     * locale string
>
>     * enabled boolean
>
>     * identityProvider object
>
>       * id string
>
>       * type string
>
>     * lifecycle object
>
>       * status string
>
>     * createdAt string
>
>     * verifyStatus string
>
>     * nickname string
>
>     * mfaEnabled boolean
>
>     * id string
>
>     * email string
>
>     * emailVerified boolean
>
>     * updatedAt string
>
>     * address object
>
>       * streetAddress string
>
>       * locality string
>
>       * region string
>
>       * postalCode string
>
>       * countryCode string
>
>     * externalId string
>
>     * photo object
>
>       * href string
>
>     * population object
>
>       * id string
>
>     * primaryPhone string
>
>     * accountId string
>
>     * mobilePhone string
>
>     * name object
>
>       * formatted string
>
>       * given string
>
>       * middle string
>
>       * family string
>
>       * honorificPrefix string
>
>       * honorificSuffix string
>
>     * account object
>
>       * canAuthenticate boolean
>
>       * status string
>
>       * lockedAt string
>
>       * secondsUntilUnlock string
>
>       * unlockAt string
>
>     * username string
>
>   * headers object
>
>   * statusCode integer

### Read Theme

Read a theme.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Theme ID textField
>
>   The ID of the PingOne theme to use when rendering the form, such as `aa4b3e81-cf7e-8685-4b7b-7ec89cfcf7c8`.
>
> * default object
>
>   * properties object
>
>     * themeId string required minLength: 0 maxLength: 100
>
>       Theme ID
>
> - output object
>
>   * theme object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * template string
>
>     * default boolean
>
>     * configuration object
>
>       * logoType string
>
>       * logo object
>
>         * href string
>
>         * id string
>
>       * backgroundColor string
>
>       * backgroundType string
>
>       * backgroundImage object
>
>         * href string
>
>         * id string
>
>       * bodyTextColor string
>
>       * cardColor string
>
>       * headingTextColor string
>
>       * linkTextColor string
>
>       * buttonTextColor string
>
>       * buttonColor string
>
>       * name string
>
>       * footer string
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * template string
>
>     * default boolean
>
>     * configuration object
>
>       * logoType string
>
>       * logo object
>
>         * href string
>
>         * id string
>
>       * backgroundColor string
>
>       * backgroundType string
>
>       * backgroundImage object
>
>         * href string
>
>         * id string
>
>       * bodyTextColor string
>
>       * cardColor string
>
>       * headingTextColor string
>
>       * linkTextColor string
>
>       * buttonTextColor string
>
>       * buttonColor string
>
>       * name string
>
>       * footer string
>
>   * headers object
>
>   * statusCode integer

## Limitations

The following are known issues or limitations with the PingOne connector:

### LiveSync operations

The PingOne connector does not support LiveSync operations.

If you attempt to implement LiveSync, you receive the following error:

```
Operation org.identityconnectors.framework.api.operations.SyncApiOp is not supported by the Connector.
```

For data synchronization, implement scheduled reconciliation which is supported.

## Troubleshooting

### "Username is immutable and cannot be updated" error

In some flows, particularly **SSPR Activate** or **Set Password** subflows, the **Update User** capability can return the following error:

Failed to update PingOne account: "username cannot be updated"

**Cause**

The username field is a unique and unchangeable identifier in PingOne. Minor variances in a username, such as leading or trailing whitespace, can occur when it passes through multiple sources or subflows before reaching the **Update User** node. When the node executes, PingOne treats the variance as an attempt to change the username value and returns the "username cannot be updated" error.

**Solution**

Add a **Find User** node (using the **Find User** capability) immediately before the **Update User** node in your flow:

1. Use the **Find User** node to look up the user in PingOne.

2. . Map the `username` value from the **Find User** output to the **Username** field of the **Update User** node.

This ensures the canonical username value stored in PingOne is always used, eliminating mismatches caused by formatting differences from upstream nodes.

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For additional robustness, enable the **Search Special-Character Usernames** toggle on the **Find User** node. This helps handle cases where usernames contain characters that might otherwise interfere with the lookup. |
