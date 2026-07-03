---
title: Apache agent information
description: The Apache agent lets your Apache server communicate with PingFederate. When a user tries to access a resource on your Apache server, the agent checks their session status. When a user starts a new session, the agent validates OpenToken information from PingFederate and lets the user access the resource.
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_agent_information
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_agent_information.html
revdate: June 27, 2024
section_ids:
  ssl-support: SSL support
  session-validation: Session validation
  memory-usage: Memory usage
  session-information-and-user-attributes: Session information and user attributes
  error-handling: Error handling
  session-logout: Session logout
  logging: Logging
---

# Apache agent information

The Apache agent lets your Apache server communicate with PingFederate. When a user tries to access a resource on your Apache server, the agent checks their session status. When a user starts a new session, the agent validates OpenToken information from PingFederate and lets the user access the resource.

## SSL support

The Apache agent supports TLS/SSL, using standard Apache SSL support for connections to the server from browsers.

## Session validation

PingFederate validates both an inactivity timeout and an overall session timeout:

* Inactivity timeout

  The amount of time that a session can be inactive when no new browser requests are received and before a user is required to reauthenticate.

* Overall session timeout

  The total amount of time that a session can be active, regardless of activity, before the user is required to re-authenticate.

If either of the timeout limits has expired, the Apache agent cancels the existing session and redirects the browser to the `PingFederateLoginPageUrl` address in your `<apache_home>/conf/mod_pf.conf` file. This starts a service provider (SP)-initiated single sign-on (SSO) request at the identity provider (IdP).

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | Session cancellation enforces session cleanup in the PingFederate server and session cookie obsolescence. |

## Memory usage

The Apache agent uses the Apache Portable Runtime (APR) pools for allocation of most data: either the configuration-time pool for storing configuration variables or request-time pools for processing sessions.

Heap is used only for temporary data with a short usage time and sensitive size, such as:

* Dynamic reallocations on compressed-token decompression

* Parsing session information

* Operations with the OpenToken library

## Session information and user attributes

The PingFederate Apache agent passes session information and user attributes from the adapter to the application.

The Apache agent includes the information in HTTP request headers or Apache environment variables. This information can then be used by the application for authorization decisions or for generation of content specific to the user making the request.

The following session and attribute information is exposed to the application:

* Attributes from the OpenToken Adapter contract

  The subject (`SUBJECT`) and any attributes that you add on the **Extended Contract** tab of the adapter configuration. Only the attributes fulfilled at runtime are exposed to the application. Attributes with a `NULL` value aren't included in the OpenToken.

* `NOT-ON-OR-AFTER`

  The time until inactivity timeout is reached.

* `RENEW-UNTIL`

  The time until overall session timeout is reached.

* `AUTH_NOT-BEFORE`

  The time when the session was created.

* `AUTHNCONTEXT`

  Information from the SAML assertion that describes how the user was authenticated at the IdP.

For security reasons, each HTTP request header or Apache environment variable is first pre-pended with a specific prefix. Learn more about configuring the prefix in [Configuring the Apache agent](../setup/pf_apache_linux_ik_configuring_the_apache_agent.html). The Apache agent always removes and rewrites the prefixed request headers and environment variables for each request.

If you can't modify your applications to accept headers with this prefix, you can configure the Apache agent to add a prefix to the HTTP headers or environment variables. In this case, on the **Extended Contract** tab of the OpenToken Adapter configuration, include an attribute named `pf_attribute_list`. Map that attribute in your identity provider (IdP) connection as a text field containing a comma-separated list of all the attributes in the adapter contract. This attribute list is sent in the OpenToken and used by the Apache agent to overwrite headers in the request.

Learn more about [Configuring target session fulfillment](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_target_session_fulfillment.html) in the PingFederate documentation.

## Error handling

When an error occurs, the Apache agent redirects the browser to the `PingFederateErrorPageURL` address in your `<apache_home>/conf/mod_pf.conf` file.

|   |                                                                 |
| - | --------------------------------------------------------------- |
|   | This value isn't enabled by default, but examples are provided. |

## Session logout

The `PingFederateCancelURL` address in your `<apache_home>/conf/mod_pf.conf` file initiates a user-session logout. This URL specifies a resource that directs the Apache agent to:

1. Initiate a single logout (SLO), if configured

2. Expire the PingFederate session

3. Clean up any resources associated with the session

4. Pass control back to the application so that it can clean up its own session

## Logging

The PingFederate Apache agent uses an Apache API logging scheme that writes into the standard `logs/error_log` file. This file is created automatically at startup with the verbosity level controlled by `LogLevel` in your `httpd.conf` file.

The PingFederate Apache agent has six internally distinguished verbosity levels, ranging from `0` to `5`. The first four correspond to Apache definitions in `error/warn/notice/info`. The last two levels are for logging HTTP requests, responses, and cURL-library debug output, if necessary. The default level is `0`, which logs only errors.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The Apache agent logs all of its output at the `info` level. To access this output, set the Apache `LogLevel` to `info` in `httpd.conf`, then restart the Apache server. |
