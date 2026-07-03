---
title: Available Docker images
description: PingAuthorize provides official Docker images for its server components and administrative tools.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_available_docker_images
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_available_docker_images.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 21, 2025
page_aliases: ["paz_before_install_using_docker.adoc"]
---

# Available Docker images

PingAuthorize provides official Docker images for its server components and administrative tools. These images are published on Ping Identity's [Docker Hub repository](https://hub.docker.com/u/pingidentity/). You can find deployment guidance, examples, and DevOps automation tools in the Ping Identity [DevOps documentation](https://devops.pingidentity.com/).

The following Docker images are available:

| Image                                                                      | Product                         | Description                                                                                 |
| -------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------- |
| [pingdataconsole](https://hub.docker.com/r/pingidentity/pingdataconsole)   | PingData administrative console | Administrative console for managing the PingAuthorize server.                               |
| [pingauthorize](https://hub.docker.com/r/pingidentity/pingauthorize)       | PingAuthorize                   | Runtime server that evaluates authorization policies.                                       |
| [pingauthorizepap](https://hub.docker.com/r/pingidentity/pingauthorizepap) | PingAuthorize Policy Editor     | Policy administration point (PAP) used to create, test, and version authorization policies. |
| [pingdirectory](https://hub.docker.com/r/pingidentity/pingdirectory)       | PingDirectory                   | Directory server for storing user identities. PingAuthorize doesn't require PingDirectory.  |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only the PingData administrative console, PingAuthorize server, PingAuthorize Policy Editor, and PingDirectory software are licensed under Ping Identity's end-user license agreement. Any other software components contained in the image are licensed solely under the terms of the applicable open source/third party license.Ping Identity accepts no responsibility for the performance of any specific virtualization software and in no way guarantees the performance or interoperability of any virtualization software with its products. |

---

---
title: Before you install manually
description: Prerequisites for manually installing PingAuthorize, including a supported platform, a valid license key, and a Java installation.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_before_install_manually
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_before_install_manually.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
---

# Before you install manually

You must prepare your computing environment by installing certain system requirements before a manual PingAuthorize software installation.

The following components are required to install PingAuthorize:

* Supported Linux or Windows platform

* Valid license key

* Java

The following sections describe these prerequisites in more detail.

---

---
title: Changing the Policy Editor authentication mode
description: Change the Policy Editor authentication mode after initial setup, for both manual and Docker deployments.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_change_pe_authn_mode
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_change_pe_authn_mode.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  changing-the-policy-editor-authentication-mode-for-manual-installs: Changing the Policy Editor authentication mode for manual installs
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  changing-the-policy-editor-authentication-mode-for-docker-deployments: Changing the Policy Editor authentication mode for Docker deployments
  about-this-task-2: About this task
  steps-2: Steps
  example-4: Example:
---

# Changing the Policy Editor authentication mode

Change the Policy Editor's authentication mode after initial setup.

## Changing the Policy Editor authentication mode for manual installs

### About this task

To change the authentication mode that a manually installed PingAuthorize Policy Editor uses, re-run the `setup` tool and choose a different authentication mode. This action overwrites the PingAuthorize Policy Editor's existing configuration.

### Steps

1. Stop the Policy Editor.

   #### Example:

   ```shell
   $ bin/stop-server
   ```

2. Run the `setup` command and select a different authentication mode.

   The modes are:

   * **Demo mode**

     Configures the PingAuthorize Policy Editor to use form-based authentication with a fixed set of credentials. Unlike OIDC mode, this mode does not require an external authentication server. However, it is inherently insecure and is recommended only for demonstration purposes.

   * **OpenID Connect (OIDC) mode**

     Configures the PingAuthorize Policy Editor to delegate authentication and sign-on services to an OpenID Connect provider, such as PingFederate.

     #### Example:

     ```shell
     $ bin/setup
     ```

3. Start the Policy Editor.

   #### Example:

   ```shell
   $ bin/start-server
   ```

## Changing the Policy Editor authentication mode for Docker deployments

### About this task

To switch to OIDC authentication for a Docker deployment of the PingAuthorize Policy Editor, re-run the `docker run` command using the OIDC environment variables.

### Steps

1. Stop the Policy Editor Docker container.

2. Run the Policy Editor Docker container in OIDC mode by using the `PING_OIDC_CONFIGURATION_ENDPOINT` and `PING_CLIENT_ID` environment variables in your `docker run` command, as shown in the following example.

   #### Example:

   |   |                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For proper communication between containers, create a Docker network using a command like `docker network create --driver <network_type> <network_name>`, and then connect to that network with the `--network=<network_name>` option. |

   ```shell
   docker run --network=<network_name>  -p 8443:1443 -d \
   --env-file ~/.pingidentity/config \
   --env PING_EXTERNAL_BASE_URL=localhost:8443 \
   --env PING_CLIENT_ID=c2f081c0-6a2e-4249-b07d-d60234bb5b21 \
   --env PING_OIDC_CONFIGURATION_ENDPOINT=https://auth.pingone.com/3e665735-23da-40a9-a2bb-7ccddc171aaa/as/.well-known/openid-configuration \
   pingidentity/{PAP_CONTAINER_NAME}:<TAG>
   ```

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The Docker image *\<TAG>* used in the example is only a placeholder. For actual tag values, see the [PingAuthorize PAP Docker Image](https://hub.docker.com/r/pingidentity/pingauthorizepap) on Docker Hub. |

---

---
title: Clustering and scaling
description: Scale PingAuthorize Server by running stateless instances behind a network load balancer without intra-cluster communication.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_clustering_scaling
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_clustering_scaling.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  automated-environments: Automated environments
---

# Clustering and scaling

PingAuthorize Servers are stateless. They do not require intra-cluster communication to scale. Instead, similarly configured independent server instances can be added behind the same network load balancer to achieve higher throughput while maintaining low latency.

## Automated environments

To maintain identically configured PingAuthorize Server instances behind your load balancer, use DevOps principles of Infrastructure-as-Code (IaC) and Automation. For more information about using server profiles to scale upward by installing a new, identically configured instance of PingAuthorize Server, see [Deployment automation and server profiles](../pingauthorize_server_administration_guide/paz_deploy_auto_server_prof.html).

---

---
title: Configuring an OIDC provider for single sign-on requests from PingAuthorize
description: Configure an OIDC provider to accept SSO requests from PingAuthorize, with steps for PingOne and PingFederate.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_config_authn_server_openid_connect
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_config_authn_server_openid_connect.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  steps: Steps
  configuring-pingone-as-an-oidc-provider-for-pingauthorize: Configuring PingOne as an OIDC provider for PingAuthorize
  components: Components
  before-you-begin: Before you begin
  config_p1_for_paz: Configuring PingOne for PingAuthorize policy administration
  about-this-task: About this task
  steps-2: Steps
  choose-from: Choose from:
  configuring-pingauthorize-policy-administration-to-use-pingone: Configuring PingAuthorize policy administration to use PingOne
  about-this-task-2: About this task
  steps-3: Steps
  result: Result:
  configuring-pingfederate-as-an-oidc-provider-for-pingauthorize: Configuring PingFederate as an OIDC provider for PingAuthorize
  components-2: Components
  before-you-begin-2: Before you begin
  config_pingfed_for_paz: Configuring PingFederate for PingAuthorize
  about-this-task-3: About this task
  steps-4: Steps
  result-2: Result:
  config_pe_for_pingfed: Configuring the PingAuthorize Policy Editor to use PingFederate
  before-you-begin-3: Before you begin
  steps-5: Steps
  result-3: Result:
  paz_config_pf_group_access: Configuring PingFederate group access for PingAuthorize
  steps-6: Steps
  result-4: Result:
  result-5: Result:
  result-6: Result:
---

# Configuring an OIDC provider for single sign-on requests from PingAuthorize

When you install the PingAuthorize software with OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* authentication, configure an OIDC provider to accept single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* requests from PingAuthorize.

If you chose OIDC mode when you set up the Policy Editor, you must configure an OIDC provider, such as PingFederate or PingOne, to accept sign-on requests from the Policy Editor. Refer to the following tabs for the configuration steps for PingOne and PingFederate.

If you're using another OIDC provider, refer to the provider's documentation for specific client configuration steps. The following steps show the general procedure:

## Steps

1. Use the following configuration values to create an OAuth 2 client that represents the Policy Editor:

   | OAuth 2 client configuration                    | Configuration value                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Client ID**                                   | `pingauthorizepolicyeditor`                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | **Redirect URI**                                | `https://<host>:<port>/idp-callback`                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | **Grant type**                                  | `Authorization Code with PKCE`                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **Response type**                               | `code`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Scopes**                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Refresh tokens**                              | `Enable`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | **Client authentication on the token endpoint** | `Disable`The Policy Editor doesn't have access to the client secret and doesn't send the credential *(tooltip: \<div class="paragraph">&#xA;\<p>Information used to identify a subject for access purposes (for example, username and password). A credential can also be a certificate.\</p>&#xA;\</div>)* to the token endpoint *(tooltip: \<div class="paragraph">&#xA;\<p>One end in a communication channel, typically a URI.\</p>&#xA;\</div>)*. |
   | **Return ID token on refresh grant**            | `true`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | **Always re-roll refresh tokens**               | `true`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When an authentication token expires, the Policy Editor performs a silent renewal, triggering a background process to retrieve a new token from the OIDC provider. For this process to work, you must configure your OIDC provider to issue the refresh token *(tooltip: \<div class="paragraph">&#xA;\<p>A long-lived token used by OAuth clients to obtain a new access token without having to obtain fresh authorization from the resource owner.\</p>&#xA;\</div>)* in the following manner:- Issue an `id_token` as part of the refresh grant.

   - Re-roll the refresh token after each use. The Policy Editor will not use refresh tokens more than once.Because these constraints apply to silent renewal, a misconfiguration of the previous items will still allow you to sign on. After your token expires, though, the application will eject you from your session and redirect you to the sign-on screen. This could cause you to lose unsaved changes in the Policy Editor. |

2. Configure the access tokens and ID tokens issued for the OAuth 2 client with the following claims:

   * `sub`

   * `name`

   * `email`

3. Configure the OIDC provider to accept a cross-origin resource sharing (CORS) origin that matches the Policy Editor's scheme, public host, and port, such as `https://<host>:<port>`.

4. Configure the OIDC provider to issue tokens to the Policy Editor only when the authenticated user is authorized to administer policies according to your organization's access rules.

   |   |                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Sign the tokens with one of the following supported algorithms:- RS256

   - RS384

   - RS512

   - ES256

   - ES384

   - ES512

   - PS256

   - PS384

   - PS512 |

   For PingFederate, this level of authorization is controlled with issuance criteria. Learn more in [Defining issuance criteria for IdP Browser SSO](https://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_defining_issuance_criteria_idp_browser_sso.html) in the PingFederate documentation.

* Configuring PingOne

* Configuring PingFederate

## Configuring PingOne as an OIDC provider for PingAuthorize

To improve security and ensure a consistent authentication experience across all enterprise applications, enable single sign-on (SSO) for the PingAuthorize Policy Editor using PingOne as an OIDC provider.

### Components

* PingOne

* PingAuthorize 9.0 or later

Instructions and screenshots might differ slightly from other product versions. For the latest documentation, refer to the [PingOne documentation](https://docs.pingidentity.com/pingone/p1_cloud__platform_main_landing_page.html).

### Before you begin

* Confirm that PingOne is accessible from the subnet on which the Policy Editor is running.

* Extract the Policy Editor distribution to your specified install location, with appropriate permissions set for write access, for example `/opt/PingAuthorize-PAP`.

### Configuring PingOne for PingAuthorize policy administration

#### About this task

Configure PingOne to authorize external access to the Policy Editor.

#### Steps

1. Sign on to PingOne and click your environment.

   ##### Choose from:

   * If you have an account, go to the URL for your environment. Each environment has a unique URL for signing on that follows the https\://console.pingone.com/?env=\<environmentID> format.

   * If you don't already have a PingOne account, create one at [Try Ping](https://www.pingidentity.com/en/try-ping.html).

2. To create an application in PingOne to represent the Policy Editor, go to **Connections > Applications** and click the **[icon: plus, set=fa]**icon.

3. Enter a name for the application, such as `PingAuthorize Policy Editor`.

4. (Optional) Enter a description and add an icon.

5. Click **OIDC Web App**, and then click **Save**.

6. On the **Configuration** tab, click the **Pencil** icon to edit the settings.

7. In the **PKCE Enforcement** list in the **Grant Type** section, select **S256\_REQUIRED**.

8. In the **Redirect URIs** field, enter a redirect URL that follows the format `https://<pap.hostname:port>/idp-callback`.

9. In the **Token Endpoint Authentication Method** section, click **None**.

10. Click **Save**.

11. On the **Resources** tab, click the pencil icon to edit the settings.

12. In the **Scopes** list, click the **[icon: plus, set=fa]**icon to add the **email** and **profile** scopes to the **Allowed Scopes** list.

13. Click **Save**.

14. Click the toggle to enable the application.

    ![Screen capture of the toggle to enable the Policy Editor application](_images/coo1641513465594.png)

15. Copy the following IDs:

    * **Client ID**: To find the client ID, go to the application's **Profile** tab.

    * **Environment ID**: To find the environment ID, click **Environment** in the left navigation pane.

      |   |                                                                                                 |
      | - | ----------------------------------------------------------------------------------------------- |
      |   | You'll need the client ID and the environment ID to configure the Policy Editor to use PingOne. |

### Configuring PingAuthorize policy administration to use PingOne

#### About this task

The following configuration enables the Policy Editor to use PingOne for authentication.

#### Steps

1. Run the \<PingAuthorize-PAP>`/bin/stop-server` command to stop the Policy Editor.

2. Using the client ID and environment ID from [Configuring PingOne for PingAuthorize policy administration](#config_p1_for_paz), run the following command to configure the Policy Editor:

   ```
   bin/setup oidc \
     --licenseKeyFile <path to PingAuthorize.lic> \
     --generateSelfSignedCertificate \
     --hostname <pap-hostname> --port <pap-port> \
     --adminPort <admin-port> \
     --oidcBaseUrl https://auth.pingone.<regional domain>/<environment id>/as \
     --clientId <client-id>
   ```

3. Run the `bin/start-server` command to start the Policy Editor.

4. Verify that you can sign on to the Policy Editor using the application you created in PingOne:

   1. Go to the Policy Editor.

   2. Click **Click to Sign in**.

      ##### Result:

      Your browser redirects to the URL you set in [Configuring PingOne for PingAuthorize policy administration](#config_p1_for_paz).

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | By default, the signed-on username uses the `sub` JSON Web Token (JWT) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>&#xA;\</div>)* claim for the OIDC *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)* user ID. You can find details on using a non-default claim in [Changing the default JWT claim for the OIDC user ID](../pingauthorize_server_administration_guide/paz_config_jwt_claims.html). |

## Configuring PingFederate as an OIDC provider for PingAuthorize

To improve security and ensure a consistent authentication experience across all enterprise applications, enable single sign-on (SSO) for the PingAuthorize Policy Editor using PingFederate as an OIDC provider.

This document describes one way to configure PingFederate as an OpenID Connect provider for the PingAuthorize Policy Editor. In this example, PingFederate also acts as the identity provider and uses a PingDirectory LDAP server with sample data as the backing store.

### Components

* PingFederate 10.3 or later

* PingDirectory 9.0 or later

* PingAuthorize 9.0 or later

Instructions and screenshots might differ slightly from other product versions. For the latest documentation, refer to the [PingFederate documentation](https://docs.pingidentity.com/pingfederate/latest/pf_pf_landing_page.html) and [PingDirectory documentation](https://docs.pingidentity.com/pingdirectory/latest/pd_ds_landing_page.html).

### Before you begin

Make sure of the following:

* PingFederate is running and accessible from the subnet on which the Policy Editor is running.

* PingDirectory is running and accessible from the subnet on which PingFederate is running.

* PingDirectory is loaded with the identities to be used. This document uses the sample data provided when running the PingDirectory setup command line tool with option `--sampleData 1000`.

* You have extracted the Policy Editor distribution to your specified install location, with appropriate permissions set for write access. This document uses an installation directory of `/opt/PingAuthorize-PAP`.

* If using SSL, the certificate chain is available as a PKCS12 keystore to upload as the server certificate chain for PingFederate.

* The signing certificate for JWT tokens is available for upload to PingFederate.

  |   |                                                                                                                                                                                                                                                                                                        |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If the PingFederate certificate chain contains certificates that are not trusted by the default Java truststore on the system that the Policy Editor is running on, you will need to add them. An example of how to do this is provided in the "Add Certificate to Java Trust Store" subsection below. |

### Configuring PingFederate for PingAuthorize

Configure PingFederate to authorize external access through tokens to the PingAuthorize Policy Editor.

#### About this task

You can also use PingAccess to authorize external access through rules. You can find more information in [Rule Creation in PingAccess](https://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/pa_access_control_rules.html).

The following example configuration assumes that any authenticated user can access the PingAuthorize Policy Editor. You can find more informarion about limiting access to members of a specific group in [Configuring PingFederate group access for PingAuthorize](#paz_config_pf_group_access).

#### Steps

1. In the PingFederate administration console, go to **System > Data & Credential Stores > Data Stores**.

2. Click **Add New Data Store**.

3. On the **Data Store Type** tab, in the **Name** field, enter a name for the data store.

4. From the **Type** list, select **Directory (LDAP)**, and then click **Next**.

5. On the **LDAP Configuration** tab, enter the address and authentication information for PingFederate to use when accessing PingDirectory, and then click **Next**.

6. On the **Summary** tab, review your configuration and click **Save**.

   ![Screen capture of the Summary tab in the Data Stores window, displaying the specified data store configuration](_images/wwt1637687448525.png)

7. Go to **Authentication > Policies > Sessions** and enable authentication sessions. The following example enables authentication sessions for all sources. Make the appropriate change for your environment, and then click **Save**.

   ![Screen capture of the Sessions window with the Track Revoked Sessions on Logout and Enable Authentication Sessions For All Sources checkboxes selected](_images/vdd1639000440193.png)

8. Go to **Security > Certificate & Key Management > SSL Client Keys & Certificates** and import your JWT signing certificate. Click **Save**.

   |   |                                                                                     |
   | - | ----------------------------------------------------------------------------------- |
   |   | PingFederate expects the certificate chain and keys to be encoded in PKCS12 format. |

9. Configure your OAuth server using the OpenID Connect protocol.

   1. Go to **System > OAuth Settings > Scope Management** and create scopes.

   2. In the **Scope Value** field, enter the `email`, `openid`, and `profile` scopes, clicking **Add** after each entry. Click **Save**.

      ![Screen capture of the Common Scopes tab on the Scope Management window, displaying the values of email, openid, and profile added to the Scope Value list](_images/pf_common_scopes_management.png)

   3. Go to **Applications > OAuth > Access Token Management** and click **Create New Instance**.

   4. On the **Type** tab, from the **Type** list, select **JSON Web Tokens**. From the **Parent Instance** list, select **None**. Click **Next**.

   5. On the **Instance Configuration** tab, click **Add a new row to 'Certificates'** and add the previously imported signing certificate. Select the desired signing algorithm and token timeout, and then click **Next**.

   6. On the **Session Validation** tab, enable the session validation options.

      ![Screen capture of the Session Validation tab on the Access Token Management window showing all checkboxes selected](_images/qbu1637792563517.png)

   7. On the **Access Token Attribute Contract** tab, add the attributes to be included in the OAuth access token. This example extends the contract with `cn`, `email`, `scope`, `sub`, and `uid` attributes.

      ![Screen capture of the Access Token Attribute Contract tab on the Access Token Management window, displaying the values of cn, email, scope, sub, and uid added to the Extend the Contract list](_images/mfm1637793365075.png)

   8. Click **Next** until you reach the **Summary** tab, and then click **Save**. Accept the default values for the **Resources URIs** and **Access Control** settings.

   9. Go to **Applications > OAuth > Access Token Mappings** to create an Access Token Mapping in the **Default** context for the Access Token Manager you just created. Click **Add Mapping**, and then click **Add Attribute Source**.

   10. From the **Active Data Store** list, select the PingDirectory data store that you created in step 2. Click **Next**.

       ![Screen capture of the Data Store tab on the Access Token Mappings window, displaying the PingDirectory Data Store selected in the Active Data Store list](_images/dcz1637796417045.png)

   11. On the **LDAP Directory Search** tab, in the **Base DN** field, enter the base DN for the PingDirectory data that provides your identities.

   12. In the **Attributes to return from search** section, click **Add Attribute** and enter the attributes to be retrieved.

       The sample data uses `ou=People,dc=example,dc=com` and the configuration shown in the following image retrieves the `cn`, `mail`, and `uid` attributes.

       ![Screen capture of the LDAP Directory Search tab on the Access Token Attribute Mapping window, with the Base DN set to ou=People,dc=example,dc=com and the attributes cn, mail, and uid added to the Attribute list](_images/seo1638916833093.png)

   13. On the **LDAP Filter** tab, in the **Filter** field, enter `uid=${USER_KEY}` to match the PingDirectory sample data with the authenticating user information.

       ![Screen capture of the LDAP Filter tab on the Access Token Attribute Mapping window with a Filter field entry of uid=${USER\_KEY}](_images/sta1638917408619.png)

   14. Click **Next** and **Save** on the **Summary** tab.

   15. On the **Contract Fulfillment** tab, fulfill the contract with the LDAP attributes from the PingDirectory data store. Leave the remaining settings as their defaults and click **Save**.

       The scope attribute is fulfilled from the OAuth context.

       ![Screen capture of the Contract Fulfillment tab on the Access Token Attribute Mapping window, with the cn, email, sub, and uid contracts configured for a Source of LDAP (PingDirectory) and Values of cn, mail, uid, and uid, respectively. The scope contract has a source of Context and a Value of Scope.](_images/nbo1638917948586.png)

   16. Go to **Applications > OAuth > OpenID Connect Policy Management** and click **Add Policy**.

   17. In the **Manage Policy** tab, from the **Access Token Manager** list, select the access token manager you previously created.

   18. Ensure that the **Include User Info in ID Token** checkbox is selected. Click **Next**.

   19. On the **Attribute Contract** tab, extend the policy contract with the `email` and `name` attributes. Click **Next**.

   20. On the **Attribute Scopes** tab, map the previously defined `email` and `profile` scopes to the `email` and `name` ID token attributes. Click **Next**.

       ![Screen capture of the Attribute Scopes tab on the Policy Management window, with the email attribute mapped to the email scope, and the name attribute mapped to the profile scope](_images/txo1638952158647.png)

   21. On the **Contract Fulfillment** tab, fulfill the contract with the values in the access token. Click **Next** until you reach the **Summary** tab, and then click **Save**.

       ![Screen capture of the Contract Fulfillment tab on the OpenID Connect Policy Management window, with the Attribute Contracts of email, name, and sub set to a Source of Access Token and Value selections of email, cn, and sub, respectively.](_images/hvu1638951288581.png)

   22. Click **Set as Default** to set the newly created policy as the default policy.

   23. Go to **Applications > OAuth > Clients** and click **Add Client**.

       To provide the Policy Editor with appropriate defaults, configure PingFederate with a **Client ID** of `pingauthorize-pap` and select the **Authorization Code** checkbox in the **Allowed Grant Types** section. From the **Default Access Token Manager** list, select the JWT Manager created earlier, and in the **Redirection URIs** field, add the correct callback URL for the Policy Editor, such as <https://pap.example.com:9443/idp-callback>.

       Click **Save**.

   24. Go to **Authentication > OAuth > IdP Adapter Grant Mapping** and create a new Form Adapter Mapping, fulfilling the contracts for `USER_NAME` and `USER_KEY` with the **username** form field. Click **Next** and **Save** on the **Summary** tab.

       ![Screen capture of the Contract Fulfillment tab on the IdP Adapter Grant Mapping window, with the USER\_KEY and USER\_NAME contracts set to a Source of Adapter and a Value of username](_images/rjp1638944892132.png)

   25. Because this PingFederate instance uses a different domain from the Policy Editor, you must modify the PingFederate CORS settings. Go to **System → OAuth Settings → Authorization Server Settings**. In the **Cross-Origin Resource Sharing Settings** section, enter the domain for the Policy Editor in the **Allowed Origin** field. Click **Add** and then **Save**.

       ![Screen capture of the Cross-Origin Resource Sharing Settings section showing a URL of https://pap.example.com:8080 added to the Allowed Origin field](_images/hdm1576709957649.png)

       ##### Result:

       PingFederate is configured to handle OpenID Connect requests.

## Configuring the PingAuthorize Policy Editor to use PingFederate

Configure the Policy Editor to use PingFederate for authentication.

### Before you begin

Configure PingFederate to handle OpenID Connect requests as described in [Configuring PingFederate for PingAuthorize](#config_pingfed_for_paz).

### Steps

1. Add the certificate to the Java Trust Store.

   If the certificate chain added to PingFederate uses an intermediate certificate authority that is not trusted by the default Java trust store, you must add the certificate. Use the following command (root permissions are usually required). `$JAVA_HOME` must be defined as the installation location of the JVM on which the Policy Editor will run.

   ```
   keytool -import \
   -file /path/to/IntermediateCA.cer \
   -keystore $JAVA_HOME/jre/lib/security/cacerts \
   -storepass changeit
   ```

2. Reconfigure PingAuthorize to point unauthenticated users to PingFederate.

   1. Stop the application.

      ```
      $ bin/stop-server
      The server was successfully stopped.
      ```

   2. Re-run `bin/setup` to reconfigure the application.

   3. Select OpenID Connect to configure the Policy Editor.

      ```
      [/opt/{pingauthorize}-PAP]$ bin/setup

      There is an existing configuration file at /config/configuration.yml. Overwrite? (yes /
      no) [no]: yes
      Detected valid license file in server root  {pingauthorize}.lic

       {pingauthorize}  Policy Editor
      ============================================

      How would you like to configure the Policy Editor?

          1)  Quickstart (DEMO PURPOSES ONLY): This option configures the server with a form based authentication and
              generates a self-signed server certificate
          2)  OpenID Connect: This option configures the server to use an OpenID Connect provider such as PingFederate
          3)  Cancel the setup

      Enter option [1]:  2

      On which port should the Policy Editor listen for HTTPS communications? [9443]:

      Enter the fully qualified host name or IP address that users' browsers will use to connect to this GUI [pap.example.com]: pap.example.com
      ```

   4. Ensure that the PingFederate discovery endpoint uses the public DNS name of the PingFederate server. In this example, the Policy Editor uses a self-signed SSL certificate.

      ```
      Enter the port of the OpenID Connect provider [9031]:

      Enter the fully qualified host name or IP address of the OpenID Connect provider [pap.example.com]:  pf.example.com

      Certificate server options:

          1)  Generate self-signed certificate (recommended for testing purposes only)
          2)  Use an existing certificate located on a Java Keystore (JKS)
          3)  Use an existing certificate located on a PKCS12 keystore

      Enter option [1]:

      There already exists a keystore at /config/keystore.p12. Do you want to delete it? (yes / no) [no]:  yes
      ```

   5. Follow the remaining prompts.

      ```
         Setup Summary
      =======================================
      Host Name:        pap.example.com
      Server Port:      9443
      Secure Access:    Self-signed certificate
      Admin Port:       9444
      Periodic Backups: Enabled
      Backup Schedule:  0 0 0 * * ?

      Command-line arguments that would set up this server non-interactively:
          setup oidc --pkcs12KeyStorePath config/keystore.p12 --licenseKeyFile  {pingauthorize}.lic \
               --oidcHostname pf.example.com --oidcPort 9031 --certNickname server-cert --backupSchedule '0 0 0 * * ?' \
               --hostname pap.example.com --port 9443 --generateSelfSignedCertificate --adminPort 9444

      What would you like to do?

          1)  Set up the server with the parameters above
          2)  Provide the setup parameters again
          3)  Cancel the setup

      Enter option [1]:

      Setup completed successfully

      Please configure the following values
      =============================================================================================
       {pingauthorize}  Server - Policy External Server
        Base URL:                                         https://pap.example.com:9443
        Shared Secret:                                    2222142a754f4838ad1e3dccb6e93940
        Trust Manager Provider:                           Blind Trust

      PingFederate - OAuth Client Config
        Client ID:                                        pingauthorizepolicyeditor
        CORS Allowed Origin:                              https://pap.example.com:9443
        Redirect URL:                                     https://pap.example.com:9443/idp-callback

      Please start the server by running bin/start-server
      ```

   6. Restart the application by running `bin/start-server`.

3. Verify that you can log into the Policy Editor using OpenID Connect provided by PingFederate.

   1. Go to the Policy Editor, for example, https\://pap.example.com:9443. Your browser should be redirected into the OAuth flow.

   2. Click **Click to Sign In**.

   3. Sign on with your user name and password.

      The sample configuration in this document creates an identity with the user name `user.20` and password `password`.

   4. Once authenticated, PingFederate will prompt the user with the scopes associated with the OAuth client. Check all of them to continue.

      ![Screen capture of the Request for Approval window with all scope check boxes selected and the Allow button at the bottom center](_images/mey1576519666160.png)

      #### Result:

      You are now authenticated and authorized to view the Policy Editor.

## Configuring PingFederate group access for PingAuthorize

Configure PingFederate so that only members of a specific LDAP group are authorized to access the application.

[Configuring PingFederate for PingAuthorize](#config_pingfed_for_paz) and [Configuring the PingAuthorize Policy Editor to use PingFederate](#config_pe_for_pingfed) explain how to configure the PingAuthorize Policy Editor and PingFederate so that any authenticated user can access the Policy Editor. This task describes how to configure PingFederate to limit access to a specific LDAP group.

### Steps

1. Create an LDAP group in PingDirectory and add the desired user (`user.20`) to the group.

   1. Create a file named `create-policy-writer-group.ldif` and add the following.

      ```
      dn: ou=groups,dc=example,dc=com
      objectclass: top
      objectclass: organizationalunit
      ou: groups

      dn: cn=PolicyWriter,ou=groups,dc=example,dc=com
      objectclass: top
      objectclass: groupOfUniqueNames
      cn: PolicyWriter
      ou: groups
      uniquemember: uid=user.20,ou=People,dc=example,dc=com
      ```

   2. Use the PingDirectory `ldapmodify` tool to load the newly created `ldif` file.

      ```
      /opt/PingDirectory/bin/ldapmodify -a -f create-policy-writer-group.ldif
      ```

2. Add the group membership claim requirement in PingFederate.

   1. In the PingFederate console, go to **Applications > OAuth > Access Token Mappings**.

   2. Select the PingDirectory mapping from the list, and then on the **Attribute Sources & User Lookup** tab, select the PingDirectory source.

   3. Click the **LDAP Directory Search** tab, and in the **Root Object Class** list, select **Show All Attributes**.

   4. Add the **isMemberOf** attribute, and then click **Done** to return to **Access Token Attribute Mapping**.

      ![Screen capture of the LDAP Directory Search tab on the Access Token Attribute Mapping window with isMemberOf added as specified and the Save button in the lower right](_images/okn1639609156619.png)

   5. Go to the **Issuance Criteria** tab and add a new row with the following values:

      | Column             | Value                                           |
      | ------------------ | ----------------------------------------------- |
      | **Source**         | **LDAP (pingdir)**                              |
      | **Attribute Name** | **isMemberOf**                                  |
      | **Condition**      | **multi-value contains (case sensitive)**       |
      | **Value**          | **cn=PolicyWriter,ou=groups,dc=example,dc=com** |

      ![Screen capture of the Issuance Criteria tab on the Access Token Attribute Mapping window with the previously described attributes added](_images/kbs1639611344459.png)

   6. Click **Save**.

      #### Result:

      Only `user.20` can access the PingAuthorize Policy Editor.

3. Verify that only specified users can access the PingAuthorize Policy Editor.

   |   |                                                                |
   | - | -------------------------------------------------------------- |
   |   | Clear any active SSO sessions before you sign on as each user. |

   1. Sign on as `user.0`.

      #### Result:

      Access is denied.

   2. Sign on as `user.20`.

      #### Result:

      Access is granted.

---

---
title: Creating a Java installation dedicated to PingAuthorize
description: Create a dedicated JDK installation for PingAuthorize Server to isolate it from system-wide Java updates.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_create_java_install_dedicated
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_create_java_install_dedicated.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating a Java installation dedicated to PingAuthorize

Create a Java installation for PingAuthorize Server using the Java Development Kit (JDK) *(tooltip: \<div class="paragraph">
\<p>A development environment for building applications and components using Java.\</p>
\</div>)*.

## About this task

PingAuthorize Server requires Java for 64-bit architectures. Even if Java is already installed on your system, you should create a separate Java installation for PingAuthorize Server. This setup ensures that updates to the system-wide Java installation do not inadvertently impact PingAuthorize Server.

|   |                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This setup requires that you install the JDK, rather than the Java Runtime Environment (JRE) *(tooltip: \<div class="paragraph">&#xA;\<p>A software layer that provides the class libraries and resources needed for a Java program to run.\</p>&#xA;\</div>)*. |

## Steps

1. Download and install a JDK.

2. Set the `JAVA_HOME` environment variable to the Java installation directory path.

3. Add the `bin` directory to the `PATH` environment variable.

---

---
title: Deploying PingAuthorize Server and Policy Editor using Docker
description: Deploy PingAuthorize Server and Policy Editor using Docker images, with optional administrative console and user store setup.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_install_server_pe_docker
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_install_server_pe_docker.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  steps: Steps
  next-steps: Next steps
  paz_install_docker: Deploying PingAuthorize Server using Docker
  about-this-task: About this task
  steps-2: Steps
  pe_install_docker: Deploying the Policy Editor using Docker
  about-this-task-2: About this task
  steps-3: Steps
  choose-from: Choose from:
---

# Deploying PingAuthorize Server and Policy Editor using Docker

Instead of manual software installation, you can run Docker images of the PingAuthorize Server and Policy Editor.

To start the setup process after you obtain the Docker images:

## Steps

1. Run the [PingAuthorize Server](#paz_install_docker) container, `pingauthorize`.

2. Run the [Policy Editor](#pe_install_docker) container, `pingauthorizepap`.

3. (Optional) To configure PingAuthorize with a GUI, run the PingAuthorize administrative console container, `pingdataconsole`.

4. (Optional) If you need user-level control of the data, set up a user store.

   If you use PingDirectory, run the `pingdirectory` container.

## Next steps

* Perform [Post-setup steps (Docker deployment)](paz_post_setup_docker.html).

* Perform [Next steps](paz_install_next_steps.html) as needed.

## Deploying PingAuthorize Server using Docker

Perform a PingAuthorize Server deployment by running a Docker image.

### About this task

The following command uses the `~/.pingidentity/config` environment file to configure common environment variables. See [Get Started](https://devops.pingidentity.com/get-started/introduction/).

### Steps

* Run the following command.

  ```shell
  docker run --network=<network_name>  \
     --env-file ~/.pingidentity/config \
     --name  {SERVER_CONTAINER_NAME}  \
     --publish 1389:1389 \
     --publish 8443:1443 \
     --detach \
     --env SERVER_PROFILE_URL=https://github.com/pingidentity/pingidentity-server-profiles.git \
     --env SERVER_PROFILE_PATH=getting-started/{SERVER_CONTAINER_NAME}  \
     --tmpfs /run/secrets \
    pingidentity/{SERVER_CONTAINER_NAME}:<TAG>
  ```

  The Docker image *\<TAG>* used in the example is only a placeholder. For actual tag values, see [Docker Hub](https://hub.docker.com/r/pingidentity/pingauthorize).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * For proper communication between containers, create a Docker network using a command, such as `docker network create --driver <network_type> <network_name>`, and then connect to that network with the `--network=<network_name>` option.

  * You can use server profiles to automate deployment of PingAuthorize Server. For more information, see [Deployment automation and server profiles](../pingauthorize_server_administration_guide/paz_deploy_auto_server_prof.html). |

## Deploying the Policy Editor using Docker

Deploy the Policy Editor by running its Docker image. Using Docker DevOps enables the automated policy database update feature with mounted volumes.

### About this task

When running the Ping Identity DevOps `pingauthorizepap` Docker container, you can use the following commands to ensure that the policy database is on the mounted volume in preparation for future versions of the image. The commands:

* Run a `pingauthorizepap` Docker container named `pap` on host port 8443.

* Use the `~/.pingidentity/config` environment file to configure common environment variables. See [Get Started](https://devops.pingidentity.com/get-started/introduction/).

* Bind mount a customized `options.yml` file named `custom-options.yml` to the server root using the server profile capability. The host system `server-profile` folder must contain `instance/custom-options.yml` for this example to work correctly. See <https://devops.pingidentity.com/reference/config/>.

* Set the `Ping_Options_File` environment variable to tell `setup` to use `custom-options.yml`.

For an H2 database, the command:

* Bind-mounts a volume that maps a policy database to `/opt/out/Symphonic.mv.db`.

* Sets the `PING_H2_FILE` environment variable to tell `setup` to use `/opt/out/Symphonic.mv.db` for the policy database. The environment variable must exclude the `.mv.db` extension.

To use a PostgreSQL policy database, make sure you have met the following prerequisites:

* The PostgreSQL instance must be reachable on the network from the Policy Editor host and listening for connections.

* The Policy Editor uses both a PostgreSQL administration user and a server runtime user. Have a database administrator create both users before providing their credentials to the `policy-db` tool. The administration user must be able to create new databases. When new releases of the Policy Editor become available, continue using the same administration user to prevent database object ownership issues.

  Learn more about creating new database users and configuring PostgreSQL to listen for remote connections securely in the [PostgreSQL documentation](https://www.postgresql.org/docs/).

* The Policy Editor uses Java Database Connectivity (JDBC) to connect to PostgreSQL. Be prepared to provide the JDBC connection string in the following format: `jdbc:postgresql://<host>:<port>/<name>`. For example: `jdbc:postgresql://example.com:5432/pap_db`

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - The Ping Identity DevOps Docker image documentation is frequently updated as new features are released. For the most recent instructions about running the Docker images, see <https://devops.pingidentity.com/>.

- For proper communication between containers, create a Docker network using a command such as `docker network create --driver <network_type> <network_name>`, and then connect to that network with the `--network=<network_name>` option.

- The Docker image *\<TAG>* used in the example is only a placeholder. For actual tag values, see [Docker Hub](https://hub.docker.com/r/pingidentity/pingauthorizepap). |

### Steps

* Run the `pingauthorizepap` Docker container.

  #### Choose from:

  * If you are using an H2 database, run the following command.

    ```shell
    $ docker run --network=<network_name>  --name pap -p 8443:1443 \
      --env-file ~/.pingidentity/config \
      --volume /home/developer/pap/server-profile:/opt/in/ \
      --env PING_OPTIONS_FILE=custom-options.yml \
      --volume /home/developer/pap/Symphonic.mv.db:/opt/out/Symphonic.mv.db \
      --env PING_H2_FILE=/opt/out/Symphonic \
      pingidentity/{PAP_CONTAINER_NAME}:<TAG>
    ```

  * If you are using a PostgreSQL database, run the following command.

    The official `pingauthorizepap` Docker image detects whether a PostgreSQL database needs to be created or upgraded when you provide the `PING_POLICY_DB_SYNC=true` environment variable along with the database connection string, database administration credentials, and server runtime credentials.

    ```shell
    $ docker run --network=<network_name>  --name pap -p 8443:1443 \
      --env PING_POLICY_DB_SYNC=true \
      --env PING_DB_CONNECTION_STRING="jdbc:postgresql://<host>:<port>/<database>" \
      --env PING_DB_ADMIN_USERNAME="<admin-username>" \
      --env PING_DB_ADMIN_PASSWORD="<admin-password>" \
      --env PING_DB_APP_USERNAME="<username>" \
      --env PING_DB_APP_PASSWORD="<password>" \
      --env-file ~/.pingidentity/config \
      --volume /home/developer/pap/server-profile:/opt/in/ \
      --env PING_OPTIONS_FILE=custom-options.yml \
      --detach \
      --tmpfs /run/secrets \
      pingidentity/pingauthorizepap:<tag>
    ```

    |   |                                                                                                                                                                                                                |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | The `PING_DB_APP_PASSWORD` and `PING_DB_ADMIN_PASSWORD` can instead be provided as Vault secrets or through a secrets volume. See [Using Hashicorp Vault](https://devops.pingidentity.com/how-to/usingVault/). |

---

---
title: Docker deployment
description: You can deploy PingAuthorize using official Docker images to create consistent, repeatable environments that support DevOps workflows.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_docker_install
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_docker_install.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 21, 2025
---

# Docker deployment

You can deploy PingAuthorize using official Docker images to create consistent, repeatable environments that support DevOps automation and CI/CD workflows. Docker deployments simplify installation, reduce configuration drift, and make it easier to create new instances for development, testing, and production.

Ping Identity provides Docker images for the PingAuthorize server, PingAuthorize Policy Editor, administrative console, and optional supporting services. Before deployment, review the following:

* [System requirements](paz_system_requirements.html)

* [Available Docker images](paz_available_docker_images.html)

* [DevOps at Ping Identity](https://developer.pingidentity.com/devops/devops-landing-page.html)

---

---
title: Installing PingAuthorize
description: Overview of PingAuthorize installation methods — Docker for DevOps environments or manual installation for direct control.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_install_pingauthorize
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_install_pingauthorize.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
---

# Installing PingAuthorize

You can install PingAuthorize manually or deploy it with Docker.

| Installation method | Recommended for                                                                                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Docker              | Server administrators familiar with Docker who want to use orchestration to manage their environments.Learn more in [Docker deployment](paz_docker_install.html).                           |
| Manual              | Server administrators familiar with their operating systems who want to tweak and maintain their environments themselves.Learn more in [Manual installation](paz_manual_installation.html). |

Learn more about the available implementation architectures and development environments for your PingAuthorize installation in [PingAuthorize architectural overview](../paz_architecture_overview.html).

---

---
title: Installing the PingAuthorize Policy Editor manually
description: Install the PingAuthorize Policy Editor manually using interactive or noninteractive mode, with H2 or PostgreSQL as the policy database.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_install_pe_manually
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_install_pe_manually.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Installing the PingAuthorize Policy Editor manually

Choose the database for your fine-grained access control use case, protected resource *(tooltip: \<div class="paragraph">
\<p>Information, typically accessed through a web URL, that is protected by an access management system.\</p>
\</div>)*, and computing environment and install the PingAuthorize Policy Editor.

## About this task

You can install the PingAuthorize Policy Editor in one of two ways: interactively or noninteractively.

## Steps

1. Choose the database to use:

   ### Choose from:

   * H2: The default embedded database.

   * PostgreSQL: This is optional and requires additional configuration.

2. **Optional:** If you are using a PostgreSQL database, set up the database.

   For more information, see [Setting up a PostgreSQL database](paz_set_up_postgresql_database.html).

3. Install the PingAuthorize Policy Editor:

   ### Choose from:

   * Interactive: The `setup` tool prompts you for information during the installation process.

     For more information, see [Installing the Policy Editor interactively](paz_install_pe_interactive.html).

   * Noninteractive: Automated installation allows more control over configuration. If you are using a PostgreSQL database, you must use this mode.

     For more information, see [Installing the Policy Editor non-interactively](paz_install_pe_noninteractive.html).

---

---
title: Installing the Policy Editor interactively
description: Install the Policy Editor interactively using the setup command-line tool in demo or OIDC authentication mode.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_install_pe_interactive
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_install_pe_interactive.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  example: Example
  next-steps: Next steps
  install_pe_interactive: "Example: Installing and configuring the Policy Editor interactively"
  about-this-task: About this task
  steps-2: Steps
  result: Result
  next-steps-2: Next steps
---

# Installing the Policy Editor interactively

You can run the Policy Editor `setup` command interactively in command-line interface (CLI) install mode.

The `setup` tool prompts you interactively for the information that it needs.

|   |                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You cannot configure some setup options when installing the Policy Editor interactively, such as PostgreSQL database configuration. Learn more in [Installing the Policy Editor non-interactively](paz_install_pe_noninteractive.html). |

## Before you begin

You must have the following information:

* The location of a valid license file

* An available port for the Policy Editor to accept HTTPS requests

## Steps

1. Choose the authentication mode for the Policy Editor:

   ### Choose from:

   * **Demo mode**: Configures the Policy Editor to use form-based authentication with a fixed set of credentials. Unlike OpenID Connect (OIDC) mode, this mode doesn't require an external authentication server. However, it is inherently insecure and should only be used for demonstration purposes.

   * **OIDC mode**: Configures the Policy Editor to delegate authentication and sign-on services to a PingFederate OIDC provider.

     In OIDC mode, you must provide the following additional information:

     * The host name and port of an OIDC provider

     * Information related to the server's connection security, including the location of a keystore that contains the server certificate, the nickname of that server certificate, and the location of a trust store

       |   |                                                                                                                                                            |
       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | To use Policy Editor with other OIDC providers, such as PingOne, see [Installing the Policy Editor non-interactively](paz_install_pe_noninteractive.html). |

2. Run the `setup` command.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you don't want to use the default database credential *(tooltip: \<div class="paragraph">&#xA;\<p>Information used to identify a subject for access purposes (for example, username and password). A credential can also be a certificate.\</p>&#xA;\</div>)*, refer to [Setting database credentials at initial setup](../pingauthorize_server_administration_guide/paz_set_db_creds_startup.html). |

3. Copy and record any generated values needed to configure external servers.

   The Shared Secret is used in PingAuthorize, under **External Servers > Policy External Server > Shared Secret**.

4. To start the Policy Editor, or policy administration point (PAP), run `bin/start-server`.

   The Policy Editor runs in the background, so you can close the terminal window in which it was started without interrupting it.

## Example

Refer to [Example: Installing and configuring the Policy Editor interactively](#install_pe_interactive) for a more detailed walkthrough of the previous steps.

## Next steps

1. Complete the steps in [Post-setup steps (manual installation)](paz_post_setup_manual.html).

2. Consider additional configuration options in [Specifying custom configuration with an options file](../pingauthorize_server_administration_guide/paz_specify_custom_config_opts_file.html).

## Example: Installing and configuring the Policy Editor interactively

This tutorial describes how to install an instance of the PingAuthorize Policy Editor interactively.

### About this task

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | These installation instructions are for tutorial purposes. They will only provide a limited install. |

### Steps

1. Extract the contents of the compressed PingAuthorize-PAP distribution file.

2. Change the directory to `PingAuthorize-PAP`.

3. To configure the application, run the `./bin/setup` script.

4. Answer the on-screen questions.

   For the following questions, use the recommended answers provided.

   | Question                                                                                               | Answer                                                                                                                                                                      |
   | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | How would you like to configure the Policy Editor?                                                     | Use `Quickstart` to set up a demo server with credentials `admin`/`password123` and to use a self-signed certificate for SSL                                                |
   | On which port should the Policy Editor listen for HTTPS communications?                                | You can use any unused port here, but most of the examples in this guide assume that port 9443 is used for the PingAuthorize Policy Editor.                                 |
   | Enter the fully qualified host name or IP address that users' browsers will use to connect to this GUI | Unless you are testing on `localhost`, ensure that the provided API URL uses the public DNS name of the PingAuthorize Policy Editor server. For example, `pap.example.com`. |

5. Copy and record any generated values needed to configure external servers.

   The Shared Secret is used in PingAuthorize, under **External Servers → Policy External Server → Shared Secret**.

6. To start the Policy Editor, or policy administration point (PAP), run `bin/start-server`.

   The Policy Editor runs in the background, so you can close the terminal window in which it was started without interrupting it.

### Result

Your demo configuration should resemble the following example.

```
[/opt/{pingauthorize}-PAP]$ bin/setup

Please enter the location of a valid  {pingauthorize}  with Symphonic license file
[/opt/{pingauthorize}-PAP/{pingauthorize}.lic]: /opt/{pingauthorize}/{pingauthorize}.lic

{pingauthorize}  Policy Editor
============================================

How would you like to configure the Policy Editor?

    1)  Quickstart (DEMO PURPOSES ONLY): This option configures the server with a form
        based authentication and generates a self-signed server certificate
    2)  OpenID Connect: This option configures the server to use an OpenID Connect
        provider such as  {pingfed}
    3)  Cancel the setup

Enter option [1]: 1

On which port should the Policy Editor listen for application HTTPS communications? [9443]: 9443

Enter the fully qualified host name or IP address that users' browsers will use to
connect to this GUI [centos.localdomain]: pap.examplecom

On which port should the Policy Editor listen for administrative HTTPS communications? [9444]: 9444

Would you like to enable periodic policy database backups? (yes / no) [yes]: yes

Enter the backup schedule as a cron expression (defaults to daily at midnight): [0 0 0 * * ?]: 0 0 0 * * ?

Setup Summary
==========================================
Host Name:         pap.example.com
Server Port:       9443
Secure Access:     Self-signed certificate
Admin Port:        9444
Periodic Backups:  Enabled
Backup Schedule:   0 0 0 * * ?

Command-line arguments that would set up this server non-interactively:
    setup demo --hostname pap.example.com --adminPort 9444 --port 9443 --certNickname server-cert \
         --licenseKeyFile /opt/{pingauthorize}/{pingauthorize}.lic \
         --backupSchedule '0 0 0 * * ?' --pkcs12KeyStorePath config/keystore.p12 \
         --generateSelfSignedCertificate

What would you like to do?

    1)  Set up the server with the parameters above
    2)  Provide the setup parameters again
    3)  Cancel the setup

Enter option [1]:

Setup completed successfully

Please configure the following values
====================================================================================
 {pingauthorize}  Server - Policy External Server
  Base URL:                                         https://pap.example.com:9443
  Shared Secret:                                    7ed6f52d6e71411ca9e58f9567c7de2e
  Trust Manager Provider:                           Blind Trust

Please start the server by running bin/start-server
```

In this example, the PingAuthorize Policy Editor is now running and listening on port 9443.

### Next steps

To sign on to the interface, go to `https://<host>:9443`. The default credentials are `admin` and `password123`.

|   |                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the default user name and password sign on credentials for demo and testing purposes only, such as this initial walk-through. To configure the PingAuthorize Policy Editor for PingFederate OpenID Connect (OIDC) single sign-on (SSO), see [Installing the Policy Editor non-interactively](paz_install_pe_noninteractive.html). |

---

---
title: Installing the Policy Editor non-interactively
description: For an automated software installation, run bin/setup in non-interactive command-line interface mode.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_install_pe_noninteractive
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_install_pe_noninteractive.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 22, 2026
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
  authentication_mode_setup_examples: Authentication mode examples
  example-set-up-the-pingauthorize-policy-editor-in-oidc-mode-pingfederate: "Example: Set up the PingAuthorize Policy Editor in OIDC mode (PingFederate)"
  example-set-up-the-pingauthorize-policy-editor-in-oidc-mode-generic-oidc-provider: "Example: Set up the PingAuthorize Policy Editor in OIDC mode (generic OIDC provider)"
  example-set-up-the-pingauthorize-policy-editor-in-oidc-mode-custom-scope: "Example: Set up the PingAuthorize Policy Editor in OIDC mode (custom scope)"
  add-oidc-scopes-during-setup: Add OIDC scopes during setup
  add-oidc-scopes-at-startup: Add OIDC scopes at startup
  example-set-up-the-pingauthorize-policy-editor-in-oidc-mode-self-governance: "Example: Set up the PingAuthorize Policy Editor in OIDC mode (self-governance)"
  example-set-up-the-pingauthorize-policy-editor-in-demo-mode: "Example: Set up the PingAuthorize Policy Editor in demo mode"
  example-set-up-the-pingauthorize-policy-editor-with-a-postgresql-policy-database: "Example: Set up the PingAuthorize Policy Editor with a PostgreSQL policy database"
  example-set-up-the-pingauthorize-policy-editor-to-use-a-custom-ssl-certificate: "Example: Set up the PingAuthorize Policy Editor to use a custom SSL certificate"
  example-set-up-the-pingauthorize-policy-editor-in-demo-mode-self-governance: "Example: Set up the PingAuthorize Policy Editor in demo mode (self-governance)"
---

# Installing the Policy Editor non-interactively

For an automated software installation, run `bin/setup` in non-interactive command-line interface (CLI) mode.

You must run `bin/setup` in non-interactive CLI mode instead of interactive mode to do any of the following:

* Configure the Policy Editor with a policy configuration key.

* Configure a key store for a policy information provider.

* Configure a trust store for a policy information provider.

* Customize the Policy Editor's logging behavior.

* Configure the Policy Editor for a PostgreSQL database.

* Configure the Policy Editor to present an existing SSL *(tooltip: \<div class="paragraph">
  \<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>
  \</div>)* certificate *(tooltip: \<div class="paragraph">
  \<p>A digital file used for identity verification and other security purposes. The certificate, which is often issued by a CA, contains a public key, which can be used to verify the originator's identity.\</p>
  \</div>)* instead of generating a self-signed certificate.

* Enable [self-governance](../pingauthorize_policy_administration_guide/paz_self_gov.html).

* Enable [Camel services](../pingauthorize_policy_administration_guide/paz_camel_enable.html).

Learn more in [Specifying custom configuration with an options file](../pingauthorize_server_administration_guide/paz_specify_custom_config_opts_file.html).

## Before you begin

To use a PostgreSQL policy database, you must [set up the database](paz_set_up_postgresql_database.html) before you install the Policy Editor.

After you set up your PostgreSQL policy database, save the following information for installing the Policy Editor:

* The PostgreSQL JDBC *(tooltip: \<div class="paragraph">
  \<p>A Java API that allows Java programs to interact with databases.\</p>
  \</div>)* connection string, with the host, port, and database name

* The server runtime credential *(tooltip: \<div class="paragraph">
  \<p>Information used to identify a subject for access purposes (for example, username and password). A credential can also be a certificate.\</p>
  \</div>)* provided through the `policy-db` tool

## Steps

1. Choose one of the following authentication modes for the Policy Editor:

   * **Demo mode**: Configures the Policy Editor to use form-based authentication with a fixed set of credentials. Unlike OIDC *(tooltip: \<div class="paragraph">
     \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
     \</div>)* mode, this mode doesn't require an external authentication server.

     |   |                                                                                      |
     | - | ------------------------------------------------------------------------------------ |
     |   | This mode is inherently insecure. You should only use it for demonstration purposes. |

   * **OIDC mode**: Configures the Policy Editor to delegate authentication and sign-on services to an OIDC provider, such as PingFederate.

     If you choose OIDC mode, you must provide the host name and port of an OIDC provider or its base URL.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you don't use the `setup` tool to generate a self-signed certificate, you must also provide information related to the Policy Editor's connection security, including the location of a keystore that contains the server certificate and the certificate's nickname.If the OIDC provider presents a certificate that isn't trusted by the Policy Editor's Java Runtime Environment (JRE) *(tooltip: \<div class="paragraph">&#xA;\<p>A software layer that provides the class libraries and resources needed for a Java program to run.\</p>&#xA;\</div>)*, do one of the following:- Add the certificate to the JRE trust store. Learn more in [Configuring an OIDC provider for single sign-on requests from PingAuthorize](paz_config_authn_server_openid_connect.html).

     - Disable certificate validation by starting the Policy Editor with the `PING_OIDC_TLS_VALIDATION` environment variable set to `NONE`. |

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The `setup` tool's `--help` option displays the options available for a non-interactive installation.The following table describes the available CLI help options for the `setup` tool:> **Collapse: CLI help options**
     >
     > Command	Description&#xA;&#xA;$ bin/setup --help&#xA;&#xA;&#x9;&#xA;&#xA;General options for running setup&#xA;&#xA;&#xA;&#xA;&#xA;$ bin/setup demo --help&#xA;&#xA;&#x9;&#xA;&#xA;Options for running setup in demo mode&#xA;&#xA;&#xA;&#xA;&#xA;$ bin/setup oidc --help&#xA;&#xA;&#x9;&#xA;&#xA;Options for running setup in OIDC mode |

2. Run the `bin/setup` command with the appropriate authentication mode, as shown in [Authentication mode examples](#authentication_mode_setup_examples).

   1. (Optional) If you're using a PostgreSQL policy database, pass the server runtime username to `--dbAppUsername`.

      |   |                                                                                                                                                                                                                              |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you don't want to use the default database credentials for your H2 policy database, refer to [Setting database credentials at initial setup](../pingauthorize_server_administration_guide/paz_set_db_creds_startup.html). |

3. Copy and record any generated values needed to configure external servers.

   The shared secret is used in the PingAuthorize admin console, under **External Servers > Policy External Server > Shared Secret**.

4. Run `bin/start-server` to start the Policy Editor.

   The Policy Editor runs in the background, so you can close the terminal window in which it was started without interrupting it.

   1. (Optional) If you're using a PostgreSQL policy database, provide the server runtime password value you used to create the database to the `PING_DB_APP_PASSWORD` environment variable before starting the server.

## Next steps

* Complete the [post-setup steps](paz_post_setup_manual.html).

* Consider additional [configuration options](../pingauthorize_server_administration_guide/paz_specify_custom_config_opts_file.html) for the Policy Editor.

## Authentication mode examples

Click the following tabs for examples of the `setup` command in different authentication modes.

* OIDC mode (PingFederate)

* OIDC mode (generic)

* OIDC mode (custom scope)

* OIDC mode (self-governance)

* Demo mode

* Demo mode (PostgreSQL)

* Demo mode (custom SSL certificate)

* Demo mode (self-governance)

## Example: Set up the PingAuthorize Policy Editor in OIDC mode (PingFederate)

Use this example as a reference to set up the PingAuthorize Policy Editor for sign-ons using a PingFederate OIDC provider:

```shell
$ bin/setup oidc \
  --oidcHostname  <ping-federate-hostname>  \
  --oidcPort  <ping-federate-port>  \
  --clientId pingauthorizepolicyeditor \
  --generateSelfSignedCertificate \
  --decisionPointSharedSecret pingauthorize \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

The Policy Editor uses the provided OIDC host name and OIDC to query the PingFederate server's autodiscovery endpoint for the information it needs to make OIDC requests. The provided client ID represents the Policy Editor and must be configured in PingFederate.

The Policy Editor can skip host name verification and accept self-signed SSL certificates from the OIDC provider.

The following example uses the `PING_OIDC_TLS_VALIDATION` environment variable to set up the Policy Editor to handle sign-ons for a provider using a self-signed certificate:

```shell
$ env PING_OIDC_TLS_VALIDATION=NONE bin/setup oidc \
  --oidcHostname  <ping-federate-hostname>  \
  --oidcPort  <ping-federate-port>  \
  --clientId pingauthorizepolicyeditor \
  --generateSelfSignedCertificate \
  --decisionPointSharedSecret pingauthorize \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

For more information about configuring PingFederate, see [Configuring an OIDC provider for single sign-on requests from PingAuthorize](paz_config_authn_server_openid_connect.html).

## Example: Set up the PingAuthorize Policy Editor in OIDC mode (generic OIDC provider)

This example sets up the PingAuthorize Policy Editor for sign-ons using an arbitrary OIDC provider.

This example departs from the PingFederate example by specifying the OIDC provider's base URL, rather than a host name and port. This can be useful if the OIDC provider's autodiscovery and authorization endpoints include an arbitrary prefix, such as a customer-specific environment identifier.

```shell
$ bin/setup oidc \
  --oidcBaseUrl https://auth.example.com/9595f417-a117-3f24-a255-5736ab01f543/auth/ \
  --clientId 7cb9f2c9-c366-57e0-9560-db2132b2d813 \
  --generateSelfSignedCertificate \
  --decisionPointSharedSecret pingauthorize \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

The Policy Editor uses the provided OIDC base URL to query the OIDC provider's autodiscovery endpoint for the information it needs to make OIDC requests. The provided client ID represents the Policy Editor and must be configured in the OIDC provider as well.

The Policy Editor can skip host name verification and accept self-signed SSL certificates from the OIDC provider.

The following example uses the `PING_OIDC_TLS_VALIDATION` environment variable to set up the Policy Editor to handle sign-ons for a provider using a self-signed certificate:

```shell
$ env PING_OIDC_TLS_VALIDATION=NONE bin/setup oidc \
  --oidcBaseUrl https://auth.example.com/9595f417-a117-3f24-a255-5736ab01f543/auth/ \
  --clientId 7cb9f2c9-c366-57e0-9560-db2132b2d813 \
  --generateSelfSignedCertificate \
  --decisionPointSharedSecret pingauthorize \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

For more information about configuring an OIDC provider, see [Configuring an OIDC provider for single sign-on requests from PingAuthorize](paz_config_authn_server_openid_connect.html).

## Example: Set up the PingAuthorize Policy Editor in OIDC mode (custom scope)

This example sets up the PingAuthorize Policy Editor for sign-ons using OIDC with one or more custom scopes.

In OIDC mode, the Policy Editor UI requests an access token with the following default scopes: `openid email profile`. You can change the default requested scopes persistently, during server setup, or on a one-time basis, at server startup.

### Add OIDC scopes during setup

To add requested OIDC scopes persistently, use the `--scope` option to provide a space-separated list of scopes to the `setup` command.

```shell
$ bin/setup oidc \
  --oidcBaseUrl https://auth.example.com/02fa3993-a851-4eb5-96c7-f0c561be23c6/auth/ \
  –-clientId 21a74125-85db-4fca-8a56-e5d45d4d8163 \
  --scope "openid email profile  <additional_scope>" \
  --generateSelfSignedCertificate \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

The Policy Editor uses the provided OIDC base URL to query the OIDC provider's autodiscovery endpoint for the information it needs to make OIDC requests. The provided client ID represents the Policy Editor and must be configured in the OIDC provider as well.

The Policy Editor can skip host name verification and accept self-signed SSL certificates from the OIDC provider. The following example uses the `PING_OIDC_TLS_VALIDATION` environment variable to set up the Policy Editor to handle sign-ons for a provider using a self-signed certificate:

```shell
$ env PING_OIDC_TLS_VALIDATION=NONE bin/setup oidc \
  --oidcBaseUrl https://auth.example.com/02fa3993-a851-4eb5-96c7-f0c561be23c6/auth/ \
  –-clientId 21a74125-85db-4fca-8a56-e5d45d4d8163 \
  --scope "openid email profile  <additional_scope>" \
  --generateSelfSignedCertificate \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

### Add OIDC scopes at startup

To override persistently requested OIDC scopes for a single runtime instance of the Policy Editor, use the `PING_SCOPE` environment variable to provide a space-separated list of scopes to the `start-server` command:

```shell
$ env PING_SCOPE="openid email profile  <different_scope>" bin/start-server
```

For more information about configuring an OIDC provider, see [Configuring an OIDC provider for single sign-on requests from PingAuthorize](paz_config_authn_server_openid_connect.html).

## Example: Set up the PingAuthorize Policy Editor in OIDC mode (self-governance)

This example sets up the PingAuthorize Policy Editor with self-governance and OIDC authentication.

You can find information about configuring OIDC authentication on the **OIDC mode (generic)** tab on this page.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | Self-governance isn't supported in clustered Policy Editor configurations. |

To enable self-governance with OIDC authentication, use the following arguments when running the `bin/setup` command:

* `--enableSelfGovernance` (required)

  Enables self-governance functionality.

* `--selfGovernanceSystemUsername` (required)

  Sets the username of the self-governance administrator for OIDC authentication. To specify multiple self-governance administrators, provide a comma-separated list of usernames.

* `--apiHttpCacheTtl` (optional)

  Sets the time-to-live (TTL) value (in seconds) for the [HTTP cache](../pingauthorize_server_administration_guide/paz_http_caching.html), after which the cache is refreshed and a new self-governance check is performed. This value must be 1 or greater.

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | If you don't specify a value, the Policy Editor uses the default TTL of 60 seconds. |

The following example sets up the Policy Editor to use PingOne for OIDC authentication, enables self-governance, and specifies an OIDC username for the self-governance administrator:

```shell
$ bin/setup oidc \
--hostname localhost \
--port 9443 \
--adminPort  <admin-port>  \
--oidcBaseUrl https://auth.pingone.com/<your-environment-id>/as \
--clientId  <your-client-id>  \
--generateSelfSignedCertificate \
--enableSelfGovernance \
--selfGovernanceSystemUsername  <oidc-authenticated-user>
```

To specify multiple self-governance administrators, provide a comma-separated list of usernames:

```shell
$ bin/setup oidc \
--hostname localhost \
--port 9443 \
--adminPort  <admin-port>  \
--oidcBaseUrl https://auth.pingone.com/<your-environment-id>/as \
--clientId  <your-client-id>  \
--generateSelfSignedCertificate \
--enableSelfGovernance \
--selfGovernanceSystemUsername <admin-user-1>,<admin-user-2>
```

## Example: Set up the PingAuthorize Policy Editor in demo mode

This example sets up the PingAuthorize Policy Editor in demo mode with an automatically-generated self-signed server certificate.

After completing setup, the Policy Editor will accept sign-ons using the username `admin` and the password `password123`.

```shell
$ bin/setup demo \
  --adminUsername admin \
  --generateSelfSignedCertificate \
  --decisionPointSharedSecret pingauthorize \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

The decision point shared secret is a credential that the PingAuthorize Server uses to authenticate to the Policy Editor when it uses the Policy Editor as an external policy decision point (PDP).

For information about how to configure PingAuthorize Server to use the decision point shared secret, see [Post-setup steps (manual installation)](paz_post_setup_manual.html).

## Example: Set up the PingAuthorize Policy Editor with a PostgreSQL policy database

This example sets up the PingAuthorize Policy Editor in demo mode with the following options:

* Automatically generated self-signed server certificate

* PostgreSQL policy database with server runtime credentials (see the following caution about `--dbAppPassword`)

```shell
$ bin/setup demo \
  --dbConnectionString "jdbc:postgresql://<host>:<port>/<database>" \
  --dbAppUsername "<db-user>" \
  --dbAppPassword "<db-password>" \
  --generateSelfSignedCertificate \
  --decisionPointSharedSecret pingauthorize \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

|   |                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Using the `--dbAppPassword` option to provide the PostgreSQL database password to the `setup` tool persists the password to a configuration file.Instead, omit `--dbAppPassword` entirely to persist the default password, and set the `PING_DB_APP_PASSWORD` environment variable before server start. For example:```shell
$ env PING_DB_APP_PASSWORD=<db-password>  bin/start-server
``` |

## Example: Set up the PingAuthorize Policy Editor to use a custom SSL certificate

This example sets up the PingAuthorize Policy Editor in demo mode with a provided SSL server certificate in PKCS12 format:

```shell
$ env KEYSTORE_PIN_FILE=<path-to-keystore.pin>  bin/setup demo
  --adminUsername admin \
  --pkcs12KeyStorePath  <path-to-keystore.p12>  \
  --certNickname  <certificate-nickname>  \
  --decisionPointSharedSecret  <shared-secret>  \
  --hostname  <pap-hostname>  \
  --port  <pap-port>  \
  --adminPort  <admin-port>  \
  --licenseKeyFile  <path-to-license>
```

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | If you don't use the `KEYSTORE_PIN_FILE` during `setup`, you can supply the `--keystorePassword` option. |

The following information describes the previous example code block:

* The `KEYSTORE_PIN_FILE` environment variable, along with the `--pkcs12KeyStorePath` and `--certNickname` command-line options, affect the server's SSL certificate configuration.

* `KEYSTORE_PIN_FILE` contains the path to a file containing a valid key store PIN value.

* The `--pkcs12KeyStorePath` value is a path to a valid PKCS12 key store file.

* The `--certNickname` value is the certificate nickname or alias.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - The PingAuthorize Policy Editor only supports lowercase certificate nicknames.

- Because the `KEYSTORE_PIN_FILE` is not persisted, it must also be available in the environment of `start-server`. |

## Example: Set up the PingAuthorize Policy Editor in demo mode (self-governance)

This example sets up the PingAuthorize Policy Editor in demo mode with self-governance enabled.

For more information about setting up the Policy Editor in demo mode, click the **Demo mode** tab on this page.

To enable self-governance in demo mode, use the `--enableSelfGovernance` argument. The following values are set by default:

* The time-to-live value for the [HTTP cache](../pingauthorize_server_administration_guide/paz_http_caching.html) is set to 60 seconds, after which the cache is refreshed and a new self-governance check is performed.

* The self-governance administrator username is set to `selfgovernanceadmin`.

* The self-governance administrator password is set to `password123`.

The following example sets up the Policy Editor in demo mode with self-governance enabled:

```shell
$ bin/setup demo \
--adminUsername admin \
--enableSelfGovernance \
--generateSelfSignedCertificate \
--licenseKeyFile /opt/PingAuthorize/PingAuthorize.lic \
--decisionPointSharedSecret pingauthorize \
--hostname localhost \
--port 9443 \
--adminPort  <admin-port>
```

---

---
title: Installing the server and the Policy Editor manually
description: Install PingAuthorize Server and Policy Editor manually, then complete post-installation configuration steps.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_install_server_pe_manually
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_install_server_pe_manually.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Installing the server and the Policy Editor manually

Use manual install mode for the PingAuthorize Policy Editor and PingAuthorize Server installations.

## About this task

After you obtain the installation files, start the setup process.

## Steps

1. Install PingAuthorize Server.

2. Install PingAuthorize Policy Editor.

3. Perform additional configuration steps.

   The following sections describe these installation and configuration steps.

---

---
title: Installing the server manually
description: Install PingAuthorize Server manually in interactive or noninteractive mode.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_install_server_manually
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_install_server_manually.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  steps: Steps
  about-the-server-installation-modes: About the server installation modes
  installing-the-server-interactively: Installing the server interactively
  before-you-begin: Before you begin
  steps-2: Steps
  example: Example:
  installing-the-server-noninteractively: Installing the server noninteractively
  before-you-begin-2: Before you begin
  steps-3: Steps
  example-2: Example
---

# Installing the server manually

Choose your manual install mode for PingAuthorize Server and then perform the server installation.

## Steps

1. Read about the server installation modes and decide which mode you want to use.

2. Complete the steps for your chosen mode, interactive or noninteractive.

## About the server installation modes

There are several different installation modes for PingAuthorize Server.

PingAuthorize Server provides the following tools to help install and configure the system:

* The `setup` tool performs the initial tasks needed to start PingAuthorize Server, including configuring Java virtual machine (JVM) runtime settings and assigning listener ports for the PingAuthorize Server's HTTP services.

* The [`create-initial-config`](../pingauthorize_server_administration_guide/paz_config_user_store.html) tool configures connectivity between a System for Cross-domain Identity Management (SCIM) 2 user store and PingAuthorize Server. During the process, the `prepare-external-store` tool prepares each PingDirectory Server to serve as a user store by PingAuthorize Server. Configuration can be written to a file to use for additional installations.

  |   |                                                                                                                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Using `create-initial-config` is optional. However, if you do not use it, you do not get the user's profile (the requester's attributes). For more information, see [User profile availability in policies](../pingauthorize_server_administration_guide/paz_user_profile_avail_policies.html). |

* After the initial setup is finished, you can use the [`dsconfig` tool](../pingauthorize_server_administration_guide/paz_examples_config_server.html) and the administrative console to perform additional configuration.

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use server profiles to automate deployment of PingAuthorize Server. For more information, see [Deployment automation and server profiles](../pingauthorize_server_administration_guide/paz_deploy_auto_server_prof.html). |

To install a server instance, run the `setup` tool in one of the following modes:

* Interactive command-line mode

  Prompts for information during the installation process. To run the installation in this mode, use the `setup --cli` command.

* Noninteractive command-line mode

  Designed for setup scripts to automate installations or for command-line usage. To run the installation in this mode, setup must be run with the `--no-prompt` option as well as the other arguments required to define the appropriate initial configuration.

You can perform all installation and configuration steps while signed on to the system as the user or the role under which PingAuthorize Server will run.

​

* Interactive

* Noninteractive

## Installing the server interactively

Run the `setup` tool, which prompts you interactively for the information that it needs to install PingAuthorize Server.

### Before you begin

Be prepared to provide the following information:

* The location of a valid license file

* The name and password for an administrative account, which is also called the root user distinguished name (DN)

* An available port for PingAuthorize Server to accept HTTPS requests

* An available LDAPS port for PingAuthorize Server to accept administrative requests

* Information related to the server's connection security, including the location of a [keystore](../pingauthorize_server_administration_guide/paz_keystores_truststores.html) that contains the server certificate, the nickname of that server certificate, and the location of a truststore

* The amount of memory to reserve for usage by the Java virtual machine (JVM)

* A unique instance name for the server

### Steps

1. Run the `setup` command.

   #### Example:

   ```shell
   $ ./setup
   ```

2. To start and stop PingAuthorize Server, use the `start-server` and `stop-server` commands, respectively.

   For additional options, see [Starting PingAuthorize Server](../pingauthorize_server_administration_guide/paz_start_server.html).

## Installing the server noninteractively

For an automated installation, run the `setup` tool in noninteractive, command-line mode.

### Before you begin

Be prepared to provide the following settings using command-line arguments:

* The location of a valid license file

* The name and password for an administrative account, which is also called the root user distinguished name (DN).

* An available port for PingAuthorize Server to accept HTTPS requests

* An available LDAPS port for PingAuthorize Server to accept administrative requests

* Information related to the server's connection security, including the location of a keystore that contains the server certificate, the nickname of that server certificate, and the location of a truststore

* The amount of memory to reserve for usage by the Java virtual machine (JVM)

* A unique instance name for the server

### Steps

* Run the `setup` tool to install the server noninteractively.

* For more information about the available setup options, run `setup` with the `--help` argument, which displays a complete list of setup options, along with examples.

  ```shell
  $ ./setup --help
  ```

### Example

The following example sets up PingAuthorize with these settings:

* LDAP port 8389

* LDAPS port 8636

* HTTPS port 8443

* An automatically generated self-signed server certificate

* 1 GB of memory reserved for the server's JVM

* A unique server instance name of `pingauthorize1`

* A server location of `Austin`

```shell
$ ./setup \
  --cli --no-prompt --acceptLicense \
  --licenseKeyFile  <path-to-license>  \
  --rootUserDN "cn=directory manager" \
  --rootUserPassword  <your-password>  \
  --ldapPort 8389 --ldapsPort 8636 \
  --httpsPort 8443 \
  --generateSelfSignedCertificate \
  --maxHeapSize 1g \
  --instanceName pingauthorize1 \
  --location Austin
```

---

---
title: Managing license keys
description: Manage license keys for PingAuthorize Server and the Policy Editor.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_license_keys
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_license_keys.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2026
section_ids:
  when-you-need-a-license: When you need a license
  obtaining-a-license: Obtaining a license
  specifying-a-license: Specifying a license
  during-setup: During setup
  after-setup: After setup
  viewing-the-license-status: Viewing the license status
  license-expiration: License expiration
---

# Managing license keys

License keys are required to install, update, and renew all Ping products.

## When you need a license

You must obtain a license to:

* Set up a single-server instance. Once you have a valid license, you can set up multiple server instances in the same environment without needing additional licenses.

* Upgrade a server to a new major version. For example, upgrading from 7.3 to 8.0 requires a new license.

  The [upgrade](../upgrading_pingauthorize/paz_upgrade_pingauthorize.html) process automatically prompts you for a new license.

## Obtaining a license

To obtain a license key, contact your account representative or use the [Ping Identity licensing portal](https://www.pingidentity.com/en/account/request-license-key.html).

## Specifying a license

Specify a license for PingAuthorize Server during or after setup. You can find instructions for specifying a license with the Policy Editor in [Installing the Policy Editor non-interactively](paz_install_pe_noninteractive.html).

### During setup

Specify a license when running the `bin/setup` tool using one of the following methods:

* Provide the `--licenseKeyFile <path-to-license>` argument.

* Copy the license file to the server's root directory and then run the `setup` tool. The tool automatically discovers and applies the license file.

### After setup

Specify a license after setup using one of the following methods:

* In the PingAuthorize admin console, in the **Topology** section, click **License**.

  * Under **License Key**, select a license file from your local directory.

* Run the following command, providing the absolute path to the new license file and making sure to preserve the double quotes:

  ```
  bin/dsconfig set-license-prop \
    --set "governance-license-key<{absolute-path-to-license}"
  ```

## Viewing the license status

To view the details of a PingAuthorize Server license, including its expiration date, do one of the following:

* Run the `bin/status` tool and scroll to the `License Details` section.

* In the admin console sidebar, click **Status**.

  * Click the **Monitors** tab and search for `License`.

## License expiration

The PingAuthorize Server provides a notification in the admin console as the license expiration date approaches. Before a license expires, obtain a new one and install it by using `dsconfig` or the admin console.

License expiration affects the servers differently depending on whether they're already running:

* If the license expires while the servers are running, there's no immediate disruption. The PingAuthorize Server and Policy Editor continue to function normally.

* Attempts to start or restart the servers with an expired license fail.

|   |                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Renew licenses before they expire to avoid pod restart failures.In containerized environments such as Kubernetes, pod restarts trigger a fresh setup using the `manage-profile` tool. Because the tool treats this as a new installation, an expired license prevents the pod from restarting successfully. |

---

---
title: Manual installation
description: Overview of PingAuthorize manual installation using .zip archive packages instead of Docker images.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_manual_installation
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_manual_installation.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
---

# Manual installation

Instead of running Docker images, you can install PingAuthorize manually using `.zip` archives.

Learn more about installation and deployment methods in [Installing PingAuthorize](paz_install_pingauthorize.html).

---

---
title: Next steps
description: Post-installation configuration steps for PingAuthorize, including access token validation, user store setup, and policy creation.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_install_next_steps
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_install_next_steps.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
---

# Next steps

After installed, complete some configuration steps and then start developing policies to enforce fine-grained access to data.

Consider performing the following next steps:

* [Configure access token validation](../pingauthorize_server_administration_guide/paz_config_access_token_val.html).

* [Configure a user store](../pingauthorize_server_administration_guide/paz_config_user_store.html).

* [Sign on to the administrative console](../pingauthorize_server_administration_guide/paz_sign_onto_admin_console.html) to configure endpoints for existing JSON APIs.

  For more information, see [About the API security gateway](../pingauthorize_server_administration_guide/paz_api_security_gw.html).

* Sign on to the administrative console to define SCIM APIs for data in databases.

  For more information, see [About the SCIM service](../pingauthorize_server_administration_guide/paz_about_scim_service.html).

* [Sign on to the PingAuthorize Policy Editor](paz_sign_onto_pe.html) to create policies.

  For more information, see the PingAuthorize Policy Administration Guide.

---

---
title: Obtaining the installation packages
description: Download and expand the PingAuthorize Server and Policy Editor .zip installation packages to start the setup process.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_obtain_install_packages
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_obtain_install_packages.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Obtaining the installation packages

To begin the software installation process for PingAuthorize, obtain the server component's .zip installation packages.

## About this task

The PingAuthorize distribution consists of two compressed files, one for each of the following server components:

* PingAuthorize Server

* PingAuthorize Policy Editor

To start the installation process, complete the following steps:

## Steps

1. Obtain the [latest compressed release bundles](https://www.pingidentity.com/en/resources/downloads/pingauthorize.html) from Ping Identity.

2. Expand the release bundles into the folders of your choice.

---

---
title: Post-setup steps (Docker deployment)
description: Configure PingAuthorize Server to use the Policy Editor as its policy decision point after a Docker deployment.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_post_setup_docker
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_post_setup_docker.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
---

# Post-setup steps (Docker deployment)

After you successfully set up the PingAuthorize Policy Editor, you must start the server and then configure PingAuthorize Server to use the Policy Editor as its policy decision point (PDP).

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | The containers must be on the same Docker network to communicate properly. |

Sign on to the Policy Editor and import a policy snapshot. You can find a set of default policies in the `resource/policies/defaultPolicies.SNAPSHOT` file. For more information, see [Signing on to the PingAuthorize Policy Editor](paz_sign_onto_pe.html).

To configure PingAuthorize Server to use the Policy Editor, use `dsconfig` or the administrative console to create a Policy External Server to represent the Policy Editor, then assign the Policy External Server to the Policy Decision Service and configure it to use external PDP mode. Also, set the Trust Framework Version to the current version, v2.

Consider the following example. Assume a container named pingauthorize and that no files are needed from the file system. The following commands run `dsconfig` from within the container.

```shell
docker exec  {SERVER_CONTAINER_NAME}  /opt/out/instance/bin/dsconfig create-external-server \
  --server-name "{PAP_Name}" \
  --type policy \
  --set "base-url:https://<pap-hostname>:<pap-port>" \
  --set "shared-secret:2FederateM0re" \
  --set "branch:Default Policies"

docker exec  {SERVER_CONTAINER_NAME}  /opt/out/instance/bin/dsconfig set-policy-decision-service-prop \
  --set pdp-mode:external \
  --set "policy-server:{PAP_Name}" \
  --set trust-framework-version:{TRUST_FRAMEWORK_VERSION}
```

In the example, the base URL consists of the host name and port chosen for the Policy Editor during setup. The shared secret value is `2FederateM0re` by default. The branch name corresponds to the branch name that you chose when importing your policy snapshot.

---

---
title: Post-setup steps (manual installation)
description: Configure PingAuthorize Server to use the Policy Editor as its policy decision point after a manual installation.
component: pingauthorize
version: 11.1
page_id: pingauthorize:installing_and_uninstalling_pingauthorize:paz_post_setup_manual
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/installing_and_uninstalling_pingauthorize/paz_post_setup_manual.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2026
---

# Post-setup steps (manual installation)

After you set up the PingAuthorize Policy Editor, you must start the server from the CLI and then change the PingAuthorize Server configuration to use the Policy Editor as its policy decision point (PDP).

To start the Policy Editor, run the following command.

```shell
$ bin/start-server
```

Then, sign on to the Policy Editor and import a policy snapshot. You can find a set of default policies in the `resource/policies/defaultPolicies.SNAPSHOT` file. For more information, see [Signing on to the PingAuthorize Policy Editor](paz_sign_onto_pe.html).

To configure PingAuthorize Server to use the Policy Editor, use `dsconfig` or the administrative console to create a Policy External Server to represent the Policy Editor, then assign the Policy External Server to the Policy Decision Service and configure it to use external PDP mode. Also, set the Trust Framework Version to the current version, v2. Consider the following example.

```
dsconfig create-external-server \
  --server-name "{PAP_Name}" \
  --type policy \
  --set "base-url:https://<pap-hostname>:<pap-port>" \
  --set "shared-secret:pingauthorize" \
  --set "branch:Default Policies" \

dsconfig set-policy-decision-service-prop \
  --set pdp-mode:external \
  --set "policy-server:{PAP_Name}"
  --set trust-framework-version:{TRUST_FRAMEWORK_VERSION}
```

In the example, the base URL consists of the host name and port chosen for the Policy Editor during setup. Similarly, the shared secret value was chosen during setup. The branch name corresponds to the branch name that you chose when importing your policy snapshot. The decision node is the ID of the root node in your policy tree. If you are using the default policies, then use the ID shown in the example.