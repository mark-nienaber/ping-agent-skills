---
title: Groovy in PingAccess
description: PingAccess provides the Groovy script and OAuth Groovy script rule types, which enable the use of Groovy, a dynamic programming language for the Java Virtual Machine (JVM).
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_groovy_in_pa
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_groovy_in_pa.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 26, 2023
---

# Groovy in PingAccess

PingAccess provides the Groovy script and OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* Groovy script rule types, which enable the use of Groovy, a dynamic programming language for the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)*.

Groovy scripts provide advanced rule logic that extends PingAccess rule development beyond the capabilities of the packaged rules. For more information, see the [Groovy documentation](http://groovy-lang.org/documentation.html).

Groovy scripts have access to important PingAccess runtime objects, such as the [Exchange](pa_exchange_object_ref.html) and [PolicyContext](pa_policycontext_object_ref.html) objects, which the scripts can interrogate and modify.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Groovy script rules](../pingaccess_user_interface_reference_guide/pa_adding_groovy_script_rules.html) and [OAuth Groovy script rules](../pingaccess_user_interface_reference_guide/pa_adding_oauth_groovy_script_rules.html) must end execution with a matcher instance. For more information, see [Matcher usage reference](pa_matcher_usage_ref.html).Groovy functions treat strings literally, and matchers perform case-sensitive string evaluation unless otherwise specified. For example, in the following line of code, the `caseSensitive` parameter determines whether the Groovy function performs case-sensitive comparison on the value.```
requestHeaderContains(Map<String, String> fieldValuesMap, boolean caseSensitive)
``` |

> **Collapse: Rule processing**
>
> Groovy script rules are invoked during the request processing phase of an exchange, allowing the script to modify the request before it is sent to the server. Groovy script rules are also invoked during the response, allowing the script to modify the response before it is returned to the client.
>
> |   |                                                                                                                          |
> | - | ------------------------------------------------------------------------------------------------------------------------ |
> |   | You can't access a mediated token through a Groovy rule because token mediation occurs after PingAccess rule processing. |
>
> The following diagram highlights the flow of rule processing.
>
> ![byy1564006721382](_images/byy1564006721382.png)

> **Collapse: Processing steps**
>
> 1. During request processing, rules associated with the application are evaluated.
>
> 2. The request passes through each of the rules before PingAccess allows it to proceed.
>
> 3. The response passes through the rules in a manner based on your deployment:
>
>    * In a proxy deployment, the response from the site passes through each of the rules.
>
>    * In an agent deployment, the response to the agent indicating the policy approval or denial passes through each of the rules.

---

---
title: Groovy script examples
description: The following examples show possible uses for Groovy scripts.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_groovy_script_examples
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_groovy_script_examples.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  oauth-policy-context-example: OAuth Policy context example
---

# Groovy script examples

The following examples show possible uses for Groovy scripts.

## OAuth Policy context example

In some instances, it might be necessary to transmit identity information to sites to provide details of the user attempting to access a site. In such instances, Groovy scripts can be used to inject identity information into various portions of the HTTP request *(tooltip: \<div class="paragraph">
\<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
\</div>)* to the target.

In this example, the site is expecting the identity of the user to be conveyed through the `User` HTTP header *(tooltip: \<div class="paragraph">
\<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
\</div>)*. You can accomplish this using the OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* Groovy script rule and the following Groovy script:

```
user=policyCtx?.context.get("oauth_token")?.attributes?.get("user")?.get(0)
exc?.request?.header?.add("User", "$user")
pass()
```

* More complex Groovy script logic

  ```
  test = exc?.request?.header?.getFirstValue("test");
  if(test != null && test.equals("foo"))
  {
    //rule will fail evaluation if Test header has value 'foo'
    fail()
  }
  else
  {
    //rule will pass evaluation is Test header has value of anything else
    //or isn't present
    pass()
  }
  ```

* Set an exchange property named `com.pingidentity.policy.error.info`

  This value will be available for the `$info` variable in error templates when an error is encountered. The `$info` variable can be set by a Groovy Script rule or an OAuth Groovy script rule.

  ```
  exc?.setProperty("com.pingidentity.policy.error.info", "this value will be passed to the template in $info variable")
  not(anything())
  ```

* Create a whitelisting rule for certain characters

  ```
  if (!exc?.request?.uri?.matches("[\\p{Po}\\p{N}\\p{Z}\\p{L}\\p{M}\\p{Zs}\\./_\\-\\()\\{\\}\\[\\]]*"))
   {
    fail()
   }
   else
   {
    pass()
   }
  ```

* Add a cookie to the response

  ```
  // Construct the cookie value
  value = "cookie-value"
  cookieHeaderFieldValue = "ResponseTestCookie=${value}; Path=/"

  // Add the cookie on to the response
  exc?.response?.header?.add("Set-Cookie", cookieHeaderFieldValue)

  pass()
  ```

* Combine an `AND` and `OR`, invoking an existing rule matcher

  ```
  if ((anyOf(containsWebSessionAttribute("engineering", "true"), containsWebSessionAttribute("marketing", "true")) && (containsWebSessionAttribute("manager", "true")))
  {pass()
  }
  else{
  fail()
  }
  ```

---

---
title: Groovy Scripts
description: Groovy scripts provide advanced rule logic that extends PingAccess rule development beyond the capabilities of the packaged rules.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_groovy_scripts
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_groovy_scripts.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  matchers: Matchers
  objects: Objects
  debuggingtroubleshooting: Debugging/troubleshooting
---

# Groovy Scripts

Groovy scripts provide advanced rule logic that extends PingAccess rule development beyond the capabilities of the packaged rules.

