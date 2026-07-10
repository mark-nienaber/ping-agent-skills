---
title: Authentication API support
description: You can use the PingFederate authentication API to integrate the Twitter IdP Adapter into your application.
component: twitter
page_id: twitter::pf_threatmetrix_ik_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/twitter/pf_threatmetrix_ik_authentication_api_support.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
---

# Authentication API support

You can use the PingFederate authentication API to integrate the Twitter IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the Twitter IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. You can find help in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Changelog
description: The following is the change history for the Twitter Login Integration Kit.
component: twitter
page_id: twitter:release_notes:pf_twitter_cic_changelog
canonical_url: https://docs.pingidentity.com/integrations/twitter/release_notes/pf_twitter_cic_changelog.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 19, 2026
section_ids:
  version-1-4-1-january-2026: Version 1.4.1 - January 2026
  version-1-4-november-2020: Version 1.4 – November 2020
  version-1-3-june-2018: Version 1.3 – June 2018
  version-1-2-january-2014: Version 1.2 – January 2014
  version-1-1-1-july-2013: Version 1.1.1 – July 2013
  version-1-1-april-2013: Version 1.1 – April 2013
  version-1-0-february-2011: Version 1.0 – February 2011
---

# Changelog

The following is the change history for the Twitter Login Integration Kit.

## Version 1.4.1 - January 2026

* Removed third-party fonts and the `authn-api-messages.properties` file.

## Version 1.4 – November 2020

* Added support for single logout (SLO).

* Added a setting to use a browser redirect or pop-up window for the sign-on presentation.

* Added customizable sign-on templates for the pop-up window presentation.

* Added customizable user-facing language-pack messages.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

* Improved security by updating bundled components.

* Improved configuration field validation.

## Version 1.3 – June 2018

* Added the ability to configure a callback URL to resolve Twitter enforcement of allowlisting callback URLs.

## Version 1.2 – January 2014

* Improved support for Twitter REST API version 1.1.

* Added support for Twitter API restrictions that allow only TLS/SSL connections.

## Version 1.1.1 – July 2013

* Added the ability to mask the **Consumer ID** and **Consumer Secret** fields. Learn more in [Twitter IdP Adapter settings reference](../setup/pf_twitter_cic_twitter_idp_adapter_settings_reference.html).

* Added support for Scribe 1.3.3.

## Version 1.1 – April 2013

* Added support for the Twitter REST API version 1.1.

## Version 1.0 – February 2011

* Initial Release.

---

---
title: Configuring an adapter instance
description: Configure the Twitter IdP Adapter to determine how PingFederate communicates with Twitter.
component: twitter
page_id: twitter:setup:pf_twitter_cic_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/twitter/setup/pf_twitter_cic_configuring_an_adapter_instance.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Twitter IdP Adapter to determine how PingFederate communicates with Twitter.

## Steps

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Click **Create New Instance**.

2. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Twitter IdP Adapter**. Click **Next**.

