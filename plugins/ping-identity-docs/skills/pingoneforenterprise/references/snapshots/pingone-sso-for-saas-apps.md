---
title: .NET Redirect Sample
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_net_redirect_sample
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_net_redirect_sample.html
revdate: March 30, 2023
---

# .NET Redirect Sample

```
<%@ Page Language="C#" %>
<script runat="server">

  protected String GetIdpId()
  {
      //Implement me!
      return "testidp.admin.pingidentity.com";
  }

/**
 * The saasid value is the GUID associated with the application. This is displayed in parentheses below the
 * application name on the My Applications page.
 * You will need to replace the saasid value in "${saasId}" in the sample below with the GUID for your application.
 * For example: String saasId = "18a6ada7-8f37-4d77-86f4-173046796193";
 */

  protected override void OnLoad(EventArgs e)
  {
      String saasId = "${saasId}";
      String idpId = GetIdpId();
      String baseUrl = "${tokenServiceBaseUrl}/sso/sp/initsso";
      String initSsoUrl = String.Format("{0}?saasid={1}&idpid={2}", baseUrl,
                                       saasId, idpId);
      Response.Redirect(initSsoUrl);
      base.OnLoad(e);
  }
</script>
```

---

---
title: .NET Token Exchange Sample
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_net_token_echange_sample
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_net_token_echange_sample.html
revdate: March 30, 2023
---

# .NET Token Exchange Sample

```
using System;
using System.Data;
using System.IO;
using System.Text;
using System.Net;
using System.Configuration;
using System.Collections.Generic;

public partial class ssoLogin : System.Web.UI.Page
{

    private static void SetBasicAuthHeader(HttpWebRequest req, String userName,
        String userPassword)
    {
        string authInfo = userName + ":" + userPassword;
        authInfo = Convert.ToBase64String(Encoding.Default.GetBytes(authInfo));
        req.Headers["Authorization"] = "Basic " + authInfo;
    }

    private static void SetAgentIdCookie(HttpWebRequest req, String agentid)
    {
        if (agentid != null)
        {
            req.Headers["Cookie"] = "agentid=" + agentid;
        }
    }

    private static string GetTokenServiceUrl(string pingConnectToken)
    {
        return "${tokenServiceBaseUrl}/sso/TXS/2.0/2/"+ pingConnectToken;
    }

 /**
 * The restApiKey value is the REST API Client Secret (the password/secret associated with your REST API Client ID). You will need
 * to uncomment the String restApiKey statement and replace the empty string in the sample below with your REST API Client Secret.
 * For example:  String restApiKey = "mySecretApiPassword";
 *
 * The restAuthUsername value is the REST API Client ID (a GUID) automatically assigned to your account in the PingOne admin portal
 * on the Account > Integration page.
 * You will need to replace the restAuthUsername value in "${restAuthUsername}" in the sample below with your REST API Client ID.
 * For example: SetBasicAuthHeader(request, "5f6ce45e-1a00-488e-8519-7c9946cb6379", restApiKey);
 */

protected void Page_Load(object sender, EventArgs e)
    {
        String tokenId = Request.QueryString["tokenid"];
        String agentId = Request.QueryString["agentid"];

        HttpWebRequest request = WebRequest.Create(GetTokenServiceUrl(tokenId))
                            as HttpWebRequest;

        // Specify this value at http://admin.pingidentity.com
        //String restApiKey = "";
        SetBasicAuthHeader(request, "${restAuthUsername}", restApiKey);
        SetAgentIdCookie(request, agentId);
        request.Method = "GET";
        request.ContentType = "text/plain;charset=utf-8";
        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        StreamReader reader = new StreamReader(response.GetResponseStream());
        String content = reader.ReadToEnd();
        String [] lines = content.Split('\\n');
        Dictionary<string, string> properties = new Dictionary<string, string>();
        foreach (string line in lines )
        {
            if (line.Contains("="))
            {
                properties.Add(line.Split('=')[0], line.Split('=')[1]);
            }
        }
        String subject = properties["pingone.subject"];
        String idpId = properties["pingone.idp.id"];
        CreateUserSession(subject, idpId);
    }

    protected void CreateUserSession(string subject, string idpId)
    {
        // Implement Me! Must validate that subject belongs to this idpId
        Response.Write("<p>Welcome, " + subject + "</p>");
    }
}
```

---

---
title: About multiplexing
description: "PingOne SSO for SaaS Apps supports two kinds of multiplexing: application multiplexing and connection multiplexing."
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_about_multiplexing
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_about_multiplexing.html
revdate: January 20, 2023
section_ids:
  application-multiplexing: Application multiplexing
  connection-multiplexing: Connection multiplexing
  combining-application-and-connection-multiplexing: Combining application and connection multiplexing
---

# About multiplexing

PingOne SSO for SaaS Apps supports two kinds of multiplexing: application multiplexing and connection multiplexing.

## Application multiplexing

A multiplexed application has a single connection to PingOne SSO for SaaS Apps. This allows you to share an application configuration across all identity providers (IdPs) connected to the application. For example, if you have one customer using PingFederate as an IdP, and another customer using Active Directory, they can both connect to a multiplexed application without any additional configuration.

PingOne SSO for SaaS Apps uses the entity ID value `PingConnect` to send SAML assertions to multiplexed applications. For non-multiplexed applications, PingOne uses the entity ID of the IdP.

With a non-multiplexed application, you configure a connection for each individual customer, often with different ACS URLS and entity IDs for each individual IdP.

|   |                                                                                                   |
| - | ------------------------------------------------------------------------------------------------- |
|   | Only SAML applications can be non-multiplexed. OIDC and REST applications are always multiplexed. |

Application multiplexing simplifies administration by allowing you to apply an application configuration to all customers and IdPs instead of administering each instance of the application separately. For example, exchanging metadata or updating certificates applies the change to all IdPs connected to the multiplexed application.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Manual connections](p14saas_create_saml_connection.html) to non-multiplexed applications are not supported. You can only create connections to non-multiplexed applications through [invited](p14saas_creating_invited_sso_connection.html) or managed PingOne for Enterprise accounts. |

## Connection multiplexing

A multiplexed connection is a single connection from an IdP to PingOne SSO for SaaS Apps. Multiplexing allows the IdP to access all of your customer's applications using a shared attribute contract, the same certificates, and a single entity ID, `PingConnect`.

A non-multiplexed connection is application-specific. The IdP configures a connection for each application using different attribute contracts and application-specific entity ID values.

|   |                                                                                  |
| - | -------------------------------------------------------------------------------- |
|   | IdP connections through a PingOne for Enterprise account are always multiplexed. |

Without multiplexing, PingOne SSO for SaaS Apps connections to your applications are separate, one-to-one connections to an IdP. Each application is assigned a separate entity ID value for its connection. If your account has an existing multiplexed connection for some IdPs, you can still create non-multiplexed connections for other IdPs.

Because the IdP only needs to maintain a single connection to PingOne SSO for SaaS Apps rather than maintaining a separate connection for each application, connection multiplexing simplifies administration.

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | [Manual connections](p14saas_create_saml_connection.html) can be either multiplexed or non-multiplexed. |