Groovy scripts have access to important PingAccess runtime objects, such as the [Exchange](pa_exchange_object_ref.html) and [PolicyContext](pa_policycontext_object_ref.html) objects, which the scripts can interrogate and modify. Groovy script rules are invoked during the request processing phase of an exchange, allowing the script to modify the request before it is sent to the server. Groovy script rules are also invoked during the response, allowing the script to modify the response before it is returned to the client. See [Groovy](pa_groovy_in_pa.html) for more information about Groovy.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | Through Groovy scripts, PingAccess administrators can perform sensitive operations that could affect system behavior and security. |

## Matchers

Groovy scripts must end execution with a matcher instance. Matchers provide a framework for establishing declarative rule matching objects. You can use a matcher from the list of [PingAccess Matchers](pa_matcher_usage_ref.html) or from the [Hamcrest library](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/CoreMatchers.html).

The following are Hamcrest method examples for constructing access control policies with the web session attribute rule using evaluations such as an `OR` group membership evaluation.

* allOf

  Matches if the examined object matches all of the specified matchers. In this example, the user needs to be in both the sales and managers groups for this rule to pass.

  ```
  allOf(containsWebSessionAttribute("group","sales"), containsWebSessionAttribute("group","managers"))
  ```

* anyOf

  Matches any of the specified matchers. In this example, the rule passes if the user is in any of the specified groups.

  ```
  anyOf(containsWebSessionAttribute("group","sales"), containsWebSessionAttribute("group","managers"), containsWebSessionAttribute("group","execs"))
  ```

* not

  Inverts the logic of a matcher to not match. In this example, the rule fails if the user is in both the sales and the managers groups.

  ```
  not(allOf(containsWebSessionAttribute("group", "sales"), containsWebSessionAttribute("group", "managers")))
  ```

See [Matchers](pa_matcher_usage_ref.html) for more information.

## Objects

The following objects are available in Groovy. For more information on an object, click the link.

* [Exchange Object](pa_exchange_object_ref.html)

  Contains the HTTP request *(tooltip: \<div class="paragraph">
  \<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
  \</div>)* and the HTTP response for the transaction processed by PingAccess.

* [PolicyContext Object](pa_policycontext_object_ref.html)

  Contains a map of objects needed to perform policy decisions. The contents of the map vary based on the context of the current user flow.

* [Request Object](pa_request_object_ref.html)

  Contains all information related to the HTTP request made to an application.

* [Response Object](pa_response_object_ref.html)

  Contains all information related to the site HTTP response.

* [Method Object](pa_method_object_ref.html)

  Contains the HTTP method name from the request made to an application.

* [Header Object](pa_headers_object_ref.html)

  Contains the HTTP header information from the request made to an application or the HTTP header from a Site response.

* [Body Object](pa_body_object_ref.html)

  Contains the HTTP body from the application request or the HTTP body from the site response.

* [OAuthToken Object](pa_oauth_token_object_ref.html)

  Contains the OAuth *(tooltip: \<div class="paragraph">
  \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
  \</div>)* access token and related identity attributes.

* [Logger Object](pa_logger_object_ref.html)

  Configure and view the state of logging.

* [MediaType Object](pa_mediatype_object_ref.html)

  Contains information related to the media type.

## Debugging/troubleshooting

Groovy script rules are evaluated when saved to ensure that they are syntactically valid. If a Groovy script rule fails to save, hover over the information icon to view additional information about the reason for the failure.

If a rule fails when it is run, information about the failure is added to the `<PA_HOME>/log/pingaccess.log` file.

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | Some error messages about Groovy rule failures are only logged if `DEBUG` level output is enabled for the `com.pingidentity` logger. |

---

---
title: Headers object reference
description: Access the Headers object in Groovy exc?.request?.header or exc?.response?.header.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_headers_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_headers_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  purpose: Purpose
  examplegroovy-sample: ExampleGroovy sample
  method-summary: Method summary
  groovyheaderfield-object: GroovyHeaderField object
  examplegroovy-sample-2: ExampleGroovy sample
---

# Headers object reference

Access the Headers object in Groovy `exc?.request?.header` or `exc?.response?.header`.

## Purpose

The Headers object contains the HTTP header *(tooltip: \<div class="paragraph">
\<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
\</div>)* information from the request made to an application or the HTTP header from a site response. The [Request](pa_request_object_ref.html) HTTP header is sent on to the site after the rules are evaluated. The [Response](pa_response_object_ref.html) HTTP header is returned to the client after the Response rules are evaluated.

Use the Headers object to add custom HTTP headers for a site, as demonstrated in the following example:

## ExampleGroovy sample

```
if ( !(exc.response) )
{
     // Set a custom header for the Site request
     def header = exc?.request?.header
     header?.add("X-PINGACCESS-SAMPLE", "SUCCESS")
}
pass()
```

## Method summary

