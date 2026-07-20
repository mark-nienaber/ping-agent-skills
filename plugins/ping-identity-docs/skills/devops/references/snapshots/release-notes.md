---
title: Version 2003
description: DevOps Docker build notes for version 2003 (March 2020), introducing the first PingDirectoryProxy, PingCentral, and PingToolkit Docker images
component: devops
page_id: devops::release-notes/relnotes-2003
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2003.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2003: DevOps Docker Builds, Version 2003
  devops-new-features: New Features
  devops-resolved-defects: Resolved Defects
  devops-changed: Changed
  devops-qualified: Qualified
---

# Version 2003

## DevOps Docker Builds, Version 2003

### New Features

* **PingDirectoryProxy**

  The PingDirectoryProxy Docker image is now available. See the Ping Identity [Docker Hub](https://hub.docker.com/r/pingidentity/pingdirectoryproxy)

* **PingCentral**

  The PingCentral Docker image is now available. See the Ping Identity [Docker Hub](https://hub.docker.com/r/pingidentity/pingcentral\))

* **Docker Compose Port Mappings**

  We now support the Docker Compose best practice of quoting all port mappings.

* **Docker Images (Tag: edge)**

  We've built a pipeline to support nightly public builds of all Ping Identity Docker images using the `edge` tag.

* **PingDirectory**

  We've upgraded the PingDirectory Docker image to the current product version 8.0.0.1.

* **PingFederate Version 10.1.0**

  We've built a beta PingFederate 10.1.0 Docker image.

* **PingAccess Version 6.1.0**

  We've built a beta PingAccess 6.1.0 Docker image.

* **Ping Tool Kit**

  The Ping Tool Kit Docker image is now available. See Ping Identity [Docker Hub](https://hub.docker.com/r/pingidentity/pingtoolkit). Both `kubectl` and `kustomize` are supported in the image.

* **PingFederate Version 9.3**

  We've updated the PingFederate 9.3 Docker image to include the latest product patches.

* **The ping-devops Utility**

  We've added Kubernetes license secret generation, and server profile generation for PingDirectory to the ping-devops utility. See [The pingctl Utility](../tools/pingctlUtil.html).

* **A New Hook**

  We've added a security start-up hook notifying administrators of keys and secrets found in the server profile.

* **DevOps Evaluation License**

  We've added retry functionality to attempt getting the DevOps evaluation license if the initial request fails.

* **Product Artifacts and Extensions**

  We've created operations to retrieve product artifacts and extensions using the DevOps credentials.

* **Java 11**

  We've migrated all Alpine-based Docker images to Java 11 (Azul).

* **PingDirectory Replication Timing**

  We've added a profile and reference example to test PingDirectory replication timing. See the pingidentity-devops-getting-started [Repo](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/20-kustomize/11-pingdirectory-replication-timing).

* **Docker Base Image Security**

  We've documented an evaluation of Docker base image security. See [Evaluation of Docker Base Image Security](../docker-images/dockerImageSecurity.html).

### Resolved Defects

* (GDO-85) Resolved an issue where PingAccess 6.0 loaded a 5.2 license.

* (GDO-87) Resolved an issue where Data Console wasn't allowing users to authenticate (edge tag).

* (GDO-124) Resolved an issue in with pipeline where starting containers using Docker-Compose timed out.

* (GDO-89) Resolved an issue where `*.subst` template files were able to overwrite the server profile configuration.

* (GDO-72) Resolved an issue where `motd.json` did not parse correctly when the product was missing.

* (GDO-88) Resolved an issue where PingFederate profile metadata did not expand `hostname`, breaking OAuth flows.

### Changed

* (GDO-97) Removed WebConsole HTTP servlet from the baseline server profile. See the pingidentity-server-profiles [repo](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/baseline).

### Qualified

* (GDO-42) Verified the ability to run our Docker containers as a non-root user. See [Securing the Containers](../how-to/secureContainers.html).

---

---
title: Version 2004
description: DevOps Docker build notes for version 2004 (April 2020), introducing the first PingCentral Docker image and PingDirectory replication support in Docker Compose
component: devops
page_id: devops::release-notes/relnotes-2004
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2004.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2004: DevOps Docker Builds, Version 2004
  devops-new-features: New Features
  devops-resolved-defects: Resolved Defects
---

# Version 2004

## DevOps Docker Builds, Version 2004

### New Features

* **PingCentral**

  The PingCentral Docker image is now available. See the [Ping Identity Docker hub](https://hub.docker.com/r/pingidentity/pingcentral).

* **Docker Compose**

  We've standardized our Docker Compose references.

* **Performance**

  We've built a performance framework.

* **PingFederate version 10.0.2**

  We've updated the PingFederate 10 Docker image for the 10.0.2 release.

* **The ping-devops utility**

  We've added major enhancements to our ping-devops utility. See [The ping-devops Utility](../tools/pingctlUtil.html).

* **PingDirectory replication**

  We've added support for PingDirectory replication using Docker Compose.

* **Variables and scope**

  We've added documentation to help with understanding the effective scope of variables. See [Variables and Scope](../reference/variableScoping.html).

## Resolved Defects

* (GDO-1) Resolved issue where users were unable to override root and admin user passwords (PingDirectory).

* (GDO-129) Removed the console from Ping Data products when the server profile isn't specified.

* (GDO-54) Resolved PingDataGovernance issues within the baseline server profile.

* (GDO-138) Resolved issue regarding PingDataGovernance Policy Administration Point (PAP) launch.

* (GDO-189) Resolved issue with PingAccess heartbeat check.

* (GDO-196) Replaced nslookup with getent due to issues running in Alpine.

* (GDO-180) Resolved issue where extension signature verification may return a false positive.

* (GDO-169) Resolved issues with Ping Data Console by upgrading to Tomcat 9.0.34.

* (GDO-166) Resolved issue with make-ldif template processing.

---

---
title: Version 2005
description: DevOps Docker Builds 2005 (May 2020) introduces the PingDelegator Docker image and updates PingAccess to version 6.0.2
component: devops
page_id: devops::release-notes/relnotes-2005
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2005.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2005: DevOps Docker Builds, Version 2005 (May 2020)
  devops-new-features: New Features
  devops-resolved-defects: Resolved Defects
---

# Version 2005

## DevOps Docker Builds, Version 2005 (May 2020)

### New Features

* **PingDelegator Docker Image**

  The PingDelegator Docker image is now available. View on [Docker Hub](https://hub.docker.com/r/pingidentity/pingdelegator) for more information.

  Test drive PingDelegator using the supplied docker-compose file in our [Simple-Stack](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/11-docker-compose/01-simple-stack) example.

* **PingAccess Image Version 6.0.2**

  We've updated the PingAccess Image to version 6.0.2.

* **PingFederate Version 9.3.3**

  We've updated the PingFederate 9.3.3 Docker image to include patch 4.

* **Docker Builds Pipeline**

  We've made a number of CI/CD enhancements to improve Image qualification (smoke/integration tests).

* **Image Enhancements**

  Improved the `wait-for` command to optionally wait for a path or file to become available.

### Resolved Defects

* (GDO-187) Resolved issue where MAX\_HEAP\_SIZE wasn't applied during container restart.

* (GDO-220) Resolved issue where log message didn't contain log file source name.

* (GDO-238) Resolved issue where ping-devops kubernetes start fails if DNS\_ZONE variable not set.

* (GDO-245) Resolved issue where PingAccess didn't exit when configuration import failed.

* (GDO-263) Resolved issue within deploy\_docs.sh which had resulted in some documentation to not be pushed to GitHub.

* (GDO-278) Resolved issue with PingAccess clustering Server Profile.

---

---
title: Version 2006
description: DevOps Docker Builds 2006 (June 2020) adds Docker Compose volume persistence and updates the PingAccess image for version 6.1
component: devops
page_id: devops::release-notes/relnotes-2006
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2006.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2006: DevOps Docker Builds, Version 2006 (June 2020)
  devops-new-features: New Features
  devops-new-product-versions: New Product Versions
  devops-improvements: Improvements
  devops-resolved-defects: Resolved Defects
---

# Version 2006

## DevOps Docker Builds, Version 2006 (June 2020)

### New Features

* **Docker Compose Volumes**

  Applications that create and manage configuration now have mounted volumes in Docker-Compose [Examples](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/11-docker-compose/), ensuring that your configuration changes are persisted across restarted.

* **PingAccess Image Enhancements**

  We've updated the PingAccess Image to support the new features available in version 6.1.

* **Customer Support Data Collection**

  Included in this release is the Java diagnostic tool to enable embedded customer support data collection. This tool set includes [jstat](https://docs.oracle.com/javase/7/docs/technotes/tools/share/jstat.html), [jmap](https://docs.oracle.com/javase/7/docs/technotes/tools/share/jmap.html) and [jhat](https://docs.oracle.com/javase/7/docs/technotes/tools/share/jhat.html).

### New Product Versions

The following new product versions are available using **edge**, **latest** and **2006** image tags:

* PingFederate 10.1.0

* PingAccess 6.1.0

* PingDirectory 8.1.0.0

* PingDirectoryProxy 8.1.0.0

* PingDataGovernance 8.1.0.0

* PingDataGovernance 8.1.0.0 PAP

* PingDataSync 8.1.0.0

* PingCentral 1.4.0

### Improvements

* **Liveness Check**

  We've made improvements to PingDirectory's liveness check to better inform dependant services on the status of the Directory service.

* **Docker Build Pipeline**

  * We've published [documentation](../how-to/buildLocal.html) on how to build a Ping Identity Docker Image using a local zip artifact.

  * We have improved our reference pipeline to allow for the build of a single product.

  * We've made several CI/CD enhancements to improve Image qualification (smoke/integration tests).

* **Configuration Substitution**

  We've made enhancements to explicitly send the variables to be substituted.

### Resolved Defects

* (GDO-218) Resolved an issue where PingDirectory threw an error on manage-profile during setup.

* (GDO-289) Resolved an issue where Alpine based image couldn't install pip3.

* (GDO-329) Resolved an issue where PingCentral docs were not syncing to GitHub.

---

---
title: Version 2007
description: Lists DevOps Docker Builds version 2007 (July 2020), introducing Docker Content Trust image signing and pre- and post-hook startup customization.
component: devops
page_id: devops::release-notes/relnotes-2007
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2007.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2007: DevOps Docker Builds, Version 2007 (July 2020)
  devops-new-features: New Features
  devops-improvements: Improvements
  devops-resolved-defects: Resolved Defects
---

# Version 2007

## DevOps Docker Builds, Version 2007 (July 2020)

### New Features

* **Signed Docker Images**

  All DockerHub Images are now signed and conform to the Docker Content Trust [specification](https://docs.docker.com/engine/security/trust/content_trust/).

* **Variablize PingAccess Ports**

  We've updated the PingAccess start up hooks to allow users to customize application ports.

* **PingAccess Upgrade Utility**

  The PingAccess upgrade utility is now part of Docker Image.

* **Certificate Management**

  Add consistency and flexibility with the injection of certs/pins.

* **Docker Image Startup Flexibility**

  We've added the ability for end users to customize the startup sequence for Docker Images using **pre** and **post** hooks. See [Using DevOps Hooks](../reference/hooks.html) for implementation details.

### Improvements

* **Docker Build Pipeline**

  We've made several CI/CD enhancements to improve Image qualification (smoke/integration tests).

### Resolved Defects

* (GDO-345) Resolved issue where PingDelegator was using PRIVATE rather than PUBLIC hostnames.

* (GDO-346) Resolved issue regarding the default minimum heap for PingDirectory.

* (GDO-380) Resolved issue within PingAccess Clustering (Admin Console) Kubernetes examples.

* (GDO-371) Resolved issue where PingDelegator wouldn't start using non-privileged user.

---

---
title: Version 2008
description: DevOps Docker Builds 2008 (August 2020) adds native secret management and self-service DevOps program registration
component: devops
page_id: devops::release-notes/relnotes-2008
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2008.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2008: DevOps Docker Builds, Version 2008 (August 2020)
  devops-new-features: New Features
  devops-improvements: Improvements
  devops-resolved-defects: Resolved Defects
---

# Version 2008

## DevOps Docker Builds, Version 2008 (August 2020)

### New Features

* **Secret Management**

  A number of key enhancements have been made to natively support secret management within our Docker Images. See [Using Hashicorp Vault](../how-to/usingVault.html) for implementation details.

* **DevOps Development Mode**

  We've added a 'Continue on Failure' option to all Docker Images. This allows the Container to say alive while any potential issues are being investigated.

* **DevOps Program Registration**

  Signing up for the Ping DevOps program is now self-service! Simply follow the instructions found in [Ping Identity DevOps Registration](../how-to/devopsRegistration.html).

### Improvements

* **Ping-DevOps Utility**

  We've added secret management commands to ping-devops, allowing you to quickly integrate secrets into your deployments.

* **Image Restart State**

  A number of enhancements have been made to improve the overall restart flow in our Docker Images.

### Resolved Defects

* (GDO-352) Resolved restart issue in PingDataGovernance PAP.

* (GDO-392) Resolved issue within PingDelegator when DS\_PORT variable was undefined.

* (GDO-395) Resolved issue within PingDirectory restart when Java versions changed.

* (GDO-397) Resolved issue where PingFederate failed to start in Kubernetes using the full-stack example.

* (GDO-404) Resolved issue where some users were unable to log into the PingAccess console using the Image edge tag and Baseline server profile.

---

---
title: Version 2009
description: DevOps Docker Builds 2009 (September 2020) introduces PingDataSync clustering and releases PingAccess 6.1.2
component: devops
page_id: devops::release-notes/relnotes-2009
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2009.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2009: Devops Docker Builds, Version 2009 (September 2020)
  devops-new-features: New Features
  devops-pingaccess-release: PingAccess Release
  devops-product-betas-and-release-candidates: Product Betas and Release Candidates
  devops-improvements: Improvements
---

# Version 2009

## Devops Docker Builds, Version 2009 (September 2020)

### New Features

* **PingDataSync Clustering**

  Within PingDataSync 8.2.0.0-EA we've introduced clustering, ensuring your deployment is highly available.

* **Certificate Management Usage**

  We've added documentation for DevOps [Certificate Management](../reference/usingCertificates.html).

### PingAccess Release

PingAccess 6.1.2 is now available using **edge**, **latest** and **2009** image tags.

### Product Betas and Release Candidates

Looking to see what the next official product release will contain? Start using the beta and early access builds today.

* PingFederate 10.2.0-Beta

* PingAccess 6.2.0-Beta

* PingDirectory 8.2.0.0-EA

* PingDirectoryProxy 8.2.0.0-EA

* PingDataGovernance 8.2.0.0-EA

* PingDataGovernance 8.2.0.0-EA PAP

* PingDataSync 8.2.0.0-EA

### Improvements

* **Image Hardening**

  We've updated our Image hardening [Guide](../how-to/secureContainers.html) to help secure your production deployments.

---

---
title: Version 2010
description: DevOps Docker Builds 2010 (October 2020) introduces Ping Identity Helm charts and the PingIntelligence Docker image
component: devops
page_id: devops::release-notes/relnotes-2010
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2010.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2010: Devops Docker Builds, Version 2010 (October 2020)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
---

# Version 2010

## Devops Docker Builds, Version 2010 (October 2020)

### New Features

* **PingIdentity Helm Charts**

  Looking to deploy the PingDevOps stack into your Kubernetes cluster? We've published our [Helm Charts](https://helm.pingidentity.com) to help streamline deployment.

* **PingIntelligence (ASE) Docker Image**

  PingIntelligence (ASE) is now available on DockerHub! Pull the 4.3 ASE image [here](https://hub.docker.com/r/pingidentity/pingintelligence).

* **PingFederate Bulk API Configuration Management**

  We've added tooling and documentation for managing PingFederate configuration using the build API export and import. View the latest documentation [here](../how-to/buildPingFederateProfile.html).

### Enhancements

* **PingFederate**

  * Version 10.0.6 now available.

  * Image now includes tcp.xml.subst for cluster parameterization.

  * Updated image to support easier enablement/use of Bouncy Castle FIPS provider with PingFederate.

* **PingAccess**

  * Version 6.1.3 is now available.

* **LDAP SDK**

  * Updated to version 5.1.1.

* **ping-devops CLI**

  * Added functionality to generate K8s license and version secret directly from the evaluation license service.

  * Added ACCEPT\_EULA value to K8s devops-secret.

### Resolved Defects

* (GDO-411) Resolved issue where access token was logged when using private Git repository.

* (GDO-444) Resolved PingDirectory issue with keystore exception on restart.

* (GDO-491) Removed GPG from base Docker image.

* (GDO-495) Removed gosu from base Docker image.

* (GDO-513) Resolved issue with replication topology list on PingDirectory restart.

---

---
title: Version 2011
description: Lists DevOps Docker Builds version 2011 (November 2020), introducing automated CVE scanning of Docker images and PingFederate 10.1.3.
component: devops
page_id: devops::release-notes/relnotes-2011
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2011.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2011: Devops Docker Builds, Version 2011 (November 2020)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
---

# Version 2011

## Devops Docker Builds, Version 2011 (November 2020)

### New Features

* **Internal XRay Scanning**

  We've automated the process to scan all Sprint Release Docker Images for CVE's

## Enhancements

* **PingFederate**

  * Version 10.1.3 now available.

  * Parameterized run.properties, ldap.properties and tcp.xml now included in Docker Image.

* **Helm Charts**

  * We added a number of enhancements to our Helm charts. See the [Helm Release Notes](https://helm.pingidentity.com/release-notes/) for details.

* **Misc.**

  * Updated EULA check to be case insensitive

  * Add Java back into pingtoolkit Image

  * Updated example docker run commands in Dockerfile documentation

  * Info message when Server Profile URLs are not present

### Resolved Defects

* (GDO-549) - Resolved issue where SCIM Swagger test pages don't work in PingDataGovernance Docker Image

* (GDO-567) - Resolved issue where changes made to PingDirectory's java.properties were erased on container restart

* (GDO-599) - Change wait-for localhost to use IP address

* (GDO-604) - Modified simple-sync server profile to work in Kubernetes environment with different service names

* (GDO-606) - Resolved issue where copy of server bits throws errors when running under non-root security context

---

---
title: Version 2012
description: DevOps Docker build notes for version 2012 (December 2020), covering the move to MkDocs and updates to PingFederate 10.2 and PingDirectory 8.2.0
component: devops
page_id: devops::release-notes/relnotes-2012
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2012.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2012: Devops Docker Builds, Version 2012 (December 2020)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2012

## Devops Docker Builds, Version 2012 (December 2020)

### New Features

* **DevOps Documentation**

  We've moved from GitBook to MKDocs to provide a richer DevOps documentation experience.

### Enhancements

* **PingFederate**

  * Version 10.2 now available.

* **PingAccess**

  * Version 6.2 is now available.

* **PingDirectory**

  * Version 8.2.0 is now available.

* **PingDataGovernance**

  * Version 8.2.0 is now available.

* **PingDataSync**

  * Version 8.2.0 is now available.

* **PingCentral**

  * Version 1.6.0 is now available.

* **LDAP SDK**

  * Version 5.1.3 is now available.

  * Updated to latest Tomcat version.

* **PingData Console SSO Example**

  * We've provided an example of running the Admin Console in Docker with SSO configured.

### Resolved Defects

* (GDO-362) Resolved issue where PingDirectory instances become active prior to being fully synchronized.

* (GDO-502) Resolved potential vulnerability by updating Ping Data products to Spring Framework v4.3.29.

* (GDO-544) Resolved issue where PingDataGovernance PAP images' MAX\_HEAP\_SIZE variable had no effect.

* (GDO-618) Resolved issue where base layer was missing JMX agent.

* (GDO-640) Resolved issue where wait-for command didn't honor timeout when waiting for host:port.

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| **Product**            | **Active Build**    | **Build EOL** |
| ---------------------- | ------------------- | ------------- |
| PingAccess             | **6.2.0** 6.1.3     | 6.0.4         |
| PingCentral            | **1.6.0** 1.5.0     |               |
| PingDataConsole        | **8.2.0.0** 8.1.0.0 | 8.0.0.1       |
| PingDataGovernance     | **8.2.0.0** 8.1.0.0 | 8.0.0.1       |
| PingDataGovernance PAP | **8.2.0.0** 8.1.0.0 | 8.0.0.1       |
| PingDataSync           | **8.2.0.0** 8.1.0.0 | 8.0.0.1       |
| PingDelegator          | **4.4.0**           | 4.2.1         |
| PingDirectory          | **8.2.0.0** 8.1.0.0 | 8.0.0.1       |
| PingDirectoryProxy     | **8.2.0.0** 8.1.0.0 | 8.0.0.1       |
| PingFederate           | 10.2.0 **10.1.3**   | 10.1.2        |
| PingIntelligence       | **4.4**             | 4.3           |

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The **bold** product version number is the version within the 'latest' image tag.

* The build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2101
description: DevOps Docker Builds 2101 (January 2021) updates PingFederate, PingDirectory, PingDataGovernance, and PingDelegator 4.4.1
component: devops
page_id: devops::release-notes/relnotes-2101
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2101.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2101: Devops Docker Builds, Version 2101 (January 2021)
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2101

## Devops Docker Builds, Version 2101 (January 2021)

### Enhancements

* **PingFederate**

  * Versions 10.2.1 and 10.1.4 are now available.

* **PingDirectory**

  * Versions 8.2.0.1 and 8.1.0.3 are now available.

  * PingDirectory now delays its readiness state until replication has completed (Kubernetes).

  * Improved container restart time by regenerating java.properties only when changes are made to JVM or JVM options.

* **PingDataGovernance**

  * Versions 8.2.0.1 and 8.1.0.3 are now available.

* **PingDataSync**

  * Versions 8.2.0.1 and 8.1.0.3 are now available.

* **PingDelegator 4.4.1**

  * Version 4.4.1 is now available.

* **LDAP SDK**

  * Version 5.1.3 is now available.

* **Container Secrets**

  * Sourcing of secret\_envs is now recursive.

### Resolved Defects

* (GDO-577) - Resolved issue to suppress environment variables in cn=monitor for PingData products.

* (GDO-658) - Enhanced error messages returned by the evaluation license service.

* (GDO-659) - Resolved issue where evaluation license server used incorrect calculation for checking image expiration.

* (GDO-668) - Resolved issue where remnants of previous server profile remained in place when restarting a container.

* (GDO-674) - Resolved issue where hashing contents of the SECRETS\_DIR risked leaving passwords stored insecurely on the container filesystem.

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| Product                | Active Build        | Build EOL       |
| ---------------------- | ------------------- | --------------- |
| PingAccess             | **6.2.0** 6.1.3     |                 |
| PingCentral            | **1.6.0** 1.5.0     |                 |
| PingDataConsole        | **8.2.0.1** 8.1.0.3 | 8.2.0.0 8.1.0.0 |
| PingDataGovernance     | **8.2.0.1** 8.1.0.3 | 8.2.0.0 8.1.0.0 |
| PingDataGovernance PAP | **8.2.0.1** 8.1.0.3 | 8.2.0.0 8.1.0.0 |
| PingDataSync           | **8.2.0.1** 8.1.0.3 | 8.2.0.0 8.1.0.0 |
| PingDelegator          | **4.4.0**           | 4.2.1           |
| PingDirectory          | **8.2.0.1** 8.1.0.3 | 8.2.0.0 8.1.0.0 |
| PingDirectoryProxy     | **8.2.0.1** 8.1.0.3 | 8.2.0.0 8.1.0.0 |
| PingFederate           | **10.2.1** 10.1.4   | 10.2.0 10.1.3   |
| PingIntelligence       | **4.4**             |                 |

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * **Bolded** product version number is version within 'latest' image tag.

* Build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2102
description: DevOps Docker Builds 2102 (February 2021) adds PingDirectory replication and restart fixes plus Helm charts for the PingDataGovernance policy editor
component: devops
page_id: devops::release-notes/relnotes-2102
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2102.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2102: DevOps Docker Builds, Version 2102 (February 2021)
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2102

## DevOps Docker Builds, Version 2102 (February 2021)

### Enhancements

* **PingFederate**

  * Support for creation and loading of certificates for admin.

  * Version 10.2.2 is now available.

* **PingAccess**

  * Baseline now has clustering support.

  * Version 6.1.4 is now available.

* **PingDirectory**

  * Improve speed of replace-profile process during PingDirectory restart.

  * Indexes are automatically rebuilt upon server restart.

  * Version 8.2.0.2 is now available.

* **PingDataGovernance**

  * Helm charts have been added for the PingDataGovernance policy editor.

  * Version 8.2.0.2 is now available.

* **PingDataSync**

  * Version 8.2.0.2 is now available.

### Resolved Defects

* (GDO-382) - Resolved issue where PingDirectory is unable to restart when upgrading 7.3 to 8.1 due to a license error.

* (GDO-543) - Updated "Related Docker Images" documentation in PAP Dockerfile.

* (GDO-672) - Resolved issue with 'manage-profile setup' signaling a dsconfig error.

* (GDO-680) - Resolved issue with PingDirectory set\_server\_available and set\_server\_unavailable methods being very.

* (GDO-311) - Updated 05-expand-templates.sh to no longer build data.zip if a *data.zip* directory is found in the profile.

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| **Product**            | **Active Build**    | **Build EOL** |
| ---------------------- | ------------------- | ------------- |
| PingAccess             | **6.2.0** 6.1.4     | 6.1.3         |
| PingCentral            | **1.6.0** 1.5.0     |               |
| PingDataConsole        | **8.2.0.2** 8.1.0.3 | 8.2.0.1       |
| PingDataGovernance     | **8.2.0.2** 8.1.0.3 | 8.2.0.1       |
| PingDataGovernance PAP | **8.2.0.2** 8.1.0.3 | 8.2.0.1       |
| PingDataSync           | **8.2.0.2** 8.1.0.3 | 8.2.0.1       |
| PingDelegator          | **4.4.0**           | 4.2.1         |
| PingDirectory          | **8.2.0.2** 8.1.0.3 | 8.2.0.1       |
| PingDirectoryProxy     | **8.2.0.2** 8.1.0.3 | 8.2.0.1       |
| PingFederate           | 10.2.2 **10.1.4**   | 10.2.1        |
| PingIntelligence       | **4.4**             |               |

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * **Bolded** product version number is version within 'latest' image tag.

* Build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2103
description: Lists DevOps Docker Builds version 2103 (March 2021), announcing a critical change to run Docker images as a non-privileged user by default.
component: devops
page_id: devops::release-notes/relnotes-2103
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2103.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2103: DevOps Docker Builds, Version 2103 (March 2021)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2103

## DevOps Docker Builds, Version 2103 (March 2021)

### New Features

* **Images run as non-privileged user by default**

  *Critical:* We've greatly improved the security of our images by having them run as a non-privileged user by default. See [Migrating from privileged images to unprivileged-by-default images](../how-to/migratingRootToUnprivileged.html) for information about migrating existing deployments.

* **Layer simplification**

  We've consolidated layers in our images where possible.

### Enhancements

* **PingFederate**

  * The baseline image now uses data.json instead of the former use of the /data folder.

  * New variables have been added to run.properties for controlling provisioning failover and grace period.

  * Versions 10.1.5 and 10.3-Beta are now available.

* **PingAccess**

  * Versions 6.2.1 and 6.3-Beta are now available.

* **PingCentral**

  * Versions 1.7.0 is now available.

* **PingDirectory**

  * The number of layers present in the image has been reduced and simplified.

  * Version 8.2.0.3 is now available.

* **PingDataGovernance**

  * Version 8.2.0.3 is now available.

* **PingDataSync**

  * Version 8.2.0.3 is now available.

### Resolved Defects

* (GDO-742) - Resolved issue which may cause permissions errors creating files under /run/secrets during PingDirectory setup

* (GDO-746) - Resolved issue in which PingDirectory cannot rejoin its replication topology after restart

* (GDO-749) - Addressed documentation issue in which bulleted lists are not printed correctly

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| **Product**            | **Active Build**    | **Build EOL** |
| ---------------------- | ------------------- | ------------- |
| PingAccess             | **6.2.1** 6.1.4     | 6.2.0         |
| PingCentral            | **1.7.0** 1.6.0     | 1.5.0         |
| PingDataConsole        | **8.2.0.3** 8.1.0.3 | 8.2.0.2       |
| PingDataGovernance     | **8.2.0.3** 8.1.0.3 | 8.2.0.2       |
| PingDataGovernance PAP | **8.2.0.3** 8.1.0.3 | 8.2.0.2       |
| PingDataSync           | **8.2.0.3** 8.1.0.3 | 8.2.0.2       |
| PingDelegator          | **4.4.0**           | 4.2.1         |
| PingDirectory          | **8.2.0.3** 8.1.0.3 | 8.2.0.2       |
| PingDirectoryProxy     | **8.2.0.3** 8.1.0.3 | 8.2.0.2       |
| PingFederate           | 10.2.2 **10.1.5**   | 10.1.4        |
| PingIntelligence       | **4.4**             |               |

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * **Bolded** product version number is version within 'latest' image tag.

* Build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2104
description: Lists DevOps Docker Builds version 2104 (April 2021), introducing early access and beta images for PingAccess, PingFederate, and PingAuthorize.
component: devops
page_id: devops::release-notes/relnotes-2104
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2104.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-docker-builds-version-2104-april-2021: DevOps Docker Builds, Version 2104 (April 2021)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2104

## DevOps Docker Builds, Version 2104 (April 2021)

### New Features

* **Early Access and Beta Release Docker Images**

  * PingAccess 6.3.0-Beta

  * PingAuthorize 8.3.0.0-EA

  * PingAuthorize PAP 8.3.0.0-EA

  * PingDataConsole 8.3.0.0-EA

  * PingDataSync 8.3.0.0-EA

  * PingDirectory 8.3.0.0-EA

  * PingDirectoryProxy 8.3.0.0-EA

  * PingFederate 10.3.0-Beta

### Enhancements

* **`watch-fs-changes`**

  We've updated the `watch-fs-changes` utility to accept command-line parameters to watch additional locations.

* **Startup Time Performance**

  We've updated the start-server.sh script to improve container start up times for all PingData products.

* **Helm Charts for PingDirectoryProxy**

  PingDirectoryProxy has been integrated into Ping's [Helm Charts](https://helm.pingidentity.com).

### Resolved Defects

* (GDO-649) - Resolved issue where the provided self-signed certificates for PingDataConsole didn't function in Chrome on MacOS

* (GDO-770) - Resolved issue where PingDataConsole didn't log console messages by default

* (GDO-773) - Resolved issue where the collect-support-data tool couldn't find the required JDK

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| Product                | Active Build        | Build EOL |
| ---------------------- | ------------------- | --------- |
| PingAccess             | **6.2.1** 6.1.4     |           |
| PingCentral            | **1.7.0** 1.6.0     |           |
| PingDataConsole        | **8.2.0.3** 8.1.0.3 |           |
| PingDataGovernance     | **8.2.0.3** 8.1.0.3 |           |
| PingDataGovernance PAP | **8.2.0.3** 8.1.0.3 |           |
| PingDataSync           | **8.2.0.3** 8.1.0.3 |           |
| PingDelegator          | **4.4.0**           |           |
| PingDirectory          | **8.2.0.3** 8.1.0.3 |           |
| PingDirectoryProxy     | **8.2.0.3** 8.1.0.3 |           |
| PingFederate           | **10.2.2** 10.1.5   |           |
| PingIntelligence       | **4.4**             |           |

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * **Bolded** product version number is version within 'latest' image tag.

* Build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2105
description: Lists DevOps Docker Builds version 2105 (June 2021), featuring new PingFederate 10.2.3 and PingDelegator 4.5.0 releases and OAuth API fixes.
component: devops
page_id: devops::release-notes/relnotes-2105
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2105.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2105-june-3-2021: DevOps Docker Builds, Version 2105 (June 3 2021)
  devops-new-features: New Features
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2105

## DevOps Docker Builds, Version 2105 (June 3 2021)

### New Features

* **PingFederate**

  * PingFederate 10.2.3 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingfederate)

* **PingDelegator**

  * PingDelegator 4.5.0 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingdelegator)

### Resolved Defects

* (GDO-813) - Resolved issue where OAuth APIS were broken using baseline server profile and pingfederate:edge

* (GDO-818) - Resolved issue where users were unable to build images locally due to a file permission error

* (GDO-829) - Resolved issue where a `dsconfig` command was unable to run due to a quoting error

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| Product                | Active Build                           | Build EOL |
| ---------------------- | -------------------------------------- | --------- |
| PingAccess             | 6.3.0-Beta **6.2.1** 6.1.4             |           |
| PingCentral            | **1.7.0** 1.6.0                        |           |
| PingDataConsole        | 8.3.0.0-EA **8.2.0.3** 8.1.0.3         |           |
| PingDataGovernance     | **8.2.0.3** 8.1.0.3                    |           |
| PingDataGovernance PAP | **8.2.0.3** 8.1.0.3                    |           |
| PingDataSync           | 8.3.0.0-EA **8.2.0.3** 8.1.0.3         |           |
| PingDelegator          | **4.5.0** 4.4.1 4.2.1                  |           |
| PingDirectory          | 8.3.0.0-EA 8.2.0.4 **8.2.0.3** 8.1.0.3 |           |
| PingDirectoryProxy     | 8.3.0.0-EA **8.2.0.3** 8.1.0.3         |           |
| PingFederate           | 10.3.0-Beta **10.2.3** 10.1.5          | 10.2.2    |
| PingIntelligence       | **4.4**                                |           |

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * **Bolded** product version number is version within 'latest' image tag.

* Build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2106
description: Release notes for DevOps Docker Builds 2106 (July 2021), introducing experimental ARM-based Docker images and updates across several Ping products
component: devops
page_id: devops::release-notes/relnotes-2106
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2106.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2106-july-6-2021: DevOps Docker Builds, Version 2106 (July 6 2021)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2106

## DevOps Docker Builds, Version 2106 (July 6 2021)

### New Features

* **ARM-Based Images**

  * Ping Identity now offers ARM-based Docker images!

  * These images are currently experimental and are **not intended for production deployment**

  * View the available tags on [Dockerhub](https://hub.docker.com/r/pingidentity/)

* **PingFederate**

  * PingFederate 10.3.0 and 10.2.4 are now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingfederate)

* **PingAccess**

  * PingAccess 6.3.0 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingaccess)

* **PingDirectory**

  * PingDirectory 8.3.0 and 8.2.0.5 are now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingdirectory)

* **PingAuthorize**

  * PingAuthorize 8.3.0 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingauthorize)

* **PingCentral**

  * PingCentral 1.8 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingcentral)

* **PingDelegator**

  * PingDelegator 4.6.0 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingdelegator)

* **PingIntelligence (ASE)**

  * PingIntelligence 5.0 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingintelligence)

* **LDAP SDK**

  * LDAP SDK 6.0.0 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/ldap-sdk-tools)

