---
title: AuthenticID Connector
description: The AuthenticID connector lets you use AuthenticID for identity verification in your PingOne DaVinci flow.
component: connectors
page_id: connectors::authenticid_connector
canonical_url: https://docs.pingidentity.com/connectors/authenticid_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-authenticid-connector: Configuring the AuthenticID connector
  connector-configuration: Connector configuration
  base-url: Base URL
  rest-api-url: REST API URL
  account-access-key: Account Access Key
  secret-token: Secret Token
  client-certificate: Client Certificate
  client-key: Client Key
  certificate-passphrase: Certificate Passphrase
  ios-sdk-license-key: iOS SDK License Key
  android-sdk-license-key: Android SDK License Key
  using-the-connector-in-a-flow: Using the connector in a flow
  verifying-identities-with-cfair: Verifying identities with CFAir
  verifying-identities-with-cfweb: Verifying identities with CFWeb
  capabilities: Capabilities
  idVerification: Verify ID with CFWeb
  authenticateDocument: Verify Document with CFAir
  matchSelfie: Match Selfie to Document with CFAir
  idVerificationMobile: Verify Identity with Mobile SDK
  webhook: Get Result from CFWeb
---

# AuthenticID Connector

The AuthenticID connector lets you use AuthenticID for identity verification in your PingOne DaVinci flow.

The connector supports the AuthenticID CFAir and CFWeb services.

For CFAir, the connector can upload a previously captured identity document and selfie images to AuthenticID.

For CFWeb, the connector allows you to direct users to a unique verification URL where they will submit their driver license or passport along with a selfie photo. After AuthenticID verifies the user's identity, it sends the results to DaVinci where you can branch your flow accordingly.

To make sure a camera is available to scan the documents and take photos, the user typically completes the verification process on a mobile device, either in a web browser or using a mobile app:

* Mobile web browser

  With this approach, the connector generates a unique verification URL and lets you provide it to the user in a few ways:

  * The connector makes the URL available as a variable in your flow.

    In the **Using the connector in a flow** section below, we use this URL to show a QR code in the web browser, which makes it easy to open the link on the mobile device.

  * The connector sends the URL directly to the customer as an SMS message.

  * The connector sends the URL directly to the customer as an email message.

* Mobile app

  * The connector starts the verification process directly in an Android or iOS app that you built using the AuthenticID mobile SDK.

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* Your AuthenticID application programming interface (API) *(tooltip: \<div class="paragraph">
  \<p>A specification of interactions available for building software to access an application or service.\</p>
  \</div>)* access credentials (provided by an AuthenticID representative)

* Your SMTP email server credentials, if you want to send verification URLs by email

* A Twilio account, if you want to send verification URLs by SMS

### Configuring the AuthenticID connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

To get the following information, speak to an AuthenticID representative.

##### Base URL

The API URL provided by AuthenticID. Change this URL to target the AuthenticID sandbox or production environment.

##### REST API URL

The REST API URL provided by AuthenticID. Change this URL to target the AuthenticID sandbox or production environment.

##### Account Access Key

The account access key provided to you by AuthenticID.

##### Secret Token

The secret token provided to you by AuthenticID.

##### Client Certificate

The client certificate provided to you by AuthenticID.

##### Client Key

The client key provided to you by AuthenticID.

##### Certificate Passphrase

The certificate passphrase, if AuthenticID provided you with one.

##### iOS SDK License Key

The iOS SDK license key provided to you by AuthenticID. This is only required if you built an iOS app with the AuthenticID mobile SDK.

##### Android SDK License Key

The Android SDK license key provided to you by AuthenticID. This is only required if you built an Android app with the AuthenticID mobile SDK.

## Using the connector in a flow

### Verifying identities with CFAir

![A screen capture of the complete CFAir flow.](_images/connector-images/dvc-authenticid-identity-verification-cfair.jpg)

If you're satisfied with your existing document and selfie image capture experience, this flow shows how you can send the resulting images to AuthenticID for identity verification.

Both capabilities allow you to associate the images with an existing AuthenticID transaction ID to build a profile.

