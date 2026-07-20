---
title: Create and edit routes with Freeform Designer
description: Create and edit PingGateway routes in the FreeForm Designer of Studio, and add objects, filters, and decorators to routes
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:freeform
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/freeform.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Routes", "Security", "User Interface"]
section_ids:
  studio-create-route-ff: Create a simple route
  studio-route-change-settings-ff: Change the basic settings of a route
  studio-add-objects-ff: Add objects to a route heap
  studio-add-filters-ff: Add configuration to a route
  studio-decorate-ff: Decorate objects in the route
---

# Create and edit routes with Freeform Designer

The following sections describe how to create a simple route in the FreeForm Designer of Studio, and then add configuration to the route. You can find examples of routes created with the FreeForm Designer in [Example routes created with Freeform Designer](examples-ff.html).

## Create a simple route

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select ![freeform](_images/freeform.svg) Freeform to use the FreeForm Designer.

2. Select [icon: file, set=fa]Basic to create a route from a blank template.

3. Enter the URL of the application you want to protect, followed by a path condition to access the route.

   For example, enter `https://app.example.com:8444/my-basic-route`.

   Studio creates the route on the ![freeform](_images/freeform.svg) Flow tab of the canvas.

4. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

   ```json
   {
     "name": "my-basic-route",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/my-basic-route')}",
     "handler": "ReverseProxyHandler",
     "heap": [
       {
         "name": "ReverseProxyHandler",
         "type": "ReverseProxyHandler"
       },
       {
         "type": "BaseUriDecorator",
         "name": "baseUri"
       },
       {
         "type": "TimerDecorator",
         "name": "timer",
         "config": {
           "timeUnit": "ms"
         }
       },
       {
         "type": "CaptureDecorator",
         "name": "capture",
         "config": {
           "captureEntity": false,
           "captureContext": false,
           "maxEntityLength": 524288
         }
       }
     ]
   }
   ```

   After deploying the route, edit it to remove the `ReverseProxyHandler` from the heap so PingGateway uses the object defined in `config.json` with TLS options to connect to the sample application.

## Change the basic settings of a route