### Enhancements

* **PingFederate** - Allow logging level to be set via an environment variable (PF\_LOG\_LEVEL) - Added property `pf.admin.baseurl` to run.properties configuration file - Added ability to generate the run.properties and jvm-memory.options files based on supplied environment variables

* **HEAP Awareness** - All Ping Identity Docker images can now calculate the heap based on the memory allocated to the container

* **Java Tools** - Added jcmd, jstat, jinfo, jmap, jps, jstack tools to images

* **Docker-Compose** - Added tmpfs secrets directory to all of the docker-compose examples in the [Getting-Started](https://github.com/pingidentity/pingidentity-devops-getting-started) repository

### Resolved Defects

* (GDO-657) - Resolved PingDelegator self-signed certificate issue

* (GDO-834) - Resolved issue where PingDataConsole doesn't build correctly when providing a local product.zip file

* (GDO-836) - Resolved issue where PingDirectory restart failed due to startup hook syntax error

* (GDO-885) - Resolved HTTPS/LDAPS port variables in PingAuthorize profiles to support Helm charts

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| Product                | Active Build        | Build EOL                  |
| ---------------------- | ------------------- | -------------------------- |
| PingAccess             | **6.3.0** 6.2.1     | 6.3.0-Beta 6.1.4           |
| PingAuthorize          | **8.3.0.0**         |                            |
| PingAuthorize PAP      | **8.3.0.0**         |                            |
| PingCentral            | **1.8.0** 1.7.0     | 1.6.0                      |
| PingDataConsole        | **8.3.0.0** 8.2.0.5 | 8.3.0.0-EA 8.2.0.3 8.1.0.3 |
| PingDataGovernance     | **8.2.0.5**         | 8.2.0.3 8.1.0.3            |
| PingDataGovernance PAP | **8.2.0.5**         | 8.2.0.3 8.1.0.3            |
| PingDataSync           | **8.3.0.0** 8.2.0.5 | 8.3.0.0-EA 8.2.0.3 8.1.0.3 |
| PingDelegator          | **4.6.0** 4.4.1     | 4.5.0 4.4.1 4.2.1          |
| PingDirectory          | **8.3.0.0** 8.2.0.5 | 8.3.0.0-EA 8.2.0.3 8.1.0.3 |
| PingDirectoryProxy     | **8.3.0.0** 8.2.0.5 | 8.3.0.0-EA 8.2.0.3 8.1.0.3 |
| PingFederate           | **10.3.0** 10.2.4   | 10.3.0-Beta 10.2.3 10.1.5  |
| PingIntelligence       | **5.0** 4.4.1       | 4.4                        |

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * **Bolded** product version number is version within 'latest' image tag.

* Build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2107
description: DevOps Docker build notes for version 2107 (August 2021), covering PingDirectory 8.3.0.1 and signed Docker images for all products
component: devops
page_id: devops::release-notes/relnotes-2107
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2107.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2107-august-4-2021: DevOps Docker Builds, Version 2107 (August 4 2021)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2107

## DevOps Docker Builds, Version 2107 (August 4 2021)

### New Features

* **PingFederate**

  * Added support for pf.admin.baseurl within baseline [Server Profile](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/baseline)

* **PingAccess**

  * PingAccess 6.2.2 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingaccess)

