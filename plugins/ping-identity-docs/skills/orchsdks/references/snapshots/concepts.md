---
title: Concepts
description: Explore high-level concepts for the Orchestration SDKs, covering system protection design and managing multiple client tokens
component: orchsdks
page_id: orchsdks::concepts/index
canonical_url: https://developer.pingidentity.com/orchsdks/concepts/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Wed, 17 May 2023 14:10:20 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Security", "SDK"]
---

# Concepts

Discover important, high-level conceptual materials regarding use of the Orchestration SDKs.

[icon: shield-check, set=fadr, size=3x]

#### [Designing protected systems](designing-a-protected-system.html)

Learn how to use the Orchestration SDKs to secure your systems.

[icon: rectangle-history-circle-plus, set=fadr, size=3x]

#### [Multiple client tokens](multiple_instances.html)

Leverage the flexibility of multiple client instances in your apps, and learn how to store their tokens securely.

---

---
title: Designing a protected system
description: Understand key concepts for designing a protected system, including session-based and OAuth 2.0 access models, and how PingOne Advanced Identity Cloud and the SDKs fit in
component: orchsdks
page_id: orchsdks::concepts/designing-a-protected-system
canonical_url: https://developer.pingidentity.com/orchsdks/concepts/designing-a-protected-system.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 18 Apr 2023 11:57:06 +0100
keywords: ["PingOne Advanced Identity Cloud", "PingAM", "Journeys", "Setup &amp; Configuration", "Source Code", "Integration", "SDK"]
section_ids:
  the_modern_system: The modern system
  what_is_a_protected_system: What is a protected system?
  single_full_stack_server_side_application: "Single, \"full-stack\", server-side application"
  whats_a_common_system_design: What's a common system design?
  client_side_apps: Client-side apps
  resource_api_services: Resource API services
  access_management_application: Access management application
  integrate_into_a_protected_system: Integrate into a protected system
  build_a_branded_ux_with_pingone_advanced_identity_cloud_and_the_sdks: Build a branded UX with PingOne Advanced Identity Cloud and the SDKs
  whats_your_intended_system_design: What's your intended system design?
  how_many_client_side_apps_need_protecting: How many client-side apps need protecting?
  how_are_you_hosting_all_these_applications: How are you hosting all these applications?
  any_third_party_companies_involved: Any third-party companies involved?
  lets_talk_about_access_models_session_v_oauth: Let's talk about access models (session v. OAuth)
  session_based_cookies_access: Session-based (cookies) access
  oauth_2_0_based_access: OAuth 2.0-based access
  whats_the_best_design_to_protect_my_system: What's the best design to protect my system?
---

# Designing a protected system

Authentication, sessions, cookies, OAuth 2.0, authorization code flow, and so on. This page explains how to make sense of the complexity.

## The modern system

In the early days, we wrote a single application that did it all. The gorgeous monolith! It did everything: handled user requests, authenticated users, rendered UIs, queried data directly from the database, served files, managed user sessions…​ everything. This could have been an application built with Rails, Spring, Node.js, but that's no longer a representation of a "modern system".

We now live in a world where "monolith" is a bad word. Everything has been split out into microservices, SPAs (single-page web app), PWAs (Progressive Web App), native mobile apps, with other functionality delegated to a FaaS, PaaS, or SaaS (Functions, Platform or Software as a Service).

This new design has given us a greater sense of organization and tooling to focus on solving the unique, novel problems independently of the common ones. Experts can now be responsible for their relative domains within their own repository or project. If a company does not employ an expert of a required domain, it can now "outsource" it to be managed by another company.

Unfortunately, this new paradigm comes with its own set of problems. Architecture diagrams now illustrate a complex web of distributed components that are simple in isolation, but hard to reason about when viewed holistically. Due to this distributed nature, the system now comes with more surface area to protect from unwanted access.

In a world where everything is a tap or click-of-the-finger away, it's more important than ever to ensure the right fingers have access to the right data. Knowing the basics of a protected system is no longer optional. Developers, product managers, IT professionals, all need to have a good grasp of the fundamentals.

Let's cover the basics to ensure we keep our data convenient but private and our users happy but safe.

## What is a protected system?

In most modern, enterprise cases, "the system" will consist of a diverse collection of entities, but let's start with the most simple use case (not quite a system, but bear with me): the monolith.

### Single, "full-stack", server-side application

![monolith diagram](../_images/designing-a-protected-system/monolith-diagram.jpg)Figure 1. Architecture diagram of a monolith

This single application was responsible for everything, including identity and access management. These were applications common around the turn of the century. Though these "systems" still exist, they are becoming much less common as they are very hard to manage and engineer at large scale.

To take some baby steps, let's consider one step up from this monolith, and separate out access management from the monolith.

![app with access management](../_images/designing-a-protected-system/app-with-access-management.jpg)Figure 2. Architecture diagram of a monolith paired with access management app

In this design, you have two entities:

1. Protected, full-stack, server-side application: An application managing the resources you want protected.

2. **Access management application**: An application managing all identity and access concerns.

