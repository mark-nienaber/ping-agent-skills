---
title: Assess your skill level
description: I can:
component: forgeops
version: 2026.2
page_id: forgeops:start:start-here-skills
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/start/start-here-skills.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Kubernetes", "Docker", "CI/CD", "Git", "Google Cloud", "AWS", "Azure", "Certificates", "SSL/TLS", "Load Testing", "Backup &amp; Restore"]
section_ids:
  skills-benchmarking: Benchmarking and load testing
  skills-cicd: CI/CD for cloud deployments
  skills-docker: Docker
  skills-git: Git
  skills-integration: External application and database integration
  skills-platform: Ping Advanced Identity Software
  skills-cdm-cloud-provider: Google Cloud, AWS, or Azure (basic)
  skills-prod-cloud-provider: Google Cloud, AWS, or Azure (expert)
  skills-integration-test: Integration testing
  skills-cdk-kubernetes: Kubernetes (basic)
  skills-prod-kubernetes: Kubernetes (expert)
  skills-kubernetes-backup: Kubernetes backup and restore
  skills-proj-plan: Project planning and management for cloud deployments
  skills-security: Security and hardening for cloud deployments
  skills-sr: Site reliability engineering for cloud deployments
---

# Assess your skill level

## Benchmarking and load testing

I can:

* Write performance tests, using tools such as Gatling and Apache JMeter, to ensure that the system meets required performance thresholds and service level agreements (SLAs).

* Resize a Kubernetes cluster, taking into account performance test results, thresholds, and SLAs.

* Run Linux performance monitoring utilities, such as top.

## CI/CD for cloud deployments

I have experience:

* Designing and implementing a CI/CD process for a cloud-based deployment running in production.

* Using a cloud CI/CD tool, such as Tekton, Google Cloud Build, Codefresh, AWS CloudFormation, or Jenkins, to implement a CI/CD process for a cloud-based deployment running in production.

* Integrating GitOps into a CI/CD process.

## Docker

I know how to:

* Write Dockerfiles.

* Create Docker images, and push them to a private Docker registry.

* Pull and run images from a private Docker registry.

I understand:

* The concepts of Docker layers, and building images based on other Docker images using the FROM instruction.

* The difference between the COPY and ADD instructions in a Dockerfile.

## Git

I know how to:

* Use a Git repository collaboration framework, such as GitHub, GitLab, or Bitbucket Server.

* Perform common Git operations, such as cloning and forking repositories, branching, committing changes, submitting pull requests, merging, viewing logs, and so forth.

## External application and database integration

I have expertise in:

* AM policy agents.

* Configuring AM policies.

* Synchronizing and reconciling identity data using IDM.

* Managing cloud databases.

* Connecting Ping Advanced Identity Software components to cloud databases.

## Ping Advanced Identity Software

I have:

* Attended Ping Identity University training courses.

* Deployed the Ping Advanced Identity Software in production, and kept the deployment highly available.

* Configured DS replication.

* Passed the Certified Access and Identity Management exams from Ping Identity (highly recommended).

## Google Cloud, AWS, or Azure (basic)

I can:

* Use the graphical user interface for Google Cloud, AWS, or Azure to navigate, browse, create, and remove Kubernetes clusters.

* Use the cloud provider's tools to monitor a Kubernetes cluster.

* Use the command user interface for Google Cloud, AWS, or Azure.

* Administer cloud storage.

## Google Cloud, AWS, or Azure (expert)

In addition to the [basic skills for Google Cloud, AWS, or Azure](#skills-cdm-cloud-provider), I can

* Review Terraform artifacts in the `forgeops-extras` repository to see how clusters that support ForgeOps deployments are configured.

* Create and manage a Kubernetes cluster using an infrastructure-as-code tool such as Terraform, AWS CloudFormation, or Pulumi.

* Configure multi-zone and multi-region Kubernetes clusters.

* Configure cloud-provider identity and access management (IAM).

* Configure virtual private clouds (VPCs) and VPC networking.

* Manage keys in the cloud using a service such as Google Key Management Service (KMS), Amazon KMS, or Azure Key Vault.

* Configure and manage DNS domains on Google Cloud, AWS, or Azure.

* Troubleshoot a deployment running in the cloud using the cloud provider's tools, such as Google Stackdriver, Amazon CloudWatch, or Azure Monitor.

* Integrate a deployment with certificate management tools, such as cert-manager and Let's Encrypt.

* Integrate a deployment with monitoring and alerting tools, such as Prometheus and Alertmanager.

I have obtained one of the following certifications (highly recommended):

* Google Certified Associate Cloud Engineer Certification.

* AWS professional-level or associate-level certifications (multiple).

* Azure Administrator.

## Integration testing

I can:

* Automate QA testing using a test automation framework.

* Design a chaos engineering test for a cloud-based deployment running in production.

* Use chaos engineering testing tools, such as Chaos Monkey.

## Kubernetes (basic)

I've gone through the tutorials at kubernetes.io, and am able to:

* Use the kubectl command to determine the status of all the pods in a namespace, and to determine whether pods are operational.

* Use the kubectl describe pod command to perform basic troubleshooting on pods that are not operational.

* Use the kubectl command to obtain information about namespaces, secrets, deployments, and stateful sets.

* Use the kubectl command to manage persistent volumes and persistent volume claims.

## Kubernetes (expert)

In addition to the [basic skills for Kubernetes](#skills-cdk-kubernetes), I have:

* Configured role-based access to cloud resources.

* Configured Kubernetes objects, such as deployments and stateful sets.

* Configured Kubernetes ingresses.

* Configured Kubernetes resources using Kustomize.

* Passed the Cloud Native Certified Kubernetes Administrator exam (highly recommended).

## Kubernetes backup and restore

I know how to:

* Schedule backups of Kubernetes persistent volumes on volume snapshots.

* Restore Kubernetes persistent volumes from volume snapshots.

I have experience with one or more of the following:

* Volume snapshots on Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (EKS), or Azure Kubernetes Service (AKS)

* A third-party Kubernetes backup and restore product, such as Velero, Kasten K10, TrilioVault, Commvault, or Portworx PX-Backup.

## Project planning and management for cloud deployments

I have planned and managed:

* A production deployment in the cloud.

* A production deployment of Ping Advanced Identity Software.

## Security and hardening for cloud deployments

I can:

* Harden a Ping Advanced Identity Software deployment.

* Configure TLS, including mutual TLS, for a multi-tiered cloud deployment.

* Configure cloud identity and access management and role-based access control for a production deployment.

* Configure encryption for a cloud deployment.

* Configure Kubernetes network security policies.

* Configure private Kubernetes networks, deploying bastion servers as needed.

* Undertake threat modeling exercises.

* Scan Docker images to ensure container security.

* Configure and use private Docker container registries.

## Site reliability engineering for cloud deployments

I can:

* Manage multi-zone and multi-region deployments.

* Implement DS backup and restore in order to recover from a database failure.

* Manage cloud disk availability issues.

* Analyze monitoring output and alerts, and respond should a failure occur.

* Obtain logs from all the software components in my deployment.

* Follow the cloud provider's recommendations for patching and upgrading software in my deployment.

* Implement an upgrade scheme, such as blue/green or rolling upgrades, in my deployment.

* Create a Site Reliability Runbook for the deployment, documenting all the procedures to be followed and other relevant information.

* Follow all the procedures in the project's Site Reliability Runbook, and revise the runbook if it becomes out-of-date.
