---
title: PingID Connector
description: Configure the PingID connector in PingOne DaVinci to add MFA authentication and device enrollment flows to your PingOne environment
component: connectors
page_id: connectors::pid_connector
canonical_url: https://docs.pingidentity.com/connectors/pid_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-pingid: Setting up PingID
  setting-up-the-connector: Setting up the connector
  connector-settings: Connector settings
  environment-id: Environment ID
  client-id: Client ID
  client-secret: Client Secret
  region: Region
  using-the-connector-in-a-flow: Using the connector in a flow
  enrolling-a-device: Enrolling a device
  authenticating-users: Authenticating users
  pingid-flow-templates: PingID flow templates
  connector_limitations: PingID connector limitations
  pingid-connector-limitations: PingID Connector limitations
  pingid-policy-related-limitations: PingID policy-related limitations
  pingid-legacy-connector: PingID Legacy Connector
  setup-2: Setup
  resources-2: Resources
  setting-up-the-connector-2: Setting up the connector
  using-the-connector-in-a-flow-2: Using the connector in a flow
  mfa-flows: MFA flows
  mfa-in-passwordless-flows: MFA in passwordless flows
  capabilities: Capabilities
  initializeMfa: Initialize MFA
  initializePasswordlessAuthentication: Initialize Passwordless Authentication
  finalizePasswordlessAuthentication: Finalize Passwordless Authentication
  troubleshooting: Troubleshooting
---

# PingID Connector

PingID is a cloud-based multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* service that protects an organization's network, applications, and data resources while providing secure and seamless experiences for your customers and users.

The PingID connector supports the use of:

* Customer-friendly authentication flows to increase security without adding unnecessary friction to the end user experience.

* User enrollment flows:

  * Automatically: Allow customers to automatically enroll an authentication method for users during the authentication process.

  * One-time device authentication: Include device details within an authentication request. Enables a user to authenticate for one session only, without pairing the device.

## Setup

### Resources

* PingOne documentation:

  * [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html)

  * [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)

