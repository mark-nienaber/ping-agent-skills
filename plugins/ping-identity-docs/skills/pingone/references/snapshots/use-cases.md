---
title: Before you begin configuring Microsoft Entra hybrid join with PingOne as the federated IdP
description: Complete the prerequisites before you can configure Microsoft Entra hybrid join to allow users to access Active Directory and Entra ID resources.
component: pingone
page_id: pingone:use_cases:p1_microsoft_entra_hybrid_join_prerequisites
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_microsoft_entra_hybrid_join_prerequisites.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
section_ids:
  p1-download-entra-connect-sync: Downloading Entra Connect Sync
  steps: Steps
  p1-install-entra-connect-sync: Installing Entra Connect Sync
  steps-2: Steps
  result: Result:
  next-steps: Next steps
---

# Before you begin configuring Microsoft Entra hybrid join with PingOne as the federated IdP

Before you can set up PingOne as the federated identity provider (IdP) for Microsoft Entra ID and enable hybrid join, you must complete the prerequisites in this topic.

|   |                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Don't use a production environment or configuration in PingOne, Active Directory (AD), or Entra ID for the initial setup.

* Test the configuration in a pre-production environment before implementing in a production environment.

* Roll out the solution in stages to a limited set of users initially and gradually increase the set of users if no issues are found. |

You must have the following:

* A PingOne organization. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* A pre-production PingOne environment, such as development or test, with the PingOne SSO service added.

* An AD domain with the following:

  * Your user identities and device records stored in the domain.

  * The service account username and password.

