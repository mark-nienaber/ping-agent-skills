---
title: Applications
description: An application in DaVinci represents one of your applications and gives you fine-grained control over which flows can be run through that application and by what methods.
component: davinci
page_id: davinci:applications:davinci_applications
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_applications.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
---

# Applications

An application in DaVinci represents one of your applications and gives you fine-grained control over which flows can be run through that application and by what methods.

An application acts as a gateway between your site and the flows you have created in DaVinci. The application contains settings to determine how external sites can send requests for flows, what flows can be requested, and how users and resources from other sites are managed. External sites can only run flows that are made available through an application.

The **General** and **OIDC** tabs let you configure receivers for incoming requests. Other tools can send requests to launch flows using API endpoints described in the **General** tab or the OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* parameters in the **OIDC** tab.

The **Flow Policy** tab lets you control which flows are run through the application. A flow policy is an entity that points to one or more flows or versions of flows. You can use a flow policy to make sure that a specific version of a flow, such as the latest version, is always used. You can also split traffic between different flows or flow versions for A/B testing or other purposes.

The **Connections** tab lets you direct requests to specific connectors.

---

---
title: Configuring a flow policy
description: Configure flow policies to control which flows and flow versions are displayed for users.
component: davinci
page_id: davinci:applications:davinci_configuring_a_flow_policy
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_configuring_a_flow_policy.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  steps: Steps
  result: Result:
---

# Configuring a flow policy

Configure flow policies to control which flows and flow versions are displayed for users.

## Steps

1. On the **Applications** tab, browse or search for the application and click **Edit**.

2. On the **Flow Policy** tab, click **+ Add Flow Policy**.

3. In the **Policy Name** field, enter a name for the flow policy.

4. Select **PingOne Flow Policy** to enable flows in the policy to be launched directly through PingOne.

   This option cannot be changed after the flow policy is created. PingOne flow policies can only include flows and flow versions that have the **PingOne Flow** setting enabled.

5. (Optional) If the flow policy is a PingOne flow policy, select one or more options for bypassing the flow if an existing session is found.

   This option is useful if you want to avoid unnecessary flow executions for users who already have a session. The **PingOne Authentication - Return Success** node includes the appropriate session options.

   1. Select **Password Based Authentication** to bypass the flow if a password-based session exists, and select **MFA Based Authentication** to bypass the flow if an MFA-based session exists.

      |   |                                                                                                                                                                                              |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you select both **Password Based Authentication** and **MFA Based Authentication**, the user's session must have both authentication method reference values for the flow to be bypassed. |

   2. For each selected authentication method, provide a time range by entering a number and selecting minutes, hours, or days. The flow is only bypassed if the existing session was created within the time range you select.

6. Click **Next**.

7. Add one or more flows to the policy:

   1. In the **Flows** section, select a flow.

   2. In the **Version** section, select one or more versions of the flow to use.

      The **Latest Version** option always uses the latest version.

   3. (Optional) Repeat the previous steps to add additional flows.

8. Click **Next**.

   ### Result:

   The **Edit Your Weight Distribution** modal opens.

9. Add weight distribution and analytics information for each flow and flow version:

   1. In the **Distribution** field for each flow version, enter or select a distribution weight from 1 - 100.

      When a flow policy with more than one flow is invoked, the flow policy selects a flow to run, using the distribution weight for each flow as the percent chance of its selection. You can use this feature to A/B test flows or flow versions.

   2. (Optional) Click **Add IP Whitelist**, then enter one or more IP addresses in the **Whitelist IP** field.

      |   |                                                                                                                      |
      | - | -------------------------------------------------------------------------------------------------------------------- |
      |   | If a request comes from an IP address on the allow list, the weight is ignored, and the specified flow is triggered. |

   3. (Optional) In the **Analytics - Select Success Nodes** list, select one or more nodes that, when run, indicate that the flow run was successful.

   This information is used to calculate the flow policy's success rate.

10. Click **Create Flow Policy**.

11. Click the **General** tab, then click **Apply**.

---

---
title: Configuring connection settings
description: Add connections to an application to enable direct interactions with that connector through REST API calls.
component: davinci
page_id: davinci:applications:davinci_configuring_connections
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_configuring_connections.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 2, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring connection settings

Add connections to an application to enable direct interactions with that connector through REST API calls.

## About this task

|   |                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------- |
|   | This feature is currently in limited release. To request access to this feature, open a support case. |

## Steps

1. Click the **Applications** tab.

2. Find the application and click **Edit**.

3. Click the **Connections** tab.

4. In the **Add Connection** list, select one or more connections.

