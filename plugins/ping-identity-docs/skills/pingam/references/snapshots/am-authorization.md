---
title: Authorization
description: Learn authorization concepts, implementation procedures, and customization techniques for PingAM authorization features
component: pingam
version: 8.1
page_id: pingam:am-authorization:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policies"]
page_aliases: ["index.adoc", "authorization-guide:preface.adoc"]
---

# Authorization

This guide covers concepts, implementation procedures, and customization techniques for working with the authorization features of PingAM.

[icon: book, set=fad, size=3x]

#### [Authorization](what-is-authz-decision.html)

Learn how AM determines access according to policies.

[icon: paste, set=fad, size=3x]

#### [Create policies](policies.html)

Define resources, and protect them by creating authorization policies.

[icon: handshake, set=fad, size=3x]

#### [What is transactional authorization?](transactional-authorization.html)

Use transactional authorization to require additional authorization.

[icon: edit, set=fad, size=3x]

#### [Dynamic OAuth 2.0 Scopes](oauth2-authorization.html)

Learn how to grant OAuth 2.0 scopes dynamically.

---

---
title: Authorization and policy decisions
description: Understand how PingAM uses policies and authorization decisions to grant or deny access to resources through policy decision points, enforcement points, and administration points
component: pingam
version: 8.1
page_id: pingam:am-authorization:what-is-authz-decision
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/what-is-authz-decision.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource", "Evaluation", "Agents"]
page_aliases: ["authorization-guide:what-is-authz-decision.adoc"]
section_ids:
  protecting-resources-with-policy: Protect resources
  policy-resolution: Policy decisions
  url-normalization: URL normalization
  tune-policy-evaluation: Tune policy evaluation
---

# Authorization and policy decisions

AM provides *access management*, which consists of:

* Authentication: determining who is trying to access a resource

* Authorization: determining whether to grant or deny access to the resource

The decision to grant access depends on a number of factors:

* the policies governing access

* who is trying to gain access

* possible additional conditions, such as whether the access needs to happen over a secure channel or what time of day it is.

AM relies on policies to reach authorization decisions, such as whether to grant or deny access to a resource, or to grant or deny OAuth 2.0 scopes.

Related information: [Dynamic OAuth 2.0 authorization](oauth2-authorization.html)

## Protect resources

When you configure policy sets to protect resources, AM acts as the *policy decision point* (PDP), whereas AM web and Java agents act as *policy enforcement points* (PEP). In other words, an agent or other PEP takes responsibility only for enforcing a policy decision rendered by AM. When you configured applications and their policies in AM, you used AM as a *policy administration point* (PAP).

Concretely speaking, when a PEP requests a policy decision from AM, it specifies the target resource(s), the policy set (default: `iPlanetAMWebAgentService`), and information about the subject and the environment. AM as the PDP retrieves policies within the specified policy set that apply to the target resource(s). AM then evaluates those policies to make a decision based on the conditions matching those of the subject and environment. When multiple policies apply for a particular resource, the default logic for combining decisions is that the first evaluation resulting in a decision to deny access takes precedence over all other evaluations. AM only allows access if all applicable policies evaluate to a decision to allow access.

AM communicates the policy decision to the PEP. The concrete decision, applying policy for a subject under the specified conditions, is called an *entitlement*.

The entitlement indicates the resource(s) it applies to, the actions permitted and denied for each resource, and optionally, response attributes and *advice*.

![Shows the relationship between realms, policies, and policy sets.](_images/realm-app-policy-overview.svg)Figure 1. Protecting pages or applications

When AM denies a request due to a failed condition, AM can send advice to the PEP, and the PEP can then take remedial action. For instance, suppose a user comes to a website after authenticating with an email address and password, which is configured as authentication level 0. Had the user authenticated using a one-time password, the user would have had authentication level 1 in their session. Yet, because they have authentication level 0, they currently cannot access the desired page, as the policy governing access requires authentication level 1. AM sends advice, prompting the PEP to have the user re-authenticate using a one-time password, gaining authentication level 1, and thus having AM grant access to the protected page.

## Policy decisions

AM has to match policies to resources to take policy decisions. For a policy to match, the resource has to match one of the resource patterns defined in the policy. The user making the request has to match a subject. Furthermore, at least one condition for each condition type has to be satisfied.

If more than one policy matches, AM has to reconcile differences. When multiple policies match, the order in which AM uses them to make a policy decision is not deterministic. However, a deny decision overrides an allow decision and so, by default, once AM reaches a deny decision, it stops checking further policies. If you want AM to continue checking despite the deny decision, go to Configure > Global Services > Policy Configuration, and enable Continue Evaluation on Deny Decision.

> **Collapse: Example**
>
> Consider the case where AM protects a user profile web page. An AM web agent installed in the web server intercepts client requests to enforce policy. The policy says that only authenticated users can access the page to view and to update their profiles.
>
> When a user browses to the profile page, the AM agent intercepts the request. The web agent notices that the request is to access a protected resource, but the request is coming from a user who has not yet logged in and consequently has no authorization to visit the page. The web agent therefore redirects the user's browser to AM to authenticate.
>
> AM receives the redirected user, serving a login page that collects the user's email and password. With the email and password credentials, AM authenticates the user, and creates a session for the user. AM then redirects the user to the web agent, which gets the policy decision from AM for the page to access, and grants access to the page.
>
> While the user has a valid session with AM, the user can go away to another page in the browser, come back to the profile page, and gain access without having to enter their email and password again.
>
> Notice how AM and the web agent handle the access in the example. The website developer can offer a profile page, but the website developer never has to manage login, or handle who can access a page. As AM administrator, you can change authentication and authorization independently of updates to the website. You might need to agree with website developers on how AM identifies users, so web developers can identify users by their own names when they log in. By using AM and web or Java agents for authentication and authorization, your organization no longer needs to update web applications when you want to add external access to your Intranet for roaming users, open some of your sites to partners, only let managers access certain pages of your HR website, or allow users already logged in to their desktops to visit protected sites without having to type their credentials again.

### URL normalization

Before AM matches a resource URL against a policy pattern, it normalizes the URL:

* Path traversals are resolved:

  `http://example.com/a/../b` is resolved to `http://example.com/b`.

  `http://example.com/a/./b` is resolved to `http://example.com/a/b`.

* If no port is specified, the default port for the scheme is added:

  `http://example.com/path` is treated as `http://example.com:80/path`.

  `https://example.com/path` is treated as `https://example.com:443/path`.

* Query string parameters are sorted alphabetically by parameter name:

  `?subject=SPBnfm+t5PlP+ISyQhVlplE22A8=&action=get` and `?action=get&subject=SPBnfm+t5PlP+ISyQhVlplE22A8=` are equivalent.

## Tune policy evaluation

Every time a policy is evaluated, AM reads the policy definition from disk. When policies are evaluated very frequently, for example thousands of evaluations per second, this can place a severe load on the server.

Storing policy definitions in cache memory can result in improved performance for policy evaluation.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following caveats apply to using the policy cache:- The size of the policy cache is limited by the available server memory.

- When a policy definition is loaded into the policy cache, policy evaluations are based on the cached definition. If you change or delete a policy definition, evaluation continues to be based on the cached definition until either the maximum cache duration is reached or you restart AM.

- In general, setting a cache duration of 1-3 seconds provides a notable performance improvement.

- Be cautious of setting a large cache size or a long cache duration:

  * This can result in unexpected behavior for policy changes made during the maximum cache duration and might have security implications if the policy change involves restricting or refining access to a resource.

  * If the server hosting your policy store becomes unavailable, there is a risk that the downtime might not be noticed until the policy cache expires. This means that connection issues might be observed only much later than the triggering event and could make future debugging of policy store availability more complex.

- Make any administrators responsible for policies in your deployment aware of the impact of using the policy cache in their environment. |

To use the policy cache, tune the following advanced server settings:

