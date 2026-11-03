---
title: AWS Storage Considerations
description: Compare AWS storage options for containerized Ping product deployments and learn why Ping recommends EBS volumes over EFS
component: devops
page_id: devops::reference/awsStorage
canonical_url: https://developer.pingidentity.com/devops/reference/awsStorage.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# AWS Storage Considerations

AWS provides many storage options. When considering Ping products deployed in a containerized deployment, the choice typically comes down to two: elastic block storage (EBS) and elastic file system (EFS). Though there are a number of differences between them, on the surface they act similar when attached to an Elastic Kubernetes Service (EKS) node or Elastic Compute Cloud (EC2) instance.

However, Ping products (whether containerized or not) require high I/O performance, and **Ping only recommends EBS volumes as the backing store**. EFS performance is significantly lower and is not supported.

For additional product-specific requirements, visit the [appropriate product page](https://docs.pingidentity.com/).

---

---
title: Components and Configuration
description: Understand how data and configuration flow through a Ping product container and learn ways to customize it using server profiles, hooks, and release tags
component: devops
page_id: devops::reference/config
canonical_url: https://developer.pingidentity.com/devops/reference/config.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-container-data-flows-and-running-state: Container data flows and running state
  devops-examples: Examples
  file-flowchart-example: File flowchart example
  devops-production-example: Production Example
  devops-development-example: Development Example
  devops-customizing-the-containers: Customizing the Containers
---

# Components and Configuration

## Container data flows and running state

The diagram below shows the topology of a container with flows of data into the container and how it transitions to the eventual running state.

![DevOps Image/Container Anatomy](../_images/container-anatomy-1.svg)

| Data Class        | Default Location  | Use | Description                                                                                                       |
| ----------------- | ----------------- | --- | ----------------------------------------------------------------------------------------------------------------- |
| VAULT             |                   | ext | Secret information from external Vault (i.e. HashiCorp Vault). Items like passwords, certificates, keys, etc.     |
| ORCH              |                   | ext | Environment variables from secrets, configmaps and/or env/envfile resources from orchestration (i.e. docker, k8s) |
| SERVER PROFILE    |                   | ext | Product server profile from either an external repository (i.e. git) or external volume (i.e. aws s3).            |
| SERVER BITS       | /opt/server       | ro  | Uncompressed copy of the product software. Provided by image.                                                     |
| SECRETS           | /run/secrets      | ro  | Read Only secrets residing on non-persistent storage (i.e. /run/secrets).                                         |
| IN                | /opt/in           | ro  | Volume intended to receive all incoming server-profile information.                                               |
| ENV               | /opt/staging/.env | mem | Environment variable settings used by hooks and product to configure container.                                   |
| STAGING           | /opt/staging      | tmp | Temporary space used to prepare configuration and store variable settings before being moved to OUT               |
| OUT               | opt/opt           | rw  | Combo of product bits/configuration resulting in running container configuration.                                 |
| PERSISTENT VOLUME |                   | rw  | Persistent location of product bits/configuration in external storage (i.e. AWS EBS)                              |

Because of these many factors affecting how an image is deployed, the configuration options for use of the elements in the previous table can vary greatly, depending on factors such as:

* Deployment Environment - Kubernetes, Cloud Vendor, Local Docker

* CI/CD Tools - Kubectl, Helm, Kustomize, Terraform

* Source Maintenance - Git, Cloud Vendor Volumes

* Customer Environment - Development, Test, QA, Stage, Prod

* Security - Test/QA/Production Data, Secrets, Certificates, Secret Management Tools

## Examples

### File flowchart example

The following diagram shows how files can enter and flow through the container:

![File Flowchart Example](../_images/container-anatomy-flow.svg)

|   |                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | There is a video that goes through the above image in more detail [here](https://videos.pingidentity.com/detail/videos/devops/video/6314748082112/ping-product-docker-image-exploration). |

### Production Example

The following diagram shows an example in a high-level production scenario in an Amazon Web Services (AWS) EKS environment, where:

* HashiCorp Vault is used to provide secrets to the container.

* Helm is used to create k8s resources and deploy them.

* AWS EBS volumes is used to persist the state of the container.

![Production Tools Example](../_images/container-anatomy-1-prod.svg)

### Development Example

The following diagram shows an example in a high-level development scenario in an Azure AKS environment, where:

* No secrets management is used.

* Simple kubectl is used to deploy k8s resources.

* AWS EBS volumes is used to persist the state of the container.

![Development Tools Example](../_images/container-anatomy-1-dev.svg)

## Customizing the Containers

You can customize our product containers by:

* [Customizing server profiles](../how-to/profiles.html)

  The server profiles supply configuration, data, and environment information to the product containers at startup. You can use our server profiles as-is or as a baseline for creating your own.

  You can find these profiles in [Baseline server profiles](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/baseline) in our pingidentity-server-profiles repository.

* [Environment substitution](../how-to/profilesSubstitution.html)

  You can deploy configurations in multiple environments with minimal changes by removing literal values and replacing them with environment variables.

* [Using DevOps hooks](hooks.html)

  Hooks are shell scripts used to automate operations during the lifecycle of a product container. These hook scripts are built into our images: some are common across all products, while others are product-specific. For more information about the repository that houses these scripts, visit the [docker-builds repository overview](../docker-builds/README.html).

* [Using release tags](../docker-images/releaseTags.html)

  We use sets of tags for each released build image. These tags identify whether the image is a specific stable release, the latest stable release, or current (potentially unstable) builds. You can find the release tag information in [Docker images](../docker-images/releaseTags.html).

  You can try different tags in either the standalone startup scripts for the deployment examples or the YAML files for the orchestrated deployment examples.

* [Adding a message of the day (MOTD)](../how-to/addMOTD.html)

  You can use a `motd.json` file to add message of the day information for inclusion in the images.

---

---
title: Container Logging
description: Learn how container logging works for Ping products and how to persist logs externally using a logging sidecar or TAIL_LOG_FILES
component: devops
page_id: devops::reference/containerLogging
canonical_url: https://developer.pingidentity.com/devops/reference/containerLogging.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-problem-statement: Problem statement
  devops-viewing-logs: Viewing logs
  devops-persisting-logs: Persisting logs
  devops-logging-sidecar: Logging sidecar
  devops-the-tail_log_files-environment-variable: The TAIL_LOG_FILES environment variable
  devops-references: References
---

# Container Logging

This document provides an outline of how logging is handled in containerized environments. Please refer to the provided links at the end of this page for details on implementing a logging solution for your deployments.

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | While providing examples for all logging solutions is impractical, there is an example for using Splunk on this portal [here](../how-to/splunkLogging.html). |

## Problem statement

In a containerized deployment model, it is expected that containers (or pods under Kubernetes) will be ephemeral. Further, the standard practice for application logging in a container is to use `stdout` and, in some cases, `stderr` as the means of streaming logs. Ping product containers follow this practice. As a result, no logs will persist outside the lifecycle of the container or pod. In particular, if a pod is failing or in crashloop due to a misconfiguration or error, it is impossible to troubleshoot the cause as the logs that might provide information on the crash are lost each time the pod attempts to restart. **It is important, then, to insure that logs are stored external to the container.**

!!! error "In Case You Missed It" If a container is stopped for any reason, including crashes, all logging information from the container that is not stored elsewhere is lost.

### Viewing logs

In a Kubernetes deployment, you can view the streaming logs (stdout/stderr) of a container in a pod by issuing the `kubectl logs` command. This function is useful for quickly examining logs from operational containers.

### Persisting logs

Because you cannot rely on the logs from the container itself for long-term use, you must implement some means of storing the logging information apart from the container itself.

### Logging sidecar

In the Kubernetes model, a common method of maintaining logs is to use the [sidecar model](../deployment/deployK8sUtilitySidecar.html). A logging sidecar is included in the pod and configured to grab the stdout/stderr streams from the application container and persist them to the logging service. Many vendors provide a Docker image for this sidecar that contains the agent for their product. In addition, they usually provide support for configuring the container to connect to their service and format the logs for consumption, such as through environment variables, Kubernetes ConfigMaps, or other means.

Advantages:

* Logs can be sent to different locations at the same time using multiple sidecars

* Access to the cluster node is not required - particularly useful for hosted Kubernetes environments

* No update to the application is required, assuming it dumps logging information to stdout/stderr

Disadvantage:

* Additional resources are required for running the extra container(s), though they tend to be lightweight

### The TAIL_LOG_FILES environment variable

Many Ping products were designed and built for a server-deployed implementation. As a result, they write log information to files (the old model for logging), rather than to `stdout`. To ease containerization, an environment variable (**`TAIL_LOG_FILES`**) is included in the Docker images and this variable is fed to a function that streams these files to `stdout` as they are written.

While Ping includes key log files as defaults, this variable can be modified. You can add additional log files to this variable to include them in the `stdout` stream. See [each product Dockerfile](https://github.com/pingidentity/pingidentity-docker-builds) for the default value of this variable for the product in question.

### References

The list below is not intended to be comprehensive but should provide a good starting point for understanding how logging works and what you can do to retain logs from your deployments.

!!! note "Examples only" Any vendor listed here should not be considered an endorsement or recommendation by Ping Identity for that service. Refer to the documentation for the image in question for further assistance.

* [Kubernetes Logging Documentation](https://kubernetes.io/docs/concepts/cluster-administration/logging/)

* [Docker Logging Documentation](https://docs.docker.com/config/containers/logging/)

* Docker Hub images, listed alphabetically:

  * [AWS Cloudwatch](https://hub.docker.com/r/amazon/cloudwatch-agent)

  * [Datadog](https://hub.docker.com/r/datadog/agent)

  * [Fluentd](https://hub.docker.com/_/fluentd)

  * [Graylog](https://hub.docker.com/u/graylog)

  * [Rsyslog](https://hub.docker.com/u/rsyslog)

  * [Sematext](https://hub.docker.com/u/sematext)

  * [Splunk Forwarder](https://hub.docker.com/r/splunk/universalforwarder/)

  * [Sumologic](https://hub.docker.com/r/sumologic/collector)

---

---
title: FAQs
description: Find frequently asked questions about Ping Docker images, container operations, Helm and Kubernetes orchestration, and troubleshooting
component: devops
page_id: devops::reference/faqs
canonical_url: https://developer.pingidentity.com/devops/reference/faqs.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-aws: AWS
  devops-docker-images: Docker Images
  devops-container-operations: Container Operations
  devops-orchestration-helm-kubernetes: Orchestration / Helm / Kubernetes
  devops-configuration-and-server-profile: Configuration and Server Profile
  devops-product-related: Product related
  devops-troubleshoot: Troubleshoot
---

# FAQs

### AWS

> **Collapse: What storage option should I use for container volumes on EKS?**
>
> Ping recommends the use of EBS volumes for container volumes on EKS. EFS is not supported. For more information, please visit 
>
> [AWS Storage Considerations](https://devops.pingidentity.com/reference/awsStorage/)
>
> .

### Docker Images

> **Collapse: I see Ping product container images hosted in Iron Bank. What are the differences between these images and those found on Docker Hub?**
>
> [Iron Bank](https://docs-ironbank.dso.mil/)
>
>  is a container image repository intended to host images for those environments requiring additional security, such as for FedRAMP certification and similar situations. Ping does not build these images, but rather they are created by a Ping partner. These images contain the same product code as found on Docker Hub; however, the OS and JDK used in building the container images are chosen by the partner as per their requirements. You can have full confidence in these images. If you encounter a problem related to an image provided through Iron Bank, you can open a ticket through your normal Ping support channels, indicating that it is an Iron Bank image in question.

> **Collapse: What OS and Java versions are included in Ping Docker images?**
>
> The operating system (OS) shims used for our images are Alpine and Red Hat UBI. The UBI-based images are intended for Openshift deployments, while Alpine should be used in most other situations. For more information on the choice of Alpine, please visit 
>
> [Supported OS Shim](https://devops.pingidentity.com/docker-images/imageSupport/#supported-os-shim)
>
> . The Java version currently included in our images is OpenJDK 25 and the distribution used is 
>
> [BellSoft Liberica](https://bell-sw.com/libericajdk/)
>
> .

> **Collapse: When are new Ping product Docker images released?**
>
> Typically, Docker images are released on a monthly basis during the first full week of the month. The images are tagged YYMM, with the month indicating the complete month prior. So, tag "2607", representing the work from July 2026, would be released in early August. As we mature our processes, the frequency and timing of these images will more closely align with product releases.

> **Collapse: How can I be informed when new images are available?**
>
> You can watch the 
>
> [docker-builds GitHub repository](https://github.com/pingidentity/pingidentity-docker-builds/)
>
>  for the Ping Identity product line. Select the "custom" option to receive notification when a release occurs. Releases in the docker-builds repository correspond to the publishing of images in Docker Hub.

> **Collapse: What are the latest Ping product versions available as Docker images?**
>
> The latest Ping product images are tagged with 
>
> **{RELEASE}-{PRODUCT VERSION}**
>
> . You can find more information about our latest product images by consulting the 
>
> [Product Version matrix](https://devops.pingidentity.com/docker-images/productVersionMatrix/)
>
> .

> **Collapse: Do the images come as product only or combined with an OS layer?**
>
> The DevOps program builds its images on Alpine (the default) and Red Hat UBI 9 minimal. For more information please visit 
>
> [Supported OS Shim](https://devops.pingidentity.com/docker-images/imageSupport/#supported-os-shim)
>
> .

> **Collapse: I have created a custom product installation. If we require a specific image, can that be supplied by Ping?**
>
> We do not provide custom images, but you are welcome to build the image locally with your customized bits. For more information, see 
>
> [Build Local Images](https://devops.pingidentity.com/how-to/buildLocal/)
>
> .
>
> \
>
>
> It is important to note using a custom image might affect support options and timing.

> **Collapse: How do I verify that a Ping container image is authentic?**
>
> Ping signs all container images published to Docker Hub using Cosign with a KMS-backed key, beginning with the 2605 sprint release. You can verify any image against the published public key before promoting or deploying it. For step-by-step instructions, see 
>
> [Image Signature Verification](https://developer.pingidentity.com/devops/docker-images/imageSignatureVerification.html)
>
> .

> **Collapse: What are the  tagged images on Docker Hub?**
>
> Flex images are a new generation of Ping container images with simplified runtime behavior, reduced dependence on startup hooks, and better alignment with standard container practices. They are 
>
> **not**
>
>  drop-in replacements for current images; both image lines will coexist during an extended transition so customers can adopt the new model on their own timeline. For details on what is changing, what is not, and migration considerations, see 
>
> [Flex Images](https://developer.pingidentity.com/devops/docker-images/flexImages.html)
>
> .

### Container Operations

> **Collapse: How do files move around when the container starts up?**
>
> To find out how our files are moved at start up, please visit 
>
> [File Flowchart](https://devops.pingidentity.com/reference/config/#file-flowchart-example)
>
> .

> **Collapse: How do I turn off the calls to the Message of the Day (MOTD)?**
>
> Set the environment variable in PingBase to: 
>
> **MOTD_URL=""**
>
> \
>
>
> For more information about the PingBase environment variables, please visit 
>
> [PingBase](https://devops.pingidentity.com/docker-images/pingbase/)
>
> .

> **Collapse: How do I get more verbosity in log outputs?**
>
> Set the environment variables in PingBase to: 
>
> `VERBOSE="true"`
>
> \
>
>
> For more information about the PingBase environment variables, please visit 
>
> [PingBase](https://devops.pingidentity.com/docker-images/pingbase/)
>
> .

### Orchestration / Helm / Kubernetes

> **Collapse: How can I be informed when a new release of the Helm charts are available?**
>
> You can watch the 
>
> [Ping helm-charts GitHub repository](https://github.com/pingidentity/helm-charts/)
>
> . Select the "custom" option to receive notification when a release occurs. As with the product Docker images, the Helm charts are usually updated once a month.

> **Collapse: Kubernetes has dropped direct integration support for Docker. Does this change impact Ping product containers?**
>
> No. The underlying container runtime has not caused problems with our images. Please let us know if you encounter errors. The 
>
> **CRI-O**
>
>  and 
>
> **containerd**
>
>  runtimes have been tested without any known issues. For more background:
>
> \
>
>
> The Kubernetes blog post on Docker removal is 
>
> [here](https://kubernetes.io/blog/2022/02/17/dockershim-faq/)
>
> .
>
> \
>
>
> An excellent write up of how it looks is on this 
>
> [page](https://kodekloud.com/blog/kubernetes-removed-docker-what-happens-now/)
>
> .

> **Collapse: My container environment is not allowed to make any external calls to services such as Github or Docker Hub. Can I still use Ping Identity containers?**
>
> Yes. This practice is common in production scenarios. To use Ping Identity containers in this situation:
>
> \
>
>
>  1. Use an 
>
> [Existing License](https://devops.pingidentity.com/how-to/existingLicense)
>
> .
>
> \
>
>
>  2. Use an empty remote profile 
>
> **SERVER_PROFILE_URL=""**
>
> . Optionally, you can build your profile into the image, visit 
>
> [Customizing Server Profiles](../how-to/profiles.html)
>
>  for more information.
>
> \
>
>
>  3. Turn off license verification with 
>
> **MUTE_LICENSE_VERIFICATION="true"**
>
> .
>
> \
>
>
>  4. Turn off calls to the Message of the Day (MOTD) with 
>
> **MOTD_URL=""**
>
> .

> **Collapse: How do we run the console and engines in a container environment?**
>
> The helm chart supports instantiating both consoles and engines. Ingress to the consoles would have to be laid out for UI access.
>
> \
>
>
> For more information about the Ping's Helm Charts, please visit 
>
> [Ping Helm](https://helm.pingidentity.com/)
>
> .

> **Collapse: Can I use Podman instead of Docker?**
>
> Yes, just like Docker, you will be able to use Podman for container orchestration.

> **Collapse: Why does Ping recommend K8s vs docker?**
>
> 1\. Docker or a pure container solution like ECS by itself is generally not as robust or resilient as a K8s environment. While managed Docker services like ECS provide some of the functionality of Kubernetes, you are locked into that provider and you would have a different experience at Google, Azure, or another cloud provider. Kubernetes, even managed services like EKS, provides more flexibility and portability.
>
> \
>
>
> 2\. It is the model we use for our SaaS offerings, so internal teams at Ping are more familiar with this model.
>
> \
>
>
> 3\. Orchestration among multiple applications and services is native to Kubernetes, a bit of an add-on with Container-only services.
>
> \
>
>
> 4\. Workload management using Kubernetes native objects, such as Horizontal Pod Autoscaling, Node scaling and so on.
>
> \
>
>
> 5\. Management through Infrastructure-as-Code principles using Helm Charts and Values files.

### Configuration and Server Profile

> **Collapse: How do I customize a container?**
>
> There are many ways to customize the container for a Ping product. For example, you can create a customized server profile to save a configuration. To find more ways on how to customize a container, see 
>
> [Customizing Containers](https://devops.pingidentity.com/reference/config/#customizing-the-containers)
>
> .

> **Collapse: How do I save product configurations?**
>
> In order to save configurations, create a server profile and store in a server profile repository. This repository can be used to pass the configuration into the runtime environment. For help with creating a custom server profile, visit 
>
> [Server Profiles](https://devops.pingidentity.com/how-to/profiles/)
>
> .
>
> \
>
>
> **Examples of how to get the profile data from the different products:**
>
> \
>
>
>   
>
> **[PingFederate](https://devops.pingidentity.com/how-to/buildPingFederateProfile/) Profile**
>
> \
>
>
> `curl -k https://localhost:9999/pf-admin-api/v1/bulk/export?includeExternalResources=false \
> -u administrator:2FederateM0re \
> -H 'X-XSRF-Header: PingFederate' \
> -o data.json`
>
> \
>
>
>   
>
> **PingAccess Profile**
>
> \
>
>
> `curl -k https://localhost:9000/pa-admin-api/v3/config/export \
> -u administrator:2FederateM0re \
> -H "X-XSRF-Header: PingAccess" \
> -o data.json`
>
> \
>
>
>   
>
> **[PingDirectory](https://devops.pingidentity.com/how-to/buildPingDirectoryProfile/) Profile**
>
> \
>
>
> `kubectl exec -it pingdirectory-0 \ + — manage-profile generate-profile \ --profileRoot /tmp/pd.profile`

> **Collapse: What should be in my server profile?**
>
> For more information about what information should be in the server profile consist, please visit 
>
> [Container Anatomy](https://devops.pingidentity.com/how-to/containerAnatomy/)
>
>  and 
>
> [Profile Structures](https://devops.pingidentity.com/reference/profileStructures/)
>
> .

> **Collapse: Does my server profile have to be hosted on Github?**
>
> No, it can be any 
>
> [Public](https://devops.pingidentity.com/how-to/profiles/#using-your-github-repository)
>
>  or 
>
> [Private](https://devops.pingidentity.com/how-to/privateRepos/)
>
>  git repository. You are also able to use a 
>
> [Local Directory](https://devops.pingidentity.com/how-to/profiles/#using-local-directories)
>
>  as your repository, which is convenient for testing and development.

### Product related

> **Collapse: How do I access various product consoles?**
>
> For a Helm-deployed stack, there are two basic ways you can access the consoles.
>
> \
>
>
> 1\. PortForward to the pod to access with localhost.
>
> \
>
>
> `kubectl port-forward <podName> <containerPort>:<localPort>`
>
> \
>
>
> 2\. Using Helm, add the ingress definition in the yaml file in order to access the container with a URL. See 
>
> [Creating Ingresses](https://devops.pingidentity.com/deployment/deployHelmLocalIngress/#create-ingresses)
>
> . You must have an ingress controller in your cluster for the ingress to work.

> **Collapse: How do I use an existing license?**
>
> You can mount the license in the container's 
>
> **`opt/in`**
>
>  directory. Please see 
>
> [using existing licenses](https://devops.pingidentity.com/how-to/existingLicense/)
>
>  for more information.

> **Collapse: Where do I get a license? How do I obtain a trial license?**
>
> The DevOps team at Ping is not responsible for issuing supported product licenses. We provide a temporary license through the DevOps program. 
>
> [After signing up](https://devops.pingidentity.com/how-to/devopsRegistration/)
>
> , you can use the provided credentials to get a short-term license to use in evaluating Ping products running in containers. If you want to use Ping products in production environments, you are required to purchase a valid license. 
>
> [Contact our sales department](https://www.pingidentity.com/en/company/contact-sales.html)
>
>  for more information.

> **Collapse: How do I turn off the license verification?**
>
> Set the environment variable in PingBase to: 
>
> **MUTE_LICENSE_VERIFICATION="true"**
>
> \
>
>
> For more information about the PingBase environment variables, please visit 
>
> [PingBase](https://devops.pingidentity.com/docker-images/pingbase/)
>
> .

### Troubleshoot

> **Collapse: How do I run Collect-Support-Data in the devops environment?**
>
> You will need to modify the liveness probe to always exit 0 and the readiness probe to always exit 1. These changes will give you enough time to capture the CSD without it crashing or trying to serve live traffic.
>
> \
>
>
> For more information about the Collect-Support-Data, please visit 
>
> [CSD](https://support.pingidentity.com/s/article/collect-support-data-tool)
>
> .

> **Collapse: How much overhead memory and CPU is needed to run the Collect-Support-Data tool?**
>
> By default, this value is set to 1GB. You would need to add additional memory (1GB to 2GB) to the heap for the server. In terms of CPU, the CSD uses whatever is available.
>
> \
>
>
> For more information about the Collect-Support-Data, please visit 
>
> [CSD](https://support.pingidentity.com/s/article/collect-support-data-tool)
>
> .

---

---
title: Helm Basics
description: Learn core Helm terminology and commands for deploying, upgrading, and deleting Ping product releases with the Ping Identity DevOps Helm chart
component: devops
page_id: devops::reference/HelmBasics
canonical_url: https://developer.pingidentity.com/devops/reference/HelmBasics.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-helm: Helm
  devops-terminology: Terminology
  devops-building-the-helm-values-file: Building the Helm Values File
  devops-providing-your-own-server-profile: Providing your own server profile
  devops-additional-commands: Additional Commands
  devops-deploy-a-release: Deploy a release:
  devops-delete-a-release: Delete a release:
  devops-delete-pvcs-associated-to-a-release: Delete PVCs associated to a release:
  devops-exit-codes: Exit Codes
  devops-example-configurations: Example Configurations
---

# Helm Basics

Although this document cannot cover the depths of this tool, new Helm users might find other technical documentation too involved for the purpose of beginning use of Ping Identity container images. This document aims to equip new users with helpful terminology in simple terms, with a focus on relevant commands. For more in-depth documentation around Helm, check out [helm.sh](https://helm.sh).

|   |                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This overview uses Ping Identity images and practices as a guide, but generally applies to any interactions using Helm with Kubernetes. With these assumptions, this document might feel incomplete or inaccurate to veterans. If you would like to contribute to this document, feel free to open a pull request! |

## Helm

|   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All of our instructions and examples are based on the [Ping Identity DevOps Helm chart](https://helm.pingidentity.com). If you are not using the Ping Identity DevOps Helm chart in production, we still recommend using it to generate your direct Kubernetes manifest files. Using our provided chart to create your files in this manner gives Ping Identity the best opportunity to support your environment. |

Everything in Kubernetes is deployed by defining what you want and allowing Kubernetes to achieve the desired state ([the declarative model](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/)).

Helm simplifies your interaction by building deployment patterns into templates with variables. The Ping Identity Helm chart includes Kubernetes templates and default values maintained by Ping Identity. With these in hand, you only need to provide values for the template variables to match your environment.

For example, a service definition looks like the following file. With this file, Kubernetes is instructed to create a `service` resource with the name `myping-pingdirectory`.

```
apiVersion: v1
kind: Service
metadata:
  labels:
    app.kubernetes.io/instance: myping
    app.kubernetes.io/name: pingdirectory
  name: myping-pingdirectory
spec:
  ports:
  - name: https
    port: 443
    protocol: TCP
    targetPort: 1443
  - name: ldap
    port: 389
    protocol: TCP
    targetPort: 1389
  - name: ldaps
    port: 636
    protocol: TCP
    targetPort: 1636
  selector:
    app.kubernetes.io/instance: myping
    app.kubernetes.io/name: pingdirectory
  type: ClusterIP
```

Using our Helm chart, you can automatically define this entire resource and all other required resources for a basic deployment by setting `pingdirectory.enabled=true`.

### Terminology

**Manifests** - the final Kubernetes YAML files that are sent to the cluster for resource creation. These files are standard Kubernetes files and will be similar to the service example shown above.

**Helm Templates** - Go Template versions of Kubernetes YAML files. These templates enable the manifest creation to be parameterized.

**Values and values.yaml** - A value is the setting you pass to a Helm chart from which the templates produce the manifests you want. Values can be passed individually on the command line, but more commonly they are collected and defined in a file named **values.yaml**. For example, if this file contained only this entry, the resulting Kubernetes manifest file would be over 200 lines long.

```
pingdirectory:
  enabled: true
```

**release** - When you deploy resources with Helm, you provide a name for identification. The combination of this name and the resources that are deployed using it make up a `release`. When using Helm, it is a common pattern to prefix all resources managed by a release with the release name. In our examples, `myping` is the release name, so you will see products in Kubernetes running with names similar to `myping-pingfederate-admin`, `myping-pingdirectory`, and `myping-pingauthorize`.

### Building the Helm Values File

This documentation focuses on the [Ping Identity DevOps Helm chart](https://github.com/pingidentity/helm-charts) and the values passed to the Helm chart to achieve your configuration. For your deployment to fit your goals, you must create a [values.yaml](https://helm.sh/docs/chart_template_guide/values_files/) file.

The most simple **values.yaml** for our Helm chart would be:

```
global:
  enabled: true
```

By default, this flag is set as `global.enabled=false`. These two lines are sufficient to turn on (deploy) every available Ping Identity software product with a basic configuration.

### Providing your own server profile

In the documentation, there is an example for providing your own server profile stored in GitHub to PingDirectory. The documenation provides this snippet in the values.yaml specific to that feature:

```
pingdirectory:
  envs:
    SERVER_PROFILE_URL: https://github.com/<your-github-user>/pingidentity-server-profiles
```

This entry alone will not turn on PingDirectory, because the default value for `pingdirectory.enabled` is false. To complete the deployment, add the snippet to turn deploy and configure PingDirectory in the values.yaml file:

```
global:
  enabled: true
pingdirectory:
  envs:
    SERVER_PROFILE_URL: https://github.com/<your-github-user>/pingidentity-server-profiles
```

This example snippet turns on all products, including PingDirectory, and overwrites the default `pingdirectory.envs.SERVER_PROFILE_URL` with `https://github.com/<your-github-user>/pingidentity-server-profiles`.

This use of substitution and parameters is where the power of Helm to simplify ease of deployment begins to shine. To fully customize your deployment, review all available options by running:

`helm show values pingidentity/ping-devops`

This command prints all of the default values applied to your deployment. To overwrite any default values from the chart, copy the corresponding snippet and include it in your own values.yaml file with any modifications needed. Remember with YAML that tabbing and spacing matters. For most editors, copying all the way to the left margin and pasting at the very beginning of a line in your file should maintain proper indentation.

Helm also provides a wide variety of plugins. A useful one is [Helm diff](https://github.com/databus23/helm-diff). This plugin shows what changes would be applied between Helm upgrade commands. For example, if this plugin indicates anything in a Deployment or Statefulset would change, you can expect the corresponding pods to be cycled. In this example, **Helm diff** is useful to note changes that would occur, particularly when you are not prepared for containers to be restarted.

### Additional Commands

As you go through the Helm examples, the goal is to build a values.yaml file that works in your environment.

#### Deploy a release:

`helm upgrade --install <release_name> pingidentity/ping-devops -f /path/to/values.yaml`

#### Delete a release:

This command will remove all resources except PVC and PV objects associated with the release from the cluster:

`helm uninstall <release name>`

#### Delete PVCs associated to a release:

`kubectl delete pvc --selector=app.kubernetes.io/instance=<release_name>`

### Exit Codes

| Exit Code     | Description                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| Exit Code 0   | Absence of an attached foreground process                                                              |
| Exit Code 1   | Indicates failure due to application error                                                             |
| Exit Code 137 | Indicates failure as container received SIGKILL (manual intervention or 'oom-killer' \[OUT-OF-MEMORY]) |
| Exit Code 139 | Indicates failure as container received SIGSEGV                                                        |
| Exit Code 143 | Indicates failure as a container received SIGTERM                                                      |

### Example Configurations

Advanced Helm examples now live in Helm section at [Helm Chart Examples](https://developer.pingidentity.com/helm/examples/index.html). Please review [Getting Started Page](../get-started/introduction.html) before trying them.