5. Click **Apply**.

---

---
title: Configuring general application settings
description: Configure an application's general properties and API settings.
component: davinci
page_id: davinci:applications:davinci_configuring_general_settings
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_configuring_general_settings.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  steps: Steps
---

# Configuring general application settings

Configure an application's general properties and API settings.

## Steps

1. Click the **Applications** tab.

2. Find the application and click **Edit**.

3. Click the **General** tab.

4. (Optional) In the **Name** field, update the name of the flow.

5. (Optional) Note the **Company ID** and **Client ID**.

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | These fields are read-only. You can copy the values if necessary. |

6. (Optional) Click the **Enable API Key** toggle to enable or disable the current API key.

7. (Optional) Click **Regenerate API Key** to generate a new API key.

   When you generate a new API key, the previous key permanently retains the enablement status it had when the key was regenerated.

   * Disable the **Enable API Key** toggle before regenerating the key to permanently disable the old key.

   * Enable the **Enable API Key** toggle before regenerating the key to permanently enable the old key.

8. (Optional) Reveal and copy the **API Key** for use in API calls.

9. (Optional) In the **FIDO2 Connection** list, select a FIDO2 authentication method to be used for `/credentials/fido2` API paths.

   |   |                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------- |
   |   | This feature is currently in limited release. To request access to this feature, open a support case. |

10. Click **Apply**.

---

---
title: Configuring OIDC settings
description: Configure OpenID Connect (OIDC) for your application to enable it as a method for invoking flows.
component: davinci
page_id: davinci:applications:davinci_configuring_openid
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_configuring_openid.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Configuring OIDC settings

Configure OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* for your application to enable it as a method for invoking flows.

## Steps

1. Click the **Applications** tab.

2. Find the application and click **Edit**.

3. Click the **OIDC** tab.

4. (Optional) Click **Regenerate Client Secret** to create a new client secret.

   Generating a new client secret invalidates the previous secret.

5. Reveal and copy the **Client Secret** for use in OIDC connections.

6. In the **Redirect URLs** field, enter one or more redirect URLs for the application.

7. In the **Logout URLs** field, enter one or more logout URLs for the application.

8. In the **Scopes** section, select one or more scopes based on your application's needs.

   | Option             | Description                              |
   | ------------------ | ---------------------------------------- |
   | **OIDC**           | Select the **OIDC** check box.           |
   | **Profile**        | Select the **Profile** check box.        |
   | **Flow Analytics** | Select the **Flow Analytics** check box. |

9. In the **Grants** section, select one or more grants based on your application's needs.

   | Option                 | Description                                  |
   | ---------------------- | -------------------------------------------- |
   | **Authorization Code** | Select the **Authorization Code** check box. |
   | **Implicit**           | Select the **Implicit** check box.           |
   | **Client Credentials** | Select the **Client Credentials** check box. |

10. Copy the **Issuer**.

11. Copy the **Token Endpoint**.

12. Copy the **UserInfo Endpoint**.

13. Copy the **JWKS Endpoint**.

14. Copy the **JWKS**.

15. Click the **Enforce receiving signed requests?** toggle to require that incoming requests be signed.

16. Provide a method for verifying service provider JSON web key sets (JWKS):

    ### Choose from:

    * In the **Service Provider (SP) JWKS URL** field, enter a URL.

    * In the **Service Provider (SP) JWKS Keys to Verify Authorization Request Signature** field, enter one or more keys.

17. Click **Apply**.

---

---
title: Creating an application
description: Create a new application to enable DaVinci to interact with that application.
component: davinci
page_id: davinci:applications:davinci_creating_an_application
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_creating_an_application.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 28, 2024
section_ids:
  steps: Steps
---

# Creating an application

Create a new application to enable DaVinci to interact with that application.

## Steps

1. Click the **Applications** tab.

2. Click **Add Application**.

   The **Add Application** modal displays.

3. In the **Name** field, enter a name for the application.

4. Click **Create**.

5. Find the application and click **Edit**.

6. Update the application's properties.

   |   |                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Although an application doesn't require most properties, you must configure a flow policy in the **Flow Policies** tab before you can run flows through the application. See [Configuring a flow policy](davinci_configuring_a_flow_policy.html) for more information. |

7. Click **Apply**.

---

---
title: Deleting a flow policy
description: Delete an existing flow policy to permanently remove it from use.
component: davinci
page_id: davinci:applications:davinci_deleting_a_flow_policy
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_deleting_a_flow_policy.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Deleting a flow policy

Delete an existing flow policy to permanently remove it from use.

## Before you begin

Verify that the flow policy is not in use.

