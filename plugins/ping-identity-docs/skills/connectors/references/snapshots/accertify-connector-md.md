---
title: Accertify Connector
description: The Accertify connector lets you send identity lifecycle events to the Accertify fraud detection platform from your PingOne DaVinci flow.
component: connectors
page_id: connectors::accertify_connector
canonical_url: https://docs.pingidentity.com/connectors/accertify_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 15, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-accertify-connector: Configuring the Accertify connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  collecting-accertify-device-and-behavioral-data: Collecting Accertify device and behavioral data
  assessing-login-risk: Assessing login risk
  capabilities: Capabilities
  loginEvent: Submit Login Event
  verificationEvent: Submit Verification Event
  accountCreateEvent: Submit Account Create Event
  accountUpdateEvent: Submit Account Update Event
  passwordForgotEvent: Submit Password Forgot Event
  passwordUpdateEvent: Submit Password Update Event
---

# Accertify Connector

The Accertify connector lets you send identity lifecycle events to the [Accertify](https://www.accertify.com/) fraud detection platform from your PingOne DaVinci flow.

The connector sends events to the Accertify API at key moments in the user journey, such as login, account creation, and password changes. It then returns a fraud risk score and recommendations your flow can use to allow, challenge, or block the user.

## Setup

### Resources

You can find more information and setup help in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An Accertify account with API access.

* The base URL for your Accertify environment (including https\://).

* Your Accertify API username and password.

* Your Accertify collector script URL for the environment where the flow runs.

|   |                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The Accertify collector script is a required part of the integration for web-based risk events. It gathers the device and behavioral values that Accertify expects to receive with the event, such as ubaID, ubaEvents, pageID, ubaSessionID, deviceTransactionID, and optionally devicePayload. |

### Configuring the Accertify connector

[Add the connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html) in DaVinci, then configure it as follows.

#### Connector configuration

| Setting      | Description                                                                                |
| ------------ | ------------------------------------------------------------------------------------------ |
| **Base URL** | The base URL for your Accertify API environment (for example, https\://api.accertify.com). |
| **Username** | The username used to build the Authorization: Basic header for Accertify API requests.     |
| **Password** | The password used to build the Authorization: Basic header for Accertify API requests.     |

## Using the connector in a flow

### Collecting Accertify device and behavioral data

Before calling an Accertify capability, add an HTTP connector with the **Custom HTML Template** capability to your flow. Place this node immediately before the Accertify connector node (typically right after the sign-on form).

The collector node loads the Accertify collector script, gathers device and behavioral data, stores the values in hidden form fields, and automatically advances the flow.

|   |                                                                                                  |
| - | ------------------------------------------------------------------------------------------------ |
|   | Use devicePayload when available. Do not send both devicePayload and devTID in the same request. |

To configure the collector node:

1. Add an **HTTP connector** with the **Custom HTML Template** capability to your flow.

2. On the **General** tab, in the **HTML Template** field, add the following:

   ```html
   <div class="end-user-nano">
     <div
       class="bg-light d-flex flex-column justify-content-center align-items-center position-absolute top-0 start-0 bottom-0 end-0 overflow-auto">
       <div style="max-width: 400px; min-width: 400px; width: 100%">
         <div class="card shadow mb-5">
           <div class="card-body p-5 d-flex flex-column">
             <img class="companyLogo align-self-center mb-5" src="{{global.variables.companyLogo}}" alt="{{global.variables.companyName}}" />
             <div class="d-flex justify-content-center align-items-center mt-4 mb-5">
               <div class="spinner-border thicker-spinner spinner-color" role="status">
                 <span class="sr-only"></span>
               </div>
             </div>
             {{#if title}}
             <h1 class="text-center mt-3 mb-4">{{title}}</h1>
             {{/if}}
             <div id="accertifyMount" style="display:none;">
               <form id="accertifyForm">
                 <input type="hidden" id="devTID" name="devTID" value="" />
                 <input type="hidden" id="ubaSessionId" name="ubaSessionId" value="" />
                 <input type="hidden" id="ubaId" name="ubaId" value="" />
                 <input type="hidden" id="pageId" name="pageId" value="" />
                 <input type="hidden" id="ubaEvents" name="ubaEvents" value="" />
                 <input type="hidden" id="devicePayload" name="devicePayload" value="" />
                 <button
                   data-id="button"
                   style="display:none"
                   type="submit"
                   class="btn btn-primary mb-3"
                   data-skcomponent="skbutton"
                   data-skbuttontype="form-submit"
                   id="btnSubmit"
                   data-skform="accertifyForm"
                   data-skbuttonvalue="SIGNON">
                   Continue
                 </button>
               </form>
             </div>
           </div>
         </div>
       </div>
     </div>
   </div>
   ```

3. In the **CSS** field, add the following:

   ```css
   .spinner-border.thicker-spinner {
       border-width: 0.3em;
       width: 65px;
       height: 65px;
   }

   .spinner-border {
       animation-duration: 1.25s;
   }

   .spinner-color {
       --bs-text-opacity: .1;
       color: rgba(39, 123, 165, 1);
   }
   ```

4. In the **Script** field, replace DATA\_COLLECTOR\_URL with the collector script URL for your Accertify environment, then add the following:

   ```javascript
   var DATA_COLLECTOR_URL = "YOUR_COLLECTOR_SCRIPT_URL";

   var s = document.createElement('script');
   s.setAttribute('type', 'text/javascript');
   s.setAttribute('src', DATA_COLLECTOR_URL);
   s.setAttribute('dvct', '500');
   s.setAttribute('id', 'bcn');
   s.setAttribute('dvc', 'a');

   s.onload = function() {
       if (window.hasOwnProperty('_bcn') && window._bcn.hasOwnProperty('dvc')) {
           window._bcn.dvc.setSubmissionCallback(registeredCallBackMethod);
       }
   };

   document.head.appendChild(s);

   function registeredCallBackMethod() {
       if (window.hasOwnProperty('_bcn') && window._bcn.hasOwnProperty('dvc')) {
           const tid = window._bcn.dvc.getTID();

           const devTidEl = document.getElementById("devTID");
           if (devTidEl) {
               devTidEl.value = tid || '';
           }

           try {
               const collector = (window._bcn && window._bcn.collector) || window.collector;
               if (collector && typeof collector.getPayload === 'function' && tid) {
                   const payloadObj = collector.getPayload(tid);
                   const devicePayload = payloadObj && payloadObj.payload;

                   if (devicePayload) {
                       const payloadEl = document.getElementById("devicePayload");
                       if (payloadEl) {
                           payloadEl.value = devicePayload;
                       }
                   }
               }
           } catch (e) {
               console.warn('Unable to retrieve device payload from Accertify collector', e);
           }
       }
   }

   setTimeout(() => {
       if (window.hasOwnProperty('_bcn')) {
           window._bcn.flush();
           document.getElementById("ubaId").value = window._bcn.getToken();
           document.getElementById("ubaSessionId").value = window._bcn.getUbaSessionId();
           document.getElementById("pageId").value = window._bcn.getPageId();
           document.getElementById("ubaEvents").value = window._bcn.getEvents();
       }
       const button = document.getElementById("btnSubmit");
       if (button) {
           button.click();
       }
   }, 3000);
   ```

5. In the **Output Fields List**, add each of the following hidden input field names into the **Property Name** field, then click **Apply**:

   * devTID

   * ubaSessionId

   * ubaId

   * pageId

   * ubaEvents

   * devicePayload

6. Map the output fields to the corresponding inputs on the Accertify capability node in your flow.

### Assessing login risk

![A screen capture of the complete Accertify login event flow.](_images/connector-images/tap-accertify-submit-login-event-flow.png)

This flow collects the user's username and password in a PingOne Forms node, runs the Accertify collector script in an HTTP node, and then sends a login event to Accertify. The **Submit Login Event** node receives the user's IP address, user agent, collector values, and account identifier, then returns a risk score and recommendations the flow can branch on to allow access, trigger a step-up challenge, or block the attempt.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Submit Login Event

Sends a login event payload to Accertify to receive a fraud/risk recommendation for the login attempt.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Event Source dropDown required
>
>   Where or how the event originated.
>
>   * agentPhone
>
>   * agentStore
>
>   * affiliate
>
>   * kiosk
>
>   * mobileApp
>
>   * other
>
>   * web
>
> - Success toggleSwitch required
>
>   Whether the event was successful or not.
>
> - IP Address textField
>
>   User's IP address.
>
> - User Agent textField
>
>   User agent of the user's browser/OS.
>
> - Device Payload textField
>
>   Accertify Device payload from the collector script (recommended over Device Transaction ID).
>
> - Device Transaction ID textField
>
>   Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
> - UBA ID textField
>
>   Accertify UBA ID used to reference behavior data.
>
> - UBA Session ID textField
>
>   The user's Session ID defined by Accertify for the user's web browsing activity.
>
> - Page ID textField
>
>   UBA unique page ID defined from the collector script.
>
> - UBA Events textField
>
>   UBA recent events payload.
>
> - Email Address textField
>
>   Email address associated with the account or event.
>
> - Username textField
>
>   User's username (if applicable).
>
> - Authentication Method dropDown
>
>   How the user authenticated.
>
>   * appAuthenticator
>
>   * appPush
>
>   * FIDO
>
>   * other
>
>   * password
>
>   * magicLink
>
>   * SMS
>
> - Account ID textField
>
>   User's unique identifier assigned by your system.
>
> - Is Mobile App Installed toggleSwitch
>
>   Whether the account has the mobile application installed somewhere.
>
> - Failure Code textField
>
>   Login Event failure code.
>
> * default object
>
>   * properties object
>
>     * eventSource string required
>
>       Where or how the event originated.
>
>     * success boolean required
>
>       Whether the login attempt was successful.
>
>     * ipAddress string
>
>       User's IP address.
>
>     * userAgent string
>
>       User agent of the user's browser/OS.
>
>     * devicePayload string
>
>       Accertify Device payload from the collector script (recommended over deviceTransactionID).
>
>     * deviceTransactionID string
>
>       Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
>     * ubaID string
>
>       Accertify UBA ID used to reference behavior data.
>
>     * ubaSessionID string
>
>       Accertify UBA session ID for the event.
>
>     * pageID string
>
>       UBA unique page ID defined from the collector script.
>
>     * ubaEvents string
>
>       UBA recent events payload.
>
>     * emailAddress string
>
>       Email address associated with the account or event.
>
>     * username string
>
>       User's username (if your site allows login by username).
>
>     * authenticationMethod string
>
>       How the user authenticated onto your site.
>
>     * accountID string
>
>       User's unique identifier you assigned.
>
>     * isMobileAppInstalled boolean
>
>       Whether the account has the mobile application installed somewhere, regardless of where the event occurred.
>
>     * loginEventFailureCode string
>
>       Login Event failure code.
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * eventID string
>
>   * status boolean
>
>   * messages object
>
>     * warning array
>
>     * error array
>
>     * info array
>
>   * eventDetails object
>
>   * results object

### Submit Verification Event

Sends a verification event payload to Accertify to record the outcome of a verification (MFA/email/SMS) for a prior login event.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Event Source dropDown required
>
>   Where or how the event originated.
>
>   * agentPhone
>
>   * agentStore
>
>   * affiliate
>
>   * kiosk
>
>   * mobileApp
>
>   * other
>
>   * web
>
> - Account ID textField
>
>   User's unique identifier assigned by your system.
>
> - Success toggleSwitch required
>
>   Whether the event was successful or not.
>
> - IP Address textField
>
>   User's IP address.
>
> - User Agent textField
>
>   User agent of the user's browser/OS.
>
> - Device Payload textField
>
>   Accertify Device payload from the collector script (recommended over Device Transaction ID).
>
> - Device Transaction ID textField
>
>   Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
> - UBA ID textField
>
>   Accertify UBA ID used to reference behavior data.
>
> - UBA Session ID textField
>
>   The user's Session ID defined by Accertify for the user's web browsing activity.
>
> - Page ID textField
>
>   UBA unique page ID defined from the collector script.
>
> - UBA Events textField
>
>   UBA recent events payload.
>
> - Email Address textField
>
>   Email address associated with the account or event.
>
> - Username textField
>
>   User's username (if applicable).
>
> - Authentication Method dropDown
>
>   How the user authenticated.
>
>   * appAuthenticator
>
>   * appPush
>
>   * FIDO
>
>   * other
>
>   * password
>
>   * magicLink
>
>   * SMS
>
> - Verification Type dropDown
>
>   Kind of verification the user attempted.
>
>   * appAuthenticator
>
>   * appPush
>
>   * captcha
>
>   * email
>
>   * FIDO
>
>   * kbAnswers
>
>   * magicLink
>
>   * other
>
>   * phoneCall
>
>   * securityQuestions
>
>   * sms
>
> - Verification Status dropDown
>
>   Status of the verification (mapped to failureCode in the doc).
>
>   * abandoned
>
>   * expired
>
>   * fail
>
>   * success
>
> - Verification Attempts textField
>
>   Number of attempts the user tried to verify.
>
> - Update Event ID textField
>
>   eventID that triggered the verification.
>
> - Update Event Type dropDown
>
>   Event type that triggered the verification.
>
>   * accountCreate
>
>   * accountUpdate
>
>   * giftCardBalance
>
>   * inventoryHold
>
>   * listingCreate
>
>   * listingUpdate
>
>   * login
>
>   * logout
>
>   * passwordForgot
>
>   * passwordUpdate
>
>   * payment
>
>   * refund
>
>   * transfer
>
>   * usernameForgot
>
> - Update Event Recommendation Detail textField
>
>   The recommendationDetail returned by Accertify for the original event.
>
> - Failure Code textField
>
>   Verification Event failure code.
>
> * default object
>
>   * properties object
>
>     * eventSource string required
>
>       Where or how the event originated.
>
>     * accountID string required
>
>       User's unique identifier assigned by your system.
>
>     * success boolean required
>
>       Whether the verification event was successful.
>
>     * ipAddress string
>
>       User's IP address.
>
>     * userAgent string
>
>       User agent of the user's browser/OS.
>
>     * devicePayload string
>
>       Accertify Device payload from the collector script (recommended over deviceTransactionID).
>
>     * deviceTransactionID string
>
>       Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
>     * ubaID string
>
>       Accertify UBA ID used to reference behavior data.
>
>     * ubaSessionID string
>
>       Accertify UBA session ID for the event.
>
>     * pageID string
>
>       UBA unique page ID defined from the collector script.
>
>     * ubaEvents string
>
>       UBA recent events payload.
>
>     * emailAddress string
>
>       Email address associated with the account or event.
>
>     * username string
>
>       User's username (if your site allows login by username).
>
>     * authenticationMethod string
>
>       How the user authenticated onto your site.
>
>     * verificationType string
>
>       Kind of verification the user attempted.
>
>     * verificationStatus string
>
>       Status of the verification (mapped to failureCode in the doc).
>
>     * verificationAttempts string
>
>       Number of attempts the user tried to verify.
>
>     * updateEventID string
>
>       eventID that triggered the verification (from the original login event).
>
>     * updateEventType string
>
>       Event type that triggered the verification (e.g., login, passwordUpdate).
>
>     * updateEventRecommendationDetail string
>
>       The recommendationDetail Accertify returned for the original event.
>
>     * verificationFailureCode string
>
>       Event failure code (abandoned / expired / fail / newCodeWithinExpiry / other).
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * eventID string
>
>   * status boolean
>
>   * messages object
>
>     * warning array
>
>     * error array
>
>     * info array
>
>   * eventDetails object
>
>     * deviceDetails object
>
>     * connectionDetails object
>
>   * results object

### Submit Account Create Event

Sends an account creation event payload to Accertify to receive a fraud/risk recommendation for the account creation attempt.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Event Source dropDown required
>
>   Where or how the event originated.
>
>   * agentPhone
>
>   * agentStore
>
>   * affiliate
>
>   * kiosk
>
>   * mobileApp
>
>   * other
>
>   * web
>
> - Success toggleSwitch required
>
>   Whether the event was successful or not.
>
> - IP Address textField
>
>   User's IP address.
>
> - User Agent textField
>
>   User agent of the user's browser/OS.
>
> - Device Payload textField
>
>   Accertify Device payload from the collector script (recommended over Device Transaction ID).
>
> - Device Transaction ID textField
>
>   Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
> - UBA ID textField
>
>   Accertify UBA ID used to reference behavior data.
>
> - UBA Session ID textField
>
>   The user's Session ID defined by Accertify for the user's web browsing activity.
>
> - Page ID textField
>
>   UBA unique page ID defined from the collector script.
>
> - UBA Events textField
>
>   UBA recent events payload.
>
> - Email Address textField
>
>   Email address associated with the account or event.
>
> - Username textField
>
>   User's username (if applicable).
>
> - Authentication Method dropDown
>
>   How the user authenticated.
>
>   * appAuthenticator
>
>   * appPush
>
>   * FIDO
>
>   * other
>
>   * password
>
>   * magicLink
>
>   * SMS
>
> - Hashed Password textField
>
>   Hashed password (do not provide a plaintext password).
>
> - First Name textField
>
>   User's first name.
>
> - Middle Name textField
>
>   User's middle name.
>
> - Last Name textField
>
>   User's last name.
>
> - Account Create Failure Code dropDown
>
>   Failure code for account create attempts.
>
>   * accountExists
>
>   * exportCompliance
>
>   * unsupportedLocation
>
>   * other
>
> * default object
>
>   * properties object
>
>     * eventSource string required
>
>       Where or how the event originated.
>
>     * success boolean required
>
>       Whether the account creation attempt was successful.
>
>     * ipAddress string
>
>       User's IP address.
>
>     * userAgent string
>
>       User agent of the user's browser/OS.
>
>     * devicePayload string
>
>       Accertify Device payload from the collector script (recommended over deviceTransactionID).
>
>     * deviceTransactionID string
>
>       Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
>     * ubaID string
>
>       Accertify UBA ID used to reference behavior data.
>
>     * ubaSessionID string
>
>       Accertify UBA session ID for the event.
>
>     * pageID string
>
>       UBA unique page ID defined from the collector script.
>
>     * ubaEvents string
>
>       UBA recent events payload.
>
>     * emailAddress string
>
>       Email address associated with the account creation event.
>
>     * username string
>
>       User's username (if applicable).
>
>     * authenticationMethod string
>
>       How the user authenticated onto your site.
>
>     * hashedPassword string
>
>       Hashed password (do not provide plaintext).
>
>     * firstName string
>
>       User's first name.
>
>     * middleName string
>
>       User's middle name.
>
>     * lastName string
>
>       User's last name.
>
>     * accountCreateFailureCode string
>
>       Failure code for account creation.
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * eventID string
>
>   * status boolean
>
>   * messages object
>
>     * warning array
>
>     * error array
>
>     * info array
>
>   * eventDetails object
>
>   * results object

### Submit Account Update Event

Sends an account update event payload to Accertify to receive a fraud/risk recommendation.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Event Source dropDown required
>
>   Where or how the event originated.
>
>   * agentPhone
>
>   * agentStore
>
>   * affiliate
>
>   * kiosk
>
>   * mobileApp
>
>   * other
>
>   * web
>
> - Account ID textField
>
>   User's unique identifier assigned by your system.
>
> - IP Address textField
>
>   User's IP address.
>
> - User Agent textField
>
>   User agent of the user's browser/OS.
>
> - Device Payload textField
>
>   Accertify Device payload from the collector script (recommended over Device Transaction ID).
>
> - Device Transaction ID textField
>
>   Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
> - UBA ID textField
>
>   Accertify UBA ID used to reference behavior data.
>
> - UBA Session ID textField
>
>   The user's Session ID defined by Accertify for the user's web browsing activity.
>
> - Page ID textField
>
>   UBA unique page ID defined from the collector script.
>
> - UBA Events textField
>
>   UBA recent events payload.
>
> - Email Address textField
>
>   Email address associated with the account or event.
>
> - Username textField
>
>   User's username (if applicable).
>
> - Authentication Method dropDown
>
>   How the user authenticated.
>
>   * appAuthenticator
>
>   * appPush
>
>   * FIDO
>
>   * other
>
>   * password
>
>   * magicLink
>
>   * SMS
>
> - Previous Email Address textField
>
>   Email address before the account update.
>
> - Previous Payment Type textField
>
>   Previous payment method type.
>
> - Previous Card Number textField
>
>   Previous credit card number (hashed or tokenized).
>
> - Previous Expiration Month textField
>
>   Previous expiration month (MM).
>
> - Previous Expiration Year textField
>
>   Previous expiration year (YYYY).
>
> - Previous Expiration Day textField
>
>   Previous expiration day (DD).
>
> - Previous Name on Card textField
>
>   Previous cardholder name.
>
> - Previous Card BIN textField
>
>   Previous leading digits (BIN).
>
> - Previous Card Last Four textField
>
>   Previous last four digits.
>
> - Previous AVS Result textField
>
>   Previous AVS result.
>
> - Previous CVV Result textField
>
>   Previous CVV result.
>
> - Updated Email Address textField
>
>   Email address after the account update.
>
> - Updated Payment Type textField
>
>   Updated payment method type.
>
> - Updated Card Number textField
>
>   Updated credit card number (hashed or tokenized).
>
> - Updated Expiration Month textField
>
>   Updated expiration month (MM).
>
> - Updated Expiration Year textField
>
>   Updated expiration year (YYYY).
>
> - Updated Expiration Day textField
>
>   Updated expiration day (DD).
>
> - Updated Name on Card textField
>
>   Updated cardholder name.
>
> - Updated Card BIN textField
>
>   Updated leading digits (BIN).
>
> - Updated Card Last Four textField
>
>   Updated last four digits.
>
> - Updated AVS Result textField
>
>   Updated AVS result.
>
> - Updated CVV Result textField
>
>   Updated CVV result.
>
> * default object
>
>   * properties object
>
>     * eventSource string required
>
>     * accountID string required
>
>     * ipAddress string
>
>     * userAgent string
>
>     * devicePayload string
>
>     * deviceTransactionID string
>
>     * ubaID string
>
>     * ubaSessionID string
>
>     * pageID string
>
>     * ubaEvents string
>
>     * emailAddress string
>
>     * username string
>
>     * authenticationMethod string
>
>     * previousEmailAddress string
>
>     * previousPaymentType string
>
>     * previousCardNumber string
>
>     * previousExpirationMonth string
>
>     * previousExpirationYear string
>
>     * previousExpirationDay string
>
>     * previousNameOnCreditCard string
>
>     * previousCardBin string
>
>     * previousCardLastFour string
>
>     * previousAvsResult string
>
>     * previousCvvResult string
>
>     * updatedEmailAddress string
>
>     * updatedPaymentType string
>
>     * updatedCardNumber string
>
>     * updatedExpirationMonth string
>
>     * updatedExpirationYear string
>
>     * updatedExpirationDay string
>
>     * updatedNameOnCreditCard string
>
>     * updatedCardBin string
>
>     * updatedCardLastFour string
>
>     * updatedAvsResult string
>
>     * updatedCvvResult string
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * eventID string
>
>   * status boolean
>
>   * messages object
>
>     * warning array
>
>     * error array
>
>     * info array
>
>   * eventDetails object
>
>   * results object

### Submit Password Forgot Event

Sends a password forgot event payload to Accertify to receive a fraud/risk recommendation for the password recovery attempt.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Event Source dropDown required
>
>   Where or how the event originated.
>
>   * agentPhone
>
>   * agentStore
>
>   * affiliate
>
>   * kiosk
>
>   * mobileApp
>
>   * other
>
>   * web
>
> - Success toggleSwitch required
>
>   Whether the event was successful or not.
>
> - IP Address textField
>
>   User's IP address.
>
> - User Agent textField
>
>   User agent of the user's browser/OS.
>
> - Device Payload textField
>
>   Accertify Device payload from the collector script (recommended over Device Transaction ID).
>
> - Device Transaction ID textField
>
>   Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
> - UBA ID textField
>
>   Accertify UBA ID used to reference behavior data.
>
> - UBA Session ID textField
>
>   The user's Session ID defined by Accertify for the user's web browsing activity.
>
> - Page ID textField
>
>   UBA unique page ID defined from the collector script.
>
> - UBA Events textField
>
>   UBA recent events payload.
>
> - Email Address textField
>
>   Email address associated with the account or event.
>
> - Username textField
>
>   User's username (if applicable).
>
> - Authentication Method dropDown
>
>   How the user authenticated.
>
>   * appAuthenticator
>
>   * appPush
>
>   * FIDO
>
>   * other
>
>   * password
>
>   * magicLink
>
>   * SMS
>
> * default object
>
>   * properties object
>
>     * eventSource string required
>
>       Where or how the event originated.
>
>     * success boolean required
>
>       Whether the event was successful or not.
>
>     * ipAddress string
>
>       User's IP address.
>
>     * userAgent string
>
>       User agent of the user's browser/OS.
>
>     * devicePayload string
>
>       Accertify Device payload from the collector script.
>
>     * deviceTransactionID string
>
>       Accertify Device transaction ID from collector JS/SDK (legacy).
>
>     * ubaID string
>
>       Accertify UBA ID used to reference behavior data.
>
>     * ubaSessionID string
>
>       Accertify UBA session ID for the event.
>
>     * pageID string
>
>       UBA unique page ID defined from the collector script.
>
>     * ubaEvents string
>
>       UBA recent events payload.
>
>     * emailAddress string
>
>       Email address associated with the account/event.
>
>     * username string
>
>       User's username (if applicable).
>
>     * authenticationMethod string
>
>       How the user authenticated onto your site.
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * eventID string
>
>   * status boolean
>
>   * messages object
>
>     * warning array
>
>     * error array
>
>     * info array
>
>   * eventDetails object
>
>   * results object

### Submit Password Update Event

Sends a password update event payload to Accertify to receive a fraud/risk recommendation for the password reset completion.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Event Source dropDown required
>
>   Where or how the event originated.
>
>   * agentPhone
>
>   * agentStore
>
>   * affiliate
>
>   * kiosk
>
>   * mobileApp
>
>   * other
>
>   * web
>
> - Account ID textField
>
>   User's unique identifier assigned by your system.
>
> - Update Trigger dropDown required
>
>   Trigger that caused the password to be updated.
>
>   * agent
>
>   * customerInitiated
>
>   * forcedPasswordReset
>
>   * other
>
>   * passwordExpired
>
> - IP Address textField
>
>   User's IP address.
>
> - User Agent textField
>
>   User agent of the user's browser/OS.
>
> - Device Payload textField
>
>   Accertify Device payload from the collector script (recommended over Device Transaction ID).
>
> - Device Transaction ID textField
>
>   Accertify Device transaction ID from collector JS/SDK (backward compatibility).
>
> - UBA ID textField
>
>   Accertify UBA ID used to reference behavior data.
>
> - UBA Session ID textField
>
>   The user's Session ID defined by Accertify for the user's web browsing activity.
>
> - Page ID textField
>
>   UBA unique page ID defined from the collector script.
>
> - UBA Events textField
>
>   UBA recent events payload.
>
> - Email Address textField
>
>   Email address associated with the account or event.
>
> - Username textField
>
>   User's username (if applicable).
>
> - Authentication Method dropDown
>
>   How the user authenticated.
>
>   * appAuthenticator
>
>   * appPush
>
>   * FIDO
>
>   * other
>
>   * password
>
>   * magicLink
>
>   * SMS
>
> * default object
>
>   * properties object
>
>     * eventSource string required
>
>       Required. Where or how the event originated.
>
>     * accountID string required
>
>       Required. User's unique identifier you assigned.
>
>     * updateTrigger string required
>
>       Required. Trigger that caused the password to be updated.
>
>     * ipAddress string
>
>       Imperative. User's IP Address you captured.
>
>     * userAgent string
>
>       Imperative. User Agent of the user's browser/OS.
>
>     * devicePayload string
>
>       Imperative. Device payload from Accertify's collector script.
>
>     * deviceTransactionID string
>
>       Imperative. Device transaction ID (legacy).
>
>     * ubaID string
>
>       Imperative. UBA ID.
>
>     * ubaSessionID string
>
>       Imperative. UBA session ID.
>
>     * pageID string
>
>       Imperative. UBA page ID.
>
>     * ubaEvents string
>
>       Imperative. UBA recent events payload.
>
>     * emailAddress string
>
>       Imperative. Email address associated with the account/event.
>
>     * username string
>
>       Imperative. User's username (if applicable).
>
>     * authenticationMethod string
>
>       Imperative. How the user authenticated onto your site.
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * eventID string
>
>   * status boolean
>
>   * messages object
>
>     * warning array
>
>     * error array
>
>     * info array
>
>   * eventDetails object
>
>   * results object