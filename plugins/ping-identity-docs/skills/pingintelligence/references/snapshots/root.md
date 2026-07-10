---
description: PingAccess
component: pingintelligence
version: 5.2
page_id: pingintelligence::common_product_keydefs
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/common_product_keydefs.html
---

PingAccess

PingAuthorize

Policy Editor

PingCentral

PingCloud

PingDataGovernance

PingDataMetrics

PingDataSync

PingDirectory

PingDirectory Consent API

PingDirectoryProxy

Delegated Admin

PingFederate

PingFederate Bridge

PingID

PingID SDK

PingID desktop app

PingID mobile app

PingIntelligence

PingIntelligence for APIs

PingOne

PingOne Authorize

PingOne SSO for SaaS Apps

PingOne

PingOne MFA

PingID

PingOne Protect

PingOne Verify

PingOne for Enterprise

the PingOne administration console

Customer360

Workforce360

DaVinci

PingOne Advanced Identity Cloud

Advanced Identity Cloud

PingOne

PingOne Neo

PingOne Solutions

PingOne for Customers

PingOne for Workforce

PingOne for Individuals

PingOne for Government

PingOne Services

PingOne SSO

PingOne Credentials

PingOne Advanced Services

PingOne Advanced Services Single Sign-on

PingOne Advanced Services Security

PingOne Advanced Services Directory

PingOne Dynamic Authorization

PingOne Advanced API Security

PingOne Advanced Central Administration

PingOne Fraud

PingOne API Intelligence

PingOne API Access Management

ShoCard

PingOne for Individuals SDK

PingOne for Customers Passwordless

PingOne for Customers Plus

NET

AD Connect

AirWatch

Akana

Amazon Web Services

AWS

Apache

Apigee

Atlassian

Axway

Azure AD

Box

Citrix

Cloud Identity

Concur

CoreBlox

Coupa

Dropbox

Duo Security

Egnyte

Evernote

Facebook

G Suite

Google

Google Apps

Heroku

IIS

Intune

Java

LinkedIn

Linux

Microsoft

MobileIron

Mulesoft

NGINX

Office 365

Oracle Access Manager

Oracle Directory Server Enterprise Edition

PHP

Palo Alto Networks

RSA SecurID

SAP NetWeaver

Salesforce

ServiceNow

SharePoint

Slack

Splunk

Symantec VIP

Twitter

VMware

WebEx

WebLogic

WebSphere

Windows Live

Workday

Workplace by Facebook

YubiCloud

YubiKey

Zendesk

---

---
title: Introduction to PingIntelligence for APIs
description: PingIntelligence for APIs uses artificial intelligence (AI) to secure APIs in your environment. It identifies and automatically blocks cyberattacks on APIs, exposes active APIs, and provides detailed reporting on all API activity.
component: pingintelligence
version: 5.2
page_id: pingintelligence::pingintelligence_introduction
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_introduction.html
revdate: April 3, 2024
section_ids:
  key-components: Key components
  related-links: Related links
---

# Introduction to PingIntelligence for APIs

PingIntelligence for APIs uses artificial intelligence (AI) to secure APIs in your environment. It identifies and automatically blocks cyberattacks on APIs, exposes active APIs, and provides detailed reporting on all API activity.

Leveraging AI models specifically tailored for application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* security, PingIntelligence brings cyberattack protection and deep API traffic insight to existing API gateways and application server-based API environments. It detects anomalous behavior on APIs and the data and applications exposed through APIs. It also automatically blocks attacks across your API environment.

## Key components

PingIntelligence is a suite of three interconnected components, API Security Enforcer (ASE), API Behavioral Security (ABS) AI engine, and PingIntelligence Dashboard:

* ASE

  The first processing layer in PingIntelligence. It captures the metadata of the monitored APIs and sends it to the ABS AI engine. You can deploy ASE in two modes, inline and sideband. When deployed in inline mode, ASE directly receives the API traffic or can work alongside other load balancers like AWSElastic Load Balancing (ELB). In sideband mode, ASE integrates with API gateways in an ecosystem and extends the cybersecurity of PingIntelligence.

* ABS AI engine

  The AI engine infers the API traffic patterns in the metadata from ASE. It builds machine learning models that self-train based on the API traffic. ABS detects the attacks on APIs and blocks the clients from which the attacks originate. It also provides in-depth forensics on the activities performed by a client. The reports provide detailed information on the activity from an individual token, Internet Protocol (IP) *(tooltip: \<div class="paragraph">
  \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
  \</div>)* address, cookie, API key, or username. In addition to attack detection, ABS continuously discovers the new and unknown APIs in an API ecosystem and brings them under observation.

* PingIntelligence Dashboard

  PingIntelligence Dashboard provides rich analytics on API activities in an environment. It gives granular insights at an API level and across APIs. It can provide information on the training status of APIs, different kinds of attacks on APIs, and much more. PingIntelligence Dashboard also supports admin activities such as attack management and discovery of APIs.

![PingIntelligence for APIs key components](_images/kvv1613806714485.png)

## Related links

* [Sideband ASE](pingintelligence_reference_guide/pingintelligence_sideband_ase.html)

* [Inline ASE](pingintelligence_reference_guide/pingintelligence_inline_ase.html)

* [ABS AI Engine](pingintelligence_reference_guide/pingintelligence_abs_ai_engine.html)

* [PingIntelligence for APIs Dashboard](pingintelligence_reference_guide/pingintelligence_dashboard.html)