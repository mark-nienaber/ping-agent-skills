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
title: Custom domain impacts and migration considerations
description: Considerations for impacts and migration when configuring a PingOne custom domain.
component: pingone
page_id: pingone:settings:p1_custom_domain_impacts
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_custom_domain_impacts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 12, 2026
keywords: ["custom domain", "impacts", "migration", "considerations", "PingOne services"]
section_ids:
  how-a-custom-domain-changes-your-environment: How a custom domain changes your environment
  endpoint-mapping-reference: Endpoint mapping reference
  api-and-cors-guidance: API and CORS guidance
  transitioning-existing-integrations: Transitioning existing integrations
---

# Custom domain impacts and migration considerations

When you add a custom domain to a PingOne environment, the environment has two sets of URLs:

* Standard PingOne URLs

* Custom domain URLs

Both sets are valid and functional.

## How a custom domain changes your environment

Adding a custom domain affects how PingOne identifies itself to applications and identity providers (IdPs) in the following ways:

**Token issuer changes**: Both the OpenID Connect (OIDC) and SAML issuer defaults to the custom domain. PingOne accepts both the standard and custom domain issuer, but your configuration should be consistent. Use one or the other for a given integration, not a mix of both.

* **URL path structure**: Custom domain URLs omit the `envId` path segment that standard URLs include:

  * Standard URL: https\://auth.pingone.\<region>/\<envId>/as

  * Custom domain URL: `https://<customDomain>/as`

### Endpoint mapping reference

The following table shows how standard PingOne URLs map to custom domain URLs across supported protocols. Assume \[.codeph]`<customDomain>` is your configured domain (for example, `sso.example.com`).

| Protocol                | Purpose                     | Standard URL                                                                               | Custom domain URL                                                          |
| ----------------------- | --------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| **OIDC app**            | Issuer                      | https\://auth.pingone.\<region>/\<envId>/as                                                | https\://\<customDomain>/as                                                |
| **OIDC app**            | Token endpoint              | https\://auth.pingone.\<region>/\<envId>/as/token                                          | https\://\<customDomain>/as/token                                          |
| **SAML app**            | Issuer ID                   | https\://auth.pingone.\<region>/\<envId>                                                   | https\://\<customDomain>                                                   |
| **SAML app**            | Initiate single sign-on URL | https\://auth.pingone.\<region>/\<envId>/saml20/idp/startsso?spEntityId=\<partnerEntityId> | https\://\<customDomain>/saml20/idp/startsso?spEntityId=\<partnerEntityId> |
| **Microsoft 365 app**   | IssuerUri                   | https\://auth.pingone.\<region>/\<envId>/applications/\<appId>                             | https\://\<customDomain>/applications/\<appId>                             |
| **Microsoft 365 app**   | PassiveSignInUri            | https\://auth.pingone.\<region>/\<envId>/wsf/prp/\<appId>                                  | https\://\<customDomain>/wsf/prp/\<appId>                                  |
| **External IdP (SAML)** | ACS Endpoint                | https\://auth.pingone.\<region>/\<envId>/saml20/sp/acs                                     | https\://\<customDomain>/saml20/sp/acs                                     |
| **External IdP (SAML)** | SingleLogoutService         | https\://auth.pingone.\<region>/\<envId>/saml20/sp/slo                                     | https\://\<customDomain>/saml20/sp/slo                                     |
| **External IdP (OIDC)** | Callback URL                | https\://auth.pingone.\<region>/\<envId>/rp/callback/openid\_connect                       | https\://\<customDomain>/rp/callback/openid\_connect                       |

|   |                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne **(SP) Entity ID** for external SAML IdPs `https://auth.pingone.<region>/<uuid>` is generated by PingOne and doesn't have a custom domain equivalent. Leave this value unchanged. |

You can view the custom domain and standard URL versions of these endpoints on the **Overview** tab for the application. Learn more in [Viewing application details](../applications/p1_viewapplications.html).

## API and CORS guidance

