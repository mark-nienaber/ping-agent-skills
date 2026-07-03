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