The beauty of this system is how it scales. If you decide to add another protected application to the system, you just delegate the access related needs to the access management application. (There are other great benefits to this, but let's save that for another article.) The new application introduced to the system could be a web app, mobile app, REST API service app, GraphQL app…​ anything that potentially serves up a protected resource.

In an effort to avoid having to rebuild such a vital function over and over with each new app, you "connect them" to your access management app. This dramatically reduces the surface area of risk in complex systems.

What's more, this serves the users better. It means they log in once, and have access to everything their role or privileges allow. With me so far? Okay, let's go a bit further.

## What's a common system design?

In modern system architectures, it's quite common to split the full-stack application into a backend with multiple, client-side apps, often one per platform: iOS, Android, Web. In these situations, it's advantageous to keep all data related concerns of our protected app within a central API server—​often referred to as a "service". Each client app requests data via an API. This prevents business logic duplication across multiple applications and simplifies client-side development.

Let's add these multiple client-side apps as a generic entity to our system from above. We now have three distinct entity types as our "protected app" has been split into two application types:

1. **Protected client-side applications (Mobile and Web)**

2. Protected server-side, resource API service

3. Access management application

![Architecture diagram a SPA, resource API server and access management app](../_images/designing-a-protected-system/spa-resource-with-access-management.jpg)

The main *access* responsibility of the protected client apps and the API service is to distinguish authenticated users from unauthenticated ones. This ensures those without access get denied, and converted to users with access by directing them to the access management app.

Let's break down the responsibility of each.

### Client-side apps

The role of a protected client-side app is to not only distinguish between authenticated and unauthenticated users, but to assist in converting unauthenticated users into authenticated with as little friction as necessary.

An app will typically have both public and private portions. The simplest way to protect the private portion is by route, page or view. The protected routes will often have a reusable function that's run before any response is given, often referred to as "middleware". This function checks if the user has access by sending the access artifact, like a session cookie, to the access management app for validation. If the validation succeeds, the app continues processing the request; if not, the app will redirect the user to the login page.

This can be something as simple as this:

```js
// Using a common client-side, middleware-style pattern (session-based example)
async function isAuthenticated(context, next) {
  const authResponse = await request(sessionValidateEndpoint);

  if (authResponse.valid) {
    next(); // continue with processing request
  } else {
    redirect(authenticationUrl); // send user to login
  }
}

routes('accounts/balances', isAuthenticated, (context) => {
  render(changePasswordForm);
});
```

|   |                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It's important to know that protected client-side apps are not truly secure, and should not have embedded within them protected resources, secrets or private keys. They are inherently vulnerable as the entire codebase is sent to the user agent—​a device outside of your control—​to be executed, so all code is subject to manipulation. |

Even though this client-side application cannot *guarantee* access protection, the implementation of such protection on the client increases user-experience and performance. It also reduces unnecessary requests to the underlying services.

### Resource API services

The role of a protected resource API service is to be the final arbiter for protecting access to resources within the system. Since we can't *fully* trust our client-side applications, our resource API will need to duplicate the same check for authentication.

It will use the authentication artifact sent from the client with every request to validate the access to the requested resource. If validation passes, process the request. If it fails, send a 401 error message, and let the client-side app appropriately handle the issue:

```js
// Using a Node.js middleware-style pattern (session-based example)
async function isAuthenticated(req, res, next) {
  const authResponse = await request(sessionValidateEndpoint);

  if (authResponse.valid) {
    next(); // continue with processing request
  } else {
    res.status(401).send(); // respond with 401 unauthorized
  }
}

routes.get('accounts/balances', isAuthenticated, (req, res) => {
  const balances = db.query('balances');

  res.json(balances);
});
```

|   |                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The above is route-level protection, which may not be granular enough for your system. Object-level protection, an increase in access control precision, may be required for your system but is outside the scope of this article. |

### Access management application

The access management (generic) application has the most important role in a protected system. It manages users, login, sessions, authorization, password management, and so on, all of which are vital functions.

At the simplest level, here are the main responsibilities of the application:

* Handles redirection from client-side apps for login, redirecting users back to the respective application upon completion.

* Provides an API for session/artifact validation.

* Provides an API for termination of session or artifact.

In situations where the above responsibilities exceed your level of comfort or skill set, it's often a good idea to delegate these responsibilities to a platform service provider, like Ping Identity. Our services and products allow you to focus on the novel aspects of your application development, and delegate the complexities of identity management (users, things, devices, and more), and access management (what those identities can do) to us.

Let's see how adopting Ping for our access management changes our system.

## Integrate into a protected system

We provide a powerful, configurable Identity and Access Management solution out of the box. Whether it's an PingOne Advanced Identity Cloud tenant; self-hosted, cloud-ready container; or individual on-premise products, our products can provide a great solution for nearly any system. For simplicity, let's go with the PingOne Advanced Identity Cloud solution for the rest of this article.

PingOne Advanced Identity Cloud comes with its own login flow, registration and self-service journeys, as well as all the APIs needed for validation, refreshing, termination, authorization and more. This all-in-one solution works perfect for internal solutions or get-up-and-running quickly situations. But eventually, most companies want their user-facing experience to be fully customizable to suit their branding requirements.

> If I'm redirecting my users to ForgeRock's platform, how do I provide a **fully** branded experience?

In ForgeRock's PingOne Advanced Identity Cloud, you can choose how much control you want over your UIs. You can use it as-is, "theme" the provided UIs, or build your own UI using the underlying APIs and our open-source SDKs.

### Build a branded UX with PingOne Advanced Identity Cloud and the SDKs

A fully branded experience means moving the responsibility of rendering the user authentication journey from PingOne Advanced Identity Cloud to an app that you will build. To facilitate this, we provide the Orchestration SDK for native Android and iOS apps, and for JavaScript application development. This allows you to easily integrate APIs into a new or existing app.

There are two choices for fully customizing the user experience:

1. Move the user authentication experience into each protected app, providing a native UX.

2. Move the user authentication experience into a single web app to centralize the login experience.

In both cases, our SDKs will help in developing these experiences. But, before we move on, it's important to know that your overall system has a significant impact on what choice suits you best.

## What's your intended system design?

There are a few important points to consider when choosing how to protect your system:

1. How many client-side apps will need protecting?

2. Are all your apps and services served from a single domain?

3. Will there be any third-party apps or services that will need protection?

Let's dive into each concern and how it impacts your system.

### How many client-side apps need protecting?

Say you have one app for each major platform: a web app, an iOS app, and an Android app. If the number of apps will not increase, you may want to develop the user experience for login, registration, and so on, within each app. This ensures that each app has full control over the best user experience for that platform.

By using our SDKs, you can more efficiently develop a dynamically responsive UI, handling each step within an authentication journey. This just slightly changes our client-side app's responsibilities.

Rather than redirecting unauthenticated users away from our application, we now just internally route the user to our native login experience. But, we will still continue to validate the user's session upon each navigation of our app.

![spa with embedded login with access management](../_images/designing-a-protected-system/spa-with-embedded-login-with-access-management.jpg)Figure 3. Architecture diagram of a SPA with Embedded Login and access management app

> But, we have dozens/hundreds of client-side applications! We don't have the resources to update all of them.

Now, if you have many apps, and each app needs to have within it a login (not to mention registration) flow, that's a lot of duplication. This will inevitably become a maintainability challenge, and a security liability as it increases your attack surface. Within this context, we need to go one step further.

To deal with this challenge, it's often recommended to extract the login (and possibly registration, self-service) related responsibilities out of the client-side apps, and build a single web app exclusively around this functionality. All front-end applications (mobile and web) can now redirect to this one, central application. This reduces your surface area for security liabilities as well as reduces duplication across your system.

Let's take a look at the system now:

1. Protected client-side apps (mobile & web)

2. Protected resource API services

3. **Authentication (login, registration & self-service) web app**

4. PingOne Advanced Identity Cloud

![resource spa login spa with access management api](../_images/designing-a-protected-system/resource-spa-login-spa-with-access-management-api.jpg)Figure 4. Architecture diagram of a SPA for resource app, a SPA for the login app, resource API server and access management app

With this design, we are now starting to organize the system components by scope of responsibility. For mobile applications, they'll have the availability of using the browser to authenticate, being redirected back to the native app when complete. Web apps will do a full redirect to the authentication app and a redirect back when done. Single sign-on functionality is provided out-of-the-box, as the browser is the shared platform for authentication between all apps, native or otherwise, on the user's device.

This provides a more scalable system that's optimized with apps having a more focused set of responsibilities while still providing full control over your brand and UX. Now that we have the core system design out of the way, let's discuss how all of these components will be hosted.

### How are you hosting all these applications?

Simply put, are all the applications in the above system on the same host? For example:

* `mydomain.com/auth`

* `mydomain.com/app`

* `mydomain.com/api`

Another example would be the use of unique subdomains all on the same parent domain:

* `auth.mydomain.com`

* `app.mydomain.com`

* `api.mydomain.com`

If using either of the two patterns, a session-based system may work well for you. Sessions are frequently based on browser cookies, which are fundamentally restricted by the host or parent domain.

On the other hand, you may be using different hosts across your apps:

* `auth-server.com`

* `web-app.com`

* `rest-server.com`

This will constrain your options as session-based auth (driven by cookies) will be a challenge with apps on multiple hosts. An OAuth-based system is well-designed for this particular environment as it uses access tokens as the artifact passed around in the system, rather than a cookie.

But, before we dive into OAuth 2.0, let's discuss one more aspect of our system.

### Any third-party companies involved?

Do you intend to extend access of your protected system to any third-party companies? For example, you may want to allow an application or service from an external company to interact with your protected system. For this, you likely want to restrict the scope of capabilities for these external entities, making an OAuth-based system a better choice.

What's OAuth and why is it better than session-based access with diverse hosting environments and third-party entities? Let's differentiate these two models.

## Let's talk about access models (session v. OAuth)

To keep things simple, let's focus on two of the most common models of access: session-based and OAuth-based. Your system design, discussed above, should strongly influence the type of access model you want to implement, but it's not the only factor in making the choice.

Additional factors that can influence your access modeling are a bit more advanced and out of scope for this article, but they include:

1. Transaction authorization (aka policy enforcement)

2. Finer control over expiry times and access lifetimes

3. Finer control over scope of access or privileges

Look out for more information about these factors in a future article. For the rest of this article, let's talk a bit more about the basics of two foundational access models.

### Session-based (cookies) access

The session-based model traditionally uses the *HTTP cookie* as its artifact. It's one of the oldest models for the web as the cookie was invented around the mid 1990's (though not originally for authentication). The HTTP cookie is a relatively simple way to persist data (a simple string of text) within a Web browser. This small piece of information is stored natively in the browser, and is tightly bound to the domain of the HTTP request the browser made to the server.

Let's use a simple example:

There's a web app running on `https://dashboard.example.com`, and an access management application running on `https://auth.example.com`. After making a request to the access management app to login, a "session cookie" gets added to the browser. This cookie is written because the server sent back a `Set-Cookie` header, so the cookie gets written to the full domain of the server, `auth.example.com`, or the parent domain, `example.com`.

Example of browser cookie storage:

```txt
-------------------- -------------------- --------------------
COOKIE NAME          VALUE                DOMAIN

session_id           AJi4QfFBCMzK3QFm...    .example.com
-------------------- -------------------- --------------------
```

Now that we have this cookie, all requests from that browser to `example.com` (even subdomains that share the same parent) will contain a `cookie` header with its value. It's worth noting that this "Just Works" as it's a seamless, almost invisible, mechanism of the browser.

Example of request with cookie:

```text
GET https://auth.example.com/sessions/validate

HEADERS
content-type: application/json
cookie:       session_id=AJi4QfFBCMzK3Qc...s9dg7f6hyGHD
origin:       https://dashboard.example.com
```

This means you can have multiple apps running on multiple subdomains. As long the same parent or root domain is used, this session cookie will be sent automatically.

For example:

* `www.example.com`

* `accounts.example.com`

* `profile.example.com`

* `tasks.example.com`

With servers running on:

* `auth.example.com`

* `data.example.com`

As long as all apps, both client and server, are running on the same parent domain (`example.com`), you can configure cookies to work with this setup. In this case, we would configure the cookie to be written to the parent domain, `example.com` for the highest amount of flexibility. Your applications can then have their own subdomains and will still receive the cookie (many browsers store this as `.example.com`).

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | The downside to this model is the tight coupling of cookies with their respective domains. |

If you have apps running on different domains, say `auth.example.com` and `data.userbase.com`, this model unfortunately does not work. The cookies written for `auth.example.com` would not be sent to our `data.userbase.com` server. In this case, OAuth provides better support.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Third-party cookies**: it's worth noting that there's still a nuance with cookies being written when browser-based apps (SPAs) are running on a different domain than the servers.These cookies are considered "Third-Party Cookies", and have been an important function of how the Web worked for years. Unfortunately, most browsers will disable this functionality within the next few years, so relying on it will be risky.[Safari has already disabled third-party cookies by default](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more). |

### OAuth 2.0-based access

OAuth is an industry standard for handling authorization and has been around since the late 2000's. OAuth 2.0 is the most recent specification of the protocol and is a large rework from the original. In this writing, any reference to [OAuth will always refer to the 2.0 specification](https://www.rfc-editor.org/rfc/rfc6749).

OAuth is a complex specification and has many variations and nuances. The details of which are beyond the scope of this article, so we will focus only on the basics.

The core artifact of OAuth is the *access token*, and like the value stored in a cookie for sessions, it is frequently just a simple string of text (sometimes called a JWT). But, unlike the cookie, the browser does not have a native concept of an access token, so obtaining and managing an Access Token doesn't automatically happen within a browser.

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | There are other tokens frequently mentioned in texts about OAuth that are beyond the scope of this article, like refresh tokens and ID tokens. These tokens will not be covered in order to keep this article more introductory. |

There are some choices about how to store and send the access tokens within a system. For the Web, as a simple example, `sessionStorage` or `localStorage` can often be used to store the token. Access Tokens are also not automatically sent along with all HTTP requests, so how one writes this token to HTTP requests is also something to be considered. Luckily, the industry has already standardized around *best practices*.

> So, why is OAuth 2.0 better than session-based cookies in certain circumstances?

OAuth is often mentioned in situations where you have third-party applications and services, or a multi-host setup with varying domains. This is because of its granularity of permissions (for security/privacy) and complete decoupling from domains. This provides more control over how it behaves. At the end of the day, an access token is just an opaque string that's passed around the system, frequently called a "bearer token", and written to the `Authorization` header of requests.

Example of request with authorization header:

```text
GET https://rest.resource.com/activity

HEADERS
content-type:  application/json
authorization: Bearer 3QcIFmU6r0q43U...LJKf807
origin:        https://dashboard.example.com
```

Using OAuth doesn't dramatically change your system design. The basic principles of how it's used doesn't significantly diverge from the session-based model. You are still obtaining an access artifact from a server, passing it to APIs, and validating it where necessary. The additional responsibilities with Access Tokens are storing it and removing it as needed.

For example, here are some minor changes to the middleware example from above:

```js
// Using Node.js middleware-style pattern (oauth-based example)
async function isAuthorized(req, res, next) {
  const authResponse = await request(oauthIntrospectionEndpoint);

  if (authResponse.access) {
    next(); // continue with processing request
  } else {
    res.redirect(authorizationUrl); // send to authorization
  }
}

routes.get('accounts/balances', isAuthorized, (req, res) => {
  res.render(changePasswordForm);
});
```

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Validating access tokens can also be done without a network request. We refer to these as "stateless" tokens. They can be introspected with a JWT decoding library for validation. |

The only remaining difference between the OAuth and session-based model is the fact that an OAuth token has to be specially obtained from your access management application. The most common flow for attaining an access token is called the authorization code flow, and involves an additional interaction with the server after the user successfully authenticates.

The good thing is you do not have to reinvent the wheel to implement OAuth within your applications. PingOne Advanced Identity Cloud and SDKs abstract away the need for requesting, storing, sharing, and revoking the access token, leaving you with more time to build the novel aspects of your applications.

## What's the best design to protect my system?

The answer is…​ well, *it depends*. As discussed above, there are quite a few important aspects to the kind of system we are discussing and the future plans for your products. Hopefully, after reading through the basics articulated above, you have a better, foundational understanding of what it means to design a protected system.

If things are still a bit fuzzy, don't worry. The good news is that Ping can help by providing the best tools and guidance to ensure you have the right information to make the best choice for you.

---

---
title: Handling tokens for multiple clients
description: Configure multiple SDK client instances with independent token storage to support step-up authentication and concurrent multi-user sessions in your app
component: orchsdks
page_id: orchsdks::concepts/multiple_instances
canonical_url: https://developer.pingidentity.com/orchsdks/concepts/multiple_instances.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 25 Nov 2025 11:07:37 +0100
keywords: ["step-up", "authentication", "multiple", "client", "instances"]
section_ids:
  understanding_the_storage_module: Understanding the Storage module
  use_case_1_step_up_authentication_isolating_tokens: "Use Case 1: Step-up authentication (isolating tokens)"
  configuration: Configuration
  code_implementation: Code implementation
  server_setup_for_step_up_authentication: Server setup for step-up authentication
  authorization_server_as: Authorization Server (AS)
  resource_server_rs: Resource Server (RS)
  use_case_2_multiple_users_isolating_sessions_and_tokens: "Use Case 2: Multiple users (isolating sessions and tokens)"
  configuration_2: Configuration
  code_implementation_2: Code implementation
  managing_multiple_client_instances_in_your_app: Managing multiple client instances in your app
  why_no_abstraction_layer: Why no abstraction layer?
  example_1_using_direct_references_for_named_instances: "Example 1: Using direct references for named instances"
  example_2_using_a_map_or_dictionary_for_named_instances: "Example 2: Using a Map or Dictionary for named instances"
  example_3_using_a_list_or_array_for_multiple_user_accounts: "Example 3: Using a List or Array for multiple user accounts"
---

# Handling tokens for multiple clients

Both the **Journey** module and the **DaVinci** module support multiple client instances in your apps. Each client instance you create is a runtime object that manages an independent authentication flow, complete with its own configuration, state, and token storage.

This powerful architecture enables a wide range of use cases, including:

* Multiple concurrent sessions for the same, or different users.

* Step-up authentication for accessing sensitive resources.

* Multi-tenant applications with isolated authentication contexts.

* Parallel token management with different lifecycle policies.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | The **Journey** module and the **DaVinci** module must not share storage.The session and OIDC tokens they use aren't interchangeable. |

## Understanding the Storage module

By default, all client instances you create share the same storage locations for session tokens and OpenID Connect tokens. This is the simplest configuration and is suitable for many applications.

* **Shared Session/Cookie Storage**: All client instances share the same session, representing the same authenticated user.

* **Shared Token Storage**: All client instances share the same access token, when using the **OIDC** module.

This default behavior means that if a user authenticates using one instance, they're authenticated across all client instances.

Figure 1. Two client instances in an app, sharing session and OIDC token storage.

In this scenario, both client instances share the same authenticated user session and access token. A change in one instance, such as signing out, affects the other.

## Use Case 1: Step-up authentication (isolating tokens)

A common requirement is to have a single user session but use different access tokens for different levels of security. For example, a user might have a long-lived token for general app usage but an on-demand, short-lived, high-security token for a sensitive transaction.

The **Journey** and **DaVinci** modules support this step-up authentication by leveraging multiple client instances, each with different authentication requirements.

To achieve this, you customize the **token storage** for each instance while continuing to use the **shared session storage**.

### Configuration

In this model:

* **Session Storage remains shared**: Both instances recognize the same authenticated user.

* **Token Storage is isolated**: Each instance manages its own access token, with its own lifecycle, scopes, and claims.

Figure 2. Two client instances in an app, sharing session tokens but isolating OIDC token storage.

With this setup, both client instances share the same user session, but each manages an independent access token. This allows for different permissions and lifecycles for each token.

### Code implementation

Here's how you would configure two instances—one for standard authentication and one for high-security transactions.

* Android - DaVinci

* Android - Journey

* iOS - DaVinci

* iOS - Journey

Configuring two client instances using two OIDC token storage locations

```kotlin
// Instance 1 - Standard authentication with long-lived tokens
val standardInstance = DaVinci {
    module(Oidc) {
        clientId = "{standard_client_id}"
        scopes = mutableSetOf("openid", "profile", "email")
        redirectUri = "org.forgerock.demo://oauth2redirect"
        discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"

        // Custom storage for this instance's access tokens
        storage {
            fileName = "standard_tokens"
        }
    }

    // No custom session storage is defined, so it uses the default shared session.

}

// Instance 2 - High-security transactions with short-lived tokens
val transactionInstance = DaVinci {
    module(Oidc) {
        clientId = "{transaction_client_id}"
        scopes = mutableSetOf("openid", "transactions")
        redirectUri = "org.forgerock.demo://oauth2redirect"
        discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"

        // Separate storage for this instance's access token
        storage {
            fileName = "transaction_tokens"
        }
    }

    // Also uses the default shared session storage.
}
```

Configuring two client instances using two OIDC token storage locations

```kotlin
// Instance 1 - Standard authentication with long-lived tokens
val standardInstance = Journey {
    serverUrl = "https://openam-forgerock-sdks.forgeblocks.com/am"
    realm = "alpha"
    module(Oidc) {
        clientId = "{standard_client_id}"
        scopes = mutableSetOf("openid", "profile", "email")
        redirectUri = "org.forgerock.demo://oauth2redirect"

        // Custom storage for this instance's access tokens
        storage {
            fileName = "standard_tokens"
        }
    }

    // No custom session storage is defined, so it uses the default shared session.

}

// Instance 2 - High-security transactions with short-lived tokens
val transactionInstance = Journey {
    serverUrl = "https://openam-forgerock-sdks.forgeblocks.com/am"
    realm = "alpha"
    module(Oidc) {
        clientId = "transaction-client"
        scopes = mutableSetOf("openid", "transactions")
        redirectUri = "org.forgerock.demo://oauth2redirect"

        // Separate storage for this instance's access token
        storage {
            fileName = "transaction_tokens"
        }
    }

    // Also uses the default shared session storage.
}
```

Configuring two client instances using two OIDC token storage locations

```swift
// Instance 1 - Standard authentication with long-lived tokens
let standardDaVinciInstance = DaVinci.createDaVinci { config in

    config.module(CookieModule.config) { cookieConfig in
        cookieConfig.cookieStorage = KeychainStorage<[CustomHTTPCookie]>(account: "standard_storage", encryptor: SecuredKeyEncryptor() ?? NoEncryptor())
    }

    config.module(PingDavinci.OidcModule.config) { oidcConfig in
        oidcConfig.clientId = "{standard_client_id}"
        oidcConfig.scopes = ["openid", "profile", "email"]
        oidcConfig.redirectUri = "org.forgerock.demo://oauth2redirect"
        oidcConfig.discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
        oidcConfig.acrValues = "" //update with actual ACR values if needed or

        // Separate storage for this instance's access token
        oidcConfig.storage = KeychainStorage<Token>(account: "standard_tokens")
    }

}

// Instance 2 - High-security transactions with short-lived tokens
let transactionDaVinciInstance = DaVinci.createDaVinci { config in

    config.module(CookieModule.config) { cookieConfig in
        cookieConfig.cookieStorage = KeychainStorage<[CustomHTTPCookie]>(account: "transaction_cookies", encryptor: SecuredKeyEncryptor() ?? NoEncryptor())
    }

    config.module(PingDavinci.OidcModule.config) { oidcConfig in
        oidcConfig.clientId = "{transaction_client_id}"
        oidcConfig.scopes = ["openid", "transactions"]
        oidcConfig.redirectUri = "org.forgerock.demo://oauth2redirect"
        oidcConfig.discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
        oidcConfig.acrValues = "" //update with actual ACR values if needed or remove

        // Separate storage for this instance's access token
        oidcConfig.storage = KeychainStorage<Token>(account: "transaction_tokens")
    }

    // Uses the custom cookie storage configured above
}
```

Configuring two client instances using two OIDC token storage locations

```swift
// Instance 1 - Standard authentication with long-lived tokens
let standardInstance = Journey.createJourney { config in
    config.serverUrl = "https://openam-forgerock-sdks.forgeblocks.com/am"
    config.realm = "alpha"
    config.module(PingJourney.OidcModule.config) { oidcConfig in
        oidcConfig.clientId = "{standard_client_id}"
        oidcConfig.scopes = ["openid", "profile", "email"]
        oidcConfig.redirectUri = "org.forgerock.demo://oauth2redirect"

        // Custom storage for this instance's access tokens
        oidcConfig.storage = KeychainStorage<Token>(account: "standard_tokens")
    }

    // No custom session storage is defined, so it uses the default shared session.
}

// Instance 2 - High-security transactions with short-lived tokens
let transactionInstance = Journey.createJourney { config in
    config.serverUrl = "https://openam-forgerock-sdks.forgeblocks.com/am"
    config.realm = "alpha"
    config.module(PingJourney.OidcModule.config) { oidcConfig in
        oidcConfig.clientId = "{transaction_client_id}"
        oidcConfig.scopes = ["openid", "transactions"]
        oidcConfig.redirectUri = "org.forgerock.demo://oauth2redirect"

        // Separate storage for this instance's access token
        oidcConfig.storage = KeychainStorage<Token>(account: "transaction_tokens")
    }

    // Also uses the default shared session storage.
}
```

### Server setup for step-up authentication

To enable step-up authentication there must be something within the access token that indicates what level of authentication it can achieve. These are collectively known as **authentication indicators**.

#### Authorization Server (AS)

Your authorization server can embed authentication indicators using one or more of the following methods:

* **`amr` (Authentication Methods Reference)**

  Indicates *how* the user authenticated, for example, `pwd`, `mfa`.

  Learn about configuring Advanced Identity Cloud to use `amr` claims at [Configure amr claims](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-authentication-requirements.html#proc-configure-amr-node).

* **`acr` (Authentication Context Class Reference)**

  A standardized OIDC claim indicating the "level" of authentication.

  Learn about `acr` claims in Advanced Identity Cloud at [The acr claim](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-authentication-requirements.html#acr-claim).

* **`scopes`**

  The permissions granted by the token, for example, `read_transaction`.

  Configure the OAuth 2.0 client to require elevated authentication for specific scopes:

  * Define scopes that trigger step-up authentication, for example `READ_TRANSACTION` and `WRITE_TRANSACTION`.

  * The authorization server enforces step-up when these scopes are requested.

  * Resource servers validate that the token contains the required scope.

* **`auth_level`**

  In Advanced Identity Cloud and PingAM, you can use a custom claim named `auth_level` that indicates authentication strength.

  If an API requires a higher level of authentication, the Resource Server rejects the request, which prompts the app to initiate a step-up flow using the appropriate high-security instance.

  Learn about setting auth levels in a journey at [Modify Auth Level node](https://docs.pingidentity.com/auth-node-ref/latest/modify-auth-level.html).

Example access token containing step-up claims

```json
{
  "sub": "445957f9--...--5452214633e8",
  "cts": "OAUTH2_STATELESS_GRANT",
  "auth_level": 3,
  "auditTrackingId": "c9611769-...-297791",
  "subname": "445957f9-...-5452214633e8",
  "iss": "https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/alpha",
  "tokenName": "access_token",
  "token_type": "Bearer",
  "authGrantId": "fpO7...MaHY",
  "client_id": "demo_user",
  "aud": "demo_user",
  "nbf": 1761261789,
  "grant_type": "authorization_code",
  "scope": [
    "address",
    "phone",
    "openid",
    "profile",
    "READ_TRANSACTION",
    "email"
  ],
  "auth_time": 1761261789,
  "realm": "/alpha",
  "exp": 1761265389,
  "iat": 1761261789,
  "expires_in": 3600,
  "jti": "Ygd5...25lk",
  "amr": [
    "Login2"
  ]
}
```

#### Resource Server (RS)

The Resource Server plays a critical role in enforcing access control by validating the claims present in the access token.

Based on the authentication indicators, the Resource Server decides whether to grant or deny access to a protected API, by using one or more of the following techniques:

* Token introspection

  The Resource Server receives the access token from the client application. It then introspects the token to validate its authenticity and retrieve the associated claims.

* Claim validation

  The server checks for specific claims to determine if the required authentication level has been met.

  * It might require a minimum `auth_level`.

  * It might check for the presence of a specific `amr` value, such as "mfa" or "biometric".

  * It can validate if a required scope is present, for example "READ\_TRANSACTION".

* Access control

  If the claims meet the security policy for the requested API, the server grants access.

  If not, it returns an error such as `403 Forbidden` or `401 Unauthorized` and includes information about the required authentication level.

For example, a resource server protecting a high-value transaction API might enforce the following business rules:

* Require `auth_level` to be `3` or higher.

* Require the `amr` claim to include `biometric`.

* Require `scope` to contain `WRITE_TRANSACTION`.

## Use Case 2: Multiple users (isolating sessions and tokens)

For applications that need to support multiple, separate user accounts on the same device, you must isolate both session and token storage. This ensures that each user has their own independent authentication context.

### Configuration

In this model, each instance has its own dedicated storage for everything.

* **Session Storage is isolated**: Each client instance has a separate session file.

* **Token Storage is isolated**: Each client instance has a separate token file.

Figure 3. Two clients with separate session and OIDC token storage

In this case, each client instance represents a different authenticated user with completely independent session and OIDC tokens. Signing one user out won't affect the others.

### Code implementation

Here's how you would configure two instances for two different users, ensuring their sessions and tokens are kept separate.

* Android - DaVinci

* Android - Journey

* iOS - DaVinci

* iOS - Journey

Configuring two client instances each using independent storage locations

```kotlin
val User_A_instance = DaVinci {

    // Custom session storage for User A
    module(Session) {
        storage {
          fileName = "user_a_sessions"
        }
    }

    module(Oidc) {
        clientId = "{standard_client_id}"
        discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
        scopes = mutableSetOf("openid", "profile", "email")
        redirectUri = "org.forgerock.demo://oauth2redirect"

        // Custom token storage for User A
        storage {
            fileName = "user_a_tokens"
        }
    }
}

val User_B_instance = DaVinci {

    // Custom session storage for User B
    module(Session) {
      storage {
        fileName = "user_b_sessions"
      }
    }

    module(Oidc) {
        clientId = "{standard_client_id}"
        discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
        scopes = mutableSetOf("openid", "profile", "email")
        redirectUri = "org.forgerock.demo://oauth2redirect"

        // Custom token storage for User B
        storage {
            fileName = "user_b_tokens"
        }
    }
}
```

Configuring two client instances each using independent storage locations

```kotlin
val User_A_instance = Journey {
    serverUrl = "https://openam-forgerock-sdks.forgeblocks.com/am"
    realm = "alpha"

    // Custom session storage for User A
    module(Session) {
        storage {
          fileName = "user_a_sessions"
        }
    }

    module(Oidc) {
        clientId = "{standard_client_id}"
        discoveryEndpoint = "https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/alpha/.well-known/openid-configuration"
        scopes = mutableSetOf("openid", "profile", "email")
        redirectUri = "org.forgerock.demo://oauth2redirect"

        // Custom token storage for User A
        storage {
            fileName = "user_a_tokens"
        }
    }
}

val User_B_instance = Journey {
    serverUrl = "https://openam-forgerock-sdks.forgeblocks.com/am"
    realm = "alpha"

    // Custom session storage for User B
    module(Session) {
      storage {
        fileName = "user_b_sessions"
      }
    }

    module(Oidc) {
        clientId = "{standard_client_id}"
        discoveryEndpoint = "https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/realms/alpha/.well-known/openid-configuration"
        scopes = mutableSetOf("openid", "profile", "email")
        redirectUri = "org.forgerock.demo://oauth2redirect"

        // Custom token storage for User B
        storage {
            fileName = "user_b_tokens"
        }
    }
}
```

Configuring two client instances each using independent storage locations

```swift
let User_A_instance = DaVinci.createDaVinci { config in

    // Custom cookie storage for User A
    config.module(CookieModule.config) { cookieConfig in
        cookieConfig.cookieStorage = KeychainStorage<[CustomHTTPCookie]>(account: "user_a_cookies", encryptor: SecuredKeyEncryptor() ?? NoEncryptor())
    }

    config.module(PingDavinci.OidcModule.config) { oidcConfig in
        oidcConfig.clientId = "{standard_client_id}"
        oidcConfig.scopes = ["openid", "profile", "email"]
        oidcConfig.redirectUri = "org.forgerock.demo://oauth2redirect"
        oidcConfig.discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"

        // Custom storage for this instance's access tokens
        oidcConfig.storage = KeychainStorage<Token>(account: "user_a_tokens")
    }
}

let User_B_instance = DaVinci.createDaVinci { config in

    // Custom cookie storage for User A
    config.module(CookieModule.config) { cookieConfig in
        cookieConfig.cookieStorage = KeychainStorage<[CustomHTTPCookie]>(account: "user_b_cookies", encryptor: SecuredKeyEncryptor() ?? NoEncryptor())
    }

    config.module(PingDavinci.OidcModule.config) { oidcConfig in
        oidcConfig.clientId = "{standard_client_id}"
        oidcConfig.scopes = ["openid", "profile", "email"]
        oidcConfig.redirectUri = "org.forgerock.demo://oauth2redirect"
        oidcConfig.discoveryEndpoint = "https://auth.pingone.com/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"

        // Custom storage for this instance's access tokens
        oidcConfig.storage = KeychainStorage<Token>(account: "user_b_tokens")
    }
}
```

Configuring two client instances each using independent storage locations

```swift
let User_A_instance = Journey.createJourney { config in

    config.serverUrl = "https://openam-forgerock-sdks.forgeblocks.com/am"
    config.realm = "alpha"

    // Custom cookie storage for User A
    config.module(SessionModule.config) { sessionConfig in
        sessionConfig.storage = KeychainStorage<SSOTokenImpl>(
            account: "user_a_sessions",
            encryptor: SecuredKeyEncryptor() ?? NoEncryptor()
        )
    }

    config.module(PingJourney.OidcModule.config) { oidcConfig in
        oidcConfig.clientId = "{standard_client_id}"
        oidcConfig.scopes = ["openid", "profile", "email"]
        oidcConfig.redirectUri = "org.forgerock.demo://oauth2redirect"

        // Custom storage for this instance's access tokens
        oidcConfig.storage = KeychainStorage<Token>(account: "user_a_tokens")
    }
}

let User_B_instance = Journey.createJourney { config in

    config.serverUrl = "https://openam-forgerock-sdks.forgeblocks.com/am"
    config.realm = "alpha"

    // Custom cookie storage for User B
    config.module(SessionModule.config) { sessionConfig in
        sessionConfig.storage = KeychainStorage<SSOTokenImpl>(
            account: "user_b_sessions",
            encryptor: SecuredKeyEncryptor() ?? NoEncryptor()
        )
    }

    config.module(PingJourney.OidcModule.config) { oidcConfig in
        oidcConfig.clientId = "{standard_client_id}"
        oidcConfig.scopes = ["openid", "profile", "email"]
        oidcConfig.redirectUri = "org.forgerock.demo://oauth2redirect"

        // Custom storage for this instance's access tokens
        oidcConfig.storage = KeychainStorage<Token>(account: "user_b_tokens")
    }
}
```

## Managing multiple client instances in your app

We designed the SDK for direct and simple management of multiple instances. You don't need an additional abstraction layer, as each instance is self-contained and provides all the necessary methods to manage its own lifecycle.

### Why no abstraction layer?

* Simplicity

  Adding an abstraction layer introduces unnecessary complexity without significant benefits.

* Flexibility

  You can implement your own management approach using any data structure, such as a list, map, or set.

* Direct Control

  Working directly with client instances provides clearer code and better understanding of what's happening.

* No Simplification

  An abstraction layer doesn't simplify the code - it just adds another layer to maintain.

You can manage your instances using standard collections like a `Map` or a `List`, or by using direct references.

### Example 1: Using direct references for named instances

This approach is easy to read as each operation is specific to a named instance. However it might not scale to support many instances.

* Android

* iOS

Using direct references for named instances on Android

```kotlin
class MyApp : Application() {
    // Switch "Journey" to "DaVinci" when using DaVinci
    val standardInstance = Journey { /* config */ }
    val transactionInstance = Journey { /* config */ }

    suspend fun logoutBoth() {
        standardInstance.user()?.logout()
        transactionInstance.user()?.logout()
    }

    suspend fun refreshTransactionToken() {
        transactionInstance.user().refresh()
    }
}
```

Using direct references for named instances on iOS

```swift
import PingJourney

class MyApp {
    // Switch "Journey.createJourney" to "DaVinci.createDaVinci" when using DaVinci
    let standardInstance = Journey.createJourney { /* config */ }
    let transactionInstance = Journey.createJourney { /* config */ }

    func logoutBoth() async {
        let _ = await standardInstance.user()?.logout()
        let _ = await transactionInstance.user()?.logout()
    }

    func refreshTransactionToken() async {
        let _ = await transactionInstance.user()?.refresh()
    }
}
```

### Example 2: Using a Map or Dictionary for named instances

This approach is useful when you have a fixed set of authentication contexts. For example, you might have "standard", "transactions", and "admin" contexts.

* Android

* iOS

Using a Map for named instances on Android

```kotlin
class AuthManager {
    // Switch "Journey" to "DaVinci" when using DaVinci
    private val instances = mutableMapOf<String, Journey>()

    init {
        // Switch "Journey" to "DaVinci" when using DaVinci
        instances["standard"] = Journey { /* standard config */ }
        instances["transactions"] = Journey { /* transactions config */ }
        instances["admin"] = Journey { /* admin config */ }
    }

    // Logout all instances
    suspend fun logoutAll() {
        instances.values.forEach { instance ->
            instance.user()?.logout()
        }
    }

    // Refresh a specific token
    suspend fun refreshToken(instanceName: String) {
        instances[instanceName]?.user()?.refresh()
    }

    fun getInstance(name: String) = instances[name]
}
```

Using a Dictionary for named instances on iOS

```swift
import PingJourney

class AuthManager {
    // Switch "Journey" to "DaVinci" when using DaVinci
    private var instances: [String: Journey] = [:]

    init() {
        // Switch "Journey.createJourney" to "DaVinci.createDaVinci" when using DaVinci
        instances["standard"] = Journey.createJourney { /* standard config */ }
        instances["transactions"] = Journey.createJourney { /* transactions config */ }
        instances["admin"] = Journey.createJourney { /* admin config */ }
    }

    // Logout all instances
    func logoutAll() async {
        for instance in instances.values {
            let _ = await instance.user()?.logout()
        }
    }

    // Refresh a specific token
    func refreshToken(instanceName: String) async {
        let _ = await instances[instanceName]?.user()?.refresh()
    }

    func getInstance(name: String) -> Journey? {
        return instances[name]
    }
}
```

### Example 3: Using a List or Array for multiple user accounts

This approach is ideal for scenarios where the number of users is dynamic.

* Android

* iOS

Using a List for multiple user accounts on Android

```kotlin
class MultiUserManager {
    // Switch "DaVinci" to "Journey" when using PingOne Advanced Identity Cloud or AM
    private val userInstances = mutableListOf<DaVinci>()

    fun addUser(userId: String): DaVinci {
        val instance = DaVinci {
            // Fully isolated storage configuration
            // Switch "Cookie" to "Session" when when using PingOne Advanced Identity Cloud or AM
            module(Cookie) { storage { fileName = "user_${userId}_session" } }
            module(Oidc) { storage { fileName = "user_${userId}_token" } }
        }
        userInstances.add(instance)
        return instance
    }

    suspend fun logoutAllUsers() {
        userInstances.forEach { it.user()?.logout() }
        userInstances.clear()
    }
}
```

Using a mutable array for multiple user accounts on iOS

```swift
import PingDavinci
import PingStorage

class MultiUserManager {
    // Switch "DaVinci" to "Journey" when using PingOne Advanced Identity Cloud or AM
    private var userInstances: [DaVinci] = []

    func addUser(userId: String) -> DaVinci {
        let instance = DaVinci.createDaVinci { config in
            // Fully isolated storage configuration
            // Switch "CookieModule.self" to "SessionModule.self" when using PingOne Advanced Identity Cloud or AM
            config.module(CookieModule.self) { cookieConfig in
                cookieConfig.storage = KeychainStorage<SSOToken>(account: "user_\(userId)_session")
            }
            config.module(OidcModule.self) { oidcConfig in
                oidcConfig.storage = KeychainStorage<Token>(account: "user_\(userId)_token")
            }
        }
        userInstances.append(instance)
        return instance
    }

    func logoutAllUsers() async {
        for instance in userInstances {
            let _ = await instance.user()?.logout()
        }
        userInstances.removeAll()
    }
}
```