## Combining application and connection multiplexing

**Multiplexing combination support**

| Connection type            | Multiplexed application | Non-multiplexed application                                                                                                                                                                                                                                  |
| -------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Multiplexed connection     | Supported               | Supported                                                                                                                                                                                                                                                    |
| Non-Multiplexed connection | Supported               | Not supported&#xA;&#xA;Because non-multiplexed connections must be established manually, and it's not possible to create a manual connection to a non-multiplexed application, non-multiplexed connections to non-multiplexed applications aren't supported. |

---

---
title: Add a SaaS application
description: As a service provider (SP), you'll make your cloud application available to your customers through PingOne SSO for SaaS Apps.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_add_saas_application
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_add_saas_application.html
revdate: September 2, 2022
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Add a SaaS application

As a service provider (SP), you'll make your cloud application available to your customers through PingOne SSO for SaaS Apps.

## Steps

1. Go to **Applications > My Applications**.

2. Select the type of application you're adding:.

   ### Choose from:

   * For instructions to add a SAML application, see [Adding or updating a SAML-enabled application](p14saas_add_update_saml_application.html).

   * For instructions to add an OpenID Connect (OIDC) application, see [Manage OAuth settings](../pingone_for_enterprise/p14e_manage_oauth_settings.html), [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html) and [Adding or updating an OIDC application](p14saas_add_update_oidc_app.html).

---

---
title: Add or update other applications
description: You can add applications to PingOne SSO for SaaS Apps that are neither SAML nor OpenID Connect (OIDC). These are software as a service (SaaS) applications that you make available directly to customers or partners.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_add_update_other_app
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_add_update_other_app.html
revdate: September 15, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  next-steps: Next steps
---

# Add or update other applications

You can add applications to PingOne SSO for SaaS Apps that are neither SAML nor OpenID Connect (OIDC). These are software as a service (SaaS) applications that you make available directly to customers or partners.

## About this task

PingOne SSO for SaaS Apps handles most of the connection details for these applications and will send single sign-on (SSO) users to the URL that you specify for an application.

However, you will need to set up the referenced page to process the security token sent from PingOne and create a user session for the authenticated user. See [Process the PingOne SSO for SaaS Apps token exchange](p14saas_process_p1_token_exchange.html) for more information.

Each application connection is multiplexed, meaning PingOne SSO for SaaS Apps will use the same connection to the application for all customers or partners.

## Steps

1. Go to **Applications > My Applications > SAML** and click **Add New Application**.

2. In the **Category** list, select the category that applies to your application.

3. In the **Name** field, enter a name for your application.

4. In the **Description** field, enter a description for your application.

5. Select a visibility option for your application:

   ### Choose from:

   * Click **Public** to add your application to the Application Catalog.

   * Click **Private** to make your application available only to the organizations you invite.

6. **Optional:** Upload an icon and logo for your application.

   |   |                                                                                |
   | - | ------------------------------------------------------------------------------ |
   |   | If you're using the current version of the dock, you don't need to add a logo. |

7. Click **Continue to Next Step**.

8. On the **Create Connections** page, click **No, I want to enable through PingOne**.

9. **Optional:** In the **Hostname or Domain** field, enter the host or domain name associated with your application.

   |   |                                                                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If your application has only one entry point, make your application more secure by leaving the **Hostname or Domain** field empty to disable the `appurl` parameter.If you must use `appurl`, a domain such as `app.example.com` can provide stricter validation than `example.com`. |

10. On the **Binding Type** line, select the binding type to use for sending tokens to this application.

    |   |                                                                                                                           |
    | - | ------------------------------------------------------------------------------------------------------------------------- |
    |   | The default binding type of **Post** is more secure, because it doesn't expose the token as a query parameter in the URL. |

11. In the **Default Application URL** field, enter an application URL to send authenticated users to.

    |   |                                                                                                                 |
    | - | --------------------------------------------------------------------------------------------------------------- |
    |   | Although both HTTP and HTTPS URLs are accepted in this field, HTTPS is more secure for production applications. |

    The page for this URL will need to process the security token sent from PingOne SSO for SaaS Apps and create a user session. For more information, see [Process the PingOne SSO for SaaS Apps token exchange](p14saas_process_p1_token_exchange.html).

12. **Optional:** In the **Error URL** field, enter a URL to direct users to in case of an error.

    If you don't specify an error URL, PingOne SSO for SaaS Apps will display a generic error page.

13. **Optional:** Select the **Allow Customization** to allow PingOne for Enterprise accounts to override the **Default Application URL** and **Error URL** when they configure this application from the application catalog.

    |   |                                                                                   |
    | - | --------------------------------------------------------------------------------- |
    |   | This option is available only if you make your application visibility **Public**. |

14. In the **Entity ID** field, enter a unique identifier for SAML connections to this application.

    If you don't specify an entity ID, PingOne SSO for SaaS Apps uses either PingConnect or the application's `saasid`, depending on what connection type you select during connection configuration.

    If a custom entity ID is in use by a non-multiplexed connection, it cannot be changed.

    For more information, see [Creating a manual SAML connection](p14saas_create_saml_connection.html).

15. Click **Continue to Next Step**.

16. **Optional:** To add SSO attributes, click **Add Attribute**.

    | Field           | Action                                                                                                                                                                       |
    | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Name**        | Enter a name for the attribute.                                                                                                                                              |
    | **Description** | Enter a description for the attribute.                                                                                                                                       |
    | **Required**    | Select the checkbox to make the attribute required for SSO.                                                                                                                  |
    | **Advanced**    | Click to configure advanced attribute options.Learn more in [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html). |

17. Click **Continue to Next Step**.

18. On the **Create Instructions** tab, enter instructions to guide a user in enabling SSO for this application.

    |   |                                                                      |
    | - | -------------------------------------------------------------------- |
    |   | This tab only appears if you made your application public in step 5. |

    1. In the **Introduction Text** field, enter text introducing your application and supplying any necessary instructions to users.

    2. **Optional:** In the **SSO Configuration Path** field, enter navigation instructions to guide users to your application's SSO configuration page.

    3. **Optional:** In the **SSO Configuration Page URL** field, enter the URL for your application's SSO configuration page.

    4. **Optional:** For each configuration step that you want to add, click **Add Step**, and fill in the **Label** and **Instruction** fields.

    5. **Optional:** To add an image, click **Select Image** and browse to the image you want to upload.

19. Click **Continue to Next Step**.

20. On the **Publish** tab, verify that the information is correct, then click **Save & Publish**.

    If you made your application public, it's submitted to us for registration. After we have processed the registration for your application, your application information is published in the Application Catalog.

Your application displays in the listing on your **My Applications** page, where you can view or edit all of the your application settings.

If you made your application private, you must invite customers to connect to your application. For instructions, see [Customer connection methods](p14saas_customer_connection_methodss.html).

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After you publish an application, you cannot change the SSO connection types. You must remove the application and add it again. However, you can change the configuration settings for the SSO connections. |

## Next steps

To test your application before connecting to a customer, see [Testing your application using the built-in IdP](p14saas_test_application_integration.html) or [Testing your application using PingOne for Enterprise](p14saas_testing_your_application_using_p14e.html).

