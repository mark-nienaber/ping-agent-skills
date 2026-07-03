---
title: AWS
description: Before you can perform a ForgeOps deployment on a Kubernetes cluster running on AWS, you must complete these prerequisite tasks:
component: forgeops
version: 2026.2
page_id: forgeops:setup:aws
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/setup/aws.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  aws-repositories: forgeops and forgeops-extras repositories
  aws-third-party-software: Third-party software
  python_venv: Python venv
  docker-aws: Docker engine
  for_users_running_microsoft_windows: For users running Microsoft Windows
  environment: Setup for AWS
  aws-cluster: Kubernetes cluster creation
  aws-ingress: Hostname resolution
---

# AWS

Before you can [perform a ForgeOps deployment](../deploy/overview.html) on a Kubernetes cluster running on AWS, you must complete these prerequisite tasks:

* [Clone the `forgeops` and `forgeops-extras` repositories](#aws-repositories)

* [Install third-party software on your local computer](#aws-third-party-software)

* [Start a virtual machine that runs Docker engine on your local computer](#docker-aws)

* [Set up your AWS environment to meet the requirements for ForgeOps deployments](#environment)

* [Create a Kubernetes cluster in AWS](#aws-cluster)

* [Set up your local computer to access the cluster's ingress controller](#aws-ingress)

## `forgeops` and `forgeops-extras` repositories

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Learn more about configuring GitHub notifications [here](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) so you can get notified on ForgeOps releases. |

Get the `forgeops` and `forgeops-extras` repositories:

1. Clone the repositories. For example:

   ```
   $ git clone https://github.com/ForgeRock/forgeops.git
   $ git clone https://github.com/ForgeRock/forgeops-extras.git
   ```

   Both repositories are public; you do not need credentials to clone them.

2. Check out the `forgeops` repository's `2026.2.1` tag:

   ```
   $ cd /path/to/forgeops
   $ git checkout 2026.2.1
   ```

   Depending on your organization's repository strategy, you might need to clone the repository from a fork. You might also need to create a working branch from the `2026.2.1` tag of your fork. Learn more about [Repository Updates here](../start/repositories.html#forgeops-updates).

3. Check out the `forgeops-extras` repository's `main` branch:

   ```
   $ cd /path/to/forgeops-extras
   $ git checkout main
   ```

## Third-party software

Before performing a ForgeOps deployment, obtain third-party software and install it on your local computer.

ForgeOps team recommends that you install third-party software using [Homebrew](https://brew.sh/) on macOS and Linux'\[[1](#_footnotedef_1 "View footnote.")]' .

The versions listed in the following table have been validated for ForgeOps deployments on Amazon Web Services. Earlier and later versions will *probably* work. If you want to try using versions that are not in the table, it is your responsibility to validate them.

Install the following third-party software:

|                                         |         |                         |
| --------------------------------------- | ------- | ----------------------- |
| Software                                | Version | Homebrew package        |
| **On all platforms**                    |         |                         |
| * Python 3                              | 3.14.5  | `python@3`              |
| - Bash                                  | 5.3.9   | `bash`                  |
| * Docker client                         | 28.4.0  | `docker`                |
| - Kubernetes client (kubectl)           | 1.36.1  | `kubernetes-cli`        |
| * Kubernetes context switcher (kubectx) | 0.11.0  | `kubectx`               |
| - Kustomize                             | 5.8.1   | `kustomize`             |
| * Helm                                  | 4.2.0   | `helm`                  |
| - JSON processor jq                     | 1.8.1   | `jq`                    |
| * Setup tools (Python)                  | 82.0.1  | `python-setuptools`     |
| - Terraform                             | 1.12.2  | `terraform`             |
| **Additionally on Amazon EKS**          |         |                         |
| * Amazon AWS Command-line Interface     | 2.34.50 | `awscli`                |
| - AWS IAM Authenticator for Kubernetes  | 0.7.16  | `aws-iam-authenticator` |

### Python `venv`

The new `forgeops` utility is built on Python3. Some of the Python3 packages used by `forgeops` must be installed using `pip`. To separate such Python3 specific packages, Python recommends the use of the `venv` Python virtual environment. Learn more about Python `venv` in [venv - virtual environments](https://docs.python.org/3/library/venv.html).

1. Create a `venv` for using the `forgeops` utility\[[2](#_footnotedef_2 "View footnote.")].

   ```
   $ python3 -m venv .venv
   ```

2. Set up Python3 dependencies for `forgeops` utility.

   ```
   $ source .venv/bin/activate
   $ /path/to/forgeops/bin/forgeops configure
   ```

### Docker engine

In addition to the software listed in the preceding table, you'll need to start a virtual machine that runs Docker engine.

* On macOS systems, use [Docker Desktop](https://docs.docker.com/desktop/install/mac-install) or an alternative, such as [Colima](https://github.com/abiosoft/colima).

* On Linux systems, use [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/), install Docker machine from your Linux distribution, or use an alternative, such as [Colima](https://github.com/abiosoft/colima).

For more information about using Colima when performing ForgeOps deployments, refer to [this article](https://community.forgerock.com/t/deploying-forgeops-to-minikube-on-an-m1-mac-with-colima/3305/2).

The default configuration for a Docker virtual machine provides adequate resources for a ForgeOps deployment.

### For users running Microsoft Windows

ForgeOps deployments are supported on macOS and Linux. If you've a Windows computer, you'll need to create a Linux VM. We tested the following configurations:

* Hypervisor: Hyper-V, VMWare Player, or VMWare Workstation

* Guest OS: Current Ubuntu LTS release with 12 GB memory and 60 GB disk space

* Nested virtualization enabled in the Linux VM.

Perform all the procedures in this documentation within the Linux VM. In this documentation, the local computer refers to the Linux VM for Windows users.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The minikube implementation on Windows Subsystem for Linux (WSL2) has networking issues. As a result, consistent access to the ingress controller or the apps deployed on minikube is not possible. This issue is tracked [here](https://github.com/kubernetes/minikube/issues/7879). Do not attempt to perform ForgeOps deployments on WSL2 until this issue is resolved. |

## Setup for AWS

Perform these steps to set up an AWS environment that meets the requirements for ForgeOps deployments:

1. Create and configure an IAM group:

   1. Create a group with the name `forgeops-users`.

   2. Attach the following AWS preconfigured policies to the `forgeops-users` group:

      * `IAMUserChangePassword`

      * `IAMReadOnlyAccess`

      * `AmazonEC2FullAccess`

      * `AmazonEC2ContainerRegistryFullAccess`

      * `AWSCloudFormationFullAccess`

   3. Create two policies in the IAM service of your AWS account:

      1. Create the `EksAllAccess` policy using the `eks-all-access.json` file in the /path/to/forgeops/etc/aws-example-iam-policies directory.

      2. Create the `IamLimitedAccess` policy using the `iam-limited-access.json` file in the /path/to/forgeops/etc/aws-example-iam-policies directory.

   4. Attach the policies you created to the `forgeops-users` group.

      Remember, a ForgeOps deployment is a reference implementation. The policies you create in this procedure are suitable for ForgeOps deployments. When you [create a project plan](../start/start-here.html#planning), you'll need to determine how to configure AWS permissions.

   5. Assign one or more AWS users who will perform ForgeOps deployments to the `forgeops-users` group.

2. If you haven't already done so, set up your aws command-line interface environment using the aws configure command.

3. Verify that your AWS user is a member of the `forgeops-users` group:

   ```
   $ aws iam list-groups-for-user --user-name my-user-name --output json
   {
       "Groups": [
           {
               "Path": "/",
               "GroupName": "forgeops-users",
               "GroupId": "ABCDEFGHIJKLMNOPQRST",
               "Arn": "arn:aws:iam::048497731163:group/forgeops-users",
               "CreateDate": "2020-03-11T21:03:17+00:00"
           }
       ]
   }
   ```

4. Verify that you are using the correct user profile:

   ```
   $ aws iam get-user
   {
       "User": {
           "Path": "/",
           "UserName": "my-user-name",
           "UserId": "...",
           "Arn": "arn:aws:iam::01...3:user/my-user-name",
           "CreateDate": "2020-09-17T16:01:46+00:00",
           "PasswordLastUsed": "2021-05-10T17:07:53+00:00"
       }
   }
   ```

## Kubernetes cluster creation

ForgeOps provides Terraform artifacts for Amazon EKS cluster creation. Use them to create a cluster that supports ForgeOps deployments. After performing a ForgeOps deployment, you can use your cluster as a sandbox to explore Ping Advanced Identity Software customization.

When you [create a project plan](../start/start-here.html#planning), you'll need to identify your organization's preferred infrastructure-as-code solution, and, if necessary, create your own cluster creation automation scripts.

Here are the steps the ForgeOps team follows to create a Kubernetes cluster on Amazon EKS:

1. Copy the file that contains default Terraform variables to a new file:

   1. Change to the /path/to/forgeops-extras/terraform directory.

   2. Copy the terraform.tfvars file to override.auto.tfvars \[[3](#_footnotedef_3 "View footnote.")].

   Copying the terraform.tfvars file to a new file preserves the original content in the file.

2. []()Determine the cluster size: [small, medium, or large](../deploy/architecture.html#cluster-and-deployment-sizes).

3. Define your cluster's configuration:

   1. Open the override.auto.tfvars file.

   2. Determine the location of your cluster's configuration in the override.auto.tfvars file:

      | Cluster size | Section containing the cluster configuration |
      | ------------ | -------------------------------------------- |
      | Small        | `cluster.tf_cluster_eks_small`               |
      | Medium       | `cluster.tf_cluster_eks_medium`              |
      | Large        | `cluster.tf_cluster_eks_large`               |

   3. Modify your cluster's configuration by setting values in the section listed in the table:

      1. Modify your cluster's configuration by setting values in the section listed in the table:

      2. Set the value of the `enabled` variable to `true`.

      3. Set the value of the `meta.cluster_name` variable to the name of the Amazon EKS cluster you'll create.

      4. Set the values of the `location.region` and `location.zones` variables to the region and zones where you'll perform the ForgeOps deployment.

         Before continuing:

         * Go to the [Amazon Elastic Kubernetes Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/eks.html) page and verify the region you're specifying supports Amazon EKS.

         * Run the aws ec2 describe-availability-zones --region region-name command to identify three availability zones in your AWS region.

   4. Save and close the override.auto.tfvars file.

4. Ensure your region has an adequate CPU quota for a ForgeOps deployment.

   Locate these two variables in your cluster's configuration in the override.auto.tfvars file:

   * `node_pool.type`: the machine type to be used in your cluster

   * `node_pool.max_count`: the maximum number of machines to be used in your cluster

   Your quotas must be large enough to let you allocate the maximum number of machines in your region. If your quotas are too low, request and wait for a quota increase from Amazon Web Services before attempting to create your cluster.

5. Create a cluster using Terraform artifacts in the `forgeops-extras` repository:

   1. Change to the directory that contains Terraform artifacts:

      ```
      $ cd /path/to/forgeops-extras/terraform
      ```

   2. Run the tf-apply script to create your cluster:

      ```
      $ ./tf-apply
      ```

      Respond `yes` to the `Do you want to perform these actions?` prompt.

      When the tf-apply script finishes, it issues a message that provides the path to a kubeconfig file for the cluster.

      The script creates:

      * The EKS cluster

      * The `fast` storage class

      * The `ds-snapshot-class` volume snapshot class

      The script deploys:

      * An ingress controller

      * Certificate manager

6. Set your Kubernetes context to reference the new cluster by setting the `KUBECONFIG` environment variable as shown in the message from the tf-apply command's output.

7. To verify the tf-apply script created the cluster, log in to the AWS console. Access the console panel for the Amazon Elastic Kubernetes Service, and then list the EKS clusters. The new cluster should appear in the list of Kubernetes clusters.

## Hostname resolution

Set up hostname resolution for the Ping Advanced Identity Software servers you'll deploy in your namespace:

1. Get the ingress controller's FQDN from the `EXTERNAL-IP` column of the kubectl get services command output:

   ```
   $ kubectl get services --namespace traefik
   ```

2. Run the host command to get the ingress controller's external IP addresses. For example:

   ```
   $ host k8s-ingress ...elb.us-east-1.amazonaws.com
   k8s-ingress ...elb.us-east-1.amazonaws.com has address 3.210.123.210
   k8s-ingress ...elb.us-east-1.amazonaws.com has address 3.208.207.77
   k8s-ingress ...elb.us-east-1.amazonaws.com has address 44.197.104.140
   ```

   Depending on the state of the cluster, between one and three IP addresses appear in the host command's output.

3. Configure hostname resolution for the ingress controller:

   1. Choose an FQDN (referred to as the *deployment FQDN*) that you'll use when you deploy the Ping Advanced Identity Software, and when you access its GUIs and REST APIs.

      Some examples in this documentation use `forgeops.example.com` as the deployment FQDN. You are not required to use `forgeops.example.com`; you can specify any FQDN you like.

   2. If DNS doesn't resolve your deployment FQDN, add an entry to the /etc/hosts file that maps the ingress controller's external IP address to the deployment FQDN. For example:

      ```
      3.210.123.210 forgeops.example.com
      ```

***

[1](#_footnoteref_1). The Linux version of Homebrew doesn't support installing software it maintains as casks. Because of this, if you're setting up an environment on Linux, you won't be able to use Homebrew to install software in several cases. You'll need to refer to the software's documentation for information about how to install the software on a Linux system.[2](#_footnoteref_2). If you have updated Python3, you should delete the existing virtual environment and create a new one using the updated python3 version: rm -rf .venv && python3 -m venv .venv && ./bin/forgeops configure[3](#_footnoteref_3). The Terraform configuration contains a set of variables under `forgerock` that adds labels required for clusters created by Ping Identity employees. If you're a Ping Identity employee creating a cluster, set values for these variables.