## Steps

1. Click the **Applications** tab.

2. Find the application and click **Edit**.

3. Click the **Flow Policy** tab.

4. Locate the flow policy and in the **More options ( [icon: ellipsis-v, set=fa])** list, select **Delete**.

   A confirmation modal opens.

5. Click **Delete**.

---

---
title: Deleting an application
description: Delete an application to remove it from the UI and stop all flow use for it.
component: davinci
page_id: davinci:applications:davinci_deleting_an_application
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_deleting_an_application.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 22, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deleting an application

Delete an application to remove it from the UI and stop all flow use for it.

## About this task

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | Verify that the application is not being used in an active production environment. |

## Steps

1. Click the **Applications** tab.

2. Find the application and click **Delete**.

   A confirmation message displays.

3. Click **Delete**.

---

---
title: Editing a flow policy
description: Edit existing flow policies to update which flows and flow versions are displayed for users.
component: davinci
page_id: davinci:applications:davinci_editing_a_flow_policy
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_editing_a_flow_policy.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Editing a flow policy

Edit existing flow policies to update which flows and flow versions are displayed for users.

## Steps

1. On the **Applications** tab, browse or search for the application and click **Edit**.

2. On the **Flow Policy** tab, locate the flow policy and, in the **More options ( [icon: ellipsis-v, set=fa])** list, select **Edit**.

3. (Optional) In the **Name** field, update the name of the flow policy.

4. (Optional) If the flow policy is a PingOne flow policy, select one or more options for skipping the flow if an existing session is found.

   This option is useful if you want to avoid unnecessary flow executions for users who already have a session.

   1. Select **Password Based Authentication** to skip the flow if a password-based session exists, and select **MFA Based Authentication** to skip the flow if an MFA-based session exists.

   2. For each selected authentication method, provide a time range by entering a number and selecting minutes, hours, or days. The flow is only skipped if the existing session was created within the time range you select.

5. Click **Next**.

6. (Optional) Update the flows and flow versions included in the flow policy:

   1. Add a flow by selecting it in the **Flows** section, then selecting one or more versions in the **Version** section.

   2. Update the included versions for a flow by selecting it in the **Flows** section, then adding or removing versions in the **Version** section.

   3. Remove a flow by clicking the **X** icon in the **Flows Added** section.

7. Click **Next**.

8. (Optional) Update the weight distribution and analytics information for each flow and flow version:

   1. In the **Distribution** field for each flow version, enter or select a distribution weight from 1 - 100.

   2. (Optional) Click **Add IP Whitelist**.

   3. (Optional) In the **Whitelist IP** field, enter one or more IP addresses.

      |   |                                                                                                                      |
      | - | -------------------------------------------------------------------------------------------------------------------- |
      |   | If a request comes from an IP address on the allow list, the weight is ignored, and the specified flow is triggered. |

   4. (Optional) In the **Analytics - Select Success Nodes** list, select one or more nodes that, when run, indicate that the flow run was successful.

   This information is used to calculate the flow policy's success rate.

9. Click **Update Flow Policy**.

---

---
title: Flow Policies
description: Flow policies let you control which flows are launched through the application.
component: davinci
page_id: davinci:applications:davinci_flow_policies
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_flow_policies.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
---

# Flow Policies

Flow policies let you control which flows are launched through the application.

Choose from one of the following topics:

* [Configuring a flow policy](davinci_configuring_a_flow_policy.html)

* [Editing a flow policy](davinci_editing_a_flow_policy.html)

* [Deleting a flow policy](davinci_deleting_a_flow_policy.html)

* [Flow policy metrics](davinci_flow_policy_comparison_metrics.html)

---

---
title: Flow policy metrics
description: The Flow Comparison Metrics page lets you view data about the flows included in a flow policy. You can view it by locating the flow policy and, in the More options ( ) list, selecting Comparison Metrics.
component: davinci
page_id: davinci:applications:davinci_flow_policy_comparison_metrics
canonical_url: http://docs.pingidentity.com/davinci/applications/davinci_flow_policy_comparison_metrics.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 25, 2023
---

# Flow policy metrics

The **Flow Comparison Metrics** page lets you view data about the flows included in a flow policy. You can view it by locating the flow policy and, in the **More options ( [icon: ellipsis-v, set=fa])** list, selecting **Comparison Metrics**.

| Data                     | Description                                                                                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Flow Variation Names** | The name and version of the flow.                                                                         |
| **Total Visitors**       | The number of runs of the specified flow and version.                                                     |
| **Success Rate**         | The percentage of flow runs that included one or more of the success nodes as defined in the flow policy. |