---
title: Actions reference
description: Actions are predefined sets of nodes designed to perform specific tasks. They are not complete flows, but you can use them during flow creation to simplify the process.
component: davinci
page_id: davinci:flows:davinci_actions
canonical_url: http://docs.pingidentity.com/davinci/flows/davinci_actions.html
llms_txt: http://docs.pingidentity.com/davinci/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 21, 2026
section_ids:
  registration: Registration
  sign-up-with-tos-agreement: Sign up with TOS Agreement
  description: Description
  required-configuration: Required configuration
  outputs: Outputs
  email-verification: Email verification
  description-2: Description
  required-configuration-2: Required configuration
  outputs-2: Outputs
  mfa-device-registration: MFA Device Registration
  description-3: Description
  required-configuration-3: Required configuration
  outputs-3: Outputs
  authentication: Authentication
  mfa-device-authentication: MFA Device Authentication
  description-4: Description
  required-configuration-4: Required configuration
  inputs: Inputs
  sign-on-with-password-reset: Sign On with Password Reset
  description-5: Description
  required-configuration-5: Required configuration
  outputs-4: Outputs
  account-recovery: Account Recovery
  account-recovery-2: Account Recovery
  description-6: Description
  required-configuration-6: Required configuration
  inputs-2: Inputs
---

# Actions reference

Actions are predefined sets of nodes designed to perform specific tasks. They are not complete flows, but you can use them during flow creation to simplify the process.

Actions can be placed in the following categories:

* **Registration**: Actions that are used in the creation of new users.

* **Authentication**: Actions that are used to authenticate existing users.

* **Account Recovery**: Actions that are used to help a user recover an account.

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | Actions are currently available in the [PingOne Marketplace](https://marketplace.pingone.com/browse?products=davinci). |

## Registration

Registration actions are used in the creation of new users.

### Sign up with TOS Agreement

This action lets a user create an account and agree to a TOS.

![A screen capture of the Sign Up With TOS Agreement action.](_images/Actions-Sign-Up-with-TOS-Agreement.png)

#### Description

This action presents the user with an account registration form including an agreement. It then uses an authentication connector to create the user account.

#### Required configuration

To configure the action:

1. Click the **Registration** node, then in the **Agreement** field, select an agreement to present to the user.

   To find the agreement ID, sign on to PingOne and go to **User Experience** > **Agreements**. Select the agreement and click the API tab to view the policy ID.

2. Click the **Authentication** node, then in the **Population** field, select a user population in which to create the user.

   To find the population ID, sign on to PingOne and go to **Directory** > **Populations**. Select the population to view the population ID.

3. Connect the beginning and ending nodes to the rest of your flow.

#### Outputs

This action identifies the user.

### Email verification

This action lets a user verify an email address.

![A screen capture of the Email Verification action.](_images/Actions-Email-Verification.png)

#### Description

This action presents the user with a registration form. An authentication node creates the user and sends a verification code, then an email verification form displays. If the user submits a verification code, an authentication node verifies the code. If the user clicks **Resend Code**, an authentication node resends the code if the retry limit has not been reached.

#### Required configuration

To configure the action:

1. Click the first **Authentication** node, then in the **Population** field, select a user population in which to create the user.

   To find the population ID, sign on to PingOne and go to **Directory** > **Populations**. Select the population to view the population ID.

2. Connect the beginning and ending nodes to the rest of your flow.

#### Outputs

This action identifies the user.

### MFA Device Registration

This action lets a user register an MFA device.

![A screen capture of the MFA Device Registration action.](_images/Actions-MFA-Device-Registration.png)

#### Description

This action presents users with a form for selecting an MFA device. If the user selects authenticator, email, text, or voice, it uses a function connector to set visibility parameters, then if the MFA method uses OTP, it presents the user with a form on which to enter their email or phone number.

The action then uses an MFA node to begin device registration. If the device type is OTP or TOTP, it presents a form on which the user can enter a passcode. If the device type is FIDO, it presents a form on which the user can configure a FIDO2 authentication method. In either case, an MFA node then completes the device registration.

#### Required configuration

To configure the action:

1. Click the first **MFA** node, then in the **MFA Policy ID** list, select an MFA policy to use.

   To find the MFA policy ID, sign on to PingOne and go to **Authentication** > **MFA**. Select the policy to view the policy ID.

2. Connect the beginning and ending nodes to the rest of your flow.

#### Outputs

This action identifies the user.

## Authentication

This section describes actions that are used to authenticate existing users.

### MFA Device Authentication

This action lets a user authenticate using a known MFA device.

![A screen capture of the MFA Device Authentication action.](_images/Actions-MFA-Device-Authentication-2.png)

#### Description

This action uses an MFA node to check the authentication policy. If the MFA policy's method selection is set to Prompt user to select, a form prompts the user to select an MFA device. If the user selects authenticator, email, text, or voice, it uses a function connector to set visibility parameters.

The action then uses an MFA node to begin device authentication. If the device type is OTP or TOTP, it presents a form on which the user can enter a passcode. If the device type is FIDO, it presents a form on which the user can configure a FIDO2 authentication method. In either case, an MFA node then completes the device authentication.

#### Required configuration

To configure the action:

1. Click the first **MFA** node, then in the **MFA Policy ID** list, select an MFA policy to use.

   To find the MFA policy ID, sign on to PingOne and go to **Authentication** > **MFA**. Select the policy to view the policy ID.

2. Connect the beginning and ending nodes to the rest of your flow.

#### Inputs

This action requires an identified user.

### Sign On with Password Reset

This action lets a user sign on and reset their password if necessary.

![A screen capture of the Sign On with Password Reset action.](_images/Actions-Sign-In-Password-Reset.png)

#### Description

This action presents the user with a sign on form. An Authentication node checks if the user requires a new password. If the user does not require a new password, an authentication node authenticates the user. If the user requires a new password, a form prompts the user for a new password, then an authentication node updates the password.

#### Required configuration

To configure the action:

1. Click the second **Authentication** node, then in the **Agreement** field, select an agreement to present to the user.

   To find the agreement ID, sign on to PingOne and go to **User Experience** > **Agreements**. Select the agreement and click the API tab to view the policy ID.

2. Connect the beginning and ending nodes to the rest of your flow.

#### Outputs

This action requires an identified user.

## Account Recovery

This section describes actions that are used to help a user recover an account.

### Account Recovery

This action lets a user recover an account.

![A screen capture of the Account Recovery action.](_images/Actions-account-recovery.png)

#### Description

This action presents the user with a password recovery form. It then uses an authentication node to send a recovery code, and presents the user with a new password form. If the user completes the form and continues, an authentication node resets their password. If the user resends the code, an authentication node checks the number of retries and resends the code if the retry limit has not been reached.

#### Required configuration

To configure the action, connect the beginning and ending nodes to the rest of your flow.

#### Inputs

This action requires an identified user.
