---
title: Deployment configuration locations
description: Understand where to store PingAM configuration and run-time data, including options for directory servers and JSON files, and recommendations for high-availability deployments
component: pingam
version: 8.1
page_id: pingam:deployment-planning:deploy-configuration-types
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/deploy-configuration-types.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "configuration store"]
page_aliases: ["deployment-planning-guide:deploy-configuration-types.adoc"]
section_ids:
  store-config-in-pingds: Store configuration in PingDS
  store-config-in-fbc: Store configuration in files
  store-runtime-data: Store run-time data
---

# Deployment configuration locations

Every AM deployment has associated *configuration* data. Configuration data consists of properties and settings used by the AM instance to function.

Configuration data is often referred to as *static*, because after your instance is configured to your requirements, it doesn't need to be changed.

Configuration data includes properties and settings for the following:

* Global services

* Realms

* Authentication trees

Configuration data can be stored in directory servers or in JSON files on the local file system. Each option is tailored to a specific deployment requirement.

## Store configuration in PingDS

Storing configuration data in DS datastores offers deployment flexibility and provides instance high availability.

Configuration data in the DS instances is shared between the AM instances in your deployment. The configuration data can be replicated between multiple DS instances in a cluster, and made available to AM instances in different regions, improving availability, and data integrity.

![Replicate data between multiple DS instances in a cluster.](_images/ds-config-store.png)

You can find information on installing AM instances with configuration datastores in [Prepare a configuration store](../installation/prepare-configuration-store.html).

## Store configuration in files

File-based configuration (FBC) is best-suited to a DevOps-style deployment, with the associated tools and practices of that approach.

Static FBC data is written to configuration files in the file system and checked into a source control system, such as Git.

AM instances are created as Docker images, with the FBC incorporated into the image.

![Kubernetes deployment using file-based configuration.](../_images/docker-deployment.png)

You can insert variables into these configuration files before you check them into source control. The variables are substituted with the appropriate values at runtime when you start the Docker container. Using variables lets you reuse the same base configuration files for multiple instances, and different staging environments. For example, development, QA, or pre-production, which are then promoted to production.

Learn more about FBC in [Store configuration data in JSON files](../installation/fbc.html).

Learn more about installing AM instances with Kubernetes in the [ForgeOps](https://docs.pingidentity.com/forgeops/2025.1) documentation.

## Store run-time data

AM instances also create dynamic, run-time data. This data can change and grow frequently, even in a production instance, as business logic changes.

Dynamic data includes properties, settings, and values for the following:

* Policies, policy sets, and resource types

* OAuth 2.0 client profiles

* Federation entities

* Core Token Service (CTS) tokens

* UMA resources, labels, audit messages, and pending requests

Dynamic data is stored in one or more DS instances. You can choose to store dynamic data alongside the configuration data, or separate it into different datastores.

How you separate dynamic data into datastores depends on the volume of dynamic data you expect to handle. For example, CTS data is often highly volatile and short-lived, so it warrants its own set of tuned DS instances. The other dynamic data types might not be as volatile and could potentially all share a set of differently tuned DS instances.

You can find information on setting up DS stores for use with AM in [Prepare datastores](../installation/prepare-ext-stores.html)

---

---
title: Deployment planning
description: Plan PingAM deployments by designing architecture, topology, and hardware requirements, plus implementing training, customization, and proof-of-concept development
component: pingam
version: 8.1
page_id: pingam:deployment-planning:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning"]
page_aliases: ["index.adoc", "deployment-planning-guide:preface.adoc"]
---

# Deployment planning

These topics help you to plan the deployment of PingAM, including implementing training teams and partners, customization and hardening, and development of a proof-of-concept implementation.

This guide is written for access management designers, developers, and administrators who build, deploy, and maintain PingAM services and features for their organizations.

[icon: book, set=fad, size=3x]

#### [Identity Access Management](understanding-iam.html)

Discover how AM helps to secure your resources.

[icon: landmark, set=fad, size=3x]

#### [Deployment architecture](planning-architecture-onprem.html)

Create a good, concrete deployment plan.

[icon: cloud, set=fad, size=3x]

#### [Deployment topology](deploy-topologies-onprem.html)

View an example, large scale topology.

[icon: expand-arrows-alt, set=fad, size=3x]

#### [Size hardware and services](deploy-sizing.html)

Size servers, network, storage, and service levels.

[icon: server, set=fad, size=3x]

#### [Deployment requirements](deploy-hardware-requirements.html)

Learn about the deployment requirements for PingAM sizing.

[icon: play, set=fad, size=3x]

#### [Quick start](deploy-highlevel-start.html)

Get started with an PingAM deployment.

---

---
title: Deployment requirements
description: System requirements for deploying PingAM servers, including disk storage for binaries, configuration, logs, and RAM requirements
component: pingam
version: 8.1
page_id: pingam:deployment-planning:deploy-hardware-requirements
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/deploy-hardware-requirements.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "storage"]
page_aliases: ["deployment-planning-guide:deploy-hardware-requirements.adoc"]
section_ids:
  storage-requirements-server: Server disk storage requirements
  storage-requirements-pa: Web and Java agents disk storage requirements
  storage-requirements-openig: PingGateway disk storage requirements
  storage-requirements-recommendations: Disk storage recommendations
  ram-requirements: RAM requirements
  deploy-software-requirements: Software requirements
---

# Deployment requirements

This page lists initial system requirements for deploying AM servers:

## Server disk storage requirements

Disk storage requirements for AM servers depend partly on AM itself and partly on your deployment. Disk storage requirements also depend on the space needed for binaries, configuration data, and log files.

* For initial installation, a few hundred MB is enough, not including the downloaded files.

* The AM `.war` file size varies from release to release. If your container holds one `.war` file and one directory with the contents of the `.war` file, the disk space required is in excess of 600 MB.

  This space requirement remains stable as you use AM.

* By default, AM servers write audit logs to flat files under `/path/to/am/var/audit`. Alternatively, AM servers can write audit logs to `syslog`, or to a relational database.

  When using flat-file audit logging, you can configure rotation and purging for logs under `/path/to/am/var/audit`, so you can effectively cap the maximum disk space used for logs.

  Retain the information you need before purging logs.

  AM logs errors and access messages. Make sure your disk can keep pace with the volume of logging, which can be significant in high-volume deployments.

  Learn more about audit logging configuration in [Audit logging](../monitoring/audit-logging.html).

* By default, AM servers write debug logs to flat files under `/path/to/am/var/debug`. You can configure rotation for debug logs.

  Because you can change debug log levels at runtime when investigating issues, debug log volume is not as predictable as for regular logs. Leave a margin in production environments, so that you can turn up debug log levels to diagnose problems.

  Learn more about debug logging configuration in [Debug logging](../monitoring/debug-logging.html).

* AM stores policy information in the configuration directory. The space this takes up depends on the policies you have.

* By default, AM stores CTS information in the configuration directory. The space this takes up depends on the volume of traffic to the server and whether AM is configured for [client-side](../am-sessions/client-based-sessions.html) sessions.

* Tune the underlying DS servers to handle multiple client connections.