* **PingDirectory**

  * PingDirectory 8.3.0.1 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingdirectory)

* **PingDirectoryProxy**

  * PingDirectoryProxy 8.3.0.1 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingdirectoryproxy)

* **PingDataSync**

  * PingDirectory 8.3.0.1 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingdatasync)

* **PingAuthorize**

  * PingAuthorize 8.3.0.1 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingauthorize)

### Enhancements

* **PingDelegator** - Baseline now works on both local and Kubernetes environments

* **Helm Charts** - Release 0.6.8 - Probes & Ingress

### Resolved Defects

* (GDO-860) - Resolved issue where the PingAuthorize Policy Editor auto-generated documentation uses wrong ports

* (GDO-907) - Restored functionality for prepending the name of the log file to each log line

* (GDO-887) - All Docker images are now signed

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| Product                | Active Build        | Build EOL |
| ---------------------- | ------------------- | --------- |
| PingAccess             | **6.3.0** 6.2.2     | 6.2.1     |
| PingAuthorize          | **8.3.0.1**         | 8.3.0.0   |
| PingAuthorize PAP      | **8.3.0.1**         | 8.3.0.0   |
| PingCentral            | **1.8.0** 1.7.0     |           |
| PingDataConsole        | **8.3.0.1** 8.2.0.5 | 8.3.0.0   |
| PingDataGovernance     | **8.2.0.5**         |           |
| PingDataGovernance PAP | **8.2.0.5**         |           |
| PingDataSync           | **8.3.0.1** 8.2.0.5 | 8.3.0.0   |
| PingDelegator          | **4.6.0** 4.4.1     |           |
| PingDirectory          | **8.3.0.1** 8.2.0.5 | 8.3.0.0   |
| PingDirectoryProxy     | **8.3.0.1** 8.2.0.5 | 8.3.0.0   |
| PingFederate           | **10.3.0** 10.2.4   |           |
| PingIntelligence       | **5.0** 4.4.1       |           |

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * **Bolded** product version number is version within 'latest' image tag.

