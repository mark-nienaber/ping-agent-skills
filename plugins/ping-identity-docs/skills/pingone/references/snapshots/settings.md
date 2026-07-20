---
title: (Customer Only) Configuring WhatsApp as a sender
description: To use WhatsApp as a strong authentication (MFA) method, you'll need to add your WhatsApp business account as a sender.
component: pingone
page_id: pingone:settings:p1-using-a-custom-whatsapp-sender-account
canonical_url: https://docs.pingidentity.com/pingone/settings/p1-using-a-custom-whatsapp-sender-account.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# (Customer Only) Configuring WhatsApp as a sender

To use [WhatsApp](../strong_authentication_mfa/p1-strong-auth_whatsapp.html) as a strong authentication (MFA) method, you'll need to add your WhatsApp business account as a sender.

## Before you begin

Before connecting your WhatsApp business account as a sender in PingOne, configure a WhatsApp business account in the Meta business and developer portals as follows:

1. If you don't have one already, create a WhatsApp business account.

2. Create a WhatsApp application that includes at least one sender number.

3. In the WhatsApp business account, create a **System User** with the **Admin** System user role.

4. Assign the **System User** to the WhatsApp application.

5. Generate an access token, and then add the following scopes to the access token:

   * `business_management`

   * `manage_app_solution`

   * `whatsapp_business_management`

   * `whatsapp_business_messaging`

6. Get the **App ID** and **App Secret**. You can find the **App ID** and **App Secret** in the Developer portal **App settings**.

7. In the WhatsApp business account, create one or more WhatsApp message templates. The message templates must be of category **Authenticator**. The message template can be used to send notifications in PingOne.

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | You can only add a single WhatsApp sender account to a PingOne environment. |

## Steps

To configure a custom WhatsApp sender:

1. Go to **Settings > Senders**.

2. In the **Sender Type** field, select **Messaging**, and then click **Next**.

3. In the **Provider Configuration** window, enter the following information, and then click **Verify**:

   * **WhatsApp for Business ID**: Enter your organization's WhatsApp business account ID.

   * **User Access Token**: Enter the user access token that was generated from your WhatsApp business account.

   * **App ID**: Enter the app ID of the relevant WhatsApp application.

   * **App Secret**: Enter the app secret for the WhatsApp application in the format `<appid|apptoken>`.

     ![Sender window. The Messaging tab shows the text To use your own sender account for WhatsApp messages, enter the relevant details and verify your account. Several fields are shown.](../strong_authentication_mfa/_images/p1-whatsapp-sender-messaging-tab.png)

     PingOne verifies the WhatsApp business account details and displays the available WhatsApp sender numbers.

     |   |                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------- |
     |   | Validation can take several minutes. Don't close the validation window until the validation is complete. |

     Result

     The WhatsApp account is saved.

     ## Next steps

     Learn more about the additional steps required to add WhatsApp as an authentication method in [(Customer Only) Configuring WhatsApp authentication](../strong_authentication_mfa/p1-strong-auth_whatsapp.html)

---

---
title: Adding a certificate
description: Learn how to add a certificate in PingOne to establish trust, verify identity, and secure communication with applications and services.
component: pingone
page_id: pingone:settings:p1_addcertificate
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_addcertificate.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 9, 2023
keywords: ["add certificate", "upload certificate", "certificate management", "certificate usage type"]
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Adding a certificate

Use the **Certificates** tab of the **Certificates and Key Pairs** page to set up a certificate for your environment.

## Before you begin

Before you add a certificate, ensure that the following requirements are met:

* The certificate is valid at the time you add it to PingOne. You can't upload a certificate before its `NotBefore` date or after its `NotAfter` expiration date.

* The private key is unencrypted.

* The certificate, private key, and certificate chain are all PEM-encoded unless you're uploading a PKCS12 file.

* Supported certificate formats include `PKCS7 (.p7b)` and `PEM (.cer, .crt, .pem)`.

* The certificate has a key length of at least 2048 bits and uses SHA-256 or stronger encoding.

## Steps

1. In the PingOne admin console, go to **Settings > Certificates and Key Pairs**.

2. On the **Certificates** tab, click the **[icon: plus, set=fa]icon**.

   ![A screenshot of the certificates page.](_images/p1-certificates-and-keypairs-page-certs-tab.png)

3. Click **Select a file** and select the certificate file to upload.

   ![A screenshot of the view of the certificates page.](_images/p1-cert-add.png)

4. In the **Usage Type** list, select one of the following options:

   | Option                      | Description                                                                                                                                                                                             |
   | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Signing - Verification**  | Used to create and validate digital signatures. Enables the certificate to sign tokens or data so that other systems can verify the signature to ensure authenticity and integrity.                     |
   | **Encryption – Decryption** | Used to securely protect sensitive data. Allows the certificate to encrypt information so only the holder of the matching private key can decrypt it.                                                   |
   | **SSL/TLS**                 | Used to secure network connections. Supports encrypted HTTPS communication, ensuring secure connections between clients and servers.                                                                    |
   | **Issuance**                | Used by certificate authorities (CAs) to sign and issue other certificates. Typically selected when the certificate will be used to generate subordinate or leaf certificates within a trust hierarchy. |

5. Click **Save**.

---

---
title: Adding a service to an environment
description: Use the Overview page to add services to an existing environment in your organization.
component: pingone
page_id: pingone:settings:p1_add_a_service
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_add_a_service.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 1, 2024
section_ids:
  steps: Steps
---

# Adding a service to an environment

Use the **Overview** page to add services to an existing environment in your organization.

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page and browse or search for the applicable environment.

2. On the **Environments** page, click the environment to open the details panel.

3. Click **Manage Environment** to go to the **Overview** page for the environment.

4. In the **Services** section, click the **[icon: plus, set=fa]**icon.

5. Select the service that you want to add.

6. Click **[icon: plus, set=fa]Add** next to the service.

7. Follow the instructions in **Add a Service**.

8. Click **Finish**.

---

---
title: Adding an environment
description: Add an environment to your organization from the Environments page using the setup assistant to guide you through the process.
component: pingone
page_id: pingone:settings:p1_addenvironment
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_addenvironment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 15, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result
---

# Adding an environment

Add an environment to your organization from the **Environments** page using the setup assistant to guide you through the process.

## About this task

|   |                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------- |
|   | You must have the Organization Admin role or a custom role with equivalent permissions to create an environment. |

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page.

2. Click the **[icon: plus, set=fa]**icon.

   ![A screenshot of the Environments page in PingOne.](../getting_started_with_pingone/_images/vxj1676308916876.png)

   ### Result:

   The **Create Environment** setup assistant starts.

3. Select the type of solution that you want to support in this environment.

   ![A screenshot of the Create Environment setup assistant in PingOne.](../_images/ppz1683237101125.png)

   | Option                      | Description                                                                                                                                          |
   | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Customer solution**       | Select to design registration and subsequent sign-on experiences for your customers and test them in a sample application tailored to your industry. |
   | **Workforce solution**      | Select to design single sign-on experiences for your employees, partners, and vendors.                                                               |
   | **Build your own solution** | Select to choose from all of our services and products to build a hybrid solution that fits your unique use case.                                    |

4. Click **Next**.

   The services that will be deployed to your new environment are listed.

5. Click **Next**.

6. Define your environment by entering the following:

   | Field                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                       |
   | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Environment Name**                                                             | A unique identifier for the environment.                                                                                                                                                                                                                                                                                                                                          |
   | **Description** (optional)                                                       | A brief description of the environment.                                                                                                                                                                                                                                                                                                                                           |
   | **Environment Type**                                                             | Select **Sandbox** or **Production**.Sandbox environments are typically used for configuration and testing before deployment. Production environments are typically used for live configurations that are deployed for real-world use. Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types). |
   | **Generate sample populations and users in this environment**                    | Select this checkbox to generate two populations and 40 sample users in the new environment.                                                                                                                                                                                                                                                                                      |
   | **Region**                                                                       | The appropriate geographical region for the environment. The list shows only regions that are included with your license.&#xA;&#xA;You can't change the region after the environment has been created.                                                                                                                                                                            |
   | **License**                                                                      | Select the license to use for this environment. The available licenses for your organization are shown in the **License** list. For more information, see [Licenses and Platform Limits](../getting_started_with_pingone/p1_licenses.html).                                                                                                                                       |
   | **Include a solution designer to easily design and test experiences** (optional) | Workforce solutions only. If selected, after you create your environment, a solution designer opens and walks you through the process of designing your experiences.                                                                                                                                                                                                              |

7. Click **Finish**.

## Result

The new environment is created in your PingOne organization.

If you chose to build a workforce solution, and selected the solution designer option, the solution designer opens and guides you through the process of designing and testing registration and sign-on experiences in less than 5 minutes.

If you did not select the solution designer option, or if you didn't build a workforce solution, the **Environments** page opens. Locate your new environment by sorting the list alphabetically or by date created, or enter the environment name in the search box.

---

---
title: Adding an icon to an environment
description: Add an icon to an environment to easily find it on the Environments page.
component: pingone
page_id: pingone:settings:p1_add_icon_to_environment
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_add_icon_to_environment.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 26, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result:
  result-2: Result
---

# Adding an icon to an environment

Add an icon to an environment to easily find it on the **Environments** page.

## Steps

