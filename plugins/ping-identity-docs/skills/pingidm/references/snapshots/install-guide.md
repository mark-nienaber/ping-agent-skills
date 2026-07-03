---
title: Additional servlet filters
description: Register and configure PingIDM Jetty servlet filters for CORS and large-payload protection (custom servlet filters removed in 8.0)
component: pingidm
version: 8.1
page_id: pingidm:install-guide:register-servlet-filters
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/register-servlet-filters.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Jetty", "Configuration", "Servlet Filter"]
---

# Additional servlet filters

|   |                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Custom servlet filters aren't supported in IDM 8.0 and later. The only `servletfilter-*` configurations you can continue to use are `CrossOriginFilter` and `LargePayloadServletFilter`. Learn more in [Discontinued functionality](../release-notes/removed-functionality.html#removed-custom-servlet-filters-80). |

You can register and customize only the `org.eclipse.jetty.ee10.servlets.CrossOriginFilter` and `org.forgerock.openidm.jetty.LargePayloadServletFilter` servlet filters. These filters are available to protect against cross-site request forgery and overly large request payloads.

A sample servlet filter configuration is provided in the `/path/to/openidm/conf/servletfilter-cors.json` file:

```json
{
    "initParams" : {
        "allowedOrigins" : "https://localhost:&{openidm.port.https}",
        "allowedMethods" : "GET,POST,PUT,DELETE,PATCH",
        "allowedHeaders" : "accept,x-openidm-password,x-openidm-nosession,
                           x-openidm-username,content-type,origin,
                           x-requested-with",
        "allowCredentials" : true,
        "chainPreflight" : false
    },
    "urlPatterns" : [
        "/*"
    ],
    "filterClass" : "org.eclipse.jetty.servlets.CrossOriginFilter"
}
```

The sample configuration includes the following properties:

* `filterClass`

  (String) The servlet filter to register.

The following additional properties can be configured for the filter:

* `httpContextId`

  (String) The HTTP context in which to register the filter. Default value `"openidm"`.

* `servletNames`

  (Array of strings) A list of servlet names where the filter should apply. Default value `["OpenIDM REST"]`.

* `urlPatterns`

  (Array of strings) A list of URL patterns where the filter applies. Default value `["/*"]`.

* `initParams`

  (Object) A map of initialization parameters passed to the servlet filter's `init` method. Keys are strings, and values can be strings, booleans, or numbers. For parameters that accept multiple values, use a comma-delimited string. Learn more in the [Interface FilterConfig](https://docs.oracle.com/javaee/5/api/javax/servlet/FilterConfig.html) documentation.