* Build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2108
description: Lists DevOps Docker Builds version 2108 (August 2021), featuring new PingFederate and PingAccess releases plus dark mode documentation support.
component: devops
page_id: devops::release-notes/relnotes-2108
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2108.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2108-august-27-2021: DevOps Docker Builds, Version 2108 (August 27 2021)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-product-build-matrix: Product Build Matrix
---

# Version 2108

## DevOps Docker Builds, Version 2108 (August 27 2021)

### New Features

* **PingFederate**

  * PingFederate 10.3.1 and 10.2.5 are now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingfederate)

* **PingAccess**

  * PingAccess 6.3.1 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingaccess)

### Enhancements

* **Documentation**

  * Our DevOps documentation now supports both light and dark modes. Toggle between the two by clicking the icon in the top navigation bar.

* **Docker Images**

  * Upgraded the Image OS from Alpine 3.13 to 3.14

* **Helm Charts**

  * View the detailed release notes for Ping's Helm Charts [here](https://helm.pingidentity.com/release-notes/currentRelease/)

    * Release 0.7.0 - ServiceAccount/Role/RoleBinding for testFramework

    * Release 0.7.1 - Public hostname/ports

    * Release 0.7.2 - PingFederate PF\_ADMIN\_PUBLIC\_BASEURL variable

    * Release 0.7.3 - Support full definition of initContainers attributes in testSteps and finalStep

    * Release 0.7.4 - Set initContainer settings from values.yaml instead of hard coded templates

