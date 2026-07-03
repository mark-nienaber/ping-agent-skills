---
title: Integrating Flows into Applications
description: After you create a flow, integrate it into a user-facing application. Integrating a flow into an application lets your users launch the flow from that application.
component: davinci
page_id: davinci:integrating_flows_into_applications:davinci_how_to_implement_a_flow
canonical_url: http://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_how_to_implement_a_flow.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 31, 2024
section_ids:
  integration-method-comparison: Integration method comparison
  description: Description
  trigger: Trigger
  ux-hosted-by: UX Hosted By
  html: HTML
  css: CSS
  user-experience: User Experience
  modes: Modes
  developer-experience-for-launching-flows: Developer Experience for Launching Flows
  time-required: Time Required
---

# Integrating Flows into Applications

After you create a flow, integrate it into a user-facing application. Integrating a flow into an application lets your users launch the flow from that application.

You can integrate a flow in different ways. Each method launches the flow in a different way. Choose an integration method based on the type of flow that you want to launch and the desired user experience.

The following methods can be used to launch a flow:

* [A redirect through PingOne](davinci_launch_flow_redirect.html). This method uses a call to [a PingOne application](http://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) to launch a flow with a redirect. This method is effective for flows with UI components. You should use a redirect through PingOne if you want to launch the flow in a new application page that replaces the current page and if you want to use OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
  \<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
  \</div>)* or Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
  \<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
  \</div>)* authentication.