| Method                                                    | Description                                                                                                                                                                                                                                                     |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `void add(String key, String val)`                        | Adds HTTP header fields for the request.&#xA;&#xA;If you use Groovy Rules to inject HTTP headers for the backend protected application, the script must sanitize the same headers from the original client request.                                             |
| `String getAccept()`                                      | Returns the acceptable response Content-Types expected by the User-Agent.                                                                                                                                                                                       |
| `void setAccept(String value)`                            | Sets the acceptable response Content-Types expected by the User-Agent.                                                                                                                                                                                          |
| `String getAuthorization()`                               | Returns the authentication credentials for HTTP authentication.                                                                                                                                                                                                 |
| `void setAuthorization(String username, String password)` | Sets authentication credentials for HTTP authentication.                                                                                                                                                                                                        |
| `String getConnection()`                                  | Returns the connection type preferred by the User-Agent.                                                                                                                                                                                                        |
| `void setConnection(List<String> values)`                 | Sets the connection type preferred by the User-Agent.                                                                                                                                                                                                           |
| `int getContentLength()`                                  | Returns the request body content length.                                                                                                                                                                                                                        |
| `void setContentLength(int length)`                       | Sets the request body content length.                                                                                                                                                                                                                           |
| `MediaType getContentType()`                              | Returns media type of Header with content type                                                                                                                                                                                                                  |
| `void setContentType(String)`                             | Sets the request body MIME type.                                                                                                                                                                                                                                |
| `Map <String, String[]> getCookies()`                     | Returns all cookies sent with the request.                                                                                                                                                                                                                      |
| `void setCookie(String)`                                  | Overwrites the request's cookie header with the passed string. This method cannot be used to set cookies in the response header.                                                                                                                                |
| `String getFirstCookieValue(String)`                      | Returns the first cookie in the cookie header.                                                                                                                                                                                                                  |
| `String getFirstValue(String)`                            | Returns the first value of the HTTP header specified by the name.                                                                                                                                                                                               |
| `void setDate(Date date)`                                 | Sets the date of the message in the Date HTTP header.                                                                                                                                                                                                           |
| `List<GroovyHeaderField> getAllHeaderFields()`            | Returns a list of GroovyHeaderFields.                                                                                                                                                                                                                           |
| `String getHost()`                                        | Returns the host name specified in the request.                                                                                                                                                                                                                 |
| `void setHost(String value)`                              | Sets the host name for the request to the Site.                                                                                                                                                                                                                 |
| `String getLocation()`                                    | Gets the redirect location Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">&#xA;\<p>Identifies a resource according to its internet location.\</p>&#xA;\</div>)* for the response.                                                            |
| `void setLocation(String value)`                          | Sets the redirect location URL for the response.                                                                                                                                                                                                                |
| `String getProxyAuthorization()`                          | Returns the proxy credentials.                                                                                                                                                                                                                                  |
| `void setProxyAuthorization(String value)`                | Sets the request proxy credentials.                                                                                                                                                                                                                             |
| `void setServer(String value)`                            | Sets the server name for the response.                                                                                                                                                                                                                          |
| `List<String> getValues(String name)`                     | Returns a list of string values for the supplied header name.                                                                                                                                                                                                   |
| `String getXForwardedFor()`                               | Returns the originating Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* address of the client and the proxies, if set. |
| `void setXForwardedFor(String value)`                     | Sets the IP address for the client and the proxies.                                                                                                                                                                                                             |
| `boolean removeContentEncoding()`                         | Removes the Content-Encoding header value. Returns true if the value has been removed.                                                                                                                                                                          |
| `boolean removeContentLength()`                           | Removes the Content-Length header value. Returns true if the value has been removed.                                                                                                                                                                            |
| `boolean removeContentType()`                             | Removes the Content-Type header value. Returns true if the value has been removed.                                                                                                                                                                              |
| `boolean removeExpect()`                                  | Removes the Expect header value. Returns true if the value has been removed.                                                                                                                                                                                    |
| `boolean removeFields(String name)`                       | Removes the header value specified by the name parameter. Returns true if the value has been removed.                                                                                                                                                           |
| `boolean removeTransferEncoding()`                        | Removes the Transfer-Encoding header value. Returns true if the value has been removed.                                                                                                                                                                         |

## GroovyHeaderField object

**Method summary**

| Method                              | Description                 |
| ----------------------------------- | --------------------------- |
| `String getValue();`                | Returns the string's value. |
| `GroovyHeaderName getHeaderName();` | Returns the header's name.  |

## ExampleGroovy sample

The following example demonstrates usage of the `getAllHeaderFields()` method, which includes both request and response logging:

```
exc?.log.info "Display Headers: "
exc?.log.info "-->Request Headers"
reqHdrs = exc?.request?.header?.getAllHeaderFields()
reqLoop = reqHdrs?.iterator()
while (reqLoop?.hasNext()) {
  hdr = reqLoop?.next()
  exc.log.info "-->reqHeader  Name: "+hdr?.getHeaderName()?.toString()
  exc.log.info "-->reqHeader Value: "+ hdr?.getValue()
}
exc?.log.info "-->Response Headers"
exc?.log.debug "-->Response HTTP Status: "+ exc?.response?.statusCode
rspHdrs = exc?.response?.header?.getAllHeaderFields()
rspLoop = rspHdrs?.iterator()
while (rspLoop?.hasNext()) {
  hdr = rspLoop?.next ()
  exc.log.info "-->rspHeader  Name: "+ hdr?.getHeaderName()?.toString()
  exc.log.info "-->rspHeader Value: "+ hdr?.getValue()
}
exc?.log.info "Display Headers EOF: "
pass()
```

---

---
title: Heartbeat endpoint
description: The heartbeat endpoint verifies that the PingAccess server is running and, depending on your security settings, can display configuration details.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_heartbeat_endpoint
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_heartbeat_endpoint.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2026
section_ids:
  paheartbeat-ping: /pa/heartbeat.ping
  making-a-heartbeat-call: Making a heartbeat call
  interpreting-the-results: Interpreting the results
---

# Heartbeat endpoint

The heartbeat endpoint verifies that the PingAccess server is running and, depending on your security settings, can display configuration details.

## /pa/heartbeat.ping

This endpoint returns a 200 HTTP status code and a message body of `OK` if the target PingAccess server is up and functional. You can customize the message by modifying a PingAccess property and a Velocity template file. Learn more in [Customizing the heartbeat message](../pingaccess_monitoring_guide/customizing_the_heartbeat_message.html).

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If a GET request receives a connection error or an HTTP status code other than 200, the server associated with the endpoint is down or malfunctioning. |

Load balancers can use the heartbeat endpoint to determine PingAccess's status.

## Making a heartbeat call

You can make a heartbeat call to any active PingAccess listener and on any node in a PingAccess cluster. For example, with default port configurations:

* A clustered console replica responds to this endpoint on port 9000.

* A clustered engine responds on port 3000.