### Resolved Defects

* (GDO-945) - Resolved issue where PingCentral was unable to communicate with PingAccess in the docker-compose full-stack [example](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/11-docker-compose/03-full-stack).

* (GDO-872) - Resolved issue in tooling when building images locally (`serial_build.sh`).

### Product Build Matrix

The following table includes product versions and their accompanying Image build status for this release.

| Product                | Active Build        | Build EOL     |
| ---------------------- | ------------------- | ------------- |
| PingAccess             | **6.3.1** 6.2.2     | 6.3.0         |
| PingAuthorize          | **8.3.0.1**         |               |
| PingAuthorize PAP      | **8.3.0.1**         |               |
| PingCentral            | **1.8.0** 1.7.0     |               |
| PingDataConsole        | **8.3.0.1** 8.2.0.5 |               |
| PingDataGovernance     | **8.2.0.5**         |               |
| PingDataGovernance PAP | **8.2.0.5**         |               |
| PingDataSync           | **8.3.0.1** 8.2.0.5 |               |
| PingDelegator          | **4.6.0** 4.4.1     |               |
| PingDirectory          | **8.3.0.1** 8.2.0.5 |               |
| PingDirectoryProxy     | **8.3.0.1** 8.2.0.5 |               |
| PingFederate           | **10.3.1** 10.2.5   | 10.3.0 10.2.4 |
| PingIntelligence       | **5.0** 4.4.1       |               |

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * **Bolded** product version number is version within 'latest' image tag.

