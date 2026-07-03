---
description: The API requires a JWT Bearer token for authenticating requests. This token can be retrieved using either an authorization code flow or a client credentials flow.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:task_summary_table:p1as_platform_api_config
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/task_summary_table/p1as_platform_api_config.html
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