The URL should begin with the server name and the PingAccess runtime port number. For example, `https://hostname:3000/pa/heartbeat.ping`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you selected the **Use context root as reserved resource base path** check box on your PingAccess application, this feature creates an instance of any reserved PingAccess resources under the application's context root. As such, the context root of the application needs to prepend the reserved context application root (`/pa` by default) in any file paths that reference it.If the context root of your application is `myApp`, the path to the heartbeat endpoint would be `myApp/pa/heartbeat.ping` and the URL would be `https://hostname:3000/myApp/pa/heartbeat.ping` instead. |

Calls to this endpoint can be logged in the audit log. You can enable heartbeat call logging using the `/httpConfig/monitoring` administrative endpoint. Learn more in [Administrative API endpoints](pa_admin_api_endpoints.html).

## Interpreting the results

The heartbeat endpoint can return either a short or detailed status for the target PingAccess server, based on the value of the `enable.detailed.heartbeat.response` property in the `run.properties` file. The default value is `false`.

* If `enable.detailed.heartbeat.response` is set to `false` and the PingAccess instance is running, the endpoint returns an HTTP 200 status code and a message body of `OK`.

* If `enable.detailed.heartbeat.response` is set to `true` and the PingAccess instance is running, the endpoint returns a configurable status with additional details. The response output format is an Apache Velocity template defined in `<PA_HOME>/conf/template/heartbeat.page.json`. You can modify this template to suit your needs. Learn more in [Customizing the heartbeat message](../pingaccess_monitoring_guide/customizing_the_heartbeat_message.html).

* If the endpoint returns an error, this indicates that the PingAccess instance associated with the endpoint is down.

---

---
title: Identity object reference
description: The Identity object contains information about the authenticated identity associated with the current HTTP request.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_identity_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_identity_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  groovy-sample: Groovy sample
  method-summary: Method summary
---

# Identity object reference

The Identity object contains information about the authenticated identity associated with the current HTTP request.

## Groovy sample

```
// Only allow access for an identity with subject "user"
def subject = exc?.identity?.subject

if ("user".equals(subject)) {
  pass()
} else {
  fail()
}
```

## Method summary

| Method                      | Description                                                                                                                                                                                                                                                                                                                  |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `String getSubject()`       | Returns the subject of the identity.                                                                                                                                                                                                                                                                                         |
| `String getMappedSubject()` | Returns the subject set by the identity mapping. If there is no identity mapping associated with the application, the return value will be null. If there is an identity mapping associated with the application, but the identity mapping did not determine a subject to map, the returned value might be the empty string. |
| `String getTrackingId()`    | Returns the tracking identifier used in PingAccess logs. This value is not guaranteed to be globally unique and should be used for diagnostic purposes only.                                                                                                                                                                 |
| `String getTokenId()`       | Returns the unique ID for the associated authentication token. This value might change when new tokens are issued for the same identity.                                                                                                                                                                                     |
| `Date getTokenExpiration()` | Returns a Date object representing the time at which the authentication token expires. This might be null if the authentication provider did not indicate an expiry.                                                                                                                                                         |
| `JsonNode getAttributes()`  | Returns a JsonNode object representing the attributes of the identity.                                                                                                                                                                                                                                                       |

---

---
title: Increasing file descriptor limits (systemd)
description: Increase file descriptor limits in a systemd environment to enable PingAccess to handle a high volume of concurrent requests.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_increasing_file_descriptor_limits_systemd
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_increasing_file_descriptor_limits_systemd.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  steps: Steps
---

# Increasing file descriptor limits (systemd)

Increase file descriptor limits in a systemd environment to enable PingAccess to handle a high volume of concurrent requests.

## Steps

1. Edit the `/etc/systemd/system/pingaccess.service` file.

2. Modify the following line under the `[Service]` section:

   ```
   LimitNOFILE=<value>
   ```

   *\<value>* is the new value. The default value of 65536 (64K) should be sufficient for most environments.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The number of open file descriptors is limited by the physical memory available to the host. You can determine this limit with the following command:```
   cat /proc/sys/fs/file-max
   ```If the file-max value is significantly higher than the 65536 limit, consider increasing the file descriptor limit to between 10% and 15% of the system-wide file descriptor limit. For example, if the file-max value is 810752, you can set the file descriptor limit to 100000. If the file-max value is lower than 65536, the host is likely not sized appropriately for PingAccess. |

3. Run the following command as root:

   ```
   systemctl daemon-reload
   ```

4. Restart the PingAccess service.

---

---
title: Increasing file descriptor limits (systemv)
description: Increase file descriptor limits in a systemv environment to enable PingAccess to handle a high volume of concurrent requests.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_increasing_file_descriptor_limits_systemv
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_increasing_file_descriptor_limits_systemv.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  steps: Steps
---

# Increasing file descriptor limits (systemv)

Increase file descriptor limits in a systemv environment to enable PingAccess to handle a high volume of concurrent requests.

## Steps

1. Edit the `/etc/security/limits.conf` file.

2. Add or modify the following lines:

   ```
   <pingAccessAccount>  soft nofile  <value>
   <pingAccessAccount>  hard nofile  <value>
   ```

   `<pingAccessAccount>` is the user account used to run the PingAccess java process, or `*` for all users, and *\<value>* is the new value. A value of 65536 (64K) should be sufficient for most environments.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The number of open file descriptors is limited by the physical memory available to the host. You can determine this limit with the following command:```
   cat /proc/sys/fs/file-max
   ```If the file-max value is significantly higher than the 65536 limit, consider increasing the file descriptor limit to between 10% and 15% of the system-wide file descriptor limit. For example, if the file-max value is 810752, you could set the file descriptor limit to 100000. If the file-max value is lower than 65536, the host is likely not sized appropriately for PingAccess. |

---