* [A redirect through PingOne using DaVinci as an external identity provider (IdP)](davinci_launch_flow_redirect_external_idp.html). This method uses a call to [a PingOne application](http://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) to launch a flow with a redirect using an external IdP configuration. This method is effective for flows with UI components, but it's not recommended unless you have already configured your environment for it. If you want to configure your environment to launch flows with a redirect through PingOne, use [this procedure instead](davinci_launch_flow_redirect.html).

* [The widget](davinci_launching_a_flow_with_the_widget.html). This method launches a flow inside of a widget on the current page. This method is effective for situations in which you do not want to redirect the user to a new URL.

* [An API call](davinci_launching_a_flow_with_an_api_call.html). This method launches a flow using an API call. This method is effective for flows without a UI component.

* [The SDK](davinci_sdk_launching_a_flow_with_the_sdk.html). This method launches a flow from an application that you develop using the DaVinci module for the Ping SDK for JavaScript, Ping SDK for iOS, or Ping SDK for Android. This method is appropriate if you want fine-grained control of a user's mobile experience.

* [The PingFederate integration](http://docs.pingidentity.com/integrations/pingone/pingone_davinci_integration_kit/pf_p1_davinci_ik.html). This method uses the widget to launch a flow from an existing PingFederate deployment.

|   |                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To switch between using flows for a PingOne redirect integration and an integration using the DaVinci widget, refer to [Switching between PingOne and DaVinci widget integrations](davinci_switch_between_flow_integrations.html). |

## Integration method comparison

### Description

|                                                        |                                                                                      |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| Redirect                                               | Launches flow in new browser tab                                                     |
| Widget                                                 | Launches flow within current browser tab                                             |
| API                                                    | Launches flow without UI components using API call                                   |
| SDK                                                    | Launches flow from native or web apps using the Ping SDKs from a PingOne application |
| DaVinci Integration Kit for PingFederate (widget mode) | Launches flow within current browser tab                                             |
| DaVinci Integration Kit for PingFederate (API mode)    | Launches flow without UI components using API call                                   |

### Trigger

|                                                        |                                                                                                        |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| Redirect                                               | PingOne Policy link                                                                                    |
| Widget                                                 | Widget embedded in application                                                                         |
| API                                                    | API Call                                                                                               |
| SDK                                                    | Launch from within SDK application                                                                     |
| DaVinci Integration Kit for PingFederate (widget mode) | PingFederate authentication policy initiates DaVinci Integration Kit adapter in widget-based flow mode |
| DaVinci Integration Kit for PingFederate (API mode)    | PingFederate authentication policy initiates DaVinci Integration Kit adapter in API-based flow mode    |

### UX Hosted By

|                                                        |                                                                  |
| ------------------------------------------------------ | ---------------------------------------------------------------- |
| Redirect                                               | DaVinci                                                          |
| Widget                                                 | Application that launched the flow                               |
| API                                                    | NoneLaunching application must handle UX                         |
| SDK                                                    | Custom application built with the SDK                            |
| DaVinci Integration Kit for PingFederate (widget mode) | PingFederate                                                     |
| DaVinci Integration Kit for PingFederate (API mode)    | NoneDaVinci adapter in API-based flow mode does not present a UI |

### HTML

|                                                        |                                                                  |
| ------------------------------------------------------ | ---------------------------------------------------------------- |
| Redirect                                               | DaVinci using PingOne Forms or Custom HTML                       |
| Widget                                                 | DaVinci with Custom HTML                                         |
| API                                                    | NoneLaunching application must handle UX                         |
| SDK                                                    | Launching application must handle UX                             |
| DaVinci Integration Kit for PingFederate (widget mode) | DaVinci Integration Kit template                                 |
| DaVinci Integration Kit for PingFederate (API mode)    | NoneDaVinci adapter in API-based flow mode does not present a UI |

### CSS

|                                                        |                                                                  |
| ------------------------------------------------------ | ---------------------------------------------------------------- |
| Redirect                                               | DaVinci                                                          |
| Widget                                                 | Host application                                                 |
| API                                                    | NoneLaunching application must handle UX                         |
| SDK                                                    | Launching application must handle UX                             |
| DaVinci Integration Kit for PingFederate (widget mode) | DaVinci Integration Kit template                                 |
| DaVinci Integration Kit for PingFederate (API mode)    | NoneDaVinci adapter in API-based flow mode does not present a UI |

### User Experience

|                                                        |                                                                  |
| ------------------------------------------------------ | ---------------------------------------------------------------- |
| Redirect                                               | User's browser tab is redirected to DaVinci with refresh         |
| Widget                                                 | Flow is launched within the host application                     |
| API                                                    | NoneLaunching application must handle UX                         |
| SDK                                                    | Flow is launched within the application                          |
| DaVinci Integration Kit for PingFederate (widget mode) | Flow is launched within PingFederate                             |
| DaVinci Integration Kit for PingFederate (API mode)    | NoneDaVinci adapter in API-based flow mode does not present a UI |

### Modes

|                                                        |                                                                  |
| ------------------------------------------------------ | ---------------------------------------------------------------- |
| Redirect                                               | Full screen                                                      |
| Widget                                                 | Embedded in host application or modal                            |
| API                                                    | NoneLaunching application must handle UX                         |
| SDK                                                    | Depends on launching application                                 |
| DaVinci Integration Kit for PingFederate (widget mode) | Embedded in DaVinci Integration Kit template                     |
| DaVinci Integration Kit for PingFederate (API mode)    | NoneDaVinci adapter in API-based flow mode does not present a UI |

### Developer Experience for Launching Flows

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | This applies only to launching flows. Flow creation is equally complex for all methods. |

|                                                        |                                                                                                 |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| Redirect                                               | No development skills neededFlow hosted in DaVinci                                              |
| Widget                                                 | Minimal development effortFlow is a component in existing application                           |
| API                                                    | Significant development effort                                                                  |
| SDK                                                    | Significant development effort                                                                  |
| DaVinci Integration Kit for PingFederate (widget mode) | Minimal development effort- Template presents flow

- Customizations optional                   |
| DaVinci Integration Kit for PingFederate (API mode)    | No development skills neededFlow result data is available in PingFederate authentication policy |

### Time Required

|                                                        |                                                 |
| ------------------------------------------------------ | ----------------------------------------------- |
| Redirect                                               | Fastest                                         |
| Widget                                                 | Fast                                            |
| API                                                    | Slow                                            |
| SDK                                                    | Slow                                            |
| DaVinci Integration Kit for PingFederate (widget mode) | Fast (with existing PingFederate deployment)    |
| DaVinci Integration Kit for PingFederate (API mode)    | Fastest (with existing PingFederate deployment) |

---

---
title: Launching a flow with a Ping SDK
description: Launch a prepared flow through an application built with one of the Ping SDKs.
component: davinci
page_id: davinci:integrating_flows_into_applications:davinci_sdk_launching_a_flow_with_the_sdk
canonical_url: http://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_sdk_launching_a_flow_with_the_sdk.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 13, 2024
section_ids:
  configuring-the-flow: Configuring the Flow
  about-this-task: About this task
  steps: Steps
  creating-a-davinci-application: Creating a DaVinci application
  steps-2: Steps
  result: Result:
  result-2: Result:
  configuring-pingone-for-flow-invocation: Configuring PingOne for flow invocation
  about-this-task-2: About this task
  steps-3: Steps
  invoking-the-flow: Invoking the flow
---

# Launching a flow with a Ping SDK

Launch a prepared flow through an application built with one of the Ping SDKs.

The Ping SDKs provide powerful orchestration capabilities with PingOne DaVinci. They let you create flows to meet your use cases, while providing a native iOS, Android, or single-page app JavaScript experience.

This method is effective when you want complete control of your end user's experience while using a flow behind the scenes.

## Configuring the Flow

Prepare a flow to be launched with the Ping SDK for Android, iOS, or JavaScript.

### About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure only covers the steps and nodes required to prepare a flow for SDK invocation. It assumes that you've already created a flow for the purpose you have in mind. You can find more information about building flows in the [Getting started with DaVinci](../flows/davinci_getting_started.html) and [DaVinci Best Practices](../davinci_best_practices/davinci_best_practices.html) documentation. |

### Steps

1. On the **Flows** tab, find the flow and click **... > Edit**.

2. Verify that your user interface nodes use only compatible connectors, capabilities, and elements.

   Compatible connectors and capabilities are:

   * The HTTP Connector and its Custom HTML Template capability

   * The Form Connector and its Show Form capability

   Compatible elements within the Custom HTML Template and Form connector capabilities are:

   | PingOne Forms element name                | Custom HTML element name                   | Description                                                                                                                     |
   | ----------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
   | **Text Input**                            | **Text field**                             | Lets the user enter text.                                                                                                       |
   | **Password**                              | **Text Input** with the **Secure** setting | Lets the user enter a password that cannot be read from the screen. The PingOne Forms **Verify Password** feature is supported. |
   | **Submit Button**                         | **Submit Button**                          | Lets the user submit field data and proceed.                                                                                    |
   | **Flow Button**                           | **Flow Button**                            | Lets the user trigger a new process without submitting field data.                                                              |
   | **Translatable Rich Text**                | **Label**                                  | Displays text for the user.                                                                                                     |
   | **Dropdown**                              | **Dropdown**                               | Lets the user make a selection from a dropdown list.                                                                            |
   | **Radio Button List**                     | **Radio Button List**                      | Lets the user make a selection from a radio button list.                                                                        |
   | **Checkbox List**                         | N/A                                        | Lets the user select any number of options from a checkbox list.                                                                |
   | **Combobox**                              | N/A                                        | Lets the user select an existing option from a dropdown list or enter text.                                                     |
   | **Social Login**                          | **skIDP component**                        | Lets users sign on using a third-party identity provider (IdP).                                                                 |
   | **MFA Device Selection - Registration**   | N/A                                        | Displays available MFA devices for a new user registration based on policy.                                                     |
   | **MFA Device Selection - Authentication** | N/A                                        | Displays available MFA devices for an existing user.                                                                            |
   | **Phone Number**                          | **Text field**                             | Lets the user enter a phone number including country and area codes.                                                            |
   | **FIDO2**                                 | **N/A**                                    | Lets the user register or authenticate with their device using FIDO2.                                                           |

3. Verify that your flow does not depend on any unsupported elements:

   * **SKPolling components**: SKPolling components cannot be processed by the SDK and should not be included.

   - **Images**: Images included in the flow cannot be passed to the SDK.

4. If you're using HTTP Connector nodes, ensure that any buttons that submit page data use the following parameters:

   * `type=submit`

   * The `data-skbuttonvalue` must be `Continue`, `Submit`, `Proceed`, or `Next`.

     For example:

     ```html
     <button data-id="button"
         type="submit"
         class="btn btn-primary mb-3"
         data-skcomponent="skbutton"
         data-skbuttontype="form-submit"
         data-skform="usernamePasswordForm"
         id="btnSignIn"
         data-skbuttonvalue="Submit">
     Sign On
     </button>
     ```

5. If you're using HTTP Connector nodes, ensure that any buttons that navigate to a different screen without submitting data use the following parameters:

   * The `data-skbuttonvalue` must not be `Continue`, `Submit`, `Proceed`, or `Next`.

     For example:

     ```html
     <button data-id="button"
         class="btn btn-link"
         data-skcomponent="skbutton"
         data-skbuttontype="form-submit"
         data-skform="usernamePasswordForm"
         id="btnTrouble"
         data-skbuttonvalue="TROUBLE">
     Having trouble signing on?
     </button>
     ```

6. If you're using HTTP Connector nodes, add each text field, password field, and button to the node's output fields.

   These outputs are all used by the SDK, regardless of any conditional logic used to control their display in the HTML.

   1. Click the node.

   2. On the **General** tab, find the **Output Fields List** section, and click **Add**.

   3. In the **Property Name** field, enter a name for the property to be passed to the SDK.

   4. In the **Display Name** field, enter a name for the property to be used in the user interface.

   5. In the **Control Type** list, select **Text Field**.

   6. In the **Data Type** list, select **String**.

   7. If the value is a password, select **Secure**.

   8. In the **Value** field, select the {} option and map the field's value to the property.

   9. Repeat steps b-h for each additional output.

   10. Click **Apply**.

   11. Repeat these steps for each additional node with outputs.

7. If you're using social login, ensure that your flow uses a supported method.

   Social login lets users sign on using a third-party IdP. Apple, Google, and Facebook are natively supported, and other IdPs can be included with a login redirect. You must configure the external IdPs according to the [PingOne documentation](http://docs.pingidentity.com/pingone/integrations/p1_external_idps.html) before including them in a flow.

   |   |                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Social Login using the **Sign On with External Identity Provider** capability of the PingOne Authentication connector is not supported in SDK flows. |

   * In a PingOne Form, you can use the **Social Login** tool to enable social login. Configure this button using the PingOne documentation.

     ![A screenshot of the configuration for the Social Login tool on a PingOne Form.](_images/DV_SDK_invocation_P1_form_config.png)

   * In a Custom HTML Template, you can use the skIDP sk-component to enable social login:

     1. In the **HTML Template** section of the **General** tab, click the **{}** icon.

     2. In the **Choose Connection** list, select **SK-Component**, then select **skIDP**.

     3. Click the **skIDP** component in the **HTML Template** field.

        ![A screenshot of the skIDP component included in a Custom HTML Template node.](_images/DV_SDK_invocation_skidp.png)

     4. In the **Identity Provider Connector** list, select **PingOne Authentication**.

     5. In the **PingOne External Identity Provider** list, select a configured social login provider.

     6. If you want to correlate the third-party login user with a PingOne user, select **Link with PingOne User**, then select a user population in the **PingOne Population** list.

     7. In the **Button ID** field, enter an ID.

        ![A screenshot of the skIDP component configuration, as described in the current step.](_images/DV_SDK_invocation_skidp_config.png)

     8. Click **Save**.

8. To use the user's PingOne User ID in your flow, include the `p1UserId` global parameter in your flow.

   |   |                                                                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The user's PingOne User ID is only available after the user has been identified. The user can be identified directly through PingOne or using a third-party authentication that is correlated with the user's PingOne account. |

   1. Open the node in which you want to include the invocation information.

   2. Click the **Variables ( {} )** icon.

   3. Click **Global**.

   4. Select the **p1UserId** property.

9. If you're using an OTP with PingOne MFA, configure your environment and flow according to the [one-time passcode use case in the SDK documentation](http://docs.pingidentity.com/sdks/latest/davinci/use-cases/otp/index.html) and verify that it uses supported elements.

   1. If you're using email OTP registration or authentication, verify that the flow has screens that:

      * Let the user enter an email address using a **Text Input** or **Text Field**

      * Let the user enter the OTP using a **Text Input** or **Text Field**

      |   |                                                                                                                                                                       |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you're using PingOne Forms, you can dynamically populate the user's email address using the **Dynamic Text** option within the **Translatable Rich Text** element. |

   2. If you're using SMS/Voice OTP registration or authentication, verify that the flow has screens that:

      * Let the user enter a phone number and select a country code using the **Phone Number Input** component

      * Let the user enter the OTP using a **Text Input** or **Text Field**

      |   |                                                                                                                                                                      |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you're using PingOne Forms, you can dynamically populate the user's phone number using the **Dynamic Text** option within the **Translatable Rich Text** element. |

10. To use data about the invocation method or the invocation platform type in your flow, include the `isSdk` and `platformType` global parameters in your flow.

    | Property       | Type    | Description                                                                                                                        |
    | -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
    | `isSdk`        | Boolean | Indicates whether the flow was launched using the SDK.                                                                             |
    | `platformType` | String  | Indicates what platform was used to launch the flow if it was launched using the SDK. Valid values are `js`, `android`, and `ios`. |

    1. Open the node in which you want to include the invocation information.

    2. Click the **Variables ( {} )** icon.

    3. Click **Global** > **Current Request**.

    4. Select the **isSdk** or **platformType** property.

       For example:

       ![A screen capture of the selection process described in steps a-d.](_images/IsSDKSelection.gif)

11. Click **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings** to show the flow settings.

12. Select the **PingOne Flow** option.

13. Click **Save**, then close the **Flow Settings** pane.

14. End the flow with the following two **PingOne Authentication** nodes, one for success and one for failure.

    ![A screen capture of a flow ending with a success and failure path.](_images/kuw1674237257955.png)

    | Node                                           | Purpose                                                                                                                                                                                                     |
    | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Return a Success Response (Redirect Flows)** | This creates a PingOne session for the user and redirects the browser back to the source of the authentication request. This response provides the requested scopes as well as an access token or ID token. |
    | **Return an Error Response (Redirect Flows)**  | This redirects the browser back to the source of the authentication request. This response provides information about the error that occurred.                                                              |

15. Click **Save**, then click **Deploy**.

16. If the main flow uses subflows, ensure that the subflows are not configured as PingOne flows.

    1. On the **Flows** tab, find the flow and click …​ > Edit.

    2. Click **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings** to show the flow settings.

    3. Select the **PingOne Flow** option.

    4. Click **Save**, then close the **Flow Settings** pane.

    5. Repeat these steps for each additional subflow.

## Creating a DaVinci application

Create an application in DaVinci to enable your flow.

### Steps

1. Sign on to DaVinci.

2. On the **Applications** tab, click **Add Application**.

   #### Result:

   The **Add Application** modal opens.

3. In the **Name** field, enter a name for the application.

4. Click **Create**.

5. Find the application and click **Edit**.

6. On the **OIDC** tab, note the application parameters for the following:

   * **Company ID**

   * **Client ID**

   * **Client Secret**

   * **Issuer**

   * **Token Endpoint**

   * **JWKS Endpoint**

7. Create a flow policy:

   1. On the **Flow Policy** tab, click **[icon: plus, set=fa]Add Flow Policy**..

   2. In the **Name** field, enter a name for the flow policy.

   3. Select **PingOne Flow Policy**.

   4. In the flow list, select your flow.

   5. In the version list, select **Latest Version**.

   6. Click **Create Flow Policy**.

      ##### Result:

      The **Edit Your Weight Distribution** modal opens.

      |   |                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | This example only uses one flow, but if your flow policy included multiple flows or flow versions, you could use this modal to split traffic between them. |

   7. Click **Save Flow Policy**.

   8. Note the **Policy ID** of your flow policy.

## Configuring PingOne for flow invocation

Configure an application in PingOne to launch flows.

### About this task

The PingOne application is used as part of the flow invocation process.

### Steps

1. Sign on to PingOne and go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon.

3. In the **Application Name** field, enter a name for the application.

4. In the **Application Type** section, select an application type corresponding to your platform:

   * If you're using the Ping SDK for JavaScript, select **OIDC Web App**.

   * If you're using the Ping SDK for iOS or Android, select **Native**.

   ![A screen capture of the OIDC Web App Application Type options. The OIDC Web App and Native Application Types options are indicated with a red border.](_images/DV_SDK_invocation_application_type.png)

5. Click **Save**.

6. On the **Policies** tab, click **Add Policies**.

7. On the **DaVinci Policies** tab, select one or more flow policies to add to the application.

   |   |                                                                      |
   | - | -------------------------------------------------------------------- |
   |   | Only flow policies with the **PingOne Policy** option are displayed. |

8. Click **Save**.

9. If you're using the Ping SDK for JavaScript, configure CORS settings for your application.

   1. On the **Configuration** tab, click the **Pencil** icon.

   2. In the **CORS Settings** section, select **Allow specific origins**.

   3. In the **Allowed Origins** field, enter the domain from which you plan to launch the flow.

   4. Click **Save**.

## Invoking the flow

To launch the flow, construct a link with the PingOne details and add it to the resource that will launch the flow. You must download the Ping SDKs and create a user experience that launches the flow.

To create the link, you need the following values:

* Client ID

* Redirect URI

* Scopes

* OIDC Discovery Endpoint

Learn more about creating the link and launching the flow in the [SDK documentation](http://docs.pingidentity.com/sdks/latest/davinci/tutorials.html).

---

---
title: Launching a flow with an API call
description: Launch a prepared flow with an API call.
component: davinci
page_id: davinci:integrating_flows_into_applications:davinci_launching_a_flow_with_an_api_call
canonical_url: http://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_an_api_call.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  configuring-the-flow: Configuring the Flow
  about-this-task: About this task
  steps: Steps
  creating-an-application: Creating an Application
  about-this-task-2: About this task
  steps-2: Steps
  adding-cors-settings-in-pingone: Adding CORS Settings in PingOne
  steps-3: Steps
  invoking-the-flow: Invoking the Flow
  steps-4: Steps
  examples: Examples
---

# Launching a flow with an API call

Launch a prepared flow with an API call.

This method is effective for flows without a UI component.

## Configuring the Flow

Prepare a flow to be launched with an API call.

### About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure only covers the steps and nodes required to prepare a flow for API invocation. It assumes that you have already created a flow for the purpose you have in mind. See the [Getting started with DaVinci](../flows/davinci_getting_started.html) and [DaVinci Best Practices](../davinci_best_practices/davinci_best_practices.html) documentation for more information about building flows. |

### Steps

1. Click the **Flows** tab.

2. Find the flow and click **... > Edit**

3. At the end of the success path, add an HTTP node to send a JSON success response.

4. At the end of any failure paths, add an HTTP node to send a JSON error response.

5. (Optional) If you want to pass parameters to the flow as part of the invocation, add them to the input schema.

   1. Click **Input Schema**.

   2. Click **Add** to add a new parameter.

   3. In the **Parameter Name** field, enter a name for the input parameter.

   4. (Optional) In the Description field, enter a description for the input parameter.

   5. In the **Data Type** list, select a data type for the input parameter.

   6. Select **Required** if the parameter is required for the flow.

   7. (Optional) Repeat steps b-f to add additional parameters.

   8. Click **Save**.

6. Click **Save**.

7. Click **Deploy**.

## Creating an Application

Create an application in DaVinci to enable your flow.

### About this task

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | If you want to use an existing application to launch the flow, you can start at step 5. |

### Steps

1. Click the **Applications** tab.

2. Click **Add Application**.

   The **Add Application** modal opens.

3. In the **Name** field, enter a name for the application.

4. Click **Create**.

5. Find the application and click **Edit**.

6. On the **General** tab, note the following parameters:

   1. Note the **Company ID**.

   2. Note the **API Key**.

7. Create a flow policy:

   1. Click the **Flow Policy** tab.

   2. Click **[icon: plus, set=fa]Add Flow Policy**.

   3. In the **Name** field, enter a name for the flow policy.

   4. In the flow list, select your flow.

   5. In the version list, select **Latest Version**.

   6. Click **Create Flow Policy**.

      |   |                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | This example only uses one flow, but if your flow policy included multiple flows or flow versions, you could use this modal to split traffic between them. |

   7. Click **Save Flow Policy**.

   8. Note the **Policy ID** of your flow policy.

## Adding CORS Settings in PingOne

Add the domain from which the flow will be launched to the DaVinci application in PingOne to prevent CORS issues.

### Steps

1. Sign on to PingOne and go to **Applications** > **Applications**.

2. Click the **PingOne DaVinci Connection** application.

   You can also add the CORS setting to any other PingOne application. For tracking and consistency, we recommend adding the CORS setting to the PingOne DaVinci application.

3. Click the **Configuration** tab.

4. Click the **Pencil** icon.

5. In the **CORS Settings** section, select **Allow specific origins**.

6. In the **Allowed Origins** field, enter the domain from which you plan to launch the flow.

7. Click **Save**.

## Invoking the Flow

### Steps

1. Using a tool such as Postman, construct the DaVinci API call using the POST method and the following URL structure:

   ```
   https://orchestrate-api.pingone.com/v1/company/<YOUR_COMPANY_ID>/policy/<YOUR_POLICY_ID>/start
   ```

   The headers should include your API key using the following format.`X-SK-API-KEY=<YOUR_API_KEY>`

   You can include one or more parameters in the call. If you do so, you must include these parameters in the input schema for the flow. The following examples include a `userId` parameter.

2. Execute the API call. The response body will be the output from the **Send Success JSON Response** action.

### Examples

cURL

```shell
curl
--location
--request POST 'https://orchestrate-api.pingone.com/v1/company/731f6c64-619a-46e5-97a5-c7cf0be0a70e/policy/e31c3b327523685b8e71ab9d76c83346/start' \
--header 'X-SK-API-KEY: 08cfa...45a6d'
--header 'Content-Type: application/json'
--data '{
    "userId": "b7e5ad3e-ccbd-4043-b22e-8d6d3bf8f7be"
}'
```

JavaScript and Fetch:

```javascript
const myHeaders = new Headers();
myHeaders.append("X-SK-API-Key",
"08cfa...45a6d");
myHeaders.append("Content-Type", "application/json");

const raw = JSON.stringify({
  "userId": "b7e5ad3e-ccbd-4043-b22e-8d6d3bf8f7be"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://orchestrate-api.pingone.com/v1/company/731f6c64-619a-46e5-97a5-c7cf0be0a70e/policy/e31c3b327523685b8e71ab9d76c83346/start", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

JavaScript and NodeJS - Axios:

```javascript
const axios = require('axios');
let data = JSON.stringify({
  "userId": "b7e5ad3e-ccbd-4043-b22e-8d6d3bf8f7be"
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://orchestrate-api.pingone.com/v1/company/731f6c64-619a-46e5-97a5-c7cf0be0a70e/policy/e31c3b327523685b8e71ab9d76c83346/start',
  headers: {
    'X-SK-API-Key': '08cfa...45a6d',
    'Content-Type': 'application/json'
  },
  data : data
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});
```

---

---
title: Launching a flow with the widget
description: Launch a prepared flow with a widget.
component: davinci
page_id: davinci:integrating_flows_into_applications:davinci_launching_a_flow_with_the_widget
canonical_url: http://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_the_widget.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  configuring-the-flow: Configuring the Flow
  about-this-task: About this task
  steps: Steps
  creating-an-application: Creating an Application
  about-this-task-2: About this task
  steps-2: Steps
  adding-cors-settings-in-pingone: Adding CORS Settings in PingOne
  steps-3: Steps
  integration-example: Integration example
  html-invocation-code: HTML invocation code
  server-side-javascript-code: Server-side JavaScript code
  getting-the-sdk-token: Getting the SDK token
  using-the-widget-with-a-return-url: Using the widget with a return URL
  limiting-the-cookies-passed-by-the-widget: Limiting the cookies passed by the widget
---

# Launching a flow with the widget

Launch a prepared flow with a widget.

This method is effective when you want to launch the flow within the current page instead of redirecting the user.

|   |                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * You can't launch the DaVinci widget in an iframe.

* You can find information on switching between using a flow for a PingOne redirect integration and an integration using the DaVinci widget in [Switching between PingOne and DaVinci widget integrations](davinci_switch_between_flow_integrations.html). |

## Configuring the Flow

Prepare a flow to be launched with the widget.

### About this task

|   |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * This procedure only covers the steps and nodes required to prepare a flow for widget invocation. It assumes that you have already created a flow for the purpose you have in mind. See the [Getting started with DaVinci](../flows/davinci_getting_started.html) and [DaVinci Best Practices](../davinci_best_practices/davinci_best_practices.html) documentation for more information about building flows. |

### Steps

1. Click the **Flows** tab.

2. Find the flow and click **... > Edit**

3. Add a nonce to the input schema.

   |   |                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you launch the flow, you provide a nonce value. This value is returned when the flow completes, letting you verify the flow's completion. |

   1. Click **Flow Options ( [icon: ellipsis-v, set=fa]) > Input Schema**.

   2. Click **Add**.

   3. In the **Parameter Name** field, enter `nonce`.

   4. In the **Data Type** list, select **String**.

   5. Select **Required**.

   6. Click **Save**.

4. At the end of the success path, add a PingOne Authentication node or an HTTP node to send a success response.

5. At the end of any failure paths, add a PingOne Authentication node or an HTTP node to send an error response.

6. Click **Save**.

7. Click **Deploy**.

## Creating an Application

Create an application in DaVinci to enable your flow.

### About this task

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | If you want to use an existing application to launch the flow, you can start at step 5. |

### Steps

1. Click the **Applications** tab.

2. Click **Add Application**.

   The **Add Application** modal opens.

3. In the **Name** field, enter a name for the application.

4. Click **Create**.

5. Find the application and click **Edit**.

6. On the **General** tab, note the following parameters:

   1. Note the **Company ID**.

7. Create a flow policy:

   1. Click the **Flow Policy** tab.

   2. Click **[icon: plus, set=fa]Add Flow Policy**.

   3. In the **Name** field, enter a name for the flow policy.

   4. In the flow list, select your flow.

   5. In the version list, select **Latest Version**.

   6. Click **Create Flow Policy**.

      The **Edit Your Weight Distribution** modal opens.

      |   |                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | This example only uses one flow, but if your flow policy included multiple flows or flow versions, you could use this modal to split traffic between them. |

   7. Click **Save Flow Policy**.

   8. Note the **Policy ID** of your flow policy.

## Adding CORS Settings in PingOne

Add the domain from which the flow will be launched to the DaVinci application in PingOne to prevent CORS issues.

### Steps

1. Sign on to PingOne and go to **Applications** > **Applications**.

2. Click the **PingOne DaVinci Connection** application.

   You can also add the CORS setting to any other PingOne application. For tracking and consistency, we recommend adding the CORS setting to the PingOne DaVinci application.

3. Click the **Configuration** tab.

4. Click the **Pencil** icon.

5. In the **CORS Settings** section, select **Allow specific origins**.

6. In the **Allowed Origins** field, enter the domain from which you plan to launch the flow.

7. Click **Save**.

## Integration example

This example is a simple hello-world application that launches a flow using the widget. The HTML code specifies the flow policy ID. A server-side JavaScript process securely provides the API key and company ID. The example checks for an existing user session, which is stored in a cookie created by the Return Success node during a previous flow execution.

|   |                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following example won't work unless you add your region-specific information. Replace any instances of `<region>` with your regional top-level domain:- Use `.com` for North America.

- Use `.ca` for Canada.

- Use `.eu` for EMEA.

- Use `.asia` for APAC.

- Use `.com.au` for Australia. |

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following example uses the `davinci.js` widget file, which uses default DaVinci CSS rules. To invoke the flow without using the default DaVinci CSS rules, use the `davinci-no-css.js` widget file. |

### HTML invocation code

```html
<!DOCTYPE html>
<html lang="en">
<meta charset="UTF-8" />

<head>
    <title>Simple HTML/JS widget Testing</title>
    <link rel="stylesheet" href="https://assets.pingone.<region>/ux/end-user-nano/0.1.0-alpha.9/end-user-nano.css" />
    <link rel="stylesheet" href="https://assets.pingone.<region>/ux/astro-nano/0.1.0-alpha.11/icons.css" />
</head>

<body>
    <h3>Simple HTML/JS widget Test</h3>
    <br />
    <p>Widget will be displayed below</p>
    <br />
    <div id="widget" class="dvWidget"></div>
    <script type="text/javascript" src="https://assets.pingone.<region>/davinci/latest/davinci.js"></script>
    <script>
        // Only the policyId is needed on the frontend.
        // API keys and companyId are securely managed server-side in bxi-server.js.
        const policyId = "<policy_id>";

        // Helper function to set a cookie with security flags
        const setCookie = (name, value, options = {}) => {
            let cookieString = `${name}=${encodeURIComponent(value)}`;

            // Set expiration (default: session cookie, or 1 day if specified)
            if (options.maxAge !== undefined) {
                cookieString += `; Max-Age=${options.maxAge}`;
            }

            // Security flags for best practices
            cookieString += "; Secure"; // Only transmit over HTTPS
            cookieString += "; SameSite=Strict"; // Prevent CSRF attacks

            // Note: HttpOnly flag cannot be set from JavaScript and must be set server-side
            // For full security, consider having your backend endpoint set the cookie

            document.cookie = cookieString;
        };

        // Callback functions
        const successCallback = (response) => {
            console.log(response);
            // Store DaVinci session token in a secure cookie (1 day expiration).
            // The server reads this as "DV-ST" to maintain session continuity.
            setCookie("DV-ST", response.sessionToken, { maxAge: 86400 });
        };

        const errorCallback = (error) => {
            console.log(error);
        };

        const onCloseModal = () => {
            console.log("onCloseModal");
        };

        // Initialize and render the DaVinci widget
        (async () => {
            try {
                // Request a DaVinci SDK token from the backend server.
                // The server handles API key management and session token forwarding
                // so that sensitive credentials are never exposed to the browser.
                const tokenResponse = await fetch("/dvtoken", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    credentials: "include", // Send cookies (DV-ST) to the server
                    body: JSON.stringify({ policyId }),
                });

                if (!tokenResponse.ok) {
                    const errorData = await tokenResponse.json();
                    throw new Error(errorData.error || "Failed to retrieve DaVinci SDK token from server.");
                }

                // Server returns { token, companyId, apiRoot }
                const { token, companyId, apiRoot } = await tokenResponse.json();

                const props = {
                    config: {
                        method: "runFlow",
                        apiRoot: apiRoot,
                        accessToken: token,
                        includeHttpCredentials: true, //either true or false. Set this to true to share cookies
                        staggerFlowExecutions: false, //Set this to true to allow multiple flow executions, with one active and others paused
                        flowTakeoverWaitTimeSeconds: 5, //The delay before a paused flow begins execution, between 3 and 15.
                        lockAcquisitionTimeoutSeconds: 300, //The timeout value for a paused flow, between 30 and 1200.
                        companyId,
                        policyId
                        // parameters: {
                        //     nonce: "string to validate",
                        // },
                    },
                    useModal: false,
                    successCallback,
                    errorCallback,
                    onCloseModal,
                };

                // Invoke the Widget
                console.log(props);
                davinci.skRenderScreen(
                    document.querySelector(".dvWidget"),
                    props
                );
            } catch (error) {
                console.error("Error initializing DaVinci widget:", error);
            }
        })();
    </script>
</body>

</html>
```

### Server-side JavaScript code

```javascript
const Fastify = require('fastify');
const fastifyCookie = require('@fastify/cookie');
const fastifyCors = require('@fastify/cors');
const fastifyStatic = require('@fastify/static');
const dotenv = require('dotenv');
const path = require('path');

// Load environment variables from .env file (relative to this script's directory)
dotenv.config({ path: path.join(dirname, '.env') });

// Initialize Fastify with logging enabled
const fastify = Fastify({ logger: true });

// Register the @fastify/cookie plugin for request.cookies support
fastify.register(fastifyCookie);

// Register CORS to allow browser requests (credentials: true for cookie support)
fastify.register(fastifyCors, {
  origin: true,
  credentials: true,
});

// Serve static files (HTML, CSS, JS) from the current directory
fastify.register(fastifyStatic, {
  root: path.join(dirname),
  prefix: '/',
});

// Get a dv token from the server, we do this in server.js as a security best practice so
// API Keys don't need to be exposed on the front-end.
fastify.post('/dvtoken', {
  schema: {
    body: {
      type: 'object',
      required: ['policyId'],
      properties: {
        policyId: { type: 'string' },
        apiKey: { type: 'string' },
        companyId: { type: 'string' },
        flowParameters: { type: 'object' },
      },
    },
  },
}, async function (request, reply) {
  // Allow for apiKey and companyId overrides to come from front end, even though it's not encouraged.
  // Optional chaining guards against null/undefined values for optional body properties.
  const apiKey = request.body?.apiKey || process.env.BXI_API_KEY;
  const companyId = request.body?.companyId || process.env.BXI_COMPANY_ID;

  let body = {
    policyId: request.body.policyId,
  };

  if (request.cookies?.['DV-ST']) {
    body.global = {
      sessionToken: request.cookies['DV-ST'],
    };
  }

  if (request.body?.flowParameters) {
    body.parameters = request.body.flowParameters;
  }

  const dvBaseUrl = `${process.env.BXI_API_URL}/`;
  const dvSdkTokenBaseUrl = `${process.env.BXI_SDK_TOKEN_URL}/v1`;

  const tokenRequest = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-SK-API-KEY': apiKey,
    },
    body: JSON.stringify(body),
  };

  const tokenResponse = await fetch(
    `${dvSdkTokenBaseUrl}/company/${companyId}/sdktoken`,
    tokenRequest
  ); // Endpoint is case sensitive in Davinci V2
  const parsedResponse = await tokenResponse.json();

  if (!parsedResponse?.success) {
    request.log.error('An error occurred getting DaVinci token');
    request.log.error({ parsedResponse }, 'Parsed Response');
    return reply.code(500).send({
      error: `An error occurred getting DaVinci token. See server logs for more details, code: ${parsedResponse?.httpResponseCode}, message: '${parsedResponse?.message}'.`,
    });
  }

  request.log.info('Successfully retrieved sdktoken for DaVinci');

  return reply.send({
    token: parsedResponse.access_token,
    companyId: companyId,
    apiRoot: dvBaseUrl,
  });
});

// Start the server
const start = async () => {
  try {
    const port = process.env.PORT || 3000;
    await fastify.listen({ port, host: '0.0.0.0' });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
```

## Getting the SDK token

When implementing a DaVinci application integration using the widget method, be aware that the `POST <authPath>/<companyID>/davinci/policy/<davinciFlowPolicyID>/start` request that invokes the flow takes an SDK token to authenticate. However, the call to get a DaVinci SDK token, `GET <orchestratePath>/company/<companyID>/sdktoken`, requires the application's API key to authenticate.

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `/sdktoken` call must be executed on the server side, not in client-side code, to protect the application's API key from exposure on a public web page. |

The following sample shows a server-side code snippet from a `server.js` file used to generate the DaVinci SDK token without exposing the application's API key. You can use this in your server-side code if you already have a server-side component. It's not necessary if you're using the example described in the previous section.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The sample won't work unless you add your region-specific information. Replace any instances of *\<region>* with your regional top-level domain:- Use `.com` for North America.

- Use `.ca` for Canada.

- Use `.eu` for EMEA.

- Use `.asia` for APAC.

- Use `.com.au` for Australia. |

```javascript
/************************
* DaVinci components
************************/

// Get a Widget sdkToken
function getDVToken(cb) {
  const url = 'https://orchestrate-api.pingone.<region>/v1/company/${companyId}/sdktoken';
  fetch(url, {
    headers: {
      "X-SK-API-KEY":  <DV API Key>
    },
    method: "GET"
  })
  .then(res => res.json())
  .then(data => cb(data))
  .catch(err => console.log("Error: ", err));
}
```

## Using the widget with a return URL

When using the widget with social providers, PingID, or other services requiring you to supply a return URL, add coding similar to this.

Retrieve the value for a `continueToken`.

```javascript
/**
 * Event listener for window.load()
 * Listening for a query parameter of `continueToken`
 */
window.addEventListener('load', (event) => {
  var urlParams = new URLSearchParams(window.location.search);
  if (urlParams.get('continueToken')) {
    // flush parameter from window url
    window.history.pushState({}, document.title, window.location.pathname);
    continueWidget('policyId', 'authnflow', urlParams.get('continueToken'))
  }
});
```

Invoke the widget and continue the flow using the `continueToken`.

|   |                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following example won't work unless you add your region-specific information. Replace any instances of `<region>` with your regional top-level domain:- Use `.com` for North America.

- Use `.ca` for Canada.

- Use `.eu` for EMEA.

- Use `.asia` for APAC.

- Use `.com.au` for Australia. |

```javascript
/**
 * Recreates an instance of the Widget placed on the page,
 * and uses the provided 'continueToken' value instead of fetching a new one from DaVinci
 * @param {string} policyId - The flow policy ID for the widget to run
 * @param {string} divId - Location on the page to place the Widget
 * @param {string} continueToken - Value of the 'continueToken' query parameter
 */
function continueWidget(policyId, divId, continueToken){
  /**
   * Creates an instance of the Widget with the following:
   * @param {object} props - Properties for the Widget execution
   * @param {object} props.config - Object containing the Widget configuration
   * @param {string} props.config.method - Widget run method { "runFlow" | "continueFlow" }
   * @param {string} props.config.apiRoot - URL of the DaVinci instance for this flow
   * @param {string} props.config.accessToken - @param {string} continueToken
   * @param {string} props.config.companyId - ID of the PingOne environment that contains the flow
   * @param {string} props.config.policyId - Flow policy ID for the Widget to run
   * @param {boolean} props.useModal - Present Widget as a modal, instead of embedded
   * @param {requestCallback} props.successCallback - The callback that handles the Success response
   * @param {requestCallback} props.errorCallback - The callback that handles the Error response
   * @param {requestCallback} props.onCloseModal - The callback that handles the modal close response ('useModal' == true)
   */
  var props= {
    config: {
      method: 'continueFlow',
      apiRoot: 'https://auth.pingone.<region>/',
      accessToken: continueToken,
      companyId:  <companyID>,
      policyId: policyId`
    },
    useModal: false,
    successCallback, errorCallback, onCloseModal
    }
    /*** Invoke DaVinci Widget ****/
    davinci.skRenderScreen(document.getElementById(divId),props)
  }
```

## Limiting the cookies passed by the widget

By default, the widget passes to DaVinci all cookies that could be presented to the origin. There can be a large number of cookies, only some of which are likely to be used for your DaVinci flows. In some cases, this can cause a `431 Error: Request Header Fields Too Large`. To avoid this possibility, you can set the `originCookies` property.

The `originCookies` property is optional and accepts a string array of cookie names. Only the cookies specified will be passed by the widget to DaVinci. Set this as you would any of the DaVinci properties.

|   |                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following example won't work unless you add your region-specific information. Replace any instances of `<region>` with your regional top-level domain:- Use `.com` for North America.

- Use `.ca` for Canada.

- Use `.eu` for EMEA.

- Use `.asia` for APAC.

- Use `.com.au` for Australia. |

```javascript
var props= {
   config: {
     apiRoot: 'https://auth.pingone.<region>/',
     companyId:  <companyID>,
     policyId:  <policyId>,
     originCookies: ["cookie-1", "cookie-2"]
   }
}
```

To disable passing cookies from the widget, set `originCookies` to an empty array.

---

---
title: Launching a PingOne flow with a redirect
description: You can configure PingOne and DaVinci so that you can invoke specifically-configured flows through PingOne.
component: davinci
page_id: davinci:integrating_flows_into_applications:davinci_launch_flow_redirect
canonical_url: http://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launch_flow_redirect.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  configuring-a-davinci-flow-for-invocation: Configuring a DaVinci flow for invocation
  about-this-task: About this task
  steps: Steps
  using-pingone-connectors: Using PingOne connectors
  referencing-pingone-data-in-the-flow: Referencing PingOne data in the flow
  configuring-a-davinci-flow-policy-for-invocation: Configuring a DaVinci flow policy for invocation
  about-this-task-2: About this task
  steps-2: Steps
  configuring-pingone-for-flow-invocation: Configuring PingOne for flow invocation
  about-this-task-3: About this task
  steps-3: Steps
  choose-from: Choose from:
  invoking-the-flow: Invoking the flow
  steps-4: Steps
---

# Launching a PingOne flow with a redirect

You can configure PingOne and DaVinci so that you can invoke specifically-configured flows through PingOne.

This approach lets you launch your flows from PingOne and lets you reference and modify user data from PingOne within the flow.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To switch between using a flow for a DaVinci widget integration and an integration using a PingOne redirect, see [Switching between PingOne and DaVinci widget integrations](davinci_switch_between_flow_integrations.html). |

## Configuring a DaVinci flow for invocation

Update a DaVinci flow to enable it to be launched through PingOne.

### About this task

This procedure assumes that the flow already exists or is in progress, and only specifies the necessary nodes and settings for invocation through PingOne. For more information about creating flows, see [Getting started with DaVinci](../flows/davinci_getting_started.html).

### Steps

1. Sign on to DaVinci and click the **Flows** tab.

2. Select the flow tile for the flow that you plan to launch through PingOne.

3. Click **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings** to show the flow settings.

4. Select the **PingOne Flow** option.

5. Click **Save**, then close the **Flow Settings** pane.

6. End the flow with the following two **PingOne Authentication** nodes, one for success and one for failure.

   ![A screen capture of a flow ending with a success and failure path.](_images/kuw1674237257955.png)

   | Node                                           | Purpose                                                                                                                                                                                                                      |
   | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Return a Success Response (Redirect Flows)** | This creates a PingOne session for the user and redirects the browser back to the source of the authentication request. This response provides the requested scopes as well as an access token, ID token, or SAML assertion. |
   | **Return an Error Response (Redirect Flows)**  | This redirects the browser back to the source of the authentication request. This response provides information about the error that occurred.                                                                               |

7. Click **Save**, then click **Deploy**.

## Using PingOne connectors

Add PingOne connectors to your environment to use PingOne capabilities in your flows.

Learn more about the available PingOne connectors in [Core connectors](../connectors/davinci_core_connectors.html). If you plan to launch flows through PingOne, you must add the PingOne Authentication connector to your environment.

## Referencing PingOne data in the flow

You can reference data from PingOne within your flow.

The format for this information is `global.parameters.<parameter name>`. Some parameters depend on the protocol used to launch the flow, while others are supplied by the PingOne application.

OIDC parameters

| Property                                     | Description                                                                                                                                                                                                                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `authorizationRequest`                       | An object that specifies all the parameters from the OIDC authorization request.                                                                                                                                                                                                |
| `authorizationRequest.<customParameter>`     | A string that specifies a custom URL parameter added to the OIDC authorization request. Replace *\<customParameter>* with the name of the custom URL parameter.                                                                                                                 |
| `authorizationRequest.client_id`             | A string that specifies the client ID of the application associated with this authorize request.                                                                                                                                                                                |
| `authorizationRequest.redirect_uri`          | A string that specifies the URL of the return entry point of the application.                                                                                                                                                                                                   |
| `authorizationRequest.response_type`         | A string that specifies the code or token type returned by an authorization request. Options are `token`, `id_token`, and `code`.                                                                                                                                               |
| `authorizationRequest.scope`                 | A string that specifies the permissions that determine the resources that the application can access.                                                                                                                                                                           |
| `authorizationRequest.state`                 | A string that maintains the state between the logout request and the callback to the endpoint specified by the `post_logout_redirect_uri` query parameter.                                                                                                                      |
| `authorizationRequest.nonce`                 | A string that is used to associate a client session with a token to mitigate replay attacks. The value is passed through unmodified from the authentication request to the token. This is an optional property for authorization requests that return a code.                   |
| `authorizationRequest.acr_values`            | A string that is used by the flow designer to pass in useful information.                                                                                                                                                                                                       |
| `authorizationRequest.login_hint`            | A string that is used to designate a login identifier to pre-fill the **username** field of the sign-on screen.                                                                                                                                                                 |
| `authorizationRequest.max_age`               | A string that specifies the maximum amount of time allowed (in seconds) since the user last authenticated. If the `max_age` value is exceeded, the user must re-authenticate. If the `max_age` value is set to 0 (`max_age=0`), the user is always required to re-authenticate. |
| `authorizationRequest.prompt`                | A string that specifies whether the user is prompted to sign on for re-authentication. The prompt parameter can be used as a way to check for existing authentication, verifying that the user is still present for the current session.                                        |
| `authorizationRequest.response_mode`         | A string that specifies the mechanism for returning authorization response parameters from the authorization endpoint. Options are `query`, `fragment`, and `form_post`.                                                                                                        |
| `authorizationRequest.code_challenge`        | A string that is computed from the `code_verifier` that is used in a Proof Key for Code Exchange (PKCE) authorization request.                                                                                                                                                  |
| `authorizationRequest.code_challenge_method` | A string that specifies the computation logic used to generate the `code_challenge` string. The token endpoint uses this method to verify the `code_verifier` for PKCE authorization requests. Options are `plain` and `S256`.                                                  |
| `authorizationRequest.code_verifier`         | A string that is used to create the `code_challenge` value passed to the authorization server in the request.                                                                                                                                                                   |
| `authorizationRequest.mobileRequest`         | An object that specifies OIDC/OAuth2 request parameters.                                                                                                                                                                                                                        |

For example, the following code references the login hint in a flow launched using OIDC:

```none
global.parameters.authorizationRequest.login_hint
```

SAML parameters

| Property                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `samlRequest`                       | A string that specifies all the parameters from the SAML request.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `samlRequest.spEntityId`            | A string that specifies the service provider entity ID used to look up the application. This is a required property and is unique within the environment.                                                                                                                                                                                                                                                                                                                                                    |
| `samlRequest.forceAuthn`            | A boolean that, when set to true, specifies that the identity provider must authenticate the presenter directly rather than rely on a previous security context. If a value is not provided, the default value is false.                                                                                                                                                                                                                                                                                     |
| `samlRequest.passive`               | A boolean that, when set to true, specifies that the identity provider and the user agent itself must not visibly take control of the user interface from the requester and interact with the presenter in a noticeable fashion. If a value is not provided, the default value is false.                                                                                                                                                                                                                     |
| `samlRequest.signed`                | A boolean that specifies whether the SAML assertion should be signed. The default value is false.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `samlRequest.subject`               | A string that specifies the SAML subject ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `samlRequest.requestedAuthnContext` | A string that specifies the authentication methods for the request.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `samlRequest.<RequestParameter>`    | A string or array that contains the value or values of any HTTP request parameter included in the **Initiate Single Sign-On URL**, up to a maximum of 4096 characters.For example, if the **Initiate Single Sign-On URL** used was:`https://sso.example.ca/saml20/idp/startsso?spEntityId=SP&key1=valueA&key2=valueB&key2=valueC`The **samlRequest.key1** parameter would be a string with a value of `valueA`. The **samlRequest.key2** parameter would be an array with a value of `["valueB", "valueC"]`. |

For example, the following code references the subject ID in a flow launched using SAML:

```none
global.parameters.samlRequest.subject
```

WS-Federation parameters

| Property              | Description                                                                                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `wsFedRequest.wfresh` | The maximum age of authentication in minutes. If the value is 0, the user should be prompted for authentication before a token is issued.                                                                                                                                                  |
| `wsFedRequest.wauth`  | The required authentication level.                                                                                                                                                                                                                                                         |
| `wsFedRequest.wctx`   | An opaque context value that can be passed in the request.When the invoked DaVinci flow completes successfully and returns to PingOne, PingOne echoes this value back to the service provider with the issued token if it was included by the service provider in the originating request. |
| `wsFedRequest.whr`    | The account partner realm of the client.                                                                                                                                                                                                                                                   |

Application parameters

| Property                  | Description                                                                                                                                                                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `application`             | An object that specifies the configuration information about the PingOne application that initiated the authentication request.                                                                                                                            |
| `application.homePageUrl` | A string that specifies the custom home page URL for the application.                                                                                                                                                                                      |
| `application.id`          | A string that specifies the application ID.                                                                                                                                                                                                                |
| `application.name`        | A string that specifies the application name.                                                                                                                                                                                                              |
| `application.protocol`    | A string that specifies the protocol for the application. Options are OPENID\_CONNECT and SAML.                                                                                                                                                            |
| `application.type`        | A string that specifies the application type. Valid values are `WEB_APP`, `NATIVE_APP`, `SINGLE_PAGE_APP`, `SERVICE`, `CUSTOM_APP`, `WORKER`, `PING_ONE_SELF_SERVICE`, `PING_ONE_ADMIN_CONSOLE`, `PING_ONE_PORTAL`, `TEMPLATE_APP`, and `PORTAL_LINK_APP`. |

For example, the following code references the application ID in a flow, regardless of the protocol used to launch the flow:

```none
global.parameters.application.id
```

Universal parameters

| Property                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `loginHint`                 | A string that specifies an identifier to pre-fill the **username** field of a sign-on screen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `maxSecondsSinceLastSignOn` | An integer that specifies the maximum amount of time allowed (in seconds) since the user last authenticated. If the user's last sign on in the session is greater than the integer value specified in this property, then existing session information cannot be used to skip authentication or influence any authentication logic. This value is set automatically to 0 if `prompt=login` is set for an OIDC application or if `ForceAuthn=true` is set for a SAML application. Otherwise, this value is set to the `max_age` property value for OIDC applications, if present, or omitted otherwise. |

For example, the following code references the login hint, regardless of the protocol used to launch the flow:

```none
global.parameters.loginHint
```

## Configuring a DaVinci flow policy for invocation

Configure a flow policy to specify which flow and which version of the flow you want to launch.

### About this task

Flows in DaVinci flows often have multiple versions as administrators make changes, and not all of these versions should be presented to users. A flow policy ensures that users see the correct version of the correct flow.

### Steps

1. Sign on to DaVinci and click the **Applications** tab.

2. Find the application and click **Edit**.

3. Click the **Flow Policy** tab.

4. Click **Add Flow Policy**.

5. In the **Name** field, enter a name for the flow policy.

6. Select **PingOne Flow Policy**.

7. Add one or more PingOne flows to the policy.

   |   |                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingOne flow policies can only include flows and flow versions that have the **PingOne Flow** setting enabled. Flows and versions without this setting cannot be selected. |

   1. In the **Flows** section, select a flow.

   2. In the **Version** section, select one or more versions of the flow.

      The **Latest Version** option always uses the latest version.

   3. (Optional) Repeat the previous steps to add additional flows.

8. Click **Create Flow Policy**.

   The **Edit Your Weight Distribution** modal opens.

9. Add weight distribution and analytics information for each flow and flow version:

   1. In the **Distribution** field for each flow version, enter or select a distribution weight from 1 to 100.

      |   |                                                                                                                    |
      | - | ------------------------------------------------------------------------------------------------------------------ |
      |   | The weight is used if the flow policy is invoked without a flow ID. You can use the weight to perform A/B testing. |

   2. (Optional) Click **Add IP Whitelist**.

   3. (Optional) In the **Whitelist IP** field, enter one or more IP addresses.

      |   |                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------- |
      |   | If a request comes from an allowed IP address, the weight is ignored, and the specified flow is triggered. |

   4. (Optional) In the **Analytics - Select Success Nodes** list, select one or more nodes that, when run, indicate that the flow run was successful.

      This information is used to calculate the flow policy's success rate.

10. Click **Save Flow Policy**.

## Configuring PingOne for flow invocation

Configure an application in PingOne to launch flows.

### About this task

The properties of the PingOne application are used as part of the URL that launches the flow.

### Steps

1. Sign on to PingOne and go to **Applications > Applications**.

2. Click the **[icon: plus, set=fa]**icon.

3. In the **Application Name** field, enter a name for the application.

4. In the **Application Type** section, select **OIDC Web App** or **SAML Application**.

5. If you selected **SAML Application**, provide the SAML configuration.

   1. Click **Configure**.

   2. Select a method for providing the application metadata.

      #### Choose from:

      * **Import Metadata**: Import the configuration details from an XML metadata file. Click **Select a File** and then select an XML metadata file on your system. Click **Open**.

        If the metadata file does not specify all the configuration values, you must enter the missing values manually.

      * **Import From URL**: Import the configuration details from a metadata URL. Enter the URL and then click **Import**.

        The URL must be a valid absolute URL.

      * **Manually Enter**: Enter the configuration details manually. In the **ACS URLs** field, enter the Assertion Consumer Service (ACS) URLs. You must specify at least one URL, and the first URL in the list is used as the default. In the **Entity ID** field, enter the service provider entity ID used to look up the application.

6. Click **Save**.

7. Click the **Policies** tab.

8. Click **[icon: plus, set=fa]Add Policies**.

9. Click the **DaVinci Policies** tab.

10. Select one or more flow policies to add to the application.

    Only flow policies with the **PingOne Policy** option are displayed.

11. Click **Save**.

12. Click the **Configuration** tab.

13. Click the **Pencil** icon.

14. In the **CORS Settings** section, select **Allow specific origins**.

15. In the **Allowed Origins** field, enter the domain from which you plan to launch the flow.

16. Click **Save**.

## Invoking the flow

To launch the flow, construct a link with the PingOne details and add it to the resource that will launch the flow.

### Steps

1. In the resource that will launch the flow, such as your organization's web application, add a call to your PingOne application using the following format:

   ```
   https://auth.pingone.com/<Environment ID>/as/authorize?response_type=<response type>
        &client_id=<client ID>
        &redirect_uri=<redirect URI>
        &scope=<scope>
        &acr_values=<Flow Policy ID>
        &<other parameter>=<value>
   ```

   The following parameters are used in the call:

   **Table 1. Parameters**

   | Parameter             | Required | Description                                                                           | Location                                                                                                                                                                  |
   | --------------------- | -------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Environment ID        | Yes      | The **Company ID** of the DaVinci application.                                        | Available in DaVinci in the **Company** tab, or in the details section at the top of any flow or application.                                                             |
   | Response Type         | Yes      | The response type expected by the PingOne application.                                | Available in PingOne under **Applications > Applications**. Click your application, then click the **Configuration** tab and find the **Response Type** field.            |
   | Client ID             | Yes      | The PingOne application's Client ID.                                                  | Available in PingOne under **Applications > Applications**. Click your application, then click the **Configuration** tab and find the **Client ID** field.                |
   | Redirect URI          | Yes      | A redirect URI configured in PingOne.                                                 | Available in PingOne under **Applications > Applications**. Click your application, then click the **Configuration** tab and find the **Redirect URIs** field.            |
   | Scope                 | Yes      | The application request scope.                                                        | Available in PingOne under **Applications > Applications > Resources**. Click your application, then click the **Resources** tab and find the **Allowed Scopes** section. |
   | Flow Policy ID        | No       | A policy that determines which flow and version is run.                               | Available in DaVinci in the **Applications** tab. Select your application, then click the **Flow Policy** tab.                                                            |
   | Additional parameters | No       | You can pass in additional parameters to make their values available during the flow. | N/A                                                                                                                                                                       |

   |   |                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can reference the parameter values passed in with the invocation. The format is:```
   global.parameters.authorizationRequest.<parameter name>
   ``` |

2. If the user requires a token but the flow did not grant a token, make an API call to the PingOne token endpoint to grant the user a token. Use the [PingOne token authentication code](https://apidocs.pingidentity.com/pingone/platform/v1/api/#post-token-authorization_code) endpoint or the [Pingone client credentials](https://apidocs.pingidentity.com/pingone/platform/v1/api/#post-token-admin-app-client_credentials) endpoint.

---

---
title: Launching a PingOne flow with a redirect using an external IdP
description: You can configure PingOne and DaVinci so that you can invoke specifically-configured flows through PingOne. This method configures DaVinci as an identity provider (IdP) in PingOne.
component: davinci
page_id: davinci:integrating_flows_into_applications:davinci_launch_flow_redirect_external_idp
canonical_url: http://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launch_flow_redirect_external_idp.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  dv_p1_external_idp_credentials: Creating PingOne credentials
  steps: Steps
  dv_p1_external_idp_adding_connections: Adding PingOne connectors
  steps-2: Steps
  dv_p1_external_idp_preparing_a_flow: Preparing a flow
  dv_p1_external_idp_p1_connectors: Using PingOne connectors
  dv_p1_external_idp_creating_an_application: Creating an application
  steps-3: Steps
  dv_p1_external_idp_configuring_external_idp: Configuring an external IDP
  steps-4: Steps
  dv_p1_external_idp_invoking_the_flow: Invoking the flow
  steps-5: Steps
---

# Launching a PingOne flow with a redirect using an external IdP

You can configure PingOne and DaVinci so that you can invoke specifically-configured flows through PingOne. This method configures DaVinci as an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* in PingOne.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have not yet configured PingOne to launch DaVinci flows, follow the steps in [Launching a PingOne flow with a redirect](davinci_launch_flow_redirect.html) instead. |

## Creating PingOne credentials

Create a set of credentials for adding PingOne connections.

### Steps

1. Sign on to PingOne.

2. Create a worker app as described in the [PingOne documentation](http://docs.pingidentity.com/pingone/applications/p1_edit_application_worker.html).

3. Assign the following roles to the worker app:

   * Identity Data Admin

   * Environment Admin

4. Note the **Client ID**, **Client Secret**, and **Environment ID** for the worker app.

5. Click **Finish**.

6. Go to **Applications > Applications**, click the application to open the application details, and click the toggle switch in the upper right to enable the application.

## Adding PingOne connectors

Add one or more PingOne connectors in DaVinci to enable your flows to use PingOne-related capabilities such as reading or updating users.

### Steps

1. Sign on to DaVinci.

2. Click the **Connectors** tab.

3. Click **Add Connector**.

4. In the list of available connectors, select one of the PingOne connectors and click **[icon: plus, set=fa]**.

   * [PingOne](http://docs.pingidentity.com/connectors/p1_connector.html)

   * [PingOne Authentication](http://docs.pingidentity.com/connectors/p1_authentication_connector.html)

   * [PingOne Form](http://docs.pingidentity.com/connectors/forms_connector.html)

   * [PingOne Notifications](http://docs.pingidentity.com/connectors/p1_notifications_connector.html)

   * [PingOne RADIUS Gateway](http://docs.pingidentity.com/connectors/p1_radius_gateway_connector.html)

   * [PingOne Authorize](http://docs.pingidentity.com/connectors/p1az_connector.html)

   * [PingOne Credentials](http://docs.pingidentity.com/connectors/p1_credentials_connector.html)

   * [PingOne MFA](http://docs.pingidentity.com/connectors/p1_mfa_connector.html)

   * [PingOne Protect](http://docs.pingidentity.com/connectors/p1_protect_connector.html)

   * [PingOne Verify](http://docs.pingidentity.com/connectors/p1_verify_connector.html)

   The **New Connector** modal opens.

5. Enter a name for the new connector and click **Create**.

6. Find and click the newly-created connector in the list of your connectors.

7. Set up the connector configuration.

   |   |                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The **Client ID**, **Client Secret**, and **Environment ID** that you noted in the previous procedure are used to configure the PingOne connectors. |

8. Click **Apply**.

## Preparing a flow

Create a flow, then prepare it for implementation through an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* call to PingOne.

|   |                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure does not go into detail about creating a flow. See the other use cases for additional information about creating specific flows. The preparation steps apply regardless of the purpose of your flow. |

This implementation method launches the flow in a new page. The user is redirected to the flow, which replaces the previous page and uses a DaVinci URL.

This implementation method is simple and does not require the addition of a widget to the page. It's also well-suited for any type of flow. Because the flow takes the entire page, you must design the flow to match your own branding and style.

Depending on the purpose of the flow, you might want to include a token connector, which directs PingOne to mint a token for the user.

You can reference information from PingOne in your flow. The format for this information is `global.skOpenId.p1Oidc.<request object hierarchy>`, where the hierarchy is taken from the request object schema.

The full request object schema for OIDC is:

```json
"p1Oidc": {
  "id": "<ID value>",
  "environment": {
    "id": "<environment ID value>"
  },
  "application": {
    "id": "<application ID value>"
  },
  "user": {
    "id": "<user ID value>"
  },
  "request": {
    "http": {
      "remoteIp": "<remote IP value>",
      "userAgent": "<user agent information>",
      "headers": {
        "Accept-Language": [
          "<language value>"
        ]
      }
    },
    "oidc": {
      "responseTypes": [
        "<response type>"
      ],
      "acrValues": [
        "<acr value>"
      ],
      "scopes": [
        "<scope value>"
      ],
      "parameters": {
        <One or more parameter-value pairs>
```

The full request object schema for Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)* is:

```json
"p1Oidc": {
    "id": "<ID value>",
    "environment": {
        "id": "<environment ID value>"
    },
    "application": {
        "id": "<application ID value>"
    },
    "request": {
        "http": {
            "remoteIp": "<remote IP value>",
            "userAgent": "<user agent information>"
        },
        "saml": {
            "environmentId": "<environment ID value>",
            "urlContext": {
                "environmentId": "<environment ID value>",
                "customDomainHost": "<custom domain host value>,
                "hostUrl": "<host URL value>",
                "authHostUrl": "<URL value>",
                "idpEntityId": "<IDP entity ID value>",
                "internalIdpEntityId": "<internal IDP entity ID value>",
                "flowHeaders": {
                    "X-Forwarded-Host": "<host value>"
                },
                "host": "<host name>",
                "customDomain": <domain value>
            },
            "ssoInitialized": <value>,
            "requestBinding": <value>,
            "requestSigned": <value>,
            "ssoRequest": {
                "requestId": <ID value>,
                "version": <value>,
                "issueInstant": <value>,
                "destination": <value>,
                "consent": <value>,
                "spEntityId": "<security ID value>",
                "forceAuthn": <value>,
                "passive": <value>,
                "acsUrl": "<value>",
                "acsBinding": "<value>",
                "subject": <value>,
                "signed": <value>,
                "authnContextRef": <value>
            },
            "application": {
                "id": "<ID value>",
                "name": "<name value>",
                "protocol": "<value>",
                "enabled": <value>,
                "spEntityId": "<value>",
                "acsBinding": "<value>",
                "acsUrls": ["<value>"],
                "assertionDuration": <value>,
                "sloBinding": "<value>",
                "assertionSigned": <value>,
                "responseSigned": <value>,
                "environment": {
                    "id": "<value>"
                }
            },
            "user": <user name value>,
            "relayState": <value>,
            "idpIssuer": "<issuer value>",
            "attributes": <value>
        }
    }
}
```

For example, the following code references the remote IP:

```none
global.skOpenId.p1Oidc.request.http.remoteIp
```

|   |                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Any property you reference must be included by the configured scopes, as described in the [Configuring an external IDP](#dv_p1_external_idp_configuring_external_idp) section. |

## Using PingOne connectors

Add PingOne connectors to your environment to use PingOne capabilities in your flows.

Learn more about the available PingOne connectors in [Core connectors](../connectors/davinci_core_connectors.html). If you plan to launch flows through PingOne, you must add the PingOne Authentication connector to your environment.

## Creating an application

Create an application in DaVinci to enable your flow.

### Steps

1. Sign on to DaVinci.

2. Click the **Applications** tab.

3. Click **Add Application**.

   The **Add Application** modal opens.

4. In the **Name** field, enter a name for the application.

5. Click **Create**.

6. Find the application and click **Edit**.

7. On the OIDC tab, note the application parameters for the following:

   * **Company ID**

   * **Client ID**

   * **Client Secret**

   * **Issuer**

   * **Token Endpoint**

   * **JWKS Endpoint**

8. Create a flow policy:

   1. Click the **Flow Policy** tab.

   2. Click **[icon: plus, set=fa]Add Flow Policy**.

   3. In the **Name** field, enter a name for the flow policy.

   4. In the flow list, select your flow.

   5. In the version list, select **Latest Version**.

   6. Click **Create Flow Policy**.

      The **Edit Your Weight Distribution** modal opens.

      |   |                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | This example only uses one flow, but if your flow policy included multiple flows or flow versions, you could use this modal to split traffic between them. |

   7. Click **Save Flow Policy**.

   8. Note the **Policy ID** of your flow policy.

## Configuring an external IDP

Configure DaVinci as an external IdP *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* in PingOne.

### Steps

1. Sign on to PingOne.

2. Add DaVinci as an OIDC identity provider according to the [PingOne documentation](http://docs.pingidentity.com/pingone/integrations/p1_add_idp_oidc.html).

   1. For the **Connection Details**, use the values that you noted in [Creating an application](#dv_p1_external_idp_creating_an_application):

      * **Client ID**

      * **Client Secret**

   2. In the **Discovery Document URI** field, enter the well-known endpoint to configure the discovery detail values. The format is:

      ```
      https://auth.pingone.com/<EnvironmentID>/davinci/.well-known/openid-configuration
      ```

   3. In the **Requested Scopes** field, add a scope for each entity you want to import from the PingOne flow. The format for these scopes is:

      `p1FlowRequest:<parent entity>.<entity>`

      The entity name and parent entities are determined by the object request schema documented above. For example, to make the remote IP available, add the scope `p1FlowRequest:http.remoteIp`.

      You can add the `p1FlowRequest` scope to make all entities from the PingOne flow available, but this can sometimes result in request size errors.

   |   |                                                     |
   | - | --------------------------------------------------- |
   |   | Do not configure the **User Information Endpoint**. |

3. Create the authorization endpoint using the following structure:

   ```
   https://<domain>/<companyID>/davinci/policy/<policyID>/authorize
   ```

   Use the values that you noted in the previous procedure:

   * **Company ID**

   * **Policy ID**

4. Create the external IdP sign-on policy step according to the [PingOne documentation](http://docs.pingidentity.com/pingone/authentication/p1_add_idp_signon_step.html).

   1. In the **External Identity Provider** list, select the external IdP application you created in step 1.

   2. In the **Required Authentication Level** field, enter `policyId-<your policy ID>`. For example, `policyId-69b043b9edeb60b6c1945617ab1b4fae`.

   3. Select **Pass user context to provider**.

   4. Select the external IdP application, and then click **Save** to save your changes.

5. Create an application in PingOne and assign the sign-on policy step to that application according to the [PingOne documentation](http://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).

6. Add the referring domain to your new application.

   1. Go to **Applications** > **Applications**.

   2. Select your new application.

   3. Click the **Configuration** tab.

   4. Click the **Pencil** icon.

   5. In the **CORS Settings** section, select **Allow specific origins**.

   6. In the **Allowed Origins** field, enter the domain from which you plan to launch the flow.

   7. Click **Save**.

7. Copy the **Callback URL** for the external IdP in PingOne.

8. (Optional) Copy the JWKS information to enable PingOne context information to be used by DaVinci.

   1. Copy the PingOne Application **JWKS URL**.

   2. Access the JWKS URL and copy the complete JWKS key.

9. Sign on to DaVinci.

10. Click the **Applications** tab.

11. Find the application that you previously created and click **Edit**.

12. Click the **OIDC** tab, and then add the copied callback URL value to the **Redirect URLs** field.

13. (Optional) Enter the JWKS information to enable DaVinci to use context information from PingOne within flows.

    1. Click **Applications**.

    2. Open your application.

    3. Click the **OIDC** tab.

    4. In the **Service Provider (SP) JWKS URL** field, enter the JWKS URL.

    5. In the **Service Provider (SP) JWKS Keys to Verify Authorization Request Signature** field, enter the JWKS key.

## Invoking the flow

Add a link to the resource that invokes the flow using a call to PingOne.

### Steps

1. Open the source file for the resource that will launch the flow.

2. Create a call to your PingOne application according to the [PingOne documentation](http://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_integrate_oidc_application.html) and add it to the launching resource.

   The general format used for this call is:

   ```
   https://auth.pingone.com/<Environment ID>/as/authorize?response_type=<response type>
        &client_id=<client ID>
        &redirect_uri=<redirect URI>
        &scope=<scope>
   ```

   |   |                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------- |
   |   | You can reference the parameter values passed in with the invocation. The format is:```
   global.skOpenId.<parameter name>
   ``` |

3. If the user requires a token but the flow did not grant a token, make an API call to the PingOne token endpoint to grant the user a token. Use the [PingOne token authorization code](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/token-authorization_code-client-secret-post.html) endpoint or the [PingOne token client credentials](https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/token-client_credentials-client-secret-post.html) endpoint.

---

---
title: Switching between PingOne and DaVinci widget integrations
description: Learn how to switch between using a flow for a PingOne redirect integration and an integration using the DaVinci widget.
component: davinci
page_id: davinci:integrating_flows_into_applications:davinci_switch_between_flow_integrations
canonical_url: http://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_switch_between_flow_integrations.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 1, 2023
section_ids:
  pingone-to-davinci-widget: PingOne to DaVinci widget
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
  davinci-widget-to-pingone: DaVinci widget to PingOne
  about-this-task-2: About this task
  steps-2: Steps
  next-steps-2: Next steps
---

# Switching between PingOne and DaVinci widget integrations

Learn how to switch between using a flow for a PingOne redirect integration and an integration using the DaVinci widget.

|   |                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The following procedures enable you to reintegrate the same DaVinci flows for different use cases. In addition to these steps, follow the relevant procedures for your integration. Learn more in [Integrating Flows into Applications](davinci_how_to_implement_a_flow.html). |

## PingOne to DaVinci widget

### About this task

To change a flow integration that uses a PingOne redirect to a flow integration that uses the DaVinci widget:

### Steps

1. Sign on to PingOne and go to **Applications > Applications**.

2. Remove your DaVinci flow policy from the relevant application. Click **Save**.

3. In the DaVinci console, go to **Applications** and select the application that uses the PingOne flow policy.

4. Click the **Flow Policy** tab.

5. Locate the PingOne flow policy and, in the **More options ( [icon: ellipsis-v, set=fa])** list, select **Delete**.

6. Go to **Flows** and select the PingOne flow.

7. Go to **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings**.

8. On the **General** tab, click the toggle to turn off **PingOne Flow**. Click **Save**.

9. Close the **Flow Settings** panel and then redeploy the flow by clicking **Deploy**.

10. Go to the **Flow Policy** tab in the application where you previously deleted the flow policy.

11. Click **Add Flow Policy** and select **All Flow Policies**.

12. Select the desired version of the previously configured flow and click **Create Flow Policy**.

13. (Optional) Configure the **Edit Your Weight Distribution** modal.

14. Click **Save Flow Policy**.

### Next steps

[Integrate your flow using the DaVinci widget](davinci_launching_a_flow_with_the_widget.html).

## DaVinci widget to PingOne

### About this task

To change a flow integration that uses the DaVinci widget to a PingOne flow integration that uses a redirect:

### Steps

1. Go to **Applications** and select the application that uses the widget-based flow policy.

2. Click the **Flow Policy** tab.

3. Locate the widget-based flow policy and, in the **More options ( [icon: ellipsis-v, set=fa])** list, select **Delete**.

4. Go to **Flows** and select the widget-based flow.

5. Go to **More options ( [icon: ellipsis-v, set=fa]) > Flow Settings**.

6. On the **General** tab, click the toggle to enable **PingOne Flow**. Click **Save**.

7. Close the **Flow Settings** panel and then redeploy the flow by clicking **Deploy**.

8. Go to the **Flow Policy** tab in the application where you previously deleted the flow policy.

9. Click **Add Flow Policy** and select **PingOne Flow Policy**.

10. Select the desired version of the previously configured PingOne flow and click **Create Flow Policy**.

11. (Optional) Configure the **Edit Your Weight Distribution** modal.

12. Click **Save Flow Policy**.

13. Assign your new flow policy to the related application in PingOne.

    |   |                                                                                                                                               |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Learn more about assigning policies to PingOne applications in [Launching a PingOne flow with a redirect](davinci_launch_flow_redirect.html). |

### Next steps

[Integrate your flow using a PingOne redirect](davinci_launch_flow_redirect.html).