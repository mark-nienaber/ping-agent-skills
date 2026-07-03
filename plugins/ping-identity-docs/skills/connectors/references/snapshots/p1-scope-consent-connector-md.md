---
title: PingOne Scope Consent Connector
description: The PingOne Scope Consent connector lets you view consent records on an application or user basis, revoke or update user consent records, or prompt users to provide or decline consent to sign-on policies and record these decisions.
component: connectors
page_id: connectors::p1_scope_consent_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_scope_consent_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
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
  manage-user-consent: Manage user consent
  capabilities: Capabilities
  getAllConsents: Read User Consent
  checkConsent: Check User Consent
  recordConsent: Save User Consent
  revokeConsent: Revoke User Consent
  appConsent: Get User Consent
---

# PingOne Scope Consent Connector

The PingOne Scope Consent connector lets you view consent records on an application or user basis, revoke or update user consent records, or prompt users to provide or decline consent to sign-on policies and record these decisions.

You can use the PingOne Scope Consent connector to:

* View a list of application consent records a user has granted, declined, or revoked

* Determine whether a user has granted consent for an application

* Accept or decline consent for an application on behalf of a user

* Update the application consent record as revoked

* Check, prompt for, and record user decisions regarding consent for an application

## Setup

### Resources

Learn more in the following sections of the PingOne documentation:

