---
title: PingIntelligence 5.0 (June 2021)
description: PingIntelligence 5.0 provides the following enhancements:
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_release_notes_50
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_release_notes_50.html
revdate: April 3, 2024
section_ids:
  all-pingintelligence-components-now-support-a-single-unified-license: All PingIntelligence components now support a single unified license
  dashboard-enhancements: Dashboard Enhancements
  ase-updates: ASE Updates
  new-in-sideband-integration-policies: New in sideband integration policies
  new-in-deployment-tools: New in deployment tools
---

# PingIntelligence 5.0 (June 2021)

PingIntelligence 5.0 provides the following enhancements:

## All PingIntelligence components now support a single unified license

New

PingIntelligence now supports up to 10 subpath levels for API base paths when API Security Enforcer (ASE) is deployed in sideband mode. Subpath depth is the number of sub-paths for a unique API definition. For more information, see [Discovery sub-paths](../managing_pingintelligence_for_apis/pingintelligence_discovery_subpaths.html).

## Dashboard Enhancements

New

The PingIntelligence Dashboard is enhanced to provide improved user experience for the following functionalities:

* The updated **Attack management** page gives a comprehensive view of Indicators of Attacks (IoAs) on a per client basis. A separate **Enable / Disable Attacks** page helps the administrators in efficient attack management. For more information, see [Indicators of Attacks on REST APIs](../pingintelligence_reference_guide/pingintelligence_indicators_of_attacks_rest_apis.html).

* The **Training Status** page now allows you to view the training status for an API by selecting the API from a drop-down list. The page also has a new capability to download per API and across API attack thresholds in a JSON formatted text file. For more information, see [Training period status](../managing_pingintelligence_for_apis/pingintelligence_training_period_status.html).

## ASE Updates

New

ASE has the following new additions:

* **External Load Balancer support for ASE to ABS AI Engine traffic -**ASE can be optionally configured to utilize external load balancers to distribute traffic across ABS AI Engine nodes. This provides the flexibility to support auto-scale of ABS AI Engine nodes and more high availability configurations.

* **REST API for sideband token management -**The `Token API` helps to create, import, and delete ASE sideband tokens. You can also retrieve the list of tokens issued by ASE.

* **REST API for sideband authentication -** The `Authentication API` helps to enable and disable ASE sideband authentication. You can also retrieve the authentication status. For more information, see [REST APIs for sideband token and authentication](../pingintelligence_reference_guide/pingintelligence_rest_api_for_sideband_authentication.html).

## New in sideband integration policies

Improved

* **NGINX plus policy -**The updated PingIntelligence sideband policy can seamlessly integrate with NGINX Plus R22 or R23 systems. This enhanced policy supports NGINX nodes with PingAccess agents installed and can capture user information from the PingAccess token introspection. For more information, see [Installing NGINX Plus for RHEL 7.6](../pingintelligence_integrations/pingintelligence_nginx_plus_install.html).

* **Apigee policy -**The updated PingIntelligence sideband policy adds optional asynchronous communication between Apigee and ASE for improved performance when deployed in environments that do not require automated client blocking. For more information, see [Apigee integration](../pingintelligence_integrations/pingintelligence_apigee_integration.html).

* **Kong policy -** The PingIntelligence sideband policy is enhanced to support extraction of user information from JWTs when OpenID Connect (OIDC) plugin is installed in a Kong gateway. For more information, see [Kong API gateway integration](../pingintelligence_integrations/pingintelligence_kong_integration.html).

## New in deployment tools

Improved

The following PingIntelligence deployment tools have been modified to support integration with PingOne:

* [PingIntelligence Ansible deployment framework](../installing_pingintelligence_for_apis/pingintelligence_automated_deployment.html)

* [PingIntelligence Docker PoC deployment](../installing_pingintelligence_for_apis/pingintelligence_docker_evaluation.html)

* [PingIntelligence Kubernetes deployment](../installing_pingintelligence_for_apis/pingintelligence_kubernetes_deployment.html)

* [PingIntelligence Docker toolkit](../installing_pingintelligence_for_apis/pingintelligence_docker_toolkit.html)