Download the [Identity verification with AuthenticID CFAir](https://marketplace.pingone.com/item/identity-verification-with-authenticid-cfair-davinci-flow) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

### Verifying identities with CFWeb

![A screen capture of the complete flow.](_images/connector-images/dvc-authenticid-identity-verification-cfweb.jpg)

In this flow, you use AuthenticID to generate a unique verification URL and show it as a QR code in the user's web browser. When the user opens the QR code link with their mobile device, they're guided through the process of taking photos of their identification card (either a driver license or passport), then instructed to take a selfie photo. After the documents and photos are accepted, the flow continues where it started in the web browser.

This flow uses the **AuthenticID** connector to create a "challenge". This lets you pause the main flow on the QR code while a secondary flow continues the verification process. When the verification process is complete, you use a [Challenge](challenge_connector.html) connector to trigger the main flow to continue. Learn more about this technique,in [Challenge](challenge_connector.html) connector.

1. Download the [AuthenticID Identity verification with CFWeb](https://marketplace.pingone.com/item/authenticid-identity-verification-with-cfweb-davinci-flow) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. (Optional) Customize the document verification QR code prompt:

   ![A screen capture of the default document verification prompt.](_images/connector-images/dvc-authenticid-verification-prompt.png)

   1. Select the **Custom HTML Template** node in the **Wait for the user to complete verification** section.

   2. In the **HTML Template** field, customize the HTML.

   3. Click **Apply**.

3. (Optional) Customize the result page:

   ![A screen capture of the default result page.](_images/connector-images/dvc-authenticid-result-page.png)

   1. Select the **Custom HTML Message** node in the **Show the verification result** section.

   2. In the **Message** field, customize the message.

   3. Click **Apply**.

      |   |                                                                                                                                                                                                                            |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The flow template shows the user the result of the verification process. In a product environment, this is where you should redirect the user to their account page, another step in the registration process, or similar. |

4. Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Verify ID with CFWeb

Verify the authenticity of an identity document with the AuthenticID hosted solution, CFWeb.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - channel dropDown
>   - Phone Number textField
>
>   Phone number to which the link is to be sent for ID Verification. (Required if channel is PHONE)
>
> - Email textField
>
>   Email address to which the link is to be sent for ID Verification. (Required if channel is EMAIL)
>
> - Mail Host textField
>
>   Contains the email server hostname.
>
> - Mail Port textField
>
>   Contains the email server port number.
>
> - Mail Username textField
>
>   Contains the email server login username.
>
> - Mail Password textField
>
>   Contains the email server login password.
>
> - Mail SMTP Auth toggleSwitch
>
>   If true, attempt to authenticate the user using the AUTH command. Defaults to false.
>
> - Mail SMTP Start TLS Enable toggleSwitch
>
>   If true, enables the use of the STARTTLS command.
>
> - Email Subject textField
>
>   Contains the subject line of the email sent to the customer. Please make sure no new lines characters are in this string.
>
> - Email Content textField
>
>   This variable provides the email content that will be sent to your customer. Use '%URL%' in your content template as a placeholder for the verification link. Please make sure no new lines characters are in this string.
>
> - Email From textField
>
>   Contains the email from which the verification email will be sent to the customer.
>
> - Twilio Account String Identifier (SID) textField
>
>   Contains Twilio account accountSid.
>
> - Twilio Authorization Token textField
>
>   Contains Twilio account authToken.
>
> - Twilio From Number textField
>
>   Contains the phone number from which the SMS will be sent.
>
> - Twilio SMS Content textField
>
>   Contains the structure of the SMS message to be sent to the customer. Use '%URL%' in your message as a placeholder for the verification link. Please make sure no new lines characters are in this string.
>
> - * channelResponse dropDownMultiSelect
>   * Request Expiry Time in Minutes textField
>
>   This value dictates the expiry time of the verify request's token. Default: 4320
>
> - Transaction Expiry Time in Minutes textField
>
>   This value dictates the expiry time of the transaction. Default: 60
>
> - Transaction Attempts textField
>
>   This value specifies the number of transaction a user can attempt before the request is marked as failures. Default: 4
>
> - Front Capture Attempt textField
>
>   This value specifies the number of front capture attempts the user is allowed to use to capture a good image, after this threshold the last image is used. Default: 4
>
> - Back Capture Attempt textField
>
>   This value specifies the number of back capture attempts the user is allowed to use to capture a good image, after this threshold the last image is used. Default: 4
>
> - Selfie Capture Attempt textField
>
>   This value specifies the number of selfies capture attempts the user can use to capture a good image, after this threshold the last image is used. Default: 4
>
> - Enable Selfie Capture toggleSwitch
>
>   Setting this value to true lets the application request for a near selfie to be captured. Default: true
>
> - Enable Far Selfie toggleSwitch
>
>   Setting this value to true lets the application request for a far selfie to be captured. Default: true
>
> - Focus Front textField
>
>   Specifies the front images focus threshold, any image which does not have a focus value greater than this value will be rejected by the application. Default: 30
>
> - Focus Back textField
>
>   Specifies the back images focus threshold, any image which does not have a focus value greater than this value will be rejected by the application. Default: 30
>
> - Glare Front textField
>
>   Specifies the front images glare threshold, any image which does not have a glare value less than this value will be rejected by the application. Default: 2.5
>
> - Glare Back textField
>
>   Specifies the front images glare threshold, any image which does not have a glare value less than this value will be rejected by the application. Default: 2.5
>
> - Review Screen Front toggleSwitch
>
>   If this flag is set to true, Front review screen is shown once front image is captured. Default: true
>
> - Review Screen Back toggleSwitch
>
>   If this flag is set to true, Back review screen is shown once back image is captured. Default: true
>
> - Logo (Base64 image) textField
>
>   This value is used to show the logo at the welcome screen. The value in this field should be Base64 encoded image file.
>
> - Home Screen (Base64 image) textField
>
>   This value is used to show the background image in the welcome and consent screen. The value in this field should be a Base64 encoded image file.
>
> - * frontCaptureMode dropDown
>   * Front Overlay Text Manual textField
>
>   This message is shown on top of the front capture screen when the frontCaptureMode is set to Manual
>
>   Default:
>
>   ```none
>   Align ID and tap <br/> to capture.
>   ```
>
> - Front Overlay Text Auto textField
>
>   This message is shown on top of the front capture screen when the frontCaptureMode is set to Auto
>
>   Default:
>
>   ```none
>   Align ID within box and capture
>   ```
>
> - Front Overlay Color textField
>
>   This value is used to color the text shown on the front capture screen. The value should be in CSS3 Hex format.
>
> - Front Enable Face Detection toggleSwitch
>
>   This flag specifies if the face detection should be enabled when the front image is captured.
>
> - Front Set Manual Timeout in Seconds textField
>
>   This value specifies after how many seconds to pass before the capture mode is switched from Auto to Manual
>
> - * backCaptureMode dropDown
>   * Back Overlay Text Manual textField
>
>   This message is shown on top of the back capture screen when the backCaptureMode is set to Manual
>
>   Default:
>
>   ```none
>   Align ID and tap <br/> to capture.
>   ```
>
> - Back Overlay Text Auto textField
>
>   This message is shown on top of the back capture screen when the backCaptureMode is set to Auto
>
>   Default:
>
>   ```none
>   Align ID within box and capture
>   ```
>
> - Back Overlay Color textField
>
>   This value is used to color the text shown on the back capture screen. The value should be in CSS3 Hex format.
>
> - Back is Barcode Detected toggleSwitch
>
>   This flag specifies if the face detection should be enabled when the back image is captured.
>
> - Back Set Manual Timeout in Seconds textField
>
>   This value specifies after how many seconds to pass before the capture mode is switched from Auto to Manual
>
> - * selfieCaptureMode dropDown
>   * Selfie Use Back Camera textField
>
>   This value specifies if the back camera should be used instead of the front facing camera
>
> - Selfie Overlay Text Manual textField
>
>   This message is shown on top of the selfie capture screen when the selfieCaptureMode is set to Manual
>
>   Default:
>
>   ```none
>   Align face and tap button</br> to capture.
>   ```
>
> - Selfie Overlay Text Auto textField
>
>   This message is shown on top of the selfie capture screen when the selfieCaptureMode is set to Auto
>
>   Default:
>
>   ```none
>   Align face and capture
>   ```
>
> - Selfie Overlay Color textField
>
>   This value is used to color the text shown on the selfie capture screen. The value should be in CSS3 Hex format.
>
> - Selfie Enable Face Detection toggleSwitch
>
>   This flag specifies if the face detection should be enabled when the selfie image is captured.
>
> - Selfie Orientation Error Text textField
>
>   This value is used when the mobile device is oriented incorrectly when selfie is being captured. The correct orientation is Portrait.
>
> - Selfie Set Manual Timeout in Seconds textField
>
>   This value specifies after how many seconds to pass before the capture mode is switched from Auto to Manual
>
> - Custom Color textField
>
>   This value is used to color all the buttons in the application. The value should in CSS3 Hex format.
>
> - Retry Count textField
>
>   Number of retries
>
> - Enable Location Detection toggleSwitch
>
>   This value specifies if GPS location should be captured and embedded in the front and back image.
>
> - Show Consent toggleSwitch
>
>   If this value is set to true then the consent screen will be shown.
>
> - Call Post Back Securely toggleSwitch
>
>   If this value is set to true then the results will be returned to the customer using a secure postback call. The postback URL should be passed in the verify request.
>
> - Transaction Expired Message textArea
>
>   Message to display when the transaction has expired
>
>   Default:
>
>   ```none
>   Your verification request has expired. Please contact support to start a new verification request.
>   ```
>
> - Redirect URL textField
>
>   This is the url where the Digital Mobile Application will be redirected once the identity verification is completed
>
> - * authenticIdDocumentType dropDown
>   * Account Code textField
>
>   Your AuthenticID account code.
>
> * default object
>
>   * properties object
>
>     * baseUrl string required
>
>     * clientCertificate string required
>
>     * clientKey string required
>
>     * passphrase string
>
>     * channel string required
>
>     * phone string
>
>     * email string
>
>     * channelResponse array
>
>     * requestExpiryTimeInMin string
>
>     * transactionExpiryTimeInMin string
>
>     * transactionAttempts string
>
>     * frontCaptureAttempt string
>
>     * backCaptureAttempt string
>
>     * selfieCaptureAttempt string
>
>     * enableSelfieCapture boolean
>
>     * enableFarSelfie boolean
>
>     * focusFront string
>
>     * focusBack string
>
>     * glareFront string
>
>     * glareBack string
>
>     * reviewScreenFront boolean
>
>     * reviewScreenBack boolean
>
>     * logo string
>
>     * homeScreen string
>
>     * frontCaptureMode string
>
>     * frontOverlayTextManual string
>
>     * frontOverlayTextAuto string
>
>     * frontOverlayColor string
>
>     * frontEnableFaceDetection boolean
>
>     * frontSetManualTimeout string
>
>     * backCaptureMode string
>
>     * backOverlayTextManual string
>
>     * backOverlayTextAuto string
>
>     * backOverlayColor string
>
>     * backIsBarcodeDetectedEnable boolean
>
>     * backSetManualTimeout string
>
>     * selfieCaptureMode string
>
>     * selfieUseBackCamera string
>
>     * selfieOverlayTextManual string
>
>     * selfieOverlayTextAuto string
>
>     * selfieOverlayColor string
>
>     * selfieEnableFaceDetection boolean
>
>     * selfieOrientationErrorText string
>
>     * selfieSetManualTimeout string
>
>     * mailHost string
>
>     * mailPort number/string
>
>     * mailUsername string
>
>     * mailPassword string
>
>     * mailSmtpAuth boolean
>
>     * mailSmtpStarttlsEnable boolean
>
>     * emailSubject string
>
>     * emailContent string
>
>     * emailFrom string
>
>     * twilioAccountSid string
>
>     * twilioAuthToken string
>
>     * twilioFromNumber string
>
>     * twilioSmsContent string
>
>     * customColor string
>
>     * retryCount string
>
>     * enableLocationDetection boolean
>
>     * showConsent boolean
>
>     * callPostbackSecurely boolean
>
>     * transactionExpiredMessage string
>
>     * redirectURL string
>
>     * authenticIdDocumentType number/string
>
>     * accountCode number/string
>
> - output object
>
>   * challenge string
>
>   * rawResponse object
>
>     * url string
>
>     * requestID string
>
> Output Example
>
> ```json
> {
>   "challenge": "7f83-b0c4-90e0-90b3-11e1",
>   "rawResponse": {
>     "requestID": "a1743e9b-bc46-4b46-9238-f950c14905de",
>     "url": "https://cfweb.amalgam.ascendant.cloud/MWA/index.html?token=c9c11bd1-5cdd-48d9-993a-fa061e050380"
>   }
> }
> ```

### Verify Document with CFAir

Verify the authenticity of an identity document with the AuthenticID API solution, CFAir.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Account Code textField
>
>   Your AuthenticID account code.
>
> - Document Type dropDown required
>
>   The type of identity document.
>
>   * License
>
>   * Passport
>
> - Front Image textField required
>
>   Image of the front side of the identity document, encoded as Base64 data.
>
> - Back Image textField
>
>   Image of the back side of the identity document, encoded as Base64 data.
>
> - Transaction ID textField
>
>   Transaction ID obtained from Authenticate Document response.
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * accountAccessKey string required
>
>     * secretToken string required
>
>     * transactionID string
>
>     * frontImageData string required
>
>     * backImageData string
>
>     * authenticIdDocumentTypeV2 string required
>
>     * accountCode number/string required
>
> - output object
>
>   * rawResponse object
>
>     * systemId string
>
>     * ApiRequestHeaders object
>
>       * DOCUMENTTYPE string
>
>       * HOST string
>
>       * RAW-REQUEST-URI string
>
>       * TRANSFER-ENCODING string
>
>       * USER-AGENT string
>
>       * X-B3-TRACEID string
>
>       * X-REQUEST-ID string
>
>     * TransactionDate string
>
>     * TransactionId string
>
>     * ApiVersion integer
>
>     * AccessKey string
>
>     * MerchantId string
>
>     * LocationCode string
>
>     * DocumentImageAnalysis object
>
>       * Front object
>
>         * ColorSpace string
>
>         * DPI integer
>
>       * Back object
>
>         * ColorSpace string
>
>         * DPI integer
>
>       * Result string
>
>     * DocumentId string
>
>     * DocumentCharacteristics object
>
>       * Classification object
>
>         * state string
>
>         * type string
>
>         * year string
>
>         * country string
>
>         * IssuerCode string
>
>         * IssuerCountry string
>
>         * IssuerContinent string
>
>         * IssuerRegion string
>
>         * DocumentClassName string
>
>       * Authentication object
>
>         * imagery number
>
>       * Pass1 object
>
>         * result\_inlier object
>
>           * angle number
>
>           * country string
>
>           * inliers string
>
>           * state string
>
>           * type string
>
>           * year string
>
>         * rotation integer
>
>       * Pass2 object
>
>         * result\_inlier object
>
>           * angle integer
>
>           * country string
>
>           * inliers string
>
>           * state string
>
>           * type string
>
>           * year string
>
>         * rotation integer
>
>     * DocumentEncoding object
>
>       * Label\_29 string
>
>       * Label\_27 string
>
>       * Label\_28 string
>
>       * GivenName string
>
>       * EyeColor string
>
>       * Version string
>
>       * Label\_21 string
>
>       * Label\_22 string
>
>       * Label\_20 string
>
>       * Label\_25 string
>
>       * Label\_26 string
>
>       * Label\_23 string
>
>       * Label\_24 string
>
>       * Label\_38 string
>
>       * processed\_image\_height string
>
>       * Label\_39 string
>
>       * Label\_32 string
>
>       * Label\_33 string
>
>       * processed\_image\_width string
>
>       * Label\_30 string
>
>       * Label\_31 string
>
>       * Label\_36 string
>
>       * Label\_37 string
>
>       * Label\_34 string
>
>       * BirthDate string
>
>       * Label\_35 string
>
>       * Sex string
>
>       * Height string
>
>       * Label\_18 string
>
>       * Label\_19 string
>
>       * Label\_16 string
>
>       * Label\_17 string
>
>       * Address2 string
>
>       * IssueDate string
>
>       * Address1 string
>
>       * DocumentNumber string
>
>       * Label\_2 string
>
>       * Label\_10 string
>
>       * Label\_7 string
>
>       * Label\_11 string
>
>       * Label\_8 string
>
>       * Label\_9 string
>
>       * Label\_14 string
>
>       * Label\_3 string
>
>       * Surname string
>
>       * Label\_15 string
>
>       * Label\_4 string
>
>       * Label\_12 string
>
>       * Label\_5 string
>
>       * Label\_13 string
>
>       * Label\_6 string
>
>       * FullName string
>
>     * DocumentMaterialAnalysis object
>
>     * DocumentImageIntegrityAnalysis object
>
>       * PaperSplice object
>
>         * Front object
>
>           * Tampered number
>
>       * IDSaturation object
>
>         * Front object
>
>           * Tampered number
>
>       * PrintDetector object
>
>         * Front object
>
>           * Tampered number
>
>           * Natural number
>
>       * Glare object
>
>         * Front object
>
>           * Tampered integer
>
>         * Back object
>
>           * Tampered integer
>
>       * Focus object
>
>         * Front object
>
>           * Tampered integer
>
>       * BiometricTamper object
>
>         * Front object
>
>           * Tampered number
>
>       * PhotoBorderDetector object
>
>         * Front object
>
>           * Tampered integer
>
>       * PaperDetector object
>
>         * Front object
>
>           * Tampered number
>
>       * ScreenPhotoDetector object
>
>         * Front object
>
>           * Tampered integer
>
>         * Back object
>
>           * Tampered number
>
>       * PhotoSplice object
>
>         * Front object
>
>           * Tampered number
>
>       * CredentialDetector object
>
>         * Front object
>
>           * Tampered number
>
>       * PhotoStitch object
>
>         * Front object
>
>           * Tampered number
>
>     * DocumentImages object
>
>       * HeadShot string
>
>     * CatfishNetUsed boolean
>
>     * DocumentFields object
>
>       * Fused object
>
>         * VizNative object
>
>         * 2DBarcode object
>
>         * Custom2DBarcode object
>
>           * error string
>
>           * transactionId string
>
>     * DocumentRiskVectorData object
>
>       * Front object
>
>         * Exif object
>
>         * MobileSDK object
>
>       * Back object
>
>         * Exif object
>
>         * MobileSDK object
>
>     * DocumentRiskConditions object
>
>       * DQL\_Default\_Results object
>
>     * SegmentName string
>
>     * SegmentUiSettings string
>
>     * MatchedSegmentAlgorithms array
>
>       * Array Item Schema string
>
>       * Array Item Schema string
>
>       * Array Item Schema string
>
>       * Array Item Schema string
>
>     * ErrorCodes object
>
>     * ActionCodes object
>
>       * code integer
>
>       * actionMessage string
>
>       * cat string
>
>     * DocumentRiskVectorAnalysis object
>
>       * CaptureTime object
>
>         * Front object
>
>           * Result string
>
>           * Display string
>
>         * Back object
>
>           * Result string
>
>           * Display string
>
>         * FrontAndBack object
>
>           * Result string
>
>           * Display string
>
>       * LocationAnalysis object
>
>         * Front object
>
>           * Result string
>
>           * Display string
>
>         * Back object
>
>           * Result string
>
>           * Display string
>
>         * FrontAndBack object
>
>           * Result string
>
>           * Display string
>
>       * CameraUsed object
>
>         * Front object
>
>           * Result string
>
>           * Display string
>
>         * Back object
>
>           * Result string
>
>           * Display string
>
>       * DeviceOrientation object
>
>         * Front object
>
>           * Result string
>
>           * Display string
>
>         * Back object
>
>           * Result string
>
>           * Display string
>
>       * CaptureMethod object
>
>         * Front object
>
>           * Result string
>
>           * Display string
>
>         * Back object
>
>           * Result string
>
>           * Display string
>
>       * CaptureType object
>
>         * Front object
>
>           * Result string
>
>           * Display string
>
>         * Back object
>
>           * Result string
>
>           * Display string
>
>       * Result string
>
>     * ProcessingTimeInMilliSeconds integer
>
>   * statusCode number
>
>   * headers object

### Match Selfie to Document with CFAir

Match selfie to document with CFAir.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Transaction ID textField
>
>   Transaction ID obtained from Authenticate Document response.
>
> - Account Code textField
>
>   Your AuthenticID account code.
>
> - Selfie Image textField required
>
>   Selfie photo of the user, encoded as Base64 data.
>
> - Use Selfie for Liveness Check toggleSwitch
>
>   When selected, the selfie image is used to fulfill the "liveness" check instead of the regular selfie image.
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * accountAccessKey string required
>
>     * secretToken string required
>
>     * transactionID string required
>
>     * selfieImageData string required
>
>     * livenessSelfie boolean required
>
>     * accountCode number/string required
>
> - output object
>
>   * rawResponse object
>
>     * systemId string
>
>     * TransactionDate string
>
>     * ApiRequestHeaders object
>
>       * CONTENT-LENGTH string
>
>       * HOST string
>
>       * LOCATION string
>
>       * RAW-REQUEST-URI string
>
>       * REMOTE-ADDRESS string
>
>       * TIMEOUT-ACCESS string
>
>       * TLS-SESSION-INFO string
>
>       * USER-AGENT string
>
>       * X-B3-PARENTSPANID string
>
>       * X-B3-SAMPLED string
>
>       * X-B3-SPANID string
>
>       * X-B3-TRACEID string
>
>       * X-ENVOY-ATTEMPT-COUNT string
>
>       * X-ENVOY-EXTERNAL-ADDRESS string
>
>       * X-FORWARDED-CLIENT-CERT string
>
>       * X-FORWARDED-FOR string
>
>       * X-FORWARDED-PROTO string
>
>       * X-REQUEST-ID string
>
>     * TransactionId string
>
>     * ApiVersion integer
>
>     * AccessKey string
>
>     * MerchantId string
>
>     * ProcessingTimeInMilliSeconds integer
>
>     * LivenessSelfie boolean
>
>     * SelfieRiskVectorAnalysis object
>
>       * CaptureTime object
>
>         * Selfie object
>
>           * Result string
>
>           * Display string
>
>       * LocationAnalysis object
>
>         * Selfie object
>
>           * Result string
>
>           * Display string
>
>       * CameraUsed object
>
>         * Selfie object
>
>           * Result string
>
>           * Display string
>
>       * DeviceOrientation object
>
>         * Selfie object
>
>           * Result string
>
>           * Display string
>
>       * CaptureMethod object
>
>         * Selfie object
>
>           * Result string
>
>           * Display string
>
>       * CaptureType object
>
>         * Selfie object
>
>           * ExifData null
>
>           * Result string
>
>           * Display string
>
>       * AuthenticityAnalysis object
>
>         * Selfie object
>
>           * Result string
>
>           * Display string
>
>       * Result string
>
>     * SelfieImageAnalysis object
>
>       * Selfie object
>
>         * ColorSpace string
>
>         * Width integer
>
>         * Height integer
>
>         * NumFaces integer
>
>       * Result string
>
>     * SelfieScores array
>
>       * Array Item Schema object
>
>         * Name string
>
>         * VerificationScore number
>
>     * LivenessSelfieScores array
>
>     * SelfieImageIntegrityAnalysis object
>
>       * Result string
>
>       * PaperSplice object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Natural number
>
>           * Tampered number
>
>       * PrintDetector object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Tampered integer
>
>           * Natural integer
>
>       * Glare object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Tampered number
>
>           * Natural number
>
>       * Focus object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Natural number
>
>           * Tampered number
>
>       * BiometricTamper object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Tampered number
>
>           * Natural number
>
>       * PhotoBorderDetector object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Tampered integer
>
>           * Natural integer
>
>       * NaturalCapture object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Tampered integer
>
>           * Natural integer
>
>       * PhotoSplice object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Tampered number
>
>           * Natural number
>
>       * CredentialDetector object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Tampered integer
>
>           * Natural integer
>
>       * PhotoStitch object
>
>         * Selfie object
>
>           * Threshold integer
>
>           * Result string
>
>           * Tampered number
>
>           * Natural number
>
>     * SelfieRiskVectorData object
>
>       * Selfie object
>
>         * Exif object
>
>           * Width integer
>
>           * Height integer
>
>           * Orientation integer
>
>         * MobileSDK object
>
>     * SelfieDemographicData object
>
>       * HeadShot object
>
>         * leftEyeX integer
>
>         * leftEyeY integer
>
>         * rightEyeX integer
>
>         * rightEyeY integer
>
>         * faceScore number
>
>         * chinX integer
>
>         * chinY integer
>
>         * yaw integer
>
>         * pitch integer
>
>         * roll integer
>
>         * iod integer
>
>         * gender string
>
>         * age integer
>
>         * ethnicity string
>
>         * glasses string
>
>         * spoof integer
>
>         * lips string
>
>       * Selfie object
>
>         * leftEyeX integer
>
>         * leftEyeY integer
>
>         * rightEyeX integer
>
>         * rightEyeY integer
>
>         * faceScore number
>
>         * chinX integer
>
>         * chinY integer
>
>         * yaw integer
>
>         * pitch integer
>
>         * roll integer
>
>         * iod integer
>
>         * gender string
>
>         * age integer
>
>         * ethnicity string
>
>         * glasses string
>
>         * spoof integer
>
>         * lips string
>
>     * SelfieRiskConditions object
>
>       * DQL\_Default\_Results object
>
>         * DQL\_Series\_9000\_Result string
>
>         * DQL\_FRScore1\_Final\_Result\_Reason string
>
>         * DQL\_FRScore1\_Final\_Result string
>
>         * DQL\_Selfie1\_Score\_Result string
>
>         * DQL\_Series\_9200\_Result string
>
>         * DQL\_FRScore\_Final\_Result string
>
>         * DQL\_FarSelfie\_Usable\_Result\_Reason string
>
>         * DQL\_Selfie1\_Usable\_Result\_Reason string
>
>         * DQL\_Selfie1Liveness\_Result string
>
>         * DQL\_FarSelfie\_Liveness\_Result\_Reason null
>
>         * DQL\_FarSelfie\_Liveness\_Result string
>
>         * DQL\_Version string
>
>         * DQL\_Series\_9100\_Result string
>
>         * DQL\_Selfie1\_Score\_Result\_Reason string
>
>         * DQL\_Series\_9500\_Result string
>
>         * DQL\_Headshot\_Usable\_Result string
>
>         * DQL\_Final\_EnrollFace\_Result null
>
>         * DQL\_FarSelfie\_Usable\_Result string
>
>         * DQL\_Headshot\_Usable\_Result\_Reason string
>
>         * DQL\_Final\_EnrollFace\_Which\_Result string
>
>         * DQL\_Series\_9400\_Result string
>
>         * DQL\_Selfie2Liveness\_Result string
>
>         * DQL\_Selfie1\_Usable\_Result string
>
>         * DQL\_Selfie1Liveness\_Result\_Reason string
>
>     * SegmentName string
>
>     * SegmentUiSettings string
>
>     * MatchedSegmentAlgorithms array
>
>     * ErrorCodes object
>
>     * ActionCodes object
>
>       * code integer
>
>       * actionMessage string
>
>       * cat string
>
>     * FRVerifications integer
>
>   * statusCode number
>
>   * headers object

### Verify Identity with Mobile SDK

Verify the authenticity of an identity document with an app powered by the AuthenticID mobile SDK.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - title textField
>
>   Default:
>
>   ```none
>   ID Verification
>   ```
>
> - * bodyHeaderText textField
>   * authenticIdDocumentType dropDown
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * accountAccessKey string required
>
>     * secretToken string required
>
>     * authenticIdDocumentType number/string
>
> - output object
>
>   * challenge string
>
>   * userReference string
>
> Output Example
>
> ```json
> {
>   "challenge": "7f83-b0c4-90e0-90b3-11e1",
>   "userReference": " a1743e9b-bc46-4b46-9238-f950c14905de"
> }
> ```

### Get Result from CFWeb

Get the result of an ID verification check from CFWeb.

> **Collapse: Show details**
>
> * Output Schema
>
> - output object
>
>   * challenge string
>
>   * rawResponse object
>
>     * requestID string
>
>     * requestStatus string
>
>     * uid string
>
>     * transactions array
>
> Output Example
>
> ```json
> {
>   "challenge": "80a6e8b8-5522-416f-9f97-473e4c3c5657",
>   "rawResponse": {
>     "requestID": "95cd0d82-5e91-4b07-8006-537b0be89b57",
>     "requestStatus": "SUCCESS",
>     "uid": "001a33d6-ca1a-4fe6-a66e-3eff243f8cc8",
>     "transactions": [
>       {
>         "transactionID": "Zt6ae_scvDvVO576",
>         "transactionStatus": "COMPLETED",
>         "transactionSubStatus": "COMPLETED",
>         "executedDeletionRule": false,
>         "sequenceNumber": 0,
>         "statusColor": "color:#FFFFFF;background:#008000;",
>         "segmentName": "Verified",
>         "transactionDetails": {
>           "documentType": "11",
>           "homeScreen": " ",
>           "focusFront": "30.0",
>           "reviewScreenFront": "true",
>           "reviewScreenBack": "true",
>           "enableSelfieCapture": "true",
>           "enableFarSelfie": "true",
>           "transactionAttempts": "4",
>           "requestExpiryTimeInMin": "4320",
>           "transactionExpiryTimeInMin": "60",
>           "enableLocationDetection": "true",
>           "showConsent": "true",
>           "callPostbackSecurely": "false",
>           "frontEnableFaceDetection": "true",
>           "selfieEnableFaceDetection": "true",
>           "mailSmtpAuth": "true",
>           "mailSmtpStarttlsEnable": "true"
>         },
>         "actionCodes": {
>           "code": 99,
>           "actionMessage": "Please click to Continue.",
>           "cat": "Environment"
>         },
>         "pii": {
>           "Address": "",
>           "AddressCity": "",
>           "AddressPostalCode": "",
>           "AddressLine1": "",
>           "AddressLine2": "",
>           "AddressLine3": "",
>           "AddressState": "",
>           "BirthDate": "21/May/1987",
>           "BirthPlace": "Cape Town",
>           "DocumentNumber": "234230432",
>           "ExpirationDate": "09/Jun/2028",
>           "EyeColor": "",
>           "FullName": "John Doe",
>           "GivenName": "John",
>           "FirstName": "Doe",
>           "MiddleName": "",
>           "Height": "",
>           "IssueDate": "10/Jun/2018",
>           "LicenseClass": "",
>           "LicenseRestrictions": "",
>           "Sex": "M",
>           "Surname": "Doe",
>           "Weight": "",
>           "ClassName": "Passport",
>           "DocumentName": "Passport",
>           "IssuerName": "South Africa",
>           "IssuerCode": "SAF",
>           "DocumentIssueDate": "2015",
>           "SystemDate": "26/Feb/2021"
>         },
>         "passIDEThreshold": [
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_General_Data_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Generalized Data Analysis"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_SubmissionDocumentType_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Wrong ID Type Submitted"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Allowable_Doc_Type_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "On Approved List"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "EXISTS",
>             "FailThreshold": "NOTEXISTS",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "",
>             "Name": "ID - System Processing Failure"
>           },
>           {
>             "Category": "DATE ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Min_Age_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Minimum Age Requirement"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Materials_Replica_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Materials Analysis"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Selfie1Liveness_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Liveness Assessment 1"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Selfie1_Score_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Selfie -  Facial Recognition Matching"
>           },
>           {
>             "Category": "FRAUD SHIELD",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Data_Source1_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Data Matching"
>           },
>           {
>             "Category": "DATE ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_ID_About_To_Expire_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Expiring Soon"
>           },
>           {
>             "Category": "MINIMUM PII EXTRACTED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Final_Minimum_PII_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Final PII - minimum extracted"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_HeadshotExtracted_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "ID Headshot Extracted"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Front_Color_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Color Analysis"
>           },
>           {
>             "Category": "DATE ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_ID_Expired_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Already Expired"
>           },
>           {
>             "Category": "SELFIE AND LIVENESS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FarSelfie_Liveness_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Liveness Assessment 2"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Selfie1_Usable_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Selfie Usable"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Pattern_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": "Passed",
>             "Name": "Visual Pattern Assessment"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": ">=250",
>             "FailThreshold": "<250",
>             "CatFishReferenceField": [
>               "DocumentImageAnalysis",
>               "Front",
>               "DPI"
>             ],
>             "ScoreSegmentResult": "PASS",
>             "IDESystemScore": 295,
>             "Name": "Minimum DPI Requirements"
>           }
>         ],
>         "failIDEThreshold": [],
>         "uncertainIDEThreshold": [
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FTB_ExpirationDate_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Expiration Date - Front-To-Back Analysis"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Street_Front_To_Back_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Street Address - Front to Back"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_City_Front_To_Back_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "City - Front to Back"
>           },
>           {
>             "Category": "SELFIE AND LIVENESS",
>             "PassThreshold": "EXISTS",
>             "FailThreshold": "NOTEXISTS",
>             "CatFishReferenceField": [
>               "SelfieScores",
>               "VerificationScore"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Selfie Received"
>           },
>           {
>             "Category": "SELFIE AND LIVENESS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_PassiveSelfie_LIFO_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Passive Selfie - LIFO"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_LastName_SpecialCharacter_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Last Name - Special Characters"
>           },
>           {
>             "Category": "MINIMUM PII EXTRACTED",
>             "PassThreshold": "<90",
>             "FailThreshold": ">=98",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "BiometricTamper",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Biometric Tamper (Replaced)"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "<90",
>             "FailThreshold": ">99",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "Focus",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Focus - Front (Info Only)"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": ">=75",
>             "FailThreshold": "<75",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "BiographicSplice",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Biographic Splice"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Useful_Output_Result2"
>             ],
>             "ScoreSegmentResult": "INFO ONLY",
>             "IDESystemScore": "Info Only",
>             "Name": "Information - Address"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_ID_Cropping_Exception_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Cropping and Capture Issues"
>           },
>           {
>             "Category": "SELFIE AND LIVENESS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Overall_Liveness_Conclusion_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Liveness 1 and 2 Fused Conclusion"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": ">=250",
>             "FailThreshold": "<250",
>             "CatFishReferenceField": [
>               "DocumentImageAnalysis",
>               "Back",
>               "DPI"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "DPI Resolution - Back"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "CaptureTime",
>               "Back",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Capture Time - Back"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Headshot_Modification_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Headshot Integrity Analysis"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_State_SpecialCharacter_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "State - Special Characters"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Useful_Output_Result1"
>             ],
>             "ScoreSegmentResult": "INFO ONLY",
>             "IDESystemScore": "Info Only",
>             "Name": "Information - Name and Dates"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FR_LIFO_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Fused FR - LIFO"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FR_BestCase_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Fused FR - Best Case"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_PostalCode_SpecialCharacter_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Postal Code - Special Characters"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "DeviceOrientation",
>               "Front",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Device Orientation - Front"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "<100",
>             "FailThreshold": ">100",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "TextBlurOcclusion",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Blur or Occlusion"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskVectorAnalysis",
>               "DeviceOrientation",
>               "Selfie",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Orientation Analysis - Selfie"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Speciality_Document_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Speciality Document Analysis"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Allowable_Doc_Type_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Allowable Document Type"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_GPS_Low_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "GPS Risk - Low"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_UsableSelfie_Fused_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Headshot Usable"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "CaptureTime",
>               "Front",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Capture Time - Front"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_IdentityDocumentType_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Unused"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FTB_BirthDate_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Birth Date - Front-To-Back Analysis"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskVectorAnalysis",
>               "CaptureTime",
>               "Selfie",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Capture Time - Selfie"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_GPS_Restricted_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "GPS Risk - Restricted"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "CaptureType",
>               "Front",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Capture Type - Front"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Compromised_Document_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Compromised Document Analysis"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_DocumentNumber_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Document Number Integrity Analysis"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskVectorAnalysis",
>               "CameraUsed",
>               "Selfie",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Camera Used - Selfie"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Gender_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Missing Fullname Data"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "<95",
>             "FailThreshold": ">99",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "Glare",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Glare - Front (Info Only)"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "<=99",
>             "FailThreshold": ">100",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "PaperDetector",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Advanced Paper Detection"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Biographic_Fused_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Biographic Tamper Conclusion"
>           },
>           {
>             "Category": "FRAUD SHIELD",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Face_Source1_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Headshot Matching"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "<50",
>             "FailThreshold": ">50",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "TinyOcclusion",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Tiny Occlusion"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "<100",
>             "FailThreshold": ">100",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "MachineReadable",
>               "Back",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Machine Readable"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FR_Avg_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Fused FR - Average Score"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FTB_FullName_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "FullName - Front-To-Back Analysis"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Image_EXIF_Issue_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Manipulated During Transmission"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_PostalCode_Front_To_Back_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Postal Code - Front to Back"
>           },
>           {
>             "Category": "FRAUD SHIELD",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Velocity_Source1_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Velocity Analysis"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_State_Front_To_Back_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "State - Front to Back"
>           },
>           {
>             "Category": "MINIMUM PII EXTRACTED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_2D_Minimum_PII_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Barcode Data - minimum extracted"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "EXISTS",
>             "FailThreshold": "NOTEXISTS",
>             "CatFishReferenceField": [
>               "SelfieScores"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "ID Photo Usable"
>           },
>           {
>             "Category": "DATE ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_ExpirationDate_Info_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "ID Expiration"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "Personal_Info_Analysis"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Personal Information Analysis"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Allowable_GPS_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Allowable GPS Location"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Visual_Image_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Visual Image Analysis"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_CheckDigit_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Check Digit Assessment"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FTB_DocumentNumber_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Document Number - Front-To-Back Analysis"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "DeviceOrientation",
>               "Back",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Device Orientation - Back"
>           },
>           {
>             "Category": "MINIMUM PII EXTRACTED",
>             "PassThreshold": "<90",
>             "FailThreshold": ">=100",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "PhotoSplice",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Biometric Splice (Replaced)"
>           },
>           {
>             "Category": "MINIMUM PII EXTRACTED",
>             "PassThreshold": "<95",
>             "FailThreshold": ">100",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "PhotoStitch",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Photo Stitch (Replaced)"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Allowable_State_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Allowable State"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_LastName_Front_To_Back_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Last Name - Front to Back"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_MiddleName_Front_To_Back_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Middle Name - Front to Back"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Overall_FR_Conclusion_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "FR Conclusion"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Dates_Validity_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Are the ID Dates Valid"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "<=30",
>             "FailThreshold": ">40",
>             "CatFishReferenceField": [
>               "SelfieImageIntegrityAnalysis",
>               "PhotoBorderDetector",
>               "Selfie",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Photo Integrity - Selfie"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "CaptureType",
>               "Back",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Capture Type - Back"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "<=30",
>             "FailThreshold": ">40",
>             "CatFishReferenceField": [
>               "SelfieImageIntegrityAnalysis",
>               "CredentialDetector",
>               "Selfie",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Credential Integrity - Selfie"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Back_Color_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "ColorSpace Analysis - Back"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": ">=40",
>             "FailThreshold": "<30",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FRScore_Final_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Facial Recognition #1"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": ">=40",
>             "FailThreshold": "<=39",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FR_Score2_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Facial Recognition #2"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "<=94",
>             "FailThreshold": ">100",
>             "CatFishReferenceField": [
>               "DocumentMaterialAnalysis",
>               "PolyCarbonate",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Advanced Polycarbonate Materials Detection"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Doc_Classified_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Document Classified"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskVectorAnalysis",
>               "AuthenticityAnalysis",
>               "Selfie",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Authenticity Capture - Selfie"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_2D_Usable_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Barcode Integrity"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": ">=40",
>             "FailThreshold": "<=39",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FR_Score3_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Facial Recognition #3"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Type_Allowed_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "DL Type Allowed"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskVectorAnalysis",
>               "CaptureType",
>               "Selfie",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Capture Type - Selfie"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "LocationAnalysis",
>               "FrontAndBack",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Location Analysis - Front And Back"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_GPS_Med_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "GPS Risk - Med"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Environment_Impact_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Environment Condition Analysis"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FTB_Address_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Full Address  - Front-To-Back Analysis"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FirstName_SpecialCharacter_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "First Name - Special Characters"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_BirthDate_Info_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Birth Date Integrity"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "<99",
>             "FailThreshold": ">=99",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "ScreenPhotoDetector",
>               "Back",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Screen Photo Detector - Back"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "<100",
>             "FailThreshold": ">100",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "TinyText",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Tiny Text"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Temporary_PaperID_Overide_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Temporary DMV ID Submission"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Useful_Output_Result3"
>             ],
>             "ScoreSegmentResult": "INFO ONLY",
>             "IDESystemScore": "Info Only",
>             "Name": "Information - Classification and Scores"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Layout_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Layout Analysis"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FTB_IssueDate_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Issue Date - Front-To-Back Analysis"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Customer_Declined_ID_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Customer Declined ID Verification"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "<90",
>             "FailThreshold": ">99",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "Focus",
>               "Back",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Focus - Back (Info Only)"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_IssueDate_Info_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Issue Date Integrity"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "CaptureTime",
>               "FrontAndBack",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Capture Time - Front and Back"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "CameraUsed",
>               "Front",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Camera Used - Front"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_GPS_High_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "GPS Risk - High"
>           },
>           {
>             "Category": "MINIMUM PII EXTRACTED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_VIZ_Minimum_PII_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "OCR - minimum extracted"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Overall_ID_Conclusion_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "ID Usable Image Conclusion"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Overall_IDAllowable_Conclusion_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Allowable ID Conclusion"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_City_SpecialCharacter_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "City - Special Characters"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "<99",
>             "FailThreshold": ">=99",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "DigitalReproduction",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Digital Reproduction (Replaced)"
>           },
>           {
>             "Category": "MINIMUM PII EXTRACTED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_MRZ_Minimum_PII_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "MRZ Data - minimum extracted"
>           },
>           {
>             "Category": "ID IMAGE USABLE",
>             "PassThreshold": "<95",
>             "FailThreshold": ">99",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "Glare",
>               "Back",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Glare - Back (Info Only)"
>           },
>           {
>             "Category": "FRAUD SHIELD",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Face_Source2_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "3rd Party - Headshot Matching"
>           },
>           {
>             "Category": "ID INTEGRITY ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Structural_Image_Assessment_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Digital Reproduction Assessment"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "<100",
>             "FailThreshold": ">=100",
>             "CatFishReferenceField": [
>               "DocumentImageIntegrityAnalysis",
>               "ScreenPhotoDetector",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Screen Photo Detector - Front"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": ">50",
>             "FailThreshold": "<=50",
>             "CatFishReferenceField": [
>               "DocumentMaterialAnalysis",
>               "IDSaturation",
>               "Front",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Paper Analysis"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "SelfieRiskConditions",
>               "DQL_Default_Results",
>               "DQL_FR_WorstCase_Result_Reason"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Fused FR - Worst Case"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_DOBSymbol_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "HKID DOB Symbol Analysis"
>           },
>           {
>             "Category": "USEFUL INFORMATION",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Useful_Output_Result4"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Information - MRZ"
>           },
>           {
>             "Category": "FRAUD SHIELD",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_Data_Source2_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "3rd Party - Data Matching"
>           },
>           {
>             "Category": "ALLOWABLE ID",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_GPS_Usable_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "GPS Is Usable ( Usable GPS )"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_SpecialCharacter_Analysis_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Potentially Incomplete Fullname"
>           },
>           {
>             "Category": "UNUSED",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskVectorAnalysis",
>               "CameraUsed",
>               "Back",
>               "Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Camera Used - Back"
>           },
>           {
>             "Category": "PII DATA ANALYSIS",
>             "PassThreshold": "Passed",
>             "FailThreshold": "Failed",
>             "CatFishReferenceField": [
>               "DocumentRiskConditions",
>               "DQL_Default_Results",
>               "DQL_ExpirationDate_Info_Result"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Expiration Date Integrity"
>           },
>           {
>             "Category": "FACIAL RECOGNITION",
>             "PassThreshold": "<=30",
>             "FailThreshold": ">40",
>             "CatFishReferenceField": [
>               "SelfieImageIntegrityAnalysis",
>               "NaturalCapture",
>               "Selfie",
>               "Tampered"
>             ],
>             "ScoreSegmentResult": "N/A",
>             "IDESystemScore": "Disabled",
>             "Name": "Natural Capture - Selfie"
>           }
>         ]
>       }
>     ]
>   }
> }
> ```