* Build EOL denotes product versions that are no longer built as of this release. |

---

---
title: Version 2109
description: Summarize DevOps Docker Builds version 2109 release notes, including new PingFederate and PingAccess releases and a security advisory
component: devops
page_id: devops::release-notes/relnotes-2109
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2109.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2109-october-06-2021: DevOps Docker Builds, Version 2109 (October 06 2021)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-supported-product-releases: Supported Product Releases
---

# Version 2109

## DevOps Docker Builds, Version 2109 (October 06 2021)

|   |                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingFederate deployments prior to sprint release 2108 (Aug 27th, 2021) may be at risk. Please visit [here](https://support.pingidentity.com/s/article/SECADV028-PingFederate-XML-Processing-Bypass) for details on impacted and patched versions. |

### New Features

* **PingFederate**

  * PingFederate 10.3.2 and 11.0 Beta are now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingfederate)

* **PingAccess**

  * PingAccess 6.3.1 and 7.0 Beta are now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingaccess)

* **PingDirectory**

  * PingDirectory 8.3.0.2, 8.2.0.6, and 9.0 EA are now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingdirectory)

* **PingAuthorize**

  * PingAuthorize 8.3.0.2, 8.2.0.6, and 9.0 EA are now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingauthorize)

* **PingIntelligence**

  * PingIntelligence 5.0.1 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingintelligence)

