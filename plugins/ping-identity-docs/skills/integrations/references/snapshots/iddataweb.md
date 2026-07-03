---
title: Adding device profiling to a web application
description: If you have a web application that uses the PingFederate authentication API and cannot accommodate HTTP cookies, modify your web application to run the device profiling script.
component: iddataweb
page_id: iddataweb:setup:pf_iddataweb_ik_adding_device_profiling_to_a_web_application
canonical_url: https://docs.pingidentity.com/integrations/iddataweb/setup/pf_iddataweb_ik_adding_device_profiling_to_a_web_application.html
revdate: June 24, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a web application

If you have a web application that uses the PingFederate authentication API and cannot accommodate HTTP cookies, modify your web application to run the device profiling script.

## About this task

Learn more in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

## Steps

1. Add the following code to the sign-on page:

   ```
   <script type="text/javascript"
   src="<device profiling URL>"></script>
   ```

   For each sign-on event, insert the device profiling URL from PingFederate.

2. Configure your application to complete the following actions in sequence:

   1. Get the device profiling URL from PingFederate. This is an attribute of the `DEVICE_PROFILE_REQUIRED` state.

   2. Run the device profiling script by including it in the page.

   3. POST `continueAuthentication` to the authentication API.

3. When you complete the steps in [Configuring an adapter instance](pf_iddataweb_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by this adapter**.
