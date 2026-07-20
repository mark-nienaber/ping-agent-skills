---
description: The API requires a JWT Bearer token for authenticating requests. This token can be retrieved using either an authorization code flow or a client credentials flow.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_api_config
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_api_config.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configuring-access-to-the-administrative-api: Configuring access to the administrative API
  _auth_code_flow: Authenticate using an authorization code flow
  assign_roles: Assigning users the appropriate roles
  steps: Steps
  signon_app: Signing on to an application to get an access token
  steps-2: Steps
  use_token: Using the token to authenticate
  steps-3: Steps
  _client_cred_flow: Authenticate using a client credentials flow
  creating-an-oidc-application: Creating an OIDC application
  steps-4: Steps
  generating-a-token: Generating a token
  steps-5: Steps
  restrict_access: Restricting access to the application
  steps-6: Steps
---

## Configuring access to the administrative API

The API requires a JWT Bearer token for authenticating requests. This token can be retrieved using either an authorization code flow or a client credentials flow.

### Authenticate using an authorization code flow

The API supports the authorization code flow, which gets access tokens by securely redirecting users to the authorization server for authentication.

To set this up, you'll need to:

1. Ensure users are [assigned the appropriate PingOne Advanced Services user access control roles](p1as_platform_admin_api.html#assign_roles).

2. [Sign on to an application to get an access token](p1as_platform_admin_api.html#signon_app).

3. [Use the token to authenticate](p1as_platform_admin_api.html#use_token) and access the API using Swagger UI, or command-line tools, such as Postman or cURL.

#### Assigning users the appropriate roles

If you're using the PingOne platform:

#### Steps

1. In the user profile, add a custom attribute. Learn more about adding these attributes in [Add custom attributes to a user](https://docs.pingidentity.com/pingone/pingone_tutorials/p1_add_custom_attributes_to_a_user.html) in the PingOne documentation.

2. Select the appropriate PingOne Advanced Services roles for the user and click **Save**. You can find a complete list of available roles in [User access control roles](p1as_platform_mng_admins.html#p1as_admin_role_mappings).

If you're using the CAP, Ping Identity manages the roles and permissions your administrators are assigned. Submit an [Elevate Admin](p1as_pf_elevate_admin.html) service request and specify which roles and permissions users should have.

#### Signing on to an application to get an access token

To get a token:

#### Steps

1. Go to the PingOne Advanced Services login URL:

   https\://self-service-api.\<environment>-\<customer>.\<region>.ping.cloud/api/v1/auth/login/\<application>

   Valid values for the application are "self-service", "pingaccess", "pingfederate", "opensearch", and "argocd".

2. Enter your credentials and click **Submit**.

   If authentication is successful, you're redirected to the **Success** page and a **Copy Token** button displays.

3. Click **Copy Token** to copy the token to your clipboard.

#### Using the token to authenticate

If you're using the API interactive documentation:

#### Steps

1. Go to the respective API docs URL.

2. Click **Authorize**.

3. Paste the token into the input field and click **Authorize** and then **Close**.

   All requests made from the interactive documentation will be authenticated.

If you're using command-line tools, such as Postman or cURL, query the API directly and include the bearer token in the headers.

For example, `{"Authorization": "Bearer <TOKEN>"}`

You can also use the interactive documentation to explore the API endpoints, view documentation for the API, and experiment with API calls. You can make API calls from an interactive user interface, custom applications, or from command-line tools. Learn more about this interactive documentation in [Using the API interactive documentation](p1as_platform_interactive_api.html).

### Authenticate using a client credentials flow

This API also supports the client credentials flow, which is designed for machine-to-machine (M2M) interactions, where an application needs to access resources without involving a user.

|   |                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This type of flow can only be used if your PingOne environment is connected to your PingOne Advanced Services environment and both are correctly configured. Learn more about setting up this connection in [Using the PingOne platform](p1as_platform_mng_admins.html#_using_pingone). |

To set this up, you'll need to:

1. Create an OIDC application.

2. Generate a token.

To ensure that only administrators can generate access tokens, restrict access to the application that you created. Learn more about this process in [Restricting access to the application](p1as_platform_admin_api.html#restrict_access).

#### Creating an OIDC application

Start by creating an OpenID Connect (OIDC) application in PingOne.

#### Steps

1. Go to **Applications** > **Resources**.

2. Click the **[icon: plus, set=fa]**icon.

3. Create the resource by completing these fields:

   * **Resource name**: A unique identifier for the resource.

   * **Description** (optional): A brief characterization of the resource that helps identify it.

4. Click **Next**.

5. On the **Attributes** page, click **Add** to add a new attribute.

6. Create an attribute labeled `name`.

   Click the **Gear** icon to open the expression builder and enter a hardcoded name, such as `OrchestrationTool`. This is the name that will display with the tokens in the application logs. Learn more in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.

7. Create an attribute labeled `groups`.

   Click the **Gear** icon to open the expression builder and enter the appropriate user access control roles. Set the values to a hardcoded list of valid roles. For example, {"dev-tls-admin", "prod-tls-audit"}. Learn more about these roles and permissions in [User access control roles](p1as_platform_mng_admins.html#p1as_admin_role_mappings).

   |   |                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The PingOne Advanced Services attributes must be set up for them to display in the list. Learn more about adding this attribute in [Creating custom user attributes](p1as_platform_mng_admins.html#p1as_custom_attributes). |

8. Click **Next**.

9. On the **Scopes** page, add a new scope to map the role to the new application. Click **Add Scope** and complete the following fields:

   * **Scope name**: A unique identifier for the scope.

   * **Description** (optional): A brief description of the scope that helps identify it.

10. Click **Save**.

11. Now, add the OIDC application. Go to **Applications > Applications**.

12. Click the **[icon: plus, set=fa]**icon.

13. Complete the following fields:

    * **Application name**: A unique identifier for the application.

    * **Description** (optional): A brief characterization of the application that helps identify it.

    * **Icon** (optional): A graphic representation of the application. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

14. In the list of available application types, select **OIDC Web App**. Click **Save**.

15. On the **Configuration** tab, click the **Pencil** icon to edit the configuration.

    * Change the **Response Type** to none by clearing all the options.

    * Change the **Grant Type** to **Client Credentials**.

16. Click **Save**.

17. On the **Resources** tab, click the **Pencil** icon to add the scope you added in step 8 to the application.

18. Click **Save** and click the toggle at the top of the details panel to enable the application.

#### Generating a token

Access the new application in the PingOne admin console to generate an access token.

#### Steps

1. Follow the steps outlined in [Getting an access token](https://docs.pingidentity.com/pingone/applications/p1_getaccesstoken.html) in the PingOne documentation.

2. Include the bearer token in the headers.

   For example, `{"Authorization": "Bearer <TOKEN>"}`

You can also use the interactive documentation to explore the API endpoints, view documentation for the API, and experiment with API calls. You can make API calls from an interactive user interface, custom applications, or from command-line tools. Learn more about this interactive documentation in [Using the API interactive documentation](p1as_platform_interactive_api.html).

#### Restricting access to the application

To ensure that only administrators can generate access tokens, restrict access to the application that you created.

#### Steps

1. Select the application, click the **Access** tab, and then the **Pencil** icon.

2. Select the **Admin Only Access** checkbox and click **Save**.

---

---
description: The API includes interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls. Built on Swagger UI, this interactive tool makes it easy for you to visualize, interact with, and test the APIs within a browser.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_api_doc
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_api_doc.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  using-the-api-interactive-documentation: Using the API interactive documentation
---

## Using the API interactive documentation

The API includes interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls. Built on Swagger UI, this interactive tool makes it easy for you to visualize, interact with, and test the APIs within a browser.

You can make API calls from an interactive user interface, custom applications, or from command line tools such as cURL.

To access the administrative API documentation:

1. Start a web browser.

2. Browse to the URL:

   ```
   https://self-service-api.<environment>-<customer>.<region>.ping.cloud/docs
   ```

   |   |                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------- |
   |   | The API is also documented in the OpenAPI Specification, previously known as the Swagger Specification. Go to: |

   ```
   https://self-service-api.<environment>-<customer>.<region>.ping.cloud/api/v1/openapi.json
   ```

To test an administrative API:

1. Select a section of the administrative API you would like to explore. For example, **/hostnames**.

2. Expand the method you want to use. For example, **GET /hostnames**.

3. Enter required parameters, if any. For more information, see **Schema Models** under the selected API endpoint.

4. Click **Try it out**.

   |   |                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You will be prompted to sign on using an access token for OAuth authentication. The role assigned to the respective administrative accounts affects the access to the requested API. |

   If the request completes successfully, the administrative API returns the **Request URL**, the **Response Body**, the **Response Code**, and the **Response Headers**.

---

---
description: The API supports the authorization code flow, which gets access tokens by securely redirecting users to the authorization server for authentication.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_auth_flow
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_auth_flow.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  authenticate-using-an-authorization-code-flow: Authenticate using an authorization code flow
  before-you-begin: Before you begin
  steps: Steps
  example: Example
---

### Authenticate using an authorization code flow

The API supports the authorization code flow, which gets access tokens by securely redirecting users to the authorization server for authentication.

#### Before you begin

After user accounts are created, you can assign the appropriate user access control roles and permissions. Users can then get an access token to use with API calls. Learn more about these roles and permissions in [User access control roles](p1as_platform_mng_admins.html#p1as_admin_role_mappings).

#### Steps

1. Go to the PingOne Advanced Services login URL:

   https\://self-service-api.\<environment>-\<customer>.\<region>.ping.cloud/api/v1/login/pingaccess

2. Enter your credentials and click **Submit**.

   If authentication is successful, you're redirected to the **Success** page and a **Copy Token** button displays.

3. Click **Copy Token**.

4. Query the API directly using tools such as Postman or cURL, and include the bearer token in the headers.

   #### Example

   ```
   {"Authorization": "Bearer {TOKEN}"}
   ```

---

---
description: The API includes interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls. Built on Swagger UI, this interactive tool makes it easy for you to visualize, interact with, and test the APIs within a browser.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_interactive_api
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_interactive_api.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  using-the-api-interactive-documentation: Using the API interactive documentation
  before-you-begin: Before you begin
  steps: Steps
  steps-2: Steps
---

## Using the API interactive documentation

The API includes interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls. Built on Swagger UI, this interactive tool makes it easy for you to visualize, interact with, and test the APIs within a browser.

You can make API calls from an interactive user interface, custom applications, or from command line tools such as cURL.

### Before you begin

Ensure you have access to the administrative API. Learn more in [Accessing the admin console and administrative API](p1as_platform_admin_api.html).

To access the administrative API documentation:

### Steps

1. Start a web browser.

2. Go to the URL:

   https\://self-service-api.\<environment>-\<customer>.\<region>.ping.cloud/docs

   |   |                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The API is also documented in the OpenAPI Specification, previously known as the Swagger Specification. Go to: https\://self-service-api.\<environment>-\<customer>.\<region>.ping.cloud/api/v1/openapi.json. |

To test an administrative API:

### Steps

1. Select a section of the administrative API you would like to explore. For example, **/hostnames**.

2. Expand the method you want to use. For example, **GET /hostnames**.

3. Enter required parameters, if any. For more information, see **Schema Models** under the selected API endpoint.

4. Click **Try it out**.

   |   |                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You will be prompted to sign on using an access token for OAuth authentication. The role assigned to the respective administrative accounts affects the access to the requested API. |

   If the request completes successfully, the administrative API returns the **Request URL**, the **Response Body**, the **Response Code**, and the **Response Headers**.

---

---
title: Accessing the PingOne Advanced Services admin console and administrative API
description: Introductory information about the PingOne Advanced Services administrative API and instructions on configuring access to it.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_admin_api
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_admin_api.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 29, 2026
section_ids:
  _admin_console: Accessing the admin console
  steps: Steps
  _platform_api_config: Configuring access to the administrative API
  _auth_code_flow: Authenticate using an authorization code flow
  assign_roles: Assigning users the appropriate roles
  steps-2: Steps
  signon_app: Signing on to an application to get an access token
  steps-3: Steps
  use_token: Using the token to authenticate
  steps-4: Steps
  _client_cred_flow: Authenticate using a client credentials flow
  creating-an-oidc-application: Creating an OIDC application
  steps-5: Steps
  generating-a-token: Generating a token
  steps-6: Steps
  restrict_access: Restricting access to the application
  steps-7: Steps
  interactive_api: Using the API interactive documentation
  before-you-begin: Before you begin
  steps-8: Steps
  steps-9: Steps
---

# Accessing the PingOne Advanced Services admin console and administrative API

You can use the PingOne Advanced Services admin console or a REST-based API to perform many tasks yourself instead of submitting a service request.

For example, you can create and update virtual hosts yourself through the admin console or the administrative API. Learn more about virtual hosts in [Creating and updating virtual hosts](p1as_platform_virtual_hosts.html).

|   |                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must be using the appropriate platform version to access the admin console and administrative API. The administrative API functionality was introduced in platform version 2.0.0, which was released in December 2024, and the administrative console was introduced in platform version 2.2.0, which was released in March 2026. |

To access the admin console:

* Ensure that you have the appropriate roles assigned. Learn more about the roles available in [User access control roles](p1as_platform_mng_admins.html#p1as_admin_role_mappings). Learn how to assign these roles in [Assigning users the appropriate roles](#assign_roles)

* Take these steps to [access the admin console](#_admin_console).

To access the administrative API:

* Ensure that you have the appropriate roles assigned. Learn more about the roles available in [User access control roles](p1as_platform_mng_admins.html#p1as_admin_role_mappings). Learn how to assign these roles in [Assigning users the appropriate roles](#assign_roles)

* Take these steps to [configure access to the API](#_platform_api_config).

|   |                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All administrative API events are logged. These logs include information about each event, the date and time it occurred, and information that identifies the users involved. Learn more about event logs in [Monitoring and logging](../monitoring_and_logging/p1as_monitoring_logging.html). |

## Accessing the admin console

To complete platform self-service tasks, access the admin console.

### Steps

1. Go to the following URL:

   https\://self-service.`<customer>`.`<region>`.ping.cloud

2. When prompted, enter your username and password.

   The admin console displays.

3. The toolbar at the top of the page indicates which environment is selected. Ensure you're working in the right environment by selecting it in the list.

4. Note the following:

   * The **Self-service** section of the sidebar helps you navigate between self-service tasks.

     ![An image of the self-service menu, which displays in the sidebar.](_images/UIMenu.png)

   * Each page contains resource icons that indicate status:

     * Blue indicates creating

     * Green indicates complete

     * Yellow indicates updating

     * Red indicates an error

## Configuring access to the administrative API

The API requires a JWT Bearer token for authenticating requests. This token can be retrieved using either an authorization code flow or a client credentials flow.

### Authenticate using an authorization code flow

The API supports the authorization code flow, which gets access tokens by securely redirecting users to the authorization server for authentication.

To set this up, you'll need to:

1. Ensure users are [assigned the appropriate PingOne Advanced Services user access control roles](#assign_roles).

2. [Sign on to an application to get an access token](#signon_app).

3. [Use the token to authenticate](#use_token) and access the API using Swagger UI, or command-line tools, such as Postman or cURL.

#### Assigning users the appropriate roles

If you're using the PingOne platform:

#### Steps

1. In the user profile, add a custom attribute. Learn more about adding these attributes in [Add custom attributes to a user](https://docs.pingidentity.com/pingone/pingone_tutorials/p1_add_custom_attributes_to_a_user.html) in the PingOne documentation.

2. Select the appropriate PingOne Advanced Services roles for the user and click **Save**. You can find a complete list of available roles in [User access control roles](p1as_platform_mng_admins.html#p1as_admin_role_mappings).

If you're using the CAP, Ping Identity manages the roles and permissions your administrators are assigned. Submit an [Elevate Admin](p1as_pf_elevate_admin.html) service request and specify which roles and permissions users should have.

#### Signing on to an application to get an access token

To get a token:

#### Steps

1. Go to the PingOne Advanced Services login URL:

   https\://self-service-api.\<environment>-\<customer>.\<region>.ping.cloud/api/v1/auth/login/\<application>

   Valid values for the application are "self-service", "pingaccess", "pingfederate", "opensearch", and "argocd".

2. Enter your credentials and click **Submit**.

   If authentication is successful, you're redirected to the **Success** page and a **Copy Token** button displays.

3. Click **Copy Token** to copy the token to your clipboard.

#### Using the token to authenticate

If you're using the API interactive documentation:

#### Steps

1. Go to the respective API docs URL.

2. Click **Authorize**.

3. Paste the token into the input field and click **Authorize** and then **Close**.

   All requests made from the interactive documentation will be authenticated.

If you're using command-line tools, such as Postman or cURL, query the API directly and include the bearer token in the headers.

For example, `{"Authorization": "Bearer <TOKEN>"}`

You can also use the interactive documentation to explore the API endpoints, view documentation for the API, and experiment with API calls. You can make API calls from an interactive user interface, custom applications, or from command-line tools. Learn more about this interactive documentation in [Using the API interactive documentation](p1as_platform_interactive_api.html).

### Authenticate using a client credentials flow

This API also supports the client credentials flow, which is designed for machine-to-machine (M2M) interactions, where an application needs to access resources without involving a user.

|   |                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This type of flow can only be used if your PingOne environment is connected to your PingOne Advanced Services environment and both are correctly configured. Learn more about setting up this connection in [Using the PingOne platform](p1as_platform_mng_admins.html#_using_pingone). |

To set this up, you'll need to:

1. Create an OIDC application.

2. Generate a token.

To ensure that only administrators can generate access tokens, restrict access to the application that you created. Learn more about this process in [Restricting access to the application](#restrict_access).

#### Creating an OIDC application

Start by creating an OpenID Connect (OIDC) application in PingOne.

#### Steps

1. Go to **Applications** > **Resources**.

2. Click the **[icon: plus, set=fa]**icon.

3. Create the resource by completing these fields:

   * **Resource name**: A unique identifier for the resource.

   * **Description** (optional): A brief characterization of the resource that helps identify it.

4. Click **Next**.

5. On the **Attributes** page, click **Add** to add a new attribute.

6. Create an attribute labeled `name`.

   Click the **Gear** icon to open the expression builder and enter a hardcoded name, such as `OrchestrationTool`. This is the name that will display with the tokens in the application logs. Learn more in [Using the expression builder](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_use_expression_builder.html) in the PingOne documentation.

7. Create an attribute labeled `groups`.

   Click the **Gear** icon to open the expression builder and enter the appropriate user access control roles. Set the values to a hardcoded list of valid roles. For example, {"dev-tls-admin", "prod-tls-audit"}. Learn more about these roles and permissions in [User access control roles](p1as_platform_mng_admins.html#p1as_admin_role_mappings).

   |   |                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The PingOne Advanced Services attributes must be set up for them to display in the list. Learn more about adding this attribute in [Creating custom user attributes](p1as_platform_mng_admins.html#p1as_custom_attributes). |

8. Click **Next**.

9. On the **Scopes** page, add a new scope to map the role to the new application. Click **Add Scope** and complete the following fields:

   * **Scope name**: A unique identifier for the scope.

   * **Description** (optional): A brief description of the scope that helps identify it.

10. Click **Save**.

11. Now, add the OIDC application. Go to **Applications > Applications**.

12. Click the **[icon: plus, set=fa]**icon.

13. Complete the following fields:

    * **Application name**: A unique identifier for the application.

    * **Description** (optional): A brief characterization of the application that helps identify it.

    * **Icon** (optional): A graphic representation of the application. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

14. In the list of available application types, select **OIDC Web App**. Click **Save**.

15. On the **Configuration** tab, click the **Pencil** icon to edit the configuration.

    * Change the **Response Type** to none by clearing all the options.

    * Change the **Grant Type** to **Client Credentials**.

16. Click **Save**.

17. On the **Resources** tab, click the **Pencil** icon to add the scope you added in step 8 to the application.

18. Click **Save** and click the toggle at the top of the details panel to enable the application.

#### Generating a token

Access the new application in the PingOne admin console to generate an access token.

#### Steps

1. Follow the steps outlined in [Getting an access token](https://docs.pingidentity.com/pingone/applications/p1_getaccesstoken.html) in the PingOne documentation.

2. Include the bearer token in the headers.

   For example, `{"Authorization": "Bearer <TOKEN>"}`

You can also use the interactive documentation to explore the API endpoints, view documentation for the API, and experiment with API calls. You can make API calls from an interactive user interface, custom applications, or from command-line tools. Learn more about this interactive documentation in [Using the API interactive documentation](p1as_platform_interactive_api.html).

#### Restricting access to the application

To ensure that only administrators can generate access tokens, restrict access to the application that you created.

#### Steps

1. Select the application, click the **Access** tab, and then the **Pencil** icon.

2. Select the **Admin Only Access** checkbox and click **Save**.

## Using the API interactive documentation

The API includes interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls. Built on Swagger UI, this interactive tool makes it easy for you to visualize, interact with, and test the APIs within a browser.

You can make API calls from an interactive user interface, custom applications, or from command line tools such as cURL.

### Before you begin

Ensure you have access to the administrative API. Learn more in [Accessing the admin console and administrative API](#).

To access the administrative API documentation:

### Steps

1. Start a web browser.

2. Go to the URL:

   https\://self-service-api.\<environment>-\<customer>.\<region>.ping.cloud/docs

   |   |                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The API is also documented in the OpenAPI Specification, previously known as the Swagger Specification. Go to: https\://self-service-api.\<environment>-\<customer>.\<region>.ping.cloud/api/v1/openapi.json. |

To test an administrative API:

### Steps

1. Select a section of the administrative API you would like to explore. For example, **/hostnames**.

2. Expand the method you want to use. For example, **GET /hostnames**.

3. Enter required parameters, if any. For more information, see **Schema Models** under the selected API endpoint.

4. Click **Try it out**.

   |   |                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You will be prompted to sign on using an access token for OAuth authentication. The role assigned to the respective administrative accounts affects the access to the requested API. |

   If the request completes successfully, the administrative API returns the **Request URL**, the **Response Body**, the **Response Code**, and the **Response Headers**.

---

---
title: ACIs
description: Instructions for completing the service request form to add, modify, or remove PingDirectory ACIs.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_pd_acis
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_pd_acis.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# ACIs

To add, modify, or remove access control instructions (ACIs), submit a request through the service request form, accessible from the [Support Portal](https://support.pingidentity.com/s/).

## About this task

Global ACIs are a set of ACIs that can apply to entries anywhere in the server, but they can also be scoped so that they only apply to a specific set of entries. These ACIs work in conjunction with access control rules stored in user data and provide a convenient way to define ACIs that span disparate portions of the DIT (Directory Information Tree).

You can apply Global ACIs to administrator access, anonymous and authenticated access, delegated access to a manager or for proxy authorization. The following table includes access control components, descriptions, and the syntax used for each component.

| Access Control Components | Description                                                                                                           | Syntax                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| targets                   | This component specifies the set of entries or attributes that the access control rule applies to.                    | Syntax: `(target keyword = \|\| != expression)`                                                                 |
| name                      | This component specifies the name of the ACI.                                                                         |                                                                                                                 |
| permissions               | This component specifies the type of operations to which an access control rule might apply.                          | Syntax: `allow\|\|deny (permission)`                                                                            |
| bind rules                | This component specifies the criteria that indicate whether an access control rule should apply to a given requester. | Syntax: `bind rule keyword = \|\|!= expression;`The bind rule syntax requires that it be terminated with a ";". |

You can find more information about ACIs in [Defining global ACIs](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_security_guide/pd_sec_define_global_acis.html) in the PingDirectory documentation.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingDirectory service request** > **ACIs**.

3. If you want to use an ACI that you constructed, select the **Do you have ACI already?** option.

4. In the **Base DN that ACI applies to** field, select the parent Base DN that the ACI should apply to. Note that this ACI will apply to all subtrees below this Base DN.

5. In the **Attributes(s) to apply to (comma separated)** field, provide a comma-separated list of attributes that should be allowed or denied by this ACI.

6. In the **DN of user or group** field, provide the User DN or Group DN that the ACI will apply to, which will determine who is allowed or denied access.

7. In the **Is the target a user or group?** field, indicate whether the target is a user or a group based on the DN provided in the previous step.

8. In the **Does this ACI allow or deny access?** field, indicate whether the ACI should allow access to users with the selected attribute or deny access.

9. In the **Permissions** field, select the permissions you want to grant or deny to the target users or groups.

10. If you have a complete ACI, paste it into the **Advanced (supply a raw ACI)** field.

11. In the **Business Priority** list, select the appropriate description:

    * Change needed by deadline to avoid business impact

    * Change modifies existing functionality

    * Change adds new functionality

12. In the **Description** field, provide a description of the request.

13. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

14. To submit your request, click **Save**.

---

---
title: Administrator MFA
description: Instructions for completing the service request form to manage administrator MFA.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_admin_mfa
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_admin_mfa.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 21, 2022
section_ids:
  steps: Steps
---

# Administrator MFA

To manage customer administrator multi-factor authentication (MFA), submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **Platform service requests** > **Administrator MFA**.

3. In the**Administrator(s)** field, enter the administrator name.

4. In the **Desired MFA setting** field, indicate whether you want to enable or disable MFA.

5. In the **MFA contact method** field, indicate whether the MFA contact method will be email or phone number.

6. In the **MFA contact info** field, provide the MFA information (email address or phone number).

7. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

8. In the **Description** field, enter a description of your request.

9. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

10. To submit your request, click **Save**.

---

---
title: Approve merge request
description: Instructions for completing the service request form to approve merge requests.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_approve_merge_request
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_approve_merge_request.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
---

# Approve merge request

To approve a merge request, submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **Platform service requests** > **Approve merge request**.

3. In the **Merge request URL** field, provide the URL for the request.

4. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. In the **Description** field, enter a description of your request.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. To submit your request, click **Save**.

---

---
title: Creating and updating product configurations
description: Instructions for creating and updating product configurations and rolling configurations back to previous versions.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_product_config
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_product_config.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configuring-product-configurations: Configuring product configurations
  steps: Steps
  updating-product-configurations: Updating product configurations
  steps-2: Steps
  rollback-product-configurations: Rollback product configurations
  steps-3: Steps
---

# Creating and updating product configurations

You and your administrators can create and update some supported product configurations yourselves using the PingOne Advanced Services admin console or administrative API. Learn more about using the API in [Accessing the PingOne Advanced Services admin console and administrative API](p1as_platform_admin_api.html)

Supported configurations currently include [PingFederate HTML templates](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_custom_user_facing_pages.html), which are used to customize your user-facing pages, and [language packs](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_local_message_end_users.html), which are used to localize messages for your users.

|   |                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To use this functionality, you must be using platform version 2.2.0 or later with the PingFederate 2.2.1 update. If you are upgrading from an earlier version and your configurations were managed using GitOps orchestration, know that we will migrate your configurations to self-service during the upgrade process. |

Keep the following in mind:

* After you create or update a configuration, it will take some time for the changes to become available.

* When you upgrade to another version, files you've customized won't be overwritten with the default files that come with the upgrade. Consequently, we recommend reviewing your customizations and comparing them to the upgrade defaults to determine which version you'd prefer to use. To ensure future upgrades go smoothly, we also recommend keeping customizations to a minimum.

* Configurations are automatically replicated to child regions in PingOne Advanced Services.

* Only the last 20 configuration uploads are available for rollback.

* The **Resetting to Default** option resets PingOne Advanced Services back to its out-of-the-box defaults and removes all version history.

## Configuring product configurations

To create new configurations, complete these steps:

### Steps

1. Access the **Product Configurations** page by selecting it from the navigation.

2. Select the appropriate configuration type line item and click **Configure**.

3. Select the `.zip` file that contains all the customized files for the configuration.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The files within the `.zip` file will be extracted and sent directly into the appropriate configuration directory on the servers, while maintaining the file's internal structure. Consequently, there's no need for you to include the root directory in this file.Ensure that this file contains all of your customized files, and not just the most recent changes to the previous upload, because your configurations won't merge with existing files. Instead, they replace them entirely. |

4. When finished, click **Save**.

## Updating product configurations

To update existing configurations, complete these steps:

### Steps

1. Access the **Product Configurations** page by selecting it from the navigation.

2. Select the appropriate configuration type line item, and then click **Deployed** under **Download Configuration** to download the current version that contains all of your files.

3. Make your updates in the downloaded file.

   |   |                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * If you no longer want to customize a file, remove it from the downloaded file.

   * You can get the product default files by downloading the software distributions from `pingidentity.com`. |

4. Click the **Pencil** icon and select the `.zip` file you just updated.

   |   |                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Ensure that this file contains all of your customized files, and not just the most recent changes to the previous upload, because your configurations won't merge with existing files. Instead, they replace them entirely. |

5. When finished, click **Save**.

## Rollback product configurations

To rollback product configurations to previous versions, complete these steps:

### Steps

1. Access the **Product Configurations** page by selecting it from the navigation.

2. Select the appropriate configuration type line item.

3. Select the **Versions** tab and the **More options** icon, and then select **Download** next to the appropriate version to download it.

4. Review the `.zip` file to ensure it contains everything needed for the configuration.

   When you're ready, return to the console, select the **More options** icon, and click **Rollback**.

5. Select the acknowledgment checkbox, then click **Rollback** when prompted.

   Your product configuration is returned to the previous version.

---

---
title: Creating and updating virtual hosts
description: You and your administrators can create and update virtual host certificates and TLS configurations yourselves.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_virtual_hosts
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_virtual_hosts.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 26, 2026
section_ids:
  before-you-begin: Before you begin
  _create_tls: Creating TLS certificates
  steps: Steps
  _updating_tls: Updating TLS certificates
  steps-2: Steps
  _create_virtual_hosts: Creating virtual hosts
  steps-3: Steps
  _updating_virtual_hosts: Updating virtual hosts
  steps-4: Steps
  troubleshooting: Troubleshooting
---

# Creating and updating virtual hosts

You and your administrators can create and update virtual host certificates and TLS configurations yourselves.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Platform version 2.0.0, released in December 2024, contained enhancements that made this functionality possible. To use it, we'll need to migrate these certificates and configurations from GitOps orchestration to the API.- If you're using platform version 1.19.2.0 or earlier, a Ping Identity representative will reach out to you to complete this migration.

- If you're using platform 2.0.0 or later, you can request this migration at any time by submitting a [service request](p1as_service_requests.html). |

Keep the following in mind:

* After you create or update a configuration, it will take some time for the virtual host to become available.

* Virtual host configurations are automatically replicated to child regions in PingOne Advanced Services.

* It is up to the user to keep track of the certificate's fullchain and private key because neither the admin console nor API will return that information.

* Configurations can only be rolled back once. Then, the configuration needs to be updated at least once before a rollback can be performed again.

Limitations include:

* You cannot currently create or update the following items yourself. Submit a service request instead.

  * MTLS configurations.

  * Configurations that need custom annotations, such as annotations of Cross-Origin Resource Sharing (CORS) responses.

  * Private Ingress configurations.

  * EC or ECC TLS certificates.

* Virtual hosts cannot be created for the PingFederate Admin UI or the PingAccess Admin UI in PingOne Advanced Services.

### Before you begin

Ensure you have access to either the admin console or the administrative API. Learn more in [Accessing the admin console and administrative API](p1as_platform_admin_api.html).

These instructions explain how to create and update virtual hosts using the admin console. Learn more about using the API in [Using the API interactive documentation](p1as_platform_admin_api.html#interactive_api).

* [Creating TLS certificates](#_create_tls)

* [Updating TLS certificates](#_updating_tls)

* [Creating virtual hosts](#_create_virtual_hosts)

* [Updating virtual hosts](#_updating_virtual_hosts)

## Creating TLS certificates

TLS certificates are required to run virtual hosts. To create TLS certificates:

### Steps

1. In the PingOne Advanced Services admin console, go to **Self-service** > **Secrets**.

2. Click the **[icon: plus, set=fa]**icon.

3. Complete the following fields:

   * **Secret Type**: Enter `TLS`.

   * **Secret Name**: A meaningful name for the certificate.

   * **Fullchain**: Contents of the certificate file.

   * **Private Key**: Contents of the key file.

4. For the fullchain, certificates should be concatenated in this order:

   ```
   -----BEGIN CERTIFICATE-----
   <Leaf certificate>
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   <Intermediate certificate 1>
   -----END CERTIFICATE-----
   -----BEGIN CERTIFICATE-----
   <Intermediate certificate 2>
   -----END CERTIFICATE-----
   ```

   * The leaf certificate must be first.

   * Followed by all non-root intermediate certificates.

     |   |                                                                                                                                                                                                                  |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Most TLS clients perform PKIX path building and require the full chain (excluding root). If intermediate certificates are not provided, clients will fail certificate validation even if the root CA is trusted. |

   * The root certificate is typically optional and should not be required.

5. Click **Save**.

## Updating TLS certificates

To update TLS certificates:

### Steps

1. In the PingOne Advanced Services admin console, go to **Self-service** > **Secrets**.

2. Click the **More Options** icon and select **Edit**.

3. Update the following fields:

   * **Fullchain**: Contents of the certificate file.

   * **Private Key**: Contents of the key file.

4. Click **Save**.

## Creating virtual hosts

To create virtual hosts, complete the following steps. You'll need to provide the name of the TLS certificate you previously created. Learn more in [Creating TLS certificates](#_create_tls).

### Steps

1. In the PingOne Advanced Services admin console, select **Self-service** > **Virtual hosts**.

2. Click the **[icon: plus, set=fa]**icon.

3. Complete the following fields:

   * **Hostname**: Enter the Fully Qualified Domain Name (FQDN).

   * **Product Mapping**: The PingOne Advanced Services product that you want to map the virtual host to.

   * **Certificate name**: The name of the TLS certificate to be used with the virtual host address.

4. Click **Save**.

## Updating virtual hosts

To update virtual hosts:

### Steps

1. In the PingOne Advanced Services admin console, go to **Self-service** > **Virtual hosts**.

2. Click the **More Options** icon, and select **Edit**.

3. Select the TLS certificate that you want to update from the list and update it.

4. Click **Save**.

## Troubleshooting

If you're having trouble:

* Review the certificate chain structure:

  ```
  openssl verify -untrusted intermediate.pem leaf.pem
  ```

* Display full certificate details (verify the expiration date and SANs):

  ```
  openssl x509 -text -noout -in leaf.pem
  ```

* Ensure that the private key matches the certificate:

  ```
  openssl x509 -noout -modulus -in leaf.pem | openssl md5
  openssl rsa  -noout -modulus -in key.pem  | openssl md5
  ```

---

---
title: Elevate admin
description: Instructions for completing the service request form to modify permissions for your administrators.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_pf_elevate_admin
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_pf_elevate_admin.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Elevate admin

To modify the permissions your administrators have, such as managing certificates or users, submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingFederate service requests** > **Elevate admins**.

3. In the **Admin Permissions to Add** field, select all the permissions that you want your administrators to have.

   |   |                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------- |
   |   | If you want administrators to be granted different permissions, submit separate requests for each. |

4. In the **Admins to change** field, provide the names of the administrators who you want to be granted the requested permissions.

5. In the **Description** field, enter a description of your request.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. To submit your request, click **Save**.

---

---
title: Email templates
description: Instructions for completing the service request form to modify email templates.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_pd_email_templates
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_pd_email_templates.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Email templates

To modify email templates, submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## About this task

You can use PingDirectory email templates in a variety of ways. An example email template is provided in the **Delegated Admin** package at the top level in the `delegated-admin-account-created.template` file. This template provides a multipart text and HTML email to the user with their username and initial password, along with a self-service link they can use to sign on to PingFederate and change their password and profile information.

You can find more information in [Editing and copying the email template to PingDirectory server](https://docs.pingidentity.com/pingdirectory/latest/delegated_admin_application_guide/pd_da_set_up_email_invites_new_user.html#editing-and-copying-the-email-template-to-the-pingdirectory-server) in the PingDirectory documentation.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingDirectory service requests** > **Email templates**.

3. In the **Specify email handler type** field, specify whether a standard email notification handler or a multipart email status notification handler will be used.

4. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. In the **Description** field, enter a description of your request.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save**.

8. Click the **Attachments** tab and upload a `.zip` file that contains all files in the template directory you are updating.

   |   |                                                                                     |
   | - | ----------------------------------------------------------------------------------- |
   |   | If necessary, request the latest instance of these files before making your update. |

---

---
title: Enable debug logger
description: Instructions for completing the service request form to enable the standard debug logger or request a non-standard debug level.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_pa_logging_settings
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_pa_logging_settings.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Enable debug logger

PingAccess generates logs that record server events. To enable the standard debug logger or request a non-standard debug level, submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingAccess service requests > Enable Debug Logger**.

3. Select the **Standard Debug?** field to configure the log level to `DEBUG`. Learn more in [Configuring log levels](https://docs.pingidentity.com/pingaccess/latest/configuring_and_customizing_pingaccess/pa_configuring_log_levels.html) in the PingAccess documentation.

4. If you're requesting a non-standard debug level, specify the targets that you want configured from the `log4j2.xml` file in the **Debug Targets** fields.

   Then, specify the appropriate debug level for each target listed in the **Debug Level** fields.

5. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

6. In the **Description** field, enter a description of your request.

7. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

8. To submit your request, click **Save**.

---

---
title: Enable debug logger
description: Instructions for completing the service request form to enable the standard debug logger or request a non-standard debug level.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_pf_logging
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_pf_logging.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enable debug logger

PingFederate generates logs that record server events. To enable the standard debug logger or request a non-standard debug level, submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## About this task

Log files are written to the PingFederate log directory, located in the following directory by default: `<pf_install>/pingfederate/log`.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingFederate service requests** > **Enable debug logger**.

3. Select the **Standard Debug?** field to configure the log level to `DEBUG`.

4. If you're requesting a non-standard debug level, specify the targets that you want configured from the `log4j2.xml` file in the **Debug Targets** fields. Learn more in [Log4j 2 logging service and configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_log4j_2_loggin_service_and_config.html).

   Then, specify the appropriate debug level for each target listed in the **Debug Level** fields.

5. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

6. In the **Description** field, enter a description of your request.

7. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

8. To submit your request, click **Save**.

---

---
title: Enable debug logging
description: Instructions for completing the service request form to enable the debug logger on an environment or application.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_logging
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_logging.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
---

# Enable debug logging

To enable the debug logger on an environment or application, submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **Platform service requests** > **Enable debug logger**.

3. In the **AWS Region** field, select the region of your P1AS environment, such as US1, EU1, or AUI, that you want to update.

4. In the **Targeted application** field, specify the application that the hostname will point to.

5. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

6. In the **Description** field, enter a description of your request.

7. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

8. To submit your request, click **Save**.

---

---
title: Enable outbound provisioning
description: To enable outbound provisioning, submit a service request through the Support Portal.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_provisioning
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_provisioning.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
---

# Enable outbound provisioning

To enable outbound provisioning, submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **Platform service requests** > **Enable outbound provisioning**.

3. In the **AWS Region** field, select the region of your P1AS environment, such as US1, EU1, or AU1, that you want to update.

4. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. In the **Description** field, enter a description of your request.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. To submit your request, click **Save**.

---

---
title: Indexes
description: Instructions for completing the service request form to request index modifications.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_pd_email_indexes
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_pd_email_indexes.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Indexes

Submit your index change requests through the service request form on the [Support Portal](https://support.pingidentity.com/s/).

## About this task

Indexes improve database search performance and provide consistent search rates, regardless of the number of database objects stored in the directory information tree (DIT) and are associated with attributes within your schema. To add an index, attributes must already exist in the schema defined for your directory. To delete an index, ensure that data is removed from user entries prior to it being deleted or data modification issues and application errors will exist.

Learn more about indexes in [Working with indexes](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_work_with_indexes.html) in the PingDirectory documentation.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingDirectory service requests** > **Indexes**.

3. In the **Attribute to index** field, provide the attribute that will be indexed.

4. In the **Index type(s)** field, select the index types that you want to create. Refer to [Index types](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_index_types.html) for a list of PingDirectory server index types.

   If you're unsure which index types to select, specify how to apply the index by providing your own filter. For example, "(cn=smith)" applies the index to users whose common name is Smith.

5. If you selected a subtree index and expect that strings might have more than 4,000 matches, you can specify a higher limit in the **Substring index entry limit** field.

6. If you expect a search to match more than 4,000 values, you can specify a higher limit in the **Index entry limit** field. Searches that exceed this value will be unindexed and are only allowed upon request.

7. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

8. In the **Description** field, enter a description of your request.

9. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

10. To submit your request, click **Save**.

---

---
title: Integration kits
description: Instructions for completing the service request form to install a new integration kit or upgrade an existing kit.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_pa_plugins
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_pa_plugins.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 28, 2024
section_ids:
  steps: Steps
---

# Integration kits

To install a new integration kit or upgrade an existing kit, submit a request through the service request form on the [Support Portal](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingAccess service requests** > **Integration kits**.

3. In the **Integration Kit Type** field, select **Non-Standard** if the kit is provided by the Professional Services team. Otherwise, select **Standard**.

4. In the **Integration Kit Name** field, provide the name of the kit you're requesting.

5. In the **Version** field, provide the version of the kit you're requesting.

6. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

7. In the **Description** field, indicate whether the request is for a new integration kit or an upgrade to an existing kit.

8. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

9. To submit your request, click **Save**.

---

---
title: Integration kits
description: Instructions for completing the service request form to install a new integration kit or upgrade an existing kit.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_pf_plugins
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_pf_plugins.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Integration kits

To install a new integration kit, or upgrade an existing integration kit, submit a service request through the [Support Portal](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingFederate service requests** > **Integration Kits**.

3. In the **Integration Kit Type** field, select **Non-Standard** if the kit is provided by the Professional Services team. Otherwise, select **Standard**.

4. In the **Integration Kit Name** field, provide the name of the kit you're requesting.

5. In the **Version** field, provide the version of the kit you're requesting.

6. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

7. In the **Description** field, indicate whether the request is for a new integration kit or an upgrade to an existing kit.

8. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

9. To submit your request, click **Save**.

---

---
title: IP allow list
description: Instructions for completing the service request form to create or update the IP allow list.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_allowlist
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_allowlist.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  steps: Steps
---

# IP allow list

Starting in platform version 2.2, you can submit a service request to ask that an IP allow list be added or updated to specific PingOne Advanced Services public endpoints. Submit this service request through the [Support Portal](https://support.pingidentity.com/s/).

|   |                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any endpoint with an allow list will only be accessible by the IP addresses in the CIDR ranges provided. Ping Identity is not responsible if a list causes downtime because it contains incorrect CIDRs, nor is Ping Identity responsible for a CIDR list that is too permissive. |

|   |                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------- |
|   | Only public IPv4 CIDR IP addresses are supported, and each allow list can be no larger than 2.8 KB (\~180 CIDRs). |

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **Platform service requests** > **IP Allowlisting**.

3. In the **Business Priority** list, select the appropriate description:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

4. In the **Description** field, enter the following information:

   * **Name**: An identifier for the IP allow list. For example, `corp-allowlist`.

   * **Description** (optional): A description for the IP allow list. For example, `allow list for the corporate network`.

   * **CIDR/IP(s)**: A list of allowed IPv4 CIDRs. For example, `10.0.0.0/24, 172.10.0.1`.

   * **vHosts** (Optional): Any virtual host endpoints for the allow list. For example, `vhostname1, vhostname2`.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | These virtual hosts must already exist in your environment. If they don't exist, you can create them yourself using the admin console or the administrative API. Learn more about this process in [Creating and updating virtual hosts](p1as_platform_virtual_hosts.html) and [Using the PingOne Advanced Services administrative API](p1as_platform_admin_api.html)Or, you can submit a service request and ask us to update your configurations for you. Learn more in [Update TLS certificate](p1as_platform_tls_certs.html). |

5. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

6. To submit your request, click **Save**.