* PingOne:

  * [Introduction to PingOne](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html)

  * [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html)

  * [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)

  * [Agreements](https://docs.pingidentity.com/pingone/user_experience/p1_agreements.html)

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

Learn how to set up your PingOne environment in [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html).

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

1. In your PingOne environment, go to **Applications > Applications**.

   If you haven't added the application yet, refer to [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).

2. Locate the appropriate application and click it to open the details panel.

3. Click the **Roles** tab and then click the **Pencil** icon to edit the roles.

4. Review the assigned roles to ensure that they include **Environment Admin** and **Identity Data Admin** roles. If not, click **[icon: plus, set=fa]Add role** to assign them.

#### Getting your application credentials

Get the **Client ID** and **Client secret** from the PingOne console before setting up the PingOne connector in DaVinci:

1. In your PingOne environment, go to **Applications > Applications**.

   If you haven't added the application yet, refer to [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).

2. Locate the appropriate application and click it to open the details panel.

3. On the **Configuration** tab, expand **General** and locate the **Client ID** and **Client secret**. Copy these values to a secure location.

#### Getting your environment details

Get your **Environment ID** and **Region** before setting up the PingOne connector in DaVinci:

1. In your PingOne environment, go to **Settings > Environment Properties**.

2. Locate the **Environment ID** and **Region**. Copy these values to a secure location.

### Setting up the PingOne connector configuration

In DaVinci, add a PingOne connection. Learn more in [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).

#### Connector configuration

##### Environment ID

The unique identifier for the appropriate PingOne environment. Learn how to find the environment ID in [Environment properties](https://docs.pingidentity.com/pingone/settings/p1_environments.html).

##### Client ID

The unique public identifier for the PingOne application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). Learn how to find the client ID in [Viewing application details](https://docs.pingidentity.com/pingone/applications/p1_viewapplications.html).

##### Client secret

The cryptographic secret that is known only to the application and the authorization server. Use the client secret of the application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). Learn how to find the client secret in [Viewing a client secret](https://docs.pingidentity.com/pingone/applications/p1_view_client_secret_application.html).

##### Region

The geographic region that hosts your PingOne tenant. Learn how to find the region in [Environment properties](https://docs.pingidentity.com/pingone/settings/p1_environments.html).

## Using the connector in a flow

### Manage user consent

You can use the PingOne Scope Consent connector to view and manage user consent to an application as part of a DaVinci flow policy.

No special configuration is needed. Add the capability and populate its properties according to the help text.

Use one of the following capabilities to view information about consent records:

* **Read User Consent**: Use to view a list of all application consent records a specific user has granted, declined, or revoked.

* **Check User Consent**: Use to determine whether a user has granted consent for a specific application.

Use one of the following capabilities to manage and update user consent records:

* **Save User Consent**: Use to accept or decline consent for an application on behalf of a user.

* **Revoke User Consent**: Use to update the application consent record for a user as revoked.

Use **Get User Consent** to check, prompt for, and record user decisions regarding consent to application as part of a DaVinci flow policy. Use this capability in a flow at the point where you want to prompt the user for their consent. Use the **Custom Screens** tab to edit the HTML and CSS to customize the appearance and text of the prompt that is displayed to the user. For example, change `Do you approve the request?` to `Do you accept this request?` or change the buttons from `Approve` and `Decline` to `Yes` and `No`.

## Capabilities

### Read User Consent

Find information about consent users have granted for all applications.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Attribute dropDown required
>
>   Select the attribute you want to use to locate a user.
>
>   * User ID
>
>   * Username
>
>   * Email
>
> - User Identifier textField required
>
>   Enter the user ID, username, or email address of the user you want to locate.
>
> * default object
>
>   * properties object
>
>     * matchUserAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * userIdentifier string required
>
>       User attribute to match user.
>
> - output object
>
>   * consents array
>
>   * properties object
>
>     * application object
>
>     * properties object
>
>       * id string
>
>       * name string
>
>       * type string
>
>     * consentId string
>
>     * consentStatus string
>
>     * consentScopes array
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * consents array
>
>     * count number
>
>     * size number
>
>   * statusCode number
>
>   * headers object

### Check User Consent

Indicate whether users have granted consent for an application.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Attribute dropDown required
>
>   Select the attribute you want to use to locate a user.
>
>   * User ID
>
>   * Username
>
>   * Email
>
> - User Identifier textField required
>
>   Enter the user ID, username, or email address of the user you want to locate.
>
> - Application Attribute dropDown required
>
>   Select the application attribute that you want to use to locate an application.
>
>   * Application ID
>
>   * Application Name
>
> - Application Identifier textField required
>
>   Enter the application ID or name of the application you want to locate.
>
> * default object
>
>   * properties object
>
>     * matchUserAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * userIdentifier string required
>
>       User attribute to match user.
>
>     * matchApplicationAttribute string required
>
>       PingOne application attribute to identify an application with.
>
>     * applicationIdentifier string required
>
>       Application attribute to match application.
>
> - output object
>
>   * application object
>
>     * id string
>
>     * name string
>
>     * type string
>
>   * consentId string
>
>   * consentStatus string
>
>   * consentScopes array
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * consents array
>
>     * count number
>
>     * size number
>
>   * statusCode number
>
>   * headers object

### Save User Consent

Accept or decline user consent for an application. It replaces the existing consent for the application if there is one.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Attribute dropDown required
>
>   Select the attribute you want to use to locate a user.
>
>   * User ID
>
>   * Username
>
>   * Email
>
> - User Identifier textField required
>
>   Enter the user ID, username, or email address of the user you want to locate.
>
> - Application Attribute dropDown required
>
>   Select the application attribute that you want to use to locate an application.
>
>   * Application ID
>
>   * Application Name
>
> - Application Identifier textField required
>
>   Enter the application ID or name of the application you want to locate.
>
> - Scopes textField required
>
>   Enter the space-separated list of scopes that have been requested. These scopes are validated against the allowed scopes assigned to the PingOne application.
>
> - Consent Result textField required
>
>   The accept or decline consent result from the user and indicated by "true", "false, "yes", "no", "accepted", or "declined".
>
> * default object
>
>   * userAgent string
>
>     User Agent
>
>   * ip string
>
>     Client IP Address
>
>   * properties object
>
>     * matchUserAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * userIdentifier string required
>
>       User attribute to match user.
>
>     * matchApplicationAttribute string required
>
>       PingOne application attribute to identify an application with.
>
>     * applicationIdentifier string required
>
>       Application attribute to match application.
>
>     * scopesUnconditionalRequired string required
>
>       Scopes.
>
>     * consentResult string required
>
>       Consent Result.
>
> - output object
>
>   * application object
>
>     * id string
>
>     * name string
>
>     * type string
>
>   * consentId string
>
>   * consentStatus string
>
>   * consentScopes array
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Revoke User Consent

Revoke and remove user consent for an application.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Attribute dropDown required
>
>   Select the attribute you want to use to locate a user.
>
>   * User ID
>
>   * Username
>
>   * Email
>
> - User Identifier textField required
>
>   Enter the user ID, username, or email address of the user you want to locate.
>
> - Consent Attribute dropDown required
>
>   Enter the consent ID, application ID, or application name of the consent record you want to locate.
>
>   * Consent ID
>
>   * Application ID
>
>   * Application Name
>
> - Consent Identifier textField required
>
>   A unique identifier for the consent record.
>
> * default object
>
>   * properties object
>
>     * matchUserAttribute string required
>
>       PingOne user attribute to identify a user with.
>
>     * userIdentifier string required
>
>       User attribute to match user.
>
>     * matchConsentAttribute string required
>
>       PingOne consent attribute to identify an consent with.
>
>     * consentIdentifier string required
>
>       Consent attribute to match consent.
>
> - output object
>
>   * application object
>
>     * id string
>
>     * name string
>
>     * type string
>
>   * consentId string
>
>   * consentStatus string
>
>   * consentScopes array
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Get User Consent

This capability facilitates application consent by checking, prompting, and recording user decisions regarding consent. This action includes the HTML template and other resources like CSS. You can customize them under the Custom Screens tab.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Always Prompt for Consent toggleSwitch required
>
>   Indicates whether the user will always be prompted to consent to the application's request. If disabled, users will only be prompted to consent to these requests if they have not already done so.
>
> - User Attribute dropDown required
>
>   Select the attribute you want to use to locate a user.
>
>   * User ID
>
>   * Username
>
>   * Email
>
> - User Identifier textField required
>
>   Enter the user ID, username, or email address of the user you want to locate.
>
> - Application Attribute dropDown required
>
>   Select the application or specify an application identifier that will be used to check, prompt and store consent for the user.
>
>   * Application ID
>
>   * Application Name
>
> - Application Identifier textField required
>
>   Enter the unique identifier of the application that will be used to check, prompt and store consent for the user.
>
> - Application Name textField required
>
>   Enter the name of the application that will be used to check, prompt and store consent for the user.
>
> - Scopes textField required
>
>   Scopes define the user information that the application wants to access and the user will need to consent to allowing, such as the user's name, email address, and phone number. You must provide at least one scope. You may provide multiple scopes, each separated by a space.
>
> - Scopes textField
>
>   Enter the space-separated list of scopes that have been requested. These scopes are validated against the allowed scopes assigned to the PingOne application.
>
> - Scopes textField
>
>   Enter the space-separated list of scopes that have been requested. These scopes are validated against the allowed scopes assigned to the PingOne application.
>
> - appConsentHtmlConfig
>
> * default object
>
>   * parameters object
>
> - output object
>
>   * matchedUser object
>
>   * application object
>
>     * id string
>
>     * name string
>
>     * type string
>
>   * consentId string
>
>   * consentStatus string
>
>   * consentScopes array
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object