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

### The TAIL\_LOG\_FILES environment variable

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
> [Supported OS Shim](https://devops.pingidentity.com/docker-images/imageSupport/<mark>supported-os-shim)
>
> . The Java version currently included in our images is OpenJDK 17 and the distribution used is 
>
> [BellSoft Liberica](https://bell-sw.com/libericajdk/)
>
> .

> **Collapse: When are new Ping product Docker images released?**
>
> Typically, Docker images are released on a monthly basis during the first full week of the month. The images are tagged YYMM, with the month indicating the complete month prior. So, tag "2303", representing the work from March 2023, would be released in early April. As we mature our processes, the frequency and timing of these images will more closely align with product releases.

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
> The DevOps program uses #
>
> **Alpine**
>
>  as its base OS shim for all images. For more information please visit 
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

---

---
title: Kubernetes Basics
description: Learn core Kubernetes terminology and commands, such as clusters, pods, deployments, statefulsets, and services, for deploying Ping products
component: devops
page_id: devops::reference/k8sBasics
canonical_url: https://developer.pingidentity.com/devops/reference/k8sBasics.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-kubernetes: Kubernetes
  devops-terms: Terms
  devops-deployments: Deployments
  devops-statefulsets: Statefulsets
  devops-commands: Commands
  devops-viewing-resources: Viewing resources
  devops-debugging: Debugging
---

# Kubernetes Basics

Although this document cannot cover all aspects of these tools, new Kubernetes users might find other technical documentation too involved for purposes of using Ping Identity images. This document aims to equip new users with helpful terminology in simple terms, with a focus on relevant commands.

|   |                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This overview uses Ping Identity images and practices as a guide, but generally applies to any interactions in Kubernetes. With these assumptions, this document might feel incomplete or inaccurate to veterans. If you would like to contribute to this document, feel free to open a pull request! |

## Kubernetes

### Terms

**Cluster** - The ice cube tray

You can consider a Kubernetes cluster as a set of resources into which you can deploy containers. A cluster can be as small as your local computer or as large as hundreds of virtual machines (VMs), called **nodes**, in a data center. Interaction with the cluster is through an API requiring authentication and role-based access control (RBAC) that allows the actions necessary within the cluster.

In a cloud provider Kubernetes cluster, such as Amazon Web Services (AWS) EKS, Azure AKS, or Google GKE, the cluster can span multiple Availability Zones (AZs), but only *one* region. In AWS terms, a cluster can be in the region us-west-2 but have nodes in the AZs us-west-2a, us-west-2b, and us-west-2c. Kubernetes provides high availability by distributing applications with multiple instances of containers, called replicas, across available AZs.

**Nodes** - The individual ice cube spaces in the tray

The nodes are the pieces that provide allocatable resources, such as CPU and memory, and make up a cluster. Typically, these are VMs, and for example in AWS, they would be EC2 instances.

**Namespace** - A loosely defined slice of the cluster

Namespaces are intended to be a virtual delimiter for deploying grouped applications. While it is possible for pods to communicate across namespaces, policies can be put in place with third-party services to prevent this communication.

|   |                                                                                      |
| - | ------------------------------------------------------------------------------------ |
|   | You can allocate resource limits available to a namespace, but this is not required. |

**Context** - A definition in your \~/.kube/config file that specifies the cluster and namespace where your `kubectl` commands will be executed.

**Deployments and Statefulsets** - The water that fills ice cube spots.

Applications are deployed as Deployments or Statefulsets. You can consider both of these objects as controllers that define and manage the following:

* Name of an application

* Number of instances (pods) of an application (replicas)

* Persistent storage

Though they are similar, Deployments differ from Statefulsets in a few fundamental ways.

#### Deployments

* Deployments are typically used for stateless applications - if a pod is lost or removed, any other pod in the same deployment can take on the activity the lost pod was performing.

* Pod names are inconsequential because each pod is identical with no state information required. As a result, the name of the pod does not matter and names are suffixed with a randomly generated string.

* The order in which pods are started is also inconsequential. When starting a deployment all pods are launched at the same time.

* When updating a deployment, you can cycle one, many, or all pods at the same time.

#### Statefulsets

StatefulSets are more structured in the manner in which the pods are handled.

* StatefulSets - as the name implies - are used for applications in which a known state is required. For example, many clustered products have an instance in the cluster that is considered the leader and all pods in the set need to know which pod is acting in this capacity. A controlled scale-up and scale-down process is needed to maintain known state as application nodes or instances join or leave the cluster or are restarted.

* Pod names are *sticky* in that each pod in the StatefulSet has a known name, with each pod receving an ordinal indicator (unlike the random pod name found in Deployments). For example, a StatefulSet will have pod names similar to: `myping-pingdirectory-0`, `myping-pingdirectory-1`, and `myping-pingdirectory-2`

* Controlled startup with health priority: unlike a Deployment, a StatefulSet deploys the first instance (pod name appended with -0) and waits for it to be healthy before adding another to the group.

* Updates occur to instances in a rolling fashion, one-at-a-time, starting with the most recent pod (e.g., `myping-pingdirectory-2`) first.

* With a known Pod name, persistent storage can be maintained for each pod. After persistent storage is created and assigned, the same storage object is provided to the same-named pod every time.

**Pod** - The molecules that make up the water

A Deployment/StatefulSet specifies the *number* of pods to run for a given application. For example, you can have a `pingfederate-engine` deployment that calls for three replicas with two CPUs and 2 GB of memory, but you cannot make one engine larger or smaller than the others.

Like a molecule, a pod can consist of just one container, or it can have multiple containers, called sidecars. For example, your pod can have a PingFederate container as the main process and a sidecar container, such as Splunk Universal Forwarder, to export logs. All containers in a pod, including these sidecars, share a namespace and IP address.

Pods are are considered disposable and by default do not persist any data. To maintain state or data, external storage or a database of some kind is needed.

**PersistentVolume (PV)** and **PersistentVolumeClaim (PVC)** - A virtual external storage device or definition attached to a Pod

The PV is the storage object and PVC is the claim that a given pod makes for that storage.

**Service** - A slim loadbalancer within the cluster

Pods can come and go, be disposed of or restarted. Every time a Pod is started, it will receive an IP address which often changes. In order to access the application hosted in the Pod, a fixed, known location or address is required.

Services provide a single IP address and cluster-internal DNS resolution that is placed in front of Deployments and Statefulsets to distribute traffic. For service-to-service communication, such as PingFederate using PingDirectory as a user store, the application should be configured to point to a service name and port rather than the individual pods. Services are given fully-qualified domain names (FQDNs) in a cluster. Within the same namespace, services are accessible by their name (`https://myping-pingdirectory:443`), but across namespaces, you must be more explicit (`https://myping-pingdirectory.<namespace>:443`). A FQDN would be `https://myping-pingdirectory.<namespace>.svc.cluster.local`.

**Ingress** - A network definition used to expose an application external to the cluster. In order for an ingress to work, you need an Ingress Controller.

A common pattern is a deployment of Nginx pods fronted by a physical loadbalancer. The client application traffic hits the loadbalancer first, then is forwarded to Nginx. The header information (hostname and path) of the request is evaluated and forwarded to a corresponding application service in the cluster.

For example, suppose a PingFederate ingress has a host name of **myping-pingfederate-engine.pingdemo.example**. If a client application makes a request to `https://myping-pingfederate-engine.pingdemo.example/pf/heartbeat.ping`, the traffic flow of the request would be:

* Client -> LoadBalancer -> Nginx k8s Service -> Nginx Pod -> Pingfederate-engine k8s Service -> Pingfederate-engine pod

### Commands

To see which cluster and namespace you are using, use the [kubectx](https://github.com/ahmetb/kubectx#installation) tool.

Alternatively, you can run the following commands:

```
# Retrieve and set context
kubectl config get-contexts
kubectl config current-context
kubectl config use-context my-cluster-name

# Set Namespace
kubectl config set-context --current --namespace=<namespace>
```

#### Viewing resources

You can use [k9s](https://github.com/derailed/k9s), which is a UI designed to run in a terminal.

If you cannot use k9s, review the standard commands here.

You can run `kubectl get` for any [resource type](https://kubernetes.io/docs/reference/kubectl/overview/#resource-types), such as Pods, Deployments, Statefulsets, and PVCs. Many resources have short names:

* `po` = pods

* `deploy` = Deployments

* `sts` = Statefulsets

* `ing` = ingresses

* `pvc` = persistentvolumeclaims

The most common command is `get pods`:

`kubectl get pods`

To show anything that the container prints to `stdout`, use `logs`:

`kubectl logs -f <pod-name>`

To show the logs of a pod with multiple containers, specify the container for which you wish to view logs with the `-c` option:

`kubectl logs -f <pod-name> -c <container-name>`

To show the logs of a crashed pod (`RESTARTS != 0`):

`kubectl logs -f <pod-name> --previous`

To see available host names by ingress:

`kubectl get ing`

#### Debugging

When a pod crashes unexpectedly, you can mine information about the cause with the following commands.

To view logs of the crash:

`kubectl logs -f <pod-name> --previous`

To view the reason for exit:

`kubectl describe pod <pod-name>`

When looking at `describe`, there are two main sections of the output to note:

* lastState - shows the exit code and the reason for exit.

* Events - this list is most helpful when your pod is not being created. It might be stuck in pending state if:

  * There are not enough resources available for the pod to be created.

  * Something about the pod definition is incorrect, such as a missing volume or secret.

Common exit codes associated with containers are:

**Table of Exit Codes and Descriptions**

| Exit Code     | Description                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| Exit Code 0   | Absence of an attached foreground process                                                              |
| Exit Code 1   | Indicates failure due to application error                                                             |
| Exit Code 137 | Indicates failure as container received SIGKILL (manual intervention or 'oom-killer' \[OUT-OF-MEMORY]) |
| Exit Code 139 | Indicates failure as container received SIGSEGV                                                        |
| Exit Code 143 | Indicates failure as a container received SIGTERM                                                      |

---

---
title: PingOne Worker Application and User Configuration
description: Configure a PingOne Worker Application and user roles for Authorization Code, Implicit, or Client Credentials authentication flows
component: devops
page_id: devops::reference/pingone-config
canonical_url: https://developer.pingidentity.com/devops/reference/pingone-config.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-pingone-worker-app-configuration: PingOne Worker Application Configuration
  devops-authorization-code-w-pkce-flow-settings: Authorization Code (w/ PKCE) Flow Settings
  devops-implicit-flow-settings: Implicit Flow Settings
  devops-client-credentials-flow-settings: Client Credentials Flow Settings
  devops-worker-app-roles-settings: Worker App Roles Settings
  devops-pingone-user-config: PingOne User Config
---

# PingOne Worker Application and User Configuration

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

## PingOne Worker Application Configuration

To manage PingOne resources using credentials other than your own, you are required to have a PingOne Worker App.

There are three options to authenticate to PingOne from pingctl:

* [Authorization Code (w/ PKCE) Flow](#devops-authorization-code-w-pkce-flow-settings) (Recommended and most secure) - Using a PingOne Admin User

* [Implicit Flow](#devops-implicit-flow-settings) - Using a PingOne Admin User

* [Client Credentials Flow](#devops-client-credentials-flow-settings) (Easiest, but most insecure, as a user isn't required)

Additionally, you must set up the proper [roles for your Worker App](#devops-worker-app-roles-settings)

### Authorization Code (w/ PKCE) Flow Settings

The following image shows an example of a Worker App setup for Authorization Code (w/ PKCE) Flow:

> **Collapse: Expand Screenshot**
>
> ![pingone worker app authorization code](../_images/pingone-worker-app-authorization_code.png)

### Implicit Flow Settings

The following image shows an example of a Worker App setup for Implicit Flow:

> **Collapse: Expand Screenshot**
>
> ![pingone worker app implicit](../_images/pingone-worker-app-implicit.png)

### Client Credentials Flow Settings

The following image shows an example of a Worker App setup for Client Credentials Flow:

> **Collapse: Expand Screenshot**
>
> ![pingone worker app client credentials](../_images/pingone-worker-app-client-credentials.png)

### Worker App Roles Settings

The following image shows an example of the minimum roles required. Typically, these are set up by default.

> **Collapse: Expand Screenshot**
>
> ![pingone worker app roles](../_images/pingone-worker-app-roles.png)

## PingOne User Config

When using Authorization Code or Implicit Flows, you must sign on with an Administrative user to use the Worker App.

It is important to add the proper administrative roles to the user. The following image shows an example of this configuration:

> **Collapse: Expand Screenshot**
>
> ![pingone user roles](../_images/pingone-user-roles.png)

---

---
title: Running product containers with a read-only root filesystem
description: Configure a Ping product container, using PingDirectory as an example, to run with a read-only root filesystem via emptyDir volumes and Kustomize
component: devops
page_id: devops::reference/readOnlyFilesystem
canonical_url: https://developer.pingidentity.com/devops/reference/readOnlyFilesystem.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-overview: Overview
  devops-high-level-process: High-level process
  devops-prerequisites: Prerequisites
  devops-file-explanation: File explanation
  devops-process: Process
  devops-diagram: Diagram
---

# Running product containers with a read-only root filesystem

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

## Overview

In some environments, there is a requirement that the container filesystem be read-only. Our product images are maturing to support this capability natively in the future. In the meantime, this guide will explain the overall concepts and provide an example with PingDirectory. The other product images can operate in a similar manner.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | This guide is intended to provide an example implementation of solving this problem; your situation might require a different approach. |

|   |                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An excellent starting point for understanding what goes on with our containers as they are instantiated can be found in [this video](https://videos.pingidentity.com/detail/videos/devops/video/6314748082112/ping-product-docker-image-exploration). It is highly recommended that you take the time to view it prior to working through this guide. |

### High-level process

In Ping product containers, the layered approach of bringing the environment and configuration parameters into the container at launch requires merging of files from server profiles and possibly other locations before the product is launched. This process means that files are modified at runtime, and a read-only root filesystem blocks this action. The overall approach is to use [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volumes to overlay the directories that need modification, allowing the hook scripts to run as normal against the volume rather than the container filesystem. In order to get everything necessary for the scripts in place, an init container (using the same image as the product container) is launched and the files necessary are copied to the shared volume before starting the product container.

## Prerequisites

* [kustomize](https://kubectl.docs.kubernetes.io/installation/kustomize/) CLI utility to serve as a [post-renderer](https://helm.sh/docs/topics/advanced/#post-rendering) for Helm.

## File explanation

In the **30-helm/read-only-filesystem** folder of the [Getting Started repository](https://github.com/pingidentity/pingidentity-devops-getting-started) is a values file and kustomize directory. First, we will explore the the `pd-values.yaml` file; inline comments explain what is going on:

> **Collapse:&#x20;**
>
> ```
> initContainers:
> pd-init:
> name: runtime-init
> # CHANGEMETAG TO VERSION NEEDED
> # Init container uses the same image as the product container and therefore versions much match
> image: pingidentity/pingdirectory:CHANGEMETAG
> env:
> # Override the startup command so the product is not launched in the init container
> - name: STARTUP_COMMAND
> value: "ls"
> # Use a name different from /opt/staging for holding the copied files from the product image into the emptyDir volume
> - name: STAGING_DIR
> value: "/opt/handoff"
> # Just in case there is a .env we will need
> - name: CONTAINER_ENV
> value: "/opt/handoff/.env"
> # Another flag for preventing the product from being launched
> - name: STARTUP_FOREGROUND_OPTS
> value: ""
> envFrom:
> # CHANGEMERELEASE TO MATCH HELM RELEASE NAME
> - configMapRef:
> name: CHANGEMERELEASE-global-env-vars
> optional: true
> - configMapRef:
> name: CHANGEMERELEASE-env-vars
> optional: true
> - configMapRef:
> name: CHANGEMERELEASE-pingdirectory-env-vars
> - secretRef:
> name: devops-secret
> optional: true
> - secretRef:
> name: CHANGEME-pingdirectory-git-secret
> optional: true
> volumeMounts:
> # emptyDir volume: /opt/staging will be copied from the init container to this volume
> # This volume will be mounted as /opt/staging in the product container
> - mountPath: /opt/handoff
> name: staging
> readOnly: false
> # The location for the license file varies by product
> # See https://devops.pingidentity.com/how-to/existingLicense/ for more information
> # The license file is required for the init container to operate
> - name: pingdirectory-license
> mountPath: "/opt/staging/pd.profile/server-root/pre-setup/PingDirectory.lic"
> subPath: PingDirectory.lic
> # Also an emptyDir
> - name: tmp
> mountPath: "/tmp"
> readOnly: false
> # Also an emptyDir
> - name: init-runtime
> mountPath: "/opt/out"
> readOnly: false
> # Mount the slightly modified versions of the bootstrap and start sequence scripts (see below)
> - mountPath: /opt/bootstrap.sh
> name: bootstrap
> readOnly: true
> subPath: bootstrap.sh
> defaultMode: 0555
> - mountPath: /opt/staging/hooks/10-start-sequence.sh
> name: init-start
> readOnly: true
> subPath: 10-start-sequence.sh
> defaultMode: 0555
>
> volumes:
> # The 3 emptyDir volumes referenced above
> init-runtime:
> emptyDir: {}
> staging:
> emptyDir: {}
> tmp:
> emptyDir: {}
> # This secret is created from a license file
> pingdirectory-license:
> secret:
> secretName: pingdirectory-license
> # Make the modified bootstrap and start sequence scripts available as configMaps
> bootstrap:
> configMap:
> items:
> - key: bootstrap.sh
> path: bootstrap.sh
> name: bootstrap
> init-start:
> configMap:
> items:
> - key: 10-start-sequence.sh
> path: 10-start-sequence.sh
> name: init-start
>
> configMaps:
> init-start:
> data:
> 10-start-sequence.sh: |-
> #!/usr/bin/env sh
> echo "overwriting 10 hook"
> #!/usr/bin/env sh
> #
> # Ping Identity DevOps - Docker Build Hooks
> #
> # Called when it has been determined that this is the first time the container has
> # been run.
> #
>
>         ##############################################################################
>         ####### Prevent init container from starting the product normally.  ##########
>         ####### These two lines are the only delta from the default script. ##########
>         ##############################################################################
>         if test ${STARTUP_FOREGROUND_OPTS} != "" ; then
>           test "${VERBOSE}" = "true" && set -x
>
>           # shellcheck source=./pingcommon.lib.sh
>           . "${HOOKS_DIR}/pingcommon.lib.sh"
>
>           echo "Initializing server for the first time"
>
>           run_hook "17-check-license.sh"
>
>           run_hook "18-setup-sequence.sh"
>         fi
>   bootstrap:
>     data:
>       bootstrap.sh: |-
>         #!/usr/bin/env sh
>         ######################################################################################################
>         ####### Make a copy of everything under /opt/staging in the product image to /opt/handoff.  ##########
>         ####### Primarily, this makes the hook scripts available in the emptyDir (writable) volume. ##########
>         ####### This line is the only delta from the default script.                                ##########
>         ######################################################################################################
>         cp -r /opt/staging/* /opt/handoff
>         test "${VERBOSE}" = "true" && set -x
>         # shellcheck source=./staging/hooks/pingcommon.lib.sh
>         . "${HOOKS_DIR}/pingcommon.lib.sh"
>
>         _userID=$(id -u)
>         _groupID=$(id -g)
>
>         echo "### Bootstrap"
>         if test "${_userID}" -eq 0; then
>             echo_yellow "### Warning: running container as root user"
>         else
>             echo "### Using the default container user and group"
>
>             _effectiveGroupName=$(awk 'BEGIN{FS=":"}$3~/^'"${_groupID}"'$/{print $1}' /etc/group)
>             test -z "${_effectiveGroupName}" && _effectiveGroupName="undefined group"
>
>             _effectiveUserName=$(awk 'BEGIN{FS=":"}$3~/^'"${_userID}"'$/{print $1}' /etc/passwd)
>             test -z "${_effectiveUserName}" && _effectiveUserName="undefined user"
>
>             echo "### Container user and group"
>             echo "###     user : ${_effectiveUserName} (id: ${_userID})"
>             echo "###     group: ${_effectiveGroupName} (id: ${_groupID})"
>         fi
>
>         # if the current process id is not 1, tini needs to register as sub-reaper
>         if test $$ -ne 1; then
>             _subReaper="-s"
>         fi
>
>         # shellcheck disable=SC2086,SC2048
>         exec "${BASE}/tini" ${_subReaper} -- "${BASE}/entrypoint.sh" ${*}
>
> pingdirectory:
> enabled: true
> envs:
> MUTE_LICENSE_VERIFICATION: "yes"
> ORCHESTRATION_TYPE: "NONE"
> VERBOSE: "true"
> # (Optional) Specify a particular tag by uncommenting these two lines and naming the tag to use.
> # Otherwise, you will get the latest from Docker Hub.
> # If a particular tag is used, be sure the init container tag matches above
> # image:
> #   tag: "2306"
> includeInitContainers:
> # Use the init container specification above at pod startup
> - pd-init
> # Share the volumes between the init container and the product container
> includeVolumes:
> - staging
> - tmp
> - pingdirectory-license
> - bootstrap
> - init-start
> - init-runtime
> volumeMounts:
> # The emptyDir mounted at /opt/handoff in the init container is mounted to /opt/staging here
> # Hook scripts and product startup will operate as with a read/write filesystem
> - mountPath: /opt/staging
> name: staging
> readOnly: false
> - name: pingdirectory-license
> mountPath: "/opt/staging/pd.profile/server-root/pre-setup/PingDirectory.lic"
> subPath: PingDirectory.lic
> - name: tmp
> mountPath: "/tmp"
> readOnly: false
> ```

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Kustomize is used as the Ping helm charts do not support setting the readOnlyFileSystem value to the securityContext of a container at this time. |

In the **30-helm/read-only-filesystem/kustomize** subdirectory is a kustomize script and definition file.

The script simply runs kustomize:

```
#!/bin/bash

cat <&0 > kustomize/all.yaml

kustomize build kustomize && rm kustomize/all.yaml
```

The `kustomization.yaml` file sets the **securityContext** for the each container's root file system to read-only:

```
resources:
  - all.yaml

patches:
  - target:
      group: apps
      version: v1
      kind: StatefulSet
    patch: |-
      - op: add
        path: /spec/template/spec/containers/0/securityContext
        value:
          readOnlyRootFilesystem: true
      - op: add
        path: /spec/template/spec/initContainers/0/securityContext
        value:
          readOnlyRootFilesystem: true
```

## Process

To use the example files to deploy PingDirectory with a read-only root filesystem, follow the steps here:

1. Generate a license file and create a secret. If you have an existing license file, you can use it here:

   ```
   # Generate the license file
   pingctl license pingdirectory 9.2 > PingDirectory.lic

   # Create the secret to match the name in the values file:
   kubectl create secret generic pingdirectory-license --from-file=./PingDirectory.lic
   ```

2. Update the **`30-helm/read-only-filesystem/pd-values.yaml`** file with the appropriate image tag and release name to be used with Helm. Afterward, use Helm to deploy the release:

   ```
   # For this example, the release name of 'rofs' is used
   cd 30-helm/read-only-filesystem
   helm upgrade --install rofs pingidentity/ping-devops -f './pd-values.yaml' \
         --post-renderer kustomize/kustomize
   ```

## Diagram

This image provides an overview of what happens. It is best viewed in a separate tab:

![Read-Only Root Filesystem Example](../_images/readOnlyFileSystem.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | One issue we encountered is that the **`/etc/motd`** file can be modified at startup by hook scripts, but /etc/ is read-only. We are exploring ways to address this in some way, but at this time, it appears one possible solution is to treat `/etc/` in the same manner as /opt/staging (copying to an emptyDir) if the `motd` file is to be updated. However, `/etc` has many more files and directories and such a solution is not practical. Baking it into a custom image is another possibility. |

---

---
title: Server Profile Structures
description: Reference the server profile directory structure and file locations for PingFederate, PingAccess, and PingData product containers
component: devops
page_id: devops::reference/profileStructures
canonical_url: https://developer.pingidentity.com/devops/reference/profileStructures.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-pingfederate: PingFederate
  devops-pingaccess: PingAccess
  devops-ping-data-products: Ping Data Products
---

# Server Profile Structures

Each of the Docker images use a server profile structure that is specific to each product. The structure (directory paths and data) of the server profile differs between products. Depending on how you [Deploy Your Server Profile](../how-to/containerAnatomy.html), it will be pulled or mounted into `/opt/in` on the container and used to stage your deployment.

The following locations are the server profile structures for each of our products with example usage. For help with an example of the basics, see the [pingidentity-server-profiles/getting-started](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/getting-started) examples.

|   |                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the getting-started profile examples, you should not use the `.sec` directory when providing passwords to your containers. These examples are only intended for demonstration purposes. Instead, set an environment variable with your secrets or orchestration later:`PING_IDENTITY_PASSWORD="secret"` |

## PingFederate

See the example at [getting-started/pingfederate](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/getting-started/pingfederate).

**Table of Paths and Location Descriptions**

| Path                                                 | Location description                                                                                                       |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| instance                                             | Directories and files that you want to be used at product runtime, in accordance with the directory layout of the product. |
| instance/server/default/data                         | An extracted configuration archive exported from PingFederate.                                                             |
| instance/bulk-config/data.json                       | A JSON export from the PingFed admin API `/bulk/export`.                                                                   |
| instance/server/default/deploy/OAuthPlayground.war   | Automatically deploy the OAuthPlayground web application.                                                                  |
| instance/server/default/conf/META-INF/hivemodule.xml | Apply a Hive module config to the container. Used for persisting OAuth clients, grants, and sessions to an external DB.    |

|   |                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | By default, PingFederate is shipped with a handful of integration kits and adapters. If you need other integration kits or adapters in the deployment, manually download them and place them inside `server/default/deploy` of the server profile. You can find these resources in the product download page [here](https://www.pingidentity.com/en/resources/downloads/pingfederate.html). |

## PingAccess

Example at [getting-started/pingaccess](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/getting-started/pingaccess).

**Table of Paths and Location Descriptions**

| Path                           | Location description                                                                                                       |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| instance                       | Directories and files that you want to be used at product runtime, in accordance with the directory layout of the product. |
| instance/conf/pa.jwk           | Used to decrypt a `data.json` configuration upon import.                                                                   |
| instance/data/data.json        | PA 6.1+ A config file that, if found by the container, is uploaded into the container.                                     |
| instance/data/PingAccess.mv.db | Database binary that would be ingested at container startup if found.                                                      |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingAccess profiles are typically minimalist because the majority of PingAccess configurations can be found within a `data.json` or `PingAccess.mv.db` file. You should use `data.json` for configurations and only use `PingAccess.mv.db` if necessary. You can easily view and manipulate configurations directly in a JSON file as opposed to the binary `PingAccess.mv.db` file. This fact makes tracking changes in version control easier as well.PingAccess 6.1.x+ supports using only `data.json`, even when clustering. *However* on 6.1.0.3 make sure `data.json` is only supplied to the admin node. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **PingAccess 6.1.0+** now supports native `data.json` ingestion, which is *the recommended method*. Place `data.json` or `data.json.subst` in `instance/conf/data/start-up-deployer`.> The JSON configuration file for PingAccess *must* be named `data.json`.A `data.json` file that corresponds to earlier PingAccess versions *might* be accepted. However, after you are on version 6.1.x, the `data.json` file will be forward compatible. This support means you are able to avoid upgrades for your deployments! |

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For **PingAccess 6.0.x and earlier**, the JSON configuration file for *must* be named `data.json` and located in the `instance/data` directory. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For **all PingAccess versions**, a corresponding file named `pa.jwk` must also exist in the `instance/conf` directory for the `data.json` file to be decrypted on import. To get a `data.json` and `pa.jwk` that work together, pull them both from the same running PingAccess instance.For example, if PingAccess is running in a local Docker container you can use these commands to export the `data.json` file and copy the `pa.jwk` file to your local Downloads directory:```
    curl -k -u "Administrator:${ADMIN_PASSWORD}" -H "X-Xsrf-Header: PingAccess" https://localhost:9000/pa-admin-api/v3/config/export -o ~/Downloads/data.json

    docker cp <container_name>:/opt/out/instance/conf/pa.jwk ~/Downloads/pa.jwk
``` |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can find the PingAccess administrator password in `PingAccess.mv.db`, not in `data.json`. For this reason, you can use the following environment variables to manage different scenarios:* `PING_IDENTITY_PASSWORD`

  Use this variable if:

  * You're starting a PingAccess container without any configurations.

  * You're using only a `data.json` file for configurations.

  * Your `PingAccess.mv.db` file has a password other than the default "2Access".

  The `PING_IDENTITY_PASSWORD` value will be used for all interactions with the PingAccess Admin API (such as importing configurations and creating clustering).

* `PA_ADMIN_PASSWORD_INITIAL`

  Use this variable in addition to `PING_IDENTITY_PASSWORD` to change the runtime admin password and override the password in `PingAccess.mv.db`.> If you use only `data.json` and do notpass `PING_IDENTITY_PASSWORD`, the password will default to "2FederateM0re". **Always** use `PING_IDENTITY_PASSWORD`. |

## Ping Data Products

The Ping Data Products (PingDirectory, PingDataSync, PingAuthorize, PingDirectoryProxy) follow the same structure for server-profiles.

Example at [getting-started/pingdirectory](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/getting-started/pingdirectory).

**Table of Paths and Location Descriptions**

| Path       | Location description                                                                                                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| pd.profile | Server profile matching the structure as defined by [PingDirectory Server Profiles](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_server_profiles.html) |
| instance   | Directories and files that you want to be used at product runtime, in accordance with the layout of the product. In general, this should be **non existing or empty**.                                       |
| env-vars   | You can set environment variables used during deployment. See [Variables and Scope](variableScoping.html) for more info. In general, this should be **non existing or empty**.                               |
| extensions | You can provide URLs to download Server SDK extensions in a remote.list file. See [Including Extensions in PingData Server Profiles](../how-to/profilesPingDataExtensions.html) for more info.               |

|   |                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * In most circumstances, the `pd.profile` directory should be the only directory in the server profile.

* All environment variables should be provided through Kubernetes configmaps/secrets and a secret management tool. Be careful providing an `env-vars` and if you do, please review [Variables and Scope](variableScoping.html) |

|   |                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the `manage-profile` tool (found in product `bin` directory) to generate a `pd.profile` from an existing Ping Data 8.0+ deployment. An example on creating this `pd.profile` looks like:```
    manage-profile generate-profile --profileRoot /tmp/pd.profile
    rm /tmp/pd.profile/setup-arguments.txt
``` |

Follow the instructions provided when you run the `generate-profile` to ensure that you include any additional components, such as `encryption-settings`.

---

---
title: Troubleshooting
description: Troubleshoot common Ping container issues such as stale Docker images, misconfigured DevOps credentials, and evaluation license failures
component: devops
page_id: devops::reference/troubleshooting
canonical_url: https://developer.pingidentity.com/devops/reference/troubleshooting.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-getting-started: Getting started
  devops-examples-not-working: Examples Not Working
  devops-misconfigured: Misconfigured pingctl
  devops-unable-to-retrieve-evaluation-license: Unable To Retrieve Evaluation License
---

# Troubleshooting

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

## Getting started

### Examples Not Working

Many common errors using Ping containers arise from using stale images. Our development is highly dynamic and Docker images can rapidly change.

To avoid issues with stale images, remove all local images from your local cache. Doing so will force Docker to pull the latest images:

`docker rmi $(docker images "pingidentity/*" -q)`

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Even though you might have a local image tagged "latest", this tag does not guarantee it is the newest image in the Docker hub registry. This tag is reapplied for each release image. |

### Misconfigured `pingctl`

If your containers cannot pull a license based on your DevOps user name and key, there might be some misconfiguration in your `pingctl config` file.

Possible solutions:

1. If you have ran `pingctl config` for the first time, see the [Environment Configuration Documentation](../get-started/prereqs.html#devops-configure-the-environment) on how to export configured variables to your environment.

2. Run `pingctl info` and make sure the configured variables in the utility are correct. See the utility's [documentation](../tools/pingctlUtil.html) for more information.

#### Unable To Retrieve Evaluation License

If a product instance or instances cannot retrieve the evaluation license, you might receive an error similar to this:

```
----- Starting hook: /opt/staging/hooks/17-check-license.sh
Pulling evaluation license from Ping Identity for:
              Prod License: PD - v7.3
              DevOps User: some-devops-user@example.com...
Unable to download evaluation product.lic (000), most likely due to invalid PING_IDENTITY_DEVOPS_USER/PING_IDENTITY_DEVOPS_KEY


        ALERT        

#
# No Ping Identity License File (PingDirectory.lic) was found in the server profile.
# No Ping Identity DevOps User or Key was passed.
#
#
# More info on obtaining your DevOps User and Key can be found at:
#     https://devops.pingidentity.com/how-to/devopsRegistration/
#
##
CONTAINER FAILURE: License File absent
CONTAINER FAILURE: Error running 17-check-license.sh
CONTAINER FAILURE: Error running 10-start-sequence.sh
```

This error can be caused by:

1. An invalid DevOps user name or key (as noted in the error). This failure is usually caused by some issue with the variables being passed in. To verify the variables in the `pingctl` configuration are correct for running Docker commands, run the following command:

   `pingctl info`

2. A bad Docker image. Pull the Docker image again to verify.

3. Network connectivity to the license server is blocked. To test this, on the machine that is running the container, run:

   `curl -k https://license.pingidentity.com/devops/license`

   If the license server is reachable, you will receive an error similar to this example:

   `{ "error":"missing devops-user header" }`

---

---
title: Using Certificates with Images
description: Configure keystore and truststore certificates for PingData product containers and learn how to rotate listener certificates
component: devops
page_id: devops::reference/usingCertificates
canonical_url: https://developer.pingidentity.com/devops/reference/usingCertificates.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-before-you-begin: Before you begin
  devops-about-this-topic: About this topic
  devops-pingdata-image-certificates: PingData Image Certificates
  pingdata-image-certificate-rotation: PingData image certificate rotation
  devops-rotating-the-listener-certificate-by-adjusting-environment-variables: Rotating the listener certificate by adjusting environment variables
  devops-rotating-the-listener-certificate-with-the-replace-certificate-command-line-tool: Rotating the listener certificate with the replace-certificate command-line tool
  rotating-the-listener-certificate-when-your-keystore-and-truststore-are-on-a-read-only-filesystem: Rotating the listener certificate when your keystore and truststore are on a read-only filesystem
  rotating-certificates-when-they-are-all-signed-by-the-same-issuer-certificate: Rotating certificates when they are all signed by the same issuer certificate
  add-the-issuer-certificate-to-the-server-instance-listeners-in-the-topology: Add the issuer certificate to the server instance listeners in the topology
  point-the-servers-key-manager-provider-at-your-new-certificate: Point the server's key manager provider at your new certificate
  removing-the-old-certs: Removing the old certs
  rotating-certificates-without-the-assumption-that-they-are-all-signed-by-the-same-issuer-certificate: Rotating certificates without the assumption that they are all signed by the same issuer certificate
  add-the-new-cert-to-the-server-instance-listeners-in-the-topology: Add the new cert to the server instance listeners in the topology
  point-the-servers-key-manager-provider-at-the-new-cert: Point the server's key manager provider at the new cert
  removing-the-old-cert: Removing the old cert
---

# Using Certificates with Images

This page provides details for using certificates with the Ping Identity images. Specifically, it outlines the preferred locations to place the certificate and PIN/key files to provide best security practices and enable use by the underlying Ping Identity product.

Currently, certificates can be provided to the PingData products (PingDirectory, PingDataSync, PingAuthorize, and PingDirectoryProxy) when the containers are started. For non-PingData images, such as PingAccess and PingFederate, the certificates are managed within the product configurations. Those images will not be covered here.

## Before you begin

You must:

* Complete [Get started](../get-started/introduction.html) to set up your DevOps environment and run a test deployment of the products.

* Strongly recommended: Have a secrets management system, such as Hashicorp Vault, that holds your certificate and places them into your SECRETS\_DIR (/run/secrets).

  For information on using a vault, if you have one, see [Using Hashicorp Vault](../how-to/usingVault.html).

## About this topic

The following examples explain how to deploy a certificate/PIN combination to an image in a secure way.

## PingData Image Certificates

The PingData products (PingDirectory, PingDataSync, PingAuthorize, and PingDirectoryProxy) use a file location to determine certificates/PIN files:

* It is best practice to use a non-persistent location, such as /run/secrets, to store these files.

* If no certificate is provided, the container/product will generate a self-signed certificate.

The default location for certificates and associated files are listed below, assuming a default SECRETS\_DIR variable of `/run/secrets`.

|                      | Variable Used         | Default Location/Value /run/secrets…​ | Notes                                                                 |
| -------------------- | --------------------- | ------------------------------------- | --------------------------------------------------------------------- |
| Keystore (JKS)       | KEYSTORE\_FILE        | keystore                              | Java KeyStore (JKS) Format. Set as default in absence of .p12 suffix. |
| Keystore (PKCS12)    | KEYSTORE\_FILE        | keystore.p12                          | PKCS12 Format                                                         |
| Keystore Type        | KEYSTORE\_TYPE        | jks, pkcs12, pem, or bcfks            | Based on suffix of KEYSTORE\_FILE. Only use BCFKS in FIPS mode.       |
| Keystore PIN         | KEYSTORE\_PIN\_FILE   | keystore.pin                          |                                                                       |
| Truststore (JKS)     | TRUSTSTORE\_FILE      | truststore                            | Set as default in absence of .p12 suffix.                             |
| Truststore (PKCS12)  | TRUSTSTORE\_FILE      | truststore.p12                        | PKCS12 Format                                                         |
| Truststore Type      | TRUSTSTORE\_TYPE      | jks, pkcs12, pem, or bcfks            | Based on suffix of TRUSTSTORE\_FILE. Only use BCFKS in FIPS mode.     |
| Truststore PIN       | TRUSTSTORE\_PIN\_FILE | truststore.pin                        |                                                                       |
| Certificate Nickname | CERTIFICATE\_NICKNAME | see below                             |                                                                       |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | There is an additional certificate-based variable used to identity the certificate alias used within the `KEYSTORE_FILE`. That variable is called `CERTIFICATE_NICKNAME`, which identifies the certificate to use by the server in the `KEYSTORE_FILE`. If a value is not provided, the container will look at the list certs found in the `KEYSTORE_FILE` and if one - and only one - certificate is found of type `PrivateKeyEntry`, that alias will be used. |

|   |                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are relying on certificates to be mounted to a different locations than the SECRET\_DIR location or a different filename, you can provide your own values for those variables identified above. As an example:```
 KEYSTORE_FILE=/my/path/to/certs/cert-file
 KEYSTORE_PIN_FILE=/my/path/to/certs/cert.pin
 KEYSTORE_TYPE=jks
 CERTIFICATE_NICKNAME=development-cert
``` |

## PingData image certificate rotation

The certificate rotation process for PingData products varies depending on which product is being configured and whether that product is in a topology. For products that are not in a topology, certificates can be rotated by simply updating the environment variables. For products in a topology, certificate rotation must be done via a command-line call with the servers in the topology online.

### Rotating the listener certificate by adjusting environment variables

The process described in this section can be used for PingAuthorize, PingDirectoryProxy, and *standalone* (single-server) instances of PingDirectory or PingDataSync.

|   |                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------ |
|   | If PingDirectory or PingDataSync is deployed with multiple servers, use the process described in the next section. |

As mentioned above, for the PingData products there are variables defining the server truststore and keystore. To change certificates, you will need to update the contents of the truststore or keystore in your server profile or secret store. After you update the contents, restart the container. The changes will be picked up automatically when the server restarts. If you have multiple certificates in the keystore, you can use the above-mentioned CERTIFICATE\_NICKNAME variable to specify the certificate. The container will pick up that certificate from those stored in the keystore. For updating the product to use the new certificates, perform a rolling update. This action ensures that other servers will remain available as each pod is cycled.

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | Verify that remaining pods in the cluster have sufficient capacity to handle the increased load during the rolling update. |

### Rotating the listener certificate with the replace-certificate command-line tool

If multiple PingDataSync or PingDirectory servers are running in a topology, then the servers must be online when updating the listener certificate. Updates to certificates with one or more servers offline (such as rolling updates) can lead to connection issues with the other members of the topology when those servers come back online. Use the PingData `replace-certificate` command-line tool to update certificates with the server online.

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | If your keystore and truststore files are on a read-only file system, use the process described in the next section. |

Shell into the running instance that needs to be updated, and ensure the keystore containing the needed certificate is mounted on the container. Then, run `replace-certificate`. Replace the `--key-manager-provider` and `--trust-manager-provider` values if necessary when using a non-JKS keystore, as well as the `--source-certificate-alias` value if necessary.

```
replace-certificate replace-listener-certificate \
    --key-manager-provider JKS \
    --trust-manager-provider JKS \
    --source-key-store-file /run/secrets/newkeystore \
    --source-key-store-password-file /run/secrets/newkeystore.pin \
    --source-certificate-alias server-cert \
    --reload-http-connection-handler-certificates
```

For more information on this command, run- `replace-certificate replace-listener-certificate --help`

Running the first command will replace the listener certificate and notify other servers in the topology that this server's certificate has changed.

To update certificates for the other servers in the topology, follow this same process, shelling into each individual instance.

Once this is done, the running pods have been updated. To ensure a restart does not undo these changes, verify that your server profile and orchestration environment variables are updated to point to the new certificates. For example, if you have modified your server configuration to point to `/run/secrets/newkeystore`, then you must update your KEYSTORE\_FILE environment variable to point to that new keystore *after* you have completed the `replace-certificate` process on each server.

### Rotating the listener certificate when your keystore and truststore are on a read-only filesystem

Typically, the `replace-certificate` tool will edit your keystore and truststore when rotating your listener certificate. Because of this, the above method will not work when the keystore and truststore are read-only. In this case, use one of the two following processes to rotate your listener certificates.

#### Rotating certificates when they are all signed by the same issuer certificate

If all your listener certs will be signed by the same certificate authority, you can add this CA to your server instance listeners to make rotation easier, as the servers will automatically trust certificates signed by the CA.

##### Add the issuer certificate to the server instance listeners in the topology

* Copy a PEM file of the your issuer certificate onto your pods. For this example the path will be `/opt/out/instance/config/ca.crt`.

* On each server, use `replace-certificate` to add the issuer certificate to the server instance listener for that server. This will make the servers trust each other provided they are using a cert signed by this issuer. Note that this must be done with all servers online, so that the change gets replicated to the other servers.

  ```
  replace-certificate add-topology-registry-listener-certificate \
      --certificate-file /opt/out/instance/config/ca.crt
  ```

##### Point the server's key manager provider at your new certificate

* Ensure your new certificate has been added to your keystore in whatever external storage method you are using (Vault, etc.), and note the alias you have given the new cert. For this example the alias will be `newcert`.

* Set `CERTIFICATE_NICKNAME=newcert` and perform a rolling update. `manage-profile replace-profile` will run and point your connection handlers to `newcert`, while the servers will continue to trust each other since that cert was signed by the trusted CA you added in the previous step.

##### Removing the old certs

* If desired, you can now remove unused certs from the server instance listeners in the topology registry. You can also remove the old certs from your keystores in your external storage. To remove the old certs from the topology registry, use `replace-certificate`, running the following command on each server in the topology. Note that again this must be done with all servers online, so that the config change gets mirrored across the topology.

  `replace-certificate purge-retired-listener-certificates`

* It is also possible to purge the retired certificates from a single server rather than running a command on each pod, but it requires some configuration changes since it relies on an extended operation and a specific topology admin permission, so it will likely be easier to simply run the previous command on each server. Using dsconfig, the necessary changes would be:

  ```
  dsconfig create-extended-operation-handler \
     --handler-name "Replace Certificate Extended Operation Handler"  \
     --type replace-certificate  \
     --set enabled:true  \
     --set allow-remotely-provided-certificates:true
  dsconfig set-topology-admin-user-prop \
     --user-name admin  \
     --add privilege:permit-replace-certificate-request
  ```

* After these changes are in place on the other servers, the following command can be used to purge retired listener certificates from remote instances:

  `replace-certificate purge-remote-retired-listener-certificates`

#### Rotating certificates without the assumption that they are all signed by the same issuer certificate

##### Add the new cert to the server instance listeners in the topology

* Add the new desired certificate to your keystore and truststore, in whatever external storage method you are using. Note that you are just adding the new cert, not removing the old one yet. Note the alias that you have given the new cert in the keystore. In these examples the new cert's alias will be `newcert` and the previous one `server-cert`.

* Ensure the pods have the updated keystore and truststore on the filesystem, via a rolling update. At this point the keystores and truststores will have both the old cert and the new cert, but the new one is not yet being used.

* On each server, export the PEM file of the new certificate to a writable location, using the `manage-certificates` tool. This action is necessary because the subsequent command can only use a PEM file, it can't read from a keystore directly.

  ```
  manage-certificates export-certificate \
      --keystore /run/secrets/keystore \
      --keystore-password-file /run/secrets/keystore.pin \
      --alias newcert \
      --output-file /opt/out/instance/config/newcert.crt \
      --output-format PEM
  ```

* On each server, use `replace-certificate` to add the exported certificate PEM file to the server instance listener in the topology. Note that this step must be done with all servers online, so that the config change is mirrored to the other servers in the topology.

  ```
  replace-certificate add-topology-registry-listener-certificate \
      --certificate-file /opt/out/instance/config/newcert.crt
  ```

* Now the server will have both the previous cert and the new cert in its server instance listener.

##### Point the server's key manager provider at the new cert

* There are two ways to do this - first is to change the CERTIFICATE\_NICKNAME environment variable to point to your new certificate's alias, and then just restart your pods, allowing manage-profile replace-profile to apply the change on startup.

* The second is to edit your keystore and truststore and rename your new cert to the same alias as the previous one (in the case of this document, renaming `newcert` to `server-cert` - the previous cert will have to be either renamed or removed from the keystores). This way, the key manager provider for the server will load in the new cert. Then you can restart the pods and the new cert will be loaded on server startup.

##### Removing the old cert

* Refer to the removal step in the previous section.

---

---
title: Using DevOps Hooks
description: Learn how DevOps hook scripts run during Ping product container startup and how to add custom pre and post hooks
component: devops
page_id: devops::reference/hooks
canonical_url: https://developer.pingidentity.com/devops/reference/hooks.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-using-pre-and-post-hooks: Using .pre and .post hooks
---

# Using DevOps Hooks

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on hook scripts, see the [Ping product image hook script exploration](https://videos.pingidentity.com/detail/video/6315184605112/hook-script-exploration) video. |

Our DevOps hooks are build-specific scripts that are called, or can be called, by the `entrypoint.sh` script used to start our product containers.

|   |                                                                                               |
| - | --------------------------------------------------------------------------------------------- |
|   | Use of the hook scripts is intended only for DevOps professionals familiar with the products. |

The available hooks are built into the product images and can be found in the `hooks` subdirectory of each product directory in the [Docker Builds](https://github.com/pingidentity/pingidentity-docker-builds) repository.

In the `entrypoint.sh` startup script, there is an example (stub) provided for the available hooks for all products.

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It is **critical** that the supplied hook names be used if you modify `entrypoint.sh`. For example, they can be used to make subtle changes to a server profile. |

## Using .pre and .post hooks

When the hook scripts are called during the `entrypoint.sh` initialization, any corresponding `.pre` and `.post` hooks are also called.

The `.pre` and `.post` extensions allow you to define custom scripts to be executed before or after any hook that is run in the container. You can include any custom `.pre` and `.post` hooks in the `hooks` directory of your server profile.

Hooks with a `.pre` extension are run before the corresponding hook, and hooks with a `.post` extension are run after the corresponding hook.

For example, a script named `80-post-start.sh.pre` will execute immediately before the `80-post-start.sh` hook and a script named `80-post-start.sh.post` will be run immediately after that hook completes.

---

---
title: Variables and Scope
description: Understand the image, orchestration, server-profile, and container variable scopes and their precedence in Ping product containers
component: devops
page_id: devops::reference/variableScoping
canonical_url: https://developer.pingidentity.com/devops/reference/variableScoping.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  image-scope: Image scope
  devops-orchestration-scope: Orchestration scope
  devops-server-profile-scope: Server profile scope
  devops-container-scope: Container scope
  devops-scoping-example: Scoping example
---

# Variables and Scope

Variables provide a way to store and reuse values with our Docker containers which are ultimately used by our Docker image hooks to customize configurations.

It's important to understand:

* The different levels at which you can set variables

* How you should use variables

* Where you should set and use variables

The following diagram shows the different scopes in which variables can be set and applied.

![Variable Scoping](../_images/variableScoping-1.png)

Assume that you are viewing this diagram as a pyramid with the container at the top. The order of precedence for variables is top-down. Generally, you set variables having an orchestration scope.

## Image scope

Variables having an image scope are assigned using the values set for the Docker image (for example, from Dockerfiles). These variables are often set as defaults, allowing scopes with a higher level of precedence to override them.

To see the default environment variables available with any Docker image, enter:

`docker run pingidentity/<product-image>:<tag> env | sort`

Where \<product-image> is the name of one of our products, and \<tag> is the release tag (such as `edge`).

For the environment variables available for all products (PingBase) or individual products, see [Container Docker Images Information](../docker-images/dockerImagesRef.html).

## Orchestration scope

Variables having orchestration scope are assigned at the orchestration layer. Typically, these environment variables are set using Docker commands, Docker Compose or Helm values. For example:

* Using `docker run` with `--env`:

  ```
  docker run --env SCOPE=env \
    pingidentity/pingdirectory:edge env | sort
  ```

* Using `docker run` with `--env-file`:

  ```
  echo "SCOPE=env-file"  > /tmp/scope.properties

  docker run --env-file /tmp/scope.properties \
    pingidentity/pingdirectory:edge env | sort
  ```

* Using Docker Compose (docker-compose.yaml):

  ```
  environment:
    - SCOPE=compose
      env_file:
    - /tmp/scope.properties
  ```

* Using Kubernetes:

  ```
  env:
    - name: SCOPE
      value: kubernetes
  ```

* Using Helm variables:

  ```
  global:
    envs:
      PING_IDENTITY_ACCEPT_EULA: "YES"
      PING_IDENTITY_PASSWORD: "2Federate"
    ...
  ```

## Server profile scope

Variables having server profile scope are supplied using property files in the server-profile repository. You need to be careful setting variables at this level because the settings can override variables already having an image or orchestration scope value set.

You can use the following masthead in your `env_vars` files to provide examples of setting variables and how they might override variables having a scope with a lower level of precedence. It will also suppress a warning when processing the env\_vars file:

```
# .suppress-container-warning
#
# NOTICE: Settings in this file will override values set at the
#         image or orchestration layers of the container.  Examples
#         include variables that are specific to this server profile.
#
# Options include:
#
# ALWAYS OVERRIDE the value in the container
#   NAME=VAL
#
# SET TO DEFAULT VALUE if not already set
#   export NAME=${NAME:=myDefaultValue}  # Sets to string of "myDefaultValue"
#   export NAME=${NAME:-OTHER_VAR}       # Sets ot value of OTHER_VAR variable
#
```

## Container scope

Variables having a container scope are assigned in the hook scripts and will overwrite variables that are set elsewhere. Variables that need to be passed to other hook scripts must be appended to the file assigned to `${CONTAINER_ENV}`, (which defaults to `/opt/staging/.env`). This file is sourced by every hook script.

## Scoping example

![Variable Scoping](../_images/variableScoping-2.png)