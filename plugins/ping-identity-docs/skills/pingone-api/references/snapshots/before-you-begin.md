---
title: Before You Begin
description: If you want to start building your own workflows with PingOne APIs, the Use Case Library provides step-by-step workflows with linked Postman collections to help you start using the PingOne APIs in your Postman environment.
component: pingone-api
page_id: pingone-api:before-you-begin:introduction
canonical_url: https://developer.pingidentity.com/pingone-api/before-you-begin/introduction.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc", "platform:working-with-pingone-apis/working-with-pingone-apis.adoc", "platform:working-with-pingone-apis.adoc"]
section_ids:
  pingone-api-domains: PingOne API domains
  the-try-a-request-feature: The Try a Request feature
  calling-the-pingone-apis-from-the-command-line: Calling the PingOne APIs from the command line
  using-postman-collection-level-authorization: Using Postman collection-level authorization
---

# Before You Begin

If you want to start building your own workflows with PingOne APIs, the [Use Case Library](../workflow-library/introduction.html) provides step-by-step workflows with linked Postman collections to help you start using the PingOne APIs in your Postman environment.

For information about how PingOne secures APIs, resources, and data, and what you can do to implement security measures for your PingOne deployment and applications, refer to [Platform security](../foundations/api-security.html).

|   |                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Client developers are responsible for ensuring that applications in their client environment are resilient to non-breaking changes to the PingOne APIs. For information about non-breaking changes and configuring your client environment, refer to [Forward compatibility guidance for PingOne client developers](forward-compatibility.html). |

## PingOne API domains

This section discusses how PingOne API regional endpoints are entered in the domain name system (DNS). In DNS, and in our endpoints, the domain part of the uniform resource locator (URL) comprises three parts separated by periods, such as `api.pingone.com`: one of our service-specific `subdomains`, our PingOne domain name of `pingone`, and one of our `top level domains`.

We use Postman variables to manage this variety of domain parts in PingOne API endpoints. The later discussion is correct regarding the domain part that the variables evaluate to. However, to ease maintenance, the Postman environment template you get when you download a collection uses variables to isolate the TLD from the rest of the domain part and to isolate the domain part from the rest of the endpoint.

The environment template has a path variable for each subdomain. Each path variable uses another variable, `{{tld}}`, for the top level domain (TLD). Such as `https://api.pingone.com/v1` for `{{apiPath}}`. The `tld` variable is first in the environment template that you downloaded.

The table below shows the top level domain value for each region. To change your region, simply change the default `{{tld}}` value from `com` to your region's TLD.

| Region                                      | Code | Top level domain |
| ------------------------------------------- | ---- | ---------------- |
| North America geographic (excluding Canada) | NA   | `com` (default)  |
| Canada region                               | CA   | `ca`             |
| European Union region                       | EU   | `eu`             |
| Australia region                            | AU   | `com.au`         |
| Singapore region                            | SG   | `sg`             |
| Asia-Pacific region                         | AP   | `asia`           |

The PingOne API includes the following domains:

| Domain                               | Postman path variable | Description                                                                                                                                                                             |
| ------------------------------------ | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api.pingone.{{tld}}/v1`             | `{{apiPath}}`         | The primary domain for calling PingOne Management API resource server. **Note**: `/v1` is required for `{{apiPath}}`.                                                                   |
| `auth.pingone.{{tld}}`               | `{{authPath}}`        | The authorization and authentication server domain called to request the access token required to authenticate PingOne API requests. **Note**: do not include `/v1` for `{{authPath}}`. |
| `orchestrate-api.pingone.{{tld}}/v1` | `{{orchestratePath}}` | The primary domain for calling the PingOne DaVinci Management API resource server. **Note**: `/v1` is required for `{{orchestratePath}}`.                                               |
| `scim-api.pingone.{{tld}}`           | `{{scimPath}}`        | PingOne API service for Cross-domain Identity Management (SCIM). **Note**: do not include `/v1` for `{{scimPath}}`.                                                                     |

The `{{…​Path}}` variable in the sample requests stand for the PingOne service endpoint. Refer to [Public endpoints](../foundations/conventions/pingone-api-requests.html) in the Foundations guide for more information.

## The Try a Request feature

Our documentation for the PingOne APIs includes an interactive *Try a Request* feature. *Try a Request* enables you to configure and send a PingOne API request and get a response from within the documentation. This is a quick way to interactively test a PingOne API request without needing to use either Postman or the command line.

Requests in [Authentication and Authorization APIs](../auth/introduction.html) do not have the *Try a Request* feature due to a Cross-Origin Resource Sharing (CORS) constraint.

|   |                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When copying values to populate the fields for a call, the Postman variable (`{{apiPath}}`, `{{orchestratePath}}`, `{{scimPath}}`) cannot contain the `https://` prefix. The *Try a Request* feature for the call (such as, POST) prepopulates a **Protocol** field with the `https://` protocol of the URL. Including `https://` in the Postman variable duplicates the protocol and generates an error. |

## Calling the PingOne APIs from the command line

Each PingOne API request in the documentation includes an example request and response. By default, the example request is displayed using cURL. However, a number of coding languages are available in the associated drop-down list. If you want to run a request from the command line, you can select the coding language and copy the displayed request. You'll need to replace any variables in the request with the appropriate values before running the request.

## Using Postman collection-level authorization

Most APIs require authorization to ensure that client requests access data securely. Postman can pass along whatever authorization details necessary for the method demanded by the endpoint. You can manually include authorization data in the header, body, or as parameters to a request. However, the easiest way is to use the **Authorization** tab in Postman. Select an authorization **Type** on that tab and Postman offers a dialog to gather the information required by that **Type**. When you run a request, Postman uses the information from the **Authorization** tab to automatically add the necessary authorization header, body, or parameters to the request. Postman offers the **Authorization** tab on requests, folders, and collections.

In PingOne collections, the authorization method is defined at the collection level. Only those requests that require a specific authorization method have authorization defined on the request (roughly 10% of PingOne requests). This allows you to easily change the authorization used for most requests. Refer to [Postman Collection-Level Authorization](../foundations/authentication-concepts/postman-collection-level-authorization.html) for more information.
