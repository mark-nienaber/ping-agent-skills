---
title: Consolidated ForgeOps documentation
description: The Ping Advanced Identity Software provides ForgeOps to help you deploy PingAM, PingDS, PingIDM, and PingGateway collectively in an integrated manner on a cloud platform that runs Kubernetes.
component: forgeops
version: 2026.2
page_id: forgeops::consolidated
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/consolidated.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  2026: 2026
  introduction_to_forgeops: Introduction to ForgeOps
  whats_new_in_forgeops_2026_2: What's new in ForgeOps 2026.2
  release_information: Release information
  highlights_in_2026_2_1_release: Highlights in 2026.2.1 release
  forgeops_release_notes: ForgeOps release notes
  june_29_2026: June 29, 2026
  forgeops-2026-2-1-features: ForgeOps 2026.2.1 release features
  forgeops_2026_2_0_release_features: ForgeOps 2026.2.0 release features
  validated_software_versions: Validated software versions
  kubernetes: Kubernetes
  forgeops_operators: ForgeOps operators
  limitations: Limitations
  platform-limitations: On all Ping Advanced Identity Software components
  ds-limitations: On PingDS
  am-limitations: On AM
  idm-limitations: On IDM
  ig-limitations: On PingGateway
  forgeops_repository_feature_evolution: forgeops repository feature evolution
  legal_notices: Legal notices
  about_ping_advanced_identity_software: About Ping Advanced Identity Software
  fontawesome_copyright: FontAwesome copyright
  start_here: Start here
  cdm-sandbox: Try an out-of-the-box ForgeOps deployment
  build-own-service: Build your own service
  planning: Create a project plan
  configure-platform: Configure the platform
  configure-cluster: Configure your cluster
  stay_up_and_running: Stay up and running
  assess_your_skill_level: Assess your skill level
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
  support_for_forgeops: Support for ForgeOps
  forgeops_support: ForgeOps support
  life-cycle: ForgeOps lifecycle policy
  forgeops-life-policy: ForgeOps product support lifecycle policy
  forgeops-image-support: Support for ForgeOps-provided images
  licensing: Licensing
  commercial-support: Support
  support-limitations: Support limitations
  kubernetes-services: Third-party Kubernetes services
  documentation_access: Documentation access
  problem_reports_and_information_requests: Problem reports and information requests
  suggestions_for_fixes_and_enhancements_to_artifacts: Suggestions for fixes and enhancements to artifacts
  contact_information: Contact information
  repositories: Repositories
  forgeops_repository: forgeops repository
  forgeops-updates: forgeops repository updates
  forgeops-reference: forgeops repository reference
  directories: Directories
  files_in_the_top_level_directory: Files in the top-level directory
  forgeops_extras_repository: forgeops-extras repository
  forgeops-extras-reference: forgeops-extras repository reference
  directories_2: Directories
  forgeops-fork: Git clone or Git fork?
  third-party-software: Third-party software
  required_third_party_software: Required third-party software
  forgeops_release_process: ForgeOps release process
  key_features: Key features
  setup_overview: Setup overview
  google_cloud: Google Cloud
  gcp-repositories: forgeops and forgeops-extras repositories
  gcp-third-party-software: Third-party software
  python_venv: Python venv
  docker-gcp: Docker engine
  for_users_running_microsoft_windows: For users running Microsoft Windows
  project: Google Cloud project setup
  gcp-cluster: Kubernetes cluster creation
  gcp-ingress: Hostname resolution
  aws: AWS
  aws-repositories: forgeops and forgeops-extras repositories
  aws-third-party-software: Third-party software
  python_venv_2: Python venv
  docker-aws: Docker engine
  for_users_running_microsoft_windows_2: For users running Microsoft Windows
  environment: Setup for AWS
  aws-cluster: Kubernetes cluster creation
  aws-ingress: Hostname resolution
  azure: Azure
  azure-repositories: forgeops and forgeops-extras repositories
  azure-third-party-software: Third-party software
  python_venv_3: Python venv
  docker-azure: Docker engine
  for_users_running_microsoft_windows_3: For users running Microsoft Windows
  subscription: Azure subscription setup
  azure-cluster: Kubernetes cluster creation
  azure-ingress: Hostname resolution
  minikube: minikube
  repository: forgeops repository
  minikube-third-party-software: Third-party software
  python_venv_4: Python venv
  docker-mini: Docker engine
  for_users_running_microsoft_windows_4: For users running Microsoft Windows
  minikube-cluster: minikube cluster
  minikube-ingress: Hostname resolution
  deployment_overview: Deployment overview
  next_step: Next step
  forgeops_architecture: ForgeOps architecture
  next_step_2: Next step
  forgeops_deployment: ForgeOps deployment
  deployment_technologies: Deployment technologies
  deployment_scenarios: Deployment scenarios
  deploy_using_helm_on_gke_eks_or_aks: Deploy using Helm on GKE, EKS, or AKS
  next_step_3: Next step
  deploy_using_helm_on_minikube: Deploy using Helm on minikube
  next_step_4: Next step
  deploy_using_kustomize_on_gke_eks_or_aks: Deploy using Kustomize on GKE, EKS, or AKS
  alt-techniques-kustomize-cloud: Alternative deployment techniques when using Kustomize
  staged_deployments: Staged deployments
  generating_kustomize_manifests_and_using_kubectl_apply_commands: Generating Kustomize manifests and using kubectl apply commands
  next_step_5: Next step
  deploy_using_kustomize_on_minikube: Deploy using Kustomize on minikube
  alt-techniques-kustomize-local: Alternative deployment techniques when using Kustomize
  staged_deployments_2: Staged deployments
  generating_kustomize_manifests_and_using_kubectl_apply_commands_2: Generating Kustomize manifests and using kubectl apply commands
  next_step_6: Next step
  ui_and_api_access: UI and API access
  am-services-cdm: AM services
  idm-services-cdm: IDM services
  ds_command_line_access: DS command-line access
  cdm-monitoring: ForgeOps deployment monitoring
  grafana: Grafana
  prometheus: Prometheus
  next_step_7: Next step
  next_steps: Next steps
  remove_a_forgeops_deployment: Remove a ForgeOps deployment
  helm-cloud: Remove a Helm deployment from GKE, EKS, or AKS
  helm-local: Remove a Helm deployment from minikube
  kustomize-cloud: Remove a Kustomize deployment from GKE, EKS, or AKS
  kustomize-local: Remove a Kustomize deployment from minikube
  customization_overview: Customization overview
  developer_checklist: Developer checklist
  additional_setup: Additional setup
  use_a_single_instance_forgeops_deployment: Use a single-instance ForgeOps deployment
  docker-push: Set up your environment to push to your Docker registry
  push-to: Identify the Docker repository to push to
  deploy-env-init: Initialize deployment environments
  next_step_8: Next step
  about_custom_images: About custom images
  in_development: In development
  in_production: In production
  next_step_9: Next step
  ds_image: ds image
  detailed_steps: Detailed steps
  next_step_10: Next step
  am_and_idm_images: am and idm images
  static-configuration: Static configuration
  dynamic-configuration: Dynamic configuration
  tips_for_managing_am_dynamic_configuration: Tips for managing AM dynamic configuration
  tips_for_managing_idm_dynamic_configuration: Tips for managing IDM dynamic configuration
  configuration-profiles: Configuration profiles
  next_step_11: Next step
  about_property_value_substitution: About property value substitution
  how_property_value_substitution_works: How property value substitution works
  export-config-expr: Export utilities and configuration expressions
  in_the_idm_configuration: In the IDM configuration
  in_the_am_configuration: In the AM configuration
  next_step_12: Next step
  am_image: am image
  customization_overview_2: Customization overview
  detailed_steps_2: Detailed steps
  redeploy-am-forgeops-command: "Redeploy AM: Kustomize deployments"
  redeploy-am-helm: "Redeploy AM: Helm deployments"
  next_step_13: Next step
  idm_image: idm image
  customization_overview_3: Customization overview
  detailed_steps_3: Detailed steps
  redeploy-idm-forgeops-command: "Redeploy IDM: Kustomize deployments"
  redeploy-idm-helm: "Redeploy IDM: Helm deployments"
  next_step_14: Next step
  prepare_to_deploy_in_production: Prepare to deploy in production
  pinggateway_deployment: PingGateway deployment
  deploy_pinggateway: Deploy PingGateway
  custom_pinggateway_image: Custom PingGateway image
  deploy_custom_pinggateway_image: Deploy custom PingGateway image
  customize_the_am_url_in_pinggateway: Customize the AM URL in PingGateway
  forgeops_deployment_monitoring: ForgeOps deployment monitoring
  about_forgeops_deployment_monitoring: About ForgeOps deployment monitoring
  monitoring_pods: Monitoring pods
  custom_grafana_dashboards: Custom Grafana dashboards
  alerts: Alerts
  security: Security
  secure_http: Secure HTTP
  tls-certificate: TLS certificate
  mkcert: Certificate generated by the mkcert utility
  access_restriction_by_ip_address: Access restriction by IP address
  network_policies: Network policies
  deny_all_policy: deny-all policy
  ds_idrepo_ldap_policy: ds-idrepo-ldap policy
  ds_cts_ldap_policy: ds-cts-ldap policy
  ds_replication_policy: ds-replication policy
  backend_http_access_policy: backend-http-access policy
  front_end_http_access_policy: front-end-http-access policy
  cluster_access_for_multiple_aws_users: Cluster access for multiple AWS users
  secret_agent_operator: Secret Agent operator
  secret_generation: Secret generation
  cloud-secret-management: Cloud secret management
  password-changes: Administration password changes
  secrets_rotation: Secrets Rotation
  introduction: Introduction
  performing_secrets_and_passwords_rotation: Performing secrets and passwords rotation
  rotating_ds_env_secrets: Rotating ds-env-secrets
  rotating_ds_passwords: Rotating ds-passwords
  rotating_amster_secret: Rotating amster secret
  rotating_am_env_secrets: Rotating am-env-secrets
  rotating_amster_env_secrets: Rotating amster-env-secrets
  rotating_idm_env_secrets: Rotating idm-env-secrets
  rotating_ds_ssl_keypair: Rotating ds-ssl-keypair
  rotating_am_passwords: Rotating am-passwords
  rotating_ds_master_keypair: Rotating ds-master-keypair
  add-cust-cert: Adding custom certificate to the truststore
  new_security_features: New security features
  backup_and_restore_overview: Backup and restore overview
  choose_a_backup_solution: Choose a backup solution
  backup_and_restore_using_volume_snapshots: Backup and restore using volume snapshots
  backup: Backup
  set_up_backup: Set up backup
  customize_the_backup_schedule: Customize the backup schedule
  restore_from_volume_snapshot: Restore from volume snapshot
  restore_examples: Restore examples
  dsbackup_utility: dsbackup utility
  dsbackup-backup: Back up using the dsbackup utility
  setup-cloud-storage: Set up cloud storage
  schedule-backups: Schedule backups
  dsbackup-restore: Restore
  new-deployment: New ForgeOps deployment using DS backup
  restore-all-directories: Restore all DS directories
  restore-one-directory: Restore one DS directory
  dr-restore: Restore a PingDS deployment after a disaster
  restore-best-practices: Best practices for restoring directories
  using_cloud_storage_locally_for_backup_and_restore: Using cloud storage locally for backup and restore
  upg-overview: Upgrade and Migration Overview
  troubleshooting: Troubleshooting
  kubernetes_logs_and_other_diagnostics: Kubernetes logs and other diagnostics
  debug_logs_utility: debug-logs utility
  example_troubleshooting_steps: Example troubleshooting steps
  ds_diagnostic_tools: DS diagnostic tools
  ds-debug: Debug script
  debug-tools-container: Debug tools container
  troubleshooting_the_amster_pod: Troubleshooting the amster pod
  start_the_amster_pod: Start the amster pod
  amster-retain: Export and import AM configuration
  staged_installation: Staged installation
  multiple_component_installation: Multiple component installation
  ingress_issues: Ingress issues
  third_party_software_versions: Third-party software versions
  expanded_kustomize_output: Expanded Kustomize output
  minikube_hardware_resources: minikube hardware resources
  cluster_configuration: Cluster configuration
  disk_space: Disk space
  kubectl_shell_autocompletion: kubectl shell autocompletion
  references: References
  base_docker_images: Base Docker images
  which_docker_images_do_i_deploy: Which Docker images do I deploy?
  base-images: Your initial base Docker images
  create_docker_images_for_use_in_production: Create Docker images for use in production
  the_forgeops_command: The forgeops command
  features_in_forgeops: Features in forgeops
  discrete_overlays: Discrete overlays
  image_defaulter_in_every_overlay: image-defaulter in every overlay
  sub_overlays: Sub-overlays
  specify_overlay_or_environment_to_target: Specify overlay or environment to target
  helm_support: Helm Support
  setup: Setup
  workflow: Workflow
  1_create_an_environment: 1. Create an environment
  2_build_images_for_the_environment: 2. Build images for the environment
  3_apply_the_environment: 3. Apply the environment
  forgeops_commands: forgeops commands
  forgeops_command_reference: forgeops command reference
  synopsis: Synopsis
  description: Description
  options: Options
  subcommands: Subcommands
  forgeops-apply: forgeops apply
  forgeops-build: forgeops build
  forgeops-delete: forgeops delete
  forgeops-env: forgeops env
  forgeops-image: forgeops image
  foregops-prereqs: forgeops prereqs
  secrets_reference: Secrets Reference
  am_configuration_passwords: AM configuration passwords
  kubernetes_secret_name_am_env_secret: "Kubernetes secret name: am-env-secret"
  am_secrets: AM secrets
  kubernetes_secret_name_am_keystore: "Kubernetes secret name: am-keystore"
  amster_secrets_keys_and_passwords: Amster secrets, keys, and passwords
  kubernetes_secret_name_amster: "Kubernetes secret name: amster"
  kubernetes_secret_name_amster_env_secrets: "Kubernetes secret name: amster-env-secrets"
  ds_secrets_keys_and_passwords: DS secrets, keys, and passwords
  kubernetes_secret_name_ds_env_secrets: "Kubernetes secret name: ds-env-secrets"
  kubernetes_secret_name_ds_passwords: "Kubernetes secret name: ds-passwords"
  kubernetes_secret_name_ds_master_keypair: "Kubernetes secret name: ds-master-keypair"
  kubernetes_secret_name_ds_ssl_keypair: "Kubernetes secret name: ds-ssl-keypair"
  idm_admin_passwords: IDM admin passwords
  kubernetes_secret_name_idm_env_secrets: "Kubernetes secret name: idm-env-secrets"
  forgeops_benchmarks: ForgeOps benchmarks
  forgeops_benchmarking_checklist: ForgeOps benchmarking checklist
  about_forgeops_benchmarking: About ForgeOps benchmarking
  next_step_15: Next step
  third_party_software: Third-party software
  next_step_16: Next step
  test_user_generation: Test user generation
  for_small_and_medium_clusters: For small and medium clusters
  for_large_clusters: For large clusters
  next_step_17: Next step
  authentication_rate: Authentication rate
  next_step_18: Next step
  oauth_2_0_authorization_code_flow: OAuth 2.0 authorization code flow
  congratulations: Congratulations!
  ingress: Ingress
  haproxy: HAProxy Ingress
  glossary: Glossary
  beyond_the_docs: Beyond the docs
  development_topics: Development topics
  deployment_topics: Deployment topics
  ds_topics: DS topics
  troubleshooting_2: Troubleshooting
  end_of_the_consolidated_file: End of the consolidated file
---

# Consolidated ForgeOps documentation

## Introduction to ForgeOps

The Ping Advanced Identity Software provides ForgeOps to help you deploy PingAM, PingDS, PingIDM, and PingGateway collectively in an integrated manner on a cloud platform that runs Kubernetes.

ForgeOps comprises mainly two sets of resources:

* The [forgeops repository](https://github.com/ForgeRock/forgeops.git)

  The repository contains artifacts that let you get a sample Ping Advanced Identity Software deployment up and running quickly. After you get the out-of-the-box deployment running, you can tailor it to explore how you might configure your Kubernetes cluster before you deploy the platform in production.

  ForgeOps deployments have the following characteristics:

  * Fully integrated AM, IDM, and DS installations

  * Multi-zone high availability'\[[1](#_footnotedef_1 "View footnote.")]'

  * Replicated directory services'\[[1](#_footnotedef_1 "View footnote.")]'

  * Ingress configuration'\[[2](#_footnotedef_2 "View footnote.")]'

  * Certificate management

  * Randomly generated secrets with ability to rotate secrets

  * Prometheus monitoring, Grafana reporting, and alert management'\[[1](#_footnotedef_1 "View footnote.")]'

* The [ForgeOps documentation](https://docs.pingidentity.com/forgeops/2026.2)

  The ForgeOps documentation helps you work with ForgeOps deployments:

  * Tells you how you can quickly [create a Kubernetes cluster](setup/overview.html) on Google Cloud, Amazon Web Services (AWS), or Microsoft Azure, [deploy the Ping Advanced Identity Software](deploy/deploy.html), and [access components in the deployment](deploy/access.html).

  * Contains [how-tos for preparing for production deployments](prepare/overview.html) by customizing monitoring, setting alerts, backing up and restoring directory data, modifying the default security configuration, and running lightweight benchmarks to test DS, AM, and IDM performance.

  * Tells you how to [modify the AM and IDM configurations](customize/overview.html) in ForgeOps deployments and create customized Docker images for the Ping Advanced Identity Software.

  * [Keeps you up-to-date with the latest changes to the `forgeops` repository](rn/rn.html).

Learn more about ForgeOps and the Ping Advanced Identity Software in <https://www.pingidentity.com/en/platform.html>.

## What's new in ForgeOps 2026.2

### Release information

#### Highlights in 2026.2.1 release

* The `main` branch contains pre-release artifacts

  The ForgeOps early adapter artifacts have been moved from the `dev` branch to the `main` branch of the [ForgeOps repository](https://github.com/ForgeRock/forgeops). The `main` branch will be the default branch for the ForgeOps repository.

  Note that the pre-release artifacts in the `main` branch are not meant for production use and are only meant for testing and providing feedback on the new features and changes.

  The `dev` branch that used to contain the pre-release artifacts is discontinued and will no longer be updated.

* Focus more on using Helm 4

  The `forgeops` utility now uses Helm 4 for deploying ForgeOps on Kubernetes. Helm 4 provides improved performance and security features compared to previous Helm versions. We recommend you use Helm in ForgeOps deployments rather than Kustomize.

* Security enabled by default

  The `forgeops` utility now enables security by default for new ForgeOps deployments. Learn more in [Enable security features](rn/rn.html#sec-2026-2-features).

* SBOM for ForgeOps images

  Software Bill of Materials (SBOM) is now available for ForgeOps images. SBOM provides a detailed inventory of the components and dependencies used in ForgeOps images, which can help you identify and manage security vulnerabilities and compliance issues.

* Images support update

  ForgeOps supports the latest available major or minor versions of the Ping Advanced Identity Software components. Learn more at [ForgeOps image support](start/support.html#forgeops-image-support).

* Further release information

  Learn more about this release in the [ForgeOps 2026.2.1 release notes](rn/rn.html#forgeops-2026-2-1-features).

## ForgeOps release notes

Subscribe to the [icon: rss-square, set=fa][ForgeOps 2026.2.1 RSS feed](https://docs.pingidentity.com/forgeops/latest/rn/rn.xml) to get notification when there's an update to the latest ForgeOps documentation.

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Learn more about configuring GitHub notifications [here](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) so you can get notified on ForgeOps releases. |

|                                                                                                                                                              |                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Validated Kubernetes, Ingress-NGINX Controller, HAProxy Ingress, cert-manager, and operator versions for deploying Ping Advanced Identity Software 2026.2    | [Link](rn/versions.html)                                           |
| Limitations when deploying Ping Advanced Identity Software `2026.2` on Kubernetes                                                                            | [Link](rn/limitations.html)                                        |
| More information about the evolving nature of the `forgeops` repository, including technology previews, legacy features, and feature deprecation and removal | [Link](rn/evolution.html)                                          |
| Legal notices                                                                                                                                                | [Link](rn/legal.html)                                              |
| Archive of release notes in ForgeOps 2026.1 are available from ForgeOps release 2026.1 documentation.                                                        | [Link](https://docs.pingidentity.com/forgeops/2026.1/rn/rn.html)   |
| Archive of release notes in ForgeOps 2025.1 and 2025.2 are available from ForgeOps release 2025.2 documentation.                                             | [Link](https://docs.pingidentity.com/forgeops/2025.2/rn/rn.html)   |
| Archive of release notes in 2024 and before are available from ForgeOps release 7.5 documentation.                                                           | [Link](https://docs.pingidentity.com/forgeops/7.5/rn/rn.html#2024) |
| Archive of release notes in 2023 and before are available from ForgeOps release 7.4 documentation                                                            | [Link](https://docs.pingidentity.com/forgeops/7.4/rn/rn.html#2023) |

### 2026

#### June 29, 2026

* Support policy for ForgeOps-provided Ping Advanced Identity Software images

  Support for ForgeOps-provided Ping Advanced Identity Software images has been clarified. Learn more in the [Support for ForgeOps-provided images](start/support.html#forgeops-image-support) section.

#### ForgeOps 2026.2.1 release features

* Updated the list of how-tos available in \`forgeops\`repository

  The list of [how-to articles](reference/how-tos.html) available in the `forgeops` repository has been updated in the documentation.

* SBOM for ForgeOps images

  Software Bill of Materials (SBOM) is now available for ForgeOps images. SBOM provides a detailed inventory of the components and dependencies used in ForgeOps images, which can help you identify and manage security vulnerabilities and compliance issues. Learn more in the [SBOM article](https://github.com/ForgeRock/forgeops/blob//2026.2.1/how-tos/retrieve-SBOMs-based-on-original-image-URL.md).

* Added self-signed certificate

  A self-signed certificate is now included for testing purposes in minikube environments.This certificate isn't intended for production use and should be used only in test environments.

* Avoid using secret generator

  There has been a lack of response from the secret generator project for questions and issues on using secret generator, we don't recommend or use it in ForgeOps environments. We'll be removing it from our artifacts in a future ForgeOps release. We've removed use of secret generator from ForgeOps documentation. Existing environments aren't affected by this change.

* IDM admin UI is deprecated in 8.1

  The IDM administration endpoint is deprecated in Ping Advanced Identity Software 8.1 and will be removed in a future release. You should use the identity Ping Advanced Identity Software admin UI or IDM REST API to administer user identities instead of the IDM admin UI. Learn more about this change in [Platform admin UI for standalone IDM](https://docs.pingidentity.com/pingidm/8.1/release-notes/whats-new.html#wn-platform-admin-ui-810).

#### ForgeOps 2026.2.0 release features

* Removed `ds-util` container

  The `ds-util` container has been removed because the same tasks can be performed directly on DS pods.

- Read-only root filesystem for init containers (Helm only)

  The init containers of all pods have been reconfigured to enable `readOnlyRootFilesystem` security context. This has no impact on deployments, but requires that DS stateful sets be recreated. To enable the `readOnlyRootFilesystem` security context, follow [these steps](#enable-sec-features).

- Flags to enable or disable security features (Helm only)

  You can enable or disable the new security features in your ForgeOps environment using the `--secure` or `--insecure` flags. By default, new environments are created with the `--secure` flag, so the new security features are enabled.

  The `temp` directory of Tomcat is writeable, so users can continue to edit scripts in AM admin UI even when security is enabled.

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | These flags can be enabled or disabled only in ForgeOps environments deployed using Helm. |

To enable the security features in an existing environment:

1. Run the `forgeops` command:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops env --env-name my-env --secure
   ```

2. Recreate the DS stateful set using the instructions in the [how to recreate an STS article](https://github.com/ForgeRock/forgeops/blob//2026.2.1/how-tos/recreating-ds-sts.md).

   * The platform pods deployed as non-root user using user ID

     The AM, DS, and IDM pods are now deployed as the standard non-root user ID `11111` and the username is no longer referred to. The user ID `11111` is a security standard across the platform. This user ID is set in the pod security context as the `runAsUser` property.

   * `PodDisruptionBudgets` for product components

     You can enable `PodDisruptionBudgets` for platform product components in the Helm charts for Ping Advanced Identity Software including PingGateway. This feature is disabled by default. You can enable it for each component by setting component.pdb.enabled: true in your values file.

     The default policy keeps at least one pod available by setting minAvailable: 1. You can change this value by appropriately changing the value of component.pdb.minAvailable or component.pdb.maxUnavailable.

     The affected components are: `am`, `idm`, `admin-ui`, `end-user-ui`, `login-ui`, `ds-idrepo`, `ds-cts` and `ig` (ping-gateway).

   * Supported Ping Advanced Identity Software images

     ForgeOps supports the last three major or minor versions of the Ping Advanced Identity Software images. With the availability of 8.1 images, ForgeOps supports 8.1, 8.0, and 7.5 versions of the platform images, and **7.4 images are no longer supported**.

     We recommend customers that upgrade to a newer version of the platform images. Use the [upgrade guide](https://docs.pingidentity.com/forgeops/2026.2/upgrade/upgrade-product.html) to upgrade to the latest image. The older tags remain available on <http://releases.forgeops.com> until the next major/minor release.

   * The `config export no-upgrade` topic is removed from documentation

     The `config export` functionality has been included in the forgeops config export command. Because the forgeops config export command already separates out the upgrade function, this topic is not required in the Troubleshooting section of the documentation. The `no-upgrade` option of `config export` topic is removed from the documentation.

   * New `ttl` options for use with `amster` and `ds-set-passwords` jobs

     The `amster` and `ds-set-passwords` jobs now have a time-to-live (TTL) option that you can set to retain these jobs for a specified time. This is useful for jobs that are run manually need and to be retained to run to completion. To use this feature, set the `ttlSecondsAfterFinished` option. The default is 7200 seconds.

     |   |                                                     |
     | - | --------------------------------------------------- |
     |   | This feature is available in new environments only. |

   * Ability to define `apiVersion`, `kind`, and `spec` for a secret

     You can now define the `apiVersion`, `kind`, and `spec` for secrets defined in the `platform.secrets`. This allows you to define secrets using `external-secrets`.

### Validated software versions

#### Kubernetes

The following Kubernetes versions have been validated for use with Ping Advanced Identity Software 2026.2:

| Cloud provider                          | Kubernetes version                                                                              |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Google Kubernetes Engine (GKE)          | 1.34                                                                                            |
| Amazon Elastic Kubernetes Service (EKS) | 1.34                                                                                            |
| Azure Kubernetes Service (AKS)          | 1.34                                                                                            |
| minikube                                | [The stable Kubernetes version for minikube](https://minikube.sigs.k8s.io/docs/commands/start). |

Earlier and later Kubernetes versions might also work. If you want to try using other Kubernetes versions, it's your responsibility to validate them.

The forgeops prereqs commmand is used to install the following prerequisites:

* Traefik version 3.6

* HAProxy Ingress controller version 0.14.5

* `cert-manager` version 1.13.0

If you install the prerequisites using a technique other than using the forgeops prereqs command, install prerequisites of this version. Newer versions might work, but they haven't been tested with Ping Advanced Identity Software 2026.2.

#### ForgeOps operators

ForgeOps has validated the following operator versions for use with Ping Advanced Identity Software 2026.2:

* [Secret Agent operator](https://github.com/ForgeRock/secret-agent) — version 1.2.10

* [DS operator](https://github.com/ForgeRock/ds-operator) — version 0.3.0

### Limitations

This page documents limitations on the Ping Advanced Identity Software when deployed on a Kubernetes cluster in the cloud.

#### On all Ping Advanced Identity Software components

* The forgeops config export command doesn't handle object deletion correctly.

  Configuration objects, such as AM authentication trees and service definitions, aren't deleted correctly by the forgeops config export command. If you've deleted one or more objects from your Ping Advanced Identity Software configuration in a single-instance deployment, and then you export the configuration, the deleted objects continue to exist in your configuration profile.

  To work around this problem, locate the deleted objects in your configuration profile after you've run the forgeops config export command. Then, delete the objects that should've been deleted from the JSON configuration files. After deleting the objects, if you build a new Docker image based on your configuration profile, the new image won't contain the deleted objects.

#### On PingDS

* PingDS live data and logs should reside on fast disks.

  PingDS data requires high performant, low latency disks. Use external volumes on solid-state drives (SSDs) for directory data when running in production. Don't use network file systems such as NFS.

* Adding DS pods to a cluster should be done in advance of anticipated additional load.

  When you increase the number of DS pods in a cluster, they're automatically provisioned with the same directory data in existing pods. You must allow time for the data provisioning to complete and new pods to become available.

* Database encryption isn't supported.

  The `ds` Docker image doesn't support database encryption. DS fails to start if it detects that any data was encrypted during the Docker build process.

* DS starts successfully even when it can't decrypt a backend.

  When the DS master key isn't available, DS starts up successfully even though it's unable to decrypt a backend.

* Root file system write access is required to run the DS Docker image.

  The DS Docker image won't run without root file system write access.

#### On AM

* AM must be reconfigured and restarted if the number of DS pods changes.

  In DS 8.1.0, you can elastically scale the number of DS pods in Kubernetes. However, the AM configuration doesn't automatically respond to changes in the number of DS pods.

  Because of this, you must modify the AM configuration after you scale the number of `idrepo` or `cts` pods in a running AM deployment.

* Using subrealms in ForgeOps deployments requires additional considerations.

  If you decide to deploy AM with subrealms, you'll need to configure the subrealms in the DS repository before starting AM. Make the LDAP configurations for the AM backend in [the relevant backend ldap configuration files](https://github.com/ForgeRock/forgeops/blob/main/docker/ds/ldif-ext/am-config/external-am-datastore.ldif).

* Session stickiness is required for some deployments.

  Two AM features are stateful, and require you to configure your load balancer to use sticky sessions:

  * SAML v2.0 single logout.

  * Browser-based authentication using authentication chains, which is deprecated in AM 8.1.0. Note that AM authentication trees are not stateful, and don't have this limitation.

  ForgeOps recommends that you configure your load balancer to use sticky sessions to achieve better performance. In the default ForgeOps deployment, Traefik is already configured with session stickiness.

* Value substitution is supported only for some configuration properties.

  AM doesn't support [property value substitution](customize/value-substitution.html) for several types of configuration properties. Refer to [Property value substitution](https://docs.pingidentity.com/pingam/8/setup-guide/property-value-substitution.html) in the AM documentation for more information.

* The SOAP binding isn't supported for SAML v2.0 single logout.

  When deploying SAML v2.0 single logout, use the HTTP-POST or HTTP-Redirect bindings. The SOAP binding isn't supported when AM runs in a container.

* The shared identity repository isn't preconfigured for UMA deployments.

  The shared identity repository deployed with the CDK and the CDM isn't preconfigured to store UMA objects, such as resources, labels, audit messages, and pending requests.

  In order to use UMA in the CDK or the CDM, you'll need to customize your deployment. For more information, refer to the [*User-Managed Access (UMA) 2.0 Guide*](https://docs.pingidentity.com/pingam/8/uma-guide).

#### On IDM

* The IDM repository is deployed in a single master topology.

  IDM can actively use only a single instance of DS as its repository. Should the DS instance fail, IDM can fail over to another DS instance; the limitation that only a single instance can be active applies. Using multiple DS replicas at the same time isn't supported.

* ForgeOps deployments aren't preconfigured to support IDM's workflow engine.

  ForgeOps deployments use DS as the IDM repository. Because of this, these deployments don't support IDM's workflow engine, and workflow features are disabled.

  Adding workflow support to ForgeOps deployments requires substantial, complex configuration changes, including:

  * Adding a JDBC repository to the ForgeOps deployment.

  * Enabling workflow features in IDM.

#### On PingGateway

There are no limitations for this release.

### `forgeops` repository feature evolution

All the features demonstrated in the `forgeops` repository evolve continuously, and should be expected to change, potentially in backwards-incompatible ways. Specific changes are documented in the [ForgeOps release notes](rn/rn.html), and might go through the following stages:

| Stage              | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Technology Preview | *Technology previews* provide access to new technology that is not yet supported. Technology preview features may be functionally incomplete, and the function as implemented is subject to change without notice. *DO NOT DEPLOY FEATURES MARKED AS BEING IN TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.* You are encouraged to test drive technology preview features in a non-production environment, and are welcome to make comments and suggestions about the features. ForgeOps doesn't guarantee that a technology preview feature will be present at a future time. The final complete version of the feature is liable to change between preview and the final version. Technology previews are provided on an "as is" basis for evaluation purposes only, and Ping Identity accepts no liability or obligations for the use thereof. |
| Evolving           | All features that are not in technology preview, legacy, deprecated, or removed status are considered to be *evolving*. Evolving features might change at any time, even in backwards-incompatible ways. Evolving features in the `forgeops` repository might or might not be supported. Learn more in [Support for ForgeOps](start/support.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Legacy             | Features in *legacy* status have been replaced with improved versions, and are no longer being developed by ForgeOps. You should migrate to the newer version; however the existing functionality will remain. Legacy features or interfaces are marked as *Deprecated* if they are scheduled to be removed. Legacy features in the `forgeops` repository might or might not be supported. Learn more in [Support for ForgeOps](start/support.html).                                                                                                                                                                                                                                                                                                                                                                                                  |
| Deprecated         | *Deprecated* features are likely to be removed in future versions of the repository. Deprecated features in the `forgeops` repository might or might not be supported. Learn more in [Support for ForgeOps](start/support.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Removed            | Removed features were previously deprecated, and have now been removed. Features that have been removed from the `forgeops` repository are not supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Legal notices

Click [here](https://backstage.forgerock.com/knowledge/backstagehelp/article/a81642400) for legal information about product documentation published by Ping Identity.

#### About Ping Advanced Identity Software

The Ping Advanced Identity Software serves as the basis for our simple and comprehensive identity and access management solution. We help our customers deepen their relationships with their customers, and improve the productivity and connectivity of their employees and partners. Learn more about ForgeOps and about the platform in <https://www.pingidentity.com/en/platform.html>.

The platform includes the following components:

* PingAM, previously ForgeRock® Access Management (AM)

* PingIDM, previously ForgeRock® Identity Management (IDM)

* PingDS, previously ForgeRock® Directory Services (DS)

* PingGateway, previously ForgeRock® Identity Gateway (IG)

#### FontAwesome copyright

Copyright © 2017 by Dave Gandy, <https://fontawesome.com/>. This Font Software is licensed under the SIL Open Font License, Version 1.1. Refer to <https://opensource.org/license/openfont-html/>.

## Start here

Ping Identity provides several resources to help you get started in the cloud. These resources demonstrate how to deploy the Ping Advanced Identity Software on Kubernetes. Before you proceed, review the following precautions:

* Deploying Ping Advanced Identity Software in a containerized environment requires advanced proficiency in many technologies. Learn more about the required skills in [Assess Your Skill Level](start/start-here-skills.html).

* If you don't have experience with complex Kubernetes deployments, then either engage a certified Ping Advanced Identity Software consulting partner or deploy the platform on traditional architecture.

* Don't deploy Ping Advanced Identity Software in Kubernetes in production until you've successfully deployed and tested the software in a non-production Kubernetes environment.

Learn more about getting support for Ping Advanced Identity Software in [Support for ForgeOps](start/support.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

### Try an out-of-the-box ForgeOps deployment

Before you start planning a production deployment, perform a ForgeOps deployment without any customizations. If you're new to Kubernetes, or new to the Ping Advanced Identity Software, it's a great way to learn, and you'll have a sandbox suitable for exploring the Ping Advanced Identity Software in a cloud environment.

![Illustrates major tasks when performing a ForgeOps deployment.](start/_images/start-cdm.png)

Perform a ForgeOps deployment on Google Cloud, AWS, or Microsoft Azure to quickly spin up the platform for demonstration purposes. You'll get a feel for what it's like to deploy the platform on a Kubernetes cluster in the cloud. When you're done, you'll have a robust starter deployment that you can use to test deployment customizations that you'll need for your production environment. Examples of deployment customizations include, but are not limited to:

* Running lightweight benchmark tests

* Making backups of data and restoring the data

* Securing TLS with a certificate that's dynamically obtained from Let's Encrypt

* Using an ingress controller other than Traefik

* Resizing the cluster to meet your business requirements

* Configuring Alert Manager to issue alerts when usage thresholds have been reached

Prerequisite technologies and skills:

* [Git](start/start-here-skills.html#skills-git)

* [Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-cdm-cloud-provider)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-cdk-kubernetes)

More information:

* [Setup overview](setup/overview.html)

### Build your own service

![Illustrates the major tasks performed when building a production deployment of ${platform.name} in the cloud.](start/_images/dg-start-overview.png)

Perform the following activities to customize, deploy, and maintain a production Ping Advanced Identity Software implementation in the cloud:

#### Create a project plan

![Illustrates the major tasks performed when planning a production deployment of ${platform.name} in the cloud.](start/_images/start-plan.png)

After you've spent some time [exploring a ForgeOps deployment](#cdm-sandbox), you're ready to define requirements for your production deployment. *Remember, an out-of-the-box ForgeOps deployment is not a production deployment*. Use out-of-the-box ForgeOps deployments to explore deployment customizations. Then, incorporate the lessons you've learned as you build your own production service.

Analyze your business requirements and define how the Ping Advanced Identity Software needs to be configured to meet your needs. Identify systems to be integrated with the platform, such as identity databases and applications, and plan to perform those integrations. Assess and specify your deployment infrastructure requirements, such as backup, system monitoring, Git repository management, CI/CD, quality assurance, security, and load testing.

Be sure to do the following when you transition to a production environment:

* Obtain and use certificates from an established certificate authority.

* Create and test your backup plan.

* Use a working production-ready FQDN.

* Implement monitoring and alerting utilities.

Prerequisite technologies and skills:

* [Project planning and management](start/start-here-skills.html#skills-proj-plan)

* [Git](start/start-here-skills.html#skills-git)

* [Docker](start/start-here-skills.html#skills-docker)

* [Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-prod-cloud-provider)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-prod-kubernetes)

* [Ping Advanced Identity Software](start/start-here-skills.html#skills-platform)

* [Applications and databases that you plan to integrate with Ping Advanced Identity Software](start/start-here-skills.html#skills-integration)

* [CI/CD for a production deployment in the cloud](start/start-here-skills.html#skills-cicd)

* [Integration testing](start/start-here-skills.html#skills-integration-test)

* [Deployment hardening and security](start/start-here-skills.html#skills-security)

* [Benchmarking and load testing](start/start-here-skills.html#skills-benchmarking)

* [Site reliability](start/start-here-skills.html#skills-sr)

More information:

* [All the ForgeOps documentation](index.html)

#### Configure the platform

![Illustrates the major tasks performed to configure the ${platform.name} before deploying in production.](start/_images/start-config-platform.png)

With your [project plan defined](#planning), you're ready to configure the Ping Advanced Identity Software to meet the plan's requirements. Install single-instance ForgeOps deployments on your developers' computers. Configure AM and IDM. If needed, include integrations with external applications in the configuration. Iteratively unit test your configuration as you modify it. Build customized Docker images that contain the configuration.

Prerequisite technologies and skills:

* [Ping Advanced Identity Software](start/start-here-skills.html#skills-platform)

* [Git](start/start-here-skills.html#skills-git)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-prod-kubernetes)

* [Docker](start/start-here-skills.html#skills-docker)

More information:

* [Customization overview](customize/overview.html)

#### Configure your cluster

![Illustrates the major tasks performed to configure the cluster before deploying in production.](start/_images/start-config-cluster.png)

With your [project plan defined](#planning), you're ready to configure a Kubernetes cluster that meets the requirements defined in the plan. Install the platform using the customized Docker images developed in [Configure the platform](#configure-platform). Provision the identity repository with users, groups, and other identity data. Load test your deployment, and then size your cluster to meet service level agreements. Perform integration tests. Harden your deployment. Set up CI/CD for your deployment. Create monitoring alerts so that your site reliability engineers are notified when the system reaches thresholds that affect your SLAs. Implement database backup and test database restore. Simulate failures while under load to make sure your deployment can handle them.

Prerequisite technologies and skills:

* [Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-prod-cloud-provider)

* [Git](start/start-here-skills.html#skills-git)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-prod-kubernetes)

* [Ping Advanced Identity Software](start/start-here-skills.html#skills-platform)

* [CI/CD for a production deployment in the cloud](start/start-here-skills.html#skills-cicd)

* [Integration testing](start/start-here-skills.html#skills-integration-test)

* [Deployment hardening and security](start/start-here-skills.html#skills-security)

* [Kubernetes backup and restore](start/start-here-skills.html#skills-kubernetes-backup)

* [Benchmarking and load testing](start/start-here-skills.html#skills-benchmarking)

* [Site reliability](start/start-here-skills.html#skills-sr)

More information:

* [Prepare to deploy in production](prepare/overview.html)

* [Setup overview](setup/overview.html)

#### Stay up and running

![Illustrates the major tasks performed to keep a ${platform.name} deployment up and running in production.](start/_images/start-sr.png)

By now, you've [configured the platform](#configure-platform), [configured a Kubernetes cluster](#configure-cluster), and deployed the platform with your customized configuration. Run your Ping Advanced Identity Software deployment in your cluster, continually monitoring it for performance and reliability. Take backups as needed.

Prerequisite technologies and skills:

* [Git](start/start-here-skills.html#skills-git)

* [Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-prod-cloud-provider)

* [Kubernetes, running on Google Cloud, AWS, or Azure](start/start-here-skills.html#skills-prod-kubernetes)

* [Ping Advanced Identity Software](start/start-here-skills.html#skills-platform)

* [CI/CD for a production deployment in the cloud](start/start-here-skills.html#skills-cicd)

* [Kubernetes backup and restore](start/start-here-skills.html#skills-kubernetes-backup)

* [Site reliability](start/start-here-skills.html#skills-sr)

More information:

* [Prepare to deploy in production](prepare/overview.html)

### Assess your skill level

#### Benchmarking and load testing

I can:

* Write performance tests, using tools such as Gatling and Apache JMeter, to ensure that the system meets required performance thresholds and service level agreements (SLAs).

* Resize a Kubernetes cluster, taking into account performance test results, thresholds, and SLAs.

* Run Linux performance monitoring utilities, such as top.

#### CI/CD for cloud deployments

I have experience:

* Designing and implementing a CI/CD process for a cloud-based deployment running in production.

* Using a cloud CI/CD tool, such as Tekton, Google Cloud Build, Codefresh, AWS CloudFormation, or Jenkins, to implement a CI/CD process for a cloud-based deployment running in production.

* Integrating GitOps into a CI/CD process.

#### Docker

I know how to:

* Write Dockerfiles.

* Create Docker images, and push them to a private Docker registry.

* Pull and run images from a private Docker registry.

I understand:

* The concepts of Docker layers, and building images based on other Docker images using the FROM instruction.

* The difference between the COPY and ADD instructions in a Dockerfile.

#### Git

I know how to:

* Use a Git repository collaboration framework, such as GitHub, GitLab, or Bitbucket Server.

* Perform common Git operations, such as cloning and forking repositories, branching, committing changes, submitting pull requests, merging, viewing logs, and so forth.

#### External application and database integration

I have expertise in:

* AM policy agents.

* Configuring AM policies.

* Synchronizing and reconciling identity data using IDM.

* Managing cloud databases.

* Connecting Ping Advanced Identity Software components to cloud databases.

#### Ping Advanced Identity Software

I have:

* Attended Ping Identity University training courses.

* Deployed the Ping Advanced Identity Software in production, and kept the deployment highly available.

* Configured DS replication.

* Passed the Certified Access and Identity Management exams from Ping Identity (highly recommended).

#### Google Cloud, AWS, or Azure (basic)

I can:

* Use the graphical user interface for Google Cloud, AWS, or Azure to navigate, browse, create, and remove Kubernetes clusters.

* Use the cloud provider's tools to monitor a Kubernetes cluster.

* Use the command user interface for Google Cloud, AWS, or Azure.

* Administer cloud storage.

#### Google Cloud, AWS, or Azure (expert)

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

#### Integration testing

I can:

* Automate QA testing using a test automation framework.

* Design a chaos engineering test for a cloud-based deployment running in production.

* Use chaos engineering testing tools, such as Chaos Monkey.

#### Kubernetes (basic)

I've gone through the tutorials at kubernetes.io, and am able to:

* Use the kubectl command to determine the status of all the pods in a namespace, and to determine whether pods are operational.

* Use the kubectl describe pod command to perform basic troubleshooting on pods that are not operational.

* Use the kubectl command to obtain information about namespaces, secrets, deployments, and stateful sets.

* Use the kubectl command to manage persistent volumes and persistent volume claims.

#### Kubernetes (expert)

In addition to the [basic skills for Kubernetes](#skills-cdk-kubernetes), I have:

* Configured role-based access to cloud resources.

* Configured Kubernetes objects, such as deployments and stateful sets.

* Configured Kubernetes ingresses.

* Configured Kubernetes resources using Kustomize.

* Passed the Cloud Native Certified Kubernetes Administrator exam (highly recommended).

#### Kubernetes backup and restore

I know how to:

* Schedule backups of Kubernetes persistent volumes on volume snapshots.

* Restore Kubernetes persistent volumes from volume snapshots.

I have experience with one or more of the following:

* Volume snapshots on Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (EKS), or Azure Kubernetes Service (AKS)

* A third-party Kubernetes backup and restore product, such as Velero, Kasten K10, TrilioVault, Commvault, or Portworx PX-Backup.

#### Project planning and management for cloud deployments

I have planned and managed:

* A production deployment in the cloud.

* A production deployment of Ping Advanced Identity Software.

#### Security and hardening for cloud deployments

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

#### Site reliability engineering for cloud deployments

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

### Support for ForgeOps

This appendix contains information about support options for ForgeOps deployments and the Ping Advanced Identity Software.

#### ForgeOps support

The Ping Identity ForgeOps team has developed artifacts in the [forgeops](https://github.com/ForgeRock/forgeops/tree/2026.2.1) and [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) Git repositories for deploying the Ping Advanced Identity Software in the cloud. The companion [ForgeOps documentation](index.html) provides examples to help you get started.

These artifacts and documentation are provided on an as-is basis. Ping Identity doesn't guarantee the individual success developers may have in implementing the code on their development platforms or in production configurations.

##### ForgeOps lifecycle policy

When a Ping Advanced Identity Software product has been deployed using ForgeOps, the product support lifecycle policy and timeline that applies to that product continues to apply regardless of the deployment type. These support policies relate to the Ping Advanced Identity Software product only and not the underlying container operating system. Therefore, refer to the support lifecycle policy for the relevant Ping Advanced Identity Software product support lifecycle:

* [Support lifecycle policy for PingAM, PingDS, PingIDM, and IGA](https://support.pingidentity.com/s/article/Ping-Identity-Product-Support-Lifecycle-Policy-PingAM-PingDS-PingIDM-and-IGA).

* [Support lifecycle policy for PingGateway and Agents](https://support.pingidentity.com/s/article/Ping-Identity-Product-Support-Lifecycle-Policy-PingGateway-and-Agents).

The support for the underlying container operating system is covered by the [ForgeOps product support lifecycle policy](#forgeops-life-policy).

###### ForgeOps product support lifecycle policy

ForgeOps product support lifecycle policy refers to the versions of the Ping Advanced Identity Software products that are supported by ForgeOps in ForgeOps version 2025.1 and later. ForgeOps will provide support for the last 3 minor or major versions of the Ping Advanced Identity Software products.

* Supported

  ForgeOps will continue to deliver supported images for the latest available patch version of the platform product. For example, if versions 7.5.0 and 7.5.1 are available, ForgeOps provides scanned and patched images only for 7.5.1. These patched images deal with OS level vulnerabilities only and not the Ping Advanced Identity Software products. With the availability of 8.1 images, ForgeOps supports 8.1, 8.0, and 7.5 versions of the platform images, and **7.4 images are no longer supported**.

* Maintained

  ForgeOps tooling continues to have access to the last three versions of the Ping Advanced Identity Software products whether it's supported or not.

  | Version | Release Date | Lifecycle Stage | Supported?                          | Maintained?                         | EOS Start Date |
  | ------- | ------------ | --------------- | ----------------------------------- | ----------------------------------- | -------------- |
  | 8.1     | Apr 21, 2026 | Active          | [icon: check-circle, set=fa]**Yes** | [icon: check-circle, set=fa]**Yes** |                |
  | 8.0     | Apr 7, 2025  | Active          | [icon: check-circle, set=fa]**Yes** | [icon: check-circle, set=fa]**Yes** |                |
  | 7.5     | Apr 2, 2024  | Active          | [icon: check-circle, set=fa]**Yes** | [icon: check-circle, set=fa]**Yes** |                |
  | 7.4     | Oct 9, 2023  | Active          | [icon: times-circle, set=fa]**No**  | [icon: check-circle, set=fa]**Yes** |                |

###### Support for ForgeOps-provided images

ForgeOps supports the latest ForgeOps-provided image for each major or minor version of the supported Ping Advanced Identity Software component. ForgeOps support is limited to ForgeOps-provided image lines. Customers should therefore plan to use the newest published ForgeOps image in a supported version stream, rather than expect vulnerability fixes to be backported to older patch images.

The ForgeOps team scans daily for critical and high severity vulnerabilities in the latest published image for each supported minor version. The team then publishes a new image when upstream fixes are available that can be applied within the currently supported base operating system version. If a vulnerability fix requires moving to a newer operating system version, the change isn't applied in place on the existing image line. Instead, the fix is applied in the next major or minor version of the image, and is made available in the product team's next release, according to that product's release cycle and support commitments.

If your corporate compliance mandates a zero known Common Vulnerabilities and Exposures (zero-CVE) footprint or immediate remediation SLAs that differ from Ping's product lifecycle, you should consider building and managing your own base images, as documented in [Base Docker images](reference/base-docker-images.html). This gives you more direct control over base image selection, update timing, and remediation policy.

##### Licensing

Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html).

##### Support

Ping Identity provides support for the following resources:

* Docker images provided by the ForgeOps team.

* Artifacts in the [forgeops](https://github.com/ForgeRock/forgeops/tree/2026.2.1) Git repository:

  * Files used to build Docker images for the Ping Advanced Identity Software:

    * Dockerfiles

    * Scripts and configuration files incorporated into the Docker images provided by ForgeOps

    * Canonical configuration profiles for the platform

  * Helm charts

  * Kustomize bases and overlays

* [ForgeOps Documentation](index.html)

For more information about support for specific directories and files in the `forgeops` repository, refer to the [`forgeops` repository reference](start/repositories.html#forgeops-reference).

Ping Identity provides support for the Ping Advanced Identity Software. For supported components, containers, and Java versions, refer to the following:

* [PingAM Release Notes](https://docs.pingidentity.com/pingam//release-notes/preface.html)

* [PingIDM Release Notes](https://docs.pingidentity.com/pingidm/8.1/release-notes/preface.html)

* [PingDS Release Notes](https://docs.pingidentity.com/pingds//release-notes/preface.html)

* [PingGateway Release Notes](https://docs.pingidentity.com/pinggateway//release-notes/preface.html)

##### Support limitations

Ping Identity provides no support for the following:

* Artifacts in the [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) repository. For more information about support for specific directories and files in the `forgeops-extras` repository, refer to the [`forgeops-extras` repository reference](start/repositories.html#forgeops-extras-reference).

* Artifacts other than Dockerfiles, Helm charts, Kustomize bases, and Kustomize overlays in the [forgeops](https://github.com/ForgeRock/forgeops/tree/2026.2.1) Git repository. Examples include scripts, example configurations, and so forth.

* Infrastructure outside Ping Identity. Examples include Docker, Kubernetes, Google Cloud Platform, Amazon Web Services, Microsoft Azure, and so forth.

* Software outside Ping Identity. Examples include Java, Apache Tomcat, Traefik, Apache HTTP Server, Certificate Manager, Prometheus, and so forth.

* Deployments that deviate from the [published ForgeOps architecture](deploy/architecture.html). Deployments that do not include the following architectural features are not supported:

  * PingAM and PingIDM are integrated and deployed together in a Kubernetes cluster.

  * PingIDM login is integrated with PingAM.

  * PingAM uses PingDS as its data repository.

  * PingIDM uses PingDS as its repository.

* Ping Identity publishes Docker images for testing and development. For production deployments, it is recommended that customers build and run containers using a [supported operating system](https://support.pingidentity.com/s/article/What-operating-systems-are-PingAM-PingDS-PingIDM-and-PingGateway-supported-on), required software dependencies, and their customized platform component configurations.

##### Third-party Kubernetes services

The ForgeOps reference tools are provided for use with Google Kubernetes Engine, Amazon Elastic Kubernetes Service, and Microsoft Azure Kubernetes Service.

Ping Identity supports running the platform on other Kubernetes platforms such as IBM RedHat OpenShift. However, ForgeOps reference tools are not provided on these platforms, and customers must build, maintain, and support their own tools and configurations.

Ping Identity doesn't support Kubernetes itself. Customers must have a support contract in place with their Kubernetes vendor to resolve infrastructure issues. To avoid any misunderstandings, it must be clear that Ping Identity cannot troubleshoot underlying Kubernetes issues.

Modifications to ForgeOps deployment assets may be required to adapt the platform to the customer's Kubernetes implementation. For example, ingress routes, storage classes, NAT gateways, etc., might need to be modified. Making the modifications requires competency in Kubernetes and familiarity with their chosen distribution.

#### Documentation access

Ping Identity publishes comprehensive documentation online:

* The [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Advanced Identity Software.

  While many articles are visible to community members, Ping Identity customers have access to much more, including advanced information for customers using Ping Advanced Identity Software in a mission-critical capacity.

* The developer documentation, such as this site, aims to be technically accurate with respect to the sample that is documented. It is visible to everyone.

#### Problem reports and information requests

If you are a named customer Support Contact, contact Ping Identity using the [Customer Support Portal](https://support.pingidentity.com/s/) to request information or report a problem with Dockerfiles, Helm charts, Kustomize bases, or Kustomize overlays in the `forgeops` repository.

When requesting help with a problem, include the following information:

* Description of the problem, including when the problem occurs and its impact on your operation.

* Steps to reproduce the problem.

  If the problem occurs on a Kubernetes system other than minikube, GKE, EKS, or AKS, we might ask you to reproduce the problem on one of those.

* HTML output from the debug-logs command. For more information, refer to [Kubernetes logs and other diagnostics](troubleshoot/pods.html).

#### Suggestions for fixes and enhancements to artifacts

ForgeOps greatly appreciates suggestions for fixes and enhancements to ForgeOps-provided artifacts in the [forgeops](https://github.com/ForgeRock/forgeops/tree/2026.2.1) and [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) repositories.

If you would like to report a problem with or make an enhancement request for an artifact in either repository, create a GitHub issue in the repository.

#### Contact information

Ping Identity provides support services, professional services, training through Ping Identity training, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, refer to <https://www.pingidentity.com/en/platform.html>.

Ping Identity has staff members around the globe who support our international customers and partners. Learn more about Ping Identity's support offering, including support plans and service-level agreements (SLAs) in the [Ping Advanced Identity Software support page](https://support.pingidentity.com/s/).

### Repositories

The ForgeOps project provides two public GitHub repositories; the `forgeops` and `forgeops-extras` repositories.

This page provides a high-level overview of the two repositories.

#### `forgeops` repository

The [`forgeops` repository](https://github.com/ForgeRock/forgeops.git) contains files needed for customizing and deploying the Ping Advanced Identity Software on a Kubernetes cluster:

* Files used to build Docker images for the Ping Advanced Identity Software:

  * Dockerfiles

  * Scripts and configuration files incorporated into ForgeOps-provided Docker images

  * Canonical configuration profiles for the platform

* Helm charts

* Kustomize bases and overlays

In addition, the repository contains utility scripts and sample files. The scripts and samples are useful for:

* Performing ForgeOps deployments quickly and easily

* Exploring monitoring, alerts, and security customization

Learn more about the files in the repository, recommendations about how to work with them, and the support status for the files in the [`forgeops` repository reference](#forgeops-reference).

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Learn more about configuring GitHub notifications [here](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) so you can get notified on ForgeOps releases. |

##### `forgeops` repository updates

New `forgeops` repository features become available in the `2026.2.1` tag of the `main` branch from time to time.

When you start working with the `forgeops` repository, clone the repository. Depending on your organization's setup, you'll clone the repository either from the public repository on GitHub, or from a fork. You can find more information in [Git clone or Git fork?](#forgeops-fork).

Then, check out the `2026.2.1` tag and create a working branch. For example:

```
$ git checkout 2026.2.1
$ git checkout -b my-working-branch
```

The ForgeOps team recommends that you regularly incorporate updates to the `2026.2.1` tag into your working branch:

1. [Get emails or subscribe to the ForgeOps RSS feed](rn/rn.html) to be notified when there have been updates to ForgeOps 2026.2.1.

2. Pull new commits in the `2026.2.1` tag from the repository into your `2026.2.1` clone.

3. Rebase the commits from the new branch into your working branch in your `forgeops` repository clone.

It's important to understand the impact of rebasing changes from the `forgeops` repository into your branches. [`forgeops` repository reference](#forgeops-reference) provides advice about which files in the `forgeops` repository to change, which files not to change, and what to look out for when you rebase. Follow the advice in [`forgeops` repository reference](#forgeops-reference) to reduce merge conflicts, and to better understand how to resolve them when you rebase your working branch with updates that the ForgeOps team has made to the `2026.2.1` tag of the `main` branch.

##### `forgeops` repository reference

For more information about support for the `forgeops` repository, see [Support for ForgeOps](start/support.html).

###### Directories

[](#bin)bin

Example scripts you can use or model for a variety of deployment tasks.

Recommendation: Don't modify the files in this directory. If you want to add your own scripts to the `forgeops` repository, create a subdirectory under bin, and store your scripts there.

Support Status: Sample files. [Not supported by Ping Identity.](start/support.html#commercial-support)

[](#charts)charts

Helm charts.

Recommendation: Don't modify the files in this directory. If you want to update a values.yaml file, create your deployment environment using the forgeops env command, and edit values.yaml files in the new environment you created. Learn more in the [`forgeops env` command reference](reference/forgeops-cmd-ref.html#forgeops-env).

Support Status: [Supported is available from Ping Identity.](start/support.html#commercial-support)

[](#cluster_removed)cluster removed

The required ForgeOps contents in this directory have been moved to other directories as relevant and this directory has been removed.

[](#docker)docker

Contains three types of files needed to build Docker images for the Ping Advanced Identity Software: Dockerfiles, support files that go into Docker images, and configuration profiles.

**Dockerfile**

Common deployment customizations require modifications to the Dockerfile in the docker directory.

Recommendation: Expect to encounter merge conflicts when you rebase changes from ForgeOps into your branches. Be sure to track changes you've made to Dockerfiles, so that you're prepared to resolve merge conflicts after a rebase.

Support Status: Dockerfiles. [Support is available from Ping Identity.](start/support.html#commercial-support)

**Support Files Referenced by Dockerfiles**

When customizing the default ForgeOps deployments, you might need to add files to the docker directory. For example, to customize the AM WAR file, you might need to add plugin JAR files, user interface customization files, or image files.

Recommendation: If you only add new files to the docker directory, you should not encounter merge conflicts when you rebase changes from ForgeOps into your branches. However, if you need to modify any files from ForgeOps, you might encounter merge conflicts. Be sure to track changes you've made to any files in the docker directory, so that you're prepared to resolve merge conflicts after a rebase.

Support Status:

Scripts and other files from ForgeOps that are incorporated into Docker images for the Ping Advanced Identity Software: [Support is available from Ping Identity.](start/support.html#commercial-support)

User customizations that are incorporated into custom Docker images for the Ping Advanced Identity Software: [Support is not available from Ping Identity.](start/support.html#commercial-support)

**Configuration Profiles**

The starter configuration profiles provided with ForgeOps. To create your own configuration profiles, use the forgeops config command in your ForgeOps deployment environment. Add your own configuration profiles to the docker directory using the export command. Don't modify the internal-use only `idm-only` and `ig-only` configuration profiles provided by ForgeOps.

Recommendation: You should not encounter merge conflicts when you rebase changes from ForgeOps into your branches.

Support Status: Configuration profiles. [Support is available from Ping Identity.](start/support.html#commercial-support)

[](#etc)etc

Files used to support ForgeOps deployments.

Recommendation: Don't modify the files in this directory (or its subdirectories).

Support Status: Sample files. [Not supported by Ping Identity.](start/support.html#commercial-support)

[](#helm)helm

Helm values files for each client environment (env) for use with Helm charts. The Helm values files are created and managed by the forgeops env command.

**Files in each ForgeOps deployment environment**

| File                  | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| `env.log`             | Log of `forgeops env` runs.                                            |
| `values.yaml`         | Configuration of components in ForgeOps deployment using Helm.         |
| `values-images.yaml`  | Docker image used in ForgeOps deployment.                              |
| `values-ingress.yaml` | Ingress configuration, such as FQDN.                                   |
| `values-size.yaml`    | Component size information such as number of replicas, cpu, and memory |

Support Status: Environment specific files. [Support is available from Ping Identity.](start/support.html#commercial-support)

[](#how_tos)how-tos

Description and usage of various utilities provided with ForgeOps.

Recommendation: Don't change these files.

Support Status: Description files. [Support is available from Ping Identity.](start/support.html#commercial-support)

[](#intezer)intezer

For ForgeOps internal use only. Don't modify or use.

[](#jenkins_scripts)jenkins-scripts

For ForgeOps internal use only. Don't modify or use.

[](#kustomize)kustomize

Artifacts for orchestrating the Ping Advanced Identity Software using Kustomize.

Recommendation: Common deployment customizations, such as changing the deployment namespace and providing a customized FQDN, require modifications to files in the kustomize/overlay directory. Be sure to track changes you've made to the files in the kustomize directory, so that you're prepared to resolve merge conflicts after a rebase.

Support Status: Kustomize bases and overlays. [Support is available from Ping Identity.](start/support.html#commercial-support)

[](#legacy_docs)legacy-docs

Documentation for performing ForgeOps deployments using older versions. Includes documentation for supported and deprecated versions of the `forgeops` repository.

Recommendation: Don't modify the files in this directory.

Support Status:

Documentation for supported versions of the `forgeops` repository: [Support is available from Ping Identity.](start/support.html#commercial-support)

Documentation for deprecated versions of the `forgeops` repository: [Not supported by Ping Identity.](start/support.html#commercial-support)

[](#lib)lib

Python and shell library files used internally. Don't modify.

[](#releases_removed)releases removed[](#upgrade)upgrade

For ForgeOps internal use only. Don't modify.

###### Files in the top-level directory

[](#gcloudignore_gitchangelog_rc_gitignore_forgeops_conf_example).gcloudignore, .gitchangelog.rc, .gitignore, forgeops.conf.example

For ForgeOps internal use only. Don't modify.

[](#changelog_md)CHANGELOG.md

This file records changes in ForgeOps artifacts, processes, and procedures.

Recommendation: Don't modify this file.

[](#license)LICENSE

Software license for artifacts in the `forgeops` repository. Don't modify.

[](#makefile)Makefile

For ForgeOps internal use only. Don't modify.

[](#notifications_json)notifications.json

For ForgeOps internal use only. Don't modify.

[](#readme_md)README.md

The top-level `forgeops` repository README file. Don't modify.

#### `forgeops-extras` repository

Use the [forgeops-extras](https://github.com/ForgeRock/forgeops-extras) repository to create sample Kubernetes clusters in which you can deploy the Ping Advanced Identity Software.

##### `forgeops-extras` repository reference

For more information about support for the `forgeops-extras` repository, see [Support for ForgeOps](start/support.html).

###### Directories

[](#terraform)terraform

Example Terraform artifacts that automate cluster creation and deletion.

Recommendation: Don't modify the files in this directory. If you want to add your own cluster creation support files to the `forgeops` repository, copy the terraform.tfvars file to a new file and make changes there.

Support Status: Sample files. [Not supported by Ping Identity.](start/support.html#commercial-support)

#### Git clone or Git fork?

For the simplest use cases—a single user performing a proof of concept, or exploration of the platform—cloning the ForgeOps public repositories from GitHub provides a quick and adequate way to access the repositories.

If, however, your use case is more complex, you might want to fork the repositories, and use the forks as your common upstream repositories. For example:

* Multiple users in your organization need to access a common version of the repository and share changes made by other users.

* Your organization plans to incorporate `forgeops` and `forgeops-extras` repository changes from ForgeOps.

* Your organization wants to use pull requests when making repository updates.

If you've forked the `forgeops` and `forgeops-extras` repositories:

* You'll need to synchronize your forks with ForgeOps repositories on GitHub when ForgeOps releases new branches.

* Your users will need to clone your forks before they start working instead of cloning the public repositories from GitHub. Because procedures in the documentation tell users to clone the public repositories, you'll need to make sure your users follow different procedures to clone the forks instead.

* The steps to initially get and update your repository clones will differ from the steps provided in the documentation. You'll need to let users know how to work with the forks as the upstream repositories instead of following the steps in the documentation.

### Third-party software

Before performing a ForgeOps deployment, install the requisite third-party software on your local computer.

The ForgeOps team recommends you install third-party software using [Homebrew](https://brew.sh/) on macOS and Linux'\[[3](#_footnotedef_3 "View footnote.")]' .

#### Required third-party software

|                                         |         |                                                             |
| --------------------------------------- | ------- | ----------------------------------------------------------- |
| Software                                | Version | Homebrew package                                            |
| **On all platforms**                    |         |                                                             |
| * Python 3                              | 3.14.5  | `python@3`                                                  |
| - Bash                                  | 5.3.9   | `bash`                                                      |
| * Docker client                         | 28.4.0  | `docker`                                                    |
| - Kubernetes client (kubectl)           | 1.36.1  | `kubernetes-cli`                                            |
| * Kubernetes context switcher (kubectx) | 0.11.0  | `kubectx`                                                   |
| - Kustomize                             | 5.8.1   | `kustomize`                                                 |
| * Helm                                  | 4.2.0   | `helm`                                                      |
| - JSON processor jq                     | 1.8.1   | `jq`                                                        |
| * Setup tools (Python)                  | 82.0.1  | `python-setuptools`                                         |
| - Terraform                             | 1.12.2  | `terraform`                                                 |
| **Additionally on Google GKE**          |         |                                                             |
| * Google Cloud SDK                      | 569.0.0 | `gcloud-cli` (cask)\[[3](#_footnotedef_3 "View footnote.")] |
| **Additionally on Amazon EKS**          |         |                                                             |
| - Amazon AWS Command-line Interface     | 2.34.50 | `awscli`                                                    |
| * AWS IAM Authenticator for Kubernetes  | 0.7.16  | `aws-iam-authenticator`                                     |
| **Additionally on Azure AKS**           |         |                                                             |
| - Azure Command-line Interface          | 2.86.0  | `azure-cli`                                                 |
| **Additionally on minikube**            |         |                                                             |
| * minikube                              | 1.38.1  | `minikube`                                                  |

### ForgeOps release process

ForgeOps release process is aimed at simplifying the management of multiple ForgeOps versions in a single branch. This process:

* Removes the need to create and maintain multiple release branches for every product release.

* Enables easier upgrading and switching between multiple supported versions.

* Supports delivery of regularly promoted secure Docker images.

* Unifies documentation to easily consume product information.

#### Key features

* Single `main` branch for all new releases

  * The `main` branch doesn't replace the already released forgeops branches. The currently released branches continue to be supported and updated with new minor and patch releases of the products.

  * Deployments use the latest available image for the current product version by default. Customers can select to use a specific supported image as per their needs.

* Product versions are separated from the `forgeops` repository

  * Product image tags are now maintained in tag files at <http://releases.forgeops.com>.

  * The refactored `forgeops` tool retrieves the requested tags and updates Dockerfiles/Helm/Kustomize as required.

  * All new major releases will be released using the new release process only.

  * The new process also supports 7.5 and 7.4 product image tags. Customers can continue to use the release/7.5-\* and release/7.4-\* branches until they are ready to migrate to the new process.

  * Customers can select the latest early-adapter images of the products to test the latest product features (similar to the dev image tag on the `master` branch previously).

* Supported Docker images

  * The new process is required to handle regular delivery of updated secure product images.

    * Docker images are routinely scanned for OS-level vulnerabilities and addressed by the ForgeOps team where OS patches are available.

    * The Ping Advanced Identity Software teams provide the platform-level patches.

  * The delivery process is automated, and the newly promoted tags will be available at <http://releases.forgeops.com>.

  * New `dev` branch for latest forgeops features. Equivalent to the erstwhile `master` branch which is no longer available.

  * Updated release information on <https://github.com/ForgeRock/forgeops>. Customers can get release updates by setting up their GitHub notifications.

  * Single set of documentation that is updated for ForgeOps releases and updates to the `main` branch.

  * Best efforts to document the dev branch updates similar to the early-adapter documentation.

## Setup overview

Before performing a ForgeOps deployment, you must perform some setup tasks in your local computer, create a Kubernetes cluster (or have access to an existing cluster), and configure your local machine to access the cluster.

The specific tasks you'll need to do vary depending on the platform on which you run Kubernetes:

[icon: google, set=fab, size=3x]

#### [Google Cloud](https://docs.pingidentity.com/forgeops/2026.2/setup/google-cloud.html)

Set up your local computer to deploy ForgeOps on Google Cloud.

[icon: aws, set=fab, size=3x]

#### [AWS](https://docs.pingidentity.com/forgeops/2026.2/setup/aws.html)

Set up your local computer to deploy ForgeOps on AWS.

[icon: microsoft, set=fab, size=3x]

#### [Azure](https://docs.pingidentity.com/forgeops/2026.2/setup/azure.html)

Set up your local computer to deploy ForgeOps on Azure.

[icon: empire, set=fab, size=3x]

#### [minikube](https://docs.pingidentity.com/forgeops/2026.2/setup/minikube.html)

Set up your local computer to deploy ForgeOps on minikube.

### Google Cloud

Before you can [perform a ForgeOps deployment](deploy/overview.html) on a Kubernetes cluster running on Google Cloud, you must complete these prerequisite tasks:

* [Clone the `forgeops` and `forgeops-extras` repositories](#gcp-repositories)

* [Install third-party software on your local computer](#gcp-third-party-software)

* [Start a virtual machine that runs Docker engine on your local computer](#docker-gcp)

* [Set up a Google Cloud project that meets the requirements for ForgeOps deployments](#project)

* [Create a Kubernetes cluster in the project](#gcp-cluster)

* [Set up your local computer to access the cluster's ingress controller](#gcp-ingress)

#### `forgeops` and `forgeops-extras` repositories

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

   Depending on your organization's repository strategy, you might need to clone the repository from a fork. You might also need to create a working branch from the `2026.2.1` tag of your fork. Learn more about [Repository Updates here](start/repositories.html#forgeops-updates).

3. Check out the `forgeops-extras` repository's `main` branch:

   ```
   $ cd /path/to/forgeops-extras
   $ git checkout main
   ```

#### Third-party software

Before performing a ForgeOps deployment, obtain third-party software and install it on your local computer.

ForgeOps team recommends that you install third-party software using [Homebrew](https://brew.sh/) on macOS and Linux'\[[3](#_footnotedef_3 "View footnote.")]' .

The versions listed in the following table have been validated for ForgeOps deployments on Google Cloud. Earlier and later versions will *probably* work. If you want to try using versions that are not in the table, it is your responsibility to validate them.

Install the following third-party software:

|                                         |         |                                                             |
| --------------------------------------- | ------- | ----------------------------------------------------------- |
| Software                                | Version | Homebrew package                                            |
| **On all platforms**                    |         |                                                             |
| * Python 3                              | 3.14.5  | `python@3`                                                  |
| - Bash                                  | 5.3.9   | `bash`                                                      |
| * Docker client                         | 28.4.0  | `docker`                                                    |
| - Kubernetes client (kubectl)           | 1.36.1  | `kubernetes-cli`                                            |
| * Kubernetes context switcher (kubectx) | 0.11.0  | `kubectx`                                                   |
| - Kustomize                             | 5.8.1   | `kustomize`                                                 |
| * Helm                                  | 4.2.0   | `helm`                                                      |
| - JSON processor jq                     | 1.8.1   | `jq`                                                        |
| * Setup tools (Python)                  | 82.0.1  | `python-setuptools`                                         |
| - Terraform                             | 1.12.2  | `terraform`                                                 |
| **Additionally on Google GKE**          |         |                                                             |
| * Google Cloud SDK                      | 569.0.0 | `gcloud-cli` (cask)\[[3](#_footnotedef_3 "View footnote.")] |

##### Python `venv`

The new `forgeops` utility is built on Python3. Some of the Python3 packages used by `forgeops` must be installed using `pip`. To separate such Python3 specific packages, Python recommends the use of the `venv` Python virtual environment. Learn more about Python `venv` in [venv - virtual environments](https://docs.python.org/3/library/venv.html).

1. Create a `venv` for using the `forgeops` utility\[[4](#_footnotedef_4 "View footnote.")].

   ```
   $ python3 -m venv .venv
   ```

2. Set up Python3 dependencies for `forgeops` utility.

   ```
   $ source .venv/bin/activate
   $ /path/to/forgeops/bin/forgeops configure
   ```

##### Docker engine

In addition to the software listed in the preceding table, you'll need to start a virtual machine that runs Docker engine.

* On macOS systems, use [Docker Desktop](https://docs.docker.com/desktop/install/mac-install) or an alternative, such as [Colima](https://github.com/abiosoft/colima).

* On Linux systems, use [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/), install Docker machine from your Linux distribution, or use an alternative, such as [Colima](https://github.com/abiosoft/colima).

For more information about using Colima when performing ForgeOps deployments, refer to [this article](https://community.forgerock.com/t/deploying-forgeops-to-minikube-on-an-m1-mac-with-colima/3305/2).

The default configuration for a Docker virtual machine provides adequate resources for a ForgeOps deployment.

##### For users running Microsoft Windows

ForgeOps deployments are supported on macOS and Linux. If you've a Windows computer, you'll need to create a Linux VM. We tested the following configurations:

* Hypervisor: Hyper-V, VMWare Player, or VMWare Workstation

* Guest OS: Current Ubuntu LTS release with 12 GB memory and 60 GB disk space

* Nested virtualization enabled in the Linux VM.

Perform all the procedures in this documentation within the Linux VM. In this documentation, the local computer refers to the Linux VM for Windows users.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The minikube implementation on Windows Subsystem for Linux (WSL2) has networking issues. As a result, consistent access to the ingress controller or the apps deployed on minikube is not possible. This issue is tracked [here](https://github.com/kubernetes/minikube/issues/7879). Do not attempt to perform ForgeOps deployments on WSL2 until this issue is resolved. |

#### Google Cloud project setup

Perform these steps to set up a Google Cloud project that meets the requirements for ForgeOps deployments:

1. Log in to the Google Cloud Console and create a new project.

2. Authenticate to the Google Cloud SDK to obtain the permissions you'll need to create a cluster:

   1. Configure the gcloud CLI to use your Google account. Run the following command:

      ```
      $ gcloud auth application-default login
      ```

   2. A browser window appears, prompting you to select a Google account. Select the account you want to use for cluster creation.

      A second screen requests several permissions. Select Allow.

      A third screen should appear with the heading, You are now authenticated with the gcloud CLI!

3. Assign the following roles to users who will be creating Kubernetes clusters and performing ForgeOps deployments:

   * Editor

   * Kubernetes Engine Admin

   * Kubernetes Engine Cluster Admin

   * Project IAM Admin

   Remember, a ForgeOps deployment is a reference implementation. The roles you assign in this step are suitable for ForgeOps deployments. When you [create a project plan](start/start-here.html#planning), you'll need to determine which Google Cloud roles are required.

#### Kubernetes cluster creation

ForgeOps provides Terraform artifacts for GKE cluster creation. Use them to create a cluster that supports ForgeOps deployments. After performing a ForgeOps deployment, you can use your cluster as a sandbox to explore Ping Advanced Identity Software customization.

When you [create a project plan](start/start-here.html#planning), you'll need to identify your organization's preferred infrastructure-as-code solution, and, if necessary, create your own cluster creation automation scripts.

Here are the steps the ForgeOps team follows to create a Kubernetes cluster on GKE:

1. Copy the file that contains default Terraform variables to a new file:

   1. Change to the /path/to/forgeops-extras/terraform directory.

   2. Copy the terraform.tfvars file to override.auto.tfvars \[[5](#_footnotedef_5 "View footnote.")].

   Copying the terraform.tfvars file to a new file preserves the original content in the file.

2. []()Determine the deployment size: [small, medium, or large](deploy/architecture.html#cluster-and-deployment-sizes).

3. Define your cluster's configuration:

   1. Open the override.auto.tfvars file.

   2. Determine the location of your cluster's configuration in the override.auto.tfvars file:

      | Cluster size | Section containing the cluster configuration |
      | ------------ | -------------------------------------------- |
      | Small        | `cluster.tf_cluster_gke_small`               |
      | Medium       | `cluster.tf_cluster_gke_medium`              |
      | Large        | `cluster.tf_cluster_gke_large`               |

   3. Modify your cluster's configuration by setting values in the section listed in the table:

      1. Set the value of the `enabled` variable to `true`.

      2. Set the value of the `auth.project_id` variable to your new Google Cloud project. Specify the project ID, not the project name.

      3. Set the value of the `meta.cluster_name` variable to the name of the GKE cluster you'll create.

      4. Set the values of the `location.region` and `location.zones` variables to the region and zones where perform your ForgeOps deployment.

         Before continuing, go to Google's [Regions and Zones](https://cloud.google.com/compute/docs/regions-zones) page and verify that the zones you've specified are available in your region you specified.

   4. Save and close the override.auto.tfvars file.

4. Ensure your region has an adequate CPU quota for a ForgeOps deployment.

   Locate these two variables in your cluster's configuration in the override.auto.tfvars file:

   * `node_pool.type`: the machine type to be used in your cluster

   * `node_pool.max_count`: the maximum number of machines to be used in your cluster

   Your quotas must be large enough to let you allocate the maximum number of machines in your region. If your quotas are too low, request and wait for a quota increase from Google Cloud before attempting to create your cluster.

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

      * The GKE cluster

      * The `fast` storage class

      * The `ds-snapshot-class` volume snapshot class

      The script deploys:

      * An ingress controller

      * Certificate manager

6. Set your Kubernetes context to reference the new cluster by setting the `KUBECONFIG` environment variable as shown in the message from the tf-apply command's output.

7. To verify that the tf-apply script created the cluster, log in to the Google Cloud console. Select the Kubernetes Engine option. The new cluster should appear in the list of Kubernetes clusters.

8. Ensure that you have the right permissions to access the cluster by running the following command:

   ```
   $ gcloud container clusters get-credentials my-region --project my-gke-project
   ```

#### Hostname resolution

Set up hostname resolution for the Ping Advanced Identity Software servers you'll deploy in your namespace:

1. Get the ingress controller's external IP address:

   ```
   $ kubectl get services --namespace traefik
   ```

   The ingress controller's IP address should appear in the `EXTERNAL-IP` column. There can be a short delay while the ingress starts before the IP address appears in the `kubectl get services` command's output; you might need to run the command several times.

2. Configure hostname resolution for the ingress controller:

   1. Choose an FQDN (referred to as the *deployment FQDN*) that you'll use when you deploy the Ping Advanced Identity Software, and when you access its GUIs and REST APIs.

      Some examples in this documentation use `forgeops.example.com` as the deployment FQDN. You are not required to use `forgeops.example.com`; you can specify any FQDN you like.

   2. If DNS doesn't resolve your deployment FQDN, add an entry to the /etc/hosts file that maps the ingress controller's external IP address to the deployment FQDN. For example:

      ```
      35.203.145.112 forgeops.example.com
      ```

### AWS

Before you can [perform a ForgeOps deployment](deploy/overview.html) on a Kubernetes cluster running on AWS, you must complete these prerequisite tasks:

* [Clone the `forgeops` and `forgeops-extras` repositories](#aws-repositories)

* [Install third-party software on your local computer](#aws-third-party-software)

* [Start a virtual machine that runs Docker engine on your local computer](#docker-aws)

* [Set up your AWS environment to meet the requirements for ForgeOps deployments](#environment)

* [Create a Kubernetes cluster in AWS](#aws-cluster)

* [Set up your local computer to access the cluster's ingress controller](#aws-ingress)

#### `forgeops` and `forgeops-extras` repositories

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

   Depending on your organization's repository strategy, you might need to clone the repository from a fork. You might also need to create a working branch from the `2026.2.1` tag of your fork. Learn more about [Repository Updates here](start/repositories.html#forgeops-updates).

3. Check out the `forgeops-extras` repository's `main` branch:

   ```
   $ cd /path/to/forgeops-extras
   $ git checkout main
   ```

#### Third-party software

Before performing a ForgeOps deployment, obtain third-party software and install it on your local computer.

ForgeOps team recommends that you install third-party software using [Homebrew](https://brew.sh/) on macOS and Linux'\[[3](#_footnotedef_3 "View footnote.")]' .

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

##### Python `venv`

The new `forgeops` utility is built on Python3. Some of the Python3 packages used by `forgeops` must be installed using `pip`. To separate such Python3 specific packages, Python recommends the use of the `venv` Python virtual environment. Learn more about Python `venv` in [venv - virtual environments](https://docs.python.org/3/library/venv.html).

1. Create a `venv` for using the `forgeops` utility\[[6](#_footnotedef_6 "View footnote.")].

   ```
   $ python3 -m venv .venv
   ```

2. Set up Python3 dependencies for `forgeops` utility.

   ```
   $ source .venv/bin/activate
   $ /path/to/forgeops/bin/forgeops configure
   ```

##### Docker engine

In addition to the software listed in the preceding table, you'll need to start a virtual machine that runs Docker engine.

* On macOS systems, use [Docker Desktop](https://docs.docker.com/desktop/install/mac-install) or an alternative, such as [Colima](https://github.com/abiosoft/colima).

* On Linux systems, use [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/), install Docker machine from your Linux distribution, or use an alternative, such as [Colima](https://github.com/abiosoft/colima).

For more information about using Colima when performing ForgeOps deployments, refer to [this article](https://community.forgerock.com/t/deploying-forgeops-to-minikube-on-an-m1-mac-with-colima/3305/2).

The default configuration for a Docker virtual machine provides adequate resources for a ForgeOps deployment.

##### For users running Microsoft Windows

ForgeOps deployments are supported on macOS and Linux. If you've a Windows computer, you'll need to create a Linux VM. We tested the following configurations:

* Hypervisor: Hyper-V, VMWare Player, or VMWare Workstation

* Guest OS: Current Ubuntu LTS release with 12 GB memory and 60 GB disk space

* Nested virtualization enabled in the Linux VM.

Perform all the procedures in this documentation within the Linux VM. In this documentation, the local computer refers to the Linux VM for Windows users.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The minikube implementation on Windows Subsystem for Linux (WSL2) has networking issues. As a result, consistent access to the ingress controller or the apps deployed on minikube is not possible. This issue is tracked [here](https://github.com/kubernetes/minikube/issues/7879). Do not attempt to perform ForgeOps deployments on WSL2 until this issue is resolved. |

#### Setup for AWS

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

      Remember, a ForgeOps deployment is a reference implementation. The policies you create in this procedure are suitable for ForgeOps deployments. When you [create a project plan](start/start-here.html#planning), you'll need to determine how to configure AWS permissions.

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

#### Kubernetes cluster creation

ForgeOps provides Terraform artifacts for Amazon EKS cluster creation. Use them to create a cluster that supports ForgeOps deployments. After performing a ForgeOps deployment, you can use your cluster as a sandbox to explore Ping Advanced Identity Software customization.

When you [create a project plan](start/start-here.html#planning), you'll need to identify your organization's preferred infrastructure-as-code solution, and, if necessary, create your own cluster creation automation scripts.

Here are the steps the ForgeOps team follows to create a Kubernetes cluster on Amazon EKS:

1. Copy the file that contains default Terraform variables to a new file:

   1. Change to the /path/to/forgeops-extras/terraform directory.

   2. Copy the terraform.tfvars file to override.auto.tfvars \[[7](#_footnotedef_7 "View footnote.")].

   Copying the terraform.tfvars file to a new file preserves the original content in the file.

2. []()Determine the cluster size: [small, medium, or large](deploy/architecture.html#cluster-and-deployment-sizes).

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

#### Hostname resolution

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

### Azure

Before you can [perform a ForgeOps deployment](deploy/overview.html) on a Kubernetes cluster running on Azure], you must complete these prerequisite tasks:

* [Clone the `forgeops` and `forgeops-extras` repositories](#azure-repositories)

* [Install third-party software on your local computer](#azure-third-party-software)

* [Start a virtual machine that runs Docker engine on your local computer](#docker-azure)

* [Set up an Azure subscription that meets the requirements for ForgeOps deployments](#subscription)

* [Create a Kubernetes cluster in the subscription](#azure-cluster)

* [Set up your local computer to access the cluster's ingress controller](#azure-ingress)

#### `forgeops` and `forgeops-extras` repositories

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

   Depending on your organization's repository strategy, you might need to clone the repository from a fork. You might also need to create a working branch from the `2026.2.1` tag of your fork. Learn more about [Repository Updates here](start/repositories.html#forgeops-updates).

3. Check out the `forgeops-extras` repository's `main` branch:

   ```
   $ cd /path/to/forgeops-extras
   $ git checkout main
   ```

#### Third-party software

Before performing a ForgeOps deployment, obtain third-party software and install it on your local computer.

ForgeOps team recommends that you install third-party software using [Homebrew](https://brew.sh/) on macOS and Linux'\[[3](#_footnotedef_3 "View footnote.")]' .

The versions listed in the following table have been validated for ForgeOps deployments on Microsoft Azure. Earlier and later versions will *probably* work. If you want to try using versions that are not in the table, it is your responsibility to validate them.

Install the following third-party software:

|                                         |         |                     |
| --------------------------------------- | ------- | ------------------- |
| Software                                | Version | Homebrew package    |
| **On all platforms**                    |         |                     |
| * Python 3                              | 3.14.5  | `python@3`          |
| - Bash                                  | 5.3.9   | `bash`              |
| * Docker client                         | 28.4.0  | `docker`            |
| - Kubernetes client (kubectl)           | 1.36.1  | `kubernetes-cli`    |
| * Kubernetes context switcher (kubectx) | 0.11.0  | `kubectx`           |
| - Kustomize                             | 5.8.1   | `kustomize`         |
| * Helm                                  | 4.2.0   | `helm`              |
| - JSON processor jq                     | 1.8.1   | `jq`                |
| * Setup tools (Python)                  | 82.0.1  | `python-setuptools` |
| - Terraform                             | 1.12.2  | `terraform`         |
| **Additionally on Azure AKS**           |         |                     |
| * Azure Command-line Interface          | 2.86.0  | `azure-cli`         |

##### Python `venv`

The new `forgeops` utility is built on Python3. Some of the Python3 packages used by `forgeops` must be installed using `pip`. To separate such Python3 specific packages, Python recommends the use of the `venv` Python virtual environment. Learn more about Python `venv` in [venv - virtual environments](https://docs.python.org/3/library/venv.html).

1. Create a `venv` for using the `forgeops` utility\[[8](#_footnotedef_8 "View footnote.")].

   ```
   $ python3 -m venv .venv
   ```

2. Set up Python3 dependencies for `forgeops` utility.

   ```
   $ source .venv/bin/activate
   $ /path/to/forgeops/bin/forgeops configure
   ```

##### Docker engine

In addition to the software listed in the preceding table, you'll need to start a virtual machine that runs Docker engine.

* On macOS systems, use [Docker Desktop](https://docs.docker.com/desktop/install/mac-install) or an alternative, such as [Colima](https://github.com/abiosoft/colima).

* On Linux systems, use [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/), install Docker machine from your Linux distribution, or use an alternative, such as [Colima](https://github.com/abiosoft/colima).

For more information about using Colima when performing ForgeOps deployments, refer to [this article](https://community.forgerock.com/t/deploying-forgeops-to-minikube-on-an-m1-mac-with-colima/3305/2).

The default configuration for a Docker virtual machine provides adequate resources for a ForgeOps deployment.

##### For users running Microsoft Windows

ForgeOps deployments are supported on macOS and Linux. If you've a Windows computer, you'll need to create a Linux VM. We tested the following configurations:

* Hypervisor: Hyper-V, VMWare Player, or VMWare Workstation

* Guest OS: Current Ubuntu LTS release with 12 GB memory and 60 GB disk space

* Nested virtualization enabled in the Linux VM.

Perform all the procedures in this documentation within the Linux VM. In this documentation, the local computer refers to the Linux VM for Windows users.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The minikube implementation on Windows Subsystem for Linux (WSL2) has networking issues. As a result, consistent access to the ingress controller or the apps deployed on minikube is not possible. This issue is tracked [here](https://github.com/kubernetes/minikube/issues/7879). Do not attempt to perform ForgeOps deployments on WSL2 until this issue is resolved. |

#### Azure subscription setup

Perform these steps to set up an Azure subscription that meets the requirements for ForgeOps deployments:

1. Assign the following roles to users who will perform ForgeOps deployments:

   * Azure Kubernetes Service Cluster Admin Role

   * Azure Kubernetes Service Cluster User Role

   * Contributor

   * User Access Administrator

   Remember, a ForgeOps deployment is a reference implementation. The roles you assign in this step are suitable for ForgeOps deployments. When you [create a project plan](start/start-here.html#planning), you'll need to determine which Azure roles are required.

2. Log in to Azure services as a user with the roles you assigned in the previous step:

   ```
   $ az login
   ```

   If you have enabled multi-factor authentication for your Azure account, the `az login` command opens a browser window and prompts you to complete the authentication process and log in to your Azure account.

3. If necessary, set the current subscription ID to the one you will use to perform the ForgeOps deployment:

   ```
   $ az account set --subscription my-subscription-id
   ```

#### Kubernetes cluster creation

ForgeOps team provides Terraform artifacts for AKS cluster creation. Use them to create a cluster that supports ForgeOps deployments. After performing a ForgeOps deployment, you can use your cluster as a sandbox to explore Ping Advanced Identity Software customization.

When you [create a project plan](start/start-here.html#planning), you'll need to identify your organization's preferred infrastructure-as-code solution, and, if necessary, create your own cluster creation automation scripts.

Here are the steps the ForgeOps team follows to create a Kubernetes cluster on AKS:

1. Copy the file that contains default Terraform variables to a new file:

   1. Change to the /path/to/forgeops-extras/terraform directory.

   2. Copy the terraform.tfvars file to override.auto.tfvars \[[9](#_footnotedef_9 "View footnote.")].

   Copying the terraform.tfvars file to a new file preserves the original content in the file.

2. []()Determine the cluster size: [small, medium, or large](deploy/architecture.html#cluster-and-deployment-sizes).

3. Define your cluster's configuration:

   1. Open the override.auto.tfvars file.

   2. Determine the location of your cluster's configuration in the override.auto.tfvars file:

      | Cluster size | Section containing the cluster configuration |
      | ------------ | -------------------------------------------- |
      | Small        | `cluster.tf_cluster_aks_small`               |
      | Medium       | `cluster.tf_cluster_aks_medium`              |
      | Large        | `cluster.tf_cluster_aks_large`               |

   3. Modify your cluster's configuration by setting values in the section listed in the table:

      1. Set the value of the `enabled` variable to `true`.

      2. Set the value of the `meta.cluster_name` variable to the name of the AKS cluster you'll create.

      3. Set the values of the `location.region` and `location.zones` variables to the region and zones where you'll perform the ForgeOps deployment.

         Before continuing, go to Microsoft's [Products available by region](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/table) page and verify if AKS product is available in your region.

   4. Save and close the override.auto.tfvars file.

4. Ensure your region has an adequate CPU quota for a ForgeOps deployment.

   Locate these two variables in your cluster's configuration in the override.auto.tfvars file:

   * `node_pool.type`: the machine type to be used in your cluster

   * `node_pool.max_count`: the maximum number of machines to be used in your cluster

   Your quotas must be large enough to let you allocate the maximum number of machines in your region. If your quotas are too low, request and wait for a quota increase from Microsoft Azure before attempting to create your cluster.

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

      * The AKS cluster

      * The `fast` storage class

      * The `ds-snapshot-class` volume snapshot class

      The script deploys:

      * An ingress controller

      * Certificate manager

6. Set your Kubernetes context to reference the new cluster by setting the `KUBECONFIG` environment variable as shown in the message from the tf-apply command's output.

7. To verify that the tf-apply script created the cluster, log in to the Azure portal. Search for Kubernetes services and access the Kubernetes services page. The new cluster should appear in the list of Kubernetes clusters.

#### Hostname resolution

Set up hostname resolution for the Ping Advanced Identity Software servers you'll deploy in your namespace:

1. Get the ingress controller's external IP address:

   ```
   $ kubectl get services --namespace traefik
   ```

   The ingress controller's IP address should appear in the `EXTERNAL-IP` column. There can be a short delay while the ingress starts before the IP address appears in the `kubectl get services` command's output; you might need to run the command several times.

2. Configure hostname resolution for the ingress controller:

   1. Choose an FQDN (referred to as the *deployment FQDN*) that you'll use when you deploy the Ping Advanced Identity Software, and when you access its GUIs and REST APIs.

      Some examples in this documentation use `forgeops.example.com` as the deployment FQDN. You are not required to use `forgeops.example.com`; you can specify any FQDN you like.

   2. If DNS doesn't resolve your deployment FQDN, add an entry to the /etc/hosts file that maps the ingress controller's external IP address to the deployment FQDN. For example:

      ```
      20.168.193.68 forgeops.example.com
      ```

### minikube

Before you can [perform a ForgeOps deployment on a Kubernetes cluster running on minikube](deploy/overview.html), you must complete these prerequisite tasks:

* [Clone the `forgeops` repository](#repository)

* [Install third-party software on your local computer](#minikube-third-party-software)

* [Start a virtual machine that runs Docker engine on your local computer](#docker-mini)

* [Create a Kubernetes cluster on minikube](#minikube-cluster)

* [Set up your local computer to access the cluster's ingress controller](#minikube-ingress)

#### `forgeops` repository

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Learn more about configuring GitHub notifications [here](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) so you can get notified on ForgeOps releases. |

Before you can perform a ForgeOps deployment, you must first get the `forgeops` repository and check out the `2026.2.1` tag you want to use:

1. Clone the `forgeops` repository. For example:

   ```
   $ git clone https://github.com/ForgeRock/forgeops.git
   ```

   The `forgeops` repository is a public Git repository. You do not need credentials to clone it.

2. Check out the `2026.2.1` tag:

   ```
   $ cd forgeops
   $ git checkout 2026.2.1
   ```

Depending on your organization's repository strategy, you might need to clone the repository from a fork. You might also need to create a working branch from the `2026.2.1` tag. Learn more in [Repository Updates](start/repositories.html#forgeops-updates).

#### Third-party software

Before performing a ForgeOps deployment, obtain third-party software and install it on your local computer.

ForgeOps team recommends that you install third-party software using [Homebrew](https://brew.sh/) on macOS and Linux'\[[3](#_footnotedef_3 "View footnote.")]' .

The versions listed in this section have been validated for ForgeOps deployments on minikube. Earlier and later versions will *probably* work. If you want to try using versions that are not in the table, it is your responsibility to validate them.

|                                         |         |                     |
| --------------------------------------- | ------- | ------------------- |
| Software                                | Version | Homebrew package    |
| **On all platforms**                    |         |                     |
| * Python 3                              | 3.14.5  | `python@3`          |
| - Bash                                  | 5.3.9   | `bash`              |
| * Docker client                         | 28.4.0  | `docker`            |
| - Kubernetes client (kubectl)           | 1.36.1  | `kubernetes-cli`    |
| * Kubernetes context switcher (kubectx) | 0.11.0  | `kubectx`           |
| - Kustomize                             | 5.8.1   | `kustomize`         |
| * Helm                                  | 4.2.0   | `helm`              |
| - JSON processor jq                     | 1.8.1   | `jq`                |
| * Setup tools (Python)                  | 82.0.1  | `python-setuptools` |
| **Additionally on minikube**            |         |                     |
| - minikube                              | 1.38.1  | `minikube`          |

##### Python `venv`

The new `forgeops` utility is built on Python3. Some of the Python3 packages used by `forgeops` must be installed using `pip`. To separate such Python3 specific packages, Python recommends the use of the `venv` Python virtual environment. Learn more about Python `venv` in [venv - virtual environments](https://docs.python.org/3/library/venv.html).

1. Create a `venv` for using the `forgeops` utility\[[10](#_footnotedef_10 "View footnote.")].

   ```
   $ python3 -m venv .venv
   ```

2. Set up Python3 dependencies for `forgeops` utility.

   ```
   $ source .venv/bin/activate
   $ /path/to/forgeops/bin/forgeops configure
   ```

##### Docker engine

In addition to the software listed in the preceding table, you'll need to start a virtual machine that runs Docker engine.

* On macOS systems, use [Docker Desktop](https://docs.docker.com/desktop/install/mac-install) or an alternative, such as [Colima](https://github.com/abiosoft/colima).

* On Linux systems, use [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/), install Docker machine from your Linux distribution, or use an alternative, such as [Colima](https://github.com/abiosoft/colima).

For more information about using Colima when performing ForgeOps deployments, refer to [this article](https://community.forgerock.com/t/deploying-forgeops-to-minikube-on-an-m1-mac-with-colima/3305/2).

Minimum requirements for the virtual machine:

* 4 CPUs

* 10 GB RAM

* 60 GB disk space

##### For users running Microsoft Windows

ForgeOps deployments are supported on macOS and Linux. If you've a Windows computer, you'll need to create a Linux VM. We tested the following configurations:

* Hypervisor: Hyper-V, VMWare Player, or VMWare Workstation

* Guest OS: Current Ubuntu LTS release with 12 GB memory and 60 GB disk space

* Nested virtualization enabled in the Linux VM.

Perform all the procedures in this documentation within the Linux VM. In this documentation, the local computer refers to the Linux VM for Windows users.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The minikube implementation on Windows Subsystem for Linux (WSL2) has networking issues. As a result, consistent access to the ingress controller or the apps deployed on minikube is not possible. This issue is tracked [here](https://github.com/kubernetes/minikube/issues/7879). Do not attempt to perform ForgeOps deployments on WSL2 until this issue is resolved. |

#### minikube cluster

minikube software runs a single-node Kubernetes cluster in a virtual machine.

The minikube start command example shown in the doc creates a minikube cluster with a configuration that's adequate for a ForgeOps deployment.

The default driver option is fine for most users. For more information about minikube virtual machine drivers, refer to [Drivers](https://minikube.sigs.k8s.io/docs/drivers) in the minikube documentation.

If you want to use a driver other than the default driver, specify the `--driver` option when you run the minikube start command in the next step.

1. Set up minikube:

   ```
   $ minikube start --cpus=3 --memory=9g --disk-size=40g --cni=true \
     --kubernetes-version=stable --addons=ingress,volumesnapshots,metrics-server \
     --driver=docker
   😄  minikube v1.36.0 on Darwin 15.6
   ✨  Using the docker driver based on existing profile
   👍  Starting "minikube" primary control-plane node in "minikube" cluster...
   🚜  Pulling base image v0.0.47 ...
   🐳  Preparing Kubernetes v1.33.1 on Docker 28.1.1 ...
   🔎  Verifying Kubernetes components...
       ▪ Using image registry.k8s.io/metrics-server/metrics-server:v0.7.2
       ▪ Using image registry.k8s.io/sig-storage/snapshot-controller:v6.1.0
       ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
   💡  After the addon is enabled, please run "minikube tunnel" and your ingress
   resources would be available at "127.0.0.1"
   ...
   🔎  Verifying ingress addon…​
   🌟  Enabled addons: volumesnapshots, metrics-server, storage-provisioner,
   default-storageclass, ingress
   🏄  Done! kubectl is now configured to use "minikube" cluster and "default"
   namespace by default
   ```

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are running minikube on an ARM-based macOS system and the minikube output indicates that you are using the qemu driver, you probably did not start the virtual machine that runs your Docker engine. |

2. Run the minikube docker-env command to set up your local computer to use the minikube's Docker engine:

   ```
   $ eval $(minikube docker-env)
   ```

#### Hostname resolution

Set up hostname resolution for the Ping Advanced Identity Software servers you'll deploy in your namespace:

1. Determine the minikube ingress controller's IP address.

   * If minikube is using the Docker driver on macOS system'\[[11](#_footnotedef_11 "View footnote.")]' , use `127.0.0.1` as the ingress IP address.

   * If minikube is running the Hyperkit driver on Intel-based macOS system or on a Linux system, get the IP address by running the minikube ip command:

     ```
     $ minikube ip
     ...
     ```

2. Choose an FQDN (referred to as the *deployment FQDN*) that you'll use when you deploy the Ping Advanced Identity Software, and when you access its GUIs and REST APIs. Ensure that the FQDN is unique in the cluster you will be deploying the Ping Advanced Identity Software.

   Some examples in this documentation use `forgeops.example.com` as the deployment FQDN. You are not required to use `forgeops.example.com`; you can specify any FQDN you like.

3. Add an entry to the /etc/hosts file to resolve the deployment FQDN:

   ```
   ingress-ip-address forgeops.example.com
   ```

   For `ingress-ip-address`, specify the IP address from step 1. For example:

   ```
   127.0.0.1 forgeops.example.com
   ```

## Deployment overview

A *ForgeOps deployment* is a deployment of the Ping Advanced Identity Software on Kubernetes based on Docker images, Helm charts, Kustomize bases and overlays, utility programs, and other artifacts you can find in the `forgeops` repository on GitHub.

You can get a ForgeOps deployment up and running on Kubernetes quickly. After performing a ForgeOps deployment, you can use it to explore how you might configure a Kubernetes cluster before you deploy the platform in production.

A ForgeOps deployment is a robust sample deployment for demonstration and exploration purposes only. *It is not a production deployment*.

This section describes how to perform a ForgeOps deployment in a Kubernetes cluster and then access the platform's GUIs and REST APIs. When you're done, you can use ForgeOps deployment to explore deployment customizations.

![Illustrates the major tasks performed to deploy the platform.](deploy/_images/deploy.png)

Performing a ForgeOps deployment is a good learning and exploration exercise that helps prepare you to put together a project plan for deploying the platform in production. To better understand how this activity fits in to the overall deployment process, refer to [Performing a ForgeOps deployment](start/start-here.html#cdm-sandbox).

Using the ForgeOps artifacts and this documentation, you can quickly get the Ping Advanced Identity Software running in a Kubernetes environment. You begin to familiarize yourself with some of the steps you'll need to perform when deploying the platform in the cloud for production use:

Standardizes the process—The ForgeOps team's mission is to standardize a process for deploying the Ping Advanced Identity Software on Kubernetes. The team is made up of technical consultants and cloud software developers. We've had numerous interactions with our customers and discussed common deployment issues. Based on our interactions, we developed the ForgeOps artifacts to make deployment of the platform easier in the cloud.

Simplifies baseline deployment—We then developed artifacts: Dockerfiles, Kustomize bases and overlays, Helm charts, and utility programs to simplify the deployment process. We deployed small-sized, medium-sized, and large-sized production-quality Kubernetes clusters, and kept them up and running 24x7. We conducted continuous integration and continuous deployment as we added new capabilities and fixed problems in the system. We maintained, benchmarked, and tuned the system for optimized performance. Most importantly, we documented the process so you could replicate it.

Eliminates guesswork—If you use our ForgeOps artifacts and follow the instructions in this documentation without deviation, you can successfully deploy the Ping Advanced Identity Software in the cloud. ForgeOps deployments take the guesswork out of setting up a cloud environment. They bypass the deploy-test-integrate-test-repeat cycle many customers struggle through when spinning up the Ping Advanced Identity Software in the cloud for the first time.

Prepares you to deploy in production—After you've performed a ForgeOps deployment you'll be ready to start working with experts on deploying in production. We strongly recommend that you engage a Ping Identity technical consultant or partner to assist you with deploying the platform in production.

### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](deploy/overview.html)

* [icon: square-o, set=fa]*[Understand ForgeOps architecture](deploy/architecture.html)*

* [icon: square-o, set=fa][Deploy the platform](deploy/deploy.html)

* [icon: square-o, set=fa][Access platform UIs and APIs](deploy/access.html)

* [icon: square-o, set=fa][Plan for production deployment](deploy/next-steps.html)

### ForgeOps architecture

After you perform a ForgeOps deployment, the Ping Advanced Identity Software is fully operational in a Kubernetes cluster. `forgeops` artifacts provide preconfigured JVM settings, memory, CPU limits, and other configurations.

Here are some of the characteristics of ForgeOps deployments:

* Cluster and deployment sizes

  When you use the Terraform artifacts in the `forgeops-extras` repository to create a Kubernetes cluster on [Google Cloud](setup/google-cloud.html#gcp-cluster-size), [AWS](setup/aws.html#aws-cluster-size), or [Azure](setup/azure.html#azure-cluster-size), you specify one of three sizes:

  * A small cluster with capacity to handle 1,000,000 test users

  * A medium cluster with capacity to handle 10,000,000 test users

  * A large cluster with capacity to handle 100,000,000 test users

  When you use the minikube start command to create a Kubernetes cluster on [minikube](setup/minikube.html#minikube-cluster), you don't specify a cluster size.

  When you [perform a ForgeOps deployment](deploy/deploy.html), you specify a deployment size. This deployment size should be the same as your cluster size, except when you perform *single-instance ForgeOps deployments*.

  []()Single-instance deployments are special deployments that you use to [configure AM and IDM and build custom Docker images for the Ping Advanced Identity Software](customize/overview.html). They are called single-instance deployments because unlike small, medium, and large deployments, they have only single pods that run AM and IDM. They are only suitable for developing the AM and IDM configurations and must not be used for testing performance, monitoring, security, and backup requirements in production environments.

  You can perform one or more single-instance deployments on small, medium, and large GKE, EKS, and AKS clusters. Each single-instance deployment resides in its own namespace.

  You can perform one (and only one) single-instance deployment on a minikube cluster.

* Multi-zone Kubernetes cluster

  In small, medium, and large ForgeOps deployments, Ping Advanced Identity Software pods are distributed across three zones for high availability.

  (In single-instance deployments, Ping Advanced Identity Software pods reside in a single zone.)

  Go [here](#cdm-topology) for a diagram that shows the organization of pods in zones and node pools in small, medium, and large ForgeOps deployments.

* Third-party deployment and monitoring tools

  * [What is Traefik?](https://doc.traefik.io/traefik/)

  * [HAProxy Ingress Controller](https://haproxy-ingress.github.io) for Kubernetes ingress support.'\[[2](#_footnotedef_2 "View footnote.")]'

  * [Prometheus](https://prometheus.io/) for monitoring and notifications.'\[[2](#_footnotedef_2 "View footnote.")]'

  * [Prometheus Alertmanager](https://prometheus.io/docs/alerting/alertmanager/) for setting and managing alerts.'\[[2](#_footnotedef_2 "View footnote.")]'

  * [Grafana](https://grafana.com/) for metrics visualization.'\[[2](#_footnotedef_2 "View footnote.")]'

  * [Certificate Manager](https://docs.cert-manager.io) for obtaining and installing security certificates.

  * [Helm](https://helm.sh) for deploying Helm charts.

  * [Terraform](https://developer.hashicorp.com/terraform) for creating example clusters.'\[[2](#_footnotedef_2 "View footnote.")]'

* Ready-to-use Ping Advanced Identity Software components

  * Multiple DS instances are deployed for higher availability. Separate instances are deployed for Core Token Service (CTS) tokens and identities. The instances for identities also contain AM and IDM run-time data.

  * The AM configuration is file-based, stored at the path `/home/forgerock/openam/config` inside the AM Docker container (and in the AM pods).

  * Multiple AM instances are deployed for higher availability.'\[[1](#_footnotedef_1 "View footnote.")]'

  * AM instances are configured to access DS data stores.

  * Multiple IDM instances are deployed for higher availability.'\[[1](#_footnotedef_1 "View footnote.")]'

  * IDM instances are configured to access DS data stores.

- Highly available, distributed deployment'\[[2](#_footnotedef_2 "View footnote.")]' '\[[1](#_footnotedef_1 "View footnote.")]'

  Deployment across three zones ensures that the ingress controller and all Ping Advanced Identity Software components are highly available.

  Pods that run DS are configured to use [soft anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity). Because of this, Kubernetes schedules DS pods to run on nodes that don't have any other DS pods whenever possible.

  The exact placement of all other ForgeOps pods is delegated to Kubernetes.

  Pods are organized across three zones in a single node pool with six nodes. Pod placement among the nodes might vary, but the DS pods should run on nodes without any other DS pods.

  ![Clusters that support ForgeOps deployments have three zones and one node pool. The node pool has six nodes.](deploy/_images/m-cluster.svg)

- Ingress controller

  Hitherto ForgeOps used ingress-nginx controller by default. In March 2026, [Kubernetes will retire support for ingress-nginx controller](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/). ForgeOps team has decided to use Traefik as the default ingress controller for new deployments. Traefik is a modern HTTP reverse proxy and load balancer that makes deploying microservices easy.

  Optionally, you can [deploy HAProxy Ingress](reference/ingress.html#haproxy) as the ingress controller instead.'\[[2](#_footnotedef_2 "View footnote.")]'

- Secret generation and management

  [The open source Secret Agent operator](https://github.com/ForgeRock/secret-agent) generates Kubernetes secrets for Ping Advanced Identity Software deployments. It also integrates with Google Cloud Secret Manager, AWS Secrets Manager, and Azure Key Vault, providing cloud backup and retrieval for secrets.

- Secured communication

  The ingress controller is TLS-enabled. TLS is terminated at the ingress controller. Incoming requests and outgoing responses are encrypted.

  Inbound communication to DS instances occurs over secure LDAP (LDAPS).

  For more information, refer to [Secure HTTP](prepare/security/https.html).

- Stateful sets

  ForgeOps deployments use Kubernetes stateful sets to manage the DS pods. Stateful sets protect against data loss if Kubernetes client containers fail.

  On small-, medium- and large- deployments, CTS data stores are configured for [affinity](reference/glossary.html#glossary-affinity) load balancing for optimal performance.

  ![AM connections to CTS servers use token affinity in ForgeOps deployments.](deploy/_images/m-cluster-cts-flow.svg)

  AM policies, application data, and identities reside in the `idrepo` directory service. Small-, medium- and large- deployments use a single `idrepo` master configured to fail over to one of two secondary directory services.

  ![For all the ${am.abbr} pods](deploy/_images/m-cluster-idrepo-flow.svg)

- Authentication

  IDM is configured to use AM for authentication.

- DS replication'\[[1](#_footnotedef_1 "View footnote.")]'

  All DS instances are configured for full replication of identities and session tokens.

- Backup and restore'\[[2](#_footnotedef_2 "View footnote.")]'

  Backup and restore can be performed using several techniques. You can:

  * Use the volume snapshot capability in GKE, EKS, or AKS. The cluster where the ForgeOps deployment resides must be configured with a volume snapshot class before you can take volume snapshots, and persistent volume claims must use a CSI driver that supports volume snapshots.

  * Use the ds-backup utility.

  * Use a "last mile" backup archival solutions, such as Amazon S3, Google Cloud Storage, and Azure Cloud Storage that is specific to the cloud provider.

  * Use a Kubernetes backup and restore product, such as Velero, Kasten K10, TrilioVault, Commvault, or Portworx PX-Backup.

  For more information, refer to [Backup and restore overview](backup/overview.html).

- Initial data loading

  After the first AM instance in a ForgeOps deployment has started, an `amster` job runs. This job loads application data, such as OAuth 2.0 client definitions, to the `idrepo` DS instance.

#### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](deploy/overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](deploy/architecture.html)

* [icon: square-o, set=fa]*[Deploy the platform](deploy/deploy.html)*

* [icon: square-o, set=fa][Access platform UIs and APIs](deploy/access.html)

* [icon: square-o, set=fa][Plan for production deployment](deploy/next-steps.html)

### ForgeOps deployment

After you set up your deployment environment and your Kubernetes cluster, you're ready to perform a ForgeOps deployment.

First, you'll need to choose a deployment technology.

#### Deployment technologies

You can perform ForgeOps deployments using either [Kustomize](https://kustomize.io) or [Helm](https://helm.sh).

The preferred deployment technology for ForgeOps deployments is Helm. If you are not familiar with either of these two technologies, choose Helm.

Choose Kustomize as your deployment technology when:

* You performed ForgeOps deployments before Helm charts were available in the `forgeops` repository, and you want to continue to use Kustomize-based deployments.

* You want to generate Kustomize manifests for the platform, including custom manifests, using the forgeops generate command.

* Kustomize is your organization's preferred deployment technology for Kubernetes.

* Kustomize offers needed features that are not available in Helm.

#### Deployment scenarios

Follow the steps in one of these scenarios to perform a ForgeOps deployment:

* [Deploy using Helm on GKE, EKS, or AKS](deploy/deploy-scenario-helm-cloud.html)

* [Deploy using Helm on minikube](deploy/deploy-scenario-helm-local.html)

* [Deploy using Kustomize on GKE, EKS, or AKS](deploy/deploy-scenario-kustomize-cloud.html)

* [Deploy using Kustomize on minikube](deploy/deploy-scenario-kustomize-local.html)

#### Deploy using Helm on GKE, EKS, or AKS

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* On minikube, ForgeOps deployments continues to use the ingress-nginx addon provided by minikube. |

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

   * If you want to use the issuer provided with the platform for demo, then you can use default-issuer.

   * For a clusters on a cloud environment specify the --deployment-size as `--small`, `--medium`, or `--large`.

   * For a single-instance deployment, specify --deployment-size as `--single-instance`.

     ```
     $ cd /path/to/forgeops/bin
     $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com --cluster-issuer my-cluster-issuer --deployment-size
     ```

     In the command above, replace my-fqdn.example.com, my-cluster-issuer, and --deployment-size with appropriate values from your environment.

     Learn more about deployment sizes in [Cluster and deployment sizes](deploy/architecture.html#cluster-and-deployment-sizes) and about single instances [here](deploy/architecture.html#single-inst).

5. Ensure that the `image.repository` and `image.tag` are correctly specified in the Helm values file (/path/to/forgeops/helm/my-env/values.yaml) in your ForgeOps deployment environment.

   In your production environment, use the forgeops image command to select the latest available platform image corresponding to the major ForgeOps release, and not necessarily the latest image available from ForgeOps. This documentation uses images as latest from ForgeOps as default for demo and learning purposes. Using images tagged as latest from ForgeOps directly in your production environment can result in unintended upgrades.

   Learn more about setting and using ForgeOps platform image version tags [here](https://github.com/ForgeRock/forgeops/blob/main/how-tos/manage-platform-images.md).

   Learn more about customizing ForgeOps platform images [here](customize/overview.html).

6. Use the forgeops image command to set up the correct component image versions to be deployed:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --release my-image --env-name my-env platform
   ```

7. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster in which you'll perform the ForgeOps deployment.

   2. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   3. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

8. Set up the certificate and secret management prerequisites:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | 1. The `forgeops` utility uses `cert-manager` as the certificate management utility. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility. You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

      ```
      $ forgeops env --env-name my-env --ingress-no-cert-manager
      ```

   2. Currently, `secret-agent` is used as the default secrets management utility in ForgeOps deployments. You can continue to use the secret agent in existing deployments.

   3. ForgeOps artifacts include alternatives for ingress (Traefik or `ha-proxy`).

      The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

      A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](reference/forgeops-cmd-ref.html#prereqs-examples).

   4. Versions 1.2.9 and 1.2.10 of `secret-agent` have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.11**. |

   1. To install all prereqs including `secret-agent` for secret management:

      ```
      $ forgeops prereqs
      ```

9. (Optional) If you've set up your Kubernetes cluster using ForgeOps provided Terraform manifest, then you would have already created the required `fast` storage and volume snapshot classes. If you are setting your Kubernetes cluster using your own scripts, then create these classes using corresponding YAML scripts provided in the /path/to/forgeops/etc/resources folder.

   For example, on GKE:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/gke-fast-storage-class.yaml
   $ kubectl apply -f /path/to/forgeops/etc/resources/gke-volume-snapshot-class.yaml
   ```

10. Run the helm upgrade command to perform a ForgeOps deployment:

    ```
    $ helm upgrade --install identity-platform  identity-platform \
     --repo https://ForgeRock.github.io/forgeops/ \
     --version 2026.2 --namespace my-namespace \
     --values /path/to/forgeops/helm/my-env/values.yaml
    ```

    When deploying the platform with Docker images other than the ForgeOps-provided images, you'll also need to set additional Helm values such as `am.image.repository`, `am.image.tag`, `idm.image.repository`, and `idm.image.tag`. For an example, refer to [Redeploy AM: Helm deployments](customize/am.html#redeploy-am-helm).

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

11. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

    1. Run the kubectl get pods command.

    2. Review the output. Deployment is complete when:

       * All entries in the `STATUS` column indicate `Running` or `Completed`.

       * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

    3. If necessary, continue to query your deployment's status until all the pods are ready.

12. Back up and save the Kubernetes secrets that contain the master and TLS keys:

    1. To avoid accidentally putting the backups under version control, change to a directory that is outside your `forgeops` repository clone.

    2. The `ds-master-keypair` secret contains the DS master key. This key is required to decrypt data from a directory backup. *Failure to save this key could result in data loss.*

       Back up the Kubernetes secret that contains the DS master key:

       ```
       $ kubectl get secret ds-master-keypair -o yaml > master-key-pair.yaml
       ```

    3. The `ds-ssl-keypair` secret contains the DS TLS key. This key is needed for cross-environment replication topologies.

       Back up the Kubernetes secret that contains the DS TLS key pair:

       ```
       $ kubectl get secret ds-ssl-keypair -o yaml > tls-key-pair.yaml
       ```

    4. Save the two backup files.

13. (Optional) Deploy Prometheus, Grafana, and Alertmanager for monitoring and alerting\[[12](#_footnotedef_12 "View footnote.")]:

    1. Deploy Prometheus, Grafana, and Alertmanager pods in your ForgeOps deployment:

       ```
       $ /path/to/forgeops/bin/prometheus-deploy.sh

       **This script requires Helm version 3.04 or later due to changes in the behaviour of 'helm repo add' command.**

       namespace/monitoring created
       "stable" has been added to your repositories
       "prometheus-community" has been added to your repositories
       Hang tight while we grab the latest from your chart repositories...
       ...
       Update Complete. ⎈Happy Helming!⎈
       Release "prometheus-operator" does not exist. Installing it now.
       NAME: prometheus-operator
       LAST DEPLOYED: ...
       NAMESPACE: monitoring
       STATUS: deployed
       REVISION: 1
       NOTES:
       kube-prometheus-stack has been installed. Check its status by running:
         kubectl --namespace monitoring get pods -l "release=prometheus-operator"

       Visit https://github.com/prometheus-operator/kube-prometheus for instructions
       on how to create & configure Alertmanager and Prometheus instances using the Operator.
       ...
       Release "forgerock-metrics" does not exist. Installing it now.
       NAME: forgerock-metrics
       LAST DEPLOYED: ...
       NAMESPACE: monitoring
       STATUS: deployed
       REVISION: 1
       TEST SUITE: None
       ```

    2. Check the status of the pods in the `monitoring` namespace until all the pods are ready:

       ```
       $ kubectl get pods --namespace monitoring
       NAME                                                     READY   STATUS    RESTARTS   AGE
       alertmanager-prometheus-operator-kube-p-alertmanager-0   2/2     Running   0          119s
       prometheus-operator-grafana-95b8f5b7d-nn65h              3/3     Running   0          2m4s
       prometheus-operator-kube-p-operator-7d54989595-pdj44     1/1     Running   0          2m4s
       prometheus-operator-kube-state-metrics-d95996bc4-wcf7s   1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-67xq4       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-b4grn       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-cwhcn       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-h9brd       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-q8zrk       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-vqpt5       1/1     Running   0          2m4s
       prometheus-prometheus-operator-kube-p-prometheus-0       2/2     Running   0          119s
       ```

14. (Optional) Install a TLS certificate instead of using the default self-signed certificate in your ForgeOps deployment. Refer to [TLS certificate](prepare/security/https.html#tls-certificate) for details.

##### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](deploy/overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](deploy/architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy/deploy.html)

* [icon: square-o, set=fa]*[Access platform UIs and APIs](deploy/access.html)*

* [icon: square-o, set=fa][Plan for production deployment](deploy/next-steps.html)

#### Deploy using Helm on minikube

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* On minikube, ForgeOps deployments continues to use the ingress-nginx addon provided by minikube. |

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

5. In a minikube, set up the default cluster issuer\[[13](#_footnotedef_13 "View footnote.")]. For example:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/selfsigned-issuer.yaml
   ```

6. In minikube, set up a single instance deployment environment. For example:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com \
     --cluster-issuer my-cluster-issuer --single-instance
   ```

   In the command above, replace my-fqdn.example.com and my-cluster-issuer with appropriate values from your environment.

   Learn more about deployment sizes in [Cluster and deployment sizes](deploy/architecture.html#cluster-and-deployment-sizes) and about single instances [here](deploy/architecture.html#single-inst).

7. Ensure that the `image.repository` and `image.tag` are correctly specified in the Helm values file (/path/to/forgeops/helm/my-env/values.yaml) in your ForgeOps deployment environment.

   In your production environment, use the forgeops image command to select the latest available platform image corresponding to the major ForgeOps release, and not necessarily the latest image available from ForgeOps. This documentation uses images as latest from ForgeOps as default for demo and learning purposes. Using images tagged as latest from ForgeOps directly in your production environment can result in unintended upgrades.

   Learn more about setting and using ForgeOps platform image version tags [here](https://github.com/ForgeRock/forgeops/blob/main/how-tos/manage-platform-images.md).

   Learn more about customizing ForgeOps platform images [here](customize/overview.html).

8. Use the forgeops image command to set up the correct component image versions to be deployed:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --release my-image --env-name my-env platform
   ```

9. Set up your Kubernetes context:

   1. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

10. Set up the certificate management and secret agent.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | 1) Because minikube provides its own ingress controller, there's no need to install another ingress controller.1. The `forgeops` utility uses `cert-manager` as the certificate management utility. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility. You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

       ```
       $ forgeops env --env-name my-env --ingress-no-cert-manager
       ```

    2. Currently, `secret-agent` is used as the default secrets management utility in ForgeOps deployments. You can continue to use the secret agent in existing deployments.

    3. ForgeOps artifacts include alternatives for ingress (Traefik or `ha-proxy`).

       The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

       A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](reference/forgeops-cmd-ref.html#prereqs-examples).

    4. Versions 1.2.9 and 1.2.10 of `secret-agent` have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.11**. |

    1. To install the secret agent for secret management:

       ```
       $ forgeops prereqs cert-manager secrets
       ```

11. In a separate terminal tab or window, run the minikube tunnel command, and enter your system's superuser password when prompted:

    ```
    $ minikube tunnel
    ✅  Tunnel successfully started

    📌  NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible …​

    ❗  ...
    Password:
    ```

    The tunnel creates networking that lets you access the minikube cluster's ingress on the localhost IP address (127.0.0.1). Leave the tab or window that started the tunnel open for as long as you run the ForgeOps deployment.

    Refer to [this post](https://stackoverflow.com/questions/70961901/ingress-with-minikube-working-differently-on-mac-vs-ubuntu-when-to-set-etc-host) for an explanation about why a minikube tunnel is required to access ingress resources when running minikube on an ARM-based macOS system.

12. Set up the `fast` storage class using the `minikube-fast-storage-class.yaml` file in the /path/to/forgeops/etc/resources directory:

    ```
    $ kubectl apply -f /path/to/forgeops/etc/resources/minikube-fast-storage-class.yaml
    ```

13. Enable secret agent in your deployment environment:

    ```
    $ forgeops env --env-name my-env --namespace my-namespace  --secret-agent
    ```

14. Run the helm upgrade command to perform a ForgeOps deployment:

    ```
    $ helm upgrade --install identity-platform identity-platform \
     --repo https://ForgeRock.github.io/forgeops/ \
     --namespace my-namespace \
     --values /path/to/forgeops/helm/my-env/values.yaml
    ```

    The preceding command creates a single-instance ForgeOps deployment. Only single-instance deployments are supported on minikube.

    Learn more about single-instance deployments in [Cluster and deployment sizes](deploy/architecture.html#cluster-and-deployment-sizes).

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

15. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

    1. Run the kubectl get pods command.

    2. Review the output. Deployment is complete when:

       * All entries in the `STATUS` column indicate `Running` or `Completed`.

       * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

    3. If necessary, continue to query your deployment's status until all the pods are ready.

16. (Optional) Install a TLS certificate instead of using the default self-signed certificate in your ForgeOps deployment. Refer to [TLS certificate](prepare/security/https.html#tls-certificate) for details.

##### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](deploy/overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](deploy/architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy/deploy.html)

* [icon: square-o, set=fa]*[Access platform UIs and APIs](deploy/access.html)*

* [icon: square-o, set=fa][Plan for production deployment](deploy/next-steps.html)

#### Deploy using Kustomize on GKE, EKS, or AKS

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* On minikube, ForgeOps deployments continues to use the ingress-nginx addon provided by minikube. |

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

   * If you want to use the issuer provided with the platform for demo, then you can use default-issuer.

   * For a clusters on a cloud environment specify the --deployment-size as `--small`, `--medium`, or `--large`.

   * For a single-instance deployment, specify --deployment-size as `--single-instance`.

     ```
     $ cd /path/to/forgeops/bin
     $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com --cluster-issuer my-cluster-issuer --deployment-size
     ```

     In the command above, replace my-fqdn.example.com, my-cluster-issuer, and --deployment-size with appropriate values from your environment.

     Learn more about deployment sizes in [Cluster and deployment sizes](deploy/architecture.html#cluster-and-deployment-sizes) and about single instances [here](deploy/architecture.html#single-inst).

5. Ensure that the `image.repository` and `image.tag` are correctly specified in the image defaulter file in your ForgeOps deployment environment. The image defaulter file is located at /path/to/forgeops/kustomize/deploy/image-defaulter/kustomization.yaml.

   In your production environment, use the forgeops image command to select the latest available platform image corresponding to the major ForgeOps release, and not necessarily the latest image available from ForgeOps. This documentation uses images tagged as latest from ForgeOps as default for demo and learning purposes. Using images tagged as latest from ForgeOps directly in your production environment can result in unintended upgrades.

   Learn more about customizing ForgeOps platform images [here](customize/overview.html).

   If you want to use ForgeOps-provided Docker images for the platform, don't modify the image defaulter file. The following command sets up the latest ForgeOps-provided Docker image for the 8.1.0:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --env-name my-env --release 8.1.0 platform
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To set up your deployment environment with your customized image, use the following example command:```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --release my-image --release-name my-release --env-name my-env platform
   ```You can get the image names and tags from the image defaulter file on the system on which the customized Docker images were developed. |

6. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster in which you'll perform the ForgeOps deployment.

   2. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   3. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

7. Set up the certificate management, secret agent, and Traefik:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | 1. The `forgeops` utility uses `cert-manager` as the certificate management utility. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility. You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

      ```
      $ forgeops env --env-name my-env --ingress-no-cert-manager
      ```

   2. Currently, `secret-agent` is used as the default secrets management utility in ForgeOps deployments. You can continue to use the secret agent in existing deployments.

   3. ForgeOps artifacts include alternatives for ingress (Traefik or `ha-proxy`).

      The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

      A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](reference/forgeops-cmd-ref.html#prereqs-examples).

   4. Versions 1.2.9 and 1.2.10 of `secret-agent` have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.11**. |

   1. To install all prereqs including `secret-agent` for secret management:

      ```
      $ forgeops prereqs
      ```

8. (Optional) If you've set up your Kubernetes cluster using ForgeOps provided Terraform manifest, then you would have already created the required `fast` storage and volume snapshot classes. If you are setting your Kubernetes cluster using your own scripts, then create these classes using corresponding YAML scripts provided in the /path/to/forgeops/etc/resources folder.

   For example, on GKE:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/gke-fast-storage-class.yaml
   $ kubectl apply -f /path/to/forgeops/etc/resources/gke-volume-snapshot-class.yaml
   ```

9. Run the forgeops apply command to perform a ForgeOps deployment. Learn more in [`forgeops apply` command reference](reference/forgeops-cmd-ref.html#forgeops-apply).

   For example:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops apply --env-name my-env
   ```

   If you prefer not to deploy using a single forgeops apply command, you can find more information in [Alternative deployment techniques when using Kustomize](#alt-techniques-kustomize-cloud).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

10. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

    1. Run the kubectl get pods command.

    2. Review the output. Deployment is complete when:

       * All entries in the `STATUS` column indicate `Running` or `Completed`.

       * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

    3. If necessary, continue to query your deployment's status until all the pods are ready.

11. Back up and save the Kubernetes secrets that contain the master and TLS keys:

    1. To avoid accidentally putting the backups under version control, change to a directory that is outside your `forgeops` repository clone.

    2. The `ds-master-keypair` secret contains the DS master key. This key is required to decrypt data from a directory backup. *Failure to save this key could result in data loss.*

       Back up the Kubernetes secret that contains the DS master key:

       ```
       $ kubectl get secret ds-master-keypair -o yaml > master-key-pair.yaml
       ```

    3. The `ds-ssl-keypair` secret contains the DS TLS key. This key is needed for cross-environment replication topologies.

       Back up the Kubernetes secret that contains the DS TLS key pair:

       ```
       $ kubectl get secret ds-ssl-keypair -o yaml > tls-key-pair.yaml
       ```

    4. Save the two backup files.

12. (Optional) Deploy Prometheus, Grafana, and Alertmanager for monitoring and alerting\[[14](#_footnotedef_14 "View footnote.")]:

    1. Deploy Prometheus, Grafana, and Alertmanager pods in your ForgeOps deployment:

       ```
       $ /path/to/forgeops/bin/prometheus-deploy.sh

       **This script requires Helm version 3.04 or later due to changes in the behaviour of 'helm repo add' command.**

       namespace/monitoring created
       "stable" has been added to your repositories
       "prometheus-community" has been added to your repositories
       Hang tight while we grab the latest from your chart repositories...
       ...
       Update Complete. ⎈Happy Helming!⎈
       Release "prometheus-operator" does not exist. Installing it now.
       NAME: prometheus-operator
       LAST DEPLOYED: ...
       NAMESPACE: monitoring
       STATUS: deployed
       REVISION: 1
       NOTES:
       kube-prometheus-stack has been installed. Check its status by running:
         kubectl --namespace monitoring get pods -l "release=prometheus-operator"

       Visit https://github.com/prometheus-operator/kube-prometheus for instructions
       on how to create & configure Alertmanager and Prometheus instances using the Operator.
       ...
       Release "forgerock-metrics" does not exist. Installing it now.
       NAME: forgerock-metrics
       LAST DEPLOYED: ...
       NAMESPACE: monitoring
       STATUS: deployed
       REVISION: 1
       TEST SUITE: None
       ```

    2. Check the status of the pods in the `monitoring` namespace until all the pods are ready:

       ```
       $ kubectl get pods --namespace monitoring
       NAME                                                     READY   STATUS    RESTARTS   AGE
       alertmanager-prometheus-operator-kube-p-alertmanager-0   2/2     Running   0          119s
       prometheus-operator-grafana-95b8f5b7d-nn65h              3/3     Running   0          2m4s
       prometheus-operator-kube-p-operator-7d54989595-pdj44     1/1     Running   0          2m4s
       prometheus-operator-kube-state-metrics-d95996bc4-wcf7s   1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-67xq4       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-b4grn       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-cwhcn       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-h9brd       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-q8zrk       1/1     Running   0          2m4s
       prometheus-operator-prometheus-node-exporter-vqpt5       1/1     Running   0          2m4s
       prometheus-prometheus-operator-kube-p-prometheus-0       2/2     Running   0          119s
       ```

13. (Optional) Install a TLS certificate instead of using the default self-signed certificate in your ForgeOps deployment. Refer to [TLS certificate](prepare/security/https.html#tls-certificate) for details.

##### Alternative deployment techniques when using Kustomize

###### Staged deployments

If you prefer not to perform a ForgeOps Kustomize deployment using a single forgeops apply command, you can deploy the platform in stages, [component by component](troubleshoot/staged-deployment.html), instead of deploying with a single command. Staging deployments can be useful if you need to troubleshoot a deployment issue.

###### Generating Kustomize manifests and using `kubectl apply` commands

You can generate Kustomize manifests using the forgeops env command, and then deploy the platform using the kubectl apply -k command.

The forgeops env command generates Kustomize manifests for your ForgeOps deployment environment. The manifests are written to the /path/to/forgeops/kustomize/overlay/my-env directory of your `forgeops` repository clone. Advanced users who prefer to work directly with Kustomize manifests that describe their ForgeOps deployment can use the generated content in the kustomize/overlay/my-env directory as an alternative to using the forgeops command:

1. Generate an initial set of Kustomize manifests by running the forgeops env command.

2. Run kubectl apply -k commands to deploy and remove platform components. Specify a manifest in the kustomize/overlay/my-env directory as an argument when you run kubectl apply -k commands.

   1. Use GitOps to manage configuration changes to the kustomize/overlay/my-env directory.

##### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](deploy/overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](deploy/architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy/deploy.html)

* [icon: square-o, set=fa]*[Access platform UIs and APIs](deploy/access.html)*

* [icon: square-o, set=fa][Plan for production deployment](deploy/next-steps.html)

#### Deploy using Kustomize on minikube

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * In a development or demo environment, you can use the Helm chart available locally in /path/to/forgeops/charts directory for performing ForgeOps deployment. In a production environment, it's highly recommended to use the Helm charts published on the registry.

* The default ForgeOps deployment provides a self-signed certificate that has a very limited use even in demo environments. You must use a certificate obtained from a certificate authority for use in your environment. You can use the [Add custom certificates](prepare/security/secrets-rotation.html#add-cust-cert) procedure.

* The current ForgeOps deployments on GKE, AKS, and EKS use Traefik as the default ingress controller. You can continue to use NGINX, but note that Kubernetes has stopped the support for ingress-nginx controller, so we strongly recommend you use Traefik for new deployments.

* On minikube, ForgeOps deployments continues to use the ingress-nginx addon provided by minikube. |

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

5. In a minikube, set up the default cluster issuer\[[15](#_footnotedef_15 "View footnote.")]. For example:

   ```
   $ kubectl apply -f /path/to/forgeops/etc/resources/selfsigned-issuer.yaml
   ```

6. In minikube, set up a single instance deployment environment. For example:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com \
     --cluster-issuer my-cluster-issuer --single-instance
   ```

   In the command above, replace my-fqdn.example.com and my-cluster-issuer with appropriate values from your environment.

   Learn more about deployment sizes in [Cluster and deployment sizes](deploy/architecture.html#cluster-and-deployment-sizes) and about single instances [here](deploy/architecture.html#single-inst).

7. Ensure that the `image.repository` and `image.tag` are correctly specified in the image defaulter file in your ForgeOps deployment environment. The image defaulter file is located at /path/to/forgeops/kustomize/deploy/image-defaulter/kustomization.yaml.

   In your production environment, use the forgeops image command to select the latest available platform image corresponding to the major ForgeOps release, and not necessarily the latest image available from ForgeOps. This documentation uses images tagged as latest from ForgeOps as default for demo and learning purposes. Using images tagged as latest from ForgeOps directly in your production environment can result in unintended upgrades.

   Learn more about customizing ForgeOps platform images [here](customize/overview.html).

   If you want to use ForgeOps-provided Docker images for the platform, don't modify the image defaulter file. The following command sets up the latest ForgeOps-provided Docker image for the 8.1.0:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --env-name my-env --release 8.1.0 platform
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To set up your deployment environment with your customized image, use the following example command:```
   $ cd /path/to/forgeops/bin
   $ ./forgeops image --release my-image --release-name my-release --env-name my-env platform
   ```You can get the image names and tags from the image defaulter file on the system on which the customized Docker images were developed. |

8. Set up your Kubernetes context:

   1. Create a Kubernetes namespace in the cluster for the Ping Advanced Identity Software pods:

      ```
      $ kubectl create namespace my-namespace
      ```

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace you just created:

      ```
      $ kubens my-namespace
      ```

9. Set up the certificate and secret management prerequisites:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | 1. Because minikube provides its own ingress controller, there's no need to install another ingress controller.

   2. The `forgeops` utility uses `cert-manager` as the certificate management utility. If you need to use a different certificate management utility, refer to the corresponding documentation for installing that utility. You can disable `cert-manager` for ingresses in your ForgeOps deployment environment using the --ingress-no-cert-manager option of the forgeops env command:

      ```
      $ forgeops env --env-name my-env --ingress-no-cert-manager
      ```

   3. Currently, `secret-agent` is used as the default secrets management utility in ForgeOps deployments. You can continue to use the secret agent in existing deployments.

   4. ForgeOps artifacts include alternatives for ingress (Traefik or `ha-proxy`).

      The forgeops prereqs command provides a corresponding `--` option to select the component you want to use. The `--` option isn't available for components, such as `cert-manager`, for which an alternative isn't provided.

      A few examples of the forgeops prereqs command are provided in the [`forgeops prereqs` command reference](reference/forgeops-cmd-ref.html#prereqs-examples).

   5. Versions 1.2.9 and 1.2.10 of `secret-agent` have a flaw that causes the `secret-agent` operator to crash when it tries to access the Kubernetes API. If you are using `secret-agent`, **avoid `secret-agent` versions 1.2.9 and 1.2.10; upgrade to version 1.2.11**. |

   1. To install the secret agent for secret management:

      ```
      $ forgeops prereqs cert-manager secrets
      ```

10. In a separate terminal tab or window, run the minikube tunnel command, and enter your system's superuser password when prompted:

    ```
    $ minikube tunnel
    ✅  Tunnel successfully started

    📌  NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible …​

    ❗  ...
    Password:
    ```

    The tunnel creates networking that lets you access the minikube cluster's ingress on the localhost IP address (127.0.0.1). Leave the tab or window that started the tunnel open for as long as you run the ForgeOps deployment.

    Refer to [this post](https://stackoverflow.com/questions/70961901/ingress-with-minikube-working-differently-on-mac-vs-ubuntu-when-to-set-etc-host) for an explanation about why a minikube tunnel is required to access ingress resources when running minikube on an ARM-based macOS system.

11. Set up the `fast` storage class using the `minikube-fast-storage-class.yaml` file in the /path/to/forgeops/etc/resources directory:

    ```
    $ kubectl apply -f /path/to/forgeops/etc/resources/minikube-fast-storage-class.yaml
    ```

12. Enable secret agent in your deployment environment:

    ```
    $ forgeops env --env-name my-env --namespace my-namespace  --secret-agent
    ```

13. Run the forgeops apply command. Learn more in [`forgeops apply` command reference](reference/forgeops-cmd-ref.html#forgeops-apply).

    For example:

    ```
    $ cd /path/to/forgeops/bin
    $ ./forgeops apply --env-name my-env
    ```

    The preceding command creates a single-instance ForgeOps deployment. Only single-instance deployments are supported on minikube.

    If you prefer not to deploy using a single forgeops apply command, you can find more information in [Alternative deployment techniques when using Kustomize](#alt-techniques-kustomize-local).

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    |   | Ping Identity only offers its software or services to legal entities that have entered into a binding license agreement with Ping Identity. When you install Docker images provided by ForgeOps, you agree either that: 1) you are an authorized user of a Ping Advanced Identity Software customer that has entered into a license agreement with Ping Identity governing your use of the Ping Identity software; or 2) your use of the Ping Advanced Identity Software is subject to the [Ping Identity Subscription Agreements](https://www.pingidentity.com/en/legal/subscription-agreement.html). |

14. Check the status of the pods in the namespace in which you deployed the platform until all the pods are ready:

    1. Run the kubectl get pods command.

    2. Review the output. Deployment is complete when:

       * All entries in the `STATUS` column indicate `Running` or `Completed`.

       * The `READY` column indicates all running containers are available. The entry in the `READY` column represents \[total number of containers/number of available containers].

    3. If necessary, continue to query your deployment's status until all the pods are ready.

15. (Optional) Install a TLS certificate instead of using the default self-signed certificate in your ForgeOps deployment. Refer to [TLS certificate](prepare/security/https.html#tls-certificate) for details.

##### Alternative deployment techniques when using Kustomize

###### Staged deployments

If you prefer not to perform a ForgeOps Kustomize deployment using a single forgeops apply command, you can deploy the platform in stages, [component by component](troubleshoot/staged-deployment.html), instead of deploying with a single command. Staging deployments can be useful if you need to troubleshoot a deployment issue.

###### Generating Kustomize manifests and using `kubectl apply` commands

You can generate Kustomize manifests using the forgeops env command, and then deploy the platform using the kubectl apply -k command.

The forgeops env command generates Kustomize manifests for your ForgeOps deployment environment. The manifests are written to the /path/to/forgeops/kustomize/overlay/my-env directory of your `forgeops` repository clone. Advanced users who prefer to work directly with Kustomize manifests that describe their ForgeOps deployment can use the generated content in the kustomize/overlay/my-env directory as an alternative to using the forgeops command:

1. Generate an initial set of Kustomize manifests by running the forgeops env command.

2. Run kubectl apply -k commands to deploy and remove platform components. Specify a manifest in the kustomize/overlay/my-env directory as an argument when you run kubectl apply -k commands.

   1. Use GitOps to manage configuration changes to the kustomize/overlay/my-env directory.

##### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](deploy/overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](deploy/architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy/deploy.html)

* [icon: square-o, set=fa]*[Access platform UIs and APIs](deploy/access.html)*

* [icon: square-o, set=fa][Plan for production deployment](deploy/next-steps.html)

### UI and API access

This page shows you how to access and monitor the Ping Advanced Identity Software components in a ForgeOps deployment.

AM and IDM are configured for access through the Kubernetes cluster's ingress controller. You can access these components using their admin UIs and REST APIs.

DS cannot be accessed through the ingress controller, but you can use Kubernetes methods to access the DS pods.

#### AM services

To access the AM admin UI:

1. Set the active namespace in your local Kubernetes context to the namespace in which you performed the ForgeOps deployment.

2. Obtain the `amadmin` user's password:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops info | grep amadmin
   vr58qt11ihoa31zfbjsdxxrqryfw0s31 (amadmin user)
   ```

3. Open a new window or tab in a web browser.

4. Go to https\://my-fqdn/platform.

   The Kubernetes ingress controller handles the request, routing it to the `login-ui` pod.

   The login UI prompts you to log in.

5. Log in as the `amadmin` user.

   The Ping Advanced Identity Software UI appears in the browser.

6. Select Native Consoles > Access Management.

   The AM admin UI appears in the browser.

To access the AM REST APIs:

1. Start a terminal window session.

2. Run a curl command to verify that you can access the REST APIs through the ingress controller. For example:

   ```
   $ curl \
    --insecure \
    --request POST \
    --header "Content-Type: application/json" \
    --header "X-OpenAM-Username: amadmin" \
    --header "X-OpenAM-Password: vr58qt11ihoa31zfbjsdxxrqryfw0s31" \
    --header "Accept-API-Version: resource=2.0, protocol=1.0" \
    "https://my-fqdn/am/json/realms/root/authenticate"

   {
       "tokenId":"AQIC5wM2...Q..*",
       "successUrl":"/am/console",
       "realm":"/"
   }
   ```

#### IDM services

To access the IDM REST APIs:

1. Start a terminal window session.

2. Set the active namespace in your local Kubernetes context to the namespace in which you performed the ForgeOps deployment.

3. Obtain the `amadmin` user's password:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops info | grep amadmin
   vr58qt11ihoa31zfbjsdxxrqryfw0s31 (amadmin user)
   ```

4. AM authorizes IDM REST API access using the [OAuth 2.0 authorization code flow](https://docs.pingidentity.com/pingam/8/oauth2-guide/oauth2-authz-grant.html). ForgeOps deployments come with the `idm-admin-ui` client, which is configured to let you get a bearer token using this OAuth 2.0 flow. You'll use the bearer token in the next step to access the IDM REST API:

   1. Get a session token for the `amadmin` user:

      ```
      $ curl \
       --request POST \
       --insecure \
       --header "Content-Type: application/json" \
       --header "X-OpenAM-Username: amadmin" \
       --header "X-OpenAM-Password: vr58qt11ihoa31zfbjsdxxrqryfw0s31" \
       --header "Accept-API-Version: resource=2.0, protocol=1.0" \
       'https://my-fqdn/am/json/realms/root/authenticate'
      {
       "tokenId":"AQIC5wM...Q..*",
       "successUrl":"/am/console",
       "realm":"/"}
      ```

   2. Get an authorization code. Specify the ID of the session token that you obtained in the previous step in the `Cookie` parameter:

      ```
      $ curl \
       --dump-header - \
       --insecure \
       --request GET \
       --header "Cookie: iPlanetDirectoryPro=AQIC5wM...Q.." \
       "https://my-fqdn/am/oauth2/realms/root/authorize?redirect_uri=https://my-fqdn/platform/appAuthHelperRedirect.html&client_id=idm-admin-ui&scope=openid%20fr:idm:&response_type=code&state=abc123"

      HTTP/2 302
      ...
      code=3cItL9G52DIiBdfXRngv2_dAaYM...
      ```

   3. Exchange the authorization code for an access token. Specify the access code that you obtained in the previous step in the `code` URL parameter:

      ```
      $ curl --request POST \
       --insecure \
       --data "grant_type=authorization_code" \
       --data "code=3cItL9G52DIiBdfXRngv2_dAaYM" \
       --data "client_id=idm-admin-ui" \
       --data "redirect_uri=https://my-fqdn/platform/appAuthHelperRedirect.html" \
       "https://my-fqdn/am/oauth2/realms/root/access_token" 
      {
       "access_token":"oPzGzGFY1SeP2RkI-ZqaRQC1cDg",
       "scope":"openid fr:idm:*",
       "id_token":"eyJ0eXAiOiJKV
        ...
        sO4HYqlQ",
       "token_type":"Bearer",
       "expires_in":239
      }
      ```

5. Run a curl command to verify that you can access the `openidm/config` REST endpoint through the ingress controller. Use the access token returned in the previous step as the bearer token in the authorization header.

   The following example command provides information about the IDM configuration:

   ```
   $ curl \
    --insecure \
    --request GET \
    --header "Authorization: Bearer oPzGzGFY1SeP2RkI-ZqaRQC1cDg" \
    --data "{}" \
    \https://my-fqdn/openidm/config
   {
    "_id":"",
    "configurations":
     [
      {
       "_id":"ui.context/admin",
       "pid":"ui.context.4f0cb656-0b92-44e9-a48b-76baddda03ea",
       "factoryPid":"ui.context"
       },
       ...
      ]
   }
   ```

#### DS command-line access

The DS pods in ForgeOps deployment are not exposed outside of the cluster. If you need to access one of the DS pods, use a standard Kubernetes method:

* Execute shell commands in DS pods using the kubectl exec command.

* Forward a DS pod's LDAPS port (1636) to your local computer. Then, you can run LDAP CLI commands, for example ldapsearch. You can also use an LDAP editor such as Apache Directory Studio to access the directory.

For all ForgeOps deployment directory pods, the directory superuser DN is `uid=admin`. Obtain this user's password by running the forgeops info command.

#### ForgeOps deployment monitoring

This section describes how to access Grafana dashboards and Prometheus UI'\[[2](#_footnotedef_2 "View footnote.")]' .

##### Grafana

To access Grafana dashboards:

1. Set up port forwarding on your local computer for port 3000:

   ```
   $ /path/to/forgeops/bin/prometheus-connect.sh -G
   Forwarding from 127.0.0.1:3000 → 3000
   Forwarding from [::1]:3000 → 3000
   ```

2. In a web browser, navigate to http\://localhost:3000 to access the Grafana dashboards.

3. Log in as the `admin` user with `password` as the password.

When you're done using the Grafana UI, stop Grafana port forwarding by entering Ctrl+c in the terminal window where you initiated port forwarding.

For information about Grafana, refer to [the Grafana documentation](http://docs.grafana.org).

##### Prometheus

To access the Prometheus UI:

1. Set up port forwarding on your local computer for port 9090:

   ```
   $ /path/to/forgeops/bin/prometheus-connect.sh -P
   Forwarding from 127.0.0.1:9090 → 9090
   Forwarding from [::1]:9090 → 9090
   ```

2. In a web browser, navigate to http\://localhost:9090 to access the Prometheus UI.

When you're done using the Prometheus UI, stop Prometheus port forwarding by entering Ctrl+c in the terminal window where you initiated port forwarding.

For information about Prometheus, refer to [the Prometheus documentation](https://prometheus.io/docs/introduction/overview).

For a description of ForgeOps monitoring architecture and information about how to customize ForgeOps monitoring, refer to [ForgeOps deployment monitoring](prepare/monitoring/overview.html).

#### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps deployments](deploy/overview.html)

* [icon: check-square-o, set=fa][Understand ForgeOps architecture](deploy/architecture.html)

* [icon: check-square-o, set=fa][Deploy the platform](deploy/deploy.html)

* [icon: check-square-o, set=fa][Access platform UIs and APIs](deploy/access.html)

* [icon: square-o, set=fa]*[Plan for production deployment](deploy/next-steps.html)*

### Next steps

If you've followed the instructions for performing a ForgeOps deployment *without modifying configurations*, then the following indicates that you've been successful:

* The Kubernetes cluster and pods are up and running.

* DS, AM, and IDM are installed and running. You can access each ForgeOps component.

* DS replication and failover work as expected.'\[[1](#_footnotedef_1 "View footnote.")]'

When you're satisfied that all of these conditions are met, then you've successfully taken the first steps towards deploying the Ping Advanced Identity Software on Kubernetes. Congratulations!

You can use the ForgeOps deployment to test deployment customizations—options that you might want to use in production but are not part of the base deployment. Examples'\[[2](#_footnotedef_2 "View footnote.")]' include, but are not limited to:

* Running lightweight benchmark tests

* Backing up and restoring your data

* Securing TLS with a certificate that's dynamically obtained from Let's Encrypt

* Using an ingress controller other than the default in ForgeOps

* Resizing the cluster to meet your business requirements

* Configuring Alert Manager to issue alerts when usage thresholds have been reached

Now that you're familiar with ForgeOps deployments, you're ready to work with a project team to plan and configure your production deployment. You'll need a team with expertise in the Ping Advanced Identity Software, in your cloud provider, and in Kubernetes on your cloud provider. We strongly recommend that you engage a Ping Identity technical consultant or partner to assist you with deploying the platform in production.

You'll perform these major activities:

Platform configuration—Ping Advanced Identity Software experts configure AM and IDM using single-instance ForgeOps deployments and build custom Docker images for the Ping Advanced Identity Software. The [Customization overview](customize/overview.html) provides information about platform configuration tasks.

Cluster configuration—Cloud technology experts configure the Kubernetes cluster that will host the Ping Advanced Identity Software for optimal performance and reliability. Tasks include configuring your Kubernetes cluster to suit your business needs, setting up monitoring and alerts to track site health and performance, backing up configuration and user data for disaster preparedness, and securing your deployment. The [Prepare to deploy in production](prepare/overview.html) and READMEs in the `forgeops` repository provide information about cluster configuration.

Site reliability engineering—Site reliability engineers monitor the Ping Advanced Identity Software deployment and keep the deployment up and running based on your business requirements. These could include use cases, service-level agreements, thresholds, and load test profiles. The [Prepare to deploy in production](prepare/overview.html), and READMEs in the `forgeops` repository, provide information about site reliability.

### Remove a ForgeOps deployment

This page provides instructions for removing ForgeOps deployments for the following scenarios:

* [Remove a Helm deployment on GKE, EKS, or AKS](#helm-cloud)

* [Remove a Helm deployment on minikube](#helm-local)

* [Remove a Kustomize deployment on GKE, EKS, or AKS](#kustomize-cloud)

* [Remove a Kustomize deployment on minikube](#kustomize-local)

#### Remove a Helm deployment from GKE, EKS, or AKS

1. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster in which you deployed the platform.

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace in which you deployed the platform:

      ```
      $ kubens my-namespace
      ```

2. Remove the ForgeOps deployment:

   ```
   $ cd /path/to/forgeops/charts/identity-platform
   $ helm uninstall identity-platform
   ```

   Running helm uninstall identity-platform doesn't delete PVCs and the `amster` job from your namespace.

3. (Optional) To delete PVCs, use the kubectl command. For example, to delete `data-ds-idrepo-0` and `data-ds-cts-0`:

   ```
   $ kubectl delete pvc data-ds-idrepo-0 data-ds-cts-0
   ```

4. (Optional) To delete the `amster` job, use the kubectl command:

   ```
   $ kubectl delete job amster
   ```

5. (Optional) Delete your cluster:

   1. Change to the directory in your `forgeops-extras` repository clone that contains Terraform artifacts:

      ```
      $ cd /path/to/forgeops-extras/terraform
      ```

   2. Run the tf-destroy script to create your cluster:

      ```
      $ ./tf-destroy
      ```

      Respond `yes` to the `Do you really want to destroy all resources?` prompt.

#### Remove a Helm deployment from minikube

1. Set the active namespace in your Kubernetes context to the Kubernetes namespace in which you deployed the platform:

   ```
   $ kubens my-namespace
   ```

2. Remove the ForgeOps deployment:

   ```
   $ cd /path/to/forgeops/charts/identity-platform
   $ helm uninstall identity-platform
   ```

   Running helm uninstall identity-platform doesn't delete PVCs and the `amster` job from your namespace.

3. (Optional) To delete PVCs, use the kubectl command. For example, to delete `data-ds-idrepo-0` and `data-ds-cts-0`:

   ```
   $ kubectl delete pvc data-ds-idrepo-0 data-ds-cts-0
   ```

4. (Optional) To delete the `amster` job, use the kubectl command:

   ```
   $ kubectl delete job amster
   ```

5. (Optional) Delete your cluster:

   ```
   $ minikube stop
   $ minikube delete
   ```

#### Remove a Kustomize deployment from GKE, EKS, or AKS

1. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster in which you deployed the platform.

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace in which you deployed the platform:

      ```
      $ kubens my-namespace
      ```

2. Remove the ForgeOps deployment:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops delete --env-name my-env
   ```

   Respond `Y` to all the `OK to delete?` prompts.

3. (Optional) Delete your cluster:

   1. Change to the directory in your `forgeops-extras` repository clone that contains Terraform artifacts:

      ```
      $ cd /path/to/forgeops-extras/terraform
      ```

   2. Run the tf-destroy script to create your cluster:

      ```
      $ ./tf-destroy
      ```

      Respond `yes` to the `Do you really want to destroy all resources?` prompt.

#### Remove a Kustomize deployment from minikube

1. Set the active namespace in your Kubernetes context to the Kubernetes namespace in which you deployed the platform:

   ```
   $ kubens my-namespace
   ```

2. Remove the ForgeOps deployment:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops delete --env-name my-env
   ```

   Respond `Y` to all the `OK to delete?` prompts.

3. (Optional) Delete your cluster:

   ```
   $ minikube stop
   $ minikube delete
   ```

## Customization overview

This section covers how developers build custom Docker images for the Ping Advanced Identity Software. It also contains important conceptual material that you need to understand before you start creating Docker images.

* Configuration container

  In ForgeOps release 2026.1, AM and IDM configuration profiles have been moved out of the PingAM and PingIDM images into dedicated [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") containers. You can now customize the configuration profiles and rebuild only the configuration [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") images.

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | It is highly recommended to deploy the latest platform images in a production environment only after due customization and testing. |

### Developer checklist

Setup:

* [icon: square-o, set=fa]*[Perform additional setup](customize/setup.html)*

* [icon: square-o, set=fa][Understand custom images](customize/custom-images.html)

DS customization:

* [icon: square-o, set=fa][Customize the DS image](customize/ds.html)

AM and IDM customization:

* [icon: square-o, set=fa][Understand AM and IDM configuration](customize/fr-data.html)

* [icon: square-o, set=fa][Understand property value substitution](customize/value-substitution.html)

* [icon: square-o, set=fa][Customize the AM image](customize/am.html)

* [icon: square-o, set=fa][Customize the IDM image](customize/idm.html)

### Additional setup

This page covers setup tasks that you'll need to perform before you can develop custom Docker images for the Ping Advanced Identity Software. Complete all of the tasks on this page before proceeding.

#### Use a single-instance ForgeOps deployment

You must use a [single-instance ForgeOps deployment](deploy/architecture.html#cluster-and-deployment-sizes) to develop custom Docker images for the Ping Advanced Identity Software.

Use the following links for information about how to create single-instance ForgeOps deployments:

* [Deploy using Helm on GKE, EKS, or AKS](deploy/deploy-scenario-helm-cloud.html)

* [Deploy using Helm on minikube](deploy/deploy-scenario-helm-local.html)

* [Deploy using Kustomize on GKE, EKS, or AKS](deploy/deploy-scenario-kustomize-cloud.html)

* [Deploy using Kustomize on minikube](deploy/deploy-scenario-kustomize-local.html)

#### Set up your environment to push to your Docker registry

ForgeOps deployments support any container registry that supports Docker containers. You'll need to set up your local environment to support your container registry. Here are setup steps for four commonly-used container registries:

> **Collapse: Docker registry on minikube**
>
> Set up your local environment to execute docker commands on minikube's Docker engine.
>
> The ForgeOps team recommends using the built-in Docker engine when developing custom Docker images using minikube. When you use minikube's Docker engine, you don't have to build Docker images on a local engine and then push the images to a local or cloud-based Docker registry. Instead, you build images using the same Docker engine that minikube uses. This streamlines development.
>
> To set up your local computer to use minikube's Docker engine, run the docker-env command in your shell:
>
> ```
> $ eval $(minikube docker-env)
> ```
>
> For more information about using minikube's built-in Docker engine, refer to [Use local images by re-using the Docker daemon](https://kubernetes.io/docs/setup/learning-environment/minikube/#use-local-images-by-re-using-the-docker-daemon) in the minikube documentation.

> **Collapse: Google Cloud Artifact Registry or Container Registry**
>
> To set up your local computer to build and push Docker images:
>
> 1. If it's not already running, start a virtual machine that runs Docker engine. Refer to [Docker engine](setup/google-cloud.html#docker-gcp) for more information.
>
> 2. Set up a Docker credential helper:
>
>    ```
>    $ gcloud auth configure-docker
>    ```

> **Collapse: AWS Elastic Container Registry**
>
> To set up your local computer to push Docker images:
>
> 1. If it's not already running, start a virtual machine that runs Docker engine. Refer to [Docker engine](setup/aws.html#docker-aws) for more information.
>
> 2. Log in to Amazon ECR:
>
>    ```
>    $ aws ecr get-login-password | \
>     docker login --username AWS --password-stdin my-docker-registry
>    Login Succeeded
>    ```
>
>    ECR login sessions expire after 12 hours. Because of this, you'll need to perform these steps again whenever your login session expires.\[[16](#_footnotedef_16 "View footnote.")]

> **Collapse: Azure Container Registry**
>
> To set up your local computer to push Docker images:
>
> 1. If it's not already running, start a virtual machine that runs Docker engine. Refer to [Docker engine](setup/azure.html#docker-azure) for more information.
>
> 2. Install the [ACR Docker Credential Helper](https://github.com/Azure/acr-docker-credential-helper).

#### Identify the Docker repository to push to

When you execute the forgeops build command, you must specify the repository to push your Docker image to with the --push-to argument.

The forgeops build command appends a component name to the destination repository. For example, the command forgeops build am --push-to us-docker.pkg.dev/my-project pushes a Docker image to the `us-docker.pkg.dev/my-project/am` repository.

To determine how to specify the --push-to argument for four commonly-used container registries:

> **Collapse: Docker registry on minikube**
>
> Specify --push-to none with the forgeops build command to push the Docker image to the Docker registry embedded in the minikube cluster.

> **Collapse: Google Cloud Artifact Registry or Container Registry**
>
> Obtain the --push-to location from your cluster administrator. After it builds the Docker image, the forgeops build command pushes the Docker image to this repository.

> **Collapse: AWS Elastic Container Registry**
>
> Obtain the --push-to location from your cluster administrator. After it builds the Docker image, the forgeops build command pushes the Docker image to this repository.

> **Collapse: Azure Container Registry**
>
> Obtain the --push-to location from your cluster administrator. After it builds the Docker image, the forgeops build command pushes the Docker image to this repository.

#### Initialize deployment environments

Deployment environments let you manage deployment manifests and image defaulters for multiple environments in a single `forgeops` repository clone.

By default, the forgeops build command updates the image defaulter in the kustomize/deploy directory.

When you specify a deployment environment, the forgeops build command updates the image defaulter in the kustomize/deploy-environment directory. For example, if you ran forgeops build --deploy-env production, the image defaulter in the kustomize/deploy-production/image-defaulter directory would be updated.

Before you can use a new deployment environment, you must initialize a directory based on the /path/to/forgeops/kustomize/deploy directory to support the deployment environment. Perform these steps to initialize a new deployment environment:

```
$ cd /path/to/forgeops/bin
$ ./forgeops clean
$ cd ../kustomize
$ cp -rp deploy deploy-my-environment
```

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | If you need multiple deployment environments, you'll need to initialize each environment before you can start using it. |

#### Next step

* [icon: check-square-o, set=fa][Perform additional setup](customize/setup.html)

* [icon: square-o, set=fa]*[Understand custom images](customize/custom-images.html)*

* [icon: square-o, set=fa][Customize the DS image](customize/ds.html)

* [icon: square-o, set=fa][Understand AM and IDM configuration](customize/fr-data.html)

* [icon: square-o, set=fa][Understand property value substitution](customize/value-substitution.html)

* [icon: square-o, set=fa][Customize the AM image](customize/am.html)

* [icon: square-o, set=fa][Customize the IDM image](customize/idm.html)

### About custom images

#### In development

To develop customized Docker images, start with ForgeOps-provided images. Then, build your configuration profile iteratively as you customize the platform to meet your needs. Building Docker images from time to time integrates your custom configuration profile into new Docker images.

To develop a customized DS Docker image, refer to [`ds` image](customize/ds.html).

To develop a customized AM Docker image, refer to [`am` image](customize/am.html).

To develop a customized IDM Docker image, refer to [`idm` image](customize/idm.html).

![Brief overview of containers for developers.](customize/_images/containerization-dev.svg)

#### In production

You can incorporate your configuration changes into the [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container. To deploy the platform in production, build your configuration [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container images and integrate in your ForgeOps deployment. The platform images are designed to work with configuration [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") containers, so you can use the latest platform images in production without building new PingAM and PingIDM base images. You don't need to build PingAM and PingIDM base images for production deployment.

Learn more about how to create Docker images for production deployment of the platform in [Base Docker images](reference/base-docker-images.html).

![Brief overview of containers used in production.](customize/_images/containerization-prod.svg)

#### Next step

* [icon: check-square-o, set=fa][Perform additional setup](customize/setup.html)

* [icon: check-square-o, set=fa][Understand custom images](customize/custom-images.html)

* [icon: square-o, set=fa]*[Customize the DS image](customize/ds.html)*

* [icon: square-o, set=fa][Understand AM and IDM configuration](customize/fr-data.html)

* [icon: square-o, set=fa][Understand property value substitution](customize/value-substitution.html)

* [icon: square-o, set=fa][Customize the AM image](customize/am.html)

* [icon: square-o, set=fa][Customize the IDM image](customize/idm.html)

### `ds` image

The `ds` Docker image contains the DS configuration. You can customize the DS image before deploying it in your production environment.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | The customization described here is for use in new Ping Advanced Identity Software deployments. |

This section covers:

* Customize LDAP configuration by including LDIF format LDAP configuration files in `ldif-ext` directory.

* Customize LDAP schema by including customized schema LDIF files in the `config` directory.

* Customize DS setup behavior by updating the setup and post-init runtime scripts in the `runtime-scripts` directory.

* Build an updated DS Docker image that contains the above-mentioned customizations.

* Redeploy DS.

* Verify the changes you've made to the DS configuration are in the new Docker image.

#### Detailed steps

1. Verify that:

   * You have access to a [single-instance ForgeOps deployment](deploy/architecture.html#cluster-and-deployment-sizes).

   * The namespace where the platform is deployed is set in your Kubernetes context.

   * All required third-party software is installed in your local environment ([minikube](setup/minikube.html#minikube-third-party-software)|[GKE](setup/google-cloud.html#gcp-third-party-software)|[EKS](setup/aws.html#aws-third-party-software)|[AKS](setup/azure.html#azure-third-party-software)).

   * You've [set up your environment to push to your Docker registry](customize/setup.html#docker-push).

2. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. (Optional) Run the git commit command to commit the changes.

3. Add your DS customizations:

   1. Learn more at [custom LDAP configuration](https://community.forgerock.com/t/forgeops-ds-customization-guide-7-4-7-5/5525#adding-custom-ldap-configuration-3) to add LDAP configuration.

   2. Learn more in [custom LDAP schema](https://community.forgerock.com/t/forgeops-ds-customization-guide-7-4-7-5/5525#adding-custom-ldap-schema-4) to add LDAP schema.

   3. Customize DS's setup behavior in the /path/to/forgeops/docker/ds/ds-new directory:

      1. To set up profiles and indexes, edit the `runtime-scripts/setup` script. Learn more in [`setup` script details](https://community.forgerock.com/t/forgeops-ds-script-guide-7-4-7-5/5522#setup-15).

      2. To add custom configurations after indexes have been rebuilt, edit the `runtime-scripts/post-init` script. Learn more in [`post-init` script details](https://community.forgerock.com/t/forgeops-ds-script-guide-7-4-7-5/5522#post-init-12).

      3. To prepare the DS docker image for setup, edit the `ds-setup.sh` script. Learn more in [`ds-setup.sh` script details](https://community.forgerock.com/t/forgeops-ds-script-guide-7-4-7-5/5522#ds-setupsh-5).

4. [Identify the repository](customize/setup.html#push-to) where you'll push the Docker image. You'll use this location to specify the --push-to argument value in the [build ds image](#build-ds) step.

5. Decide on the DS image tag for each build of the image. You'll use this tag to specify the `--tag` argument value in the [build DS image](#build-ds) step.

6. []()Build a new DS image that includes your customization:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops build ds --env-name my-env --config-profile my-profile --push-to my-repo --tag my-ds-tag
   ```

7. Redeploy DS using your new DS image:

* Deploy using the `forgeops` command

* Deploy using Helm

The `forgeops build` command calls Docker to build a new `ds` Docker image and to push the image to your Docker repository. The new image includes your custom LDAP and schema files. It also updates the image defaulter file so that the next time you install DS, the deployed DS server includes your custom DS image.

Perform version control activities on your `forgeops` repository clone:

1. Run the git status command.

   Review the state of the kustomize/overlay/my-env/image-defaulter/kustomization.yaml file.

2. (Optional) Run the git commit command to commit changes to the image defaulter file.

3. Remove DS from your ForgeOps deployment:

   ```
   $ ./forgeops delete ds --env-name my-env
   ...
   deployment.apps "ds" deleted
   ```

4. Delete the PVCs attached to DS pods using the kubectl delete pvc command.

5. Redeploy DS using the new Docker image:

   ```
   $ ./forgeops apply ds --env-name my-env --single-instance
   Checking cert-manager and related CRDs: cert-manager CRD found in cluster.
   Checking secret-agent operator and related CRDs: secret-agent CRD found in cluster
   ```

1) Locate the repository and tag for the new DS Docker image from the forgeops build command output.

2) Delete the PVCs attached to DS pods using the kubectl delete pvc command.

   If the attached DS pod is running, the PVC is not deleted immediately. So you should stop the running DS pods.

   In another terminal window, stop the DS pods using the kubectl delete pods command. This deletes the pods and its attached PVC.

3) Redeploy DS using the new Docker image:

   ```
   $ cd /path/to/forgeops/charts/identity-platform
   $ helm upgrade identity-platform ./ \
    --namespace my-namespace \
    --set 'ds.image.repository=my-repository' \
    --set 'ds.image.tag=my-ds-tag'
   ```

#### Next step

* [icon: check-square-o, set=fa][Perform additional setup](customize/setup.html)

* [icon: check-square-o, set=fa][Understand custom images](customize/custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](customize/ds.html)

* [icon: square-o, set=fa]*[Understand AM and IDM configuration](customize/fr-data.html)*

* [icon: square-o, set=fa][Understand property value substitution](customize/value-substitution.html)

* [icon: square-o, set=fa][Customize the AM image](customize/am.html)

* [icon: square-o, set=fa][Customize the IDM image](customize/idm.html)

### `am` and `idm` images

AM and IDM use two types of configuration: [static configuration](#static-configuration) and [dynamic configuration](#dynamic-configuration).

#### Static configuration

Static configuration consists of properties and settings used by the Ping Advanced Identity Software. Examples of static configuration include AM realms, AM authentication trees, IDM social identity provider definitions, and IDM data mapping models for reconciliation.

Static configuration is stored in JSON configuration files. Because of this, static configuration is also referred to as *file-based configuration*.

You build static configuration into the `am` and `idm` Docker images during development using the following general process:

1. Change the AM or IDM configuration in a single-instance ForgeOps deployment using the UIs and APIs.

2. Export the changes to your `forgeops` repository clone.

3. Build a new AM or IDM Docker image that contains the updated configuration.

4. Restart Ping Advanced Identity Software services using the new Docker images.

5. Test your changes. Incorrect changes to static configuration might cause the platform to become inoperable.

6. Promote your changes to your test and production environments as desired.

Refer to [`am` image](customize/am.html) and [`idm` image](customize/idm.html) for more detailed steps.

In Ping Advanced Identity Software deployments, static configuration is *immutable*. Do not change static configuration in testing or production. Instead, if you need to change static configuration, return to the development phase, make your changes, and build new custom Docker images that include the changes. Then, promote the new images to your test and production environments.

#### Dynamic configuration

Dynamic configuration consists of access policies, applications, and data objects used by the Ping Advanced Identity Software. Examples of dynamic configuration include AM access policies, AM agents, AM OAuth 2.0 client definitions, IDM identities, and IDM relationships.

Dynamic configuration can change at any time, including when the platform is running in production.

You'll need to devise a strategy for managing AM and IDM dynamic configuration, so that you can:

* Extract sample dynamic configuration for use by developers.

* Back up and restore dynamic configuration.

##### Tips for managing AM dynamic configuration

You can use one or both of the following techniques to manage AM dynamic configuration:

* Use the forgeops amster command to manage AM dynamic configuration. For example:

  1. Make modifications to AM dynamic configuration by using the AM admin UI.

  2. Export the AM dynamic configuration to your local file system by using the forgeops amster command. You might manage these files in a Git repository. For example:

     ```
     $ cd /path/to/forgeops/bin
     $ mkdir /tmp/amster
     $ ./forgeops amster export --env-name my-env /tmp/amster
     Cleaning up amster components
     Packing and uploading configs
     configmap/amster-files created
     configmap/amster-export-type created
     Deploying amster
     job.batch/amster created

     Waiting for amster job to complete. This can take several minutes.
     pod/amster-r99l9 condition met
     tar: Removing leading `/' from member names
     Updating amster config.
     Updating amster config complete.
     Cleaning up amster components
     job.batch "amster" deleted
     configmap "amster-files" deleted
     configmap "amster-export-type" deleted
     ```

  3. If desired, import these files into another AM deployment by using the forgeops amster import command.

  Note that the forgeops amster command automatically converts passwords in AM dynamic configuration to configuration expressions. Because of this, passwords in AM configuration files will not appear in cleartext. For details about how to work with dynamic configuration that has passwords and other properties specified as configuration expressions, refer to [Export Utilities and Configuration Expressions](customize/value-substitution.html#export-config-expr).

* Write REST API applications to import and export AM dynamic configuration. For more information, refer to [Rest API](https://docs.pingidentity.com/pingam/8/REST-guide/preface.html) in the AM documentation.

##### Tips for managing IDM dynamic configuration

You can use one or both of the following techniques to manage IDM dynamic configuration:

* Migrate dynamic configuration by using IDM's Data Migration Service. For more information, refer to [Migrate Data](https://docs.pingidentity.com/pingidm/8/upgrade-guide/data-migration.html) in the IDM documentation.

* Write REST API applications to import and export IDM dynamic configuration. For more information, refer to the [Rest API Reference](https://docs.pingidentity.com/pingidm/8/rest-api-reference/preface.html) in the IDM documentation.

#### Configuration profiles

A Ping Advanced Identity Software *configuration profile* is a named set of configuration that describes the operational characteristics of a running ForgeOps deployment. A configuration profile consists of:

* AM static configuration

* IDM static configuration

Configuration profiles reside in the following paths in the `forgeops` repository:

* docker/am/config-profiles

* docker/idm/config-profiles

User-customized configuration profiles are stored in subdirectories of these paths. For example, a configuration profile named `my-profile` would be stored in the paths docker/am/config-profiles/my-profile and docker/idm/config-profiles/my-profile.

Use Git to manage the directories that contain configuration profiles.

#### Next step

* [icon: check-square-o, set=fa][Perform additional setup](customize/setup.html)

* [icon: check-square-o, set=fa][Understand custom images](customize/custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](customize/ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](customize/fr-data.html)

* [icon: square-o, set=fa]*[Understand property value substitution](customize/value-substitution.html)*

* [icon: square-o, set=fa][Customize the AM image](customize/am.html)

* [icon: square-o, set=fa][Customize the IDM image](customize/idm.html)

#### About property value substitution

Many property values in ForgeOps deployments' canonical configuration profile are specified as *configuration expressions* instead of as hard-coded values. Fully-qualified domain names (FQDNs), passwords, and several other properties are all specified as configuration expressions.

Configuration expressions are property values in the AM and IDM configurations that are set when AM and IDM start up. Instead of being set to fixed, hard-coded values in the AM and IDM configurations, their values vary, depending on conditions in the run-time environment.

Using configuration expressions lets you use a single configuration profile that takes different values at run-time depending on the deployment environment. For example, you can use a single configuration profile for development, test, and production deployments.

In the Ping Advanced Identity Software, configuration expressions are preceded by an ampersand and enclosed in braces. For example, `&{am.encryption.key}`.

The statement, `am.encryption.pwd=&{am.encryption.key}` in the AM configuration indicates that the value of the property, `am.encryption.pwd`, is determined when AM starts up. Contrast this with a statement, `am.encryption.pwd=myPassw0rd`, which sets the property to a hard-coded value, `myPassw0rd`, regardless of the run-time environment.

##### How property value substitution works

This example shows how property value substitution works for a value specified as a configuration expression in the AM configuration:

1. Search the /path/to/forgeops/docker directory for the string `&{`.

2. Locate this line in your search results:

   ```
   "am.encryption.pwd=&{am.encryption.key}",
   ```

   Because the property `am.encryption.pwd` is being set to a configuration expression, its value will be determined when AM starts up.

3. Search the `forgeops` repository for the string `AM_ENCRYPTION_KEY`. You'll notice that the secret agent operator sets the environment variable, `AM_ENCRYPTION_KEY`. The property, `am.encryption.pwd`, will be set to the value of the environment variable, `AM_ENCRYPTION_KEY` when AM starts up.

Configuration expressions take their values from environment variables as follows:

* Uppercase characters replace lowercase characters in the configuration expression's name.

* Underscores replace periods in the configuration expression's name.

For more information about configuration expressions, refer to [Property Value Substitution](https://docs.pingidentity.com/pingidm/8/setup-guide/using-property-substitution.html) in the IDM documentation.

##### Export utilities and configuration expressions

This section covers differences in how `forgeops` repository utilities export configuration that contains configuration expressions from a running ForgeOps deployment.

###### In the IDM configuration

The IDM admin UI is aware of configuration expressions.

Passwords specified as configuration expressions are stored in IDM's JSON-based configuration files as configuration expressions.

[](#idm_static_configuration_export)IDM static configuration export

The `forgeops` repository's bin/config export idm command exports IDM static configuration from running ForgeOps deployments to your `forgeops` repository clone. The config utility makes no changes to IDM static configuration; if properties are specified as configuration expressions, the configuration expressions are preserved in the IDM configuration.

###### In the AM configuration

The AM admin UI is *not* aware of configuration expressions.

Properties cannot be specified as configuration expressions in the AM admin UI; they must be specified as string values. The string values are preserved in the AM configuration.

AM supports specifying configuration expressions in both static and dynamic configuration.

[](#am_static_configuration_export)AM static configuration export

The `forgeops` repository's bin/config export am command exports AM static configuration from running ForgeOps deployments to your `forgeops` repository clone. All AM static configuration properties, including passwords, have string values. However, after the config utility copies the AM static configuration from the `forgeops` repository, it calls the AM configuration upgrader. The upgrader transforms the AM configuration, following rules in the etc/am-upgrader-rules/placeholders.groovy file.

These rules tell the upgrader to convert a number of string values in AM static configuration to configuration expressions. For example, there are rules to convert all the passwords in AM static configuration to configuration expressions.

You'll need to modify the etc/am-upgrader-rules/placeholders.groovy file if:

* You add AM static configuration that contains new passwords.

* You want to change additional properties in AM static configuration to use configuration expressions.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An alternative to modifying the etc/am-upgrader-rules/placeholders.groovy file is using the jq command to modify the output from the config utility. |

[](#am_dynamic_configuration_export)AM dynamic configuration export

The `forgeops` repository's forgeops amster export command exports AM dynamic configuration from running ForgeOps deployments to your `forgeops` repository clone. When dynamic configuration is exported, it contains properties with string values. The forgeops amster export command transforms values for several types of properties to configuration expressions:

* Passwords

* Fully-qualified domain names

* The Amster version

The Secret Agent configuration computes and propagates passwords for AM dynamic configuration. You'll need to modify the `kustomize/base/secrets/secret_agent_config.yaml` file if:

* You add new AM dynamic configuration that contains passwords to be generated.

* You want to hard code a specific value for an existing password, instead of using a generated password.

[](#limitations_on_property_value_substitution_in_am)Limitations on property value substitution in AM

AM doesn't support property value substitution for several types of configuration properties. Refer to [Property value substitution](https://docs.pingidentity.com/pingam/8/setup-guide/property-value-substitution.html) in the AM documentation for more information.

##### Next step

* [icon: check-square-o, set=fa][Perform additional setup](customize/setup.html)

* [icon: check-square-o, set=fa][Understand custom images](customize/custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](customize/ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](customize/fr-data.html)

* [icon: check-square-o, set=fa][Understand property value substitution](customize/value-substitution.html)

* [icon: square-o, set=fa]*[Customize the AM image](customize/am.html)*

* [icon: square-o, set=fa][Customize the IDM image](customize/idm.html)

#### `am` image

Prior to the ForgeOps 2026.1 release, the `am` Docker image contained the AM configuration. In ForgeOps 2026.1 and later releases, AM configuration has been separated from the AM image into a [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container that contains the configuration profiles. This lets you customize configuration changes and build only the [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") images.

##### Customization overview

* Customize AM's configuration data by using the AM admin UI and REST APIs.

* Capture changes to the AM configuration by exporting them from the AM service running on Kubernetes to the staging area.

* Save the modified AM configuration to a configuration profile in your `forgeops` repository clone.

* Build a [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container image using the exported configuration profile.

* Redeploy AM.

* Verify that changes you've made to the AM configuration are in the new Docker image.

##### Detailed steps

1. Verify that:

   * You have access to a [single-instance ForgeOps deployment](deploy/architecture.html#cluster-and-deployment-sizes).

   * The namespace where the platform is deployed is set in your Kubernetes context.

   * All required third-party software is installed in your local environment ([minikube](setup/minikube.html#minikube-third-party-software)|[GKE](setup/google-cloud.html#gcp-third-party-software)|[EKS](setup/aws.html#aws-third-party-software)|[AKS](setup/azure.html#azure-third-party-software)).

   * You've [set up your environment to push to your Docker registry](customize/setup.html#docker-push).

2. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. Review the state of the docker/am/config-profiles/my-profile directory.

   3. (Optional) Run the git commit command to commit changes to files that have been modified.

3. Modify the AM configuration using the AM admin UI or the REST APIs.

   You can find more information about how to access the AM admin UI or REST APIs in [AM Services](deploy/access.html#am-services-cdm).

   You can find important information about configuring values that vary at run-time, such as passwords and host names in [About property value substitution](customize/value-substitution.html).

4. Export the changes you made to the AM configuration in the running ForgeOps deployment to a configuration profile. To use the version of `am-config-upgrader` for your release, speciy the `--release-name` option:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops config export am --release-name my-release my-profile --sort
   ...
   ```

   If the configuration profile doesn't exist yet, the forgeops config export command creates it.

   The forgeops config export am my-profile command copies AM static configuration from the ForgeOps deployment to the configuration profile:

   ![Exporting the configuration from the single-instance deployment to a configuration profile.](customize/_images/config-export-am.svg)

5. Perform version control activities on your `forgeops` repository clone:

   1. Review the differences in the files you exported to the configuration profile. For example:

      ```
      $ git diff
      diff --git a/docker/am/config-profiles/my-profile/config/services/realm/root/selfservicetrees/1.0/organizationconfig/default.json b/docker/am/config-profiles/my-profile/config/services/realm/root/selfservicetrees/1.0/organizationconfig/default.json
      index 970c5a257..19f4f17f0 100644
      --- a/docker/am/config-profiles/my-profile/config/services/realm/root/selfservicetrees/1.0/organizationconfig/default.json
      + b/docker/am/config-profiles/my-profile/config/services/realm/root/selfservicetrees/1.0/organizationconfig/default.json
      @@ -9,6 +9,7 @@
           "enabled": true,
           "treeMapping": {
             "Test": "Test",
      +      "Test1": "Test1",
             "forgottenUsername": "ForgottenUsername",
             "registration": "Registration",
             "resetPassword": "ResetPassword",
      ```

      The first time you export AM configuration changes to a configuration profile, the git diff command doesn't show any changes.

   2. Run the git status command.

   3. If you have new untracked files in your clone, run the git add command.

   4. Review the state of the docker/am/config-profiles/my-profile directory.

   5. (Optional) Run the git commit command to commit changes to files that have been modified.

6. [Identify the repository](customize/setup.html#push-to) to which you'll push the Docker image. You'll use this location to specify the --push-to argument value in the [build am image](#build-am) step.

7. Decide on the image tag name to tag each build of the image. You'll use this tag name to specify the --tag argument in the [build am image](#build-am) step.

8. []()Build a new `BusyBox` image that includes AM static configuration change:

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | While the forgeops build command uses the Docker engine by default for ForgeOps deployments, it supports Podman as well. If you are using Podman engine instead of Docker in your environment, then set the `CONTAINER_ENGINE` environment variable to `podman` before running the forgeops build command, for example:```
   $ export CONTAINER_ENGINE="podman"
   ``` |

   ```
   $ ./forgeops config build --env-name my-env am \
     --config-profile my-profile --push-to my-repo --tag my-am-tag
   ...
   ```

9. Redeploy AM using your new AM [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") image:

   * If you installed the platform using the forgeops command, follow the steps in [Redeploy AM: Kustomize deployments](#redeploy-am-forgeops-command).

   * If you installed the platform using Helm, follow the steps in [Redeploy AM: Helm deployments](#redeploy-am-helm).

###### Redeploy AM: Kustomize deployments

The forgeops build command calls Docker to build a new `am` Docker image and to push the image to your Docker repository. The new image includes your configuration profile. It also updates the [image defaulter](https://github.com/ForgeRock/forgeops/blob/2026.2.1/kustomize/overlay/default/image-defaulter/kustomization.yaml) file so that the next time you install AM, the forgeops apply command gets AM static configuration from your new custom Docker image.

![Building the new custom Docker image.](customize/_images/cdk-build.svg)

1. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. Review the state of the kustomize/overlay/my-env/image-defaulter/kustomization.yaml file.

   3. (Optional) Run the git commit command to commit changes to the image defaulter file.

2. Remove AM from your ForgeOps deployment:

   ```
   $ ./forgeops delete am --env-name my-env
   ... platform detected in namespace: "my-namespace".
   Uninstalling component(s): ['am'] from namespace: "my-namespace".
   OK to delete components? [Y/N] Y
   service "am" deleted
   deployment.apps "am" deleted
   ```

3. Redeploy AM:

   ```
   $ ./forgeops apply am --env-name my-env
   Checking cert-manager and related CRDs: cert-manager CRD found in cluster.
   Checking secret-agent operator and related CRDs: secret-agent CRD found in cluster

   Installing component(s): ['am'] ... from deployment manifests in ...

   service/am created
   deployment.apps/am created

   Enjoy your deployment!
   ```

4. Validate that AM has the expected configuration:

   * Run the kubectl get pods command to monitor the status of the AM pod. Wait until the pod is ready before proceeding to the next step.

   * Describe the AM pod. Locate the tag of the Docker image that Kubernetes loaded, and verify that it's your new custom Docker image's tag.

   * Start the AM admin UI and verify that your configuration changes are present.

###### Redeploy AM: Helm deployments

1. Locate the `Successfully tagged` message in the forgeops build output, which contains the new AM Docker image's repository and tag.

2. Redeploy AM using the new AM Docker image:

   ```
   $ helm upgrade identity-platform ./ \
    --namespace my-namespace \
    --values /path/to/forgeops/helm/my-env/values.yaml
   ```

3. Validate that AM has the expected configuration:

   * Run the kubectl get pods command to monitor the status of the AM pod. Wait until the pod is ready before proceeding to the next step.

   * Describe the AM pod. Locate the tag of the Docker image that Kubernetes loaded, and verify that it's your new custom Docker image's tag.

   * Start the AM admin UI and verify that your configuration changes are present.

##### Next step

* [icon: check-square-o, set=fa][Perform additional setup](customize/setup.html)

* [icon: check-square-o, set=fa][Understand custom images](customize/custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](customize/ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](customize/fr-data.html)

* [icon: check-square-o, set=fa][Understand property value substitution](customize/value-substitution.html)

* [icon: check-square-o, set=fa][Customize the AM image](customize/am.html)

* [icon: square-o, set=fa]*[Customize the IDM image](customize/idm.html)*

#### `idm` image

Prior to the ForgeOps 2026.1 release, the `idm` Docker image contained the IDM configuration. In ForgeOps 2026.1 and later releases, IDM configuration has been separated from the IDM image into a [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container that contains the configuration profiles. This lets you customize configuration changes and build only the [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") images.

##### Customization overview

* Customize IDM's configuration data by using the REST APIs.

* Capture changes to the IDM configuration by exporting them from the IDM service running on Kubernetes to the staging area.

* Save the modified IDM configuration to a configuration profile in your `forgeops` repository clone.

* Build a [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") container image using the exported configuration profile.

* Redeploy IDM.

* Verify that changes you've made to the IDM configuration are in the new Docker image.

##### Detailed steps

1. Verify that:

   * You have access to a [single-instance ForgeOps deployment](deploy/architecture.html#cluster-and-deployment-sizes).

   * The namespace where the platform is deployed is set in your Kubernetes context.

   * All required third-party software is installed in your local environment ([minikube](setup/minikube.html#minikube-third-party-software)|[GKE](setup/google-cloud.html#gcp-third-party-software)|[EKS](setup/aws.html#aws-third-party-software)|[AKS](setup/azure.html#azure-third-party-software)).

   * You've [set up your environment to push to your Docker registry](customize/setup.html#docker-push).

2. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. Review the state of the docker/idm/config-profiles/my-profile directory.

   3. (Optional) Run the git commit command to commit changes to files that have been modified.

3. Modify the IDM configuration using the REST APIs.

   Learn more about how to access the REST APIs in [IDM Services](deploy/access.html#idm-services-cdm).

   More information about configuring values that vary at run-time, such as passwords and host names is available in [About property value substitution](customize/value-substitution.html).

4. Export the changes you made to the IDM configuration in the running ForgeOps deployment to a configuration profile:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops config export idm my-profile --sort
   ...
   ```

   If the configuration profile doesn't exist yet, the forgeops config export command creates it.

   The forgeops config export idm my-profile command copies IDM static configuration from the ForgeOps deployment to the configuration profile:

   ![Exporting the configuration from the single-instance deployment to a configuration profile.](customize/_images/config-export-idm.svg)

5. Perform version control activities on your `forgeops` repository clone:

   1. Review the differences in the files you exported to the configuration profile. For example:

      ```
      $ git diff
      diff --git a/docker/idm/config-profiles/my-profile/conf/audit.json b/docker/idm/config-profiles/my-profile/conf/audit.json
      index 0b3dbeed6..1e5419eeb 100644
      --- a/docker/idm/config-profiles/my-profile/conf/audit.json
      + b/docker/idm/config-profiles/my-profile/conf/audit.json
      @@ -135,7 +135,9 @@
         },
         "exceptionFormatter": {
           "file": "bin/defaults/script/audit/stacktraceFormatter.js",
      -    "globals": {},
      +    "globals": {
      +      "Test": "Test value"
      +    },
           "type": "text/javascript"
         }
       }
      ```

      The first time you export IDM configuration changes to a configuration profile, the git diff command doesn't show any changes.

   2. Run the git status command.

   3. If you have new untracked files in your clone, run the git add command.

   4. Review the state of the docker/idm/config-profiles/my-profile directory.

   5. (Optional) Run the git commit command to commit changes to files that have been modified.

6. [Identify the repository](customize/setup.html#push-to) to which you'll push the Docker image. You'll use this location to specify the --push-to argument value in the [build idm image](#build-idm) step.

7. Decide on the image tag name so you can tag each build of the image. You'll use this tag name to specify the --tag argument value in the [build idm image](#build-idm) step.

8. []()Build a new [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") image that includes IDM static configuration changes:

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | While the forgeops build command uses the Docker engine by default for ForgeOps deployments, it supports Podman as well. If you are using Podman engine instead of Docker in your environment, then set the `CONTAINER_ENGINE` environment variable to `podman` before running the forgeops build command, for example:```
   $ export CONTAINER_ENGINE="podman"
   ``` |

   ```
   $ ./forgeops config build --env-name my-env idm \
     --config-profile my-profile --push-to my-repo --tag my-idm-tag

   ...
   ```

9. Redeploy IDM using your new IDM [BusyBox](# "A BusyBox container is a minimal, lightweight containerized environment that includes a compact implementation of common UNIX utilities.") image:

   * If you installed the platform using the forgeops command, follow the steps in [Redeploy IDM: Kustomize deployments](#redeploy-idm-forgeops-command).

   * If you installed the platform using Helm, follow the steps in [Redeploy IDM: Helm deployments](#redeploy-idm-helm).

###### Redeploy IDM: Kustomize deployments

The forgeops build command calls Docker to build a new `idm` Docker image and to push the image to your Docker repository. The new image includes your configuration profile. It also updates the [image defaulter](https://github.com/ForgeRock/forgeops/blob/2026.2.1/kustomize/overlay/default/image-defaulter/kustomization.yaml) file so that the next time you install IDM, the forgeops apply command gets IDM static configuration from your new custom Docker image.

![Building the new custom Docker image.](customize/_images/cdk-build.svg)

1. Perform version control activities on your `forgeops` repository clone:

   1. Run the git status command.

   2. Review the state of the kustomize/overlay/my-env/image-defaulter/kustomization.yaml file.

   3. (Optional) Run the git commit command to commit changes to the image defaulter file.

2. Remove IDM from your ForgeOps deployment:

   ```
   $ ./forgeops delete idm --env-name my-env
   "cdk" platform detected in namespace: "my-namespace".
   Uninstalling component(s): ['idm'] from namespace: "my-namespace".
   OK to delete components? [Y/N] Y
   service "idm" deleted
   deployment.apps "idm" deleted
   ```

3. Redeploy IDM:

   ```
   $ ./forgeops apply idm --env-name my-env

   ...
   ```

4. Validate that IDM has the expected configuration:

   * Run the kubectl get pods command to monitor the status of the IDM pod. Wait until the pod is ready before proceeding to the next step.

   * Describe the IDM pod. Locate the tag of the Docker image that Kubernetes loaded, and verify that it's your new custom Docker image's tag.

###### Redeploy IDM: Helm deployments

1. Locate the `Successfully tagged` message in the forgeops build output, which contains the new IDM Docker image's repository and tag.

2. Redeploy IDM using the new IDM Docker image:

   ```
   $ helm upgrade identity-platform ./ \
    --version 2026.2 --namespace my-namespace \
    --values /path/to/forgeops/helm/my-env/values.yaml
   ```

3. Validate that IDM has the expected configuration:

   * Run the kubectl get pods command to monitor the status of the AM pod. Wait until the pod is ready before proceeding to the next step.

   * Describe the IDM pod. Locate the tag of the Docker image that Kubernetes loaded, and verify that it's your new custom Docker image's tag.

##### Next step

* [icon: check-square-o, set=fa][Perform additional setup](customize/setup.html)

* [icon: check-square-o, set=fa][Understand custom images](customize/custom-images.html)

* [icon: check-square-o, set=fa][Customize the DS image](customize/ds.html)

* [icon: check-square-o, set=fa][Understand AM and IDM configuration](customize/fr-data.html)

* [icon: check-square-o, set=fa][Understand property value substitution](customize/value-substitution.html)

* [icon: check-square-o, set=fa][Customize the AM image](customize/am.html)

* [icon: check-square-o, set=fa][Customize the IDM image](customize/idm.html)

## Prepare to deploy in production

After you get your ForgeOps deployment up and running, you can add deployment customizations—options that are not part of an out-of-the-box ForgeOps deployment, but which you may need when you deploy in production.

[icon: play-circle, set=fas, size=3x]

#### [Production Deployment Overview](https://docs.pingidentity.com/forgeops/2026.2/start/start-here.html#build-own-service)

Customize, deploy, and maintain a production ForgeOps deployment.

[icon: door-open, set=fas, size=3x]

#### [Identity Gateway](https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/overview.html)

Add PingGateway to your deployment.

[icon: stethoscope, set=fas, size=3x]

#### [Monitoring](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/overview.html)

Customize Prometheus monitoring and alerts.

[icon: user-lock, set=fas, size=3x]

#### [Security](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/overview.html)

Customize the security features built into ForgeOps deployments.

[icon: floppy-disk-circle-arrow-right, set=fas, size=3x]

#### [Backup](https://docs.pingidentity.com/forgeops/2026.2/backup/overview.html)

Back up and restore data, such as identities and tokens.

### PingGateway deployment

[icon: user-lock, set=fas, size=3x]

#### [Default PingGateway](https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/deploy-default-ig.html)

Add PingGateway to a ForgeOps deployment.

[icon: user-shield, set=fas, size=3x]

#### [Custom PingGateway](https://docs.pingidentity.com/forgeops/2026.2/prepare/ig/deploy-custom-ig.html)

Build a custom PingGateway image and add it to a single-instance ForgeOps deployment.

#### Deploy PingGateway

ForgeOps deployments don't include PingGateway by default.

To deploy PingGateway after you've performed a ForgeOps deployment:

1. Verify that the ForgeOps deployment is up and running.

2. Set the active namespace in your local Kubernetes context to the namespace in which you've deployed the platform components.

3. Add the - ./ig line in the default overlay file, kustomize/overlay/my-env/kustomization.yaml:

   ```
   kind: Kustomization
   apiVersion: kustomize.config.k8s.io/v1beta1
   resources:
   - ./base
   - ./secrets
   - ./ds-cts
   - ./ds-idrepo
   - ./am
   - ./amster
   - ./idm
   - ./ig
   - ./ds-set-passwords
   - ./admin-ui
   - ./end-user-ui
   - ./login-ui
   ```

4. Add PingGateway Docker image to your ForgeOps deployment configuration:

   ```
   $ cd /path/to/forgeops/bin/
   $ ./forgeops image --release 2026.3.0 ig --env-name my-env
   ```

5. Deploy PingGateway:

   1. In a Kustomize-based deployment:

      ```
      $ /path/to/forgeops/bin/forgeops apply --env-name my-env ig
      ```

   2. In a Helm-based deployment:

      ```
      $ cd /path/to/forgeops
      $ helm upgrade --install ping-gateway charts/ping-gateway/ \
        --values helm/my-env/values.yaml --namespace my-namespace
      ```

6. Run the kubectl get pods command to check the status of the PingGateway pod. Wait until the pod is ready before proceeding to the next step.

7. Verify that PingGateway is running:

   ```
   $ curl --insecure -L -X GET https://my-fqdn/ig/openig/ping -v

   ...
   > GET /ig/openig/ping HTTP/2
   > Host: my-fqdn
   > User-Agent: curl/7.64.1
   > Accept: /
   * Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
   < HTTP/2 200
   < date: Thu, 29 Jul 2021 21:07:44 GMT
   <
   * Connection #0 to host my-fqdn left intact
   * Closing connection 0
   ```

8. Verify that the reverse proxy to the IDM pod is running:

   ```
   $ curl --insecure -L -X GET https://my-fqdn/ig/openidm/info/ping -v
   ...
   * Using HTTP2, server supports multi-use
   * Connection state changed (HTTP/2 confirmed)
   * Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
   ...
   * Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
   < HTTP/2 200
   ...
   ```

#### Custom PingGateway image

The default PingGateway configuration provided for use with ForgeOps deployments is an example. Replace this configuration with your own routes before using PingGateway in your environment.

Refer to the [PingGateway Deployment Guide](https://docs.pingidentity.com/pinggateway/2026.3/devops-guide/preface.html) for configuring routes.

##### Deploy custom PingGateway image

To build a custom PingGateway image and deploy PingGateway:

1. Verify you've already set up ForgeOps deployment environment using the forgeops env command.

2. Verify that your ForgeOps deployment is up and running.

3. [Set up your environment to push to your Docker registry](customize/setup.html#docker-push).

4. Configure PingGateway by creating, modifying, or deleting rules in the /path/to/forgeops/docker/ig/config-profiles/my-profile/config/routes-service directory.

5. [Identify the repository](customize/setup.html#push-to) to which you'll push the Docker image. You'll use this location in the next step to specify the --push-to argument's value.

6. Build a new `ig` image that includes your changes to PingGateway static configuration:

   ```
   $ cd /path/to/forgeops/bin
   ...
   $ forgeops image --release 2026.3.0 --release-name my-ig-release ig
   ...
   $ ./forgeops build ig --env-name my-env \
     --config-profile my-profile --push-to my-repo
   ```

7. If PingGateway hadn't already been deployed in the existing ForgeOps deployment, add the - ./ig line in the default overlay file, kustomize/overlay/my-env/kustomization.yaml:

   ```
   kind: Kustomization
   apiVersion: kustomize.config.k8s.io/v1beta1
   resources:
   - ./base
   - ./secrets
   - ./ds-cts
   - ./ds-idrepo
   - ./am
   - ./amster
   - ./idm
   - ./ig
   - ./ds-set-passwords
   - ./admin-ui
   - ./end-user-ui
   - ./login-ui
   ```

8. Uninstall previously deployed PingGateway from your ForgeOps deployment:

   1. Set the active namespace in your local Kubernetes context to the namespace in which you've deployed the PingGateway.

   2. Delete PingGateway:

      ```
      $ ./forgeops delete --env-name my-env ig
      ...
      secret "openig-secrets-env" deleted
      service "ig" deleted
      deployment.apps "ig" deleted
      ```

9. Deploy PingGateway using your customized PingGateway image:

   1. In a Kustomize-based deployment:

      ```
      $ /path/to/forgeops/bin/forgeops apply --env-name my-env ig
      ```

   2. In a Helm-based deployment:

      ```
      $ cd /path/to/forgeops
      $  helm upgrade --install ping-gateway charts/ping-gateway/ \
        --values helm/my-env/values.yaml --namespace my-namespace
      ```

10. Run the kubectl get pods command to check the status of the PingGateway pod. Wait until the PingGateway pod is ready before proceeding to the next step.

11. Verify that your PingGateway routes work.

##### Customize the AM URL in PingGateway

To customize the AM URL in PingGateway and deploy using Helm:

1. Edit the configuration file in your ForgeOps deployment environment (`helm/my-env/values.yaml`) and add PingGateway configuration lines. For example:

   ```
   ig:
     env:
       - name: AM_URL
         value: "\http://am/my-am"
   ```

2. Redeploy PingGateway:

   ```
   $ helm upgrade --install ping-gateway charts/ping-gateway/ \
     --values helm/my-env/values.yaml --namespace my-namespace
   ```

3. Verify that the new AM URL has been set up:

   ```
   $ kubectl get pod ig-75f8f95bbf-hk9b7 -o json |grep  -A1 -i AM_URL

        "name": "AM_URL",
        "value": "\http://am/my-am"
   ```

### ForgeOps deployment monitoring

ForgeOps deployments optionally use Prometheus to monitor Ping Advanced Identity Software components and Kubernetes objects, Prometheus Alertmanager to send alert notifications, and Grafana to analyze metrics using dashboards.

This topic describes the use of monitoring tools in ForgeOps deployments:

[icon: eye, set=fas, size=3x]

#### [Overview](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/monitoring-intro.html)

Monitoring installation and architecture.

[icon: fedora, set=fab, size=3x]

#### [Monitoring Pods](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/pods.html)

Prometheus and Grafana pods that monitor ForgeOps deployments and provide reporting services.

[icon: tachometer-alt, set=fas, size=3x]

#### [Grafana Dashboards](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/dashboards.html)

Grafana dashboards for the platform that are available in ForgeOps deployments.

[icon: exclamation, set=fas, size=3x]

#### [Prometheus Alerts](https://docs.pingidentity.com/forgeops/2026.2/prepare/monitoring/alerts.html)

Prometheus alerts for the platform that are available in ForgeOps deployments.

#### About ForgeOps deployment monitoring

Prometheus, Alertmanager, and Grafana, used for monitoring ForgeOps deployments, are deployed if you run the prometheus-deploy.sh script after performing a ForgeOps deployment. This script installs Helm charts from the [prometheus-operator](https://github.com/coreos/prometheus-operator) project into the `monitoring` namespace of a ForgeOps deployment. The Prometheus operator project provides monitoring definitions for Kubernetes services and deployment, and management of Prometheus instances.

The Helm charts deploy [Kubernetes pods that run the Prometheus and Grafana services](prepare/monitoring/pods.html). The Prometheus operator then watches for service monitor CRDs—Kubernetes custom resource definitions. CRDs are Kubernetes class types that you manage with the kubectl command. The service monitor CRDs define targets to be scraped.

In ForgeOps deployments, the Prometheus operator configuration is defined in the [prometheus-operator.yaml](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/prometheus-operator.yaml) file in the `forgeops` repository. For information about how to customize Prometheus, Alertmanager, and Grafana, refer to the [Prometheus README file in the `forgeops` repository](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/README.md).

After a ForgeOps deployment is done, you can access the monitoring dashboards. For details, refer to [ForgeOps deployment monitoring](deploy/access.html#cdm-monitoring).

|   |                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Out-of-the-box ForgeOps deployments use Prometheus, Grafana, and Alertmanager for monitoring, reporting, and sending alerts. If you prefer to use different tools, deploy infrastructure in Kubernetes to support those tools.Prometheus and Grafana are evolving technologies. Descriptions of these technologies were accurate at the time of this writing, but might differ when you deploy them. |

#### Monitoring pods

The following Prometheus and Grafana pods from the `prometheus-operator` project run in the `monitoring` namespace:

| Pod                                                      | Description                                                                                                                                               |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alertmanager-prometheus-operator-kube-p-alertmanager-0` | Handles Prometheus alerts by grouping them together, filtering them, and then routing them to a receiver, such as a Slack channel.                        |
| `prometheus-operator-kube-state-metrics-...`             | Generates Prometheus metrics for cluster node resources, such as CPU, memory, and disk usage. One pod is deployed for each node in a ForgeOps deployment. |
| `prometheus-operator-prometheus-node-exporter-...`       | Generates Prometheus metrics for Kubernetes objects, such as deployments and nodes.                                                                       |
| `prometheus-operator-grafana-...`                        | Provides the Grafana service.                                                                                                                             |
| `prometheus-prometheus-operator-kube-p-prometheus-0`     | Provides the Prometheus service.                                                                                                                          |
| `prometheus-operator-kube-p-operator-...`                | Runs the Prometheus operator.                                                                                                                             |

See the [prometheus-operator Helm chart README file](https://github.com/helm/charts/blob/master/stable/prometheus-operator/README.md) for more information about the pods in the preceding table.

#### Custom Grafana dashboards

In addition to the pods from the `prometheus-operator` project, ForgeOps deployments include a set of Grafana dashboards. The `import-dashboards-...` pod from the `forgeops` repository runs after Grafana starts up. This pod imports Grafana dashboards for the Ping Advanced Identity Software and terminates after importing has completed.

You can customize, export and import Grafana dashboards using the Grafana UI or HTTP API.

For information about importing custom Grafana dashboards, refer to the [Import Custom Grafana Dashboards](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/README.md#import-custom-grafana-dashboards) section of the Prometheus and Grafana Deployment README file in the `forgeops` repository.

#### Alerts

Alerts for ForgeOps deployments are defined in the [fr-alerts.yaml](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/forgerock-metrics/templates/fr-alerts.yaml) file in the `forgeops` repository.

To configure additional alerts, refer to the [Configure Alerting Rules](https://github.com/ForgeRock/forgeops/blob/2026.2.1/cluster/addons/prometheus/README.md#Configure-alerting-rules) section of the Prometheus and Grafana Deployment README file in the `forgeops` repository.

### Security

This topic describes some security options in a ForgeOps deployment:

[icon: lock, set=fas, size=3x]

#### [Secure Communications](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/https.html)

Secure HTTP and certificate management.

[icon: id-card, set=fas, size=3x]

#### [IP Address Restriction](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/restrict-access-ip-address.html)

Access restriction by incoming IP address, enforced by the ingress controller.

[icon: network-wired, set=fas, size=3x]

#### [Network Policies](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/network-policies.html)

Secure cross-pod communications, enforced by Kubernetes network policies.

[icon: user-friends, set=fas, size=3x]

#### [Cluster Access on AWS](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/multi-user-access-aws.html)

User entries in the Amazon EKS authorization configuration map.

[icon: user-secret, set=fas, size=3x]

#### [Secret Agent](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/secret-agent.html)

Kubernetes operator that generates secrets and provides cloud secret management.

[icon: arrows-spin, set=fas, size=3x]

#### [Rotate Secrets](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/secrets-rotation.html)

Rotate secrets in a ForgeOps deployment.

[icon: shield-check, set=fas, size=3x]

#### [New security features](https://docs.pingidentity.com/forgeops/2026.2/prepare/security/sec-features.html)

New ForgeOps security features

#### Secure HTTP

ForgeOps deployments use a TLS-enabled ingress controller to enable secure communication to the cluster\[[17](#_footnotedef_17 "View footnote.")]. Incoming requests and outgoing responses are encrypted. TLS is terminated at the ingress controller.

By default, ForgeOps installs Traefik on AKS, EKS, and GKE clusters, and ingress-nginx on minikube\[[18](#_footnotedef_18 "View footnote.")]. The /path/to/forgeops/kustomize/base/ingress/ingress.yaml file contains an annotation—`cert-manager.io/cluster-issuer`—that configures the Traefik to use [cert-manager](https://github.com/jetstack/cert-manager) software for certificate management\[[19](#_footnotedef_19 "View footnote.")].

The forgeops apply command installs the `cert-manager` utility in the `cert-manager` namespace and configures `cert-manager` to generate self-signed certificates for securing communication into the ingress.

When self-signed certificates are used, communication is encrypted, but users receive warnings about insecure communication from some browsers. Because of this, self-signed certificates are suitable for test environments only.

For all other environments, reconfigure certificate management. Two common configurations are:

* Using a certificate with a trust chain that starts at a trusted root certificate—Communication is encrypted, and users do not receive warnings from their browsers.

  [TLS certificate](#tls-certificate) contains a simple example of how to deploy a certificate from a trusted authority in a ForgeOps deployment. The steps in the example:

  * Remove the cert-manager annotation from the ingress.

  * Create a secret named `tls-myfqdn` (for example:tls-forgeops.example.com) that contains the certificate you want to use in your deployment.

* Using a dynamically obtained certificate from [Let's Encrypt](https://letsencrypt.org/)—Communication is encrypted and users do not receive warnings from their browsers.

  You reconfigure cert-manager to use a ClusterIssuer that calls Let's Encrypt to obtain a certificate and installs the certificate as a Kubernetes secret.

There are many options for certificate management in a Ping Advanced Identity Software deployment. For more information about configuring certificate manager, refer to the [cert-manager documentation](https://cert-manager.io/docs).

##### TLS certificate

The forgeops apply command installs [cert-manager software](https://cert-manager.io/docs). Similarly, when using Helm, the default ForgeOps deployment requires `cert-manager` annotations.

When the `default-issuer` is used, the ingress controller in ForgeOps deployments is configured to use the self-signed certificate\[[20](#_footnotedef_20 "View footnote.")]. This is the simplest encryption option—you don't have to make any changes to your deployment to get encryption.

However, when you access one of the Ping Identity web applications from your browser, you'll get a "Not Secure" message from your browser. Users will need to bypass the message.

If you have a certificate from a CA, or a [certificate generated by the mkcert utility](#mkcert), you can use your certificate for TLS encryption instead of the default self-signed certificate:

1. Obtain the certificate:

   * Make sure that the certificate is PEM-encoded.

   * A best practice is to include the entire chain of trust with your certificate.

2. Make sure that the deployment FQDN (that you specified in your /etc/hosts file) works with your certificate. Refer to the hostname resolution page for your cluster provider: [Google Cloud](setup/google-cloud.html#gcp-ingress) | [AWS](setup/aws.html#aws-ingress) | [Azure](setup/azure.html#azure-ingress) | [minikube](setup/minikube.html#minikube-ingress).

3. Remove cert-manager's annotation from the ingress definition:

   1. If you are using Kustomize, run the kubectl annotate command:

      ```
      $ kubectl annotate ingress forgerock cert-manager.io/cluster-issuer-
      ```

   2. If you are using Helm, edit the charts/identity-platform/values.yaml file and set `cert_manager.enabled` to false:

      ```
      ...
      cert_manager:

          enabled: false
      ```

4. Delete the certificate resource originally created by cert-manager:

   ```
   $ kubectl delete certificate tls-myfqdn
   ```

5. Update your tls-myfqdn secret with your certificate. For example:

   ```
   $ kubectl create secret tls tls-myfqdn --cert=/path/to/my-cert.crt --key=/path/to/my-key.key \
     --dry-run=client -o yaml | kubectl replace -f -
   ```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | 1) If you have SSL certificate and do not want to use TLS certificates, then you can use your custom SSL certificate in your ForgeOps deployment environment:

   ```
   forgeops env --env-name my-env --ssl-secretname my-ssl-secret
   ```

2) If you disable `cert-manager` in the Helm chart, `cert-manager` is disabled for all certificates including the `ds-ssl-keypair` secret. You must create a custom version of that secret as well. |

##### Certificate generated by the mkcert utility

If you don't have a certificate from a CA, you can use the mkcert utility to generate a locally trusted certificate. In many cases, it's acceptable to use mkcert certificates for development purposes.

To use a certificate generated by the mkcert utility in a ForgeOps deployment that uses `my-fqdn` as the deployment FQDN:

1. If you don't have mkcert software installed locally, [install it](https://github.com/FiloSottile/mkcert#installation). Firefox users must install certutil software. Refer to the mkcert installation instructions for more information.

2. If you haven't ever done so, run the mkcert -install command to create a local certificate authority (CA) and install it in your system root store. Restart your browser after creating the local CA.

3. Create a wildcard certificate for the `example.com` domain:

   ```
   $ cd
   $ mkcert "*.example.com"
   ```

   The mkcert utility generates the certificate file as \_wildcard.example.com.pem and the private key file as \_wildcard.example.com-key.pem. Use these two file names when you create the Kubernetes TLS secret.

#### Access restriction by IP address

When installing the ingress controller in production environments, you should consider configuring a CIDR block in the Helm chart for the ingress controller so that you restrict access to worker nodes from a specific IP address or a range of IP addresses.

#### Network policies

Kubernetes [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies) let you specify specify how pods are allowed to communicate with other pods, namespaces, and IP addresses.

The `forgeops` repository contains two sets of example network policies for the Ping Advanced Identity Software:

1. [Network policies for DS](https://github.com/ForgeRock/forgeops/blob/2026.2.1/kustomize/base/security/ds-netpolicy.yaml).

2. [Network policies for AM and IDM](https://github.com/ForgeRock/forgeops/blob/2026.2.1/kustomize/base/security/app-netpolicy.yaml).

Customize the example policies to meet your security needs, or use them to help you better understand how network policies can make Kubernetes deployments more secure.

All the example policies have the value `Ingress` in the `spec.policyTypes` key:

```
spec:
  policyTypes:
  - Ingress
```

Network policies with this policy type are called *ingress policies*, because they limit ingress traffic in a deployment.

##### `deny-all` policy

By default, if no network policies exist in a namespace, then all ingress and egress traffic is allowed to and from pods in that namespace.

The `deny-all` policy modifies the default network policy for ingress. If a pod isn't selected by another network policy in the namespace, ingress is *not* allowed.

For information about how Kubernetes controls pod ingress when pods are selected by multiple network policies in a namespace, refer to [the Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/#isolated-and-non-isolated-pods).

##### `ds-idrepo-ldap` policy

The `ds-idrepo-ldap` policy limits access to `ds-idrepo` pods. Access can only be requested over port 1389, 1636, or 8080, and must come from an `am`, `idm`, or `amster` pod.

This part of the network policy specifies that access must be requested over port *1389*, *1636*, or *8080*:

```
ingress:
- from:
  ...
  ports:
  - protocol: TCP
    port: 1389
  - protocol: TCP
    port: 1636
  - protocol: TCP
    port: 8080
```

This part of the network policy specifies that access must be from an `am`, `idm`, or `amster` pod:

```
ingress:
- from:
  - podSelector:
      matchExpressions:
      - key: app
        operator: In
        values:
        - am
        - idm
        - amster
```

Understanding the example network policies and how to customize them requires some knowledge about labels defined in ForgeOps deployments. For example, `am` pods are defined with a label, `app`, that has the value `am`. You'll find this label in /path/to/forgeops/kustomize/base/am/kustomization.yaml file:

```
commonLabels:
  app.kubernetes.io/name: am
  app.kubernetes.io/instance: am
  app.kubernetes.io/component: am
  app.kubernetes.io/part-of: forgerock
  tier: middle
  app: am
```

##### `ds-cts-ldap` policy

The `ds-cts-ldap` policy limits access to `ds-cts` pods. Access can only be requested over port 1389, 1636, or 8080, and must come from an `am` or `amster` pod.

##### `ds-replication` policy

`ds` pods in ForgeOps deployments are labeled with `tier: ds`; they're said to reside in the `ds` tier of the deployment.

The `ds-replication` policy limits access to the pods on the `ds` tier. This policy specifies that access to `ds` tier pods over port 8989 can only come from other pods in the same tier.

Note that port 8989 is the default DS replication port. This network policy ensures that only DS pods can access the replication port.

##### `backend-http-access` policy

The `backend-http-access` policy limits access to the pods in the `middle` tier, which contains the `am`, `idm`, and `ig` pods. Access can only be requested over port 8080.

##### `front-end-http-access` policy

The `front-end-http-access` policy limits access to the pods in the `ui` tier: the `login-ui`, `admin-ui`, and `end-user-ui` pods. Access can only be requested over port 8080.

Note that users send HTTPS requests for the Ping Advanced Identity Software UIs to the ingress controller over port 443. The ingress controller terminates TLS, and then forwards requests to the UI pods over port 8080.

#### Cluster access for multiple AWS users

It's common for team members to share the use of a cluster. For team members to share a cluster, the cluster owner must grant access to each user:

1. Get the ARNs and names of users who need access to your cluster.

2. Set the Kubernetes context to your Amazon EKS cluster.

3. Edit the authorization configuration map for the cluster using the kubectl edit command:

   ```
   $ kubectl edit -n kube-system configmap/aws-auth
   ```

4. Under the `mapRoles` section, insert the `mapUser` section. An example is shown here with the following parameters:

   * The user ARN is `arn:aws:iam::012345678901:user/new.user`.

   * The user name registered in AWS is new\.user.

     ```
     ... mapUsers: |
         - userarn: arn:aws:iam::012345678901:user/new.user
           username: new.user
           groups:
             - system:masters
     ...
     ```

5. For each additional user, insert the `- userarn:` entry in the `mapUsers:` section:

   ```
   ... mapUsers: |
       - userarn: arn:aws:iam::012345678901:user/new.user
         username: new.user
         groups:
           - system:masters
       - userarn: arn:aws:iam::901234567890:user/second.user
         username: second.user
         groups:
           - system:masters
   ...
   ```

6. Save the configuration map.

#### Secret Agent operator

The open source Secret Agent operator generates all the secrets needed for ForgeOps deployments except for the DS master key and TLS key. When directory instances are created, certificate manager is called to generate these two keys.

In addition to generating secrets, the operator also integrates with Google Cloud Secret Manager, AWS Secrets Manager, and Azure Key Vault to manage secrets, providing cloud backup and retrieval for secrets.

The Secret Agent operator runs as a Kubernetes deployment that must be available before you can install AM, IDM, and DS.

##### Secret generation

By default, the operator examines your namespace to determine whether it contains all the secrets that it manages for Ping Advanced Identity Software deployments. If any of the secrets it manages are not present, the operator generates them.

Refer to the Secret Agent project README for information about:

* [Importing your own secrets](https://github.com/ForgeRock/secret-agent#importing-your-own-secrets)

* [Secret Agent naming conventions](https://github.com/ForgeRock/secret-agent#naming-convention-for-cloud-backups)

* [Modifying the Secret Agent configuration](https://github.com/ForgeRock/secret-agent#secret-agent-configuration-schema)

##### Cloud secret management

Configuring the Secret Agent operator to integrate with a cloud secret manager, such as Google Cloud Secret Manager, AWS Secret Manager, or Azure Key Vault, changes the operator's behavior:

* First, the operator examines your namespace to determine whether it contains all the secrets it manages for Ping Advanced Identity Software deployments.

* If any of the secrets it manages are not in your namespace, the operator checks to refer to if the missing secrets are available in the cloud secret manager:

  * If any of the secrets missing from your namespace are available in the cloud secret manager, the operator gets them from the cloud secret manager and adds them to your namespace.

  * If missing secrets are not available in the cloud secret manager, the Secret Agent operator generates them.

Configure cloud secret management when you have multiple Ping Advanced Identity Software deployments that need to use the same secrets.

Refer to the Secret Agent project README for information about how to configure the Secret Agent operator for cloud secret management using these cloud secret managers:

* [Google Cloud Secret Manager](https://github.com/ForgeRock/secret-agent#set-up-cloud-backup-with-gcp-secret-manager)

* [AWS Secret Manager](https://github.com/ForgeRock/secret-agent#set-up-cloud-backup-with-aws-secret-manager)

* [Azure Key Vault](https://github.com/ForgeRock/secret-agent#set-up-cloud-backup-with-azure-key-vault)

##### Administration password changes

ForgeOps deployments use these administration passwords:

* The AM and IDM administration user, `amadmin`

* The AM application store service account, `uid=am-config,ou=admins,ou=am-config`

* The AM CTS service account, `uid=openam_cts,ou=admins,ou=famrecords,ou=openam-session,ou=tokens`

* The shared identity repository service account, `uid=am-identity-bind-account,ou=admins,ou=identities`

* The DS root user, `uid=admin`

Some organizations have a requirement to change administration passwords from time to time. Follow these steps if you need to change the administration passwords:

1. Set the value of the `secretsManagerPrefix` key to `prod` in your [Secret Agent configuration](https://github.com/ForgeRock/secret-agent#naming-convention-for-cloud-backups).

   You can set the value of the `secretsManagerPrefix` key to any prefix you like. These steps use `prod` as an example prefix.

2. Change the `amadmin` user's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the `amadmin` user.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains the `amadmin` user's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `AM-PASSWORDS-AMADMIN-CLEAR` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-am-env-secrets-AM-PASSWORDS-AMADMIN-CLEAR
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `AM-PASSWORDS-AMADMIN-CLEAR` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-am-env-secrets-AM-PASSWORDS-AMADMIN-CLEAR-c3KfsL
      > ```

      > **Collapse: Azure**
      >
      > Soft delete the secret that contains the `AM-PASSWORDS-AMADMIN-CLEAR` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-am-env-secrets-AM-PASSWORDS-AMADMIN-CLEAR
      > ```
      >
      > Purge the soft deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-am-env-secrets-AM-PASSWORDS-AMADMIN-CLEAR
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the `amadmin` user's password from the namespace in which the platform is deployed:

      ```
      $ kubectl patch secrets am-env-secrets --type=json \
       --patch='[{"op":"remove", "path": "/data/AM_PASSWORDS_AMADMIN_CLEAR"}]'
      ```

   6. Restart AM by deleting all active AM pods: list all the pods in the namespace where you deployed the platform and then delete all the pods running AM.

   7. After AM comes up, run the forgeops info command again to get the current administration passwords.

      Verify that the `amadmin` user's password has changed by comparing its previous value to its current value.

   8. Verify that you can log in to the platform UI using the new password.

3. Change the AM application store service account's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the AM application store service account.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains this account's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `AM_STORES_APPLICATION_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-ds-env-secrets-AM_STORES_APPLICATION_PASSWORD
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `AM_STORES_APPLICATION_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-ds-env-secrets-AM_STORES_APPLICATION_PASSWORD-1d4432
      > ```

      > **Collapse: Azure**
      >
      > Soft delete the secret that contains the `AM_STORES_APPLICATION_PASSWORD` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_APPLICATION_PASSWORD
      > ```
      >
      > Purge the deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_APPLICATION_PASSWORD
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the service account's password from the namespace where the platform is deployed:

      ```
      $ kubectl patch secrets ds-env-secrets --type=json \
       --patch='[{"op":"remove", "path": "/data/AM_STORES_APPLICATION_PASSWORD"}]'
      ```

   6. Remove your ForgeOps deployment. Be sure to reply `N` when you're prompted to delete PVCs, volume snapshots, and secrets:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops delete
      "small" platform detected in namespace: "my-namespace".
      Uninstalling component(s): ['all'] from namespace: "my-namespace".
      OK to delete components? [Y/N] Y
      OK to delete PVCs? [Y/N] N
      OK to delete volume snapshots? [Y/N] N
      OK to delete secrets? [Y/N] N
      service "admin-ui" deleted
      ...
      ```

   7. Redeploy the platform:

      ```
      $ forgeops apply --small --fqdn my-fqdn
      ```

   8. Review the administration passwords listed in the forgeops install command's' output.

      Verify that the AM application store service account's password has changed by comparing its previous value to its current value.

4. Change the CTS service account's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the identity repository service account.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains this account's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `AM_STORES_CTS_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-ds-env-secrets-AM_STORES_CTS_PASSWORD
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `AM_STORES_CTS_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-ds-env-secrets-AM_STORES_CTS_PASSWORD-1d4432
      > ```

      > **Collapse: Azure**
      >
      > Delete the secret that contains the `AM_STORES_CTS_PASSWORD` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_CTS_PASSWORD
      > ```
      >
      > Purge the deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_CTS_PASSWORD
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the service account's password from the namespace where the platform is deployed:

      ```
      $ kubectl patch secrets ds-env-secrets --type=json \
       --patch='[{"op":"remove", "path": "/data/AM_STORES_CTS_PASSWORD"}]'
      ```

   6. Remove your ForgeOps deployment. Be sure to reply `N` when you're prompted to delete PVCs, volume snapshots, and secrets:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops delete
      "small" platform detected in namespace: "my-namespace".
      Uninstalling component(s): ['all'] from namespace: "my-namespace".
      OK to delete components? [Y/N] Y
      OK to delete PVCs? [Y/N] N
      OK to delete volume snapshots? [Y/N] N
      OK to delete secrets? [Y/N] N
      service "admin-ui" deleted
      ...
      ```

   7. Redeploy the platform:

      ```
      $ forgeops apply --small --fqdn my-fqdn
      ```

   8. Review the administration passwords listed in the forgeops install command's' output.

      Verify that the CTS service account's password has changed by comparing its previous value to its current value.

5. Change the identity repository service account's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the identity repository service account.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains this account's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `AM_STORES_USER_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-ds-env-secrets-AM_STORES_USER_PASSWORD
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `AM_STORES_USER_PASSWORD` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-ds-env-secrets-AM_STORES_USER_PASSWORD-1d4432
      > ```

      > **Collapse: Azure**
      >
      > Soft delete the secret that contains the `AM_STORES_USER_PASSWORD` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_USER_PASSWORD
      > ```
      >
      > Purge the deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-ds-env-secrets-AM_STORES_USER_PASSWORD
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the service account's password from the namespace where the platform is deployed:

      ```
      $ kubectl patch secrets ds-env-secrets --type=json \
       --patch='[{"op":"remove", "path": "/data/AM_STORES_USER_PASSWORD"}]'
      ```

   6. Remove your ForgeOps deployment. Be sure to reply `N` when you're prompted to delete PVCs, volume snapshots, and secrets:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops delete
      "small" platform detected in namespace: "my-namespace".
      Uninstalling component(s): ['all'] from namespace: "my-namespace".
      OK to delete components? [Y/N] Y
      OK to delete PVCs? [Y/N] N
      OK to delete volume snapshots? [Y/N] N
      OK to delete secrets? [Y/N] N
      service "admin-ui" deleted
      ...
      ```

   7. Redeploy the platform:

      ```
      $ forgeops apply --small --fqdn my-fqdn
      ```

   8. Review the administration passwords listed in the forgeops install command's' output.

      Verify that the identity repository service account's password has changed by comparing its previous value to its current value.

6. Change the DS root user's password:

   1. Change to the bin directory in your `forgeops` repository clone.

   2. Run the forgeops info command. Note the current password for the `uid=admin` account.

   3. If you've enabled [cloud secret management](#cloud-secret-management), delete the entry that contains this account's password from the cloud secret manager:

      > **Collapse: Google Cloud**
      >
      > List the secrets managed by the cloud secret manager, locate the URI for the secret that contains the `dirmanager-pw` password, and delete it. For example:
      >
      > ```
      > $ gcloud secrets list --uri
      > $ gcloud secrets delete \
      >  https://secretmanager.googleapis.com/.../prod-ds-passwords-dirmanager-pw
      > ```

      > **Collapse: AWS**
      >
      > List the secrets managed by the cloud secret manager, locate the ARN for the secret that contains the `dirmanager-pw` password, and delete it. For example:
      >
      > ```
      > $ aws secretsmanager list-secrets --region=my-region
      > $ aws secretsmanager delete-secret --region=my-region \
      >  --force-delete-without-recovery \
      >  --secret-id arn:aws:secretsmanager:...:prod-ds-passwords-dirmanager-pw-2eeaa0
      > ```

      > **Collapse: Azure**
      >
      > Soft delete the secret that contains the `dirmanager-pw` password from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret delete --vault-name my-key-vault --name prod-ds-passwords-dirmanager-pw
      > ```
      >
      > Purge the deleted secret from Azure Key Vault. For example:
      >
      > ```
      > $ az keyvault secret purge --vault-name my-key-vault --name prod-ds-passwords-dirmanager-pw
      > ```

   4. Make the namespace where the platform is deployed the active namespace in your local Kubernetes context.

   5. Delete the Kubernetes secret that contains the service account's password from the namespace where the platform is deployed:

      ```
      $ kubectl patch secrets ds-passwords --type=json \
       --patch='[{"op":"remove", "path": "/data/dirmanager.pw"}]'
      ```

   6. Remove your ForgeOps deployment. Be sure to reply `N` when you're prompted to delete PVCs, volume snapshots, and secrets:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops delete
      "small" platform detected in namespace: "my-namespace".
      Uninstalling component(s): ['all'] from namespace: "my-namespace".
      OK to delete components? [Y/N] Y
      OK to delete PVCs? [Y/N] N
      OK to delete volume snapshots? [Y/N] N
      OK to delete secrets? [Y/N] N
      service "admin-ui" deleted
      ...
      ```

   7. Redeploy the platform:

      ```
      $ forgeops apply --small --fqdn my-fqdn
      ```

   8. Review the administration passwords listed in the forgeops install command's' output.

      Verify that the password for the `uid=admin` account has changed by comparing its previous value to its current value.

#### Secrets Rotation

##### Introduction

Secrets rotation is the process of updating or replacing sensitive information stored as Kubernetes secrets. Secrets rotation is crucial for maintaining strong security and mitigating risks of unauthorized access or data breaches.

In a multi-component system, such as a ForgeOps deployment, each component interacts with others using secrets. Therefore, it's important to consider dependencies among components and perform secrets rotation while maintaining consistent interaction among dependent components.

The forgeops command includes the rotate sub-command to enable `ds-env-secrets` and `ds-passwords` rotation consistently. You can rotate other ForgeOps required secrets also with due consideration to the impact on dependent components and downtime.

##### Performing secrets and passwords rotation

This section describes how to rotate secrets and password in ForgeOps deployments. The steps for rotating each secret are mentioned separately for easier understanding and usage.

###### Rotating `ds-env-secrets`

The `ds-env-secrets` controls access to DS from AM and IDM, and would normally cause a downtime when rotated. To avoid such a downtime, the forgeops rotate command creates old-ds-env-secrets temporarily to contain old secrets.

In ForgeOps release 2025.2.1, the DS image was built to accommodate multiple passwords. This enables secrets rotation with no downtime.

* For deployments using DS images from 2025.1 or earlier

  If you are using the DS image from the 2025.1 release or earlier, then perform these steps to enable multiple passwords in DS.

  1. In your terminal window, set up environment variables to get the password and connection string (DSPASS and CONN\_STR):

     ```
     $ export DSPASS=$(kubectl get secret ds-passwords -n my_ns -o yaml | yq '.data["dirmanager.pw"]' | tr -d '"' | base64 -d -i -)

     $ export CONN_STR="--hostname localhost --port 4444 --bindDn uid=admin --trustAll --no-prompt --bindPassword $DSPASS"
     ```

  2. Set up DS pods to enable multiple passwords:

     ```
     $ kubectl exec -it ds-cts-0 — bin/dsconfig set-password-policy-prop \
       set-password-policy-prop --policy-name "Default Password Policy" \
       --set allow-multiple-password-values:true $CONN_STR

     $ kubectl exec -it ds-cts-0 — bin/dsconfig set-password-policy-prop \
       set-password-policy-prop --policy-name "Root Password Policy" \
       --set allow-multiple-password-values:true $CONN_STR

     $ kubectl exec -it ds-idrepo-0 — bin/dsconfig set-password-policy-prop \
       set-password-policy-prop --policy-name "Default Password Policy" \
       --set allow-multiple-password-values:true $CONN_STR

     $ kubectl exec -it ds-idrepo-0 — bin/dsconfig set-password-policy-prop \
       set-password-policy-prop --policy-name "Root Password Policy" \
       --set allow-multiple-password-values:true $CONN_STR
     ```

To rotate `ds-env-secrets`, run the forgeops rotate --namespace my\_ns ds-env-secrets command.

The command prompts you to perform steps to complete rotation of `ds-env-secrets`.

###### Rotating `ds-passwords`

To rotate `ds-passwords`, run the forgeops rotate --namespace my\_ns ds-passwords command. The command prompts you to perform steps to complete rotation of `ds-passwords`.

You must restart the DS pods to update the `admin` user password because that password is set on DS pod startup. This could also require restarting some services instead of redeploying components.

At the end of its successful run, the forgeops rotate command prompts the user to:

* Delete the temporary secrets.

* Remove the old passwords.

###### Rotating `amster` secret

* Impact

  This secret is specific to Amster and doesn't cause a downtime.

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret amster
     ```

  2. Rolling restart AM pods to pick up new `amster` secret:

     ```
     $ kubectl rollout restart deployment am -n my-ns
     ```

  3. Refresh amster job to verify `amster` can access AM:

     1. Delete amster job to allow redeployment:

        ```
        $ kubectl delete job amster -n my-ns
        ```

     2. Deploy platform changes (`amster`)

        1. For Helm:

           ```
           $ helm upgrade -i identity-platform --repo https://ForgeRock.github.io/forgeops/ \
            --version my-prod-version \
            --values /path/to/forgeops/helm/my-env/values.yaml
           ```

        2. For Kustomize:

           ```
           $ forgeops apply amster --env-name my-env
           ```

  4. Ensure that the `amster import` process has completed successfully:

     ```
     $ kubectl logs -f amster-pod -n my-ns
     ```

###### Rotating `am-env-secrets`

* Impact

  AM depends on this secret for authentication. Therefore, during the short time between restarting AM and rerunning Amster, requests that need authentication could fail.

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret am-env-secrets
     ```

  2. Rolling restart AM pods to pick up new amster secret:

     ```
     $ kubectl rollout restart deployment am -n my-ns
     ```

  3. Reinitiate the amster job:

     1. Delete the amster job to allow redeployment:

        ```
        $ kubectl delete job amster -n my-ns
        ```

     2. Redeploy `amster`:

        1. For Helm:

           ```
           $ helm upgrade -i identity-platform --repo https://ForgeRock.github.io/forgeops/ \
             --values /path/to/forgeops/helm/my-env/values.yaml
           ```

        2. For Kustomize:

           ```
           $ forgeops apply amster --env-name my-env
           ```

  4. Ensure that the amster import process has completed successfully:

     ```
     $ kubectl logs -f amster-pod -n my-ns
     ```

  5. Retrieve the new password for `amadmin` user to log in to the platform:

     ```
     $ forgeops info | grep amadmin
     ```

  6. Log in to the platform with new `amadmin` password to verify the platform is up and running.

###### Rotating `amster-env-secrets`

* Impact

  In the very short time between restarting IDM and Amster importing necessary data, the platform isn't accessible. Amster takes a few seconds to import data.

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret amster-env-secrets
     ```

  2. Rolling restart IDM pods to get the new amster secret:

     ```
     $ kubectl rollout restart deployment idm -n my-ns
     ```

  3. Rerun the `amster` job to import the new secrets:

     1. Delete the `amster` job to allow redeployment:

        ```
        $ kubectl delete job amster -n my-ns
        ```

     2. Redeploy Amster:

        1. When using Helm to deploy:

           ```
           $ helm upgrade -i identity-platform --repo https://ForgeRock.github.io/forgeops/ --values /path/to/custom/values.yaml
           ```

        2. When using Kustomize deploy:

           ```
           $ forgeops apply --env-name my-env amster
           ```

###### Rotating idm-env-secrets

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret idm-env-secrets
     ```

  2. Rolling restart IDM pods:

     ```
     $ kubectl rollout restart deployment idm
     ```

  3. Check pods have come up:

     ```
     $ kubectl get pods -l app.kubernetes.io/component=idm -n my-ns
     ```

###### Rotating `ds-ssl-keypair`

|   |                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------- |
|   | It's not advisable to rotate this secret. If you rotate this secret DS data replication will fail until all the DS pods are restarted. |

* Procedure

  1. Delete the `ds-ssl-keypair` secret:

     ```
     $ kubectl delete secret ds-ssl-keypair -n my-ns
     ```

  2. Check that the secret is recreated:

     ```
     $ kubectl get secret ds-ssl-keypair -n my-ns
     ```

  3. Rolling restart `ds-cts` pods to pick up new secret:

     ```
     $ kubectl rollout restart sts ds-cts -n my-ns
     ```

  4. Rolling restart `ds-idrepo` pods to pick up new secret:

     ```
     $ kubectl rollout restart sts ds-idrepo -n my-ns
     ```

  5. Rolling restart AM pods to pick up new secret:

     ```
     $ kubectl rollout restart deployment am -n my-ns
     ```

  6. Rolling restart IDM pods to pick up new secret:

     ```
     $ kubectl rollout restart deployment idm -n my-ns
     ```

  7. Check pods to ensure they have come back up:

     ```
     $ kubectl get pods -l app.kubernetes.io/component=ds-cts -n my-ns
     $ kubectl get pods -l app.kubernetes.io/component=ds-idrepo -n my-ns
     $ kubectl get pods -l app.kubernetes.io/component=am -n my-ns
     $ kubectl get pods -l app.kubernetes.io/component=idm -n my-ns
     ```

###### Rotating `am-passwords`

* Impact

  Rotating `am-passwords` doesn't necessitate a down-time. `am-passwords` is used only in ForgeOps deployments that use `secret agent` for secrets management. It's not relevant for deployments that use `secrets generator`.

* Procedure

  1. Trigger renewal of Kubernetes secret:

     ```
     $ kubectl delete secret am-passwords
     $ kubectl delete secret am-keystore
     ```

  2. Delete the AM pod:

     ```
     $ kubectl delete pod am-wxyz-abcd
     ```

  3. Recreate keystore to use the new secret.

###### Rotating `ds-master-keypair`

|   |                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Do not rotate `ds-master-keypair` because it's used in DS data backups**. The same secret is required to decrypt data when you need to restore from backups. If you must rotate these secrets, then restart backups and discard the previous backups because they can't be used for restoring directory data. |

###### Adding custom certificate to the truststore

The following environment variables are used to point to the paths for certificates. You don't need to update any of it.

* **AM\_DEFAULT\_TRUSTSTORE**: PingAM and PingIDM now use the default Java ca certificate as the default truststore.

* **AM\_PEM\_TRUSTSTORE**: Custom user-supplied certificates to append to the truststore.

* **AM\_PEM\_TRUSTSTORE\_DS**: The DS SSL key pair used for LDAPS connectivity between PingAM and PingDS.

The following procedure helps in adding user supplied certificates to the truststore for PingAM and PingIDM. **Certificates should be in pem format.**

* In a Helm based deployment

  * (Option 1) Provide the certificate using a manually created secret. This is the preferred option.

    1. Set `platform.truststore.secret.enabled` to "true".

    2. Ensure `truststore.secret.create` is set to "false".

    3. Create a Kubernetes secret containing certificate:

       ```
       $ kubectl --namespace my-namespace create secret generic \
        platform-truststore-certificates --from-file=/path/to/my-certificates
       ```

  * (Option 2) Provide certificate content in `values.yaml`. This option is useful for testing purposes or if you only have a single certificate.

    1. Set `platform.truststore.secret.enabled` to "true".

    2. Set `platform.truststore.secret.create` to "true".

    3. Add the content of the certificate to `platform.truststore.secret.certificates`.

* In a Kustomize based deployment

  1. Create a Kubernetes secret containing the certificate:

     ```
     $ kubectl --namespace my-namespace create secret generic \
       platform-truststore-certificates --from-file=/path/to/my-certificates
     ```

* Add an existing secret containing custom certificates to the truststore

  1. (Option 1) Recreate your current secret with the name `platform-truststore-certificates` to match the previous steps.

  2. (Option 2) In the overlay file of your environment, update the mount points where `platform-truststore-certificates` is configured with the name of your custom secret.

#### New security features

New security features in ForgeOps 2026.2.

## Backup and restore overview

[ForgeOps deployments](deploy/architecture.html#cdm-topology) include two directory services:

* The `ds-idrepo` service, which stores identities, application data, and AM policies

* The `ds-cts` service, which stores AM Core Token Service data

Before deploying the Ping Advanced Identity Software in production, create and test a backup plan that lets you recover these two directory services should you experience data loss.

### Choose a backup solution

There are numerous options to implement data backup. ForgeOps deployments provide two solutions:

* Kubernetes [volume snapshots](backup/snapshots.html)

* [The dsbackup utility](backup/dsbackup.html)

You can also use backup products from third-party vendors. For example:

* Backup tooling from your cloud provider. For example, [Google backup for GKE](https://cloud.google.com/blog/products/storage-data-transfer/google-cloud-launches-backups-for-gke).

* Third-party utilities, such as Velero, Kasten K10, TrilioVault, Commvault, and Portworx Backup. These third-party products are cloud-platform agnostic, and can be used across cloud platforms.

Your organization might have specific needs for its backup solution. Some factors to consider include:

* Does your organization already have a backup strategy for Kubernetes deployments? If it does, you might want to use the same backup strategy for your Ping Advanced Identity Software deployment.

* Do you plan to deploy the platform in a hybrid architecture, where part of your deployment is on-premises and another part of it is in the cloud? If you do, then you might want to employ a backup strategy that lets you move around DS data most easily.

* When considering how to store your backup data, is cost or convenience more important to you? If cost is more important, then you might need to take into account that archival storage in the cloud is much less expensive than snapshot storage—ten times less expensive, as of this writing.

* If you're thinking about using snapshots for backup, are there any limitations imposed by your cloud provider that are unacceptable to you? Historically, cloud providers have placed quotas on snapshots. Check your cloud provider's documentation for more information.

### Backup and restore using volume snapshots

Kubernetes [volume snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots) provide a standardized way to create copies of persistent volumes at a point in time without creating new volumes. Backing up your directory data with volume snapshots lets you perform rapid recovery from the last snapshot point. Volume snapshot backups also facilitate testing by letting you initialize DS with sample data.

In ForgeOps deployments, the DS data, changelog, and configuration are stored in the same persistent volume. This ensures the volume snapshot captures DS data and changelog together.

#### Backup

##### Set up backup

Kustomize overlays and Helm values necessary for configuring volume snapshots are already provided, but they have not been enabled to take backup. The default volume snapshot setup takes snapshots of the `data-ds-idrepo-0` and `data-ds-cts-0` PVCs once a day.

* Enable volume snapshot before deployment

  You can enable volume snapshot when you set up an environment before performing a ForgeOps deployment. For example, to enable snapshot for both `idrepo` and `cts`:

  ```
  $ cd /path/to/forgeops/bin
  $ ./forgeops env --env-name  my-env --fqdn my-fqdn \
    --namespace my-namespace --cluster-issuer my_issuer \
    --idrepo-snap-enable --cts-snap-enable
  ```

* Enable volume snapshot in a ForgeOps deployment

  To enable volume snapshots of DS data where ForgeOps has been deployed in my-namespace namespace:

  1. Revise the environment to enable snapshot:

     ```
     $ cd /path/to/forgeops/bin
     $ ./forgeops env --env-name  my-env --idrepo-snap-enable --cts-snap-enable
     ```

     |   |                                                                                                                   |
     | - | ----------------------------------------------------------------------------------------------------------------- |
     |   | If you want to enable snapshot for `idrepo` alone, don't specify `--cts-snap-enable` in the forgeops env command. |

  2. Apply the changes to your ForgeOps deployment:

     1. In a Kustomize-based deployment:

        ```
        $ cd /path/to/forgeops/bin
        $ ./forgeops apply --env-name  my-env
        ```

     2. In a Helm-based deployment:

        ```
        $ cd /path/to/forgeops/charts/identity-platform
        $ helm upgrade --install identity-platform ./ \
         --namespace my-namespace --values /path/to/forgeops/helm/my-env/values.yaml
        ```

You can view the volume snapshots that are available for restore, using this command:

```
$ kubectl get volumesnapshots --namespace my-namespace

NAME                               READYTOUSE   SOURCEPVC          SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS       SNAPSHOTCONTENT
          CREATIONTIME   AGE
ds-idrepo-snapshot-20231117-1320   true         data-ds-idrepo-0                           100Gi         ds-snapshot-class   snapcontent-be3f4a44-cfb2-4f68-aa2b-60902
bb44192   3h29m          3h29m
ds-idrepo-snapshot-20231117-1330   true         data-ds-idrepo-0                           100Gi         ds-snapshot-class   snapcontent-7bcf6779-382d-40e3-9c9f-edf31
c54768e   3h19m          3h19m
ds-idrepo-snapshot-20231117-1340   true         data-ds-idrepo-0                           100Gi         ds-snapshot-class   snapcontent-c9c88332-ad05-4880-bda7-48616
ec13579   3h9m           3h9m
ds-idrepo-snapshot-20231117-1401   true         data-ds-idrepo-0                           100Gi         ds-snapshot-class   snapcontent-1f3f4ce9-0083-447f-9803-f6b45
e03ac27   167m           167m
ds-idrepo-snapshot-20231117-1412   true         data-ds-idrepo-0                           100Gi         ds-snapshot-class   snapcontent-4c39c095-0891-4da8-ae61-fac78
c7147ff   156m           156m
```

##### Customize the backup schedule

When enabled, volume snapshots are created once every day by default and purged after three days. You can customize the backup schedules as required in your environment.

* In a Kustomize-based deployment

* In a Helm-based deployment

To modify the default schedule and purge delay for the `idrepo` repository\[[21](#_footnotedef_21 "View footnote.")]:

1. In a terminal window, change to the path/to/idrepo directory.

2. Copy the schedule.yaml file to a temporary location, so you can restore if needed.

3. Edit the schedule.yaml file and set the `schedule` and `purge-delay` parameters as needed.

4. Run the kubectl apply command.

   * Examples for scheduling snapshots

     * To schedule snapshots twice a day, at noon and midnight:

       ```
       ...
         spec:
           schedule: "0 0/12 * * *"
       ...
       ```

     * To schedule snapshots every 8 hours:

       ```
       ...
         spec:
           schedule: "0 */8 * * *"
       ...
       ```

   * Examples for purging schedule

     * To schedule purge after 4 days:

       ```
       ...
                env:
                  - name: PURGE_DELAY
                    value: "-4 day"
       ```

     * To schedule purge after a week:

       ```
       ...
                env:
                  - name: PURGE_DELAY
                    value: "-7 day"
       ```

To modify the default schedule and purge delay:

1. In a terminal window, change to the /path/to/forgeops/helm/my-env directory:

   ```
   $ cd /path/to/forgeops/helm/my-env
   ```

2. Copy the values.yaml file, so you can restore it if required:

   ```
   $ cp values.yaml /tmp/values.yaml
   ```

3. Edit the values.yaml file and set the `schedule` and `purge-delay` parameters as needed.

4. Run the helm upgrade command.

   * Examples for scheduling snapshots for the `idrepo` repository\[[22](#_footnotedef_22 "View footnote.")]

     * To schedule snapshots twice a day, at noon and midnight:

       ```
       ...
       ds-idrepo:
         ...
         snapshot:
            ...
            schedule: "0 0/12 * * *"
       ...
       ```

     * To schedule snapshots every 8 hours:

       ```
       ...
       ds-idrepo:
         ...
         snapshot:
            ...
            schedule: "0 */8 * * *"
       ...
       ```

   * Examples for purging schedule for the `idrepo` repository\[[22](#_footnotedef_22 "View footnote.")]

     * To schedule purge after 4 days:

       ```
       ...
       ds-idrepo:
         ...
         snapshot:
            ...
            purgeDelay: "-4 day"
       ...
       ```

     * To schedule purge after a week:

       ```
       ...
       ds-idrepo:
         ...
         snapshot:
            ...
            purgeDelay: "-7 day"
       ...
       ```

#### Restore from volume snapshot

The snapshot-restore.sh script lets you restore DS instances in a ForgeOps deployment. By default, this script restores a DS instance from the latest available snapshot.

There are two options when using the snapshot-restore.sh script to restore a DS from a volume snapshot:

* Full—Use the full option to fully restore a DS instance from a volume snapshot. When you specify this option, the DS is scaled down to 0 pods before restoring data. The data is restored to an existing PVC from a snapshot. This operation requires downtime.

* Selective—Use the selective option to restore a portion of DS data from volume snapshot. The selective restore creates a new temporary DS instance with a new DS pod. You can selectively export from the temporary DS pod and import into your functional DS instance. After restoring data, you can clean up the temporary resources.

The snapshot-restore.sh command is available in the `bin` directory of the `forgeops` repository. To learn more about the snapshot-restore.sh command and its options, run snapshot-restore.sh --help.

##### Restore examples

* Trial run without actually restoring DS data

  1. In a terminal window, change to the /path/to/forgeops/bin directory.

  2. Set your Kubernetes context to the correct cluster and namespace.

  3. Run the snapshot-restore.sh command with the `--dryrun` option:

     ```
     $ ./snapshot-restore.sh --dryrun --namespace my-namespace full idrepo

     ./snapshot-restore.sh --dryrun --namespace my-namespace full idrepo
     /usr/local/bin/kubectl apply -f /tmp/snapshot-restore-idrepo.20231121T23:03:15Z/sts-restore.json -n my-namespace
     /usr/local/bin/kubectl delete pvc data-ds-idrepo-0 -n my-namespace
     /usr/local/bin/kubectl apply -f /tmp/snapshot-restore-idrepo.20231121T23:03:15Z/data-ds-idrepo-0.json -n my-namespace
     /usr/local/bin/kubectl apply -f /tmp/snapshot-restore-idrepo.20231121T23:03:15Z/sts.json -n my-namespace
     ```

* Full restore of the `idrepo` instance from the latest available volume snapshot

  1. In a terminal window, change to the /path/to/forgeops/bin directory.

  2. Set your Kubernetes context to the correct cluster and namespace.

  3. Get a list of available volume snapshots:

     ```
     $ kubectl get volumesnapshots --namespace my-namespace
     ```

  4. Restore the full DS instance:

     ```
     $ ./snapshot-restore.sh --namespace my-namespace full idrepo
     ```

  5. Verify that DS data has been restored.

* Selective restore from a specific volume snapshot and storing data in a user-defined storage path

  1. In a terminal window, change to the /path/to/forgeops/bin directory.

  2. Set your Kubernetes context to the correct cluster and namespace.

  3. Get a list of available volume snapshots:

     ```
     $ kubectl get volumesnapshots --namespace my-namespace
     ```

  4. Perform a selective restore trial run:

     ```
     $ ./snapshot-restore.sh --dryrun --path /tmp/ds-restore --snapshot ds-idrepo-snapshot-20231121-2250 --namespace my-namespace selective idrepo

     VolumeSnapshot ds-idrepo-snapshot-20231121-2250 is ready to use
     /usr/local/bin/kubectl apply -f /tmp/ds-rest/sts-restore.json -n my-namespace
     /usr/local/bin/kubectl apply -f /tmp/ds-rest/svc.json -n my-namespace
     ```

  5. Perform a selective restore using a specific snapshot:

     ```
     $ ./snapshot-restore.sh --path /tmp/ds-restore --snapshot ds-idrepo-snapshot-20231121-2250 --namespace my-namespace selective idrepo

     statefulset.apps/ds-idrepo-restore created
     service/ds-idrepo configured
     ```

  6. Verify that a new `ds-idrepo-restore-0` pod was created:

     ```
     $ kubectl get pods
     NAME                          READY   STATUS      RESTARTS   AGE
     admin-ui-656db67f54-2brbf     1/1     Running     0          3h17m
     am-7fffff59fd-mkks5           1/1     Running     0          107m
     amster-hgkv9                  0/1     Completed   0          3h18m
     ds-idrepo-0                   1/1     Running     0          39m
     ds-idrepo-restore-0           1/1     Running     0          2m40s
     end-user-ui-df49f79d4-n4q54   1/1     Running     0          3h17m
     idm-fc88578bf-lqcdj           1/1     Running     0          3h18m
     login-ui-5945d48fc6-ljxw2     1/1     Running     0          3h17m
     ```

     |   |                                                                                                                                                                                                 |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The `ds-idrepo-restore-0` pod is temporary and not to be used as a complete DS instance. You can export required data from the temporary pod, and import data into your functional DS instance. |

  7. Clean up resources from the selective restore:

     ```
     $ ./snapshot-restore.sh clean idrepo

     statefulset.apps "ds-idrepo-restore" deleted
     persistentvolumeclaim "data-ds-idrepo-restore-0" deleted
     ```

### dsbackup utility

This page provides instructions for backing up and restoring DS data in a ForgeOps deployment using the dsbackup utility.

#### Back up using the dsbackup utility

Before you can back up DS data using the dsbackup utility, you must [set up a cloud storage container](#setup-cloud-storage) in Google Cloud Storage, Amazon S3, or Azure Blob Storage and configure a Kubernetes secret with the container's credentials in your ForgeOps deployment. Then, you [schedule backups](#schedule-backups) by running the ds-backup.sh script.

##### Set up cloud storage

Cloud storage setup varies depending on your cloud provider. Expand one of the following sections for provider-specific setup instructions:

> **Collapse: Google Cloud**
>
> Set up a Google Cloud Storage (GCS) bucket for the DS data backup and configure the ForgeOps deployment with the credentials for the bucket:
>
> 1. Create a Google Cloud service account with required privileges to write objects in a GCS bucket. For example, Storage Object Creator.
>
> 2. Add a key to the service account, and then download the JSON file containing the new key.
>
> 3. Configure a multi-region GCS bucket for storing DS backups:
>
>    1. Create a new bucket, or identify an existing bucket to use.
>
>    2. Note the bucket's Link for gsutil value.
>
>    3. Grant permissions on the bucket to the service account you created in step 1.
>
> 4. Make sure your current Kubernetes context references the cluster and namespace where the DS pods are running.
>
> 5. Create the `cloud-storage-credentials` secret that contains credentials to write to cloud storage. The DS pods use this secret when performing backups.
>
>    For `my-sa-credential.json`, specify the JSON file containing the service account's key:
>
>    ```
>    $ kubectl create secret generic cloud-storage-credentials \
>     --from-file=GOOGLE_CREDENTIALS_JSON=/path/to/my-sa-credential.json
>    ```
>
> 6. Restart the pods that perform backups so that DS can get the credentials needed to write to the backup location:
>
>    ```
>    $ kubectl delete pods ds-cts-0
>    $ kubectl delete pods ds-idrepo-0
>    ```
>
> After the pods have restarted, you can [schedule backups](#schedule-backups).

> **Collapse: AWS**
>
> Set up an S3 bucket for the DS data backup and configure the ForgeOps deployment with the credentials for the bucket:
>
> 1. Create or identify an existing S3 bucket for storing the DS data backup and note the S3 link of the bucket.
>
> 2. Make sure your current Kubernetes context references the cluster and namespace where the DS pods are running.
>
> 3. Create the `cloud-storage-credentials` secret that contains credentials to write to the cloud storage. The DS pods use this secret when performing backups:
>
>    ```
>    $ kubectl create secret generic cloud-storage-credentials \
>     --from-literal=AWS_ACCESS_KEY_ID=my-access-key \
>     --from-literal=AWS_SECRET_ACCESS_KEY=my-secret-access-key
>    ```
>
> 4. Restart the pods that perform backups so that DS can get the credentials needed to write to the backup location:
>
>    ```
>    $ kubectl delete pods ds-cts-0
>    $ kubectl delete pods ds-idrepo-0
>    ```
>
> After the pods have restarted, you can [schedule backups](#schedule-backups).

> **Collapse: Azure**
>
> Set up an Azure Blob Storage container for the DS data backup and configure the ForgeOps deployment with the credentials for the container:
>
> 1. Create or identify an existing Azure Blob Storage container for the DS data backup. Learn more about how to create and use Azure Blob Storage in [Quickstart: Create, download, and list blobs with Azure CLI](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-cli).
>
> 2. Log in to Azure Container Registry:
>
>    ```
>    $ az acr login --name my-acr-name
>    ```
>
> 3. Get the full Azure Container Registry ID:
>
>    ```
>    $ ACR_ID=$(az acr show --name my-acr-name --query id | tr -d '"')
>    ```
>
>    With the full registry ID, you can connect to a container registry even if you are logged in to a different Azure subscription.
>
> 4. Add permissions to connect your AKS cluster to the container registry:
>
>    ```
>    $ az aks update --name my-aks-cluster-name --resource-group my-cluster-resource-group --attach-acr $ACR_ID
>    ```
>
> 5. Make sure your current Kubernetes context references the cluster and namespace where the DS pods are running.
>
> 6. Create secrets that contain credentials to write to cloud storage. The DS pods use these when performing backups:
>
>    1. Get the name and access key of the Azure storage account for your storage container\[[23](#_footnotedef_23 "View footnote.")].
>
>    2. Create the `cloud-storage-credentials` secret:
>
>    ```
>    $ kubectl create secret generic cloud-storage-credentials \
>     --from-literal=AZURE_STORAGE_ACCOUNT_NAME=my-storage-account-name \
>     --from-literal=AZURE_ACCOUNT_KEY=my-storage-account-access-key
>    ```
>
> 7. Restart the pods that perform backups so that DS can get the credentials needed to write to the backup location:
>
>    ```
>    $ kubectl delete pods ds-cts-0
>    $ kubectl delete pods ds-idrepo-0
>    ```
>
> After the pods have restarted, you can [schedule backups](#schedule-backups).

##### Schedule backups

1. Make sure you've [set up cloud storage for your cloud provider platform](#setup-cloud-storage).

2. Make sure your current Kubernetes context references the cluster and namespace where the DS pods are running.

3. Make sure you've backed up and saved the shared master key and TLS key for the ForgeOps deployment.

4. Set variable values in the /path/to/forgeops/bin/ds-backup.sh script:

   | Variable Name             | Default                   | Notes                                                                                                                                                                                                                           |
   | ------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `HOSTS`                   | `ds-idrepo-2`             | The `ds-idrepo` or `ds-cts` replica or replicas to back up. Specify a comma-separated list to back up more than one replica. For example, to back up the `ds-idrepo-2` and `ds-cts-2` replicas, specify `ds-idrepo-2,ds-cts-2`. |
   | `BACKUP_SCHEDULE_IDREPO`  | On the hour and half hour | How often to run backups of the `ds-idrepo` directory. Specify using [cron job format](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules).                                                                 |
   | `BACKUP_DIRECTORY_IDREPO` | n/a                       | Where the `ds-idrepo` directory is backed up. Specify:- `gs://bucket/path` to back up to Google Cloud Storage

   - `s3://bucket/path` to back up to Amazon S3

   - `az://container/path` to back up to Azure Blob Storage           |
   | `BACKUP_SCHEDULE_CTS`     | On the hour and half hour | How often to run backups of the `ds-cts` directory. Specify using [cron job format](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules).                                                                    |
   | `BACKUP_DIRECTORY_CTS`    | n/a                       | Where the `ds-cts` directory is backed up. Specify:- `gs://bucket/path` to back up to Google Cloud Storage

   - `s3://bucket/path` to back up to Amazon S3

   - `az://container/path` to back up to Azure Blob Storage              |

5. Run the ds-backup.sh create command to schedule backups:

   ```
   $  /path/to/forgeops/bin/ds-backup.sh create
   ```

   The first backup is a full backup; all later backups are incremental from the previous backup.

   By default, the ds-backup.sh create command configures:

   * The backup task name to be `recurringBackupTask`

   * The backup tasks to back up all DS backends

   If you want to change either of these defaults, configure variable values in the ds-backup.sh script.

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | To cancel a backup schedule, run the ds-backup.sh cancel command. |

#### Restore

This section covers three options to restore data from dsbackup backups:

* [New ForgeOps deployment using DS backup](#new-deployment)

* [Restore all DS directories](#restore-all-directories)

* [Restore one DS directory](#restore-one-directory)

##### New ForgeOps deployment using DS backup

Creating new instances from previously backed up DS data is useful when a system disaster occurs or when directory services are lost. It is also useful when you want to port test environment data to a production deployment.

To create new DS instances with data from a previous backup:

1. Make sure your current Kubernetes context references the new ForgeOps cluster. Also make sure that the namespace of your Kubernetes context contains the DS pods into which you plan to load data from backup.

2. Create Kubernetes secrets containing your cloud storage credentials:

   > **Collapse: On Google Cloud**
   >
   > ```
   > $ kubectl create secret generic cloud-storage-credentials \
   >  --from-file=GOOGLE_CREDENTIALS_JSON=/path/to/my-sa-credential.json
   > ```
   >
   > In this example, specify the path and file name of the JSON file containing the Google service account key for my-sa-credential.json.

   > **Collapse: On AWS**
   >
   > ```
   > $ kubectl create secret generic cloud-storage-credentials \
   >  --from-literal=AWS_ACCESS_KEY_ID=my-access-key \
   >  --from-literal=AWS_SECRET_ACCESS_KEY=my-secret-access-key
   >  --from-literal=AWS_REGION=my-region
   > ```

   > **Collapse: On Azure**
   >
   > ```
   > $ kubectl create secret generic cloud-storage-credentials \
   >  --from-literal=AZURE_STORAGE_ACCOUNT_NAME=my-storage-account-name \
   >  --from-literal=AZURE_ACCOUNT_KEY=my-storage-account-access-key
   > ```

3. Configure the backup bucket location and enable the automatic restore capability:

* In a Kustomize-based deployment

* In a Helm-based deployment

1. Change to the /path/to/forgeops/kustomize/base/kustomizeConfig directory.

2. Open the kustomization.yaml file.

3. Set the `DSBACKUP_DIRECTORY` parameter to the location of the backup bucket. For example:

   > **Collapse: On Google Cloud**
   >
   > `DSBACKUP_DIRECTORY="gs://my-backup-bucket"`

   > **Collapse: On AWS**
   >
   > `DSBACKUP_DIRECTORY="s3://my-backup-bucket"`

   > **Collapse: On Azure**
   >
   > `DSBACKUP_DIRECTORY="az://my-backup-bucket"`

4. Set the `AUTORESTORE_FROM_DSBACKUP` parameter to `"true"`.

1) Change to the /path/to/forgeops/charts/identity-platform directory.

2) Edit values.yaml file and set up `autoRestore`, `backupLocation`, and `backupHosts` parameters for `ds-idrepo` and `ds-cts`. For example to restore `ds-idrepo-2`:

   > **Collapse: On Google Cloud**
   >
   > ```
   > ...
   > ds_restore:
   >   autoRestore: true
   >   backupLocation: "gs://my-backup-bucket"
   >   backupHosts: "ds-idrepo-2"
   > ...
   > ```

   > **Collapse: On AWS**
   >
   > ```
   > ...
   > ds_restore:
   >   autoRestore: true
   >   backupLocation: "s3://my-backup-bucket"
   >   backupHosts: "ds-idrepo-2"
   > ...
   > ```

   > **Collapse: On Azure**
   >
   > ```
   > ...
   > ds_restore:
   >   autoRestore: true
   >   backupLocation: "az://my-backup-bucket"
   >   backupHosts: "ds-idrepo-2"
   > ...
   > ```

4. Then [Deploy the platform](deploy/deploy.html).

   When the platform is deployed, new DS pods are created, and the data is automatically restored from the most recent backup available in the cloud storage location you configured.

To verify that the data has been restored:

* Use the IDM UI or platform UI.

* Review the logs for the DS pods' `init` container. For example:

  ```
  $ kubectl logs --container init ds-idrepo-0
  ```

##### Restore all DS directories

To restore all the DS directories in your ForgeOps deployment from backup:

1. Delete all the PVCs attached to DS pods using the kubectl delete pvc command.

2. Because PVCs might not get deleted immediately when the pods to which they're attached are running, stop the DS pods.

   Using separate terminal windows, stop every DS pod using the kubectl delete pod command. This deletes the pods and their attached PVCs.

   Kubernetes automatically restarts the DS pods after you delete them. The automatic restore feature of ForgeOps deployments recreates the PVCs as the pods restart by retrieving backup data from cloud storage and restoring the DS directories from the latest backup.

3. After the DS pods come up, restart IDM pods to reconnect IDM to the restored PVCs:

   1. List all the pods in the namespace.

   2. Delete all the pods running IDM.

##### Restore one DS directory

In a ForgeOps deployment with automatic restore enabled, you can recover a failed DS pod if the latest backup is within the [replication purge delay](https://docs.pingidentity.com/pingds/8/configref/objects-replication-synchronization-provider.html#replication-purge-delay):

1. Delete the PVC attached to the failed DS pod using the kubectl delete pvc command.

2. Because the PVC might not get deleted immediately if the attached pod is running, stop the failed DS pod.

   In another terminal window, stop the failed DS pod using the kubectl delete pod command. This deletes the pod and its attached PVC.

   Kubernetes automatically restarts the DS pod after you delete it. The automatic restore feature recreates the PVC as the pod restarts by retrieving backup data from cloud storage and restoring the DS directory from the latest backup.

3. If the DS instance you restored was the `ds-idrepo` instance, restart IDM pods to reconnect IDM to the restored PVC:

   1. List all the pods in the namespace.

   2. Delete all the pods running IDM.

For information about manually restoring DS where the latest available backup is older than the replication purge delay, refer to the [Restore](https://docs.pingidentity.com/pingds/8/maintenance-guide/backup-restore.html#restore) section in the DS documentation.

##### Restore a PingDS deployment after a disaster

The PingDS disaster recovery involves additional steps beyond restoring a complete PingDS environment from backup. The dsrepl disaster-recovery must be run after a normal restore and before the PingDS server starts.

The disaster recovery process resets replication metadata to allow the newly restored version of the PingDS topology. A disaster recovery ID identifies the new topology. The data pods not being restored have a different disaster recovery ID and don't exchange data with pods already recovered.

The disaster recovery process is automated in Forgeops. When a restore is initiated, the disaster recovery is also initiated using the disaster recovery ID defined in the configuration. If the disaster recovery ID matches the contents of the restored backup, the disaster recovery is stopped; otherwise, the data is disaster recovered.

The disaster recovery ID is configured in the `platform-config` configmap as follows:

* For Helm: update `ds_restore.disasterRecoveryId` in your custom values file

* For Kustomize: update DISASTER\_RECOVERY\_ID in your custom overlay in base/platform-config.yaml

##### Best practices for restoring directories

* Use a backup newer than the last replication purge.

* When you restore a single DS replica, the backup must be recent. Learn more at [DS README](https://github.com/ForgeRock/forgeops/blob/dev/docker/ds/README.md#restore-of-a-single-instance-rest-of-topology-still-valid).

#### Using cloud storage locally for backup and restore

In DS version 8.1.0 you can use cloud storage mounted locally for backup and restore. This is useful for local testing of backup and restore. You can mount cloud storage as local filesystem and use the local mount point as a local backup location. Learn more about mounting cloud storage locally in the [Cloud storage section](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html#cloud-storage) of DS documentation.

## Upgrade and Migration Overview

This section provides the conceptual and procedural details for upgrading your ForgeOps deployment environment or migrating utilities therein.

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because the Ping Advanced Identity Software is highly customizable, testing all possible upgrade scenarios is challenging. It is your responsibility to validate that these upgrade steps work correctly in a test environment with your customized configuration before you upgrade a production environment. |

Upgrading ForgeOps deployments involves three main sections:

* Upgrade ForgeOps deployment from 2025.1

  * [Upgrade Helm charts](upgrade/update-helm.html)

* Upgrade Ping Advanced Identity Software Docker images

  * [Upgrade Ping Advanced Identity Software Docker images to new major or minor version](upgrade/upgrade-product.html).

  * [Upgrade Ping Advanced Identity Software Docker image to new patch release](upgrade/upgrade-patch.html).

* Upgrade from previous ForgeOps releases

  * [Migrate Kustomize configurations](upgrade/migrate-forgeops.html).

  * [Migrate from a ForgeOps 7.4 or 7.5 release branch to the 2026.2 tag](upgrade/mig-74-75.html).

## Troubleshooting

Kubernetes deployments are multi-layered and often complex.

Errors and misconfigurations can crop up in a variety of places. Performing a logical, systematic search for the source of a problem can be daunting.

Before you troubleshoot, verify your ForgeOps version:

```
$ cd /path/to/forgeops
$ ./bin/forgeops version
```

Here are some techniques you can use to troubleshoot problems with ForgeOps deployments:

| Problem                                                                                 | Troubleshooting Technique                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Some pods don't start.                                                                  | Review [Kubernetes logs and other diagnostics](troubleshoot/pods.html). Verify if your cluster is resource-constrained. Check for under-configured clusters by using the `kubectl describe nodes` and `kubectl get events -w` commands. Pods terminated with out of memory (OOM) errors indicate that your cluster is under-configured. Make sure that you're using [tested versions of third-party software](troubleshoot/sw-versions.html). [Stage your installation](troubleshoot/staged-deployment.html). Install Ping Advanced Identity Software components separately, instead of installing all the components with a single command. Staging your installation lets you make sure each component works correctly before installing the next component. |
| All the pods have started, but you can't reach the services running in them.            | Make sure you don't have any [ingress issues](troubleshoot/ingress.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AM doesn't work as expected.                                                            | [Set the AM logging level](https://community.forgerock.com/t/how-to-enable-and-modify-logging-level-in-forgeops-for-am.html), recreate the issue, and analyze the AM log files. [Turn on audit logging in AM.](https://community.forgerock.com/t/how-to-enable-and-modify-audit-logging-in-am-and-idm-for-forgeops.html)                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| IDM doesn't work as expected.                                                           | [Set the IDM logging level](https://community.forgerock.com/t/how-to-enable-and-modify-logging-level-in-forgeops-for-idm.html), recreate the issue, and analyze the IDM log files. [Turn on audit logging in IDM.](https://community.forgerock.com/t/how-to-enable-and-modify-audit-logging-in-am-and-idm-for-forgeops.html)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Your JVM crashed with an out of memory error, or you suspect that you've a memory leak. | [Collect and analyze Java thread dumps and heap dumps](https://support.pingidentity.com/s/article/How-do-I-collect-Java-thread-dumps-and-heap-dumps-for-troubleshooting-a-ForgeOps-deployment).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Changes you've made to ForgeOps's Kustomize files don't work as expected.               | [Fully expand the Kustomize output](troubleshoot/kustomize.html), and then examine the output for unintended effects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Your minikube deployment doesn't work.                                                  | Make sure that you don't have a problem with [virtual hardware requirements](troubleshoot/minikube.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| You're having name resolution or other DNS issues.                                      | Use diagnostic tools in the [debug tools container](troubleshoot/debug-tools.html#debug-tools-container).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| You want to run DS utilities without disturbing a DS pod.                               | Use the [bin/ds-debug.sh script](troubleshoot/debug-tools.html#ds-debug) or DS tools in the [debug tools container](troubleshoot/debug-tools.html#debug-tools-container).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| You want to keep the `amster` pod running to diagnose AM configuration issues.          | Use the [forgeops amster command](troubleshoot/amster.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| The `kubectl` command requires too much typing.                                         | Enable [kubectl tab autocompletion](troubleshoot/tab-completion.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Kubernetes logs and other diagnostics

Look at pod descriptions and container log files for irregularities that indicate problems.

*Pods Information* contains details about active Kubernetes pods, including their configuration, status, containers (including containers that have finished running), volume mounts, and pod-related events.

*Container logs* contain startup and run-time messages that might indicate problem areas. Each Kubernetes container has its own log that contains all output written to `stdout` by the application running in the container. The `am` container logs are especially important for troubleshooting AM issues in Kubernetes deployments. AM writes its debug logs to `stdout`. Therefore, the `am` container logs include all the AM debug logs.

#### debug-logs utility

The debug-logs utility generates the following HTML-formatted output, which you can view in a browser:

* Descriptions of all the Kubernetes pods running in your namespace

* Logs for all the containers running in these pods

* Descriptions of the PVCs running in your cluster

* Operator logs

* Information about your local environment, including:

  * ForgeOps release version

  * Deployment method (Helm or Kustomize)

  * Third-party software versions

  * The custom resource definitions (CRDs) installed in your cluster

  * Kubernetes storage classes

  * The most recent commits in your forgeops repository clone's commit log

  * Deployment environment in the `env.log` file

  * Details about a variety of Kubernetes objects on your cluster

#### Example troubleshooting steps

Suppose you performed a ForgeOps deployment but noticed that one of the pods had an `ImagePullBackOff` error at startup. Here's an example of how you can use pod descriptions and container logs to troubleshoot the problem:

1. Make sure the active namespace in your local Kubernetes context is the one that contains the component you are debugging.

2. Make sure you've checked out the 2026.2.1 branch of the `forgeops` repository.

3. Change to the /path/to/forgeops/bin directory in your `forgeops` repository clone.

4. Run the debug-logs command appropriate to the method you used for deployment:

   1. For Helm-based deployments:

      ```
      $ ./debug-logs --helm --env-name my-env
      Writing environment information
      Writing pod descriptions and container logs
       ...
      Writing information about various Kubernetes objects
      Open /tmp/forgeops/log.html in your browser.
      ```

   2. For Kustomize-based deployments:

      ```
      $ ./debug-logs --kustomize --env-name my-env
      Writing environment information
      Writing pod descriptions and container logs
       ...
      Writing information about various Kubernetes objects
      Open /tmp/forgeops/log.html in your browser.
      ```

5. In a browser, go to the URL shown in the debug-logs output. In this example, the URL is file:///tmp/forgeops/log.html. The browser displays a screen with a link for each Ping Advanced Identity Software pod in your namespace:

   ![Screen shot of debug-logs output.](troubleshoot/_images/debug-logs.png)

6. Access the information for the pod that didn't start correctly by selecting its link from the Pod Descriptions and Container Logs section of the debug-logs output.

   Selecting the link takes you to the pod's description. Logs for each of the pod's containers follow the pod's description.

After you've obtained the pod descriptions and container logs, here are some actions you might take:

* Examine each pod's event log for failures.

* If a Docker image could not be pulled, verify that the Docker image name and tag are correct. If you are using a private registry, verify that your image pull secret is correct.

* Examine the init containers. Did each init container complete with a zero (success) exit code? If not, examine the logs from that failed init container using the `kubectl logs pod-xxx -c init-container-name` command.

* Look at the logs from pods to check if the main container entered a crash loop.

### DS diagnostic tools

#### Debug script

The bin/ds-debug.sh script lets you obtain diagnostic information for any DS pod running in your cluster. It also lets you perform several cleanup and recovery operations on DS pods.

Run bin/ds-debug.sh -h to refer to the command's syntax.

The following bin/ds-debug.sh subcommands provide diagnostic information:

| Subcommand   | Diagnostics                                                   |
| ------------ | ------------------------------------------------------------- |
| status       | Server details, connection handlers, backends, and disk space |
| rstatus      | Replication status                                            |
| idsearch     | All the DNs in the `ou=identities` branch                     |
| monitor      | All the directory entries in the `cn=monitor` branch          |
| list-backups | A list of the backups associated with a DS instance           |

The bin/ds-debug.sh purge command purges all the backups associated with a DS instance.

#### Debug tools container

The `ds-util` debug tools container provides a suite of diagnostic tools that you can execute inside of a running Kubernetes cluster.

The container has two types of tools:

* DS tools—A DS instance is installed in the /opt/opendj directory of the `ds-util` container. DS tools, such as the ldapsearch and ldapmodify commands, are available in the /opt/opendj/bin directory.

* Miscellaneous diagnostic tools—A set of diagnostic tools, including `dig`, `netcat`, `nslookup`, `curl`, and `vi`, have been installed in the container. The file, /path/to/forgeops/docker/ds/dsutil/Dockerfile, has the list of operating system packages that have been installed in the debug tools container.

To start the debug tools container:

```
$ kubectl run -it ds-util --image=gcr.io/forgeops-public/ds-util -- bash
```

After you start the tools container, a command prompt appears:

```
root@ds-util:/opt/opendj#
```

You can access all the tools available in the container from this prompt. For example:

```
root@ds-util:/opt/opendj# nslookup am
Server:		10.96.0.10
Address:	10.96.0.10#53

Name:	am.my-namespace.svc.cluster.local
Address: 10.100.20.240
```

### Troubleshooting the `amster` pod

When ForgeOps deployments start, the `amster` pod starts and imports AM dynamic configuration. Once dynamic configuration is imported, the `amster` pod is stopped and remains in `Completed` status.

```
$ kubectl get pods
NAME                          READY   STATUS      RESTARTS   AGE
admin-ui-b977c857c-2m9pq      1/1     Running     0          10m
am-666687d69c-94thr           1/1     Running     0          12m
amster-4prdg                  0/1     Completed   0          12m
ds-idrepo-0                   1/1     Running     0          13m
end-user-ui-674c4f79c-h4wgb   1/1     Running     0          10m
idm-869679958c-brb2k          1/1     Running     0          12m
login-ui-56dd46c579-gxrtx     1/1     Running     0          10m
```

#### Start the `amster` pod

After you install AM, use the forgeops amster run command to start the `amster` pod for manually interacting with AM using the forgeops amster run command-line interface and perform tasks such as exporting and importing AM configuration and troubleshooting:

```
$ ./bin/forgeops amster run --env-name my-env
starting...
...

$ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
admin-ui-b977c857c-2m9pq      1/1     Running   0          22m
am-666687d69c-94thr           1/1     Running   0          24m
amster-852fj                  1/1     Running   0          12s
ds-idrepo-0                   1/1     Running   0          25m
end-user-ui-674c4f79c-h4wgb   1/1     Running   0          22m
idm-869679958c-brb2k          1/1     Running   0          24m
login-ui-56dd46c579-gxrtx     1/1     Running   0          22m
```

The amster jobs have a default time-to-live (TTL) value set to 600 seconds. The amster jobs are removed from the namespace after 10 minutes to allow later runs of amster jobs if the spec is updated in the user's environment and redeployed.

A Kubernetes job cannot be updated after it has started running. If the amster job is running when you apply an update, then an error is thrown. The beginning of the error appears similar to the following:

```
The Job "amster" is invalid: spec.template: Invalid value: ...
...
"batch.kubernetes.io/job-name":"amster", ...
"job-name":"amster"}
```

If an `amster` job fails due to low TTL, then delete `amster` jobs using the kubectl delete jobs command and redeploy.

#### Export and import AM configuration

To export AM configuration, use the forgeops amster export command. Similarly, use the forgeops amster import command to import AM configuration. At the end of the export or import session, the `amster` pod is stopped by default. To keep the `amster` pod running, use the --retain option. You can specify the time (in seconds) to keep the `amster` running.

In the following example, the `amster` pod is kept running for 900 seconds after completing export:

```
$ ./bin/forgeops amster export --env-name my-env --retain 900 /tmp/myexports
Cleaning up amster components
job.batch "amster" deleted
configmap "amster-files" deleted
Packing and uploading configs
configmap/amster-files created
configmap/amster-export-type created
Deploying amster
job.batch/amster created

Waiting for amster job to complete. This can take several minutes.
pod/amster-d6vsv condition met
tar: Removing leading `/' from member names
Updating amster config.
Updating amster config complete.
```

```
$ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
admin-ui-b977c857c-2m9pq      1/1     Running   0          27m
am-666687d69c-94thr           1/1     Running   0          29m
amster-d6vsv                  1/1     Running   0          53s
ds-idrepo-0                   1/1     Running   0          30m
end-user-ui-674c4f79c-h4wgb   1/1     Running   0          27m
idm-869679958c-brb2k          1/1     Running   0          29m
login-ui-56dd46c579-gxrtx     1/1     Running   0          27m
```

After 900 seconds notice that the `amster` pod is in `Completed` status:

```
$ kubectl get pods
NAME                          READY   STATUS      RESTARTS   AGE
admin-ui-b977c857c-2m9pq      1/1     Running     0          78m
am-666687d69c-94thr           1/1     Running     0          80m
amster-d6vsv                  0/1     Completed   0          51m
ds-idrepo-0                   1/1     Running     0          81m
end-user-ui-674c4f79c-h4wgb   1/1     Running     0          78m
idm-869679958c-brb2k          1/1     Running     0          80m
login-ui-56dd46c579-gxrtx     1/1     Running     0          78m
```

Similarly, use the `--retain` option with the forgeops amster import command to keep the `amster` job running to completion.

### Staged installation

By default, the forgeops apply command installs the entire Ping Advanced Identity Software.

You can also install the platform in stages to help troubleshoot deployment issues.

To install the platform in stages:

1. Verify you've set up your environment and created a Kubernetes cluster as documented in the [setup section](setup/overview.html).

2. Use the terminal where you have already activated Python3 virtual environment. If you haven't already done so, activate the virtual environment in a new terminal window:

   ```
   $ source .venv/bin/activate
   ```

3. Verify your ForgeOps version:

   ```
   $ cd /path/to/forgeops
   $ ./bin/forgeops version
   ```

4. The configuration of a ForgeOps deployment is steered through the use of Kustomize overlays or Helm values. Use the forgeops env command to set up the Kustomize overlays and Helm values files to configure your ForgeOps deployment environment:

   * If you want to use the issuer provided with the platform for demo, then you can use default-issuer.

   * For a clusters on a cloud environment specify the --deployment-size as `--small`, `--medium`, or `--large`.

   * For a single-instance deployment, specify --deployment-size as `--single-instance`.

     ```
     $ cd /path/to/forgeops/bin
     $ ./forgeops env --env-name my-env --fqdn my-fqdn.example.com --cluster-issuer my-cluster-issuer --deployment-size
     ```

     In the command above, replace my-fqdn.example.com, my-cluster-issuer, and --deployment-size with appropriate values from your environment.

     Learn more about deployment sizes in [Cluster and deployment sizes](deploy/architecture.html#cluster-and-deployment-sizes) and about single instances [here](deploy/architecture.html#single-inst).

5. Install the `base` and `ds` components first. Other components have dependencies on these two components:

   1. Install the platform `base` component:

      ```
      $ cd /path/to/forgeops/bin
      $ ./forgeops apply base --env-name my-env
      ...
      configmap/platform-config created
      Warning: spec.privateKey.rotationPolicy: In cert-manager >= v1.18.0, the default value changed from Never to Always.
      certificate.cert-manager.io/ds-master-cert created
      certificate.cert-manager.io/ds-ssl-cert created
      issuer.cert-manager.io/selfsigned-issuer created
      secretagentconfiguration.secret-agent.secrets.forgerock.io/forgerock-sac created
      Waiting for secrets to be ready.
      ...
      Relevant passwords:
      ...

      Relevant URLs:
      ...
      ```

   2. After you've installed the `base` component, install the `ds` component:

      ```
      $ ./forgeops apply ds --env-name my-env
      service/ds-cts created
      statefulset.apps/ds-cts created
      service/ds-idrepo created
      statefulset.apps/ds-idrepo created
      configmap/ds-set-passwords-scripts created
      job.batch/ds-set-passwords created
      ```

6. Install the other Ping Advanced Identity Software components. You can either install all the other components by using the forgeops apply apps command, or install them separately:

   1. Install AM:

      ```
      $ ./forgeops apply am --env-name my-env

      configmap/am-entrypoint created
      configmap/am-import-pem-certs created
      configmap/am-logback created
      service/am created
      deployment.apps/am created
      ingress.networking.k8s.io/am created
      Targeting namespace: my-ns
      ```

   2. Install Amster:

      ```
      $ ./forgeops apply amster --env-name my-env
      job.batch/amster created
      ```

   3. Install IDM:

      ```
      $ ./forgeops apply idm --env-name my-env
      configmap/idm created
      configmap/idm-import-pem-certs created
      configmap/idm-logback-xml created
      configmap/idm-logging-properties created
      service/idm created
      deployment.apps/idm created
      ingress.networking.k8s.io/idm created
      ```

7. Install the user interface components. You can either install all the applications by using the forgeops apply ui command, or install them separately:

   1. Install the administration UI:

      ```
      $ ./forgeops apply admin-ui --env-name my-env
      name my-env
      service/admin-ui created
      deployment.apps/admin-ui created
      ingress.networking.k8s.io/admin-ui created
      ```

   2. Install the login UI:

      ```
      $ ./forgeops apply login-ui --env-name my-env
      service/login-ui created
      deployment.apps/login-ui created
      ingress.networking.k8s.io/login-ui created
      ```

   3. Install the end user UI:

      ```
      $ ./forgeops apply end-user-ui --env-name my-env
      name my-env
      service/end-user-ui created
      deployment.apps/end-user-ui created
      ingress.networking.k8s.io/end-user-ui created
      ```

8. In a separate terminal tab or window, run the kubectl get pods command to monitor status of the deployment. Wait until all the pods are ready.

#### Multiple component installation

You can specify multiple components with a single forgeops apply command. For example, to install the `base`, `ds`, `am`, and `amster` components in a ForgeOps deployment:

```
$ ./forgeops apply base ds am amster --env-name my-env
```

### Ingress issues

If the pods in a ForgeOps deployment are starting successfully, but you can't reach the services in those pods, you probably have ingress issues.

To diagnose ingress issues:

1. Use the `kubectl describe ing` and `kubectl get ing ingress-name -o yaml` commands to view the ingress object.

2. Describe the service using the `kubectl get svc; kubectl describe svc xxx` command. Does the service have an `Endpoint:` binding? If the service endpoint binding is not present, the service did not match any running pods.

### Third-party software versions

The ForgeOps team recommends installing tested versions of third-party software in environments where you'll run ForgeOps deployments.

Refer to the tables that list the tested versions of third-party software for your deployment:

* [On minikube](setup/minikube.html#minikube-third-party-software)

* [On GKE](setup/google-cloud.html#gcp-third-party-software)

* [On EKS](setup/aws.html#aws-third-party-software)

* [On AKS](setup/azure.html#azure-third-party-software)

You can use the debug-logs utility to get the versions of third-party software installed in your local environment. After you've performed a ForgeOps deployment:

1. Run the /path/to/forgeops/bin/debug-logs utility.

2. Open the log file in your browser.

3. Select Environment Information > Third-party software versions.

### Expanded Kustomize output

If you've modified any of the Kustomize bases and overlays that come with the `cdk` canonical configuration, you might want to consider how your changes affect deployment. Use the kustomize build command to assess how Kustomize expands your bases and overlays into YAML files.

For example:

```
$ cd /path/to/forgeops/kustomize/overlay
$ kustomize build all
apiVersion: v1
data:
  IDM_ENVCONFIG_DIRS: /opt/openidm/resolver
  LOGGING_PROPERTIES: /var/run/openidm/logging/logging.properties
  OPENIDM_ANONYMOUS_PASSWORD: anonymous
  OPENIDM_AUDIT_HANDLER_JSON_ENABLED: "false"
  OPENIDM_AUDIT_HANDLER_STDOUT_ENABLED: "true"
  OPENIDM_CLUSTER_REMOVE_OFFLINE_NODE_STATE: "true"
  OPENIDM_CONFIG_REPO_ENABLED: "false"
  OPENIDM_ICF_RETRY_DELAYSECONDS: "10"
  OPENIDM_ICF_RETRY_MAXRETRIES: "12"
  PROJECT_HOME: /opt/openidm
  RCS_AGENT_CONNECTION_CHECK_SECONDS: "5"
  RCS_AGENT_CONNECTION_GROUP_CHECK_SECONDS: "900"
  RCS_AGENT_CONNECTION_TIMEOUT_SECONDS: "10"
  RCS_AGENT_HOST: rcs-agent
  RCS_AGENT_IDM_PRINCIPAL: idmPrincipal
  RCS_AGENT_PATH: idm
  RCS_AGENT_PORT: "80"
  RCS_AGENT_USE_SSL: "false"
  RCS_AGENT_WEBSOCKET_CONNECTIONS: "1"
kind: ConfigMap
metadata:
  labels:
    app: idm
    app.kubernetes.io/component: idm
    app.kubernetes.io/instance: idm
    app.kubernetes.io/name: idm
    app.kubernetes.io/part-of: forgerock
    tier: middle
  name: idm
---
apiVersion: v1
data:
  logging.properties: |
...
```

### minikube hardware resources

#### Cluster configuration

The minikube start command example in [minikube](setup/minikube.html) provides a good default virtual hardware configuration for a minikube cluster running a single-instance ForgeOps deployment.

#### Disk space

When the minikube cluster runs low on disk space, it acts unpredictably. Unexpected application errors can appear.

Verify that adequate disk space is available by logging in to the minikube cluster and running a command to display free disk space:

```
$ minikube ssh
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        3.9G     0  3.9G   0% /dev
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           3.9G  383M  3.6G  10% /run
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
tmpfs           3.9G   64K  3.9G   1% /tmp
/dev/sda1        25G  7.7G   16G  33% /mnt/sda1
/Users          465G  219G  247G  48% /Users
$ exit
logout
```

In the preceding example, 16 GB of disk space is available on the minikube cluster.

### `kubectl` shell autocompletion

The kubectl shell autocompletion extension lets you extend the Tab key completion feature of Bash and Zsh shells to the kubectl commands. While not a troubleshooting tool, this extension can make troubleshooting easier, because it lets you enter kubectl commands more easily.

For more information about the Kubernetes autocompletion extension, see [Enabling shell autocompletion](https://kubernetes.io/docs/tasks/kubectl/install/#enabling-shell-autocompletion) in the Kubernetes documentation.

Note that to install the autocompletion extension in Bash, you must be running version 4 or later of the Bash shell. To determine your bash shell version, run the bash --version command.

## References

This section includes:

* Steps to create your own [Base Docker images](reference/base-docker-images.html).

* [Reference documentation](reference/forgeops.html) for the forgeops command.

* A [glossary](reference/glossary.html) of terminology used in this documentation.

* [Articles and knowledge base entries](reference/beyond-the-docs.html) pertaining ForgeOps that aren't part of the official ForgeOps documentation.

* [How-to articles in `forgeops` repository](reference/how-tos.html).

### Base Docker images

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This procedure is moved into the reference section because creating Docker images from scratch is only required under special circumstances.Before you begin building custom images, ensure you've installed Java version 25 or 21 on your computer.For example:> **Collapse: When using platform versions 8.x**
>
> ```
> $ java --version
> openjdk version "25.0.2" 2026-01-20
> OpenJDK Runtime Environment Homebrew (build 25.0.2)
> OpenJDK 64-Bit Server VM Homebrew (build 25.0.2, mixed mode, sharing)
> ```> **Collapse: When using platform versions 7.x**
>
> ```
> $ java --version
> openjdk 21.0.5 2024-10-15 LTS
> OpenJDK Runtime Environment Temurin-21.0.5+11 (build 21.0.5+11-LTS)
> OpenJDK 64-Bit Server VM Temurin-21.0.5+11 (build 21.0.5+11-LTS, mixed mode)
> ``` |

#### Which Docker images do I deploy?

* I am a developer using a single-instance ForgeOps deployment.

  * UI elements. Deploy the supported images from ForgeOps.

  * Other platform elements. Deploy either:

    * The ForgeOps-provided images.

    * Customized Docker images that are based on ForgeOps-provided images and contain customized configuration profile.

* I am doing a proof-of-concept ForgeOps deployment.

  * UI elements. Deploy the supported images from ForgeOps.

  * Other platform elements. Deploy either:

    * The ForgeOps-provided images.

    * Customized Docker images that are based on ForgeOps-provided images and contain customized configuration profile.

* I am deploying the platform in production.

  * UI elements. Deploy the supported images from ForgeOps.

  * Other platform elements. Deploy Docker images you've built that are based on [your own base images](#base-images), but contain your customized configuration profile.

#### Your initial base Docker images

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The procedures here describe the use of:1) Docker container engine to create images for ForgeOps deployment. You can use Podman container engine for the same.

2) The latest ForgeOps-provided Docker images. You can select a specific image release suitable to your environment. |

Perform the following steps to build base images. After you've built your own base images, push them to your Docker repository:

1. Download the latest versions of the AM, Amster, IDM, and DS `.zip` files from [the Ping Identity Download Center](https://backstage.forgerock.com/downloads). Optionally, you can also download the latest version of the PingGateway `.zip` file.

2. If you haven't already done so, clone the `forgeops` and `forgeops-extras` repositories. For example:

   ```
   $ git clone https://github.com/ForgeRock/forgeops.git
   $ git clone https://github.com/ForgeRock/forgeops-extras.git
   ```

   Both repositories are public; you do not need credentials to clone them.

3. Check out the `forgeops` repository's `2026.2.1` tag:

   ```
   $ cd /path/to/forgeops
   $ git checkout 2026.2.1
   ```

4. Check out the `forgeops-extras` repository's `main` tag:

   ```
   $ cd /path/to/forgeops-extras
   $ git checkout main
   ```

5. Build the Java base image, which is required by several of the other Dockerfiles:

   > **Collapse: For platform images 8.x**
   >
   > ```
   > $ cd /path/to/forgeops-extras/images/java-25
   > $ docker build --tag my-repo/my-java .
   > ```

   > **Collapse: For platform images 7.x**
   >
   > ```
   > $ cd /path/to/forgeops-extras/images/java-21
   > $ docker build --tag my-repo/my-java .
   > ```

6. Build the base Docker image for Amster. The Amster image is required to build the base image for AM in the next step:

   1. Unzip the Amster `.zip` file.

   2. Change to the amster/samples/docker directory in the expanded `.zip` file output.

   3. Run the setup.sh script:

      ```
      $ ./setup.sh

      + mkdir -p build
      + find ../.. '!' -name .. '!' -name samples '!' -name docker -maxdepth 1 -exec cp -R '{}' build/ ';'
      + cp ../../docker/amster-install.sh ../../docker/docker-entrypoint.sh ../../docker/export.sh ../../docker/tar.sh build
      ```

   4. Edit the Dockerfile in the samples/docker directory. Change the line:

      ```
      FROM gcr.io/forgerock-io/java-...:latest
      ```

      to:

      ```
      FROM my-repo/my-java
      ```

   5. Build the `amster` Docker image:

      ```
      $ docker build --tag amster:8.1.0 .

       ⇒ [internal] load build definition from Dockerfile
      ...
       ⇒ [1/8] FROM docker.io/my-repo/my-java
      ...
       ⇒ exporting to image
       ⇒ ⇒ exporting layers
       ⇒ ⇒ writing image sha256:bc47...f9e52                       0.0s
       ⇒ ⇒ naming to docker.io/library/amster:8.1.0
      ```

7. Build the empty AM image:

   1. Unzip the AM `.zip` file.

   2. Change to the openam/samples/docker directory in the expanded `.zip` file output.

   3. Change to the images/am-empty directory.

   4. Build the `am-empty` Docker image:

      ```
      $ docker build --tag am-empty:8.1.0 .

       ⇒ [internal] load build definition from Dockerfile                                                                                          0.0s
       ⇒ ⇒ transferring dockerfile: 3.60kB                                                                                                         0.0s
       ⇒ [internal] load .dockerignore                                                                                                             0.0s
       ⇒ ⇒ transferring context: 2B                                                                                                                0.0s
       ⇒ [internal] load metadata for docker.io/library/tomcat:9-jdk17-openjdk-slim-bullseye                                                       1.8s
       ⇒ [internal] load build context                                                                                                             5.6s
       ⇒ ⇒ transferring context: 231.59MB                                                                                                          5.6s
       ⇒ [base  1/14] FROM docker.io/library/tomcat:9-jdk17-openjdk-slim-bullseye@...
      ...
       ⇒ exporting to image                                                                                                                        1.7s
       ⇒ ⇒ exporting layers                                                                                                                        1.6s
       ⇒ ⇒ writing image sha256:9784a73...1d36018c9                                                                                                0.0s
       ⇒ ⇒ naming to docker.io/library/am-empty:8.1.0
      ```

8. Build the base image for AM:

   1. Change to the ../am-base directory.

   2. Edit the Dockerfile in the ../am-base directory and change the line:

      ```
      FROM ${docker.push.repo}/am-empty:${docker.tag}
      ```

      to:

      ```
      FROM am-empty:8.1.0
      ```

   3. Build the `am-base` Docker image:

      ```
      $ docker build --tag am-base:8.1.0 .

       ⇒ [internal] load build definition from Dockerfile                                                               0.0s
       ⇒ ⇒ transferring dockerfile: 2.72kB                                                                              0.0s
       ⇒ [internal] load .dockerignore                                                                                  0.0s
       ⇒ ⇒ transferring context: 2B                                                                                     0.0s
       ⇒ [internal] load metadata for docker.io/library/amster:8.1.0                                                    0.0s
       ⇒ [internal] load metadata for docker.io/library/am-empty:8.1.0                                                  0.0s
       ⇒ [internal] load build context                                                                                  0.4s
       ⇒ ⇒ transferring context: 35.66MB                                                                                0.4s
       ⇒ [generator  1/15] FROM docker.io/library/am-empty:8.1.0                                                        0.4s
       ⇒ [amster 1/1] FROM docker.io/library/amster:8.1.0                                                               0.2s
       ⇒ [generator  2/15] RUN apt-get update -y &&     apt-get install -y git jq unzip
      ...
       ⇒ [am-base  7/11] COPY --chown=forgerock:root docker-entrypoint.sh /home/forgerock/                              0.0s
       ⇒ [am-base  8/11] COPY --chown=forgerock:root scripts/import-pem-certs.sh /home/forgerock/                       0.0s
       ⇒ [am-base  9/11] RUN rm "/usr/local/tomcat"/webapps/am/WEB-INF/lib/click-extras-*.jar                           0.2s
       ⇒ [am-base 10/11] RUN rm "/usr/local/tomcat"/webapps/am/WEB-INF/lib/click-nodeps-*.jar                           0.3s
       ⇒ [am-base 11/11] RUN rm "/usr/local/tomcat"/webapps/am/WEB-INF/lib/velocity-*.jar                               0.2s
       ⇒ exporting to image                                                                                             0.2s
       ⇒ ⇒ exporting layers                                                                                             0.2s
       ⇒ ⇒ writing image sha256:2c06...87c6c                                                                            0.0s
       ⇒ ⇒ naming to docker.io/library/am-base:8.1.0
      ```

   4. Change to the ../am-cdk directory.

   5. Edit the Dockerfile in the ../am-cdk directory. Change the line:

      ```
      FROM ${docker.push.registry}/forgerock-io/am-base/${docker.promotion.folder}:${docker.tag}
      ```

      to:

      ```
      FROM am-base:8.1.0
      ```

   6. Build the `am` Docker image:

      ```
      $ docker build --tag my-repo/am:8.1.0 .
      [+] Building 5.1s (10/10) FINISHED                                                                 docker:desktop-linux
       ⇒ [internal] load build definition from Dockerfile                                                               0.0s
       ⇒ ⇒ transferring dockerfile: 1.71kB                                                                              0.0s
       ⇒ [internal] load .dockerignore                                                                                  0.0s
       ⇒ ⇒ transferring context: 2B                                                                                     0.0s
       ⇒ [internal] load metadata for docker.io/library/am-base:8.1.0                                                   0.0s
       ⇒ [1/5] FROM docker.io/library/am-base:8.1.0                                                                     0.2s
       ⇒ [internal] load build context                                                                                  0.2s
       ⇒ ⇒ transferring context: 403.07kB                                                                               0.1s
       ⇒ [2/5] RUN apt-get update         && apt-get install -y git         && apt-get clean         && rm -r /var/lib  3.9s
       ⇒ [3/5] RUN cp -R /usr/local/tomcat/webapps/am/XUI /usr/local/tomcat/webapps/am/OAuth2_XUI                       0.3s
       ⇒ [4/5] COPY --chown=forgerock:root /config /home/forgerock/cdk/config                                           0.0s
       ⇒ [5/5] RUN rm -rf /home/forgerock/openam/config/services &&     mkdir /home/forgerock/openam/config/services    0.5s
       ⇒ exporting to image                                                                                             0.1s
       ⇒ ⇒ exporting layers                                                                                             0.1s
       ⇒ ⇒ writing image sha256:14b43fb5121cee08341130bf502b7841429b057ff406bbe635b23119a74dec45                        0.0s
       ⇒ ⇒ naming to my-repo/am:8.1.0                                                                                   0.0s
      ```

9. Now that the AM image is built, tag the base image for Amster in advance of pushing it to your private repository:

   ```
   $ docker tag amster:8.1.0 my-repo/amster:8.1.0
   ```

10. Build the `am-config-upgrader` base image:

    1. Change to the `openam` directory in the expanded AM `.zip` file output.

    2. Unzip the `Config-Upgrader-8.1.0.zip` file.

    3. Change to the `amupgrade/samples/docker` directory in the expanded `Config-Upgrader-8.1.0.zip` file output.

    4. Edit the Dockerfile in the amupgrade/samples/docker directory and change line 16 from:

       ```
       FROM gcr.io/forgerock-io/java-17:latest
       ```

       to:

       ```
       FROM my-repo/my-java
       ```

    5. Run the setup.sh script:

       ```
       $ ./setup.sh

       + mkdir -p build/amupgrade
       + find ../.. '!' -name .. '!' -name samples '!' -name docker -maxdepth 1 -exec cp -R '{}' build/amupgrade ';'
       + cp ../../docker/docker-entrypoint.sh .
       ```

    6. Create the base `am-config-upgrader` image:

       ```
       $ docker build --tag my-repo/am-config-upgrader:8.1.0 .

       [+] Building 8.5s (9/9) FINISHED                                  docker:desktop-linux
        ⇒ [internal] load build definition from Dockerfile                               0.0s
        ⇒ ⇒ transferring dockerfile: 1.10kB                                              0.0s
        ⇒ [internal] load .dockerignore                                                  0.0s
        ⇒ ⇒ transferring context: 2B                                                     0.0s
        ⇒ [internal] load metadata for my-repo/my-java:latest                            0.0s
        ⇒ CACHED [1/4] FROM my-repo/my-java                                              0.0s
        ⇒ [internal] load build context                                                  0.3s
        ⇒ ⇒ transferring context: 20.58MB                                                0.3s
        ⇒ [2/4] RUN apt-get update &&     apt-get upgrade -y                             8.3s
        ⇒ [3/4] COPY --chown=forgerock:root docker-entrypoint.sh /home/forgerock/        0.0s
        ⇒ [4/4] COPY build/ /home/forgerock/                                             0.0s
        ⇒ exporting to image                                                             0.1s
        ⇒ ⇒ exporting layers                                                             0.1s
        ⇒ ⇒ writing image sha256:3f6845…​44011                                            0.0s
        ⇒ ⇒ naming to my-repo/am-config-upgrader:8.1.0                                   0.0s
       ```

11. Build the base image for DS:

    1. Unzip the DS `.zip` file.

    2. Change to the opendj directory in the expanded `.zip` file output.

    3. Run the samples/docker/setup.sh script to create a server:

       ```
       $ ./samples/docker/setup.sh

       + rm -f template/config/tools.properties
       + cp -r samples/docker/Dockerfile samples/docker/README.md ...
       + rm -rf — README README.md bat '*.zip' opendj_logo.png setup.bat upgrade.bat setup.sh
       + ./setup --serverId docker --hostname localhost
       ...

       Validating parameters... Done
       Configuring certificates... Done
       ...
       ```

    4. Edit the Dockerfile in the opendj directory. Change the line:

       ```
       FROM gcr.io/forgerock-io/java-...:latest
       ```

       to:

       ```
       FROM my-repo/my-java
       ```

    5. Build the `ds` base image:

       ```
       $ docker build --tag my-repo/ds:8.1.0 .

       [+] Building 11.0s (9/9) FINISHED

        ⇒ [internal] load build definition from Dockerfile                                                                                          0.0s
        ⇒ ⇒ transferring dockerfile: 1.23kB                                                                                                         0.0s
        ⇒ [internal] load .dockerignore                                                                                                             0.0s
        ⇒ ⇒ transferring context: 2B                                                                                                                0.0s
        ⇒ [internal] load metadata for my-repo/my-java:latest                                                                                       1.7s
        ⇒ [internal] load build context                                                                                                             1.2s
        ⇒ ⇒ transferring context: 60.85MB                                                                                                           1.2s
        ⇒ CACHED [1/4] FROM my-repo/my-java:latest
       ...
        ⇒ [4/4] WORKDIR /opt/opendj                                                                                                                 0.0s
        ⇒ exporting to image                                                                                                                        0.4s
        ⇒ ⇒ exporting layers                                                                                                                        0.3s
        ⇒ ⇒ writing image sha256:713ac...b107e0f                                                                                                    0.0s
        ⇒ ⇒ naming to my-repo/ds:8.1.0
       ```

12. []()Build the base image for IDM:

    1. Create a new shell script file named build-idm-image.sh and copy the following lines into it:

       ```none
       #!/bin/bash

       if [ $# -lt 3 ]; then
         echo "$0 <source image> <new base image> <result image>"
         exit 0
       fi

       sourceImage="$1"
       javaImage="$2"
       resultImage="$3"

       container_id=$(docker create $sourceImage)
       docker export $container_id -o image.tar
       docker rm $container_id

       tar xvf image.tar opt/openidm
       rm -f image.tar

       cd opt/openidm
       # use | separators because image names often have / and :
       sed -i.bak 's|^FROM.*$|FROM '$javaImage'|' bin/Custom.Dockerfile
       rm bin/Custom.Dockerfile.bak

       docker build . --file bin/Custom.Dockerfile --tag "$resultImage"
       rm -rf opt
       ```

    2. Change the mode of the file to be executable and run it.

       ```
       $ chmod +x build-idm-image.sh
       $ ./build-idm-image.sh docker.pkg.dev/forgeops-public/images-base/idm:8.1.0 my-repo/my-java my-repo/idm:8.1.0
       ```

       |   |                                                                                                          |
       | - | -------------------------------------------------------------------------------------------------------- |
       |   | The build-idm-image.sh script expands the IDM Docker image, rebuilds the image, and cleans up afterward. |

13. (Optional) Build the base image for PingGateway:

    1. Unzip the PingGateway `.zip` file.

    2. Change to the identity-gateway directory in the expanded `.zip` file output.

    3. Edit the Dockerfile in the identity-gateway/docker directory. Change the line:

       ```
       FROM gcr.io/forgerock-io/java-...:latest
       ```

       to:

       ```
       FROM my-repo/my-java
       ```

    4. Build the `ig` base image:

       ```
       $ docker build . --file docker/Dockerfile --tag my-repo/ig:2026.3.0

       [+] Building 2.1s (8/8) FINISHED
       ⇒ [internal] load build definition from Dockerfile                                                                                          0.0s
        ⇒ ⇒ transferring dockerfile: 1.43kB                                                                                                        0.0s
        ⇒ [internal] load .dockerignore                                                                                                            0.0s
        ⇒ ⇒ transferring context: 2B                                                                                                               0.0s
        ⇒ [internal] load metadata for my-repo/my-java:latest                                                                                      0.3s
        ⇒ [internal] load build context                                                                                                            2.2s
        ⇒ ⇒ transferring context: 113.60MB                                                                                                         2.2s
        ⇒ CACHED [1/3] FROM my-repo/my-java:latest
        ⇒ [2/3] COPY --chown=forgerock:root . /opt/ig                                                                                              0.7s
        ⇒ [3/3] RUN mkdir -p "/var/ig"     && chown -R forgerock:root "/var/ig" "/opt/ig"     &&  -R g+rwx "/var/ig" "/opt/ig"                     0.9s
        ⇒ exporting to image                                                                                                                       0.6s
        ⇒ ⇒ exporting layers                                                                                                                       0.6s
        ⇒ ⇒ writing image sha256:77fc5...6e63                                                                                                      0.0s
        ⇒ ⇒ naming to my-repo/ig:2026.3.0
       ```

14. Run the docker images command to verify that you built the base images:

    ```
    $ docker images | grep my-repo

    REPOSITORY                   TAG      IMAGE ID        CREATED        SIZE
    my-repo/am                   8.1.0    552073a1c000    1 hour ago     795MB
    my-repo/am-config-upgrader   8.1.0    d115125b1c3f    1 hour ago     795MB
    my-repo/amster               8.1.0    d9e1c735f415    1 hour ago     577MB
    my-repo/ds                   8.1.0    ac8e8ab0fda6    1 hour ago     196MB
    my-repo/idm                  8.1.0    0cc1b7f70ce6    1 hour ago     387MB
    my-repo/ig                   2026.3.0 cc52e9623b3c    1 hour ago     249MB
    my-repo/java-...             latest   a504925c2672    1 hour ago     144MB
    ```

15. Push the new base Docker images to your Docker repository.

    Refer to your registry provider documentation for detailed instructions. For most Docker registries, you run the docker login command to log in to the registry. Then, you run the docker push command to push a Docker image to the registry.

    Be sure to configure your Docker registry so that you can successfully push your Docker images. Each cloud-based Docker registry has its own specific requirements. For example, on Amazon ECR, you must create a repository for each image.

    Push the following images to your repository:

    * `my-repo/am:8.1.0`

    * `my-repo/am-config-upgrader:8.1.0`

    * `my-repo/amster:8.1.0`

    * `my-repo/ds:8.1.0`

    * `my-repo/idm:8.1.0`

    * `my-repo/my-java`

    If you're deploying your own PingGateway base image, also push the `my-repo/ig:2026.3.0` image.

#### Create Docker images for use in production

After you've [built and pushed your own base images](#base-images) to your Docker registry, you're ready to build customized Docker images that can be used in a production deployment of the Ping Advanced Identity Software. These images:

* Contain customized [configuration profiles](customize/fr-data.html#configuration-profiles) for AM, IDM, and, optionally, PingGateway.

* Must be based on [your own base Docker images](#base-images).

Create your production-ready Docker images, create a Kubernetes cluster to test them, and delete the cluster when you've finished testing the images:

1. Clone the `forgeops` repository.

2. Obtain custom configuration profiles that you want to use in your Docker images from your developer, and copy them into your `forgeops` repository clone:

   * Obtain the AM configuration profile from the /path/to/forgeops/docker/am/config-profiles directory.

   * Obtain the IDM configuration profile from the /path/to/forgeops/docker/idm/config-profiles directory.

   * (Optional) Obtain the PingGateway configuration profile from the /path/to/forgeops/docker/ig/config-profiles directory.

3. Change the `FROM` lines of Dockerfiles in the `forgeops` repositories to refer to your own base Docker images:

   | In the `forgeops` repository file: | Change the `FROM` line to:                                          |
   | ---------------------------------- | ------------------------------------------------------------------- |
   | docker/am/Dockerfile               | `FROM my-repo/am:8.1.0` \[[24](#_footnotedef_24 "View footnote.")]  |
   | docker/amster/Dockerfile           | `FROM my-repo/amster:8.1.0`                                         |
   | docker/ds/ds-new/Dockerfile        | `FROM my-repo/ds:8.1.0`                                             |
   | docker/idm/Dockerfile              | `FROM my-repo/idm:8.1.0` \[[25](#_footnotedef_25 "View footnote.")] |
   | (Optional) docker/ig/Dockerfile    | `FROM my-repo/ig:2026.3.0`                                          |

4. If necessary, log in to your Docker registry.

5. Enable the Python3 virtual environment:

   ```
   $ source .venv/bin/activate
   ```

6. Set up a ForgeOps deployment environment:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops env --env-name my-env --fqdn my-fqdn --cluster-issuer my-cluster-issuer
   ```

   In the command above, replace my-fqdn and my-cluster-issuer with appropriate values from your environment. If you want to use the issuer provided with the platform for demo, then you can use default-issuer.

7. Build Docker images that are based on your own base images.

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | While the forgeops build command uses the Docker engine by default for ForgeOps deployments, it supports Podman as well. If you are using Podman engine instead of Docker in your environment, then set the `CONTAINER_ENGINE` environment variable to `podman` before running the forgeops build command, for example:```
   $ export CONTAINER_ENGINE="podman"
   ``` |

   The AM and IDM images contain your customized configuration profiles:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops build --env-name my-env ds --push-to my-repo --tag my-tag
   $ ./forgeops build --env-name my-env amster --push-to my-repo --tag my-tag
   $ ./forgeops build --env-name my-env am --push-to my-repo --tag my-tag --config-profile my-profile
   $ ./forgeops build --env-name my-env idm --push-to my-repo --tag my-tag --config-profile my-profile
   ```

   The forgeops build command:

   * Builds Docker images. The AM and IDM images incorporate customized configuration profiles.

   * Pushes Docker images to the repository specified in the --push-to argument.

   * Updates the image defaulter file, which the forgeops apply command uses to determine which Docker images to run.

8. (Optional) Build and push an PingGateway Docker image that's based on your own base image and contains your customized configuration profile:

   ```
   $ ./forgeops build --env-name my-env ig --config-profile my-profile --push-to my-repo
   ```

9. Prepare a Kubernetes cluster to test your images:

   1. Create the cluster. This example assumes that you create a cluster suitable for a small-sized ForgeOps deployment.

   2. Make sure your cluster can [access and pull Docker images](https://kubernetes.io/docs/concepts/containers/images/#configuring-nodes-to-authenticate-to-a-private-registry) from your repository.

   3. Create a namespace in the new cluster, and then make the new namespace the active namespace in your local Kubernetes context.

10. Perform a ForgeOps deployment in your cluster:

    ```
    $ cd /path/to/forgeops/bin
    $ ./forgeops apply --env-name my-env --fqdn my-fqdn --namespace my-namespace
    ```

11. Access the AM admin UI and verify that your customized configuration profiles are active.

12. Delete the Kubernetes cluster that you used to test images.

At the end of this process, the artifacts that you'll need to deploy the Ping Advanced Identity Software in production are available:

* Docker images for the Ping Advanced Identity Software, in your Docker repository

* An updated image defaulter file, in your `forgeops` repository clone

You'll need to copy the image defaulter file to your production deployment, so that when you run the forgeops apply command, it will use the correct Docker images.

Typically, you model the image creation process in a CI/CD pipeline. Then, you run the pipeline at milestones in the development of your customized configuration profile.

### The forgeops command

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | forgeops — The new generation utility replaces the previous version of `forgeops`. The new forgeops utility simplifies deploying and managing Ping Advanced Identity Software components in a Kubernetes cluster.**The previous version of the forgeops utility is not supported in this ForgeOps release. It continues to be supported in ForgeOps 7.5 and 7.4, as long as the corresponding Ping Advanced Identity Software components are supported.** |

You can create and manage custom overlays and Helm values files for each deployment. You can then apply the overlays or value files appropriately using Kustomize or Helm accordingly.

The forgeops utility lets you:

* Use Kustomize natively so you can update and use overlays as expected.

* Generate a Kustomize overlay manually when you need the overlay.

* Generate Helm value files from the same environment set up.

* Build and manage Docker images per overlay to allow different images in an environment.

* Create and manage each ForgeOps deployment configuration.

* Apply the environment configuration changes using either Kustomize or Helm.

#### Features in forgeops

##### Discrete overlays

The current forgeops command has the following limitations:

* It generates a Kustomize overlay every time it runs.

* It overwrites any post-deployment changes in Kustomize overlays.

* It uses the preconfigured patch files and ignores the customizations during deployment.

The forgeops command doesn't generate overlay files automatically. Instead, overlay files are manually generated as needed.

It is recommended to create an overlay for each environment, such as `test`, `stage`, and `prod`. It is also recommended to create an overlay for each single-instance environment, such as `test-single`, `stage-single`, and `prod-single`. The single-instance overlays help you develop file-based configuration changes, export them, and build new images.

##### `image-defaulter` in every overlay

Each overlay includes an `image-defaulter` component. When using Kustomize, you can develop and build and test custom images in your single-instance environment. Once you are satisfied with the image, you can copy the image-defaulter's `kustomization.yaml` file into your running overlay.

##### Sub-overlays

To install and delete individual components, ForgeOps provided overlays are composed of sub-overlays. Each Ping Advanced Identity Software product has its own overlay. There are other overlays to handle shared pieces. You can apply or delete sub-overlay or the entire overlay using `kubectl apply -k` or `kubectl delete -k` commands.

##### Specify overlay or environment to target

With discrete overlays, you need to specify which overlay you want to target when running the `forgeops` commands. If you forget to specify the overlay, the command exits and lets you know to provide one. Only the apply and info commands allow you to not specify an overlay.

##### Helm Support

Both Kustomize and Helm are supported by the forgeops command. Use the forgeops env command to generate Helm `values` file and Kustomize overlays for existing environments. The forgeops build command updates the Helm `values` file and the Kustomize `image-defaulter` overlay file for the specified environment.

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The forgeops command can generate the `values.yaml` file from an already deployed environment, it cannot generate the `values.yaml` file for a new environment. |

The `values.yaml` file contains all the Helm values. While the `values.yaml` file contains all the Helm values for an environment, few more files are created each containing a group of interrelated values that can be copied and used in other environments, if you need to.

#### Setup

The forgeops command is developed using Python. Run the forgeops configure command to ensure the required packages are set up:

```
$ cd /path/to/forgeops/bin
$ ./forgeops configure
```

You need to run the forgeops configure once before creating and managing your ForgeOps deployment environments.

#### Workflow

The workflow of `forgeops` is designed to be production first and has three distinct steps:

* [1. Create an environment](#create-env)

  This step is used to manage the overlay and values files on an ongoing basis. Only the requested changes are incorporated, so the customizations are not impacted.

* [2. Build images for the environment](#build-env)

  The `build` step assembles the file-based configuration changes into container images, and updates the `image-defaulter` and `values` files for the targeted environment.

* [3. Apply the environment](#apply-env)

  In this step, you deploy the image you configured.

|   |                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It is recommended that you start with a single-instance deployment to develop your AM and IDM configuration, so you can export them and build your custom container images. |

##### 1. []()Create an environment

You must create an environment first using the forgeops env command. You need to specify an FQDN (`--fqdn`) and an environment name (`--env-name`).

Previously, the t-shirt sized overlays called `small`, `medium`, and `large` were provided, along with the default overlay `cdk`. With `forgeops`, a `single-instance` overlay replaces `cdk`. The `single-instance` overlay is considered the default and is provided in the kustomize-ng/overlay/default directory.

You can use `--small`, `--medium`, and `--large` flags to configure your overlay, and the forgeops env command populates your environment with the size you requested.

For example, the following command creates a medium-sized stage deployment with an FQDN of stage.example.com:

```
$ cd /path/to/forgeops
$ ./bin/forgeops env --fqdn stage.example.com --medium --env-name stage
```

The default deployment size is `single-instance`. The following example command creates a single-instance environment:

```
$ cd /path/to/forgeops
$ ./bin/forgeops env --fqdn stage.example.com --env-name stage-single
```

You will find the generated Kustomize overlay files in the kustomize-ng/overlay/ENV-NAME folder. If you are modifying an existing Helm-based environment, then you will also find the Helm specific value files in the charts/identity-platform folder.

##### 2. []()Build images for the environment

Use the forgeops build command to create a new container image for the environment you created in the [Create an environment](#create-env) step. The forgeops build command applies the config profile from the build docker/am/config-profiles/profile and docker/idm/config-profiles/profile to build AM and IDM container images and push the images to your container registry. It also updates the `image-defaulter` and `values` files for the targeted environment.

To build new AM and IDM images for our stage environment using the stage-cfg profile, run the command:

```
$ ./bin/forgeops build --env-name stage \
 --config-profile stage-cfg \
 --push-to my.registry.com/my-repo/stage am idm
```

##### 3. []()Apply the environment

Use the overlay you created in the [Create an environment](#create-env) step and deploy the environment built in the [Build images for the environment](#build-env) step.

* Kustomize-based deployment

  You have two options to perform ForgeOps deployment in a Kustomize-based environment:

  * Using the kubectl apply command, for example:

    ```
    $ kubectl apply -k /path/to/forgops/kustomize-ng/overlay/my-overlay
    ```

  * Using the forgeops apply command, for example:

    ```
    $ ./bin/forgeops apply --env-name stage
    ```

|   |                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are using Helm-based deployment methods, you cannot use the forgeops command to perform ForgeOps deployment. Instead, use the helm install or helm upgrade command with the Helm values file:```
$ helm upgrade --install ...
``` |

#### `forgeops` commands

The forgeops command is a Bash wrapper script that calls appropriate scripts in `bin/commands`. These scripts are written in either Bash or Python. All the bash scripts support the new `--dryrun` flag which display the command that would be run and enable you to inspect it before actually running the command. The Python scripts `env` and `info` do not support `--dryrun`.

* Helm Support

  Both Kustomize and Helm are supported by the forgeops command. Use the forgeops env command to generate Helm `values` files and Kustomize overlays for each environment. The forgeops build command updates the Helm `values` file and the Kustomize `image-defaulter` overlay file for the specified environment.

  The `values.yaml` file contains all the Helm values. The other files group the different values so that you can use them individually if you need to.

* Custom paths

  By default, forgeops uses the `docker`, `kustomize`, and `helm` directories. You can set up your own locations separately and specify the appropriate flags on the command line or set the appropriate environment variable in the path/to/forgeops/forgeops.conf file.

Learn more about the forgeops command options in the [forgeops command reference](reference/forgeops-cmd-ref.html).

#### forgeops command reference

forgeops — The new generation utility simplifies deploying and managing Ping Advanced Identity Software components in a Kubernetes cluster. You can create and manage custom Kustomize overlays and Helm value files for each deployment. You can then apply the customized overlays or value files using Kustomize or Helm appropriately.

To get help in the command-line interface, use the forgeops --help command. Some of the important subcommands are described in this section. You can also get help on the forgeops subcommands using forgeops subcommand --help.

##### Synopsis

forgeops subcommand options

##### Description

* Generate custom component overlays and value files.

* Use Kustomize or Helm to install Ping Advanced Identity Software components in a Kubernetes cluster.

* Delete platform components from a Kubernetes cluster.

* Build custom Docker images for the Ping Advanced Identity Software.

##### Options

The forgeops command takes the following option:

* `--help`

  Display command usage information.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following subcommands `clean`, `config`, `install`, and `generate` have been deprecated because their functionality is provided through other existing subcommands. |

##### Subcommands

###### forgeops apply

forgeops apply components options

Runs the `kubectl apply -k` command to apply Ping Advanced Identity Software Kustomize overlay from the specified overlay directory into a Kubernetes namespace. If the specified overlay directory doesn't exist, a new one is created.

* The `forgeops apply` subcommand subsumes all the functionality of `forgeops install`. Accordingly, `forgeops install` is deprecated.

For components, specify:

* `am`, `amster`, `ds-cts`, `ds-idrepo`, `idm`, or `ig` to deploy each Ping Advanced Identity Software component.

* More than one component or set of components separated by a space to deploy multiple Ping Advanced Identity Software components. For example, forgeops apply ds-idrepo ds-cts am.

* `secrets` to deploy Kubernetes secrets. Secrets generated by cert-manager are not deployed.

* `base` to deploy the `platform-config` configmap Kubernetes ingress resources and Kubernetes secrets. Secrets generated by cert-manager are not deployed.

* `all` to deploy all the Ping Advanced Identity Software components.

The default value for components is `all`.

[](#options_2)Options

The forgeops apply subcommand takes the following options:

* `--create-namespace`

  Create a namespace if it doesn't exist. The default is the current namespace of the user.

* `--debug`

  Display debug information when executing the command.

* `--dryrun`

  To perform a dry run without actually applying or installing the components.

* `--env-name` my-env

  Name of environment to apply. The default is `demo`.

* `--fqdn` my-fqdn

  The fully qualified hostname to use in the deployment.

  * The namespace specified in the forgeops env command is used by default. For simple demo purposes, the namespace specified in the default overlay file is used.

  * Relevant only for the forgeops apply all and forgeops apply base commands. This option is ignored for other forgeops apply commands.

* `--namespace` ns

  The namespace in which to install the ForgeOps platform components. If you need to create the namespace, then specify the `--create-namespace | -c` option.

* `--kustomize` my-kustomize-path

  The directory that contains Kustomize overlays. Specify the full path to the directory or the path relative to the base of your local `forgeops` repository. The default value is `kustomize`.

[](#examples)Examples

* Use an environment my-env

  forgeops apply --env-name my-env

* Do a dry run

  forgeops apply --dryrun --env-name my-env

###### forgeops build

forgeops build --env-name my\_env components options

Use the forgeops build command to build custom Docker images for one or more Ping Advanced Identity Software components, and update the Helm `values` file and the Kustomize `image-defaulter` overlay file for the specified environment.

|   |                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Building an `amster` image is not supported, so use bin/forgeops amster.

* The `--config-profile` option is applicable only for AM, idm\_abbr, and PingGateway.

* Use the `--push-to` option or set the PUSH\_TO variable in your environment.

* Use the `--push-to none` option for building local images in minikube. |

For components, specify:

* `am`, `ds`, `idm`, or `ig` to build a custom Docker image for a single Ping Advanced Identity Software component.

* More than one component or set of components separated by a space to build multiple Docker images in a single forgeops build command. For example, forgeops build --env-name \[.var]#my-env am idm#.

* `all` to build Docker images for all the Ping Advanced Identity Software components\[[26](#_footnotedef_26 "View footnote.")] by running a single forgeops build command.

[](#options_3)Options

In addition to the global forgeops command options, the forgeops build subcommand takes the following options:

* `--build-path path`

  The directory path where the build images are to be located. By default, the images are placed in path/to/forgeops/docker.

* `--config-profile config-profile-path`

  Path that contains the configuration for `am`, `idm`, or `ig`. The forgeops build command incorporates the configuration files located in this path in the custom Docker image it builds.

  Configuration profiles reside in subdirectories of one of these paths in a `forgeops` repository clone:

  * docker/am/config-profiles

  * docker/idm/config-profiles

  * docker/ig/config-profiles

  Learn more in [Configuration profiles](customize/fr-data.html#configuration-profiles).

  Customized `ds` images do not use configuration profiles. To customize the `ds` image, add customizations to the docker/ds directory before running the forgeops build ds command.

* `--debug`

  Display debug information when executing the command.

* `--dryrun`

  To perform a dry run without actually building the component images.

* `--env-name my-env`

  The name of the deployment environment that is used for building or deploying the image. Deployment environments let you manage deployment manifests and image defaulters.

  You must initialize new deployment environments before using them for the first time. You must specify the `--env-name` option in the `forgeops build` command if you haven't set up the `ENV_NAME` shell environment variable.

  The forgeops build command updates the image defaulter in the target environment. For example, if you ran forgeops build --env-name prod, the image defaulter in the kustomize/overlay/deploy-prod/image-defaulter directory would be updated.

* `--kustomize`

  The path to the directory where the Kustomize overlays and the image defaulter files for the environment are located. You can specify the full path or path relative to the local directory of your `forgeops` repository clone.

* `--push-to registry`

  Docker registry where the Docker image being built is pushed. You must specify the `push-to` option unless you've set the `PUSH_TO` environment variable.

  For deployments on minikube, specify `--push-to none` to push the Docker image to the Docker instance running within minikube.

  If you specify both the `--push-to` option and the `PUSH_TO` environment variable, the value of the `--push-to` option takes precedence.

* `--reset`

  Revert all the tags and new image names in the image defaulter file to their last committed values.

* `--tag my-tag`

  Tag to apply to the Docker image being built.

[](#examples_2)Examples

* Normal operation

  forgeops build --config-profile prod --env-name prod --tag prod-am-123 am

* Do a dry run

  forgeops build --config-profile prod --env-name prod --dryrun am

###### forgeops delete

forgeops delete --env-name my-env \<components> \<options>

Delete Ping Advanced Identity Software components or sets of components, PVCs, volume snapshots, and Kubernetes secrets from a running Kustomize-based ForgeOps deployment.

By default, the forgeops delete command prompts you to confirm if you want to delete PVCs, volume snapshots, and Kubernetes secrets. You can suppress confirmation prompts as necessary by using the `--yes` option. For example, forgeops delete --env-name test --yes, deletes all Ping Advanced Identity Software components in the `test` environment.

For components, specify:

* `am`, `ds-cts`, `ds-idrepo`, `idm`, or `ig` to delete a single Ping Advanced Identity Software component.

* `secrets` to delete the Kubernetes secrets from the deployment.

  * `base` to delete the `platform-config` configmap, Kubernetes ingress resources, and Kubernetes secrets. Secrets generated by cert-manager are not deleted.

* `all` to delete all the Ping Advanced Identity Software components.

* More than one component or set of components separated by a space to delete multiple Ping Advanced Identity Software components. For example, forgeops delete --env-name my-env am idm.

The default value for components is `all`.

[](#options_4)Options

The forgeops delete subcommand takes the following options:

* `--debug`

  Display debug information when executing the command.

* `--dryrun`

  To perform a dry run without actually deleting the components.

* `--env-name my-env`

  The name of the deployment environment that contains the Kustomization overlays. You must specify the `--env-name` option, otherwise the forgeops delete command fails to run.

* `--force`

  When deleting Ping Advanced Identity Software components, also delete PVCs, volume snapshots, and Kubernetes secrets.

  When you specify this option, you still receive the `OK to delete components?` confirmation prompt. Specify the --yes option together with --force to suppress this confirmation prompt.

* `--namespace my-namespace`

  The namespace from which to delete Ping Advanced Identity Software components.

  Defaults to the active namespace in your local Kubernetes context.

* `--yes`

  Suppress all confirmation prompts.

  When you specify this option, PVCs, volume snapshots, and Kubernetes secrets are not deleted. Specify the --force option together with --yes to delete PVCs, volume snapshots, and Kubernetes secrets.

[](#examples_3)Examples

* Normal operation

  forgeops delete --env-name prod am

* Do a dry run

  forgeops delete --env-name prod am --dryrun

###### forgeops env

The forgeops env command enables you to set up a ForgeOps deployment environment with parameters such as FQDN, ingress, and secret management tool.

[](#command_details)Command details

forgeops env --env-name my-env OPTION

Create, configure, and manage a ForgeOps deployment environment. This command lets you define the parameters for your deployment environment, such as FQDN, certificate issuer, and so on by configuring:

* Kustomize overlay files for each component in the /path/to/forgeops/kustomize/overlay/my-env directory.

* A Helm values file in the /path/to/forgeops/helm/my-env directory.

By unifying the parameters in a location, you don't have to specify these parameters when using the other commands, such as `forgeops apply`, `forgeops build`, and so on.

[](#options_5)Options

* `--amster-retain` n

  Keep the `amster` pod running for n seconds. The default is 10 seconds.

* `--fqdn` my-fqdn

  A comma separated list of FQDNs. For example:

  forgeops env --env-name my-env --fqdn my-fqdn1, my-fqdn2

  This is a mandatory parameter. Default: None.

* `--helm path/to/helm/directory`

  The directory where Helm values files are located. The directory path can be relative to the `forgeops` root directory or an absolute path.

* `--ingress my-ingress`

  Ingress class name.

  Default: None.

* `--kustomize my/kustomize`

  The directory that contains Kustomize overlays. The directory path can be an absolute or relative to the `forgeops` root directory.

* `--namespace my-namespace`

  The Kubernetes namespace where the Ping Advanced Identity Software components are deployed.

  Default: None.

* `--no-namespace`

  Remove namespace from Kustomize overlay.

  Default: False.

* `--env-name my-env`

  Name of environment to manage.

  Default: None.

* `--secret-agent`

  To enable the secret agent as the secret management utility.

  Default: `--secret-agent` is enabled.

* `--single-instance`

  To use a `single-instance` configuration. In a minikube environment, you must use the `single-instance` configuration option.

  Default: False.

* `--source my-kust-source`

  Name of the source Kustomize overlay.

  Default: None.

* `--ssl-secretname my-ssl-secret`

  Name of the secret containing private SSL data.

  Default: None

* `--am-cpu, --am-mem, --am-rep`

  Specify the CPU, memory, and the number of AM pod replicas.

* `--cts-cpu, --cts-disk, --cts-mem, --cts-rep, --cts-snap-enable`

  Specify CPU, disk size, memory, replicas, and volume snapshots for `ds-cts` pods.

* `--idm-cpu --idm-mem --idm-rep`

  Specify the CPU, memory, and the number of IDM pod replicas.

* `--idrepo-cpu, --idrepo-disk, --idrepo-mem, --idrepo-rep, --idrepo-snap-enable`

  Specify CPU, disk size, memory, replicas, and enable volume snapshots for `ds-idrepo` pods.

* `--pull-policy my-pull-policy`

  Set policy for all platform images.

* `--no-helm`

  Don't create or manage Helm values files.

  Default: False.

* `--no-kustomize`

  Don't create or manage Kustomize overlay.

  Default: False.

* `--small`, `--medium`, or `--large`

  The size of ForgeOps deployment used in the environment.

  Default: None.

* `--issuer my-issuer`

  The TLS certificate issuer within the namespace where the ForgeOps components are to be deployed.

  Default: None.

* `--cluster-issuer my-cluster-issuer`

  The TLS certificate issuer that is available across the Kubernetes cluster where ForgeOps components are to be deployed. For demo purposes, you can use the certificate sample certificate issuer provided with ForgeOps, by using the `--cluster-issuer default-issuer`.

  Default: None.

* `--skip-issuer`

  Skip TLS certificate issuer setup. If you use the `--skip-issuer` option when you set up a ForgeOps deployment environment, you must set up your TLS certificate issuer before performing a ForgeOps deployment.

  Default: False.

###### forgeops image

The forgeops image command enables you to maintain ForgeOps deployments with the latest images available. Also, you can work with multiple versions of ForgeOps-provided images, providing more flexibility to upgrade the `forgeops` tool and ForgeOps deployment.

**This feature is supported for ForgeOps version 7.4 and later.**

* Advantages

  * You can upgrade forgeops command and ForgeOps deployment separately on your schedule.

  * When upgrading, you can create a new release and test it through your different ForgeOps deployment environments.

  * Manage a single Git release branch instead of separate branches for each platform version.

  * You can use supported container images that are regularly scanned for OS-level security vulnerabilities.

[](#command_details_2)Command details

forgeops image --env-name my-env my-components

Replace my-components with one or more of `platform`, `apps`, `ui`, `am`, `amster`, `idm`, `ds`, `admin-ui`, `end-user-ui`, `login-ui`, `ig`.

[](#options_6)Options

* `--kustomize-path` my-kustomize-loc

  The absolute path or the path relative to the `forgeops` directory where Kustomize overlay files are stored.

  Default: kustomize

* `--build-path` my-docker-loc

  The absolute path or the path relative to the `forgeops` directory where Docker files are stored.

  Default: docker

* `--helm-path` my-helm-loc

  The absolute path or the path relative to the `forgeops` directory where Helm values files are stored.

  Default: helm

* `--env-name` my-env

  Name of ForgeOps deployment environment in which you intend to manage Docker images.

* `--source` my-src-env

  Name of source environment if you are copying images.

* `--tag` my-tag

  Set the tag used for images.

* `--no-helm`

  Don't manage Helm values files.

* `--no-kustomize`

  Don't manage Kustomize overlay.

* `--copy`

  Copy images from `--source` to --env-name.

* `--release` platform-release

  Specify platform image release to set, for example `7.5.1`.

* `--release-name` my-release

  Name of the release file in docker/component/releases. Default: my-release in UTC format.

* `--releases-src` my-release-source-url

  URL or path where release files live (default: <http://releases.forgeops.com>)

* `--image-repo` my-docker-repo

  The URL to the container registry that contains Docker images.

  | Short form | Default URL                                   |
  | ---------- | --------------------------------------------- |
  | base       | us-docker.pkg.dev/forgeops-public/images-base |
  | deploy     | us-docker.pkg.dev/forgeops-public/images      |
  | dev        | gcr.io/forgerock-io                           |

Learn more about the forgeops image command in [Managing Ping Advanced Identity Software images](https://github.com/ForgeRock/forgeops/blob/2025.1.1/how-tos/manage-platform-images.md).

###### forgeops prereqs

The forgeops prereqs installs or upgrades prerequisites such as certificate manager, ingress, or secrets for deploying ForgeOps. This command replaces the install-prereqs script used in earlier ForgeOps releases.

[](#command_details_3)Command details

forgeops prereqs prereqs

[](#options_7)Options

* \--`debug`

  Turn on debugging.

* \--`dryrun`

  Do a dry run to validate the command without making any changes.

* \--`verbose`

  Get detailed messages when running the command.

*  — `haproxy`

  Use `HAProxy` ingress controller.

* \--upgrade

  Upgrade if the prerequisite has been installed.

[](#prereqs-examples)Examples

* Install all prerequisites with defaults:

  forgeops prereqs

* Install HAProxy:

  forgeops prereqs ingress --haproxy secrets

* Install only `cert-manager` and `secret-agent`:

  forgeops prereqs cert-manager secrets

* Install only `cert-manager` and Traefik:

  forgeops prereqs cert-manager ingress

* Install HAProxy:

  forgeops prereqs ingress --haproxy

### Secrets Reference

To protect network communication and keep data confidential and unalterable, ForgeOps authentication relies on:

* AM and IDM signing

* Encryption methods.

AM and IDM signing and encryption depend on keys or secrets generated using cryptographic algorithms.

This section describes various secrets and keys used in ForgeOps. Secrets, passwords, and keys used in ForgeOps are configured as environment variables or as files mounted on the Kubernetes pods.

#### AM configuration passwords

##### Kubernetes secret name: `am-env-secret`

* Passwords stored as environment variables in `am` pod

  * Pod: `am`

  * Container: `openam`

  * Type: Environment variable

    | Description or role                                                                                       | Location on container                                                                                                                                                                                                                                                 |
    | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **AM\_AUTHENTICATION\_SHARED\_SECRET**                                                                    |                                                                                                                                                                                                                                                                       |
    | Core authentication secret for the root realm.                                                            | * `cdk/config/services/realm/root/iplanetamauthservice/1.0/organizationconfig/defaultconfig.json`

    * Value: `security.sharedSecret`                                                                                                                                   |
    | **AM\_ENCRYPTION\_KEY**                                                                                   |                                                                                                                                                                                                                                                                       |
    | Key used for encrypting information stored in the secure state of authentication trees in AM.             | - `cdk/config/services/realm/root/iplanetamplatformservice/1.0/globalconfig/default/com-sun-identity-servers/http___am_80_am.json`

    - `cdk/config/services/realm/root/iplanetamplatformservice/1.0/globalconfig/default/com-sun-identity-servers/server-default.json` |
    | **AM\_OIDC\_CLIENT\_SUBJECT\_IDENTIFIER\_HASH\_SALT**                                                     |                                                                                                                                                                                                                                                                       |
    | Configuration parameter used to specify the Subject Identifier Hash Salt in the OAuth 2.0 and OIDC flows. | `base/config/services/realm/root/oauth2provider/1.0/organizationconfig/defaultconfig.json`                                                                                                                                                                            |
    | **AM\_PASSWORDS\_AMADMIN\_CLEAR**                                                                         |                                                                                                                                                                                                                                                                       |
    | Password for the amadmin user. Updated to AM\_PASSWORDS\_AMADMIN\_HASHED in `docker-entrypoint.sh`.       | `base/config/services/realm/root/sunidentityrepositoryservice/1.0/globalconfig/default/users/amadmin.json`                                                                                                                                                            |
    | **AM\_SELFSERVICE\_LEGACY\_CONFIRMATION\_EMAIL\_LINK\_SIGNING\_KEY**                                      |                                                                                                                                                                                                                                                                       |
    | A 256-bit key (base64-encoded) used for HMAC signing of the legacy self-service confirmation email links. | `base/config/services/realm/root/restsecurity/1.0/organizationconfig/defaultconfig.json`                                                                                                                                                                              |
    | **AM\_SESSION\_STATELESS\_ENCRYPTION\_KEY**                                                               |                                                                                                                                                                                                                                                                       |
    | Encryption key for encrypting stateless session tokens.                                                   | `base/config/services/realm/root/iplanetamsessionservice/1.0/globalconfig/default.json`                                                                                                                                                                               |
    | **AM\_SESSION\_STATELESS\_SIGNING\_KEY**                                                                  |                                                                                                                                                                                                                                                                       |
    | Signing key for validating the security of stateless session tokens.                                      | `base/config/services/realm/root/iplanetamsessionservice/1.0/globalconfig/default.json`                                                                                                                                                                               |

#### AM secrets

##### Kubernetes secret name: `am-keystore`

* Keystore mounted in `am` pod

  * Description: The default AM keystore with test aliases

  * Container: openam

  * Mount path: /var/run/secrets

|   |                                                                              |
| - | ---------------------------------------------------------------------------- |
|   | For use with the secret agent only. Not applicable for the secret generator. |

| Description or role                                                 | Location on container                                                        |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **`.keystore.jceks`**                                               |                                                                              |
| Default AM keystore with test aliases                               | Copied in `docker-entrypoint.sh` to `/home/forgerock/security/keystores`.    |
| **`.keystore`**                                                     |                                                                              |
| Default password for all the key aliases in the default AM keystore | Copied in `` `docker-entrypoint.sh to `/home/forgerock/security/keystore ``. |
| **`.storepass`**                                                    |                                                                              |
| Default AM keystore password                                        | Copied in `docker-entrypoint.sh` to `/home/forgerock/security/keystore`.     |

#### Amster secrets, keys, and passwords

##### Kubernetes secret name: `amster`

* Mounted files on `amster` pod

  * Description: The key-pair for SSH connectivity to PingAM

  * Pod: `amster`

  * Container: `amster` or `pause`

  * Mount path: `/var/run/secrets/amster`

    | Description or role                       | Location on container            |
    | ----------------------------------------- | -------------------------------- |
    | **`id_rsa`**                              |                                  |
    | Private key for SSH connection to PingAM. | `/var/run/secrets/amster/id_rsa` |

* Mounted files on `am` pod

  * Pod: `am`

  * Container: `openam`

  * Mount path: `/var/run/secrets/amster`

    | Description or role                         | Location on container                     |
    | ------------------------------------------- | ----------------------------------------- |
    | **`id_rsa.pub`**                            |                                           |
    | Public key for SSH connections from Amster. | `/var/run/secrets/amster/authorized_keys` |

##### Kubernetes secret name: `amster-env-secrets`

* Environment variables in `amster` pod

  * Description: The key pairs for SSH connectivity to PingAM

  * Pod: `amster`

  * Container: `amster`

  * Type: Environment variable

    | Description or role                                                                                                                       | Location on container                                |
    | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
    | **IDM\_PROVISIONING\_CLIENT\_SECRET**                                                                                                     |                                                      |
    | AM nodes in authentication journeys use this confidential client to authenticate through AM and provision identities through IDM.         | Used for provisioning Oauth2Client in IDM.           |
    | **IDM\_RS\_CLIENT\_SECRET**                                                                                                               |                                                      |
    | IDM uses this confidential client to introspect access tokens through the `am/oauth2/introspect` endpoint to get information about users. | Used in the Oauth2Client of the IDM resource server. |

* Environment variables in `idm` pod

  * Pod: `idm`

  * Container: `openidm`

  * Type: Environment variable

    | Description or role                                                                                                                       | Location on container                                                                                         |
    | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
    | **IDM\_RS\_CLIENT\_SECRET**                                                                                                               |                                                                                                               |
    | IDM uses this confidential client to introspect access tokens through the `am/oauth2/introspect` endpoint to get information about users. | Set in `boot.properties: "rs.client.secret"` to communicate with the Oauth2Client of the IDM resource server. |

#### DS secrets, keys, and passwords

##### Kubernetes secret name: `ds-env-secrets`

Service account passwords for AM connecting to DS backends. `ds-set-passwords` is used to update the passwords on the DS backends.

* Environment variables in `am` pod

  * Pod: `am`

  * Container: `openam`

  * Type: Environment variables

    | Description or role                                              | Location on container                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **AM\_STORES\_USER\_PASSWORD**                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | Password for AM to access the identities backend on `ds-idrepo`. | 1. `cdk/config/services/realm/root/sunidentityrepositoryservice/1.0/organizationconfig/default/opendj.json`

    2. `base/config/services/realm/root/amdatastoreservice/1.0/globalconfig/default/datastorecontainer/application-store.json`

    3. `base/config/services/realm/root/iplanetamauthldapservice/1.0/organizationconfig/default.json`

    4. `base/config/services/realm/root/iplanetamauthldapservice/1.0/organizationconfig/defaultconfig.json`

    5. `base/config/services/realm/root/iplanetamplatformservice/1.0/globalconfig/default/com-sun-identity-servers/server-default.json`

    6. `base/config/services/realm/root-sunamhiddenrealmdelegationservicepermissions/iplanetamauthldapservice/1.0/organizationconfig/default.json`

       * **Variables are set in the `docker-entrypoint.sh`** |
    | **AM\_STORES\_APPLICATION\_PASSWORD**                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | Password for AM to access the config backend on `ds-idrepo`.     | 1) `cdk/config/services/realm/root/iplanetamplatformservice/1.0/globalconfig/default/com-sun-identity-servers/server-default.json`

    2) `base/config/services/realm/root/amdatastoreservice/1.0/globalconfig/default/datastorecontainer/application-store.json`

    3) `base/config/services/realm/root/amdatastoreservice/1.0/globalconfig/default/datastorecontainer/policy-store.json`

    4) `base/config/services/realm/root/iplanetamplatformservice/1.0/globalconfig/default/com-sun-identity-servers/server-default.json`

    5) `base/config/services/realm/root/iplanetampolicyconfigservice/1.0/organizationconfig/defaultconfig.json`

    6) `base/config/services/realm/root-sunamhiddenrealmdelegationservicepermissions/iplanetampolicyconfigservice/1.0/organizationconfig/default.json`        |
    | **AM\_STORES\_CTS\_PASSWORD**                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | Password for AM to access the tokens backend on `ds-cts`.        | 1. `cdk/config/services/realm/root/iplanetamplatformservice/1.0/globalconfig/default/com-sun-identity-servers/server-default.json`

    2. `base/config/services/realm/root/iplanetamplatformservice/1.0/globalconfig/default/com-sun-identity-servers/server-default.json`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

* Environment variables in `ds-set-passwords` pod

  * Pod: `ds-set-passwords`

  * Container: `openidm`

  * Type: Environment variables

    | Name                                  | Description                                                         |
    | ------------------------------------- | ------------------------------------------------------------------- |
    | **AM\_STORES\_USER\_PASSWORD**        | Password for AM to access the identity backend on the `ds-idrepo`.  |
    | **AM\_STORES\_APPLICATION\_PASSWORD** | Password for AM to access the configuration backend on `ds-idrepo`. |
    | **AM\_STORES\_CTS\_PASSWORD**         | Password for AM to access the tokens backend on `ds-cts`.           |

##### Kubernetes secret name: `ds-passwords`

* Passwords mounted in `ds-idrepo` or `ds-cts` pods

  DS management passwords for administration and monitoring.

  * Pod: `ds-idrepo` or `ds-cts`

  * Container: `ds`

  * Mount path: `/var/run/secrets/admin`

    | Description or role                                                                                                                     | Location on container                                                       |
    | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
    | **dirmanager.pw**                                                                                                                       |                                                                             |
    | Root password for the `uid=admin` user.                                                                                                 | Set in `/opt/opendj/data/db/rootUser/rootUser.ldif` as `uid-admin`.         |
    | **monitor.pw**                                                                                                                          |                                                                             |
    | Password for the monitor backend. The monitor backend allows clients to access information provided by the DS server monitor providers. | Set in `/opt/opendj/data/db/monitorUser/monitorUser.ldif` as `uid=monitor`. |

* Passwords mounted in `idm` pods

  * Pod: `idm`

  * Container: `idm`

  * Type: Environment variables - `OPENIDM_REPO_PASSWORD` and `USERSTORE_PASSWORD`

    | Description or role                                                                           | Location on container |
    | --------------------------------------------------------------------------------------------- | --------------------- |
    | **`dirmanager.pw`**                                                                           |                       |
    | Root password for communicating with DS. Configured in `docker/idm/resolver/boot.properties`. |                       |

##### Kubernetes secret name: `ds-master-keypair`

Master SSL key pair for encrypting DS data

* Pod: `ds-idrepo` or `ds-cts`

* Container: `init` and `ds`

* Mount path: `/var/run/secrets/ds-master-keypair`

  | Description or role                                                        | Location on container                                                                                  |
  | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
  | **`ca.crt`, `tls.crt`, or `tls.key`**                                      |                                                                                                        |
  | SSL key pair with ca self-signed cert used to encrypt DS data for backups. | `/var/run/secrets/keys/ds/master-key`. Used by `PEM Key Manager` provider configured in `ds-setup.sh`. |

##### Kubernetes secret name: `ds-ssl-keypair`

The SSL key pair used for encrypting replication traffic. It also used by AM and IDM as a trust store for LDAPS connections to DS.

* Pod: `ds-idrepo` or `ds-cts`

* Container: `init` and `ds`

* Mount path: `/var/run/secrets/keys/ds/ds-ssl-keypair`

  | Description or role                                                                                                            | Location on container                                                                                          |
  | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- |
  | **ca.crt/tls.crt/tls.key**                                                                                                     |                                                                                                                |
  | SSL key pair with a self-signed certificate of the certificate authority. Used for encrypting data replicated between servers. | `/var/run/secrets/keys/ds/ds-ssl-keypair`. Used by the `PEM Key Manager` provider configured in `ds-setup.sh`. |

* Pod: `idm`

* Container: `truststore-init`

* Mount path: `/var/run/secrets/truststore/ca.crt`

  | Description or role                                                                                                | Location on container                                                                                |
  | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
  | **ca.crt**                                                                                                         |                                                                                                      |
  | SSL key pair with a certificate authority signed certificate. Used for encrypting data replicated between servers. | `IDM_PEM_TRUSTSTORE_DS=/var/run/secrets/truststore/cacerts`, copied to `/opt/openidm/idmtruststore`. |

* Pod: `am`

* Container: `truststore-init`

* Mount path: `/var/run/secrets/truststore/ca.crt`

  | Description or role                                                                                                              | Location on container                                                                               |
  | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
  | **ca.crt**                                                                                                                       |                                                                                                     |
  | SSL key pair with the self-signed certificate of the certificate authority. Used for encrypting data replicated between servers. | `IDM_PEM_TRUSTSTORE_DS=/var/run/secrets/truststore/ca.crt`, copied to `/opt/openidm/idmtruststore`. |

#### IDM admin passwords

##### Kubernetes secret name: `idm-env-secrets`

IDM administration and keystore passwords

* Pod: `idm`

* Container: `openidm`

* Type: ENV VARS

  | Description or role             | Location on container                               |
  | ------------------------------- | --------------------------------------------------- |
  | **OPENIDM\_ADMIN\_PASSWORD**    |                                                     |
  | IDM admin password.             | Configured in `repo.init.json`                      |
  | **OPENIDM\_KEYSTORE\_PASSWORD** |                                                     |
  | IDM keystore password.          | Configured in `docker/idm/resolver/boot.properties` |

### ForgeOps benchmarks

The benchmarking instructions in this part of the documentation give you a method to validate performance of your ForgeOps deployment.

The benchmarking techniques we present are a lightweight example, and are not a substitute for load testing a production deployment. Use our benchmarking techniques to help you get started with the task of constructing your own load tests.

When you[create a project plan](start/start-here.html#planning), you'll need to think about how you'll put together production-quality load tests that accurately measure your own deployment's performance.

#### ForgeOps benchmarking checklist

* [icon: square-o, set=fa][Become familiar with ForgeOps benchmarking](reference/benchmark/intro.html)

* [icon: square-o, set=fa][Install third-party software](reference/benchmark/sw.html)

* [icon: square-o, set=fa][Generate test users](reference/benchmark/testusers.html)

* [icon: square-o, set=fa][Benchmark the authentication rate](reference/benchmark/authrate.html)

* [icon: square-o, set=fa][Benchmark the OAuth 2.0 authorization code flow](reference/benchmark/oauth2.html)

#### About ForgeOps benchmarking

[ForgeOps benchmarks](reference/benchmark/overview.html) provides instructions for running lightweight benchmarks to give you a means for validating your own ForgeOps deployment.

The ForgeOps team runs the same benchmark tests. Our results are available upon request. To get them, contact your Ping Identity sales representative.

We conduct our tests using the configurations specified for [small, medium, and large clusters](deploy/architecture.html#cluster-and-deployment-sizes). We create our clusters using the techniques described in the [Setup documentation](setup/overview.html).

Next, we [generate test users](reference/benchmark/testusers.html):

* 1,000,000 test users for a small cluster.

* 10,000,000 test users for a medium cluster.

* 100,000,000 test users for a large cluster.

Finally, we run tests that measure authentication rates and OAuth 2.0 authorization code flow performance.

If you follow the same method of performing a ForgeOps deployment and running benchmarks, the results you obtain similar results. However, factors beyond the scope of ForgeOps deployment or a failure to use our documented sizing and configuration may affect your benchmark test results. These factors might include (but are not limited to) updates to cloud platform SDKs, changes to third-party software required for Kubernetes, and changes you've made to sizing or configuration to suit your business needs.

ForgeOps deployments are designed to:

* Conform to DevOps best practices

* Facilitate continuous integration and continuous deployment

* Scale and deploy on any Kubernetes environment in the cloud

If you require higher performance than the benchmarks reported here, you can scale your deployment horizontally and vertically. Vertically scaling Ping Advanced Identity Software works particularly well in the cloud. For more information about scaling your deployment, contact your qualified Ping Identity partner or technical consultant.

##### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps benchmarking](reference/benchmark/intro.html)

* [icon: square-o, set=fa]*[Install third-party software](reference/benchmark/sw.html)*

* [icon: square-o, set=fa][Generate test users](reference/benchmark/testusers.html)

* [icon: square-o, set=fa][Benchmark the authentication rate](reference/benchmark/authrate.html)

* [icon: square-o, set=fa][Benchmark the OAuth 2.0 authorization code flow](reference/benchmark/oauth2.html)

#### Third-party software

The ForgeOps team uses Gradle 6.8.3 to benchmark ForgeOps deployments. Before you start running benchmarks, install this version of Gradle in your local environment.

Earlier and later versions will *probably* work. If you want to try using another version, it is your responsibility to validate it.

In addition to Gradle, you'll need all the third-party software required to perform a ForgeOps deployment

* [GKE](setup/google-cloud.html#gcp-third-party-software)

* [EKS](setup/aws.html#aws-third-party-software)

* [AKS](setup/azure.html#azure-third-party-software)

##### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps benchmarking](reference/benchmark/intro.html)

* [icon: check-square-o, set=fa][Install third-party software](reference/benchmark/sw.html)

* [icon: square-o, set=fa]*[Generate test users](reference/benchmark/testusers.html)*

* [icon: square-o, set=fa][Benchmark the authentication rate](reference/benchmark/authrate.html)

* [icon: square-o, set=fa][Benchmark the OAuth 2.0 authorization code flow](reference/benchmark/oauth2.html)

#### Test user generation

Running the [Authentication rate](reference/benchmark/authrate.html) and [OAuth 2.0 authorization code flow](reference/benchmark/oauth2.html) benchmarks requires a set of test users. This page provides instructions for generating a set of test users suitable for these two lightweight AM benchmarks. Note that these test users are not necessarily suitable for other benchmarks or load tests, and that they can't be used with IDM.

##### For small and medium clusters

Follow these steps to generate test users for lightweight AM benchmarks, provision the user stores, and prime the directory servers:

1. Set up your Kubernetes context:

   1. Set the `KUBECONFIG` environment variable so that your Kubernetes context references the cluster where you'll perform the ForgeOps deployment.

   2. Set the active namespace in your Kubernetes context to the Kubernetes namespace where you deployed the platform.

2. Obtain the password for the directory superuser, `uid=admin`:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops info | grep uid=admin
   ```

   Make a note of this password. You'll need it for subsequent steps in this procedure.

3. Change to the directory that contains the source for the `dsutil` Docker container:

   ```
   $ cd /path/to/forgeops/docker/ds/dsutil
   ```

   You'll generate test users from a pod you create from the `dsutil` container.

4. Build and push the `dsutil` Docker container to your container registry, and then run the container.

   The my-registry parameter varies, depending on the location of your registry:

   ```
   $ docker build --tag=my-registry/dsutil .
   $ docker push my-registry/dsutil
   $ kubectl run -it dsutil --image=my-registry/dsutil --restart=Never -- bash
   ```

   The kubectl run command creates the `dsutil` pod, and leaves you in a shell that lets you run commands in the pod.

5. Generate the test users—1,000,000 users for a small cluster and 10,000,000 for a medium cluster:

   Run these substeps from the `dsutil` pod's shell:

   1. Make an LDIF file that has the number of user entries for your cluster size:

      For example, for a small cluster:

      ```
      $ /opt/opendj/bin/makeldif -o data/entries.ldif \
       -c numusers=1000000 config/MakeLDIF/ds-idrepo.template
      Processed 1000 entries
      Processed 2000 entries
      Processed 3000 entries
      ...
      Processed 1000000 entries
      LDIF processing complete. 1000003 entries written
      ```

      When the ForgeOps team ran the makeldif script, it took approximately:

      * 30 seconds to run on a small cluster.

      * 4 minutes to run on a medium cluster.

   2. Create the user entries in the directory:

      ```
      $ /opt/opendj/bin/ldapmodify \
       -h ds-idrepo-0.ds-idrepo -p 1389 --useStartTls --trustAll \
       -D "uid=admin" -w directory-superuser-password --noPropertiesFile \
       --no-prompt --continueOnError --numConnections 10 data/entries.ldif
      ```

      `ADD operation successful` messages appear as user entries are added to the directory.

      When the ForgeOps team ran the ldapmodify command, it took approximately:

      * 15 minutes to run on a small cluster.

      * 2 hours 35 minutes to run on a medium cluster.

6. Prime the directory servers:

   1. Open a new terminal window or tab.

      Use this new terminal window—not the one running the `dsutil` pod's shell—for the remaining substeps in this step.

   2. Prime the directory server running in the `ds-idrepo-0` pod:

      1. Start a shell that lets you run commands in the `ds-idrepo-0` pod:

         ```
         $ kubectl exec ds-idrepo-0 -it -- bash
         ```

      2. Run the following command:

         ```
         $ ldapsearch -D "uid=admin" -w directory-superuser-password \
          -p 1389 -b "ou=identities"  uid=user.*  | grep dn: | wc -l
         10000000
         ```

      3. Exit from the `id-dsrepo-0` pod's shell:

         ```
         $ exit
         ```

   3. Prime the directory server running in the `ds-idrepo-1` pod.

##### For large clusters

Here are some very general steps you can follow if you want to generate test users for benchmarking or load testing a large cluster:

1. Install DS in a VM in the cloud.

2. Run the `makeldif` and `ldapmodify` commands, as described above.

3. Back up your directory.

4. Upload the backup files to cloud storage.

5. Restore an `idrepo` pod from your backup following steps similar to the procedure in [Restore](backup/dsbackup.html#dsbackup-restore).

##### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps benchmarking](reference/benchmark/intro.html)

* [icon: check-square-o, set=fa][Install third-party software](reference/benchmark/sw.html)

* [icon: check-square-o, set=fa][Generate test users](reference/benchmark/testusers.html)

* [icon: square-o, set=fa]*[Benchmark the authentication rate](reference/benchmark/authrate.html)*

* [icon: square-o, set=fa][Benchmark the OAuth 2.0 authorization code flow](reference/benchmark/oauth2.html)

#### Authentication rate

The `AMRestAuthNSim.scala` simulation tests authentication rates using the REST API. It measures the throughput and response times of an AM server performing REST authentications when AM is configured to use CTS-based sessions.

To run the simulation:

1. Make sure the userstore is provisioned, and the PingDS cache is primed.

   Refer to [Test user generation](reference/benchmark/testusers.html).

2. Set environment variables that specify the host on which to run the test, the number of concurrent threads to spawn when running the test, the duration of the test (in seconds), the first part of the user ID, and the user password, and the number of users for the test:

   ```
   $ export TARGET_HOST=
   $ export CONCURRENCY=100
   $ export DURATION=60
   $ export USER_PREFIX=user.
   $ export USER_PASSWORD=T35tr0ck123
   $ export USER_POOL=n-users
   ```

   where *n-users* is `1000000` for a small cluster, `10000000` for a medium cluster, and `100000000` for a large cluster.

3. Configure AM for CTS-based sessions:

   1. Log in to the Ping Advanced Identity Software admin UI as the `amadmin` user. For details, refer to [AM Services](deploy/access.html#am-services-cdm).

   2. Access the AM admin UI.

   3. Select the top level realm.

   4. Select Properties.

   5. Make sure the Use Client-based Sessions option is disabled.

      If it's not disabled, disable it, and then select Save Changes.

4. Change to the /path/to/forgeops/docker/gatling directory.

5. Run the simulation:

   ```
   $ gradle clean; gradle gatlingRun-am.AMRestAuthNSim
   ```

   When the simulation is complete, the name of a file containing the test results appears near the end of the output.

6. Open the file containing the test results in a browser to review the results.

##### Next step

* [icon: check-square-o, set=fa][Become familiar with ForgeOps benchmarking](reference/benchmark/intro.html)

* [icon: check-square-o, set=fa][Install third-party software](reference/benchmark/sw.html)

* [icon: check-square-o, set=fa][Generate test users](reference/benchmark/testusers.html)

* [icon: check-square-o, set=fa][Benchmark the authentication rate](reference/benchmark/authrate.html)

* [icon: square-o, set=fa]*[Benchmark the OAuth 2.0 authorization code flow](reference/benchmark/oauth2.html)*

#### OAuth 2.0 authorization code flow

The `AMAccessTokenSim.scala` simulation tests OAuth 2.0 authorization code flow performance. It measures the throughput and response time of an AM server performing authentication, authorization, and session token management when AM is configured to use client-based sessions, and OAuth 2.0 is configured to use client-based tokens. In this test, one transaction includes all three operations.

To run the simulation:

1. Make sure the userstore is provisioned, and the PingDS cache is primed.

   Refer to [Test user generation](reference/benchmark/testusers.html).

2. Set environment variables that specify,

   * the host on which to run the test,

   * the number of concurrent threads to spawn when running the test,

   * the duration of the test (in seconds),

   * the first part of the user ID, and the user password, and

   * the number of users for the test:

   ```
   $ export TARGET_HOST=my-fqdn
   $ export CONCURRENCY=100
   $ export DURATION=60
   $ export USER_PREFIX=user.
   $ export USER_PASSWORD=T35tr0ck123
   $ export USER_POOL=n-users
   ```

   where *n-users* is `1000000` for a small cluster, `10000000` for a medium cluster, and `100000000` for a large cluster.

3. Configure AM for CTS-based sessions:

   1. Log in to the Ping Advanced Identity Software admin UI as the `amadmin` user. For details, refer to [AM Services](deploy/access.html#am-services-cdm).

   2. Access the AM admin UI.

   3. Select the top level realm.

   4. Select Properties.

   5. Make sure the Use Client-based Sessions option is disabled.

      If it's not disabled, disable it, and then select Save Changes.

4. Configure AM for CTS-based OAuth2 tokens:

   1. Select Realms > Top Level Realm.

   2. Select Services > OAuth2 Provider.

   3. Make sure the Use Client-based Access & Refresh Tokens option is disabled.

      If it's not disabled, disable it, and then select Save Changes.

5. Change to the /path/to/forgeops/docker/gatling directory.

6. Run the simulation:

   ```
   $ gradle clean; gradle gatlingRun-am.AMAccessTokenSim
   ```

   When the simulation is complete, the name of a file containing the test results appears near the end of the output.

7. Open the file containing the test results in a browser to review the results.

##### Congratulations!

You've successfully run the lightweight benchmark tests on a ForgeOps deployment.

* [icon: check-square-o, set=fa][Become familiar with ForgeOps benchmarking](reference/benchmark/intro.html)

* [icon: check-square-o, set=fa][Install third-party software](reference/benchmark/sw.html)

* [icon: check-square-o, set=fa][Generate test users](reference/benchmark/testusers.html)

* [icon: check-square-o, set=fa][Benchmark the authentication rate](reference/benchmark/authrate.html)

* [icon: check-square-o, set=fa][Benchmark the OAuth 2.0 authorization code flow](reference/benchmark/oauth2.html)

### Ingress

By default, ForgeOps deployments use Ingress-NGINX controller.

For deployments on GKE, EKS, and AKS, the tf-apply cluster creation script deploys the Traefik ingress controller when it creates new Kubernetes clusters. Alternatively, you can deploy [HAProxy Ingress](#haproxy) as your ingress controller.

For deployments on minikube, the minikube start command example installs the ingress add-on in your [minikube cluster](setup/minikube.html).

#### HAProxy Ingress

This section lists adjustments you'll need to make if you want to perform a ForgeOps deployment that uses HAProxy Ingress as the ingress controller instead of Ingress-NGINX controller.

When you create your [GKE](setup/google-cloud.html#gcp-cluster), [EKS](setup/aws.html#aws-cluster), or [AKS](setup/azure.html#azure-cluster) cluster:

1. Before you run the tf-apply script, configure Terraform to deploy HAProxy Ingress in your cluster.

   Modify these values under `cluster.tf_cluster_gke_small` in the override.auto.tfvars file:

   1. Set the value of the `helm.ingress-haproxy.deploy` variable to `false`.

2. To get the ingress controller's external IP address on your GKE, EKS, or AKS cluster, specify --namespace haproxy-ingress when you run the kubectl get services command. For example:

   ```
   $ kubectl get services --namespace haproxy-ingress
   NAME              TYPE           CLUSTER-IP   EXTERNAL-IP  PORT(S)                      AGE
   haproxy-ingress   LoadBalancer   10.84.6.68   34.82.11.221 80:32288/TCP,443:32325/TCP   38s
   ...
   ```

When you [perform your ForgeOps deployment](deploy/deploy.html):

1. Specify the --ingress-class haproxy argument. For example:

   ```
   $ cd /path/to/forgeops/bin
   $ ./forgeops apply --small --ingress-class haproxy --fqdn my-fqdn --namespace my-namespace
   ```

### Glossary

* affinity (AM)

  AM affinity deployment lets AM spread the LDAP requests load over multiple directory server instances. Once a CTS token is created and assigned to a session, AM sends all further token operations to the same token origin directory server from any AM node. This ensures that the load of CTS token management is spread across directory servers.

  Source: [CTS Affinity Deployment](https://docs.pingidentity.com/pingam/8/cts-guide/cts-deployment-architectures.html#cts-affinity) in the Core Token Service (CTS) documentation

* Amazon EKS

  Amazon Elastic Container Service for Kubernetes (Amazon EKS) is a managed service that makes it easy for you to run Kubernetes on Amazon Web Services without needing to set up or maintain your own Kubernetes control plane.

  Source: [What is Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) in the Amazon EKS documentation

* ARN (AWS)

  An Amazon Resource Name (ARN) uniquely identifies an Amazon Web Service (AWS) resource. AWS requires an ARN when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls.

  Source: [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the AWS documentation

* AWS IAM Authenticator for Kubernetes

  The AWS IAM Authenticator for Kubernetes is an authentication tool that lets you use Amazon Web Services (AWS) credentials for authenticating to a Kubernetes cluster.

  Source: [AWS IAM Authenticator for Kubernetes](https://github.com/kubernetes-sigs/aws-iam-authenticator/blob/master/README.md) README file on GitHub

* Azure Kubernetes Service (AKS)

  AKS is a managed container orchestration service based on Kubernetes. AKS is available on the Microsoft Azure public cloud. AKS manages your hosted Kubernetes environment, making it quick and easy to deploy and manage containerized applications.

  Source: [Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes) in the Microsoft Azure documentation

* BusyBox container

  A BusyBox container is a minimal, lightweight containerized environment that includes a single, small executable file providing a compact implementation of over 300 common UNIX utilities. It's widely used for creating extremely small container images.

  In ForgeOps deployments, the BusyBox container is used as a base image for custom configurations.

  Source: [BusyBox page on Docker Hub](https://hub.docker.com/_/busybox).

* cloud-controller-manager

  The `cloud-controller-manager` daemon runs controllers that interact with the underlying cloud providers. The `cloud-controller-manager` daemon runs provider-specific controller loops only.

  Source: [cloud-controller-manager](https://kubernetes.io/docs/concepts/overview/components/#cloud-controller-manager) in the Kubernetes Concepts documentation

- ForgeOps deployment

  A ForgeOps deployment is a deployment of the Ping Advanced Identity Software on Kubernetes based on Docker images, Helm charts, Kustomize bases and overlays, utility programs, and other artifacts you can find in the `forgeops` repository on GitHub.

  A *single-instance ForgeOps deployment* is a special ForgeOps deployment that you use to [configure AM and IDM and build custom Docker images for the Ping Advanced Identity Software](customize/overview.html). They are called single-instance deployments because unlike small, medium, and large deployments, they have only single pods that run AM and IDM. They are only suitable for developing the AM and IDM configurations and must not be used for testing performance, monitoring, security, and backup requirements in production environments.

  Source: [Deployment overview](deploy/overview.html)

- CloudFormation (AWS)

  CloudFormation is a service that helps you model and set up your AWS resources. You create a template that describes all the AWS resources that you want. CloudFormation takes care of provisioning and configuring those resources for you.

  Source: [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) in the AWS documentation

* CloudFormation template (AWS)

  An AWS CloudFormation template describes the resources that you want to provision in your [AWS stack](#stack-aws). AWS CloudFormation templates are text files formatted in JSON or YAML.

  Source: [Working with AWS CloudFormation Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the AWS documentation

* cluster

  A container cluster is the foundation of Kubernetes Engine. A cluster consists of at least one [control plane](#control-plane) and multiple worker machines called nodes. The Kubernetes objects that represent your containerized applications all run on top of a cluster.

  Source: [Standard cluster architecture](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) in the Google Kubernetes Engine (GKE) documentation

* ConfigMap

  A configuration map, called `ConfigMap` in Kubernetes manifests, binds the configuration files, command-line arguments, environment variables, port numbers, and other configuration artifacts to the assigned containers and system components at runtime. The configuration maps are useful for storing and sharing non-sensitive, unencrypted configuration information.

  Source: [ConfigMap](https://cloud.google.com/kubernetes-engine/docs/concepts/configmap) in the Google Kubernetes Engine (GKE) documentation

- container

  A container is an allocation of resources such as CPU, network I/O, bandwidth, block I/O, and memory that can be "contained" together and made available to specific processes without interference from the rest of the system. Containers decouple applications from underlying host infrastructure.

  Source: [Containers](https://kubernetes.io/docs/concepts/containers/) in the Kubernetes Concepts documentation

* control plane

  A control plane runs the control plane processes, including the Kubernetes API server, scheduler, and core resource controllers. GKE manages the lifecycle of the control plane when you create or delete a cluster.

  Source: [Control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) in the Google Kubernetes Engine (GKE) documentation

* DaemonSet

  A set of daemons, called `DaemonSet` in Kubernetes manifests, manages a group of replicated pods. Usually, the daemon set follows a one-pod-per-node model. As you add nodes to a node pool, the daemon set automatically distributes the pod workload to the new nodes as needed.

  Source: [DaemonSet](https://cloud.google.com/kubernetes-engine/docs/concepts/daemonset) in the Google Cloud documentation

* deployment

  A Kubernetes deployment represents a set of multiple, identical pods. Deployment runs multiple replicas of your application and automatically replaces any instances that fail or become unresponsive.

  Source: [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) in the Kubernetes Concepts documentation

* deployment controller

  A deployment controller provides declarative updates for pods and replica sets. You describe a desired state in a deployment object, and the deployment controller changes the actual state to the desired state at a controlled rate. You can define deployments to create new replica sets, or to remove existing deployments and adopt all their resources with new deployments.

  Source: [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) in the Google Cloud documentation

* Docker container

  A Docker container is a runtime instance of a Docker image. The container is isolated from other containers and its host machine. You can control how isolated your container's network, storage, or other underlying subsystems are from other containers or from the host machine.

  Source: [Containers](https://docs.docker.com/get-started/overview/#docker-objects) in the Docker Getting Started documentation

* Docker daemon

  The Docker daemon (`dockerd`) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A Docker daemon can also communicate with other Docker daemons to manage Docker services.

  Source: [The Docker daemon](https://docs.docker.com/get-started/overview/#the-docker-daemon) section in the Docker Overview documentation

* Docker Engine

  Docker Engine is an open source containerization technology for building and containerizing applications. Docker Engine acts as a client-server application with:

  * A server with a long-running daemon process, `dockerd`.

  * APIs, which specify interfaces that programs can use to talk to and instruct the Docker daemon.

  * A command-line interface (CLI) client, `docker`. The CLI uses Docker APIs to control or interact with the Docker daemon through scripting or direct CLI commands. Many other Docker applications use the underlying API and CLI. The daemon creates and manages Docker objects, such as images, containers, networks, and volumes.

  Source: [Docker Engine overview](https://docs.docker.com/engine/) in the Docker documentation

* Dockerfile

  A Dockerfile is a text file that contains the instructions for building a Docker image. Docker uses the Dockerfile to automate the process of building a Docker image.

  Source: [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) in the Docker documentation

- Docker Hub

  Docker Hub provides a place for you and your team to build and ship [Docker images](#docker-image). You can create public repositories that can be accessed by any other Docker Hub user, or you can create private repositories you can control access to.

  Source: [Docker Hub Quickstart](https://docs.docker.com/docker-hub/) section in the Docker Overview documentation

* Docker image

  A Docker image is an application you would like to run. A container is a running instance of an image.

  An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization.

  An image includes the application code, a runtime engine, libraries, environment variables, and configuration files that are required to run the application.

  Source: [Docker objects](https://docs.docker.com/get-started/overview/#docker-objects) section in the Docker Overview documentation

* Docker namespace

  Docker namespaces provide a layer of isolation. When you run a container, Docker creates a set of namespaces for that container. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.

  The `PID` namespace is the mechanism for remapping process IDs inside the container. Other namespaces such as net, mnt, ipc, and uts provide the isolated environments we know as containers. The user namespace is the mechanism for remapping user IDs inside a container.

  Source: [The underlying technology](https://docs.docker.com/get-started/overview/#the-underlying-technology) section in the Docker Overview documentation

* Docker registry

  A Docker registry stores [Docker images](#docker-image). Docker Hub and Docker Cloud are public registries that anyone can use, and Docker is configured to look for images on [Docker Hub](#docker-hub) by default. You can also run your own private registry.

  Source: [Docker registries](https://docs.docker.com/get-started/overview/#docker-registries) section in the Docker Overview documentation

* Docker repository

  A Docker repository is a public, certified repository from vendors and contributors to Docker. It contains [Docker images](#docker-image) that you can use as the foundation to build your applications and services.

  Source: [Manage repositories](https://docs.docker.com/docker-hub/repos/) in the Docker documentation

* dynamic volume provisioning

  The process of creating storage volumes on demand is called dynamic volume provisioning. Dynamic volume provisioning lets you create storage volumes on demand. It automatically provisions storage when it is requested by users.

  Source: [Dynamic Volume Provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/) in the Kubernetes Concepts documentation

- egress

  An egress controls access to destinations outside the network from within a Kubernetes network. For an external destination to be accessed from a Kubernetes environment, the destination should be listed as an allowed destination in the allowlist configuration.

  Source: [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) in the Kubernetes Concepts documentation

- firewall rule

  A firewall rule lets you allow or deny traffic to and from your virtual machine instances based on a configuration you specify. Each Kubernetes network has a set of firewall rules controlling access to and from instances in its subnets. Each firewall rule is defined to apply to either incoming ([ingress](#gloss-ingress)) or outgoing ([egress](#egress)) traffic, not both.

  Source: [VPC firewall rules](https://cloud.google.com/firewall/docs) in the Google Cloud documentation

- garbage collection

  Garbage collection is the process of deleting unused objects. [Kubelets](#kubelet) perform garbage collection for containers every minute, and garbage collection for images every five minutes. You can adjust the high and low threshold flags and garbage collection policy to tune image garbage collection.

  Source: [Garbage Collection](https://kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/) in the Kubernetes Concepts documentation

- Google Kubernetes Engine (GKE)

  The Google Kubernetes Engine (GKE) is an environment for deploying, managing, and scaling your containerized applications using Google infrastructure. The GKE environment consists of multiple machine instances grouped together to form a container cluster.

  Source: [GKE overview](https://cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) in the Google Cloud documentation

* horizontal pod autoscaler

  The horizontal pod autoscaler enables the cluster to automatically increase or decrease the number of pods in a replication controller, deployment, replica set, or stateful set based on observed CPU utilization. Users can specify the CPU utilization target to enable the controller to adjust the number of replicas.

  Source: [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) in the Kubernetes documentation

- ingress

  An ingress is a collection of rules that allow inbound connections to reach the cluster services.

  Source: [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) in the Kubernetes Concepts documentation

- instance group

  An instance group is a collection of virtual machine instances. The instance groups lets you easily monitor and control the group of virtual machines together.

  Source: [Instance groups](https://cloud.google.com/compute/docs/instance-groups/) in the Google Cloud documentation

- instance template

  An instance template is a global API resource to create VM instances and managed instance groups. Instance templates define instance properties such as machine type, image, zone, labels, and so on. They are very helpful in replicating the environments.

  Source: [Instance templates](https://cloud.google.com/compute/docs/instance-templates/) in the Google Cloud documentation

- kubectl

  The kubectl command-line tool supports several different ways to create and manage Kubernetes objects.

  Source: [Kubernetes Object Management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/) in the Kubernetes Concepts documentation

- kube-controller-manager

  The Kubernetes controller manager embeds core controllers shipped with Kubernetes. Each controller is a separate process. To reduce complexity, the controllers are compiled into a single binary and run in a single process.

  Source: [kube-controller-manager](https://kubernetes.io/docs/reference/generated/kube-controller-manager/) in the Kubernetes Reference documentation

* kubelet

  A kubelet is an agent that runs on each node in the cluster. It ensures that containers are running in a pod.

  Source: [kubelet](https://kubernetes.io/docs/concepts/overview/components/#kubelet) in the Kubernetes Concepts documentation

* kube-scheduler

  The `kube-scheduler` component is on the master node. It watches for newly created pods that do not have a node assigned to them, and selects a node for them to run on.

  Source: [kube-scheduler](https://kubernetes.io/docs/concepts/overview/components/#kube-scheduler) in the Kubernetes Concepts documentation

* Kubernetes

  Kubernetes is an open source platform designed to automate deploying, scaling, and operating application containers.

  Source: [Overview](https://kubernetes.io/docs/concepts/overview/) in the Kubernetes Concepts documentation

* Kubernetes DNS

  A Kubernetes DNS pod is a pod used by the kubelets and the individual containers to resolve DNS names in the cluster.

  Source: [DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) in the Kubernetes Concepts documentation

* Kubernetes namespace

  Kubernetes supports multiple virtual clusters backed by the same physical cluster. A Kubernetes namespace is a virtual cluster that provides a way to divide cluster resources between multiple users. Kubernetes starts with three initial namespaces:

  * **`default`**: The default namespace for user created objects which don't have a namespace.

  * **`kube-system`**: The namespace for objects created by the Kubernetes system.

  * **`kube-public`**: The automatically created namespace that is readable by all users.

  Source: [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) in the Kubernetes Concepts documentation

* Let's Encrypt

  Let's Encrypt is a free, automated, and open certificate authority.

  Source: [Let's Encrypt website](https://letsencrypt.org/)

* Microsoft Azure

  Microsoft Azure is the Microsoft cloud platform, including infrastructure as a service (IaaS) and platform as a service (PaaS) offerings.

  Source: [What is Azure?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-azure) in the Microsoft Azure documentation

* network policy

  A Kubernetes network policy specifies how groups of pods are allowed to communicate with each other and with other network endpoints.

  Source: [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) in the Kubernetes Concepts documentation

* node (Kubernetes)

  A Kubernetes node is a virtual or physical machine in the cluster. Each node is managed by the master components and includes the services needed to run the pods.

  Source: [Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) in the Kubernetes documentation

* node controller (Kubernetes)

  A Kubernetes node controller is a Kubernetes master component that manages various aspects of the nodes, such as lifecycle operations, operational status, and maintaining an internal list of nodes.

  Source: [Node Controller](https://kubernetes.io/docs/concepts/architecture/nodes/#node-controller) in the Kubernetes Concepts documentation

* node pool (Kubernetes)

  A Kubernetes node pool is a collection of nodes with the same configuration. At the time of creating a cluster, all the nodes created in the `default` node pool. You can create your custom node pools for configuring specific nodes that have different resource requirements such as memory, CPU, and disk types.

  Source: [About node pools](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools) in the Google Kubernetes Engine (GKE) documentation

* persistent volume

  A persistent volume (PV) is a piece of storage in the cluster that has been provisioned by an administrator. It is a resource in the cluster just like a node is a cluster resource. PVs are volume plugins that have a lifecycle independent of any individual pod that uses the PV.

  Source: [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) in the Kubernetes Concepts documentation

* persistent volume claim

  A persistent volume claim (PVC) is a request for storage by a user. A PVC specifies size and access modes such as:

  * Mounted once for read and write access

  * Mounted many times for read-only access

  Source: [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) in the Kubernetes Concepts documentation

* pod anti-affinity (Kubernetes)

  Kubernetes pod anti-affinity constrains which nodes can run your pod, based on labels on the pods that are already running on the node, rather than based on labels on nodes. Pod anti-affinity lets you control the spread of workload across nodes and also isolate failures to nodes.

  Source: [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#inter-pod-affinity-and-anti-affinity-beta-feature) in the Kubernetes Concepts documentation

* pod (Kubernetes)

  A Kubernetes pod is the smallest, most basic deployable object in Kubernetes. A pod represents a single instance of a running process in a cluster. Containers within a pod share an IP address and port space.

  Source: [Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/#understanding-pods) in the Kubernetes Concepts documentation

* region (Azure)

  An Azure region, also known as a location, is an area within a geography, containing one or more data centers.

  Source: [region](https://docs.microsoft.com/en-us/azure/azure-glossary-cloud-terminology#region) in the Microsoft Azure glossary

* replication controller (Kubernetes)

  A replication controller ensures that a specified number of Kubernetes pod replicas are running at any one time. The replication controller ensures that a pod or a homogeneous set of pods is always up and available.

  Source: [ReplicationController](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/) in the Kubernetes Concepts documentation

* resource group (Azure)

  A resource group is a container that holds related resources for an application. The resource group can include all the resources for an application, or only those resources that are logically grouped together.

  Source: [resource group](https://docs.microsoft.com/en-us/azure/azure-glossary-cloud-terminology#resource-group) in the Microsoft Azure glossary

* secret (Kubernetes)

  A Kubernetes secret is a secure object that stores sensitive data, such as passwords, OAuth 2.0 tokens, and SSH keys in your clusters.

  Source: [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) in the Kubernetes Concepts documentation

* security group (AWS)

  A security group acts as a virtual firewall that controls the traffic for one or more compute instances.

  Source: [Amazon EC2 security groups for Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) in the AWS documentation

* service (Kubernetes)

  A Kubernetes service is an abstraction that defines a logical set of pods and a policy by which to access them. This is sometimes called a microservice.

  Source: [Service](https://kubernetes.io/docs/concepts/services-networking/service/) in the Kubernetes Concepts documentation

* service principal (Azure)

  An Azure service principal is an identity created for use with applications, hosted services, and automated tools to access Azure resources. Service principals let applications access resources with the restrictions imposed by the assigned roles instead of accessing resources as a fully privileged user.

  Source: [Create an Azure service principal with Azure PowerShell](https://docs.microsoft.com/en-us/powershell/azure/create-azure-service-principal-azureps?view=azps-2.4.0) in the Microsoft Azure PowerShell documentation

* shard

  Sharding is a way of partitioning directory data so that the load can be shared by multiple directory servers. Each data partition, also known as a shard, exposes the same set of naming contexts, but only a subset of the data. For example, a distribution might have two shards. The first shard contains all users whose names begin with A-M, and the second contains all users whose names begin with N-Z. Both have the same naming context.

  Source: [Class Partition](https://docs.pingidentity.com/pingds/8/_attachments/javadoc/org/opends/server/discovery/Partition.html) in the DS Javadoc

* single-instance ForgeOps deployment

  Refer to [ForgeOps deployment](#forgeops-deployment).

- stack (AWS)

  A stack is a collection of AWS resources that you can manage as a single unit. You can create, update, or delete a collection of resources by using stacks. The [AWS template](#cloudformation-template) defines all the resources in a stack.

  Source: [Working with stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the AWS documentation

- stack set (AWS)

  A stack set is a container for stacks. You can provision stacks across AWS accounts and regions by using a single [AWS template](#cloudformation-template). A single template defines the resources included in each stack of a stack set.

  Source: [StackSets concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html) in the AWS documentation

- subscription (Azure)

  An Azure subscription is used for pricing, billing, and payments for Azure cloud services. Organizations can have multiple Azure subscriptions, and subscriptions can span multiple regions.

  Source: [subscription](https://docs.microsoft.com/en-us/azure/azure-glossary-cloud-terminology#subscription) in the Microsoft Azure glossary

- volume (Kubernetes)

  A Kubernetes volume is a storage volume that has the same lifetime as the pod that encloses it. Consequently, a volume outlives any containers that run within the pod, and data is preserved across container restarts. When a pod ceases to exist, the Kubernetes volume also ceases to exist.

  Source: [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) in the Kubernetes Concepts documentation

- volume snapshot (Kubernetes)

  In Kubernetes, you can copy the content of a persistent volume at a point in time, without having to create a new volume. You can efficiently back up your data using volume snapshots.

  Source: [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) in the Kubernetes Concepts documentation

- VPC (AWS)

  A virtual private cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud.

  Source: [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the AWS documentation

- worker node (AWS)

  An Amazon Elastic Container Service for Kubernetes (Amazon EKS) worker node is a standard compute instance provisioned in Amazon EKS.

  Source: [Self-managed nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html) in the AWS documentation

- workload (Kubernetes)

  A Kubernetes workload is the collection of applications and batch jobs packaged into a container. Before you deploy a workload on a cluster, you must first package the workload into a [container](#container).

  Source: [Workloads](https://kubernetes.io/docs/concepts/workloads) in the Kubernetes Concepts documentation

### Beyond the docs

Useful links that cover topics beyond the scope of this documentation.

#### Development topics

* [Get a full Amster export out of a ForgeOps deployment](https://support.pingidentity.com/s/article/How-do-I-get-a-full-Amster-export-out-of-a-ForgeOps-deployment)

#### Deployment topics

* [Deploy and customize Prometheus, Grafana, and Alertmanager in a ForgeOps deployment](https://github.com/ForgeRock/forgeops/blob/2026.2.1/etc/addons/prometheus#prometheus-and-grafana-deployment)

* [Deploy the platform in a multi-cluster environment using Google Cloud Multi Cluster Ingress and Cloud DNS for GKE](https://github.com/ForgeRock/forgeops-extras/tree/master/samples/multi-cluster/google-cloud/multi-cluster-ingress)

* [Import a certificate into the truststore in a ForgeOps deployment](https://support.pingidentity.com/s/article/How-do-I-import-a-certificate-into-the-truststore-in-a-ForgeOps-deployment) **(Updated)**

* [Enable the IDM workflow in a ForgeOps deployment](https://community.forgerock.com/t/enabling-the-idm-workflow-with-forgeops-v7-x/3949)

* [ForgeOps deployment to minikube on M1 or M2 based Mac running Colima](https://community.forgerock.com/t/deploying-forgeops-to-minikube-on-an-m1-mac-with-colima/3305)

#### DS topics

* DS script guide

  * [An overview of DS scripts to customize, build, and deploy DS Docker images](https://community.forgerock.com/t/forgeops-ds-script-guide-7-4-7-5/5522)

  * []()The `ds/ds-new/ldif-ext` directory now contains subdirectories matching each DS backend setup-profile. This makes it easier for customers to add custom ldap configuration for backends without having to manipulate the `ds-setup.sh` script.

    Customers can now just add their custom files in:

    * `ldif-ext/am-config/` for the `` am-config` `` backend

    * `ldif-ext/identities/` for the `identities` backend

    * `ldif-ext/tokens/` for the `tokens` backend

    * `ldif-ext/idm-repo/` for the `openidm` backend

* Synchronization of DS data

  * [Synchronize persistent DS data between ForgeOps deployments](https://support.pingidentity.com/s/article/How-to-Replicate-Persistent-DS-Data-Between-ForgeOps-Deployments-Using-Synchronisation).

#### Troubleshooting

* [Enable and modify the AM logging level](https://community.forgerock.com/t/how-to-enable-and-modify-logging-level-in-forgeops-for-am.html)

* [Enable and modify the IDM logging level](https://community.forgerock.com/t/how-to-enable-and-modify-logging-level-in-forgeops-for-idm/3152)

* [Enable and modify the audit logging level](https://community.forgerock.com/t/how-to-enable-and-modify-audit-logging-in-am-and-idm-for-forgeops/3263)

## End of the consolidated file

***

[1](#_footnoteref_1). Not available on single-instance ForgeOps deployments.[2](#_footnoteref_2). Not available on ForgeOps deployments on minikube.[3](#_footnoteref_3). The Linux version of Homebrew doesn't support installing software it maintains as casks. Because of this, if you're setting up an environment on Linux, you won't be able to use Homebrew to install software in several cases. You'll need to refer to the software's documentation for information about how to install the software on a Linux system.[4](#_footnoteref_4). If you have updated Python3, you should delete the existing virtual environment and create a new one using the updated python3 version: rm -rf .venv && python3 -m venv .venv && ./bin/forgeops configure[5](#_footnoteref_5). The Terraform configuration contains a set of variables under `forgerock` that adds labels required for clusters created by Ping Identity employees. If you're a Ping Identity employee creating a cluster, set values for these variables.[6](#_footnoteref_6). If you have updated Python3, you should delete the existing virtual environment and create a new one using the updated python3 version: rm -rf .venv && python3 -m venv .venv && ./bin/forgeops configure[7](#_footnoteref_7). The Terraform configuration contains a set of variables under `forgerock` that adds labels required for clusters created by Ping Identity employees. If you're a Ping Identity employee creating a cluster, set values for these variables.[8](#_footnoteref_8). If you have updated Python3, you should delete the existing virtual environment and create a new one using the updated python3 version: rm -rf .venv && python3 -m venv .venv && ./bin/forgeops configure[9](#_footnoteref_9). The Terraform configuration contains a set of variables under `forgerock` that adds labels required for clusters created by Ping Identity employees. If you're a Ping Identity employee creating a cluster, set values for these variables.[10](#_footnoteref_10). If you have updated Python3, you should delete the existing virtual environment and create a new one using the updated python3 version: rm -rf .venv && python3 -m venv .venv && ./bin/forgeops configure[11](#_footnoteref_11). For example, systems based on M1 or M2 chipsets.[12](#_footnoteref_12). Installing Prometheus, Grafana, and Alertmanager technology in ForgeOps deployments provides an example of how you might set up monitoring and alerting in a Ping Advanced Identity Software deployment in the cloud. Remember, [ForgeOps deployments are reference implementations.](start/start-here.html#cdm-sandbox) When you [create a project plan](start/start-here.html#planning), you'll need to determine how to monitor and send alerts in your production deployment.[13](#_footnoteref_13). You can use the self-signed issuer provided by ForgeOps for test purposes. For production environments, ForgeOps recommends using a cluster issuer that uses a certificate from a trusted certificate authority (CA).[14](#_footnoteref_14). Installing Prometheus, Grafana, and Alertmanager technology in ForgeOps deployments provides an example of how you might set up monitoring and alerting in a Ping Advanced Identity Software deployment in the cloud. Remember, [ForgeOps deployments are reference implementations.](start/start-here.html#cdm-sandbox) When you [create a project plan](start/start-here.html#planning), you'll need to determine how to monitor and send alerts in your production deployment.[15](#_footnoteref_15). You can use the self-signed issuer provided by ForgeOps for test purposes. For production environments, ForgeOps recommends using a cluster issuer that uses a certificate from a trusted certificate authority (CA).[16](#_footnoteref_16). You can automate logging into ECR every 12 hours by using the `cron` utility.[17](#_footnoteref_17). To access DS, refer to [DS command-line access.](deploy/access.html#ds_command_line_access)[18](#_footnoteref_18). If you prefer to use a different ingress controller, deploy infrastructure in Kubernetes to support it.[19](#_footnoteref_19). Traefik and cert-manager are evolving technologies. Descriptions of these technologies were accurate at the time of this writing, but might differ when you deploy them.[20](#_footnoteref_20). For more information on howto change the default behavior, refer to [the steps for creatingTLS certificate](#mkcert-use).[21](#_footnoteref_21). Use similar steps to modify the schedule and purge delay for the `cts` repository[22](#_footnoteref_22). Change the `ds-cts` parameters to modify the schedule and purge delay for the `cts` repository[23](#_footnoteref_23). To get the access key from the Azure portal, go to your storage account. Under Security + networking on the left navigation menu, select Access keys[24](#_footnoteref_24). The `FROM` statement originally contained `am-cdk` as part of the repository name. Be sure to use `am`, not `am-cdk`, in the revised statement.[25](#_footnoteref_25). The `FROM` statement originally contained `idm-cdk` as part of the repository name. Be sure to use `idm`, not `idm-cdk`, in the revised statement.[26](#_footnoteref_26). Except for the deprecated `amster` component.

---

---
title: Welcome to ForgeOps
description: The Ping Advanced Identity Software provides ForgeOps to help you deploy PingAM, PingDS, PingIDM, and PingGateway collectively in an integrated manner on a cloud platform that runs Kubernetes.
component: forgeops
version: 2026.2
page_id: forgeops::index
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/index.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["_@forgeops::index.adoc"]
section_ids:
  chapters_in_this_documentation: Chapters in this documentation
---

# Welcome to ForgeOps

The Ping Advanced Identity Software provides ForgeOps to help you deploy PingAM, PingDS, PingIDM, and PingGateway collectively in an integrated manner on a cloud platform that runs Kubernetes.

ForgeOps comprises mainly two sets of resources:

* The [forgeops repository](https://github.com/ForgeRock/forgeops.git)

  The repository contains artifacts that let you get a sample Ping Advanced Identity Software deployment up and running quickly. After you get the out-of-the-box deployment running, you can tailor it to explore how you might configure your Kubernetes cluster before you deploy the platform in production.

  ForgeOps deployments have the following characteristics:

  * Fully integrated AM, IDM, and DS installations

  * Multi-zone high availability'\[[1](#_footnotedef_1 "View footnote.")]'

  * Replicated directory services'\[[1](#_footnotedef_1 "View footnote.")]'

  * Ingress configuration'\[[2](#_footnotedef_2 "View footnote.")]'

  * Certificate management

  * Randomly generated secrets with ability to rotate secrets

  * Prometheus monitoring, Grafana reporting, and alert management'\[[1](#_footnotedef_1 "View footnote.")]'

* The [ForgeOps documentation](https://docs.pingidentity.com/forgeops/2026.2)

  The ForgeOps documentation helps you work with ForgeOps deployments:

  * Tells you how you can quickly [create a Kubernetes cluster](setup/overview.html) on Google Cloud, Amazon Web Services (AWS), or Microsoft Azure, [deploy the Ping Advanced Identity Software](deploy/deploy.html), and [access components in the deployment](deploy/access.html).

  * Contains [how-tos for preparing for production deployments](prepare/overview.html) by customizing monitoring, setting alerts, backing up and restoring directory data, modifying the default security configuration, and running lightweight benchmarks to test DS, AM, and IDM performance.

  * Tells you how to [modify the AM and IDM configurations](customize/overview.html) in ForgeOps deployments and create customized Docker images for the Ping Advanced Identity Software.

  * [Keeps you up-to-date with the latest changes to the `forgeops` repository](rn/rn.html).

## Chapters in this documentation

[icon: play-circle, set=fas, size=3x]

#### [Start Here](https://docs.pingidentity.com/forgeops/2026.2/start/start-here.html)

Important considerations for a ForgeOps deployment.

[icon: hands-helping, set=fas, size=3x]

#### [Support](https://docs.pingidentity.com/forgeops/2026.2/start/support.html)

Support options for ForgeOps deployments.

[icon: github, set=fab, size=3x]

#### [Repositories](https://docs.pingidentity.com/forgeops/2026.2/start/repositories.html)

How to use the artifacts in ForgeOps public repositories.

[icon: circle-nodes, set=fas, size=3x]

#### [Setup](https://docs.pingidentity.com/forgeops/2026.2/setup/overview.html)

Create a Kubernetes cluster for a ForgeOps deployment.

[icon: sign-posts-wrench, set=fas, size=3x]

#### [Deploy](https://docs.pingidentity.com/forgeops/2026.2/deploy/overview.html)

Deploy the platform on a Kubernetes cluster.

[icon: sliders, set=fas, size=3x]

#### [Customize](https://docs.pingidentity.com/forgeops/2026.2/customize/overview.html)

Customize AM and IDM configurations.

[icon: tasks, set=fas, size=3x]

#### [Prepare for production](https://docs.pingidentity.com/forgeops/2026.2/prepare/overview.html)

PingGateway, monitoring, security, and benchmarking.

[icon: floppy-disk-circle-arrow-right, set=fas, size=3x]

#### [Backup](https://docs.pingidentity.com/forgeops/2026.2/backup/overview.html)

Backup and restore your data.

[icon: level-up, set=fas, size=3x]

#### [Upgrade](https://docs.pingidentity.com/forgeops/2026.2/upgrade/upgrade-overview.html)

Upgrade or apply a patch to ForgeOps deployments.

[icon: ban-bug, set=fas, size=3x]

#### [Troubleshoot](https://docs.pingidentity.com/forgeops/2026.2/troubleshoot/overview.html)

Troubleshoot problems.

[icon: books, set=fas, size=3x]

#### [Reference](https://docs.pingidentity.com/forgeops/2026.2/reference/overview.html)

Command external references, glossary, articles.

[icon: newspaper, set=fas, size=3x]

#### [Single Page](https://docs.pingidentity.com/forgeops/2026.2/consolidated.html)

This entire documentation set on a single HTML page.

***

[1](#_footnoteref_1). Not available on single-instance ForgeOps deployments.[2](#_footnoteref_2). Not available on ForgeOps deployments on minikube.