3. (Optional) On the **IdP Adapter** tab, in the **Attribute Selector** section, select or define attributes to request from Twitter.

   You can find a list of available attributes in [User Object](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/user-object) in the Twitter documentation.

   1. Click **Add a new row to 'Attribute Selector'**.

   2. Select an attribute from the **Twitter Attribute** list or enter an attribute in the **Additional Twitter Attribute** field.

      |   |                                                                                                                                                                                                                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You must use the correct syntax for manual entries. You can find an example of the data structure in [GET account/verify\_credentials](https://developer.twitter.com/en/docs/accounts-and-users/manage-account-settings/api-reference/get-account-verify_credentials) in the Twitter documentation. |

   3. In the **Action** column, click **Update**.

   4. To add more attributes, repeat steps a - c.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to [Twitter IdP Adapter settings reference](pf_twitter_cic_twitter_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Extended Contract** tab, add any attributes you want to include in the contract. Click **Next**.

6. On the **Adapter Attributes** tab, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

7. On the **Adapter Contract Mapping** tab, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

8. On the **Summary** tab, check your configuration, then click **Save**.

---

---
title: Deploying the integration files
description: To get started with the integration, deploy the Twitter Login Integration Kit files to your PingFederate directory.
component: twitter
page_id: twitter:setup:pf_twitter_cic_deploying_the_integration_files
canonical_url: https://docs.pingidentity.com/integrations/twitter/setup/pf_twitter_cic_deploying_the_integration_files.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  steps: Steps
---

# Deploying the integration files

To get started with the integration, deploy the Twitter Login Integration Kit files to your PingFederate directory.

## Steps

1. Download the Twitter Login Integration Kit `.zip` archive from the [**Add-ons** tab of the PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) or the [Ping Identity Marketplace](https://marketplace.pingone.com/item/twitter-login-integration-kit).

2. Stop PingFederate, if it's running.

3. If you're upgrading an existing deployment, back up your customizations and delete earlier versions of the integration files:

   1. Back up any Twitter Login Integration Kit files that you customized in the `<pf_install>/pingfederate/server/default/conf/` directory.

   2. Delete the `pf-twitter-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. Extract the `.zip` archive and merge the contents of the `dist` directory with your `<pf_install>/pingfederate` directory.

5. If there's more than one version of the `pf-authn-api-sdk-<version>.jar` file in your `<pf_install>/pingfederate/server/default/lib` directory, delete all but the latest version of the file.

6. If you backed up any customized files, modify the new files with your customizations.

7. Start PingFederate.

8. If you operate PingFederate in a cluster, repeat steps 2 - 7 for each engine node.

---

---
title: Download manifest
description: The following files are included in the Twitter Login Integration Kit .zip archive:
component: twitter
page_id: twitter:release_notes:pf_twitter_cic_download_manifest
canonical_url: https://docs.pingidentity.com/integrations/twitter/release_notes/pf_twitter_cic_download_manifest.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
---

# Download manifest

The following files are included in the Twitter Login Integration Kit `.zip` archive:

* `ReadMeFirst.pdf`: Contains links to this online documentation.

* `legal/Legal.pdf`: Copyright and license information.

* `dist`: Contains the integration files.

  * `deploy`: Contains the Java libraries.

    * `pf-twitter-adapter-<version>.jar`: A `.jar` file containing the Twitter IdP Adapter.

  * `conf`: Contains the HTML template that presents the Twitter sign-on form.

    * `language-packs`: Contains files with customizable user-facing messages.

      * `pingfederate-twitter-adapter-messages.properties`: A variable file that customizes the messages that appear on the template files.

    * `template`: Contains user-facing HTML template files.

      * `twitter-pop-up-template.html`: A template that opens a pop-up window to prompt the user to sign on.

      * `twitter-post-auth-template.html`: A template that returns the user to the PingFederate sign-on flow after they sign on with Twitter.

      * `assets`: Contains functional scripts and files used by the template.

        * `css/twitter.css`: A CSS file that customizes the appearance of the template files.

        * `fonts/end-user`: Contains template fonts and icons.

          * `icons`: Contains template icons.

        * `images`: Contains template image files.

          * `ping-logo.svg`: An image file with company branding.

* `lib/pf-authn-api-sdk-<version>.jar`: A `.jar` file containing the PingFederate Authentication API SDK.

---

---
title: Enabling debug logging
description: To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.
component: twitter
page_id: twitter:troubleshooting:pf_twitter_cic_enabling_debug_logging
canonical_url: https://docs.pingidentity.com/integrations/twitter/troubleshooting/pf_twitter_cic_enabling_debug_logging.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling debug logging

To help with troubleshooting or monitoring, you can turn on activity logging for the adapter.

## About this task

These steps are optional. You can find general information about logging in [Enabling debug messages and console logging](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html) in the PingFederate documentation.

## Steps

1. Open the `<pf_install>/pingfederate/server/default/conf/log4j2.xml` file for editing.

2. To log activity for PingFederate and all adapters, do the following:

   1. Find the following section:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   2. Change `INFO` to `DEBUG`:

      ```html
      <AsyncRoot level="DEBUG" includeLocation="false">
      	<!-- <AppenderRef ref="CONSOLE" /> -->
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

   3. To see the adapter activity in the console, remove the comment tags:

      ```html
      <AsyncRoot level="INFO" includeLocation="false">
      	<AppenderRef ref="CONSOLE" />
      	<AppenderRef ref="FILE" />
      </AsyncRoot>
      ```

3. To log activity for the Twitter IdP Adapter only, add the following line:

   ```html
   <Logger name="com.pingidentity.adapter.idp.twitter" level="DEBUG"/>
   ```

4. Save the file.

---

---
title: Integrating social sign-on into your application
description: To complete your Twitter sign-on integration, add a sign-on hyperlink to your application.
component: twitter
page_id: twitter:setup:pf_twitter_cic_integrating_social_sign_on_into_your_application
canonical_url: https://docs.pingidentity.com/integrations/twitter/setup/pf_twitter_cic_integrating_social_sign_on_into_your_application.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  steps: Steps
---

# Integrating social sign-on into your application

To complete your Twitter sign-on integration, add a sign-on hyperlink to your application.

## Steps

1. If your application is outside the PingFederate domain, configure an SP connection:

   1. Create a service provider (SP) connection to your application as shown in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

      |   |                                                                                                                                                                                                                                                                     |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Use the Twitter IdP Adapter instance as an authentication source. Learn more in [Mapping an adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapping_adapter_instance.html) in the PingFederate documentation. |

   2. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the following table:

      `https://<pf_host>:<pf_port>/idp/startSSO.ping?PartnerSpId=<ConnectionId>`

      | Variable          | Description                                                                                        |
      | ----------------- | -------------------------------------------------------------------------------------------------- |
      | *\<pf\_host>*     | The host name or IP address of the PingFederate server.                                            |
      | *\<pf\_port>*     | The port number for PingFederate.                                                                  |
      | *\<ConnectionId>* | The federation identifier of the SP for the connection that uses the Twitter IdP Adapter instance. |

2. If your application is inside the PingFederate domain, configure an adapter-to-adapter mapping:

   1. Create an SP connection to your application as shown in [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html) in the PingFederate documentation.

      |   |                                                                                                                                                                                                                                                                     |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Use the Twitter IdP Adapter instance as an authentication source. Learn more in [Mapping an adapter instance](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_mapping_adapter_instance.html) in the PingFederate documentation. |

   2. On the **System > Protocol Settings > Roles & Protocols** page, select **Enable Identity Provider (IdP) role and support for the following** and **Enable Service Provider (SP) role and support for the following**.

   3. In both the **Enable Identity Provider** and **Enable Service Provider** sections, select any protocol, such as **SAML 2.0**. Click **Save**.

      |   |                                                                                                                                  |
      | - | -------------------------------------------------------------------------------------------------------------------------------- |
      |   | PingFederate requires a protocol selection to activate the roles. The protocol that you select is not used for this integration. |

   4. On the **Service Provider > Adapters** page, create or select an adapter instance that's integrated with the application as shown in [SP application integration settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_applicat_integra_settings.html) in the PingFederate documentation.

   5. On the **Identity Provider > Adapter-to-Adapter Mappings** page, configure the IdP-to-SP adapter mapping as shown in [Adapter-to-adapter mappings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_adaptertoadapter_mappings.html) in the PingFederate documentation.

   6. In your web application, create a hyperlink to allow users to sign on to the SP application. Use the following URL and replace the variables based on the descriptions in the table below:

      `https://<pf_host>:<pf_port>/pf/adapter2adapter.ping?IdpAdapterId=<IdpAdapterId>&SpSessionAuthnAdapterId=<SpAdapterId>`

      | Variable          | Description                                                                               |
      | ----------------- | ----------------------------------------------------------------------------------------- |
      | *\<pf\_host>*     | The host name or IP address of the PingFederate server.                                   |
      | *\<pf\_port>*     | The port number for PingFederate.                                                         |
      | *\<IdpAdapterId>* | The instance ID of the Twitter IdP Adapter instance.                                      |
      | *\<SpAdapterId>*  | The instance ID of the SP adapter instance that has been integrated with the application. |

---

---
title: Known issues and limitations
description: The following are known issues or limitations for the Twitter Login Integration Kit.
component: twitter
page_id: twitter:release_notes:pf_twitter_cic_known_issues_and_limitations
canonical_url: https://docs.pingidentity.com/integrations/twitter/release_notes/pf_twitter_cic_known_issues_and_limitations.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  known-issues: Known issues
  known-limitations: Known limitations
---

# Known issues and limitations

The following are known issues or limitations for the Twitter Login Integration Kit.

## Known issues

* Twitter doesn't support single logout (SLO) *(tooltip: \<div class="paragraph">
  \<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
  \</div>)*.

## Known limitations

* Twitter has rate limiting for OAuth calls.

  You can find more information in [Rate limits](https://developer.twitter.com/en/docs/basics/rate-limits) in the Twitter documentation.

---

---
title: Overview of the SSO flow
description: With the Twitter Login Integration Kit, PingFederate includes the Twitter authentication API in the sign-on flow.
component: twitter
page_id: twitter::pf_twitter_cic_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/twitter/pf_twitter_cic_overview_of_the_sso_flow.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  description: Description
---

# Overview of the SSO flow

With the Twitter Login Integration Kit, PingFederate includes the Twitter authentication API in the sign-on flow.

The following diagram illustrates a SP-initiated SSO *(tooltip: \<div class="paragraph">
\<p>In SAML, an identity federation transaction in which the initial action for SSO occurs at the SP site.\</p>
\</div>)* scenario where PingFederate authenticates users to an SP application using the Twitter IdP Adapter.

![A diagram showing the SSO flow using the Twitter Login Integration Kit.](_images/twitter-login-ik-sso-flow-overview.jpg)

## Description

1. The user opens a web application and chooses the Twitter sign-on option.

2. The sign-on link points to the Twitter IdP Adapter.

3. The Twitter IdP Adapter requests a request token from Twitter and provides the callback URL. Twitter returns the request token.

4. The PingFederate server redirects the user to Twitter with the request token and a list of requested permissions. On Twitter, the user authenticates their identity, then authorizes the requested permissions.

   Twitter redirects the browser to the Twitter IdP Adapter callback URL with a verification code.

   |   |                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------- |
   |   | If the user fails to authenticate or doesn't authorize the request, the response includes an error code instead. |

5. PingFederate sends Twitter the request token and verification code. Twitter validates these components and returns an access token to the PingFederate callback URL.

6. PingFederate sends Twitter a request for user attributes and presents the access token.

7. PingFederate redirects the user to the web application with the user attributes.

---

---
title: Registering PingFederate in Twitter
description: To allow PingFederate to process social sign-on requests with Twitter, add PingFederate as an application in the Twitter admin console.
component: twitter
page_id: twitter:setup:pf_twitter_cic_registering_pf_in_twitter
canonical_url: https://docs.pingidentity.com/integrations/twitter/setup/pf_twitter_cic_registering_pf_in_twitter.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  steps: Steps
---

# Registering PingFederate in Twitter

To allow PingFederate to process social sign-on requests with Twitter, add PingFederate as an application in the Twitter admin console.

## Steps

1. Sign on to the Twitter [Developer portal Apps page](https://developer.twitter.com/en/portal/projects-and-apps) using a Twitter developer account.

2. On the **My Applications Dashboard**, create a new Twitter application.

3. In the **Name** field, enter the name of the application.

   For example, `MyPingFederate`.

4. In the **Website** field, enter the domain for your web application.

   For example, `http://www.example.com`.

5. In the **Callback URL** field, enter the hostname (or virtual hostname) and port of your PingFederate server, followed by the Twitter IdP Adapter instance endpoint.

   For example, `https://pf.example.com:9031/ext/twitter-authn`.

   |   |                                                                                                                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The default endpoint is `/twitter-authn`. If you set a custom endpoint here, enter the matching value in the **Authorization Callback Endpoint** field of your adapter instance configuration in [Configuring an adapter instance](pf_twitter_cic_configuring_an_adapter_instance.html). |

6. If your web application will use the access token for subsequent Twitter API calls that require read and write access, set the **Default Access Type** to **Read & Write**.

7. Complete the configuration based on the needs of your specific environment. You can find help in [Developer Apps](https://developer.twitter.com/en/docs/apps/overview) in the Twitter documentation.

8. Click **Create your Twitter application**.

9. On the application details page, note the **Consumer Key** and **Consumer Secret**. You'll use these in [Configuring an adapter instance](pf_twitter_cic_configuring_an_adapter_instance.html).

---

---
title: Twitter IdP Adapter settings reference
description: Field descriptions for the Twitter IdP Adapter configuration tab.
component: twitter
page_id: twitter:setup:pf_twitter_cic_twitter_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/twitter/setup/pf_twitter_cic_twitter_idp_adapter_settings_reference.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
---

# Twitter IdP Adapter settings reference

Field descriptions for the Twitter IdP Adapter configuration tab.

> **Collapse: Standard fields**
>
> | Field                         | Description                                                                                                                                                                                                                                                                                                          |
> | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Consumer Key**              | The consumer key that noted in [Registering PingFederate in Twitter](pf_twitter_cic_registering_pf_in_twitter.html).                                                                                                                                                                                                 |
> | **Consumer Secret**           | The consumer secret you noted in [Registering PingFederate in Twitter](pf_twitter_cic_registering_pf_in_twitter.html).                                                                                                                                                                                               |
> | **Callback Endpoint**         | The PingFederate endpoint that Twitter uses to respond to authorization requests.If you set a custom endpoint in the **Authorization callback URL** field in [Registering PingFederate in Twitter](pf_twitter_cic_registering_pf_in_twitter.html), change this field to match.The default value is `/twitter-authn`. |
> | **Error Redirect URL**        | When an error occurs in the adapter, PingFederate redirects the browser to this URL instead of the default error page.This field is blank by default.                                                                                                                                                                |
> | **Unauthorized Redirect URL** | When a user denies the requested Twitter permissions, PingFederate redirects the browser to this URL instead of the default error page.This field is blank by default.                                                                                                                                               |

> **Collapse: Advanced fields**
>
> | Field                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **PingFederate Base URL**                 | The fully-qualified host name, port, and path of the PingFederate server.This URL is used to construct the callback URL sent to Twitter.This field is blank by default.                                                                                                                                                                                                                                                                                 |
> | **Twitter Authentication URL**            | The URL PingFederate uses to send authentication requests to Twitter.If Twitter changes this endpoint, enter the new URL.The default value is `https://api.twitter.com/oauth/authenticate?oauth_token=`.                                                                                                                                                                                                                                                |
> | **Twitter User Data URL**                 | The URL PingFederate uses to retrieve user data from Twitter.The default value is `https://api.twitter.com/1.1/account/verify_credentials.json`.                                                                                                                                                                                                                                                                                                        |
> | **Twitter Access Token Invalidation URL** | The URL PingFederate uses to signal Twitter to invalidate an access token.The default value is `https://api.twitter.com/1.1/oauth/invalidate_token`.                                                                                                                                                                                                                                                                                                    |
> | **Twitter Login Presentation**            | Determines how the adapter presents the Twitter sign-on form:- Redirect (default)
>
>   The adapter redirects the browser to the Twitter sign-on form.
>
> - Pop-up window
>
>   The adapter opens a new window with the Twitter sign-on form on a PingFederate template.
>
>   &#xA;&#xA;Use this option if automatic redirects are blocked by your users' browsers.This setting has no effect when using the adapter through the PingFederate authentication API. |
> | **Twitter Pop-Up Template**               | The template file that presents the Twitter sign-on form.Applies only when **Twitter Login Presentation** is set to **Pop-up window**.The default value is `twitter-pop-up-template.html`.                                                                                                                                                                                                                                                              |
> | **Twitter Post-Auth Template**            | The template file that the adapter presents after the user signs on.Applies only when **Twitter Login Presentation** is set to **Pop-up window**.The default value is `twitter-post-auth-template.html`.                                                                                                                                                                                                                                                |
> | **Twitter Messages File**                 | The language-pack file associated with the Twitter pop-up template.The default value is `pingfederate-twitter-adapter-messages`.                                                                                                                                                                                                                                                                                                                        |
> | **Retry Request**                         | Determines whether PingFederate will retry requests after it receives a response with a failure code.This checkbox is selected by default.                                                                                                                                                                                                                                                                                                              |
> | **Maximum Retries Limit**                 | Determines how many times PingFederate retries a request.The default value is `5`.                                                                                                                                                                                                                                                                                                                                                                      |
> | **Retry Error Codes**                     | A list of response codes that you want to trigger a retry. Separate response codes with a comma.The default value is `429`.                                                                                                                                                                                                                                                                                                                             |
> | **API Request Timeout**                   | The amount of time in milliseconds that PingFederate allows when establishing a connection with Twitter or waiting for a response to a request.A value of `0` disables the timeout.The default value is `2000`.                                                                                                                                                                                                                                         |
> | **Proxy Settings**                        | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                                             |
> | **Custom Proxy Host**                     | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                          |
> | **Custom Proxy Port**                     | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                                               |

---

---
title: Twitter Login Integration Kit
description: The Twitter Login Integration Kit allows PingFederate to use Twitter as an identity provider (IdP). This allows users to access service provider (SP) applications by signing into Twitter.
component: twitter
page_id: twitter::pf_twitter_cic
canonical_url: https://docs.pingidentity.com/integrations/twitter/pf_twitter_cic.html
llms_txt: https://docs.pingidentity.com/integrations/twitter/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Twitter Login Integration Kit

The Twitter Login Integration Kit allows PingFederate to use Twitter as an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*. This allows users to access service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* applications by signing into Twitter.

## Features

* Supports the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

* Twitter IdP Adapter

  * Allows PingFederate to communicate with the Twitter API to process sign-on requests and get user information.

* Templates

  * Allows the adapter to prompt the user to sign on. The template can be presented with a browser redirect or as a pop-up window.

  * Allows you to modify the appearance of the sign-on prompt.

* Language packs

  * Allows you to customize or localize the messages returned by the PingFederate authentication API and shown on the templates during authentication. You can find help in [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

## Intended audience

This document is intended for PingFederate administrators. If you need help during the setup process, refer to the following resources:

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

* The following sections of the Twitter documentation:

  * [Developer portal](https://developer.twitter.com/en/docs/developer-portal/dev-portal-enhancements)

  * [Developer Apps](https://developer.twitter.com/en/docs/apps/overview)

## System requirements

* PingFederate 11.3 or later

* A Twitter developer account