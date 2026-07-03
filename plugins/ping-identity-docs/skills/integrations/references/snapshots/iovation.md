---
title: Adding device profiling to an authentication page
description: Instead of using the iovation IdP Adapter to gather the device profile, you can speed up the sign-on process by adding the device profiling scripts to an existing authentication adapter.
component: iovation
page_id: iovation:setup:pf_iovation_ik_adding_device_profiling_to_an_authentication_page
canonical_url: https://docs.pingidentity.com/integrations/iovation/setup/pf_iovation_ik_adding_device_profiling_to_an_authentication_page.html
revdate: May 30, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an authentication page

Instead of using the iovation IdP Adapter to gather the device profile, you can speed up the sign-on process by adding the device profiling scripts to an existing authentication adapter.

## About this task

These steps describe how to add the device-profiling scripts to the HTML Form Adapter that's bundled with PingFederate. You can adapt these instructions for any page that meets the criteria listed in [Device profiling method](../pf_iovation_ik_device_profiling_method.html).

The authentication page you modify must appear earlier in the sign-on flow than the iovation IdP Adapter.

## Steps

1. Embed the JavaScript files in the page.

   1. Open the `<pf_install>/pingfederate/server/default/conf/template/html.form.login.template.html` file for editing.

   2. At the end of the file, above the \</body> tag, add the following external script references:

      ```
      <script language="javascript" src="../assets/scripts/iovation_adapter_custom.js"></script>
      <script language="javascript" src="../assets/scripts/iovation_device_profiling.js"></script>
      ```

   3. Save the file.

2. (Optional) Customize the name prefix for the blackbox cookie to suit your environment:

   1. Open the `<pf_install>/pingfederate/server/default/conf/assets/scripts/iovation_adapter_custom.js` file for editing.

   2. On the following line, change `iovation_bb` to a name prefix of your choosing:

      ```
      var bbCookieNamePrefix = "iovation_bb";
      ```

      |   |                                                                                                                                                                                                                                                                                                                                       |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you customize the name prefix, you must enter the new prefix value in the **Blackbox Cookie Name Prefix** field in [Configuring an adapter instance](pf_iovation_ik_configuring_an_adapter_instance.html). Additionally, you must set the **Device Profiling Method** to **Captured by a previous adapter**. Learn more in step 5. |

   3. Save the file.

3. (Optional) Increase the client header buffer size setting on your proxy server.

   It must be able to accommodate the blackbox HTTP cookies (up to 8 KB) as well as any other cookies in your sign-on flow.

4. Configure your proxy server to pass the user's IP address to PingFederate through HTTP headers:

   1. In your reverse proxy server configuration, specify a header to store the IP address associated with the request, such as *\<X-Forwarded-For>*.

   2. In the PingFederate admin console, go to **Security > System Integration > Incoming Proxy Settings**.

   3. In the **HTTP Header For Client IP Addresses** field, enter the header you specified in step 4a.

      You can find more details in [Configure incoming proxy settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_systemoptionstasklet_systemoptionsstate.html) in the PingFederate documentation.

5. When [Configuring an adapter instance](pf_iovation_ik_configuring_an_adapter_instance.html), configure the **Device Profiling Method** and **Blackbox Cookie Name Prefix** fields as shown in [iovation IdP Adapter settings reference](pf_iovation_ik_iovation_idp_adapter_settings_reference.html).
