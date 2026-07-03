---
title: Secure containers
description: Ping Government Identity Cloud Secure Containers are self-contained software packages that encapsulate Ping Identity software and relevant dependencies.
component: pgic
page_id: pgic::secure-containers
canonical_url: http://docs.pingidentity.com/pgic/secure-containers.html
revdate: August 15, 2025
section_ids:
  whats-included: What's included
  add-on-compatibility: Add-on compatibility
  middleware: Middleware
  security-and-maintenance: Security and maintenance
  secure-container-distribution: Secure container distribution
---

# Secure containers

Ping Government Identity Cloud Secure Containers are self-contained software packages that encapsulate Ping Identity software and relevant dependencies.

Secure containers protect against unauthorized access, tampering, and exploitation by leveraging isolation, encryption, and access control. Secure containers minimize attack surface and help protect sensitive data, application functionality, and underlying infrastructure.

## What's included

Secure containers are available for the following products:

* [PingAM (Access Management)](http://docs.pingidentity.com/pingam/)

* [PingDS (Directory Services)](http://docs.pingidentity.com/pingds/)

* [PingGateway (Identity Gateway)](http://docs.pingidentity.com/pinggateway/)

* [PingIDM (Identity Management)](http://docs.pingidentity.com/pingidm/)

* [Identity Governance](http://docs.pingidentity.com/identity-governance/)

* [PingFederate](http://docs.pingidentity.com/pingfederate/)

* [PingDirectory](http://docs.pingidentity.com/pingdirectory)

* [PingAccess](http://docs.pingidentity.com/pingaccess/)

* [PingCentral](http://docs.pingidentity.com/pingcentral/)

* [PingAuthorize](http://docs.pingidentity.com/pingauthorize/)

## Add-on compatibility

The following add-ons are not guaranteed to work with secure containers:

* Kits

* Marketplace nodes

* Marketplace connectors

## Middleware

Secure containers run on the following middleware:

|                      |                                             |
| -------------------- | ------------------------------------------- |
| All container images | RedHat UBI                                  |
| PingAM               | Tomcat; JDK                                 |
| PingDS               | JDK                                         |
| PingGateway          | JDK                                         |
| PingIDM              | JDK                                         |
| Platform UI          | NGINX; JDK                                  |
| PingFederate         | GETTEXT; JQ; OPENJDK; OPENJDK-DEVEL         |
| PingDirectory        | GETTEXT; JQ; OPENJDK; OPENJDK-DEVEL; Tomcat |
| PingAM               | GETTEXT; JQ; OPENJDK; OPENJDK-DEVEL         |
| PingCentral          | GETTEXT; JQ; OPENJDK; OPENJDK-DEVEL         |
| PingAuthorize        | GETTEXT; JQ; OPENJDK; OPENJDK-DEVEL         |

## Security and maintenance

Secure containers are updated monthly to include the latest versions of container-ready base images, products, and middleware.

1. A secure container is created and undergoes a comprehensive vulnerability scan.

2. Any identified vulnerabilities are triaged and documented if they cannot be immediately resolved.

3. The container image and its corresponding vulnerability documentation are published and available to users.

## Secure container distribution

Secure containers are distributed as Docker images.

The following links provide background, context, and details:

* [Container Docker images information](https://developer.pingidentity.com/devops/docker-images/dockerImagesRef.html)

* [Accessing Ping Identity secure containers](https://backstage.pingidentity.com/knowledge/backstagehelp/article/a46417859) (sign-on required)

* [Docker image hardening guide](https://support.pingidentity.com/s/article/Docker-Image-Hardening-Deployment-Guide) (sign-on required)

* Ping Identity [security hardening guides](https://support.pingidentity.com/s/article/Security-Hardening-Guides) (sign-on required)