---

---
title: Adding a new connection to an existing customer
description: Connect an existing customer to a new application by creating a new application connection using the same customer details.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_adding_new_connection_existing_customer
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_adding_new_connection_existing_customer.html
revdate: August 3, 2022
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result
---

# Adding a new connection to an existing customer

Connect an existing customer to a new application by creating a new application connection using the same customer details.

## Steps

1. Create a new connection:

   ### Choose from:

   * Add the [SSO self-service widget](p14saas_create_connection_using_sso_self_service_widget.html) to your new application.

   * Use the [customer connection API](p14saas_create_connection_using_customer_connection_api.html) to add a new connection to your new application.

   * Send a new [SSO connection invitation](p14saas_creating_invited_sso_connection.html).

   * Create a new [manual SSO connection](p14saas_create_saml_connection.html).

2. When choosing which applications to add to the connection, select only the new applications you want to add.

   |   |                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you select applications that are part of an existing customer connection, PingOne SSO for SaaS Apps attempts to create a duplicate application connection, which results in an error. |

3. When entering the **Customer Email** and **Customer ID (idpid)**, use the same values as the existing connection for this customer.

   |   |                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To find the email and `idpid` values for an existing customer connection, go to **Customer Connections** and click **Details** for the appropriate customer connection. |

4. Complete the rest of the connection creation process as normal.

## Result

PingOne SSO for SaaS Apps adds your new application to the existing customer connection.

---

---
title: Adding or updating a SAML-enabled application
description: Create a SAML application for your customers to connect to.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_add_update_saml_application
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_add_update_saml_application.html
revdate: September 22, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  result: Result
  next-steps: Next steps
---

# Adding or updating a SAML-enabled application

Create a SAML application for your customers to connect to.

## About this task

When you're adding or updating a SAML-enabled application, you'll need to specify the proper SAML configuration to establish a connection for your application.

## Steps

1. Go to **Applications > My Applications > SAML**.

2. Click **Add New Application**.

3. On **Basic information** tab, select the category that applies to your application.

4. Enter the application name and a description that will identify your application to users.

5. Select whether your application is to be made publicly available (listed in the Application Catalog), or privately available (not listed in the Application Catalog, and available to organizations only at your invitation).

6. **Optional:** Upload a logo and icon to use for your application. The logo is used for workstation users. The icon is displayed for mobile users.

   PNG is the only supported graphics format.

7. Click **Continue to Next Step** and choose **Yes, it is SAML-enabled**.

8. **Optional:** On the Create Connections page, select the SAML version supported by your application. If you're uncertain, the default version (SAML 2.0) is generally correct.

9. **Upload Metadata**. Click **Select File** to upload the application's metadata file, or click **Or use URL** to enter the URL of the metadata file. The **ACS URL** and **Entity ID** will then be supplied for you. If you don't upload the application metadata, you'll need to enter this information manually with values provided by the application.

   |   |                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The application's **Entity ID** must be unique within your account. You can't configure more than one application in PingOne SSO for SaaS Apps using the same SP entity ID. |

10. **Optional:** Choose whether or not to enable SAML multiplexing (the default).

    For more information about application multiplexing, see [About multiplexing](p14saas_about_multiplexing.html).

11. Select the public signing certificate to use. PingOne SSO for SaaS Apps will use this certificate on your behalf to sign SAML assertions. You can choose either:

    ### Choose from:

    * Primary Certificate

      When you select the primary certificate, the PingOne SSO for SaaS Apps metadata for download contains both the primary and the renewal certificates.

    * Renewal Certificate

      When you select the renewal certificate, the PingOne SSO for SaaS Apps metadata for download contains only the renewal certificate. A renewal certificate is available only thirty days before the expiration of the primary certificate.

      |   |                                                                                                                                                                                                                         |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you are using multiplexing, the primary and renewal certificates are PingOne SSO for SaaS Apps universal certificates. In this case, when you're notified to update the certificate, it's imperative that you do so. |

      1. You can also choose to download the certificates independently (not as part of the PingOne SSO for SaaS Apps metadata). To do this, scroll down to the certificate **Download** links and click the appropriate link.

         The Signing Certificate download link is for the certificate you selected in the **Signing Certificate** dropdown list. The other certificate is the certificate you didn't select in the **Signing Certificate** dropdown list. Note the expiration dates for the certificates.

         If a certificate is identified as Expired, currently, we'll still accept it. At some point, we may no longer accept the certificate, so we recommend you install a valid certificate soon. Note that your IdP or an application may not accept an expired certificate.

12. You need to supply the PingOne SSO for SaaS Apps connection information to each customer connecting to your application. You can either:

    * Click **Download** to retrieve all of SAML metadata for the PingOne SSO for SaaS Apps connection.

    * Copy the displayed connection information (for **SSO Service URL** and **Entity ID**) and download the PingOne SSO for SaaS Apps signing certificate.

13. **Optional:** Enter the URL for the SAML **Single Logout Endpoint**. We send the single logout (SLO) request to this URL using the binding type you select for **Single Logout Binding Type**.

    The attributes for **Single Logout Endpoint**, **Single Logout Binding Type** and **Verification Certificate** are interdependent. To support SLO, you'll need to specify all of these attribute values, and optionally, **Single Logout Response Endpoint**. See [PingOne for Enterprise and SLO](../pingone_for_enterprise/p14e_slo.html) for more information.

    |   |                                                                                                                       |
    | - | --------------------------------------------------------------------------------------------------------------------- |
    |   | If you choose not to support SLO for an application, when the user session ends the application will not be notified. |

14. **Optional:** Enter the URL for the SAML **Single Logout Response Endpoint**. If you don't assign a value here, **Single Logout Endpoint** is also used as the response endpoint. You send the application SLO response to this URL.

15. **Optional:** Select the binding type to use for SLO. This can be **POST** or **Redirect** (defaults to **POST**).

16. **Optional:** Upload the signing certificate you'll use to sign SLO requests. This can be the same certificate you use for SAML assertions.

17. Click **Signing Algorithm** to choose the algorithm used to sign both SAML assertions and SLO requests.

    If you are setting up a new application, the signing algorithm defaults to the recommended SHA-256.

    If you have an existing application configuration, SHA-1 may be displayed as the default signing algorithm. We recommend you change it to SHA-256 at your convenience.

18. **Optional:** **Encrypt Assertion**. If selected, the assertions sent from PingOne SSO for SaaS Apps for the application will be encrypted. Available for SAML 2.0 multiplexed applications only.

    Selecting this option will prompt you for the information necessary to encrypt the assertion:

    * Encryption Certificate

      Upload the certificate to use to encrypt the assertions.

    * Encryption Algorithm

      Choose the algorithm to use for encrypting the assertions. We recommend **AES\_256** (the default), but you can select **AES\_128** instead.

    * Transport Algorithm

      The algorithm used for securely transporting the encryption key. Currently, **RSA-OAEP** is the only transport algorithm supported.

