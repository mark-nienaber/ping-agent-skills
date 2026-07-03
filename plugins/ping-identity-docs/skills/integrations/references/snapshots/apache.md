---
title: Overview of the SSO flow
description: The Apache agent acts as a filter in front of an external protected resource, such as an application.
component: apache
page_id: apache::pf_apache_linux_ik_overview_of_the_sso_flow
canonical_url: https://docs.pingidentity.com/integrations/apache/pf_apache_linux_ik_overview_of_the_sso_flow.html
revdate: June 27, 2024
---

# Overview of the SSO flow

The Apache agent acts as a filter in front of an external protected resource, such as an application.

For each request, the Apache agent does one of the following:

* If the request is for an unprotected resource, the Apache agent passes the request to the application.

* If the request is for a protected resource, the Apache agent checks to see if there is a PingFederate session available and if the session parameters meet session policy for that session.

* If a session exists and the session meets session policy for that request, the Apache agent passes the request through to the application.

* If a session doesn't exist or if the existing session doesn't meet the session policy for that request, the Apache agent redirects the browser through the PingFederate server to an identity provider (IdP) for authentication. After authentication, PingFederate redirects the user back to the protected resource with a valid session.

The following diagram illustrates a service provider (SP)-initiated single sign-on (SSO) scenario, showing the request flow and how the PingFederate OpenToken Adapter wraps attributes from an assertion into a secure token (OpenToken) and passes the token to Apache.

![A diagram that shows the flow of information between the server, PingFederate, and the browser.](_images/lop1563995115032.png)

In this flow:

1. A user attempts to access a resource on the Apache server protected by the PingFederate Apache agent.

   1. The user is redirected to the PingFederate server for authentication.

   2. If an OpenToken session already exists, the user is granted immediate access.

2. The PingFederate server redirects the user's browser to an IdP for authentication using either the SAML or WS-Federation protocols. The IdP partner authenticates the user and returns a SAML assertion.

3. PingFederate validates the assertion and creates an OpenToken for the user including any configured attributes. PingFederate then redirects the browser, including the OpenToken, back to the Apache agent.

4. The Apache agent verifies the OpenToken and grants access to the protected resource. The User ID and any attributes from the OpenToken are exposed to the resource as HTTP request headers or Apache environment variables.

---

---
title: Session information and user attributes
description: The PingFederate Apache agent passes session information and user attributes from the adapter to the application.
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_session_information_and_user_attributes
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_session_information_and_user_attributes.html
revdate: June 27, 2024
---

# Session information and user attributes

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

---

---
title: Session logout
description: The PingFederateCancelURL address in your <apache_home>/conf/mod_pf.conf file initiates a user-session logout. This URL specifies a resource that directs the Apache agent to:
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_session_logout
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_session_logout.html
revdate: June 27, 2024
---

# Session logout

The `PingFederateCancelURL` address in your `<apache_home>/conf/mod_pf.conf` file initiates a user-session logout. This URL specifies a resource that directs the Apache agent to:

1. Initiate a single logout (SLO), if configured

2. Expire the PingFederate session

3. Clean up any resources associated with the session

4. Pass control back to the application so that it can clean up its own session

---

---
title: Session validation
description: PingFederate validates both an inactivity timeout and an overall session timeout:
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_session_validation
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_session_validation.html
revdate: June 27, 2024
---

# Session validation

PingFederate validates both an inactivity timeout and an overall session timeout:

* Inactivity timeout

  The amount of time that a session can be inactive when no new browser requests are received and before a user is required to reauthenticate.

* Overall session timeout

  The total amount of time that a session can be active, regardless of activity, before the user is required to re-authenticate.

If either of the timeout limits has expired, the Apache agent cancels the existing session and redirects the browser to the `PingFederateLoginPageUrl` address in your `<apache_home>/conf/mod_pf.conf` file. This starts a service provider (SP)-initiated single sign-on (SSO) request at the identity provider (IdP).

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | Session cancellation enforces session cleanup in the PingFederate server and session cookie obsolescence. |

---

---
title: Setting up virtual hosts
description: Each virtual host can optionally have its own respective Apache agent configuration.
component: apache
page_id: apache:setup:pf_apache_linux_ik_setting_up_virtual_hosts
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_setting_up_virtual_hosts.html
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Setting up virtual hosts

Each virtual host can optionally have its own respective Apache agent configuration.

## About this task

If no custom configuration is provided, a virtual host uses the agent configuration from the base server.

## Steps

* If you want to use this feature, add the following to the Apache `httpd.conf` file in the virtual host context:

  ```none
  PingFederateConfigurationFile conf/mod_pf_vhost.conf
  ```

  In this example, `mod_pf_vhost.conf` is an agent configuration file that contains settings unique to the virtual host. PingFederate attributes from the base server configuration aren't merged with the virtual host when the `PingFederateConfigurationFile` attribute is specified for the virtual host.

---

---
title: SSL support
description: The Apache agent supports TLS/SSL, using standard Apache SSL support for connections to the server from browsers.
component: apache
page_id: apache:apache_agent_information:pf_apache_linux_ik_ssl_support
canonical_url: https://docs.pingidentity.com/integrations/apache/apache_agent_information/pf_apache_linux_ik_ssl_support.html
revdate: June 27, 2024
---

# SSL support

The Apache agent supports TLS/SSL, using standard Apache SSL support for connections to the server from browsers.

---

---
title: Testing the Apache agent
description: The Apache agent includes a protected start page to help you verify your configuration. This feature is for testing purposes only and is disabled by default.
component: apache
page_id: apache:setup:pf_apache_linux_ik_testing_the_agent
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_testing_the_agent.html
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Testing the Apache agent

