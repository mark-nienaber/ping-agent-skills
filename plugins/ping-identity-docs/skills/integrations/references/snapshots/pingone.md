---
title: Adding an application in DaVinci
description: Create an application to associate your PingFederate integration with your flow.
component: pingone
page_id: pingone:pingone_davinci_integration_kit:pf_p1_davinci_ik_adding_an_application_in_davinci
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_davinci_integration_kit/pf_p1_davinci_ik_adding_an_application_in_davinci.html
revdate: June 19, 2024
section_ids:
  steps: Steps
---

# Adding an application in DaVinci

Create an application to associate your PingFederate integration with your flow.

## Steps

1. Sign on to the DaVinci admin portal.

2. Create a blank flow:

   1. Go to **Flows** and click **[icon: plus, set=fa]Add Flow**.

   2. Select **Blank Flow**.

   3. On the **Add Flow** dialog, enter a name for your flow. Click **Create**.

   4. Complete the flow as described in [Building a flow in DaVinci](pf_p1_davinci_ik_building_a_flow_in_davinci.html).

3. Add an application:

   1. Go to **Applications**.

   2. Click **[icon: plus, set=fa]Add Application**

   3. On the **Add Application** dialog, enter a name for your application. Click **Create**.

   4. Click your application.

4. Add a flow policy to your application:

   1. On the **Flow Policy** tab, click **[icon: plus, set=fa]Add Flow Policy**.

   2. Select the flow that you made in step 2. Select **Latest Version** or another version. Click **Create My Flow Policy**.

   3. On the **Edit Your Weight Distribution** dialog, in the **Analytics - Select Success Nodes** list, select your **Send success JSON response** node. Click **Save My Flow Policy**.

   4. On the **Flow Policy** tab, note your **Policy ID**. You'll use this to configure the DaVinciadapter.

5. On the **General** tab, note your **Company ID** and **API Key**. You'll use these to configure the DaVinci adapter.

---

---
title: Adding device profiling to a browser-based authentication page
description: You can adapt these instructions to add device profiling to any web page included in an adapter, such as the Identifier First Adapter or a custom adapter. The page must meet the criteria listed in Device profiling methods.
component: pingone
page_id: pingone:pingone_protect_integration_kit:pf_p1_protect_ik_adding_device_profiling_to_a_browser
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_adding_device_profiling_to_a_browser.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a browser-based authentication page

## About this task

You can adapt these instructions to add device profiling to any web page included in an adapter, such as the Identifier First Adapter or a custom adapter. The page must meet the criteria listed in [Device profiling methods](pf_p1_protect_ik_device_profiling_methods.html).

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use the HTML Form Adapter, follow the instructions in [Configuring an adapter instance](pf_p1_protect_ik_configuring_an_adapter_instance.html). |

## Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `signals-sdk-<version>.js`

   * `signals.js` in the `captcha` directory

   * `pingone-protect-device-profiling-implementation.js`. (If you are using version 1.0.1 or earlier of the integration kit, the file is called `pingone-protect-device-profiling.js`)

2. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk-<version>.js"></script>
   <script type="text/javascript" src="pingone-protect-device-profiling-implementation.js"></script>
   <script type="text/javascript" src="signals.js"></script>
   ```

   |   |                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are using version 1.0.1 or earlier of the integration kit, replace the reference to `pingone-protect-device-profiling-implementation.js` with a reference to `pingone-protect-device-profiling.js` |

3. When you complete the steps in [Configuring an adapter instance](pf_p1_protect_ik_configuring_an_adapter_instance.html), you can enable risk evaluation for active sessions. Follow the steps in [Configuring authentication sessions](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_config_auth_sessions.html) to set up sessions for the PingOne Protect Adapter, and complete steps 2a, 2b, and 3.

---

---
title: Adding device profiling to a browser-based authentication page
description: "There are two ways for device profiling data to be collected: by the PingOne Risk IdP Adapter, or by a previous adapter such as the HTML Form Adapter."
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authentication_page
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authentication_page.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  adding-device-profiling-to-a-browser-based-authentication-page-using-the-pingone-risk-signals-sdk-with-integration-kit-1-3-1: Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK with integration kit 1.3.1
  about-this-task-2: About this task
  steps: Steps
  adding-device-profiling-to-a-browser-based-authentication-page-using-the-pingone-risk-signals-sdk-and-integration-kit-1-3-or-earlier: Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier
  about-this-task-3: About this task
  steps-2: Steps
  adding-device-profiling-to-a-browser-based-authentication-page-using-fingerprint-js: Adding device profiling to a browser-based authentication page using Fingerprint JS
  about-this-task-4: About this task
  steps-3: Steps
---

# Adding device profiling to a browser-based authentication page

There are two ways for device profiling data to be collected: by the PingOne Risk IdP Adapter, or by a previous adapter such as the HTML Form Adapter.

## About this task

Getting the device profile on the HTML Form Adapter page reduces the perceived wait times for the user. Learn more in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

## Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK with integration kit 1.3.1

### About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Risk Integration Kit version 1.3.1 must be deployed before any changes can be made on the HTML side. SDK version 5.2 and later requires adapter version 1.3.1 or later. |

### Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `pingone-risk-profiling-signals-sdk.js`

   * `pingone-risk-management-embedded.js`

   * `signals-sdk-<version>.js`

2. **Optional:** Edit the `pingone-risk-profiling-signals-sdk.js` file and add your PingOne environment ID.

   ```
   function profileDevice(callback) {
       // Initialize the SDK
       // replace <envid> with the PingOne console > Environment > Environment ID value
       onPingOneSignalsReady(function () {
           _pingOneSignals.initSilent({
                envId: "<envid>",
               behavioralDataCollection: false,
               deviceAttributesBlackList: []
           }).then(function ()
   ```

3. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk-<version>.js"></script>
   <script type="text/javascript" src="pingone-risk-profiling-signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-management-embedded.js"></script>
   ```

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

## Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier

### About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

### Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `pingone-risk-profiling-signals-sdk.js`

   * `pingone-risk-management-embedded.js`

   * `signals-sdk.js`

2. Edit the `pingone-risk-profiling-signals-sdk.js` file and add your PingOne environment ID.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | The PingOne Risk SDK won't work if the PingOne environment ID is missing. |

   ```
   function profileDevice(callback) {
       // Initialize the SDK
       // replace <envid> with the PingOne console > Environment > Environment ID value
       onPingOneSignalsReady(function () {
           _pingOneSignals.initSilent({
                envId: "<envid>",
               deviceAttributesBlackList: []
           }).then(function ()
   ```

3. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-profiling-signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-management-embedded.js"></script>
   ```

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

## Adding device profiling to a browser-based authentication page using Fingerprint JS

### About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Risk (Signals) SDK is the preferred way to get device profiling and is recommended for use in the PingOne Risk Integration Kit 1.3 and later. |

### Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `fingerprint2-<version>.min.js`

   * `pingone-risk-management-profiling.js`

   * `pingone-risk-management-embedded.js`

2. Add the following external script references to the sign-on page.

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order: |

   ```
   <script type="text/javascript" src="fingerprint2-<version>.min.js"></script>
   <script type="text/javascript" src="{file-prefix}-profiling.js"></script>
   <script type="text/javascript" src="{file-prefix}-embedded.js"></script>
   ```

3. Edit the `pingone-risk-management-embedded.js` file to use Fingerprint JS according to the comments in the file.

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

---

---
title: Adding device profiling to a browser-based authentication page using Fingerprint JS
description: You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in Device profiling methods.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_fingerprint_js
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_fingerprint_js.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a browser-based authentication page using Fingerprint JS

## About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Risk (Signals) SDK is the preferred way to get device profiling and is recommended for use in the PingOne Risk Integration Kit 1.3 and later. |

## Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `fingerprint2-<version>.min.js`

   * `pingone-risk-management-profiling.js`

   * `pingone-risk-management-embedded.js`

2. Add the following external script references to the sign-on page.

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order: |

   ```
   <script type="text/javascript" src="fingerprint2-<version>.min.js"></script>
   <script type="text/javascript" src="{file-prefix}-profiling.js"></script>
   <script type="text/javascript" src="{file-prefix}-embedded.js"></script>
   ```

3. Edit the `pingone-risk-management-embedded.js` file to use Fingerprint JS according to the comments in the file.

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

---

---
title: Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier
description: You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in Device profiling methods.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_p1risk_signals_sdk_and_ik_13_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_p1risk_signals_sdk_and_ik_13_or_earlier.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier

## About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

## Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `pingone-risk-profiling-signals-sdk.js`

   * `pingone-risk-management-embedded.js`

   * `signals-sdk.js`

2. Edit the `pingone-risk-profiling-signals-sdk.js` file and add your PingOne environment ID.

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | The PingOne Risk SDK won't work if the PingOne environment ID is missing. |

   ```
   function profileDevice(callback) {
       // Initialize the SDK
       // replace <envid> with the PingOne console > Environment > Environment ID value
       onPingOneSignalsReady(function () {
           _pingOneSignals.initSilent({
                envId: "<envid>",
               deviceAttributesBlackList: []
           }).then(function ()
   ```

3. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-profiling-signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-management-embedded.js"></script>
   ```

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

---

---
title: Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK with integration kit 1.3.1
description: You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in Device profiling methods.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_p1risk_signals_sdk_with_ik_131
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_a_browser_based_authn_page_using_p1risk_signals_sdk_with_ik_131.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to a browser-based authentication page using the PingOne Risk (Signals) SDK with integration kit 1.3.1

## About this task

You can adapt these instructions to add device profiling to any page, such as the HTML Form Adapter or your web application. The page must meet the criteria listed in [Device profiling methods](pf_p1_risk_ik_device_profiling_methods.html).

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Risk Integration Kit version 1.3.1 must be deployed before any changes can be made on the HTML side. SDK version 5.2 and later requires adapter version 1.3.1 or later. |

## Steps

1. If you are modifying an external web application, copy the following files from the integration `.zip` archive to a location that your page can access.

   * `pingone-risk-profiling-signals-sdk.js`

   * `pingone-risk-management-embedded.js`

   * `signals-sdk-<version>.js`

2. **Optional:** Edit the `pingone-risk-profiling-signals-sdk.js` file and add your PingOne environment ID.

   ```
   function profileDevice(callback) {
       // Initialize the SDK
       // replace <envid> with the PingOne console > Environment > Environment ID value
       onPingOneSignalsReady(function () {
           _pingOneSignals.initSilent({
                envId: "<envid>",
               behavioralDataCollection: false,
               deviceAttributesBlackList: []
           }).then(function ()
   ```

3. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="signals-sdk-<version>.js"></script>
   <script type="text/javascript" src="pingone-risk-profiling-signals-sdk.js"></script>
   <script type="text/javascript" src="pingone-risk-management-embedded.js"></script>
   ```

4. **Optional:** Customize the device profile cookie name prefix to suit your environment.

   1. Open `pingone-risk-management-embedded.js` for editing.

   2. On the following line, change the value to a name of your choosing:

      ```
      var cookieNamePrefix = "pingone.risk.device.profile";
      ```

   3. Save the file.

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), follow the instructions to set the **Device profiling method** to **Captured by a previous adapter**. Update the **Cookie Name Prefix** field if you customized it above.

---

---
title: Adding device profiling to an authentication API-based application
description: Use the following instructions to add device profiling to a web application using the PingOne Protect SDK. For more information about the authentication API, see Authentication API in the PingFederate documentation or PingOne Protect Native SDKs in the PingOne Native SDK documentation.
component: pingone
page_id: pingone:pingone_protect_integration_kit:pf_p1_protect_ik_adding_device_profiling_to_an_api_application
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik_adding_device_profiling_to_an_api_application.html
revdate: June 28, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding device profiling to an authentication API-based application

## About this task

Use the following instructions to add device profiling to a web application using the PingOne Protect SDK. For more information about the authentication API, see [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Protect Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-protect-native-sdks) in the PingOne Native SDK documentation.

## Steps

1. Implement the Signals SDK by following the steps in [PingOne Protect Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-protect-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-protect-device-profiling.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_protect_ik_configuring_an_adapter_instance.html), set the device profiling method. The provider or the adapter can receive the payload sent by the authentication API.

   ### Choose from:

   * If the provider is configured, you must add the payload to the `checkUsernamePassword` `requestOptions` API call in the captchaResponse.

     ```json
     {
       "username": "string",
       "password": "string",
       "rememberMyUsername": "boolean",
       "thisIsMyDevice": "boolean",
       "captchaResponse": "string"
     }
     ```

   * When using the PingOne Protect IdP Adapter, submit the payload following the `submitDeviceProfile` `requestOptions` action of the authentication API.

     |   |                                                                                                                                                                                                                                     |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | For more information on these options, see [Exploring the authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation. |

---

---
title: Adding device profiling to an authentication API-based application
description: If you are using the PingFederate authentication application programming interface (API) and want to avoid using HTTP cookies, modify your application to collect the device profile and send it to the authentication API.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authentication_api_based_application
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authentication_api_based_application.html
revdate: July 12, 2024
section_ids:
  adding-device-profiling-to-an-authentication-api-based-application-using-the-pingone-risk-signals-sdk-and-integration-kit-1-3-1: Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3.1
  about-this-task: About this task
  steps: Steps
  adding-device-profiling-to-an-authentication-api-based-application-using-the-pingone-risk-signals-sdk-and-integration-kit-1-3-or-earlier: Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier
  about-this-task-2: About this task
  steps-2: Steps
  adding-device-profiling-to-an-authentication-api-based-application-using-fingerprint-js: Adding device profiling to an Authentication API-based application using Fingerprint JS
  about-this-task-3: About this task
  steps-3: Steps
---

# Adding device profiling to an authentication API-based application

If you are using the PingFederate authentication application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* and want to avoid using HTTP cookies, modify your application to collect the device profile and send it to the authentication API.

## Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3.1

### About this task

Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Risk Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) in the PingOne Native SDK documentation.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Risk Integration Kit version 1.3.1 must be deployed before any changes can be made on the HTML side. SDK version 5.2.1 or later requires adapter version 1.3.1 or later. |

### Steps

1. Implement the Signals SDK by following the steps in [PingOne Risk Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-risk-profiling-signals-sdk.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by previous adapter**.

## Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier

### About this task

Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Risk Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) in the PingOne Native SDK documentation.

### Steps

1. Implement the Signals SDK by following the steps in [PingOne Risk Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-risk-profiling-signals-sdk.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by previous adapter**.

## Adding device profiling to an Authentication API-based application using Fingerprint JS

### About this task

Use the following instructions to add device profiling to a web application using Fingerprint JS. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Risk (Signals) SDK is the preferred way to get device profiling and is recommended for use in the PingOne Risk Integration Kit 1.3 and later. |

### Steps

1. Copy the following files from the integration `.zip` archive to your web server.

   * `fingerprint2-<version>.min.js`

   * `pingone-risk-management-profiling.js`

2. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="fingerprint2-<version>.min.js"></script>
   <script type="text/javascript" src="{file-prefix}-profiling.js"></script>
   ```

3. Configure your application to call the `profileDevice(onCompletion)` function. This creates the device profile.

4. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   ```
   function onCompletion(flowId, components) {
       var deviceProfile = transformComponentsToDeviceProfile(components);
       submitDeviceProfile(flowId, deviceProfile);
   }
   ​
   function submitDeviceProfile(flowId, deviceProfile) {
       var myHeaders = new Headers();
       myHeaders.append("X-XSRF-Header", "test");
       myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
       var raw = JSON.stringify({
           "deviceProfile": deviceProfile
       });
   ​
       var requestOptions = {
           method: 'POST',
           headers: myHeaders,
           body: raw,
           redirect: 'follow'
       };
   ​
       fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
           .then(response => response.text())
           .then(result => console.log(result))
           .catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with a value structured as follows:

   ```html
   {
      "deviceProfile":{
         "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0",
         "language":"en-CA",
         "colorDepth":24,
         "deviceMemory":null,
         "hardwareConcurrency":12,
         "screenResolution":[
            3440,
            1440
         ],
         "availableScreenResolution":[
            3440,
            1417
         ],
         "timezoneOffset":480,
         "timezone":"America/Los_Angeles",
         "sessionStorage":true,
         "localStorage":true,
         "indexedDb":true,
         "addBehaviour":false,
         "openDatabase":false,
         "cpuClass":null,
         "platform":"MacIntel",
         "plugins":[
         ],
         "webgl":[
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAYAAABkW7XSAAARYUlEQVR4nO3c30vcj57f8effUWg5F1
   		 [...]
   		 WEBGL_draw_buffers;WEBGL_lose_context",
            "webgl aliased line width range:[1, 1]",
            "webgl aliased point size range:[1, 8191]",
            [...]
            "webgl fragment shader low int precision rangeMin:24",
            "webgl fragment shader low int precision rangeMax:24"
         ],
         "webglVendorAndRenderer":"ATI Technologies Inc.~AMD Radeon Pro 560X OpenGL Engine",
         "adBlock":false,
         "hasLiedLanguages":false,
         "hasLiedResolution":false,
         "hasLiedOs":false,
         "hasLiedBrowser":false,
         "touchSupport":[
            "0",
            "false",
            "false"
         ],
         "fonts":[
            "Andale Mono",
            "Arial",
            [...]
            "Wingdings",
            "Wingdings 2",
            "Wingdings 3"
         ],
         "audio":"35.7383295930922"
      }
   }
   ```

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by this adapter**.

---

---
title: Adding device profiling to an Authentication API-based application using Fingerprint JS
description: Use the following instructions to add device profiling to a web application using Fingerprint JS. Learn more about the authentication API in Authentication API in the PingFederate documentation.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_fingerprint_js
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_fingerprint_js.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an Authentication API-based application using Fingerprint JS

## About this task

Use the following instructions to add device profiling to a web application using Fingerprint JS. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOne Risk (Signals) SDK is the preferred way to get device profiling and is recommended for use in the PingOne Risk Integration Kit 1.3 and later. |

## Steps

1. Copy the following files from the integration `.zip` archive to your web server.

   * `fingerprint2-<version>.min.js`

   * `pingone-risk-management-profiling.js`

2. Add the following external script references to the sign-on page:

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The scripts must be added in the following order. |

   ```
   <script type="text/javascript" src="fingerprint2-<version>.min.js"></script>
   <script type="text/javascript" src="{file-prefix}-profiling.js"></script>
   ```

3. Configure your application to call the `profileDevice(onCompletion)` function. This creates the device profile.

4. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   ```
   function onCompletion(flowId, components) {
       var deviceProfile = transformComponentsToDeviceProfile(components);
       submitDeviceProfile(flowId, deviceProfile);
   }
   ​
   function submitDeviceProfile(flowId, deviceProfile) {
       var myHeaders = new Headers();
       myHeaders.append("X-XSRF-Header", "test");
       myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
       var raw = JSON.stringify({
           "deviceProfile": deviceProfile
       });
   ​
       var requestOptions = {
           method: 'POST',
           headers: myHeaders,
           body: raw,
           redirect: 'follow'
       };
   ​
       fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
           .then(response => response.text())
           .then(result => console.log(result))
           .catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with a value structured as follows:

   ```html
   {
      "deviceProfile":{
         "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0",
         "language":"en-CA",
         "colorDepth":24,
         "deviceMemory":null,
         "hardwareConcurrency":12,
         "screenResolution":[
            3440,
            1440
         ],
         "availableScreenResolution":[
            3440,
            1417
         ],
         "timezoneOffset":480,
         "timezone":"America/Los_Angeles",
         "sessionStorage":true,
         "localStorage":true,
         "indexedDb":true,
         "addBehaviour":false,
         "openDatabase":false,
         "cpuClass":null,
         "platform":"MacIntel",
         "plugins":[
         ],
         "webgl":[
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAYAAABkW7XSAAARYUlEQVR4nO3c30vcj57f8effUWg5F1
   		 [...]
   		 WEBGL_draw_buffers;WEBGL_lose_context",
            "webgl aliased line width range:[1, 1]",
            "webgl aliased point size range:[1, 8191]",
            [...]
            "webgl fragment shader low int precision rangeMin:24",
            "webgl fragment shader low int precision rangeMax:24"
         ],
         "webglVendorAndRenderer":"ATI Technologies Inc.~AMD Radeon Pro 560X OpenGL Engine",
         "adBlock":false,
         "hasLiedLanguages":false,
         "hasLiedResolution":false,
         "hasLiedOs":false,
         "hasLiedBrowser":false,
         "touchSupport":[
            "0",
            "false",
            "false"
         ],
         "fonts":[
            "Andale Mono",
            "Arial",
            [...]
            "Wingdings",
            "Wingdings 2",
            "Wingdings 3"
         ],
         "audio":"35.7383295930922"
      }
   }
   ```

5. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by this adapter**.

---

---
title: Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier
description: Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in Authentication API in the PingFederate documentation or PingOne Risk Native SDKs in the PingOne Native SDK documentation.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_the_p1risk_signals_sdk_and_ik_13_or_earlier
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_the_p1risk_signals_sdk_and_ik_13_or_earlier.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3 or earlier

## About this task

Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Risk Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) in the PingOne Native SDK documentation.

## Steps

1. Implement the Signals SDK by following the steps in [PingOne Risk Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-risk-profiling-signals-sdk.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by previous adapter**.

---

---
title: Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3.1
description: Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in Authentication API in the PingFederate documentation or PingOne Risk Native SDKs in the PingOne Native SDK documentation.
component: pingone
page_id: pingone:pingone_risk_integration_kit:pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_the_p1risk_signals_sdk_and_ik_131
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_risk_integration_kit/pf_p1_risk_ik_adding_device_profiling_to_an_authtication_api_based_app_using_the_p1risk_signals_sdk_and_ik_131.html
revdate: July 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding device profiling to an authentication API-based application using the PingOne Risk (Signals) SDK and integration kit 1.3.1

## About this task

Use the following instructions to add device profiling to a web application using the PingOne Risk (Signals) SDK. Learn more about the authentication API in [Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation or [PingOne Risk Native SDKs](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) in the PingOne Native SDK documentation.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Risk Integration Kit version 1.3.1 must be deployed before any changes can be made on the HTML side. SDK version 5.2.1 or later requires adapter version 1.3.1 or later. |

## Steps

1. Implement the Signals SDK by following the steps in [PingOne Risk Native SDKs](https://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks).

2. Configure functions to format the device profile and submit it to the authentication API. Use the following code sample as a guide.

   |   |                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `pingone-risk-profiling-signals-sdk.js` assumes you are using the web SDK. If using a mobile device and you want to send the `deviceProfile` check the [SDK documentation](http://apidocs.pingidentity.com/pingone/native-sdks/v1/api/#pingone-risk-native-sdks) and use accordingly. |

   ```
   function onCompletion(flowId, deviceProfile) {
   	submitDeviceProfile(flowId, deviceProfile);
   }

   function submitDeviceProfile(flowId, deviceProfile) {
   	var myHeaders = new Headers();
   	myHeaders.append("X-XSRF-Header", "test");
   	myHeaders.append("Content-Type", "application/vnd.pingidentity.submitDeviceProfile+json");
   ​
   	var raw = JSON.stringify({
       	"signalsSdkDeviceProfile": deviceProfile
   	});
   ​
   	var requestOptions = {
       	method: 'POST',
       	headers: myHeaders,
       	body: raw,
       	redirect: 'follow'
   	};
   ​
   	fetch("https://pf_host:pf_port/pf-ws/authn/flows/" + flowId, requestOptions)
       	.then(response => response.text())
       	.then(result => console.log(result))
       	.catch(error => console.log('error', error));
   }
   ```

   When the authentication API is in the `DEVICE_PROFILE_REQUIRED` state, your application should `submitDeviceProfile` with the value from the `profileDevice(callback)` method.

3. When you complete the steps in [Configuring an adapter instance](pf_p1_risk_ik_configuring_an_adapter_instance.html), set the **Device profiling method** to **Captured by previous adapter**.

---

---
title: Adding PingOne MFA to your authentication policy
description: By modifying your PingFederate authentication policy to include the PingOne MFA IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_4.0:pf_p1_mfa_ik_adding_p1_mfa_to_your_authentication_policy_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_4.0/pf_p1_mfa_ik_adding_p1_mfa_to_your_authentication_policy_4.0.html
revdate: March 18, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding PingOne MFA to your authentication policy

By modifying your PingFederate authentication policy to include the PingOne MFA IdP Adapter, you can challenge users to complete a multi-factor authentication (MFA) step.

## About this task

These steps are designed to help you add to an existing authentication policy. You can find more information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Changes in Version 4.0:**- **Attribute Mapping:** The `id_token` and `access_token` core contracts are removed. You must manually update policies to use `pingone.mfa.enrollment` or `pingone.mfa.device.id`. |

## Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   Learn more in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** area, in the **Select** list, select a PingOne MFA IdP Adapter instance.

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | In the adapter configuration, ensure a selection is made in the **MFA Policy for Authentication** list. |

   ![Adding the to the authentication policy](_images/zcr1599149554163.jpg)

5. Map the PingOne user ID or username into the PingOne MFA IdP Adapter instance.

   |   |                                                                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In version 4.0, the PingOne MFA IdP Adapter returns claims directly in the attribute map. To avoid errors, you must set the **Source** to **Adapter**.Attributes include:- `pingone.mfa.enrollment`

   - `pingone.mfa.device.id`You can use these attributes to define additional policy rules and branches. |

   ![Passing the user ID from the first-factor authentication adapter to the](_images/dnb1651867080726.png)

   1. Under the PingOne MFA IdP Adapter instance, click **Options**.

   2. In the **Options** modal, in the **Source** list, select a previous authentication source that collects the PingOne user ID or username.

      |   |                                                                                                                                                                                                                                                                                                                     |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The adapter uses the **Username Attribute** value as the username when provisioning new users.In version 4.0, the **User Not Found** failure mode only applies if a user does not exist in the directory. It no longer covers disabled users or users with the MFA service disabled, as it did in earlier versions. |

   3. In the **Attribute** list, select the user ID. Click **Done**.

   4. (Optional) Select the **User ID Authenticated** checkbox.

      |   |                                                                                                                                                                                                                                                             |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **User ID Authenticated** checkbox indicates whether the mapped user ID has been authenticated by the authentication source and therefore can be trusted by the current adapter. Device management options are limited if the user isn't authenticated. |

6. (Optional) Define policy paths based on the `pingone.mfa.status` or `pingone.mfa.status.reason` attributes.

   ![Branching the authentication policy based on the pingone.mfa.status attribute.](_images/dxf1601405103816.jpg)

   1. Under the PingOne MFA IdP Adapter instance, click **Rules**.

   2. In the **Rules** modal, in the **Attribute Name** list, select **pingone.mfa.status** or **pingone.mfa.status.reason**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter a value from [PingOne MFA status attributes reference](pf_p1_mfa_ik_p1_mfa_status_attributes_reference_4.0.html).

   5. In the **Result** field, enter a name. This appears as a new policy path that branches from the authentication source.

   6. If you want to add more authentication paths, click **Add** and repeat steps a-e.

   7. Click **Done**.

7. Configure each of the authentication paths.

   ![The complete authentication policy](_images/xxp1599151225895.jpg)

8. Click **Done**.

9. Configure tracked HTTP parameters:

   1. On the **Tracked HTTP Parameters** tab, in the **Parameter Name** field, enter the name of the parameter that you want to track.

      For example:

      * To enable automatic device pairing, enter `mobilePayload`.

   2. Click **Add**.

   3. Click **Save**.

   4. Repeat the previous steps for any other parameters that you want to add.

---

---
title: Adding PingOne Verify to your authentication policy
description: By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter, you can challenge users to verify their identity as part of the authentication process.
component: pingone
page_id: pingone:pingone_verify_integration_kit:pf_p1_verify_ik_adding_p1_verify_to_your_authentication_policy
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit/pf_p1_verify_ik_adding_p1_verify_to_your_authentication_policy.html
revdate: August 2, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adding PingOne Verify to your authentication policy

By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter, you can challenge users to verify their identity as part of the authentication process.

## About this task

Use these steps to add to an existing authentication policy. You can find general information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to **Authentication > Policies > Policies**.

2. On the **Policies** tab, select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   You can find more information in [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** section, in the **Select** list, select a PingOne Verify IdP Adapter instance.

   ![Adding the to the authentication policy](../_images/gvz1607722317720.jpg)

5. Map the PingOne `user ID` or `username` into the PingOne Verify IdP Adapter instance.

   ![Passing the user ID from the first-factor authentication adapter to the](../_images/mar1607722605939.jpg)

   1. Under the PingOne Verify IdP Adapter instance, click **Options**.

   2. On the **Options** window, in the **Source** list, select a previous authentication source that collects the PingOne user ID or username.

   3. In the **Attribute** list, select the user ID.

   4. Select the **User ID Authenticated** checkbox.

   5. Click **Done**.

6. (Optional) Define policy paths based on verification results.

   |   |                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on the failure mode settings in your adapter configuration, the adapter can potentially return a `success` result in the authentication policy even when the user verification process did not succeed. It can be useful to create separate policy paths for a successful adapter result and a successful user verification result. |

   ![Screen shot that shows the Rules dialog in the authentication policy with two paths configured based on the transactionStatus attribute.](../_images/vne1610049349809.png)

   1. Under the PingOne Verify IdP Adapter instance, click **Rules**.

   2. On the **Rules** window, in the **Attribute Name** list, select **transactionStatus**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `SUCCESS` or `BYPASS`.

      * SUCCESS

        The user successfully verified their identity.

      * BYPASS

        An error occurred, and the verification process was not completed, but the adapter is configured to bypass verification and continue the authentication flow.

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the authentication source.

   6. To add more authentication paths, click **Add** and repeat steps a-e.

   7. Click **Done**.

7. Configure each of the authentication paths, including **Fail**, **Success**, and any paths that you defined in the **Rules** window.

   ![The complete authentication policy](../_images/pji1607722789395.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.

---

---
title: Adding PingOne Verify to your authentication policy
description: By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter, you can challenge users to verify their identity as part of the authentication process.
component: pingone
page_id: pingone:pingone_verify_integration_kit_11:pf_p1_verify_ik_adding_p1_verify_to_your_authentication_policy_11
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_verify_integration_kit_11/pf_p1_verify_ik_adding_p1_verify_to_your_authentication_policy_11.html
revdate: August 2, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Adding PingOne Verify to your authentication policy

By modifying your PingFederate authentication policy to include the PingOne Verify IdP Adapter, you can challenge users to verify their identity as part of the authentication process.

## About this task

Use these steps to add to an existing authentication policy. You can find general information about configuring authentication policies in [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html) in the PingFederate documentation.

## Steps

1. In the PingFederate administrative console, go to the **Policies** tab.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Authentication > Policies > Policies**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > Authentication Policies > Policies**.

2. Select the **IdP Authentication Policies** checkbox.

3. Open an existing authentication policy, or click **Add Policy**.

   For more information, see [Defining authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_defining_auth_policies.html) in the PingFederate documentation.

4. In the **Policy** section, in the **Select** list, select a PingOne Verify IdP Adapter instance.

   ![Adding the to the authentication policy](../_images/gvz1607722317720.jpg)

5. Map the PingOne `user ID` or `username` into the PingOne Verify IdP Adapter instance.

   ![Passing the user ID from the first-factor authentication adapter to the](../_images/mar1607722605939.jpg)

   1. Under the PingOne Verify IdP Adapter instance, click **Options**.

   2. On the **Options** window, in the **Source** list, select a previous authentication source that collects the PingOne user ID or username.

   3. In the **Attribute** list, select the user ID.

   4. For PingFederate 10.2 and later, select the **User ID Authenticated** checkbox.

   5. Click **Done**.

6. **Optional:** Define policy paths based on verification results.

   |   |                                                                                                                                                                                                                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on the failure mode settings in your adapter configuration, the adapter can potentially return a `success` result in the authentication policy even when the user verification process did not succeed. It can be useful to create separate policy paths for a successful adapter result and a successful user verification result. |

   ![Screen shot that shows the Rules dialog in the authentication policy with two paths configured based on the transactionStatus attribute.](../_images/vne1610049349809.png)

   1. Under the PingOne Verify IdP Adapter instance, click **Rules**.

   2. On the **Rules** window, in the **Attribute Name** list, select **transactionStatus**.

   3. In the **Condition** list, select **equal to**.

   4. In the **Value** field, enter `SUCCESS` or `BYPASS`.

      * SUCCESS

        The user successfully verified their identity.

      * BYPASS

        An error occurred, and the verification process was not completed, but the adapter is configured to bypass verification and continue the authentication flow.

   5. In the **Result** field, enter a name.

      This appears as a new policy path that branches from the authentication source.

   6. To add more authentication paths, click **Add** and repeat steps a-e.

   7. Click **Done**.

7. Configure each of the authentication paths, including **Fail**, **Success**, and any paths that you defined in the **Rules** window.

   ![The complete authentication policy](../_images/pji1607722789395.jpg)

8. Click **Done**.

9. In the **Policies** window, click **Save**.

---

---
title: CIBA prompt customizations
description: Client-initiated backchannel authentication (CIBA) involves prompting a user to accept or reject a request. You can customize the request prompt using pre-defined attributes or map complex custom attributes.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_ciba_prompt_customizations
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_ciba_prompt_customizations.html
revdate: June 15, 2024
section_ids:
  simple-prompt-customizations: Simple prompt customizations
  advanced-prompt-customizations: Advanced prompt customizations
---

# CIBA prompt customizations

Client-initiated backchannel authentication (CIBA) involves prompting a user to accept or reject a request. You can customize the request prompt using pre-defined attributes or map complex custom attributes.

## Simple prompt customizations

For simple, centralized customizations, you can modify the notification template that PingOne uses to generate the request prompt. Notification template customizations allow you to use the following:

* Static text

* A pre-defined set of attributes from the client request context

Simple prompt customizations require changes to the PingOne notification template only.

* Location: **PingOne console > Experiences > Notifications**.

You can find more descriptions and examples in [Simple CIBA prompt customizations](pf_p1_mfa_ik_simple_ciba_prompt_customizations.html).

## Advanced prompt customizations

If you need more advanced customizations in the request prompt, you can define custom attributes in PingFederate and pass them to PingOne.

The PingOne MFA CIBA Authenticator allows you to use the following:

* Static text

* Modified attributes from the client request context

* Contract attributes from the PingFederate CIBA request policy

* Messages from the PingFederate language-pack localization files

* Apache Velocity Template Language code to manipulate any of the above

Advanced prompt customizations require coordinated changes to all the following:

* The PingOne notification template

  * Location: **PingOne console > Experiences > Notifications**.

* The **PingOne Template Variables** table of the PingOne MFA CIBA Authenticator instance

  * Location: **PingFederate console > Authentication > OAuth > CIBA Authenticators > Your PingOne MFA CIBA Authenticator instance > Instance Configuration**.

* The **Extended Contract** tab of the PingOne MFA CIBA Authenticator instance

  * Location: **PingFederate console > Authentication > OAuth > CIBA Authenticators > Your PingOne MFA CIBA Authenticator instance > Instance Configuration**.

* The PingFederate CIBA request policy

  * Location: **PingFederate console > Applications > OAuth > CIBA Request Policies > Your CIBA request policy > Contract Fulfillment**.

You can find more descriptions and examples in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations.html).

---

---
title: CIBA prompt customizations
description: Client-initiated backchannel authentication (CIBA) involves prompting a user to accept or reject a request. You can customize the request prompt using pre-defined attributes or map complex custom attributes.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_4.0:pf_p1_mfa_ik_ciba_prompt_customizations_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_4.0/pf_p1_mfa_ik_ciba_prompt_customizations_4.0.html
revdate: June 15, 2024
section_ids:
  simple-prompt-customizations: Simple prompt customizations
  advanced-prompt-customizations: Advanced prompt customizations
---

# CIBA prompt customizations

Client-initiated backchannel authentication (CIBA) involves prompting a user to accept or reject a request. You can customize the request prompt using pre-defined attributes or map complex custom attributes.

## Simple prompt customizations

For simple, centralized customizations, you can modify the notification template that PingOne uses to generate the request prompt. Notification template customizations allow you to use the following:

* Static text

* A pre-defined set of attributes from the client request context

Simple prompt customizations require changes to the PingOne notification template only.

* Location: **PingOne console > Experiences > Notifications**.

You can find more descriptions and examples in [Simple CIBA prompt customizations](pf_p1_mfa_ik_simple_ciba_prompt_customizations_4.0.html).

## Advanced prompt customizations

If you need more advanced customizations in the request prompt, you can define custom attributes in PingFederate and pass them to PingOne.

The PingOne MFA CIBA Authenticator allows you to use the following:

* Static text

* Modified attributes from the client request context

* Contract attributes from the PingFederate CIBA request policy

* Messages from the PingFederate language-pack localization files

* Apache Velocity Template Language code to manipulate any of the above

Advanced prompt customizations require coordinated changes to all the following:

* The PingOne notification template

  * Location: **PingOne console > Experiences > Notifications**.

* The **PingOne Template Variables** table of the PingOne MFA CIBA Authenticator instance

  * Location: **PingFederate console > Authentication > OAuth > CIBA Authenticators > Your PingOne MFA CIBA Authenticator instance > Instance Configuration**.

* The **Extended Contract** tab of the PingOne MFA CIBA Authenticator instance

  * Location: **PingFederate console > Authentication > OAuth > CIBA Authenticators > Your PingOne MFA CIBA Authenticator instance > Instance Configuration**.

* The PingFederate CIBA request policy

  * Location: **PingFederate console > Applications > OAuth > CIBA Request Policies > Your CIBA request policy > Contract Fulfillment**.

You can find more descriptions and examples in [Advanced CIBA prompt customizations](pf_p1_mfa_ik_advanced_ciba_prompt_customizations_4.0.html).

---

---
title: CIBA request flow
description: When a client makes a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, PingFederate can modify and add to the request information before sending it to PingOne MFA.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_ciba_request_flow
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_ciba_request_flow.html
revdate: June 15, 2024
---

# CIBA request flow

When a client makes a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, PingFederate can modify and add to the request information before sending it to PingOne MFA.

The following steps are involved in conveying the CIBA request information from the client application to the request prompt that the user sees on their mobile device.

1. The client application sends a CIBA request to PingFederate that includes some request context attributes.

2. The CIBA request policy collects attributes from the client request and other attribute sources that you configure, such as a data store.

3. The PingOne MFA CIBA Authenticator parses the client request attributes. The authenticator also processes any custom attribute definitions, as described in [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations.html).

4. The authenticator sends the attributes to PingOne along with information to identify which PingOne notification template to use for the user prompt.

5. PingOne uses the attributes from the PingOne MFA CIBA Authenticator to populate the variables in a customizable notification template.

6. PingOne sends the notification to the mobile app, which is built with the PingOne Mobile SDK.

7. The mobile app show the request prompt to the user to approve or deny.

---

---
title: CIBA request flow
description: When a client makes a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, PingFederate can modify and add to the request information before sending it to PingOne MFA.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_4.0:pf_p1_mfa_ik_ciba_request_flow_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_4.0/pf_p1_mfa_ik_ciba_request_flow_4.0.html
revdate: June 15, 2024
---

# CIBA request flow

When a client makes a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, PingFederate can modify and add to the request information before sending it to PingOne MFA.

The following steps are involved in conveying the CIBA request information from the client application to the request prompt that the user sees on their mobile device.

1. The client application sends a CIBA request to PingFederate that includes some request context attributes.

2. The CIBA request policy collects attributes from the client request and other attribute sources that you configure, such as a data store.

3. The PingOne MFA CIBA Authenticator parses the client request attributes. The authenticator also processes any custom attribute definitions, as described in [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations_4.0.html).

4. The authenticator sends the attributes to PingOne along with information to identify which PingOne notification template to use for the user prompt.

5. PingOne uses the attributes from the PingOne MFA CIBA Authenticator to populate the variables in a customizable notification template.

6. PingOne sends the notification to the mobile app, which is built with the PingOne Mobile SDK.

7. The mobile app show the request prompt to the user to approve or deny.

---

---
title: CIBA setup
description: When a client application sends a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, the PingOne MFA CIBA Authenticator allows PingFederate to initiate an out-of-band authentication request using PingOne MFA.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_3.2:pf_p1_mfa_ik_ciba_setup
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_3.2/pf_p1_mfa_ik_ciba_setup.html
revdate: June 15, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# CIBA setup

When a client application sends a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, the PingOne MFA CIBA Authenticator allows PingFederate to initiate an out-of-band authentication request using PingOne MFA.

## About this task

By completing the steps below, you can show CIBA prompts on the mobile device that a user has paired with their PingOne MFA account.

For general information about CIBA, see [Client Initiated Backchannel Authentication (CIBA)](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ciba.html) in the PingFederate documentation. Note that the CIBA Authenticator mentioned on that page is different from the PingOne MFA CIBA Authenticator.

For detailed information about the following steps, see [CIBA request flow](pf_p1_mfa_ik_ciba_request_flow.html) and [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations.html).

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | The CIBA setup section is optional and independent from the MFA setup section. |

## Steps

1. In PingOne, complete the steps in [Creating a CIBA authentication policy in PingOne](pf_p1_mfa_ik_creating_a_ciba_authentication_policy_p1.html).

2. In PingFederate, complete the steps in [Configuring a CIBA authenticator instance](pf_p1_mfa_ik_configuring_a_ciba_authenticator_instance.html).

3. In PingFederate, create a CIBA request policy as shown in [Managing CIBA request policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_cibapoliciesmanagementtasklet_cibapoliciesmanagementstate.html) in the PingFederate documentation.

---

---
title: CIBA setup
description: When a client application sends a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, the PingOne MFA CIBA Authenticator allows PingFederate to initiate an out-of-band authentication request using PingOne MFA.
component: pingone
page_id: pingone:pingone_mfa_integration_kit_4.0:pf_p1_mfa_ik_ciba_setup_4.0
canonical_url: https://docs.pingidentity.com/integrations/pingone/pingone_mfa_integration_kit_4.0/pf_p1_mfa_ik_ciba_setup_4.0.html
revdate: June 15, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# CIBA setup

When a client application sends a Client Initiated Backchannel Authentication (CIBA) request to PingFederate, the PingOne MFA CIBA Authenticator allows PingFederate to initiate an out-of-band authentication request using PingOne MFA.

## About this task

By completing the steps below, you can show CIBA prompts on the mobile device that a user has paired with their PingOne MFA account.

For general information about CIBA, see [Client Initiated Backchannel Authentication (CIBA)](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ciba.html) in the PingFederate documentation. Note that the CIBA Authenticator mentioned on that page is different from the PingOne MFA CIBA Authenticator.

For detailed information about the following steps, see [CIBA request flow](pf_p1_mfa_ik_ciba_request_flow_4.0.html) and [CIBA prompt customizations](pf_p1_mfa_ik_ciba_prompt_customizations_4.0.html).

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | The CIBA setup section is optional and independent from the MFA setup section. |

## Steps

1. In PingOne, complete the steps in [Creating a CIBA authentication policy in PingOne](pf_p1_mfa_ik_creating_a_ciba_authentication_policy_p1_4.0.html).

2. In PingFederate, complete the steps in [Configuring a CIBA authenticator instance](pf_p1_mfa_ik_configuring_a_ciba_authenticator_instance_4.0.html).

3. In PingFederate, create a CIBA request policy as shown in [Managing CIBA request policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_cibapoliciesmanagementtasklet_cibapoliciesmanagementstate.html) in the PingFederate documentation.