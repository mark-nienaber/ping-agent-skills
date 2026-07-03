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