19. Verify that all entries are correct, then click **Continue to Next Step**. The SSO Attribute Requirements page is displayed.

    On the SSO Attribute Requirements page, click **Add Attribute** to add any attributes necessary for SSO to your application.

20. **Optional:** Click on the **Name** or **Description** of any existing attribute to edit the value. Press Enter to save your changes or Esc to cancel.

    Click the **Required** checkbox for any attributes that require a value for SSO to your application.

    Click **Continue to Next Step**.

    On the Create Instructions page, for **Introduction Text**, enter text introducing your application and supplying any necessary instructions to users.

    For **SSO Configuration Path**, enter user guidance for the location of any SSO settings for your application.

    For **SSO Configuration Page URL**, enter the URL for any SSO settings for your application.

    For **Configuration Steps**, click **Add Step** to add stepped instructions for configuring SSO for your application.

    For **SSO Configuration Page Screenshot**, click **Select Image** to upload a screenshot of the SSO configuration page for your application.

    On the Publish page, click **Add Parameter** to assign any connection parameters customers can use for your application. You can elect to make the parameters required.

    On the Publish page, verify that the information is correct, then click **Save & Publish**.If you have selected to publish your application publicly, it is submitted to us for registration. When we have processed the registration for your application, your application information is published in the Application Catalog.

    Your application is displayed in the listing on your My Applications page, where you can view or edit all of the your application settings as needed.

    If you have selected to publish your application privately, the application will not be listed in the Application Catalog. Instead, you will invite customers to connect to your application. See [Customer connection methods](p14saas_customer_connection_methodss.html) for instructions.

## Result

After you have published an application, you will not be able to change the SSO connection type(s). You will need to remove the application, then add it again in this case. However, you can change configuration settings for the SSO connections.

## Next steps

To test your application before connecting to a customer, see [Testing your application using the built-in IdP](p14saas_test_application_integration.html) or [Testing your application using PingOne for Enterprise](p14saas_testing_your_application_using_p14e.html).

---

---
title: Adding or updating an OIDC application
description: Create a new OpenID Connect (OIDC) application, or modify an existing application in PingOne SSO for SaaS Apps.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_add_update_oidc_app
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_add_update_oidc_app.html
revdate: June 5, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  result: Result
  next-steps: Next steps
---

# Adding or updating an OIDC application

Create a new OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* application, or modify an existing application in PingOne SSO for SaaS Apps.

## Before you begin

Before you initially add an OICD application, you need to configure the access token your account will use for OIDC applications. These are account-level settings that will be inherited at the application level when you add or update and application, as you are doing here.

PingOne SSO for SaaS Apps returns OIDC user attributes in different ways depending on the `response_type` parameter.

The contents of the ID token depend on whether or not the application also returns an access token:

* For flows that return both an access token and an ID token (such as authorization code flow, or implicit flows where the `response_type` includes `token`) the ID token contains the `sub` and, if requested, `email` scopes. The `userinfo` endpoint contains all of the attributes for the requested scopes and attributes configured on the **User Info** tab for the application, if the `openid` scope was requested.

* For flows that don't return an access token, the ID token contains all of the attributes for the requested scopes and any attributes configured on the **User Info** tab for the application, if the `openid` scope was requested. The `userinfo` endpoint is inaccessible in this case because no access token is issued.

The access token contains attributes configured at **Applications > OAuth Settings > Access Token**.

See [Manage OAuth settings](../pingone_for_enterprise/p14e_manage_oauth_settings.html) and [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html).

## About this task

When updating an application, any changes you make to the existing configuration parameters will be reflected in your customer's or partner's connection to the application.

However, if your customer or partner has changed the parameter settings in their PingOne for Enterpriseaccount, their local settings will override your updated configuration.

In other words, configuration updates made by a service provider at the application level will not override configuration updates made at the connection level.

## Steps

1. Go to **Applications > My Applications > OIDC**.

2. Add a new application or edit an existing application.

   ### Choose from:

   * To create a new application, click **Add Application**. See Step 3 for new application types.

   * To update an existing application, expand the application and click the **Pencil** icon. Skip to Step 4.

3. Select the type of application you want to add and click **Next**:

   ### Choose from:

   * To create an application that is accessed and used within a browser, click **Web App**.

   * To create an application that is stored locally and run on a desktop or device, click **Native App**.

   * To create an API-driven front-end application, such as applications using Node.js or Angular, click **Single Page App**.

   * If you want full control of all available configuration parameters, click **Advanced Configuration**.

4. In the **Application Name** field, enter a name for the application.

5. In the **Short Description** field, enter a description of the application.

   Customers will be able to see your description.

6. In the **Category** list, select a category for the application.

7. **Optional:** Click **Icon** to add an icon for this application.

   The icon file can be up to 1 Mb in size. The supported graphics formats are JPG, PNG and GIF.

8. Click **Next**.

9. **Optional:** To enable or disable a custom valid duration for the application access token, click the **Override Access Token Lifetime** toggle.

   When this control is enabled, a **Minutes** selector is displayed. The valid range is 1 - 60 minutes. The default value is inherited from your account-level OAuth settings.

10. If you enabled the override, enter the number of minutes access token lifetime in the **Minutes** field.

    The valid range is 1 - 60 minutes. The default value is inherited from your account-level OAuth settings. For more information, see [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html).

11. Select the grant types allowed for the application.

    Available grant types are determined by the application type. For more information, see [OIDC application grant types](../pingone_for_enterprise/p14e_oidc_app_grant_types.html).

12. If you selected **Refresh Token**, configure the token settings:

    1. Click the **Override Refresh Idle Lifetime** toggle to override the global OAuth setting for the application.

    2. In the **Refresh Token Idle Lifetime** field, enter the number of minutes that a refresh token can be idle before being used again.

    3. Click the **Override Refresh Token Max Lifetime** toggle to override the global OAuth setting for this application.

    4. In the **Refresh Token Max Lifetime** field, enter the maximum number of minutes that a refresh token can be valid.

13. Copy the **Client ID**, **Discovery URL**, and **Issuer** values to use later in integrating the application with PingOne SSO for SaaS Apps.

14. **Optional:** For applications that use the Authorization Code grant type, you can click **Add Secret** to generate up to two client secrets to pair with the client ID.

15. Click **Next**

16. **Optional:** In the **Start SSO URL** field, enter the URL to use for SSO to the application.

    This is the URL to which application users will redirect to initiate SSO to PingOne for Enterprise using OIDC.

17. In the **Redirect URI** field, enter URIs for PingOne SSO for SaaS Apps to send responses to for the application's authorization requests.

    |   |                                                     |
    | - | --------------------------------------------------- |
    |   | Click **Add URL** to define multiple redirect URIs. |

18. **Optional:** In the **Logout URI** field, enter the URI to which PingOne for Enterprise sends a user for single logout (SLO) *(tooltip: \<div class="paragraph">
    \<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
    \</div>)*.

19. Click **Next**

20. Click **Add Attribute** to configure attributes returned by the `UserInfo` endpoint for this application when the `openid` scope is included in the authorization request.

    1. In the **Attribute Name** field, enter a name for the attribute.

    2. Select the **Required** checkbox to require the attribute mapping when a UserInfo request is made for this application.

       The `sub` (Subject) attribute is required for all UserInfo requests.

    The `idpid` attribute is used by PingOne for Enterprise to identify the identity provider (IdP) *(tooltip: \<div class="paragraph">
    \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
    \</div>)*, and is included in the attribute contract by default.

