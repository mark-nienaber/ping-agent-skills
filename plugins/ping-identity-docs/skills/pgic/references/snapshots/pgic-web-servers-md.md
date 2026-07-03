---
title: Web servers and Ingress
description: Web servers proxies HTTP requests to web application servers, while Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.
component: pgic
page_id: pgic::pgic_web_servers
canonical_url: http://docs.pingidentity.com/pgic/pgic_web_servers.html
---

# Web servers and Ingress

Web servers proxies HTTP requests to web application servers, while Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.

Ping Government Identity Cloud is deployed with a variety of host name URLs by default, but it's important that you use your own host name URLs. Using the default URLs can cause issues for your users if you have a multi-region deployment or plan to in the future.