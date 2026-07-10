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

---

---
title: PingIntelligence 5.0.1 (August 2021)
description: PingIntelligence for APIs 5.0.1 provides the following updates:
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_release_notes_501
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_release_notes_501.html
revdate: April 3, 2024
section_ids:
  ase-integration: ASE Integration
  new-pingintelligence-docker-toolkit-environment-variables: New PingIntelligence Docker Toolkit Environment Variables
---

# PingIntelligence 5.0.1 (August 2021)

PingIntelligence for APIs 5.0.1 provides the following updates:

## ASE Integration

Improved

The API Security Enforcer (ASE) now supports integration with [PingOne](https://docs.pingidentity.com/bundle/p14c/page/als1564020488261.html) platform. You can deploy ASE on-premise in either inline or sideband mode and integrate it with [PingOne](https://docs.pingidentity.com/bundle/p14c/page/als1564020488261.html). This hybrid integration delivers API security through the new PingOne API Intelligence service.

## New PingIntelligence Docker Toolkit Environment Variables

New

The PingIntelligence Docker toolkit adds environment variables to support integration of ASE with the PingOne API Intelligence platform. For more information, see [PingIntelligence Docker toolkit](../installing_pingintelligence_for_apis/pingintelligence_docker_toolkit.html). The new environment variables support:

* Configuring gateway credentials to use for connecting ASE with the PingOne API Intelligence platform

* Setting the ABS AI engine deployment type to cloud or on-premise

---

---
title: PingIntelligence 5.1 (December 2021)
description: PingIntelligence for APIs 5.1 provides the following enhancements:
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_release_notes_51
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_release_notes_51.html
revdate: April 3, 2024
section_ids:
  new-in-dashboard: New in Dashboard
  new-in-ai-engine: New in AI Engine
  new-in-ase: New in ASE
  new-kubernetes-deployment: New Kubernetes Deployment
  resolved-issue-abs-ai-engine: "Resolved Issue: ABS AI engine"
  resolved-issue-dashboard-update: "Resolved Issue: Dashboard update"
---

# PingIntelligence 5.1 (December 2021)

PingIntelligence for APIs 5.1 provides the following enhancements:

## New in Dashboard

Improved

The PingIntelligence for APIs Dashboard is enhanced to provide an improved user experience for the following functionalities:

* New **PingOne Dashboard** provides a streamlined user interface with support for drill down into API details, blocklisted clients, and clients flagged for Indicators of Attack (IoAs). The rearchitected Dashboard significantly accelerates the processing of API metadata to speed updates to administrators on API activity and abnormal events. See [Dashboard](../managing_pingintelligence_for_apis/pingintelligence_dashboard_reference.html).

* An updated **Attack management GUI** delivers more detailed information to assist security administrators in analyzing Indicators of Attack (IoAs). The enhanced reporting includes additional insight into why a client's behavior was flagged, suggested remediation steps, and transaction-level details from API requests and responses associated with the anomalous behavior. See [Attack management](../managing_pingintelligence_for_apis/pingintelligence_attack_management.html).

* **Enhanced SIEM integration** pushes the same detailed IoA information (e.g. why flagged, remediation steps, transaction data) available via the Attack Management GUI to a SIEM. The SIEM integration enables a customer to combine anomalous API activity data with events from other security tools.

* **Automated Publishing of Discovered APIs** supports distributed discovery of APIs across multiple datacenters from a centralized or cloud-based Dashboard.

## New in AI Engine

Improved

Improved Anomalous API Header and Query String Detection

Updated AI algorithms detect anomalous values and content in API headers or query strings. Examples include hackers manipulating content, executing malicious scripts, passing attack variables, accessing unauthorized content, and other abnormal behavior. PingIntelligence detects and optionally blocks these manipulations and malicious activity. For more information, see [IoAs (Indicators of Attack)](../managing_pingintelligence_for_apis/pingintelligence_ioas.html).

## New in ASE

New

Real-Time Enforcement of Missing Token

For inline or sideband deployments, ASE can be configured to detect and automatically block clients not presenting a token to APIs requiring access tokens.

## New Kubernetes Deployment

New

Support for production PingIntelligence deployments in AWS EKS using a Ping-supplied Helm-Chart. See [PingIntelligence Kubernetes deployment](../installing_pingintelligence_for_apis/pingintelligence_kubernetes_deployment.html).

## Resolved Issue: ABS AI engine

Fixed

ABS AI engine has been updated to use a Log4j version with the fixes for the critical vulnerabilities.

## Resolved Issue: Dashboard update

Fixed

Dashboard has been updated to use a Log4j version with the fixes for the critical vulnerabilities.

---

---
title: PingIntelligence 5.2 (September 2023)
description: PingIntelligence for APIs 5.2 provides the following enhancements:
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_release_notes_52
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_release_notes_52.html
revdate: April 3, 2024
section_ids:
  new-in-dashboard: New in Dashboard
  new-in-ai-engine: New in AI Engine
---

# PingIntelligence 5.2 (September 2023)

PingIntelligence for APIs 5.2 provides the following enhancements:

## New in Dashboard

Improved

The PingIntelligence for APIs Dashboard is enhanced to provide an improved user experience with the following functionalities:

* Enhanced Main Dashboard

  The main dashboard adds tiles with quick links for **Discovered APIs**, **API Count**, and **Indicators of Attack**. See [PingIntelligence Dashboard](../pingintelligence_reference_guide/pingintelligence_dashboard.html).

* Enhanced SIEM integration

  The security information and event management (SIEM) integration provides a webhooks connection to a Splunk SIEM. The SIEM integration also enables a customer to combine anomalous API activity data with events from other security tools.

## New in AI Engine

Improved

Support for detection of user-based broken object-level authorization (BOLA), broken function-level authorization (BFLA), user-based data injection, and anomalous token claim detection. PingIntelligence detects and optionally blocks these manipulations and malicious activity. For more information, see [Indicators of attack](../pingintelligence_reference_guide/pingintelligence_indicators_of_attacks_rest_apis.html).

---

---
title: Previous Releases
description: This page shows changes and updates to PingIntelligence for APIs.
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_previous_releases
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_previous_releases.html
revdate: April 3, 2024
---

# Previous Releases

This page shows changes and updates to PingIntelligence for APIs.

* [PingIntelligence 4.4 (December 2020)](https://docs.pingidentity.com/bundle/pingintelligence-44/page/vmy1608344509701.html)

  * [PingIntelligence 4.4.1 (April 2021)](https://docs.pingidentity.com/bundle/pingintelligence-44/page/wzi1618467619364.html)

* [PingIntelligence 4.3](https://docs.pingidentity.com/bundle/pingintelligence-43/page/ehw1596783740016.html)

* [PingIntelligence 4.2](https://docs.pingidentity.com/bundle/pingintelligence-42/page/cxb1592908081245.html)

* [PingIntelligence 4.1](https://docs.pingidentity.com/bundle/pingintelligence-41/page/jty1574058854555.html)

  * [PingIntelligence 4.1.0](https://docs.pingidentity.com/bundle/pingintelligence-41/page/fms1582088964676.html)

  * [PingIntelligence 4.1.1](https://docs.pingidentity.com/bundle/pingintelligence-41/page/qmm1585822163289.html)

---

---
title: Release Notes
description: New features and improvements in PingIntelligence for APIs. Updated September 28, 2023.
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_release_notes
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_release_notes.html
revdate: April 3, 2024
section_ids:
  pingintelligence-5-2-september-2023: PingIntelligence 5.2 (September 2023)
  new-in-dashboard: New in Dashboard
  new-in-ai-engine: New in AI Engine
  pingintelligence-5-1-december-2021: PingIntelligence 5.1 (December 2021)
  new-in-dashboard-2: New in Dashboard
  new-in-ai-engine-2: New in AI Engine
  new-in-ase: New in ASE
  new-kubernetes-deployment: New Kubernetes Deployment
  resolved-issue-abs-ai-engine: "Resolved Issue: ABS AI engine"
  resolved-issue-dashboard-update: "Resolved Issue: Dashboard update"
  pingintelligence-5-0-1-august-2021: PingIntelligence 5.0.1 (August 2021)
  ase-integration: ASE Integration
  new-pingintelligence-docker-toolkit-environment-variables: New PingIntelligence Docker Toolkit Environment Variables
  pingintelligence-5-0-june-2021: PingIntelligence 5.0 (June 2021)
  all-pingintelligence-components-now-support-a-single-unified-license: All PingIntelligence components now support a single unified license
  dashboard-enhancements: Dashboard Enhancements
  ase-updates: ASE Updates
  new-in-sideband-integration-policies: New in sideband integration policies
  new-in-deployment-tools: New in deployment tools
  previous-releases: Previous Releases
---

# Release Notes

New features and improvements in PingIntelligence for APIs. Updated September 28, 2023.

## PingIntelligence 5.2 (September 2023)

PingIntelligence for APIs 5.2 provides the following enhancements:

### New in Dashboard

Improved

The PingIntelligence for APIs Dashboard is enhanced to provide an improved user experience with the following functionalities:

* Enhanced Main Dashboard

  The main dashboard adds tiles with quick links for **Discovered APIs**, **API Count**, and **Indicators of Attack**. See [PingIntelligence Dashboard](../pingintelligence_reference_guide/pingintelligence_dashboard.html).

* Enhanced SIEM integration

  The security information and event management (SIEM) integration provides a webhooks connection to a Splunk SIEM. The SIEM integration also enables a customer to combine anomalous API activity data with events from other security tools.

### New in AI Engine

Improved

Support for detection of user-based broken object-level authorization (BOLA), broken function-level authorization (BFLA), user-based data injection, and anomalous token claim detection. PingIntelligence detects and optionally blocks these manipulations and malicious activity. For more information, see [Indicators of attack](../pingintelligence_reference_guide/pingintelligence_indicators_of_attacks_rest_apis.html).

## PingIntelligence 5.1 (December 2021)

PingIntelligence for APIs 5.1 provides the following enhancements:

### New in Dashboard

Improved

The PingIntelligence for APIs Dashboard is enhanced to provide an improved user experience for the following functionalities:

* New **PingOne Dashboard** provides a streamlined user interface with support for drill down into API details, blocklisted clients, and clients flagged for Indicators of Attack (IoAs). The rearchitected Dashboard significantly accelerates the processing of API metadata to speed updates to administrators on API activity and abnormal events. See [Dashboard](../managing_pingintelligence_for_apis/pingintelligence_dashboard_reference.html).

* An updated **Attack management GUI** delivers more detailed information to assist security administrators in analyzing Indicators of Attack (IoAs). The enhanced reporting includes additional insight into why a client's behavior was flagged, suggested remediation steps, and transaction-level details from API requests and responses associated with the anomalous behavior. See [Attack management](../managing_pingintelligence_for_apis/pingintelligence_attack_management.html).

* **Enhanced SIEM integration** pushes the same detailed IoA information (e.g. why flagged, remediation steps, transaction data) available via the Attack Management GUI to a SIEM. The SIEM integration enables a customer to combine anomalous API activity data with events from other security tools.

* **Automated Publishing of Discovered APIs** supports distributed discovery of APIs across multiple datacenters from a centralized or cloud-based Dashboard.

### New in AI Engine

Improved

Improved Anomalous API Header and Query String Detection

Updated AI algorithms detect anomalous values and content in API headers or query strings. Examples include hackers manipulating content, executing malicious scripts, passing attack variables, accessing unauthorized content, and other abnormal behavior. PingIntelligence detects and optionally blocks these manipulations and malicious activity. For more information, see [IoAs (Indicators of Attack)](../managing_pingintelligence_for_apis/pingintelligence_ioas.html).

### New in ASE

New

Real-Time Enforcement of Missing Token

For inline or sideband deployments, ASE can be configured to detect and automatically block clients not presenting a token to APIs requiring access tokens.

### New Kubernetes Deployment

New

Support for production PingIntelligence deployments in AWS EKS using a Ping-supplied Helm-Chart. See [PingIntelligence Kubernetes deployment](../installing_pingintelligence_for_apis/pingintelligence_kubernetes_deployment.html).

### Resolved Issue: ABS AI engine

Fixed

ABS AI engine has been updated to use a Log4j version with the fixes for the critical vulnerabilities.

### Resolved Issue: Dashboard update

Fixed

Dashboard has been updated to use a Log4j version with the fixes for the critical vulnerabilities.

## PingIntelligence 5.0.1 (August 2021)

PingIntelligence for APIs 5.0.1 provides the following updates:

### ASE Integration

Improved

The API Security Enforcer (ASE) now supports integration with [PingOne](https://docs.pingidentity.com/bundle/p14c/page/als1564020488261.html) platform. You can deploy ASE on-premise in either inline or sideband mode and integrate it with [PingOne](https://docs.pingidentity.com/bundle/p14c/page/als1564020488261.html). This hybrid integration delivers API security through the new PingOne API Intelligence service.

### New PingIntelligence Docker Toolkit Environment Variables

New

The PingIntelligence Docker toolkit adds environment variables to support integration of ASE with the PingOne API Intelligence platform. For more information, see [PingIntelligence Docker toolkit](../installing_pingintelligence_for_apis/pingintelligence_docker_toolkit.html). The new environment variables support:

* Configuring gateway credentials to use for connecting ASE with the PingOne API Intelligence platform

* Setting the ABS AI engine deployment type to cloud or on-premise

## PingIntelligence 5.0 (June 2021)

PingIntelligence 5.0 provides the following enhancements:

### All PingIntelligence components now support a single unified license

New

PingIntelligence now supports up to 10 subpath levels for API base paths when API Security Enforcer (ASE) is deployed in sideband mode. Subpath depth is the number of sub-paths for a unique API definition. For more information, see [Discovery sub-paths](../managing_pingintelligence_for_apis/pingintelligence_discovery_subpaths.html).

### Dashboard Enhancements

New

The PingIntelligence Dashboard is enhanced to provide improved user experience for the following functionalities:

* The updated **Attack management** page gives a comprehensive view of Indicators of Attacks (IoAs) on a per client basis. A separate **Enable / Disable Attacks** page helps the administrators in efficient attack management. For more information, see [Indicators of Attacks on REST APIs](../pingintelligence_reference_guide/pingintelligence_indicators_of_attacks_rest_apis.html).

* The **Training Status** page now allows you to view the training status for an API by selecting the API from a drop-down list. The page also has a new capability to download per API and across API attack thresholds in a JSON formatted text file. For more information, see [Training period status](../managing_pingintelligence_for_apis/pingintelligence_training_period_status.html).

### ASE Updates

New

ASE has the following new additions:

* **External Load Balancer support for ASE to ABS AI Engine traffic -**ASE can be optionally configured to utilize external load balancers to distribute traffic across ABS AI Engine nodes. This provides the flexibility to support auto-scale of ABS AI Engine nodes and more high availability configurations.

* **REST API for sideband token management -**The `Token API` helps to create, import, and delete ASE sideband tokens. You can also retrieve the list of tokens issued by ASE.

* **REST API for sideband authentication -** The `Authentication API` helps to enable and disable ASE sideband authentication. You can also retrieve the authentication status. For more information, see [REST APIs for sideband token and authentication](../pingintelligence_reference_guide/pingintelligence_rest_api_for_sideband_authentication.html).

### New in sideband integration policies

Improved

* **NGINX plus policy -**The updated PingIntelligence sideband policy can seamlessly integrate with NGINX Plus R22 or R23 systems. This enhanced policy supports NGINX nodes with PingAccess agents installed and can capture user information from the PingAccess token introspection. For more information, see [Installing NGINX Plus for RHEL 7.6](../pingintelligence_integrations/pingintelligence_nginx_plus_install.html).

* **Apigee policy -**The updated PingIntelligence sideband policy adds optional asynchronous communication between Apigee and ASE for improved performance when deployed in environments that do not require automated client blocking. For more information, see [Apigee integration](../pingintelligence_integrations/pingintelligence_apigee_integration.html).

* **Kong policy -** The PingIntelligence sideband policy is enhanced to support extraction of user information from JWTs when OpenID Connect (OIDC) plugin is installed in a Kong gateway. For more information, see [Kong API gateway integration](../pingintelligence_integrations/pingintelligence_kong_integration.html).

### New in deployment tools

Improved

The following PingIntelligence deployment tools have been modified to support integration with PingOne:

* [PingIntelligence Ansible deployment framework](../installing_pingintelligence_for_apis/pingintelligence_automated_deployment.html)

* [PingIntelligence Docker PoC deployment](../installing_pingintelligence_for_apis/pingintelligence_docker_evaluation.html)

* [PingIntelligence Kubernetes deployment](../installing_pingintelligence_for_apis/pingintelligence_kubernetes_deployment.html)

* [PingIntelligence Docker toolkit](../installing_pingintelligence_for_apis/pingintelligence_docker_toolkit.html)

## Previous Releases

This page shows changes and updates to PingIntelligence for APIs.

* [PingIntelligence 4.4 (December 2020)](https://docs.pingidentity.com/bundle/pingintelligence-44/page/vmy1608344509701.html)

  * [PingIntelligence 4.4.1 (April 2021)](https://docs.pingidentity.com/bundle/pingintelligence-44/page/wzi1618467619364.html)

* [PingIntelligence 4.3](https://docs.pingidentity.com/bundle/pingintelligence-43/page/ehw1596783740016.html)

* [PingIntelligence 4.2](https://docs.pingidentity.com/bundle/pingintelligence-42/page/cxb1592908081245.html)

* [PingIntelligence 4.1](https://docs.pingidentity.com/bundle/pingintelligence-41/page/jty1574058854555.html)

  * [PingIntelligence 4.1.0](https://docs.pingidentity.com/bundle/pingintelligence-41/page/fms1582088964676.html)

  * [PingIntelligence 4.1.1](https://docs.pingidentity.com/bundle/pingintelligence-41/page/qmm1585822163289.html)

---

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

---

---
title: PingIntelligence 5.0.1 (August 2021)
description: PingIntelligence for APIs 5.0.1 provides the following updates:
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_release_notes_501
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_release_notes_501.html
revdate: April 3, 2024
section_ids:
  ase-integration: ASE Integration
  new-pingintelligence-docker-toolkit-environment-variables: New PingIntelligence Docker Toolkit Environment Variables
---

# PingIntelligence 5.0.1 (August 2021)

PingIntelligence for APIs 5.0.1 provides the following updates:

## ASE Integration

Improved

The API Security Enforcer (ASE) now supports integration with [PingOne](https://docs.pingidentity.com/bundle/p14c/page/als1564020488261.html) platform. You can deploy ASE on-premise in either inline or sideband mode and integrate it with [PingOne](https://docs.pingidentity.com/bundle/p14c/page/als1564020488261.html). This hybrid integration delivers API security through the new PingOne API Intelligence service.

## New PingIntelligence Docker Toolkit Environment Variables

New

The PingIntelligence Docker toolkit adds environment variables to support integration of ASE with the PingOne API Intelligence platform. For more information, see [PingIntelligence Docker toolkit](../installing_pingintelligence_for_apis/pingintelligence_docker_toolkit.html). The new environment variables support:

* Configuring gateway credentials to use for connecting ASE with the PingOne API Intelligence platform

* Setting the ABS AI engine deployment type to cloud or on-premise

---

---
title: PingIntelligence 5.1 (December 2021)
description: PingIntelligence for APIs 5.1 provides the following enhancements:
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_release_notes_51
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_release_notes_51.html
revdate: April 3, 2024
section_ids:
  new-in-dashboard: New in Dashboard
  new-in-ai-engine: New in AI Engine
  new-in-ase: New in ASE
  new-kubernetes-deployment: New Kubernetes Deployment
  resolved-issue-abs-ai-engine: "Resolved Issue: ABS AI engine"
  resolved-issue-dashboard-update: "Resolved Issue: Dashboard update"
---

# PingIntelligence 5.1 (December 2021)

PingIntelligence for APIs 5.1 provides the following enhancements:

## New in Dashboard

Improved

The PingIntelligence for APIs Dashboard is enhanced to provide an improved user experience for the following functionalities:

* New **PingOne Dashboard** provides a streamlined user interface with support for drill down into API details, blocklisted clients, and clients flagged for Indicators of Attack (IoAs). The rearchitected Dashboard significantly accelerates the processing of API metadata to speed updates to administrators on API activity and abnormal events. See [Dashboard](../managing_pingintelligence_for_apis/pingintelligence_dashboard_reference.html).

* An updated **Attack management GUI** delivers more detailed information to assist security administrators in analyzing Indicators of Attack (IoAs). The enhanced reporting includes additional insight into why a client's behavior was flagged, suggested remediation steps, and transaction-level details from API requests and responses associated with the anomalous behavior. See [Attack management](../managing_pingintelligence_for_apis/pingintelligence_attack_management.html).

* **Enhanced SIEM integration** pushes the same detailed IoA information (e.g. why flagged, remediation steps, transaction data) available via the Attack Management GUI to a SIEM. The SIEM integration enables a customer to combine anomalous API activity data with events from other security tools.

* **Automated Publishing of Discovered APIs** supports distributed discovery of APIs across multiple datacenters from a centralized or cloud-based Dashboard.

## New in AI Engine

Improved

Improved Anomalous API Header and Query String Detection

Updated AI algorithms detect anomalous values and content in API headers or query strings. Examples include hackers manipulating content, executing malicious scripts, passing attack variables, accessing unauthorized content, and other abnormal behavior. PingIntelligence detects and optionally blocks these manipulations and malicious activity. For more information, see [IoAs (Indicators of Attack)](../managing_pingintelligence_for_apis/pingintelligence_ioas.html).

## New in ASE

New

Real-Time Enforcement of Missing Token

For inline or sideband deployments, ASE can be configured to detect and automatically block clients not presenting a token to APIs requiring access tokens.

## New Kubernetes Deployment

New

Support for production PingIntelligence deployments in AWS EKS using a Ping-supplied Helm-Chart. See [PingIntelligence Kubernetes deployment](../installing_pingintelligence_for_apis/pingintelligence_kubernetes_deployment.html).

## Resolved Issue: ABS AI engine

Fixed

ABS AI engine has been updated to use a Log4j version with the fixes for the critical vulnerabilities.

## Resolved Issue: Dashboard update

Fixed

Dashboard has been updated to use a Log4j version with the fixes for the critical vulnerabilities.

---

---
title: Release Notes
description: New features and improvements in PingIntelligence for APIs. Updated September 28, 2023.
component: pingintelligence
version: 5.2
page_id: pingintelligence:release_notes:pingintelligence_release_notes
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/release_notes/pingintelligence_release_notes.html
revdate: April 3, 2024
section_ids:
  pingintelligence-5-2-september-2023: PingIntelligence 5.2 (September 2023)
  new-in-dashboard: New in Dashboard
  new-in-ai-engine: New in AI Engine
  pingintelligence-5-1-december-2021: PingIntelligence 5.1 (December 2021)
  new-in-dashboard-2: New in Dashboard
  new-in-ai-engine-2: New in AI Engine
  new-in-ase: New in ASE
  new-kubernetes-deployment: New Kubernetes Deployment
  resolved-issue-abs-ai-engine: "Resolved Issue: ABS AI engine"
  resolved-issue-dashboard-update: "Resolved Issue: Dashboard update"
  pingintelligence-5-0-1-august-2021: PingIntelligence 5.0.1 (August 2021)
  ase-integration: ASE Integration
  new-pingintelligence-docker-toolkit-environment-variables: New PingIntelligence Docker Toolkit Environment Variables
  pingintelligence-5-0-june-2021: PingIntelligence 5.0 (June 2021)
  all-pingintelligence-components-now-support-a-single-unified-license: All PingIntelligence components now support a single unified license
  dashboard-enhancements: Dashboard Enhancements
  ase-updates: ASE Updates
  new-in-sideband-integration-policies: New in sideband integration policies
  new-in-deployment-tools: New in deployment tools
  previous-releases: Previous Releases
---

# Release Notes

New features and improvements in PingIntelligence for APIs. Updated September 28, 2023.

## PingIntelligence 5.2 (September 2023)

PingIntelligence for APIs 5.2 provides the following enhancements:

### New in Dashboard

Improved

The PingIntelligence for APIs Dashboard is enhanced to provide an improved user experience with the following functionalities:

* Enhanced Main Dashboard

  The main dashboard adds tiles with quick links for **Discovered APIs**, **API Count**, and **Indicators of Attack**. See [PingIntelligence Dashboard](../pingintelligence_reference_guide/pingintelligence_dashboard.html).

* Enhanced SIEM integration

  The security information and event management (SIEM) integration provides a webhooks connection to a Splunk SIEM. The SIEM integration also enables a customer to combine anomalous API activity data with events from other security tools.

### New in AI Engine

Improved

Support for detection of user-based broken object-level authorization (BOLA), broken function-level authorization (BFLA), user-based data injection, and anomalous token claim detection. PingIntelligence detects and optionally blocks these manipulations and malicious activity. For more information, see [Indicators of attack](../pingintelligence_reference_guide/pingintelligence_indicators_of_attacks_rest_apis.html).

## PingIntelligence 5.1 (December 2021)

PingIntelligence for APIs 5.1 provides the following enhancements:

### New in Dashboard

Improved

The PingIntelligence for APIs Dashboard is enhanced to provide an improved user experience for the following functionalities:

* New **PingOne Dashboard** provides a streamlined user interface with support for drill down into API details, blocklisted clients, and clients flagged for Indicators of Attack (IoAs). The rearchitected Dashboard significantly accelerates the processing of API metadata to speed updates to administrators on API activity and abnormal events. See [Dashboard](../managing_pingintelligence_for_apis/pingintelligence_dashboard_reference.html).

* An updated **Attack management GUI** delivers more detailed information to assist security administrators in analyzing Indicators of Attack (IoAs). The enhanced reporting includes additional insight into why a client's behavior was flagged, suggested remediation steps, and transaction-level details from API requests and responses associated with the anomalous behavior. See [Attack management](../managing_pingintelligence_for_apis/pingintelligence_attack_management.html).

* **Enhanced SIEM integration** pushes the same detailed IoA information (e.g. why flagged, remediation steps, transaction data) available via the Attack Management GUI to a SIEM. The SIEM integration enables a customer to combine anomalous API activity data with events from other security tools.

* **Automated Publishing of Discovered APIs** supports distributed discovery of APIs across multiple datacenters from a centralized or cloud-based Dashboard.

### New in AI Engine

Improved

Improved Anomalous API Header and Query String Detection

Updated AI algorithms detect anomalous values and content in API headers or query strings. Examples include hackers manipulating content, executing malicious scripts, passing attack variables, accessing unauthorized content, and other abnormal behavior. PingIntelligence detects and optionally blocks these manipulations and malicious activity. For more information, see [IoAs (Indicators of Attack)](../managing_pingintelligence_for_apis/pingintelligence_ioas.html).

### New in ASE

New

Real-Time Enforcement of Missing Token

For inline or sideband deployments, ASE can be configured to detect and automatically block clients not presenting a token to APIs requiring access tokens.

### New Kubernetes Deployment

New

Support for production PingIntelligence deployments in AWS EKS using a Ping-supplied Helm-Chart. See [PingIntelligence Kubernetes deployment](../installing_pingintelligence_for_apis/pingintelligence_kubernetes_deployment.html).

### Resolved Issue: ABS AI engine

Fixed

ABS AI engine has been updated to use a Log4j version with the fixes for the critical vulnerabilities.

### Resolved Issue: Dashboard update

Fixed

Dashboard has been updated to use a Log4j version with the fixes for the critical vulnerabilities.

## PingIntelligence 5.0.1 (August 2021)

PingIntelligence for APIs 5.0.1 provides the following updates:

### ASE Integration

Improved

The API Security Enforcer (ASE) now supports integration with [PingOne](https://docs.pingidentity.com/bundle/p14c/page/als1564020488261.html) platform. You can deploy ASE on-premise in either inline or sideband mode and integrate it with [PingOne](https://docs.pingidentity.com/bundle/p14c/page/als1564020488261.html). This hybrid integration delivers API security through the new PingOne API Intelligence service.

### New PingIntelligence Docker Toolkit Environment Variables

New

The PingIntelligence Docker toolkit adds environment variables to support integration of ASE with the PingOne API Intelligence platform. For more information, see [PingIntelligence Docker toolkit](../installing_pingintelligence_for_apis/pingintelligence_docker_toolkit.html). The new environment variables support:

* Configuring gateway credentials to use for connecting ASE with the PingOne API Intelligence platform

* Setting the ABS AI engine deployment type to cloud or on-premise

## PingIntelligence 5.0 (June 2021)

PingIntelligence 5.0 provides the following enhancements:

### All PingIntelligence components now support a single unified license

New

PingIntelligence now supports up to 10 subpath levels for API base paths when API Security Enforcer (ASE) is deployed in sideband mode. Subpath depth is the number of sub-paths for a unique API definition. For more information, see [Discovery sub-paths](../managing_pingintelligence_for_apis/pingintelligence_discovery_subpaths.html).

### Dashboard Enhancements

New

The PingIntelligence Dashboard is enhanced to provide improved user experience for the following functionalities:

* The updated **Attack management** page gives a comprehensive view of Indicators of Attacks (IoAs) on a per client basis. A separate **Enable / Disable Attacks** page helps the administrators in efficient attack management. For more information, see [Indicators of Attacks on REST APIs](../pingintelligence_reference_guide/pingintelligence_indicators_of_attacks_rest_apis.html).

* The **Training Status** page now allows you to view the training status for an API by selecting the API from a drop-down list. The page also has a new capability to download per API and across API attack thresholds in a JSON formatted text file. For more information, see [Training period status](../managing_pingintelligence_for_apis/pingintelligence_training_period_status.html).

### ASE Updates

New

ASE has the following new additions:

* **External Load Balancer support for ASE to ABS AI Engine traffic -**ASE can be optionally configured to utilize external load balancers to distribute traffic across ABS AI Engine nodes. This provides the flexibility to support auto-scale of ABS AI Engine nodes and more high availability configurations.

* **REST API for sideband token management -**The `Token API` helps to create, import, and delete ASE sideband tokens. You can also retrieve the list of tokens issued by ASE.

* **REST API for sideband authentication -** The `Authentication API` helps to enable and disable ASE sideband authentication. You can also retrieve the authentication status. For more information, see [REST APIs for sideband token and authentication](../pingintelligence_reference_guide/pingintelligence_rest_api_for_sideband_authentication.html).

### New in sideband integration policies

Improved

* **NGINX plus policy -**The updated PingIntelligence sideband policy can seamlessly integrate with NGINX Plus R22 or R23 systems. This enhanced policy supports NGINX nodes with PingAccess agents installed and can capture user information from the PingAccess token introspection. For more information, see [Installing NGINX Plus for RHEL 7.6](../pingintelligence_integrations/pingintelligence_nginx_plus_install.html).

* **Apigee policy -**The updated PingIntelligence sideband policy adds optional asynchronous communication between Apigee and ASE for improved performance when deployed in environments that do not require automated client blocking. For more information, see [Apigee integration](../pingintelligence_integrations/pingintelligence_apigee_integration.html).

* **Kong policy -** The PingIntelligence sideband policy is enhanced to support extraction of user information from JWTs when OpenID Connect (OIDC) plugin is installed in a Kong gateway. For more information, see [Kong API gateway integration](../pingintelligence_integrations/pingintelligence_kong_integration.html).

### New in deployment tools

Improved

The following PingIntelligence deployment tools have been modified to support integration with PingOne:

* [PingIntelligence Ansible deployment framework](../installing_pingintelligence_for_apis/pingintelligence_automated_deployment.html)

* [PingIntelligence Docker PoC deployment](../installing_pingintelligence_for_apis/pingintelligence_docker_evaluation.html)

* [PingIntelligence Kubernetes deployment](../installing_pingintelligence_for_apis/pingintelligence_kubernetes_deployment.html)

* [PingIntelligence Docker toolkit](../installing_pingintelligence_for_apis/pingintelligence_docker_toolkit.html)

## Previous Releases

This page shows changes and updates to PingIntelligence for APIs.

* [PingIntelligence 4.4 (December 2020)](https://docs.pingidentity.com/bundle/pingintelligence-44/page/vmy1608344509701.html)

  * [PingIntelligence 4.4.1 (April 2021)](https://docs.pingidentity.com/bundle/pingintelligence-44/page/wzi1618467619364.html)

* [PingIntelligence 4.3](https://docs.pingidentity.com/bundle/pingintelligence-43/page/ehw1596783740016.html)

* [PingIntelligence 4.2](https://docs.pingidentity.com/bundle/pingintelligence-42/page/cxb1592908081245.html)

* [PingIntelligence 4.1](https://docs.pingidentity.com/bundle/pingintelligence-41/page/jty1574058854555.html)

  * [PingIntelligence 4.1.0](https://docs.pingidentity.com/bundle/pingintelligence-41/page/fms1582088964676.html)

  * [PingIntelligence 4.1.1](https://docs.pingidentity.com/bundle/pingintelligence-41/page/qmm1585822163289.html)