### Enhancements

* **Documentation**

  * Improved [Introduction to Image/Container anatomy](../reference/config.html)

* **Docker Images**

  * JDK Liberica 11.0.12+7 is now supported

  * Images now include a startup probe script /opt/startup.sh

* **Helm Charts**

  * View the detailed release notes for Ping's Helm Charts [here](https://helm.pingidentity.com/release-notes)

    * Release 0.7.6 - Support for scheduler name on pods

* **Kubernetes**

  * PingDirectory now waits for its pod DNS hostname to match expected K8 pod IP

### Resolved Defects

* (GDO-896) - Resolved issue where PingDirectory failed to pick up the product license during deployment

* (GDO-989) - Resolved issue in which PingDirectory seed failure in multi-region topology causes a replication island

### Supported Product Releases

* See the [Product Version, Image Release Matrix](../docker-images/productVersionMatrix.html) for currently supported image and product versions.

---

---
title: Version 2110
description: DevOps Docker build notes for version 2110 (November 2021), covering PingDirectory 8.3.0.3 and required PingFederate LDAP credentials
component: devops
page_id: devops::release-notes/relnotes-2110
canonical_url: https://developer.pingidentity.com/devops/release-notes/relnotes-2110.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-devops-docker-builds-version-2110-november-01-2021: DevOps Docker Builds, Version 2110 (November 01 2021)
  devops-new-features: New Features
  devops-enhancements: Enhancements
  devops-resolved-defects: Resolved Defects
  devops-supported-product-releases: Supported Product Releases