1. Using the route created in [Create a simple route](#studio-create-route-ff), on the top-right of the screen select [icon: cog, set=fa]Route settings.

2. Using the on-screen hints for guidance, change the name, condition, or other features of the route, and save the changes.

3. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

## Add objects to a route heap

1. Using the route created in [Create a simple route](#studio-create-route-ff), select [icon: database, set=fa]All Objects > Create Object.

2. In Node Type, select an object type from the drop down list. For example, create an AmService object, using the following values:

   * Name: `AmService-1`

   * URI: `http://am.example.com:8088/openam/`

   * Agent:

     * Agent: `ig-agent`

     * Password: `password`

       |   |                                                                                                                   |
       | - | ----------------------------------------------------------------------------------------------------------------- |
       |   | Use secure passwords in a production environment. Consider using a password manager to generate secure passwords. |

     When you save, the object is added to route heap but is not used in the route.

3. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

## Add configuration to a route

1. Using the route created in [Create a simple route](#studio-create-route-ff), select the ![freeform](_images/freeform.svg) Flow tab, and delete the connector between Start and ReverseProxyHandler.

2. Drag a [icon: chain, set=fa]Chain from the side bar onto the canvas, and then drag a SingleSignOnFilter into the chain.

3. In the menu for the SingleSignOnFilter, enter the name of the AmService object you created in [Add objects to a route heap](#studio-add-objects-ff), `AmService-1`. The filter uses the object previously defined in the heap.

4. Connect Start to Chain-1, and Chain-1 to ReverseProxyHandler.

5. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

## Decorate objects in the route

1. Using the route created in [Create a simple route](#studio-create-route-ff), select the [icon: database, set=fa]All Objects tab.

   A list of objects in the route is displayed. By default, all available decorators are included in the route heap, but they don't decorate any objects.

2. For the ReverseProxyHandler or filter, select [icon: pencil-alt, set=fa], select the Decorations tab, and then enable one or more of the decorators.

3. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

---

---
title: Create and edit routes with Structured Editor (deprecated)
description: Deprecated. Create and edit PingGateway routes using the structured editor of Studio to add filters, decorators, and manage the route chain
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:structured
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/structured.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Routes", "Security", "User Interface"]
section_ids:
  studio-create-route: Creating simple routes
  studio-route-change-settings: Change the basic settings of a route
  studio-add-filters: Adding configuration to a route
  add_other_configuration_to_a_route: Add other configuration to a route
  add_other_filters_to_a_route: Add other filters to a route
  studio-manage-chain: Managing the route chain
  deploy: Deploy and undeploy routes
  deploy_a_route: Deploy a Route
  undeploy_a_route: Undeploy a Route
---

# Create and edit routes with Structured Editor (deprecated)

This section describes basic tasks for creating and deploying routes in the structured editor of Studio.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The structured editor of Studio is deprecated. For more information, refer to the [Deprecated](https://docs.pingidentity.com/pinggateway/release-notes/deprecated.html) section of the *Release Notes*. |

## Creating simple routes

1. In PingGateway Studio, create a route:

   1. Go to <http://ig.example.com:8085/studio> and select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

2. Enter the URL of the application you want to protect, followed by a path condition to access the route.

   For example, enter `https://app.example.com:8444/my-basic-route`.

   Studio creates the route and displays menus to add configuration objects to the route.

3. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

   A route similar to the following displays, where the route name reflects the path condition:

   ```json
   {
     "name": "my-basic-route",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/my-basic-route')}",
     "handler": "ReverseProxyHandler"
   }
   ```

## Change the basic settings of a route

1. In Studio, select [icon: sitemap, set=fa]ROUTES, and then select a route with the [icon: list-ul, set=fa]icon.

2. On the top-right of the screen select [icon: cog, set=fa]Route settings.

3. Using the on-screen hints for guidance, change the name, condition, or other features of the route, and save the changes.

4. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

## Adding configuration to a route

After creating a route in the structured editor, you can add filters, decorators, scripts, and other configuration to the route.

### Add other configuration to a route

1. In Studio, select [icon: sitemap, set=fa]ROUTES, and then select a route with the [icon: list-ul, set=fa]icon.

2. Select one of the configuration options, and follow the on-screen hints to select configuration settings.

   For routes to test with the examples in the Gateway guide, refer to [Example routes created with Structured Editor (deprecated)](examples-se.html).

### Add other filters to a route

Use this procedure to add any filter type to the configuration.

1. In Studio, select [icon: sitemap, set=fa]ROUTES, and then select a route with the [icon: list-ul, set=fa]icon.

2. Select [icon: file, set=fa]Other filters > [icon: plus, set=fa]New filter > Other filter.

3. In Create filter, select a filter type from the list, enter a name, and optionally enter a configuration for the filter.

   |   |                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Studio checks that the JSON is valid, but doesn't check that the configuration of the filter is valid. If the filter configuration isn't valid, when you deploy the route it fails to load. |

   When you save, the filter is added to the list of other filters but is not added to the configuration.

4. Enable the filter to add it to the configuration.

   If you disable the filter again, it is removed from the route's chain but the configuration is saved. Simply enable the filter again to add it back in the chain.

## Managing the route chain

The [icon: chain, set=fa]Chain view lists the filters in the order that they appear in the configuration.

Some filters have a natural position in the chain. For example, so that an authenticated user is given the correct permissions, an authentication filter must come before an authorization filter. Similarly, so that an authorization token is transformed, an authorization filter always comes before a token transformation filter.

Other filters have a flexible position in the chain. For example, an AssignmentFilter can be used before a request is handled or after a response is handled.

When the position of a filter is fixed, it is automatically placed in the correct position in the chain; you cannot change the position. When the position of a filter is flexible, the [icon: tag, set=fa]icon is displayed, and you can drag the filter into a different position in the chain.

Select [icon: chain, set=fa]Chain to view and manage the filters in the chain as follows:

* When the [icon: tag, set=fa]icon is displayed, drag a filter up or down the chain.

* Select [icon: pencil-alt, set=fa]to edit a filter.

* Select [icon: cog, set=fa]Realm Settings to disable and remove a filter from the chain.

For information about chains, refer to [Chain](../reference/Chain.html).

## Deploy and undeploy routes

### Deploy a Route

1. In Studio, select [icon: sitemap, set=fa]ROUTES, and then select a route created with the structured editor (with the [icon: list-ul, set=fa]icon).

2. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

3. If the route is okay, select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   |   |                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If the route configuration is not valid, or if a service that the route relies on, such as an AM service, is not available, the route fails to deploy. |

   If the route deploys successfully, [icon: check-circle, set=fa]Deployed is displayed and the [icon: cloud-upload-alt, set=fa]Deploy button is greyed out.

4. Check the `$HOME/.openig/config/routes` folder in your PingGateway configuration to see that the route is there.

   By default, routes are loaded automatically into the PingGateway configuration. You don't need to stop and restart PingGateway. For more information, refer to [Prevent the reload of routes](../configure/configure.html#routing-lockdown).

5. Check the system log to confirm that the route was loaded successfully into the configuration. For information about logs, refer to [Managing PingGateway logs](../maintenance-guide/logging.html).

### Undeploy a Route

1. In Studio, select [icon: sitemap, set=fa]ROUTES and then select a route with the status [icon: check-circle, set=fa]Deployed.

2. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: times, set=fa]Undeploy, and then confirm your request.

   The route is removed from the PingGateway configuration. On the Studio screen, the route status [icon: check-circle, set=fa]Deployed is no longer displayed and the [icon: cloud-upload-alt, set=fa]Deploy option is active again.

---

---
title: Editing and importing routes in Studio
description: Edit routes in PingGateway Studio using the JSON editor, or import existing routes from your filesystem into Studio
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:import-edit
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/import-edit.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Routes", "Security", "User Interface"]
section_ids:
  edit-route: Edit routes in editor mode
  import-route: Import routes into Studio
  view-route: View and search for routes in your configuration
---

# Editing and importing routes in Studio

The following sections describe basic tasks for Edit and import routes in Studio:

## Edit routes in editor mode

After creating a route in Studio, you can edit it by using the options offered in Studio, or by switching to editor mode and using the JSON editor.

Routes created only in the menus of structured editor have the icon [icon: list-ul, set=fa]. Routes created only in the menus of FreeForm Designer have the icon ![freeform](_images/freeform.svg). Imported routes and routes edited in editor mode have the icon { }.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you go into editor mode, you can use the JSON editor to manually edit the route, but can no longer use the full Studio interface to add to or edit the configuration. |

1. In Studio, select [icon: sitemap, set=fa]ROUTES, and then select a route created with the structured editor (with the [icon: list-ul, set=fa]icon).

2. Edit the route in Studio or manually:

   * To edit in Studio, select options offered in Studio.

   * To edit manually, select [icon: ellipsis-v, set=fa]and [icon: file-code, set=fa]Editor mode and use the JSON editor to edit the route.

   If the route status is [icon: check-circle, set=fa]Deployed, it changes to [icon: exclamation-circle, set=fa]Changes pending.

3. Deploy the route as described in [Deploying and undeploying routes](structured.html#deploy).

## Import routes into Studio

When you import a route into Studio, it is imported in editor mode. You can use the JSON editor to manually edit the route, but can't use the full Studio interface to add or edit filters.

Routes created only in the menus of structured editor have the icon [icon: list-ul, set=fa]. Routes created only in the menus of FreeForm Designer have the icon ![freeform](_images/freeform.svg). Imported routes and routes edited in editor mode have the icon **{ }**.

1. In Studio, select [icon: sitemap, set=fa]ROUTES and then [icon: upload, set=fa]Import a route.

2. Click in the window to import a route, or drag a route from your filesystem.

   If the route has a `name` property, the name is automatically used for the Name and ID fields in Studio.

3. If necessary, make the following changes, and then select Import:

   * If the Name and ID fields are empty, enter a unique name and ID for the route.

   * If the Name and ID fields are outlined in red, the route name or ID already exists in Studio. Change the name and ID to be unique.

   * If an error message is displayed, the route is not valid JSON. Fix the route and then try again to import it.

   The route is added to the list of routes on the [icon: sitemap, set=fa]ROUTES page.

4. Deploy the route as described in [Deploying and undeploying routes](structured.html#deploy).

## View and search for routes in your configuration

All of the routes that exist in your backend configuration are displayed on the [icon: sitemap, set=fa]ROUTES page, including imported routes and routes created outside Studio.

To search for a route, select [icon: sitemap, set=fa]ROUTES, and type part of the route name in the search box. Matching routes are displayed as you enter the search criteria.

---

---
title: Example routes created with Freeform Designer
description: Example routes for SSO, policy enforcement, and token introspection built using the PingGateway Studio Freeform Designer
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:examples-ff
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/examples-ff.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Routes", "Security", "User Interface", "Single sign-on (SSO)"]
section_ids:
  example-SingleSignOnFilter-ff: Use a basic template in FreeForm Designer
  example-pep-sso-ff: Protect a web app with Freeform Designer
  example-rsintrospect-ff: Protect an API with Freeform Designer
---

# Example routes created with Freeform Designer

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't configure secrets providers in Studio.Documentation examples generated with Studio refer to secrets providers you must configure separately in `config.json`. |

The following sections give examples of how to use the templates provided by the FreeForm Designer:

## Use a basic template in FreeForm Designer

This section describes how to use a basic template in FreeForm Designer to set up SSO. For more information about setting up and testing SSO, refer to [Authentication with PingAM](../gateway-guide/sso-cdsso.html).

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select ![freeform](_images/freeform.svg) Freeform to use the FreeForm Designer.

2. Select [icon: file, set=fa]Basic to create a route from a blank template.

3. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/sso-ff`

   * Name: `sso-ff`

     The route is displayed on the ![freeform](_images/freeform.svg) Flow tab of the canvas. Select the [icon: database, set=fa]All Objects tab to view a list of objects in the route.

     Double-click on any object to review or edit it. After double-clicking on an object, select the Decorations tab to decorate it.

4. Configure authentication with a SingleSignOnFilter:

   1. In the ![freeform](_images/freeform.svg) Flow tab, delete the connector between Start and ReverseProxyHandler.

   2. From the sidebar, drag a [icon: chain, set=fa]Chain onto the canvas, and then drag a [icon: user, set=fa]SingleSignOnFilter into the chain.

   3. In the Edit SingleSignOnFilter page, click [icon: plus, set=fa], and create an AM service, with the following values:

      * URI: `http://am.example.com:8088/openam`

      * Secrets Provider: `SystemAndEnvSecretStore-1`

      * Agent:

        * Username: `ig_agent`

        * Password Secret ID : `agent.secret.id`

   4. Connect Start to Chain-1, and Chain-1 to ReverseProxyHandler.

5. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

   ```json
   {
     "name": "sso-ff",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/sso-ff')}",
     "handler": "Chain-1",
     "heap": [
       {
         "name": "ReverseProxyHandler",
         "type": "ReverseProxyHandler"
       },
       {
         "type": "BaseUriDecorator",
         "name": "baseUri"
       },
       {
         "type": "TimerDecorator",
         "name": "timer",
         "config": {
           "timeUnit": "ms"
         }
       },
       {
         "type": "CaptureDecorator",
         "name": "capture",
         "config": {
           "captureEntity": false,
           "captureContext": false,
           "maxEntityLength": 524288
         }
       },
       {
         "name": "Chain-1",
         "type": "Chain",
         "config": {
           "handler": "ReverseProxyHandler",
           "filters": [
             "SingleSignOnFilter-1"
           ]
         }
       },
       {
         "name": "AmService-1",
         "type": "AmService",
         "config": {
           "url": "http://am.example.com:8088/openam",
           "realm": "/",
           "secretsProvider": "SystemAndEnvSecretStore-1",
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "sessionCache": {
             "enabled": false
           }
         }
       },
       {
         "name": "SingleSignOnFilter-1",
         "type": "SingleSignOnFilter",
         "config": {
           "amService": "AmService-1"
         }
       }
     ]
   }
   ```

   Source: [sso-ff.json](../_attachments/config/routes/sso-ff.json)

6. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

   After deploying the route, edit it to remove the `ReverseProxyHandler` from the heap so PingGateway uses the object defined in `config.json` with TLS options to connect to the sample application.

## Protect a web app with Freeform Designer

This section describes how to use FreeForm Designer to protect a web app, using AM for single sign-on and policy enforcement.

The generated route contains a chain of objects to authenticate the user, enforce an AM authorization policy, retrieve the user's profile, insert it into the request, and, finally, forward the request to the web app.

Before you start, set up AM as described in [Enforce AM policy decisions](../gateway-guide/pep.html).

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select ![freeform](_images/freeform.svg) Freeform to use the FreeForm Designer.

2. Select [icon: globe, set=fa]Web SSO to use the template for protecting web apps.

3. Select Advanced options on the right, and create a route with the following options:

   * Base URI : `https://app.example.com:8444`

   * Condition: Path : `/home/pep-sso-ff`

   * Name : `pep-sso-ff`

   * AM Configuration :

     * URI : `http://am.example.com:8088/openam`

     * Secrets Provider: `SystemAndEnvSecretStore-1`

     * Username : `ig_agent`

     * Password Secret ID : `agent.secret.id`

       The route is displayed on the ![freeform](_images/freeform.svg) Flow tab of the canvas. Select the [icon: database, set=fa]All Objects tab to view a list of objects in the route.

       Double-click on any object to review or edit it. After double-clicking on an object, select the Decorations tab to decorate it.

4. On the ![freeform](_images/freeform.svg) Flow tab, double-click the Policy Enforcement object, and add a policy set with the following values:

   * Policy set : `PEP-SSO`

   * AM SSO token : `${contexts.ssoToken.value}`

     Leave all other values as default.

5. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

6. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

   After deploying the route, edit it to remove the `ReverseProxyHandler` from the heap so PingGateway uses the object defined in `config.json` with TLS options to connect to the sample application:

   ```json
   {
     "name": "pep-sso-ff",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/pep-sso-ff')}",
     "handler": "Chain",
     "heap": [
       {
         "name": "Chain",
         "type": "Chain",
         "config": {
           "handler": "ReverseProxyHandler",
           "filters": [
             "SSO",
             "Policy Enforcement",
             "GetEmail",
             "InjectEmail"
           ]
         }
       },
       {
         "name": "SSO",
         "type": "SingleSignOnFilter",
         "config": {
           "amService": "AmService"
         }
       },
       {
         "name": "AmService",
         "type": "AmService",
         "config": {
           "url": "http://am.example.com:8088/openam",
           "realm": "/",
           "secretsProvider": "SystemAndEnvSecretStore-1",
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "sessionCache": {
             "enabled": false
           }
         }
       },
       {
         "name": "Policy Enforcement",
         "type": "PolicyEnforcementFilter",
         "config": {
           "amService": "AmService",
           "ssoTokenSubject": "${contexts.ssoToken.value}",
           "cache": {
             "enabled": false
           },
           "application": "PEP-SSO"
         }
       },
       {
         "name": "GetEmail",
         "type": "UserProfileFilter",
         "config": {
           "username": "${contexts.ssoToken.info.uid}",
           "userProfileService": {
             "type": "UserProfileService",
             "config": {
               "amService": "AmService"
             }
           }
         }
       },
       {
         "name": "InjectEmail",
         "type": "HeaderFilter",
         "config": {
           "messageType": "REQUEST",
           "add": {
             "Email": [
               "${contexts.userProfile.username}"
             ]
           }
         }
       },
       {
         "type": "BaseUriDecorator",
         "name": "baseUri"
       },
       {
         "type": "TimerDecorator",
         "name": "timer",
         "config": {
           "timeUnit": "ms"
         }
       },
       {
         "type": "CaptureDecorator",
         "name": "capture",
         "config": {
           "captureEntity": false,
           "captureContext": false,
           "maxEntityLength": 524288
         }
       }
     ]
   }
   ```

   Source: [pep-sso-ff.json](../_attachments/config/routes/pep-sso-ff.json)

## Protect an API with Freeform Designer

This section describes how to use FreeForm Designer to protect APIs, using AM as an OAuth 2.0 Authorization Server.

The generated route contains a chain of objects to authenticate the user, throttle the rate of requests to the API, and, finally, forward the request to the sample app.

Before you start, set up AM as described in [Validating PingAM access tokens with introspection](../gateway-guide/oauth2-rs-introspect.html). In addition, create an OAuth 2.0 Client authorized to introspect tokens with the following values:

* Client ID : `resource-server`

* Client secret : `password`

* Scope(s) : `am-introspect-all-tokens`

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select ![freeform](_images/freeform.svg) Freeform to use the FreeForm Designer.

2. Select API Security.

3. Select Advanced options on the right, and create a route with the following options:

   * Base URI : `https://app.example.com:8444`

   * Condition: Path : `/home/rs-introspect-ff`

   * Name : `rs-introspect-ff`

   * AM Configuration :

     * URI : `http://am.example.com:8088/openam`

     * Secrets Provider: `SystemAndEnvSecretStore-1`

     * Username : `ig_agent`

     * Password Secret ID : `agent.secret.id`

     * Scopes : `mail`, `employeenumber`

       The route is displayed on the ![freeform](_images/freeform.svg) Flow tab of the canvas.

       Notice that the Start, Chain, and ReverseProxyHandler objects are connected by solid lines, but other objects, such as Authenticate to Am Chain, are connected by a fading line. Objects connected by a fading line are used by other objects in the route.

       Select the [icon: database, set=fa]All Objects tab to view a list of objects in the route. Double-click on any object to review or edit it. After double-clicking on an object, select the Decorations tab to decorate it.

4. On the ![freeform](_images/freeform.svg) Flow tab, double-click the OAuth2RS object, and edit it as follows:

   * Require HTTPS : Deselect this option

   * Realm : `OpenIG`

     Leave the other values as they are.

5. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

6. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

   After deploying the route, edit it to remove the `ReverseProxyHandler` from the heap so PingGateway uses the object defined in `config.json` with TLS options to connect to the sample application.

   ```json
   {
     "name": "rs-introspect-ff",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/rs-introspect-ff')}",
     "handler": "Chain",
     "properties": {
       "amSecretsProvider": "SystemAndEnvSecretStore-1",
       "amUsername": "ig_agent",
       "amPasswordSecretId": "agent.secret.id"
     },
     "heap": [
       {
         "name": "ClientHandler",
         "type": "ClientHandler"
       },
       {
         "name": "Chain",
         "type": "Chain",
         "config": {
           "handler": "ReverseProxyHandler",
           "filters": [
             "OAuth2RS",
             "Throttling"
           ]
         }
       },
       {
         "type": "OAuth2ResourceServerFilter",
         "name": "OAuth2RS",
         "config": {
           "requireHttps": false,
           "scopes": [
             "mail",
             "employeenumber"
           ],
           "accessTokenResolver": "TokenIntrospectionAccessTokenResolver"
         }
       },
       {
         "type": "TokenIntrospectionAccessTokenResolver",
         "name": "TokenIntrospectionAccessTokenResolver",
         "config": {
           "amService": "AmService",
           "providerHandler": "Authenticate to AM Chain"
         }
       },
       {
         "name": "AmService",
         "type": "AmService",
         "config": {
           "url": "http://am.example.com:8088/openam",
           "realm": "/",
           "secretsProvider": "SystemAndEnvSecretStore-1",
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "sessionCache": {
             "enabled": false
           }
         }
       },
       {
         "name": "Authenticate to AM Chain",
         "type": "Chain",
         "config": {
           "handler": "ClientHandler",
           "filters": [
             "Authenticate to AM Filter"
           ]
         }
       },
       {
         "name": "Authenticate to AM Filter",
         "type": "HttpBasicAuthenticationClientFilter",
         "config": {
           "username": "ig_agent",
           "passwordSecretId": "password.secret.id",
           "secretsProvider": "SystemAndEnvSecretStore-1"
         }
       },
       {
         "name": "Throttling",
         "type": "ThrottlingFilter",
         "config": {
           "requestGroupPolicy": "${contexts.oauth2.info.sub}",
           "rate": {
             "numberOfRequests": 60,
             "duration": "60 s"
           }
         }
       },
       {
         "type": "BaseUriDecorator",
         "name": "baseUri"
       },
       {
         "type": "TimerDecorator",
         "name": "timer",
         "config": {
           "timeUnit": "ms"
         }
       },
       {
         "type": "CaptureDecorator",
         "name": "capture",
         "config": {
           "captureEntity": false,
           "captureContext": false,
           "maxEntityLength": 524288
         }
       }
     ]
   }
   ```

   Source: [rs-introspect-ff.json](../_attachments/config/routes/rs-introspect-ff.json)

7. Test the setup:

   1. In a terminal window, use a `curl` command similar to the following to retrieve an access token:

      ```console
      $ mytoken=$(curl -s \
      --user "client-application:password" \
      --data "grant_type=password&username=demo&password=Ch4ng31t&scope=mail%20employeenumber" \
      http://am.example.com:8088/openam/oauth2/access_token | jq -r ".access_token")
      ```

   2. Validate the access token returned in the previous step:

      ```console
      $ curl -v http://ig.example.com:8080/home/rs-introspect-ff --header "Authorization: Bearer ${mytoken}"
      ```

      The HTML of the sample application is returned.

---

---
title: Example routes created with Structured Editor (deprecated)
description: Deprecated. Example routes created with the PingGateway Studio Structured Editor for SSO, CDSSO, OAuth 2.0, OIDC, SAML 2.0, throttling, and WebSocket
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:examples-se
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/examples-se.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Routes", "Security", "User Interface", "Single sign-on (SSO)", "Policy", "Configuration", "Cross Domain SSO (CDSSO)", "OAuth 2.0", "OpenID Connect (OIDC)", "SAML 2.0", "Throttling", "Proxy"]
section_ids:
  example-sso-se: Single sign-on in Structured Editor
  example-pep-sso-se: Policy enforcement in Structured Editor
  example-pep-cdsso: Policy enforcement for CDSSO in Structured Editor
  example-rsintrospect-se: Token validation using the introspection endpoint in Structured Editor
  example-oidc-am: OpenID Connect in Structured Editor
  example-ttf-se: Token transformation in Structured Editor
  example-throttle-simple: Simple throttling filter in Structured Editor
  example-throttle-mapped: Mapped throttling filter in Structured Editor
  example-throttle-scriptable: Scriptable throttling filter in Structured Editor
  example-websocket-se: Proxy for websocket traffic in Structured Editor
---

# Example routes created with Structured Editor (deprecated)

The following sections give examples of use the structured editor to set up some routes from the [PingGateway guide](../gateway-guide/preface.html).

|   |                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The structured editor of Studio is deprecated.

  Learn more in the release notes page about [Deprecated](https://docs.pingidentity.com/pinggateway/release-notes/deprecated.html) features.

* You can't configure secrets providers in Studio.

  Documentation examples generated with Studio refer to secrets providers you must configure separately in `config.json`. |

## Single sign-on in Structured Editor

This section describes how to set up SSO in the structured editor of Studio. For more information about setting up SSO, refer to [Authentication with PingAM](../gateway-guide/sso-cdsso.html).

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

2. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/sso-studio`

   * Name : `sso-studio`

3. Configure authentication:

   1. Select [icon: user, set=fa]Authentication.

   2. Select Single Sign-On, and enter the following information:

      * AM service : Configure an AM service to use for authentication:

        * URI: `http://am.example.com:8088/openam`

        * Secrets Provider: `SystemAndEnvSecretStore-1`

        * Agent :

          * Username : `ig_agent`

          * Password Secret ID : `password.secret.id`

      Leave all other values as default.

4. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

5. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## Policy enforcement in Structured Editor

This section describes how to set up PingGateway as a policy enforcement point in the structured editor of Studio. For more information about setting up policy enforcement, refer to [Enforce AM policy decisions](../gateway-guide/pep.html).

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

2. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/pep-sso`

   * Name : `pep-sso`

   The structured editor is displayed.

3. Configure authentication:

   1. Select [icon: user, set=fa]Authentication.

   2. Select Single Sign-On, and enter the following information:

      * AM service : Configure an AM service to use for authentication:

        * URI: `http://am.example.com:8088/openam`

        * Secrets Provider: `SystemAndEnvSecretStore-1`

        * Agent : The credentials of the agent you created in AM.

          * Username : `ig_agent`

          * Password Secret ID : `password.secret.id`

   Leave all other values as default.

4. Configure a PolicyEnforcementFilter:

   1. Select [icon: key, set=fa]Authorization.

   2. Select AM Policy Enforcement, and then select the following options:

      * Access Management configuration:

        * AM service : `http://am.example.com:8088/openam (/)`.

      * Access Management policies:

        * Policy set : `PEP-SSO`

        * AM SSO token : `${contexts.ssoToken.value}`

      Leave all other values as default.

5. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

6. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## Policy enforcement for CDSSO in Structured Editor

This section describes how to set up PingGateway as a policy enforcement point for CDSSO in the structured editor of Studio. For more information about how to set up SSO, refer to [Decisions in different domains with PingAM](../gateway-guide/pep-cdsso.html)

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

2. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/pep-cdsso`

   * Name : `pep-cdsso`

3. Configure authentication:

   1. Select [icon: user, set=fa]Authentication.

   2. Select Cross-Domain Single Sign-On, and enter the following information:

      * AM service :

        * URI: `http://am.example.com:8088/openam`

        * Secrets Provider: `SystemAndEnvSecretStore-1`

        * Agent : The credentials of the agent you created in AM.

          * Username : `ig_agent_cdsso`

          * Password Secret ID : `password.secret.id`

      * Redirect endpoint : `/home/pep-cdsso/redirect`

      * Authentication cookie :

        * Path : `/home`

   Leave all other values as default.

4. Configure a PolicyEnforcementFilter:

   1. Select [icon: key, set=fa]Authorization.

   2. Select AM Policy Enforcement, and select the following options to reflect the configuration of the PingGateway agent in AM:

      * Access Management configuration:

        * AM service : `http://am.example.com:8088/openam (/)`.

      * Access Management policies:

        * Policy set : `PEP-CDSSO`

        * AM SSO token ID : `${contexts.cdsso.token}`

      Leave all other values as default.

5. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

6. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## Token validation using the introspection endpoint in Structured Editor

This section sets up PingGateway as an OAuth 2.0 resource server, using the introspection endpoint, in the structured editor of Studio.

1. Set up AM as described in [Validating PingAM access tokens with introspection](../gateway-guide/oauth2-rs-introspect.html). In addition, create an OAuth 2.0 Client authorized to introspect tokens with the following values:

   * Client ID : `resource-server`

   * Client secret `password`

   * Scope(s) : `am-introspect-all-tokens`

2. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

   3. Create a route with the following option:

      * Application URL: `https://app.example.com:8444/rs-introspect-se`

3. Configure authorization:

   1. Select [icon: key, set=fa]Authorization > OAuth 2.0 Resource Server, and then select the following options:

      * Token resolver configuration:

        * Access token resolver: `OAuth 2.0 introspection endpoint`

        * Introspection endpoint URI: `http://am.example.com:8088/openam/oauth2/introspect`

        * Client name and Client secret : `resource-server` and `password`

          This is the name and password of the OAuth 2.0 client with the scope to examine (introspect) tokens, configured in AM.

      * Scope configuration:

        * Evaluate scopes: `Statically`

        * Scopes: `mail`, `employeenumber`

      * OAuth 2.0 Authorization settings:

        * Require HTTPS: Deselect this option

        * Enable cache: Deselect this option

   Leave all other values as default.

4. Add a StaticResponseHandler:

   1. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: file-code, set=fa]Editor mode to switch into editor mode.

      |   |                                                                                                                                                                                                              |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | After switching to Editor mode, you cannot go back. You will be able to use the JSON file editor to manually edit the route but will no longer be able use the full Studio interface to add or edit filters. |

   2. Replace the last ReverseProxyHandler in the route with the following StaticResponseHandler, and then save the route:

      ```json
      "handler": {
        "type": "StaticResponseHandler",
        "config": {
         "status": 200,
         "headers": {
           "Content-Type": [ "text/html; charset=UTF-8" ]
         },
         "entity": "<html><body><h2>Decoded access_token: ${contexts.oauth2.accessToken.info}</h2></body></html>"
        }
      }
      ```

5. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

6. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## OpenID Connect in Structured Editor

This section describes how to set up PingGateway as an OpenID Connect relying party in the structured editor of Studio. For more information, refer to [AM as OIDC provider](../gateway-guide/oidc-am.html).

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

2. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/id_token`

   * Name: `07-openid`

3. Configure authentication:

   1. Select [icon: user, set=fa]Authentication.

   2. Select OpenID Connect, and then select the following options:

      * Client Filter:

        * Client Endpoint: `/home/id_token`

        * Require HTTPS: Deselect this option

      * Client Registration:

        * Client ID: `oidc_client`

        * Client secret: `password`

        * Scopes: `openid`, `profile`, and `email`

        * Basic authentication: Select this option

      * Issuer:

        * Well-known Endpoint: `http://am.example.com:8088/openam/oauth2/.well-known/openid-configuration`

      Leave all other values as default.

4. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

5. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## Token transformation in Structured Editor

This section describes how to set up token transformation in the structured editor of Studio. For more information about setting up token transformation, refer to [OIDC ID tokens to SAML assertions with PingAM](../gateway-guide/ttf.html).

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

2. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/id_token`

   * Name : `50-idtoken`

3. Configure authentication:

   1. Select [icon: user, set=fa]Authentication.

   2. Select OpenID Connect, and enter the following information:

      * Client Filter :

        * Client Endpoint: `/home/id_token`

        * Require HTTPS: Deselect this option

      * Client Registration :

        * Client ID : `oidc_client`

        * Client secret : `password`

        * Scopes: `openid`, `profile`, and `email`

        * Basic authentication: Select this option

      * Issuer :

        * Well-known endpoint: `http://am.example.com:8088/openam/oauth2/.well-known/openid-configuration`

   Leave all other values as default, and save your settings.

4. Set up token transformation:

   1. Select and enable Token transformation.

   2. Enter the following information:

      * AM service : Configure an AM service to use for authentication and REST STS requests.

        * URI: `http://am.example.com:8088/openam`

        * Secrets Provider: `SystemAndEnvSecretStore-1`

        * Agent : The credentials of the agent you created in AM.

          * Username : `ig_agent`

          * Password Secret ID : `password.secret.id`

      * Username : `oidc_client`

      * Password : `password`

      * id\_token : `${contexts.oauth2Info.idToken}`

      * Instance : `openig`

5. Add a StaticResponseHandler:

   1. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: file-code, set=fa]Editor mode to switch into editor mode.

      |   |                                                                                                                                                                                                              |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | After switching to Editor mode, you cannot go back. You will be able to use the JSON file editor to manually edit the route but will no longer be able use the full Studio interface to add or edit filters. |

   2. Replace the last ReverseProxyHandler in the route with the following StaticResponseHandler, and then save the route:

      ```json
      "handler": {
        "type": "StaticResponseHandler",
        "config": {
          "status": 200,
          "headers": {
            "Content-Type": [ "text/plain; charset=UTF-8" ]
          },
          "entity": "{\"id_token\":\n\"${contexts.oauth2Info.idToken}\"} \n\n\n{\"saml_assertions\":\n\"${contexts.sts.issuedToken}\"}"
        }
      }
      ```

6. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

7. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## Simple throttling filter in Structured Editor

This section describes how to set up a simple throttling filter in the structured editor of Studio. For more information about how to set up throttling, refer to [Configure simple throttling](../gateway-guide/throttling.html#throttling-simple).

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

2. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/throttle-simple`

   * Name : `00-throttle-simple`

3. Select and enable [icon: filter, set=fa]Throttling.

4. In GROUPING POLICY, apply the rate to a single group.

   All requests are grouped together, and the default throttling rate is applied to the group. By default, no more than 100 requests can access the sample application each second.

5. In RATE POLICY, select Fixed, and allow 6 requests each 10 seconds.

6. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

7. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## Mapped throttling filter in Structured Editor

This section describes how to set up a mapped throttling filter in the structured editor of Studio. For more information about how to set up throttling, refer to [Configure mapped throttling](../gateway-guide/throttling.html#throttling-mapped).

1. Set up AM as described in [Validating PingAM access tokens with introspection](../gateway-guide/oauth2-rs-introspect.html). In addition, create an OAuth 2.0 Client authorized to introspect tokens with the following values:

   * Client ID : `resource-server`

   * Client secret `password`

   * Scope(s) : `am-introspect-all-tokens`

2. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

3. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/throttle-mapped-se`

   * Name : `00-throttle-mapped-se`

4. Configure authorization:

   1. Select [icon: key, set=fa]Authorization > OAuth 2.0 Resource Server, and then select the following options:

      * Token resolver configuration:

        * Access token resolver: `OAuth 2.0 introspection endpoint`

        * Introspection endpoint URI: `http://am.example.com:8088/openam/oauth2/introspect`

        * Client name and Client secret : `resource-server` and `password`

          This is the name and password of the OAuth 2.0 client with the scope to examine (introspect) tokens, configured in AM.

      * Scope configuration:

        * Evaluate scopes: `Statically`

        * Scopes: `mail`, `employeenumber`

      * OAuth 2.0 Authorization settings:

        * Require HTTPS: Deselect this option

        * Enable cache: Deselect this option

   Leave all other values as default.

5. Configure throttling:

   1. Select and enable [icon: filter, set=fa]Throttling.

   2. Set up the grouping policy:

      1. In GROUPING POLICY, apply the rate to independent groups of requests.

         Requests are split into different groups according to criteria, and the throttling rate is applied to each group.

      2. Select to group requests by custom criteria.

         Enter `${contexts.oauth2.accessToken.info.mail}` as the custom expression. This expression defines the subject in the OAuth2Context.

   3. Set up the rate policy:

      1. In RATE POLICY, select Mapped.

      2. Select to map requests by custom criteria.

      3. Enter the custom expression `${contexts.oauth2.accessToken.info.status}`.

      4. In Default Rate, select Edit and change the default rate to 1 request each 10 seconds.

      5. In Mapped Rates, add the following rate for `gold` status:

         * Match Value : `gold`

         * Number of requests : `6`

         * Period : `10 seconds`

      6. Add a different rate for `silver` status:

         * Match Value : `silver`

         * Number of requests : `3`

         * Period : `10 seconds`

      7. Add a different rate for `bronze` status:

         * Match Value : `bronze`

         * Number of requests : `1`

         * Period : `10 seconds`

      8. Save the rate policy.

6. Select [icon: chain, set=fa]Chain, and change the order of the filters so [icon: filter, set=fa]Throttling comes after [icon: key, set=fa]Authorization.

7. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

8. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## Scriptable throttling filter in Structured Editor

This section describes how to set up a scriptable throttling filter in the structured editor of Studio. For more information about how to set up throttling, refer to [Configure scriptable throttling](../gateway-guide/throttling.html#throttling-scriptable).

1. Set up AM as described in [Validating PingAM access tokens with introspection](../gateway-guide/oauth2-rs-introspect.html). In addition, create an OAuth 2.0 Client authorized to introspect tokens with the following values:

   * Client ID: `resource-server`

   * Client secret: `password`

   * Scope(s): `am-introspect-all-tokens`

2. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

3. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/home/throttle-scriptable-se`

   * Name: `00-throttle-scriptable-se`

4. Configure authorization:

   1. Select [icon: key, set=fa]Authorization > OAuth 2.0 Resource Server, and then select the following options:

      * Token resolver configuration:

        * Access token resolver: `OAuth 2.0 introspection endpoint`

        * Introspection endpoint URI: `http://am.example.com:8088/openam/oauth2/introspect`

        * Client name and Client secret : `resource-server` and `password`

          This is the name and password of the OAuth 2.0 client with the scope to examine (introspect) tokens, configured in AM.

      * Scope configuration:

        * Evaluate scopes: `Statically`

        * Scopes: `mail`, `employeenumber`

      * OAuth 2.0 Authorization settings:

        * Require HTTPS: Deselect this option

        * Enable cache: Deselect this option

   Leave all other values as default.

5. Configure throttling:

   1. Select and enable [icon: filter, set=fa]Throttling.

   2. Set up the grouping policy:

      1. In GROUPING POLICY, apply the rate to independent groups of requests.

         Requests are split into different groups according to criteria, and the throttling rate is applied to each group.

      2. Select to group requests by custom criteria.

      3. Enter `${contexts.oauth2.accessToken.info.mail}` as the custom expression.

   3. Set up the rate policy:

      1. In RATE POLICY, select Scripted.

      2. Select to create a new script, and name it `X-User-Status`. So that you can easily identify the script, use a name that describes the content of the script.

      3. Add the following argument/value pairs:

         * argument: `status`, value: `gold`

         * argument: `rate`, value: `6`

         * argument: `duration`, value: `10 seconds`

           * Replace the default script with the content of a valid Groovy script. For example, enter the following script:

             ```groovy
             if (contexts.oauth2.accessToken.info.status == status) {
               return new ThrottlingRate(rate, duration)
             } else {
               return null
             }
             ```

             Alternatively, skip the step to define arguments, and add the following script instead:

             ```groovy
             if (contexts.oauth2.accessToken.info.status == 'gold') {
               return new ThrottlingRate(6, '10 seconds')
             } else {
               return null
             }
             ```

             |   |                                                         |
             | - | ------------------------------------------------------- |
             |   | Studio doesn't check the validity of the Groovy script. |

      4. Enable the default rate, and set it to 1 request each 10 seconds.

      5. Save the rate policy. The script is added to the list of reference scripts available to use in scriptable throttling filters.

6. Select [icon: chain, set=fa]Chain, and change the order of the filters so [icon: filter, set=fa]Throttling comes after [icon: key, set=fa]Authorization.

7. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

8. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

## Proxy for websocket traffic in Structured Editor

This section describes how to set up PingGateway to proxy WebSocket traffic, in the structured editor of Studio. For more information about how to set up proxying for WebSocket traffic, refer to [WebSocket traffic with PingAM](../gateway-guide/websocket.html).

1. In PingGateway Studio, create a route:

   1. Go to `http://ig.example.com:8085/studio`, and then select [icon: plus, set=fa]Create a route.

   2. Select [icon: list-ul, set=fa]Structured to use the structured editor.

2. Select Advanced options on the right, and create a route with the following options:

   * Base URI: `https://app.example.com:8444`

   * Condition: Path: `/websocket-se`

   * Name : `websocket-se`

   * Enable WebSocket: Select this option

     1. Select [icon: user, set=fa]Authentication.

     2. Select Single Sign-On, and enter the following information:

        * AM service : Configure an AM service to use for authentication:

          * URI: `http://am.example.com:8088/openam`

          * Secrets Provider: `SystemAndEnvSecretStore-1`

          * Agent :

            * Username : `ig_agent`

            * Password Secret ID : `password.secret.id`

     Leave all other values as default.

3. On the top-right of the screen, select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display to review the route.

4. Select [icon: cloud-upload-alt, set=fa]Deploy to push the route to the PingGateway configuration.

   You can check the `$HOME/.openig/config/routes` folder to see that the route is there.

---

---
title: PingGateway Studio
description: Overview of PingGateway Studio and how to use it to design and develop routes to protect your applications
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:preface
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/preface.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Routes", "Security", "User Interface"]
page_aliases: ["index.adoc"]
---

# PingGateway Studio

This guide gives an overview of how to use Studio to design and develop routes to protect applications.

---

---
title: Restrict access to Studio
description: Configure PingGateway to restrict Studio access using a studioProtectionFilter with SingleSignOnFilter and CSRF protection
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:restrict-access
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/restrict-access.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-01-02T12:52:32Z
keywords: ["Routes", "Security", "User Interface"]
---

# Restrict access to Studio

When PingGateway is running in development mode, by default the Studio endpoint is open and accessible. To allow only specific users to access Studio, configure a `"studioProtectionFilter"` in `admin.json` with a SingleSignOnFilter or CrossDomainSingleSignOnFilter.

The following example uses a SingleSignOnFilter to require users to authenticate with AM before they can access Studio, and protects the request from Cross Site Request Forgery (CSRF) attacks.

1. Set up AM:

   1. Select Services > Add a Service and add a Validation Service with the following Valid goto URL Resources:

      * `http://ig.example.com:8085/*`

      * `http://ig.example.com:8085/*?*`

   2. Register a PingGateway agent with the following values, as described in [Register a PingGateway agent in AM](preface.html#register-agent-am):

      * Agent ID: `ig_agent`

      * Password: `password`

        |   |                                                                                                                   |
        | - | ----------------------------------------------------------------------------------------------------------------- |
        |   | Use secure passwords in a production environment. Consider using a password manager to generate secure passwords. |

2. Set up PingGateway:

   1. Set an environment variable for the PingGateway agent password, and then restart PingGateway:

      ```console
      $ export AGENT_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by a SystemAndEnvSecretStore, and must be base64-encoded.

   2. Add the following `admin.json` configuration to PingGateway:

      ```json
      {
        "mode": "DEVELOPMENT",
        "properties": {
          "SsoTokenCookieOrHeader": "iPlanetDirectoryPro"
        },
        "adminConnector": {
          "host": "ig.example.com",
          "port": 8085
        },
        "connectors": [
          {
            "port": 8080
          },
          {
            "port": 8443
          }
        ],
        "heap": [
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          },
          {
            "name": "AmService-1",
            "type": "AmService",
            "config": {
              "agent" : {
                "username" : "ig_agent",
                "passwordSecretId" : "agent.secret.id"
              },
              "secretsProvider": "SystemAndEnvSecretStore-1",
              "url": "http://am.example.com:8088/openam/",
              "ssoTokenHeader": "&{SsoTokenCookieOrHeader}"
            }
          }
        ],
        "studioProtectionFilter": {
          "type": "ChainOfFilters",
          "config": {
            "filters": [
              {
                "type": "SingleSignOnFilter",
                "config": {
                  "amService": "AmService-1"
                }
              },
              {
                "type": "CsrfFilter",
                "config": {
                  "cookieName": "&{SsoTokenCookieOrHeader}",
                  "failureHandler": {
                    "type": "StaticResponseHandler",
                    "config": {
                      "status": 403,
                      "headers": {
                        "Content-Type": [
                          "text/plain"
                        ]
                      },
                      "entity": "Request forbidden"
                    }
                  }
                }
              }
            ]
          }
        }
      }
      ```

      Source: [admin-StudioProtectionFilter.json](../_attachments/config/admin-StudioProtectionFilter.json)

      Notice the following features of the configuration:

      * The `mode` is `development`, so by default the Studio endpoint is open and unfiltered.

      * The `properties` object sets a configuration parameter for the value of the SSO token cookie or header, which is used in AmService and CorsFilter.

      * The AmService uses the PingGateway agent in AM for authentication.

        The agent password for AmService is provided by a SystemAndEnvSecretStore in the heap.

      * The `"studioProtectionFilter"` calls the [SingleSignOnFilter](../reference/SingleSignOnFilter.html) to redirect unauthenticated requests to AM. It uses the [CsrfFilter](../reference/CsrfFilter.html) to protect requests from CSRF attacks.

   3. Restart PingGateway to take into account the changes to `admin.json`.

3. Test the setup:

   1. If you are logged in to AM, log out and clear any cookies.

   2. Go to <http://ig.example.com:8085/studio>. The SingleSignOnFilter redirects the request to AM for authentication.

   3. Log in to AM with user `demo`, password `Ch4ng31t`. The Studio Routes screen is displayed.

---

---
title: Starting with Studio
description: Get started with PingGateway Studio — a UI for building and deploying routes using the FreeForm Designer or structured editor
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:about
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/about.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Routes", "Security", "User Interface", "JSON"]
section_ids:
  access_to_studio: Access to Studio
  upgrades_and_secrets: Upgrades and secrets
---

# Starting with Studio

PingGateway Studio is a user interface to help you build and deploy your PingGateway configuration. There are two ways to create routes in Studio:

* With the *structured editor* (deprecated) to build simple routes by using predefined menus and templates. The structured editor presents valid options and default values as you add filters, decorators, and other objects to your configuration.

* With the *FreeForm Designer* to design complex, multi-branched routes. Drag handlers and filters from a sidebar onto the canvas to begin designing the route. The FreeForm Designer helps you to visualize the chain and track the path of requests, responses, and contexts.

By default, PingGateway is in production mode. The `/routes` endpoint isn't exposed or accessible, effectively disabling Studio.

## Access to Studio

Configure access to Studio by following these steps:

1. Install PingGateway as described in [Getting started with PingGateway](../getting-started/preface.html).

2. Switch PingGateway to [development mode](../configure/operating-modes.html).

   For example, add the following configuration to `admin.json` and restart PingGateway:

   ```json
   {
     "mode": "DEVELOPMENT",
     "adminConnector": {
       "host": "localhost",
       "port": 8085
     },
     "connectors": [
       {
         "port": 8080
       }
     ]
   }
   ```

   Source: [admin-dev.json](../_attachments/config/admin-dev.json)

3. Configure PingGateway to connect to the sample application over HTTPS with a route to access static resources:

   Learn more in [Using the sample application](../getting-started/start-sampleapp.html), making sure to restart PingGateway to load your changes.

   When you configure PingGateway with a `config.json` file, include a main router named `_router` as in the example.

4. With PingGateway installed and running in development mode, go to <http://ig.example.com:8085/studio> to access Studio.

   The browser displays the Routes screen:

   ![The \[.label\]#Routes# screen is displayed in Studio.](_images/studio-welcome-page.png)

## Upgrades and secrets

During PingGateway upgrade, PingGateway transfers routes you created previously in Studio automatically. Where possible, PingGateway replaces deprecated settings with the newer evolved settings. If PingGateway needs additional information to upgrade a route, the route status becomes [icon: exclamation-triangle, set=fa]Compatibility update required. Select the route and provide the requested information.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't configure secrets providers in Studio.Documentation examples generated with Studio refer to secrets providers you must configure separately in `config.json`. |

---

---
title: Summary of tasks, route status, and icons
description: Reference tables summarizing Studio tasks, route status indicators, and icons in PingGateway
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:task-summary
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/task-summary.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-09-10T14:57:24Z
keywords: ["Routes", "Security", "User Interface"]
---

# Summary of tasks, route status, and icons

The following tables summarize the basic tasks that you can do in Studio, and summarizes the icons and status displayed in Studio:

**Task reference**

| To do this                             | Do this                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Create a new route                     | Select [icon: sitemap, set=fa]ROUTES, [icon: plus, set=fa]Create a route.                               |
| Select a route                         | Select [icon: sitemap, set=fa]ROUTES, and then select a route to view.                                  |
| Display the config of a selected route | Select a route, and then select [icon: ellipsis-v, set=fa]and [icon: share-square, set=fa]Display.      |
| Deploy a selected route                | Select a route, and then select [icon: cloud-upload-alt, set=fa]Deploy.                                 |
| Undeploy a selected route              | Select a deployed route, and then select [icon: ellipsis-v, set=fa]and [icon: times, set=fa]Undeploy.   |
| Change the basic config of a route     | Select a route, and then select [icon: cog, set=fa]Route settings. Edit the route and save the changes. |

**Route status**

| Status                                                            | Description                                                                                                               | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [icon: exclamation-circle, set=fa]Undeployed                      | The route is saved in Studio but is not deployed to the backend.                                                          | Deploy the route. The status changes to [icon: check-circle, set=fa]Deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [icon: check-circle, set=fa]Deployed                              | The route is saved in Studio and deployed to the backend.                                                                 | None. The route has the same configuration in Studio and the backend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [icon: exclamation-circle, set=fa]Changes pending                 | The route has been deployed and then subsequently changed in Studio.                                                      | Deploy the route. The status changes to [icon: check-circle, set=fa]Deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [icon: exclamation-triangle, set=fa]Out of sync                   | The route has been deployed and then subsequently changed in the backend, or in both Studio and the backend.              | Select [icon: cloud-upload-alt, set=fa]Deploy. A message informs you that a different version of the route is deployed in the backend. Select an option:- [icon: cloud-upload-alt, set=fa]Deploy: The version in Studio overwrites the backend.

- [icon: upload, set=fa]Import a route: The version in the backend overwrites Studio.When you import a route into Studio you go into **editor mode**. You can use the JSON editor to manually edit the route, but can no longer use the full Studio interface to add or edit filters. |
| [icon: exclamation-triangle, set=fa]Compatibility update required | The route was created in Studio in an earlier version of PingGateway. Some information is needed to complete the upgrade. | Enter the information as prompted, and then select [icon: cloud-upload-alt, set=fa]Deploy to deploy the route.                                                                                                                                                                                                                                                                                                                                                                                                                         |

**Icons**

| Icon                                   | Mode              | Description                                                                                  |
| -------------------------------------- | ----------------- | -------------------------------------------------------------------------------------------- |
| [icon: list-ul, set=fa]                | Structured editor | The route was created and edited using the menus and options of structured editor.           |
| **{ }**                                | Editor mode       | The route was imported into Studio, or was created in Studio and then edited in editor mode. |
| ![FreeForm Icon](_images/freeform.svg) | Freeform designer | The route was created on the canvas of FreeForm Designer.                                    |

---

---
title: Upgrade from an earlier version of Studio
description: Upgrade routes created in earlier versions of PingGateway Studio, including automatic migration for secrets and audit event handlers
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:upgrade
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/upgrade.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-09-10T14:57:24Z
keywords: ["u=Upgrade"]
---

# Upgrade from an earlier version of Studio

From PingGateway 2024.3, Studio manages the migration of deprecated objects for routes created and managed in earlier versions of Studio.

PingGateway doesn't manage migration for the following:

* Routes in Studio editor mode

* Custom filters in routes

  * Migration for routes containing secrets

    PingGateway automatically:

    * Updates the route to use SecretsProvider and SecretIds

    * Removes references to the password

    You must manually create the required SecretsProvider in `config.json` and create its referenced secrets.

  * Migration for routes containing Splunk or ElasticSearch audit event handlers

    PingGateway automatically deletes the Splunk or ElasticSearch audit event handlers from the route.