21. Click **Next**.

22. Click the **[icon: plus, set=fa]**icon to add scopes to the allowed list, or click the **-** icon to remove them.

    These OAuth user scopes are the user resources to which the application will request access. The `openid` scope is expected to always be included in the authorization request.

23. Click **Save**.

## Result

The new OIDC application is added to your **My Applications** list for OIDC. You can edit the application configuration as needed by expanding the application and clicking the **Pencil** icon. Refer to this documentation when updating configuration values.

## Next steps

Integrate the application with PingOne SSO for SaaS Apps. See [Integrating an OIDC application](p14saas_integrate_oidc_application.html) for instructions.

---

---
title: Application Catalog app connection
description: Use either of these ways to connect customers to your Application Catalog app:
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_application_catalog_app_connection
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_application_catalog_app_connection.html
revdate: December 23, 2021
---

# Application Catalog app connection

Use either of these ways to connect customers to your Application Catalog app:

* The SSO Self-Service widget

  You will need to paste some JavaScript and a minimal amount of code into a page or section of your application that's accessible only to your customer's administrative users. You then ask one of your customer's administrators to visit your page and run our widget. The administrator is redirected to a page on the PingOne portal where they enter their customer configuration information. This makes it easy for you to capture customer configurations without having to be concerned with customer-specific protocol settings.

* Customer Connection API

  To use the Customer Connection API, you will authenticate using your PingOne credentials. See [Using the global REST API client credentials](p14saas_use_rest_api_client_credentials.html). Your application needs to include an administrator-only page or section for the customer. You also need to elicit the necessary SAML connection information from your customer.

---

---
title: Assign administrators
description: Members of your organization who are assigned the Global Administrator role can manage the PingOne for SaaS Apps account. If you created the account, you are automatically assigned Global Administrator permissions.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_assign_administrators
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_assign_administrators.html
revdate: December 22, 2021
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Assign administrators

## About this task

Members of your organization who are assigned the Global Administrator role can manage the PingOne for SaaS Apps account. If you created the account, you are automatically assigned Global Administrator permissions.

You can also choose to assign an Audit & Report Administrator. Administrators having this role can manage subscriptions for audit events and run reports. They have access only to the Reporting and Dashboard pages.

## Steps

1. Select the **Account > Administrators**.

2. Click **Add Administrator**.

3. Enter the **First Name**, **Last Name**, and **Email** for the administrator you want to add.

4. From the **Role** list, select the administrator role to assign.

   For more information about administrative roles and permissions, see [Administrative roles](../pingone_for_enterprise/p14e_administrative_roles.html).

5. If you want to assign read-only permissions to the administrator role, click the **Read Only** checkbox.

6. Click **Save**. An email invitation is sent to the person you're inviting. The email invitation is valid for 3 days, or until a new invitation is sent.

   When the person clicks the PingOne link in the email to accept the invitation, they're prompted to assign a password.

7. Repeat these steps for each of the administrators you want to add.

---

---
title: Assign branding and design
description: Assign your organization's branding for the IdP Discovery page and the associated error page. Both of these pages are displayed to users.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_assign_branding_design
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_assign_branding_design.html
revdate: December 22, 2021
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
  choose-from-4: Choose from:
---

# Assign branding and design

## About this task

Assign your organization's branding for the IdP Discovery page and the associated error page. Both of these pages are displayed to users.

## Steps

1. Go to the **Account > Branding** page.

2. In the **Corporate Logo** section, click the **Add** and browse for the logo that you want to assign.

3. To create a banner message, enter text into the **Banner Message** field.

   The banner will display at the top of the admin portal, and will only be visible to your administrative users.

4. In the **Backgrounds** section, select from the following:

   ### Choose from:

   * **Main Background**. Select one of the following:

   * **None**: No background color or image. The background is white by default.

   * **Image**: Click **Choose Background** and navigate to the image that you want to use as the dock background.

     |   |                                                                                                  |
     | - | ------------------------------------------------------------------------------------------------ |
     |   | Images larger than 3000 x 1500 are automatically resized, resulting in possible loss of quality. |

   * **Color**: Select a background color from the dropdown color palette, or enter the Hex color code you require.

   * **Form Background Color**: Select a background color from the dropdown color palette, or enter the Hex color code you require.

5. In the **Buttons** section, select from the following:

   ### Choose from:

   * **Button Color**: Select a button color from the dropdown color palette, or enter the Hex color code you require.

   * **Font Color**: Select a font color for button labels from the dropdown color palette, or enter the Hex color code you require.

6. In the **Text** section, select from the following:

   ### Choose from:

   * **Form Fill Color**: Select a fill color to use for the form from the dropdown color palette, or enter the Hex color code you require.

   * **Form Font Color**: Select a font color to use for text from the dropdown color palette, or enter the Hex color code you require.

   * **Link color**: Select a color to use for links from the dropdown color palette, or enter the Hex color code you require.

   * **Header and Custom Text Color**: Select the color to use for the header and custom text from the dropdown color palette, or enter the Hex color code you require.

7. In the **Content** section, select from the following:

   ### Choose from:

   * Select whether to display application icons on the IdP Discovery page.

   * **IdP Discovery Page Text**: Enter any custom text to display in the IdP Discovery form (300 characters maximum).

   * **Error Page Header**: Enter any custom text to display in the header for the error page (100 characters maximum).

   * **Error Page Text**: Enter any custom text to display on the the error page (300 characters maximum).

8. Click **Save**. The changes are applied and will be immediately visible on the IdP Discovery page and the associated error page.

---

---
title: Associate certificates with a SAML application or customer IdP connection
description: When you manage the customer's identity provider (IdP) configuration and connection to a SAML application, or when the application is multiplexed, you can select the signing and verification certificates to associate with the application or direct customer IdP connection.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_associate_certificate_with_saml_application_idp_connection
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_associate_certificate_with_saml_application_idp_connection.html
revdate: December 23, 2021
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Associate certificates with a SAML application or customer IdP connection

When you manage the customer's identity provider (IdP) configuration and connection to a SAML application, or when the application is multiplexed, you can select the signing and verification certificates to associate with the application or direct customer IdP connection.

## About this task

|   |                                                                                              |
| - | -------------------------------------------------------------------------------------------- |
|   | Signing certificates can be associated with multiple applications and identity repositories. |

## Steps

1. Go to **Setup > Certificates**.

2. Click to expand the certificate currently associated with the application or direct customer IdP connection you want to change.

3. Click **Usage** to display a list of applications and direct customer IdP connections associated with that certificate.

4. Click to select the application or direct customer IdP connection you want to change. The **Update Certificate** window will appear.

5. Select a new signing certificate or verification certificate from the drop-down list and click **Save**.

---

---
title: Certificate management
description: PingOne SSO for SaaS Apps tracks the status of active certificates and allows you to manage them from the Certificate Management page.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_managing_certificates
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_managing_certificates.html
revdate: September 2, 2022
---