The Apache agent includes a protected start page to help you verify your configuration. This feature is for testing purposes only and is disabled by default.

## About this task

The start page initiates a single sign-on transaction with the identity provider partner. If it succeeds, it displays the HTTP headers that the Apache agent will expose to your application. These headers correspond to attributes from the SAML assertion.

## Steps

1. Turn on the test page:

   1. Edit the `<apache_home>/conf/mod_pf.conf` by adding `#` to comment out the `PingFederateStartPageURL` property.

   2. Save the file and restart Apache.

2. Modify the following URL for your environment and then open it in a browser.

   ```none
   http://apache-server/protected-path/?cmd=PingStartPage
   ```

3. When you finish testing, revert your changes to `mod_pf.conf`.

   |   |                                                                                   |
   | - | --------------------------------------------------------------------------------- |
   |   | For security reasons, you should disable this feature in production environments. |

4. Restart Apache.

---

---
title: Updating the OpenToken Adapter
description: The Apache Linux Integration Kit relies on the OpenToken Adapter that is distributed with the Java Integration Kit. Update the OpenToken Adapter to get the latest feature and security updates.
component: apache
page_id: apache:setup:pf_apache_linux_ik_updating_the_opentoken_adapter
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_updating_the_opentoken_adapter.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Updating the OpenToken Adapter

The Apache Linux Integration Kit relies on the OpenToken Adapter that is distributed with the Java Integration Kit. Update the OpenToken Adapter to get the latest feature and security updates.

## Steps

1. Download the Java Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

2. Stop PingFederate.

3. Delete the `opentoken-adapter-<version>.jar` file from your `<pf_install>/pingfederate/server/default/deploy` directory.

4. From the Java Integration Kit `.zip` archive, copy the contents of `dist/pingfederate` to your `<pf_install>/pingfederate` directory.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `commons-collections`, `commons-beanutils`, and `commons-logging` libraries are provided as a convenience and should be installed only if they aren't already contained in the application `CLASSPATH`. |

5. Start PingFederate.

6. If you operate PingFederate in a cluster, repeat steps 2-5 for each engine node.

---

---
title: Upgrading an existing deployment
description: If you're upgrading from a previous version of the Apache Linux Integration Kit, modify your existing configuration files.
component: apache
page_id: apache:setup:pf_apache_linux_ik_upgrading_an_existing_deployment
canonical_url: https://docs.pingidentity.com/integrations/apache/setup/pf_apache_linux_ik_upgrading_an_existing_deployment.html
revdate: June 27, 2024
section_ids:
  steps: Steps
---

# Upgrading an existing deployment

If you're upgrading from a previous version of the Apache Linux Integration Kit, modify your existing configuration files.

## Steps

1. Stop Apache.

2. Download the Apache Linux Integration Kit `.zip` archive from the **Add-ons** tab of the [PingFederate downloads page](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

3. From the `.zip` archive, copy `apache-agent/lib/<your platform>/libopentoken.so` to the Apache modules directory.

4. Edit your existing `mod_pf.conf` file:

   1. Add the following if it doesn't already exist.

      ```none
      # Enables or disables the "http only" attribute of the cookie. Http only cookies
      # inform the browser that the cookie shouldn't be accessible by client-side scripts.
      # The default is set to "yes"

      PingFederateCookieHttpOnly              yes
      ```

   2. Set the value to `yes` or `no` to suit your environment. Save the file.

5. Edit your existing `mod_pf.so` file:

   1. Add the following if it doesn't already exist.

      ```none
      # (Required)
      # The SameSite cookie attribute is set to this value. Set this to match the value of
      # 'cookie-samesite-attribute' in the Agent configuration file (defined in
      # PingFederateAgentConfigurationFile), if that is defined.
      # The allowed values for this setting are: Strict, Lax, None, and Nothing
      # The "Strict", "Lax", and "None" value changes the SameSite cookie attribute setting.
      # The "Nothing" value leaves the SameSite cookie attribute unset in the OpenToken Session Cookie.
      # For the "None" value, you must use secure attributes because cross-site cookies can only be
      # accessed over HTTPS connections.
      # If the cookie is not secure and the "None" value is selected, the SameSite cookie attribute
      # will not be set.

      PingFederateCookieSameSiteAttribute	Nothing
      ```

   2. Set the value to `Strict`, `Lax`, `None`, or `Nothing` to suit your environment. Save the file.

6. Add the following if it doesn't already exist.

   ```none
   # (Optional)
   # Enables or disables fragment preservation in requests.
   # When set to "yes", preserves request fragment and redirects user back
   # to the URI with fragment.
   # To prevent sensitive data leakage, ensure that no sensitive information
   # is present in a preserved fragment.
   # The default is "no".
   PingFederateEnableFragmentPreservation   no

   # (Optional)
   # The HTML template used to generate client side (JavaScript-based) redirects for
   # fragment preservation. If not specified, a prebuilt template is used.
   # Path could be an absolute or relative to the httpd.conf ServerRoot
   # definition.

   #PingFederateFragmentPreservationPageTemplateFile conf/fragment_preservation_request_template.html
   ```

7. Start Apache.

8. Update the OpenToken Adapter in PingFederate as shown in [Updating the OpenToken Adapter](pf_apache_linux_ik_updating_the_opentoken_adapter.html).

9. Reinstall the Apache agent as shown in [Apache Agent setup](pf_apache_linux_ik_agent_setup.html).