---
title: Increasing the number of available ephemeral ports
description: Increase the number of available ephemeral ports to prevent deployment issues, particularly in high capacity environments.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_increasing_the_number_of_available_ephemeral_ports
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_increasing_the_number_of_available_ephemeral_ports.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Increasing the number of available ephemeral ports

Increase the number of available ephemeral ports to prevent deployment issues, particularly in high capacity environments.

## About this task

This setting increases the performance and capacity of network, specifically the TCP socket, connectivity, enabling PingAccess to handle a high volume of concurrent requests.

## Steps

1. View the ephemeral ports with the `netsh int ipv4 show dynamicportrange tcp` command.

2. Increase the ephemeral ports with the `netsh int ipv4 set dynamicport tcp start=1025 num=64510` command.

3. Reboot the machine.

4. View and confirm the updated port range with the `netsh int ipv4 show dynamicportrange tcp` command.

---

---
title: Java tuning
description: One of the most important tuning options you can apply to the Java Virtual Machine (JVM) is to configure how much heap (memory for runtime objects) to use.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_java_tuning
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_java_tuning.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
---

# Java tuning

One of the most important tuning options you can apply to the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* is to configure how much heap (memory for runtime objects) to use.

The JVM grows the heap from a specified minimum to a specified maximum. If you have sufficient memory, fix the size of the heap by setting minimum and maximum to the same value. This allows the JVM to reserve its entire heap at startup, optimizing organization and eliminating potentially expensive resizing.

By default, PingAccess fixes the Java heap at 512 megabytes (MB). This is a fairly small footprint and not optimal for supporting higher concurrent user loads over extended periods of activity. If you expect your deployment of PingAccess to serve more than 50 concurrent users, per PingAccess node, if deploying a cluster, increase the heap size.

For more information, see the following topics:

* [Configuring JVM crash log in Java startup](pa_configuring_jvm_crash_log_in_java_startup.html)

* [Configuring memory dumps in Java startup](pa_configuring_memory_dumps_in_java_startup.html)

* [Modifying the Java heap size](pa_modifying_the_java_heap_size.html)

---

---
title: JsonNode object reference
description: The JsonNode object represents the attributes of an identity.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_jsonnode_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_jsonnode_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  groovy-sample: Groovy sample
  method-summary: Method summary
  remarks: Remarks
---

# JsonNode object reference

The JsonNode object represents the attributes of an identity.

## Groovy sample

```
// Only allow access if the user is in the group "staff"
def groups = exc?.identity?.attributes?.get("groups")

foundGroup = falseif (groups) {
  for (group in groups) {
    if ("staff".equals(group.asText())) {
      foundGroup = truebreak
    }
  }
}

if (foundGroup) {
  pass()
} else {
  fail()
}
```

## Method summary

| Method                                    | Description                                                                                                                                                                                                                                                                                           |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `JsonNode get(String fieldName)`          | Gets the JsonNode representing a field of this JsonNode. This method will return null if no field exists with the specified name.                                                                                                                                                                     |
| `boolean has(String fieldName)`           | Returns true if this JsonNode has a field with the specified name.                                                                                                                                                                                                                                    |
| `java.util.Iterator<String> fieldNames()` | Returns an java.util.Iterator providing access to the names of all the fields of this JsonNode.                                                                                                                                                                                                       |
| `boolean isTextual()`                     | Returns true if this JsonNode represents a string value.                                                                                                                                                                                                                                              |
| `String asText()`                         | Returns a string representation of this JsonNode. If this JsonNode is an array or object, this will return an empty string.                                                                                                                                                                           |
| `int intValue()`                          | Returns an integer representation of this JsonNode. If this JsonNode does not represent a number, 0 is returned.                                                                                                                                                                                      |
| `boolean isArray()`                       | Returns true if this JsonNode is an array.                                                                                                                                                                                                                                                            |
| `boolean isObject()`                      | Returns true if this JsonNode is an object.                                                                                                                                                                                                                                                           |
| `int size()`                              | For an array JsonNode, returns the number of elements in the array. For an object JsonNode, returns the number of fields in the object. 0 otherwise.                                                                                                                                                  |
| `java.util.Iterator<JsonNode>iterator()`  | Returns an java.util.Iterator over all JsonNode objects contained in this JsonNode. For an array JsonNode, the returned java.util.Iterator will iterate over all the elements in the array. For an object JsonNode, the returned java.util.Iterator will iterate over all field values in the object. |

## Remarks

A JsonNode implements java.lang.Iterable*\<JsonNode>* so a for loop can be used to iterate over all the elements in an array JsonNode or the field values in an object JsonNode.

---

---
title: Linux tuning
description: This section describes tuning recommendations for the Linux operating system environment.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_linux_tuning
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_linux_tuning.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Linux tuning

This section describes tuning recommendations for the Linux operating system environment.

Implement these recommendations to prevent deployment issues, particularly in high capacity environments. The following settings will increase the performance and capacity of the networking, particularly TCP, stack, and file descriptor usage, respectively, enabling PingAccess to handle a high volume of concurrent requests.

For more information, see the following topics:

* [Tuning network and TCP settings](pa_tuning_network_and_tcp_settings.html)

* [Increasing file descriptor limits (systemv)](pa_increasing_file_descriptor_limits_systemv.html)

* [Increasing file descriptor limits (systemd)](pa_increasing_file_descriptor_limits_systemd.html)

---

---
title: Logger object reference
description: This object accesses the Logger object.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_logger_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_logger_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  configuration: Configuration
  method-summary: Method summary
---

# Logger object reference

This object accesses the Logger object.

## Configuration

PingAccess must be configured to accept logging from Groovy rules.

In the `conf/log4j2.xml` file, uncomment or add the following line to enable debug-level logging from Groovy rules.

```
<AsyncLogger name="GroovyRule" level="DEBUG"/>
```