Not all PingOne API host names support custom domains. You can find a complete list of host names that support them in [Custom Domains](https://developer.pingidentity.com/pingone-api/platform/custom-domains.html) in the PingOne API documentation.

**CORS for single-page applications (SPAs)**: If you're integrating PingOne Auth APIs with your own hosted single-page applications, cross-origin resource sharing (CORS) is typically handled automatically through the **Allowed Origins** configured in your PingOne application settings. PingOne DaVinci doesn't have a separate CORS configuration. It uses the allow lists defined in PingOne applications.

* **New integrations**: When you add new applications or IdPs after configuring a custom domain, use the custom domain URLs. This avoids the need for a migration later.

## Transitioning existing integrations

When you add a custom domain to an environment that already has configured applications or IdPs, you don't need to update these integrations to use the custom domain URLs immediately. The standard PingOne URLs remain valid.

|   |                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your custom domain routes through Cloudflare (either because it was migrated or created after Cloudflare was implemented), use custom domain URLs to take advantage of additional security features, such as inbound traffic policies. Learn more in [Migrating a custom domain to Cloudflare](p1_migrate_custom_domain_to_cloudflare.html). |

|   |                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Changing the **Issuer**, **Issuer ID**, **IssuerUri**, or **ACS URLs** for an existing integration is a breaking change. You must coordinate with your service provider or IdP partners to update their metadata and trust settings before making the switch. Both sides must update at the same time to avoid authentication failures. |

---

---
title: Managing a Syniverse account in PingOne
description: Use the information in this section to manage your Syniverse account.
component: pingone
page_id: pingone:settings:p1_manage_syniverse_account
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_manage_syniverse_account.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 9, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Managing a Syniverse account in PingOne

Use the information in this section to manage your Syniverse account.

## About this task

Managing an account includes:

* Changing active originating numbers and fallback setting (as in [Configuring a Syniverse account for PingOne](p1_configure_syniverse_account.html))

* Changing to another account

* Deleting the custom account

## Steps

1. Go to **Settings > Senders**.

   You'll see a list of Senders.

2. Click the relevant Syniverse account.

   The custom Syniverse account configuration displays.

3. Select at least one originating telephone number to use.

4. You can change the **Fallback to Default Account** settings.

5. To switch to a different account, click **Change Account**. You'll be offered the configuration window for a new account. Proceed as in [Configuring a Syniverse account for PingOne](p1_configure_syniverse_account.html).

6. To delete the active custom account, click the **Custom Provider** radio button.

7. To save your settings, click **Save**.

---

---
title: Managing a Twilio account in PingOne
description: Use the information in this section to manage your Twilio account.
component: pingone
page_id: pingone:settings:p1_manage_twilio_account
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_manage_twilio_account.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 9, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Managing a Twilio account in PingOne

Use the information in this section to manage your Twilio account.

## About this task

Managing a Twilio account includes:

* Changing active organization numbers and fallback setting (as in [Configuring a Twilio account for PingOne](p1_configure_twilio_account.html))

* Changing to another account

* Deleting the account

## Steps

1. Go to **Settings > Senders**.

   You'll see a list of Senders.

2. Click the relevant Twilio account.

   The custom Twilio account's configuration displays.

3. Select at least one originating telephone number to use.

4. You can change the **Fallback to Default Account** settings.

5. To switch to a different Twilio account, click **Change Account**. You'll be offered the configuration window for a new account. Proceed as in [Configuring a Twilio account for PingOne](p1_configure_twilio_account.html).

6. To delete the active custom account, click the **Custom Provider** radio button.

7. To save your settings, click **Save** at the bottom of the window.

---

---
title: Managing certificate and key pair expiration
description: Learn how to manage certificate and key pair expiration in PingOne to ensure uninterrupted service and maintain security.
component: pingone
page_id: pingone:settings:p1_cert_keypair_expiration_and_alerts
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_cert_keypair_expiration_and_alerts.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 21, 2026
keywords: ["certificate expiration", "key pair expiration", "certificate lifecycle management", "key pair lifecycle management"]
section_ids:
  steps: Steps
  setting-up-expiration-alerts: Setting up expiration alerts
  steps-2: Steps
---

# Managing certificate and key pair expiration

PingOne auto-generates new cryptographic keys every 90 days, exceeding best practices. To maintain uninterrupted service for your single sign-on (SSO) and encrypted applications, you must proactively manage the lifecycle of your certificates and key pairs. If these assets expire, authentication requests might fail, and secure connections will be dropped.

## Steps

If a certificate or key pair has already expired, or is nearing its expiration date, perform the following steps:

1. In the PingOne admin console, go to **Settings > Certificates and Key Pairs**.

2. Click the **Certificates** or **Key Pairs** tab to identify any items marked as expired.

3. Create or import a new key pair:

   * Create a key pair: If your organization allows self-signed keys, generate a new one directly in PingOne.

   * Import a key pair: If you require a Trusted CA-signed certificate, import the new files provided by your authority.

4. If the expired key pair was the default key pair for your environment, designate your new key as the default.

5. Ensure any applications are updated with the new public certificate.

## Setting up expiration alerts

You can configure PingOne to automatically notify your team before a certificate or key pair expires.

## Steps

1. In the PingOne admin console, go to **Monitoring > Alerts**.

2. Click the **[icon: plus, set=fa]**icon and configure the following:

   * **Name**: A unique name for the alert.

   * **Email Addresses**: The addresses to which the alert will be sent. You can specify individual email addresses or mailing lists.

3. **Alert Types**: Select the event types that will trigger the alert:

   | Option                   | Description                                                  |
   | ------------------------ | ------------------------------------------------------------ |
   | **Certificate Expiring** | Provides an alert when a certificate will expire in 60 days. |
   | **Certificate Expired**  | Provides an alert when a certificate expires.                |
   | **KeyPair Expiring**     | Provides an alert when a certificate will expire in 60 days. |
   | **KeyPair Expired**      | Provides an alert when a key pair expires.                   |

4. Click **Save**.

---

---
title: Managing opt-ins for early access features in PingOne
description: Some PingOne features are available early so that you can try them in your own environments and provide feedback before general availability. Opting in to a feature early lets you use the capability in real-world scenarios and test how it works with your specific environment configuration. You have full control over the features you enable and the environments in which you enable them, and you can remove features you opt in to from the environment at any time during the early access period.
component: pingone
page_id: pingone:settings:p1_managing_opt_ins_for_ea_features
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_managing_opt_ins_for_ea_features.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
  result-2: Result
  learn-more: Learn more
---

# Managing opt-ins for early access features in PingOne

Some PingOne features are available early so that you can try them in your own environments and provide feedback before general availability. Opting in to a feature early lets you use the capability in real-world scenarios and test how it works with your specific environment configuration. You have full control over the features you enable and the environments in which you enable them, and you can remove features you opt in to from the environment at any time during the early access period.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Not all features are enabled for early access. Additionally, early access features can be enabled only at the environment level. You can't enable an early access feature for the entire organization.Early access features related to services that aren't in the environment or that aren't allowable by the license assigned to the environment aren't available for opt-in. If you change the environment type or the license assigned to the environment, some early access features might be removed from the environment, and others might be available. You must perform a hard refresh in the browser to see the list of early access features available after making these changes. |

## Before you begin

You must have one of the following administrator roles to manage early access features for an environment:

* Organization Admin

* Environment Admin

* A custom administrator role with equivalent permissions

## Steps

1. In the PingOne admin console, go to **Settings > Environment Properties**.

2. Scroll to the **Early Access Participation** section and click **Manage Opt-Ins**.

   ![A screen shot of the Early Access Participation section of the Environment Properties page.](_images/p1-env-props-ea-opt-in-section.png)

   ### Result

   A list of early access features that are available for the environment opens.

3. Select the checkboxes for features you want to enable, or clear the checkboxes for features you want to remove.

   ![A screen capture of the Early Access Participation Opt-ins page with a feature selected.](_images/p1-env-settings-manage-opt-ins.png)

4. Click **Save**, and then click **Refresh** on the **Opt-Ins Updated** modal to see the updates in the admin console.

## Result

The early access features you enabled are listed in the **Early Access Participation** section of the **Environment Properties** page and are now ready for use. If you removed a feature, it's no longer displayed in this list.

During the early access period, click **Feedback** to let Ping Identity know if the feature meets your expectations and use case requirements or what changes you might like to see. This early feedback helps Ping understand customer context and consider feature enhancements or new features for future development.

## Learn more

Find draft documentation for early access features in the [Early Access](../early-access-features/p1_early_access_features.html) section of the PingOne documentation.

---

---
title: Migrating a custom domain to Cloudflare
description: If you have an existing custom domain in PingOne that routes to Amazon CloudFront, you should migrate it to use Cloudflare.
component: pingone
page_id: pingone:settings:p1_migrate_custom_domain_to_cloudflare
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_migrate_custom_domain_to_cloudflare.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 12, 2025
section_ids:
  preparing-for-migration: Preparing for migration
  before-you-begin: Before you begin
  steps: Steps
  result: Result
  p1-test-locally: Testing the migration locally before applying DNS configuration changes
  steps-2: Steps
  next-steps: Next steps
  completing-the-migration: Completing the migration
  before-you-begin-2: Before you begin
  steps-3: Steps
  result-2: Result
  p1-enable-mtls-custom-domain: Enabling mTLS for the custom domain (optional)
  steps-4: Steps
  result-3: Result
  disabling-mtls-for-the-custom-domain: Disabling mTLS for the custom domain
  testing-the-custom-domain: Testing the custom domain
  steps-5: Steps
---

# Migrating a custom domain to Cloudflare

As part of our continued efforts to support best practice security measures in PingOne, we'll be using Cloudflare instead of Amazon CloudFront as our custom domain ingress infrastructure.

Custom domains configured after March 17, 2025 are already using Cloudflare, and no action is required.

If you configured your custom domain before March 17, 2025, your domain is routing to CloudFront and you should consider migrating your domain to use Cloudflare.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you currently use a reverse proxy or Web Application Firewall (WAF) with a CloudFront custom domain that you plan to migrate, Cloudflare DNS must not be the authoritative nameserver for your custom domain or the provider of the reverse proxy or WAF. Before migrating your custom domain to Cloudflare, consult with your network infrastructure team to discuss these limitations. Note that Cloudflare DNS could be in use directly or through an intermediate supplier.These limitations apply to all custom domains created since March 17, 2025, as well as to any CloudFront custom domains that you are considering for migration to Cloudflare. |

Any custom domains that aren't migrated by late 2026 will be migrated automatically by Ping Identity. Migrating now gives you more control over the timing of the migration and allows you to take advantage of additional security features developed only for Cloudflare domains as soon as they are available.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Create a new custom domain in a test environment and ensure that everything works properly for your use cases before you migrate any custom domains in your Production environments. |

The easiest way to migrate your custom domain is to delete your existing domain and create it again. When you add the domain again, it will automatically start routing to Cloudflare. If your custom domain isn't receiving live traffic yet, or if your applications aren't yet configured to use the custom domain, it's safe to delete it and create it again. Learn more in [Deleting a custom domain or trusted email domain](p1_remove_custom_domain.html) and [Setting up a custom domain](p1_set_up_custom_domain.html).

If deleting your existing custom domain might cause an outage, follow the steps in this topic.

## Preparing for migration

To prepare your existing domain for migration, you must renew your TLS/SSL certificate or upload your existing certificate again. If your certificate is expired, you'll need to generate and upload a new one. Messages and labels displayed on the **Custom Domain and Email Trust** page will help you understand where you are in the process.

The following diagram illustrates the different stages of the migration:

![A diagram with the various status labels and the order in which they progress during a custom domain migration.](_images/p1-migrate-custom-domain-diagram.png)

|    |                                                                                                                                                                                                                                                                                                |
| -- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. | Your custom domain starts in **Migration Blocked** status and is routing to CloudFront.                                                                                                                                                                                                        |
| 2. | After you upload your certificate, the domain moves to **Setup in Progress** status. The domain continues to route to CloudFront.2.1.&#xA;&#xA;If there is an issue after uploading your certificate, the domain moves to Review Required status. The domain continues to route to CloudFront. |
| 3. | When setup completes, the domain moves to **Migration Ready** status and continues to route to CloudFront.                                                                                                                                                                                     |
| 4. | After you modify your DNS configuration and the changes propagate to the DNS, the domain moves to **Cloudflare Active** status. The migration is complete.                                                                                                                                     |

### Before you begin

Before you begin this process, ensure that:

* You have access to your DNS manager.

* You have a valid TLS/SSL certificate.

* The custom domain is labeled **CloudFront Active**. This label indicates that your custom domain is currently routing to Amazon CloudFront and should be migrated to Cloudflare.

* Any inbound traffic policies are either disabled or deleted. Learn more in [Adding or editing inbound traffic policies for custom domains](p1_configure_inbound_traffic_policies.html).

  If a **Certificate Expired** label is displayed, you must renew your TLS/SSL certificate to continue.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're using an LDAP gateway with Kerberos, you must add a Cloudflare SPN applicable to the region in which your organization resides. If your custom domain was created between March 17 and August 11, 2025, you must add two SPN references. Custom domains created during that time period have unique references for each custom domain, such as `<uuid>.ping-ccd.com`. Learn more in [Creating SPNs](../integrations/p1_creating_spns.html) and [SPN reference](../integrations/p1_spn_reference.html).If you don't add the necessary SPN references, a Kerberos outage can occur. |

### Steps

1. In the PingOne admin console, go to **Settings > Domains** and go to the applicable step or section based on the labels displayed on the custom domain entry:

   * **Migration Blocked** and **CloudFront Active**: Continue to [step 2](#p1-step-2) in this section.

   * **Certificate Expired**: Continue to [step 2](#p1-step-2) in this section.

   * **Migration Ready** and **CloudFront Active**: Go to [Testing the migration locally before applying DNS configuration changes](#p1-test-locally).

   * **Review Required** and **CloudFront Active**: Go to [Review Required](#p1-review-required).

2. []()Click the custom domain entry to open the details panel.

3. In the **TLS/SSL Certificate** section, click **Renew TLS/SSL certificate**.

   |   |                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your existing certificate is still valid, you can upload it again to prepare for the migration.If you don't have a TLS/SSL certificate or it has expired, generate a new certificate outside of PingOne. Learn more in [Generating a CSR for a custom domain](p1_generate_csr_for_custom_domain.html). |

   Ensure that your certificate meets the following requirements:

   * A minimum encryption of RSA-2048 or ECDSA-256 is used.

   * The certificate isn't self-signed.

   * The certificate chain leads to a globally trusted CA. If your certificate was issued by an intermediate CA, include the full intermediate certificate chain. Omitting it can cause validation errors for public clients, including PingOne services.

   * The certificate is valid.

   * If using a wildcard and Subject Alternative Name (SAN) certificate, the certificate matches the domain name.

4. In the **Renew TLS/SSL Certificate** modal, enter the following information and then click **Save**:

   * **Private Key**: A PEM-encoded unencrypted private key that matches the certificate's public key.

   * **Certificate**: A PEM-encoded certificate to import.

   * **Intermediate Certificates**: A PEM-encoded certificate chain that leads to a globally trusted CA.

|   |                                           |
| - | ----------------------------------------- |
|   | Don't include the end-entity certificate. |

## Result

A **Valid until** date is listed in the **TLS/SSL Certificate** section of the custom domain details panel, and a **TXT Record** entry is displayed in the **Cloudflare** section under the CNAME fields. One of the following status labels is displayed:

* Setup in Progress

  The steps to prepare your custom domain for migration have been completed, but the domain setup is updating in PingOne. Check back in 10 minutes.

* []()Review Required

  The preparation for migration can't be completed. If your custom domain isn't publicly accessible, possibly because it's behind a VPN or using reverse proxy, you need to complete domain control validation (DCV) for setup to complete. Copy the values from the **TXT Name** and **TXT Value** fields in the **Cloudflare** section of the details panel for the custom domain. Add these values to your DNS configuration.

  |   |                                                                                                                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If **Review Required** is still displayed after 10 minutes, try renewing your certificates again. If **Review Required** is still displayed after another 10 minutes, open a Support case. Do not continue with the migration until the issue is resolved. |

After 10 minutes or so, the **Migration Ready** label should be displayed indicating that you can proceed with the migration. The **CloudFront Active** label will also be displayed. Your custom domain is still active and routing traffic to CloudFront.

![A screen capture of the custom domain entry with the Migration Ready and CloudFront Routing labels.](_images/p1-custom-domain-mig-ready.png)

A **Cloudflare** section is displayed on the details panel after the **CloudFront** section. Note that the **CNAME Name** in both sections is the same. The **CNAME Name** for your domain doesn't change for the migration. Only the **CNAME Value** changes.

![A screen capture of the custom domain details panel showing the CloudFront and Cloudflare CNAME records and the Migration Ready and CloudFront Active labels.](_images/p1-custom-domain-mig-ready-details.png)

## Testing the migration locally before applying DNS configuration changes

When you migrate a custom domain by changing the CNAME value in your DNS configuration, you will affect live production environments. To test the changes locally first, you can add a line to your `hosts` file.

Local testing helps you discover unexpected issues that the Cloudflare configuration might cause so that you can resolve them before moving live traffic.

### Steps

To test your changes locally, complete the following steps:

1. In a terminal or command window, run `nslookup` and make sure that traffic is routing to CloudFront by verifying that the response contains `*.cloudfront.net`.

2. In the PingOne admin console, go to **Settings > Domains** and click the custom domain entry to open the details panel.

3. Copy the **CNAME Value** from the **Cloudflare** section.

4. In a terminal window, run `nslookup <cloudflareCNAMEValue>` where `<cloudflareCNAMEValue>` is the value you copied in the previous step:

   The response should look similar to the following:

   Cloudflare routing example

   ```
   Server:	        127.0.0.1
   Address:	127.0.0.1#53

   Non-authoritative answer:
   <cloudflareCNAMEValue>	canonical name = cloudflare.ping-ccd.com.
   Name:	cloudflare.ping-ccd.com
   Address: <CustomDomainIPAddress>
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your custom domain was created between March 17, 2025 and August 11, 2025, the name in the response will look something like `<UUID>.ping.ccd.com`.This example assumes the organization resides in the North America (US) region. If your organization is in a different region, the end of the canonical name differs depending on that region:- North America (Canada): `ping-ccd.ca`

   - Europe: `ping-ccd.eu`

   - Australia: `ping-ccd.com.au`

   - Asia-Pacific: `ping-ccd.asia`

   - Singapore: `ping-ccd.sg` |

5. Copy the IP address from the response.

6. Open the applicable `hosts` file for your operating system:

   * For MacOS, open `/etc/hosts`.

   * For Windows, open `C:\Windows\System32\drivers\etc\hosts`.

7. []()On a new line in the `hosts` file, add an entry similar to the following:

   ```
   <IPAddressFromNslookup>    <cloudflareCNAMEValue>
   ```

   Local traffic to the custom domain should now be routing to Cloudflare.

8. To verify that traffic is routing to Cloudflare, check the `ping-endpoint.json` file for `"server": "v2"`:

   * From a terminal window, run the following command:

     ```
     > curl -H "Cache-Control: no-cache, no-store, must-revalidate" \
         -H "Pragma: no-cache" \
         -H "Expires: 0" \
         "https://<customDomainHostname>/.well-known/ping-endpoints.json"
     ```

     If traffic is routing to Cloudflare, the response will be similar to the following example, in which the `"server": "v2"` JSON property is included at the end of the response:

     ```json
     {
       "uploadUrl":
       "https://uploads.pingone.com/environments/418ffffe-44aa-4072-8535-549a
       9fffbd0f",
       "apiUrl":
       "https://api.pingone.com/v1/environments/418ffffe-44aa-4072-8535-549a9
       fffbd0f",
       "authUrl": "https://<customDomainHostname>",
       "assetsUrl": "https://assets.pingone.com",
       "server": "v2"
     }
     ```

     If traffic is routing to CloudFront, the response will be similar to the following example, which doesn't include the `"server": "v2"` JSON property:

     ```json
     {
       "uploadUrl":"https://uploads.pingone.com/environments/418ffffe-44aa-4072-8535-
       549a9fffbd0f",
       "apiUrl":"https://api.pingone.com/v1/environments/418ffffe-44aa-4072-8535-549a9fffbd0f",
       "authUrl":"https://<customDomainHostname>",
       "assetsUrl":"https://assets.pingone.com"
     }
     ```

### Next steps

After you've verified that traffic is routing to Cloudflare using this local setup, test your single sign-on (SSO) use cases using the custom domain. If everything works as expected, remove the line from your `hosts` file that you added in [step 7](#p1-add-entry-hosts) and then complete the migration by updating your DNS configuration.

## Completing the migration

Complete the following steps to update your DNS configuration and complete the migration to Cloudflare.

|   |                                                                |
| - | -------------------------------------------------------------- |
|   | The specifics of DNS configuration depend on your DNS manager. |

### Before you begin

If you tested your migration locally, remove the `<IPAddressFromNslookup> <cloudflareCNAMEValue>` line from your `hosts` file before continuing.

### Steps

1. Lower the time-to-live (TTL) setting for the CNAME record in your DNS configuration:

   1. In the PingOne admin console, go to **Settings > Domains**.

   2. Click the custom domain entry to open the details panel.

   3. Locate the CNAME entry in your DNS configuration that matches the **CNAME Name** field of the CNAME entries in the custom domain details panel in PingOne.

   4. Set the TTL to 60 seconds.

      Setting the TTL to 60 seconds ensures that traffic quickly switches from CloudFront to Cloudflare after you update the CNAME record value and prevents a situation where some users are directed to CloudFront and some to Cloudflare. For example, if the TTL is set to 86400 seconds (24 hours), after you change the CNAME record value, DNS servers will continue to cache the old CNAME record value for up to 24 hours.

2. Wait for the period of time that the TTL was set to before you lowered it. For example, if the TTL was originally set to 86400, wait 86400 seconds (24 hours) before continuing.

3. Update the CNAME `value` entry in your DNS configuration:

   1. In the PingOne admin console, go to **Settings > Domains**.

   2. Click the custom domain entry to open the details panel.

   3. In the **Cloudflare** section, copy the entry in the **CNAME Value** field.

   4. Locate the CNAME entry in your DNS configuration that matches the **CNAME Name** field of the CNAME entries in the custom domain details panel in PingOne.

      Replace the CNAME `value` in the DNS configuration with the value you copied in the previous step.

      |   |                                                                                                                                                              |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Some DNS providers don't support a trailing period in the CNAME. If you're using one of these DNS providers, omit the trailing period from the CNAME record. |

      |   |                                                                                                                                                      |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Do not change the CNAME `name` entry in the DNS configuration because that will cause an outage and stop traffic routing through your custom domain. |

### Result

After updating the DNS value, it can take up to an hour for the **Custom Domain and Email Trust** page in PingOne to reflect the change and show the **Cloudflare Active** label. This label indicates that PingOne is detecting traffic to Cloudflare, and no further action is required.

![A screen capture of the custom domain details panel showing the Cloudflare Active label](_images/p1-custom-domain-cloudflare-active-details.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **Cloudflare Active** and **CloudFront Active** labels are applied based on the response from the custom domain when the **Domains** page is loaded. The response can be affected by DNS and browser caching, especially during an active migration.You can find information about performing a final check to ensure that your custom domain is routing to Cloudflare in [Verifying that custom domain traffic is routing to Cloudflare](p1_verifying_custom_domain_traffic_to_cloudflare.html). |

## Enabling mTLS for the custom domain (optional)

To configure inbound traffic policies to match requests using a certificate's SHA-256 thumbprint, you must enable mTLS for the custom domain.

|   |                                                                          |
| - | ------------------------------------------------------------------------ |
|   | Only custom domains routing to Cloudflare can be configured to use mTLS. |

To enable mTLS on the custom domain, do the following.

### Steps

1. In the PingOne admin console, go to **Settings > Domains**.

2. Click the custom domain entry to open the details panel.

3. In the **Mutual TLS (mTLS) Support** section, click **Enable Support**.

4. On the confirmation modal, click **Enable**.

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Changes might take up to 10 minutes to take effect.mTLS isn't compatible with some clients, including [Microsoft Entra ID hybrid join](../use_cases/p1_microsoft_entra_hybrid_join.html). Verify compatibility before enabling mTLS. |

### Result

You can now configure inbound traffic policies to use mTLS thumbprint as a match criteria for requests. Learn more in [Adding or editing inbound traffic policies for custom domains](p1_configure_inbound_traffic_policies.html).

### Disabling mTLS for the custom domain

To disable mTLS on the custom domain, do the following.

1. In the PingOne admin console, go to **Settings > Domains**.

2. Click the custom domain entry to open the details panel.

3. In the **Mutual TLS (mTLS) Support** section, click **Disable Support**.

4. On the confirmation modal, click **Disable**.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Changes might take up to 10 minutes to take effect.Disabling mTLS can interrupt traffic to your custom domain if you've configured inbound traffic policies to use mTLS thumbprint as a match criteria. |

## Testing the custom domain

Test your custom domain to ensure that it resolves to the correct location.

### Steps

1. Open a web browser and enter the address of your custom domain, such as `https://auth.example.com/myaccount`.

2. Verify that you're presented with the sign-on screen for your application or other applicable resource.

If the domain isn't working as you expected after the migration, you can revert it by replacing the CNAME value in your DNS configuration with the **CNAME Value** from the **CloudFront** section of the custom domain details panel in PingOne.

---

---
title: Promoting a Sandbox environment to Production
description: Use the Environment Properties page to promote a Sandbox environment to Production.
component: pingone
page_id: pingone:settings:p1_promote_sandbox_environment_to_prod
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_promote_sandbox_environment_to_prod.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 3, 2025
page_aliases: ["p1_demoteenvironment.adoc"]
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  result: Result
---

# Promoting a Sandbox environment to Production

Use the **Environment Properties** page to promote a Sandbox environment to Production.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Promoting a Sandbox environment to Production is a permanent change and can't be reversed. You cannot demote a Production environment to Sandbox. |

## Before you begin

To promote an environment, you must have the Environment Admin role or a custom role with equivalent permissions.

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | If you have a trial license, you can't promote Sandbox environments to Production. |

Learn more about environment types in [Sandbox and Production environments](../introduction_to_pingone/p1_introduction.html#p1-env-types).

## Steps

1. In the PingOne admin console sidebar, click the Ping Identity logo to open the **Environments** page and browse or search for the applicable environment.

2. Click the environment to view the environment properties and verify that the environment is a Sandbox environment.

   ![A screenshot of the environment details view for the BX Books environment with the Type outlined to show it is a Sandbox environment](_images/p1-env-props-sandbox-env.png)

3. Click the **Pencil** icon.

4. At the bottom of the page, under **Type**, select the **Promote to Production** checkbox.

   ![Screenshot of an environment in edit mode showing the Promote to Production checkbox selected](_images/p1-env-promote-to-prod.png)

5. Click **Save**.

6. Click **Promote** on the **Promote to Production** modal to confirm the change.

   |   |                                 |
   | - | ------------------------------- |
   |   | This action cannot be reversed. |

## Result

The environment is now a Production environment.

---

---
title: Rate Limits and Allowed IPs
description: Use the Rate Limits and Allowed IPs page in PingOne to allow traffic from specific IP addresses to exceed per IP per environment limits.
component: pingone
page_id: pingone:settings:p1_rate_limits
canonical_url: https://docs.pingidentity.com/pingone/settings/p1_rate_limits.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 4, 2025
section_ids:
  configure-rate-limits: Configuring rate limits and allowed IPs
  before-you-begin: Before you begin
  steps: Steps
  result: Result
---

# Rate Limits and Allowed IPs

To ensure that every PingOne customer has the share of resources they need at any given time, PingOne sets rate limits based on your purchased PingOne products, as well as the product APIs licensed in your product license. Rate groups, which are groups of endpoints related to a particular product or service, each have their own rate limit entitlements.

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the **API Usage Dashboard** to monitor your peak usage against the established entitlements so that you can plan effectively and request a Maximum Throughput Assurance package if necessary. Learn more in [API Usage Dashboard](p1_api_usage_dashboard.html). |

In addition to overall API usage limits based on your product license, there are environment-level limits per IP address for traffic that comes from a single IP address or server. An IP address is limited to 35% of the overall license rate by default. This limit prevents a single user, client, or device from consuming the full rate entitlement. If a significant portion of the API usage for your environment comes from a specific set of internal servers or a limited range of IP addresses, you can enter them on the **Rate Limits and Allowed IPs** page to allow traffic from those servers and addresses to exceed the **Per IP Per Environment** limits for the environment.

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For Trial licenses, an IP address can use 100% of the overall license rate, and the **Server-Sourced Traffic** list doesn't apply, but the overall rate cap is lower. |

![A screen capture of the Rate Limits and Allowed IPs page in PingOne showing a sample IP address in the Allowed IP addresses or CIDR ranges field.](_images/p1-rate-limits-allowed-ips.png)

You must have the Environment Admin role or a custom role with equivalent permissions to configure these settings. Administrators who have the Configuration Admin role can view this page but cannot edit the settings.

## Configuring rate limits and allowed IPs

Use the **Rate Limits and Allowed IPs** page in PingOne to allow traffic from specific IP addresses to exceed the Per IP Per Environment limits for the environment.

|   |                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use this setting to allow traffic concentrated through your company systems before it comes into PingOne to bypass the per IP rate limits. It isn't intended to allow excess traffic from individual user IP addresses.This setting does not allow you to exceed the per license entitlement limits. |

### Before you begin

You must have the Environment Admin role or a custom role with equivalent permissions to configure **Rate Limits and Allowed IPs**.

### Steps

1. In the PingOne admin console, go to **Settings > Rate Limits**.

   The **Maximum HTTP Requests from License \<licenseID>** table displays the per license and per IP per environment entitlement limits for each applicable rate group.

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | You can click **View API Usage Dashboard** to open the dashboard in a separate window. |

2. In the **Server-Sourced Traffic** section, enter the IP addresses or address ranges to exclude from the per IP per environment limits.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | IPv4 addresses, IPv6 addresses, and CIDR ranges are accepted. Enter one IP address or CIDR address range per line. |

3. (Optional) Click **+ Add** to add rows and enter more addresses as needed.

4. Click **Save**.

### Result

The traffic from the IP addresses or ranges you entered is no longer limited at the per IP per environment level.

To view the auditing information for when IP rate limits were exceeded, click **View rate limit alert history**. The IP rate limiting event types are selected by default. Learn more about configuring and running auditing reports in [Running an audit report](../monitoring/p1_running_audit_report.html).