* [PingID documentation](https://docs.pingidentity.com/pingid/pid_landing_page.html)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A PingOne license ([Try PingOne for free](https://www.pingidentity.com/en/try-ping.html))

* A PingID license.

* A PingOne environment with a configured Worker app.

* A PingID tenant linked to the PingOne environment.

### Setting up PingID

You can find instructions on how to set up PingID in the [PingID documentation](https://docs.pingidentity.com/pingid/pid_landing_page.html).

### Setting up the connector

In PingOne DaVinci, add a **PingID** connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector settings

##### Environment ID

Your PingOne Environment ID. In PingOne, go to **Settings > Environment Properties**.

##### Client ID

The Client ID for your PingOne Worker application. In PingOne, go to your application **Applications > Applications > Configuration**.

##### Client Secret

The Client Secret for your PingOne Worker application. In PingOne, go to your application **Applications > Applications > Configuration**.

##### Region

Your PingOne environment region. In PingOne, go to **Settings > Environment Properties**.

## Using the connector in a flow

### Enrolling a device

To seamlessly add MFA for your users and increase MFA adoption, use the PingID connector. You can include device enrollment as part of user registration, or as a just-in-time (JIT) registration within an authentication flow.

The user can select an authentication method for MFA from a list of methods defined by the PingID configuration. This list can include traditional methods, such as email and SMS, and more secure and frictionless methods, such as FIDO2 biometrics and PingID mobile app. Learn more in the [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) guide.

### Authenticating users

Use the PingID connector to increase security by adding an authentication factor that requires the user to prove their identity using a trusted device.

Learn more in the [Creating an authentication flow](https://docs.pingidentity.com/davinci/use_cases/davinci_use_cases_creating_an_authentication_flow.html) guide.

### PingID flow templates

Ping Identity provides out-of-the-box PingOne DaVinci subflows that you can add to a main flow to register authentication devices and to use those devices to authenticate with PingID.

The following PingID flows are available:

* [PingID Device Registration Subflow](https://marketplace.pingone.com/item/pingid-device-registration-subflow)

  Use this subflow to register a new authentication method for use with PingID.

  |   |                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------- |
  |   | The variable `pingIdUserId` represents the ID attribute from PingOne and must be provided when triggering the flow. |

* [PingID Authentication Subflow](https://marketplace.pingone.com/item/pingid-authentication-subflow)

  Use this subflow to add PingID as a secondary authentication factor to a main flow, as part of an authentication process.

  * Customize PingID authentication sub-flow variables.

  Click the **Variables** node to customize any of the following options:

  * `AdminMessage`: The administrative message you want to display during authentication.

  * `SMSBackup`: Use the user's mobile number as a backup authentication method, so they can receive a one-time passcode by SMS, if the user forgets their registered authentication device.

  * `phoneBackup`: Use the user's mobile number as a backup authentication method, to receive a one-time passcode by voice message, if the user forgets their registered authentication device.

  * `emailBackup`: Use the user's email address as a backup authentication method, to receive a one-time passcode by email, if the user forgets their registered authentication device.

  * `useCode`: When set to `true`, the user can click a **Use Code** button to enter an OTP, rather than waiting for a push notification to arrive.

  * `OTP Fallback`: When set to `true`, user's can authenticate with a one-time passcode in the event that the PingID server cannot reach their device, or the push response cannot be completed.

    * Define a list of mandatory authentication devices

      You can define a list of mandatory authentication methods. If defined, users are forced to register all of the required authentication methods in order to access their resources.

      1. In the relevant PingID authentication subflow, click the **Flow Settings** node.

      2. In the **Variable Name** field, select **mandatoryAuthenticationMethods**, and then enter the authentication methods that the user must register with their account. Valid authentication methods include:

         * `PINGID_DESKTOP`

         * `PINGID_MOBILE`

         * `SMS`

         * `VOICE`

         * `EMAIL`

         * `TOTP`

         * `SECURITY_KEY`

         * `PLATFORM`

         * `YUBIKEY`

         * `OATH_TOKEN`

         |   |                                                                                                                                                                                                                    |
         | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
         |   | This field is empty by default. Authentication methods must be entered in upper case, with a space between each entry. If no authentication method is defined, the user is not required to pair a specific device. |

         Example:

         ```
         SMS VOICE EMAIL
         ```

         The next time the user attempts to authenticate, even if they have one of the mandatory methods paired with their account, they are forced to register all of the authentication methods specified in the **mandatoryAuthenticationMethods** list, before they can access their resources.

         ![Mandatory Devices information window, listing all of the devices that the user must pair in order to access their resources. Devices that are already paired with their account display a green checkmark and the word Paired next to the entry](_images/connector-images/dvc-pid-mandatory-devices-window.png)

         |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
         | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | * This flow requires the PingID - registration welcome page flow. The variable `pingIDUserId` must be provided when triggering the flow.

         * The following PingID Connector variables override the equivalent values in the PingID admin console **Configuration** tab:PingID PingIDconnector variable	PingID PingIDadmin console location&#xA;&#xA;SMSBackup, phoneBackup, emailBackup&#xA;&#xA;&#x9;&#xA;&#xA;Alternate Authentication Methods, Backup Authentication (SMS, Voice, or Email checkbox).&#xA;&#xA;&#xA;&#xA;&#xA;OTP Fallback&#xA;&#xA;&#x9;&#xA;&#xA;Mobile App Authentication, One-time Passcode Fallback&#xA;&#xA;&#xA;&#xA;&#xA;useCode&#xA;&#xA;&#x9;&#xA;&#xA;Mobile App Authentication, Direct Passcode Usage |

         |   |                                                                                                       |
         | - | ----------------------------------------------------------------------------------------------------- |
         |   | It is recommended that you review the [PingID connector limitations](#connector_limitations) section. |

## PingID connector limitations

This section describes the known limitations relating to the PingID Connector, and evaluation of PingID policy.

### PingID Connector limitations

* The PingID Devices page is not available when using the PingID Authentication sub-flow. The **Settings** button is therefore not displayed on the **Authentication** screen.

* The PingID connector only support the English language. Localization is not currently supported.

### PingID policy-related limitations

* Backup authentication: If a backup authentication configuration is defined in the PingID authentication sub-flow, it overrides any backup configuration defined in a PingID policy.

* Authentication success message: When authenticating successfully, the Authentication Successful screen appears by default, even if the **Show Approved Authentication** check box is not selected in PingID policy. This behavior can only be modified by editing the flow.

* PingID policy rule evaluation: The Evaluate Policy capability does not enforce the following policy rules:

  * Limit push notifications rule

  * Mobile OS version rule

  * Recent authentication from office rule

  * Authentication from company network rule: authenticating device in company offices section

  * Recent authentication from company network rule: authenticating device in company offices section

* IPv6 address support: If you only have an IPv6 address configured on your local machine, PingID policy is not evaluated.

* PingID policy log entries: Log entries do not support multiple users authenticating from the same browser. Log entries for transaction details such as IP address, transaction time, and geolocation are overwritten by the last user that authenticates.

* If you want to disable the OTP fallback or Direct passcode Usage (**Use Code** button) features, you must disable the relevant feature in the flow settings node in PingOne DaVinci, and the Admin portal.

## PingID Legacy Connector

You can use the PingID connector to add MFA (multi-factor authentication) to flows, including passwordless login flows.

PingID is a cloud-based authentication service that allows your users to carry out MFA (multi-factor authentication) using a variety of methods, including the PingID mobile app, security keys, and biometrics.

### Setup

#### Resources

* PingID documentation:

  * [Overview of PingID authentication types](https://docs.pingidentity.com/pingid/introduction_to_pingid/pid_overview_of_authentication_types.html)

  * [PingID Integrations](https://docs.pingidentity.com/pingid/pingid_integrations/pid_integrations.html)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

#### Setting up the connector

In PingOne DaVinci, add a **PingID** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

After creating the connector, configure it by going to its **General** tab and pasting in the content of the PingID properties file that you downloaded.

![PingID connector configuration](_images/connector-images/dvc-pid-connector-configuration.png)

### Using the connector in a flow

#### MFA flows

You can find examples of using the PingID connector in basic MFA flows, in the following templates in the [Flow Library](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html):

* PingID - Basic MFA flow (username/password + MFA)

* PingID - MFA flow + Risk (username/password + risk evaluation, MFA according to risk score generated for user)

In flows of this type, a connector using the Initialize MFA capability should be placed in the flow at the point where you want an MFA challenge to be issued, for example, after the user has entered their password.

#### MFA in passwordless flows

You can find examples of using the PingID connector to combine MFA with passwordless login in the following templates in the [Flow Library](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html):

* PingID - FIDO2 Passwordless (FIDO2 username, no password required)

* PingID - FIDO2 Passwordless + Risk (FIDO2 username, no password + risk evaluation, action based on risk score generated for user)

In passwordless login flows, two PingID connectors should be added to the flow:

* A connector using the Initialize Passwordless Authentication capability

* Later in the flow, a second connector using the Finalize Passwordless Authentication capability and using as input the *passwordlessContext* that was returned by the initialize step. The username must also be provided as input.

### Capabilities

#### Initialize MFA

Multi-Factor Authentication and on-the-fly registration.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Username textField
>
>   The username for the user in PingOne.
>
> - First Name textField
>
>   User's first name.
>
> - Last Name textField
>
>   User's last name.
>
> - User Groups textField
>
>   The groups to which the user belongs. Used for applying PingID policies that have been defined.
>
> - Mobile Number textField
>
>   User's mobile phone number.
>
> - Landline Number textField
>
>   User's landline number.
>
> - Application Name textField
>
>   The name of the application the user is trying to access.
>
> - Application ID textField
>
>   The ID of the application the user is trying to access. Used for applying PingID policies that have been defined.
>
> - Application Icon (URL) textField
>
>   The URL of the icon that is used for the application the user is trying to access.
>
> - IP of accessing device textField
>
>   The IP of the device trying to access the application. Used for applying PingID policies that have been defined.
>
> - Attributes selectNameValueListColumn
>
>   Use this section to add attribute to the request
>
> * default object
>
>   * properties object
>
>     * customAuth object required
>
>       Custom Auth Properties
>
>       * pingIdProperties string minLength: 0 maxLength: 1000
>
>         PingID properties file
>
>       * skRedirectUri string minLength: 0 maxLength: 100 pattern: \[-a-zA-Z0-9@:%.\_+\~#={1,256}.\[a-zA-Z0-9()]{1,6} (\[-a-zA-Z0-9()@:%\_+.\~#?&//=]\*)]
>
>         Return URL
>
>     * sub string required minLength: 0 maxLength: 100
>
>       Subject
>
>     * fname string minLength: 0 maxLength: 100
>
>       First Name
>
>     * lname string minLength: 0 maxLength: 100
>
>       Last Name
>
>     * group string minLength: 0
>
>       User Groups
>
>     * phone string minLength: 0 maxLength: 100
>
>       Mobile Number
>
>     * voiceNumber string minLength: 0 maxLength: 100
>
>       Phone Number
>
>     * appName string minLength: 0 maxLength: 100
>
>       Application Name
>
>     * saasid string minLength: 0 maxLength: 100
>
>       Application ID
>
>     * appIconUrl string minLength: 0 maxLength: 1000
>
>       Application Icon (URL)
>
>     * pingidIp string minLength: 0 maxLength: 100
>
>       Policy Evaluation IP
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "customAuth": {
>       "pingIdProperties": "{pingid} props file"
>     },
>     "sub": "User"
>   }
> }
> ```
>
> * output object
>
>   * ppmResponse string
>
>   * status string
>
>   * sub string
>
>   * accessingDevice object
>
>     * ip string
>
>   * authenticationDevice object
>
>     * id string
>
>   * authenticationType string

#### Initialize Passwordless Authentication

Passwordless authentication using FIDO2 supported devices.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Attributes selectNameValueListColumn
>
>   Use this section to add attribute to the request
>
> * default object
>
>   * properties object
>
>     * customAuth object required
>
>       Custom Auth Properties
>
>       * pingIdProperties string minLength: 0 maxLength: 1000
>
>         PingID properties file
>
>       * skRedirectUri string minLength: 0 maxLength: 100 pattern: \[-a-zA-Z0-9@:%.\_\\\\+\~#={1,256}\\\\.\[a-zA-Z0-9()]{1,6}\ (\[-a-zA-Z0-9()@:%\_\\\\+.\~#?&//=]\*)]
>
>         Return URL
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "customAuth": {
>       "pingIdProperties": "{pingid} props file"
>     }
>   }
> }
> ```
>
> * output object
>
>   * ppmResponse string
>
>   * status string
>
>   * sub string
>
>   * passwordlessContext string

#### Finalize Passwordless Authentication

Policy evaluation to complete the Passwordless Authentication.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Username textField
>
>   The username for the user in PingOne.
>
> - Passwordless Context textField
>
>   Information returned by the initializePasswordlessAuthentication capability of the connector. Required to continue the passwordless session.
>
> - First Name textField
>
>   User's first name.
>
> - Last Name textField
>
>   User's last name.
>
> - User Groups textField
>
>   The groups to which the user belongs. Used for applying PingID policies that have been defined.
>
> - Mobile Number textField
>
>   User's mobile phone number.
>
> - Landline Number textField
>
>   User's landline number.
>
> - Application Name textField
>
>   The name of the application the user is trying to access.
>
> - Application ID textField
>
>   The ID of the application the user is trying to access. Used for applying PingID policies that have been defined.
>
> - Application Icon (URL) textField
>
>   The URL of the icon that is used for the application the user is trying to access.
>
> - IP of accessing device textField
>
>   The IP of the device trying to access the application. Used for applying PingID policies that have been defined.
>
> - Attributes selectNameValueListColumn
>
>   Use this section to add attribute to the request
>
> * default object
>
>   * properties object
>
>     * customAuth object required
>
>       Custom Auth Properties
>
>       * pingIdProperties string minLength: 0 maxLength: 1000
>
>         PingID properties file
>
>       * skRedirectUri string minLength: 0 maxLength: 100 pattern: \[-a-zA-Z0-9@:%.\_\\\\+\~#={1,256}\\\\.\[a-zA-Z0-9()]{1,6}\ (\[-a-zA-Z0-9()@:%\_\\\\+.\~#?&//=]\*)]
>
>         Return URL
>
>     * sub string required minLength: 0 maxLength: 100
>
>       Subject
>
>     * passwordlessContext string required
>
>       Passwordless Context
>
>     * fname string minLength: 0 maxLength: 100
>
>       First Name
>
>     * lname string minLength: 0 maxLength: 100
>
>       Last Name
>
>     * group string minLength: 0
>
>       User Groups
>
>     * phone string minLength: 0 maxLength: 100
>
>       Mobile Number
>
>     * voiceNumber string minLength: 0 maxLength: 100
>
>       Phone Number
>
>     * appName string minLength: 0 maxLength: 100
>
>       Application Name
>
>     * saasid string minLength: 0 maxLength: 100
>
>       Application ID
>
>     * appIconUrl string minLength: 0 maxLength: 1000
>
>       Application Icon (URL)
>
>     * pingidIp string minLength: 0 maxLength: 100
>
>       Policy Evaluation IP
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "customAuth": {
>       "pingIdProperties": "{pingid} props file"
>     },
>     "sub": "User",
>     "passwordlessContext": "context"
>   }
> }
> ```
>
> * output object
>
>   * ppmResponse string
>
>   * status string
>
>   * sub string
>
>   * accessingDevice object
>
>     * ip string
>
>   * authenticationType string

### Troubleshooting

If you are having trouble with the PingID connector, you can try the following:

* Verify that when you created and configured the connector on the Connections page, you pasted correctly the contents of your PingID properties file.

* For each connector in the flow, make sure that all the mandatory inputs have been provided.

* Use the Analytics feature to find where the flow stopped.

* Select the Options icon, and turn on **Show Node ID**. This makes it easier to identify the source of inputs and outputs.