# Certificate management

PingOne SSO for SaaS Apps tracks the status of active certificates and allows you to manage them from the **Certificate Management** page.

For multiplexed SAML applications and connected customer identity providers, you use signing certificates to sign single sign-on (SSO) and single logout (SLO) messages sent from PingOne SSO for SaaS Apps. Signing certificates created in PingOne SSO for SaaS Apps are self-signed by default. You can also create a certificate signing request (CSR) in PingOne SSO for SaaS Apps and send the certificate for signing by a certificate authority (CA).

PingOne SSO for SaaS Apps uses verification certificates to verify the signature on SSO and SLO messages received by PingOne SSO for SaaS Apps from service providers and identity providers. PingOne SSO for SaaS Apps first attempts to validate a signature using the primary verification certificate. If verification fails, PingOne SSO for SaaS Apps will then attempt to use the secondary verification certificate, where defined.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | Verification and encryption certificates are not supported for applications using SAML v1.1 |

|   |                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because of a platform limitation, the **Usage** tab for the global encryption certificate shows all [manual SAML connections](p14saas_create_saml_connection.html) in your tenant rather than showing only those connections that use the encryption certificate. |

The **Dashboard** notification area in the admin portal displays an alert for certificates that are about to expire or have expired.

A yellow alert indicates:

* One or more signing certificates are due to expire in the next three months

* A primary verification certificate is about to expire (and will be replaced by a secondary verification certificate, if available)

* A secondary verification certificate is about to expire

* An encryption certificate is about to expire

A yellow alert for expiring certificates creates a link to the **Certificate Management** page.

A red alert indicates a certificate has expired. The alert contains a link to the **Certificate Management** page.

In addition to **Dashboard** messages, PingOne SSO for SaaS Apps notifies Global Administrators about expiring certificates by email. Notification emails are sent 60 days, seven days, and one day before a certificate expires, and again after the certificate expires.

