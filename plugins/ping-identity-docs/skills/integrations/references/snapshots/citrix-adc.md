---
title: Citrix ADC Integration Guide
description: This guide describes how to configure PingFederate and Citrix ADC to enable single sign-on (SSO).
component: citrix-adc
page_id: citrix-adc::pf_citrix_adc_integration
canonical_url: https://docs.pingidentity.com/integrations/citrix-adc/pf_citrix_adc_integration.html
revdate: June 26, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Citrix ADC Integration Guide

This guide describes how to configure PingFederate and Citrix ADC to enable single sign-on (SSO).

This allows you to use PingFederate as an identity provider (IdP) for Citrix ADC and Gateway.

The integration uses a standard SAML configuration and does not require any additional software.

## Features

* Browser-based SSO initiated by the IdP or service provider (SP).

## Intended audience

This document is intended for PingFederate administrators. Before you start, you should be familiar with the following:

* [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html) in the PingFederate documentation

* The following sections of the Citrix documentation:

  * [SAML authentication](https://docs.citrix.com/en-us/citrix-adc/13/aaa-tm/saml-authentication.html)

  * [Authentication, authorization, and auditing Application Traffic](https://docs.citrix.com/en-us/citrix-adc/13/aaa-tm)

## System requirements

* Citrix ADC 13.0 or later

* A DNS configuration that routes authentication requests to a Citrix ADC virtual IP address

* An SSL certificate installed on the Citrix ADC appliance