Learn more about tuning DS in the [DS Release Notes](https://docs.pingidentity.com/pingds/release-notes/requirements.html#prerequisites-operating-systems).

## Web and Java agents disk storage requirements

Web and Java agent binaries do not require more than a few MB of disk space, although they may require additional free space to store configuration files, POST data cache files, and others. Refer to the installation requirements of your web or Java agent for more information.

You should also consider the web or Java agent logging when provisioning disk storage:

* Web and Java agents can log audit messages locally to the agent installation or can send them to the AM instances. Refer to the configuration reference of your agent for more information.

* Debug messages are logged to files local to the agent installation, and their volume depends on the debug log level. In production environments, provision additional storage to ensure you can enable higher debug log levels for diagnostic purposes.

Learn more about agents in the [Web Agents documentation](https://docs.pingidentity.com/web-agents/2025.3) and the [Java Agents documentation](https://docs.pingidentity.com/java-agents/2025.3).

## PingGateway disk storage requirements

PingGateway can vary in size from release to release. On disk, the `.zip` file is under 75 MB. If you keep both the `.zip` file and the unzipped version, the total size is under 150 MB.

By default, PingGateway configuration files are located under `$HOME/.openig` (on Windows `%appdata%\OpenIG`).

Log messages in PingGateway and third-party dependencies are recorded using Logback, and are stored under `$HOME/.openig/logs`.

As for other components, debug logging volume depends on log level. Leave a margin in production environments so that you can turn up debug log levels to diagnose problems.

Learn more about logging in [Manage Logs](https://docs.pingidentity.com/pinggateway/2025.11/maintenance-guide/logging.html).

## Disk storage recommendations

The following are based on the preceding information in this section. When deciding on disk storage, keep the following recommendations in mind:

* Plan enough space and enough disk I/O to comfortably absorb the load for logs.

  Check your assumptions in testing. For example, make sure that logs are cleaned up so they don't exceed your space threshold even in long-duration testing.

* When using local web or Java agent logs, make sure you have a mechanism in place to clean them up.

* For PingGateway, make sure you turn off unnecessary logging and handler debug logging before moving to production.

## RAM requirements

AM core services require a minimum JVM heap size of 1 GB. In production environments, the JVM heap size should be at least 2 to 3 GB.

|   |                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Make sure the `Xms` and `Xmx` JVM parameters are set to the same value to prevent a large garbage collection as the memory profile increases from the default up to the `Xms` value. Also, setting `Xms` and `Xmx` to the same value ensures that small controlled garbage collection events minimize application unresponsiveness. |

## Software requirements

Refer to [Requirements](https://docs.pingidentity.com/pingam/release-notes/requirements.html) in the Release notes for up-to-date information about the software requirements for this version.

---

---
title: Example deployment topology
description: Configure PingAM deployment topology across multiple data centers with highly available and scalable architecture using load balancers, reverse proxies, and DMZ security layers
component: pingam
version: 8.1
page_id: pingam:deployment-planning:deploy-topologies-onprem
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/deploy-topologies-onprem.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "architecture", "availability", "failover", "agent"]
page_aliases: ["deployment-planning-guide:deploy-topologies-onprem.adoc"]
section_ids:
  public-tier: The public tier
  about-the-app-tier: The application tier
  openam-agents: PingAM agents
  openam-sites: Sites
  backend-ds: Backend directory servers
  realms: Realms
---

# Example deployment topology

You can configure AM in a wide variety of deployments depending on your security requirements and network infrastructure. This page presents an example enterprise deployment, featuring a highly available and scalable architecture across multiple data centers.

The following illustration presents an example topology of a multi-city multi-data-center deployment across a wide area network (WAN). The example deployment is partitioned into a two-tier architecture. The top tier is a DMZ with the initial firewall securing public traffic into the network. The second firewall limits traffic from the DMZ into the application tier where the protected resources are housed.

The example components in this page are presented for illustrative purposes. Ping Identity doesn't provide guidance on specific products, such as reverse proxies, load balancers, switches, firewalls, and so on, as AM can be deployed within your existing networking infrastructure.

![The example AM deployment across multi-data centers.](_images/active-active-deployment.svg)Figure 1. Deployment example

Read the following sections for more information about the different actors in the example:

## The public tier

The public tier provides an extra layer of security with a DMZ consisting of load balancers and reverse proxies. This section presents the DMZ elements:

> **Collapse: The global load balancer**
>
> The example deployment uses a global load balancer (GLB) to route DNS requests efficiently to multiple data centers. The GLB reduces application latency by spreading the traffic workload among data centers and maintains high availability during planned or unplanned downtime, during which it quickly reroutes requests to another data center to ensure online business activity continues successfully.
>
> You can install a cloud-based or a hardware-based version of the GLB. The leading GLB vendors offer solutions with extensive health-checking, site affinity capabilities, and other features for most systems. Detailed deployment discussions about global load balancers are beyond the scope of this document.

> **Collapse: Front-end local load balancers**
>
> Each data center has local front-end load balancers to route incoming traffic to multiple reverse proxy servers, thereby distributing the load based on a scheduling algorithm. Many load balancer solutions provide server affinity or stickiness to efficiently route a client's inbound requests to the same server. Other features include health checking to determine the state of its connected servers, and SSL offloading to secure communication with the client.
>
> You can cluster the load balancers themselves or configure load balancing in a clustered server environment, which provides data and session high availability across multiple nodes. Clustering also allows horizontal scaling for future growth. Many vendors offer hardware and software solutions for this requirement. In most cases, you must determine how you want to configure your load balancers, for example, in an active-passive configuration that supports high availability, or in an active-active configuration that supports session high availability.
>
> There are many load balancer solutions available in the market. You can set up an external network hardware load balancer, or a software solution like HAProxy (L4 or L7 load balancing) or Linux Virtual Server (LVS) (L4 load balancing), and many others.

> **Collapse: Reverse proxies**
>
> The reverse proxies work in concert with the load balancers to route the client requests to the back end Web or application servers, providing an extra level of security for your network. The reverse proxies also provide additional features, like caching to reduce the load on the Web servers, HTTP compression for faster transmission, URL filtering to deny access to certain sites, SSL acceleration to offload public key encryption in SSL handshakes to a hardware accelerator, or SSL termination to reduce the SSL encryption overhead on the load-balanced servers.
>
> The use of reverse proxies has several key advantages. First, the reverse proxies serve as an highly scalable SSL layer that can be deployed inexpensively using freely available products, like Apache HTTP server or nginx. This layer provides SSL termination and offloads SSL processing to the reverse proxies instead of the load balancer, which could otherwise become a bottleneck if the load balancer is required to handle increasing SSL traffic.
>
> [Front-end load balancer reverse proxy layer](#figure-active-frontend-lbs-detailed) illustrates one possible deployment using HAProxy in an active-passive configuration for high availability. The HAProxy load balancers forward the requests to Apache 2.2 reverse proxy servers. For this example, we assume SSL is configured everywhere within the network.
>
> ![Using HAProxy as front-end load balancers to reverse proxies](_images/active-frontend-lbs-detailed.svg)
>
> Figure 2. Front-end load balancer reverse proxy layer
>
> Another advantage to reverse proxies is that they allow access to only those endpoints required for your applications. If you need the authentication user interface and OAuth2/OpenID Connect endpoints, then you can expose only those endpoints and no others. A good rule of thumb is to check which functionality is required for your public interface and then use the reverse proxy to expose only those endpoints.
>
> A third advantage to reverse proxies is when you have applications that sit on non-standard containers for which Ping Identity doesn't provide a native agent. In this case, you can implement a reverse proxy in your web tier, and deploy a web or Java agent on the reverse proxy to filter any requests.
>
> [Front-end load balancers and reverse proxies with agent](#figure-active-frontend-lbs-rp-with-agent) shows a simple topology diagram of your Web tier with agents deployed on your reverse proxies. The dotted agents indicate that they can be optionally deployed in your network depending on your configuration, container type, and application.
>
> ![Using HAProxy as front-end load balancers to reverse proxies with agents](_images/active-frontend-lbs-rp-with-agent.svg)
>
> Figure 3. Front-end load balancers and reverse proxies with agent

> **Collapse: PingGateway**
>
> PingGateway is a specialized reverse proxy that allows you to secure web applications and APIs, and integrate your applications with identity and access management.
>
> PingGateway extends AM's authentication and authorization services to provide SSO and API security across mobile applications, social applications, partner applications, and web applications. When used in conjunction with AM, PingGateway intercepts HTTP requests and responses, enforces authentication and authorization, and provides throttling, auditing, password replay, and redaction or enrichment of messages.
>
> PingGateway runs as a standalone Java application, and can be deployed inside a Docker container.
>
> ![The example deployment using front-end load balancers to reverse proxies.](_images/active-frontend-lbs.svg)
>
> Figure 4. Front-end load balancers
>
> |   |                                                                                                                                                                                                                                                                                            |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | Some authentication nodes may require additional user information to authenticate, such as the IP address where the request originated. When AM is accessed through a load balancer or proxy layer, you can configure AM to consume and forward this information with the request headers. |

> **Collapse: SSL termination**
>
> One important security decision ia whether to terminate SSL or offload your SSL connections at the load balancer. Offloading SSL effectively decrypts your SSL traffic before passing it on as HTTP or at the reverse proxy. Another option is to run SSL pass-through where the load balancer does not decrypt the traffic but passes it on to the reverse proxy servers, which are responsible for the decryption. The other option is to deploy a more secure environment using SSL everywhere within your deployment.

## The application tier

The application tier is where the protected resources reside on Web containers, application servers, or legacy servers. AM web and Java agents intercept all access requests to protected resources on the web servers and grant access to the user based on AM policy decisions. You can find a list of supported containers in [Application containers](https://docs.pingidentity.com/pingam/release-notes/requirements.html#prerequisites-application-servers).

Because AM is Java-based, you can install the server on a variety of platforms, such as Linux, Solaris, and Windows. You can find the list of platforms on which AM has been tested in [Operating systems](https://docs.pingidentity.com/pingam/release-notes/requirements.html#operating-systems).

![A simplified deployment of web servers with agents](_images/app-svr-deployment.svg)Figure 5. App Server Deployment

> **Collapse: How does it work?**
>
> When the client sends an access request to a resource, the web or Java agent redirects the client to an authentication login page. Upon successful authentication, the web or Java agent forwards the request via the load balancer to one of the AM servers.
>
> In AM deployments storing authenticated sessions in the CTS token store, the AM server that satisfies the request maintains the authenticated session in its in-memory cache to improve performance. If a request for the same user is sent to another AM server, that server must retrieve the authenticated session from the CTS token store, incurring a performance overhead.
>
> Client-side authenticated sessions are held by the client and passed to AM on each request. For security reasons, you should sign and encrypt client-side authenticated sessions. However, depending on the signing or encryption algorithms, decrypting sessions on each request can be an expensive operation. To improve performance, the decrypt sequence is cached in AM's memory. If a request for the same user is sent to another AM server, that server must decrypt the session again, incurring a performance overhead.
>
> Therefore, even if sticky load balancing is not a requirement when deploying AM, it is recommended for performance.
>
> Server-side and client-side journey sessions share the same characteristics as their server-side and client-side authenticated session counterparts. Therefore, their performance also benefits from sticky load balancing.
>
> In-memory journey sessions, however, require sticky load balancing to make sure the same AM server handles the authentication flow for a user. If a request is sent to a different AM server, the authentication flow restarts.
>
> AM provides a cookie (default: `amlbcoookie`) for sticky load balancing to ensure that the load balancer optimally routes requests to the AM servers. The load balancer inspects the cookie to determine which AM server should receive the request. This makes sure all subsequent requests for a journey or authenticated session are routed to the same server.

## PingAM agents

PingAM agents are components installed on web servers or Java containers that protect resources, such as websites and applications. Interacting with AM, web and Java agents ensure that inbound requests to protected resources are authenticated and authorized.

AM provides two agents:

* **Web agent**. Comprised of agent modules tailored to each web server and several native shared libraries. Configure the web agent in the web server's main configuration file.

  > **Collapse: Web agents simplified flow**
  >
  > ![The web agent acts as a gatekeeper to a protected resource.](_images/web-policy-agent.svg)
  >
  > Figure 6. Web agent
  >
  > Learn more in the [Web Agents documentation](https://docs.pingidentity.com/web-agents/2025.3).

* **Java agent**. Comprised of an agent filter, an agent application, and the AM SDK libraries.

  > **Collapse: Java agents simplified flow**
  >
  > ![The Java agent is installed in an application server.](_images/jee-policy-agent.svg)
  >
  > Figure 7. Java agent
  >
  > The figure represents the agent filter (configured in the protected Java application), and the agent application (deployed in the Java container) in the same box as a simplification.
  >
  > Learn more in the [Java Agents documentation](https://docs.pingidentity.com/java-agents/2025.3).

Web and Java agents provide the following capabilities, among others:

* **Cookie reset**. Web and Java agents can reset any number of cookies in the journey session before the client is redirected for authentication. Reset cookies when the agent is deployed with a parallel authentication mechanism and when cookies need to be reset between mechanisms.

* **Authentication-only mode**. Instead of enforcing both authentication and resource-based policy evaluation, web and Java agents can enforce authentication only. Use the authentication-only mode when there is no need for fine-grain authorization to particular resources, or when you can provide authorization by different means.

* **Not-enforced lists**. Web and Java agents can bypass authentication and authorization and grant immediate access to specific resources or client IP addresses. Use not-enforced lists to configure URL and URI lists of resources that does not require protection, or client IP lists for IPs that do not require authentication or authorization to access specific resources.

* **URL checking and correction**. Web and Java agents require that clients accessing protected resources use valid URLs with fully qualified domain names (FQDNs). If invalid URLs are referenced, policy evaluation can fail as the FQDN will not match the requested URL, leading to blocked access to the resource. Misconfigured URLs can also result in incorrect policy evaluation for subsequent access requests. Use FQDN checking and correction when clients may specify a resource URL that differs from the FQDN configured in AM's policies, for example, in environments with load balancers and virtual hosts.

* **Attribute injection**. Web and Java agents can inject user profile attributes into cookies, requests, and HTTP headers. Use attribute injection, for example, with websites that address the user by the name retrieved from the user profile.

* **Notifications**. AM can notify web and Java agents about configuration and session state changes. Notifications affect the validity of the web or Java agent caches, for example, requesting the agent to drop the policy and session cache after a change to policy configuration.

* **Cross-domain single sign-on (CDSSO)**. Web and Java agents can be configured to provide [cross-domain single sign-on](../am-authentication/about-sso.html) capabilities. Configure CDSSO when the web or Java agents and the AM instances are in different DNS domains.

* **POST data preservation**. Web and Java agents can preserve HTML form data posted to a protected resource by an unauthenticated client. Upon successful authentication, the agent recovers the data stored in the cache and auto-submits it to the protected resource. Use POST data preservation, for example, when users or clients submit large amounts of data, such as blog posts and wiki pages, and their sessions are short-lived.

* **Continuous security**. Web and Java agents can collect inbound login requests' cookie and header information which an AM server-side authorization script can then process. Use continuous security to configure AM to act upon specific headers or cookies during the authorization process.

* **Conditional redirection**. Web and Java agents can redirect users to specific AM instances, AM sites, or websites other than AM based on the incoming request URL. Configure conditional redirection login and logout URLs when you want to have fine-grained control over the login or logout process for specific inbound requests.

Learn more in the [Web Agents documentation](https://docs.pingidentity.com/web-agents/2025.3) and the [Java Agents documentation](https://docs.pingidentity.com/java-agents/2025.3).

## Sites

AM provides the capability to logically group two or more redundant AM servers into a *site*, allowing the servers to function as a single unit identified by a site ID across a LAN or WAN. When you set up a single site, you place the AM servers behind a load balancer to spread the load and provide system failover should one of the servers go down for any reason. You can use round-robin or load average for your load balancing algorithms.

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Round-robin load balancing should only be used for the initial access to AM or if the `amlbcookie` is not set; otherwise, cookie-based load balancing should be used. |

In AM deployments with server-side sessions, the set of servers comprising a site provides uninterrupted service. Server-side sessions are shared among all servers in a site. If one of the AM servers goes down, other servers in the site read the authenticated session data from the CTS token store, allowing the user to run new transactions or requests without re-authenticating to the system. The same is true for server-side journey sessions. If one of the AM servers becomes unavailable while authenticating a user, any other server in the site can read the journey session data from the CTS token store and continue with the authentication flow.

AM provides uninterrupted session availability if all servers in a site use the same CTS token store, which is replicated across all servers. Learn more in [Core Token Service (CTS)](../cts/preface.html).

AM deployments configured for client-side authenticated sessions don't use the CTS token store for authenticated session storage and retrieval to make authenticated sessions highly available. Instead, authenticated sessions are stored in HTTP cookies on clients. The same is true for client-side journey sessions.

Journey sessions stored in AM's memory aren't highly available. If the AM server authenticating a user becomes unavailable during the authentication flow, the user needs to start the authentication flow again on a different server.

**Site deployment examples**:

* Routing and load balancing on the AM servers

  The following illustration shows a possible implementation using Linux servers with AM and routing software, like Keepalived, installed on each server. If you require L7 load balancing, you can consider many other software and hardware solutions. AM relies on DS's SDK for load balancing, failover, and heartbeat capabilities to spread the load across the directory servers or to throttle performance.

  ![Possible AM deployment of the app tier](_images/active-app-tier-deployment.svg)Figure 8. Application tier deployment

  |   |                                                                                                                                             |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | When protecting AM with a load balancer or proxy service, configure your container so that AM can trust the load balancer or proxy service. |

* Single load balancer deployment

  You can also set up a load balancer with multiple AM servers. You configure the load balancer to be sticky using the value of the AM cookie, `amlbcookie`, which routes client requests to that primary server. If the primary AM server goes down for any reason, it fails over to another AM server. Session data also continues uninterrupted if a server goes down as it is shared between AM servers. You must also ensure that the container trusts the load balancer.

  You must determine if SSL should be terminated on the load balancer or communication be encrypted from the load balancer to the AM servers.

  ![Single load balancer with multiple servers for high availability](_images/site-deployment-single-lb.svg)Figure 9. Site Deployment With a Single Load Balancer

  The load balancer is a single point of failure. If the load balancer goes down, then the system becomes inoperable.

* Multiple load balancer deployment

  To make the deployment highly available, you add more than one load balancer to the set of AM servers in an active/passive configuration that provides high availability should one load balancer go down for an outage.

  ![Multiple load balancers for high availability](_images/site-deployment-multi-lbs.svg)Figure 10. Site Deployment With Multiple Load Balancers

## Backend directory servers

AM servers require PingDS instances to store policies, configuration data, and CTS tokens.

AM supports multiple stores for deployments that require them. It is possible to install separate DS services for each type of data. If a directory service from another vendor already holds the identity data for the deployment, you can perhaps add a DS service only for policies, configuration, and CTS data.

When determining whether to add multiple DS stores, make sure you test and measure the deployment performance before you decide. It is easy to install more directory servers than necessary, only to find you have significantly complicated deployment management and maintenance without clear benefits. In many cases, a simpler service performs better because it requires less replication traffic and administration.

> **Collapse: Identity stores**
>
> For identity stores, AM provides built-in support for LDAP repositories. You can implement a number of different directory server vendors for storing your identity data, allowing you to configure your directory servers in a number of deployment typologies. You can find a list of supported datastores in [Directory servers](https://docs.pingidentity.com/pingam/release-notes/requirements.html#directory-servers).
>
> When configuring LDAP identity stores, you must manually carry out additional installation tasks that could require a bit more time for the configuration process. For example, you must manually add schema definitions, access control instructions (ACIs), privileges for reading and updating the schema, and resetting user passwords. Learn more in [Prepare identity stores](../installation/prepare-identity-repository.html).
>
> If AM doesn't support your particular identity store type, you can develop your own customized plugin to allow AM to run method calls to fetch, read, create, delete, edit, or authenticate to your identity store data. Learn more in [Customize identity stores](../setup/customizing-data-stores.html).
>
> You can configure AM to require the user to authenticate against a particular identity store for a specific realm. AM associates a realm with at least one identity store and authentication process. When you initially configure AM, you define the identity store for authenticating at the top level realm (/), which is used to administer AM. From there, you can define additional realms with different authentication and authorization services as well as different identity stores if you have enough identity data. Learn more in [Realms](../setup/am-realms.html).

> **Collapse: Configuration datastores**
>
> Configuration data includes authentication information that defines how users and groups authenticate, identity store information, service information, policy information for evaluation, and partner server information that can send trusted SAML assertions. You can find a list of supported datastores in [Directory servers](https://docs.pingidentity.com/pingam/release-notes/requirements.html#directory-servers).
>
> A combined configuration, policy, and application store might be enough for your environment, but you might want to deploy separate policy and/or application stores if required for large-scale systems with many policies, realms, or applications (OAuth 2.0 clients, SAML entities, etc).
>
> You can find more information about datastores and the type of data they contain in [Prepare datastores](../installation/prepare-ext-stores.html).

> **Collapse: CTS datastores**
>
> The CTS provides persistent and highly available token storage for the following:
>
> * Server-side journey and authenticated sessions
>
> * Session denylist (if enabled for [client-side](../am-sessions/client-based-sessions.html) authenticated sessions)
>
> * Journey session allowlist (if enabled for [client-side](../security/auth-session-whitelist.html) journey sessions)
>
> * SAML 2.0-related data (if enabled for Security Token Service token validation and cancellation)
>
> * OAuth 2.0 and UMA 2.0 server-side tokens, and OAuth 2.0 client-side token denylist
>
> * Push notification data during authentication
>
> * Site-wide notification, such as logout or session termination notifications.
>
> CTS traffic is volatile compared to configuration data. To handle the data volatility in high-load deployments, configure an additional DS service, separate from your configuration store, to isolate session and token information. Learn more in [Core Token Service (CTS)](../cts/preface.html).

For high availability, configure AM to use multiple directory servers for a datastore. AM employs internal mechanisms using DS's SDK for load balancing. Let AM perform load balancing between AM and directory servers in one of the following ways:

* AM uses failover (active/passive) load balancing for connections to configuration datastores. When AM uses multiple configuration datastores, AM connects to the primary if it is available. AM only fails over to non-primary servers when the primary is not available.

* AM uses *affinity* load balancing for its pools of connections to CTS token stores and identity stores. Affinity load balancing routes LDAP requests with the same target DN to the same directory server. AM only fails over to another directory server when that directory server becomes unavailable. Affinity load balancing is advantageous because it:

  * Allows AM to use all available directory servers in read-write mode.

  * Combats replication delay between directory servers.

  * Removes the need for end-to-end stickiness to AM for session activities.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The connection strings to the data or identity stores are static and not hot-swappable. This means that, if you expand or contract your DS affinity deployment, AM will not detect the change.To work around this, either:* Manually add or remove the instances from the connection string and restart AM or the container where it runs.

* Configure a [DS proxy](https://docs.pingidentity.com/pingds/8.1/config-guide/proxy.html) in front of the DS instances to distribute data across multiple DS *shards*, and configure the proxy's URL in the connection string. |

You can find details about load balancing and directory services in [On load balancers](https://docs.pingidentity.com/pingds/8.1/config-guide/load-balancing.html) in the PingDS documentation.

[Site deployment with DS datastore service](#figure-site-deployment-ext-datastores) shows a deployment with replicated DS servers for configuration, identities, CTS, policy, and application data. Although not shown in the diagram, you can set up a directory tier, separating the application tier from the stores with another firewall. This tier provides added security for your identity store or policy data.

![Replicated external service for datastores](_images/site-deployment-ext-datastores.svg)Figure 11. Site deployment with DS datastore service

## Realms

The previous sections present the logical and physical topologies of an example highly available AM deployment, including the clustering of servers using *sites*. One important configuration feature of AM is its ability to run multiple client entities to secure and manage applications through a single AM instance.

AM supports its multiple clients through its use of *realms*. You configure realms within AM to handle different sets of users to whom you can set up different configuration options, storage requirements, delegated administrators, and customization options per realm.

Typically, you can configure realms for customers, partners, or employees within your AM instance, for different departments, or for subsidiaries. In such cases, you create a global administrator who can delegate privileges to realm administrators, each specifically responsible for managing their respective realms.

---

---
title: Getting started for architects and deployers
description: Begin your PingAM deployment by learning product capabilities, setting up a demo or pilot, attending training, determining service levels, and planning your topology, sizing, and deployment objectives
component: pingam
version: 8.1
page_id: pingam:deployment-planning:deploy-highlevel-start
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/deploy-highlevel-start.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "sla", "training", "security"]
page_aliases: ["deployment-planning-guide:deploy-highlevel-start.adoc"]
---

# Getting started for architects and deployers

* **Learn about AM**. You can access online information, meet with your Ping Identity Sales representative, go to a seminar, or call Ping Identity about AM's capabilities.

  The following are some general initial tasks you might want to resolve:

  **Initial questions**

  | Initial tasks                                                        | Done ? |   |
  | -------------------------------------------------------------------- | ------ | - |
  | Understand the access management problems that AM helps to solve     | Y      | N |
  | Learn how to protect a website with AM                               | Y      | N |
  | Get to know the AM software deliverables                             | Y      | N |
  | Get to know the tools for administering AM                           | Y      | N |
  | Get to know the APIs for AM client applications                      | Y      | N |
  | Find out how to get help and support from Ping Identity and partners | Y      | N |
  | Find out how to get training from Ping Identity and partners         | Y      | N |
  | Find out how to keep up to date on new development and new releases  | Y      | N |
  | Find out how to report problems                                      | Y      | N |

* **Set up a demo or pilot**. View an AM demo or set up a pilot to determine how you want to use AM to protect your site(s). Ping Identity Sales representatives can assist you with a demo or pilot.

* **Attend a training class**. Ping Identity presents effective training classes to deploy AM in your environment. Learn more at [Ping Identity Training](https://www.pingidentity.com/en/support/customer-care.html#training).

* **Become a certified professional**. Complete the product-specific Certified Professional exams to gain in-depth design and deployment expertise or find a partner to help you from the [Ping Identity Partner Directory](https://support.pingidentity.com/s/partner-directory-home-page).

* **Determine your service level agreements**. Ping Identity provides different [Customer Care](https://www.pingidentity.com/en/support/customer-care.html) packages you can sign up for.

* **Determine your services**. Ping Identity provides a complete Identity Management stack to meet your requirements.

  **Services**

  | Services task                                                                                                                                                                                                 | Done ? |   |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | - |
  | Understand the services AM software provides                                                                                                                                                                  | Y      | N |
  | Determine which services to deploy                                                                                                                                                                            | Y      | N |
  | Determine which services the deployment consumes (load balancing, application container, authentication services, configuration storage, profile storage, token/session storage, policy storage, log storage) | Y      | N |
  | Determine which services the deployment provides (SSO, CDSSO, SAML Federation IdP/SP, XACML PDP, STS, OAuth 2.0/OpenID Connect 1.0, and so on)                                                                | Y      | N |
  | Determine which resources AM protects (who consumes AM services)                                                                                                                                              | Y      | N |

* **Determine your deployment objectives**. AM provides proven performance and security in many production deployments. You should determine your overall deployment objectives.

  **Deployment Objectives**

  | Deployment objectives                                                                                                                                                                                                                   | Done ? |   |
  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | - |
  | Define deployment objectives in terms of service levels (expectations for authentication rates, active sessions maintained, session life cycles, policies managed, authorization decision rates, response times, throughput, and so on) | Y      | N |
  | Define deployment objectives in terms of service availability (AM service availability, authentication availability, authorization decision availability, session availability, elasticity)                                             | Y      | N |
  | Understand how AM services scale for high availability                                                                                                                                                                                  | Y      | N |
  | Understand the restrictions in an AM deployment that uses client-side sessions                                                                                                                                                          | Y      | N |
  | Plan for availability (number of sites and servers, load balancing and AM software configuration)                                                                                                                                       | Y      | N |
  | Define the domains managed and domains involved in the deployment                                                                                                                                                                       | Y      | N |
  | Define deployment objectives for delegated administration                                                                                                                                                                               | Y      | N |
  | Agree with partners for federated deployments on circles of trust and terms                                                                                                                                                             | Y      | N |

* **Plan sizing**. At this stage, you should determine the sizing estimates for your deployment. Ping Identity Sales Engineers can assist you in this task.

  **Sizing**

  | Sizing                                                                                                   | Done ? |   |
  | -------------------------------------------------------------------------------------------------------- | ------ | - |
  | Derive sizing estimates from service levels and availability                                             | Y      | N |
  | Understand how to test sizing estimates (load generation tools?)                                         | Y      | N |
  | Size servers for AM deployment: CPU                                                                      | Y      | N |
  | Size servers for AM deployment: Memory                                                                   | Y      | N |
  | Size servers for AM deployment: Network                                                                  | Y      | N |
  | Size servers for AM deployment: I/O                                                                      | Y      | N |
  | Size servers for AM deployment: Storage                                                                  | Y      | N |
  | Quantify the impact on external services consumed (LDAP, other auth services, load balancing, and so on) | Y      | N |
  | Plan testing and acceptance criteria for sizing                                                          | Y      | N |

* **Plan the topology**. Plan your logical and physical deployment.

  **Topology Planning**

  | Topology                                                                                                                                                                                                                                                                                                                                              | Done ? |   |
  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | - |
  | Specify the logical and physical deployment topology (show examples of each)                                                                                                                                                                                                                                                                          | Y      | N |
  | Determine how many datastores you need (configuration, CTS, application, policy, UMA…​)                                                                                                                                                                                                                                                               | Y      | N |
  | Plan installation of AM services (including external dependencies)                                                                                                                                                                                                                                                                                    | Y      | N |
  | Plan installation of AM web and Java agents, Fedlets, and PingGateway (might be done by partner service providers)                                                                                                                                                                                                                                    | Y      | N |
  | Plan integration with client applications                                                                                                                                                                                                                                                                                                             | Y      | N |
  | Plan customization of AM (UI, user profile attributes, authentication nodes, identity stores, OAuth 2.0 scope handling, OAuth 2.0 response types, post-authentication actions, policy evaluation, session quota exhaustion actions, policy evaluation, identity data storage, AM service, custom logger, custom policy enforcement points or agents). | Y      | N |

* **Plan security**. At this stage, you must plan how to secure your deployment.

  **Security**

  | Security                                                                                                                     | Done ? |   |
  | ---------------------------------------------------------------------------------------------------------------------------- | ------ | - |
  | Understand security guidelines, including legal requirements                                                                 | Y      | N |
  | Change default settings and administrative user credentials                                                                  | Y      | N |
  | Protect service ports (Firewall, Dist Auth UI, reverse proxy)                                                                | Y      | N |
  | Turn off unused service endpoints                                                                                            | Y      | N |
  | Separate administrative access from client access                                                                            | Y      | N |
  | Secure communications (HTTPS, LDAPS, secure cookies, cookie hijacking protection, key management for signing and encryption) | Y      | N |
  | Determine if components handle SSL acceleration or termination                                                               | Y      | N |
  | Securing processes and files (e.g. with SELinux, dedicated non-privileged user and port forwarding, and so forth)            | Y      | N |

* **Post-deployment tasks**. At this stage, you should plan your post-deployment tasks to sustain and monitor your system.

  **Post-deployment Tasks**

  | Post deployment tasks                                                                                | Done ? |   |
  | ---------------------------------------------------------------------------------------------------- | ------ | - |
  | Plan administration following AM deployment (services, agents/PingGateway, delegated administration) | Y      | N |
  | Plan monitoring following deployment                                                                 | Y      | N |
  | Plan how to expand the deployment                                                                    | Y      | N |
  | Plan how to upgrade the deployment                                                                   | Y      | N |

---

---
title: History
description: "Review the evolution of PingAM from its origins as Sun's iPlanet Directory Server through its acquisition by Ping Identity, including key milestones and version releases"
component: pingam
version: 8.1
page_id: pingam:deployment-planning:openam-history
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/openam-history.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["ciam"]
page_aliases: ["deployment-planning-guide:openam-history.adoc"]
---

# History

AM's timeline is summarized as follows:

* In 2001, Sun Microsystems releases iPlanet Directory Server, Access Management Edition.

* In 2003, Sun renames iPlanet Directory Server, Access Management Edition to Sun ONE Identity Server.

* Later in 2003, Sun acquires Waveset.

* In 2004, Sun releases Sun Java Enterprise System. Waveset Lighthouse is renamed to Sun Java System Identity Manager and Sun ONE Identity Server is renamed to Sun Java System Access Manager. Both products are included as components of Sun Java Enterprise System.

* In 2005, Sun announces an open-source project, OpenSSO, based on Sun Java System Access Manager.

* In 2008, Sun releases OpenSSO build 6, a community open-source version, and OpenSSO Enterprise 8.0, a commercial enterprise version.

* In 2009, Sun releases OpenSSO build 7 and 8.

* In January 2010, Sun was acquired by Oracle and development for the OpenSSO products were suspended as Oracle no longer planned to support the product.

In February 2010, a small group of former Sun employees founded ForgeRock to continue OpenSSO support, which was renamed to OpenAM, and later renamed to Access Management. ForgeRock continued development with the following releases:

* 2010: OpenAM 9.0

* 2011: OpenAM 9.5

* 2012: OpenAM 10 and 10.1

* 2013: OpenAM 11.0

* 2014: OpenAM 11.1, 12.0, and 12.0.1

* 2015: OpenAM 11.0.3 and 12.0.2

* 2016: OpenAM 12.0.3, 12.0.4, 13.0.0, and 13.5.0

* 2017: Access Management 5 and 5.5

* 2018: Access Management 6 and 6.5

* 2020: Access Management 7

* 2021: Access Management 7.1

* 2022: Access Management 7.2

* 2023: Access Management 7.3 and 7.4

ForgeRock became part of Ping Identity in 2023. Ping Identity continues to develop, enhance, and support the industry-leading AM product to meet the changing and growing demands of the market with the following releases:

* 2024: PingAM 7.5

* 2025: PingAM 8

For a full list of all AM releases, refer to the [Release timeline](https://docs.pingidentity.com/pingam/release-notes/timeline.html).

---

---
title: Identity and Access Management
description: Learn how Identity and Access Management secures identity data across cloud, mobile, and enterprise environments with automated provisioning and access control
component: pingam
version: 8.1
page_id: pingam:deployment-planning:understanding-iam
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/understanding-iam.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["ciam"]
page_aliases: ["deployment-planning-guide:understanding-iam.adoc"]
---

# Identity and Access Management

The proliferation of cloud-based technologies, mobile devices, social networks, Big Data, enterprise applications, and business-to-business (B2B) services has spurred the exponential growth of identity information, which is often stored in varied and widely-distributed identity environments.

The challenges of securing such identity data and the environments that depend on the identity data are daunting. Organizations that expand their services through internal development or acquisitions must manage identities across a wide spectrum of identity infrastructures. This expansion requires a careful integration of disparate access management systems, platform-dependent architectures with limited scalability, and ad-hoc security components.

Ping Identity, a leader in the Identity and Access Management (IAM) market, provides proven solutions to securing your identity data.

Identity Management (IDM) is the automated provisioning, updating, and de-provisioning of identities over their lifecycles.

Access Management (AM) is the authentication and authorization of identities who desire privileged access to an organization's resources. AM encompasses the central auditing of operations performed on the system by customers, employees, and partners. AM) also provides the means to share identity data across different access management systems, legacy implementations, and networks.

Continue reading to learn more about AM and what it can do for your environment.

---

---
title: Key benefits
description: PingAM provides secure, low-friction access to resources with transparent security, enabling new revenue streams, reducing operational complexity, improving user experience, and centralizing...
component: pingam
version: 8.1
page_id: pingam:deployment-planning:key-benefits
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/key-benefits.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "security"]
page_aliases: ["deployment-planning-guide:key-benefits.adoc"]
---

# Key benefits

The goal of AM is to provide secure, low friction access to valued resources while presenting the user with a consistent experience. AM provides excellent security, which is totally transparent to the user.

AM provides the following key benefits to your organization:

* **Enables solutions for additional revenue streams**. AM provides the tools and components to quickly deploy services to meet customer demand. For example, AM's Federation Services supports quick and easy deployment with existing SAML 2.0, OAuth2, and OpenID Connect systems. For systems that do not support a full SAMLv2 deployment, AM provides a *Fedlet*, a small SAML 2.0 application, which lets service providers quickly add SAML 2.0 support to their Java applications. These solutions open up new possibilities for additional revenue streams.

* **Reduces operational cost and complexity**. AM can function as a hub, leveraging existing identity infrastructures and providing multiple integration paths using its authentication, SSO, and policies to your applications without the complexity of sharing Web access tools and passwords for data exchange. AM decreases the total cost of ownership (TCO) through its operational efficiencies, rapid time-to-market, and high scalability to meet the demands of our market.

* **Improves user experience**. AM enables users to experience more services using SSO without the need of multiple passwords.

* **Easier configuration and management**. AM centralizes the configuration and management of your access management system, allowing easier administration through its console and command-line tools. AM also features a flexible deployment architecture that unifies services through its modular and embeddable components. AM provides a common REST framework and common user interface (UI) model, providing scalable solutions as your customer base increases to the hundreds of millions. AM also allows enterprises to outsource IAM services to system integrators and partners.

* **Increased compliance**. AM provides an extensive entitlements service, featuring attribute-based access control (ABAC) policies as its main policy framework with features like import/export support to XACML, a policy editor, and REST endpoints for policy management. AM also includes an extensive auditing service to monitor access according to regulatory compliance standards.

---

---
title: More than just single sign-on
description: PingAM provides authentication, authorization, federation, and adaptive risk services as part of the Ping Identity platform
component: pingam
version: 8.1
page_id: pingam:deployment-planning:not-just-sso
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/not-just-sso.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning"]
page_aliases: ["deployment-planning-guide:not-just-sso.adoc"]
---

# More than just single sign-on

PingAM (AM) is an all-in-one, centralized access management solution, securing protected resources across the network and providing authentication, authorization, web security, and federation services in a single, integrated solution.

AM is deployed as a simple `.war` file and provides production-proven platform independence, flexible and extensible components, as well as a high availability and a highly scalable infrastructure. Using open standards, AM is fully extensible, and can expand its capabilities through its SDKs and numerous REST endpoints.

AM is part of the Ping Advanced Identity Software, and provides identity and access management of mobile-ready, cloud, enterprise, social, and partner services. The Ping Advanced Identity Software provides global consumer services across any platform for any connected device or any Internet-connected entity.

The Ping Advanced Identity Software features the following products:

* **PingAM**. Context-based access management system. PingAM is an all-in-one industry-leading access management solution, providing authentication, authorization, federation, Web services security, adaptive risk, and entitlements services among many other features. AM is deployed as a simple `.war` file, featuring an architecture that is platform independent, flexible, and extensible, and highly available and scalable.

* **PingIDM**. Cloud-focused identity administration. PingIDM is a lightweight provisioning system, built on resource-oriented principles. IDM is a self-contained system, providing workflow, compliance, synchronization, password management, and connectors. IDM features a next-generation modular architecture that is self-contained and highly extensible.

* **PingDS**. Internet scale directory server. PingDS provides full LDAP protocol support, multi-protocol access, cross-domain replication, common REST framework, SCIM support, and many other features.

* **PingGateway**. No touch single sign-on (SSO) to enterprise, legacy, and custom applications. PingGateway is a reverse proxy server with specialized session management and credential replay functionality. PingGateway works with AM to integrate Web applications without needing to modify the target application, or the container that it runs in.

* **OpenICF**. Enterprise and cloud identity infrastructure connectors. OpenICF provides identity provisioning connections offering a consistent layer between target resources and applications and exposing a set of programming functions for the full lifecycle of an identity. OpenICF connectors are compatible with OpenIDM, Sun Identity Manager, Oracle™ Waveset, Brinqa™ GRC Platform, and so on.

The following figure illustrates these components:

![The Ping Advanced Identity Software features a modular and flexible architecture.](_images/forgerock-identity-platform.svg)Figure 1. Ping Advanced Identity Software

---

---
title: Plan the deployment architecture
description: Plan your PingAM deployment architecture by defining goals, scope, roles, and responsibilities while considering user capacity, high availability, security requirements, and scaling needs
component: pingam
version: 8.1
page_id: pingam:deployment-planning:planning-architecture-onprem
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/planning-architecture-onprem.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "architecture", "availability", "performance", "security", "training", "upgrade"]
page_aliases: ["deployment-planning-guide:planning-architecture-onprem.adoc"]
section_ids:
  deployment-considerations: Deployment planning considerations
  deployment-steps: Deployment planning steps
  prepare-deployment-plans: Prepare deployment plans
  plan-training: Plan training
  plan-customization: Plan customization
  plan-pilot: Plan a pilot implementation
  plan-security: Plan security hardening
  plan-with-providers: Plan with providers
  plan-integration-with-apps: Plan integration with client applications
  plan-integration-with-audit: Plan integration with audit tools
  plan-tests: Plan tests
  plan-documentation: Plan documentation and tracking changes
  plan-maintenance: Plan maintenance and support in production
  plan-rollout: Plan rollout into production
  plan-growth: Plan for growth
  plan-upgrades: Plan for upgrades
  plan-disaster-recovery: Plan for disaster recovery
---

# Plan the deployment architecture

Deployment planning is critical to ensuring your AM system is properly implemented within the time frame determined by your requirements. The more thoroughly you plan your deployment, the more solid your configuration will be, and you will meet timelines and milestones while staying within budget.

A deployment plan defines the goals, scope, roles, and responsibilities of key stakeholders, architecture, implementation, and testing of your AM deployment. A good plan ensures that a smooth transition to a new product or service is configured and all possible contingencies are addressed to quickly troubleshoot and solve any issue that may occur during the deployment process. The deployment plan also defines a training schedule for your employees, procedural maintenance plans, and a service plan to support your AM system.

## Deployment planning considerations

When planning a deployment, you must consider some important questions regarding your system:

> **Collapse: What are you protecting?**
>
> You must determine which applications, resources, and levels of access to protect? Are there plans for additional services, either developed in-house or through future acquisitions that also require protected access?

> **Collapse: How many users are supported?**
>
> It is important to determine the number of users supported in your deployment based on system usage. Once you have determined the number of users, it is important to project future growth.

> **Collapse: What are your product service-level agreements?**
>
> In addition to planning for the growth of your user base, it is important to determine the production service-level agreements (SLAs) that help determine the current load requirements on your system and for future loads. The SLAs help define your scaling and high-availability requirements.
>
> For example, suppose you have 100,000 active users today, and each user has an average of two devices (laptop, phone) that each get a session every day. Suppose that you also have 20 protected applications, with each device hitting an average of seven protected resources an average of 1.4 times daily. Let's say that works out to about 200,000 sessions per day with 7 x 1.4 = \~10 updates to each session object. This can result in 200K session creations, 200K session deletions, and 2M session updates.
>
> Now, imagine next year you still have the same number of active users, 100K, but each has an average of three devices (laptop, phone, tablet), and you have added another 20 protected applications. Assume the same average usage per application per device, or even a little less per device. You can see that although the number of users is unchanged, the whole system needs to scale up considerably.
>
> You can scale your deployment using vertical or horizontal scaling. Vertical scaling involves increasing components to a single host server, such as increasing the number of CPUs or increasing heap memory to accommodate a larger session cache or more policies. Horizontal scaling involves adding additional host servers, possibly behind a load balancer, so that the servers can function as a single unit.

> **Collapse: What are your high availability requirements?**
>
> High availability refers to your system's ability to operate continuously for a specified length of time. It is important to design your system to prevent single points of failure and for continuous availability. Based on the size of your deployment, you can create an architecture using a single-site configuration. For larger deployments, consider implementing a multi-site configuration with replication.

> **Collapse: Which type of clients will be supported?**
>
> The type of client determines the components required for the deployment. For example, applications deployed on a web server require a web agent. Applications deployed in Java containers require a Java agent. An AJAX application can use AM's RESTful API. Legacy or custom applications can use the PingGateway. Applications in an unsupported application server can use a reverse proxy with a web or Java agent. Third party applications can use federation or a fedlet, or an OpenID Connect or an OAuth 2.0 component.

> **Collapse: What are your SSL/TLS requirements?**
>
> There are two common approaches to handling SSL. First, using SSL through to the application servers themselves, for example, using SSL on the containers. Or second, using SSL offloading via a network device and running HTTP clear internally. You must determine the appropriate approach as each method requires different configurations. Determining SSL use early in the planning process is vitally *important*, as adding SSL later in the process is more complicated and could result in delays in your deployment.

> **Collapse: What are your other security requirements?**
>
> The use of firewalls provides an additional layer of security for your deployment. If you are planning to deploy the AM server behind a firewall, you can deploy a reverse proxy, such as PingGateway. For another level of security, consider using multiple DNS infrastructures using zones; one zone for internal clients, another zone for external clients. To provide additional performance, you can deploy the DNS zones behind a load balancer.

*Ensure all stakeholders are engaged during the planning phase*. This effort includes but is not limited to delivery resources, such as project managers, architects, designers, implementers, testers, and service resources, such as service managers, production transition managers, security, support, and sustaining personnel. Input from all stakeholders ensures all viewpoints are considered at project inception, rather than downstream, when it may be too late.

## Deployment planning steps

The general deployment planning steps can be summarized as follows:

* Project initiation

  The project initiation phase begins by defining the overall scope and requirements of the deployment.

  > **Collapse: Items to plan**
  >
  > * Determine the scope, roles and responsibilities of key stakeholders and resources required for the deployment.
  >
  > * Determine critical path planning including any dependencies and their assigned expectations.
  >
  > * Run a pilot to test the functionality and features of AM and uncover any possible issues early in the process.
  >
  > * Determine training for administrators of the environment and training for developers, if needed.

* Architecting

  The architecting phase involves designing the deployment.

  > **Collapse: Items to plan**
  >
  > * Determine the use of products, map requirements to features, and ensure the architecture meets the functional requirements.
  >
  > * Ensure that the architecture is designed for ease of management and scale. TCO is directly proportional to the complexity of the deployment.
  >
  > * Determine how the Identity, Configuration, and Core Token Service (CTS) datastores are to be configured.
  >
  > * Determine the sites configuration.
  >
  > * Determine where SSL is used in the configuration and how to maintain and update the certificate keystore and truststore for AM's components, such as the agent installer, agent server, and other AM servers. Planning for SSL at this point can avoid more difficulty later in the process.
  >
  > * Determine if AM will be deployed behind a load balancer with SSL offloading. If this is the case, you must ensure that the load balancer rewrites the protocol during redirection. If you have a web or Java agent behind a load balancer with SSL offloading, ensure that you set the web or Java agent's override request URL properties.
  >
  > * For multiple AM deployments, there is a requirement to deploy a layer 7 cookie-based load balancer and intelligent keep-alives (for example, `/am/isAlive.jsp`). The network teams should design the appropriate solution in the architecting phase.
  >
  > * Determine requirements for vertical scaling, which involves increasing the Java heap based on anticipated session cache, policy cache, federation session, and restricted token usage. Note that vertical scaling could come with performance cost, so this must be planned accordingly.
  >
  > * Determine requirements for horizontal scaling, which involves adding additional AM servers and load balancers for scalability and availability purposes.
  >
  > * Determine whether to configure AM to store journey sessions in the CTS token store, on the client, or in AM's memory:
  >
  >   * Client-side journey sessions provide authentication high availability and are easier to deploy in global authentication environments, but the journey session is held by the client.
  >
  >   * Server-side journey sessions provide high availability and keep the journey session in your environment, but require consistent and fast replication across the CTS token store deployment.
  >
  >   * In-memory journey sessions don't provide authentication high availability, but keep journey sessions in your environment.
  >
  > * Determine whether to configure AM to store authenticated sessions in the CTS token store or on the client. Client-side authenticated sessions allow for easier horizontal scaling but don't provide equivalent functionality to server-side authenticated sessions.
  >
  > * Determine if any coding is required including extensions and plugins. Unless it is absolutely necessary, leverage the product features instead of implementing custom code. AM provides numerous plugin points and REST endpoints.

* Implementation

  The implementation phase involves deploying your AM system.

  > **Collapse: Items to consider**
  >
  > * Install and configure the AM server, datastores, and components. For information on installing AM, see [Installation](../installation/preface.html).
  >
  > * Maintain a record and history of the deployment to maintain consistency across the project.
  >
  > * Tune AM's JVM, caches, LDAP connection pools, container thread pools, and other items. For information on tuning AM, see [Tune AM](../maintenance/tuning-am.html).
  >
  > * Tune the DS server. Consider tuning the database back end, replication purge delays, garbage collection, JVM memory, and disk space considerations. For more information, see the DS server documentation.
  >
  > * Consider implementing separate file systems for both AM and DS, so that you can keep log files on a different disk, separate from data or operational files, to prevent device contention should the log files fill up the file system.

* Automation and continuous integration

  The Automation and Continuous Integration phase involves using tools for testing:

  * Set up a continuous integration server, such as Jenkins, to ensure that builds are consistent by running unit tests and publishing Maven artifacts. Perform continuous integration unless your deployment includes no customization.

  * Ensure your custom code has unit tests to ensure nothing is broken.

* Functional testing

  The Functional Testing phase should test all functionality to deliver the solution without any failures. You must ensure that your customizations and configurations are covered in the test plan.

* Non-functional testing

  The Non-Functional Testing phase tests failover and disaster recovery procedures. Run load testing to determine the demand of the system and measure its responses. You can anticipate peak load conditions during the phase.

* Supportability

  The supportability phase involves creating the runbook for system administrators including procedures for backup and restore, debugging, change control, and other processes. If you have a Ping Identity Support contract, it ensures everything is in place prior to your deployment.

## Prepare deployment plans

When you create a good concrete deployment plan, it ensures that a change request process is in place and utilized, which is essential for a successful deployment. This section looks at planning the full deployment process. When you have addressed everything in this section, then you should have a concrete plan for deployment.

### Plan training

Training provides common understanding, vocabulary, and basic skills for those working together on the project. Depending on previous experience with access management and with AM, both internal teams and project partners might need training.

> **Collapse: What types of training do team members need?**
>
> * All team members should take at least some training that provides an overview of AM. This helps to ensure a common understanding and vocabulary for those working on the project.
>
> * Team members planning the deployment should take an AM deployment training before finalizing your plans, and ideally before starting to plan your deployment.
>
>   AM not only offers a broad set of features with many choices, but the access management it provides tends to be business critical. AM deployment training pays for itself as it helps you to make the right initial choices to deploy more quickly and successfully.
>
> * Team members involved in designing and developing AM client applications or custom extensions should take training in AM development in order to help them make the right choices. This includes developers customizing the AM UI for your organization.
>
> * Team members who have already had been trained in the past might need to refresh their knowledge if your project deploys newer or significantly changed features, or if they have not worked with AM for some time.

Ping Identity regularly offers training courses for AM topics, including AM development and deployment. You can find a current list of available courses on [Ping Identity Training](https://training.pingidentity.com/).

When you have determined who needs training and the timing of the training during the project, prepare a training schedule based on team member and course availability. Include the scheduled training plans in your deployment project plan.

Ping Identity also offers product-specific Certified Professional exams to gain in-depth design and deployment expertise.

### Plan customization

When you customize AM, you can improve how the software fits your organization. AM customizations can also add complexity to your system as you increase your test load and potentially change components that could affect future upgrades. Therefore, a best practice is to deploy AM with a minimum of customizations.

Most deployments require at least some customization, like skinning end user interfaces for your organization, rather than using the AM defaults. If your deployment is expected to include additional client applications, or custom extensions (authentication nodes, policy conditions, and so on), then have a team member involved in the development help you plan the work. [REST API](../am-rest/preface.html) can be useful when scoping a development project.

Although some customizations involve little development work, it can require additional scheduling and coordination with others in your organization. An example is adding support for profile attributes in the identity store.

The more you customize, the more important it is to test your deployment thoroughly before going into production. Consider each customization as sub-project with its own acceptance criteria, and consider plans for unit testing, automation, and continuous integration. See [Planning Tests](#plan-tests) for details.

When you have prepared plans for each customization sub-project, you must account for those plans in your overall deployment project plan. Functional customizations, such as custom authentication nodes or policy conditions might need to reach the pilot stage before you can finish an overall pilot implementation.

### Plan a pilot implementation

Unless you are planning a maintenance upgrade, consider starting with a pilot implementation, which is a long term project that is aligned with customer-specific requirements.

A pilot shows that you can achieve your goals with AM plus whatever customizations and companion software you expect to use. The idea is to demonstrate feasibility by focusing on solving key use cases with minimal expense, but without ignoring real-world constraints. The aim is to fail fast before you have too much invested so that you can resolve any issues that threaten the deployment.

Do not expect the pilot to become the first version of your deployment. Instead, build the pilot as something you can afford to change easily, and to throw away and start over if necessary.

The cost of a pilot should remain low compared to overall project cost. Unless your concern is primarily the scalability of your deployment, you run the pilot on a much smaller scale than the full deployment. Scale back on anything not necessary to validating a key use case.

Smaller scale does not necessarily mean a single-server deployment, though. If you expect your deployment to be highly available, for example, one of your key use cases should be continued smooth operation when part of your deployment becomes unavailable.

The pilot is a chance to try and test features and services before finalizing your plans for deployment. The pilot should come early in your deployment plan, leaving appropriate time to adapt your plans based on the pilot results. Before you can schedule the pilot, team members might need training and you might require prototype versions of functional customizations.

Plan the pilot around the key use cases that you must validate. Make sure to plan the pilot review with stakeholders. You might need to iteratively review pilot results as some stakeholders refine their key use cases based on observations.

### Plan security hardening

When you first configure AM, there are many options to evaluate, plus a number of ways to further increase levels of security. You must, therefore, plan to secure the deployment as described in [Security](../security/preface.html).

### Plan with providers

AM delegates authentication and profile storage to other services. AM can store configuration, policies, session, and other tokens in an external directory service. AM can also participate in a circle of trust with other SAML entities. In each of these cases, a successful deployment depends on coordination with service providers, potentially outside of your organization.

The infrastructure you need to run AM services might be managed outside your own organization. Hardware, operating systems, network, and software installation might be the responsibility of providers with which you must coordinate.

When working with providers, take the following points into consideration:

* Shared authentication and profile services might have been sized prior to or independently from your access management deployment.

  An overall outcome of your access management deployment might be to decrease the load on shared authentication services (and replace some authentication load with single-sign on that is managed by AM), or it might be to increase the load (if, for example, your deployment enables many new applications or devices, or enables controlled access to resources that were previously unavailable).

  identity stores are typically backed by shared directory services. Directory services might need to provision additional attributes for AM. This could affect not only directory schema and access for AM, but also sizing for the directory services that your deployment uses.

* If your deployment uses an external directory service for AM configuration data and AM policies, then the directory administrator must include attributes in the schema and provide access rights to AM. The number of policies depends on the deployment. For deployments with thousands or millions of policies to store, AM's use of the directory could affect sizing.

* If your deployment uses an external directory service as a backing store for the AM Core Token Service (CTS), then the directory administrator must include attributes in the schema and provide access rights to AM.

  CTS load tends to involve more write operations than configuration and policy load, as CTS data tend to be more volatile, especially if most tokens concern short-lived sessions. This can affect directory service sizing.

  CTS enables cross-site session high availability by allowing a remote AM server to retrieve an authenticated session from the directory service backing the CTS. For this feature to work quickly in the event of a failure or network partition, CTS data must be replicated rapidly, including across WAN links. This can affect network sizing for the directory service.

  When configured to store authenticated sessions in the client, AM doesn't write the authenticated sessions to the CTS token store. Instead, AM uses the CTS token store for session denylists. Session denylisting is an optional AM feature that provides logout integrity.

* SAML federation circles of trust require organizational and legal coordination before you can determine what the configuration looks like. Organizations must agree on which security data they share and how, and you must be involved to ensure that their expectations map to the security data that is actually available.

  There also needs to be coordination between all SAML parties, (that is, agreed-upon SLAs, patch windows, points of contact and escalation paths). Often, the technical implementation is considered, but not the *business requirements*. For example, a common scenario occurs when a service provider takes down their service for patching without informing the identity provider or vice-versa.

* When working with infrastructure providers, realize that you are likely to have better sizing estimates after you have tried a test deployment under load. Even though you can expect to revise your estimates, take into account the lead time necessary to provide infrastructure services.

  Estimate your infrastructure needs not only for the final deployment, but also for the development, pilot, and testing stages.

For each provider you work with, add the necessary coordinated activities to your overall plan, as well as periodic checks to make sure that parallel work is proceeding according to plan.

### Plan integration with client applications

When planning integration with AM client applications, the applications that are most relevant are those that register with AM; therefore, you should make note of the following types of client applications registering with AM:

> **Collapse: AM web and Java Agents Reside with the Applications They Protect**
>
> By default, web and Java agents store their configuration profiles in AM's configuration store. If notifications are enabled, AM sends web and Java agents notifications about configuration changes.
>
> To delegate administration of multiple web or Java agents, AM lets you create a group profile for each realm to register the agent profiles.
>
> While the AM administrator manages web or Java agent configuration, application administrators are often the ones who install the agents. You must coordinate installation and upgrades with them.

> **Collapse: OAuth 2.0/OpenID Connect 1.0 clients register profiles with AM**
>
> AM optionally allows registration of such applications without prior authentication. By default, however, registration requires an access token granted to an OAuth 2.0 client with access to register profiles.
>
> If you expect to allow dynamic registration, or if you have many clients registering with your deployment, then consider clearly documenting how to register the clients, and building a client to register clients.

> **Collapse: Configure circles of trust for SAML 2.0 federation**
>
> Registration happens at configuration time, rather than at runtime.
>
> Address the necessary configuration as described in [Plan with providers](#plan-with-providers).
>
> If your deployment functions as a SAML 2.0 Identity Provider (IDP) and shares Fedlets with Service Providers (SP), the SP administrators must install the Fedlets, and must update their Fedlets for changes in your IDP configuration. Consider at least clearly documenting how to do so, and if necessary, build installation and upgrade capabilities.

* If you have custom client applications, consider how they are configured and how they must register with AM.

* REST API client applications authenticate based on a user profile.

  REST client applications can therefore authenticate using whatever authentication mechanisms you configure in AM, and therefore do not require additional registration.

For each client application whose integration with AM requires coordination, add the relevant tasks to your overall plan.

### Plan integration with audit tools

AM and the web or Java agents can log audit information to different formats, such as flat files and relational databases. Log volumes depend on usage and on logging levels. By default, AM generates both access and error messages for each service, providing the raw material for auditing the deployment. For more information about supported audit log formats and the information logged, see [Audit logging](../monitoring/audit-logging.html) and [Reference](../am-reference/preface.html).

In order to analyze the raw material, however, you must use other software, such as [Splunk](https://www.splunk.com/), which indexes machine-generated data for analysis.

If you require integration with an audit tool, plan the tasks of setting up logging to work with the tool, and analyzing and monitoring the data once it has been indexed. Consider how you must retain and rotate log data once it has been consumed, as a high volume service can produce large volumes of log data.

Include these plans in the overall plan.

### Plan tests

In addition to planning tests for each customized component, test the functionality of each service you deploy, such as authentication, policy decisions, and federation. You should also perform non-functional testing to validate that the services hold up under load in realistic conditions. Perform penetration testing to check for security issues. Include acceptance tests for the actual deployment. The data from the acceptance tests help you to make an informed decision about whether to go ahead with the deployment or to roll back.

> **Collapse: Plan functional testing**
>
> Functional testing validates that specified test cases work with the software considered as a black box.
>
> Because Ping Identity already tests AM and the web and Java agents functionally, focus your functional testing on customizations and service-level functions. For each key service, devise automated functional tests. Automated tests make it easier to integrate new deliveries to take advantage of recent bug fixes and to check that fixes and new features do not cause regressions.
>
> Tools for running functional testing include [Apache JMeter](https://jmeter.apache.org/) and [Selenium](https://www.selenium.dev/). Apache JMeter is a load testing tool for Web applications. Selenium is a test framework for Web applications, particularly for UIs.
>
> As part of the overall plan, include not only tasks to develop and maintain your functional tests, but also to provision and to maintain a test environment in which you run the functional tests before you significantly change anything in your deployment. For example, run functional tests whenever you upgrade AM, AM web and Java agents, or any custom components, and analyze the output to understand the effect on your deployment.

> **Collapse: Plan service performance testing**
>
> For written service-level agreements and objectives, even if your first version consists of guesses, you turn performance plans from an open-ended project to a clear set of measurable goals for a manageable project with a definite outcome. Therefore, start your testing with clear definitions of success.
>
> Also, start your testing with a system for load generation that can reproduce the traffic you expect in production, and provider services that behave as you expect in production. To run your tests, you must therefore generate representative load data and test clients based on what you expect in production. You can then use the load generation system to perform iterative performance testing.
>
> Iterative performance testing consists in identifying underperformance and the bottlenecks that cause it, and discovering ways to eliminate or work around those bottlenecks. Underperformance means that the system under load does not meet service level objectives. Sometimes re-sizing and/or tuning the system or provider services can help remove bottlenecks that cause underperformance.
>
> Based on service level objectives and availability requirements, define acceptance criteria for performance testing, and iterate until you have eliminated underperformance.
>
> Tools for running performance testing include [Apache JMeter](https://jmeter.apache.org/), for which your loads should mimic what you expect in production, and [Gatling](https://gatling.io/), which records load using a domain specific language for load testing. To mimic the production load, examine both the access patterns and also the data that AM stores. The representative load should reflect the expected random distribution of client access, so that sessions are affected as in production. Consider authentication, authorization, logout, and session timeout events, and the lifecycle you expect to see in production.
>
> Although you cannot use actual production data for testing, you can generate similar test data using tools, such as the DS `makeldif` command, which generates user profile data for directory services. AM REST APIs can help with test provisioning for policies, users, and groups.
>
> As part of the overall plan, include not only tasks to develop and maintain performance tests, but also to provision and to maintain a pre-production test environment that mimics your production environment. Security measures in your test environment must also mimic your production environment, as changes to secure AM as described in [Plan security hardening](#plan-security), such as using HTTPS rather than HTTP, can impact performance.
>
> Once you are satisfied that the baseline performance is acceptable, run performance tests again when something in your deployment changes significantly with respect to performance. For example, if the load or number of clients changes significantly, it could cause the system to underperform. Also, consider the thresholds that you can monitor in the production system to estimate when your system might start to underperform.

> **Collapse: Plan penetration testing**
>
> Penetration testing involves attacking a system to expose security issues before they show up in production.
>
> When planning penetration testing, consider both white box and black box scenarios. Attackers can know something about how AM works internally, and not only how it works from the outside. Also, consider both internal attacks from within your organization, and external attacks from outside your organization.
>
> As for other testing, take time to define acceptance criteria. Know that Ping Identity has performed penetration testing on the software for each enterprise release. Any customization, however, could be the source of security weaknesses, as could configuration to secure AM.
>
> You can also plan to perform penetration tests against the same hardened, pre-production test environment also used for performance testing.

> **Collapse: Plan deployment testing**
>
> Deployment testing is used as a description, and not a term in the context of this guide. It refers to the testing implemented within the deployment window after the system is deployed to the production environment, but before client applications and users access the system.
>
> Plan for minimal changes between the pre-production test environment and the actual production environment. Then test that those changes have not cause any issues, and that the system generally behaves as expected.
>
> Take the time to agree upfront with stakeholders regarding the acceptance criteria for deployment tests. When the production deployment window is small, and you have only a short time to deploy and test the deployment, you must trade off thorough testing for adequate testing. Make sure to plan enough time in the deployment window for performing the necessary tests and checks.
>
> Include preparation for this exercise in your overall plan, as well as time to check the plans close to the deployment date.

### Plan documentation and tracking changes

The AM product documentation is written for readers like you, who are architects and solution developers, as well as for AM developers and for administrators who have had AM training. The people operating your production environment need concrete documentation specific to your deployed solution, with an emphasis on operational policies and procedures.

Procedural documentation can take the form of a runbook with procedures that emphasize maintenance operations, such as backup, restore, monitoring and log maintenance, collecting data pertaining to an issue in production, replacing a broken server or web or Java agent, responding to a monitoring alert, and so forth. Make sure in particular that you document procedures for taking remedial action in the event of a production issue.

Furthermore, to ensure that everyone understands your deployment and to speed problem resolution in the event of an issue, changes in production must be documented and tracked as a matter of course. When you make changes, always prepare to roll back to the previous state if the change does not perform as expected.

Include documentation tasks in your overall plan. Also, include the tasks necessary to put in place and to maintain change control for updates to the configuration.

### Plan maintenance and support in production

If you own the architecture and planning, but others own the service in production, or even in the labs, then you must plan coordination with those who own the service.

Start by considering the service owners' acceptance criteria. If they have defined support readiness acceptance criteria, you can start with their acceptance criteria. You can also ask yourself the following questions:

* What do they require in terms of training in AM?

* What additional training do they require to support your solution?

* Do your plans for documentation and change control, as described in [Plan documentation and tracking changes](#plan-documentation), match their requirements?

* Do they have any additional acceptance criteria for deployment tests, as described in [Plan deployment testing](#plan-deployment-tests)?

Also, plan back line support with Ping Identity or a qualified partner. The aim is to define clearly who handles production issues, and how production issues are escalated to a product specialist if necessary.

Include a task in the overall plan to define the hand off to production, making sure there is clarity on who handles monitoring and issues.

### Plan rollout into production

In addition to planning for the hand off of the production system, also prepare plans to roll out the system into production. Rollout into production calls for a well-choreographed operation, so these are likely the most detailed plans.

Take at least the following items into account when planning the rollout:

* Availability of all infrastructure that AM depends upon the following elements:

  * Server hosts and operating systems

  * Web application containers

  * Network links and configurations

  * Load balancers

  * Reverse proxy services to protect AM

  * Data stores, such as directory services

  * Authentication providers

* Installation for all AM services.

* Installation of AM client applications:

  * Web and Java agents

  * Fedlets

  * SDK applications

  * OAuth 2.0 applications

  * OpenID Connect 1.0 applications

* Final tests and checks.

* Availability of the personnel involved in the rollout.

In your overall plan, leave time and resources to finalize rollout plans toward the end of the project.

### Plan for growth

Before rolling out into production, plan how to monitor the system to know when you must grow, and plan the actions to take when you must add capacity.

Unless your deployment is very constrained, after your successful rollout of access management services, you can expect to add capacity at some point in the future. Therefore, you should plan to monitor system growth.

You can grow many parts of the system by adding servers or adding clients. The parts of the system that you cannot expand so simply are those parts that depend on writing to the directory service.

The directory service eventually replicates each write to all other servers. Therefore, adding servers simply adds the number of writes to perform. One simple way of getting around this limitation is to split a monolithic directory service into several directory services. That said, directory services often are not a bottleneck for growth.

When should you expand the deployed system? The time to expand the deployed system is when growth in usage causes the system to approach performance threshold levels that cause the service to underperform. For that reason, devise thresholds that can be monitored in production, and plan to monitor the deployment with respect to the thresholds. In addition to programming appropriate alerts to react to thresholds, also plan periodic reviews of system performance to uncover anything missing from regular monitoring results.

### Plan for upgrades

In this section, "upgrade" means moving to a more recent release, whether it is a patch, maintenance release, minor release, or major release. You can find the definitions of the release types in [Product release levels](https://docs.pingidentity.com/pingam/release-notes/stability.html#release-levels).

Upgrades generally bring fixes, or new features, or both. For each upgrade, you must build a new plan. Depending on the scope of the upgrade, that plan might include almost all of the original overall plan, or it might be abbreviated, for example, for a patch that fixes a single issue. In any case, adapt deployment plans, as each upgrade is a new deployment.

When planning an upgrade, pay particular attention to testing and to any changes necessary in your customizations. For testing, consider compatibility issues when not all agents and services are upgraded simultaneously. Choreography is particularly important, as upgrades are likely to happen in constrained low usage windows, and as users already have expectations about how the service should behave.

When preparing your overall plan, include a regular review task to determine whether to upgrade, not only for patches or regular maintenance releases, but also to consider whether to upgrade to new minor and major releases.

### Plan for disaster recovery

Disaster recovery planning and a robust backup strategy is essential when server hardware fails, network connections go down, a site fails, and so on. Your team must determine the disaster recovery procedures to recover from such events.

---

---
title: Server overview
description: "Learn about PingAM's modular architecture, centralized access management capabilities, and deployment options for securing resources across cloud, enterprise, and B2B systems"
component: pingam
version: 8.1
page_id: pingam:deployment-planning:am-server-overview
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/am-server-overview.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "architecture"]
page_aliases: ["deployment-planning-guide:am-server-overview.adoc"]
section_ids:
  architecture: Architecture
  get_am: Get AM
  training_and_support: Training and support
---

# Server overview

Use AM to secure your resources and manage user access across your network. As a centralized access management server, AM provides authentication, authorization, web security, and federation services in a single, integrated solution.

With AM, you can:

* Control who has access to your protected resources.

* Define when, how long, and under what conditions users can access resources.

* Centralize access management for your cloud, enterprise, mobile, and business-to-business (B2B) systems.

## Architecture

The modular and flexible architecture of AM includes multiple plugin points, so you can adapt it to your specific deployment needs.

![AM has a highly modular and flexible architecture.](_images/openam-architecture-dpg.svg)Figure 1. Architecture

AM uses industry-standard protocols, such as HTTP, XML, SOAP, REST, SAML 2.0, OAuth 2.0, and OpenID Connect 1.0. All AM services are 100% Java-based and are compatible with multiple platforms and containers.

## Get AM

You can deploy and integrate the AM core server into your existing network infrastructure.

Download AM from the [Ping Identity Download Center](https://backstage.pingidentity.com/downloads). Before you download the files, make sure to review the Software License and Subscription Agreement.

The download includes a `.zip` file with all components, such as the `.war` file, tools, the configurator, and samples.

The distribution provides the following files:

**Distribution Files**

| File                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AM-8.1.1.war`                 | The distribution `.war` file includes the core server code and an administrative graphical user interface (GUI) Web console.During installation, the `.war` file accesses properties to get the fully qualified domain name, port, context path, and the location of the configuration folder. These properties can be retrieved from the `boot.json` file in the AM installation directory, from environment variables, or from a combination of the two.This file is also available to download individually. |
| `AM-crypto-tool-8.1.1.war`     | A utility with some cryptographic functionality used for creating Docker images.	Strictly for future use, not currently supported.                                                                                                                                                                                                                                                                                                                                                                              |
| `Config-Upgrader-8.1.1.zip`    | Configuration file upgrade tool.Find more information on converting configuration files for import into AM in the `README.md` file in the `Config-Upgrader-8.1.1.zip` file.                                                                                                                                                                                                                                                                                                                                     |
| `Fedlet-8.1.1.zip`             | An AM Fedlet, a light-weight SAML 2.0 service provider.The Fedlet lets you set up a federated deployment without the need of a fully-featured service provider.                                                                                                                                                                                                                                                                                                                                                 |
| `IDPDiscovery-8.1.1.war`       | An IdP Discovery Profile (SAMLv2 binding profile) for its IdP Discovery service. The profile keeps track of the identity providers for each user.                                                                                                                                                                                                                                                                                                                                                               |
| `sample-trees-8.1.1.zip`       | Sample authentication trees for demonstration purposes. The trees are provided as JSON files and can be imported into an AM deployment using *Amster*. Find information on importing files using Amster in [Import configuration data](../amster/import-config.html).                                                                                                                                                                                                                                           |
| `Truststore-Utility-8.1.1.zip` | A utility to help with creating a trust store for use with web authentication.Find more information in the `readme.md` in the `.zip` archive and [MFA: Web authentication (WebAuthn) and passkeys](../am-authentication/authn-mfa-webauthn.html).                                                                                                                                                                                                                                                               |

The [Ping Identity Download Center](https://backstage.pingidentity.com/downloads) hosts downloadable versions of AM, including a `.zip` file with all of the AM components, the `.war` file, AM tools, the configurator, web and Java agents, and documentation. Verify that you review the Software License and Subscription Agreement presented before you download AM files.

## Training and support

If you need help deploying AM into production, Ping Identity offers services that include training, consulting, and support.

---

---
title: Size hardware and services for deployment
description: Determine hardware and services sizing for your deployment by evaluating availability requirements, failover strategies, session management, and service-level goals
component: pingam
version: 8.1
page_id: pingam:deployment-planning:deploy-sizing
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/deploy-sizing.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "availability", "storage"]
page_aliases: ["deployment-planning-guide:deploy-sizing.adoc"]
---

# Size hardware and services for deployment

Determine the correct size of your deployment by understanding what is that you need out of it. Availability over anything? Fast response times? Can you find a compromise?

* Size for availability

  Any part of a system that can fail eventually will fail. Keeping your service available means tolerating failure in any part of the system without interrupting the service. You make AM services highly available through good maintenance practices and by removing single points of failure from your architectures.

  Removing single points of failure involves replicating each system component, so that when one component fails, another can take its place. Replicating components comes with costs not only for the deployment and maintenance of more individual components, but also for the synchronization of anything those components share. Due to necessary synchronization between components, what you spend on availability is never fully recovered as gains in capacity. (Two servers cannot do quite twice the work of one server.) Instead, you must determine the right trade-offs for the deployment.

  To start thinking about the trade-offs, answer the following questions.

  > **Collapse: What is the impact of the AM service becoming unavailable?**
  >
  > In an online system, this could be a severe problem, interrupting all access to protected resources. Most deployments fall into this category.
  >
  > In a system protecting local resources, it might be acceptable to restart the service.
  >
  > Deployments that require always-on service availability require some sort of load balancing solution at minimum between AM and AM client applications. The load balancer itself must also be redundant, so it doesn't become a single point of failure. Illustrations in [Example deployment topology](deploy-topologies-onprem.html), show multiple levels of load balancing for availability and firewalls for security.

  > **Collapse: Is the service critical enough to warrant deployment across multiple sites?**
  >
  > AM allows you to deploy replicated configurations in different physical locations, so that if the service experiences complete failure at one site, you can redirect client traffic to another site and continue operation. The question is whether the benefit in reducing the likelihood of failure outweighs the costs of maintaining multiple sites.
  >
  > When you need failover across sites, one of the costs is (redundant) WAN links scaled for inter-site traffic. AM synchronizes configuration and policy data across sites, and by default also synchronizes session data as well. AM also expects profiles in identity stores to remain in sync. As shown in [Example deployment topology](deploy-topologies-onprem.html), the deployment involves directory service replication between sites.

  > **Collapse: What is the impact of losing individual session information?**
  >
  > AM offers different ways of storing session information to suit your environment needs. If your environment requires session high availability, AM can store sessions in the CTS token store. Even if a server fails or the client browser crashes, the session remains available as long as the CTS is available.
  >
  > In deployments where an interruption in access to a protected resource could cause users to lose valuable information, configuring the CTS correctly can prevent the loss. The underlying directory service should replicate sessions stored in CTS. Because session information can be quite volatile—more volatile than configuration and policy data—replication of the CTS across sites can therefore call for more WAN bandwidth, as more information is shared across sites.

  Once you have the answers to these questions for the deployment, you can draw a diagram of the deployment, checking for single points of failure to avoid. In the end, you should have a count of the number of load balancers, network links, and servers that you need, with the types of clients and an estimated numbers of clients that access the AM service.

  Also, you must consider the requirements for non-functional testing, covered in [Planning Tests](planning-architecture-onprem.html#plan-tests). While you might be able to perform functional testing by using a single AM server, other tests require a more complete environment with multiple servers, secure connections, and so forth. Performance testing should reveal any scalability issues. Performance testing should also run through scenarios where components fail, and check that critical functionality remains available and continues to provide acceptable levels of service.

- Size for service levels

  Beyond service availability, your aim is to provide some level of service. You can express service levels in terms of throughput and response times. For example, the service level goal could be to handle an average of 10,000 authentications per hour with peaks of 25,000 authentications per hour, and no more than 1 second wait for 95% of users authenticating, with an average of 100,000 live authenticated sessions at any given time. Another service level goal could be to handle an average of 500 policy requests per minute per web or Java agent with an average response time of 0.5 seconds.

  When you have established your service level goals, you can create load tests for each key service as described in [Plan tests](planning-architecture-onprem.html#plan-tests). Use the load tests to check your sizing assumptions.

  To estimate sizing based on service levels, take some initial measurements and extrapolate from those measurements.

  > **Collapse: For a service that handles policy decision (authorization) requests, what is the policy size?**
  >
  > To answer these questions, you can measure the current disk space and memory occupied by the configuration directory data. Next, create a representative sample of the policies you expect in your deployment, and measure the difference. Then, derive the average policy size, and use it to estimate total size.

  > **Collapse: How big is CTS data?**
  >
  > The average total size depends on the number of live CTS entries, which in turn depends on session and token lifetimes. The lifetimes are configurable and depend also on user actions like logout, that are specific to the deployment.
  >
  > For example, suppose that the deployment only handles server-side authenticated sessions, session entries occupy on average 20 KB of memory, and that you anticipate on average 100,000 active sessions. In that case, you would estimate the need for 2 GB (100,000 x 20,000) RAM on average if you wanted to cache all the session data in memory. If you expect that sometimes the number of active sessions could rise to 200,000, then you would plan for 4 GB RAM for the session cache. Keep in mind that this is extra memory needed in addition to memory needed for everything else that the system does, including running AM server.
  >
  > Session data is relatively volatile, as the CTS creates session entries when sessions are created. CTS deletes session entries when sessions are destroyed due to logout or timeout. Sessions are also modified regularly to update the idle timeout. Suppose the rate of session creation is about 5 per second, and the rate of session destruction is also about 5 per second. Then you know that the underlying directory service must handle on average 5 adds and 5 deletes per second. The added entries generate on the order of 100 KB replication traffic per second (5/s x 20 KB plus some overhead). The deleted entries generate less replication traffic, as the directory service only needs to know the distinguished name (DN) of the entry to delete, not its content.
  >
  > You can also gather statistics about CTS operations over using AM monitoring services. Learn more in [Monitor AM instances](../monitoring/monitoring-am.html).

  > **Collapse: What level of network traffic do you expect for session change notifications?**
  >
  > When sizing the network, you must account for change notifications from the Core Token Server token store to the AM server.
  >
  > In AM deployments, there is no direct network traffic between AM servers.

  > **Collapse: What increase in user and group profile size should you expect?**
  >
  > AM stores data in user profile attributes. AM can use or provision many profile attributes, as described in [To Configure an Identity Store](../setup/setting-up-identity-stores.html#realm-data-store).
  >
  > When you know which attributes are used, you can estimate the average increase in size by measuring the identity store as you did for configuration and CTS-related data. If you do not manage the identity store as part of the deployment, you can communicate this information with the maintainers. For a large deployment, the increase in profile size can affect sizing for the underlying directory service.

  > **Collapse: How does the number of realms affect the configuration data size?**
  >
  > In a centrally managed deployment with only a few realms, the size of realm configuration data might not be consequential. Also, you might have already estimated the size of policy data. For example, each new realm might add about 1 MB of configuration data to the configuration directory, not counting the policies added to the realm.
  >
  > In a multi-tenant deployment or any deployment where you expect to set up many new realms, the realm configuration data and the additional policies for the realm can add significantly to the size of the configuration data overall. You can measure the configuration directory data as you did previously, but specifically for realm creation and policy configuration, so that you can estimate an average for a new realm with policies and the overall size of realm configuration data for the deployment.

Find information on CPU, memory, network, and disk-specific sizing in [Sizing systems](size-systems.html).

---

---
title: Sizing systems
description: Estimate required capacity for PingAM systems, networks, and storage based on availability requirements and service sizing
component: pingam
version: 8.1
page_id: pingam:deployment-planning:size-systems
canonical_url: https://docs.pingidentity.com/pingam/8.1/deployment-planning/size-systems.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["deployment", "planning", "architecture", "availability", "storage"]
page_aliases: ["deployment-planning-guide:size-systems.adoc"]
section_ids:
  size-cpu-memory: Sizing system CPU and memory
  size-network-connections: Sizing network connections
  size-io-storage: Sizing disk I/O and storage
---

# Sizing systems

Given availability requirements and estimates on sizing for services, estimate the required capacity for individual systems, networks, and storage. This page considers the AM server systems, not the load balancers, firewalls, independent directory services, and client applications.

Although you can start with a rule of thumb, you see from the previous sections that the memory and storage footprints for the deployment depend in large part on the services you plan to provide. With that in mind, to performance test a basic deployment providing SSO, you can start with AM systems having at least 4 GB free RAM, 4 CPU cores (not throughput computing cores, but normal modern cores), plenty of local storage for configuration, policy, and CTS data, and LAN connections to other AM servers. This rule of thumb assumes the identity stores are sized separately, and that the service is housed on a single local site. Notice that this rule of thumb does not take into account anything particular to the service levels you expect to provide. Consider it a starting point when you lack more specific information.

## Sizing system CPU and memory

AM services use CPU resources to process requests and responses, and essentially to make policy decisions. Encryption, decryption, signing, and checking signatures can absorb CPU resources when processing requests and responses. Policy decision evaluation depends both on the number of policies configured and on their complexity.

Memory depends on space for AM code, on the number of live connections AM maintains, on caching of configuration data, user profile data, and server-side session data. The AM code in memory probably never changes while the server is running, as JSPs deployed are unlikely ever to change in production.

The number of connections and data caching depending on server tuning, as described in [Tune AM](../maintenance/tuning-am.html).

## Sizing network connections

When sizing network connections, you must account for the requests and notifications from other servers and clients, as well as the responses. This depends on the service levels that the deployment provides, as described in [Size hardware and services for deployment](deploy-sizing.html). Responses for browser-based authentication can be quite large if each time a new user visits the authentication UI pages, AM must respond with the UI page, plus all images and JavaScript logic and libraries included to complete the authentication process. Inter-server synchronization and replication can also require significant bandwidth.

For deployments with sites in multiple locations, be sure to account for configuration, CTS, and identity directory data over WAN links, as this is much more likely to be an issue than replication traffic over LAN links.

Make sure to size enough bandwidth for peak throughput, and do not forget redundancy for availability.

## Sizing disk I/O and storage

As described in [Deployment requirements](deploy-hardware-requirements.html), the largest disk I/O loads for AM servers arise from logging. You can estimate your storage requirements as described in that page.

I/O rates depend on the service levels that the deployment provides, as described in [Size hardware and services for deployment](deploy-sizing.html). When you size disk I/O and disk space, you must account for peak rates and leave a safety margin when you must briefly enable debug logging to troubleshoot any issues that arise.

Also, keep in mind the possible sudden I/O increases that can arise in a highly available service when one server fails and other servers must take over for the failed server temporarily.

Another option is to consider placing log, configuration, and database files on a different file system to maximize throughput and minimize service disruption due to a file system full or failure scenarios.