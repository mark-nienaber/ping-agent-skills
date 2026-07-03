---
title: Change signing certificates
description: The Dynamics CRM server may cache the signing certificate, which can cause trust errors when changing the PingFederate signing certificate. Reconfiguring claims-based authentication is recommended when you change the PingFederate signing certificate. After changing the signing certificate in the Dynamics CRM connection, do the following in the Dynamics CRM server:
component: dynamicscrm
page_id: dynamicscrm::pf_dynamicscrm_integration_change_signing_certificates
canonical_url: https://docs.pingidentity.com/integrations/dynamicscrm/pf_dynamicscrm_integration_change_signing_certificates.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Change signing certificates

## About this task

The Dynamics CRM server may cache the signing certificate, which can cause trust errors when changing the PingFederate signing certificate. Reconfiguring claims-based authentication is recommended when you change the PingFederate signing certificate. After changing the signing certificate in the Dynamics CRM connection, do the following in the Dynamics CRM server:

## Steps

1. In the Microsoft Dynamics CRM Deployment Manager, disable claims-based authentication.

2. Run `iisreset` from the command line on the Dynamics CRM Web server.

3. In the Microsoft Dynamics CRM Deployment Manager, reconfigure claims-based authentication.

4. In the Microsoft Dynamics CRM Deployment Manager, if previously enabled, reconfigure Internet-Facing Deployment.

5. Run `iisreset` from the command line on the Dynamics CRM Web server.
