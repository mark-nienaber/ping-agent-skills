---
title: Environments
description: With Ping Government Identity Cloud, you have one production environment and one non-production environment that you can use to develop and test your code and configurations. You can also add up to three additional environments if you need them.
component: pgic
page_id: pgic:environments:pgic_environments
canonical_url: http://docs.pingidentity.com/pgic/environments/pgic_environments.html
revdate: December 15, 2025
section_ids:
  prod: Production environment
  non-prod: Non-production environments
  development-environments-dev: Development Environments (Dev)
  testing-test: Testing (Test)
  staging-stage: Staging (Stage)
---

# Environments

With Ping Government Identity Cloud, you have one production environment and one non-production environment that you can use to develop and test your code and configurations. You can also add up to three additional environments if you need them.

Items of note include:

* Automation is used to build and deploy Ping Government Identity Cloud into AWS GovCloud so that all environments follow the same generic footprint.

* Auto-scaling is set according to the environment size required.

* Ping Government Identity Cloud comes with a number of URLs to access different services, such as PingFederate and PingAccess runtime endpoints. Don't use these URLs for users accessing your production environment. Instead, work with our Professional Services team to define the requirements and naming conventions that you'll use for your environments.

## Production environment

The production environment (Prod) is where the latest versions of software, products, or updates are pushed live to their intended users.

With Ping Government Identity Cloud, the production environment:

* Is built to support the predicted load for each customer, based on their licensed identity count.

* Is subject to Ping Identity's uptime and Severity 1 and 2 service-level agreement.

* Can't be used for performance or load testing.

With multiregion deployments, production environments use active-active clustering configurations to achieve load balancing.

## Non-production environments

Non-production environments provide you with a way to develop and test your code and configurations using smaller sets of representative data, and then perform final testing and load testing in accordance with Ping Identity's load testing policies. Development and testing environments can't be revised after they're created and remain static throughout their existence.

### Development Environments (Dev)

Each Ping Government Identity Cloud deployment includes one development environment by default. Development environments are used to create and test code without interfering with the content on live sites.

Keep the following in mind:

* These environments don't scale and are always deployed in a single-region model.

* These environments shouldn't be used for performance or load testing and aren't subject to Ping Identity's uptime and Severity 1 and 2 service-level agreements.

### Testing (Test)

Testing environments are replicas of the development environments and are optional add-ons with Ping Government Identity Cloud. Testing environments are used to quality-check applications and perform user acceptance testing.

These environments shouldn't be used for performance or load testing and aren't subject to Ping Identity's uptime and Severity 1 and 2 service-level agreements.

Keep the following in mind:

* These environments don't scale and are always deployed in a single-region model.

* These environments shouldn't be used for performance or load testing and aren't subject to Ping Identity's uptime and Severity 1 and 2 service-level agreements.

### Staging (Stage)

Staging environments are replicas of the production environment and are optional add-ons with Ping Government Identity Cloud. They can be used for performance and load testing (with prior written consent), and for final testing before changes are released to the live site. These environments aren't subject to Ping Identity's uptime and Severity 1 and 2 service-level agreements.

Keep the following in mind:

* Indirect penetration testing and load testing are permitted as part of a wider test of your own infrastructure and applications.

* Denial-of-service (DoS) or distributed denial-of-service (DDoS) attacks aren't permitted.

* Load testing is only permitted up to your license volume limits.

* Penetration testing and load testing is only permitted with Ping Identity's prior written consent, an approved test plan, and at least 2 weeks' notice.