* [am.authorization.policy.cache.expirationDurationSeconds](../setup/deployment-configuration-reference.html#am.authorization.policy.cache.expirationDurationSeconds)

* [am.authorization.policy.cache.maxSize](../setup/deployment-configuration-reference.html#am.authorization.policy.cache.maxSize)

* [am.authorization.policySet.cache.expirationDurationSeconds](../setup/deployment-configuration-reference.html#am.authorization.policySet.cache.expirationDurationSeconds)

* [am.authorization.policySet.cache.maxSize](../setup/deployment-configuration-reference.html#am.authorization.policySet.cache.maxSize)

---

---
title: Customize policy evaluation with a plugin
description: Extend PingAM policy evaluation with custom plug-ins to implement custom subject conditions, environment conditions, and resource attributes for specialized authorization requirements
component: pingam
version: 8.1
page_id: pingam:am-authorization:customizing-authz-plugin
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/customizing-authz-plugin.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Customization", "Policy"]
page_aliases: ["authorization-guide:customizing-authz-plugin.adoc"]
section_ids:
  about-sample-policy-plugins: Sample plugin
  build-a-sample-plugin: Build the sample plugin
  add-custom-policy-impl-to-existing-apps: Add a custom policy to an existing policy set
  trying-sample-policy-plugin: Try the sample subject and environment conditions
  trying-custom-policy-resource-attributes: Try the sample resource attributes
---

# Customize policy evaluation with a plugin

AM policies let you restrict access to resources based both on identity and group membership, and also on a range of conditions including:

* session age

* authentication tree used

* authentication level

* realm

* session properties

* IP address and DNS name

* user profile content

* resource environment

* date

* day

* time of day

* time zone

However, some deployments require further distinctions for policy evaluation. This section explains how to customize policy evaluation for deployments with particular requirements that aren't met by built-in AM functionality.

This page shows how to build and use a custom policy plugin that implements a custom subject condition, a custom environment condition, and a custom resource attribute.

## Sample plugin

The AM policy framework lets you build plugins that extend subject conditions, environment conditions, and resource attributes.

Learn about downloading and building PingAM sample source code in the following *Knowledge Base* article: [How do I access and build the sample code provided for PingAM?](https://support.pingidentity.com/s/article/How-do-I-access-and-build-the-sample-code-provided-for-PingAM).

Get a local clone so that you can try the sample on your system. You'll find the relevant files in the `/path/to/openam-samples/policy-evaluation-plugin` directory.

> **Collapse: Files in the sample**
>
> * `pom.xml`
>
>   Apache Maven project file for the module.
>
>   This file specifies how to build the sample policy evaluation plugin, and also specifies its dependencies on AM components.
>
> * `src/main/java/org/forgerock/openam/examples/SampleAttributeType.java`
>
>   Extends the `com.sun.identity.entitlement.ResourceAttribute` interface, and shows an implementation of a resource attribute provider to send an attribute with the response.
>
> * `src/main/java/org/forgerock/openam/examples/SampleConditionType.java`
>
>   Extends the `com.sun.identity.entitlement.EntitlementCondition` interface, and shows an implementation of a condition that is the length of the username.
>
>   A condition influences whether the policy applies for a given access request. If the condition is fulfilled, then AM includes the policy in the set of policies to evaluate in order to respond to a policy decision request.
>
> * `src/main/java/org/forgerock/openam/examples/SampleSubjectType.java`
>
>   Extends the `com.sun.identity.entitlement.EntitlementSubject` interface and shows an implementation that defines a user to whom the policy applies.
>
>   A subject, like a condition, influences whether the policy applies. If the subject matches in the context of a given access request, then the policy applies.
>
> * `src/main/java/org/forgerock/openam/examples/SampleEntitlementModule.java`
>
>   These files serve to register the plugin with AM.
>
>   The Java class, `SampleEntitlementModule`, implements the `org.forgerock.openam.entitlement.EntitlementModule` interface. In the sample, this class registers `SampleAttribute`, `SampleCondition`, and `SampleSubject`.
>
>   The services file, `org.forgerock.openam.entitlement.EntitlementModule` , holds the fully qualified class name of the `EntitlementModule` that registers the custom implementations. In this case, `org.forgerock.openam.entitlement.EntitlementModule`.
>
>   You can find an explanation of service loading in the [ServiceLoader](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ServiceLoader.html) API specification.

## Build the sample plugin

1. If you haven't already done so, download and build the samples.

   Learn about downloading and building PingAM sample source code in the following *Knowledge Base* article: [How do I access and build the sample code provided for PingAM?](https://support.pingidentity.com/s/article/How-do-I-access-and-build-the-sample-code-provided-for-PingAM).

2. When the build is complete, copy the `policy-evaluation-plugin-8.1.1.jar` file to the `WEB-INF/lib` directory where you deployed AM:

   ```bash
   $ cp target/*.jar /path/to/tomcat/webapps/am/WEB-INF/lib/
   ```

3. Update the user UI to include the custom subject and environment conditions.

   Learn more in [UI customization](../ui-customization/preface.html):

   * Locate the line that contains the following text:

     ```
     "subjectTypes": {
     ```

   * Insert the following text after the line you located in the previous step:

     ```
     "SampleSubject": {
         "title": "Sample Subject",
         "props": {
             "name": "Name"
         }
     },
     ```

   * Locate the line that contains the following text:

     ```
     "conditionTypes": {
     ```

   * Insert the following text after the line you located in the previous step:

     ```
     "SampleCondition": {
         "title": "Sample Condition",
         "props": {
             "nameLength": "Minimum username length"
         }
     },
     ```

4. If your UI supports multiple locales, change the `translation.json` files for those locales, as needed.

5. Restart AM or the container in which it runs.

## Add a custom policy to an existing policy set

To use your custom policy in an existing policy set, you must update the policy set.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't update a policy set that already has policies configured. If policies are configured for a policy set, you must first delete the policies, then update the policy set. |

Update the `iPlanetAMWebAgentService` policy set in the top level realm of a fresh installation.

1. Authenticate to AM as the `amAdmin` user:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: amadmin" \
   --header "X-OpenAM-Password: password" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"AQIC5wM…​TU3OQ*",
       "successUrl":"/am/console",
       "realm":"/alpha"
   }
   ```

2. Update the `iPlanetAMWebAgentService` policy set by adding the `SampleSubject` subject condition and the `SampleCondition` environment condition:

   ```bash
   $ curl \
   --request PUT \
   --header "iPlanetDirectoryPro: AQIC5wM2…​" \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=1.0" \
   --data '{
   "name": "iPlanetAMWebAgentService",
   "conditions": [
       "LEAuthLevel",
       "Script",
       "AuthenticateToService",
       "SimpleTime",
       "AMIdentityMembership",
       "OR",
       "IPv6",
       "IPv4",
       "SessionProperty",
       "AuthScheme",
       "AuthLevel",
       "NOT",
       "AuthenticateToRealm",
       "AND",
       "ResourceEnvIP",
       "LDAPFilter",
       "OAuth2Scope",
       "Session",
       "SampleCondition"
   ],
   "subjects": [
       "NOT",
       "OR",
       "JwtClaim",
       "AuthenticatedUsers",
       "AND",
       "Identity",
       "NONE",
       "SampleSubject"
   ],
   "applicationType": "iPlanetAMWebAgentService",
   "entitlementCombiner": "DenyOverride"
   }' "https://am.example.com:8443/am/json/realms/root/realms/alpha/applications/iPlanetAMWebAgentService"
   ```

## Try the sample subject and environment conditions

In the AM admin UI, add a policy to the `iPlanetAMWebAgentService` policy set in the top level realm that allows HTTP GET access for URLs based on the template `http://www.example.com:80/*`, and uses the custom subject and environment conditions.

1. Create the policy with the following properties:

   **Sample Policy Properties**

   | Property               | Value                                                                                                                                                                                      |
   | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Name                   | `Sample Policy`                                                                                                                                                                            |
   | Resource Type          | `URL`                                                                                                                                                                                      |
   | Resources              | Use the `*://*:*/*` resource template to specify the resource `http://www.example.com:80/*`.                                                                                               |
   | Actions                | Allow `GET`                                                                                                                                                                                |
   | Subject Conditions     | Add a subject condition of type `Sample Subject` and a name of `bjensen` so that `bjensen` is the only user who can access the resource.                                                   |
   | Environment Conditions | Add an environment condition of type `Sample Condition` and a minimum username length of `4` so that only users with a username length of four or more characters can access the resource. |

2. With the policy in place, authenticate both as a user who can request policy decisions and as a user trying to access a resource.

   Both of these calls return `tokenId` values for use in the policy decision request.

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: amadmin" \
   --header "X-OpenAM-Password: password" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"AQIC5wM…​TU3OQ*",
       "successUrl":"/am/console",
       "realm":"/alpha"
   }
   ```

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: bjensen" \
   --header "X-OpenAM-Password: Ch4ng31t" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"AQIC5wM…​TU3OQ*",
       "successUrl":"/am/console",
       "realm":"/alpha"
   }
   ```

3. Use the administrator `tokenId` as the header of the policy decision request, and the user `tokenId` as the subject `ssoToken` value.

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=2.1" \
   --header "iPlanetDirectoryPro: AQIC5wM2LY4Sfcw…​" \
   --data '{
       "subject":{
           "ssoToken":"AQIC5wM2LY4Sfcy…​"
       },
       "resources":[
           "http://www.example.com:80/index.html"
       ],
       "application":"iPlanetAMWebAgentService"
   }' \
   "https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_action=evaluate"
   {
      "resource": "http://www.example.com:80/index.html",
      "actions": {
          "GET": true
      },
      "attributes": {},
      "advices": {}
   }
   ```

   Notice that the actions returned from the policy evaluation call are set in accordance with the policy.

## Try the sample resource attributes

The sample custom policy plugin can have AM return an attribute with the policy decision. In order to make this work, list the resource type for the `URL` resource type to obtain its UUID, and then update your policy to return a `test` attribute:

```bash
$ curl \
--request GET \
--header "iPlanetDirectoryPro: AQIC5wM2…​" \
--header "Accept-API-Version: resource=1.0" \
"https://am.example.com:8443/am/json/realms/root/resourcetypes?_queryFilter=name%20eq%20%22URL%22"
{
    "result":[
        {
            "uuid":"URL-resource-type-UUID",
            "name":"URL",
            "description":"The built-in URL Resource Type available policies.",
            "patterns":["://:*/","://:/?"],
            …​
        }
    ],
    "resultCount":1,
    "pagedResultsCookie":null,
    "totalPagedResultsPolicy":"NONE",
    "totalPagedResults":-1,f
    "remainingPagedResults":0
}
```

When you now request the same policy decision as before, AM returns the `test` attribute that you configured in the policy.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.1" \
--header "iPlanetDirectoryPro: AQIC5wM2LY4Sfcw…​" \
--data '{
    "subject":{
        "ssoToken":"AQIC5wM2LY4Sfcy…​"
    },
    "resources":[
        "http://www.example.com:80/index.html"
    ],
    "application":"iPlanetAMWebAgentService"
}' \
"https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_action=evaluate"
{
    "resource": "http://www.example.com/profile",
    "actions": {
        "GET": true
    },
    "attributes": {
    "test": [
        "sample"
     ]
},
"advices": {}
}
```

---

---
title: Dynamic OAuth 2.0 authorization
description: Configure PingAM to grant OAuth 2.0 scopes dynamically using policies that evaluate scope requests at runtime based on user context and conditions
component: pingam
version: 8.1
page_id: pingam:am-authorization:oauth2-authorization
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/oauth2-authorization.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "OAuth 2.0", "Scope", "Policy"]
page_aliases: ["authorization-guide:oauth2-authorization.adoc"]
section_ids:
  example_use_case: Example use case
  how_it_works: How it works
  validate_oauth_2_0_scope_policies: Validate OAuth 2.0 scope policies
  prepare_a_demonstration: Prepare a demonstration
  oauth2-authz-oauth2-provider: OAuth 2.0 provider
  oauth2-authz-scope-policy: OAuth 2.0 scope policy
  oauth2-authz-client: OAuth 2.0 client
  oauth2-authz-resource-owner: Resource owner
  test_the_demonstration: Test the demonstration
  non_interactive: Non-interactive
  interactive: Interactive
  implied_consent: Implied consent
---

# Dynamic OAuth 2.0 authorization

AM can grant OAuth 2.0 scopes statically or dynamically:

* Static scopes (default)

  OAuth 2.0 client configurations specify the allowed and, optionally, default scopes.

  When the client requests allowed scopes and the resource owner consents to grant the client access, AM issues the token with the scopes requested.

  When different users use the same client that requests scopes `A` and `B`, the access token always includes scopes `A` and `B`.

* Dynamic scopes

  OAuth 2.0 client configurations specify the allowed and, optionally, default scopes.

  1. You configure AM policies for OAuth 2.0 scope decisions.

  2. You configure the client or the OAuth 2.0 provider service to use the AM policy engine for scope decisions.

  AM checks each scope against the applicable OAuth 2.0 scope policies. AM grants or denies access to scopes dynamically at runtime.

  When different users use the same client that requests scopes `A` and `B`, the access token scopes can differ.

## Example use case

A company supports custom OAuth 2.0 clients for internal applications. The use of the internal applications is bound by the terms and conditions in the contracts of those who work for the company. The terms and conditions grant the internal applications access to profile information the company maintains. It would be redundant to prompt employees and contractors for consent to access their profile information.

The AM administrator creates policies to grant the `profile` scope for all internal client tokens.

## How it works

![How policies determine whether to grant or deny an OAuth 2.0 scope](_images/oauth2-realm-app-policy-overview.svg)Figure 1. Policies for dynamic scopes

AM processes consent based on the policy decision:

* If a policy grants access to a scope (`GRANT=true`), consent is automatic.

  AM does not prompt the user to grant access.

* If a policy denies access to a scope (`GRANT=false`), AM omits the scope from any resulting token.

  AM does not prompt the user to grant access.

* If no policy grants or denies access, then the result depends on the flow.

  When the flow is interactive as in authorization or device code flows, AM prompts the user to grant access or uses the saved consent state if available.

  If the flow is not interactive as in resource owner password or client credentials flows, AM omits the scope from any resulting token.

  For details about which flows are interactive, refer to the examples in [OAuth 2.0 grant flows](../am-oauth2/oauth2-implementing-flows.html) and [OpenID Connect grant flows](../am-oidc1/oidc-implementing-flows.html).

The default scopes behavior doesn't change for dynamic authorization. AM only evaluates default scopes from the OAuth 2.0 client profile when the client doesn't request a scope. AM follows the same rules to deduce consent for both default and requested scopes.

When issuing refresh tokens, AM issues the same scopes as for the access token, unless a policy explicitly denies one of the scopes.

## Validate OAuth 2.0 scope policies

Writing policies for OAuth 2.0 might not be straightforward if your environment requires complex conditions. The easiest way to validate OAuth 2.0 policies is to configure a client to use the policies and request some tokens.

## Prepare a demonstration

Start by preparing the demonstration:

1. [Configure the OAuth 2.0 provider](#oauth2-authz-oauth2-provider).

2. [Create a sample policy](#oauth2-authz-scope-policy).

3. [Create an OAuth 2.0 client](#oauth2-authz-client).

4. [Create a resource owner account](#oauth2-authz-resource-owner).

### OAuth 2.0 provider

Configure the OAuth 2.0 provider service to use the AM policy engine for scope decisions: Configure the OAuth 2.0 provider service to use the AM policy engine for scope decisions: . In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider. . Enable Use Policy Engine for Scope decisions.

### OAuth 2.0 scope policy

The sample scope policy denies access to the `email` scope.

1. In the AM admin UI, go to Realms > *realm name* > Authorization > Policy Sets and select Default OAuth2 Scopes Policy Set to edit the policy set.

   This is the `oauth2Scopes` policy.

2. Click + Add a Policy, use the following settings, and create the policy:

   * Name

     `Dynamic OAuth 2.0 Scopes`

   * Resource Type

     `OAuth2 Scope`

   * Resources

     Select `*` as the pattern and add `email` as the scope.

3. Click the Actions tab, set `GRANT` to `Deny`, and save your changes.

4. Click the Subjects tab, set the subject type to `Authenticated Users`, and save your changes.

The resulting policy reflects your work:

![OAuth 2.0 policy denying the email scope for all authenticated users](_images/oauth2-scope-policy.png)Figure 2. OAuth 2.0 scopes policy

### OAuth 2.0 client

The OAuth 2.0 client profile in this example overrides the AM OAuth 2.0 provider settings. This lets you test the scope policy without affecting other clients.

1. Create a confidential OAuth 2.0 client account.

   In the AM admin UI, select Realms > *realm name* > Applications > OAuth 2.0 > Clients > + Add Client, and create a new confidential client with the following settings:

   * Client ID: `myClient`

   * Client Secret: `mySecret`

   * Redirection URIs: `https://www.example.com:443/callback`

   * Scopes:\
     `openid`\
     `profile`\
     `email`

2. Add the following settings in the client profile and save your work:

   1. On the Core tab, set Client Name to `Dynamic scopes client`.

   2. On the Advanced tab, add the following Grant Types:\
      `Authorization Code`\
      `Client Credentials`\
      `Implicit`\
      `Refresh Token`\
      `Resource Owner Password Credentials`

3. Override the OAuth 2.0 provider settings for this client.

   On the OAuth2 Provider Overrides tab, update the following settings and save your work:

   * Enable OAuth2 Provider Overrides: Enabled

   * Use Policy Engine for Scope decisions: Enabled

   * Scopes Policy Set: `oauth2Scopes`

### Resource owner

Create the OAuth 2.0 resource owner account:

1. In the AM admin UI, select Identities > + Add Identity and complete the required fields. For example:

   1. Username: `bjensen`

   2. Password: `Ch4ng31t`

   3. Email address: `bjensen@example.com`

2. Record the username and password.

## Test the demonstration

Test the feature with non-interactive and interactive flows.

The sample policy denies the `email` scope for all authenticated users. The `profile` scope has no policy — it's a *no-policy-match* case. The tests show how AM handles each case depending on the flow type.

### Non-interactive

This test uses the [resource owner password credentials](../am-oauth2/oauth2-ropc-grant.html) (ROPC) flow:

* The OAuth 2.0 client credentials are `myClient:mySecret`.

* The resource owner credentials are the username and password you recorded: `bjensen:Ch4ng31t`.

* The requested scopes are `openid`, `profile`, and `email`.

```bash
$ curl \
--request POST \
--user 'myClient:mySecret' \
--data 'scope=openid profile email' \
--data 'grant_type=password' \
--data 'username=bjensen' \
--data 'password=Ch4ng31t' \
"https://am.example.com:8443/am/oauth2/realms/root/realms/realm name/access_token"
{
  "access_token": "…​",
  "refresh_token": "…​",
  "scope": "openid",
  "id_token": "…​",
  "token_type": "Bearer",
  "expires_in": 3599
}
```

Notice the access token has `"scope": "openid"`. AM removed both `email` and `profile` from the scopes:

* `email`: a policy explicitly denies it (`GRANT=false`), so AM omits it.

* `profile`: no policy matches this scope, so AM also omits it.

In non-interactive flows, AM treats no-policy-match scopes the same as explicitly denied scopes.

### Interactive

This test uses the [implicit](../am-oauth2/oauth2-implicit-grant.html) flow. It stops after demonstrating the user consent phase of the process.

1. In a web browser, go to the `/authorize` endpoint to initiate the implicit flow.

   ```none
   https://am.example.com:8443/am/authorize?scope=openid+profile+email&response_type=id_token&client_id=myClient&nonce=123&state=456&redirect_uri=https://www.example.com:443/callback
   ```

2. Sign in with the resource owner's credentials.

3. Observe the prompt for consent that doesn't include the `email` scope:

   ![AM prompts for consent to access the profile scope.](_images/oauth2-example-oidc.png)Figure 3. Consent for the profile scope

The consent page shows `profile` but not `email`:

* `email`: the policy explicitly denies it (`GRANT=false`), so AM omits it from the consent page entirely.

* `profile`: no policy matches this scope, so AM presents it for the user to grant or deny.

In interactive flows, AM doesn't treat no-policy-match scopes the same as explicitly denied scopes. Instead, it presents them for user consent.

|   |                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To explicitly deny a scope in interactive flows, you must create a policy that sets `GRANT` to `Deny` for that scope and the relevant condition. Without an explicit deny policy, a scope that fails a policy condition (for example, a user who doesn't meet a group membership requirement) is still presented for consent rather than denied outright. |

### Implied consent

If you enable Implied consent on the client, AM auto-grants no-policy-match scopes, in both interactive and non-interactive flows.

---

---
title: Export to XACML
description: Export PingAM policies and policy sets to XACML 3.0 format using the admin UI or REST API with optional search filters
component: pingam
version: 8.1
page_id: pingam:am-authorization:xacml-export
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/xacml-export.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Administration", "XACML"]
page_aliases: ["authorization-guide:xacml-export.adoc"]
section_ids:
  export-policy-to-xacml-xui: Export policies in XACML format (UI)
  export-policies: Export policies in XACML format (REST)
  export-policies-search-filter: Export policies in XACML format with search filters (REST)
---

# Export to XACML

AM only exports a policy set that contains policy definitions. No other types can be included in the policy set, such as sub-policy sets or rules.

> **Collapse: Policy sets to XACML mappings**
>
> | AM                                           | XACML                         |
> | -------------------------------------------- | ----------------------------- |
> | Realm:\<timestamp> (yyyy.MM.dd.HH.mm.ss.SSS) | PolicySet ID                  |
> | Current Time (yyyy.MM.dd.HH.mm.ss.SSS)       | Version                       |
> | Deny Overrides                               | Policy Combining Algorithm ID |
> | No targets defined                           | Target                        |

When exporting AM policies to XACML 3.0 policy sets, AM maps its policies to XACML 3.0 policy elements.

> **Collapse: Policies to XACML mappings**
>
> | AM Policy                                                                                                                                                    | XACML Policy                        |
> | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
> | Policy Name                                                                                                                                                  | Policy ID                           |
> | Description                                                                                                                                                  | Description                         |
> | Current Time (yyyy.MM.dd.HH.mm.ss.SSS)                                                                                                                       | Version                             |
> | xacml rule target                                                                                                                                            | entitlement excluded resource names |
> | Rule Deny Overrides                                                                                                                                          | Rule Combining Algorithm ID         |
> | Any of:- Entitlement Subject
>
> - Resource Names
>
> - Policy Set Names
>
> - Action Values                                                                          | Target                              |
> | Any of:- Policy Set Name
>
> - Entitlement Name
>
> - Privilege Created By
>
> - Privilege Modified By
>
> - Privilege Creation Date
>
> - Privilege Last Modification Date | Variable Definitions                |
> | Single Level Permit/Deny Actions converted to Policy Rules                                                                                                   | Rules                               |
>
> |   |                                                                                                                                                              |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | XACML obligation is not supported. Also, only one XACML match is defined for each privilege action, and only one XACML rule for each privilege action value. |

## Export policies in XACML format (UI)

1. In the AM admin UI, go to Realms > *realm name* > Authorization > Policy Sets, and click Export Policy Sets.

   All policy sets, and the policies within will be exported in XACML format.

## Export policies in XACML format (REST)

The export service is accessible at the `/xacml/policies` endpoint using an HTTP GET request at the following endpoint for the root realm or a specific realm:

`https://am.example.com:8443/am/xacml/policies` `https://am.example.com:8443/am/xacml/realm/policies`

Here, *realm* is the name of a specific realm.

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can filter your XACML exports using query search filters. See [Export policies in XACML format with search filters (REST)](#export-policies-search-filter). |

1. Use the `/xacml/policies` endpoint to export the AM entitlement policies into XACML 3.0 format.

   The following curl command exports the policies and returns the XACML response (truncated for display purposes).

   ```bash
   $ curl \
   --request GET \
   --header "iPlanetDirectoryPro: AQIC5…​" \
   "https://am.example.com:8443/am/xacml/policies"
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
   <PolicySet xmlns="urn:oasis:names:tc:xacml:3.0:core:schema:wd-17"
    PolicyCombiningAlgId="urn:oasis:names:tc:xacml:3.0:rule-combining-algorithm:deny-overrides"
    Version="2014.10.08.21.59.39.231" PolicySetId="/:2014.10.08.21.59.39.231">
    <Target/>
    <Policy RuleCombiningAlgId="urn:oasis:names:tc:xacml:3.0:rule-combining-algorithm:deny-overrides"
     Version="2014.10.08.18.01.03.626"
     PolicyId="Rockshop_Checkout_https://forgerock-rockshop.openrock.org:443/wp-login.php*?*">
     …​
   ```

## Export policies in XACML format with search filters (REST)

Note the following points about the search filters:

* **LDAP-based searches**. The search filters follow the standard guidelines for LDAP searches as they are applied to the entitlements index in the LDAP configuration backend, located at: `ou=default,ou=OrganizationalConfig,ou=1.0,ou=sunEntitlementIndexes, ou=services,dc=am,dc=example,dc=com`.

* **Search filter format**. You can specify a single search filter or multiple filters in the HTTP URL parameters. The format for the search filter is as follows:

  ```
  [attribute name][operator][attribute value]
  ```

  If you specify multiple search filters, they are logically ANDed: the search results meet the criteria specified in all the search filters.

  > **Collapse: XACML export search filter format**
  >
  > | Element         | Description                                                                                                                                                                                                      |
  > | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  > | Attribute Name  | The name of the attribute to be searched for. The only permissible values are: `application` (keyword for policy set), `createdby`, `lastmodifiedby`, `creationdate`, `lastmodifieddate`, `name`, `description`. |
  > | Operator        | The type of comparison operation to perform.- = Equals (text)
  >
  > - < Less Than or Equal To (numerical)
  >
  > - > Greater Than or Equal To (numerical)                                                                   |
  > | Attribute Value | The matching value. Asterisk wildcards are supported.                                                                                                                                                            |

  1. Use the `/xacml/policies` endpoint to export the policies into XACML 3.0 format with a search filter.

     This command only exports policies that were created by "amadmin".

     ```bash
     $ curl \
     --request GET \
     --header "iPlanetDirectoryPro: AQIC5…​" \
     "https://am.example.com:8443/am/xacml/policies?filter=createdby=amadmin"
     ```

  2. You can also specify more than one search filter by logically ANDing the filters as follows:

     ```bash
     $ curl \
     --request GET \
     --header "iPlanetDirectoryPro: AQIC5…​" \
     "https://am.example.com:8443/am/xacml/policies?filter=createdby=amadmin&filter=creationdate=135563832"
     ```

---

---
title: Import and export policies
description: Back up, transfer, or version control PingAM policies by importing and exporting them in JSON or XACML 3.0 format
component: pingam
version: 8.1
page_id: pingam:am-authorization:import-export-policy
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/import-export-policy.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Administration", "Policy"]
page_aliases: ["authorization-guide:import-export-policy.adoc"]
---

# Import and export policies

You can import and export policies to and from files.

You can use these files to back up policies, transfer policies between AM instances, or store policy configuration in a version control system such as Git or Subversion.

AM supports exporting policies in JSON and [eXtensible Access Control Markup Language (XACML) Version 3.0](http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html) format.

**Comparison of policy import/export formats**

| Feature                                                                                      | Supported for JSON? | Supported for XACML? |
| -------------------------------------------------------------------------------------------- | ------------------- | -------------------- |
| Can be imported/exported from within the AM admin UI?                                        | No                  | Yes                  |
| Can be imported/exported using REST?                                                         | Yes                 | Yes                  |
| Exports policies?                                                                            | Yes                 | Yes                  |
| Exports policy sets?                                                                         | Yes                 | Partial(1)           |
| Exports resource types?                                                                      | Yes                 | Partial              |
| Creates an exact copy of the original policy sets, resource types, and policies upon import? | Yes                 | Partial(2)           |

(1) Only the details of policy sets and resource types that are actually used within a policy are exported to the XACML format. The full definition is not exported.

(2) Policy sets and resource types will be generated from the details in the XML, but may not match the definitions of the originals. For example, the names are auto-generated.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM can only import XACML 3.0 files that were either created by an AM instance, or that have had minor manual modifications, due to the reuse of some XACML 3.0 parameters for non-standard information. |

Importing and exporting JSON:

* Export

  You export policies in JSON format by sending a GET request to the `policies` endpoint. This is the same request as the one detailed in [read a policy](rest-api-authz-policies.html#rest-api-authz-policies-read).

* Import

  You import policies in JSON format by sending a POST request to the `policies` endpoint. This is the same request as the one detailed in [create a policy](rest-api-authz-policies.html#rest-api-authz-policies-create).

Importing and exporting XACML:

* [Export to XACML](xacml-export.html)

* [Import from XACML](xacml-import.html)

---

---
title: Import from XACML
description: Import XACML policies into PingAM using the UI or REST API, with optional dry-run testing to validate changes before saving to the database
component: pingam
version: 8.1
page_id: pingam:am-authorization:xacml-import
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/xacml-import.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Administration", "XACML"]
page_aliases: ["authorization-guide:xacml-import.adoc"]
section_ids:
  import-policy-in-xacml-xui: Import policies in XACML format (UI)
  procedure-xacml-import: Import policies in XACML format (REST)
---

# Import from XACML

To test an import, AM provides a dry run feature that runs an import without saving the changes to the database. The dry run feature provides a summary of the import so that you can troubleshoot any potential mismatches prior to the actual import.

## Import policies in XACML format (UI)

1. In the AM admin UI, go to Realms > *realm name* > Authorization > Policy Sets, and click Import Policy Sets.

2. Browse to the XACML format file, select it, and click Open.

   Any policy sets, and the policies within will be imported from the selected XACML format file.

   |   |                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Policy sets and resource types will be generated from the details in the XACML format file, but may not match the definitions of the originals, for example the names are auto-generated. |

## Import policies in XACML format (REST)

You can import a XACML policy using an HTTP POST request for the root realm or a specific realm at the following endpoints:

`https://am.example.com:8443/am/xacml/policies` `https://am.example.com:8443/am/xacml/realm/policies`

Here, *realm* is the name of a specific realm.

1. You can do a dry run using the `dryrun=true` query to test the import. The dry run option outputs in JSON format and displays the status of each import policy, where "U" indicates "Updated"; "A" for "Added". The dry run does not actually update to the database. When you are ready for an actual import, you need to re-run the command without the `dryrun=true` query.

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/xml" \
   --header "iPlanetDirectoryPro: AQIC5…​" \
   --data @xacml-policy.xml \
   "https://am.example.com:8443/am/xacml/policies?dryrun=true"
   [
       {
           "status":"A",
           "name":"aNewPolicy"
       },
       {
           "status":"U",
           "name":"anExistingPolicy"
       },
       {
           "status":"U",
           "name":"anotherExistingPolicy"
       }
   ]
   ```

2. Use the `/xacml/policies` endpoint to import a XACML policy:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/xml" \
   --header "iPlanetDirectoryPro: AQIC5…​" \
   --data @xacml-policy.xml \
   "https://am.example.com:8443/am/xacml/policies"
   ```

   |   |                                                                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can import a XACML policy into a realm as follows:```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/xml" \
   --header "iPlanetDirectoryPro: AQIC5…​" \
   --data @xacml-policy.xml \"
   "https://am.example.com:8443/am/xacml/realm/policies"
   ``` |

---

---
title: Policies
description: Define authorization policies in PingAM to control subject access to resources based on actions, subject conditions, environment conditions, and response attributes
component: pingam
version: 8.1
page_id: pingam:am-authorization:policies
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/policies.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy"]
page_aliases: ["authorization-guide:policies.adoc"]
---

# Policies

Authorization *policies* let AM determine whether to grant a subject access to a resource.

A policy defines the following:

* *resources*

  The resource to which access is restricted, such as a web page, a mobile app, or a boarding area in an airport.

* *actions*

  The verbs that describe what users can do to the resource, such as *read* a web page, *submit* a web form, or *access* a boarding area.

* *subject conditions*

  Who the policy applies to, such as all authenticated users, only administrators, or only passengers with valid tickets for planes leaving soon.

* *environment conditions*

  The circumstances under which the policy applies, such as only during work hours, only when accessing from a specific IP address, or only when the flight is scheduled to leave within the next four hours.

* *response attributes*

  Information that AM attaches to a response following a policy decision, such as a name, email address, or frequent flyer status.

|   |                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Policy conditions don't determine the outcome of the policy but determine whether a specific policy is applicable and whether its actions should contribute towards the overall policy decision. If a condition fails (due to authentication failure, for example), AM disregards the corresponding policy and assesses any other configured policies to make the authorization decision. |

---

---
title: Policies in the UI
description: Manage policies through the PingAM admin UI by creating them within policy sets, configuring resources and actions, and defining subject and environment conditions
component: pingam
version: 8.1
page_id: pingam:am-authorization:policies-ui
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/policies-ui.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Configuration"]
page_aliases: ["authorization-guide:policies-ui.adoc"]
section_ids:
  policy-names: Policy type names
  resources: Resources
  policy-actions: Policy actions
  conditions: Conditions
  subjects: Subjects
  environments: Environments
  response-attributes: Response attributes
  example: Example
---

# Policies in the UI

You manage policies through the AM admin UI. You can only create a policy as part of a [policy set](policy-sets.html).

To configure a policy, go to Realms > *realm name* > Authorization > Policy Sets and select the name of the policy set in which to configure the policy.

| To…​            | Action                                                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a policy | Click Add a Policy.When creating a policy, specify a [name](#policy-names), a [resource type](resource-types.html), and at least one [resource](#resources).Click Create. |
| Modify a policy | Click the policy name or the pencil icon ([icon: pencil-alt, set=fa]).                                                                                                    |
| Delete a policy | Click the delete icon ([icon: times, set=fa]) or click the policy name then x Delete.                                                                                     |

## Policy type names

Do not use any of the following characters in policy, policy set, or resource type names:\
\
Double quotes (`"`)\
Plus sign (`+`)\
Comma (`,`)\
Less than (`<`)\
Equals (`=`)\
Greater than (`>`)\
Backslash (`\`)\
Forward slash (`/`)\
Semicolon (`;`)\
Null (`\u0000`)

## Resources

To define resources that the policy applies to:

1. Click the Resources pencil icon ([icon: pencil-alt, set=fa]) or the Resources tab.

2. Select a resource type from the Resource Type list.

   The resource type determines which resource patterns are available. The `OAuth2 Scope` resource type contains the same resource patterns as the `URL` resource type, as well as the `*` pattern.

   Use the resource patterns that are most relevant for the scopes in your environment.

   Learn more about resource types in [Resource types](resource-types.html).

3. Select a resource pattern from the Resources drop-down list.

4. Replace the asterisks with values for matching resources, and click Add.

   Learn more about resource patterns in [Resource type patterns](resource-types-ui.html#policy-patterns-wildcards).

5. Optionally, click Add Resource to add more resource patterns, or click [icon: times, set=fa]to delete a resource pattern.

6. Save your changes.

## Policy actions

To define policy actions that allow or deny access to a resource:

1. Click the Actions pencil icon ([icon: pencil-alt, set=fa]) or the Actions tab.

2. Click Add an Action to select an action from the drop-down list.

3. Select whether to allow or deny the action on the resources.

4. Optionally, add further actions, or click ([icon: times, set=fa]) to delete actions.

5. Save your changes.

## Conditions

To define subject and environment conditions:

* Combine logical operators with blocks of configured parameters to create a rule set. The policy uses this rule set to filter requests for resources.

* Use drag and drop to nest logical operators at multiple levels to create complex rule sets.

  ![Nested subject conditions](_images/policy-subjects.png)

* A gray horizontal bar indicates a valid point to drop a block.

  ![Drop blocks into drop points, which are shown as a gray horizontal band.](_images/policy-editor-valid-drop-points.png)

### Subjects

To define the subject conditions the policy applies to:

1. Click Add a Subject Condition, choose the [type](#subject-types) from the drop-down menu, and provide any required subject values.

2. When complete, click the check icon ([icon: check, set=fa]) and drag the block into a valid drop point in the rule set.

3. To add a logical operator, click Add a Logical Operator, choose between `All Of`, `Not`, and `Any Of` from the drop-down list, and drag the block into a valid drop point in the rule set.

4. To edit a condition, click the edit icon ([icon: pencil-alt, set=fa]), or click ([icon: times, set=fa]) to delete.

5. Continue combining logical operators and subject conditions and click Save Changes when you've finished.

| Subject condition types  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Authenticated Users      | Any user that has successfully authenticated with AM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Users & Groups           | Search for and select one or more users or groups that are defined in AM admin UI under the Realms > *realm name* > Identities or the Groups tab.                                                                                                                                                                                                                                                                                                                                                                              |
| OpenID Connect/Jwt Claim | Validate a claim within a JSON Web Token (JWT).Type the name of the claim to validate in the Claim Name field, for example, `sub`, and the required value in the Claim Value field, and click the check icon ([icon: check, set=fa]).Repeat the step to enter additional claims.The claim(s) will be part of the JWT payload together with the JWT header and signature. The JWT is sent in the authorization header of the bearer token.This condition type only supports string equality comparisons, and is case-sensitive. |
| Never Match              | Never match any subject. This disables the policy.If you do not set a subject condition, `Never Match` is the default. In other words, you must set a subject condition for the policy to apply.To match regardless of the subject, configure a `Never Match` subject condition inside a logical `Not` block.                                                                                                                                                                                                                  |

### Environments

To define the environment conditions the policy applies to:

1. Click Add an Environment Condition, select an environment condition type from the Type list, and provide any required values.

   The fields differ, according to the type you've selected. Learn more in [Environment condition types](#environment-types).

   |   |                                                                              |
   | - | ---------------------------------------------------------------------------- |
   |   | `Script` is the only environment condition available for OAuth 2.0 policies. |

2. When complete, click the check icon ([icon: check, set=fa]) button and drag the block into a valid drop point in the rule set.

3. To add a logical operator, click Add a Logical Operator, choose between `All Of`, `Not`, and `Any Of` from the drop-down list, and drag the block into a valid drop point in the rule set.

4. To edit a condition, click the edit icon ([icon: pencil-alt, set=fa]), or click ([icon: times, set=fa]) to delete.

5. Continue combining logical operators and subject conditions and click Save Changes when you've finished.

**Environment condition types**

| Environment condition type                      | Description                                                                                                                                                                                                                                                                                                             | Additional fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Active Session Time                             | Set a condition for the maximum duration the authenticated session has been active.                                                                                                                                                                                                                                     | * `Max Session Time`: Set the period the session can be active, in seconds.

* `Terminate Session`: Set to `True` if the session must end when it reaches the `Max Session Time`. If set to `True`, the user will need to reauthenticate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Authentication Level (greater than or equal to) | The policy tests the required authentication level.                                                                                                                                                                                                                                                                     | - `Authentication level`: Set the minimum acceptable authentication level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Authentication Level (less than or equal to)    | The policy tests the required authentication level.                                                                                                                                                                                                                                                                     | * `Authentication level`: Set the maximum acceptable authentication level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Authentication by Module Instance               | *Deprecated*.This property was used only for authentication with modules and chains and is no longer documented.For existing policies, this condition type evaluates to `false`, unless you've temporarily re-enabled modules and chains.You should remove this condition type from all policies as soon as convenient. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Authentication by Service                       | The policy tests the authentication journey used.                                                                                                                                                                                                                                                                       | `Authenticate To Service`: Set the journey through which the user must authenticate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Authentication to a Realm                       | The policy evaluates the realm to which the user authenticated. A session can belong to only one realm. Session upgrade between realms is not allowed.                                                                                                                                                                  | `Authenticate to a realm`: Set the realm to which the user must authenticate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Current Session Properties                      | The policy evaluates property values set in the authenticated session.                                                                                                                                                                                                                                                  | - `Ignore Value Case`: Set to `True` to make the test case-insensitive.

- `Properties`: Set the properties you want to evaluate using the format `property:value`. For example, use `clientType:genericHTML` to test whether the value of the `clientType` property is equal to `genericHTML`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| IDM User                                        | Lets you query an IDM resource to form the basis of the policy evaluation. AM must be part of a Ping Advanced Identity Software deployment to use this environment condition.                                                                                                                                           | * `Identity Resource`: The identity resource to query, for example, `managed/user`.

* `Query Field`: The unique IDM attribute that identifies the user, for example, `userName`.

* `Decision Field`: The IDM attribute whose value is evaluated, for example, `roles/*/name` or `/manager/userName`.

* `Comparator`: Select the comparator to create the query, for example, `Equal to`.

* `Value`: Enter the value of the `Decision Field` property that must match for the policy to evaluate to true, for example `administrator`.                                                                                                                                                                                                                                                                                                                                                                    |
| IPv4 Address/DNS Name                           | The policy evaluates the IP version 4 address from which the request originated.The IP address is taken from the `requestIp` value of policy decision requests. If the `requestIp` isn't provided, AM uses the IP address stored in the SSO token.                                                                      | - `Start IP`, `End IP`: Specify a range of addresses to test against by entering four sets of up to three digits, separated by periods (`.`).

  If you set only one of these values, it's used as a single IP address to match.

- `DNS Name`: Optionally, specify a domain against which requests are filtered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| IPv6 Address/DNS Name                           | The policy evaluates the IP version 6 address from which the request originated.The IP address is taken from the `requestIp` value of policy decision requests. If the `requestIp` isn't provided, AM uses the IP address stored in the SSO token.                                                                      | * `Start IP` and `End IP`: Specify a range of addresses to test against by entering eight sets of four hexadecimal characters, separated by a colon (`:`).

  If only one of these values is provided, it's used as a single IP address to match.

* `DNS Name`: Optionally, specify a domain against which requests are filtered.

  Use an asterisk (`\*`) in the DNS name to match multiple subdomains. For example, `*.example.com` applies to requests from `www.example.com`, `secure.example.com`, or any other subdomain of `example.com`.                                                                                                                                                                                                                                                                                                                                                           |
| Identity Membership                             | The policy evaluates the user's *universal ID*, in the format `id=name,ou=identity-type,realm-DN`. For example, `id=bjensen,ou=user,dc=am,dc=example,dc=com` or `id=admins,ou=group,dc=am,dc=example,dc=com`.                                                                                                           | `AM Identity Name`: The policy applies if the user's universal ID is a member of at least one of the AMIdentity objects specified here.For example, use this type to filter requests on the identity of a Web Service Client (WSC).&#xA;&#xA;This condition requires the user's universal ID to be provided as part of the evaluation request (with the invocatorPrincipalUuid key in the environment object). Java agents and web agents don't provide the universal ID and therefore don't support the Identity Membership environment condition. Use the Users & Groups subject condition instead.&#xA;&#xA;This condition works slightly differently to the Users & Groups subject condition. For that condition, the universal ID is inferred from the username provided, so you don't have to provide the full universal ID.                                                                           |
| LDAP Filter Condition                           | The policy evaluates whether the user's entry can be found using the specified LDAP search filter.                                                                                                                                                                                                                      | `LDAP Filter`: Set the LDAP search filter for the identity store configured for the policy service.	If you define a filter condition that uses LDAP accounts or groups in a different identity store, you must configure the LDAP settings under Realms > realm name > Services > Policy Configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| OAuth2 Scope                                    | The policy evaluates whether an authorization request includes all the specified OAuth 2.0 scopes.                                                                                                                                                                                                                      | `Scopes`: Enter the OAuth 2.0 scopes using the syntax described in RFC 6749, [Access Token Scope](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3).Separate multiple scope strings with spaces, for example, `openid profile`.Scope strings match regardless of the order in which they occur, so `openid profile` is equivalent to `profile openid`.The condition is also met when additional scope strings are provided beyond those required to match the specified list. For example, if the condition specifies `openid profile`, then `openid profile email` also matches.                                                                                                                                                                                                                                                                                                                     |
| Resource/Environment/IP Address                 | The policy evaluates a complex condition, such as whether the user is making a request from the localhost, and has also authenticated in a particular way.                                                                                                                                                              | `Resource/Environment/IP Address`: Enter a condition in the form of an `IF…​ELSE` statement.The `IF` statement can specify either `IP` to match the user's IP address, or `dnsName` to match their DNS name.If the `IF` statement is true, the `THEN` statement must also be true for the condition to be fulfilled. If not, AM returns relevant advice in the policy evaluation request.The available parameters for the `THEN` statement are as follows:* `service`: The authentication journey used to authenticate the user

* `authlevel`: The minimum required authentication level

* `role`: The role of the authenticated user

* `user`: The name of the authenticated user

* `redirectURL`: The URL the user was redirected from.

* `realm`: The realm to which the user authenticated.The IP address can be IPv4, IPv6, or a hybrid of the two. Example: `IF IP=[127.0.0.1] THEN role=admins`. |
| Script                                          | The policy evaluates the outcome of a JavaScript.                                                                                                                                                                                                                                                                       | `Script Name`: Select the script the policy evaluates. Learn more about scripting policy conditions in [Scripted policy conditions](scripted-policy-condition.html).`Script` is the only environmental condition available for OAuth 2.0 policies. Use scripts to capture the `ClientId` environmental attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Time (day, date, time, and timezone)            | The policy evaluates a time condition.                                                                                                                                                                                                                                                                                  | - `Start Time`

- `End Time`

- `Start Day`

- `End Day`

- `Start Date`

- `End Date`Set values in start:end pairs.- `Time Zone`: Select a time zone from the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Transaction                                     | The policy evaluates successful completion of a [transactional authorization](transactional-authorization.html).Transactional authorization requires the user to authenticate for each access to the resource.                                                                                                          | * `Authentication Strategy`: Select from the following:

  * `Authenticate to Realm`: The full path of a realm in which the user must successfully authenticate to access the protected resource. For example, `/alpha`.

  * `Authenticate to Tree`: The authentication journey the user must successfully traverse to access the protected resource.

  * `Auth Level`:The minimum authentication level the user must achieve to access the protected resource.

  `Authenticate to Chain` and `Authenticate to Module` apply only to modules and chains (deprecated) and are no longer documented.

* `Strategy Specifier`: Enter the realm, tree or level.

  If you specify an Auth Level, you must ensure there are methods available to users to reach that level. If none are found, the policy returns a 400 Bad request error when attempting to complete the transaction.                         |

## Response attributes

Add user attributes from the identity store as response attributes—either as subject attribute or static attributes—to the request header at policy decision time.

Note that response attributes are not available for the `OAuth2 Scope` resource type.

The web or Java agent for the protected resources/applications, or the protected resources/applications themselves, retrieve the policy response attributes to customize the application.

To define response attributes in the policy:

1. Click the Response Attributes edit icon ([icon: pencil-alt, set=fa]) or the Response Attributes tab.

2. To add subject attributes, select them from the Subject attributes drop-down list.

   To remove an entry, select the value, and then press Delete (Windows/GNU/Linux) or Backspace (Mac OS X).

3. To add a static attribute, specify the key-value pair for each static attribute. Enter the Property Name and its corresponding Property Value in the fields, and click Add (`+`).

   To edit a static attribute, click the edit icon ([icon: pencil-alt, set=fa]), or click ([icon: times, set=fa]) to delete.

4. Continue adding subject and static attributes, and when finished, click Save Changes.

## Example

This example policy requires authenticated users to have a session no longer than 30 minutes to access resources at `https://www.example.com:*/*`.

![Example policy](_images/policy-example.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before testing your OAuth 2.0 policies, ensure your OAuth 2.0 provider is configured to interact with AM's authorization service:1) In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider.

2) Ensure Use Policy Engine for Scope decisions is enabled.For more information about testing OAuth 2.0 policies, refer to [Dynamic OAuth 2.0 authorization](oauth2-authorization.html). |

---

---
title: Policies over REST
description: Manage authorization policies over REST at the policies endpoint, including policy objects, environment conditions, and subject conditions
component: pingam
version: 8.1
page_id: pingam:am-authorization:rest-api-authz-policies
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-policies.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "REST API", "Configuration"]
page_aliases: ["authorization-guide:rest-api-authz-policies.adoc"]
section_ids:
  policy_resource_objects: Policy resource objects
  environment-conditions: Environment conditions
  subject-conditions: Subject conditions
  access_the_endpoints: Access the endpoints
  rest-api-authz-policies-query: Query policies
  rest-api-authz-policies-read: Read a policy
  rest-api-authz-policies-create: Create a policy
  rest-api-authz-policies-update: Update a policy
  rest-api-authz-policies-delete: Delete a policy
  rest-api-authz-policies-copy-move-policies: Copy and move policies
  rest-api-authz-condition-types: Environment conditions
  rest-api-authz-subject-types: Subject conditions
  rest-api-authz-subject-attributes: Query subject attributes
  rest-api-authz-decision-combiners: Decision combiners
---

# Policies over REST

You can manage policies over REST at the `policies` endpoint.

Policies belong to a [policy set](policy-sets.html).

## Policy resource objects

The policy resources are JSON objects. A policy object can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Policy field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `name`(1)      | A string identifying the policy.This string matches the policy name part of the URL path to the resource.Do not use any of the following characters in policy, policy set, or resource type names: Double quotes (`"`) Plus sign (`+`) Comma (`,`) Less than (`<`) Equals (`=`) Greater than (`>`) Backslash (`\`) Forward slash (`/`) Semicolon (`;`) Null (`\u0000`)                                                                                                                                                                                                                          |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `actionValues`        | An object where each field is an action name.The [resource type](resource-types.html) of the [policy set](policy-sets.html) governs the available actions.The value for each action name field is a boolean indicating whether to allow the action by default. (AM also accepts `0` for `false` and any non-zero numeric value for `true`.)                                                                                                                                                                                                                                                     |
| `active`              | A boolean indicating whether AM considers the policy active for evaluation purposes.Default: `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `applicationName`     | A string identifying the policy set that contains the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `condition`           | An optional object specifying the [environment conditions](#environment-conditions) where the policy applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `description`         | A string describing the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `resourceAttributes`  | An optional array of response attribute objects; does not apply to `OAuth2 Scope` resource types.The default implementation returns statically defined attributes and attributes from user profiles. A response attribute object has these fields:- `type`

  The implementation type:

  * `Static` for statically defined attributes

  * `User` for attributes from the user profile

- `propertyName`

  The attribute name.

- `propertyValues`

  * For static attributes, the attribute values.

  * For user attributes, not used; AM determines the values when evaluating the policy. |
| `resources`           | An array of the resource name pattern strings to which the policy applies.The [resource type](resource-types.html) must allow the patterns.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `resourceTypeUuid`    | An optional string identifying the resource type that governs the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `subject`             | An optional object specifying the [subject conditions](#subject-conditions) where the policy applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `createdBy`(1)        | A string indicating who created the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `lastModifiedBy`(1)   | A string indicating who last changed the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

(1) Do not change the value of this field.

### Environment conditions

Environment conditions clarify where the policy applies.

Express environment conditions as single conditions or combine them using boolean operators. The following example demonstrates a single environment condition that requires an `access` OAuth 2.0 scope:

```json
{
  "condition": {
    "type": "OAuth2Scope",
    "requiredScopes": ["access"]
  }
}
```

The following example demonstrates a combined environment condition that excludes Saturday, Sunday, and a range of IP addresses:

```json
{
  "type": "NOT",
  "condition": {
    "type": "OR",
    "conditions": [{
      "type": "SimpleTime",
      "startTime": "",
      "endTime": "",
      "startDay": "sat",
      "endDay": "sun",
      "enforcementTimeZone": "US/Mountain"
    }, {
      "type": "IPv4",
      "startIp": "192.168.0.1",
      "endIp": "192.168.0.255",
      "ipRange": [],
      "dnsName": []
    }]
  }
}
```

The boolean operator strings to combine conditions in JSON correspond to these in the AM admin UI:

* `AND` is All of.

* `OR` is Any of.

* `NOT` is Not.

Use the following environment conditions in your policies:

* `AMIdentityMembership`

  Applies to this array of users and groups.

  ```json
  {
    "type": "AMIdentityMembership",
    "amIdentityName": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
  }
  ```

  AM Java and web agents do not support the `AMIdentityMembership` environment condition. Use the `Identity` subject condition instead.

* `AuthLevel`

  Requires at least the specified authentication level.

  ```json
  {
    "type": "AuthLevel",
    "authLevel": 2
  }
  ```

* `AuthScheme`

  Only used for authentication with modules and chains and is no longer documented.

* `AuthenticateToRealm`

  Requires authentication to the specified realm.

  ```json
  {
    "type": "AuthenticateToRealm",
    "authenticateToRealm": "alpha"
  }
  ```

* `AuthenticateToService`

  Requires authentication with the specified journey (tree).

  ```json
  {
      "type": "AuthenticateToService",
      "authenticateToService": "PushAuthentication"
  }
  ```

* `IdmUser`

  Lets you query an IDM resource to form the basis of the policy evaluation. AM must be part of a Ping Advanced Identity Software deployment to use this environment condition.

  ```json
  {
      "type": "IdmUser",
      "identityResource": "managed/user",
      "queryField": "userName",
      "decisionField": "effectiveRoles",
      "comparator": "CONTAINS",
      "value": "manager"
  }
  ```

  For multivalued attributes, use a wildcard search to find all possible values. For example:

  ```json
  {
    "type": "IdmUser",
    "identityResource": "managed/user",
    "queryField": "userName",
    "decisionField": "effectiveAssignments/*/name",
    "comparator": "EQUALS",
    "value": "employee"
  }
  ```

* `IPv4` or `IPv6`

  Requires a request from the specified IP address range or domain name.

  ```json
  {
    "type": "IPv4",
    "startIp": "127.0.0.1",
    "endIp": "127.0.0.255"
  }
  ```

  Omit `startIp` and `endIp` and use the `dnsName` field to specify an array of domain name strings:

  ```json
  {
    "type": "IPv4",
    "dnsName": ["*.example.com"]
  }
  ```

* `LDAPFilter`

  Requires the LDAP representation of the user's profile matches the specified LDAP search filter.

  ```json
  {
    "type": "LDAPFilter",
    "ldapFilter": "(&(c=US)(preferredLanguage=en-us))"
  }
  ```

* `LEAuthLevel`

  Requires at most the specified authentication level.

  ```json
  {
    "type": "LEAuthLevel",
    "authLevel": 2
  }
  ```

* `OAuth2Scope`

  Requires the specified OAuth 2.0 scopes.

  ```json
  {
    "type": "OAuth2Scope",
    "requiredScopes": ["access"]
  }
  ```

* `ResourceEnvIP`

  Requires a complex condition.

  The following example requires an authentication level of at least 4 for requests from an IP address in `127.168.10.*`:

  ```json
  {
    "type": "ResourceEnvIP",
    "resourceEnvIPConditionValue": ["IF IP=[127.168.10.*] THEN authlevel=4"]
  }
  ```

  Each `resourceEnvIPConditionValue` has one or more `IF...THEN...[ELSE...THEN]` statements.

  When the `IF` statement is true, a true `THEN` statement fulfills the condition.

  The `IF` statement specifies either:

  * An IPv4, IPv6, or hybrid address to match the IP address. The IP address can include wildcards.

  * A `dnsName` to match DNS name. The IP address can be IPv4 or IPv6 format, or a hybrid of the two, and can include wildcard characters.

  | `THEN` parameter | Description                               |
  | ---------------- | ----------------------------------------- |
  | `authlevel`      | The minimum required authentication level |
  | `realm`          | The realm where authentication completed  |
  | `redirectURL`    | The URL the user was redirected from      |
  | `role`           | The role of the authenticated user        |
  | `service`        | The authentication journey                |
  | `user`           | The name of the authenticated user        |

* `Script`

  Lets you customize the policy decision with a script. Reference the script using the script ID.

  ```json
  {
    "type": "Script",
    "scriptId": "9de3eb62-f131-4fac-a294-7bd170fd4acb"
  }
  ```

  You can find more information about using a script to evaluate policies in [Scripted policy conditions](scripted-policy-condition.html).

* `Session`

  Sets the maximum age of the authenticated session, and whether to terminate old sessions, forcing reauthentication.

  ```json
  {
    "type": "Session",
    "maxSessionTime": "10",
    "terminateSession": false
  }
  ```

* `SessionProperty`

  Require attributes set in the authenticated session.

  ```json
  {
    "type": "SessionProperty",
    "ignoreValueCase": true,
    "properties": {
      "CharSet": ["UTF-8"],
      "clientType": ["genericHTML"]
    }
  }
  ```

* `SimpleTime`

  Set a time range. The `type` is the only required field.

  ```json
  {
    "type": "SimpleTime",
    "startTime": "07:00",
    "endTime": "19:00",
    "startDay": "mon",
    "endDay": "fri",
    "startDate": "2023:01:01",
    "endDate": "2023:12:31",
    "enforcementTimeZone": "GMT+0:00"
  }
  ```

### Subject conditions

Subject conditions specify who the policy targets.

Express subject conditions as single conditions or combine them using boolean operators. The following example of a single subject condition means the policy applies to all authenticated users:

```json
{
  "subject": {
    "type": "AuthenticatedUsers"
  }
}
```

The following example of a combined subject condition means the policy applies to either of two users:

```json
{
  "type": "OR",
  "subjects": [{
    "type": "Identity",
    "subjectValues": ["id=scarter,ou=user,o=alpha,ou=services,ou=am-config"]
  }, {
    "type": "Identity",
    "subjectValues": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
  }]
}
```

The boolean operator strings to combine conditions in JSON correspond to these in the AM admin UI:

* `AND` is All of.

* `OR` is Any of.

* `NOT` is Not.

The `type` field specifies the subject:

* `AuthenticatedUsers`

  Applies to any user that successfully authenticated to AM regardless of the realm.

  To limit this to a specific realm, add an `AuthenticateToRealm` environment condition to the policy.

* `Identity`

  Applies to the specified users or groups.

  The following example means the policy applies to members of the account administrators group:

  ```json
  {
    "type": "Identity",
    "subjectValues": ["id=account-administrators,ou=group,o=alpha,ou=services,ou=am-config"]
  }
  ```

* `JwtClaim`

  Applies based on a claim in a user's JSON web token (JWT).

  ```json
  {
    "type": "JwtClaim",
    "claimName": "sub",
    "claimValue": "bjensen"
  }
  ```

* `NONE`

  Never applies; AM never evaluates the policy as part of a decision.

## Access the endpoints

The REST calls to manage policies rely on an account with the appropriate privileges:

1. Create a resource type administrator.

   In the AM admin UI, select Realm > *realm name* > Identities > + Add Identity and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the policy administrator.

   In the AM admin UI, select Realms > *realm name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-policy-admins`

   * Members

     The policy administrator whose username you recorded

   * Privileges

     Policy Admin\
     Condition Types Read Access\
     Decision Combiners Read Access\
     Entitlement Rest Access\
     Subject Types Read Access

3. Before making REST calls to manage policies, authenticate as the policy administrator:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <policy-admin-username>' \
   --header 'X-OpenAM-Password: <policy-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {"tokenId":"<policy-admin-tokenId>","successUrl":"/enduser/?realm=/alpha","realm":"/alpha"}
   ```

   For additional details, refer to [Session token after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<policy-admin-tokenId>` as the value of the AM session cookie (default name: `iPlanetDirectoryPro`) to access the REST endpoints.

## Query policies

To list all the policy sets defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies` endpoint with `_queryFilter=true` as the query string parameter.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_queryFilter=true'
{
  "result": [{
    "_id": "myExamplePolicy",
    "_rev": "1669650078159",
    "name": "myExamplePolicy",
    "active": true,
    "description": "",
    "resources": ["*://*:*/*", "*://*:*/*?*"],
    "applicationName": "myPolicySet",
    "actionValues": {
      "GET": true,
      "PUT": true
    },
    "subject": {
      "type": "Identity",
      "subjectValues": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
    },
    "lastModifiedBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,ou=am-config",
    "lastModifiedDate": "2022-11-28T15:41:18.159Z",
    "createdBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,ou=am-config",
    "creationDate": "2022-11-28T15:39:04.82Z"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../am-rest/rest-intro.html#about-crest-query) to refine the results.

| Field              | Supported `_queryFilter` operators                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `name`             | Equals (`eq`)                                                                                                      |
| `applicationName`  |                                                                                                                    |
| `description`      |                                                                                                                    |
| `createdBy`        |                                                                                                                    |
| `lastModifiedBy`   |                                                                                                                    |
| `creationDate`     | Equals (`eq`)(1) Greater than or equal to (`ge`) Greater than (`gt`) Less than or equal to (`le`) Less than (`lt`) |
| `lastModifiedDate` |                                                                                                                    |

(1) Do not use regular expression patterns with `eq`.

To list policies that explicitly reference a user or group as part of a subject condition, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies` endpoint with the query string parameters `_queryId=queryByIdentityUid` and `uid=universal-uid`, where *universal-uid* is the universal ID for the user or group.

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_queryId=queryByIdentityUid&uid=id=bjensen,ou=user,o=alpha,ou=services,ou=am-config'
{
  "result": [{
    "_id": "myExamplePolicy",
    "_rev": "1669650078159",
    "name": "myExamplePolicy",
    "active": true,
    "description": "",
    "resources": ["*://*:*/*", "*://*:*/*?*"],
    "applicationName": "myPolicySet",
    "actionValues": {
      "GET": true,
      "PUT": true
    },
    "subject": {
      "type": "Identity",
      "subjectValues": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
    },
    "lastModifiedBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,ou=am-config",
    "lastModifiedDate": "2022-11-28T15:41:18.159Z",
    "createdBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,ou=am-config",
    "creationDate": "2022-11-28T15:39:04.82Z"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

The following caveats apply when querying policies by user or group:

* AM does not evaluate group membership.

  When you specify only groups in the condition, AM does not also return policies for users who are members of the specified groups.

* AM supports only exact matches for users and groups; you cannot use wildcards.

* AM only returns policies with `Identity` subject conditions—​not `AMIdentityMembership` environment conditions.

* AM does not return policies with subject conditions that only contain the user or group in a logical *NOT* operator.

## Read a policy

To read an individual policy in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies/myExamplePolicy'
{
  "_id": "myExamplePolicy",
  "_rev": "1669650078159",
  "name": "myExamplePolicy",
  "active": true,
  "description": "",
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "GET": true,
    "PUT": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,ou=am-config",
  "lastModifiedDate": "2022-11-28T15:41:18.159Z",
  "createdBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,ou=am-config",
  "creationDate": "2022-11-28T15:39:04.82Z"
}
```

## Create a policy

To create a policy in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies` endpoint with `_action=create` as the query string parameter and a JSON representation of the policy as the POST data.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--data '{
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": false,
    "GET": true
  },
  "resources": ["https://www.example.com:443/*", "https://www.example.com:443/*?*"],
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "resourceTypeUuid": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies/?_action=create'
{
  "_id": "myExamplePolicy",
  "_rev": "1669650078159",
  "name": "myExamplePolicy",
  "active": true,
  "description": "",
  "resources": ["https://www.example.com:443/*", "https://www.example.com:443/*?*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "GET": true,
    "POST": false
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,ou=am-config",
  "lastModifiedDate": "2022-11-28T15:41:18.159Z",
  "createdBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,ou=am-config",
  "creationDate": "2022-11-28T15:39:04.82Z"
}
```

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before testing OAuth 2.0 policies, configure the `OAuth2 Provider` service for the realm to Use Policy Engine for Scope decisions.For details, refer to [Dynamic OAuth 2.0 authorization](oauth2-authorization.html). |

## Update a policy

To update an individual policy in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint with a JSON representation of the updated policy as the PUT data.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--request PUT \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--data '{
  "_id": "myNewExamplePolicy",
  "_rev": "1669721075177",
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "resources": ["https://www.example.com:443/*?*", "https://www.example.com:443/*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": true,
    "GET": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
  }
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies/myNewExamplePolicy'
{
  "_id": "myNewExamplePolicy",
  "_rev": "1669721293147",
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "resources": ["https://www.example.com:443/*?*", "https://www.example.com:443/*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": true,
    "GET": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=bjensen,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": "2022-11-29T11:28:13.147Z",
  "createdBy": "id=policy-administrator,ou=user,ou=alpha,ou=services,o=alpha,ou=services,ou=am-config",
  "creationDate": "2022-11-29T11:24:35.177Z"
}
```

## Delete a policy

To delete an individual policy in a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies/myNewExamplePolicy'
{"_id":"myNewExamplePolicy","_rev":"0"}
```

## Copy and move policies

To copy or move an individual policy, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies/policyName` endpoint. Include the appropriate parameters and POST data.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

The appropriate parameters for copying and moving policies take the following into account:

* The realm in the URL is the realm of the policy or policies to copy or to move.

* The policy name in the URL is the name of an individual policy to copy or to move.

* Specify either `_action=copy` or `_action=move` as the query string parameter.

* When moving policies from one realm to another, use the administrator's AM session cookie to authenticate.

  The policy administrator is a member of a realm, and does not have access to change another realm's settings.

The following example copies `myExamplePolicy` from the `alpha` realm to `Copied policy` in the `bravo` realm.

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: <amAdmin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "to": {
    "name": "Copied policy",
    "realm": "/bravo",
    "resourceType": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies/myExamplePolicy?_action=copy'
{
  "name": "Copied policy",
  "…​": "…​"
}
```

The POST data JSON object for copying and moving individual policies has these fields:

| Outer field | Inner field    | Description                                                                                                                                                             |
| ----------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `to`        | `name`         | The target policy.Required unless you are copying or moving a policy to a different realm, and you want the target policy to have the same name as the original policy. |
|             | `application`  | The target policy set.Required when copying or moving a policy to a different policy set.                                                                               |
|             | `realm`        | The target realm.Required when copying or moving a policy to a different realm.                                                                                         |
|             | `resourceType` | The resource type UUID for the target policy.The resource type must exist in the target realm.Required when copying or moving a policy to a different realm.            |

The following example moves `myExamplePolicy` to `Moved policy` in the same realm. The policy administrator can complete this request because the target is in the same realm.

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "to": {
    "name": "Moved policy",
    "realm": "/alpha",
    "resourceType": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies/myExamplePolicy?_action=move'
{
  "name": "Moved policy",
  "…​": "…​"
}
```

To copy or move multiple policies, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies` endpoint with the appropriate parameters and POST data.

The following example copies all the policies in `myPolicySet` to the `bravo` realm:

* The target policy set already exists in the `bravo` realm. It allows the same policies as its counterpart in the `alpha` realm.

* The `bravo` realm has resource types matching those in the `alpha` realm.

```bash
$ curl \
--request POST \
--header "iPlanetDirectoryPro: <amAdmin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "from": {
    "application": "myPolicySet"
  },
  "to": {
    "realm": "/bravo",
    "namePostfix": "-copy"
  },
  "resourceTypeMapping": {
    "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "76656a38-5f8e-401b-83aa-4ccb74ce88d2": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_action=copy'
[{
  "name": "Moved policy-copy",
  "…​": "…​"
}]
```

The POST data JSON object for copying and moving multiple policies has these fields:

| Outer field           | Inner field                                   | Description                                                                                                                                                                |
| --------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from`                | `application`                                 | The policy set to copy or move policies from.Required.                                                                                                                     |
| `to`                  | `application`                                 | The target policy set.Required when copying or moving policies to a different policy set.                                                                                  |
|                       | `realm`                                       | The target realm.Required when copying or moving policies to a different realm.                                                                                            |
|                       | `namePostfix`                                 | A string appended to target policy names to prevent clashes.Required.                                                                                                      |
| `resourceTypeMapping` | The UUID(s) of the original resource type(s). | The UUID(s) of the target resource type(s).Each pair of resource types must have the same resource patterns.Required when copying or moving policies to a different realm. |

## Environment conditions

AM lets you read and query [environment condition](#environment-conditions) schema over REST.

The schemas describe the environment condition JSON objects that you include in authorization policies. Each environment condition schema has these fields:

* `title`

  The short name for the environment condition.

* `logical`

  Whether the type is a logical operator or takes a predicate.

* `config`

  The layout of the environment condition object.

Environment conditions have these characteristics:

* Environment conditions are the same for each realm.

* The only environment condition for OAuth 2.0 policies is `Script`. Use scripts to capture the `ClientId` environment attribute.

To list all environment condition schemas, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/conditiontypes` endpoint with `_queryFilter=true` as the query string parameter.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/conditiontypes?_queryFilter=true'
```

> **Collapse: Display output**
>
> ```json
> {
>   "result": [{
>     "_id": "AMIdentityMembership",
>     "title": "AMIdentityMembership",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "amIdentityName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "AND",
>     "title": "AND",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "conditions": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthLevel",
>     "title": "AuthLevel",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authLevel": {
>           "type": "integer"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthScheme",
>     "title": "AuthScheme",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authScheme": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         },
>         "applicationIdleTimeout": {
>           "type": "integer"
>         },
>         "applicationName": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticateToRealm",
>     "title": "AuthenticateToRealm",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticateToRealm": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticateToService",
>     "title": "AuthenticateToService",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticateToService": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "IPv4",
>     "title": "IPv4",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startIp": {
>           "type": "string"
>         },
>         "endIp": {
>           "type": "string"
>         },
>         "dnsName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "IPv6",
>     "title": "IPv6",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startIp": {
>           "type": "string"
>         },
>         "endIp": {
>           "type": "string"
>         },
>         "dnsName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "LDAPFilter",
>     "title": "LDAPFilter",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "ldapFilter": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "LEAuthLevel",
>     "title": "LEAuthLevel",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authLevel": {
>           "type": "integer"
>         }
>       }
>     }
>   }, {
>     "_id": "NOT",
>     "title": "NOT",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "condition": {
>           "type": "object",
>           "properties": {}
>         }
>       }
>     }
>   }, {
>     "_id": "OAuth2Scope",
>     "title": "OAuth2Scope",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "requiredScopes": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "OR",
>     "title": "OR",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "conditions": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "Policy",
>     "title": "Policy",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "className": {
>           "type": "string"
>         },
>         "properties": {
>           "type": "object"
>         }
>       }
>     }
>   }, {
>     "_id": "ResourceEnvIP",
>     "title": "ResourceEnvIP",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "resourceEnvIPConditionValue": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "Script",
>     "title": "Script",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "scriptId": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "Session",
>     "title": "Session",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "maxSessionTime": {
>           "type": "number"
>         },
>         "terminateSession": {
>           "type": "boolean",
>           "required": true
>         }
>       }
>     }
>   }, {
>     "_id": "SessionProperty",
>     "title": "SessionProperty",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "ignoreValueCase": {
>           "type": "boolean",
>           "required": true
>         },
>         "properties": {
>           "type": "object"
>         }
>       }
>     }
>   }, {
>     "_id": "SimpleTime",
>     "title": "SimpleTime",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startTime": {
>           "type": "string"
>         },
>         "endTime": {
>           "type": "string"
>         },
>         "startDay": {
>           "type": "string"
>         },
>         "endDay": {
>           "type": "string"
>         },
>         "startDate": {
>           "type": "string"
>         },
>         "endDate": {
>           "type": "string"
>         },
>         "enforcementTimeZone": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "Transaction",
>     "title": "Transaction",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticationStrategy": {
>           "type": "string"
>         },
>         "strategySpecifier": {
>           "type": "string"
>         }
>       }
>     }
>   }],
>   "resultCount": 20,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": 0
> }
> ```

To read an environment condition schema, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/conditiontypes/condition-type` endpoint.

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/conditiontypes/IPv4'
{
  "_id": "IPv4",
  "_rev": "1669721841603",
  "title": "IPv4",
  "logical": false,
  "config": {
    "type": "object",
    "properties": {
      "startIp": {
        "type": "string"
      },
      "endIp": {
        "type": "string"
      },
      "dnsName": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    }
  }
}
```

## Subject conditions

AM lets you read and query [subject condition](#subject-conditions) schema over REST.

The schemas describe the subject condition JSON objects that you include in authorization policies. Each environment condition schema has these fields:

* `title`

  The short name for the subject condition.

* `logical`

  Whether the type is a logical operator or takes a predicate.

* `config`

  The layout of the subject condition object.

Subject conditions are the same for each realm.

To list all subject condition schemas, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/subjecttypes` endpoint with `_queryFilter=true` as the query string parameter.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/subjecttypes?_queryFilter=true'
```

> **Collapse: Display output**
>
> ```json
> {
>   "result": [{
>     "_id": "AND",
>     "title": "AND",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjects": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticatedUsers",
>     "title": "AuthenticatedUsers",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {}
>     }
>   }, {
>     "_id": "Identity",
>     "title": "Identity",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjectValues": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "JwtClaim",
>     "title": "JwtClaim",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "claimName": {
>           "type": "string"
>         },
>         "claimValue": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "NONE",
>     "title": "NONE",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {}
>     }
>   }, {
>     "_id": "NOT",
>     "title": "NOT",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subject": {
>           "type": "object",
>           "properties": {}
>         }
>       }
>     }
>   }, {
>     "_id": "OR",
>     "title": "OR",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjects": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "Policy",
>     "title": "Policy",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "name": {
>           "type": "string"
>         },
>         "className": {
>           "type": "string"
>         },
>         "values": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }],
>   "resultCount": 8,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": 0
> }
> ```

To read a subject condition schema, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/subjecttypes/subject-type` endpoint.

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/subjecttypes/Identity'
{
  "_id": "Identity",
  "_rev": "1669721896953",
  "title": "Identity",
  "logical": false,
  "config": {
    "type": "object",
    "properties": {
      "subjectValues": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    }
  }
}
```

## Query subject attributes

When you define a policy subject condition, the condition can depend on the values of subject attributes stored in a user's profile. The subject attributes that you can use depend on the LDAP User Attributes configured for the identity store where AM looks up the user's profile. For more information on these attributes, refer to [Identity stores](../setup/setting-up-identity-stores.html).

To list the available subject attributes, send an HTTP GET request to the `/json/subjectattributes` endpoint, with a `_queryFilter` parameter set to `true`.

The `iPlanetDirectoryPro` header is required and should contain the SSO token of an administrative user, such as `amAdmin`, who has access to perform the operation.

For example:

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/subjectattributes/?_queryFilter=true'
{
  "result" : [
      "sunIdentityServerPPInformalName",
      "sunIdentityServerPPFacadeGreetSound",
      "uid",
      "manager",
      "sunIdentityServerPPCommonNameMN",
      "sunIdentityServerPPLegalIdentityGender",
      "preferredLocale",
      "…​",
      "…​",
      "…​"
  ],
  "resultCount": 87,
  "pagedResultsCookie": null,
  "remainingPagedResults": 0
}
```

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | No pagination cookie is set and the subject attribute names are all returned as part of the `result` array. |

## Decision combiners

Decision combiners describe how to resolve policy decisions when multiple policies apply.

Decision combiners are the same for each realm.

To list all decision combiners, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/decisioncombiners` endpoint with `_queryFilter=true` as the query string parameter.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/decisioncombiners?_queryFilter=true'
{
  "result": [{
    "_id": "DenyOverride",
    "title": "DenyOverride"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

To read a decision combiner, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/decisioncombiners/decision-combiner` endpoint.

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/decisioncombiners/DenyOverride'
{"_id":"DenyOverride","_rev":"1669722054745","title":"DenyOverride"}
```

---

---
title: Policy set application types over REST
description: Use the REST API to query and read policy set application types that define how to compare resources and index policies
component: pingam
version: 8.1
page_id: pingam:am-authorization:rest-api-authz-application-types
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-application-types.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource", "Configuration", "REST API"]
page_aliases: ["authorization-guide:rest-api-authz-application-types.adoc"]
section_ids:
  rest-api-authz-application-types-query: Query application types
  rest-api-authz-application-types-read: Read a specific application type
---

# Policy set application types over REST

*Application types* define how to compare resources and index policies. The default application type, `iPlanetAMWebAgentService`, represents web resources. The policy set for web and Java agents (also called `iPlanetAMWebAgentService`) is based on this default application type.

The `applicationtypes` REST endpoint lets you do the following:

* [Query application types](#rest-api-authz-application-types-query)

* [Read a specific application type](#rest-api-authz-application-types-read)

Application types are configured per *server*, not per realm. Therefore, the URI for the application types API does not include a realm component, and is simply `/json/applicationtypes`.

Application types are represented in JSON format, for example:

```json
{
    "name": "iPlanetAMWebAgentService",
    "actions": {
        "POST": true,
        "PATCH": true,
        "GET": true,
        "DELETE": true,
        "OPTIONS": true,
        "PUT": true,
        "HEAD": true
    },
    "resourceComparator": "com.sun.identity.entitlement.URLResourceName",
    "saveIndex": "org.forgerock.openam.entitlement.indextree.TreeSaveIndex",
    "searchIndex": "org.forgerock.openam.entitlement.indextree.TreeSearchIndex",
    "applicationClassName": "com.sun.identity.entitlement.Application"
}
```

An application type object includes the following information:

* `name`

  Name of the application type.

* `actions`

  Set of actions for that application type, each with a boolean value indicating whether the action is allowed.

* `resourceComparator`

  The class name of the resource comparator implementation used in the context of this application type.

  The following implementations are available:

  `"com.sun.identity.entitlement.ExactMatchResourceName"`\
  `"com.sun.identity.entitlement.PrefixResourceName"`\
  `"com.sun.identity.entitlement.RegExResourceName"`\
  `"com.sun.identity.entitlement.URLResourceName"`

* `saveIndex`

  Class name of the implementation for creating indexes for resource names, such as `"com.sun.identity.entitlement.util.ResourceNameIndexGenerator"`, for URL resource names.

* `searchIndex`

  Class name of the implementation for searching indexes for resource names, such as `"com.sun.identity.entitlement.util.ResourceNameSplitter"`, for URL resource names.

* `applicationClassName`

  Class name of the application type implementation, such as `"com.sun.identity.entitlement.Application"`.

## Query application types

To list all application types, send an HTTP GET request to the `/json/applicationtypes` endpoint, with a `_queryFilter` parameter set to `true`.

The `iPlanetDirectoryPro` header is required and should contain the SSO token of an administrative user, such as `amAdmin`, who has access to perform the operation.

```bash
$ curl \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Accept-API-Version: resource=1.0" \
"https://am.example.com:8443/am/json/applicationtypes?_queryFilter=true"
{
  "result": [
    {
      "_id": "umaApplicationType",
      "applicationClassName": "com.sun.identity.entitlement.Application",
      "saveIndex": "org.forgerock.openam.uma.UmaPolicySaveIndex",
      "searchIndex": "org.forgerock.openam.uma.UmaPolicySearchIndex",
      "resourceComparator": "org.forgerock.openam.uma.UmaPolicyResourceMatcher",
      "name": "umaApplicationType",
      "actions": {}
    },
    {
      "_id": "sunAMDelegationService",
      "applicationClassName": "com.sun.identity.entitlement.Application",
      "saveIndex": "com.sun.identity.entitlement.opensso.DelegationResourceNameIndexGenerator",
      "searchIndex": "com.sun.identity.entitlement.opensso.DelegationResourceNameSplitter",
      "resourceComparator": "com.sun.identity.entitlement.RegExResourceName",
      "name": "sunAMDelegationService",
      "actions": {
        "READ": true,
        "MODIFY": true,
        "DELEGATE": true
      }
    },
    {
      "_id": "iPlanetAMWebAgentService",
      "applicationClassName": "com.sun.identity.entitlement.Application",
      "saveIndex": "org.forgerock.openam.entitlement.indextree.TreeSaveIndex",
      "searchIndex": "org.forgerock.openam.entitlement.indextree.TreeSearchIndex",
      "resourceComparator": "com.sun.identity.entitlement.URLResourceName",
      "name": "iPlanetAMWebAgentService",
      "actions": {
        "HEAD": true,
        "DELETE": true,
        "POST": true,
        "GET": true,
        "OPTIONS": true,
        "PUT": true,
        "PATCH": true
      }
    }
  ],
  "resultCount": 3,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Use additional query strings to narrow down the results. For details, refer to [Query](../am-rest/rest-intro.html#about-crest-query).

## Read a specific application type

To read an specific application type, send an HTTP GET request to the `/json/applicationtypes` endpoint, specifying the application type name in the URL.

The `iPlanetDirectoryPro` header is required and should contain the SSO token of an administrative user, such as `amAdmin`, who has access to perform the operation.

```bash
$ curl \
--header "iPlanetDirectoryPro: AQIC5…​" \
--header "Accept-API-Version: resource=1.0" \
"https://am.example.com:8443/am/json/applicationtypes/iPlanetAMWebAgentService"
{
  "_id": "iPlanetAMWebAgentService",
  "_rev": "1664877005610",
  "applicationClassName": "com.sun.identity.entitlement.Application",
  "saveIndex": "org.forgerock.openam.entitlement.indextree.TreeSaveIndex",
  "searchIndex": "org.forgerock.openam.entitlement.indextree.TreeSearchIndex",
  "resourceComparator": "com.sun.identity.entitlement.URLResourceName",
  "name": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": true,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": true,
    "PATCH": true
  }
}
```

---

---
title: Policy sets
description: Use policy sets to group policies that protect similar resources and simplify configuration across websites, web applications, and other resource types in PingAM
component: pingam
version: 8.1
page_id: pingam:am-authorization:policy-sets
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/policy-sets.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Administration", "Configuration", "Agents"]
page_aliases: ["authorization-guide:policy-sets.adoc"]
---

# Policy sets

AM uses a *policy* to determine whether to grant a principal access to a resource.

Policies belong to *policy sets*. Policy sets define a template for policies that apply to one or more [*resource types*](resource-types.html). A policy set groups policies with similar characteristics that protect websites, web applications, or other resources. It eliminates the need to configure the same basic settings repeatedly for each policy.

AM includes the following default policy sets:

* The Customer Application Policy Set, `customerApplicationPolicySet`, for application authorization journeys. Add policies to this policy set and use the `Authentication` resource type to simplify authentication flows.

  Learn about app authorization journeys in the [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/app-policy-decision.html) documentation.

* The Default Policy Set, `iPlanetAMWebAgentService`, for web and Java agents. You can create new policy sets for agents and configure them in the agent profile.

* The Default OAuth2 Scopes Policy Set, `oauth2Scopes`, for the OAuth 2.0 service.

*Application types* are templates for policy sets. The AM admin UI doesn't show application types. When you define a policy or policy set over REST, the application type appears in the JSON resource. You only configure application types using the [REST API](rest-api-authz-application-types.html). The default application types suffice for most use cases.

When creating and editing policy sets, consider the following points:

* You can specify the realm and policy set in an AM web or Java agent profile.

  AM directs requests from the agent to the specified realm and policy set, providing compatibility with older web and Java agents.

  For details, refer to the agent documentation:

  * Java agents

    [Policy Evaluation Realm Map](https://docs.pingidentity.com/java-agents/2025.3/properties-reference/org.forgerock.agents.policy.evaluation.realm.map.html)\
    [Policy Set Map](https://docs.pingidentity.com/java-agents/2025.3/properties-reference/org.forgerock.agents.policy.set.map.html)

  * Web agents

    [Policy Evaluation Realm](https://docs.pingidentity.com/web-agents/2025.3/properties-reference/org.forgerock.openam.agents.config.policy.evaluation.realm.html)\
    [Policy Set](https://docs.pingidentity.com/web-agents/2025.3/properties-reference/org.forgerock.openam.agents.config.policy.evaluation.application.html)

* AM only honors `OAuth2 Scope` resource type policies. Configure policies for your OAuth 2.0 service in a custom policy set with `OAuth2 Scope` resource type policies, or use the existing Default OAuth2 Scopes Policy Set.

* AM creates a policy set with policies for UMA 2.0 resources and identities. A resource owner using UMA 2.0 relies on the policies to share their registered resources.

  These policies appear in the AM admin UI as read-only. Even the administrative users like `amAdmin` cannot edit them. Policy administrators can view and delete the policies.

---

---
title: Policy sets in the UI
description: Manage policy sets in the PingAM admin UI to organize and control authorization policies by resource type
component: pingam
version: 8.1
page_id: pingam:am-authorization:policy-sets-ui
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/policy-sets-ui.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Configuration"]
page_aliases: ["authorization-guide:policy-sets-ui.adoc"]
section_ids:
  policy_set_names: Policy set names
---

# Policy sets in the UI

You manage policy sets through the AM admin UI. Go to Realms > *realm name* > Authorization > Policy Sets.

| To…​                | Action                                                                                                                                                                  |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a policy set | Click + New Policy Set.When creating a policy set, specify an ID and select at least one resource type.You cannot change the ID after you create the policy set.        |
| Modify a policy set | Click the policy set name or the pencil icon ([icon: pencil-alt, set=fa]).                                                                                              |
| Delete a policy set | Click the delete icon ([icon: times, set=fa]) or click the policy set name then the x Delete button.The AM admin UI prevents deletion if the set contains any policies. |

## Policy set names

Do not use any of the following characters in policy, policy set, or resource type names:\
\
Double quotes (`"`)\
Plus sign (`+`)\
Comma (`,`)\
Less than (`<`)\
Equals (`=`)\
Greater than (`>`)\
Backslash (`\`)\
Forward slash (`/`)\
Semicolon (`;`)\
Null (`\u0000`)

---

---
title: Policy sets over REST
description: Manage policy sets over REST using the applications endpoint to define authorization policies, resources, conditions, and subject types
component: pingam
version: 8.1
page_id: pingam:am-authorization:rest-api-authz-applications
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-applications.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "REST", "Configuration", "REST API"]
page_aliases: ["authorization-guide:rest-api-authz-applications.adoc"]
section_ids:
  access_the_endpoint: Access the endpoint
  rest-api-authz-applications-query: Query policy sets
  rest-api-authz-applications-read: Read a policy set
  rest-api-authz-applications-create: Create a policy set
  rest-api-authz-applications-update: Update a policy set
  rest-api-authz-applications-delete: Delete a policy set
---

# Policy sets over REST

You can manage policy sets over REST at the `applications` endpoint. ("Application" is the internal AM name for a policy set.)

Policy sets are realm-specific. The URI for the policy set API can therefore contain a realm component; for example, `/json/realms/root/realms/Realm Name/applications`. If you omit the realm path from the URL, AM uses the Top Level Realm.

AM stores policy sets as JSON objects. A policy set can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Policy set field      | Description                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `name`         | A unique string identifying the policy set.Do not use any of the following characters in policy, policy set, or resource type names: Double quotes (`"`) Plus sign (`+`) Comma (`,`) Less than (`<`) Equals (`=`) Greater than (`>`) Backslash (`\`) Forward slash (`/`) Semicolon (`;`) Null (`\u0000`)                                                                        |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                                                                                             |
| `actions`             | An object where each field is an action name.The value for each action name field is a boolean indicating whether to allow the action by default.                                                                                                                                                                                                                               |
| `applicationType`     | A string containing the application type name.For more information, refer to [Policy set application types over REST](rest-api-authz-application-types.html).                                                                                                                                                                                                                   |
| `attributeNames`      | An optional array of response attribute name strings restricting what policies in this set can return.                                                                                                                                                                                                                                                                          |
| `conditions`          | An array of environment condition identifier strings defining environment conditions allowed for policies in this set.For information, refer to [Policies over REST](rest-api-authz-policies.html) and [Manage environment condition types](rest-api-authz-policies.html#rest-api-authz-condition-types).                                                                       |
| `description`         | An optional text string to help identify the policy set.                                                                                                                                                                                                                                                                                                                        |
| `editable`            | A boolean indicating whether you can edit this policy set definition after creation.                                                                                                                                                                                                                                                                                            |
| `entitlementCombiner` | An optional string identifying how AM evaluates multiple policies for a resource.For more information, refer to [Manage decision combiners](rest-api-authz-policies.html#rest-api-authz-decision-combiners).                                                                                                                                                                    |
| `realm`               | A string identifying the realm for this policy set.You must specify the realm in the policy set JSON, even though it can be derived from the URL that is used when creating the policy set.                                                                                                                                                                                     |
| `resources`           | An array of resource pattern strings for resources governed by policies in this set.                                                                                                                                                                                                                                                                                            |
| `resourceComparator`  | An optional string identifying the fully qualified class name of the implementation to match resources for policies.The following implementations are available:`"com.sun.identity.entitlement.ExactMatchResourceName"` `"com.sun.identity.entitlement.PrefixResourceName"` `"com.sun.identity.entitlement.RegExResourceName"` `"com.sun.identity.entitlement.URLResourceName"` |
| `saveIndex`           | An optional string identifying the fully qualified class name of the implementation to save indexes for policies.                                                                                                                                                                                                                                                               |
| `searchIndex`         | An optional string identifying the fully qualified class name of the implementation to index policies.                                                                                                                                                                                                                                                                          |
| `subjects`            | Array of subject type identifier strings defining subject types allowed for policies in this set.For more information, refer to [Policies over REST](rest-api-authz-policies.html) and [Subject conditions](rest-api-authz-policies.html#rest-api-authz-subject-types).                                                                                                         |
| `createdBy`(1)        | A string indicating who created the policy set.                                                                                                                                                                                                                                                                                                                                 |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                                                                  |
| `lastModifiedBy`(1)   | A string indicating who last changed the policy set.                                                                                                                                                                                                                                                                                                                            |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                                                             |

(1) Do not change the value of this field.

## Access the endpoint

The REST calls to manage policy sets rely on an account with the appropriate privileges:

1. Create a policy set administrator.

   In the AM admin UI, select Realm > *realm name* > Identities > + Add Identity and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the policy set administrator.

   In the AM admin UI, select Realms > *realm name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-policy-set-admins`

   * Members

     The policy set administrator whose username you recorded

   * Privileges

     Policy Admin\
     Application Modify Access\
     Application Read Access

3. Before making REST calls to manage policy sets, authenticate as the policy set administrator.

   For example:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <policy-set-admin-username>' \
   --header 'X-OpenAM-Password: <policy-set-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {"tokenId":"<policy-set-admin-tokenId>","successUrl":"/enduser/?realm=/alpha","realm":"/alpha"}
   ```

   For additional details, refer to [Session token after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<policy-set-admin-tokenId>` as the value of the AM session cookie (default name: `iPlanetDirectoryPro`) to access the REST endpoints.

## Query policy sets

To list all the policy sets defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/applications` endpoint with `_queryFilter=true` as the query string parameter.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/applications?_queryFilter=true'
{
  "result": [{
    "_id": "oauth2Scopes",
    "name": "oauth2Scopes",
    "description": "A policy set for policies based on OAuth 2.0 scopes",
    "attributeNames": [],
    "createdBy": "id=dsameuser,ou=user,ou=am-config",
    "conditions": ["Script", "AMIdentityMembership", "IPv6", "SimpleTime", "IPv4", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "SessionProperty", "OAuth2Scope", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
    "lastModifiedBy": "id=dsameuser,ou=user,ou=am-config",
    "creationDate": 1578580064992,
    "lastModifiedDate": 1595479030629,
    "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "JwtClaim"],
    "saveIndex": null,
    "searchIndex": null,
    "entitlementCombiner": "DenyOverride",
    "resourceComparator": null,
    "editable": true,
    "applicationType": "iPlanetAMWebAgentService",
    "actions": {
      "GRANT": true
    },
    "resources": ["*://*:*/*", "*://*:*/*?*", "*"],
    "realm": "/alpha"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../am-rest/rest-intro.html#about-crest-query) to refine the results.

| Field              | Supported `_queryFilter` operators                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `name`             | Equals (`eq`)                                                                                                      |
| `description`      |                                                                                                                    |
| `createdBy`        |                                                                                                                    |
| `lastModifiedBy`   |                                                                                                                    |
| `creationDate`     | Equals (`eq`)(1) Greater than or equal to (`ge`) Greater than (`gt`) Less than or equal to (`le`) Less than (`lt`) |
| `lastModifiedDate` |                                                                                                                    |

(1) Do not use regular expression patterns with `eq`.

## Read a policy set

To read a specific policy set in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/applications/oauth2Scopes'
{
  "_id": "oauth2Scopes",
  "_rev": "1595479030629",
  "name": "oauth2Scopes",
  "description": "A policy set for policies based on OAuth 2.0 scopes",
  "attributeNames": [],
  "createdBy": "id=dsameuser,ou=user,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "SimpleTime", "IPv4", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "SessionProperty", "OAuth2Scope", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=dsameuser,ou=user,ou=am-config",
  "creationDate": 1578580064992,
  "lastModifiedDate": 1595479030629,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "GRANT": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*", "*"],
  "realm": "/alpha"
}
```

## Create a policy set

To create a policy set in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/applications` endpoint with `_action=create` as the query string parameter and a JSON representation of the policy set as the POST data.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "entitlementCombiner": "DenyOverride",
  "attributeNames": [],
  "saveIndex": null,
  "searchIndex": null,
  "resourceComparator": null,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": true,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": true,
    "PATCH": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/applications/?_action=create'
{
  "_id": "samplePolicySet",
  "_rev": "1669134131264",
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "attributeNames": [],
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669134131264,
  "lastModifiedDate": 1669134131264,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": true,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": true,
    "PATCH": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}
```

## Update a policy set

To update a specific policy set in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint with a JSON representation of the updated policy set as the PUT data.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--request PUT \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "entitlementCombiner": "DenyOverride",
  "attributeNames": [],
  "saveIndex": null,
  "searchIndex": null,
  "resourceComparator": null,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": false,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": false,
    "PATCH": false
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/applications/samplePolicySet'
{
  "_id": "samplePolicySet",
  "_rev": "1669134221194",
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "attributeNames": [],
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669134131264,
  "lastModifiedDate": 1669134221194,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": false,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PATCH": false,
    "PUT": false
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}
```

## Delete a policy set

To delete a policy set in a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/applications/samplePolicySet'
{"_id":"samplePolicySet","_rev":"0"}
```

AM does not permit deletion of a policy set containing policies. If you attempt to delete the policy set, AM returns an HTTP 409 Conflict status code and a message like the one in the following example:

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/applications/oauth2Scopes'
{
  "code": 409,
  "reason": "Conflict",
  "message": "Application cannot be altered because policies exist within the Application. Remove all policies from the Application before attempting to delete the Application."
}
```

Remove the policies from the set before you delete it.

---

---
title: Request authorization from AM
description: Configure policy enforcement points to request authorization decisions from PingAM based on your defined policies
component: pingam
version: 8.1
page_id: pingam:am-authorization:requesting-authorization
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/requesting-authorization.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Agents"]
page_aliases: ["authorization-guide:requesting-authorization.adoc"]
---

# Request authorization from AM

When you have configured AM to determine whether to grant or deny access based on your configured [policies](policies.html), you must configure policy enforcement points (PEPs) to use AM.

The Ping Advanced Identity Software provides the following PEPs:

* Web agents and Java agents

  Add-on components installed on the web server or container that serves your applications. The web and Java agents are tightly integrated with AM and serve exclusively as PEPs.

  Learn more in the [Web Agents User Guide](https://docs.pingidentity.com/web-agents/2025.3/user-guide/pep.html) or the [Java Agents User Guide](https://docs.pingidentity.com/java-agents/2025.3/user-guide/pep.html).

* PingGateway

  A high-performance reverse proxy server that can also function as a PEP.

  Learn more in [Policy enforcement](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/policy-enforcement.html) in the PingGateway documentation.

The Ping Advanced Identity Software PEPs intercept inbound client requests to access resources in your website or application. Based on internal rules, the PEPs can defer requests to AM for policy evaluation. Because they are tightly integrated with AM, you do not need additional code to request policy evaluation or to manage advices.

Use the Ping Advanced Identity Software PEPs where possible. If your deployment has specific requirements that aren't met by the Ping Advanced Identity Software PEPs, you can write your own PEPs that make REST calls to AM to request policy evaluation.

Related information: [Request policy decisions over REST](rest-api-authz-policy-decisions.html)

---

---
title: Request policy decisions over REST
description: Request policy decisions from PingAM over REST to evaluate access based on configured policies and return allowed or denied actions with attributes and advice
component: pingam
version: 8.1
page_id: pingam:am-authorization:rest-api-authz-policy-decisions
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-policy-decisions.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "REST API", "Evaluation"]
page_aliases: ["authorization-guide:rest-api-authz-policy-decisions.adoc"]
section_ids:
  rest-api-authz-policy-decision-concrete: Request policy decisions for a specific resource
  example_request: Example request
  rest-api-authz-policy-decision-subtree: Request policy decisions for a tree of resources
  example_request_2: Example request
  rest-api-authz-policy-decision-advice: Policy decision advice
---

# Request policy decisions over REST

You can request policy decisions from AM over REST. AM evaluates requests based on the context and the configured policies, and returns decisions that indicate what actions are allowed or denied, as well as any attributes or advices for the specified resources.

|   |                                                   |
| - | ------------------------------------------------- |
|   | This section doesn't apply to OAuth 2.0 policies. |

Request policy evaluation at the `/json/realms/root/realms/Realm Name/policies` endpoint.

When making a REST API call, specify the realm in the path component of the endpoint. You must specify the entire hierarchy of the realm, starting at the Top Level Realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/customers/realms/europe`.

Before making a REST API call to manage a policy, you must have:

* Authenticated successfully to AM as a user with sufficient privileges to make the REST API call.

* Obtained the session token returned after successful authentication.

When making the REST API call, pass the session token in the HTTP header. Find more information about the AM session token and its use in REST API calls in [Session token after authentication](../am-authentication/rest-using-ssotokens.html).

Learn more about requesting decisions for specific resources in [Request policy decisions for a specific resource](#rest-api-authz-policy-decision-concrete).

Learn more about requesting decisions for a resource and all resources beneath it in [Request policy decisions for a tree of resources](#rest-api-authz-policy-decision-subtree).

## Request policy decisions for a specific resource

To request policy decisions for specific resources, send a POST request to the `policies` endpoint, with the `evaluate` action. For example:

`/json/realms/root/realms/Realm Name/policies?_action=evaluate`.

When making a REST API call, specify the realm in the path component of the endpoint. You must specify the entire hierarchy of the realm, starting at the Top Level Realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/customers/realms/europe`.

The payload for the HTTP POST is a JSON object that specifies at least the resources, and takes the following form.

```json
{
    "resources": [
        "resource1",
        "resource2",
        ...,
        "resourceN"
    ],
    "application": "defaults to iPlanetAMWebAgentService if not specified",
    "subject": {
        "ssoToken": "SSO token ID string",
        "jwt": "JSON Web Token string",
        "claims": {
            "key": "value",
            ...
        }
    },
    "environment": {
        "optional key1": [
            "value",
            "another value",
            ...
        ],
        "optional key2": [
            "value",
            "another value",
            ...
        ],
        ...
    }
}
```

The input fields are as follows:

* `resources`

  (Required) Specifies the list of resources for which to return decisions.

  For example, when using the default policy set, `"iPlanetAMWebAgentService"`, you can request decisions for resource URLs.

  ```json
  {
      "resources": [
          "http://www.example.com/index.html",
          "http://www.example.com/do?action=run"
      ]
  }
  ```

* `application`

  The name of the policy set. Defaults to `"iPlanetAMWebAgentService"`, if not specified.

  Learn more in [Policy sets over REST](rest-api-authz-applications.html).

* `subject`

  (Optional). Holds an object that represents the subject. If you don't specify the subject, AM uses the SSO token ID of the subject making the request.

  Specify one or more of the following keys. If you specify multiple keys, the subject can have multiple associated principals, and you can use subject conditions corresponding to any type in the request:

  * `ssoToken`

    The value is the SSO token ID string for the subject, which is returned, for example, on successful authentication as described in [Authenticate over REST](../am-authentication/authn-rest.html).

    If the client the token's been issued for is authorized to use ID tokens as session tokens, you can use an OIDC token instead. Learn more in [ID tokens as session cookies](../am-oidc1/oidc-additional-use-cases.html#idtokens-as-session-tokens).

  * `jwt`

    The value is a JWT string.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you pass the subject details as a JWT, AM doesn't attempt to validate the JWT signature or the claims in the JWT. It's assumed you've already validated the JWT before calling the authorization endpoint.For AM-issued ID Tokens, you can pass the ID Token as the value of the `ssoToken` field (after adding your client to the `Authorized SSO Clients` list). In this case, AM validates the token. Learn more in [ID tokens as policy subjects](../am-oidc1/oidc-additional-use-cases.html#idtokens-in-policy-decision). |

  * `claims`

    The value is an object (map) of JWT claims to their values. Any string is permitted, but you must include the `sub` claim.

* `environment`

  (Optional). Holds a map of keys to lists of values.

  If you do not specify the environment, the default is an empty map.

### Example request

The following example requests policy decisions for two URL resources. The `iPlanetDirectoryPro` header sets the SSO token for a user who has access to perform the operation.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.1" \
--header "iPlanetDirectoryPro: AQIC5…​" \
--data '{
    "resources":[
        "http://www.example.com/index.html",
        "http://www.example.com/do?action=run"
    ],
    "application":"iPlanetAMWebAgentService"
}' \
"https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_action=evaluate"
[
    {
        "resource":"http://www.example.com/do?action=run",
        "actions":{

        },
        "attributes":{

        },
        "advices":{
            "AuthLevelConditionAdvice":[
                "3"
            ]
        }
    },
    {
        "resource":"http://www.example.com/index.html",
        "actions":{
            "POST":false,
            "GET":true
        },
        "attributes":{
            "cn":[
                "bjensen"
            ]
        },
        "advices":{

        }
    }
]
```

In the JSON list of decisions returned for each resource, AM includes these fields:

* `resource`

  The resource specified in the request.

  The decisions returned aren't guaranteed to be in the same order as the requested resources.

* `actions`

  A map of action name keys to Boolean values that indicate whether the action is allowed (`true`) or denied (`false`) for the specified resource.

  In the example, for resource `http://www.example.com/index.html` HTTP GET is allowed, whereas HTTP POST is denied.

* `attributes`

  A map of attribute names to their values, if any response attributes are returned, according to applicable policies.

  In the example, the policy that applies to `http://www.example.com/index.html` causes the value of the subject's "cn" profile attribute to be returned.

* `advices`

  A map of advice names to their values, if any advice is returned according to applicable policies.

  The `advices` field can provide hints about what AM requires to make an authorization decision.

  In the example, the policy that applies to `http://www.example.com/do?action=run` requests the subject to be authenticated at an authentication level of at least 3.

  ```json
  {
      "advices": {
          "AuthLevelConditionAdvice": [
              "3"
          ]
      }
  }
  ```

  Learn more in [Policy decision advice](#rest-api-authz-policy-decision-advice).

You can use the query string parameters `_prettyPrint=true` to make the output easier to read, and `_fields=field-name[,field-name…​]` to limit the fields returned in the output.

## Request policy decisions for a tree of resources

To request policy decisions for a resource, and all other resources in the subtree, send a POST request to the `policies` endpoint, with the `evaluateTree` action. For example:

`/json/realms/root/realms/Realm Name/policies?_action=evaluateTree`

The payload for the HTTP POST is a JSON object that specifies at least the root resource, and takes the following form.

```json
{
    "resource": "resource string",
    "application": "defaults to iPlanetAMWebAgentService if not specified",
    "subject": {
        "ssoToken": "SSO token ID string",
        "jwt": "JSON Web Token string",
        "claims": {
            "key": "value",
            ...
        }
    },
    "environment": {
        "optional key1": [
            "value",
            "another value",
            ...
        ],
        "optional key2": [
            "value",
            "another value",
            ...
        ],
        ...
    }
}
```

The values for the fields shown above are explained below:

* `resource`

  (Required) Specifies the root resource for the decisions to return.

  For example, when using the default policy set, `"iPlanetAMWebAgentService"`, you can request decisions for resource URLs.

  ```json
  {
      "resource": "http://www.example.com/"
  }
  ```

* `application`

  The name of the policy set. Defaults to `"iPlanetAMWebAgentService"` if not specified.

  Learn more in [Policy sets over REST](rest-api-authz-applications.html).

* `subject`

  (Optional) An object that represents the subject. You can specify one or more of the following keys. If you specify multiple keys, the subject can have multiple associated principals, and you can use subject conditions that correspond to any type in the request.

  * `ssoToken`

    The SSO token ID string for the subject, returned on successful authentication, as described in [Authenticate over REST](../am-authentication/authn-rest.html).

  * `jwt`

    The value is a JWT string.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you pass the subject details as a JWT, AM doesn't attempt to validate the JWT signature or the claims in the JWT. It's assumed you've already validated the JWT before calling the authorization endpoint.For AM-issued ID Tokens, you can pass the ID Token as the value of the `ssoToken` field (after adding your client to the `Authorized SSO Clients` list). In this case, AM validates the token. Learn more in [ID tokens as policy subjects](../am-oidc1/oidc-additional-use-cases.html#idtokens-in-policy-decision). |

  * `claims`

    An object (map) of JWT claims to their values. If you do not specify the subject, AM uses the SSO token ID of the subject making the request.

* `environment`

  (Optional) A map of keys to lists of values.

  If you don't specify the environment, the default is an empty map.

### Example request

The following example requests policy decisions for `http://www.example.com/`. The `iPlanetDirectoryPro` header sets the SSO token for a user who has access to perform the operation. The subject takes the SSO token of the user who wants to access a resource.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: AQIC5…​NDU1*" \
--header "Accept-API-Version: resource=1.0" \
--data '{
    "resource": "http://www.example.com/",
    "subject": { "ssoToken": "AQIC5…​zE4*" }
}' \
"https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_action=evaluateTree"
[
    {
        "resource":"http://www.example.com/",
        "actions":{
            "GET":true,
            "OPTIONS":true,
            "HEAD":true
        },
        "attributes":{

        },
        "advices":{

        }
    },
    {
        "resource":"http://www.example.com/",
        "actions":{
            "POST":false,
            "PATCH":false,
            "GET":true,
            "DELETE":true,
            "OPTIONS":true,
            "HEAD":true,
            "PUT":true
        },
        "attributes":{
            "myStaticAttr":[
                "myStaticValue"
            ]
        },
        "advices":{

        }
    },
    {
        "resource":"http://www.example.com/?*",
        "actions":{
            "POST":false,
            "PATCH":false,
            "GET":false,
            "DELETE":false,
            "OPTIONS":true,
            "HEAD":false,
            "PUT":false
        },
        "attributes":{

        },
        "advices":{
            "AuthLevelConditionAdvice":[
                "3"
            ]
        }
    }
]
```

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | AM returns decisions not only for the specified resource, but also for matching resource names in the tree whose root is the specified resource. |

In the JSON list of decisions returned for each resource, AM includes these fields:

* `resource`

  A resource name whose root is the resource specified in the request.

  The decisions returned aren't guaranteed to be in the same order as the resources were requested.

* `actions`

  A map of action name keys to Boolean values that indicate whether the action is allowed (`true`) or denied (`false`) for the specified resource.

  In the example, for matching resources with a query string, only HTTP OPTIONS is allowed according to the policies configured.

* `attributes`

  A map of attribute names to their values, if any response attributes are returned according to applicable policies.

  In the example, the policy that applies to `http://www.example.com/*` causes a static attribute to be returned.

* `advices`

  A map of advice names to their values, if any advice is returned according to applicable policies.

  The `advices` field can provide hints regarding what AM needs to make the authorization decision.

  In the example, the policy that applies to resources with a query string requests the subject to be authenticated at an authentication level of at least 3.

  Notice that with the `advices` field present, no `advices` appear in the JSON response.

  ```json
  {
      "advices": {
          "AuthLevelConditionAdvice": [ "3" ]
      }
  }
  ```

You can use the query string parameters `_prettyPrint=true` to make the output easier to read, and `_fields=field-name[,field-name…​]` to limit the fields returned in the output.

## Policy decision advice

When AM returns a policy decision, the JSON for the decision can include an `advices` field. This field contains hints for the policy enforcement point.

```json
{
    "advices": {
        "type": [
            "advice"
        ]
    }
}
```

The advices returned depend on [policy conditions](rest-api-authz-policies.html).

The following examples show different types of policy decision advice and the conditions that cause AM to return the advice.

* AuthLevel and LEAuthLevel condition failures

  `AuthLevel` and `LEAuthLevel` condition failures can result in an advice showing the expected or maximum possible authentication level. For example, failure against the following condition:

  ```json
  {
      "type": "AuthLevel",
      "authLevel": 2
  }
  ```

  Leads to this advice:

  ```json
  {
      "AuthLevelConditionAdvice": [
          "2"
      ]
  }
  ```

* AuthenticateToRealm condition failure

  An `AuthenticateToRealm` condition failure can result in an advice showing the name of the realm to which authentication is required. For example, failure against the following condition:

  ```json
  {
      "type": "AuthenticateToRealm",
      "authenticateToRealm": "MyRealm"
  }
  ```

  Leads to this advice:

  ```json
  {
      "AuthenticateToRealmConditionAdvice": [
          "/myRealm"
      ]
  }
  ```

* AuthenticateToService condition failure

  An `AuthenticateToService` condition failure can result in an advice showing the name of the required authentication tree. For example, failure against the following condition:

  ```json
  {
      "type": "AuthenticateToService",
      "authenticateToService": "Login"
  }
  ```

  Leads to this advice:

  ```json
  {
      "AuthenticateToServiceConditionAdvice": [
          "Login"
      ]
  }
  ```

* ResourceEnvIP condition failure

  A `ResourceEnvIP` condition failure can result in an advice that indicates corrective action to be taken. The advice varies, depending on what the condition tests. For example, failure against the following condition:

  ```json
  {
      "type": "ResourceEnvIP",
      "resourceEnvIPConditionValue": [
          "IF IP=[127.0.0.12] THEN authlevel=4"
      ]
  }
  ```

  Leads to this advice:

  ```json
  {
      "AuthLevelConditionAdvice": [
          "4"
      ]
  }
  ```

  Failure against a different type of `ResourceEnvIP` condition such as the following:

  ```json
  {
      "type": "ResourceEnvIP",
      "resourceEnvIPConditionValue": [
          "IF IP=[127.0.0.11] THEN service=Login"
      ]
  }
  ```

  Leads to this advice:

```json
{
    "AuthenticateToServiceConditionAdvice": [
        "Login"
    ]
}
```

* Session condition failure

  A `Session` condition failure can result in an advice showing that access was denied because the authenticated session was active longer than allowed by the condition.

  If `terminateSession` is `true` and policy evaluation is requested, AM sends the session advice to the Java, Web, or PingGateway agent when the `maxSessionTime` elapses.

  For example, failure against the following condition:

  ```json
  {
      "type": "Session",
      "maxSessionTime": "10",
      "terminateSession": true
  }
  ```

  Leads to this advice:

  ```json
  {
      "SessionConditionAdvice": [
          "deny"
      ]
  }
  ```

  When AM receives the terminate advice, the user is redirected to the login page to reauthenticate.

  |   |                                                                                                                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If `terminateSession` is `false` and policy evaluation is requested, AM doesn't send the session advice to the Java, Web, or PingGateway agent when the `maxSessionTime` elapses. Instead of being redirected to the login page, the user receives a 403 Forbidden response for the protected resource. |

When policy evaluation denials occur against the following conditions, AM doesn't return any advice:

* `IPv4`

* `IPv6`

* `LDAPFilter`

* `OAuth2Scope`

* `SessionProperty`

* `SimpleTime`

When policy evaluation is requested for a nonexistent or inactive subject, AM returns an HTTP 200 code and a response that contains no actions or advice. Access to the resource is denied.

---

---
title: Resource types
description: Define resource type templates to establish which resources policies apply to and which actions are permitted on those resources
component: pingam
version: 8.1
page_id: pingam:am-authorization:resource-types
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/resource-types.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource"]
page_aliases: ["authorization-guide:resource-types.adoc"]
section_ids:
  default_resource_types: Default resource types
---

# Resource types

Resource types define a template for the resources that policies apply to, and the actions that can be performed on those resources.

AM needs a *policy* to decide whether a user can access a resource. When you configure a policy, you also configure a resource (or a pattern to match several resources) that the policy applies to, and the actions that the policy allows or denies.

Resource types are templates that you can define once and reuse in several policies. For example, you could create a template that always allows PUT and POST operations from your internal network.

## Default resource types

AM includes the following resource types by default:

* `Authentication`

  The `Authentication` resource type supports the identification of applications during the authentication journey using unique identifiers like client IDs (for OAuth 2.0 or OIDC) or entity IDs (for SAML 2.0). It contains a single wildcard pattern, `*`.

  This resource type supports the `Access` action, which can be allowed or denied.

* `OAuth2 Scope`

  The `OAuth2 Scope` resource type acts as a template for granting or denying OAuth 2.0 scopes. It contains a string-based scope pattern, `*`, and two URL-based scope patterns, such as `*://*:*/*?*`.

  This resource type supports the `GRANT` action, which can be allowed or denied.

* `URL`

  The `URL` resource type acts as a template for protecting web pages or applications. It contains resource patterns, such as `*://*:*/*?*`, that can be more specific when used in the policy.

  This resource type supports the following actions:

  GET\
  POST\
  PUT\
  HEAD\
  PATCH\
  DELETE\
  OPTIONS

  For example, an application for Example.com's HR service might contain resource types that constrain all policies to apply to URL resource types under `http*://example.com/hr*` and `http*://example.com/hr*?*`, and only allow HTTP `GET` and `POST` actions.

---

---
title: Resource types in the UI
description: Create and manage resource types through the PingAM admin UI to define patterns and actions for authorization policies
component: pingam
version: 8.1
page_id: pingam:am-authorization:resource-types-ui
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/resource-types-ui.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource", "Configuration"]
page_aliases: ["authorization-guide:resource-types-ui.adoc"]
section_ids:
  resource_type_names: Resource type names
  policy-patterns-wildcards: Resource type patterns
  wildcards: Wildcards
  wildcards_in_schemes_hosts_and_port_numbers: Wildcards in schemes, hosts, and port numbers
  wildcards_in_paths: Wildcards in paths
  wildcards_in_query_strings: Wildcards in query strings
  non_ascii_characters: Non-ASCII characters
  resource_type_actions: Resource type actions
  resource-types-console: Example
---

# Resource types in the UI

You manage resource types through the AM admin UI. Go to Realms > *realm name* > Authorization > Resource Types.

| To…​                   | Action                                                                                                                                                                                               |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a resource type | Click New Resource Type.When creating a resource type, specify at least one action and one pattern.                                                                                                  |
| Modify a resource type | Click the resource type name or the pencil icon ([icon: pencil-alt, set=fa]).                                                                                                                        |
| Delete a resource type | Click the delete icon ([icon: times, set=fa]) or click the resource type name then the x Delete button.The AM admin UI prevents deletion if any policies or policy sets depend on the resource type. |

## Resource type names

Do not use any of the following characters in policy, policy set, or resource type names:\
\
Double quotes (`"`)\
Plus sign (`+`)\
Comma (`,`)\
Less than (`<`)\
Equals (`=`)\
Greater than (`>`)\
Backslash (`\`)\
Forward slash (`/`)\
Semicolon (`;`)\
Null (`\u0000`)

## Resource type patterns

Policies apply to resources that match their patterns.

* A policy belongs to a policy set.

* A policy set permits one or more resource types in their policies.

* A policy can only define patterns that fit the patterns of its resource types.

### Wildcards

Resource type patterns can include a mix of literal characters and wildcards, `*` or `-*-` by default. Wildcards can appear anywhere in a resource type pattern to match resources, such as URLs or OAuth 2.0 scopes.

* Do not mix `*` and `-*-` in the same pattern.

* Wildcards cannot be escaped.

* By default, comparisons are not case-sensitive.

  To configure the delimiter, wildcards, and case-sensitivity, in the AM admin UI, go to Configure > Global Services > Policy Configuration, and edit the Resource Comparator.

### Wildcards in schemes, hosts, and port numbers

When using wildcards for the scheme and authority parts of a URL:

* The pattern `*://*:*/*` matches these URLs:

  `http://www.example.com:80/index.html`\
  `https://www.example.com:443/index.html`\
  `http://www.example.net:8080/index.html`

* Omitting the port number implies the default port number for the scheme:

  `http://www.example.com/*` is the same as `http://www.example.com:80/*`.

  `https://www.example.com/*` is the same as `https://www.example.com:443/*`.

### Wildcards in paths

Wildcards have these properties in a URL path:

* The wildcard `*` matches *multiple* path segments.

  For example, `https://www.example.com/*` matches `https://www.example.com/`, `https://www.example.com/index.html`, and `https://www.example.com/company/images/logo.png`.

* The wildcard `-*-` matches *a single* path segment.

  For example, `https://www.example.com/-*-` matches `https://www.example.com/index.html`.

  It does not match `https://www.example.com/company/resource.html` or `https://www.example.com/company/images/logo.png`.

* Duplicate slashes (`//`) count as a single slash.

  `http://www.example.com//path/` and `http://www.example.com/path//` are equivalent.

* A trailing slash counts as a distinct part of the resource to match.

  `https://www.example.com/path` and `https://www.example.com/path/` are not equivalent.

### Wildcards in query strings

Wildcards do not match `?`.

Add explicit patterns to match URLs with query strings:

* When matching URLs protected by a web or Java agent, an asterisk (`*`) at the end of a pattern after `?` matches *one or more* characters, not zero or more characters.

  For example, `https://www.example.com/*?*` matches `https://www.example.com/users?_action=create`, not `https://www.example.com/users?`.

  To match all URLs under `https://www.example.com/`, specify three patterns:

  `https://www.example.com/*`\
  `https://www.example.com/*?`\
  `https://www.example.com/*?*`

* When matching resources with a `policies?_action=evaluate` REST call, an asterisk (`*`) at the end of a pattern after `?` matches *zero or more* characters.

  For example, `https://www.example.com/*?*` matches `https://www.example.com/users?_action=create` and `https://www.example.com/users?`.

  To match all URLs under `http://www.example.com/`, specify two patterns:

  `https://www.example.com/*`\
  `https://www.example.com/*?*`

* AM normalizes query strings before checking whether a policy matches a resource.

  To normalize the query string, AM sorts the query string field-value pairs alphabetically by field name. These query strings are equivalent:

  `?subject=SPBnfm+t5PlP+ISyQhVlplE22A8=&action=get`\
  `?action=get&subject=SPBnfm+t5PlP+ISyQhVlplE22A8=`

### Non-ASCII characters

Use percent-encoding for non-ASCII characters in resource patterns.

For example, to match resources under the Internationalized Resource Identifier (IRI) `https://www.example.com/forstå/` use:

`https://www.example.com:443/forst%C3%A5/*`\
`https://www.example.com:443/forst%C3%A5/*?*`

## Resource type actions

AM policies use actions to grant or deny access to a resource. A policy can only determine actions defined by its resource types.

Choose a name that summarizes the action the principal aims to perform on the resource. The default state for each action is either Allow or Deny.

## Example

The following screen creates a resource type for policies to switch lights on and off:

![Add the patterns and actions that policies using this resource type can make use of.](_images/resource-types-console.png)Figure 1. Configuring a resource type in the UI

---

---
title: Resource types over REST
description: Manage resource types in PingAM over REST using the resourcetypes endpoint to create, read, update, and delete JSON-based resource types that specify URLs or resource names to protect
component: pingam
version: 8.1
page_id: pingam:am-authorization:rest-api-authz-resource-types
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/rest-api-authz-resource-types.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Resource", "REST API", "Configuration"]
page_aliases: ["authorization-guide:rest-api-authz-resource-types.adoc"]
section_ids:
  access_the_endpoints: Access the endpoints
  rest-api-authz-resource-types-query: Query resource types
  rest-api-authz-resource-types-read: Read a resource type
  rest-api-authz-resource-types-create: Create a resource type
  rest-api-authz-resource-types-update: Update a resource type
  rest-api-authz-resource-types-delete: Delete a resource type
---

# Resource types over REST

You can manage resource types over REST at the `resourcetypes` endpoint.

AM stores resource types as JSON objects. A resource type can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Resource type field   | Description                                                                                                                                                                                                                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `uuid`(1)      | A unique, system-generated UUID string.Use this string to identify a specific resource type. Do not change the generated UUID.                                                                                                                                                                                   |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                              |
| `name`                | A human-readable name string for the resource type.Do not use any of the following characters in policy, policy set, or resource type names: Double quotes (`"`) Plus sign (`+`) Comma (`,`) Less than (`<`) Equals (`=`) Greater than (`>`) Backslash (`\`) Forward slash (`/`) Semicolon (`;`) Null (`\u0000`) |
| `description`         | An optional text string to help identify the resource type.                                                                                                                                                                                                                                                      |
| `patterns`            | An array of resource pattern strings specifying URLs or resource names to protect.For details, refer to [Resource type patterns](resource-types-ui.html#policy-patterns-wildcards).                                                                                                                              |
| `actions`             | An object where each field is an action name.The value for each action name field is a boolean indicating whether to allow the action by default in policies that derive from this resource type.                                                                                                                |
| `createdBy`(1)        | A string indicating who created the resource type.                                                                                                                                                                                                                                                               |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                   |
| `lastModifiedBy`(1)   | A string indicating who last changed the resource type.                                                                                                                                                                                                                                                          |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                              |

(1) Do not change the value of this field.

## Access the endpoints

The REST calls to manage resource types rely on an account with the appropriate privileges:

1. Create a resource type administrator.

   In the AM admin UI, select Realm > *realm name* > Identities > + Add Identity and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the resource type administrator.

   Select Realms > *realm name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-resource-type-admins`

   * Members

     The resource type administrator whose username you recorded

   * Privileges

     Policy Admin\
     Resource Type Modify Access\
     Resource Type Read Access

3. Before making REST calls to manage resource types, authenticate as the resource type administrator:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <resource-type-admin-username>' \
   --header 'X-OpenAM-Password: <resource-type-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {"tokenId":"<resource-type-admin-tokenId>","successUrl":"/enduser/?realm=/alpha","realm":"/alpha"}
   ```

   For additional details, refer to [Session token after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<resource-type-admin-tokenId>` as the value of the AM session cookie (default name: `iPlanetDirectoryPro`) to access the REST endpoints.

## Query resource types

To list all the resource types defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/resourcetypes` endpoint with `_queryFilter=true` as the query string parameter.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/resourcetypes?_queryFilter=true'
[{
  "result": [{
    "_id": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
    "uuid": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
    "name": "Light",
    "description": "",
    "patterns": ["light://*/*"],
    "actions": {
      "switch_off": false,
      "switch_on": false
    },
    "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "creationDate": 1669038769034,
    "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "lastModifiedDate": 1669038769034
  }, {
    "_id": "76656a38-5f8e-401b-83aa-4ccb74ce88d2",
    "uuid": "76656a38-5f8e-401b-83aa-4ccb74ce88d2",
    "name": "URL…​"
  }, {
    "_id": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "uuid": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "name": "OAuth2 Scope…​"
  }],
  "resultCount": 3,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../am-rest/rest-intro.html#about-crest-query) to refine the results.

| Field         | Supported `_queryFilter` operators               |
| ------------- | ------------------------------------------------ |
| `uuid`        | Equals (`eq`) Contains (`co`) Starts with (`sw`) |
| `name`        |                                                  |
| `description` |                                                  |
| `patterns`    |                                                  |
| `actions`     |                                                  |

## Read a resource type

To read a resource type in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--header "iPlanetDirectoryPro: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/resourcetypes/fcaee7dc-f99c-43b1-b10d-592e1c4bd394'
{
  "_id": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
  "_rev": "1669045336245",
  "uuid": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
  "name": "Light",
  "description": "",
  "patterns": ["light://*/*"],
  "actions": {
    "switch_off": false,
    "switch_on": false
  },
  "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "creationDate": 1669038769034,
  "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "lastModifiedDate": 1669038769034
}
```

## Create a resource type

To create a resource type in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/resourcetypes` endpoint with `_action=create` as the query string parameter and a JSON representation of the resource type as the POST data.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

AM generates the UUID for the resource.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "My Resource Type",
  "actions": {
    "LEFT": true,
    "RIGHT": true,
    "UP": true,
    "DOWN": true
  },
  "patterns": ["https://device/location/*"]
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/resourcetypes/?_action=create'
{
  "_id": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "uuid": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "name": "My Resource Type",
  "description": null,
  "patterns": ["https://device/location/*"],
  "actions": {
    "RIGHT": true,
    "DOWN": true,
    "UP": true,
    "LEFT": true
  },
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669045619375,
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": 1669045619375
}
```

## Update a resource type

To update a resource type in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource. Include a JSON representation of the resource type as the PUT body, making sure the `"uuid"` and `"_id"` fields match the original resource.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--request PUT \
--header "Content-Type: application/json" \
--header "iPlanetDirectoryPro: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "My Resource Type",
  "actions": {
    "LEFT": true,
    "RIGHT": true,
    "UP": false,
    "DOWN": false
  },
  "patterns": ["https://device/location/*"]
}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/resourcetypes/c7e09ca1-a0db-4434-9327-ca685ae99899'
{
  "_id": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "uuid": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "name": "My Resource Type",
  "description": null,
  "patterns": ["https://device/location/*"],
  "actions": {
    "RIGHT": true,
    "DOWN": false,
    "UP": false,
    "LEFT": true
  },
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669045619375,
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": 1669045765822
}
```

## Delete a resource type

To delete a resource type from a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | If you omit the realm path from the URL, AM uses the Top Level Realm. |

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/resourcetypes/c7e09ca1-a0db-4434-9327-ca685ae99899'
{"_id":"c7e09ca1-a0db-4434-9327-ca685ae99899","_rev":"0"}
```

AM does not permit deletion of a resource type when a policy set or policy depends on it. If you attempt to delete a resource type that is in use, AM returns an HTTP 409 Conflict status code and a message like the one in the following example:

```bash
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/resourcetypes/76656a38-5f8e-401b-83aa-4ccb74ce88d2'
{
  "code": 409,
  "reason": "Conflict",
  "message": "Unable to remove resource type 76656a38-5f8e-401b-83aa-4ccb74ce88d2 because it is referenced in the policy model."
}
```

Remove the dependency on the resource type from all policy sets and policies before you delete it.

---

---
title: Scripted policy conditions
description: Use scripts to customize policy evaluation actions in PingAM by creating policy condition scripts that validate user attributes and environment parameters
component: pingam
version: 8.1
page_id: pingam:am-authorization:scripted-policy-condition
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-authorization/scripted-policy-condition.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Policy", "Administration", "Scripting", "Evaluation"]
page_aliases: ["authorization-guide:scripted-policy-condition.adoc"]
section_ids:
  sec-scripted-policy-condition-prepare: Prepare a demonstration
  scripted-policy-privilege: Policy administrator account
  scripted-policy-enduser: End user account
  scripted-policy-script: Create a script
  scripted-policy-policy: Create a policy
  sec-scripted-policy-condition-evaluate: Try the demonstration
  scripting-api-oauth2-policy: OAuth 2.0 scopes policy script API
---

# Scripted policy conditions

You can use scripts to tailor the actions AM takes as part of policy evaluation.

This example uses a next-generation policy condition script.

Find information about the available bindings for legacy and next-generation policy condition scripts in the [Policy condition scripting API](../am-scripting/policy-condition-scripting-api.html).

## Prepare a demonstration

To demonstrate an example policy condition script:

* [Create a policy administrator user](#scripted-policy-privilege).

* [Create an end user](#scripted-policy-enduser).

* [Create a policy condition script](#scripted-policy-script)

* [Create a policy that uses the script](#scripted-policy-policy).

### Policy administrator account

This account represents the policy enforcement point (PEP) account. It has the Entitlement Rest Access privilege required to request AM policy decisions over HTTP using the REST API. In a production deployment, use a PEP like PingGateway or an AM agent in this role.

1. Create a policy administrator.

   In the AM admin UI, select Realms > *realm name* > Identities > + Add Identity and fill the required fields.

   Record the username and password.

2. Create a group that grants the Entitlement Rest Access privilege to the policy administrator.

   Select Realms > alpha > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-policy-evaluation`

   * Members

     The policy administrator whose username you recorded

   * Privileges

     Entitlement Rest Access

### End user account

This account represents the end user who tries to access online resources.

1. Create a user.

   In the AM admin UI, select Realms > *realm name* > Identities > + Add Identity and fill the required fields.

   Record the username and password.

2. In the Home Address field of the user profile, enter `United States`.

### Create a script

1. In the AM admin UI, [create a script](../am-scripting/manage-scripts-console.html#create-scripts-with-console) with the following values:

   * Name

     `Location Authorization Script`

   * Script Type

     `Policy Condition`

   * Evaluator Version

     `Next Generation`

2. In the Script field, paste the following JavaScript:

   > **Collapse: Next-generation policy condition example script**
   >
   > ```javascript
   > var userAddress, userIP, resourceHost;
   >
   > if (validateAndInitializeParameters()) {
   >
   >     var countryFromUserIP = getCountryFromUserIP();
   >     logger.info("Country retrieved from user's IP: " + countryFromUserIP);
   >     var countryFromResourceURI = getCountryFromResourceURI();
   >     logger.info("Country retrieved from resource URI: " + countryFromResourceURI);
   >
   >     if (userAddress === countryFromUserIP && userAddress === countryFromResourceURI) {
   >
   >         logger.info("Authorization succeeded");
   >         responseAttributes.put("countryOfOrigin", [countryFromUserIP]);
   >         authorized = true;
   >     } else {
   >         logger.info("Authorization failed");
   >         authorized = false;
   >     }
   >
   > } else {
   >     logger.error("Required parameters not found. Authorization Failed.");
   >     authorized = false;
   > }
   >
   > function getCountryFromUserIP() {
   >
   >     var options = {
   >         method: "GET",
   >         headers: {
   >             "Content-Type": "application/json"
   >         }
   >     };
   >     var requestURL = "http://ip-api.com/json/" + userIP;
   >
   >     var response = httpClient.send(requestURL, options).get();
   >
   >     if (response.status === 200) {
   >         var result = JSON.parse(response.text());
   >         if (result) {
   >             return result.country;
   >         }
   >     } else {
   >         logger.error("Error generating IP location: " + response.statusText);
   >     }
   > }
   >
   > function getCountryFromResourceURI() {
   >
   >     var options = {
   >         method: "GET",
   >         headers: {
   >             "Content-Type": "application/json"
   >         }
   >     };
   >     var requestURL = "http://ip-api.com/json/" + resourceHost;
   >
   >     var response = httpClient.send(requestURL, options).get();
   >
   >     if (response.status === 200) {
   >         var result = JSON.parse(response.text());
   >         if (result) {
   >             return result.country;
   >         }
   >     } else {
   >         logger.error("Error generating IP location: " + response.statusText);
   >     }
   > }
   >
   > function validateAndInitializeParameters() {
   >
   >     var userAddressList = identity.getAttributeValues("postalAddress");
   >     if (userAddressList == null || userAddressList.isEmpty()) {
   >         logger.error("No address specified for user: " + username);
   >         return false;
   >     }
   >     userAddress = userAddressList[0];
   >
   >     if (!environment) {
   >         logger.error("No environment parameters specified in the evaluation request.");
   >         return false;
   >     }
   >     var ipList = environment.get("IP");
   >     if (ipList == null || ipList.length == 0) {
   >         logger.error("No IP specified in the evaluation request environment parameters.");
   >         return false;
   >     }
   >     userIP = ipList[0];
   >
   >     if (!resourceURI) {
   >         logger.error("No resource URI specified.");
   >         return false;
   >     }
   >     resourceHost = resourceURI.match(/^(.*:\/\/)(www\.)?([A-Za-z0-9\-\.]+)(:[0-9]+)?(.*)$/)[3];
   >     return true;
   > }
   > ```

3. Save your changes.

### Create a policy

The policy references the script through environmental conditions.

1. Create a policy set for policies regarding URLs.

   In the AM admin UI, select Realms > *realm name* > Authorization > Policy Sets > + New Policy Set to create a policy set with the following settings:

   * Id

     `am-policy-set`

   * Resource Types

     `URL`

2. Create a policy in the policy set.

   Select Realms > *realm name* > Authorization > Policy Sets > am-policy-set > + Add a Policy to create a policy with the following settings:

   * Name

     `Scripted policy example`

   * Resource Types

     `URL`

   * Resources

     `*://*:*/*`, `*://*:*/*?*`

3. In the new policy, update the settings.

   Allow HTTP GET access by all authenticated users when permitted by the script:

   * Actions

     GET: Allow

   * Subjects

     Type: `Authenticated Users`

   * Environments

     Type: `Script`, Script Name: `Location Authorization Script`

   When modifying settings in the policy editor, select the edit icon [icon: pencil-alt, set=fa]to begin changing the setting, the check icon [icon: check, set=fa]to confirm the change, then Save Changes to commit the change.

4. Verify the policy settings.

   ![Policy settings for the scripted policy example](_images/scripted-policy-example.png)

## Try the demonstration

The `policies?_action=evaluate` endpoint lets a policy administrator make a REST call over HTTP to get a policy decision from AM. AM policy decisions for URL policies show at least the HTTP actions the user can perform. Find more information in [Request policy decisions over REST](rest-api-authz-policy-decisions.html).

Here, when AM grants the user access to complete an HTTP GET request to the resource, the decision includes `"actions":{"GET":true}`. When AM denies access, the decision includes `"actions":{}`.

The REST call to the `policies?_action=evaluate` endpoint requires:

* An SSO token ID for the policy administrator making the request.

* An SSO token ID for the end user attempting to access the resource.

* A request body that specifies who is attempting to access what in what way under what conditions.

  1. Get an SSO token for the policy administrator:

     ```bash
     $ curl \
     --request POST \
     --header 'Content-Type: application/json' \
     --header 'X-OpenAM-Username: policy-admin-username' \
     --header 'X-OpenAM-Password: policy-admin-password' \
     --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
     'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
     {
       "tokenId":"policy-admin-tokenId",
       "successUrl":"/am/console",
       "realm":"/alpha"
     }
     ```

  2. Get an SSO token for the end user:

     ```bash
     $ curl \
     --request POST \
     --header 'Content-Type: application/json' \
     --header 'X-OpenAM-Username: end-user-username' \
     --header 'X-OpenAM-Password: end-user-password' \
     --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
     'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
     {
       "tokenId":"end-user-tokenId",
       "successUrl":"/am/console",
       "realm":"/alpha"
     }
     ```

  3. Request evaluation for a request by an end user in the United States to access a resource located in the United States.

     The script lets users access resources located in their country of residence. AM grants access when both the user's home country and IP address match the resource location.

     ```bash
     $ curl \
     --header 'iPlanetDirectoryPro: policy-admin-tokenId' \
     --request POST \
     --header 'Content-Type: application/json' \
     --header "Accept-API-Version: resource=2.1" \
     --data '{
       "resources": ["https://www.whitehouse.gov:443/about-the-white-house/"],
       "actions": {"GET": true},
       "application": "am-policy-set",
       "subject": {
         "ssoToken": "end-user-tokenId"
       },
       "environment": {
         "IP": ["8.8.8.8"]
       }
     }' \
     'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_action=evaluate'
     [{
       "resource": "https://www.whitehouse.gov:443/about-the-white-house/",
       "actions": {
         "GET": true
       },
       "attributes": {
         "countryOfOrigin": ["United States"]
       },
       "advices": {},
       "ttl": <ttl>
     }]
     ```

     The script adds `"attributes":{"countryOfOrigin":["United States"]}` to the result when AM grants access.

  4. Request evaluation for a request by an end user in France to access a resource located in the United States.

     The user's IP address (`88.174.153.24`) maps to a French location, so no actions are returned:

     ```bash
     $ curl \
     --header 'iPlanetDirectoryPro: policy-admin-tokenId' \
     --request POST \
     --header 'Content-Type: application/json' \
     --header "Accept-API-Version: resource=2.1" \
     --data '{
       "resources": ["https://www.whitehouse.gov:443/about-the-white-house/"],
       "actions": {"GET": true},
       "application": "am-policy-set",
       "subject": {
         "ssoToken": "end-user-tokenId"
       },
       "environment": {
         "IP": ["88.174.153.24"]
       }
     }' \
     'https://am.example.com:8443/am/json/realms/root/realms/alpha/policies?_action=evaluate'
     [{
       "resource": "https://www.whitehouse.gov:443/about-the-white-house/",
       "actions": {},
       "attributes": {},
       "advices": {},
       "ttl": <ttl>
     }]
     ```

     Both the `attributes` and the `actions` fields are empty. To verify the authorization outcome, look for an `Authorization failed` entry in the logs.

## OAuth 2.0 scopes policy script API

To customize OAuth 2.0 scope decisions, configure the `oauth2Scopes` policy with an [environment script condition](policies-ui.html#environments) that references an OAuth 2.0 policy condition script.

The following JavaScript writes the ID of the OAuth 2.0 client to the debug log and then authorizes the request:

```javascript
logger.message("Client ID: " + environment.get("clientId"));
authorized=true;
```

OAuth 2.0 policy condition scripts can access the bindings available to the [policy condition script API](../am-scripting/policy-condition-scripting-api.html), except for the `environment` object. Instead of an IP property, this object returns the ID for the client making the authorization request.

For example, the following shows an `environment` map with a single entry:

```none
"environment": {
    "clientId": [
        "MyOAuth2Client"
    ]
}
```