* An Entra account with:

  * A tenant with a verified custom domain configured as a federated domain, where Entra ID redirects users to a federated IdP for authentication.

    Learn more about domains in [Managing custom domain names](https://learn.microsoft.com/en-us/entra/identity/users/domains-manage) in the Entra documentation.

  * Either the Entra Hybrid Identity Administrator or Global Administrator role assigned.

  * Entra Connect Sync installed on a domain-joined Windows Server 2016 or later following the steps in these sections:

    1. [Download Entra Connect Sync](#p1-download-entra-connect-sync).

    2. [Install Entra Connect Sync](#p1-install-entra-connect-sync).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You must use Entra Connect Sync in this configuration and can't use Entra Connect Cloud Sync. Learn more in [What is Microsoft Entra Connect?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect#) and [Comparison between Microsoft Entra Connect Sync and Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync#comparison-between-microsoft-entra-connect-and-cloud-sync) in the Entra documentation. |

## Downloading Entra Connect Sync

Download Entra Connect Sync to sync AD users and devices joined to the domain to a verified custom domain in Entra ID.

### Steps

1. Review the [Entra Connect prerequisites and hardware requirements](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-prerequisites) in the Entra documentation.

2. On a Windows-based computer, download Entra Connect Sync:

   1. In the Entra admin center, enter `Entra Connect` in the search bar.

   2. Go to **Microsoft Entra Connect > Connect Sync**.

   3. Click **Download the latest Entra Connect Sync Version**.

      ![A screen capture of the page from which to download Connect Sync in the Microsoft Entra admin center.](_images/p1-entra-hybrid-join-download-connect-sync.png)

## Installing Entra Connect Sync

After downloading Entra Connect Sync, install it with the following configuration to ensure Entra hybrid join can sync successfully with AD.

### Steps

1. On the Windows-based computer on which Entra Connect Sync is downloaded, run the installation program.

2. In the **Microsoft Entra Connect Sync** installation tool, select the checkbox to consent to the terms and click **Continue**.

3. In the **Express Settings** step, click **Customize**.

4. In the **Required Components** steps, leave all the checkboxes cleared and click **Install**.

5. In the **User Sign-In** step, select **Do not configure** for the sign-on method and click **Next**.

   ![A screen capture of the Entra Connect Sync installation program - User sign-in step.](_images/p1-entra-hybrid-join-connect-sync-user-signin.png)

6. In the **Connect to Microsoft Entra ID** step, sign on to your Entra ID account.

7. In the **Connect Directories** step, ensure the AD domain displayed for **Forest** is the AD domain you want to use for hybrid join and click **Add Directory**.

   ![A screen capture of the Entra Connect Sync installation program - Connect your directories step.](_images/p1-entra-hybrid-join-connect-sync-directory.png)

   #### Result:

   The **AD forest account** window opens.

   1. Select **Create new AD account**.

   2. Enter the applicable Enterprise admin AD account sign-on credentials.

   3. Click **OK**.

   4. In the **Connect your directories** step, click **Next**.

8. []()In the **Microsoft Entra sign-in** step, verify **User Principal Name** is set to `userPrincipalName` as the on-premise attribute to use as the Entra ID username and click **Next**.

   ![A screen capture of the Entra Connect Sync installation program - Microsoft Entra sign-in configuration step.](_images/p1-entra-hybrid-join-connect-sync-upn.png)

9. In the **Domain/OU Filtering** step:

   1. Click **Sync selected domains and OUs**.

   2. Select the checkboxes for any organizational units (OUs) where cloud users to be synced to Entra ID are located.

      |   |                                                                                                                                                                                                                                                                                                                                      |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Although you can select multiple OUs in this step, we recommend only selecting the OU where your users are located. When users can successfully authenticate with PingOne, you can configure Entra Connect Sync to sync devices in [Configuring Entra Connect Sync](p1_microsoft_hybrid_join_tasks.html#p1-configure-entra-connect). |

      ![A screen capture of the Entra Connect Sync installation program - Domain and OU filtering step.](_images/p1-entra-hybrid-join-connect-sync-ou-filtering.png)

   3. Click **Next**.

10. In the **Identifying users** step, leave the default settings and click **Next**.

    The default **Let Azure manage the source anchor** setting means Entra ID will identify users with the `sourceAnchor` attribute of `mS-DS-ConsistencyGuid`.

    ![A screen capture of the Entra Connect Sync installation program - Identifying users step.](_images/p1-entra-hybrid-join-connect-sync-identifying-users.png)

    Learn more about `sourceAnchor` in [Entra Connect: Design concepts](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/plan-connect-design-concepts) in the Entra documentation.

11. In the **Filtering** step:

    1. Choose either:

       * **Synchronize all users and devices**: Syncs all users and devices to Entra ID.

       * **Synchronize selected**: Allows you to enter a name or distinguished name (DN) of a group to sync to Entra ID.

    2. Click **Next**.

12. In the **Optional Features** step, leave all the checkboxes cleared and click **Next**.

    ![A screen capture of the Entra Connect Sync installation program - Optional features step.](_images/p1-entra-hybrid-join-connect-sync-optional-features.png)

13. In the **Configure** step, select the **Start the synchronization process when configuration completes** checkbox and click **Install**.

14. When the installation completes, click **Exit**.

15. In the Entra admin center, go to the **All users** page and verify the expected users appear. It could take a few minutes for the users to sync.

16. Use ADSI Edit to connect to your AD domain and ensure each user object in the OU for cloud users is populated with the `mS-DS-ConsistencyGuid` value after the initial sync.

    If any AD user object is missing the `mS-DS-ConsistencyGuid` value:

    1. Re-run the Entra Connect Sync installation program.

    2. In the **Tasks** step, click **Customize synchronization options** and click through the steps without changing any settings.

       ![A screen capture of the Entra Connect Sync installation program - Additional tasks step.](_images/p1-entra-hybrid-join-connect-sync-tasks.png)

    3. In the **Configure** step, select the **Start the synchronization process when configuration completes** checkbox and click **Configure**.

       ![A screen capture of the Entra Connect Sync installation program - Ready to configure step.](_images/p1-entra-hybrid-join-connect-sync-ready.png)

### Next steps

Complete the setup in [Configuring PingOne as the federated IdP](p1_microsoft_hybrid_join_tasks.html).

---

---
title: Configuring a CIBA flow
description: PingOne supports client-initiated backchannel authentication (CIBA), enabling users to approve out-of-band authentication requests.
component: pingone
page_id: pingone:use_cases:p1_configure_ciba_flow
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_configure_ciba_flow.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 20, 2026
section_ids:
  example-use-case: Example use case
  how-it-works: How it works
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  creating-the-email-templates: Creating the email templates
  steps: Steps
  p1-ciba-davinci-flow: Configuring the DaVinci flow
  steps-2: Steps
  adding-an-application: Adding an application
  steps-3: Steps
  validation: Validation
  troubleshooting: Troubleshooting
---

# Configuring a CIBA flow

Client-initiated backchannel authentication (CIBA) is an OpenID Connect (OIDC) extension that enables an end user to use an application on one device and grant consent to the application request on another device. Learn more in the [OIDC CIBA specification](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html).

The following devices are involved:

* **A consumption device**: A device the end user interacts with that initiates a CIBA request, such as a point-of-sale system.

* **An authentication device**: The device used by the end user, such as their mobile phone, to grant or deny consent to authenticate with the OpenID Provider.

  To qualify as an authentication device, the user's device must meet requirements, including that the authorization server must recognize the device and must be able to map it to the identified user based on the `login_hint` parameter in the CIBA request. The `login_hint` parameter is a hint related to the end user being authenticated, such as their username or email address. Learn more about [CIBA requests](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html#auth_request) in the OIDC CIBA specification.

CIBA provides increased security and improves the user experience by allowing end users to seamlessly grant or deny authentication requests on their mobile device.

## Example use case

1. The user attempts to purchase $50 worth of gas into a gas station pump point-of-sale terminal (consumption device).

2. The point-of-sale system initiates a CIBA request to PingOne.

3. PingOne sends an email to the user's verified email address containing a magic link that prompts the user to grant or deny the authentication request.

4. The user grants the authentication request sent to their email address from their mobile phone (authentication device)

5. The point-of-sale system allows the user to get $50 worth of gas.

## How it works

The high-level process with PingOne as the OpenID provider is as follows:

![A diagram of the high-level CIBA process using PingOne and DaVinci."](_images/p1-ciba-diagram.png)

1. 1 The user interacts with the consumption device, and the application on the consumption device sends a backchannel request (`/cibaAuthorization` endpoint) to PingOne as the OpenID provider.

   A CIBA request contains the following parameters in the request body:

   | Parameter                    | Description                                                                                                                                                                                                                                                                                                                  |
   | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `client_id`                  | The application's client ID. Required when the application's **Token Endpoint Authentication Method** is set to **Client Secret Post**. Learn more about the [CIBA Authorize endpoint](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-ciba.html) in the PingOne API documentation.     |
   | `client_secret`              | The application's client secret. Required when the application's **Token Endpoint Authentication Method** is set to **Client Secret Post**. Learn more about the [CIBA Authorize endpoint](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-ciba.html) in the PingOne API documentation. |
   | `scope`                      | The `openid` scope value is required. You can optionally include the `offline_access` scope value to request a refresh token if the application has the refresh token grant type enabled.                                                                                                                                    |
   | `binding_message` (optional) | The message displayed to the end user on the consumption device and authentication device, matching the authentication request to the transaction and ensuring the user knows what they're approving.                                                                                                                        |

   A CIBA request must also include one of the following three parameters for the application on the consumption device to identify the target end user:

   | Parameter          | Description                                                                                                     |
   | ------------------ | --------------------------------------------------------------------------------------------------------------- |
   | `login_hint`       | A string PingOne uses to map to a user, such as username or email address.                                      |
   | `id_token_hint`    | An ID token issued by PingOne representing a previous authentication for the target end user.                   |
   | `login_hint_token` | A JSON Web Token (JWT) created by the application on the consumption device, containing the user ID as a claim. |

   Learn more about [CIBA request parameters](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/ciba-intro.html) in the PingOne API documentation.

2. 2 PingOne returns a CIBA response to the application on the consumption device.

   For example:

   ```json
   {
       "auth_req_id": "003d2608-adeb-49af-8e8d-ec22f2a6198d",
       "expires_in": 120,
       "interval": 2
   }
   ```

3. 3 PingOne invokes the PingOne DaVinci CIBA flow to launch the out-of-band authentication request.

4. 4 The DaVinci CIBA flow locates the user based on the information from the CIBA request and sends an email to the user's email address on record containing a magic link.

5. 5 The application on the consumption device receives the CIBA response and begins polling PingOne for tokens, waiting for the user's authentication response. Learn more about poll mode in the [OpenID CIBA Flow specification](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html#token_request).

   1. If the user hasn't responded to the out-of-band authentication request, PingOne returns the following token response:

      ```json
      {
          "error": "authorization_pending",
          "error_description": "The request could not be completed. There was an issue processing the request.: The authorization request is still pending. (Correlation ID: <id>)"
      }
      ```

   2. If the application on the consumption device sends token requests too frequently, PingOne returns the following token response:

      ```json
      {
          "error": "slow_down",
          "error_description": "The request could not be completed. There was an issue processing the request.: The authorization request is still pending. Please slow down the poll requests. (Correlation ID: <id>)"
      }
      ```

   3. If the user declines the authentication request, PingOne returns the following token response:

      ```json
      {
          "error": "access_denied",
          "error_description": "The request could not be completed. There was an issue processing the request.: The authorization request has been denied. (Correlation ID: <id>)"
      }
      ```

   4. If the CIBA request has expired, PingOne returns the following token response:

      ```json
      {
          "error": "expired_token",
          "error_description": "The request could not be completed. There was an issue processing the request.: The authorization request for the provided auth_req_id has expired. (Correlation ID: <id>)"
      }
      ```

6. 6 The user opens the email sent to their authentication device and decides whether to grant or deny the out-of-band authentication request.

7. 7 The consumption device sends another poll request to PingOne, and if the user grants the authentication request, PingOne returns an access token and ID token.

## Goals

After completing this use case, you'll know how to:

* Configure a CIBA flow using PingOne and DaVinci.

* Send email notifications for out-of-band authentication requests to your users.

* Enable your users to grant or deny authentication requests initiated from a consumption device.

## What you'll do

1. Create notification templates for CIBA authorization email requests to the end user.

2. Configure a DaVinci CIBA sample flow to orchestrate the user experience and send email notifications to the end user.

3. Add an OIDC application to launch the DaVinci flow.

## Before you begin

* Ensure you have a PingOne organization and environment with the PingOne SSO, PingOne MFA, and DaVinci services added. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* Download the [PingOne CIBA sample flow](https://marketplace.pingone.com/item/pingone-ciba) from the Ping Identity Marketplace and extract the contents of the `.zip` archive to a folder on your computer.

* Create a notification policy in PingOne to set notification limits that can be sent to users per day. Learn more in [Notification Policies](../user_experience/p1_creating_a_notification_policy.html).

## Tasks

### Creating the email templates

Create two notification templates for the authentication request emails sent to the end user:

* Email with an authorization binding message, matching the authentication request to the transaction

* Generic email without a binding message requesting the user's approval

#### Steps

1. In the PingOne admin console, go to **User Experience > Notification Templates**.

2. Create an email template for the authorization binding message:

   1. Click **[icon: plus, set=fa]**to create the first of the two email templates.

   2. In the **Add Notification** modal, do the following:

      1. In the **Type** list, select **General**.

      2. Enter a name for the template, such as `CIBA with binding message`.

      3. Click **Create**.

   3. In the **Email** section, click the **Pencil** icon ([icon: pencil, set=fa]) next to the **Subject** field and define the subject of the email, such as `Authentication request from ${appName}`.

   4. Click the **Checkmark** icon ([icon: check, set=fa]) to save the subject.

   5. Click [icon: pencil, set=fa]in the **New Email** field to configure the email message.

      For example:

      ```html
      ${appName} wants to access your account.
      <p>
      Open this link in your browser to review the request: ${magicLink}
      <p>
      The authorization binding message for this request is ${bindingMessage}
      <p>
      If you do not recognize this request, ignore this email.
      <p>
      Request ID: ${authReqId}
      ```

   6. Click [icon: check, set=fa]to save the message.

      ![A screen capture of the CIBA email notification template with binding message.](_images/p1-ciba-notification-template-binding-message.png)

3. Create an email template for the generic message without the authorization binding:

   1. Click **[icon: plus, set=fa]**to create the second email template.

   2. In the **Add Notification** modal, do the following:

      1. In the **Type** list, select **General**.

      2. Enter a name for the template, such as `CIBA without binding message`.

      3. Click **Create**.

   3. In the **Email** section, click [icon: pencil, set=fa]in the **Subject** field to define the subject, such as `Authentication request from ${appName}`.

   4. Click [icon: check, set=fa]to save the subject.

   5. Click [icon: pencil, set=fa]in the **New Email** field to define the message.

      For example:

      ```html
      ${appName} wants to access your account.
      <p>
      Open this link in your browser to review the request: ${magicLink}
      <p>
      If you do not recognize this request, ignore this email.
      <p>
      Request ID: ${authReqId}
      ```

   6. Click [icon: check, set=fa]to save the email message.

      ![A screen capture of the CIBA email notification template without binding message.](_images/p1-ciba-notification-template-without-binding.png)

4. Go to **User Experience > Notification Policies** and click the **Copy to clipboard** icon ([icon: copy, set=fa]) for the notification policy ID you plan to use for sending notifications. You'll add the notification policy ID to the DaVinci flow.

### Configuring the DaVinci flow

Add the notification template IDs in your DaVinci flow so that DaVinci can send notifications to your end users requesting their authentication response.

#### Steps

1. In DaVinci, on the **Flows** tab, click **[icon: plus, set=fa]Add Flow** and select **Import Flow**.

2. Upload the `ciba-flow.json` file from the sample flow `.zip` file and click **Import**.

3. Enable the required flow settings:

   1. Click the **More Options** (⋮) icon and then click **Flow Settings** to open the flow settings panel.

   2. Click to enable the **PingOne Flow** toggle.

   3. Enable the **CIBA Flow** toggle.

   4. Click **Save**.

      ![A screen capture of the DaVinci flow settings requirements.](_images/p1-ciba-davinci-flow-settings.png)

4. In the flow, configure the **Binding message check node False** and **True** paths.

   ![A screen capture of the DaVinci CIBA flow with the Binding message nodes highlighted.](_images/p1-davinci-ciba-flow-binding-message.png)

   * False path

     1. Locate the **Binding message check** node.

     2. From the **False** path, click the **Sends email notification** node.

     3. In the configuration settings panel, click the **Gear** icon ([icon: gear, set=fa]) at the top. In the **PingOne Notification Details** modal, paste the notification policy ID you copied from PingOne into the **Notification Policy ID** field.

        ![A screen capture of the DaVinci CIBA flow PingOne Notification Details modal.](_images/p1-davinci-ciba-flow-notification-details.png)

     4. Click **Apply** and then click **Close**.

     5. In the configuration settings panel, for **Notification Name**, select the email template with the binding message.

     6. Click **Apply** and then click **Close**.

   * True path

     1. From the **True** path, click the **Sends email notification** node.

     2. In the configuration settings panel, for **Notification Name**, select the email template without the binding message.

     3. Click **Apply** and then click **Close**.

5. Save and deploy the flow.

6. Add a DaVinci flow policy for the CIBA flow:

   1. Go to the **Applications** tab and click **[icon: plus, set=fa]Add Application**.

   2. In the **Name** field, enter a name for the application and click **Create**.

   3. To edit the application, select the application in the **Applications** list.

   4. On the **Flow Policy** tab, click **[icon: plus, set=fa]Add Flow Policy**.

   5. In the **Policy Name** field, enter a name for the flow policy.

   6. Select **PingOne Flow Policy** to enable flows in the policy to be launched directly through PingOne.

   7. Click **Next**.

   8. In the flow list, select the **Show only CIBA Flows** checkmark to filter the results to only CIBA flows.

   9. Click the CIBA sample flow you imported and select either **Latest Version** or the most recent version of it.

      ![A screen capture of the DaVinci CIBA flow policy version selection.](_images/p1-davinci-ciba-flow-policy-version.png)

   10. Click **Next**.

   11. (Optional) Add weight distribution, such as `100` for 100 percent, and analytics information for each flow and flow version. Learn more in [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation.

   12. Click **Create Flow Policy**.

### Adding an application

Create an OIDC application in PingOne and add the DaVinci flow policy so that PingOne can launch the CIBA flow.

#### Steps

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon.

3. Create the application profile by entering the following:

   1. **Application Name**: Enter a unique identifier for the application, such as `CIBA app`.

   2. **Description** (optional): A brief description of the application.

   3. **Icon** (optional): A graphic representation of the application. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

   4. **Application Type**: Click **OIDC Web App**.

   5. Click **Save**.

4. Edit the application configuration as follows:

   1. On the **Configuration** tab:

      1. Select **CIBA** for **Grant Type** and clear other pre-selected grant types and response types.

      2. In the **Token Endpoint Authentication Method** list, select any authentication method except **None**. The default is **Client Secret Basic**.

      3. Click **Save**.

   2. On the **Policies** tab:

      1. Click **[icon: plus, set=fa]Add Policies**.

      2. On the **DaVinci Policies** tab, select the DaVinci CIBA flow policy you created in [Configuring the DaVinci flow](#p1-ciba-davinci-flow).

      3. Click **Save**.

## Validation

Now that you've configured a CIBA flow, validate the flow works:

1. Deploy and test the flow and verify the end-user paths function as expected.

2. Check the PingOne audit log for the **CIBA Authentication Succeeded** event, which applies to when the user approves or declines the request:

   1. Go to **Monitoring > Audit** and enter the report parameters to filter the results to include your flow test.

   2. Click **Run**.

   3. Verify that a **CIBA Authentication Succeeded** event type displays in the results.

## Troubleshooting

To troubleshoot issues when configuring the CIBA flow, check the PingOne audit log for the **CIBA Authentication Failed** event:

1. Go to **Monitoring > Audit** and enter the report parameters to limit the results to the show your flow testing.

2. Click **Run**.

3. Look for a **CIBA Authentication Failed** event type in the results.

4. Click **View** in the **Details** column for any **CIBA Authentication Failed** event types and review the event details to determine what issues caused the flow to fail.

---

---
title: Configuring OAuth 2.0 token exchange
description: PingOne supports OAuth 2.0 token exchange as an extension of OAuth 2.0, exchanging one security token for another token.
component: pingone
page_id: pingone:use_cases:p1_oauth_2_token_exchange
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 25, 2026
section_ids:
  how-it-works: How it works
  what-youll-do: What you'll do
  before-you-begin: Before you begin
---

# Configuring OAuth 2.0 token exchange

PingOne supports OAuth 2.0 token exchange, allowing an application to exchange a security token it already has for an access token to access a custom resource. Learn more about the [RFC 8693 - OAuth 2.0 Token Exchange specification](https://datatracker.ietf.org/doc/html/rfc8693) in the Internet Engineering Task Force (IETF) documentation.

OAuth 2.0 token exchange enhances security by restricting the scope or audience of a token and provides a seamless user experience without requiring reauthentication when accessing multiple resources.

PingOne supports many OAuth 2.0 token exchange use cases, including the following examples:

* Impersonation: Allows an application to act as the user. The access token represents the user's identity, and the custom resource handles the request as if it came from the user.

* Delegation: Allows an application to act on behalf of a user. The access token contains information about the user (*subject*) and the application performing the action (*actor*) on the user's behalf.

* Machine-to-machine interaction: Enables server-to-server communication and shields downstream resources from the original upstream caller.

## How it works

OAuth 2.0 token exchange allows an application (client) in PingOne to send a token request when accessing protected resources where the application:

* Uses the token exchange grant type.

* Provides the required subject token and optional actor token as inputs.

  * The subject token is the original security token and identifies the entity (user or application) for which the new token is being requested.

  * The actor token provides additional information. For example, it can represent the entity making the request on behalf of the subject, such as in delegation scenarios.

* Specifies the type of input tokens and output token.

## What you'll do

To enable token exchange in PingOne, you can set up the following use cases:

* [Impersonation](p1_oauth_2_token_exchange_impersonation.html): Set up an application to act as the user and retrieve information from a custom resource.

* [Delegation](p1_oauth_2_token_exchange_delegation.html): Set up an application to act on behalf of the user when retrieving information from a custom resource.

* [Machine-to-machine interaction](p1_oauth_2_token_exchange_machine_to_machine.html): Set up a backend application to retrieve information from a custom resource, which then retrieves additional information from another resource without exposing that call to the application.

## Before you begin

To configure any of the OAuth 2.0 token exchange use cases, you'll need:

* A PingOne organization. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* A PingOne environment with the PingOne SSO service added.

---

---
title: Configuring PingOne as an external IdP in ZIdentity
description: Configure PingOne as an external identity provider in ZIdentity to enable single sign-on using OpenID Connect.
component: pingone
page_id: pingone:use_cases:p1_configure_p1_as_idp_in_zscaler
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_configure_p1_as_idp_in_zscaler.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 20, 2024
---

# Configuring PingOne as an external IdP in ZIdentity

You can configure PingOne as an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* to enable single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* to ZIdentity using the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* authentication protocol.

Learn more in [Configuring PingOne as an External IdP](https://help.zscaler.com/zidentity/configuring-pingone-external-idp) in the ZIdentity documentation.

---

---
title: Configuring PingOne as the federated IdP
description: Set up Microsoft Entra hybrid join to allow users to access Active Directory and Entra ID resources.
component: pingone
page_id: pingone:use_cases:p1_microsoft_hybrid_join_tasks
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_microsoft_hybrid_join_tasks.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2025
section_ids:
  p1-connect-users-microsoft365: User authentication
  p1-create-attribute: Creating an attribute in PingOne
  steps: Steps
  p1-add-ldap-gateway: Adding an LDAP gateway to connect PingOne with AD
  steps-2: Steps
  example: Example
  p1-add-auth-policy: Adding an authentication policy
  steps-3: Steps
  p1-add-microsoft-app: Adding a Microsoft 365 application
  p1-hybrid-join-custom-domains: Custom domains
  steps-4: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  p1-update-microsoft-app-user-auth: Updating the Microsoft 365 application
  steps-5: Steps
  example-scenarios: Example scenarios
  p1-assign-policy-to-microsoft-app: Assigning the authentication policy to the Microsoft 365 application
  steps-6: Steps
  results: Results
  p1-enable-hybrid-join: Hybrid join
  before-you-begin: Before you begin
  p1-create-attributes: Creating attributes and a population for hybrid joined devices
  steps-7: Steps
  p1-enable-kerberos: Enabling Kerberos authentication
  steps-8: Steps
  p1-add-user-type: Adding a user type for hybrid joined devices
  steps-9: Steps
  example-2: Example
  p1-update-microsoft-app: Updating the Microsoft 365 application
  steps-10: Steps
  p1-update-federated-idp: Updating the federated IdP setting
  before-you-begin-2: Before you begin
  steps-11: Steps
  p1-allow-join-devices: Allowing users to join their devices to Entra ID
  steps-12: Steps
  p1-configure-entra-connect: Configuring Entra Connect Sync and verifying the SCP
  before-you-begin-3: Before you begin
  steps-13: Steps
  result-4: Result:
  result-5: Result
  p1-disable-fallback-sync: (Optional) Disabling fallback sync in Windows
  steps-14: Steps
  p1-hybrid-join-validation: Validation
  result-6: Result:
  example-3: Example:
  troubleshooting: Troubleshooting:
  result-7: Result:
  result-8: Result:
  troubleshooting-2: Troubleshooting
  whats-next: What's next
---

# Configuring PingOne as the federated IdP

You're ready to configure Microsoft Entra hybrid join with PingOne as the federated identity provider (IdP) after:

* Reviewing the overview in [Setting up PingOne as the federated IdP for Microsoft Entra ID](p1_microsoft_entra_hybrid_join.html)

* Completing the prerequisites in [Before you begin configuring Microsoft Entra hybrid join with PingOne as the federated IdP](p1_microsoft_entra_hybrid_join_prerequisites.html)

To set up PingOne as the federated IdP, you'll configure PingOne to fulfill two use cases:

1. [User authentication](#p1-connect-users-microsoft365): Set up PingOne as the federated IdP to connect users to sign on to Microsoft 365.

2. [Hybrid join](#p1-enable-hybrid-join): After setting up PingOne as the federated IdP, enable PingOne to process hybrid join requests to sync devices from on-premise Active Directory (AD) to Entra ID if your organization plans to transition their AD infrastructure to the cloud with Entra ID.

## User authentication

Set up PingOne as the federated IdP for Entra ID so that your users can authenticate with PingOne when attempting to use single sign-on (SSO) to access resources like Microsoft 365.

### Creating an attribute in PingOne

By default, Entra Connect Sync uses the `userPrincipalName` attribute from AD as the source of the Entra ID username. In most deployments, the `userPrincipalName` attribute value looks like an email address and might match the value of the email address (`mail` attribute) in the PingOne user record. However, in some deployments, the attributes don't match.

If the values don't match, PingOne can't match a user record to the username token from Entra ID. To ensure PingOne can locate the user record, create a custom user attribute in PingOne to store the `userPrincipalName` attribute value instead of relying on the `mail` attribute as the username.

#### Steps

1. In the PingOne admin console, go to **Directory > User Attributes** and click the **[icon: plus, set=fa]**icon.

2. Select **Declared** for the attribute type and click **Next**.

3. Enter or edit the following:

   1. **Name**: A unique identifier for the attribute, such as `ms-upn`.

   2. **Display Name** (optional): The name of the attribute as you want it to display in the UI.

   3. **Description** (optional): A brief description of the attribute.

   4. Select the **Enforce unique values** checkbox and click **Confirm** in the **Enable Enforce Unique Values** modal.

   5. Verify the **Allow multiple values** checkbox is cleared and **No Validation** is selected in the list.

4. Click **Save**.

### Adding an LDAP gateway to connect PingOne with AD

Add an LDAP gateway and optionally enable Kerberos authentication to authenticate AD users through SSO.

#### Steps

1. In the PingOne admin console, [add an LDAP gateway](../integrations/p1_add_ldap_gateway.html) for Microsoft 365 and select **Microsoft Active Directory** for **LDAP Directory Type**.

2. To enable Kerberos authentication for a seamless SSO experience:

   1. Select the **Enable Kerberos Authentication** checkbox.

   2. Enter the **Service Account User Principal Name** and **Service Account Password**.

   3. Click **Save**.

   4. [Configure the service account](../integrations/p1_creating_spns.html) with the appropriate `servicePrincipalName` to enable Kerberos authentication.

      Learn more in [SPN reference](../integrations/p1_spn_reference.html).

   5. [Configure end user browsers](../integrations/p1_configuring_end_user_browsers.html) with the required trusted URIs to support Kerberos authentication.

3. Add a user type for cloud users:

   1. On the **Lookup** tab of the LDAP gateway, click the **[icon: plus, set=fa]**icon.

   2. Click **Use default values** to pre-populate fields with values PingOne needs when connecting to your on-premise AD.

   3. Configure the following:

      > **Collapse: LDAP gateway configuration**
      >
      > | Setting                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      > | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      > | **User Type**                                               | Enter a name for the user type, such as `cloud user`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      > | **Select Password Authority**                               | Select **LDAP** in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      > | **Enable password changes from PingOne**                    | Select to enable the checkbox.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      > | **User Search LDAP Base DN**                                | Enter the distinguished name (DN) of the organizational unit (OU) where users synced to Entra ID are located. Use a specific DN location where only the users are located, instead of a broad location that includes both users and devices.#### Example`OU=Employees,OU=People,DC=pingdemo,DC=ping-eng,DC=com`You can find the DN in ADSI Edit:1) Right-click the **CN=Computers** folder under your computer name.
      >
      > 2) In the **CN=Computers Properties** modal, locate the **distinguishedName** attribute and copy it.
      >
      >    ![A screenshot of ADSI Edit with the distinguishedName attribute selected.](_images/p1-entra-hybrid-join-distinguishedName.png)                                                                                                                                                                                                                                                                                                                                                                                     |
      > | **User Link Attributes**                                    | Leave the pre-populated default attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      > | **Enable migration of new users upon first authentication** | Select to enable the checkbox.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      > | **LDAP Filter**                                             | Enter the following to limit the filter to search for AD user records only:```
      > (&(objectClass=user)(objectCategory=person)(|(sAMAccountName=${identifier})(mail=${identifier})(userPrincipalName=${identifier})))
      > ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      > | **Population**                                              | Select a population in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      > | **Update PingOne user attributes as users sign on**         | Select to enable the checkbox.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      > | **Map Attributes**                                          | 1. Leave the pre-populated default mappings.
      >
      >    &#xA;&#xA;The default source of External ID is the mS-DS-ConsistencyGuid attribute because Entra Connect Sync uses the mS-DS-ConsistencyGuid attribute as the sourceAnchor attribute to identify synced users by default. If you selected another AD user attribute as the sourceAnchor attribute in Installing Entra Connect Sync (step 11), select that AD user attribute as the source of External ID in this step.
      >
      > 2. Add a mapping for the custom attribute you created in [Creating an attribute in PingOne](#p1-create-attribute).
      >
      >    1. Click **[icon: plus, set=fa]Add Mapping**.
      >
      >    2. In the **PingOne User Profile Attribute** list, select the custom attribute you previously created to store `userPrincipalName` from AD user objects.
      >
      >    3. In the **LDAP Attribute** field, enter `userPrincipalName`.You can find more information about the required attribute mappings in [User type for cloud users](p1_microsoft_hybrid_join_troubleshooting.html#p1-cloud-user-type). |

   4. Click **Save**.

### Adding an authentication policy

Create an authentication policy with a **Login** step to verify AD user identities through LDAP authentication.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can optionally use a DaVinci flow policy instead of an authentication policy to orchestrate the authentication experience. If your users access Microsoft 365 desktop applications, such as Excel for Windows, consider opting in to the Legacy Browser and WebView Compatible Rendering Mode early access feature in PingOne. Learn more in [Managing opt-ins for early access features in PingOne](../settings/p1_managing_opt_ins_for_ea_features.html). |

#### Steps

1. In the PingOne admin console, go to **Authentication > Authentication** and click **[icon: plus, set=fa]Add Policy**.

2. Enter a **Policy Name**, such as `Authentication policy for Microsoft 365`.

3. In the **Step Type** list, select **Login**.

4. In the **Migrate Gateways Users upon First Authentication** section, click **[icon: plus, set=fa]Add Gateway User Type**.

5. Select the **Gateway** and **User Type** you previously created in [Adding an LDAP gateway to connect PingOne with AD](#p1-add-ldap-gateway).

6. [Configure the recovery and registration settings](../authentication/p1_add_login_auth_step.html) as needed.

7. To add multi-factor authentication (MFA):

   1. Click **[icon: plus, set=fa]Add step**.

   2. Select the desired step type.

   3. Configure the step as required.

8. Click **Save**.

### Adding a Microsoft 365 application

Add a Microsoft 365 application and run the PowerShell cmdlets to allow your users to sign on using PingOne.

If you're using a custom domain for configuring hybrid join, refer to the following section to determine whether you can use your custom domain in the PowerShell cmdlets to set up PingOne as the federated IdP. Hybrid join doesn't support using a custom domain if mutual TLS (mTLS) is enabled for the domain.

#### Custom domains

PingOne uses the Cloudflare infrastructure to handle traffic routing for custom domains created after March 17, 2025, but custom domains created before this date use the AWS CloudFront infrastructure.

Hybrid join using Entra ID only supports custom domains using the following infrastructure:

* CloudFront

* Cloudflare only if mTLS is disabled

Hybrid join doesn't support custom domains using the Cloudflare infrastructure if mTLS is enabled. The following types of custom domains are supported:

| Custom domain infrastructure  | Supported? |
| ----------------------------- | ---------- |
| CloudFront                    | Yes        |
| Cloudflare with mTLS disabled | Yes        |
| Cloudflare with mTLS enabled  | No         |

To configure PingOne as the federated IdP using the PowerShell cmdlets in PingOne, you must:

1. Determine whether your custom domain traffic is routed through CloudFront or Cloudflare infrastructure.

2. For custom domains with traffic routed through Cloudflare, determine whether the domain has mTLS enabled.

3. Use either the custom domain or PingOne domain for the PowerShell cmdlets depending on which configuration your custom domain uses, as shown in the following diagram:

   ![A diagram showing how to determine whether to use your custom domain or the PingOne domain in the PowerShell cmdlets.](_images/p1-entra-hybrid-join-custom-domain-flowchart.png)

   * For custom domains using the CloudFront infrastructure, you can choose whether to use your custom domain or the PingOne domain.

   * For custom domains using the Cloudflare infrastructure:

     * If mTLS is disabled, you can choose whether to use your custom domain or the PingOne domain.

     * If mTLS is enabled, you can't use your custom domain in the PowerShell cmdlets and must use the PingOne domain.

#### Steps

1. In the PingOne admin console, [add a Microsoft 365 application](../applications/p1_adding_microsoft_365.html).

2. In the **Map Attributes** step:

   1. Map the **ImmutableID** and **Subject** attributes and sync them to Entra ID using the following advanced expression:

      ```
      #string.uuidAsBase64Guid(user.externalId,null)
      ```

   2. Map the **UPN** attribute by selecting the `userPrincipalName` attribute you previously created in the **PingOne Mappings** list.

3. If the authentication policy you previously created includes MFA, [configure an authentication claim](../applications/p1_configure_authentication_claim_microsoft_365.html) for the Microsoft 365 application to communicate to Entra ID that PingOne will handle MFA.

4. If you're using a custom domain, determine whether your domain uses the CloudFront or Cloudflare infrastructure by opening a terminal window and choosing either of the following:

   * Run `nslookup <yourcustomdomain.com>`.

     #### Result:

     The following is an example response for a custom domain using the CloudFront infrastructure:

     > **Collapse: CloudFront routing example**
     >
     > ```
     > Server:		10.247.247.54
     > Address:	10.247.247.54#53
     >
     > Non-authoritative answer:
     > <yourcustomdomain.com>	canonical name = 08b31479-e3a6-43a7-900c-68fb8f4dc738.edge1.pingone.com.
     > 08b31479-e3a6-43a7-900c-68fb8f4dc738.edge1.pingone.com	canonical name = d3j27p1mzr08wt.cloudfront.net.
     > Name:	d3j27p1mzr08wt.cloudfront.net
     > Address: 18.64.183.63
     > Name:	d3j27p1mzr08wt.cloudfront.net
     > Address: 18.64.183.104
     > Name:	d3j27p1mzr08wt.cloudfront.net
     > Address: 18.64.183.109
     > Name:	d3j27p1mzr08wt.cloudfront.net
     > Address: 18.64.183.116
     > ```

     The following is an example response for a custom domain using the Cloudflare infrastructure:

     > **Collapse: Cloudflare routing example**
     >
     > ```
     > Server:		10.247.247.54
     > Address:	10.247.247.54#53
     >
     > Non-authoritative answer:
     > <yourcustomdomain.com>	canonical name = a97e2bbf-6680-12b6-a2cf-97aa0b4a4227.edge1.pingone.com.
     > a97e2bbf-6680-12b6-a2cf-97aa0b4a4227.edge1.pingone.com	canonical name = 1238af3f-0d5b-4cc8-8460-8a35a26efc5d.ping-ccd.com.
     > Name:	1238af3f-0d5b-4cc8-8460-8a35a26efc5d.ping-ccd.com
     > Address: 130.250.137.31
     > ```

   * Run `dig <yourcustomdomain.com>`.

     #### Result:

     The following is an example response for a custom domain using the CloudFront infrastructure:

     > **Collapse: CloudFront routing example**
     >
     > ```
     > ; <<>> DiG 9.10.6 <<>> <yourcustomdomain.com>
     > ;; global options: +cmd
     > ;; Got answer:
     > ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 33676
     > ;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 0, ADDITIONAL: 1
     >
     > ;; OPT PSEUDOSECTION:
     > ; EDNS: version: 0, flags:; udp: 4000
     > ;; QUESTION SECTION:
     > ;<yourcustomdomain.com>.	IN A
     >
     > ;; ANSWER SECTION:
     > <yourcustomdomain.com>.	284 IN CNAME 08b31479-e3a6-43a7-900c-68fb8f4dc738.edge1.pingone.com.
     > 08b31479-e3a6-43a7-900c-68ab8f4dc738.edge1.pingone.com. 14471 IN CNAME	d3j27p1mzr08wt.cloudfront.net.
     > d3j27p1mzr08wt.cloudfront.net. 44 IN	A	18.64.183.63
     > d3j27p1mzr08wt.cloudfront.net. 44 IN	A	18.64.183.104
     > d3j27p1mzr08wt.cloudfront.net. 44 IN	A	18.64.183.116
     > d3j27p1mzr08wt.cloudfront.net. 44 IN	A	18.64.183.109
     >
     > ;; Query time: 4 msec
     > ;; SERVER: 10.247.247.54#53(10.247.247.54)
     > ;; WHEN: Tue Mar 04 14:41:08 PST 2025
     > ;; MSG SIZE  rcvd: 248
     > ```

     The following is an example response for a custom domain using the Cloudflare infrastructure:

     > **Collapse: Cloudflare routing example**
     >
     > ```
     > ; <<>> DiG 9.10.6 <<>> <yourcustomdomain.com>
     > ;; global options: +cmd
     > ;; Got answer:
     > ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 21291
     > ;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1
     >
     > ;; OPT PSEUDOSECTION:
     > ; EDNS: version: 0, flags:; udp: 4000
     > ;; QUESTION SECTION:
     > ;<yourcustomdomain.com>.	IN	A
     >
     > ;; ANSWER SECTION:
     > <yourcustomdomain.com>. 300	IN	CNAME	a97e2bbf-6680-12b6-a2cf-97aa0b4a4227.edge1.pingone.com.
     > a97e2bbf-6680-12b6-a2cf-97aa0b4a4227.edge1.pingone.com. 2501 IN CNAME 1238af3f-0d5b-4cc8-8460-8a35a26efc5d.ping-ccd.com.
     > 1238af3f-0d5b-4cc8-8460-8a35a26efc5d.ping-ccd.com. 300	IN A 130.250.137.31
     >
     > ;; Query time: 36 msec
     > ;; SERVER: 10.247.247.54#53(10.247.247.54)
     > ;; WHEN: Tue Mar 04 14:47:09 PST 2025
     > ;; MSG SIZE  rcvd: 211
     > ```

5. If your custom domain uses the Cloudflare infrastructure, determine whether mTLS is enabled using the `/customDomains/{{customDomainId}}` API endpoint. Learn more in [Custom domains](https://developer.pingidentity.com/pingone-api/platform/custom-domains.html) in the PingOne API documentation.

6. On the **Overview** tab, copy the PowerShell cmdlets to set up PingOne as the federated IdP, depending on whether you're using a custom domain and how the domain is configured. Learn more in [Custom domains](#p1-hybrid-join-custom-domains).

   * If you aren't using a custom domain, if you're using a custom domain with the CloudFront infrastructure, or if you're using a custom domain with the Cloudflare infrastructure with mTLS disabled, copy the default PowerShell cmdlets.

   * If you're using a custom domain with the Cloudflare infrastructure with mTLS enabled, click **Show PingOne Domain** to change the PowerShell cmdlets to use the PingOne domain and copy the cmdlets.

     ![A screen capture of the Microsoft 365 application Overview tab with Show PingOne Domain circled.](_images/p1-entra-hybrid-join-powershell-domain.png)

7. Open PowerShell and select the **Run as Administrator** option.

8. In PowerShell, paste and run the cmdlets.

   |   |                                                                              |
   | - | ---------------------------------------------------------------------------- |
   |   | You might be prompted to sign on with your Entra account to run the cmdlets. |

   #### Result:

   Your custom domain now has the **Federated** checkmark in the Entra admin center with PingOne as the federated IdP.

### Updating the Microsoft 365 application

After adding the Microsoft 365 application, you'll need to update it by:

* Enabling advanced configuration.

* Specifying the attribute to match a PingOne user record to the username from security token service (STS) requests. Refer to the example scenarios for guidance on which attribute to select, depending on your configuration.

#### Steps

1. In the PingOne admin console, go to **Applications > Applications** and select the Microsoft 365 application.

2. On the **Overview** tab, click **Enable Advanced Configuration** and click **Enable** in the confirmation modal.

3. On the **Configuration** tab, click the **Pencil** icon ([icon: pencil, set=fa]).

4. In the **Attribute to identify users from username tokens** list, select the attribute for PingOne to use when matching the username from the STS request to an existing user reocrd.

   Use the example scenarios in the following section for guidance on which attribute to select.

5. Click **Save**.

#### Example scenarios

The following scenarios describe example configurations and which attribute to select for PingOne to match to the username token:

> **Collapse: Example 1: You use  from AD as the Entra ID username, and the  and  attributes always share the same value.**
>
> | Attribute configurations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Username attribute selection                                                                                                                                                                                                                                                                                                                                                                                   |
> | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | You set up the following attribute configurations:- Kept the default mapping for **User Principal Name** to `userPrincipalName` in [Installing Microsoft Entra Connect Sync](p1_microsoft_entra_hybrid_join_prerequisites.html#p1-install-entra-connect-sync-upn)
>
> - Kept the default mapping for `mail` attribute from AD to **Email Address** in PingOne when [adding an LDAP gateway user type for cloud users](#p1-add-ldap-gateway)
>
> - Didn't create a custom attribute to store `userPrincipalName` in PingOne | In this example configuration, you can select either **None** or **Email Address** if the `userPrincipalName` and `mail` attributes always share the same value.Selecting either has the same outcome because the username in the username token is the `userPrincipalName` for the user, and PingOne can locate an existing user profile by matching the username from the token to the email address record. |

> **Collapse: Example 2: You use  from AD as the Entra ID username and store  from AD in PingOne.**
>
> | Attribute configurations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Username attribute selection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
> | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | You set up the following attribute configurations:- Kept the default mapping for **User Principal Name** to `userPrincipalName` in [Installing Microsoft Entra Connect Sync](p1_microsoft_entra_hybrid_join_prerequisites.html#p1-install-entra-connect-sync)
>
> - Kept the default mapping for `mail` attribute from AD to **Email Address** in PingOne when [adding an LDAP gateway user type for cloud users](#p1-add-ldap-gateway)
>
> - [Created a custom attribute](#p1-create-attribute) to store `userPrincipalName` in PingOne and mapped the custom attribute when [adding an LDAP gateway user type for cloud users](#p1-add-ldap-gateway) | * If the `userPrincipalName` and `mail` attributes always share the same value, you can select **None**. You can alternatively select **Email Address** or the custom attribute you created to store `userPrincipalName` in PingOne.
>
>   Selecting any of these has the same outcome because the username in the username token is the `userPrincipalName` for the user, and PingOne can locate an existing user profile by matching the username from the token to the selected attribute.
>
> * If the `userPrincipalName` and `mail` attributes don't always share the same value, select the custom attribute you created to store `userPrincipalName` in PingOne. PingOne can locate an existing user profile by matching the username from the token to the custom attribute.
>
>   If you don't select the custom attribute you created, PingOne won't be able to locate the user record for any user whose `userPrincipalName` and `mail` attributes don't share the same value. This can lead to failures, such as PingOne not being able to obtain a primary refresh token (PRT) from Entra ID. |

> **Collapse: Example 3: You use an alternative AD user attribute as the Entra ID username.**
>
> | Attribute configurations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Username attribute selection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
> | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | You set **User Principal Name** to a different AD user attribute (not `userPrincipalName`) to use as the Entra ID username.In this scenario, you must:1) Create a custom user attribute in PingOne to store the AD attribute you set for **User Principal Name**. Learn more in [Creating an attribute in PingOne](#p1-create-attribute).
>
> 2) Map the attribute from AD to the custom attribute in PingOne in the LDAP gateway user type for your cloud users. Learn more in [Adding an LDAP gateway to connect PingOne with AD](#p1-add-ldap-gateway). | Select the custom attribute you created to store the AD attribute you set for **User Principal Name** in Entra. This enables PingOne to locate an existing user profile by matching the username in the username token to this attribute.If you don't select the custom attribute you created, PingOne won't be able to locate the user record for any user whose `userPrincipalName` and `mail` attributes don't share the same value. This can lead to failures, such as PingOne not being able to obtain a PRT from Entra ID. |

### Assigning the authentication policy to the Microsoft 365 application

Assign the authentication policy you created in [Adding an authentication policy](#p1-add-auth-policy) to the Microsoft 365 application to set how PingOne authenticates users.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can optionally use a DaVinci flow policy instead of an authentication policy to orchestrate the authentication experience. If your users access Microsoft 365 desktop applications, such as Excel for Windows, consider opting in to the Legacy Browser and WebView Compatible Rendering Mode early access feature in PingOne. Learn more in [Managing opt-ins for early access features in PingOne](../settings/p1_managing_opt_ins_for_ea_features.html). |

#### Steps

1. In the PingOne admin console, go to **Applications > Applications** and click the Microsoft 365 application.

2. On the **Policies** tab, click **[icon: plus, set=fa]Add Policies**.

3. On the **PingOne Policies** tab, select the authentication policy you previously created.

4. Click **Save**.

### Results

A user can now sign on to Microsoft 365:

* In a browser at <https://www.office.com>:

  1. The user enters a username in the format of `<user>@domain.tld`, where `domain.tld` is your verified custom domain.

  2. Microsoft redirects the browser to PingOne for authentication.

* Using a Microsoft 365 desktop application, such as Excel for Windows:

  1. The user enters their username.

  2. The desktop application opens a sign-on modal coming from PingOne.

* Using Kerberos authentication:

  * If Kerberos authentication is enabled with the required SPN and browser configuration, the user isn't presented with a sign-on form, and no interaction is required unless your authentication policy uses MFA.

  * If Kerberos authentication isn't enabled, the user is presented with a sign-on form from PingOne and must enter their AD username and password to complete the LDAP authentication process to your AD.

## Hybrid join

Set up PingOne as the federated IdP and Entra Connect Sync to process hybrid join requests using the Kerberos protocol to sync devices from AD to Entra ID.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Device authentication using hybrid join is available as a limited access release for customers with a PingOne for Workforce Plus or Premium license in the North America (US) geography only and isn't covered under standard Support service level agreements (SLAs). You can open support cases for feedback, bug reports, configuration questions, or other inquiries related, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so response times might exceed the usual SLAs for your Support package.Topics for this feature are draft documentation for limited access purposes only and aren't complete or final. |

### Before you begin

Before you begin enabling hybrid join, you must complete the steps in [User authentication](#p1-connect-users-microsoft365) to set up PingOne as the federated IdP for Entra ID.

### Creating attributes and a population for hybrid joined devices

Create an attribute to indicate hybrid joined devices and to store the `objectSid` for the devices and add a population where hybrid joined device records will be created.

#### Steps

1. Add an attribute to indicate hybrid joined devices:

   1. In the PingOne admin console, go to **Directory > User Attributes** and click the **[icon: plus, set=fa]**icon.

   2. Select **Declared** for the attribute type and click **Next**.

   3. Enter or edit the following:

      1. **Name**: A unique identifier for the attribute.

      2. **Display Name** (optional): The name of the attribute as you want it to display in the UI.

      3. **Description** (optional): A brief description of the attribute.

      4. Leave the **Enforce unique values** checkbox cleared.

      5. Verify the **Allow multiple values** checkbox is cleared and **No Validation** is selected in the list.

   4. Click **Save**.

2. Add an attribute to store `objectSid` for hybrid joined devices:

   1. Click the **[icon: plus, set=fa]**icon.

   2. Select **Declared** for attribute type and click **Next**.

   3. Enter or edit the following:

      1. **Name**: A unique identifier for the attribute.

      2. **Display Name** (optional): The name of the attribute as you want it to display in the user interface.

      3. **Description** (optional): A brief description of the attribute.

      4. Leave the **Enforce unique values** checkbox cleared.

      5. Verify the **Allow multiple values** checkbox is cleared and **No Validation** is selected in the list.

   4. Click **Save**.

3. Add a population where hybrid joined device records will be created:

   1. Go to **Directory > Populations** and click the **[icon: plus, set=fa]**icon.

   2. Enter a **Population Name**.

   3. (Optional) Enter a **Description**.

   4. Leave **PingOne** as the **Identity Provider** (default).

   5. Leave the **Default Population** cleared so that this population isn't the default.

   6. Click **Save**.

### Enabling Kerberos authentication

When the hybrid join process begins, the device sends a request security token (RST) message with a Kerberos token directly to PingOne as the federated IdP. The request occurs as part of an STS flow to obtain a security token and without a browser involved. If PingOne as the federated IdP is able to validate the Kerberos token, it creates an assertion and sends it to the device in an RST response (RSTR) message.

To allow PingOne to validate the Kerberos token, you must enable Kerberos authentication in the LDAP gateway for Microsoft 365.

#### Steps

1. In the PingOne admin console, go to **Integrations > Gateways**.

2. Select the LDAP gateway you previously created in [Adding an LDAP gateway to connect PingOne with AD](#p1-add-ldap-gateway).

3. Enable Kerberos authentication for browser SSO so that PingOne can process hybrid join requests from devices:

   1. On the **Connection** tab, click **Edit**.

   2. Select the **Enable Kerberos Authentication** checkbox.

   3. Enter the **Service Account User Principal Name** and **Service Account Password**.

   4. Click **Save**.

   5. [Configure the service account](../integrations/p1_creating_spns.html) with the appropriate `servicePrincipalName` to enable Kerberos authentication.

      Learn more in [SPN reference](../integrations/p1_spn_reference.html).

   6. [Configure end user browsers](../integrations/p1_configuring_end_user_browsers.html) with the required trusted URIs to support Kerberos authentication.

      If you don't want users to authenticate using Kerberos authentication, skip this step. When browsers aren't configured to support Kerberos authentication, users are presented with a sign-on form.

   7. Click **Save**.

### Adding a user type for hybrid joined devices

Add a user type to your LDAP gateway for hybrid joined devices to allow PingOne to store the value from AD and send it to Microsoft 365.

#### Steps

1. In the PingOne admin console, go to **Integrations > Gateways** and select the LDAP gateway you previously created for Microsoft 365.

2. On the **Lookup** tab, click the **[icon: plus, set=fa]**icon.

3. Click **Use default values** to pre-populate fields with values PingOne needs when connecting to your on-premise AD.

4. Configure the following:

   > **Collapse: LDAP gateway configuration**
   >
   > | Setting                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **User Type**                                               | Enter a name for the user type, such as `hybrid joined devices`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | **Select Password Authority**                               | Select **LDAP** in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | **Enable password changes from PingOne**                    | Clear the checkbox to disable this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | **User Search LDAP Base DN**                                | Enter the DN of the OU where devices to be joined to Entra are located. Use a specific DN location where only the devices are located, instead of a broad location that includes both users and devices.#### Example`OU=Computers,DC=pingdemo,DC=ping-eng,DC=com`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   > | **User Link Attributes**                                    | Leave the pre-populated default attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **Enable migration of new users upon first authentication** | Select to enable the checkbox.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | **LDAP Filter**                                             | Enter the following to limit the filter to search for AD device records only:```
   > (&(objectClass=computer)(sAMAccountName=${identifier}))
   > ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | **Population**                                              | Select the population you previously created for hybrid joined devices in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   > | **Update PingOne user attributes as users sign on**         | Clear the checkbox to disable this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | **Map Attributes**                                          | 1. Click the **Delete** icon ([icon: trash, set=fa]) for all attributes except **Username** and **External ID**.
   >
   >    &#xA;&#xA;The default source of External ID is the mS-DS-ConsistencyGuid attribute. If Entra Connect Sync doesn't populate the synced AD device objects with the mS-DS-ConsistencyGuid value, update the source of External ID with another AD attribute that can be used to identify synced devices, such as objectGUID. Make sure to use the same source for Username.
   >
   > 2. For **Username**, use the same attribute used for **External ID**.
   >
   > 3. Map the **Nickname** attribute:
   >
   >    1. Click **[icon: plus, set=fa]Add Mapping**.
   >
   >    2. In the **PingOne User Profile Attribute** list, select **Nickname**.
   >
   >    3. in the **LDAP Attribute** field, enter `sAMAccountName`.
   >
   > 4. Map the `objectSid` attribute:
   >
   >    1. Click **[icon: plus, set=fa]Add Mapping**.
   >
   >    2. In the **PingOne User Profile Attribute** list, select the custom attribute you previously created to store `objectSid` for hybrid joined devices.
   >
   >    3. In the **LDAP Attribute** field, enter `objectSid`.You can find more information about the required attribute mappings in [User type for hybrid joined devices](p1_microsoft_hybrid_join_troubleshooting.html#p1-hybrid-join-user-type). |

5. Click **Save**.

### Updating the Microsoft 365 application

Update the Microsoft 365 application you previously created by:

* Configuring hybrid join support

* Adding the attribute you created for hybrid joined devices

* Enabling Kerberos authentication to allow users to use SSO

#### Steps

1. In the PingOne admin console, go to **Applications > Applications** and select the Microsoft 365 application.

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you didn't already in [Updating the Microsoft 365 application](#p1-update-microsoft-app-user-auth), click **Enable Advanced Configuration** on the **Overview** tab and click **Enable** in the confirmation modal. |

2. On the **Configuration** tab, click [icon: pencil, set=fa]and edit the following:

   1. **Subject NameIdentifier Format**: Either leave the default **`urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`** selected or select **`urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`** in the list.

   2. **STS Token Type**: Select **SAML 1.1 for Office 365** in the list.

   3. **Attribute to indicate Entra hybrid joined devices**: Select the attribute you previously created for hybrid joined devices in the list.

   4. **Show WS-Trust 1.3 Metadata Exchange URL in Powershell cmdlets**: Select to enable the checkbox.

   5. **Enable Kerberos Authentication**:

      1. Select to enable the checkbox.

      2. Click **[icon: plus, set=fa]Add Gateway User Type**.

      3. For **Gateway**, select the LDAP gateway you created for Microsoft 365 in the list.

      4. For **User Type**, select the user type you previously created for cloud users.

         This allows PingOne to process RSTs with Kerberos tokens that desktop applications send for users.

      5. Click **[icon: plus, set=fa]Add Gateway User Type**.

      6. For **Gateway**, select the LDAP gateway you created for Microsoft 365 in the list.

      7. For **User Type**, select the user type you previously created for hybrid joined devices.

         This allows PingOne to process RSTs sent by devices with Kerberos tokens for devices.

   6. Click **Save**.

3. On the **Attribute Mappings** tab, click [icon: pencil, set=fa]and add three new attributes:

   > **Collapse: Microsoft 365 application attributes**
   >
   > | Attribute          | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   > | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | `accounttype`      | 1. Click **[icon: plus, set=fa]Add**.
   >
   > 2. In the **Attributes** field, enter `accounttype`.
   >
   > 3. Click the **More Options** (⋮) icon and click **Update NameFormat**.
   >
   > 4. In the **Update NameFormat** modal, select **http\://schemas.microsoft.com/ws/2012/01** in the **NameFormat** list.
   >
   > 5. Click **Update**.
   >
   > 6. Click the **Gear** icon ([icon: gear, set=fa]) to open the **Advanced Expression** modal.
   >
   > 7. Enter `"DJ"` (including the quotation marks) for domain-joined devices in the **Expression** modal.
   >
   > 8. Click **Save**. |
   > | `onpremobjectguid` | 1) Click **[icon: plus, set=fa]Add**.
   >
   > 2) In the **Attributes** field, enter `onpremobjectguid`.
   >
   > 3) Click the **More Options** (⋮) icon and click **Update NameFormat**.
   >
   > 4) In the **Update NameFormat** modal, select **http\://schemas.microsoft.com/identity/claims** in the **NameFormat** list.
   >
   > 5) Click **Update**.
   >
   > 6) Click **[icon: gear, set=fa]**to open the **Advanced Expression** modal.
   >
   > 7) Enter `#string.uuidAsBase64Guid(user.externalId,null)` in the **Expression** modal.
   >
   > 8) Click **Save**.                        |
   > | `primarysid`       | 1. Click **[icon: plus, set=fa]Add**.
   >
   > 2. In the **Attributes** field, enter `primarysid`.
   >
   > 3. In the **PingOne Mappings** list, select the attribute you previously created in [Creating an attribute in PingOne](#p1-create-attribute) to store `objectSid` for hybrid joined devices.
   >
   > 4. Click the **More Options** (⋮) icon and click **Update NameFormat**.
   >
   > 5. In the **Update NameFormat** modal, select **http\://schemas.microsoft.com/ws/2008/06/identity/claims** in the **NameFormat** list.
   >
   > 6. Click **Update**.              |

   You can find more information about the required attribute mappings in [Attribute mappings for the Microsoft 365 application](p1_microsoft_hybrid_join_troubleshooting.html#p1-microsoft-365-mappings).

4. On the **Edit Attribute Mappings** panel, click **Save**.

### Updating the federated IdP setting

Entra hybrid join uses the WS-Trust 1.3 STS where devices send WS-Trust 1.3-compliant RSTs and expect to receive WS-Trust 1.3-compliant RSTRs. After enabling the **Show WS-Trust 1.3 Metadata Exchange URL in PowerShell cmdlets** setting in the [Microsoft 365 application](#p1-add-microsoft-app), you must re-run the PowerShell cmdlets to update Entra ID to use the new WS-Trust 1.3 metadata exchange URL.

#### Before you begin

If you're using a custom domain for configuring hybrid join, refer to [Custom domains](#p1-hybrid-join-custom-domains) and [Adding a Microsoft 365 application](#p1-add-microsoft-app) (steps 4 and 5) to determine whether you can use your custom domain in the PowerShell cmdlets to update existing federation settings. Hybrid join doesn't support using a custom domain if mTLS is enabled for the domain.

#### Steps

1. In the PingOne admin console, go to **Applications > Applications** and click the Microsoft 365 application.

2. On the **Overview** tab, copy the PowerShell cmdlets to change existing identity federation settings, depending on whether you're using a custom domain and how the domain is configured (steps 4 and 5 in [Adding a Microsoft 365 application](#p1-add-microsoft-app)):

   * If you aren't using a custom domain, if you're using a custom domain with the CloudFront infrastructure, or if you're using a custom domain with the Cloudflare infrastructure with mTLS disabled, copy the default PowerShell cmdlets.

   * If you're using a custom domain with the Cloudflare infrastructure with mTLS enabled, click **Show PingOne Domain** to change the PowerShell cmdlets to use the PingOne domain and copy the cmdlets.

     ![A screen capture of the Microsoft 365 application Overview tab with Show PingOne Domain circled.](_images/p1-entra-hybrid-join-powershell-domain.png)

3. Open PowerShell and select the **Run as Administrator** option.

4. In PowerShell, paste and run the cmdlets.

### Allowing users to join their devices to Entra ID

Enable users to register their own devices with Entra ID as Entra joined devices. Learn more in [Configure device settings](https://learn.microsoft.com/en-us/entra/identity/devices/manage-device-identities#configure-device-settings) in the Entra documentation.

#### Steps

1. In the Entra admin center, go to **Devices > Device settings**.

2. For **Users may join devices to Microsoft Entra**, select **All**.

   ![A screenshot of the Users may join devices to Microsoft Entra setting set to All in the Entra admin center."](_images/p1-entra-hybrid-join-setting.png)

### Configuring Entra Connect Sync and verifying the SCP

Configure Entra Connect Sync and verify the service connection point (SCP) is properly configured to allow devices to be joined to your on-premise AD and Entra ID. A device isn't eligible for hybrid join until Entra Connect Sync syncs the device to Entra ID.

#### Before you begin

Before you can complete the configuration steps in this section, you must [download and install Entra Connect Sync](p1_microsoft_entra_hybrid_join_prerequisites.html).

#### Steps

1. Sign on to the computer on which Entra Connect Sync is installed.

2. Open the Entra Connect Sync application and click **Configure**.

3. In the **Tasks** step, click **Configure device options** and click **Next**.

4. In the **Overview** step, click **Next**.

5. In the **Connect to Microsoft Entra ID** step, enter your administrator credentials for your Entra tenant.

6. In the **Device options** step, select **Configure Hybrid Microsoft Entra join** and click **Next**.

7. In the **Device systems** step, select the **Windows 10 or later domain-joined devices** checkbox and click **Next**.

8. In the **SCP configuration** step:

   1. For **Forest**, select the checkbox for your AD domain.

   2. For **Authentication Service**, select the applicable PingOne domain in the list.

   3. For **Enterprise Admin**, click **Add**.

      #### Result:

      A **Windows Security Enterprise Admin Credentials** sign-on modal opens.

   4. Enter the applicable AD account credentials for an enterprise administrator and click **OK**.

   5. In the **SCP configuration** step, click **Next**.

      ![A screen capture of the Entra Connect Sync SCP configuration step.](_images/p1-entra-hybrid-join-connect-sync-scp-config.png)

9. In the **Federation** step, click **Next**.

10. In the **Configure** step, click **Configure** and click **Exit** when the installation completes.

11. Confirm your Entra tenant and verified custom domain display in AD:

    1. Open **ADSI Edit** and go to **Action > Connect to**.

    2. In the **Connection Settings** modal:

       1. For **Connection Point**, click **Select a well known Naming Context**.

       2. Select **Configuration** in the list.

          ![A screen capture of the ADSI Edit Connection Settings modal with Configuration selected as well known naming context.](_images/p1-entra-hybrid-join-adsi-edit.png)

       3. Click **OK** to close the **Connection Settings** modal.

    3. Go to **Configuration > CN=Configuration > CN=Services > CN=Device Registration Configuration**.

    4. Right-click **CN=62a0ff2e-97b9-4513-943f-0d221bd30080** and click **Properties**.

    5. In the **Properties** modal, locate **keywords** and click **Edit**.

    6. In the **Multi-valued String Editor** modal, verify the following values exist and update them as needed:

       * `azureADId:<tenant ID>`

       * `azureADName:<verified custom domain>`

    7. Click **OK** to close the **Multi-valued String Editor** modal.

    8. Click **Apply** and **OK** to close the **Properties** modal.

    9. Close **ADSI Edit**.

#### Result

Devices joined to the domain found in the specified AD OU are now eligible for hybrid join after the next sync completes. They don't typically display in the Entra admin center on the **All devices** page until after the next sync, but they might appear with a **Registered** status of `Pending` at this point.

### (Optional) Disabling fallback sync in Windows

Recent Windows operating systems come with a fallback sync mechanism if a hybrid join request fails at the federated IdP. Consider disabling fallback sync on the device for which you want to verify the hybrid join process is configured properly. Disabling fallback sync allows PingOne as the federated IdP to handle hybrid join and any other scenarios that use the STS flow.

You can disable or re-enable the **Fallback to Sync-Join** setting by editing the DWORD in the Windows Registry.

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Modifying the registry should be done with caution. Incorrect changes can cause serious operating system problems or corruption and can prevent your system from booting. |

#### Steps

1. On a Windows-based computer to be joined to the cloud, open **Registry Editor**.

2. Go to `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CDJ` and locate the **FallbackToSyncJoin** DWORD, as shown in the following image.

   ![A screen capture of the Windows Registry Editor showing Fallback to Sync Join selected.](_images/p1_microsoft_hybrid_join_fallback_sync.png)

   * If the `CDJ` key doesn't exist in `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion`, create this new key by right-clicking in the `CurrentVersion` folder and clicking **New > Key**.

   * If the **FallbackToSyncJoin** DWORD doesn't exist in the `CDJ` key folder, create this new DWORD by right-clicking in the `CDJ` key folder and clicking **New > DWORD (32-bit) Value**.

3. To disable fallback sync:

   1. Double-click the **FallbackToSyncJoin DWORD**.

   2. Set **Value data** to `0`.

   3. Click **OK**.

      When disabled, the device won't try fallback sync when `dsregcmd /join` fails.

4. To re-enable fallback sync:

   1. Double click the **FallbackToSyncJoin DWORD**.

   2. Set **Value data** to `1`.

   3. Click **OK**.

      The device will try fallback sync when `dsregcmd /join` fails.

You can find additional guidance on disabling the **Fallback to Sync-Join** setting in [Troubleshoot devices using the `dsregcmd` command](https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd#diagnostics-data) in the Entra documentation.

## Validation

You're ready to run the `dsregcmd` command to start the hybrid join process for a device and verify it succeeded. You can find examples of successful and failed responses in [Reference and troubleshooting for Microsoft Entra hybrid join](p1_microsoft_hybrid_join_troubleshooting.html).

1. Sign on to a Windows-based computer.

2. Open PowerShell and select the **Run as Administrator** option.

3. In PowerShell, run `dsregcmd /status` to review the current state.

   ### Result:

   The following is returned:

   ```
   PS C:\Windows\System32> dsregcmd /status

   +----------------------------------------------------------------------+
   | Device State                                                         |
   +----------------------------------------------------------------------+

                AzureAdJoined : NO
             EnterpriseJoined : NO
                 DomainJoined : YES
   ```

   `AzureAdJoined : NO` means the device isn't hybrid joined to Entra ID yet.

   If it's already joined, you can run `dsregcmd /leave` to remove the device from Entra ID, and you shouldn't see this device in **Devices > All devices** in the Entra admin center.

4. Run `dsregcmd /join /debug` to start the hybrid join process.

   ### Example:

   The following is an example response:

   ```
   PS C:\Windows\System32> dsregcmd /join /debug
   DsrCLI: logging initialized.
   ...
   Join request ID: 7d05360e-378f-4e2e-81b1-0289d60b974b
   Join response time: Thu, 10 Jul 2025 17:22:14 GMT
   Join HTTP status: 200
   DsrCmdJoinHelper::Join: AutoEnrollAsComputer completed successfully
   DSREGCMD_END_STATUS
                AzureAdJoined : YES
             EnterpriseJoined : NO
                     DeviceId : 3f0817b9-ca17-4714-ab81-f7b5943dec7b
   ...
                     TenantId : 07ec9af2-7ce5-4ab7-8638-115736bbf990
   ```

   `AzureAdJoined : YES` means the hybrid join attempt succeeded, and the device is now hybrid joined to Entra ID. You should now see the device in **Devices > All devices** in the Entra admin center.

   ### Troubleshooting:

   If `dsregcmd /join` fails to hybrid join the device and it isn't showing in the Entra admin center:

   * If you ran the `dsregcmd /leave` cmdlet to unjoin a device from Entra ID, it can take some time before you can join the device again. Try again in 5 - 15 minutes.

   * Run `dsregcmd /join /debug` again to get additional information for troubleshooting. You can find troubleshooting information in [Reference and troubleshooting for Microsoft Entra hybrid join](p1_microsoft_hybrid_join_troubleshooting.html).

5. Run `dsregcmd /status` again.

   ### Result:

   The following is returned:

   ```
   PS C:\Windows\System32> dsregcmd /status
   ...
   +----------------------------------------------------------------------+
   | SSO State                                                            |
   +----------------------------------------------------------------------+

                   AzureAdPrt : YES
         AzureAdPrtUpdateTime : 2025-07-10 15:46:21.000 UTC
         AzureAdPrtExpiryTime : 2025-07-24 15:46:20.000 UTC
          AzureAdPrtAuthority : https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990
                EnterprisePrt : NO
       EnterprisePrtAuthority :
   ```

   `AzureAdPrt : YES` means the device received a PRT from Entra ID for the signed-on user.

6. Verify an event displays in the PingOne audit log and the device you just joined displays in the population you created for hybrid joined devices:

   1. In the PingOne admin console, go to **Monitoring > Audit** and review the newest events.

      You should see a **Kerberos Check Succeeded** event.

      ![A screen capture of a Kerberos Check Succeeded event type in PingOne.](_images/p1_entra_hybrid_join_audit.png)

   2. Go to **Directory > Users**.

   3. Click the **Filter** icon ([icon: filter, set=fa]) and select the checkbox for the population you created for hybrid joined devices.

      ### Result:

      The **Users** list displays user records in the hybrid joined population. You should see a record for the device you joined. The **Username** will match the **User Identity** in the audit log.

## Troubleshooting

Refer to [Reference and troubleshooting for Microsoft Entra hybrid join](p1_microsoft_hybrid_join_troubleshooting.html) for help troubleshooting issues.

## What's next

1. Repeat the steps in [Validation](#p1-hybrid-join-validation) for each device you want to be hybrid joined to both AD and Entra ID.

2. Implement the hybrid join configuration in your PingOne production environment and roll it out in stages to your users:

   1. Move early adopters to a separate OU and configure Entra Connect Sync to sync devices from the early adopters OU only by running `dsregcmd /join /debug` on those devices. This should prevent configuration issues from impacting all of your users.

   2. If you don't experience issues with the early adopters OU, repeat step 2a with another set of users.

   3. Gradually increase the set of users to cover all applicable users and devices.

---

---
title: Delegation
description: The delegation use case for token exchange allows an application in PingOne to act on behalf of a user.
component: pingone
page_id: pingone:use_cases:p1_oauth_2_token_exchange_delegation
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_delegation.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 25, 2026
section_ids:
  example-scenario: Example scenario
  what-youll-do: What you'll do
  example-tasks: Example tasks
  p1-delegation-dob: Adding DoB as a custom resource
  steps: Steps
  p1-add-goodies: Adding the Goodies Token Exchange application
  steps-2: Steps
  p1-delegation-goodies: Adding Goodies as a custom resource
  steps-3: Steps
  adding-yankee-coffee-as-an-application: Adding Yankee Coffee as an application
  steps-4: Steps
  required-configurations: Required configurations
  p1-delegation-runtime: Runtime process overview
---

# Delegation

Delegation is one of the use cases supported by OAuth 2.0 token exchange in PingOne. Learn more about how it works and the supported use cases in [Configuring OAuth 2.0 token exchange](p1_oauth_2_token_exchange.html).

Use delegation for token exchange to enable an application (client) to act on the user's behalf while maintaining separate identities for the user (*subject*) and the application (*actor*), such as accessing a protected resource.

In general, your organization's PingOne administrator, application, and resource server teams are responsible for collaborating to determine which attributes PingOne should include in the access tokens to represent delegation. The [OAuth 2.0 token exchange specification](https://datatracker.ietf.org/doc/html/rfc8693#section-a.2) provides a delegation token exchange example.

In delegation, the application has two tokens:

* A subject token represents the authenticated user and is obtained with the user's authorization.

* An actor token represents the identity acting on behalf of the user and is obtained for the application itself or a user it represents. The actor token is required only for delegation flows.

The application exchanges both tokens for a new token to access the protected resource. The `act` (actor) claim in the new token informs the resource server that the application using the token isn't the actual user but is acting on the user's behalf.

## Example scenario

In this scenario, users order coffee using an application, Yankee Coffee, and apply their reward points to redeem free coffee. To complete an order:

1. The application, Yankee Coffee, must retrieve the reward points balance of the user from a resource server, Goodies.

2. Goodies must verify whether the user's birthday bonus reward has been claimed, but Goodies doesn't have this information and must retrieve it from another resource server, DoB.

3. Yankee Coffee must include the identity (actor) that can act on behalf of the user to Goodies so that Goodies can include the delegation information when it requests the birthday bonus reward from DoB.

## What you'll do

To set up the example scenario for delegation, you'll add:

* Yankee Coffee application: The user interacts with this application to initiate the flow.

* Goodies custom resource: This resource has the information needed by the Yankee Coffee application.

* Goodies Token Exchange application: This application processes the token exchange request.

* DoB custom resource: This resource has the additional information the Yankee Coffee application can act on behalf of the user to retrieve.

## Example tasks

### Adding DoB as a custom resource

As a PingOne administrator, add a custom resource in PingOne for the DoB resource server.

#### Steps

1. In the PingOne admin console, go to **Applications > Resources** and click the [icon: plus, set=fa]icon.

2. In the **Create Resource Profile** step:

   1. For **Resource Name**, enter `DoB`.

   2. For **Audience**, enter the audience for resource in the format of `https://api.example.com/d`.

   3. (Optional) For **Description**, enter a brief description of the resource.

   4. For **Access token time to live**, leave the default or optionally edit the maximum time that the access token will be valid for use in the application, in seconds.

   5. Click **Next**.

3. In the **Attributes** step:

   1. Click the **Gear** icon ([icon: gear, set=fa]) next to the **`sub`** attribute to open the **Advanced Expressions** modal.

   2. In the modal, enter the following and click **Save**:

      ```json
      #root.context.requestData.subjectToken.sub
      ```

      This expression populates the `sub` claim value in the issued token with the `sub` claim value from the subject token.

   3. Click **[icon: plus, set=fa]Add** to add another attribute.

   4. In the **Attribute** field, enter `act` and then click [icon: gear, set=fa]next to the attribute to open the **Advanced Expressions** modal.

   5. In the modal, enter the following and click **Save**:

      ```json
      (#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?#root.context.requestData.subjectToken.may_act:null)
      ```

   6. Select the checkbox to make the `act` attribute required.

      This expression checks whether the token request uses the client credentials grant type.

      * If the token request uses the client credentials grant type, it populates `act` with a hard-coded value of `noActor` to signal to DoB that no delegation is involved.

      * If the token request doesn't use the client credentials grant type, it assumes the token request uses the token exchange grant type and checks whether the `may_act` claim value in the subject token matches the `client_id` in the actor token.

        * If the value matches, it populates `act` with the `may_act` claim value from the subject token.

        * If the value doesn't match, it sets `act` as `null`, and the token exchange token request fails because the `act` claim is marked as required.

   7. Click **Next**.

4. In the **Scopes** step:

   1. Click **[icon: plus, set=fa]Add Scope**.

   2. For **Scope Name**, enter a name, such as `d.read`.

   3. (Optional) Enter a **Description** for the scope.

   4. Click **Save**.

### Adding the Goodies Token Exchange application

Create an application to handle the token exchange requests and obtain access tokens from PingOne to send API requests to DoB. The Goodies Token Exchange application must use:

* The token exchange grant type to obtain access tokens from PingOne to send API requests to DoB to retrieve birthday reward information

* The application credentials in its token request because only applications can send token requests to PingOne, and custom resources can't.

The resulting access token contains:

* The identity of the actor acting on behalf of the user as the subject (`sub`). The subject is taken taken directly from the subject of the access token from Yankee Coffee.

* An `act` claim indicating the identity acting on behalf of the user. In this scenario, the identity is the Goodies Token Exchange application.

#### Steps

1. Go to **Applications > Applications** and click the [icon: plus, set=fa]icon.

2. In the **Add Application** panel:

   1. For **Application Name**, enter `Goodies Token Exchange`.

   2. (Optional) Enter a **Description** for the application.

   3. Select an OIDC-based application type and click **Save**.

3. On the **Configuration** tab:

   1. Click the **Pencil** icon ([icon: pencil, set=fa]).

   2. For **Grant Type**, select **Client Credentials** and **Token Exchange**.

   3. Leave all other default settings.

   4. Click **Save**.

4. On the **Resources** tab:

   1. Click [icon: pencil, set=fa].

   2. Assign the resource you created in [Adding DoB as a custom resource](#p1-delegation-dob).

   3. Click **Save**.

5. On the **Overview** tab, click the **Copy to clipboard** icon ([icon: copy, set=fa]) for **Client ID**. You'll need the client ID to configure the subject for the `may_act` attribute in the Goodies custom resource.

### Adding Goodies as a custom resource

Add a custom resource in PingOne for the Goodies resource server.

#### Steps

1. Go to **Applications > Resources** and click the [icon: plus, set=fa]icon.

2. In the **Create Resource Profile** step:

   1. For **Resource Name**, enter `Goodies`.

   2. For **Audience**. enter the audience for resource in the format of `https://api.example.com/g`.

   3. (Optional) For **Description**, enter a brief description of the resource.

   4. For **Access token time to live**, leave the default or optionally edit the maximum time that the access token will be valid for use in the application, in seconds.

   5. Click **Next**.

3. In the **Attributes** step:

   1. Leave **`sub`** mapped to **User ID** (default).

   2. Click **[icon: plus, set=fa]Add**.

   3. For **Attribute**, enter `may_act` and then click [icon: gear, set=fa]next to the attribute to open the **Advanced Expressions** modal.

   4. In the modal, enter the following, using the client ID that you copied in step 6 of [Adding the Goodies Token Exchange application](#p1-add-goodies):

      ```
      {"sub": "<client ID of the Goodies Token Exchange application>"}
      ```

   5. Click **Save**.

   6. Click **Next**.

4. In the **Scopes** step:

   1. Click **[icon: plus, set=fa]Add Scope**.

   2. For **Scope Name**, enter a name, such as `g.crud`.

   3. (Optional) Enter a **Description** for the scope.

   4. Click **Save**.

### Adding Yankee Coffee as an application

Add an end-user application in PingOne for Yankee Coffee and and assign the scope from the Goodies custom resource. Yankee Coffee must use the authorization code grant type to obtain access tokens from PingOne to send API requests to the Goodies custom resource to retrieve the user's reward points balance. The access tokens contain:

* The identity that can act on behalf of the user as the subject (`sub`). The subject is the user who authenticates and authorizes the application request from Yankee Coffee.

* A `may_act` claim indicating the identity that can act on behalf of the user. In this scenario, the identity is the Goodies Token Exchange application.

#### Steps

1. Go to **Applications > Applications** and click the [icon: plus, set=fa]icon.

2. In the **Add Application** panel:

   1. For **Application Name**, enter `Yankee Coffee`.

   2. (Optional) Enter a **Description** for the application.

   3. Select an OIDC-based application type and click **Save**.

3. On the **Configuration** tab:

   1. Click [icon: pencil, set=fa].

   2. For **Grant Type**, select **Authorization Code**.

   3. Leave all other default settings.

   4. Click **Save**.

4. On the **Resources** tab:

   1. Click [icon: pencil, set=fa].

   2. Assign the resource you created in [Adding Goodies as a custom resource](#p1-delegation-goodies).

   3. Click **Save**.

5. Provide the application credentials and custom resource credentials to your organization's developers for the applications and custom resources, respectively.

## Required configurations

The following table lists the required configurations for the applications and custom resources and includes example client IDs that correspond to the [runtime process overview](#p1-delegation-runtime):

| Applications                                                                                                                                              | Custom resources                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yankee Coffee- Client ID: f6c78a5b

- Grant type: Authorization code

- Scopes:

  * **openid** (default)

  * `g.crud`                                   | Goodies- Client ID: 75d8cea3

- Audience: https\://api.example.com/g

- Scopes: `g.crud`

- Attributes:

  * `sub`: **User ID** (default)

  * `may act`: `{"sub": "45f60a71"}`                                                                                                                                                                                                                                 |
| Goodies Token Exchange- Client ID: 45f60a71

- Grant type:

  * Client credentials

  * Token exchange

- Scopes:

  * **openid** (default)

  * `d.read` | DoB- Client ID: 81ca41a2

- Audience: https\://api.example.com/d

- Scopes: `d.read`

- Attributes:

  * `sub`: `#root.context.requestData.subjectToken.sub`

  * `act`: `(#root.context.requestData.grantType == "client_credentials")?"noActor":((#root.context.requestData.subjectToken.may_act.sub == #root.context.requestData.actorToken.client_id)?#root.context.requestData.subjectToken.may_act:null)` |

## Runtime process overview

The following diagram shows a high-level overview of the example delegation flow:

![A diagram of the example delegation token exchange flow.](_images/p1-token-exchange-delegation-diagram.png)

1. Yankee Coffee sends an authorization request to PingOne with `scope=openid+g.crud`, `client_id=f6c78a5b`, and other parameters.

2. PingOne authenticates the user, obtains the authorization from the user, and returns an authorization code to Yankee Coffee.

3. Yankee Coffee sends a token request using the authorization code grant type to PingOne.

4. PingOne returns an access token to Yankee Coffee.

   The payload is decoded as follows:

   ```json
   {
     "client_id": "f6c78a5b-9d39-4cd7-b94e-81dad33c8773", # the client ID of Yankee Coffee
     "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
     "jti": "54ffa426-1410-4383-8ec5-344a7b1b948e",
     "iat": 1770574186,
     "exp": 1770577786,
     "aud": [
       "https://api.example.com/g" # the audience is Goodies
     ],
     "scope": "g.crud", # the scope of this access token
     "sub": "user@example.net", # the user using Yankee Coffee
     "sid": "86635114-c633-4c13-b1eb-4a8a3f0e7dcd",
     "auth_time": 1770573761,
     "acr": "1Single_Factor",
     "may_act": {                                    # the identity that can act on behalf of the user
       "sub": "45f60a71-df8c-42d6-9410-f64f0454874d" # the client ID of Goodies Token Exchange App
     },
     "env": "6991589d-87eb-47f4-9131-284cebe106b3",
     "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
     "p1.userId": "8ca2b15a-e3bd-43a5-bee1-1e533bae759d"
   }
   ```

5. Yankee Coffee sends an API request to Goodies. For authorization, Yankee Coffee includes the access token (from step 4) as the `Authorization` HTTP request header value in the API request.

6. Goodies evaluates the access token and determines that:

   * The issuer of the access token is PingOne.

   * The application requesting the token is Yankee Coffee.

   * The audience of the access token includes itself, Goodies.

7. Goodies sends an introspection request to PingOne to validate the access token.

   For client identification and authentication, Goodies uses the client ID and secret defined in PingOne for the custom resource (`client_id=75d8cea3`).

8. Goodies sends a token request using the client credentials grant type to PingOne.

   For client identification and authentication, Goodies uses the client ID and secret defined in PingOne for the Goodies Token Exchange application (`client_id=45f60a71`).

9. PingOne returns an access token to Goodies.

   The payload is decoded as follows:

   ```json
   {
     "client_id": "45f60a71-df8c-42d6-9410-f64f0454874d", # the client ID of Goodies Token Exchange App
     "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
     "jti": "47d54766-7b9a-4485-96d9-6c09d410b943",
     "iat": 1770574217,
     "exp": 1770577817,
     "aud": [
       "https://api.example.com/d" # the audience is DoB
     ],
     "scope": "d.read",
     "act": "noActor", # a value of `noActor' indicates (to DoB) that no delegation is involved
     "env": "6991589d-87eb-47f4-9131-284cebe106b3",
     "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
     "p1.rid": "47d54766-7b9a-4485-96d9-6c09d410b943"
   }
   ```

10. Goodies sends a token request using the token exchange grant type to PingOne.

    * For client identification and authentication, Goodies uses the client ID and secret defined in PingOne for the Goodies Token Exchange application (`client_id=45f60a71`).

    * Goodies includes the following parameters in the token request:

      * `scope=d.read`

      * `subject_token=<access token from step 5>`

      * `subject_token_type=urn:ietf:params:oauth:token-type:access_token`

      * `actor_token=<access token from step 9>`

      * `actor_token_type=urn:ietf:params:oauth:token-type:access_token`

      * `requested_token_type=urn:ietf:params:oauth:token-type:access_token`

11. PingOne validates the subject token for the following:

    * The subject token and the actor token are valid JWTs.

    * The issuer of the subject token and the actor token matches the issuer of the current PingOne environment.

    * The associated PingOne user session is valid.

12. PingOne mints an access token based on the attribute mappings defined in PingOne for DoB.

13. PingOne returns a token response containing an access token to Goodies.

    The following is the token response:

    ```json
    {
        "access_token": "eyJ…", # the access token as a result of the token exchange token request
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": "d.read",
        "issued_token_type": "urn:ietf:params:oauth:token-type:access_token"
    }
    ```

    The access token is decoded as follows:

    ```json
    {
      "client_id": "45f60a71-df8c-42d6-9410-f64f0454874d", # the client ID of Goodies Token Exchange App
      "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
      "jti": "337a5736-bea4-44dd-9692-dc5f696ef710",
      "iat": 1770574249,
      "exp": 1770577849,
      "aud": [
        "https://api.example.com/d" # the audience is DoB
      ],
      "scope": "d.read",
      "sub": "user@example.net", # the user using Yankee Coffee
      "sid": "86635114-c633-4c13-b1eb-4a8a3f0e7dcd",
      "auth_time": 1770573761,
      "acr": "1Single_Factor",
      "act": {                                        # the identity acting on behalf of the user
        "sub": "45f60a71-df8c-42d6-9410-f64f0454874d" # the client ID of Goodies Token Exchange App
      },
      "env": "6991589d-87eb-47f4-9131-284cebe106b3",
      "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
      "p1.userId": "8ca2b15a-e3bd-43a5-bee1-1e533bae759d"
    }
    ```

14. Goodies sends an API request to DoB. For authorization, Goodies includes the access token (from step 13) as the `Authorization` HTTP request header value in the API request.

15. DoB evaluates the access token and determines that:

    * The issuer of the access token is PingOne.

    * The application requesting the token is the Goodies Token Exchange application.

    * The audience of the access token includes itself, DoB.

16. DoB sends an introspection request to PingOne to validate the access token.

17. DoB returns an API response to Goodies. At this point, Goodies as a resource server can fulfill the API request from Yankee Coffee (in step 5).

18. Goodies returns an API response to Yankee Coffee.

---

---
title: Impersonation
description: The impersonation use case for token exchange allows an application in PingOne to act as a user.
component: pingone
page_id: pingone:use_cases:p1_oauth_2_token_exchange_impersonation
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_impersonation.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 25, 2026
section_ids:
  example-scenario: Example scenario
  what-youll-do: What you'll do
  example-tasks: Example tasks
  p1-impersonation-address: Adding the Address custom resource
  steps: Steps
  adding-xl-delivery-as-an-application: Adding XL Delivery as an application
  steps-2: Steps
  p1-impersonation-buzzer: Adding Buzzer as a custom resource
  steps-3: Steps
  adding-the-address-token-exchange-application: Adding the Address Token Exchange application
  steps-4: Steps
  required-configurations: Required configurations
  p1-impersonation-runtime: Runtime process overview
---

# Impersonation

Impersonation is one of the use cases supported by OAuth 2.0 token exchange in PingOne. Learn more about how it works and the supported use cases in [Configuring OAuth 2.0 token exchange](p1_oauth_2_token_exchange.html).

Use impersonation for token exchange to enable an application (client) to perform a job or duty without maintaining separation between the user and the application. The application obtains a subject token representing the user who authenticates and authorizes the request, and exchanges it for a new token to access a custom resource. The custom resource handles the request as if it came from the user.

## Example scenario

In this scenario:

1. Users ship packages using a shipping company, XL Delivery.

2. To successfully ship packages, XL Delivery must retrieve user shipping information from a resource server, Address.

3. The Address resource server must then retrieve the user's apartment buzzer number from another resource server, Buzzer, by impersonating the user.

## What you'll do

To set up the example scenario for impersonation, you'll add:

* XL Delivery application: The user interacts with this application to initiate the flow.

* Address custom resource: This resource has the information needed by the XL Delivery application.

* Address Token Exchange application: This application processes the token exchange request.

* Buzzer custom resource: This resource has the additional information the XL Delivery application will impersonate the user to retrieve.

## Example tasks

### Adding the Address custom resource

As a PingOne administrator, create a custom resource in PingOne for the Address resource server.

#### Steps

1. In the PingOne admin console, go to **Applications > Resources** and click the **[icon: plus, set=fa]**icon.

2. In the **Create Resource Profile** step:

   1. For **Resource Name**, enter `Address`.

   2. For **Audience**, enter the audience for the resource in the format `https://api.example.com/a`.

   3. (Optional) For **Description**, enter a brief description of the resource.

   4. For **Access token time to live**, leave the default or optionally edit the maximum time that the access token will be valid for use in the application, in seconds.

   5. Click **Next**.

3. In the **Attributes** step, leave the default mapping of **`sub`** to **User ID** and click **Next**.

4. In the **Scopes** step:

   1. Click **[icon: plus, set=fa]Add Scope**.

   2. For **Scope Name**, enter a name, such as `a.crud`.

   3. (Optional) Enter a **Description** for the scope.

   4. Click **Save**.

### Adding XL Delivery as an application

Configure an application in PingOne for the end-user application, XL Delivery, and assign the required scope from the Address custom resource. In this flow, the XL Delivery application uses the authorization code grant type to obtain access tokens from PingOne. The resulting access tokens contain a subject (`sub`), representing the user who authenticated and authorized the request to retrieve shipping information from Address.

#### Steps

1. Go to **Applications > Applications** and click the [icon: plus, set=fa]icon.

2. In the **Add Application** panel:

   1. For **Application Name**, enter `XL Delivery`.

   2. (Optional) Enter a **Description** for the application.

   3. Select an OIDC-based application type and click **Save**.

3. On the **Configuration** tab:

   1. Click the **Pencil** icon ([icon: pencil, set=fa]).

   2. For **Grant Type**, select **Authorization Code**.

   3. Leave all other default settings.

   4. Click **Save**.

4. On the **Resources** tab:

   1. Click [icon: pencil, set=fa].

   2. Assign the resource you created in [Adding the Address custom resource](#p1-impersonation-address).

   3. Click **Save**.

      ![A screenshot of assigning the Address custom resource to the XL Delivery application.](_images/p1-token-exchange-address-scope.png)

### Adding Buzzer as a custom resource

Add a custom resource in PingOne for the Buzzer resource server.

#### Steps

1. Go to **Applications > Resources** and click the [icon: plus, set=fa]icon.

2. In the **Create Resource Profile** step:

   1. For **Resource Name**, enter `Buzzer`.

   2. For **Audience**, enter the audience for resource in the format `https://api.example.com/b`.

   3. (Optional) For **Description**, enter a brief description of the resource.

   4. For **Access token time to live**, leave the default or optionally edit the maximum time that the access token will be valid for use in the application, in seconds.

   5. Click **Next**.

3. In the **Attributes** step:

   1. Click the **Gear** icon ([icon: gear, set=fa]) next to the **`sub`** attribute to open the **Advanced Expressions** modal.

   2. In the modal, enter `#root.context.requestData.subjectToken.sub` and click **Save**.

   3. Click **Next**.

4. In the **Scopes** step:

   1. Click **[icon: plus, set=fa]Add Scope**.

   2. For **Scope Name**, enter a name, such as `b.read`.

   3. (Optional) Enter a description for the scope.

   4. Click **Save**.

### Adding the Address Token Exchange application

Create an application to handle the token exchange requests and obtain access tokens from PingOne to send API requests to Buzzer. The Address Token Exchange application must use:

* The token exchange grant type to obtain access tokens from PingOne to send API requests to Buzzer.

* The application credentials in its token request because only applications can send token requests to PingOne, and custom resources can't.

The access tokens contain a subject (`sub`) taken directly from the subject of the access token from the XL Delivery application.

#### Steps

1. Go to **Applications > Applications** and click the [icon: plus, set=fa]icon.

2. In the **Add Application** panel:

   1. For **Application Name**, enter `Address Token Exchange`.

   2. (Optional) Enter a **Description** for the application.

   3. Select an OIDC-based application type.

   4. Click **Save**.

3. On the **Configuration** tab:

   1. Click [icon: pencil, set=fa].

   2. For **Grant Type**, select **Token Exchange**.

   3. Leave all other default settings.

   4. Click **Save**.

4. On the **Resources** tab:

   1. Click [icon: pencil, set=fa].

   2. Assign the resource you created in [Adding Buzzer as a custom resource](#p1-impersonation-buzzer).

   3. Click **Save**.

5. Provide the application credentials and custom resource credentials to your organization's developers for the applications and custom resources, respectively.

## Required configurations

The following table lists the required configurations for the applications and custom resources and includes example client IDs that correspond to the [runtime process overview](#p1-impersonation-runtime):

| Applications                                                                                                                 | Custom resources                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| XL Delivery- Client ID: a85f7a70

- Grant type: Authorization code

- Scopes:

  * **openid** (default)

  * `a.crud`        | Address- Client ID: 44278071

- Audience: https\://api.example.com/a

- Scopes: `a.crud`

- Attribute: `sub`: **User ID** (default)                        |
| Address Token Exchange- Client ID: e8f90620

- Grant type: Token exchange

- Scopes:

  * **openid** (default)

  * `b.read` | Buzzer- Client ID: b0bc42b0

- Audience: https\://api.example.com/b

- Scopes: `b.read`

- Attributes: `sub`: `#root.context.requestData.subjectToken.sub` |

## Runtime process overview

The following diagram shows a high-level overview of the example impersonation flow:

![A diagram of the example impersonation token exchange flow.](_images/p1-token-exchange-impersonation-diagram.png)

1. XL Delivery sends an authorization request to PingOne with `scope=openid+a.crud`, `client_id=a85f7a70`, and other parameters.

2. PingOne authenticates the user, obtains the authorization from the user, and returns an authorization code to XL Delivery.

3. XL Delivery sends a token request to PingOne using the authorization code grant type.

4. PingOne returns an access token to XL Delivery.

   The payload is decoded as follows:

   ```json
   {
     "client_id": "a85f7a70-c9ae-46cc-99cb-ff78a4ce486e", # the client ID of XL Delivery
     "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
     "jti": "ea50083a-a3d2-4c4a-978b-1175d83c59fd",
     "iat": 1770155043,
     "exp": 1770158643,
     "aud": [
       "https://api.example.com/a" # the audience is Address
     ],
     "scope": "a.crud", # the scope of this access token
     "sub": "8ca2b15a-e3bd-43a5-bee1-1e533bae759d", # the id of the user using XL Delivery
     "sid": "2fc3e42c-f074-4efe-9bc7-ad91627be19b",
     "auth_time": 1770155030,
     "acr": "1Single_Factor",
     "env": "6991589d-87eb-47f4-9131-284cebe106b3",
     "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c"
   }
   ```

5. XL Delivery sends an API request to Address. For authorization, XL Delivery includes the access token (from step 4) as the `Authorization` HTTP request header value in the API request.

6. Address evaluates the access token and determines that:

   * The issuer of the access token is PingOne.

   * The application requesting the token is XL Delivery.

   * The audience of the access token includes itself, Address.

7. Address sends an introspection request to PingOne to validate the access token.

   For client identification and authentication, Address uses the client ID and secret defined in PingOne for the custom resource (`client_id=44278071`).

8. Address sends a token request to PingOne using the token exchange grant type.

   * For client identification and authentication, Address must use the client ID and secret defined in PingOne for the Address Token Exchange application (`client_id=e8f90620`)).

   * Address includes the following parameters in the token request:

     * `grant_type=urn:ietf:params:oauth:grant-type:token-exchange`

     * `scope=b.read`

     * `subject_token=<access token from step 5>`

     * `subject_token_type=urn:ietf:params:oauth:token-type:access_token`

     * `requested_token_type=urn:ietf:params:oauth:token-type:access_token`

9. PingOne validates the subject token for the following:

   * The subject token is a valid JWT.

   * The issuer of the subject token matches the issuer of the current PingOne environment.

   * The associated PingOne user session is valid.

10. PingOne mints an access token based on the attribute mappings defined in PingOne for Buzzer.

11. PingOne returns a token response containing an access token to Address.

    The following is the token response:

    ```json
    {
        "access_token": "eyJ…", # the access token as a result of the token exchange token request
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": "b.read",
        "issued_token_type": "urn:ietf:params:oauth:token-type:access_token"
    }
    ```

    The access token is decoded as follows:

    ```json
    {
      "client_id": "e8f90620-43e7-4d56-af96-fb0efb77076f", # the client_id of Address Token Exchange App
      "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
      "jti": "b6c4af53-4396-452d-a3da-88008846cf76",
      "iat": 1770155325,
      "exp": 1770158925,
      "aud": [
        "https://api.example.com/b" # the audience is Buzzer
      ],
      "scope": "b.read", # the scope of this access token
      "sub": "8ca2b15a-e3bd-43a5-bee1-1e533bae759d", # the id of the user using XL Delivery
      "sid": "2fc3e42c-f074-4efe-9bc7-ad91627be19b",
      "auth_time": 1770155030,
      "acr": "1Single_Factor",
      "env": "6991589d-87eb-47f4-9131-284cebe106b3",
      "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
      "p1.userId": "8ca2b15a-e3bd-43a5-bee1-1e533bae759d"
    }
    ```

12. Address sends an API request to Buzzer. For authorization, Address includes the access token (from step 11) as the `Authorization` HTTP request header value in the API request.

13. Buzzer evaluates the access token and determines that:

    * The issuer of the access token is PingOne.

    * The application requesting the token is Address Token Exchange.

    * The audience of the access token includes itself, Buzzer.

14. Buzzer sends an introspection request to PingOne to validate the access token.

15. Buzzer returns an API response to Address. At this point, Address as a resource server can fulfill the API request from XL Delivery (in step 5).

16. Address as a resource server returns an API response to XL Delivery.

---

---
title: Machine-to-machine interaction
description: The machine-to-machine use case for token exchange enables server-to-server communication without user involvement.
component: pingone
page_id: pingone:use_cases:p1_oauth_2_token_exchange_machine_to_machine
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_oauth_2_token_exchange_machine_to_machine.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 25, 2026
section_ids:
  example-scenario: Example scenario
  what-youll-do: What you'll do
  example-tasks: Example tasks
  p1-m2m-eflyers: Adding e-Flyers as a custom resource
  steps: Steps
  adding-zillion-deals-as-an-application: Adding Zillion Deals as an application
  steps-2: Steps
  p1-m2m-zing: Adding Zing as a custom resource
  steps-3: Steps
  adding-the-e-flyers-token-exchange-application: Adding the e-Flyers Token Exchange application
  steps-4: Steps
  required-configurations: Required configurations
  p1-m2m-runtime: Runtime process overview
---

# Machine-to-machine interaction

Machine-to-machine interaction is one of the use cases supported by OAuth 2.0 token exchange in PingOne. Learn more about how it works and the supported use cases in [Configuring OAuth 2.0 token exchange](p1_oauth_2_token_exchange.html).

Use machine-to-machine token exchange for server-to-server communication without user interaction. In this use case, the application initiating the flow first uses the client credentials grant type to obtain the initial access token from PingOne to access protected data on a resource server.

In ecosystems with multiple resource servers, allowing services unrestricted API access can risk unintended usage and complex dependencies. To further enhance security and maintain least-privilege boundaries, that resource server then uses the token exchange grant type to obtain a new token scoped to each downstream service. This prevents downstream services from accessing the original caller's token.

## Example scenario

A backend system, Zillion Deals, generates the top 10 deals of the week for an online retail store. To complete this task:

1. Zillion Deals needs to retrieve flyers from across the country from a resource server, e-Flyers.

2. e-Flyers must retrieve the best deals from another resource server, Zing.

3. Zillion Deals only communicates with e-Flyers, not directly with Zing. This prevents Zing as the downstream service from accessing Zillion Deals' original token.

## What you'll do

To set up the example scenario for machine-to-machine interaction, you'll add:

* Zillion Deals application: This backend application initiates the flow.

* e-Flyers custom resource: This resource has the information needed by the Zillion Deals application.

* e-Flyers Token Exchange application: This application processes the token exchange request.

* Zing custom resource: This resource has additional information the Zillion Deals application retrieves data from without user interaction.

## Example tasks

### Adding e-Flyers as a custom resource

As a PingOne administrator, add a custom resource in PingOne for the e-Flyers resource server.

#### Steps

1. In the PingOne admin console, go to **Applications > Resources** and click the [icon: plus, set=fa]icon.

2. In the **Create Resource Profile** step:

   1. For **Resource Name**, enter `e-Flyers`.

   2. For **Audience**, enter the audience for the resource in the format of `https://api.example.com/e`.

   3. (Optional) For **Description**, enter a brief description of the resource.

   4. For **Access token time to live**, leave the default or optionally edit the maximum time that the access token will be valid for use in the application, in seconds.

   5. Click **Next**.

3. In the **Attributes** step:

   1. Leave the default mapping of **`sub`** to **User ID**.

      |   |                                                                                                                                                                                                                                                                                               |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Even if you map the `sub` claim to a user attribute, such as **User ID**, the resulting access token won't contain the `sub` claim. This occurs because machine-to-machine interactions have no end users involved because this initial token request uses the client credentials grant type. |

   2. Click **[icon: plus, set=fa]Add**.

   3. Enter an **Attribute** representing the flyers, such as `e.attr` and then click the **Gear** icon ([icon: gear, set=fa]) next to the attribute to open the **Advanced Expressions** modal.

   4. In the modal, enter an expression to map the flyers to the attribute, such as `'Eee'`, and click **Save**.

      The `e.attr` attribute is an example sample attribute used for demonstration purposes only and isn't a required attribute. The resulting access token (step 2 in [Runtime process overview](#p1-m2m-runtime)) will contain the `e.attr` claim, where the value is always `Eee`.

   5. Click **Next**.

4. In the **Scopes** step:

   1. Click **[icon: plus, set=fa]Add Scope**.

   2. For **Scope Name**, enter a name, such as `e.crud`.

   3. (Optional) Enter a **Description** for the scope.

   4. Click **Save**.

### Adding Zillion Deals as an application

Add an application in PingOne for Zillion Deals and assign the scope from the e-Flyers custom resource. Zillion Deals must use the client credentials grant type to obtain access tokens from PingOne to send API requests to e-Flyers to retrieve flyers from across the country.

When minting these access tokens, PingOne populates the attribute claim with the mapped value you provide (`e.attr` = `Eee` in this example) and doesn't include the `sub` claim because no user is involved (**User ID** is null).

#### Steps

1. Go to **Applications > Applications** and click the [icon: plus, set=fa]icon.

2. In the **Add Application** panel:

   1. For **Application Name**, enter `Zillion Deals`.

   2. (Optional) Enter a **Description** for the application.

   3. Select an OIDC-based application type and click **Save**.

3. On the **Configuration** tab:

   1. Click the **Pencil** icon ([icon: pencil, set=fa]).

   2. For **Grant Type**, select **Client Credentials**.

      The client credentials grant type is used for machine-to-machine interactions.

   3. Leave all other default settings.

   4. Click **Save**.

4. On the **Resources** tab:

   1. Click [icon: pencil, set=fa].

   2. Assign the resource you created in [Adding e-Flyers as a custom resource](#p1-m2m-eflyers).

   3. Click **Save**.

### Adding Zing as a custom resource

Add a custom resource in PingOne for the Zing resource server.

#### Steps

1. Go to **Applications > Resources** and click the [icon: plus, set=fa]icon.

2. In the **Create Resource Profile** step:

   1. For **Resource Name**, enter `Zing`.

   2. For **Audience**, enter the audience for the resource in the format of `https://api.example.com/z`.

   3. (Optional) For **Description**, enter a brief description of the resource.

   4. For **Access token time to live**, leave the default or optionally edit the maximum time that the access token will be valid for use in the application, in seconds.

   5. Click **Next**.

3. In the **Attributes** step:

   1. Leave the default mapping of **`sub`** to **User ID**.

      |   |                                                                                                                                                                                                                                                                   |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Although you can map the `sub` claim to a user attribute, such as **User ID**, the resulting access token won't contain the `sub` claim. This occurs because machine-to-machine interactions use the client credentials grant type, which doesn't involve a user. |

   2. Click **[icon: plus, set=fa]Add** to add another attribute.

   3. Enter an **Attribute** representing the deals, such as `z.attr` and click [icon: gear, set=fa]next to the attribute to open the **Advanced Expressions** modal.

   4. In the modal, enter an expression to map the deals to the attribute, such as `'Zee'`, and click **Save**.

      The `z.attr` attribute is an example sample attribute used for demonstration purposes only and isn't a required attribute. The resulting access token (step 9 in [Runtime process overview](#p1-m2m-runtime)) will contain the `z.attr` claim, where the value is always `Zee`.

   5. Click **Next**.

4. In the **Scopes** step:

   1. Click **[icon: plus, set=fa]Add Scope**.

   2. For **Scope Name**, enter a name, such as `z.read`.

   3. (Optional) Enter a **Description** for the scope.

   4. Click **Save**.

### Adding the e-Flyers Token Exchange application

Create an application to handle token exchange requests and obtain access tokens from PingOne to send API requests to Zing. The e-Flyers Token Exchange application must use:

* The token exchange grant type to ensure e-Flyers can request a token for Zing only when it presents a valid token from Zillion Deals. This maintains the authorization chain and improves audit traceability that the client credentials grant type can't provide.

* The application credentials in its token request because only applications can send token requests to PingOne, and custom resources can't.

When minting these access tokens, PingOne populates the attribute claim with the value you provide (`z.attr` = `Zee`) and doesn't include the `sub` claim because no user is involved (**User ID** is null).

#### Steps

1. Go to **Applications > Applications** and click the [icon: plus, set=fa]icon.

2. In the **Add Application** panel:

   1. For **Application Name**, enter `e-Flyers Token Exchange`.

   2. (Optional) Enter a **Description** for the application.

   3. Select an OIDC-based application type and click **Save**.

3. On the **Configuration** tab:

   1. Click [icon: pencil, set=fa].

   2. For **Grant Type**, select **Token Exchange**.

   3. Leave all other default settings.

   4. Click **Save**.

4. On the **Resources** tab:

   1. Click [icon: pencil, set=fa].

   2. Assign the resource you created in [Adding Zing as a custom resource](#p1-m2m-zing).

   3. Click **Save**.

5. Provide the application credentials and custom resource credentials to your organization's developers for the applications and custom resources, respectively.

## Required configurations

The following table lists the required configurations for the applications and custom resources and includes example client IDs that correspond to the [runtime process overview](#p1-m2m-runtime):

| Applications                                                                                                                  | Custom resources                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zillion Deals- Client ID: 4076de38

- Grant type: Client credentials

- Scopes:

  * **openid** (default)

  * `e.crud`       | e-Flyers- Client ID: bc82af8d

- Audience: https\://api.example.com/e

- Scopes: `e.crud`

- Attributes:

  * `sub`: **User ID** (default)

  * `e.attr`: `Eee` |
| e-Flyers Token Exchange- Client ID: b03ae60a

- Grant type: Token exchange

- Scopes:

  * **openid** (default)

  * `z.read` | Zing- Client ID: bf53b521

- Audience: https\://api.example.com/z

- Scopes: `z.read`

- Attributes:

  * `sub`: **User ID** (default)

  * `z.attr`: `Zee`     |

## Runtime process overview

The following diagram shows a high-level overview of the example machine-to-machine interaction flow:

![A diagram of the example machine-to-machine token exchange flow.](_images/p1-token-exchange-machine-to-machine-diagram.png)

1. Zillion Deals sends a token request to PingOne using the client credentials grant type.

   * For client identification and authentication, Zillion Deals uses the client ID and secret defined in PingOne for Zillion Deals (`client_id=4076de38`).

   * Zillion Deals includes `scope=e.crud` in the token request.

2. PingOne returns an access token to Zillion Deals based on the attribute mappings defined in PingOne for e-Flyers.

   The payload is decoded as follows:

   ```json
   {
     "client_id": "4076de38-d226-49c8-8b47-5f8df21ef3a2", # the client ID of Zillion Deals
     "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
     "jti": "98dccaf3-44d9-47a3-ba56-9f2db0888fca",
     "iat": 1770161254,
     "exp": 1770164854,
     "aud": [
       "https://api.example.com/e" # the audience is e-Flyers
     ],
     "scope": "e.crud", # the scope of the access token
     "e.attr": "Eee",
     "env": "6991589d-87eb-47f4-9131-284cebe106b3",
     "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
     "p1.rid": "98dccaf3-44d9-47a3-ba56-9f2db0888fca"
   }
   ```

3. Zillion Deals sends an API request to e-Flyers. For authorization, Zillion Deals includes the access token (from step 2) as the `Authorization` HTTP request header value in the API request.

4. e-Flyers evaluates the access token and determines that:

   * The issuer of the access token is PingOne.

   * The application that requested the token is Zillion Deals.

   * The audience of the access token includes itself, e-Flyers.

5. e-Flyers sends an introspection request to PingOne to validate the access token.

   For client identification and authentication, e-Flyers uses the client ID and secret defined in PingOne for e-Flyers (`client_id=bc82af8d`).

6. e-Flyers sends a token request using the token exchange grant type to PingOne.

   * For client identification and authentication, e-Flyers uses the client ID and secret defined in PingOne for the e-Flyers Token Exchange application (`client_id=b03ae60a`).

   * e-Flyers includes the following parameters in the token request:

     * `scope=z.read`

     * `subject_token=<access token from step 3>`

     * `subject_token_type=urn:ietf:params:oauth:token-type:access_token`

     * `requested_token_type=urn:ietf:params:oauth:token-type:access_token`

7. PingOne validates the subject token for the following:

   * The subject token is a valid JWT.

   * The issuer of the subject token matches the issuer of the current PingOne environment.

8. PingOne mints an access token based on the attribute mappings defined in PingOne for Zing.

9. PingOne returns a token response containing an access token to e-Flyers.

   The following is the token response:

   ```json
   {
       "access_token": "eyJ…", # the access token as a result of the token exchange token request
       "token_type": "Bearer",
       "expires_in": 3600,
       "scope": "z.read",
       "issued_token_type": "urn:ietf:params:oauth:token-type:access_token"
   }
   ```

   The access token is decoded as follows:

   ```json
   {
     "client_id": "b03ae60a-e4f9-4e9e-ae3d-52592e61d939", # the client ID of e-Flyers Token Exchange App
     "iss": "https://auth.pingone.com/6991589d-87eb-47f4-9131-284cebe106b3/as",
     "jti": "03965dbd-6db1-40a9-92ae-7267faf7808a",
     "iat": 1770161259,
     "exp": 1770164859,
     "aud": [
       "https://api.example.com/z" # the audience is Zing
     ],
     "scope": "z.read", # the scope of the access token
     "z.attr": "Zee",
     "env": "6991589d-87eb-47f4-9131-284cebe106b3",
     "org": "d4229c38-0f5e-4bf7-9292-9d3b0df7294c",
     "p1.rid": "03965dbd-6db1-40a9-92ae-7267faf7808a"
   }
   ```

10. e-Flyers sends an API request to Zing. For authorization, e-Flyers includes the access token (from step 9) as the `Authorization` HTTP request header value in the API request.

11. Zing evaluates the access token and determines that:

    * The issuer of the access token is PingOne.

    * The application requesting the token is the e-Flyers Token Exchange application.

    * The audience of the access token includes itself, Zing.

12. Zing sends an introspection request to PingOne to validate the access token.

13. Zing returns an API response to e-Flyers. At this point, e-Flyers as a resource server can fulfill the API request from Zillion Deals (in step 3).

14. e-Flyers returns an API response to Zillion Deals.

---

---
title: PingOne Use Cases
description: Browse PingOne use cases for integrating PingOne with Ping Identity products and third-party products to secure your business.
component: pingone
page_id: pingone:use_cases:p1_use_cases
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_use_cases.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 20, 2024
---

# PingOne Use Cases

Learn how to configure PingOne with other Ping products and selected third-party products to enable you to better run your security business.

---

---
title: Reference and troubleshooting for Microsoft Entra hybrid join
description: Use the reference and troubleshooting information when configuring Microsoft Entra hybrid join in PingOne.
component: pingone
page_id: pingone:use_cases:p1_microsoft_hybrid_join_troubleshooting
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_microsoft_hybrid_join_troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2025
section_ids:
  entra_hybrid_join_reference: Reference
  federated-idp-settings: Federated IdP settings
  p1-microsoft-365-mappings: Attribute mappings for the Microsoft 365 application
  p1-m365-app-mappings: Attribute mappings reference
  p1-cloud-user-type: User type for cloud users
  user-link-attributes: User link attributes
  attribute-mappings: Attribute mappings
  p1-hybrid-join-user-type: User type for hybrid joined devices
  user-link-attributes-2: User link attributes
  attribute-mappings-2: Attribute mappings
  entra_hybrid_join_troubleshooting: Troubleshooting
  dsregcmd-join-debug-succeeded: dsregcmd /join /debug succeeded
  dsregcmd-status-after-hybrid-join: dsregcmd /status after hybrid join
  dsregcmd-join-debug-failed: dsregcmd /join /debug failed
  attribute-mappings-issue: Attribute mappings issue
  federation-settings-issue: Federation settings issue
  fallback-sync-issue: Fallback sync issue
  messages-from-event-viewer: Messages from Event Viewer
  kerberos-service-account-and-aes-encryption: Kerberos service account and AES encryption
---

# Reference and troubleshooting for Microsoft Entra hybrid join

Use this reference and troubleshooting information when [setting up PingOne as the federated identity provider (IdP)](p1_microsoft_entra_hybrid_join.html) with Microsoft Entra ID:

* [Reference](#entra_hybrid_join_reference)

* [Troubleshooting](#entra_hybrid_join_troubleshooting)

## Reference

Use the information in this section to verify each attribute is mapped correctly when configuring PingOne as the federated identity provider (IdP) and enabling hybrid join.

### Federated IdP settings

Verify the federated identity provider (IdP) settings in PingOne match the federated IdP settings in Microsoft Graph:

1. In the PingOne admin console, go to **Applications > Applications** and click the Microsoft 365 application.

   You'll compare the properties on the **Overview** tab with the settings in Microsoft Graph.

2. On a Windows-based computer, open PowerShell and select the **Run as Administrator** option.

3. Connect to Microsoft Graph and retrieve the current federated IdP settings using the following commands:

   > **Collapse: Connect to Microsoft Graph**
   >
   > ```
   > Connect-MgGraph -Scopes "Directory.ReadWrite.All", "User.ReadWrite.All", "Domain.ReadWrite.All", "Directory.AccessAsUser.All" -NoWelcome
   > ```

   > **Collapse: Retrieve current federated IdP settings**
   >
   > The following command uses an example custom domain of `imokatdi.ping-eng.com`:
   >
   > ```
   > Get-MgDomainFederationConfiguration -DomainId 'imokatdi.ping-eng.com' | Format-List
   > ```

   > **Collapse: Sample output**
   >
   > ```
   > ActiveSignInUri                       : https://sso.whosatwork.ca/wsf/sts/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
   > DisplayName                           : PingOne WS-Federation Identity Provider
   > FederatedIdpMfaBehavior               : acceptIfMfaDoneByFederatedIdp
   > Id                                    : 49d756d3-5c24-411f-b66c-fb8bc7625eaa
   > IsSignedAuthenticationRequestRequired :
   > IssuerUri                             : https://sso.whosatwork.ca/applications/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
   > MetadataExchangeUri                   : https://sso.whosatwork.ca/wsf/mex13/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
   > NextSigningCertificate                :
   > PassiveSignInUri                      : https://sso.whosatwork.ca/wsf/prp/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
   > PasswordResetUri                      :
   > PreferredAuthenticationProtocol       : wsFed
   > PromptLoginBehavior                   :
   > SignOutUri                            : https://sso.whosatwork.ca/wsf/prp/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
   > SigningCertificate                    : MII...
   > SigningCertificateUpdateStatus        : Microsoft.Graph.PowerShell.Models.MicrosoftGraphSigningCertificateUpdateStatus
   > AdditionalProperties                  : {}
   > ```

4. Compare the results from Microsoft Graph with the properties on the **Overview** tab of the Microsoft 365 application in PingOne.

   1. Verify the URL for `MetadataExchangeUri` ends with `/wsf/mex13/<appId>`, where `<appId>` is the application ID of the Microsoft 365 application in PingOne.

   2. If the URL ends with `/wsf/mex/<appId>` (without `13`):

      1. Verify the **Show WS-Trust 1.3 Metadata Exchange URL in Powershell cmdlets** setting is enabled on the **Configuration** tab of the Microsoft 365 application in PingOne.

      2. Follow the steps in [Updating the federated IdP setting](p1_microsoft_hybrid_join_tasks.html#p1-update-federated-idp) to update the `MetadataExchangeUri` property.

   3. Make sure to compare the other properties between PingOne and Microsoft Graph.

### Attribute mappings for the Microsoft 365 application

If `dsregcmd /join /debug` fails with an error code of `invalid_grant`, error description of `AADSTS51004`, or both, verify the `accounttype`, `onpremobjectguid`, and `primarysid` attributes are configured with the required formats:

1. In the PingOne admin console, go to **Applications > Applications** and select the Microsoft 365 application.

2. On the **Attribute Mappings** tab, click the **Pencil** icon ([icon: pencil, set=fa]).

3. For the **`accounttype`** attribute, click the **More Options** (⋮) icon and click **Update NameFormat**.

4. In the **Update NameFormat** modal, verify the format matches the required format. If it doesn't match, select the correct format in the list.

   Refer to the table in [Attribute mappings reference](#p1-m365-app-mappings) for the required format.

5. Repeat steps 3 and 4 for the **`onpremobjectguid`** and **`primarysid`** attributes.

6. On the **Attribute Mappings** tab, click **Save** if you made any changes.

#### Attribute mappings reference

The following table lists the required attribute mappings for the [Microsoft 365 application](p1_microsoft_hybrid_join_tasks.html#p1-update-microsoft-app) in PingOne:

> **Collapse: Microsoft 365 application attribute mappings**
>
> | Attribute          | Mapping                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `ImmutableID`      | * **Format**: Leave the default or select either:
>
>   * **http\://schemas.xmlsoap.org/ws/2005/05/identity/claims**
>
>   * **http\://schemas.microsoft.com/LiveID/Federation/2008/05**
>
> * **Source**: Use the following expression:
>
>   ```
>   #string.uuidAsBase64Guid(user.externalId,null)
>   ```                                                                                                                                    |
> | `Subject`          | - **Format**: Map **Subject NameIdentifier Format** on the **Configuration** tab of the application. Choose either of the following:
>
>   * Leave **`urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`** (default) selected.
>
>   * Select **`urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`** in the list.
>
> - **Source**: Use the following expression:
>
>   ```
>   #string.uuidAsBase64Guid(user.externalId,null)
>   ``` |
> | `UPN`              | * **Format**: Leave the default or select either:
>
>   * **http\://schemas.xmlsoap.org/ws/2005/05/identity/claims**
>
>   * **http\://schemas.xmlsoap.org/claims**
>
> * **Source**: Select the [custom attribute you created to store `userPrincipalName`](p1_microsoft_hybrid_join_tasks.html#p1-create-attribute) from AD user objects in the **PingOne Mappings** list.                                                              |
> | `accounttype`      | - **Format**: Select **http\://schemas.microsoft.com/ws/2012/01 **.
>
> - **Source**: Use the following expression: `"DJ"` (including the quotation marks).                                                                                                                                                                                                                                                                         |
> | `onpremobjectguid` | * **Format**: Select **http\://schemas.microsoft.com/identity/claims**.
>
> * **Source**: Use the following expression:
>
>   ```
>   #string.uuidAsBase64Guid(user.externalId,null)
>   ```                                                                                                                                                                                                                                               |
> | `primarysid`       | - **Format**: Select **http\://schemas.microsoft.com/ws/2008/06/identity/claims**.
>
> - **Source**: Select the [attribute you previously created to store `objectSid`](p1_microsoft_hybrid_join_tasks.html#p1-create-attributes) for hybrid joined devices.                                                                                                                                                                        |

### User type for cloud users

Refer to the attribute mappings in this section when you [configure the LDAP gateway and add a user type for cloud users](p1_microsoft_hybrid_join_tasks.html#p1-add-ldap-gateway).

#### User link attributes

The following attributes must be mapped on the **Lookup** tab of the LDAP gateway in PingOne in the following order:

1. `objectGUID`

2. `objectSid`

3. `dn`

4. `sAMAccountName`

#### Attribute mappings

The following table lists the required attribute mappings when you add a new user type to the LDAP gateway and click **Use default values**. The mappings can be added in any order.

> **Collapse: LDAP gateway cloud user attribute mappings**
>
> | **PingOne User Profile Attribute**                                                                                                            | **LDAP Attribute**      |
> | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
> | Username                                                                                                                                      | `sAMAccountName`        |
> | Email Address                                                                                                                                 | `mail`                  |
> | Family Name                                                                                                                                   | `sn`                    |
> | Formatted                                                                                                                                     | `displayName`           |
> | Given Name                                                                                                                                    | `givenName`             |
> | Title                                                                                                                                         | `title`                 |
> | Primary Phone                                                                                                                                 | `telephoneNumber`       |
> | Mobile Phone                                                                                                                                  | `mobile`                |
> | Street Address                                                                                                                                | `streetAddress`         |
> | Locality                                                                                                                                      | `l`                     |
> | Region                                                                                                                                        | `st`                    |
> | Postal Code                                                                                                                                   | `postalCode`            |
> | Country Code                                                                                                                                  | `c`                     |
> | External ID                                                                                                                                   | `mS-DS-ConsistencyGuid` |
> | The [custom attribute you created to store `userPrincipalName`](p1_microsoft_hybrid_join_tasks.html#p1-create-attribute) from AD user objects | `userPrincipalName`     |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default source of **External ID** is the `mS-DS-ConsistencyGuid` attribute because Entra Connect Sync uses the `mS-DS-ConsistencyGuid` attribute as the `sourceAnchor` attribute to identify synced users by default. If you selected another AD user attribute as the `sourceAnchor` attribute in [Installing Entra Connect Sync](p1_microsoft_entra_hybrid_join_prerequisites.html#p1-install-entra-connect-sync) (step 11), select that AD user attribute as the source of **External ID** in this step. |

### User type for hybrid joined devices

Refer to the attribute mappings in this section when you [add a user type for hybrid joined devices](p1_microsoft_hybrid_join_tasks.html#p1-add-user-type) to the LDAP gateway.

#### User link attributes

The following attributes must be added on the **Lookup** tab of the LDAP gateway in PingOne in the following order:

1. `objectGUID`

2. `objectSid`

3. `dn`

4. `sAMAccountName`

#### Attribute mappings

The following table lists the attribute mappings when you:

* Add a new user type to the LDAP gateway.

* Click **Use default values**.

* Delete all default values except those listed in the following table.

The mappings can be added in any order.

> **Collapse: LDAP gateway hybrid joined devices attribute mappings**
>
> | **PingOne User Profile Attribute**                                                                                                          | **LDAP Attribute**      |
> | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
> | Username                                                                                                                                    | `mS-DS-ConsistencyGuid` |
> | Nickname                                                                                                                                    | `sAMAccountName`        |
> | External ID                                                                                                                                 | `mS-DS-ConsistencyGuid` |
> | The [custom attribute you created to store `objectSid`](p1_microsoft_hybrid_join_tasks.html#p1-create-attributes) for hybrid joined devices | `objectSid`             |

|   |                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default source of **External ID** is the `mS-DS-ConsistencyGuid` attribute. If Entra Connect Sync doesn't populate the synced AD device objects with the `mS-DS-ConsistencyGuid` value, update the source of **External ID** with another AD attribute that can be used to identify synced devices, such as `objectGUID`. Make sure to use the same source for **Username**. |

* Use the same LDAP attribute for **Username** and **External ID**.

* Map **Nickname** to `sAMAccountName` to represent device names and identify devices in PingOne.

* Create a custom attribute to map the required `objectSid` attribute.

  Alternatively, you can map `objectSid` to the system-provided **Account ID**. However, note that **Account ID** is typically associated with a user account.

## Troubleshooting

Use the information in this section to troubleshoot the hybrid join process when running `dsregcmd /join /debug` in [Validation](p1_microsoft_hybrid_join_tasks.html#p1-hybrid-join-validation).

### `dsregcmd /join /debug` succeeded

When you run `dsregcmd /join /debug`, the following is an example response when the hybrid join process succeeds, and the device is successfully hybrid joined:

> **Collapse: succeeded example response**
>
> ```
> PS C:\Windows\System32> dsregcmd /join /debug
> DsrCLI: logging initialized.
> DsrCLI: logging initialized.
> DsrCmdJoinHelper::Join: ClientRequestId: 7d05360e-378f-4e2e-81b1-0289d60b974bDsrCmdAccountMgr::IsDomainControllerAvailable: DsGetDcName success { domain:imokatdi.ping-eng.com forest:imokatdi.ping-eng.com domainController:\\IMOK-DC02.imokatdi.ping-eng.com isDcAvailable:true }
> PreJoinChecks Complete.
> preCheckResult: Join
> deviceKeysHealthy: undefined
> isJoined: undefined
> isDcAvailable: YES
> isSystem: YES
> keyProvider: undefined
> keyContainer: undefined
> dsrInstance: undefined
> elapsedSeconds: 0
> resultCode: 0x0
> Automatic device join pre-check tasks completed.
> TenantInfo::Discover: Join Info { TenantType = Federated; AutoJoinEnabled = 1; TenandID = 07ec9af2-7ce5-4ab7-8638-115736bbf990; TenantName = imokatdi.ping-eng.com }
> GetComputerTokenForADRS: Get token for ADRS
> GetComputerTokenForADRS: Auth code URL: "https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990/oauth2/authorize"
> GetComputerTokenForADRS: Token request authority: "https://login.microsoftonline.com/common"
> AdalLog: Token is not available in the cache ; HRESULT: 0x0
> AdalLog: Authority validation is enabled ; HRESULT: 0x0
> AdalLog: Authority validation is completed ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken get refresh token info ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken- refresh token is not available ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken- returns false ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuth w Tenant ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuth- received realm info ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::GetAppliesTo: using resource ID "urn:federation:MicrosoftOnline" for authority "https://login.microsoftonline.com/common". ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: Webrequest opening connection ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: Webrequest has valid state ; HRESULT: 0x0
> AdalLog: WebRequest Status:200 ; HRESULT: 0x0
> AdalLog: Webrequest returns success for oauth response ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa9000f
> AdalLog:  HRESULT: 0x4aa9000d
> Join request ID: 7d05360e-378f-4e2e-81b1-0289d60b974b
> Join response time: Thu, 10 Jul 2025 17:22:14 GMT
> Join HTTP status: 200
> DsrCmdJoinHelper::Join: AutoEnrollAsComputer completed successfully
> DSREGCMD_END_STATUS
>              AzureAdJoined : YES
>           EnterpriseJoined : NO
>                   DeviceId : 3f0817b9-ca17-4714-ab81-f7b5943dec7b
>                 Thumbprint : F243C1D15BF2CD9D33764913B003E9FB56543560
>  DeviceCertificateValidity : [ 2025-07-10 16:52:13.000 UTC -- 2035-07-10 17:22:13.000 UTC ]
>             KeyContainerId : 9b004996-ad3f-4d33-ba3c-c25bc5cbdb73
>                KeyProvider : Microsoft Software Key Storage Provider
>               TpmProtected : NO
>           DeviceAuthStatus : SUCCESS
>                 TenantName :
>                   TenantId : 07ec9af2-7ce5-4ab7-8638-115736bbf990
>                AuthCodeUrl : https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990/oauth2/authorize
>             AccessTokenUrl : https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990/oauth2/token
>                     MdmUrl :
>                  MdmTouUrl :
>           MdmComplianceUrl :
>                SettingsUrl :
>             JoinSrvVersion : 2.0
>                 JoinSrvUrl : https://enterpriseregistration.windows.net/EnrollmentServer/device/
>                  JoinSrvId : urn:ms-drs:enterpriseregistration.windows.net
>              KeySrvVersion : 1.0
>                  KeySrvUrl : https://enterpriseregistration.windows.net/EnrollmentServer/key/
>                   KeySrvId : urn:ms-drs:enterpriseregistration.windows.net
>         WebAuthNSrvVersion : 1.0
>             WebAuthNSrvUrl : https://enterpriseregistration.windows.net/webauthn/07ec9af2-7ce5-4ab7-8638-115736bbf990/
>              WebAuthNSrvId : urn:ms-drs:enterpriseregistration.windows.net
>     DeviceManagementSrvVer : 1.0
>     DeviceManagementSrvUrl : https://enterpriseregistration.windows.net/manage/07ec9af2-7ce5-4ab7-8638-115736bbf990/
>      DeviceManagementSrvId : urn:ms-drs:enterpriseregistration.windows.net
> ```

Note the following in the response:

* `AzureAdJoined : YES` means the hybrid join attempt succeeded, and the device is now hybrid joined to Entra ID.

* `DeviceId` in the output matches the device ID of the device record in the Entra admin center.

* `TenantId` is your Entra tenant ID.

### `dsregcmd /status` after hybrid join

The following is an example response when you run `dsregcmd /status` after hybrid join succeeded:

> **Collapse: example response**
>
> ```
> PS C:\Windows\System32> dsregcmd /status
>
> +----------------------------------------------------------------------+
> | Device State                                                         |
> +----------------------------------------------------------------------+
>
>              AzureAdJoined : YES
>           EnterpriseJoined : NO
>               DomainJoined : YES
>                 DomainName : IMOKATDI
>                Device Name : IMOK-HYJD.imokatdi.ping-eng.com
>
> +----------------------------------------------------------------------+
> | Device Details                                                       |
> +----------------------------------------------------------------------+
>
>                   DeviceId : 3f0817b9-ca17-4714-ab81-f7b5943dec7b
>                 Thumbprint : F243C1D15BF2CD9D33764913B003E9FB56543560
>  DeviceCertificateValidity : [ 2025-07-10 16:52:13.000 UTC -- 2035-07-10 17:22:13.000 UTC ]
>             KeyContainerId : 9b004996-ad3f-4d33-ba3c-c25bc5cbdb73
>                KeyProvider : Microsoft Software Key Storage Provider
>               TpmProtected : NO
>           DeviceAuthStatus : SUCCESS
>
> +----------------------------------------------------------------------+
> | Tenant Details                                                       |
> +----------------------------------------------------------------------+
>
>                 TenantName :
>                   TenantId : 07ec9af2-7ce5-4ab7-8638-115736bbf990
>                AuthCodeUrl : https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990/oauth2/authorize
>             AccessTokenUrl : https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990/oauth2/token
>                     MdmUrl :
>                  MdmTouUrl :
>           MdmComplianceUrl :
>                SettingsUrl :
>             JoinSrvVersion : 2.0
>                 JoinSrvUrl : https://enterpriseregistration.windows.net/EnrollmentServer/device/
>                  JoinSrvId : urn:ms-drs:enterpriseregistration.windows.net
>              KeySrvVersion : 1.0
>                  KeySrvUrl : https://enterpriseregistration.windows.net/EnrollmentServer/key/
>                   KeySrvId : urn:ms-drs:enterpriseregistration.windows.net
>         WebAuthNSrvVersion : 1.0
>             WebAuthNSrvUrl : https://enterpriseregistration.windows.net/webauthn/07ec9af2-7ce5-4ab7-8638-115736bbf990/
>              WebAuthNSrvId : urn:ms-drs:enterpriseregistration.windows.net
>     DeviceManagementSrvVer : 1.0
>     DeviceManagementSrvUrl : https://enterpriseregistration.windows.net/manage/07ec9af2-7ce5-4ab7-8638-115736bbf990/
>      DeviceManagementSrvId : urn:ms-drs:enterpriseregistration.windows.net
>
> +----------------------------------------------------------------------+
> | User State                                                           |
> +----------------------------------------------------------------------+
>
>                     NgcSet : NO
>            WorkplaceJoined : NO
>              WamDefaultSet : YES
>        WamDefaultAuthority : organizations
>               WamDefaultId : https://login.microsoft.com
>             WamDefaultGUID : {B16898C6-A148-4967-9171-64D755DA8520} (AzureAd)
>
> +----------------------------------------------------------------------+
> | SSO State                                                            |
> +----------------------------------------------------------------------+
>
>                 AzureAdPrt : YES
>       AzureAdPrtUpdateTime : 2025-07-10 15:46:21.000 UTC
>       AzureAdPrtExpiryTime : 2025-07-24 15:46:20.000 UTC
>        AzureAdPrtAuthority : https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990
>              EnterprisePrt : NO
>     EnterprisePrtAuthority :
>
> +----------------------------------------------------------------------+
> | Diagnostic Data                                                      |
> +----------------------------------------------------------------------+
>
>         AadRecoveryEnabled : NO
>     Executing Account Name : IMOKATDI\ecotton, ecotton@imokatdi.ping-eng.com
>                KeySignTest : PASSED
>
> +----------------------------------------------------------------------+
> | IE Proxy Config for Current User                                     |
> +----------------------------------------------------------------------+
>
>       Auto Detect Settings : YES
>     Auto-Configuration URL :
>          Proxy Server List :
>          Proxy Bypass List :
>
> +----------------------------------------------------------------------+
> | WinHttp Default Proxy Config                                         |
> +----------------------------------------------------------------------+
>
>                Access Type : DIRECT
>
> +----------------------------------------------------------------------+
> | Ngc Prerequisite Check                                               |
> +----------------------------------------------------------------------+
>
>             IsDeviceJoined : YES
>              IsUserAzureAD : YES
>              PolicyEnabled : NO
>           PostLogonEnabled : YES
>             DeviceEligible : NO
>         SessionIsNotRemote : NO
>             CertEnrollment : none
>               PreReqResult : WillNotProvision
>
> For more information, please visit https://www.microsoft.com/aadjerrors
> ```

Note the following in the response:

* In the `Device State` section:

  * `DomainName` is your Active Directory (AD) domain name.

  * `Device Name` is the fully qualified name of the device.

* In the `SSO State` section:

  * `AzureAdPrt` indicates the device was issued a primary refresh token (PRT) for the signed-on user.

Learn more in [Troubleshoot devices using the `dsregcmd` command](https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd#diagnostics-data) in the Entra documentation.

### `dsregcmd /join /debug` failed

Hybrid join can fail if the assertion from PingOne doesn't contain the required attributes, values, or formats.

When you run `dsregcmd /join /debug`, the following is an example response if hybrid join fails because of PingOne and fallback sync:

> **Collapse: failed example response**
>
> ```
> PS C:\Windows\System32> dsregcmd /join /debug
> DsrCLI: logging initialized.
> DsrCLI: logging initialized.
> DsrCmdJoinHelper::Join: ClientRequestId: 7b690c51-7ff3-4900-8875-18a409e1053eDsrCmdAccountMgr::IsDomainControllerAvailable: DsGetDcName success { domain:imokatdi.ping-eng.com forest:imokatdi.ping-eng.com domainController:\\IMOK-DC01.imokatdi.ping-eng.com isDcAvailable:true }
> PreJoinChecks Complete.
> preCheckResult: Join
> deviceKeysHealthy: undefined
> isJoined: undefined
> isDcAvailable: YES
> isSystem: YES
> keyProvider: undefined
> keyContainer: undefined
> dsrInstance: undefined
> elapsedSeconds: 0
> resultCode: 0x0
> Automatic device join pre-check tasks completed.
> TenantInfo::Discover: Join Info { TenantType = Federated; AutoJoinEnabled = 1; TenandID = 07ec9af2-7ce5-4ab7-8638-115736bbf990; TenantName = imokatdi.ping-eng.com }
> GetComputerTokenForADRS: Get token for ADRS
> GetComputerTokenForADRS: Auth code URL: "https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990/oauth2/authorize"
> GetComputerTokenForADRS: Token request authority: "https://login.microsoftonline.com/common"
> AdalLog: Token is not available in the cache ; HRESULT: 0x0
> AdalLog: Authority validation is enabled ; HRESULT: 0x0
> AdalLog: Authority validation is completed ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken get refresh token info ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken- refresh token is not available ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken- returns false ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuth w Tenant ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuth- received realm info ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::GetAppliesTo: using resource ID "urn:federation:MicrosoftOnline" for authority "https://login.microsoftonline.com/common". ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: Webrequest opening connection ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: Webrequest has valid state ; HRESULT: 0x0
> AdalLog: WebRequest Status:400 ; HRESULT: 0x0
> AdalLog: Token response is not successfull. Status:400 ResponseText:{"error":"invalid_grant","error_description":"AADSTS51004: The user account {EUII Hidden} does not exist in the 07ec9af2-7ce5-4ab7-8638-115736bbf990 directory. To sign into this application, the account must be added to the directory. Trace ID: a441252e-1978-48b9-a07b-5926cfb74400 Correlation ID: 7b690c51-7ff3-4900-8875-18a409e1053e Timestamp: 2025-07-09 02:14:21Z","error_codes":[51004],"timestamp":"2025-07-09 02:14:21Z","trace_id":"a441252e-1978-48b9-a07b-5926cfb74400","correlation_id":"7b690c51-7ff3-4900-8875-18a409e1053e","error_uri":"https://login.microsoftonline.com/error?code=51004"} ; HRESULT: 0x0
> AdalLog: Webrequest returns error code:invalid_grant and error description:AADSTS51004: The user account {EUII Hidden} does not exist in the 07ec9af2-7ce5-4ab7-8638-115736bbf990 directory. To sign into this application, the account must be added to the directory. Trace ID: a441252e-1978-48b9-a07b-5926cfb74400 Correlation ID: 7b690c51-7ff3-4900-8875-18a409e1053e Timestamp: 2025-07-09 02:14:21Z ; HRESULT: 0x0
> AdalLog:  HRESULT: 0xcaa20003
> AdalLog:  HRESULT: 0xcaa90006
> GetStatus returned failure
> AdalLog:  HRESULT: 0xcaa1000e
> GetComputerTokenForADRS: AdalErrorCode: 0xcaa1000e
> AdalCorrelationId: 7b690c51-7ff3-4900-8875-18a409e1053e
> AdalLog:  HRESULT: 0xcaa1000e
> GetStatus returned failure
> AdalLog:  HRESULT: 0xcaa90006
> AdalLog:  HRESULT: 0xcaa20003
> AdalLog: Webrequest returns error code:invalid_grant and error description:AADSTS51004: The user account {EUII Hidden} does not exist in the 07ec9af2-7ce5-4ab7-8638-115736bbf990 directory. To sign into this application, the account must be added to the directory. Trace ID: a441252e-1978-48b9-a07b-5926cfb74400 Correlation ID: 7b690c51-7ff3-4900-8875-18a409e1053e Timestamp: 2025-07-09 02:14:21Z ; HRESULT: 0x0
> AdalLog: Token response is not successfull. Status:400 ResponseText:{"error":"invalid_grant","error_description":"AADSTS51004: The user account {EUII Hidden} does not exist in the 07ec9af2-7ce5-4ab7-8638-115736bbf990 directory. To sign into this application, the account must be added to the directory. Trace ID: a441252e-1978-48b9-a07b-5926cfb74400 Correlation ID: 7b690c51-7ff3-4900-8875-18a409e1053e Timestamp: 2025-07-09 02:14:21Z","error_codes":[51004],"timestamp":"2025-07-09 02:14:21Z","trace_id":"a441252e-1978-48b9-a07b-5926cfb74400","correlation_id":"7b690c51-7ff3-4900-8875-18a409e1053e","error_uri":"https://login.microsoftonline.com/error?code=51004"} ; HRESULT: 0x0
> AdalLog: WebRequest Status:400 ; HRESULT: 0x0
> AdalLog: Webrequest has valid state ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: Webrequest opening connection ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: AggregatedTokenRequest::GetAppliesTo: using resource ID "urn:federation:MicrosoftOnline" for authority "https://login.microsoftonline.com/common". ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuth- received realm info ; HRESULT: 0x0
> AdalLog:  HRESULT: 0x4aa90010
> AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuth w Tenant ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken- returns false ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken- refresh token is not available ; HRESULT: 0x0
> AdalLog: AggregatedTokenRequest::AcquireToken get refresh token info ; HRESULT: 0x0
> AdalLog: Authority validation is completed ; HRESULT: 0x0
> AdalLog: Authority validation is enabled ; HRESULT: 0x0
> AdalLog: Token is not available in the cache ; HRESULT: 0x0
> AutoEnrollAsComputer: Unable to retrieve access token. GetComputerTokenForADRS failed with error 0xcaa20003.
> DsrCmdJoinHelper::Join: Federated ADRS join failed with error 0xcaa1000e. Try synchronized join.
> Join request ID: 2b1b97b0-539e-4b48-91fe-55761b923b45
> Join response time: Wed, 09 Jul 2025 02:14:22 GMT
> Join HTTP status: 200
> DsrCmdJoinHelper::Join: completed successfully
> DSREGCMD_END_STATUS
>              AzureAdJoined : YES
>           EnterpriseJoined : NO
>                   DeviceId : 3f0817b9-ca17-4714-ab81-f7b5943dec7b
>                 Thumbprint : DADA1C38EBA6E6884F7DF92E22F057F689C07C8C
>  DeviceCertificateValidity : [ 2025-07-09 01:44:22.000 UTC -- 2035-07-09 02:14:22.000 UTC ]
>             KeyContainerId : 3fb81d8c-c49a-4ade-ac2b-8be7ebc4c54b
>                KeyProvider : Microsoft Software Key Storage Provider
>               TpmProtected : NO
>           DeviceAuthStatus : SUCCESS
>                 TenantName :
>                   TenantId : 07ec9af2-7ce5-4ab7-8638-115736bbf990
>                AuthCodeUrl : https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990/oauth2/authorize
>             AccessTokenUrl : https://login.microsoftonline.com/07ec9af2-7ce5-4ab7-8638-115736bbf990/oauth2/token
>                     MdmUrl :
>                  MdmTouUrl :
>           MdmComplianceUrl :
>                SettingsUrl :
>             JoinSrvVersion : 2.0
>                 JoinSrvUrl : https://enterpriseregistration.windows.net/EnrollmentServer/device/
>                  JoinSrvId : urn:ms-drs:enterpriseregistration.windows.net
>              KeySrvVersion : 1.0
>                  KeySrvUrl : https://enterpriseregistration.windows.net/EnrollmentServer/key/
>                   KeySrvId : urn:ms-drs:enterpriseregistration.windows.net
>         WebAuthNSrvVersion : 1.0
>             WebAuthNSrvUrl : https://enterpriseregistration.windows.net/webauthn/07ec9af2-7ce5-4ab7-8638-115736bbf990/
>              WebAuthNSrvId : urn:ms-drs:enterpriseregistration.windows.net
>     DeviceManagementSrvVer : 1.0
>     DeviceManagementSrvUrl : https://enterpriseregistration.windows.net/manage/07ec9af2-7ce5-4ab7-8638-115736bbf990/
>      DeviceManagementSrvId : urn:ms-drs:enterpriseregistration.windows.net
> ```

Note the following errors in the response:

* `AdalLog: Webrequest returns error code:invalid_grant and error description:AADSTS51004`

* `AutoEnrollAsComputer: Unable to retrieve access token GetComputerTokenForADRS failed with error 0xcaa20003`

* `DsrCmdJoinHelper::Join: Federated ADRS join failed with error 0xcaa1000e`

#### Attribute mappings issue

If you receive the previously noted errors when running `dsregcmd /join /debug`, verify the attributes and mappings are configured correctly in the [user type for hybrid joined devices](#p1-hybrid-join-user-type) and [Microsoft 365 application](#p1-microsoft-365-mappings).

For the Microsoft 365 application, ensure each required attribute is configured with the correct attribute format.

#### Federation settings issue

Verify the federation settings of the verified custom domain using Microsoft Graph cmdlets.

In the following example, the verified custom domain is `imokatdi.ping-eng.com`, and the custom domain of the PingOne environment is `sso.example.com`:

> **Collapse: PowerShell example with custom domain**
>
> ```
> PowerShell 7.5.2
> PS C:\Windows\System32> Connect-MgGraph -Scopes "Directory.ReadWrite.All", "User.ReadWrite.All", "Domain.ReadWrite.All", "Directory.AccessAsUser.All" -NoWelcome
>
> (Complete the sign on process as prompted by Microsoft.)
>
> PS C:\Windows\System32> Get-MgDomainFederationConfiguration -DomainId "imokatdi.ping-eng.com" | Format-List
>
> ActiveSignInUri                       : https://sso.example.com/wsf/sts/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
> DisplayName                           : PingOne WS-Federation Identity Provider
> FederatedIdpMfaBehavior               : acceptIfMfaDoneByFederatedIdp
> Id                                    : 49d756d3-5c24-411f-b66c-fb8bc7625eaa
> IsSignedAuthenticationRequestRequired :
> IssuerUri                             : https://sso.example.com/applications/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
> MetadataExchangeUri                   : https://sso.example.com/wsf/mex13/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
> NextSigningCertificate                :
> PassiveSignInUri                      : https://sso.example.com/wsf/prp/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
> PasswordResetUri                      :
> PreferredAuthenticationProtocol       : wsFed
> PromptLoginBehavior                   :
> SignOutUri                            : https://sso.example.com/wsf/prp/4afaa6b9-1497-44b6-b1ce-1a6d396f7f7e
> SigningCertificate                    : MIIDATCCAemgAwIBAgIGAZXugDEBMA0GCSqGSIb3DQEBCwUAMDcxCzAJBgNVBAYTAkNBMRMwEQYDVQQKEwpEYW5ueSB0ZXN0MRMwEQYDVQQDEwpTaWdu
> IE1lIFVwMB4XDTI1MDMzMTIzMTg1M1oXDTM1MDMyOTIzMTg1M1owNzELMAkGA1UEBhMCQ0ExEzARBgNVBAoTCkRhbm55IHRlc3QxEzARBgNVBAMTClNp
> Z24gTWUgVXAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC1oEADpq5sJ5ifgVtzt8rRBUYfLOMrvHowj05y2qB9wFdobvOsBqXq8mAPr+gz
> Iq3MpTvYwsdLZ7yw55FNu59yTykVakAH+IKYfMe1X44IWvZQ4tmbvvtmmOlCsLDL8vPi6iJOyQHj1iUtDprb9YxeuQSRLJ4B98XGxQ5cJwurbbs3Zgfo
> PrKTuoprmRlsxSllB0HVdGIh0WrBmfgJWmJXK0dOn4Rm0WtiU8P15aktBkI9Zn/pVEC8Ix6HAX6hkJT10GV9sMBXxQtGNB+OBT4OFTcomEAzLP2av6uU
> 6X60Mlv+79sTzFBnEDGZYWWMOTlEziVw3QJrbcm1OxTCSrklAgMBAAGjEzARMA8GA1UdEQQIMAaHBH8AAAEwDQYJKoZIhvcNAQELBQADggEBALUbyug+
> xa99My7zqa1SHXY4F3sGCQPG7LZPWWGCd+6Plw/EXoGjnocx2Mg9WYCJCXTmchjXef7U4SDN5F8h3ZcaFAjVey9FjX2uvQt0v/l23+ZpQIVxulbIZKIE
> a4iHrquSzDao3w8vIrL40ZvOUyvk+OjiP5PFOXlZ9kyN9EOfbuWjT1+sM49JmskVq70hfF4kO7o/+bmwMkE8rrKVocKjES/nGlcTit66FADkBDW1unCS
> VWWRoNz4BuWa0M04tMj54aIqyZO3fXmje+l/xKUcpD3myfDhybncn0kIa0LmaqlNaCVm7zBjsyPi4NiYHAcJpzeeqMbC/1BV4Do0sYg=
> SigningCertificateUpdateStatus        : Microsoft.Graph.PowerShell.Models.MicrosoftGraphSigningCertificateUpdateStatus
> AdditionalProperties                  : {}
> ```

Verify each setting against the **Microsoft Graph PowerShell cmdlets** on the **Overview** tab of the Microsoft 365 application in PingOne.

The `MetadataExchangeUri` value should contain `/wsf/mex13/` in the path. If the path contains `/wsf/mex/` without the `13`, follow the steps in [Updating the federated IdP setting](p1_microsoft_hybrid_join_tasks.html#p1-update-federated-idp) to configure Entra ID to use the WS-Trust 1.3-compliant metadata exchange URL.

#### Fallback sync issue

If fallback sync isn't disabled in Windows, the fallback mechanism initiates and succeeds with the following response from the previous example:

```
Try synchronized join
DsrCmdJoinHelper::Join: completed successfully
```

We recommend [disabling fallback sync](p1_microsoft_hybrid_join_tasks.html#p1-disable-fallback-sync) when configuring PingOne to handle Entra hybrid join. Learn more in [Troubleshoot devices using the `dsregcmd` command](https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd#diagnostics-data) in the Entra documentation.

If you don't disable fallback sync, failures will occur in other applications that use the security token service (STS) flow for authentication but don't support the fallback mechanism.

### Messages from Event Viewer

Depending on the device setup and the status of Entra Connect Sync, a device might try to hybrid join to Entra ID when it boots or when the user signs on. Log messages from failures and successful attempts can be found in the Windows Event Viewer application.

1. On a Windows-based computer, start **Event Viewer**.

2. Go to **Applications and Service Logs > Microsoft > Windows > User Device Registration > Admin**.

   ![A screen capture of the Event Viewer log messages.](_images/p1_microsoft_hybrid_join_event_viewer_logs.png)

Log messages are displayed in the center panel and are similar to messages shown when you run the `dsregcmd` command.

### Kerberos service account and AES encryption

The Kerberos service account must be configured to support Kerberos AES encryption.

1. On a Windows-based computer, open **Active Directory Users and Computers** and locate the service account you configured for the PingOne LDAP gateway Kerberos integration.

2. Right-click the service account and click **Properties**.

3. On the **Account** tab, in the **Account Options** section, select the **This account supports Kerberos AES 256 bit encryption** checkbox.

4. Restart the gateway instance.

   Learn more in [Starting a gateway instance](../integrations/p1_starting_gateway_instance_ldap.html).

5. Confirm that Kerberos authentication is working.

6. If Kerberos authentication still isn't working, purge existing Kerberos tickets:

   1. Open a command prompt and enter `klist purge`.

   2. Sign off from Windows and sign back on.

   3. Attempt Kerberos authentication.

7. If Kerberos authentication still isn't working after purging existing Kerberos tickets, reset the password for the service account and purge existing Kerberos tickets again.

---

---
title: Securing your APIs using PingOne and Amazon Verified Permissions
description: Configure PingOne as an identity provider with Amazon Verified Permissions to secure API Gateway APIs using group-based access control.
component: pingone
page_id: pingone:use_cases:p1_use_case_amazon_verified_permissions
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_use_case_amazon_verified_permissions.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 21, 2025
section_ids:
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  create-oidc-app: Creating and configuring an OIDC application in PingOne
  creating-example-users-and-groups-in-pingone: Creating example users and groups in PingOne
  creating-an-example-api-in-aws: Creating an example API in AWS
  result: Result
  next-steps: Next Steps
  creating-an-amazon-verified-permissions-policy-store: Creating an Amazon Verified Permissions policy store
  result-2: Result
---

# Securing your APIs using PingOne and Amazon Verified Permissions

Reduce the time your developers spend securing APIs using permissions based on role-based access control (RBAC) *(tooltip: \<div class="paragraph">
\<p>Also known as non-discretionary access control, this authorization strategy bases user access on assigned roles.\</p>
\</div>)* by using PingOne as your identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* and Amazon Verified Permissions (AVP) as your permissions manager.

PingOne is a cloud-based identity as a service (IDaaS) *(tooltip: \<div class="paragraph">
\<p>Cloud-based authentication solutions for identity and access management (IAM).\</p>
\</div>)* framework for secure identity access management that uses an organization-based model to define tenant accounts and their related entities within the PingOne platform.

AVP is a fine-grained authorization service that accelerates application development by decoupling authorization logic from business logic. It uses the [Cedar policy language](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html#avp-cedar) to write authorization policies and allows developers to build applications faster by externalizing authorization and centralizing policy management.

This use case walks through how configuring AVP to secure access to application APIs hosted on the Amazon API Gateway for identities managed in PingOne. AVP will automatically create the Cedar policies that determine which APIs a user is permitted to call based on their PingOne group membership. When the user authenticates with PingOne, their group membership is included in the OIDC token that PingOne generates. AVP then compares the user's group memberships in the OIDC token to the Cedar policies and either allows or denies access to the API accordingly.

## Goals

After completing this use case, you'll know how to configure AVP to secure access to your API for identities managed in PingOne.

## What you'll do

In PingOne, you'll:

1. Create an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)* web application.

2. Create two example users.

3. Create two example groups.

In Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">
\<p>An Amazon subsidiary providing cloud computing platforms.\</p>
\</div>)*, you'll:

1. Create an example REST API and deploy the API to the Amazon API Gateway.

2. Configure AVP to secure access to your API for identities managed in PingOne.

## Before you begin

In PingOne, each organization contains one or more tenants, known as environments, which define separate working domains within an organization.

To set up this use case, you'll need:

* A PingOne organization. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* A PingOne environment that includes the PingOne SSO service.

* An AWS account with access to the API Gateway and AVP services.

## Tasks

### Creating and configuring an OIDC application in PingOne

Create and configure an OIDC web application to manage using PingOne SSO.

1. In the PingOne admin console, go to **Applications > Applications** and click the **[icon: plus, set=fa]**icon.

2. In the **Application Name** field, enter a unique identifier for the application.

   For example, `AVP app`.

3. (Optional) In the **Description** field, enter a brief description of the application.

   For example, `Use this application to verify sign on using Amazon Verified Permissions`.

4. (Optional) Click **Icon** to upload an image to represent the application.

   |   |                                                        |
   | - | ------------------------------------------------------ |
   |   | Use a file up to 1MB in JPG, JPEG, GIF, or PNG format. |

5. For **Application Type**, click **OIDC Web App**.

6. Click **Save**.

   The details panel for the application opens.

7. []()On the **Overview** tab, copy the following values and save them to a secure location. You'll need these values when you configure AVP:

   1. In the **General** section, copy the values for **Client ID** and **Client Secret**.

   2. In the **Connection Details section**, copy the **Issuer ID**.

8. On the **Configuration** tab, click the **Pencil** icon.

9. In the **OIDC Settings** section, in the **Redirect URIs** field, enter the address to which PingOne will forward the OIDC response after verification.

   For example, `https://oauth.pstmn.io/v1/browser-callback`.

10. Click **Save**.

11. []()On the **Attribute Mappings** tab, click the **Pencil** icon

12. Click **[icon: plus, set=fa]Add** and add a new custom attribute as follows:

    1. In the **Attributes** column, enter `group`.

    2. In the **PingOne Mappings** column, select **Group Names**.

13. Click **Save**.

14. (Optional) On the **Policies** tab, click the **Pencil** icon, select the authentication policies for the application, and click **Save**.

    Learn more in [Authentication policies for applications](../applications/p1_auth_policies_for_applications.html) and [Applying authentication policies to an application](../applications/p1_apply_auth_policy_to_applications.html).

15. (Optional) On the **Access** tab, click the **Pencil** icon, configure the access settings for your application, and click **Save**.

    Learn more in [Application access control](../applications/p1_application_access_control.html).

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you selected **Response Type = Code** and **Grant Type = Authorization Code**, there's also an **Integrate** tab that you can use to test your configuration. Learn more in [Integrate PingOne with a Node.js Express app](../pingone_tutorials/p1_tutorial_integrate_nodejs_express_app.html) and [Integrate Ping SDK for JavaScript with PingOne](https://docs.pingidentity.com/sdks/latest/sdks/tutorials/javascript/pingone/index.html). |

16. On the **Applications** page, browse or search for the application you just created and click the toggle to enable it.

    |   |                                                    |
    | - | -------------------------------------------------- |
    |   | The application can't be used until it is enabled. |

### Creating example users and groups in PingOne

Create two example users and groups to use for testing the AVP policies. As configured, user Alice will have full permissions to the example API, whereas user Bob will have restricted permissions.

1. In the PingOne admin console, go to **Directory > Users** and click the **[icon: plus, set=fa]**icon.

2. For the first user, enter the following information:

   1. In the **Username** field, enter `alice`.

   2. In the **Population** list, select the population to which you want to add the user.

      |   |                                                                                                                                                                                                           |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | All users must belong to a population. If you don't have a population configured in your environment, you must create one. Learn more in [Managing populations](../directory/p1_manage_populations.html). |

   3. In the **Password** field, enter a password for the user.

   4. Click **Save**.

3. For the second user, enter the following information:

   1. In the **Username** field, enter `bob`.

   2. In the **Population** list, select the population to which you want to add the user.

   3. In the **Password** field, enter a password for the user.

   4. Click **Save**.

4. Go to **Directory > Groups** and click the **[icon: plus, set=fa]**icon.

5. For the first group, enter the following information:

   1. In the **Group Name** field, enter `AVP_Admin`.

   2. Click **Save**.

   3. On the **Groups** page, locate the **AVP\_Admin** group and click it to open the details panel.

   4. On the **Users** tab, click **Add Individually**.

   5. In the **All Users** list, select the checkbox next to **alice** and click **Save**.

6. For the second group, enter the following information:

   1. In the **Group Name** field, enter `AVP_User`.

   2. Click **Save**.

   3. On the **Groups** page, locate the **AVP\_User** group and click it to open the details panel.

   4. On the **Users** tab, click **Add Individually**.

   5. In the **All Users** list, select the checkbox next to **bob** and click **Save**.

### Creating an example API in AWS

Now you'll create an example API to secure with AVP.

1. Sign on to the [AWS Management Console](https://console.aws.amazon.com/).

2. Go to **API Gateway**.

   |   |                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If **API Gateway** is not listed in your console, use the search bar to find it. Learn more about API Gateway in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html). |

3. Click **Create API**.

4. Scroll to **REST API** and click **Build**.

5. Select **Example API**, and then click **Create API**.

   ![A screen capture of the Create REST API page.](_images/p1-use-case-avp-api-create.png)

   #### Result

   A message displays that states the API creation was successful.

6. Click **Deploy API**.

7. On the **Deploy API** modal, from **Stage**, select **\*New Stage**\*.

8. In the **Stage name** field, enter `prod`.

9. Click **Deploy**.

   ![A screen capture showing the Deploy API modal with Stage and Stage name completed.](_images/p1-use-case-avp-deploy-api.png)

#### Next Steps

View details about your API in the AWS Management Console by going to **API Gateway > APIs**.

![A screen capture of your API listed in the AWS console.](_images/p1-use-case-avp-api-in-api-gateway.png)

### Creating an Amazon Verified Permissions policy store

Next you'll create an AVP policy store and configure it to protect your API.

1. In the [AWS Management Console](https://console.aws.amazon.com/), go to **Amazon Verified Permissions > Policy stores**.

   |   |                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If **Amazon Verified Permissions** isn't listed in your console, use the search bar to find it. Learn more in the [Amazon Verified Permissions User Guide](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html). |

2. Click **Create new policy store**.

3. In the **Starting options** section, select **Set up with API Gateway and an identity provider**.

4. Click **Next**.

5. On the **Import resources and actions** page, in the **API Gateway details** section, for **API**, select the API you created previously.

6. For **Deployment stage**, select **prod**.

   ![A screen capture of the Import resources and actions page showing the PetStore API and the prod deployment stage selected.](_images/p1-use-case-avp-api-gateway-details.png)

7. Click **Next**.

8. On the **Choose identity source** page, in the **Configure provider** section, select **External OIDC provider**.

9. In **OIDC provider details**, enter the **Issuer ID** URL you copied from the [**Overview** tab](#issuer-id) when you [created your OIDC application in PingOne](#create-oidc-app).

10. For **Token type**, select **Identity token**.

    |   |                                                                                                                                                                                                                                 |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | **Access token** will also work, but PingOne only includes the `group` claim in identity tokens, not in access tokens. When making API calls, use the **Identity token** type to ensure the AVP policies are applied correctly. |

11. In **User and group token claims**, ensure that the values in **User claim name in token** and **Group claim name in token** match what you configured on [the **Attribute Mappings** tab](#attribute-mappings) when you [created your OIDC application in PingOne](#create-oidc-app).

    ![A screen capture of the Choose identiy source page with the selections form the previous steps.](_images/p1-use-case-avp-choose-identity-source.png)

12. Click **Next**.

13. In **Assign actions to groups**, in the **Group name** field, enter `AVP_Admin`.

14. In **Actions allowed**, click **Select All** to give users in this group full permissions to the API.

15. Click **+ Add more groups**.

16. In the **Group Name** field, enter `AVP_User`.

17. In **Actions allowed**, clear the checkbox next to **post/pets** to give users in this group restricted permissions to the API.

    ![A screen capture of the Assign actions to groups page completed with the AVP\_Admin and AVP\_User groups as described in the previous steps.](_images/p1-use-case-avp-assign-actions-to-groups.png)

18. Click **Next**.

19. On **Deploy app integration**, for **Start authorizing for API**, select **Now, automatically**.

20. Click **Create policy store**.

### Result

A message displays indicating that you successfully created the policy store. View details about your policy store in the AWS Management Console by going to **Amazon Verified Permissions > Policy Stores**.

![A screen capture of the policy stoe you created displayed in the AWS console.](_images/p1-use-case-avp-policy-store-in-console.png)

---

---
title: Setting up PingOne as the federated IdP for Microsoft Entra ID
description: Learn about configuring Microsoft Entra hybrid join to allow users to access Active Directory and Entra ID resources.
component: pingone
page_id: pingone:use_cases:p1_microsoft_entra_hybrid_join
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_microsoft_entra_hybrid_join.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2025
section_ids:
  goals: Goals
  p1-hybrid-join-what-to-do: What you'll do
---

# Setting up PingOne as the federated IdP for Microsoft Entra ID

As organizations expand their on-premise Active Directory (AD) infrastructure to the cloud with Microsoft Entra ID, you can configure PingOne as the federated identity provider (IdP) to fulfill two use cases:

* User authentication

  * When you set up PingOne as the federated IdP in Entra ID, users authenticate with PingOne when they attempt to use single sign-on (SSO) to access resources like Microsoft 365.

  * You can use Microsoft Entra Connect Sync to sync users from AD to Entra ID.

  * PingOne can authenticate users with the Kerberos or LDAP protocol.

* Hybrid join

  * Hybrid join simplifies device management and allows organizations to join devices to on-premise AD and the cloud with Entra ID.

  * You can use Entra Connect Sync to sync devices joined to the domain to Entra ID and make them eligible for hybrid join.

  * When you're ready to start the hybrid join process to join a device to Entra ID, PingOne as the federated IdP enables the process by authenticating the device using the Kerberos protocol.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Device authentication using hybrid join is available as a limited access release for customers with a PingOne for Workforce Plus or Premium license in the North America (US) geography only and isn't covered under standard Support service level agreements (SLAs). You can open support cases for feedback, bug reports, configuration questions, or other inquiries related, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so response times might exceed the usual SLAs for your Support package.Topics for this feature are draft documentation for limited access purposes only and aren't complete or final. |

  > **Collapse: Hybrid join diagram**
  >
  > The following diagram shows the high-level process of setting up Entra hybrid join with PingOne as the federated IdP.
  >
  > ![A diagram of the Entra hybrid join process.](_images/p1_microsoft_entra_hybrid_join_diagram.png)
  >
  > 1. An administrator opens PowerShell and runs `dsregcmd /join` on the device.
  >
  > 2. The device sends a metadata request to PingOne using the WS-Trust 1.3 metadata exchange URL.
  >
  > 3. PingOne returns the requested metadata to the device.
  >
  > 4. The device processes the metadata and sends a request security token (RST) message with a Kerberos ticket for the device to PingOne.
  >
  > 5. PingOne validates the Kerberos ticket, creates an assertion, and returns the assertion in an RST response (RSTR) to the device.
  >
  > 6. The device sends a hybrid join request with the assertion from PingOne to Entra ID.
  >
  > 7. Entra ID processes the request, accepts it if the configuration is set up properly, and returns a response with a success message.
  >
  > 8. The device is hybrid joined to Entra ID.

## Goals

After completing this configuration, you'll know how to:

* Set up PingOne as the federated IdP for Entra ID.

* Use Entra Connect Sync to sync users and devices from an AD domain to an Entra ID verified custom domain.

* Enable users to authenticate with PingOne to access resources like Microsoft 365.

* Enable hybrid join on your organization's devices to sync them from AD to Entra ID.

## What you'll do

1. Complete the required [prerequisites](p1_microsoft_entra_hybrid_join_prerequisites.html).

2. **User authentication**: Connect users to sign on to Microsoft 365 with PingOne as the federated IdP:

   1. [Create an attribute in PingOne](p1_microsoft_hybrid_join_tasks.html#p1-create-attribute).

   2. [Add an LDAP gateway to connect PingOne with AD](p1_microsoft_hybrid_join_tasks.html#p1-add-ldap-gateway).

   3. [Add an authentication policy](p1_microsoft_hybrid_join_tasks.html#p1-add-auth-policy).

   4. [Add a Microsoft 365 application](p1_microsoft_hybrid_join_tasks.html#p1-add-microsoft-app).

   5. [Update the Microsoft 365 application](p1_microsoft_hybrid_join_tasks.html#p1-update-microsoft-app-user-auth).

   6. [Assign the authentication policy to the Microsoft 365 application](p1_microsoft_hybrid_join_tasks.html#p1-assign-policy-to-microsoft-app).

3. **Hybrid join**: Enable PingOne to process hybrid join requests from devices to sync devices from AD to Entra ID:

   1. [Create two attributes and a population in PingOne](p1_microsoft_hybrid_join_tasks.html#p1-create-attributes).

   2. [Enable Kerberos authentication](p1_microsoft_hybrid_join_tasks.html#p1-enable-kerberos).

   3. [Add a user type for hybrid joined devices](p1_microsoft_hybrid_join_tasks.html#p1-add-user-type).

   4. [Update the Microsoft 365 application](p1_microsoft_hybrid_join_tasks.html#p1-update-microsoft-app).

   5. [Update the federated IdP setting](p1_microsoft_hybrid_join_tasks.html#p1-update-federated-idp).

   6. [Allow users to join their devices to Entra ID](p1_microsoft_hybrid_join_tasks.html#p1-allow-join-devices).

   7. [Configure Entra Connect Sync to sync devices and verify the service connection point (SCP)](p1_microsoft_hybrid_join_tasks.html#p1-configure-entra-connect).

   8. [(Optional) Disable fallback sync in Windows](p1_microsoft_hybrid_join_tasks.html#p1-disable-fallback-sync).

---

---
title: Setting up PingOne SSO and PingID as the external MFA provider for Microsoft Entra ID
description: Learn how to set up Entra ID, PingOne SSO, and PingID to support an external authentication method in Microsoft Entra ID.
component: pingone
page_id: pingone:use_cases:p1_set_up_external_mfa_provider_microsoft_entra_use_case
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_set_up_external_mfa_provider_microsoft_entra_use_case.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2025
page_aliases: ["strong_authentication_mfa:p1_set_up_external_mfa_provider_microsoft_entra_use_case.adoc"]
section_ids:
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  new_pingid_account: "New PingID accounts: Creating a population for Entra ID users"
  steps: Steps
  existing_pingid_account: "Existing PingID accounts: Creating a population for Microsoft Entra ID users and changing the default population"
  steps-2: Steps
  result: Result
  registering-your-application-with-microsoft: Registering your application with Microsoft
  before-you-begin-2: Before you begin
  steps-3: Steps
  enabling-the-implicit-grant: Enabling the implicit grant
  steps-4: Steps
  getting-the-client-id-and-client-secret-for-your-application-and-the-tenant-id-of-your-entra-tenant: Getting the client ID and client secret for your application and the tenant ID of your Entra tenant
  steps-5: Steps
  setting-up-api-permissions: Setting up API permissions
  steps-6: Steps
  add_microsoft_idp: Adding Microsoft as an identity provider in PingOne
  steps-7: Steps
  updating-the-population: Updating the population
  steps-8: Steps
  auth_policy_eam: Adding an authentication policy for Entra ID external authentication
  steps-9: Steps
  configuring-the-oidc-application: Configuring the OIDC application
  steps-10: Steps
  creating-external-mfa-in-microsoft-entra: Creating external MFA in Microsoft Entra
  steps-11: Steps
  result-2: Result:
  creating-a-conditional-access-policy-in-microsoft-entra: Creating a conditional access policy in Microsoft Entra
  steps-12: Steps
  configuring-pingid-as-the-external-mfa: Configuring PingID as the external MFA
  steps-13: Steps
  result-3: Result:
  adding-an-authentication-policy-for-oidc-authentication: Adding an authentication policy for OIDC authentication
  steps-14: Steps
  result-4: Result:
  adding-the-callback-url-to-the-entra-admin-center: Adding the callback URL to the Entra admin center
  steps-15: Steps
  result-5: Result
  assigning-the-oidc-authentication-policy-to-an-application-in-pingone: Assigning the OIDC authentication policy to an application in PingOne
  steps-16: Steps
  next-steps: Next steps
  validation: Validation
  result-6: Result:
  result-7: Result:
  result-8: Result:
  result-9: Result:
  result-10: Result:
  result-11: Result:
---

# Setting up PingOne SSO and PingID as the external MFA provider for Microsoft Entra ID

Microsoft Entra ID allows customers to use an external authentication provider for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* through Entra ID external MFA, formerly known as external authentication methods (EAMs). In this use case, you'll learn how to set up Entra ID, PingOne SSO, and PingID to support external MFA in Entra ID.

Set up external MFA in Entra ID if:

* Entra ID is the identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)*.

* The users reside in a [managed domain](https://learn.microsoft.com/en-us/entra/identity/users/domains-manage#add-custom-domain-names-to-your-microsoft-entra-organization) in Entra ID.

  Learn more in [Create and configure a managed domain](https://learn.microsoft.com/en-us/entra/identity/domain-services/tutorial-create-instance) in the Entra ID documentation.

* PingOne is the external authentication provider.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you [added a Microsoft 365 application to PingOne using the application catalog](../applications/p1_adding_microsoft_365.html) and completed the PowerShell cmdlets to set up PingOne as the federated IdP for the domain in Entra ID, external MFA isn't required for MFA. Instead, you can [add an MFA claim in the Microsoft 365 application](../applications/p1_configure_authentication_claim_microsoft_365.html) to communicate to Entra ID that PingOne will handle MFA. Learn more in [Using WS-Fed or SAML 1.1 federated IdP](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-expected-inbound-assertions#using-ws-fed-or-saml-11-federated-idp) in the Entra ID documentation. |

The high-level process of signing on with external MFA works as follows, with PingOne and PingID acting as the external authentication provider:

1. A user opens an application protected by Entra ID and is prompted to complete first-factor MFA in Entra ID.

2. Entra ID determines that another factor needs to be satisfied, such as if a conditional access policy requires MFA.

3. The user chooses the applicable external MFA as second-factor MFA.

4. Entra ID sends an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)* authentication request to PingOne (the external authentication provider in this use case).

5. PingOne initiates MFA for the user.

6. The user completes the MFA requirement using the PingID app.

7. PingOne returns an ID token to Entra ID in the authentication response.

8. Entra ID validates the ID token and signs the users on to the application.

Learn more about external MFA in [Use Microsoft Entra MFA with an external MFA provider](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-external-method-provider) in the Entra ID documentation.

## Goals

After completing this use case, you'll know how to:

* Configure Entra ID to support external MFA.

* Add Entra ID as an external IdP in PingOne.

* Set up PingID as the MFA solution for Entra ID users.

## What you'll do

In Entra ID, you'll configure three components:

1. Add and configure an application.

2. Create external MFA.

3. Add a conditional access policy.

In PingOne, you'll configure the following:

1. Create a population for Entra ID users.

2. Create a Microsoft IdP connection.

3. Add an authentication policy and OIDC application to handle external authentication requests from Entra ID.

4. Add a second authentication policy to redirect users to Entra ID for OIDC authentication.

The last step is configuring PingID as external MFA for Entra ID.

## Before you begin

To set up this use case, you'll need:

* A PingOne organization. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* A PingOne environment with the PingOne SSO and PingID services added.

  Create a new environment as follows, depending on whether you're already using PingID:

  * If you aren't using PingID already or if you want to create a new PingID account, [create a new PingID environment in PingOne](../strong_authentication_mfa/p1_create_environment_strong_authentication_start.html).

  * If you're using PingID currently and want to use your existing PingID account, [integrate a PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html). You should also follow these steps if you've previously integrated PingID with Entra ID using custom controls. Learn more about integrating PingID with Entra ID in the [PingID documentation](https://docs.pingidentity.com/pingid/pingid_integrations/pid_integrate_with_azure_ad.html).

* An Entra account with an active subscription and an Entra tenant.

## Tasks

### New PingID accounts: Creating a population for Entra ID users

If you created a new PingID environment in PingOne, your new environment includes a population named **Default**. Learn more in [Setting up an environment for strong authentication (MFA)](../strong_authentication_mfa/p1_create_environment_strong_authentication_start.html).

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you [integrated an existing PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html), skip to [Existing PingID accounts: Creating a population for Entra ID users and changing the default population](#existing_pingid_account). |

![A screen capture of the Populations page with one Default environment.](_images/p1_pingid_env_default_population.png)

When you configure external MFA for Entra ID, you'll need to create a new population in PingOne for users coming from Entra ID.

## Steps

1. In the PingOne admin console, go to **Directory > Populations**.

2. Click the **[icon: plus, set=fa]**icon to add a new population.

3. Enter the following:

   1. **Population Name**: A unique label for the population, such as `Entra ID users`.

   2. **Description** (optional): A brief description of the population.

   3. **Default Population** (optional): Don't select this checkbox in this scenario unless you want to specify this population as the new default population.

4. Click **Save**.

   ![A screen capture of the Populations page with a Default and Entra ID population.](_images/p1_population_entra_eam.png)

### Existing PingID accounts: Creating a population for Microsoft Entra ID users and changing the default population

If you [integrated your PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html), your new environment includes a population named **Default** with users from PingID assigned to this population. The following image shows the **Default** population with two users from PingID.

|   |                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you [created a new PingID environment in PingOne](../strong_authentication_mfa/p1_create_environment_strong_authentication_start.html), follow the steps in [New PingID accounts: Creating a population for Entra ID users](#new_pingid_account). |

![A screen capture of the Populations page with one Default environment that has two identities.](_images/p1_existing_pingid_env_default_population.png)

By default, the **Identity Provider** for this population is set to **PingOne**. You'll update this setting as part of this process.

![A screen capture of the Populations page with the Default population selected and the details panel showing.](_images/p1_existing_pingid_identity_provider.png)

Because you could have a future scenario where users in this environment aren't coming from Entra ID, you should rename the **Default** population, create a new population for users coming from Entra ID, and set the new population as the default population.

## Steps

1. In the PingOne admin console, go to **Directory > Populations**.

2. Click the **Default** population, and then click the **Pencil** icon ([icon: pencil, set=fa]) to edit the population.

3. Change **Population Name** from **Default** to a new name, such as `Entra ID users`.

   ![A screen capture of the Edit Population panel with the Population Name changed to Entra ID users.](_images/p1_existing_pingid_change_population_name.png)

4. Click **Save**.

5. To create a new population, click the **[icon: plus, set=fa]**icon.

6. Enter the following:

   1. **Population Name**: A unique label for the population, such as `Home`.

   2. **Description** (optional): A brief description of the population.

   3. **Default Population**: Select the **Enable** checkbox to set this population as the new default population.

   4. In the confirmation modal, click **Confirm** to make this population the new default population.

      ![A screen capture of the New Population with the Make Default Population confirmation message showing.](_images/p1_existing_pingid_new_default_population.png)

7. Click **Save**.

## Result

You now have two populations in your environment:

1. **Entra ID users**: Users from PingID are assigned to this population. This is also the population where future Entra ID users will be assigned when Entra ID redirects users to PingOne for MFA. Previously, this population was named **Default** and was set as the default population.

2. **Home**: This population is the new default population and was created for future scenarios where users aren't coming from Entra ID.

![A screen capture of the Populations page with two populations: Entra ID users and Home.](_images/p1_existing_pingid_two_populations.png)

### Registering your application with Microsoft

To configure external MFA, register an application in Microsoft Entra. Learn more in [Quickstart to registering an app](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) in the Microsoft Entra documentation.

#### Before you begin

Ensure that you have:

* A Microsoft Entra account with an active subscription

* An Entra tenant

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/) and sign on to your account.

   If you don't have a Microsoft Entra account, you can create one now.

2. In the sidebar, go to **Identity > Applications > App registrations**.

3. Click **[icon: plus, set=fa]New registration**.

   ![A screenshot of the App registrations page in the Entra admin center.](_images/p1-entra-eam-new-app-registration.png)

4. Enter and configure the following:

   1. **Name**: Enter a user-facing display name for the application.

   2. **Supported account types**: Select either of the following, depending on the needs of your organization:

      * **Accounts in this organizational directory only (\<Your Entra tenant name> only - Single tenant)**: Select this option if you're working with only identities from your environment.

      * **Accounts in any organizational directory and personal Microsoft accounts**

   3. **Redirect URI**: Select **Web** as the platform and enter the authorization URL of your PingOne environment.

      |   |                                                                                                                                           |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can find this URL on the **Overview** tab of any OIDC application in the PingOne admin console in the **Connection Details** section. |

      The format is `<issuer>/authorize`.

      Example 1: `https://auth.pingone.<region>/<envID>/as/authorize`

      Example 2: `https://<customDomain>/as/authorize` if you set up a custom domain. Learn more in [Setting up a custom domain](../settings/p1_set_up_custom_domain.html).

      ![A screenshot of the Register an application page in the Entra admin center.](_images/p1-entra-eam-register-app.png)

5. Click **Register**.

### Enabling the implicit grant

After registering the application in Entra, enable the implicit grant type for your application to support external MFA.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Identity > Applications > App registrations** and click your application.

3. On the **App registrations** page, in the **Manage** section, click **Authentication**.

4. In the **Implicit grant and hybrid flows** section, select the **ID tokens** checkbox for the token type to be issued by the authorization endpoint.

   ![A screenshot of the Authentication page for the application in the Entra admin center.](_images/p1-entra-eam-implicit-grant.png)

5. Click **Save**.

### Getting the client ID and client secret for your application and the tenant ID of your Entra tenant

When you register your application with Microsoft, Microsoft generates an application (client) ID and application secret for the application.

Microsoft also generates a directory (tenant) ID for each Entra tenant. You'll copy these values and enter them into PingOne.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Identity > Applications > App registrations** and click your application.

3. On the **App registrations** page, in the **Manage** section, click **Certificates & secrets**.

4. On the **Client secrets** tab, click **[icon: plus, set=fa]New client secret**.

5. Enter the following:

   1. **Description**: A brief description of the client secret.

   2. **Expires**: Select the duration of the certificate based on the needs of your organization.

6. Click **Add**.

7. On the **Client secrets** tab, click the **Copy** icon ([icon: copy, set=fa]) for the **Value** and paste it in a secure location.

   ![A screenshot of the Certificates & secrets page in the Entra admin center.](_images/p1-entra-eam-certificate-secrets.png)

8. In the **App registrations** sidebar, click **Overview**.

   ![A screenshot of the Certificates & secrets page in the Entra admin center.](_images/p1-entra-eam-certificates-secrets-overview.png)

9. Copy the **Application (client) ID** and paste it in a secure location.

   ![A screenshot of the Application Overview page - Application ID in the Entra admin center.](_images/p1-entra-eam-application-id.png)

10. Copy the **Directory (tenant) ID** and paste it in a secure location.

    ![A screenshot of the Application Overview page - Directory ID in the Entra admin center.](_images/p1-entra-eam-directory-id.png)

### Setting up API permissions

Using external MFA with Microsoft Entra requires certain API permissions that you'll need to enable in your application.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Identity > Applications > App registrations** and click your application.

3. On the **App registrations** page, in the **Manage** section, click **API permissions**.

4. Click **[icon: plus, set=fa]Add a permission**.

   ![A screenshot of the API permissions page in the Entra admin center.](_images/p1-entra-eam-api-permissions-default.png)

5. On the **Request API permissions** panel, click **Microsoft Graph**.

   ![A screenshot of the Request API permissions panel in the Entra admin center.](_images/p1-entra-eam-api-permissions-microsoft-graph.png)

6. Click **Delegated permissions** for the type of permissions to allow for your application.

   ![A screenshot of the Request API permissions panel - Type of permissions in the Entra admin center.](_images/p1-entra-eam-api-permissions-delegated-permissions.png)

7. Expand **Openid permissions**.

8. Select the `openid` and `profile` permissions.

   |   |                                                                |
   | - | -------------------------------------------------------------- |
   |   | `User.Read` is included by default and should remain selected. |

   ![A screenshot of the Request API permissions page - Openid permissions in the Entra admin center.](_images/p1-entra-eam-api-permissions-openid-profile.png)

9. In the **Application permissions** section, expand **User** and select the `User.Read.All` permission.

   |   |                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you don't intend to retrieve many attributes from Entra ID and populate them into PingOne, you can select the `User.ReadBasic.All` permission instead of the `User.Read.All` permission.Both of these permissions require admin consent. |

10. To grant admin consent, click **Add permissions**.

11. Click **Grant admin consent for \<your Entra tenant>**.

    ![A screenshot of the API permissions page in the Entra admin center showing how to grant admin consent.](_images/p1-entra-eam-api-permissions-granted.png)

### Adding Microsoft as an identity provider in PingOne

Configure the IdP connection in PingOne.

#### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click the **[icon: plus, set=fa]**icon.

2. Click **Microsoft** as the **Identity Provider Type**.

3. Click **Next**.

4. In the **Create Profile** step, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: Select a population that overrides the authentication policy's registration population and enables just-in-time (JIT) registration from the IdP.

     |   |                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on button**, in accordance with the provider's brand standards. |

5. Click **Next**.

6. In the **Connection Details** step, enter the following information:

   * **Client ID**: The application ID from the Microsoft Entra admin center that you copied earlier. You can find this information on the Microsoft Entra admin center.

   * **Client secret**: The application secret from the Microsoft Entra admin center that you copied earlier. You can find this information on the Microsoft Entra admin center.

   * **Tenant ID**: The tenant ID of your Entra tenant from the Microsoft Entra admin center that you copied earlier. You can find this information on the Microsoft Entra admin center.

   * **Callback URL**: Copy the **Callback URL** and paste it in a secure location. You'll add this value in the Microsoft Entra admin center later.

7. Click **Next**.

8. Define how the PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Leave the default PingOne user profile attributes and the external IdP attributes:

     * **Preferred Username** (from Microsoft) as the source of the PingOne **Username**

     * **Email** (from Microsoft) as the source of the PingOne **Email Address**

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon ([icon: gear, set=fa]). Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html) and [Using expressions to retrieve Microsoft Entra attributes](../pingone_expression_language/p1_expressionlang_expressions_concatenation.html#p1-expressions-microsoft).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

9. Click **Save**.

10. Click the connection in the **External IdPs** list to expand the connection details.

11. On the **Profile** tab, click [icon: pencil, set=fa].

12. For **Population**, select the population that you previously created for Entra ID users.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | * If you [created a new PingID environment in PingOne](../strong_authentication_mfa/p1_create_environment_strong_authentication_start.html), use the population that you created in [New PingID accounts: Creating a population for Entra ID users](#new_pingid_account).

    * If you [integrated your PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html), use the population that you created in [Existing PingID accounts: Creating a population for Entra ID users and changing the default population](#existing_pingid_account). |

13. Click **Save**.

14. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

    ![A screen capture of the Microsoft Identity Provider connection with the Entra ID users population selected.](_images/p1_microsoft_entra_registration_population.png)

### Updating the population

After creating your connection to Microsoft, update the **Identity Provider** setting for the population that you created for users coming from Entra ID.

The **Identity Provider** setting is used as the runtime fallback IdP for users in the population who don't have an authoritative IdP configured in their user profile. Updating the population is especially important if you [integrated your PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html) because those user profiles are created in PingOne without an authoritative IdP set. If the user is removed from the population, the IdP set in the population no longer applies to them.

#### Steps

1. In the PingOne admin console, go to **Directory > Populations** and click the population that you previously created for Entra ID users.

2. On the **Overview** tab, click [icon: pencil, set=fa].

3. In the **Identity Provider** list, select the IdP that you previously created in [Adding Microsoft as an identity provider in PingOne](#add_microsoft_idp).

4. In the **Confirm Changes** modal, click **Confirm**.

5. Click **Save**.

### Adding an authentication policy for Entra ID external authentication

Add the Microsoft IdP to an authentication policy followed by an MFA step.

#### Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add policy** and enter a name for the policy.

3. For the first step:

   1. In the **Step Type** list, select **External Identity Provider**.

   2. In the **External Identity Provider** list, select your Microsoft IdP.

   3. For **Policy Purpose**, select the **Entra ID External Authentication Method** option.

4. Click **[icon: plus, set=fa]Add step**.

5. For the second step, in the **Step Type** list, select **PingID Authentication**.

   ![A screen capture of an authentication policy with External IDP as the first step and PingID Authentication as the second step.](_images/p1_pingid_authentication_policy.png)

6. Click **Save**.

### Configuring the OIDC application

Configure an OIDC application to handle authentication requests from Microsoft Entra ID.

## Steps

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon to add an application.

3. On the **Add Application** panel, enter and choose the following:

   1. **Application Name**: A unique identifier for the application.

   2. **Description** (optional): A brief description of the application.

   3. **Icon** (optional): A graphic representation of the application. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

   4. **Application Type**: Choose **OIDC Web App**.

   5. Click **Save**.

4. On the **Configuration** tab, click [icon: pencil, set=fa]and enter or edit the following:

   1. **Response Type**: Clear the default **Code** checkbox and select **ID Token**.

   2. **Grant Type**: Clear the default **Authorization Code** checkbox and select **Implicit** checkbox.

   3. **Redirect URIs**: Enter `https://login.microsoftonline.com/common/federation/externalauthprovider`.

   4. Click **Save**.

5. On the **Policies** tab, click **[icon: plus, set=fa]Add Policies**.

6. On the **PingOne Policies** tab, select the authentication policy that you created to handle external authentication requests from Entra ID.

7. Click **Save**.

8. To enable the application, click the toggle at the top of the details panel to the right (blue).

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | You can disable the application by clicking the toggle to the left (gray). |

9. Click the application entry to open the details panel.

10. On the **Overview** tab, copy the following PingOne application details to add in the Microsoft Entra admin center:

    * In the **General** section, copy the **Client ID** and paste it in a secure location.

    * In the **Connection Details** section, copy the **OIDC Discovery Endpoint** and paste it in a secure location.

### Creating external MFA in Microsoft Entra

After creating the OIDC application in PingOne and copying the application ID, OIDC discovery endpoint, and client ID, create external MFA in Microsoft Entra.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Protection > Authentication methods > Policies**.

3. Click **Add External MFA**.

4. Enter the following:

   1. **Name**: Enter a name for the external MFA.

   2. **Client ID**: Enter your PingOne application's client ID that you copied earlier.

   3. **Discovery Endpoint**: Enter the **OIDC Discovery Endpoint** that you copied earlier from PingOne. The format is `<issuer>/.well-known/openid-configuration`.

   4. **App ID**: Enter the Microsoft Entra application ID that you copied previously. You can find the application ID in the [Microsoft Entra admin center](https://entra.microsoft.com/).

5. Click **Request permission**.

   ![A screenshot of the External MFA configuration page in the Entra admin center.](_images/p1-entra-eam-add-external-method-request-permission.png)

   ##### Result:

   The browser opens a new window for you to sign on with your Microsoft Entra admin credentials.

6. Review the requested permissions and click **Accept** if you agree.

7. In the **Enable and target** section, configure whether you want to include a subset of your users or all users.

8. Click the **Enable** toggle to enable the external MFA.

   ![A screenshot of the External MFA configuration page in the Entra admin center.](_images/p1-entra-eam-add-external-method-enable.png)

### Creating a conditional access policy in Microsoft Entra

Configure a conditional access policy in Microsoft Entra to define authentication requirements for users accessing applications.

|   |                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your Microsoft Entra tenant contains other conditional access policies that use custom controls to initiate MFA, ensure those policies don't apply to the same users, groups, and applications that you select in this conditional access policy. Otherwise, your users could be prompted multiple times for MFA. |

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Protection > Conditional Access > Policies**.

3. Click **[icon: plus, set=fa]Create new policy** or update an existing policy.

4. Configure the following:

   1. **Name**: Enter a name for the policy.

   2. **Users**: Select the same users and groups that you selected in your external MFA.

   3. **Target resources**: Select the applications to which you want to apply this conditional access policy.

   4. **Grant**:

      1. Click **Grant access**.

      2. Select the **Require multifactor authentication** checkbox.

         ![A screenshot of Conditional Access Policy - Grant access modal in the Entra admin center.](_images/p1-entra-eam-conditional-access-policy-grant.png)

      3. Click **Select**.

   5. **Enable policy**: Select **On** to turn on the policy.

5. Click **Save**.

### Configuring PingID as the external MFA

Configure a PingID policy to process user MFA requests coming from the PingOne application that you created to handle Microsoft Entra requests.

#### Steps

1. In the PingID admin portal, go to **Setup > PingID** and click the **Configuration** tab.

   |   |                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you selected **Enable** for **Enforce Policy**, you might need to create an additional PingID policy. Learn more in the next step. |

2. Click the **Policy** tab, and on the **Web** tab, expand and review each policy.

   |   |                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Microsoft Entra ID doesn't allow MFA bypasses from external MFA and requires always prompting the user to complete MFA. If you have a policy that can apply to all applications and that has a rule with an action of **Approve**, you must create a new policy for the PingOne application. Examples of such policies include Recent Authentication or Accessing from Company Network. |

   ![A screen capture of a PingID policy that has a rule with an action of Approve for Recent Authentication.](_images/pingid_microsoft_entra_eam.png)

   1. To add a new policy, click **Add Policy**.

   2. Enter a name for the policy, such as `External MFA PingID policy`.

   3. In the **Target** section, in the **Applications** list, select the PingOne application that you previously created.

   4. For **Groups**, select all applicable groups.

   5. (Optional) In the **Allowed Methods** section, select the authentication methods you want to allow.

      ![A screen capture of a new PingID policy with the PingOne Entra application selected.](_images/pingid_policy_eam.png)

   6. Click **Save**.

      #### Result:

      The new policy becomes the first PingID policy, which works as Microsoft Entra ID external MFA. PingID will use this new policy when processing MFA requests coming from the PingOne application that you created to handle Microsoft Entra ID requests.

3. In a scenario where a user forgot or lost their mobile phone and can't use the PingID app for MFA, you can allow a user to bypass MFA with PingID for a specificed period of time, such as 8 hours.

   1. In the PingOne admin console, go to **Directory > Users**.

   2. Browse or search for the applicable user and click the user entry to open the details panel.

   3. In the list for the **Services** tab, select **Authentication**.

   4. Scroll down to the **Integrations** section, click the **More Options** icon, and select **Bypass**.

   5. In the **Bypass** window, select the desired amount of time from the **Allow bypass of PingID authentication on SSO for** list and click **Bypass**.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                        |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Because Microsoft Entra ID requires the third-party MFA provider to specify the MFA method used and doesn't accept MFA bypasses as an acceptable MFA method, you must also configure bypass in the Microsoft Entra admin center. Learn more about configuring conditional access in the [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview). |

### Adding an authentication policy for OIDC authentication

If you want to allow users to sign on to the **PingOne Self-Service - MyAccount** application to manage their MFA methods or to other applications you've added to PingOne, you must create an authentication policy for OIDC authentication using the same Microsoft IdP connection.

#### Steps

1. In the PingOne admin console, go to **Authentication > Authentication**.

2. Click **[icon: plus, set=fa]Add policy** and enter a name for the policy.

3. For the first step:

   1. In the **Step Type** list, select **External Identity Provider**.

   2. In the **External Identity Provider** list, select your Microsoft IdP. This is the same Microsoft IdP you selected in [Adding an authentication policy for Entra ID external authentication](#auth_policy_eam).

   3. For **Policy Purpose**, select the **OIDC Authentication** option.

4. (Optional) To prompt users for MFA, click **[icon: plus, set=fa]Add step** and select **PingID Authentication** in the **Step Type** list for the second step.

   ![A screen capture of a PingOne authentication policy with External IdP as the first step and PingID Authentication as the second step.](_images/p1_microsoft_entra_oidc_auth_policy.png)

5. Click **Save**.

#### Result:

You now have two authentication policies:

* An authentication policy for users authenticating with PingOne as external MFA for Entra ID

* An authentication policy for OIDC authentication to allow users to sign on to other applications

![A screen capture of the PingOne Authentication Policies list with two policies: Entra\_ID\_EAM\_Policy and Entra\_ID\_OIDC\_Auth\_Policy.](_images/p1_microsoft_eam_two_auth_policies.png)

### Adding the callback URL to the Entra admin center

If you created an authentication policy for OIDC authentication, you must also add the callback URL from the Microsoft IdP connection in PingOne to the application you registered in the Microsoft Entra admin center.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Identity > Applications > App registrations** and click your application.

3. On the **App registrations** page, in the **Manage** section, click **Authentication**.

4. In the **Platform configurations > Web > Redirect URIs** section, click **Add URI**.

   ![A screenshot of the Authentication page - Redirect URIs in the Entra admin center.](_images/p1-entra-eam-redirect-uris.png)

5. Paste the **Callback URL** that you copied from the PingOne admin console.

   The following examples show the URL format:

   Example 1: `https://auth.pingone.<region>/<envID>/rp/callback/microsoft`

   Example 2: `https://<customDomain>/rp/callback/microsoft`

6. Click **Save**.

#### Result

The **Redirect URIs** section displays both URLs you've added:

1. Authorization URL

2. Callback URL

![A screen capture of the Entra ID Authentication page with two redirect URIs identified with a red number callouts.](_images/p1_microsoft_entra_redirect_uris.png)

### Assigning the OIDC authentication policy to an application in PingOne

After you create an authentication policy for OIDC authentication and add the callback URL to the application in Entra ID, assign the OIDC authentication policy to applicable applications in PingOne, such as the **PingOne Self-Service - MyAccount** application or other applications you've added.

#### Steps

1. In the PingOne admin console, go to **Applications > Applications** and click the relevant application to open the details panel.

2. On the **Policies** tab, click **[icon: plus, set=fa]Add policies**.

3. On the **PingOne Policies** tab, select the OIDC authentication policy.

4. Click **Save**.

![A screen capture of the PingOne Applications page with the PingOne Self-Service - MyAccount app selected and the Policies tab showing an added policy named Entra\_ID\_OIDC\_Auth\_Policy.](_images/p1_selfservice_app_microsoft_entra_auth_policy.png)

#### Next steps

Repeat these steps for any other applications to which you want users to be able to sign on, for example **Another App** in the following screenshot.

![A screen capture of the PingOne Applications page with an example application called Another App selected and the Policies tab showing an added policy named Entra\_ID\_OIDC\_Auth\_Policy.](_images/p1_microsoft_entra_another_app_policy.png)

## Validation

Now that you've set up external MFA in Entra ID and configured PingOne and PingID as the external MFA provider, you're ready to validate that your Entra ID users can use PingID to complete MFA.

1. Open a new browser window in incognito mode.

2. In the [Entra admin center](https://entra.microsoft.com/), locate the application you added to the conditional access policy that requires MFA and click the URL for the application.

   In this example, **My Apps** at https\://myapps.microsoft.com.

3. Sign on to the application and complete the first-factor authentication at Microsoft using a test user's credentials.

   ### Result:

   Entra ID prompts the user to complete MFA action based on what Entra thinks is the most secure method if:

   * You, as an Entra ID admin, have activated system-preferred MFA and included the test user as the target user.

   * The test user has installed and successfully used the system-preferred MFA method.

   In this example, the test user has installed and used both Microsoft Authenticator and verification code by text message, so Entra ID prompts the user to enter the code from Microsoft Authenticator.

   ![A screen capture of the Microsoft Enter code page.](_images/p1_microsoft_enter_code.png)

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you haven't activated system-preferred MFA, the user won't see the **Enter code** modal and is prompted to verify their identity. |

4. To use your external MFA, click **Sign in another way** at the bottom of the **Enter code** modal.

   ### Result:

   After selecting **Sign in another way** or if system-preferred MFA doesn't apply, Entra ID displays the **Verify your identity** modal.

   ![A screen capture of the Microsoft Enter code page.](_images/p1_microsoft_verify_identity.png)

5. Select the external MFA.

   ### Result:

   Entra ID redirects the browser to PingOne.

6. If the test user hasn't yet paired the PingID app, they're shown a **Welcome to PingID** page. Click **Start** to start the pairing process.

   ![A screen capture of the Welcome to PingID page and then the Add New Device page with a QR code and pairing key.](_images/p1_pingid_add_device.png)

   ### Result:

   After pairing, the PingID app prompts the user to complete the MFA requirement.

7. After PingID is paired for the test user, complete the MFA prompt from the PingID app.

   ### Result:

   PingOne returns an ID token to Entra ID, and Entra ID processes the ID token and signs the test user on to the application.

8. Sign off of the application.

9. In the [Entra admin center](https://entra.microsoft.com/), locate the same application and authenticate to the application again as the test user.

   ### Result:

   This time, PingID shouldn't prompt the test user to pair a device. Instead, the PingID app should prompt the test user to complete the MFA requirement.

   When the test user completes the MFA requirement, PingOne returns an ID token to Entra ID, and Entra ID processes the ID token and signs the test user on to the application.

   ![A screen capture of the Microsoft Apps dashboard.](_images/p1_microsoft_my_apps.png)

---

---
title: Setting up PingOne SSO, DaVinci, and PingID as the external MFA provider for Microsoft Entra ID
description: Learn how to set up Entra ID, PingOne SSO, DaVinci, and PingID to support external MFA in Microsoft Entra ID.
component: pingone
page_id: pingone:use_cases:p1_set_up_external_mfa_provider_microsoft_entra_davinci
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_set_up_external_mfa_provider_microsoft_entra_davinci.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  goals: Goals
  what-youll-do: What you'll do
  before-you-begin: Before you begin
  tasks: Tasks
  new_pingid_account_davinci: "New PingID accounts: Creating a population for Entra ID users"
  steps: Steps
  existing_pingid_account_davinci: "Existing PingID accounts: Creating a population for Entra ID users and changing the default population"
  steps-2: Steps
  result: Result
  registering-your-application-with-microsoft: Registering your application with Microsoft
  before-you-begin-2: Before you begin
  steps-3: Steps
  enabling-the-implicit-grant: Enabling the implicit grant
  steps-4: Steps
  getting-the-client-id-and-client-secret-for-your-application-and-the-tenant-id-of-your-entra-tenant: Getting the client ID and client secret for your application and the tenant ID of your Entra tenant
  steps-5: Steps
  setting-up-api-permissions: Setting up API permissions
  steps-6: Steps
  add_microsoft_idp_davinci: Adding Microsoft as an identity provider in PingOne
  steps-7: Steps
  updating-the-population: Updating the population
  steps-8: Steps
  add_davinci_flow: Adding a DaVinci flow and flow policy for Entra ID external authentication
  steps-9: Steps
  configuring-the-oidc-application: Configuring the OIDC application
  steps-10: Steps
  creating-external-mfa-in-microsoft-entra: Creating external MFA in Microsoft Entra
  steps-11: Steps
  result-2: Result:
  creating-a-conditional-access-policy-in-microsoft-entra: Creating a conditional access policy in Microsoft Entra
  steps-12: Steps
  configuring-pingid-as-the-external-mfa: Configuring PingID as the external MFA
  steps-13: Steps
  result-3: Result:
  davinci-flow-oidc: Adding a DaVinci flow and flow policy for OIDC authentication
  before-you-begin-3: Before you begin
  steps-14: Steps
  result-4: Result:
  adding-the-callback-url-to-the-entra-admin-center: Adding the callback URL to the Entra admin center
  steps-15: Steps
  result-5: Result
  assigning-the-davinci-oidc-flow-policy-to-an-application-in-pingone: Assigning the DaVinci OIDC flow policy to an application in PingOne
  steps-16: Steps
  next-steps: Next steps
  validation: Validation
  result-6: Result:
  result-7: Result:
  result-8: Result:
  result-9: Result:
  result-10: Result:
  result-11: Result:
---

# Setting up PingOne SSO, DaVinci, and PingID as the external MFA provider for Microsoft Entra ID

Microsoft Entra ID allows customers to use an external authentication provider for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* through Entra ID external MFA, formerly known as external authentication methods (EAMs). In this use case, you'll learn how to set up Entra ID, PingOne SSO, DaVinci, and PingID to support external MFA in Entra ID.

Set up external MFA in Entra ID if:

* Entra ID is the identity provider (IdP) *(tooltip: \<div class="paragraph">
  \<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
  \</div>)*.

* The users reside in a [managed domain](https://learn.microsoft.com/en-us/entra/identity/users/domains-manage#add-custom-domain-names-to-your-microsoft-entra-organization) in Entra ID.

  Learn more in [Create and configure a managed domain](https://learn.microsoft.com/en-us/entra/identity/domain-services/tutorial-create-instance) in the Entra ID documentation.

* PingOne is the external authentication provider.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you [added a Microsoft 365 application to PingOne using the application catalog](../applications/p1_adding_microsoft_365.html) and completed the PowerShell cmdlets to set up PingOne as the federated IdP for the domain in Entra ID, external MFA isn't required for MFA. Instead, you can [add an MFA claim in the Microsoft 365 application](../applications/p1_configure_authentication_claim_microsoft_365.html) to communicate to Entra ID that PingOne will handle MFA. Learn more in [Using WS-Fed or SAML 1.1 federated IdP](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-expected-inbound-assertions#using-ws-fed-or-saml-11-federated-idp) in the Entra ID documentation. |

The high-level process of signing on with external MFA works as follows, with PingOne and PingID acting as the external authentication provider:

1. A user opens an application protected by Entra ID and is prompted to complete first-factor MFA in Entra ID.

2. Entra ID determines that another factor needs to be satisfied, such as if a conditional access policy requires MFA.

3. The user chooses the applicable external MFA as second-factor MFA.

4. Entra ID sends an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
   \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
   \</div>)* authentication request to PingOne (the external authentication provider in this use case).

5. PingOne initiates MFA for the user.

6. The user completes the MFA requirement using the PingID app.

7. PingOne returns an ID token to Entra ID in the authentication response.

8. Entra ID validates the ID token and signs the users on to the application.

Learn more about external MFA in [Use Microsoft Entra MFA with an external MFA provider](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-external-method-provider) in the Entra ID documentation.

## Goals

After completing this use case, you'll know how to:

* Configure Entra ID to support external MFA.

* Add Entra ID as an external IdP in PingOne.

* Set up PingID as the MFA solution for Entra ID users.

## What you'll do

In Entra ID, you'll configure three components:

1. Add and configure an application.

2. Create external MFA.

3. Add a conditional access policy.

In PingOne, you'll configure the following:

1. Create a population for Entra ID users.

2. Create a Microsoft IdP connection.

In PingOne DaVinci, you'll configure two flows:

1. Add a flow to handle external authentication requests from Entra ID.

2. Add a second DaVinci flow to redirect users to Entra ID for OIDC authentication.

The last step is configuring PingID as the external MFA for Entra ID.

## Before you begin

To set up this use case, you'll need:

* A PingOne organization. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* A PingOne environment with the PingOne SSO, DaVinci, and PingID services added.

  Create a new environment as follows, depending on whether you're already using PingID:

  * If you aren't using PingID already or if you want to create a new PingID account, [create a new PingID environment in PingOne](../strong_authentication_mfa/p1_create_environment_strong_authentication_start.html).

  * If you're using PingID currently and want to use your existing PingID account, [integrate a PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html). You should also follow these steps if you've previously integrated PingID with Entra ID using custom controls. Learn more about integrating PingID with Entra ID in the [PingID documentation](https://docs.pingidentity.com/pingid/pingid_integrations/pid_integrate_with_azure_ad.html).

* An Entra account with an active subscription and an Entra tenant.

## Tasks

### New PingID accounts: Creating a population for Entra ID users

If you created a new PingID environment in PingOne, your new environment includes a population named **Default**. Learn more in [Setting up an environment for strong authentication (MFA)](../strong_authentication_mfa/p1_create_environment_strong_authentication_start.html).

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you [integrated an existing PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html), skip to [Existing PingID accounts: Creating a population for Entra ID users and changing the default population](#existing_pingid_account_davinci). |

![A screen capture of the Populations page with one Default environment.](_images/p1_pingid_env_default_population.png)

When you configure external MFA for Entra ID, you'll need to create a new population in PingOne for users coming from Entra ID.

## Steps

1. In the PingOne admin console, go to **Directory > Populations**.

2. Click the **[icon: plus, set=fa]**icon to add a new population.

3. Enter the following:

   1. **Population Name**: A unique label for the population, such as `Entra ID users`.

   2. **Description** (optional): A brief description of the population.

   3. **Default Population** (optional): Don't select this checkbox in this scenario unless you want to specify this population as the new default population.

4. Click **Save**.

   ![A screen capture of the Populations page with a Default and Entra ID population.](_images/p1_population_entra_eam.png)

### Existing PingID accounts: Creating a population for Entra ID users and changing the default population

If you [integrated your PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html), your new environment includes a population named **Default** with users from PingID assigned to this population. The following image shows the **Default** population with two users from PingID.

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you [created a new PingID environment in PingOne](../strong_authentication_mfa/p1_create_environment_strong_authentication_start.html), follow the steps in [New PingID accounts: Creating a population for Entra ID users](#new_pingid_account_davinci). |

![A screen capture of the Populations page with one Default environment that has two identities.](_images/p1_existing_pingid_env_default_population.png)

By default, the **Identity Provider** for this population is set to **PingOne**. You'll update this setting as part of this process.

![A screen capture of the Populations page with the Default population selected and the details panel showing.](_images/p1_existing_pingid_identity_provider.png)

Because you could have a future scenario where users in this environment aren't coming from Entra ID, you should rename the **Default** population, create a new population for users coming from Entra ID, and set the new population as the default population.

## Steps

1. In the PingOne admin console, go to **Directory > Populations**.

2. Click the **Default** population, and then click the **Pencil** icon ([icon: pencil, set=fa]) to edit the population.

3. Change **Population Name** from **Default** to a new name, such as `Entra ID users`.

   ![A screen capture of the Edit Population panel with the Population Name changed to Entra ID users.](_images/p1_existing_pingid_change_population_name.png)

4. Click **Save**.

5. To create a new population, click the **[icon: plus, set=fa]**icon.

6. Enter the following:

   1. **Population Name**: A unique label for the population, such as `Home`.

   2. **Description** (optional): A brief description of the population.

   3. **Default Population**: Select the **Enable** checkbox to set this population as the new default population.

   4. In the confirmation modal, click **Confirm** to make this population the new default population.

      ![A screen capture of the New Population with the Make Default Population confirmation message showing.](_images/p1_existing_pingid_new_default_population.png)

7. Click **Save**.

## Result

You now have two populations in your environment:

1. **Entra ID users**: Users from PingID are assigned to this population. This is also the population where future Entra ID users will be assigned when Entra ID redirects users to PingOne for MFA. Previously, this population was named **Default** and was set as the default population.

2. **Home**: This population is the new default population and was created for future scenarios where users aren't coming from Entra ID.

![A screen capture of the Populations page with two populations: Entra ID users and Home.](_images/p1_existing_pingid_two_populations.png)

### Registering your application with Microsoft

To configure external MFA, register an application in Microsoft Entra. Learn more in [Quickstart to registering an app](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) in the Microsoft Entra documentation.

#### Before you begin

Ensure that you have:

* A Microsoft Entra account with an active subscription

* An Entra tenant

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/) and sign on to your account.

   If you don't have a Microsoft Entra account, you can create one now.

2. In the sidebar, go to **Identity > Applications > App registrations**.

3. Click **[icon: plus, set=fa]New registration**.

   ![A screenshot of the App registrations page in the Entra admin center.](_images/p1-entra-eam-new-app-registration.png)

4. Enter and configure the following:

   1. **Name**: Enter a user-facing display name for the application.

   2. **Supported account types**: Select either of the following, depending on the needs of your organization:

      * **Accounts in this organizational directory only (\<Your Entra tenant name> only - Single tenant)**: Select this option if you're working with only identities from your environment.

      * **Accounts in any organizational directory and personal Microsoft accounts**

   3. **Redirect URI**: Select **Web** as the platform and enter the authorization URL of your PingOne environment.

      |   |                                                                                                                                           |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can find this URL on the **Overview** tab of any OIDC application in the PingOne admin console in the **Connection Details** section. |

      The format is `<issuer>/authorize`.

      Example 1: `https://auth.pingone.<region>/<envID>/as/authorize`

      Example 2: `https://<customDomain>/as/authorize` if you set up a custom domain. Learn more in [Setting up a custom domain](../settings/p1_set_up_custom_domain.html).

      ![A screenshot of the Register an application page in the Entra admin center.](_images/p1-entra-eam-register-app.png)

5. Click **Register**.

### Enabling the implicit grant

After registering the application in Entra, enable the implicit grant type for your application to support external MFA.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Identity > Applications > App registrations** and click your application.

3. On the **App registrations** page, in the **Manage** section, click **Authentication**.

4. In the **Implicit grant and hybrid flows** section, select the **ID tokens** checkbox for the token type to be issued by the authorization endpoint.

   ![A screenshot of the Authentication page for the application in the Entra admin center.](_images/p1-entra-eam-implicit-grant.png)

5. Click **Save**.

### Getting the client ID and client secret for your application and the tenant ID of your Entra tenant

When you register your application with Microsoft, Microsoft generates an application (client) ID and application secret for the application.

Microsoft also generates a directory (tenant) ID for each Entra tenant. You'll copy these values and enter them into PingOne.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Identity > Applications > App registrations** and click your application.

3. On the **App registrations** page, in the **Manage** section, click **Certificates & secrets**.

4. On the **Client secrets** tab, click **[icon: plus, set=fa]New client secret**.

5. Enter the following:

   1. **Description**: A brief description of the client secret.

   2. **Expires**: Select the duration of the certificate based on the needs of your organization.

6. Click **Add**.

7. On the **Client secrets** tab, click the **Copy** icon ([icon: copy, set=fa]) for the **Value** and paste it in a secure location.

   ![A screenshot of the Certificates & secrets page in the Entra admin center.](_images/p1-entra-eam-certificate-secrets.png)

8. In the **App registrations** sidebar, click **Overview**.

   ![A screenshot of the Certificates & secrets page in the Entra admin center.](_images/p1-entra-eam-certificates-secrets-overview.png)

9. Copy the **Application (client) ID** and paste it in a secure location.

   ![A screenshot of the Application Overview page - Application ID in the Entra admin center.](_images/p1-entra-eam-application-id.png)

10. Locate the **Directory (tenant) ID** and copy it to a secure location.

### Setting up API permissions

Using external MFA with Microsoft Entra requires certain API permissions that you'll need to enable in your application.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Identity > Applications > App registrations** and click your application.

3. On the **App registrations** page, in the **Manage** section, click **API permissions**.

4. Click **[icon: plus, set=fa]Add a permission**.

   ![A screenshot of the API permissions page in the Entra admin center.](_images/p1-entra-eam-api-permissions-default.png)

5. On the **Request API permissions** panel, click **Microsoft Graph**.

   ![A screenshot of the Request API permissions panel in the Entra admin center.](_images/p1-entra-eam-api-permissions-microsoft-graph.png)

6. Click **Delegated permissions** for the type of permissions to allow for your application.

   ![A screenshot of the Request API permissions panel - Type of permissions in the Entra admin center.](_images/p1-entra-eam-api-permissions-delegated-permissions.png)

7. Expand **Openid permissions**.

8. Select the `openid` and `profile` permissions.

   |   |                                                                |
   | - | -------------------------------------------------------------- |
   |   | `User.Read` is included by default and should remain selected. |

9. Click **Application permissions**, expand **User**, and select the `User.Read.All` permission.

   |   |                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you don't intend to retrieve many attributes from Entra ID and populate them into PingOne, you can select the `User.ReadBasic.All` permission instead of the `User.Read.All` permission.Both of these permissions require admin consent. |

10. To grant admin consent, click **Add permissions**.

11. Click **Grant admin consent for \<your Entra tenant>**.

### Adding Microsoft as an identity provider in PingOne

Configure the IdP connection in PingOne.

#### Steps

1. In the PingOne admin console, go to **Integrations > External IdPs** and click the **[icon: plus, set=fa]**icon.

2. Click **Microsoft** as the **Identity Provider Type**.

3. Click **Next**.

4. In the **Create Profile** step, enter the following information:

   * **Name**: A unique identifier for the IdP.

   * **Description** (optional): A brief description of the IdP.

   * **Population**: Select a population that overrides the authentication policy's registration population and enables just-in-time (JIT) registration from the IdP.

     |   |                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------- |
     |   | You can't change the **Icon** and **Sign-on button**, in accordance with the provider's brand standards. |

5. Click **Next**.

6. In the **Connection Details** step, enter the following information:

   * **Client ID**: The application ID from the Microsoft Entra admin center that you copied earlier. You can find this information on the Microsoft Entra admin center.

   * **Client secret**: The application secret from the Microsoft Entra admin center that you copied earlier. You can find this information on the Microsoft Entra admin center.

   * **Tenant ID**: The tenant ID of your Entra tenant from the Microsoft Entra admin center that you copied earlier. You can find this information on the Microsoft Entra admin center.

   * **Callback URL**: Copy the **Callback URL** and paste it in a secure location. You'll add this value in the Microsoft Entra admin center later.

7. Click **Next**.

8. Define how the PingOne user attributes are mapped to IdP attributes. Learn more in [Mapping attributes](../directory/p1_editsamlattributemapping.html).

   * Leave the default PingOne user profile attributes and the external IdP attributes:

     * **Preferred Username** (from Microsoft) as the source of the PingOne **Username**

     * **Email** (from Microsoft) as the source of the PingOne **Email Address**

   * To add an attribute, click **[icon: plus, set=fa]Add**.

   * To use the advanced expression builder, click the **Gear** icon ([icon: gear, set=fa]). Learn more in [Using the expression builder](../pingone_expression_language/p1_use_expression_builder.html) and [Using expressions to retrieve Microsoft Entra attributes](../pingone_expression_language/p1_expressionlang_expressions_concatenation.html#p1-expressions-microsoft).

   * Select the update condition, which determines how PingOne updates its user directory with the values from the IdP. The options are:

     * **Empty only**: Update the PingOne attribute only if the existing attribute is empty.

     * **Always**: Always update the PingOne directory attribute.

9. Click **Save**.

10. Click the connection in the **External IdPs** list to expand the connection details.

11. On the **Profile** tab, click [icon: pencil, set=fa].

12. For **Population**, select the population that you previously created for Entra ID users.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | * If you [created a new PingID environment in PingOne](../strong_authentication_mfa/p1_create_environment_strong_authentication_start.html), use the population that you created in [New PingID accounts: Creating a population for Entra ID users](#new_pingid_account_davinci).

    * If you [integrated your PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html), use the population that you created in [Existing PingID accounts: Creating a population for Entra ID users and changing the default population](#existing_pingid_account_davinci). |

13. Click **Save**.

14. To enable the IdP, click the toggle at the top of the details panel to the right (blue).

    |   |                                                                    |
    | - | ------------------------------------------------------------------ |
    |   | You can disable the IdP by clicking the toggle to the left (gray). |

![A screen capture of the Microsoft external IdP connection with the Entra ID users population selected.](_images/p1_microsoft_entra_registration_population.png)

### Updating the population

After creating your connection to Microsoft, update the **Identity Provider** setting for the population that you created for users coming from Entra ID.

The **Identity Provider** setting is used as the runtime fallback IdP for users in the population who don't have an authoritative IdP configured in their user profile. Updating the population is especially important if you [integrated your PingID account with a new PingOne account](../strong_authentication_mfa/p1_integrate_pid_env_with_new_p1_env_updated.html) because those user profiles are created in PingOne without an authoritative IdP set. If the user is removed from the population, the IdP set in the population no longer applies to them.

#### Steps

1. In the PingOne admin console, go to **Directory > Populations**.

2. Click the population that you previously created for Entra ID users and click [icon: pencil, set=fa].

3. In the **Identity Provider** list, select the IdP that you previously created in [Adding Microsoft as an identity provider in PingOne](#add_microsoft_idp_davinci).

4. Click **Confirm** in the modal, and then click **Save**.

### Adding a DaVinci flow and flow policy for Entra ID external authentication

Download and configure the DaVinci Entra ID external MFA sample flow to handle external authentication requests from Entra ID.

#### Steps

1. Download the [Entra ID External MFA & OIDC Authentication Reference Flow](https://marketplace.pingone.com/item/entra-id-eam-oidc-authentication-reference-flow) from the Ping Identity Marketplace and extract the contents of the `.zip` archive to a folder on your computer.

2. In DaVinci, on the **Flows** tab, click **[icon: plus, set=fa]Add Flow** and select **Import Flow**.

3. Upload the `entra-id-external-multifactor-authentication-reference-flow.json` file from the sample flow `.zip` file and click **Import**.

4. Configure the **Entra ID external MFA - Sign On with External Identity Provider** node:

   1. Click the node to open the configuration settings.

   2. On the **General** tab, in the **PingOne External Identity Provider** list, select the Microsoft IdP you created in [Adding Microsoft as an identity provider in PingOne](#add_microsoft_idp_davinci).

   3. Make sure the following default configurations are set:

      * **Policy Purpose** is set to **Entra ID External Authentication Method**.

      * **ID Token Hint** is set to `{{global.parameters.authorizationRequest.id_token_hint}}`.

      * The **Link with PingOne User** toggle is enabled (blue).

   4. In the **PingOne Population** list, select the applicable population.

      * For new PingID accounts, learn more in [New PingID accounts: Creating a population for Entra ID users](#new_pingid_account_davinci).

      * For existing PingID accounts, learn more in [Existing PingID accounts: Creating a population for Entra ID users and changing the default population](#existing_pingid_account_davinci).

        ![A screen capture of the PingOne Authentication - Sign On with External Identity Provider node configuration settings.](_images/p1_entra_eam_davinci_signon_node.png)

   5. Click **Apply**.

5. Review the default configuration settings for the **Mint Tokens - Return Success Response** node:

   1. Click the node to open the settings.

   2. On the **General** tab, make sure **User ID** is mapped to `id` from the **Entra ID External MFA - Sign On with External Identity Provider** node.

   3. Make sure **Custom Authentication Methods** is mapped to `entraIdAmr` from the **Map PingID AMR Value - Custom Function** node.

   4. Click **Apply**.

6. Add a DaVinci flow policy for the sample flow:

   1. Go to the **Applications** tab and click **[icon: plus, set=fa]Add Application**.

   2. In the **Name** field, enter a name for the application and click **Create**.

   3. To edit the application, select the application in the **Applications** list.

   4. On the **Flow Policy** tab, click **[icon: plus, set=fa]Add Flow Policy**.

   5. In the **Policy Name** field, enter a name for the flow policy.

   6. Select **PingOne Flow Policy** to enable flows in the policy to be launched directly through PingOne.

      |   |                                                                                                                                                                                                                                                                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | This option can't be changed after the flow policy is created. PingOne flow policies can only include flows and flow versions that have the **PingOne Flow** setting enabled. Learn more in [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation. |

   7. Click **Next**.

   8. In the flow list, click **Entra ID External MFA Sample Flow** and select one or more versions of the flow to use.

      ![A screen capture of the Add FLow Policy modal with Entra ID External MFA Sample Flow and Latest Version selected.](_images/p1_entra_eam_flow_policy.png)

   9. Click **Next**.

   10. (Optional) Add weight distribution and analytics information for each flow and flow version. Learn more in [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation.

   11. Click **Create Flow Policy**.

### Configuring the OIDC application

Configure an OIDC application to handle authentication requests from Microsoft Entra ID.

## Steps

1. In the PingOne admin console, go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon to add an application.

3. On the **Add Application** panel, enter and choose the following:

   1. **Application Name**: A unique identifier for the application.

   2. **Description** (optional): A brief description of the application.

   3. **Icon** (optional): A graphic representation of the application. Use a file up to 1 MB in JPG, JPEG, GIF, or PNG format.

   4. **Application Type**: Choose **OIDC Web App**.

   5. Click **Save**.

4. On the **Configuration** tab, click [icon: pencil, set=fa]and enter or edit the following:

   1. **Response Type**: Clear the default **Code** checkbox and select **ID Token**.

   2. **Grant Type**: Clear the default **Authorization Code** checkbox and select **Implicit** checkbox.

   3. **Redirect URIs**: Enter `https://login.microsoftonline.com/common/federation/externalauthprovider`.

   4. Click **Save**.

5. On the **Policies** tab, click **[icon: plus, set=fa]Add Policies**.

6. On the **DaVinci Policies** tab, select the DaVinci flow policy that you created to handle external authentication requests from Entra ID.

   ![A screen capture of the Entra ID External MFA Flow Policy selected on the DaVinci Policies tab.](_images/p1_entra_oidc_app_davinci_policy.png)

7. Click **Save**.

8. To enable the application, click the toggle at the top of the details panel to the right (blue).

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | You can disable the application by clicking the toggle to the left (gray). |

9. Click the application entry to open the details panel.

10. On the **Overview** tab, copy the following PingOne application details to add in the Microsoft Entra admin center:

    * In the **General** section, copy the **Client ID** and paste it in a secure location.

    * In the **Connection Details** section, copy the **OIDC Discovery Endpoint** and paste it in a secure location.

### Creating external MFA in Microsoft Entra

After creating the OIDC application in PingOne and copying the application ID, OIDC discovery endpoint, and client ID, create external MFA in Microsoft Entra.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Protection > Authentication methods > Policies**.

3. Click **Add External MFA**.

4. Enter the following:

   1. **Name**: Enter a name for the external MFA.

   2. **Client ID**: Enter your PingOne application's client ID that you copied earlier.

   3. **Discovery Endpoint**: Enter the **OIDC Discovery Endpoint** that you copied earlier from PingOne. The format is `<issuer>/.well-known/openid-configuration`.

   4. **App ID**: Enter the Microsoft Entra application ID that you copied previously. You can find the application ID in the [Microsoft Entra admin center](https://entra.microsoft.com/).

5. Click **Request permission**.

   ![A screenshot of the External MFA configuration page in the Entra admin center.](_images/p1-entra-eam-add-external-method-request-permission.png)

   ##### Result:

   The browser opens a new window for you to sign on with your Microsoft Entra admin credentials.

6. Review the requested permissions and click **Accept** if you agree.

7. In the **Enable and target** section, configure whether you want to include a subset of your users or all users.

8. Click the **Enable** toggle to enable the external MFA.

   ![A screenshot of the External MFA configuration page in the Entra admin center.](_images/p1-entra-eam-add-external-method-enable.png)

### Creating a conditional access policy in Microsoft Entra

Configure a conditional access policy in Microsoft Entra to define authentication requirements for users accessing applications.

|   |                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If your Microsoft Entra tenant contains other conditional access policies that use custom controls to initiate MFA, ensure those policies don't apply to the same users, groups, and applications that you select in this conditional access policy. Otherwise, your users could be prompted multiple times for MFA. |

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Protection > Conditional Access > Policies**.

3. Click **[icon: plus, set=fa]Create new policy** or update an existing policy.

4. Configure the following:

   1. **Name**: Enter a name for the policy.

   2. **Users**: Select the same users and groups that you selected in your external MFA.

   3. **Target resources**: Select the applications to which you want to apply this conditional access policy.

   4. **Grant**:

      1. Click **Grant access**.

      2. Select the **Require multifactor authentication** checkbox.

         ![A screenshot of Conditional Access Policy - Grant access modal in the Entra admin center.](_images/p1-entra-eam-conditional-access-policy-grant.png)

      3. Click **Select**.

   5. **Enable policy**: Select **On** to turn on the policy.

5. Click **Save**.

### Configuring PingID as the external MFA

Configure a PingID policy to process user MFA requests coming from the PingOne application that you created to handle Microsoft Entra requests.

#### Steps

1. In the PingID admin portal, go to **Setup > PingID** and click the **Configuration** tab.

   |   |                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you selected **Enable** for **Enforce Policy**, you might need to create an additional PingID policy. Learn more in the next step. |

2. Click the **Policy** tab, and on the **Web** tab, expand and review each policy.

   |   |                                                                                                                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Microsoft Entra ID doesn't allow MFA bypasses from external MFA and requires always prompting the user to complete MFA. If you have a policy that can apply to all applications and that has a rule with an action of **Approve**, you must create a new policy for the PingOne application. Examples of such policies include Recent Authentication or Accessing from Company Network. |

   ![A screen capture of a PingID policy that has a rule with an action of Approve for Recent Authentication.](_images/pingid_microsoft_entra_eam.png)

   1. To add a new policy, click **Add Policy**.

   2. Enter a name for the policy, such as `External MFA PingID policy`.

   3. In the **Target** section, in the **Applications** list, select the PingOne application that you previously created.

   4. For **Groups**, select all applicable groups.

   5. (Optional) In the **Allowed Methods** section, select the authentication methods you want to allow.

      ![A screen capture of a new PingID policy with the PingOne Entra application selected.](_images/pingid_policy_eam.png)

   6. Click **Save**.

      #### Result:

      The new policy becomes the first PingID policy, which works as Microsoft Entra ID external MFA. PingID will use this new policy when processing MFA requests coming from the PingOne application that you created to handle Microsoft Entra ID requests.

3. In a scenario where a user forgot or lost their mobile phone and can't use the PingID app for MFA, you can allow a user to bypass MFA with PingID for a specificed period of time, such as 8 hours.

   1. In the PingOne admin console, go to **Directory > Users**.

   2. Browse or search for the applicable user and click the user entry to open the details panel.

   3. In the list for the **Services** tab, select **Authentication**.

   4. Scroll down to the **Integrations** section, click the **More Options** icon, and select **Bypass**.

   5. In the **Bypass** window, select the desired amount of time from the **Allow bypass of PingID authentication on SSO for** list and click **Bypass**.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                        |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Because Microsoft Entra ID requires the third-party MFA provider to specify the MFA method used and doesn't accept MFA bypasses as an acceptable MFA method, you must also configure bypass in the Microsoft Entra admin center. Learn more about configuring conditional access in the [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview). |

### Adding a DaVinci flow and flow policy for OIDC authentication

If you want to allow users to sign on to the **PingOne Self-Service - MyAccount** application to manage their MFA methods or to other applications you've added to PingOne, you must create a DaVinci flow and flow policy for OIDC authentication using the same Microsoft IdP connection.

#### Before you begin

Make sure you've downloaded the [Entra ID External MFA & OIDC Authentication Reference Flow](https://marketplace.pingone.com/item/entra-id-eam-oidc-authentication-reference-flow) from the Ping Library and extracted the contents of the `.zip` archive to a folder on your computer. Learn more in [Adding a DaVinci flow and flow policy for Entra ID external authentication](#add_davinci_flow).

#### Steps

1. In DaVinci, on the **Flows** tab, click **[icon: plus, set=fa]Add Flow** and select **Import Flow**.

2. Upload the `entra-id-external-mfa-oidc-authentication-reference-flow.json` file from the sample flow `.zip` archive and click **Import**.

3. Configure the **Entra ID OIDC authentication - Sign On with External Identity Provider** node:

   1. Click the node to open the configuration settings.

   2. In the **PingOne External Identity Provider** list, select the same Microsoft IdP you used in the **Entra ID External MFA Sample Flow**.

   3. Make sure **Policy Purpose** is set to **OIDC Authentication**.

   4. Make sure the **Link with PingOne User** toggle is enabled (blue).

   5. In the **PingOne Population** list, select the same population you used in the [Entra ID External MFA Sample Flow](#add_davinci_flow).

   6. Click **Apply**.

4. Review the default configuration settings for the **Mint Tokens - Return Success Response** node:

   1. Click the node to open the configuration settings.

   2. On the **General** tab, make sure **User ID** is mapped to `id` from the **Entra ID OIDC authentication - Sign On with External Identity Provider** node.

   3. In the **Authentication Methods** list, make sure **mfa** is selected.

      ![A screen capture of the PingOne Authentication - Return Success Response node configuration settings.](_images/p1_entra_eam_davinci_oidc_node.png)

   4. Click **Apply**.

5. Add a DaVinci flow policy for the sample flow:

   1. Go to the **Applications** tab and click **[icon: plus, set=fa]Add Application**.

   2. In the **Name** field, enter a name for the application and click **Create**.

   3. To edit the application, select the application in the **Applications** list.

   4. On the **Flow Policy** tab, click **[icon: plus, set=fa]Add Flow Policy**.

   5. In the **Policy Name** field, enter a name for the flow policy.

   6. Select **PingOne Flow Policy** to enable flows in the policy to be launched directly through PingOne.

      |   |                                                                                                                                                                                                                                                                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | This option can't be changed after the flow policy is created. PingOne flow policies can only include flows and flow versions that have the **PingOne Flow** setting enabled. Learn more in [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation. |

   7. Click **Next**.

   8. In the flow list, click **Entra ID OIDC Authentication Sample Flow** and select one or more versions of the flow to use.

      ![A screen capture of the Add Flow Policy modal with Entra ID OIDC Authentication Sample Flow and Latest Version selected.](_images/p1_entra_eam_oidc_flow_policy.png)

   9. Click **Next**.

   10. (Optional) Add weight distribution and analytics information for each flow and flow version. Learn more in [Configuring a flow policy](https://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html) in the DaVinci documentation.

   11. Click **Create Flow Policy**.

#### Result:

You now have two DaVinci flows:

* A flow for users authenticating with PingOne as the external MFA for Entra ID

* A flow for OIDC authentication to allow users to sign on to other applications

![A screen capture of the two Entra ID sample flows in DaVinci.](_images/p1_entra_eam_davinci_flows.png)

### Adding the callback URL to the Entra admin center

If you created an authentication policy for OIDC authentication, you must also add the callback URL from the Microsoft IdP connection in PingOne to the application you registered in the Microsoft Entra admin center.

#### Steps

1. Go to the [Microsoft Entra admin center](https://entra.microsoft.com/).

2. In the sidebar, go to **Identity > Applications > App registrations** and click your application.

3. On the **App registrations** page, in the **Manage** section, click **Authentication**.

4. In the **Platform configurations > Web > Redirect URIs** section, click **Add URI**.

   ![A screenshot of the Authentication page - Redirect URIs in the Entra admin center.](_images/p1-entra-eam-redirect-uris.png)

5. Paste the **Callback URL** that you copied from the PingOne admin console.

   The following examples show the URL format:

   Example 1: `https://auth.pingone.<region>/<envID>/rp/callback/microsoft`

   Example 2: `https://<customDomain>/rp/callback/microsoft`

6. Click **Save**.

#### Result

The **Redirect URIs** section displays both URLs you've added:

1. Authorization URL

2. Callback URL

![A screen capture of the Entra Authentication page with two redirect URIs identified with a red number callouts.](_images/p1_microsoft_entra_redirect_uris.png)

### Assigning the DaVinci OIDC flow policy to an application in PingOne

After you create a DaVinci flow and flow policy for OIDC authentication and add the callback URL to the application in Entra ID, assign the DaVinci OIDC flow policy to applicable applications in PingOne, such as the **PingOne Self-Service - MyAccount** application or other applications you've added.

#### Steps

1. In the PingOne admin console, go to **Applications > Applications** and click the relevant application to open the details panel.

2. On the **Policies** tab, click **[icon: plus, set=fa]Add policies**.

3. On the **DaVinci Policies** tab, select the DaVinci OIDC flow policy that you created in [Adding a DaVinci flow and flow policy for OIDC authentication](#davinci-flow-oidc).

   ![A screen capture of the Entra ID OIDC Authentication Flow Policy selected on the DaVinci Policies tab.](_images/p1_entra_eam_selfservice_app_oidc_flow_policy.png)

4. Click **Save**.

#### Next steps

Repeat these steps for any other applications to which you want users to be able to sign on, for example **Another App** in the following screenshot.

![A screen capture of the PingOne Applications page with an example application called Another App selected and the Policies tab showing an added policy named Entra\_ID\_OIDC\_Auth\_Policy.](_images/p1_microsoft_entra_another_app_policy.png)

## Validation

Now that you've set up external MFA in Entra ID and configured PingOne and PingID as the external MFA provider, you're ready to validate that your Entra ID users can use PingID to complete MFA.

1. Open a new browser window in incognito mode.

2. In the [Entra admin center](https://entra.microsoft.com/), locate the application you added to the conditional access policy that requires MFA and click the URL for the application.

   In this example, **My Apps** at https\://myapps.microsoft.com.

3. Sign on to the application and complete the first-factor authentication at Microsoft using a test user's credentials.

   ### Result:

   Entra ID prompts the user to complete MFA action based on what Entra thinks is the most secure method if:

   * You, as an Entra ID admin, have activated system-preferred MFA and included the test user as the target user.

   * The test user has installed and successfully used the system-preferred MFA method.

   In this example, the test user has installed and used both Microsoft Authenticator and verification code by text message, so Entra ID prompts the user to enter the code from Microsoft Authenticator.

   ![A screen capture of the Microsoft Enter code page.](_images/p1_microsoft_enter_code.png)

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you haven't activated system-preferred MFA, the user won't see the **Enter code** modal and is prompted to verify their identity. |

4. To use your external MFA, click **Sign in another way** at the bottom of the **Enter code** modal.

   ### Result:

   After selecting **Sign in another way** or if system-preferred MFA doesn't apply, Entra ID displays the **Verify your identity** modal.

   ![A screen capture of the Microsoft Enter code page.](_images/p1_microsoft_verify_identity.png)

5. Select the external MFA.

   ### Result:

   Entra ID redirects the browser to PingOne.

6. If the test user hasn't yet paired the PingID app, they're shown a **Welcome to PingID** page. Click **Start** to start the pairing process.

   ![A screen capture of the Welcome to PingID page and then the Add New Device page with a QR code and pairing key.](_images/p1_pingid_add_device.png)

   ### Result:

   After pairing, the PingID app prompts the user to complete the MFA requirement.

7. After PingID is paired for the test user, complete the MFA prompt from the PingID app.

   ### Result:

   PingOne returns an ID token to Entra ID, and Entra ID processes the ID token and signs the test user on to the application.

8. Sign off of the application.

9. In the [Entra admin center](https://entra.microsoft.com/), locate the same application and authenticate to the application again as the test user.

   ### Result:

   This time, PingID shouldn't prompt the test user to pair a device. Instead, the PingID app should prompt the test user to complete the MFA requirement.

   When the test user completes the MFA requirement, PingOne returns an ID token to Entra ID, and Entra ID processes the ID token and signs the test user on to the application.

   ![A screen capture of the Microsoft Apps dashboard.](_images/p1_microsoft_my_apps.png)

---

---
title: Using PingGateway no-code application and API protection
description: PingGateway connects to PingOne as a single sign-on (SSO) provider. This integrates web applications, APIs, and microservices with PingOne without modifying the applications or the containers where they run.
component: pingone
page_id: pingone:use_cases:p1_use_pg_no_code_app_and_api_protection
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_use_pg_no_code_app_and_api_protection.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Using PingGateway no-code application and API protection

PingGateway connects to PingOne as a single sign-on (SSO) provider. This integrates web applications, APIs, and microservices with PingOne without modifying the applications or the containers where they run.

PingGateway runs as reverse proxy gateway calling on PingOne for authentication and authorization. In deploying PingGateway, you protect APIs and applications as they are without changing them.

The PingGateway declarative configuration model gives you the flexibility to serve many use cases without the need to write or change code.

Learn more in the [PingGateway documentation](https://docs.pingidentity.com/pinggateway/latest/pingone/preface.html).