Uncomment or add the following line to enable info-level logging from the *\<RuleName>* Groovy rule.

```
<AsyncLogger name="GroovyRule.<RuleName>" level="INFO"/>
```

## Method summary

| Method                                          | Description                                                                |
| ----------------------------------------------- | -------------------------------------------------------------------------- |
| `void trace(String format, Object…​ arguments)` | Logs a `TRACE` level message based on the specified format and arguments.  |
| `void debug(String format, Object…​ arguments)` | Logs a `DEBUG` level message based on the specified format and arguments.  |
| `void info(String format, Object…​ arguments)`  | Logs an `INFO` level message based on the specified format and arguments.  |
| `void warn(String format, Object…​ arguments)`  | Logs a `WARN` level message based on the specified format and arguments.   |
| `void error(String format, Object…​ arguments)` | Logs an `ERROR` level message based on the specified format and arguments. |
| `boolean isTraceEnabled()`                      | Checks if the logger instance is enabled for the `TRACE` level.            |
| `boolean isDebugEnabled()`                      | Checks if the logger instance is enabled for the `DEBUG` level.            |
| `boolean isInfoEnabled()`                       | Checks if the logger instance is enabled for the `INFO` level.             |
| `boolean isWarnEnabled()`                       | Checks if the logger instance is enabled for the `WARN` level.             |
| `boolean isErrorEnabled()`                      | Checks if the logger instance is enabled for the `ERROR` level.            |

---

---
title: Logging and Auditing
description: PingAccess uses a high performance, asynchronous logging framework to provide logging and auditing services with the lowest possible impact to overall application performance.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_logging_and_auditing
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_logging_and_auditing.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 16, 2024
section_ids:
  logging: Logging
  auditing: Auditing
---

# Logging and Auditing

PingAccess uses a high performance, asynchronous logging framework to provide logging and auditing services with the lowest possible impact to overall application performance.

## Logging

Modify your logging settings to increase performance.

Although logging is handled by a high performance, asynchronous logging framework, it is more efficient for the system overall to log the minimum amount of information required. Review the [logging section of the documentation](../configuring_and_customizing_pingaccess/pa_logging_configuration.html) and adjust the logging level to the lowest level that suits your needs.

## Auditing

Modify your environment's auditing settings based on your security and performance needs.

As with logging, auditing is provided by the same high performance, asynchronous logging framework. Auditing messages can be written to a database instead of flat files, decreasing file I/O.

If you do not require auditing for interactions with a resource or between PingAccess and PingFederate, it is more efficient to disable audit logging. However, if you do require auditing services and have access to a Relational Database Management System (RDBMS), audit to a database. You will see a decrease in disk I/O, which might result in increased performance, depending on database resources.

---

---
title: Manually promoting the replica administrative node
description: To promote the replica admin manually:
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_manually_promoting_the_replica_admin_node
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_manually_promoting_the_replica_admin_node.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Manually promoting the replica administrative node

## About this task

To promote the replica admin manually:

## Steps

1. Open the `<PA_HOME>/conf/run.properties` file in a text editor.

2. Locate the `pa.operational.mode` line and change the value from `CLUSTERED_CONSOLE_REPLICA` to `CLUSTERED_CONSOLE`.

   These properties are case-sensitive.

   |   |                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Do not restart the replica node during the promotion process. PingAccess can detect and apply this change without a restart, and restarting the node during its promotion can cause file corruption or failure to promote correctly. |

## Next steps

Complete [Reinstating a replica administrative node after failing over](pa_reinstating_a_replica_admin_node_after_failing_over.html).

---

---
title: Matcher usage reference
description: Groovy script rules and OAuth Groovy script rules must end execution with a matcher instance. Matchers provide a framework for establishing declarative rule matching objects.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_matcher_usage_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_matcher_usage_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 26, 2023
section_ids:
  pingaccess-matchers: PingAccess matchers
---

# Matcher usage reference

Groovy script rules and OAuth Groovy script rules must end execution with a matcher instance. Matchers provide a framework for establishing declarative rule matching objects.