1. Access the environment details page for the environment to which you want to add an icon by doing one of the following.

   ### Choose from:

   * If you are in the console for the environment that you want to edit, go to **Settings > Environment Properties**.

   * If you're not in the environment that you want to edit, click the Ping Identity logo in the sidebar to open the **Environments** page and click the environment that you want to edit.

     ![A screenshot of the environment details view for the BX Finance environment](_images/p1-env-props-bxins-no-boxes.png)

2. Click the **Pencil** icon.

3. Click the **Icon** box.

   ![A screen capture of the edit view of the BX Insurance environment .](_images/p1-edit-bx-ins-env-before-adding-logo.png)

   ### Result:

   A file browser opens.

4. Browse for and select the icon you want to use and click **Open**.

   |   |                                |
   | - | ------------------------------ |
   |   | The maximum icon size is 2 MB. |

5. Click **Save**.

## Result

The icon is displayed in the environment details view and on the **Environments** page.

![Screenshot of the environments list with BX Insurance and its logo highlighted, and details pane open.](_images/gzq1711041113506.png)

---

---
title: Adding or editing inbound traffic policies for custom domains
description: Inbound traffic policies allow you to set rules for processing requests to your custom domain based on the source of the request.
component: pingone
page_id: pingone:settings:p1_configure_inbound_traffic_policies
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_configure_inbound_traffic_policies.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# Adding or editing inbound traffic policies for custom domains

Inbound traffic policies allow you to set rules for processing requests to your custom domain based on the source of the request.

Your custom domain must be routing to Cloudflare to use inbound traffic policies.

Learn more in [Inbound traffic policies](p1_inbound_traffic_policies.html).

## Before you begin

To use inbound traffic policies, you must:

* Have a custom domain configured for the environment. Learn more in [Setting up a custom domain](p1_set_up_custom_domain.html).

* Ensure that the custom domain is routing to Cloudflare by going to **Settings > Domains** in the PingOne admin console and checking for the **Cloudflare Active** label.

  ![A screenshot of the Domains page showing a custom domain with the Cloudflare Active label.](_images/p1-custom-domain-cloudflare.png)

* Ensure that your custom domain allows all requests to `https://<customdomain>/.well-known/ping-endpoints.json`. PingOne must be able to successfully issue an HTTP GET call to this URL to confirm that your custom domain is routing to Cloudflare. If this request is blocked, you won't be able to configure inbound traffic policies.