---

# Version 2110

## DevOps Docker Builds, Version 2110 (November 01 2021)

### New Features

* **PingFederate**

  * PingFederate 10.3.3 and 10.2.7 are now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingfederate).

* **PingDirectory**

  * PingDirectory 8.3.0.3 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingdirectory).

* **PingAuthorize**

  * PingAuthorize 8.3.0.3 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingauthorize).

* **PingCentral**

  * PingCentral 1.9 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/pingcentral).

* **UnboundID LDAP SDK**

  * UnboundID LDAP SDK tool set 6.0.2 is now available on [Dockerhub](https://hub.docker.com/r/pingidentity/ldap-sdk-tools).

### Enhancements

* **Documentation**

  * Improved documenation around certificate rotation for PingDirectory.

  * Update DevOps support policy statement.

* **Docker Images**

  * Images that include Apache Tomcat have been updated to 9.0.54.

  * Startup time for PingDirectory has been improved.

  * PF\_LDAP\_USERNAME and PF\_LDAP\_PASSWORD variables are now required with PingFederate to promote best security practices.

* **Helm Charts**

  * View the detailed release notes for Ping's Helm Charts [here](https://helm.pingidentity.com/release-notes)

    * Release 0.7.7 - Update default security context group id to root.

    * Release 0.7.8 - Server profile updates, generate master password for Ping services.

### Resolved Defects

* (BRASS-72) - Resolved issue in which numbers were not rendered correctly in some cases in public docs.

* (BRASS-71) - Resolved issue in which PingDirectory seed name is not rendered correctly.

### Supported Product Releases

* See the [Product Version, Image Release Matrix](../docker-images/productVersionMatrix.html) for currently supported image and product versions.