For more information about email notification preferences, see [Editing administrative roles, permissions, and notifications](../pingone_for_enterprise/p14e_editing_administrative_roles_permissions_notifications.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You will be able to see certificates (signing or verification) that you cannot manage, and that originate outside of your account in the following circumstances:- A PingOne for Enterprise or Invited SSO account has a connection to your account's non-multiplexed SAML application. In this case, the connection's signing certificates will be visible to you.

- A PingOne for Enterprise account uses an identity repository that employs certificates, such as PingFederate, a custom SAML, or ADFS identity repository, and also has a connection to one of your account's SAML applications. In this case both the signing and verification certificates for the identity repository, as well as the connection's signing certificate, will be visible to you.Although these certificates are visible to you, they are owned by a separate account and must be managed by an administrator in that account.Such certificates will also appear in your **Dashboard** notification area, if the certificates are expired or due to expire. This gives you visibility into certificates that are expiring or expired that your connected customers need to take action on. |

---

---
title: Code grant type
description: For any grant type, the application needs to send the authorization request to the PingOne SSO for SaaS Apps authorization endpoint returned by the Discovery URL(https://sso.connect.pingidentity.com/sso/as/authorization.oauth2).
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_odic_code_grant_type
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_odic_code_grant_type.html
revdate: September 25, 2023
---

# Code grant type

For any grant type, the application needs to send the authorization request to the PingOne SSO for SaaS Apps authorization endpoint returned by the **Discovery URL**(`https://sso.connect.pingidentity.com/sso/as/authorization.oauth2`).

PingOne SSO for SaaS Apps sends the response to the authorization request to the URL you assigned to the **Redirect (Callback) URI** setting when you created the application. You can find this URL in the **Authentication Flow** section on the application summary page.

PingOne SSO for SaaS Apps validates the `redirect_uri` parameter against the list of redirect URIs specified in the application's configuration. You can find these URIs in the **Authentication Flow** section on the application summary page. If the `redirect_uri` is valid, PingOne SSO for SaaS Apps sends the response to the specified redirect URI.

If your application uses an authorization code grant type, PingOne SSO for SaaS Apps uses the following process to complete the authorization request:

1. The application sends an authorization request for a code grant type.

   Here is an example of an authorization request URI:

   ```
   https://sso.connect.pingidentity.com/sso/as/authorization.oauth2?client_id=cdd237bb-3404-4ad4-90eb-d2e2528xxxxx&scope=openid&response_type=code
   ```

   The following table describes the parameters that make up the authorization request URI.

   | Parameter               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `client_id`             | Your client ID, assigned by PingOne for Enterprise. You can find this value on the **Details** tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | `scope`                 | The user resources that can be accessed by the application. The `openid` scope is expected to be specified, either as the sole scope value or one of the scope values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | `response_type`         | This must be `code`. An authorization code is then returned in the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | `code_challenge`        | This PKCE parameter is either plain text or a cryptographic hash of a random string. The random string or plain text must be a `code_verifier` value that you will include in the subsequent token request.&#xA;&#xA;Use PKCE only when you aren't using a client secret, including client\_secret in the token request.&#xA;&#xA;For more information, see OAuth 2.0 RFC 7636.                                                                                                                                                                                                                                                                                                                                                               |
   | `code_challenge_method` | This PKCE parameter is required only when `code_challenge` is specified.This can be either:- `plain` When the `code_challenge_method` value is plain text

   - `S256` When the `code_challenge_method` value is an SHA-256 cryptographic hash&#xA;&#xA;When you subsequently include the code\_verifier value in the token request, the code\_challenge value and the code\_verifier value must match.For more information, see [OAuth 2.0 RFC 7636](https://tools.ietf.org/html/rfc7636).                                                                                                                                                                                                                                                      |
   | `login_hint`            | Used to specify either the idpid or an email domain.If you specify the idpid, the user is redirected to the IdP associated with the idpid value for the current application, identified in PingOne SSO for SaaS Apps by the `saasid` parameter.If you specify an email domain as the `login_hint` value, the domain must be included in the IdP Discovery configuration for the application and tenant.For more information about IdP Discovery for your connection type, see:- [Edit an invited customer connection](p14saas_edit_invited_customer_connection.html)

   - [Edit a managed customer connection](p14saas_edit_managed_customer_connection.html)

   - [Enable IdP discovery for partner accounts](p14saas_enable_idp_discovery.html) |

2. The PingOne for Enterprise authorization endpoint returns the authorization code to the application.

   The HTTPS response will be similar to this:

   ```
   https://example.com/#code=IDa4e54a98b90b234476819295a791e4a95bbb9a6e1a3095b50200000164fbeb8b43
   ```

3. The application uses the authorization code returned in the response to request an access token and ID token from the PingOne for Enterprise token endpoint, https\://sso.connect.pingidentity.com/sso/as/token.oauth2 .

   Here is an example request using cURL:

   ```shell
   curl -k -X POST -H "Accept: application/json" -d 'client_id=cdd237bb-3404-4ad4-90eb-d2e2528xxxxx&client_secret=CpquMknCg9An9Up1Ys2mnVEdKkCDaxtJcJG4adFPBDnPU6SBp7VNGUhyTmaJXXmpR&grant_type=authorization_code&code=ID5d7d1770409374639980ce161952fda57b21db562ff8320b020000016543fxxxxx&redirect_uri=https://example.com\' \https://sso.connect.pingidentity.com/sso/as/token.oauth2
   ```

   Because the authorization request did not include PKCE parameters, the token request must use the client secret value assigned when the application was added to PingOne SSO for SaaS Apps. You can find the assigned client secret in the **Details** tab.

4. The application validates the `id_token` returned. For more information see the [OpendID Connect Core 1.0 specifications](https://openid.net/specs/openid-connect-core-1_0.html).

5. The application can also optionally validate the token or access token returned.

   Use the PingOne for Enterprise introspection endpoint returned by the **Discovery URL** `https://sso.connect.pingidentity.com/sso/as/introspect.oauth2` to validate the access token.

   For access tokens that are signed rather than encrypted, you can also use the JWKS URI returned by the **Discovery URL** `https://sso.connect.pingidentity.com/sso/as/jwks`.

   |   |                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can see your access token settings at **Applications > My Applications > OAuth Settings**.For more information, see [Configuring your OAuth settings](../pingone_for_enterprise/p14e_configure_oauth_settings.html). |

---

---
title: Configure partner account service settings
description: As a Global Administrator, configure partner settings for your managed service.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_configure_partner_account_service_settings
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_configure_partner_account_service_settings.html
revdate: July 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Configure partner account service settings

As a Global Administrator, configure partner settings for your managed service.

## About this task

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All of the settings on this page are optional. Any settings that you do not assign will use the default values. Default values are noted where possible. |

## Steps

1. Go to **Managed Accounts > Service Settings**.

   **Service Settings** is not displayed for Audit & Report Administrators.

2. To enable Edit mode, click **Edit**.

3. To allow your partners to change the corporate logo displayed on their dock, select **Allow Logo Customization**.

   |   |                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When this option is enabled, your partners can change this logo on one of three menus in their PingOne SSO for SaaS Apps admin portal:- **Setup > Branding > Dock**

   - **Setup > Branding > Logon & SSO**

   - **Account > Branding** |

4. To assign the corporate branding logos for your service, click the appropriate **Select Image** button, and then select the local image you want to use.

   Once saved, the logo will appear on your partners' **User Dock** and in their **Admin Portal**

5. To make only certain identity repositories available for selection, click to clear the **Allow All Identity Repositories** checkbox.

   By default, all PingOne SSO for SaaS Apps identity repositories (current or future) are available for your customers to select. After you disable the **Allow All Identity Repositories** checkbox, the identity repository options display.

   1. Select the identity repositories to allow your customers to use.

6. To allow your partners to set up, customize, or disable the multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
   \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
   \</div>)* policy, enable the **Allow MFA Customization** setting.

   When this setting is enabled (the default), your customers can change their account settings for MFA.

   When disabled, the configuration for MFA appears as read-only information to your customers and they're unable to change the settings.

7. Configure the templates for emails automatically sent to partners.

   | Option         | Description                                                                                                                                                                                                                 |
   | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Sender         | The sender address used in emails sent to your customers.The ability to customize this field is disabled by default. To enable it, [log on to your account](https://support.pingidentity.com/s/) and submit a support case. |
   | Admin Invite   | In the **Subject Line** field, enter a subject line for admin invite emails.To customize the admin invite email template click **Download Template**.                                                                       |
   | Password Reset | In the **Subject Line** field, enter a subject line for password reset emails.To customize the password reset email template click **Download Template**.                                                                   |

   1. To view or modify the default HTML email template sent to customers, click **Download Current Template**.

   You can modify this template for your use or create a new HTML template. Any new templates you create need to be valid HTML and use the same variables as in the default template. Do not add any new variables.

   1. To replace the current default template, click **Replace Template** and then select the HTML file to use.

   2. To delete an email template, click **Remove Saved Template**, and then click **Save**.

      ### Result:

      The custom template is removed and the default PingOne SSO for SaaS Apps email template is restored.

      |   |                                                                                                                                                                    |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | The ability to customize this field is disabled by default. To enable it, [log on to your account](https://support.pingidentity.com/s/) and submit a support case. |

8. To change the support link that appears in the header of each page, enter a new URL in the **Support Link** field.

9. Click **Save**.

---

---
title: Configure SSO to the admin portal
description: Grant administrative users single sign-on (SSO) access to the PingOne SSO for SaaS Apps admin portal.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_configure_sso_admin_portal
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_configure_sso_admin_portal.html
revdate: March 30, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  result: Result
  next-steps: Next steps
---

# Configure SSO to the admin portal

Grant administrative users single sign-on (SSO) access to the PingOne SSO for SaaS Apps admin portal.

## About this task

To permit service-provider (SP)-initiated SSO to the admin portal, you must configure the connection between the portal and your identity provider (IdP).

## Steps

1. In the admin portal, go to **Setup > Admin Portal SSO > IdP Configuration**.

2. **Optional:** Import the IdP metadata.

   ### Choose from:

   * To upload the metadata file, click **Select File**.

   * To enter the metadata URL, click **Or use URL**.

3. In the **Entity ID** field, enter the entity ID provided by the IdP.

4. In the **SSO Endpoint** field, enter the endpoint at the IdP to which PingOne sends AuthnRequests.

5. On the **Verification Certificate** line, click **Select File** to browse and upload the IdP's public signing certificate that PingOne will use to sign SAML assertions.

6. In the **Single Logout Endpoint** field, enter the IdP endpoint to which PingOne will send single logout (SLO) requests.

7. In the **Single Logout Response Endpoint** field, enter the IdP endpoint to which PingOne will send SLO responses.

8. On the **Single Logout Binding Type** line, click either the **Redirect** or **Post** button to determine which binding type PingOne will use to send SLO requests.

9. Select the **Sign the AuthnRequest** box to make PingOne sign AuthnRequests to the IdP.

10. To download the PingOne signing certificate for upload to your IdP, click **Download**.

11. From the **Signing Algorithm** list, select the algorithm PingOne will use to sign AuthnRequests to the IdP.

12. To download the PingOne metadata for upload to your IdP, click **Download PingOne Metadata**.

13. Click **Save Settings**.

14. Go to **Setup > Admin Portal SSO > Group Permissions**.

15. For each admin group you want to authorize to SSO, click **Add Group**.

    If you're using LDAP groups, this needs to be the full distinguished name (FDN) for the administrator group (`CN=admins,OU=example,…​`).

    |   |                                                                                                                                                                                                         |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | You can assign groups to a read-only administrative role, which grants the administrator access to the areas of the admin portal normally allowed by that role, but not the ability to change settings. |

16. Click **Save**.

## Result

Your administrative users can sign on from the **Initiate Single Sign-On (SSO) URL** displayed at **Setup > Admin Portal SSO > IdP Configuration** after you complete the form.

## Next steps

If you also intend to initiate SSO from your IdP, you must configure your IdP to append one of the following parameters to PingOne's ACS URL:

* `RelayState=https://pingone.com/1.0/8bfe0aeb-79ca-4fd4-a116-c3f7c7dbe6ca`

* `saasid=8bfe0aeb-79ca-4fd4-a116-c3f7c7dbe6ca`

---

---
title: Configure your account
description: You can edit your company information, add administrators and add your corporate branding to your PingOne SSO for SaaS Apps account.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_configure_your_account
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_configure_your_account.html
revdate: June 28, 2024
---

# Configure your account

You can edit your company information, add administrators and add your corporate branding to your PingOne SSO for SaaS Apps account.

---

---
title: Connect an application for a partner account
description: For partner accounts, you will need to set up the connection to an application that you have added from your PingOne SSO for SaaS Apps account by entering the partner PingOne for Enterprise account and selecting the application from the list on the the Private App Catalog page.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_connect_application_partner_account
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_connect_application_partner_account.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  in-your-pingone-sso-for-saas-apps-account: In your PingOne SSO for SaaS Apps account
  in-the-partner-pingone-for-enterprise-account: In the partner PingOne for Enterprise account
---

# Connect an application for a partner account

## About this task

For partner accounts, you will need to set up the connection to an application that you have added from your PingOne SSO for SaaS Apps account by entering the partner PingOne for Enterprise account and selecting the application from the list on the the Private App Catalog page.

## Steps

### In your PingOne SSO for SaaS Apps account

1. On the **Managed Accounts** page, expand the details for the partner account for which you want to connect an application and click **Enter Account** to administer the partner account.

### In the partner PingOne for Enterprise account

2. Go to **Applications > Private App Catalog**.

3. **Optional:** In the Search field, search for your app by typing the name, entity ID, or description of the application you want to add.

   The application listing will display the type of the application.

4. When you find the application you want to configure, click the right-arrow icon. The application description is displayed.

5. Click **Setup** to begin.

6. **Optional:** If the application connection is multiplexed or uses IdP-initiated SSO (the PingOne SSO for SaaS Apps Customer Connection API), the option to enter the URL to use as the **Target Resource** is displayed.

   This is the URL to which the user is directed after IdP-initiated SSO.

7. **Optional:** Select whether or not to enable **Force Re-authentication**. Click **Continue to Next Step**.

   When enabled, to establish a connection to the application, users having a current, active SSO session are re-authenticated by the identity provider.

8. To add a new attribute, click **Add New Attribute**.

   In most cases, the default attribute mappings are sufficient. These mappings assign your identity repository attributes to the attributes provided by the Service Provider for the application.

   For each application attribute, you can:

   1. Enter a value in the **Application Attribute** field

   2. Click the **Required** checkbox to designate an attribute or attributes as required by the application.

   3. In the **Identity Bridge Attribute or Literal Value** field, choose between:

      * Select an attribute from the drop down list.

      * Select **As Literal** and enter a literal value to assign.

        1. Click **Advanced** and enter Advanced Attribute Mapping mode.

           For more information, see [Creating advanced attribute mappings](../pingone_for_enterprise/p14e_creating_advaced_attribute_mappings.html)

        2. Select the **Provisioning** checkbox to make this a provisioning attribute rather than an SSO attribute.

           Custom provisioning attributes are currently only available for Aquera and Salesforce applications.

9. When you've finished modifying or adding any additional attributes, click **Continue to Next Step**.

10. Make the new application available to your partner's users.

    See [Authorize group access to applications](../pingone_for_enterprise/p14e_authorize_group_access_applications.html) for instructions.

---

---
title: Connect customers to your application
description: PingOne SSO for SaaS Apps has several ways to connect customers to your application.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_connect_customers_your_application
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_connect_customers_your_application.html
revdate: May 11, 2023
---

# Connect customers to your application

PingOne SSO for SaaS Apps has several ways to connect customers to your application.

To connect a customer to your application, you first choose a connection method. When the customer has accepted the connection, you edit the connection to assign additional settings and verify or reconfigure the existing settings.

Choose the appropriate connection method for your application:

* SSO Self-Service widget

  Adding the single sign-on (SSO) *(tooltip: \<div class="paragraph">
  \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
  \</div>)* Self-Service widget is the easiest way to add customer connections to your Application Catalog app. For more information, see [Application Catalog app connection](p14saas_application_catalog_app_connection.html).

* Email Invitation

  You can send you customer an invitation email containing a link to PingOne for Enterprise to provide their SSO information. This is the best option if you can't use the Self-Service widget. For more information, see [Creating an invited SSO connection](p14saas_creating_invited_sso_connection.html).

* Customer Connection REST API

  If you want your customers to provide their information directly to your application without ever visiting PingOne for Enterprise, you can add connections using the Customer Connection REST API. You should only use the Customer Connection API in cases where sending the customer's administrative user to the PingOne for Enterprise portal isn't a viable option. For more information, see [Application Catalog app connection](p14saas_application_catalog_app_connection.html).

* Manual SAML connection

  You can add customer connections manually. You should only choose this method in circumstances, such as:

  * Your customer prefers that you manage their connection to your application.

  * A direct SAML connection to your application is all that your customer needs.

  * You anticipate connecting to a limited number of customers.

  * Your customer is not using PingOne for Enterprise.

See [Direct SAML connection](p14saas_direct_saml_connection.html) for more information.

* Configure a private application for a managed partner account

  If you have a PingOne SSO for SaaS Apps with Managed Accounts license, you can create a private connection for your partner accounts. After entering a partner account and adding an application, you'll configure the application connection from within the partner's account, rather than from your PingOne SSO for SaaS Apps account. For more information, see [Connect an application for a partner account](p14saas_connect_application_partner_account.html).

* PingOne Invited SSO

  Invited SSO accounts are PingOne for Enterprise accounts designed specifically for your customers who already have an identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)* set up and want to handle the application connection themselves. They can then use their Invited SSO account to add the connection to your application and configure an identity bridge to their IdP. For more information, see [Invited SSO](p14saas_invited_sso.html).

---

---
title: Create a connection using the Customer Connection API
description: Create a page or section in your application for the customer's administrator. Then use the Customer Connection REST API to elicit the necessary SAML connection information (SAML attribute values) from the customer.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_sso_for_saas_apps:p14saas_create_connection_using_customer_connection_api
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_create_connection_using_customer_connection_api.html
revdate: December 23, 2021
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Create a connection using the Customer Connection API

## About this task

Create a page or section in your application for the customer's administrator. Then use the Customer Connection REST API to elicit the necessary SAML connection information (SAML attribute values) from the customer.

All PingOne resource requests require authentication. You need to include your REST API Client ID and REST API Client Secret credentials in the request, otherwise the resource returns a 401 (Unauthorized) status code. Currently, we support HTTP basic authentication, which includes encrypted credentials in the request header. See [Using the global REST API client credentials](p14saas_use_rest_api_client_credentials.html) for more information.

## Steps

1. Create a page or section in your application that can be accessed only by the customer's administrator.

2. Use the Customer Connection API to:

   1. Get the SAML attributes containing the customer's information.

   2. Create a customer connection using the customer information retrieved and the customer's signing certificate.

   See the [PingOne SSO for SaaS Apps Customer Connection API](p14saas_customer_connection_api.html) for more information.