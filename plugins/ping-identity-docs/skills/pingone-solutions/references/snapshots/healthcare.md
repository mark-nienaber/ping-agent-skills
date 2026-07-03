---
title: About Healthcare flow pack
description: Learn about the purpose and configuration of the Healthcare flow pack.
component: pingone-solutions
page_id: pingone-solutions:healthcare:index
canonical_url: https://docs.pingidentity.com/pingone-solutions/healthcare/index.html
revdate: January 15, 2026
---

# About Healthcare flow pack

The Healthcare flow pack lets you provide end users (your patients) with a secure way to register an account and sign on, and provides customer service representatives with a way to manage user healthcare accounts, all using a simple getting started experience and pre-built PingOne DaVinci flows.

This flow pack enables robust threat detection against bots, disposable email, and Adversary-in-the-Middle (AITM) attacks. It also analyzes risk signals to detect high, medium, and low threats to reduce the risk of account takeovers.

The flow pack uses three main flows to handle separate portions of the process:

* **Healthcare - Registration with Threat Detection and ID Verification - Main Flow** lets users register an account, including performing a threat assessment and verifying the user's identity.

* **Healthcare - Progressive Verification during Authentication - Main Flow** lets users sign on.

* **Healthcare - CSR Help Desk - Main Flow** lets customer service representatives assist users with account management tasks such as enabling an account or resetting a password.

You can view additional information about the solution, including download links, in the Ping Identity Marketplace. Learn more at [Healthcare flow pack on the Marketplace](https://marketplace.pingone.com/item/healthcare-patient-experience-flow-pack).

Preparing the Healthcare flow pack solution involves configuration steps in PingOne and DaVinci:

* In PingOne, perform basic configuration to prepare the flows to be launched and enable features such as multi-factor authentication (MFA) and PingOne notifications.

* In DaVinci, configure variables and flow settings to customize the flow behavior for your environment and customers.

* Clone the flows for use in your production environment.

The Healthcare flow pack solution offers many of the available DaVinci capabilities. However, the solution limits the pre-built components to common use cases and selected best practices.

The solution includes a variety of authentication methods, such as email magic link, email and SMS OTP, FIDO2, voice, mobile applications, and Time-based One-Time Passwords (TOTPs).

|   |                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Healthcare flow pack solution offers pre-built flow templates and configurations. Review these components with your Ping Identity account representative to understand the limitations and risks associated with this solution. Your account representative can also help you customize the pre-built flow templates to satisfy any compliance or regulatory requirements that relate to your business. |

This solution uses PingOne and DaVinci. Learn more about managing users and other PingOne tasks in the [PingOne documentation](https://docs.pingidentity.com/pingone/p1_cloud__platform_main_landing_page.html). Learn more about customizing flows in the [DaVinci documentation](https://docs.pingidentity.com/davinci/davinci_landing_page.html).
