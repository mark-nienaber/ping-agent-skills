---
title: Accertify Connector
description: Configure the Accertify connector in PingOne DaVinci to send identity events to the Accertify fraud detection platform and receive risk scores
component: connectors
page_id: connectors::accertify_connector
canonical_url: https://docs.pingidentity.com/connectors/accertify_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-09T00:00:00Z
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

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

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

[Add the connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html) in PingOne DaVinci, then configure it as follows.

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

4. In the **Script** field, replace DATA_COLLECTOR_URL with the collector script URL for your Accertify environment, then add the following:

   ```javascript
   // Configuration
   const DATA_COLLECTOR_URL = "YOUR_COLLECTOR_SCRIPT_URL";
   const MAX_UBA_EVENTS_SIZE = 10; // Maximum UBA payload size: 10 KB (10,000 characters)

   // Load Accertify collector script
   const script = document.createElement("script");
   script.type = "text/javascript";
   script.src = DATA_COLLECTOR_URL;
   script.id = "bcn";
   script.async = true;
   script.setAttribute("dvct", "500");
   script.setAttribute("dvc", "a");

   script.onload = () => {
       window._bcn?.dvc?.setSubmissionCallback?.(populateDeviceData);
   };

   document.head.appendChild(script);

   // Populate device attributes
   function populateDeviceData() {
       setFieldValue("devTID", window._bcn?.dvc?.getTID?.());
   }

   // Flush and populate UBA fields when the button is clicked
   document.getElementById("btnSubmit")?.addEventListener("click", () => {
       window._bcn?.flush?.();

       setFieldValue("ubaId", window._bcn?.getToken?.());
       setFieldValue("ubaSessionId", window._bcn?.getUbaSessionId?.());
       setFieldValue("pageId", window._bcn?.getPageId?.());
       setFieldValue("ubaEvents", window._bcn?.getEvents?.(MAX_UBA_EVENTS_SIZE));
   });

   // Helper function
   function setFieldValue(fieldId, value) {
       const field = document.getElementById(fieldId);

       if (field) {
           field.value = value || "";
       }
   }
   ```

5. In the **Output Fields List**, add each of the following hidden input field names into the **Property Name** field, then click **Apply**:

   * devTID

   * ubaSessionId

   * ubaId

   * pageId

   * ubaEvents

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
> - Brand textField
>
>   The brand submitting the event. For clients with multiple brands under one corporate entity. Maximum field length = 50 characters.
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
> - Failure Code dropDown
>
>   Login Event failure code.
>
>   * Account Doesn't Exist
>
>   * Account Locked
>
>   * Other
>
>   * Password Incorrect
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
>     * brand string
>
>       The brand submitting the event. For clients with multiple brands under one corporate entity.
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
>       Login Event failure code (accountDoesntExist / accountLocked / other / passwordIncorrect).
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
> - Brand textField
>
>   The brand submitting the event. For clients with multiple brands under one corporate entity. Maximum field length = 50 characters.
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
>   * App Authenticator
>
>   * App Push
>
>   * Captcha
>
>   * Email
>
>   * FIDO
>
>   * KB Answers
>
>   * Magic Link
>
>   * Other
>
>   * Phone Call
>
>   * Security Questions
>
>   * SMS
>
> - Verification Status dropDown
>
>   Status of the verification (mapped to failureCode).
>
>   * Abandoned
>
>   * Expired
>
>   * Fail
>
>   * Success
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
>   * Account Create
>
>   * Account Update
>
>   * Gift Card Balance
>
>   * Inventory Hold
>
>   * Listing Create
>
>   * Listing Update
>
>   * Login
>
>   * Logout
>
>   * Password Forgot
>
>   * Password Update
>
>   * Payment
>
>   * Refund
>
>   * Transfer
>
>   * Username Forgot
>
> - Update Event Recommendation Detail textField
>
>   The recommendationDetail returned by Accertify for the original event.
>
> - Failure Code dropDown
>
>   Verification Event failure code.
>
>   * Abandoned
>
>   * Expired
>
>   * Fail
>
>   * New Code Within Expiry
>
>   * Other
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
>     * brand string
>
>       The brand submitting the event. For clients with multiple brands under one corporate entity.
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
> - Brand textField
>
>   The brand submitting the event. For clients with multiple brands under one corporate entity. Maximum field length = 50 characters.
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
>   * Account Exists
>
>   * Export Compliance
>
>   * Unsupported Location
>
>   * Other
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
>     * brand string
>
>       The brand submitting the event. For clients with multiple brands under one corporate entity.
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
> - Brand textField
>
>   The brand submitting the event. For clients with multiple brands under one corporate entity. Maximum field length = 50 characters.
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
>     * brand string
>
>       The brand submitting the event. For clients with multiple brands under one corporate entity.
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
> - Brand textField
>
>   The brand submitting the event. For clients with multiple brands under one corporate entity. Maximum field length = 50 characters.
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
> - Failure Code dropDown
>
>   Password Forgot Event failure code.
>
>   * Account Doesn't Exist
>
>   * Other
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
>     * brand string
>
>       The brand submitting the event. For clients with multiple brands under one corporate entity.
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
>     * passwordForgotFailureCode string
>
>       Password Forgot Event failure code (accountDoesntExist / other).
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
> - Brand textField
>
>   The brand submitting the event. For clients with multiple brands under one corporate entity. Maximum field length = 50 characters.
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
>     * brand string
>
>       Optional. The brand submitting the event. For clients with multiple brands under one corporate entity.
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