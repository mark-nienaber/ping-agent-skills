---
title: Create and edit routes with Freeform Designer
description: Create and edit PingGateway routes in the FreeForm Designer of Studio, and add objects, filters, and decorators to routes
component: pinggateway
version: 2026
page_id: pinggateway:studio-guide:freeform
canonical_url: https://docs.pingidentity.com/pinggateway/2026/studio-guide/freeform.html
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