Learn more in [Migrating a custom domain to Cloudflare](p1_migrate_custom_domain_to_cloudflare.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following restricted headers aren't allowed in any of the header configuration fields in the policy. This restriction applies to the **Header (Single Value)** and **Header (List)** options in the **Client IP Source Selection** section, and to any **Accepted Custom Headers**.- `Authorization`

- `Cookie`

- `X-Ping-Itp-Jwt`

- `X-Ping-Itp-Secret`

- `X-Ping-Ingress`

- Any header starting with `Cf-`Additionally, although you can use a mix of cases in the header fields in the policy, case is ignored at runtime. |

## Steps

1. In the PingOne admin console, go to **Settings > Inbound Traffic Policies** and do one of the following:

   * To add a new inbound traffic policy, click the [icon: plus, set=fa]icon.

   * To edit an existing inbound traffic policy, browse or search for the policy you want to edit, and click it to open the details panel. Then click the **Pencil** icon ([icon: pencil, set=fa]).

     ![A screenshot of the Add Inbound Traffic Policy page with Match All Traffic selected.](_images/p1-add-new-traffic-policy.png)

2. Enter a name for the policy.

   The name must be unique to the environment and is only used to identify the policy in the PingOne admin console.

   |   |                                                                              |
   | - | ---------------------------------------------------------------------------- |
   |   | Use the name to identify the source of the requests addressed by the policy. |

3. In the **Inbound Traffic Criteria** section, select and configure the criteria used to determine whether requests match the policy.

   |   |                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Requests are matched to the first enabled policy on the **Inbound Traffic Policies** page for which all defined inbound traffic criteria are met. |

   **Inbound Traffic Criteria**

   | Option                | Description and Configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Match All Traffic** | All requests are considered a potential match to the policy.If you select this option, all other options are disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **Signed JWT**        | Requests must include an `X-Ping-Itp-Jwt` header that contains a JSON Web Token (JWT) value signed by a private key corresponding to one of the public keys in the JWKS configured on this page. The JWT is in JWS compact serialization format and must have the following header and payload:```json
   {
     "typ": "JWT",
     "alg": "RS256",
     "kid": "<kid in jwks>"
   }
   .
   {
     "iss": "<policyId>",
     "aud": "<environmentId>",
     "exp": "<seconds from epoch>"
   }
   ```where:- `RS256` is the only supported signing algorithm.

   - `kid` must refer to one of the public keys in the **JWKS** field.

     &#xA;&#xA;You are responsible for maintaining the confidentiality of the private key. If a private key is compromised, you must remove the public key from the JWKS configured on the Inbound Traffic Policies page immediately.

   - `iss` is the ID of the inbound traffic policy that's using this **Signed JWT** criteria. You can find this ID under the policy name in the **Inbound Traffic Policies** list and in the policy details panel.

   - `aud` is the ID of the environment associated with the custom domain to which the request is submitted. You can find this ID on the **Environment Properties** page.

   - `exp` is optional and is the number of seconds from epoch after which the JWT is considered expired and no longer accepted by the **Signed JWT** criteria.

     &#xA;&#xA;Include exp for security purposes and set it to 300 seconds (5 minutes). This value allows for clock drift while still limiting the lifespan of the JWT.Select this option and then paste in the JSON for the JWKS in the **JWKS** field.You can paste the JSON in a single line or in multiple lines. |
   | **Secret Header**     | Requests must include an `X-Ping-Itp-Secret` header that contains a secret with a value that, when hashed, matches one of the SHA-256 hash values in the list.&#xA;&#xA;You are responsible for maintaining the confidentiality of the secret. If a secret is compromised, you must remove the hash configured on the Inbound Traffic Policies page immediately.Select this option and click **+ Add Secret** to open the **Add Secret** modal. In the modal, select one of the following options:- **Secret**: Enter secret text in the **Secret** field or click **Generate** to allow PingOne to generate a secret for you.

   - **Hashed Secret**: Paste a secret hash in the **Secret** field.&#xA;&#xA;Before you exit the modal, copy the secret and paste it to a secure location in case you need to use it later. When the secret is added to your policy criteria, the value will be hashed, and you won't be able to view the original secret text.Click **Add Secret** to add the secret hash to your policy. You can add a maximum of five secret hashes.To remove a secret hash, click the **Delete** icon ([icon: trash, set=fa]).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | **mTLS Thumbprint**   | Requests must use an mTLS connection where the certificate's SHA-256 thumbprint matches one of the thumbprints in the list.&#xA;&#xA;To use this option, you must use the PingOne API to enable mTLS for the custom domain. Learn more in Custom Domains in the PingOne API documentation.Select this option and click **+ Add Thumbprint** to open the **Add mTLS Thumbprint** modal. Paste your PEM-encoded X.509 certificate to generate the thumbprint, then click **Add mTLS Thumbprint** to add the thumbprint to your policy.You can add a maximum of five thumbprints.To remove a thumbprint, click [icon: trash, set=fa].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | **IP Address**        | Requests must use a connection for which the socket IP address matches one of the entries in this list.&#xA;&#xA;The socket IP address refers to the final or actual connection to the custom domain. For requests made through an intermediate connection, the socket IP address might differ from the client's logical IP address. Learn more in step 5.Select this option to enter up to five IP ranges in CIDR notation. Both IPv4 and IPv6 addresses are supported.To remove an IP range, click the **X** on the entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

4. In the **Traffic Rule** section, select one of the following options:

   * **Allow**: Requests matching this policy are allowed to pass. If you select **Allow**, continue to [step 5](#p1-client-ip-source).

   * **Block**: Requests matching this policy are blocked. If you select **Block**, there are no additional options to configure. Go to [step 7](#p1-click-save).

     |   |                                                                                                                                                                               |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If the policy criteria are too broad, and you select **Block**, you might unintentionally block requests that you want to allow. Use more specific criteria to block traffic. |

5. []()Select an option in the **Client IP Source Selection** section to configure how the client IP address for the request is determined.

   This IP address represents the logical end user or device that's making the request in cases where there is an intermediate connection through which the request is submitted. The client IP address is used for IP-based operations, such as rate limiting, and to populate the `global.ip` variable in PingOne DaVinci. Learn more in [Including variables and other data in DaVinci flows](https://docs.pingidentity.com/davinci/flows/davinci_global_variables.html) in the PingOne DaVinci documentation.

   * **Socket IP**: If you select **Socket IP**, no configuration is required. The client connects directly to the custom domain using the socket IP as the client IP address.

     |   |                                                                                                                              |
     | - | ---------------------------------------------------------------------------------------------------------------------------- |
     |   | If you selected **Match All Traffic** in the **Inbound Traffic Criteria** section, **Socket IP** is the only option enabled. |

   * **Header**: Select this option and enter the **Header Name**. Requests must include this header, and the value must be an IPv4 or IPv6 address.

   * **Header (List)**: Select this option and enter the **Header (List) Name**.

     * For **Required number of elements**, select the number of elements that make up the header value. Request headers must include a header value with the exact number of elements specified or the request will be rejected.

     * For **Element position**, select the position of the element within the header in which the IP source is expected. Request headers must include an IPv4 or IPv6 address in this exact position or the request will be rejected. Element position is counted from left to right starting at 1.

       ![A screenshot of the Client IP Source Selection section with Header (List) selected and the Required number of elements and Element position defined.](_images/p1-traffic-policy-client-ip-header-list.png)

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use **Socket IP** or **Header (Single Value)** if possible. The **Header (List)** option should be used only if you're certain of the number of elements and element position. Even then, the **Header (List)** option can be more prone to errors. If the number or order of header elements changes after you've configured your traffic policy, you might inadvertently block all of the requests to your custom domain or associate the client with an incorrect IP address. |

6. To define custom headers that can be included in requests, add the headers in the **Accepted Custom Headers** section.

   If the header must be present in requests, select the **Required** checkbox. Requests that don't include required headers will be blocked.

   You can add up to 15 custom headers. The combined length of all custom headers in the policy can be no more than 768 characters. Requests with custom headers exceeding these limits will be blocked.

   To remove a header, click [icon: trash, set=fa].

7. []()Click **Save**.

The policy is added to the bottom of the list on the **Inbound Traffic Policies** page and is disabled by default. Enable it by clicking the toggle to the right (blue).

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | It can take up to 60 seconds for the new or updated policy to take effect. |

## Next steps

Because inbound traffic policies are processed in the order in which they are listed on the **Inbound Traffic Policies** page, ensure that they're in the intended order.

To reorder the policies, click **Reorder**, drag and drop the policies into the order in which you want them to be matched, and click **Save**.

---

---
title: Administrator security
description: Security settings for administrators accessing the PingOne admin console are configured on the Administrator Security page.
component: pingone
page_id: pingone:settings:p1_administrator_security
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_administrator_security.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 23, 2025
section_ids:
  learn-more: Learn more
---

# Administrator security

Security settings for administrators accessing the PingOne admin console are configured on the **Administrator Security** page.

Ping Identity requires MFA for all PingOne administrators as of June 1, 2025. Learn more in the [PingOne administrators MFA requirement - FAQ](https://docs.pingidentity.com/pingone-admin-mfa-faq/p1_mfa_required_for_admins_faq.html).

## Learn more

* [Configuring administrator security](p1_configure_administrator_security.html)

* [Configuring administrator security - PingID](p1_configure_administrator_security_pingid.html)

---

---
title: API Usage Dashboard
description: "Use the API Usage Dashboard to decide if you're approaching the default entitlements for any of your PingOne rate groups."
component: pingone
page_id: pingone:settings:p1_api_usage_dashboard
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_api_usage_dashboard.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 13, 2025
keywords: ["rate limiting"]
section_ids:
  rate-groups-and-base-level-entitlements: Rate groups and base-level entitlements
  maximum-throughput-assurance: Maximum Throughput Assurance
  using-the-api-usage-dashboard: Using the API Usage Dashboard
  historic-peak-http-request-rates-table: Historic Peak HTTP Request Rates table
  daily-peak-http-request-rates-graphs: Daily Peak HTTP Request Rates graphs
---

# API Usage Dashboard

The **API Usage Dashboard** shows an overview of how your peak API usage is trending against the limits allowed by your license, per rate group. This information can help you decide whether you have sufficient capacity or are approaching the rate entitlements for any of your rate groups.

There are two types of rate groups in PingOne:

* **Buyable groups**: You can increase entitlements for these rate groups by purchasing a [Maximum Throughput Assurance](#maximum-throughput-assurance) package. Only buyable rate groups are displayed on the dashboard.

* **Non-buyable groups**: These rate groups contain API endpoints with usage that shouldn't increase with additional end-user activity, such as configuration updates or audit data retrieval. Entitlements for these rate groups are the same for all licenses and can't be changed. These groups aren't displayed on the dashboard.

Because usage entitlements are applied at the license level and are measured across all of the environments assigned to the license, the dashboard is at the organization level. You must have the Organization Admin role or a custom role with equivalent permissions to view it.

![A screen capture of the API Usage Dashboard showing both the Historic Peak HTTP Request Rates table and Daily Peak HTTP Request Rates graphs for several rate groups.](_images/p1-api-usage-db.png)

## Rate groups and base-level entitlements

Rate limiting helps Ping ensure that each customer has the share of resources they need at any given time.

The default entitlements provided for each rate group should be sufficient for the majority of customers.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In addition to the license-level entitlements, there are environment-level limits that control incoming traffic from single IP addresses. An IP address is limited to 35% of the overall license rate by default. If you have traffic that comes from a limited number of IP addresses or servers, bypass these limits by adding those addresses in **Settings > Rate Limits**.For Trial licenses, an IP address can use 100% of the overall license rate, but the overall rate cap is lower.Learn more in [Configuring rate limits and allowed IPs](p1_rate_limits.html#configure-rate-limits). |

## Maximum Throughput Assurance

For some rate groups, you can purchase a Maximum Throughput Assurance package to increase your peak usage entitlements. For example, you could decide you need additional throughput at peak times because you've reviewed the dashboard and anticipate a higher number of simultaneous HTTP requests in the future. Based on the current data displayed in the dashboard, you determine that the increased requests could put you over your current entitlement limits.

Anticipated traffic increases might occur because of something like a popular sporting event, a Black Friday sale, or the start of ticket sales for a large music festival. To prevent users from receiving an interruption in service or a too-many-requests warning during these high-traffic times, contact your Ping representative about Maximum Throughput Assurance packages.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To ensure that you have the increased throughput when you need it, consider your organization's purchasing process and timelines when requesting a Maximum Throughput Assurance package. |

Maximum Throughput Assurance can be purchased for the following rate groups:

| Product     | Rate Group                              |
| ----------- | --------------------------------------- |
| Authorize   | Authorization API Rate                  |
| Credentials | Credentials Issuance and Check API Rate |
| DaVinci     | Flow Execution (post-start) Rate        |
| DaVinci     | Flow Progression and Callbacks          |
| DaVinci     | Flow Start (invocation) Rate            |
| Directory   | Data Read Rate                          |
| Directory   | Data Write Rate                         |
| MFA         | MFA Polling Rate                        |
| MFA         | MFA API Rate                            |
| Protect     | Protect API Rate                        |
| SSO         | SSO API Rate                            |
| SSO         | Token Check Rate                        |
| Verify      | Verification API Rate                   |

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find a detailed listing of all rate groups, including their base entitlements and associated endpoints, in [Base rate limits](https://developer.pingidentity.com/pingone-api/platform/rate-limiting/base-rate-limits.html) in the PingOne API documentation. |

## Using the API Usage Dashboard

You must have the Organization Admin role or a custom role with equivalent permissions to view the **API Usage Dashboard**.

To access the dashboard, click the Ping Identity logo in the PingOne admin console sidebar, click **API Usage Dashboard**, and then select a license from the list.

The dashboard includes two panels for viewing your API usage data:

* **Historic Peak HTTP Request Rates**: Displays your peak API usage for each rate group and how the usage compares against your entitlements in an easy-to-read table format.

* **Daily Peak HTTP Request Rates**: Displays your peak API usage, entitlement limits, and 30-day averages for each rate group in line graphs that you can zoom into and analyze to determine when spikes in usage occurred.

### Historic Peak HTTP Request Rates table

![A screen capture of the Historic Peak HTTP Request Rates table from the API Usage Dashboard.](_images/p1-api-db-historic-peak-http-requests-table.png)

The **Historic Peak HTTP Request Rates** table on the left side of the page lists the following information about your HTTP requests for different groups of API endpoints over a period of 14 months:

| Column          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Product**     | The PingOne services and products included in your license. **All Products** indicates that these endpoints apply to all areas of PingOne. For example, configuration-related endpoints apply to all products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Rate Group**  | The rate groups that are included under each product. A rate group defines the base rate limits for a particular set of API endpoints. The endpoints are grouped by functionality under each PingOne service or area, and each service or area can have more than one rate group. Each rate group is subject to its own entitlement limit.The rate groups displayed on the dashboard depend on the selected license and the API activity.- Only rate groups related to products that are included in the selected license or that aren't related to a specific licensed product are displayed.

- Only rate groups with traffic during the reporting period are displayed.

- Data for new or modified rate groups is available only going forward from the date the group is added or modified.For example, if the selected license doesn't include PingOne Verify, you won't see Verify rate groups on the dashboard. Similarly, if there's no activity for the **Bulk Data Import** rate group during the reporting period, it won't be listed on the dashboard. |
| **Peak**        | The peak HTTP requests reached during the reporting period for the rate group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Base Limit**  | The default number of requests allowed for the rate group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Entitlement** | The maximum requests allowed by your license for the rate group. This value is the same as the **Base Limit** unless you've purchased a Maximum Throughput Assurance package to increase the entitlement for that group.For example, if the **Base Limit** for a rate group is 200 requests per second (RPS), and you purchased a Maximum Throughput Assurance package that doubles that entitlement, the **Base Limit** column still shows 200 RPS, but the **Entitlement** column shows 400 RPS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Interval**    | The unit of measurement for the rate limit. Some rate groups use RPS, and others use requests per minute (RPM).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Usage**       | The percentage of the allowed entitlement that was used when you hit the peak rate limit. For example, if your peak was 250 RPS, and your entitlement is 500 RPS, you used 50% of your entitlement during the peak. If you're at 80% to 89% of your entitlement, the entry is highlighted in orange. If you're at or over 90% of your entitlement, the entry is highlighted in red. In both cases, you should investigate further and determine if you need to increase your entitlements.&#xA;&#xA;Enable the Rate Limit Warning and Rate Limit Exceeded alerts to send email notifications when you're approaching or exceeding your rate limits. Learn more in Alerts.                                                                                                                                                                                                                                                                                                                                                                                           |

Hover over the upper-right corner of the pane to show icons that you can use to change your view of the table:

* Maximize the table: Click the **Maximize** icon (![An image of the maximize icon](../_images/p1-dashboard-maximize.png)) to hide the **Daily Peak HTTP Request Rates** graphs and show only the table.

  Click the icon again to show the **Daily Peak HTTP Request Rates** graphs.

* Resize the columns: Grab a column separator in the table header to make columns wider or narrower.

* Sort the data: Click the **Sort visual** icon (![An image of the Sort visual icon](../_images/p1-dashboard-sort-visual.png)) at the upper right corner of the table. Select a column from **Sort by** and choose **Ascending** or **Descending**. Click **+ Add Sort** to add sort criteria and then click **Apply**.

  You can also click a column heading for sort options and to freeze or unfreeze columns.

To export the data to either a CSV file or an Excel file for further review and analysis, click the **Menu options** icon (![An image of the Menu options icon](../_images/p1-dashboard-menu-options.png)) and select the applicable option.

Click inside a row in the table to display the **Daily Peak HTTP Request Rates** graph for a particular rate group in the right pane.

### Daily Peak HTTP Request Rates graphs

![A screen capture of the Daily Peak HTTP Request Rates graph for the Authorize - Authorization API Rate rate group. Callouts are used to define the meaning of each line in the graph.](_images/p1-api-db-daily-peak-http-req-rates-callouts.png)

The **Daily Peak HTTP Request Rates** graphs are based on rate group and include three lines of data:

* The purple line shows your daily peak usage for the selected rate group.

  |   |                                                                                                             |
  | - | ----------------------------------------------------------------------------------------------------------- |
  |   | For each day over a 14-month period, there's a single data point indicating the busiest second of that day. |

* The red line at the top of the graph indicates the current entitlement for the group. If you've purchased increased capacity, this line will be higher than the base rate.

* The orange line indicates your average peak usage over a 30-day period.

  |   |                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
  |   | View the 30-day average to see whether your peak usage is an anomaly or if you're approaching the entitlement limits on a regular basis. |

Hover over the graph lines to see detailed data for a particular date, including the total number of requests received and the percentage of those requests that were throttled due to that number exceeding your daily entitlement.

![A screen capture showing the detailed peak usage data for February 24](_images/p1-api-usage-db-daily-peak-detail.png)

Hover over the upper right corner of the pane to show icons that allow you to perform the following actions:

* Maximize the **Daily Peak HTTP Request Rates** panel: Click the **Maximize** icon (![An image of the maximize icon](../_images/p1-dashboard-maximize.png)) to hide the **Historic Peak HTTP Request Rates** table and expand the **Daily Peak HTTP Request Rates** panel.

  Click the icon again to minimize the panel.

* Click the **[icon: filter, set=fa]Filter** icon to see the filters that are applied to the graph.

* Click the **Menu options** icon (![An image of the Menu options icon](../_images/p1-dashboard-menu-options.png)) to:

  * **View summary data**: Display the data in a table format.

  * **Export to CSV**: Export the data to a CSV file for further review and analysis.

---

---
title: Assigning a key pair to an application
description: Learn how to assign a key pair to an application in PingOne to ensure secure communication and token integrity.
component: pingone
page_id: pingone:settings:p1_assign_keypair_to_an_application
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_assign_keypair_to_an_application.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 9, 2023
keywords: ["assign key pair to application", "application key pair management", "certificate management", "key pair"]
section_ids:
  steps: Steps
---

# Assigning a key pair to an application

New applications automatically use the default key pair, but you can change the key pair that an existing application uses.

## Steps

1. In the PingOne admin console, go to **Settings > Certificates and Key Pairs**.

2. On the **Key Pairs** tab, browse or search for the key pair you want to assign.

   ![A screenshot of the view of the certificates page.](_images/p1-cert-keypairs-page-keypair-tab.png)

3. Click the key pair to see more information.

4. On the **Applications** tab, locate the applicable application and click **Reassign**.

   ![A screenshot of the view of the certificates page.](_images/p1-cert-applications-tab.png)

5. For the appropriate application, click **Reassign**.

6. In the **Reassign Key Pair** modal, select the new key pair from the list and click **Continue**.

   |   |                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you change the default key, existing applications will continue to use the key that was assigned when the application was created. |

---

---
title: Certificates
description: Learn about certificates in PingOne, including their usage, details, and how they work with key pairs to secure communication and establish trust.
component: pingone
page_id: pingone:settings:p1_certificates
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_certificates.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 1, 2025
keywords: ["certificate", "certificates", "certificate management", "certificate usage", "certificate details"]
---

# Certificates

Certificates are digital credentials that PingOne uses to establish trust, verify identity, and secure communication with applications and services. They contain identifying information and details that help ensure data is exchanged safely and reliably. Certificates work alongside key pairs, a shared public and private key to enable secure data encryption.

The following table shows the default fields and descriptions for certificates in PingOne:

| Field               | Description                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| **Usage Type**      | The primary usage for this certificate, such as signing and verification, encryption, SSL, issuance. |
| **Subject DN**      | Used to identify the certificate owner.                                                              |
| **Serial Number**   | Unique identifier that is assigned to a certificate.                                                 |
| **Issuer**          | Authority that issued the certificate.                                                               |
| **Issued Date**     | The date that the certificate became valid.                                                          |
| **Expiration Date** | The date that the certificate expires.                                                               |

---

---
title: Certificates and key pairs
description: Learn about certificates and key pairs in PingOne.
component: pingone
page_id: pingone:settings:p1_certs_and_keypairs
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_certs_and_keypairs.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 9, 2023
keywords: ["certificates", "key pairs", "certificate management", "key pair management", "certificate usage", "key pair usage"]
---

# Certificates and key pairs

In PingOne, certificates and key pairs work together to protect data, verify identities, and ensure trustworthy communication between services. When you create a new environment, PingOne automatically generates two default key pairs, one for signing and one for encryption. These keys, along with their associated certificates, form the foundation of secure operations within your environment.

The following topics can help you understand how to view, create, and use certificates and key pairs to maintain strong security, support integrations, and uphold compliance.

* [Certificates](p1_certificates.html)

* [Key pairs](p1_key_pairs.html)

---

---
title: Configuring a custom notification provider for PingOne
description: Use the information in this section to configure PingOne to use a custom notification provider.
component: pingone
page_id: pingone:settings:p1_sender_configure_custom_provider
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_sender_configure_custom_provider.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 19, 2026
section_ids:
  steps: Steps
---

# Configuring a custom notification provider for PingOne

Use the information in this section to configure PingOne to use a custom notification provider.

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * You can define up to 10 SMS and Voice custom notification providers.

* When defining more than one custom provider, the first provider on the **SMS/Voice** tab is the one that's used to send notifications unless you specify one of the other providers in the notification policy you're using. |

## Steps

1. Go to **Settings > Senders**.

2. Click **+**, enter the following options, and then click **Next**:

   1. In the **Sender Type** list, select **SMS/Voice**.

   2. In the **Provider Type** list, select **Custom Provider**.

3. In the **Provider Configuration** window, enter the following information:

   * **Provider Name**: Enter a meaningful name for your provider.

   * **Authorization**:

     * To use basic authentication, select **Basic** and enter the username and password.

       |   |                                                                                                                           |
       | - | ------------------------------------------------------------------------------------------------------------------------- |
       |   | When editing an existing configuration, click **Change Account** to enter a new password for the custom provider account. |

     * To use bearer token authorization, select **Bearer** and enter the token to use.

     * To use OAuth 2.0 authorization, select **OAuth2 - Client Credentials** and enter the URL of the authorization server that provides the access token, the client's public identifier, and the client's secret.

     * To use OAuth 2.0 JSON Web Tokens (JWT) bearer authentication, select **OAuth2 - JWT Bearer** and enter the URL of the authorization server that provides the access token and the JWT assertion.

     * To use custom header authorization, select **Custom Header** and enter the header name and the value to use for the header.

   * **Scope**: Click **[icon: plus, set=fa]Add Scope** to configure an OAuth 2.0 scope.

   * **Origination**: Click **[icon: plus, set=fa]Add Sender Phone Number** to configure a sender phone number, and for each number entered, select the following:

     1. **Type**: Select the type of phone number

        * **Standard**: The sender **Number** must conform to the valid format of a full international phone number.

        * **Toll-free**: The sender **Number** should be a valid toll-free phone number (United States only). It's the customer's responsibility to confirm that the number is toll-free.

        * **Short code**: The sender **Number** must conform to the valid format of a short code phone number (United States only). It's the customer's responsibility to confirm that the number is a short code.

     2. **Countries**: For **Toll-free** and **Short code** numbers, to configure supported **Countries** for notification recipients do the following:

        * Click in the **Countries** field. The **Configure countries** modal opens.

        * Click in the **Select countries** field to display the list of countries. Select a country from the list.

          |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
          | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
          |   | * **Toll-free**: Add multiple countries in the **Select countries** list. If you don't specify a country, the specified toll-free number is only used to dispatch notifications to recipient numbers in the United States.

          * **Short code**: Select only one country in the **Select countries** list. If you don't specify a country, the specified short code is only used to dispatch notifications to recipient numbers in the United States. |

     3. **Voice**: Mark the checkbox to configure the number to dispatch voice notifications.

     4. **SMS**: Mark the checkbox to configure the number to dispatch SMS notifications.

   Repeat this step to configure additional sender phone numbers.

4. To specify the information required by the API of your provider for SMS messages, select the **SMS** checkbox and then configure the following fields:

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | You must select and configure at least one type of message (SMS or Voice). |

   1. **Type**: Choose the type of operation to issue SMS notification requests to the associated vendor **URL** endpoint.

      * **POST** (default)

      * **GET**

   2. **URL**: The vendor endpoint that receives SMS notification requests using the corresponding operation and request body.

   3. **Body** (optional):

      * **None**: The vendor endpoint receives SMS notification requests without a request body.

      * **Form**: The notification request body is in the form of key and value pairs. Click **[icon: plus, set=fa]Add Key, Value** for each new key and value pair that you want to enter.

      * **Raw**: Enter the notification request as free-form JSON text.

        |   |                                                                                                                                                                                                 |
        | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Changing the request body format style from **Form** deletes the request body's key and value pairs, and changing the format style from **Raw** deletes the request body's free-form JSON text. |

      * Include the following variables in the customized body:

        * `${from}` - Depending on vendor requirements, the `${from}` variable might be optional.

        * `${to}` - If there is a requirement to send the country code and national (significant) number separately, instead of `${to}`, the body should include:

          * `${to.country-code}`

          * `${to.national-number}`

        * `${message}`

      * You can use the following optional variables:

        * `${locale}` - locale

        * `${otp}` - OTP

      * The Body section supports dynamic variables. Learn more in [Dynamic variables](https://developer.pingidentity.com/pingone-api/platform/notifications/notifications-templates.html#notifications-templates-dynamic-variables) in the PingOne Platform API Reference.

        To prevent problems related to special character encoding when passing PingOne variables to the provider, it's recommended that you specify the type of input your provider expects when you include a PingOne variable. Use the syntax `${variable_name|format_used}`, for example, `${message|json}`.

        The formats you can specify are:

        * json

        * html

        * url

        * base64

   4. **Headers**: Enter any required headers for the SMS notification request. Click **[icon: plus, set=fa]Add Header** for each new header you want to add.

      * For JSON body format, set the header to `content-type=application/json`.

      * For x-www-form-urlencoded body format, set the header to `content-type=application/x-www-form-urlencoded`.

   5. **Plus sign**:

      * **Enabled** (default): Permit the standard number format for the sender and recipient numbers, including a leading plus sign.

      * **Disabled**: For configurations where the provider requires the sender and recipient numbers without a leading plus sign.

   6. Click **Send Test SMS** to verify your configuration.

      The **Send Test SMS** modal opens. Enter a destination phone number to test receiving an SMS notification from your configured custom provider.

      1. In the **Send To** field, select the phone number's country, and enter the destination phone number.

      2. Click **Send**.

         The **Send Test SMS** modal closes.

      3. Verify that you've received a test notification on the destination phone.

5. To specify the information required by the API of your provider for voice messages, select the **Voice** checkbox and then configure the following fields:

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | You must select and configure at least one type of message (SMS or Voice). |

   1. **Type**: Choose the type of operation to issue voice notification requests to the associated **URL** endpoint.

      * **POST**

      * **GET**

   2. **URL**: The vendor endpoint that will receive voice notification requests using the corresponding operation and request body.

   3. **Body**:

      * **None**: The vendor endpoint receives voice notification requests without a request body.

      * **Form**: The notification request body is in the form of key and value pairs. Click **[icon: plus, set=fa]Add Key, Value** for each new key and value pair that you want to enter.

      * **Raw**: Enter the notification request as free-form JSON text.

        |   |                                                                                                                                                                                                 |
        | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Changing the request body format style from **Form** deletes the request body's key and value pairs, and changing the format style from **Raw** deletes the request body's free-form JSON text. |

        * Include the following variables in the customized body:

          * `${from}` - Depending on vendor requirements, the `${from}` variable might be optional.

          * `${to}` - If there is a requirement to send the country code and national (significant) number separately, instead of `${to}`, the body should include:

            * `${to.country-code}`

            * `${to.national-number}`

          * `${message}`

        * You can use the following optional variables:

          * `${voice}` - the type of voice configured for notifications

          * `${locale}` - locale

          * `${otp}` - OTP

          * `${user.username}` - user's username

          * `${user.name.given}` - user's given name

          * `${user.name.family}` - user's family name

        * The Body section supports dynamic variables. Learn more in [Dynamic variables](https://developer.pingidentity.com/pingone-api/platform/notifications/notifications-templates.html#notifications-templates-dynamic-variables) in the PingOne Platform API Reference.

          To prevent problems related to special character encoding when passing PingOne variables to the provider, it's recommended that you specify the type of input your provider expects when you include a PingOne variable. Use the syntax `${variable_name|format_used}`, for example, `${message|json}`.

          The formats you can specify are:

          * json

          * html

          * url

          * base64

          |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
          | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
          |   | The `<repeatMessage>` and `<pause1sec>` tags aren't supported for custom provider voice one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* messages. To add a pause in a custom provider voice message, use the **Preceding padding** (`"beforeTag"`) and **Succeeding padding** (`"afterTag"`) parameters, for example: |

   4. **Preceding padding**: Set a custom pause or padding before an OTP character, to leverage vendor capabilities when sending voice notifications. For example:

      ```
      "beforeTag":"<Say>",
      ```

   5. **Succeeding padding**: Set a custom pause or padding after an OTP character to leverage vendor capabilities when sending voice notifications. For example:

      ```
      "afterTag":"</Say> <Pause length=\"1\"/>"
      ```

   6. **Headers**: Enter any required headers for the voice notification request. Click **[icon: plus, set=fa]Add Header** for each new header you want to add.

      * For JSON body format, set the header to `content-type=application/json`.

      * For x-www-form-urlencoded body format, set the header to `content-type=application/x-www-form-urlencoded`.

   7. **Plus sign**:

      * **Enabled** (default): Permit the standard number format for the sender and recipient numbers, including a leading plus sign.

      * **Disabled**: For configurations where the provider requires the sender and recipient numbers without a leading plus sign.

   8. Click **Send Test Voice** to verify your configuration.

      The **Send Test Voice** modal opens. Enter a destination phone number to test receiving a voice notification from your configured custom provider.

      1. In the **Send To** field, select the phone number's country, and enter the destination phone number.

      2. Click **Send**.

         The **Send Test SMS** modal closes.

      3. Verify that you've received a test notification on the destination phone.

6. Click **Save**.

|   |                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * When using a custom provider, if there are repeated errors within a short period or long delays before responses from the provider, PingOne assumes that there is an underlying issue and temporarily activates a circuit breaker, suspending notification attempts for that provider.

* Custom providers use a five-second connect timeout and a three-second read timeout. |

---

---
title: Configuring a custom SMTP email notification server
description: Use the Senders page to configure your organization's SMTP server.
component: pingone
page_id: pingone:settings:p1_configure_custom_smtp_server
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_configure_custom_smtp_server.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 15, 2026
section_ids:
  steps: Steps
---

# Configuring a custom SMTP email notification server

Use the Senders page to configure your organization's SMTP server.

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you use a custom SMTP server, PingOne sends email through your organization's mail infrastructure. Your domain's existing Domain-based Message Authentication, Reporting, and Conformance (DMARC) policies apply to all messages sent by PingOne from this server. |

## Steps

1. Go to **Settings > Senders**.

2. Click **+**, enter the following options, and then click **Next**:

   1. In the **Sender Type** list, select **Email**.

   2. In the **Provider Type** list, select **Custom Server**

3. In the Email Sender **Custom SMTP Server** area, enter the relevant details:

   |   |                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------ |
   |   | Any edit changes on previously saved custom server fields requires re-entry of the **Password** field. |

   | Field                | Type      | Description                                                                                                                                                                                                                    |
   | -------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Username**         | Mandatory | The organization's SMTP server's username.                                                                                                                                                                                     |
   | **Password**         | Mandatory | The organization's SMTP server's passcode.                                                                                                                                                                                     |
   | **Server Name**      | Mandatory | The name of the organization's SMTP server.                                                                                                                                                                                    |
   | **Port**             | Mandatory | The port used by organization's SMTP server to send emails (default: 465). NOTE: The protocol used depends upon the port specified. If you specify port 25,587, or 2525, SMTP with STARTTLS is used. Otherwise, SMTPS is used. |
   | **From Name**        | Optional  | The name that displays as the sender's name in the email message.                                                                                                                                                              |
   | **From Address**     | Mandatory | The email address that displays as the sender's email address in the email message.                                                                                                                                            |
   | **Reply-To Name**    | Optional  | The name that displays as the sender's reply-to name in the email message.                                                                                                                                                     |
   | **Reply-To Address** | Optional  | The email address that displays as the sender's reply-to address in the email message.                                                                                                                                         |

4. Click **Save**.

   If you haven't yet sent a test email, you might get a warning message indicating that saving SMTP settings without validating credentials using the test email button can cause problems sending emails. You can also send a test email later.

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When saving, authentication isn't tested using the new credentials. Follow up with the **Send Test Email** step to confirm successful SMTP server configuration. |

5. To test the SMTP server configuration, edit the Email entry in the **Senders** list and then click **Send Test Email**.

   The **Send Test Email** modal opens.

   ![The Send Test Email modal, showing an option to send a test email message to a specified address.](_images/TestEmailSMTP.png)

6. Enter a recipient email address in **Send to** and click **Send**.

7. Check the destination email box for the test email.

   PingOne returns one of the following status messages:

   * **Success**

     ![A successful status message with the text A test message was successfully sent to some.body at acme.com.](_images/wuh1567784302549.png)

   * **Failure**

     ![A failure status message with the message, Using the credentials you provided, we couldn't authenticate with your email server.](_images/aan1567784303621.png)

---

---
title: Configuring a Syniverse account for PingOne
description: Use the information in this section to configure PingOne to use your Syniverse account.
component: pingone
page_id: pingone:settings:p1_configure_syniverse_account
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_configure_syniverse_account.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 13, 2026
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  fallback: Fallback
  adding-syniverse-notification-tracking-to-pingone-audit-logs: Adding Syniverse notification tracking to PingOne audit logs
---

# Configuring a Syniverse account for PingOne

Use the information in this section to configure PingOne to use your Syniverse account.

## Before you begin

Ensure that you have:

* Your Syniverse account Access Token from the Syniverse dashboard.

* One or more Syniverse phone numbers that support SMS or Voice.

## About this task

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | By enabling your Syniverse account, you're taking responsibility for dispatching SMS and voice messages. |

## Steps

1. Go to **Settings > Senders**.

2. Click **+**, enter the following options, and then click **Next**:

   1. In the **Sender Type** list, select **SMS/Voice**.

   2. In the **Provider Type** list, select **Syniverse**.

   3. In the **Syniverse Account Type** list, select **Syniverse**.

3. In the **Provider Configuration** window, enter the following information to configure your Syniverse account to work with PingOne:

   |   |                                                                                 |
   | - | ------------------------------------------------------------------------------- |
   |   | A Syniverse account applies across all PingOne applications of the environment. |

   * **Provider Name**: Enter a meaningful name for the Syniverse account.

   * **Access Token**: Enter the Syniverse Access Token.

   |   |                                                                                                                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The system uses your access token to connect to your Syniverse account.Recommended: In your account in the Syniverse portal, define an application that is dedicated to PingOne traffic. Use this application for analyzing PingOne traffic throughput, and troubleshooting SMS or voice message dispatch cases. |

4. Click **Verify**. This validates the account to PingOne and populates the **Organization Numbers** list from your Syniverse account.

   |   |                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * If the **Access Token** is incorrect, an error message displays.

   * If your Syniverse account isn't fully configured, a warning displays next to the **Access Token** field.

   * If there are no organization numbers in the Syniverse account, it won't be validated to PingOne. |

   Once the account is successfully verified, **Organization Numbers** displays.

5. Select one or more phone numbers available to this Syniverse account.

   1. For **Toll-free** and **Short code** numbers, you can configure supported **Countries** for notification recipients:

      * Click in the **Countries** field. The **Configure countries** modal opens.

      * Click in the **Select countries** field to display the list of countries. Select a country from the list.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
        | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | * **Toll-free**: You can add multiple countries in the **Select countries** list. If no country is specified, the specified toll-free number can only be used to dispatch notifications to United States recipient numbers.

        * **Short code**: You can select only one country in the **Select countries** list. If no country is specified, the specified short code can only be used to dispatch notifications to United States recipient numbers. |

   2. Click the **Show only selected** or **Show all** toggle to show only the marked phone numbers and hide the numbers that aren't selected, or to show selected and unselected numbers.

   3. Click **Select all** or **Unselect all** to select or deselect all the numbers for this account.

      |   |                                                                                                                                                                                                                                                                                                                                                                                            |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | * If you intend to use both SMS and voice, all your selected numbers must support both SMS and voice.

      * Syniverse allows the use of sender IDs (in place of telephone numbers) for commercial use or to comply with regulations requiring SMSs to be sent as **transactional** and not **promotional**.

      * Sender IDs are displayed according to the Sender IDs sent in the API requests. |

6. Click **Save**. A **Third-party Service Consent** message shows. Click **I Consent** to proceed and save your changes.

   After configuring this sender, add it to a notification policy to control when PingOne uses it for SMS or voice notifications. Learn more in [Notification Policies](../user_experience/p1_creating_a_notification_policy.html).

## Fallback

If PingOne receives an error during the message dispatch process that the used number is invalid, it retries using another configured Syniverse number. After attempting to dispatch the message and receiving an error for all configured numbers, the fallback flow is triggered.

* If there is no way of originating the SMS or voice event with the tenant's own Syniverse account and you defined a fallback, the event will be originated from the configured fallback account.

* The following errors will cause fallback:

  * All API errors (but not SMS delivery errors).

  * No organization number was found on the Syniverse account.

* If a transaction was charged to a specific account, it doesn't imply that subsequent transactions will be charged to the same account. The account charged for each transaction is determined on an individual basis. Preference is always given to the custom account.

## Adding Syniverse notification tracking to PingOne audit logs

To help troubleshoot any potential issues, include Syniverse notification events in the PingOne audit logs. To include Syniverse notification events in the PingOne audit logs:

1. In the list of configured senders, locate your sendert.

2. Click the sender name. The summary of the sender configuration is displayed on the right side of the screen.

3. Copy the URL from the **Address** field.

4. In your Syniverse account:

   1. In the **Delivery Configuration**, paste the URL that you copied from the PingOne **Address** field.

   2. Create two subscriptions: **SCG-Message** and **SCG-Voice-Calls**.

      Learn more in the Syniverse article [How to setup a Webhook for Receiving Messages and Notifications](https://sdcsupport.syniverse.com/hc/en-us/articles/360001528033-How-to-setup-a-Webhook-for-Receiving-Messages-and-Notifications).

   |   |                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | These Syniverse configurations are required in order that Ping Identity's dashboards and reports will reflect complete and accurate data. Ping Identity won't be able to troubleshoot SMS or voice events related to Syniverse if these configurations are incomplete. |

---

---
title: Configuring a Twilio account for PingOne
description: How to configure your Twilio sender in PingOne to connect your users with SMS or voice notifications.
component: pingone
page_id: pingone:settings:p1_configure_twilio_account
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_configure_twilio_account.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2026
keywords: ["Twilio", "SMS", "voice", "notifications", "organization numbers", "fallback", "Syniverse"]
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  fallback: Fallback
---

# Configuring a Twilio account for PingOne

Use the information in this section to configure PingOne to use your Twilio account. To set up a Twilio Messaging Service account, refer to [Creating a Twilio Messaging Services notification sender for PingOne](p1_sender_twilio_messaging_services.html).

## Before you begin

Ensure that you have:

* Your Twilio account string identifier (SID) and Auth Token from the Twilio dashboard.

* One or more Twilio phone numbers that support SMS and Voice.

## Steps

1. Go to **Settings > Senders**.

2. Click **+**, enter the following options, and then click **Next**:

   1. In the **Sender Type** list, select **SMS/Voice**.

   2. In the **Provider Type** list, select **Twilio**.

   3. In the **Twilio Account Type** list, select **Twilio Services**.

3. Click **Next**.

4. In the **Provider Configuration** window, enter the following information to configure your Twilio account to work with PingOne:

   * **Provider Name**: Enter a meaningful name for the Twilio account.

   * **Account SID**: Enter the Twilio account SID.

   * **Auth Token**: Enter the Twilio account's Auth Token.

   |   |                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can't change the Auth Token after you save this configuration. To use a new Auth Token, create a new Twilio configuration with the updated token, then delete the original configuration. |

5. Click **Verify**. This validates the account to PingOne and populates the **Organization Numbers** list from your Twilio account.

   |   |                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * If the **Auth Token** is incorrect, an error message is displayed.

   * If there are no organization phone numbers in the Twilio account, it won't be validated to PingOne. |

   After the account is successfully verified, **Organization Numbers** displays.

6. Select one or more phone numbers available to this Twilio account.

   1. For **Toll-free** and **Short code** numbers, you can configure supported **Countries** for notification recipients:

      * Click in the **Countries** field. The **Configure countries** modal opens.

      * Click in the **Select countries** field to display the list of countries. Select a country from the list.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
        | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | * **Toll-free**: You can add multiple countries in the **Select countries** list. If no country is specified, the specified toll-free number can only be used to dispatch notifications to United States recipient numbers.

        * **Short code**: You can select only one country in the **Select countries** list. If no country is specified, the specified short code can only be used to dispatch notifications to United States recipient numbers. |

   2. Click the **Show only selected** or **Show all** toggle to show only the marked phone numbers and hide the numbers that aren't selected, or to show selected and unselected numbers.

   3. Click **Select all** or **Unselect all** to select or deselect all the organization numbers for this account.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * If you intend to use both SMS and voice, all your selected numbers must support both SMS and voice.

   * Twilio allows the use of sender IDs (in place of telephone numbers) for commercial use or to comply with regulations requiring SMSs to be sent as **transactional** and not **promotional**.

   * Sender IDs defined in Twilio aren't displayed. PingOne uses the actual phone numbers.

   * Sender IDs are displayed according to the Sender IDs sent in the API requests. |

7. Click **Save**. A **Third-party Service Consent** message shows. Click **I Consent** to proceed and save your changes.

After configuring this sender, add it to a notification policy to control when PingOne uses it for SMS or voice notifications. Learn more in [Notification Policies](../user_experience/p1_creating_a_notification_policy.html).

## Fallback

If PingOne receives an error during the message dispatch process that the used number is invalid, it retries using the fallback option defined in the [Notification policy](../user_experience/p1_creating_a_notification_policy.html).

* If there is no way of originating the SMS or voice event with the tenant's own account, and you defined a fallback to Syniverse, the event is originated from the fallback account.

* The following errors will cause fallback:

  * All API errors (but not SMS delivery errors)

  * No organization number was found on the Twilio account

* If a transaction was charged to a specific account, it doesn't imply that subsequent transactions will be charged to the same account. The account charged for each transaction is determined on an individual basis. Preference is always given to the custom account.

---

---
title: Configuring administrator security
description: Use the Administrator Security page to view or change authentication settings for the PingOne admin console.
component: pingone
page_id: pingone:settings:p1_configure_administrator_security
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_configure_administrator_security.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Configuring administrator security

Use the **Administrator Security** page to view or change the authentication settings for the PingOne admin console.

You can use PingOne, an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*, or a combination of an external IdP and PingOne to provide secure access to the admin console.

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic only applies to environments that don't include PingID. If your environment includes PingID, go to [Configuring administrator security - PingID](p1_configure_administrator_security_pingid.html). |

Ping Identity requires multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* for all PingOne administrators.

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Administrators must sign on again after 30 minutes of inactivity in the admin console. MFA is required if the last sign-on is older than 12 hours. These settings aren't configurable. |

You must have the Organization Admin role, Environment Admin role, or a custom role with equivalent permissions to configure **Administrator Security**.

## Steps

1. In the PingOne admin console, go to **Settings > Administrator Security**.

   ![Screen capture of the Administrator Security page showing PingOne as the authentication source.](_images/vnq1720529762503.png)

2. Click the **Pencil** icon to change the security settings.

   ![Screen shot of the Administrator Security page in edit mode. External IdP & PingOne is shown as the selected authentication source, and the PingOne DaVinci IdP is selected under Identity Provider.](_images/spq1720529879991.png)

3. For **Authentication Source**, select one of the following.

   ### Choose from:

   * **PingOne** (default): PingOne is used as the authentication source. A system-delivered authentication policy requiring MFA is enabled. You can't use a different authentication policy, but you can select which supported methods to use for MFA. Supported MFA methods include email, authenticator app (TOTP), and FIDO2. The first time an administrator signs on to the admin console, they're prompted to configure one of the methods you enable.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you haven't updated the MFA policies for your environment to use FIDO2 instead of FIDO, you won't see the FIDO2 option on **Administrator Settings**. Learn more in [Updating an existing MFA policy to use FIDO2](../strong_authentication_mfa/p1_updating_an_mfa_policy_to_fido2.html).FIDO isn't supported for new device registration during just-in-time (JIT) registration of administrators. If existing administrators have a registered FIDO device for MFA, that method is valid as long as your MFA policy is not updated to FIDO2. |

   * **External IdP**: This option is enabled only if you have configured at least one external IdP in your environment. The selected IdP is used as the authentication source for the admin console. If you select this option, ensure that your external IdP is configured to follow best practice security recommendations.

     You should also test the connection to ensure that it's configured correctly. Administrators will be unable to sign on if this connection is configured incorrectly.

     |   |                                                                                                                                                                                                                                        |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can't make changes to the IdP configuration from this page. Go to **Integrations > External IdPs** if you need to edit the connection. Learn more in [Editing an identity provider](../integrations/p1_editidentityprovider.html). |

   * **PingOne & External IdP**: This option is enabled only if you've configured at least one external IdP in your environment. The selected IdP is used as the initial authentication source for the admin console. After the user authenticates through the IdP, PingOne sends a secondary authentication request unless you select **Limit MFA to specific populations** and require secondary authentication only for specific populations.

     Test the connection to the IdP to ensure that it's configured correctly. If the connection to the IdP fails, the administrator can sign on to PingOne directly, as long as they have valid credentials in PingOne.

   |   |                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When configuring an external IdP for administrator single sign-on (SSO), always use the standard pingone.com domains. Using a custom domain for administrator SSO will cause authentication to fail because the admin console doesn't support custom domains. |

4. Configure the applicable settings:

   | Setting                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Allowed Authentication Methods**    | **PingOne** and **PingOne & External IdP** only.Select at least one MFA method for verification.- **Authenticator App (TOTP)**

   - **FIDO2**

   - **Email**

     &#xA;&#xA;The Administrators environment is limited to 100 email notifications per day. If you have a large number of administrators and are concerned about hitting this limit, consider using either the Authenticator App (TOTP) or FIDO2 option for notifications. You can also set one of these options as a secondary method in the event that you reach the email notification limit.&#xA;&#xA;The daily notification counters reset every night at midnight UTC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Account Recovery**                  | **PingOne** and **PingOne & External IdP** only.If selected, PingOne administrators who forget their password can recover their accounts with a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* sent to the email address configured in the PingOne user directory.&#xA;&#xA;This setting applies only to the PingOne account and not to the external IdP. Account recovery for the external IdP is managed by the provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | **Identity Provider**                 | **External IdP** and **PingOne & External IdP** only.Select the IdP to use for authentication.This IdP will be labeled with an **Administrator IDP** badge in **Integrations > External IdPs**. The IdP can't be disabled or deleted while assigned in **Administrator Security**.&#xA;&#xA;If you change the selected IdP, the settings for the new IdP are used for authentication. You should always test the connection configuration when you change this setting to ensure that administrators are able to sign on to PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | **Identifier First**                  | **PingOne & External IdP** only.If selected, you can identify users before you authenticate them.Click **Add Discovery Rule** to configure rules that will take different authentication actions based on who the user is. You can also edit existing rules.- **Username Contains**: Enter a domain name to be evaluated by this rule. The rule evaluates to true if the string contains any part of the provided value.

     &#xA;&#xA;For increased security, be specific and enter multiple canonical domains, such as @marketing.example.com and @payroll.example.com. To add fewer entries, you could just enter example.com, and the rule would pick up both @marketing.example.com and @payroll.example.com, but that configuration might match users at unintended hosts.

   - **Identity Provider**: Select the IdP to use for authentication if the rule is matched. Discovery rules are evaluated in the order they appear in the list.If the user name matches a configured rule, the system sends the user to a particular external IdP. If the user name doesn't match a configured rule, the user authenticates through PingOne. |
   | **Limit MFA to specific populations** | **PingOne & External IdP** only.Select this checkbox to require a secondary authentication request from PingOne only for the populations you select in the **Populations Requiring MFA** list. Users in populations that aren't selected will authenticate only once, through the external IdP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

5. Click **Save**.

---

---
title: Configuring administrator security - PingID
description: Use the Administrator Security page to view or change the authentication settings for the PingOne admin console.
component: pingone
page_id: pingone:settings:p1_configure_administrator_security_pingid
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_configure_administrator_security_pingid.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Configuring administrator security - PingID

Use the **Administrator Security** page to view or change the authentication settings for the PingOne admin console.

You can use PingID, an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*, or a combination of external IdP and PingID. Some configuration might need to be done in the PingID console.

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic only applies to environments that include PingID. If your environment doesn't include PingID, go to [Configuring administrator security](p1_configure_administrator_security.html). |

Ping Identity requires multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* for all PingOne administrators.

You must have the Organization Admin role, Environment Admin role, or a custom role with equivalent permissions to configure **Administrator Security**.

## Steps

1. In the PingOne admin console, go to **Settings > Administrator Security**.

   ![Screen capture of the Administrator Security page showing PingID as the authentication source.](_images/p1-admin-sec-page-pingid.png)

2. Click the **Pencil** icon to change the settings.

   ![Screen shot of the Administrator Security page in edit mode. PingID is shown as the selected authentication source.](_images/p1-admin-sec-edit-pingid.png)

3. For **Authentication Source**, select one of the following.

   ### Choose from:

   * **PingID** (default): PingID is used as the authentication source. You configure the authentication policy and set the allowed MFA methods in the PingID console. Click **Configure Now** to open the PingID admin portal in a separate window and configure the authentication policy. Learn more in the [Authentication Policy](https://docs.pingidentity.com/pingid/pingid_service_management/pid_authentication_policy.html) section of the PingID documentation.

     |   |                                                                                                                                                                                                                                                                                                                                                            |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If the environment was created after January 7, 2025, or if your PingID tenant was migrated to PingOne after March 31, 2025, the default MFA policy is managed from **Authentication > MFA** in PingOne. Learn more in [Configuring an MFA policy for strong authentication](../strong_authentication_mfa/p1_creating_an_mfa_policy_for_strong_auth.html). |

   * **External IdP**: This option is enabled only if you have configured at least one external IdP in your environment. The selected IdP is used as the authentication source for the admin console. If you select this option, ensure that your external IdP is configured to follow best practice security recommendations.

     You should also test the connection to ensure that it's configured correctly. Administrators will be unable to sign on if this connection is configured incorrectly.

     |   |                                                                                                                                                                                                                                        |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can't make changes to the IdP configuration from this page. Go to **Integrations > External IdPs** if you need to edit the connection. Learn more in [Editing an identity provider](../integrations/p1_editidentityprovider.html). |

   * **PingID & External IdP**: This option is enabled only if you have configured at least one external IdP in your environment. The selected IdP is used as the initial authentication source for the admin console. After the user authenticates through the IdP, PingID sends a secondary authentication request.

     Test the connection to the IdP to ensure that it's configured correctly. If the connection to the IdP fails, as long as the administrator has a recovery account in PingOne, the administrator can sign on to PingOne directly. PingID will then prompt them for secondary authentication.

   |   |                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When configuring an external IdP for administrator single sign-on (SSO), always use the standard pingone.com domains. Using a custom domain for administrator SSO will cause authentication to fail because the admin console doesn't support custom domains. |

4. Configure the applicable settings:

   | Setting               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Account Recovery**  | **PingID** and **PingID & External IdP** only.If selected, PingOne admins who forget their password can recover their accounts with a one-time passcode (OTP) *(tooltip: \<div class="paragraph">&#xA;\<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>&#xA;\</div>)* sent to the email address configured in the PingOne user directory.&#xA;&#xA;This setting applies only to the PingID account and not to the external IdP. Account recovery for the external IdP is managed by the provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | **Identity Provider** | **External IdP** and **PingID & External IdP** only.Select the IdP to use for authentication.This IdP will be labeled with an **Administrator IDP** badge in **Integrations > External IdPs**. The IdP can't be disabled or deleted while assigned in **Administrator Security**.&#xA;&#xA;If you change the selected IdP, the settings for the new IdP are used for authentication. You should always test the connection configuration when you change this setting to ensure that administrators are able to sign on to PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | **Identifier First**  | **PingID & External IdP** only.If selected, you can identify users before you authenticate them.Click **Add Discovery Rule** to configure rules that will take different authentication actions based on who the user is. You can also edit existing rules.- **Username Contains**: Enter a domain name to be evaluated by this rule. The rule evaluates to true if the string contains any part of the provided value.

     &#xA;&#xA;For increased security, be specific and enter multiple canonical domains, such as @marketing.example.com and @payroll.example.com. To add fewer entries, you could just enter example.com, and the rule would pick up both @marketing.example.com and @payroll.example.com, but that configuration might match users at unintended hosts.

   - **Identity Provider**: Select the IdP to use for authentication if the rule is matched. Discovery rules are evaluated in the order they appear in the list.If the user name matches a configured rule, the system sends the user to a particular external IdP. If the user name doesn't match a configured rule, the user authenticates through PingID. |

5. Click **Save**.

---

---
title: Configuring an SMS/Voice sender account with PingOne
description: If you have an existing Twilio or Syniverse account, you can configure PingOne to use it for SMS and voice notifications:
component: pingone
page_id: pingone:settings:p1_using_custom_sms_voice_sender_account
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_using_custom_sms_voice_sender_account.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 20, 2023
---

# Configuring an SMS/Voice sender account with PingOne

If you have an existing Twilio or Syniverse account, you can configure PingOne to use it for SMS and voice notifications:

* [Using a Twilio account with PingOne](p1_use_custom_twilio_account.html)

* [Using Twilio Verify with PingOne](p1_using_twilio_verify_for_notifications.html)

* [Using a Syniverse account with PingOne](p1_use_syniverse_account.html)

* You can also view [Sender IDs per country](p1_senderid_per_country.html).

If you have an account with a provider that is not one of the providers natively supported by PingOne (Twilio, Twilio Verify, and Syniverse) you can configure PingOne to use it for SMS and voice notifications:

* [Using a custom provider account with PingOne](p1_use_a_custom_provider.html)

---

---
title: Configuring trusted email addresses
description: Ping Identity can send trusted emails on your organization's behalf, from your organization's trusted domain. This option requires that you first Set up a trusted email domain for your environment, and then configure associated trusted email addresses.
component: pingone
page_id: pingone:settings:p1_configure_trusted_email
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_configure_trusted_email.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring trusted email addresses

Ping Identity can send trusted emails on your organization's behalf, from your organization's trusted domain. This option requires that you first [Set up a trusted email domain](p1_set_up_trusted_email_domain.html) for your environment, and then configure associated trusted email addresses.

## About this task

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | You can configure up to 10 trusted email addresses for each trusted email domain. |

## Steps

1. Go to **Settings > Senders**.

2. In the Senders list, in the **Email** area, click **Ping Server**, and then click the **Pencil** icon.

   ![A screen capture showing the Sender page with default options selected.](_images/trusted_email_sender_image.png)

   |   |                                                                                                                                                                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The default **Ping Server** details are shown, until a trusted email domain and its associated addresses are configured, or alternatively, a **Custom Server** is configured for the organization. The **Ping Server** settings are configurable only when a trusted email domain is already configured. |

   * **Domain**: The email domain name. Default: `pingidentity.com`.

   * **From Name**: The name that appears as the sender's name in the email message. Default: `PingOne`.

   * **From Address**: The email address that appears as the sender's email address in the email message. Default: `noreply@pingidentity.com`.

   * **Reply-To Name**: The name that appears as the sender's reply-to name in the email message. Default: `PingOne`.

   * **Reply-To Address**: The email address that appears as the sender's reply-to address in the email message. Default: `noreply@pingidentity.com`.

3. Select your trusted email domain from the **Domain** dropdown.

4. Enter the sender details:

   1. **From Name**: Enter the name that should appear as the sender's name in the email message.

   2. **From Address**: Select an email address from the dropdown, or click **[icon: plus, set=fa]New Email Address** to open the **New Email Addresses** screen and create a new address.

      In the **New Email Addresses** screen:

      1. Enter the local-part (username) of the trusted email address, and click **Done**. If the `_pingoneemail` text record was not added to your DNS, you'll have to verify the email address by clicking **Next** and carrying out the remaining steps.

      2. When you click **Next**, a verification code is mailed to the trusted email address, and the **Email Verification** screen opens.

      3. Enter the verification code in the **Verification Code** field.

      4. Click **Done**. If verification failed, or if no verification code email was received, click **Resend verification email** to retry.

5. Enter the reply-to details:

   1. **Reply-To Name**: Enter the name that should appear as the reply-to name in the email message.

   2. **Reply-To Address**: Select an email address from the dropdown, or click **[icon: plus, set=fa]New Email Address** to open the **New Email Addresses** screen and create a new address, as described for **From Address**.

6. Click **Save** to save your custom changes, or **Discard Changes** to abandon them.

---

---
title: Converting PEM certificates to a different format
description: If needed, you can convert PEM certificates to a different format, such as PFX or PKCS#7.
component: pingone
page_id: pingone:settings:p1_convertcertificate
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_convertcertificate.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2023
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Converting PEM certificates to a different format

If needed, you can convert PEM certificates to a different format, such as PFX or PKCS#7.

## Before you begin

You must have:

* The original private key that was used for the certificate

* A PEM (`.pem`, `.crt`, `.cer`) file

* OpenSSL

## About this task

Certificates are commonly issued as PFX files, with the extension `.pfx` or `.p12`. If you have a certificate in another format, you can convert it to PFX and import it to PingOne.

The PKCS#7 or P7B format is stored in Base64 ASCII format and has a file extension of `.p7b` or `.p7c`. A P7B file contains certificates but not the private key.

## Steps

1. Open a terminal window.

2. Run the command for the conversion you want to perform:

   ### Choose from:

   * PEM to PFX:

     ```
     openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile more.crt
     ```

     | Syntax                         | Description                                                                                           |
     | ------------------------------ | ----------------------------------------------------------------------------------------------------- |
     | `openssl`                      | The command for executing OpenSSL.                                                                    |
     | `pkcs12`                       | The file utility for PKCS#12 files in OpenSSL.                                                        |
     | `-export -out certificate.pfx` | Exports and saves the PFX file as `certificate.pfx.`                                                  |
     | `-inkey privateKey.key`        | Uses the private key file `privateKey.key` as the private key to combine with the certificate.        |
     | `-in certificate.crt`          | Uses `certificate.crt` as the certificate to combine with the private key.                            |
     | `-certfile more.crt`           | (Optional) Use this option if you have more than one certificate you want to include in the PFX file. |

   * PEM to PKCS#7:

     ```
     openssl crl2pkcs7 -nocrl -certfile certificate.crt -out certificate.p7b -outform DER
     ```

     | Syntax                      | Description                                                                                                                                                                                                              |
     | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     | `openssl`                   | The command for executing OpenSSL.                                                                                                                                                                                       |
     | `crl2pkcs7`                 | The file utility for PKCS#7 files in OpenSSL.                                                                                                                                                                            |
     | `-nocrl`                    | Specifies to not include a certificate revocation list (CRL) in the output file and to not read a CRL from the input file.                                                                                               |
     | `-certfile certificate.crt` | Specifies a filename containing one or more certificates in PEM format. All certificates in the file are added to the PKCS#7 structure. You can use this option more than once to read certificates from multiple files. |
     | `-out certificate.p7b`      | Outputs the file as `certificate.p7b`.                                                                                                                                                                                   |
     | `-outform DER`              | Specifies the PKCS#7 structure output format. The distinguished encoding rules (DER) format is a DER-encoded CRL structure.                                                                                              |