You can use a matcher from the list of PingAccess matchers or from the [Hamcrest library](http://hamcrest.org/JavaHamcrest/javadoc/1.3/org/hamcrest/CoreMatchers.html).

* For more information on Hamcrest, see the [Hamcrest Tutorial](http://code.google.com/p/hamcrest/wiki/Tutorial).

* For more information on creating and troubleshooting Groovy scripts, and examples of how you might use Hamcrest matchers instead of PingAccess matchers, see [Groovy Scripts](pa_groovy_scripts.html).

* For more information on PingAccess matchers, review the following examples and tables.

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Matcher string evaluation is case sensitive unless otherwise specified. In the PingAccess matchers table, case insensitivity is called out in a matcher's description when applicable. |

> **Collapse: Examples**
>
> In the following example, the Groovy script rule inserts a custom HTTP header *(tooltip: \<div class="paragraph">
> \<p>A section of an HTTP request or response that conveys additional information relevant to the client or server in the transaction.\</p>
> \</div>)* and the script ends with a call to the `pass()` matcher. The `pass()` matcher signals that the rule has passed.
>
> ```
> test = "let's get Groovy!"
> exc?.response?.header?.add("X-Groovy", "$test")
> pass()
> ```
>
> In the following example, the OAuth *(tooltip: \<div class="paragraph">
> \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
> \</div>)* Groovy script rule checks the HTTP method and confirms the OAuth scope, and a matcher is evaluated at the end of each line of execution. The first matcher is the `hasScope()` matcher, which confirms whether the OAuth access token has the `WRITE` scope. If it does, the rule passes.
>
> ```
> //Get the HTTP method name
> def methodName = exc?.request?.method?.methodName()
> if (methodName == "POST") {
>     hasScope("WRITE")
> } else {
>     fail()
> }
> ```
>
> The `fail()` matcher combination is only evaluated when the `methodName` does not equal `POST`. This matcher combination evaluates to false.

## PingAccess matchers

The following table lists the PingAccess matchers available for the [Groovy script rule](../pingaccess_user_interface_reference_guide/pa_adding_groovy_script_rules.html) and the [OAuth Groovy script rule](../pingaccess_user_interface_reference_guide/pa_adding_oauth_groovy_script_rules.html).

> **Collapse: Groovy and OAuth Groovy script rule matchers**
>
> | Matcher                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `pass()`                                                                                                                                              | Signals that the rule has passed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `fail()`                                                                                                                                              | Signals that the rule has failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `inIpRange(String cidr)`                                                                                                                              | Validates the source Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* address of the request against the `cidr` string parameter in CIDR notation. When source IP headers defined in the [HTTP Requests](../pingaccess_user_interface_reference_guide/pa_http_requests.html) page are found, the source IP address determined from those headers is used as the source address.For agents, this value is potentially controlled by the override options on the agent settings.**Example:** `inIpRange("127.0.0.1/8")`                                                                                                                                                        |
> | `inIpRange(java.net.InetAddress ipAddress, int prefixSize)`                                                                                           | Validates the source IP address against the `ipAddress` and the `prefixSize` parameters specified individually. When source IP headers defined in the [HTTP Requests](../pingaccess_user_interface_reference_guide/pa_http_requests.html) page are found, the source IP address determined from those headers is used as the source address.For agents, this value is potentially controlled by the override options on the agent settings.**Example:** `inIpRange(InetAddress.getByName("127.0.0.1"),8)`is equivalent to  `inIpRange("127.0.0.1/8")`                                                                                                                                                                                                                                                                |
> | `inIpRange(String cidr, String listValueLocation, boolean fallBackToLastHopIp, String…​ headerNames)`                                                 | Validates the source IP address in the first of the specified `headerNames` using the `cidr` value. Can be specified as part of a Groovy script as a means of overriding the configuration stored in PingAccess for a specific Groovy script rule.Valid values for the `listValueLocation` parameter are `FIRST`, `LAST`, and `ANY`. This parameter controls where, in a multivalued list of source IP addresses, the last source should be taken from. If `ANY` is used, if any of the source IP addresses in a matching header match the CIDR value, the matcher evaluates to `true`.**Example:** `inIpRange("127.0.0.1/8", "LAST", true, "X-Forwarded-For", "Custom-Source-IP")`                                                                                                                                  |
> | `inIpRange(java.net.InetAddress address, int prefixSize, String listValueLocation, boolean fallBackToLastHopIp, String…​ headerName)`                 | Validates the source IP address in the first of the specified `headerNames` using the `address` and `prefixSize` values. In all other respects, this matcher behaves the same as the version that uses a `cidr` value for comparison.**Example:** `inIpRange(InetAddress.getByName("127.0.0.1"), 8, "LAST", true, "X-Forwarded-For", "Custom-Source-IP")`                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | `requestXPathMatches(String xPathString, String xPathValue)`                                                                                          | Validates that the value returned by the `xPathString` parameter is equal to the `xPathValue` parameter.**Example:** `requestXPathMatches("//header[@name='Host']/text()","localhost:3000")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | `inTimeRange(String startTime, String endTime)`                                                                                                       | Validates that the current server time is between the `startTime` and `endTime` parameters.**Example:** `inTimeRange("9:00 am","5:00 pm")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | `inTimeRange24(String startTime, String endTime)`                                                                                                     | Validates that the current server time is between the specified 24-hour formatted time range between the `startTime` and `endTime` parameters.**Example:** `inTimeRange24("09:00","17:00")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `requestHeaderContains(String field, String value)`                                                                                                   | Validates that the HTTP header field value is equal to the `value` parameter.**Example:** `requestHeaderContains("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
> | `requestHeaderContains(Map<String, String> fieldValuesMap, boolean caseSensitive)`&#xA;&#xA;This matcher can be case sensitive or case insensitive.   | Validates that all of the HTTP header fields map to the associated value. The first `fieldValuesMap` string contains the HTTP header name, and the second string contains the value to compare the incoming request header value with.The `caseSensitive` parameter determines whether a case-sensitive comparison is performed on the value.The second string in the `fieldValuesMap` supports Java regular expressions.If multiple pairs of strings are present in the `fieldValuesMap` parameter, then all conditions must be met in order for the matcher to pass.**Example:** `requestHeaderContains(['User-Agent':'Mozilla/5.0', 'Cookie':'JSESSIONID'], false)`                                                                                                                                               |
> | `requestPostFormContains(Map<String, String> fieldValuesMap, boolean caseSensitive)`&#xA;&#xA;This matcher can be case sensitive or case insensitive. | Validates that all of the HTTP form fields maps to the associated value. The first `fieldValuesMap` string contains the form header name, and the second string contains the value to compare the incoming request header value with.The `caseSensitive` parameter determines whether a case-sensitive comparison is performed on the value.&#xA;&#xA;This matcher determines whether to use fields passed in the URL or forms with a content-type header of application/x-www-form-urlencoded.The second string in the `fieldValuesMap` supports Java regular expressions.If multiple pairs of strings are present in the `fieldValuesMap` parameter, then all conditions must be met in order for the matcher to pass.**Example:** `requestPostFormContains(['email':'@example.com', 'phonenumber':'720'], false)` |
> | `requestHeaderDoesntContain(String field, String value)`                                                                                              | Validates that the HTTP header field value is not equal to the `value` parameter.**Example:** `requestHeaderDoesntContain("User-Agent", "InternetExplorer")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | `requestBodyContains(String value)`                                                                                                                   | Validates that the HTTP body contains the `value` parameter.**Example:** `requestBodyContains("production")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | `requestBodyDoesntContain(String value)`                                                                                                              | Validates that the HTTP body does not contain the value parameter.**Example:** `requestBodyDoesntContain("test")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> | `containsWebSessionAttribute(String attributeName, String attributeValue)`                                                                            | Validates that the PingAccess token contains the attribute name and value.**Example:** `containsWebSessionAttribute("sub", "sarah")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
> | `containsACRValues(String value)`                                                                                                                     | Validates that the PingAccess token contains a matching ACR value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

The following table lists the PingAccess matchers available to only the [OAuth Groovy script rule](../pingaccess_user_interface_reference_guide/pa_adding_oauth_groovy_script_rules.html).

> **Collapse: OAuth Groovy script rule matchers**
>
> | Matcher                                                                                                                                  | Description                                                                                                         |
> | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
> | `hasScope(String scope)`                                                                                                                 | Validates that the OAuth access token contains the `scope` parameter.**Example:** `hasScope("access")`              |
> | `hasScopes(String…​ scopes)`                                                                                                             | Validates that the OAuth access token contains the list of scopes.**Example:** `hasScopes("access","portfolio")`    |
> | `hasAttribute(String attributeName, String attributeValue)`&#xA;&#xA;This matcher is case insensitive and cannot be made case sensitive. | Checks for an attribute value within the current OAuth2 policy context.**Example:** `hasAttribute("account","joe")` |

---

---
title: MediaType object reference
description: Access the MediaType object.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_mediatype_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_mediatype_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  method-summary: Method summary
---

# MediaType object reference

Access the MediaType object.

## Method summary

| Method                        | Description                                                     |
| ----------------------------- | --------------------------------------------------------------- |
| `Map getParameters()`         | Returns a list of parameters.                                   |
| `String getBaseType()`        | Returns the media base type.                                    |
| `String getSubType()`         | Returns the media sub type.                                     |
| `String getParameter(String)` | Returns a string containing the value of the request parameter. |
| `String getPrimaryType()`     | Returns the primary media type.                                 |

---

---
title: Method object reference
description: Access the Method object in Groovy exc?.request?.method.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_method_object_ref
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_method_object_ref.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  purpose: Purpose
  groovy-sample: Groovy sample
  method-summary: Method summary
---

# Method object reference

Access the Method object in Groovy `exc?.request?.method`.

## Purpose

The Method object contains the HTTP method name from the request made to an application. The HTTP method is sent on to the site after the rules are evaluated.

## Groovy sample

```
//Retrieve the HTTP Method name and make different decisions based on the method name
def method = exc?.request?.method?.methodName
switch (method) {
     case "GET":
         println("GET")
         break;
     case "POST":
         println("POST")
         break;
     case "PUT":
         println("PUT")
         break;
     case "DELETE":
         println("DELETE")
         break;
default:
     println("DEFAULT")
     pass()
}
```

## Method summary

| Method                 | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| String getMethodName() | Returns the name of the HTTP method, GET, PUT, POST, DELETE, HEAD. |

---

---
title: Modifying the Java heap size
description: Modify the Java heap size for both Windows and Linux installations, including the Windows and Linux services.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_modifying_the_java_heap_size
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_modifying_the_java_heap_size.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
---

# Modifying the Java heap size

Modify the Java heap size for both Windows and Linux installations, including the Windows and Linux services.

## Steps

1. Edit the `jvm-memory.options` file located in the `<PA_HOME>/conf` directory.

2. Specify overall heap size by modifying the `#Minimum heap size` and `#Maximum heap size` parameters.

   ### Choose from:

   * Modify `-Xms512m` to change the `#Minimum heap size` value.

   * Modify `-Xmx512m` to change the `#Maximum heap size` value.

   Specify units as `m`, megabytes, or `g`, gigabytes.

3. Specify young generation size by modifying the `#Minimum size for the Young Gen space` and `#Maximum size for the Young Gen space` variables.

   ### Choose from:

   * Modify `-XX:NewSize=256m` to change the `#Minimum size for the Young Gen space` value.

   * Modify `-XX:MaxNewSize=256m` to change the `#Maximum size for the Young Gen space` value.

   Set values to 50% of `#Minimum heap size` and `#Maximum heap size`.

   |   |                                                                                                                                                 |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Not advisable if selecting the G1 collector. For more information, see [Garbage Collector Configuration](pa_garbage_collector_config_ref.html). |

4. If you are running PingAccess as a Windows service, run the `generate-wrapper-jvm-options.bat` file located in the `<PA_HOME>/sbin/windows` directory.

   This file applies the changes from the `jvm-memory.options` file to the `wrapper-jvm-options.conf` file, which is used by the Windows service.

---

---
title: OAuth endpoint
description: This page describes the endpoint used by an OAuth authorization server to interface with PingAccess as an OAuth resource server.
component: pingaccess
version: 9.1
page_id: pingaccess:reference_guides:pa_oauth_endpoint
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/reference_guides/pa_oauth_endpoint.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 6, 2023
section_ids:
  paoauthjwks: /pa/oauth/JWKS
---

# OAuth endpoint

This page describes the endpoint used by an OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* authorization server to interface with PingAccess as an OAuth resource server.

## /pa/oauth/JWKS

An OAuth authorization server uses this endpoint to acquire PingAccess public keys to encrypt access tokens. The output uses the Internet Engineering Task Force (IETF) JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
\</div>)* format for public keys.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you selected the **Use context root as reserved resource base path** check box on your PingAccess application, this feature creates an instance of any reserved PingAccess resources under the application's context root. As such, the context root of the application needs to prepend the reserved context application root (`/pa` by default) in any file paths that reference it.If the context root of your application is `myApp`, the path to the OAuth endpoint would be `myApp/pa/oauth/JWKS` instead. |