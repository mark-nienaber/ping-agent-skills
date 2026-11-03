---
description: See Using release tags for more information.
component: devops
page_id: devops::docker-images/README
canonical_url: https://developer.pingidentity.com/devops/docker-images/README.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

See [Using release tags](releaseTags.html) for more information.

---

---
title: Container Docker Images Information
description: Introduce the per-image Docker documentation set covering related images, ports, environment variables, deployment, and tagging
component: devops
page_id: devops::docker-images/dockerImagesRef
canonical_url: https://developer.pingidentity.com/devops/docker-images/dockerImagesRef.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-image-information: Image Information
---

# Container Docker Images Information

## Image Information

These documents for Ping Identity Docker images include information on:

* Related Docker images

* Ports exposed for the containers

* Environment variables for the image

* Associated deployment information

* Tagging methodology and support policy

The image-specific documentation is generated from each new build ensuring these documents align with any changes over time.

|   |                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When deploying Ping products in containers, please consider the information found [here on storage options](../reference/awsStorage.html). |

Older images based on product versions that are no longer supported under our policy are removed from Docker Hub. See the [support policy page](imageSupport.html) for details.

As with many organizations, Ping Identity uses *floating* Docker image tags. This practice means, for example, that the **`edge`** tag does not refer to the same image over time as product updates occur. The [release tags](releaseTags.html) page has information on the `edge` and other tags, how often they are updated, and how to ensure the use of a particular version and release of a product image.

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you want to be notified when new versions of product Docker images are available, see the **Docker Images** section of the [FAQ page](../reference/faqs.html) for instructions on following the docker-builds GitHub repository. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For FedRAMP certification and other United States government compliance, Ping Identity partners to build and host highly-secured images at Iron Bank that are compliant with the increased security requirements. More information is provided in the [FAQ](../reference/faqs.html) section of this documentation. The Iron Bank images are available on the [Iron Bank](https://docs-ironbank.dso.mil/) repository and are not provided on Docker Hub. |

---

---
title: Evaluation of Docker Base Image Security
description: Compare Alpine Linux against Ubuntu, CentOS, and RHEL7 for Docker base image security to explain why Ping Identity uses Alpine
component: devops
page_id: devops::docker-images/dockerImageSecurity
canonical_url: https://developer.pingidentity.com/devops/docker-images/dockerImageSecurity.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-evaluation-of-docker-base-image-security: Evaluation of Docker Base Image Security
  devops-evaluation-overview: Evaluation overview
  devops-image-size: Image size
  devops-number-of-packages-installed: Number of packages installed
  devops-number-of-historical-cves: Number of historical CVEs
  devops-number-of-vulnerabilities-reported-by-clair: Number of vulnerabilities reported by Clair
  devops-final-evaluation-results: Final evaluation results
  devops-references: References
---

# Evaluation of Docker Base Image Security

## Evaluation of Docker Base Image Security

In the Center for Internet Security (CIS) [Docker Benchmark v1.2.0](https://www.cisecurity.org/benchmark/docker/), one of the recommendations says, "4.3 Ensure that unnecessary packages are not installed in the container."

It further states, "You should consider using a minimal base image rather than the standard Red Hat/CentOS/Debian images if you can. Some of the options available include BusyBox and Alpine."

The following sections present security aspects of different Linux distributions compared to Alpine Docker image. This doesn't necessarily mean that one is the best for Docker base images. Other factors, such as usability and compatibility, should also be considered when choosing the most suitable Docker image for an organization.

### Evaluation overview

To evaluate Alpine's security, we compared it with the following popular Linux distributions: Ubuntu, CentOS, and Red Hat Enterprise Linux 7.

For this comparison, we used the latest version, as of March 12, 2020, of each distribution's Docker image and compared them in four different categories:

* Image size

* Number of packages installed by default

* Number of historical vulnerabilities reported on [cvedetails.com](https://www.cvedetails.com/)

* Number of vulnerabilities reported by the Clair scan

The following table summarizes the numbers for each distribution.

|                                             | Alpine        | Ubuntu       | CentOS                | RHEL7         |
| ------------------------------------------- | ------------- | ------------ | --------------------- | ------------- |
| Image Version                               | alpine:3.11.3 | ubuntu:18.04 | centos:centos8.1.1911 | rhel7:7.7-481 |
| Image Size                                  | 5.59MB        | 64.2MB       | 237MB                 | 205MB         |
| Number of Packages Installed                | 14            | 89           | 173                   | 162           |
| Number of Historical CVE\*s                 | 2             | 2007         | 2                     | 662           |
| Number of Vulnerabilities Reported by Clair | 0             | 32           | 7                     | 0             |

> \*CVE - Common Vulnerabilities and Exposures

### Image size

Alpine has an advantage in image size. Although smaller size doesn't directly translate into better security, the smaller size does mean less code packed into the image, which means smaller attack surface.

### Number of packages installed

Because of Alpine's smaller size, Alpine has the fewest packages out of box. Fewer packages means lesser chance of having vulnerabilities in the dependencies, which is a plus for security.

### Number of historical CVEs

Alpine and CentOS both rank highest in number of historical CVEs even though CentOS has a close relationship with RHEL7, and RHEL7 has 600+ reported vulnerabilities.

### Number of vulnerabilities reported by Clair

Some vulnerabilities reported by Clair might not be real issues, but their presence does mean extra overhead for developers or security teams to triage these findings. This overhead can be avoided if unnecessary dependencies are excluded from the image in the first place.

### Final evaluation results

Although none of the four categories is perfect on its own for evaluating the security of a Linux distribution, in combination, **Alpine** presents greater advantages for use, which is why we selected it as the disribution for all of our Docker images.

### References

* [CIS Docker Benchmarks](https://www.cisecurity.org/benchmark/docker/)

* [Alpine CVEs](https://www.cvedetails.com/product/38838/Alpinelinux-Alpine-Linux.html?vendor_id=16697)

* [Ubuntu CVEs](https://www.cvedetails.com/product/20550/Canonical-Ubuntu-Linux.html?vendor_id=4781)

* [CentOS CVEs](https://www.cvedetails.com/product/18131/Centos-Centos.html?vendor_id=10167)

* [Redhat Enterprise Linux CVEs](https://www.cvedetails.com/product/78/Redhat-Enterprise-Linux.html?vendor_id=25)

---

---
title: Flex Images
description: Explain Ping container images published with the flex tag suffix, their simplified operational model, and migration considerations
component: devops
page_id: devops::docker-images/flexImages
canonical_url: https://developer.pingidentity.com/devops/docker-images/flexImages.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-flex-images: Flex Images
  devops-flex-images-overview: Overview
  devops-flex-images-background: Background
  devops-flex-images-what-is-flex: "What \"flex\" means"
  devops-flex-images-what-is-changing: What is changing
  devops-flex-images-what-is-not-changing: What is not changing
  devops-flex-images-migration: Migration
  devops-flex-images-signatures: Image signatures
---

# Flex Images

## Flex Images

### Overview

Ping container images published with a **-flex** tag suffix represent a new generation of images designed to be more cloud-friendly, easier to operate, and better aligned with standard container practices.

Flex images **are not drop-in replacements for current images**. Current and flex images will coexist for an extended period so customers can adopt the new model deliberately, on their own timeline.

### Background

As Ping moved its legacy products — such as PingFederate, PingDirectory, and PingAccess — into container-based operations, some patterns emerged that were useful early on but added complexity that impacted modern testing, staging, and production environments. Examples include:

* Layered configuration behavior that makes it hard to accurately determine how a product is configured at runtime

* Container lifecycle hook scripts rather than relying on the product to manage its own container behavior

* Log handling that does not always align naturally with container platforms

Addressing these issues required improvements to both the products themselves and the design of the container images. For example, recent product versions can be configured through environment variables, reducing dependence on configuration files. The image design has been reworked accordingly as the internal **V2 image** effort.

### What "flex" means

In this context, **flex** refers to the simplified operational model for the image itself — cleaner container behavior, clearer runtime expectations, and a design that better fits modern orchestration environments.

Improvements in flex images include:

* Simplified image structure and runtime behavior

* Reduced dependence on startup hooks and file manipulation at launch

* Reduced or eliminated need for profile overlays to configure products

* Reduced startup and restart times

* Removal of non-critical components such as integration kits for some products

* Simplified upgrade paths in container environments

### What is changing

Customers will begin to see new images published with a **-flex** tag suffix on Docker Hub and other container registries, starting with PingFederate. For example:

```shell
pingidentity/pingfederate:13.0.3-alpine-flex
```

These images reflect the broader container direction for Ping products.

### What is not changing

Current images will continue to have the same release cycle with the same tags they have had to this point, using a primary YYMM tag (for example, `2608`). Existing automation and workflows using these images will continue to operate unchanged even as the new flex images arrive.

See [Using Release Tags](releaseTags.html) for tag format details.

### Migration

Flex images are not a drop-in replacement. Plan for a deliberate migration rather than a tag swap.

* For PingFederate, see [Migrating PingFederate Deployments to Flex Images](migratePingFederateFlex.html) for a demonstration walkthrough using the Helm example values.

More detailed guidance for other products will be published as the rollout continues, covering:

* Migration considerations and guides for moving from current to flex images per product

* Known limitations and support expectations

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Ping encourages moving to flex images to gain improved efficiency, operational simplicity, and better alignment with product support lifecycles. Timing is at your discretion; both image lines are supported during the transition. |

### Image signatures

Flex images are signed with Cosign using the same KMS-backed key as current images. See [Image Signature Verification](imageSignatureVerification.html) for verification steps.

---

---
title: Image Signature Verification
description: Describe how to verify Ping container image signatures using Cosign and the published KMS-backed signing key
component: devops
page_id: devops::docker-images/imageSignatureVerification
canonical_url: https://developer.pingidentity.com/devops/docker-images/imageSignatureVerification.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-image-signature-verification: Image signature verification
  devops-image-signature-verification-summary: Summary
  devops-image-signature-verification-details: Details
  devops-image-signature-verification-steps: Verification steps
  devops-image-signature-step-1: Step 1 — Download and verify the public key fingerprint
  devops-image-signature-step-2: Step 2 — Pull the image and get its digest
  devops-image-signature-step-3: Step 3 — Verify the image signature
  devops-image-signature-expected-output: Expected output
  devops-image-signature-common-errors: Common errors
  devops-image-signature-which-images: Which images are signed?
---

# Image Signature Verification

## Image signature verification

### Summary

For verification of Ping container images, use the Cosign utility along with the published Ping image signing trust material to verify by image digest. This process ensures the provenance of the image. If your environment requires policy enforcement, add verification to your promotion or deployment pipeline before the image is admitted to production.

### Details

Provenance of software artifacts is a key component of ensuring the integrity and security of your environments. Container images are no different, and Ping recognizes this requirement and has taken steps to ensure your confidence.

Ping container images were historically signed using Docker Content Trust, which Docker deprecated in 2025. As of May 2026, Ping container images published to Docker Hub are signed with a utility known as **Cosign** using a managed KMS-backed signing key.

These Cosign signatures provide an extra layer of security, ensuring that images you pull were built and published by Ping. The following sections outline what Ping is doing and how you as a consumer of Ping container images can ensure that you are using our images.

The necessary information you will need to verify images can be found at two locations:

* <https://download.pingidentity.com/public/security.txt>

* <https://download.pingidentity.com/public/ping-cosign-prod-v1.pub>

The first link includes verification details for Ping product zip files as well as container images. The second link contains the public key needed to validate the images. This information will be kept current; if the signing key is rotated in the future, these files will be updated with the new public key and fingerprint. Any such changes will be announced in multiple channels when they happen.

Verification uses the public key corresponding to the private key active at the time the image was signed. Ping has implemented asymmetric KMS-backed verification as its method of validation. To verify images, you will need the [Cosign application installed](https://docs.sigstore.dev/cosign/system_config/installation/).

As recommended by [Sigstore](https://github.com/sigstore/cosign), signing is performed on the digest rather than a tag, meaning that you should also verify by digest. While tags can move, a digest identifies the exact image manifest that was signed.

|   |                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Since Ping signs with a private key rather than Sigstore's keyless flow, no entries are written to the Rekor transparency log. This practice is why `--insecure-ignore-tlog` is required in all `cosign verify` commands below. |

Signatures include an optional set of annotations:

* **signer.key.label** — the alias associated with the signing key; useful for troubleshooting and human recognition, not a security gate

* **signer.key.fingerprint.sha256** — the SHA-256 fingerprint of the public key; can be used to confirm you have the correct public key

### Verification steps

#### Step 1 — Download and verify the public key fingerprint

```shell
curl -O https://download.pingidentity.com/public/ping-cosign-prod-v1.pub

openssl pkey -pubin -in ping-cosign-prod-v1.pub -outform DER | \
  openssl dgst -sha256 | awk '{print $2}'
# Expected: a0047fc42c554bc105fed4642bab36eb1f5871b810a2c5115664f508958fe586
```

#### Step 2 — Pull the image and get its digest

PingFederate 2605 is used as an example.

```shell
docker pull pingidentity/pingfederate:2605
docker inspect --format='{{index .RepoDigests 0}}' pingidentity/pingfederate:2605
# or if you have crane installed
crane digest docker.io/pingidentity/pingfederate:2605
```

#### Step 3 — Verify the image signature

```shell
cosign verify \
  --key ping-cosign-prod-v1.pub \
  --insecure-ignore-tlog \
  docker.io/pingidentity/pingfederate@sha256:<digest>
```

Example using PingDirectory 2605:

```shell
cosign verify \
  --key ping-cosign-prod-v1.pub \
  --insecure-ignore-tlog \
  docker.io/pingidentity/pingdirectory@sha256:f9a83da90d2fd254f9b95b0f30148edaac61bb2a2dce2c1cf65a532f12320d1a
```

### Expected output

A successful verification produces output similar to the following. The only difference from actual output is that the JSON block has been formatted for easier readability:

```json
Verification for docker.io/pingidentity/pingdirectory@sha256:f9a83da90d2fd254f9b95b0f30148edaac61bb2a2dce2c1cf65a532f12320d1a --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - The signatures were verified against the specified public key

[
  {
    "critical": {
      "identity": {
        "docker-reference": "index.docker.io/pingidentity/pingdirectory"
      },
      "image": {
        "docker-manifest-digest": "sha256:f9a83da90d2fd254f9b95b0f30148edaac61bb2a2dce2c1cf65a532f12320d1a"
      },
      "type": "cosign container image signature"
    },
    "optional": {
      "signer.key.fingerprint.sha256": "a0047fc42c554bc105fed4642bab36eb1f5871b810a2c5115664f508958fe586",
      "signer.key.label": "alias/product-container-image-production-signing-key"
    }
  }
]
```

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some images published before June 2026 had duplicate signatures applied during pipeline processing. If you see repeated output blocks, there is no security concern; the pipelines have since been corrected. |

### Common errors

| Error                                  | Meaning                                                                                                                                                          |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `no signatures found`                  | Image is not signed — confirm you are using a multi-arch manifest tag, not a per-arch tag.                                                                       |
| `no matching signatures`               | Wrong public key — re-download from the canonical URL above and verify the fingerprint.                                                                          |
| `error: signing config or tlog errors` | Transparency log lookup failed. Ping images are signed with a private key and have no Rekor entry. Add `--insecure-ignore-tlog` to your `cosign verify` command. |

### Which images are signed?

Signed images are multi-arch manifests published to Docker Hub and archived images in Artifactory, beginning with the 2605 sprint release. [Flex images](flexImages.html) are also signed using the same key.

---

---
title: Migrating PingFederate Deployments to Flex Images
description: Migrate PingFederate deployments from the current image line to flex images with the ping-devops Helm chart, using the bridge and minimal-profile example values
component: devops
page_id: devops::docker-images/migratePingFederateFlex
canonical_url: https://developer.pingidentity.com/devops/docker-images/migratePingFederateFlex.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-pf-flex-migration-overview: Before you begin
  devops-pf-flex-migration-prerequisites: Prerequisites
  devops-pf-flex-migration-common-setup: Common setup
  devops-pf-flex-migration-choose-path: Choose a migration path
  devops-pf-flex-migration-path-a: "Path A: bridge an existing full server profile"
  devops-pf-flex-migration-verify: Verify the deployment
  devops-pf-flex-migration-path-b: "Path B: move to a minimal, flex-native profile"
  devops-pf-flex-migration-private-repos: Private profile repositories
  devops-pf-flex-migration-what-changes: What changes from the legacy model
  devops-pf-flex-migration-reduce-profile: Reducing the profile
  devops-pf-flex-migration-clustered: Clustered deployments
  devops-pf-flex-migration-openshift: OpenShift and Helm considerations
  devops-pf-flex-migration-sequence: Suggested migration sequence
  devops-pf-flex-migration-troubleshooting: Troubleshooting
  devops-pf-flex-migration-support: Support boundaries
  devops-pf-flex-migration-cleanup: Cleaning up
---

# Migrating PingFederate Deployments to Flex Images

This walkthrough expands the [Flex Images](flexImages.html) overview into a complete sample migration for PingFederate using the `ping-devops` Helm chart and the [PingFederate flex example values](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/pingfederate-flex) in the `pingidentity-devops-getting-started` repository.

## Before you begin

PingFederate flex images use a simplified container runtime model designed for modern orchestration platforms. They reduce reliance on image startup hooks and runtime file manipulation, and support configuration through environment variables and selected file mounts.

Flex images are **not drop-in replacements** for the current PingFederate image line. Existing deployments may depend on startup hooks, automatic server-profile retrieval, profile overlays, or filesystem assumptions that differ in flex. Plan and validate a deliberate migration above and beyond simply changing the image tag. Current and flex image lines can coexist during migration (the same product code will be operating in each set); select and pin the image tag that you have tested.

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The example values used in this walkthrough are for demonstration and are not suitable for production use without modification. Validate startup, probes, licensing, persistence, and clustering in a non-production environment before cutover. See [Support boundaries](#devops-pf-flex-migration-support). |

## Prerequisites

* A Kubernetes cluster and Helm 3+

* [`ping-devops` Helm chart](https://developer.pingidentity.com/helm/getting-started/index.html) version `0.14.0` or later (this guide was validated on `0.16.0`). Charts require explicit flex probe commands and literal Secret/ConfigMap names in sidecars.

* A valid PingFederate license file. Flex images do not use the DevOps license-server flow; the license is delivered as a file mounted at `/opt/staging/license`.

* For Examples 5 and 6 from the getting-started repository, a default StorageClass capable of ReadWriteOnce volumes (the admin console requests a 4Gi PVC).

* The [`30-helm/pingfederate-flex` example directory](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/pingfederate-flex) checked out locally.

If necessary, add the chart repository:

```shell
helm repo add pingidentity https://helm.pingidentity.com/
helm repo update
```

## Common setup

Create the namespace, Secrets, and ConfigMap that every flex example consumes. Run these commands from the `30-helm/pingfederate-flex` directory.

```shell
kubectl create namespace ping

# DevOps secret: used by Example 5's bootstrap sidecar, and carries the
# PING_IDENTITY_ACCEPT_EULA setting over from the v1 pattern.
kubectl create secret generic devops-secret -n ping \
  --from-literal=PING_IDENTITY_ACCEPT_EULA='YES' \
  --from-literal=PING_IDENTITY_PASSWORD='<admin-password>'

# Credential secret: used by Example 6's bootstrap sidecar.
kubectl create secret generic pingfederate-admin-creds -n ping \
  --from-literal=PING_IDENTITY_PASSWORD='<admin-password>'

# License secret: mounted at /opt/staging/license.
kubectl create secret generic pingfederate-license -n ping \
  --from-file=license=./pingfederate.lic

# Bootstrap script ConfigMap: mounted into the flex-bootstrap sidecar.
kubectl create configmap flex-bootstrap-script -n ping \
  --from-file=flex-bootstrap.sh=./flex-bootstrap.sh
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Flex images ship without the former hook-script system, so there is no mechanism in the image that accepts the license agreement or creates the initial administrator. The `flex-bootstrap` sidecar performs both actions over the Admin API after PingFederate starts, mirroring what the legacy image's post-start hooks did. It waits up to 900 seconds for the admin API — a budget tied to the examples' startup probe window. |

## Choose a migration path

### Path A: bridge an existing full server profile

Use the full-profile staging pattern when you need to keep an existing Git-hosted server profile while beginning the migration. An init container stages the profile before PingFederate starts. For deployments that persist runtime data, keep the durable PVC separate from temporary profile staging and mount it only at the intended data path.

This is a **transitional compatibility pattern**, not the preferred end state: staging the full runtime and overlaying a full profile can mask the image runtime and couple profile contents to the image tag. Keep the image and profile version-aligned, and plan to reduce the profile over time.

Start with [Example 5: server profile with PVC](https://github.com/pingidentity/pingidentity-devops-getting-started/blob/master/30-helm/pingfederate-flex/05-server-profile-pvc.yaml). For a deployment without a PVC, see Examples 3 and 4 in the [example directory](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/pingfederate-flex).

What Example 5 does:

* Runs the admin console as a StatefulSet so chart-generated persistence is available (charts at least through `0.16.0` tie StatefulSet persistence to StatefulSet workloads only; the PingFederate admin defaults to a Deployment).

* Remaps the PVC from the chart's default `/opt/out` mount to exactly `/opt/pingidentity/runtime/server/default/data` — the single durable path the flex image actually writes (the flex image has no `/opt/out` convention).

* Seeds the PVC on first start: the flex image ships a populated data-directory seed (base config store, embedded database), and an empty PVC mounted at that path hides the seed and prevents startup. A `seed-pvc-data` init container copies the seed in exactly once; later pods leave existing data intact.

* Keeps profile staging in a separate ephemeral `emptyDir` that is rebuilt on every pod creation, while the PVC survives pod deletion and Helm upgrades.

Install it:

```shell
helm install pf-flex pingidentity/ping-devops -n ping \
  -f 05-server-profile-pvc.yaml
```

### Verify the deployment

Use the same checks for Path A and Path B. The following assumes the release name `pf-flex`; adjust for your release.

```shell
# Both admin and engine pods reach Running.
kubectl get pods -n ping -l app.kubernetes.io/instance=pf-flex

# The bootstrap sidecar reports completion.
kubectl logs -n ping sts/pf-flex-pingfederate-admin -c flex-bootstrap --tail=5
# Expected final line: Bootstrap complete.

# Heartbeat responds on the admin port.
kubectl port-forward -n ping sts/pf-flex-pingfederate-admin 9999:9999
# In a second shell:
curl -sk https://localhost:9999/pf/heartbeat.ping
```

Sign in to the admin console at `https://localhost:9999` as the bootstrap administrator to confirm licensing and initial configuration.

Confirm persistence for the PVC examples:

```shell
kubectl get pvc -n ping
kubectl exec -n ping sts/pf-flex-pingfederate-admin -- \
  ls /opt/pingidentity/runtime/server/default/data
```

The data directory exists on first start and holds the runtime data PingFederate writes (key material, `config-store/`, the embedded database); it persists across pod deletion and `helm upgrade`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Flex images keep all durable state under `/opt/pingidentity/runtime/server/default/data` — not the v1 `/opt/out/instance/server/default/data` path. The image ships that directory pre-populated with its base configuration seed, so mounting an **empty** volume at the path also breaks startup ("Unable to locate configuration list value …​"). Mount the PVC at the runtime data path as the examples do, and seed it on first start (the examples' `seed-pvc-data` init container handles this). |

### Path B: move to a minimal, flex-native profile

Move scalar settings into supported environment variables and retain only files that cannot be represented through environment variables. Stage those files separately and mount only the individual files needed by the product. Do not mount the profile over the flex image runtime directory: a directory mount can hide files supplied by the image.

For deployments with persistent runtime data, use [Example 6: minimal profile with PVC](https://github.com/pingidentity/pingidentity-devops-getting-started/blob/master/30-helm/pingfederate-flex/06-minimal-server-profile-pvc.yaml). The PVC remains at `/opt/pingidentity/runtime/server/default/data`; profile staging is temporary and rebuilt when a pod is created. For deployments without a PVC, see Example 4 in the [example directory](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/pingfederate-flex).

What Example 6 does:

* Does not mount anything over the image's `/opt/pingidentity/runtime` — the image stays authoritative for the runtime, and only verified profile artifacts are delivered as individual file mounts with `subPath`. (The one exception is the durable data directory: the PVC is mounted there and seeded on first start, so runtime state persists.)

* Seeds the PVC data directory exactly once via a `seed-pvc-data` init container, for the same reason as Example 5.

* Delivers scalar settings as environment variables (`PF_RUN_<property>` for `run.properties` settings, `PF_<FILE>_<property>` for other config files), rendered by the chart into its env-vars ConfigMap.

* Pins the profile Git ref to a commit and asserts it before staging, so pod creation fails fast if the pin no longer matches.

Install it with the same release name after deleting the Path A release, or into a separate namespace for comparison:

```shell
helm install pf-flex pingidentity/ping-devops -n ping \
  -f 06-minimal-server-profile-pvc.yaml
```

Then repeat the checks in [Verify the deployment](#devops-pf-flex-migration-verify).

### Private profile repositories

The staging init container in Example 6 clones the profile repository with Git. For a private repository, create a credential Secret and pass it to the init container:

```shell
kubectl create secret generic pf-profile-git -n ping \
  --from-literal=username='<git-username>' \
  --from-literal=password='<git-token>'
```

Uncomment the `GIT_USERNAME`/`GIT_PASSWORD` environment entries in the example's `stage-server-profile` init container, set `GIT_TERMINAL_PROMPT=0`, and configure a Git credential helper that reads those variables. Keep the `SERVER_PROFILE_REF` pinned to a commit so staging stays deterministic.

## What changes from the legacy model

* Flex images do not use the legacy hook system. Work previously performed by hooks — such as staging configuration or post-start bootstrap — must be handled through the documented flex deployment pattern.

* Flex does not automatically retrieve and merge a Git-hosted server profile through the legacy `SERVER_PROFILE_*` startup flow. Use an init container or another supported staging method, then deliver only the required artifacts.

* Durable application/runtime data must be kept distinct from ephemeral configuration staging. Do not use the staging volume as the persistence mechanism.

* Flex-specific paths and health probes shown in the examples (`/opt/pingidentity/runtime/bin/liveness.sh`) will vary from the previous model. See the example [README](https://github.com/pingidentity/pingidentity-devops-getting-started/blob/master/30-helm/pingfederate-flex/README.md) prerequisites for the Helm chart, license, credentials, ConfigMaps, and storage.

## Reducing the profile

Once the bridge (Path A) is stable, shrink the profile toward the Path B target:

1. Inventory every file the profile delivers and classify each as a scalar setting, a required filesystem artifact, or obsolete.

2. Move supported scalar values to environment variables in the `container.env`/`envs` blocks; the chart renders them into the product env-vars ConfigMap.

3. Keep only files that cannot be represented as environment variables (for example, drop-in deployer artifacts or custom XML) and deliver each as an individual file mount.

4. Update the staging init container to copy only those files, and extend its assertions (`test -f`, `test -s`) so staging fails fast on drift.

File-mounting rules:

* One `volumeMounts` entry per file. `mountPath` is the same path under `/opt/pingidentity/runtime`; `subPath` mirrors the repository path.

* Never mount a directory over image-populated directories (`conf/`, `bin/`, `lib/`) — a directory mount hides the image's own files. Directory mounts are safe only where the image directory is empty.

* For drop-in deployer artifacts, mount the drop-in-deployer **directory**, not `data.zip` itself: PingFederate renames the file to `data.zip.deployed` after import, which fails if the file is a mount point.

* The init container must create every `subPath` source before the main container starts.

## Clustered deployments

The examples use standalone operation. For clustered consoles and engines, see [Example 2](https://github.com/pingidentity/pingidentity-devops-getting-started/blob/master/30-helm/pingfederate-flex/02-clustered.yaml) and [Example 4](https://github.com/pingidentity/pingidentity-devops-getting-started/blob/master/30-helm/pingfederate-flex/04-minimal-server-profile.yaml), which deliver `jgroups.properties` (DNS_PING discovery) and `cluster-admin-nodes-sync.conf` as files — environment-variable overrides do not work on either file in flex.

|   |                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The admin cluster Service FQDN in `jgroups.properties` must match your release name and namespace exactly. Create the `pingfederate-cluster-config` ConfigMap with the helper script before installing a clustered example:```shell
./create-cluster-config.sh <release-name> <namespace>
```Without working DNS_PING discovery, every admin pod self-promotes to ACTIVE (split-brain). |

In clustered mode, engine containers additionally need the uppercase `RUN_PF_OPERATIONAL_MODE` variable, which the flex `liveness.sh` reads to select the engine heartbeat port (see Example 4).

## OpenShift and Helm considerations

Use the [OpenShift overlay](https://github.com/pingidentity/pingidentity-devops-getting-started/blob/master/30-helm/pingfederate-flex/openshift-overlay.yaml) and deployment settings documented with the example values — it removes the chart's hardcoded `runAsUser`/`fsGroup` values that OpenShift rejects. Add `-f openshift-overlay.yaml` to the install command alongside the main example values file.

Validate the security context, file ownership and permissions, startup command, probes, Secrets, PVC behavior, and profile staging in a non-production environment before cutover. Do not assume values that worked with a legacy image behave identically with flex.

The Ping Helm charts through at least `0.16.0` do not render sidecar values through templating, so keep Secret and ConfigMap names in sidecar blocks literal. They also hardcode `OPERATIONAL_MODE` in the product env ConfigMap, which is why the examples set both `PF_RUN_pf_operational_mode` and `OPERATIONAL_MODE`.

## Suggested migration sequence

1. Inventory current image tags, Helm chart version, server-profile repository and ref, hook scripts, mounted paths, persisted data, Secrets, and OpenShift constraints.

2. Pin a flex image version and test it in a non-production environment; keep the existing image deployment available for rollback under its own release name.

3. If needed, begin with the full-profile bridge example and keep durable data on its separate PVC.

4. Validate startup, health probes, licensing, bootstrap, configuration, clustering (if applicable), and persistence.

5. Reduce the profile: move supported scalar values to environment variables and identify only the required filesystem artifacts.

6. Switch to the minimal-profile example, verify upgrades and rollback behavior, then promote through the normal release process.

Do not point a flex deployment and the legacy deployment at the same PVC. The examples create a new PVC for the flex release; moving existing runtime data into it is deployment-specific and should be validated separately.

## Troubleshooting

* **Bootstrap sidecar gives up while PingFederate is still starting.** The sidecar waits 900 seconds, matched to the startup probe window (`failureThreshold: 90` x `periodSeconds: 10`). If you change the probe, update the retry budget in `flex-bootstrap.sh` to match.

* **Administrator creation returns 422 repeatedly.** PingFederate can report the heartbeat before the administrative-account resource finishes initializing; the sidecar retries this transient response. Persistent non-422 errors indicate a real failure — inspect the Admin API response.

* **Administrator creation returns 401.** The credential Secret's password does not match, or the administrator already exists with different credentials. The sidecar verifies the configured credentials before declaring success; check the Secret the sidecar actually reads (Example 5 uses `devops-secret`, Example 6 uses `pingfederate-admin-creds`).

* **Clustered admin consoles all report ACTIVE.** DNS_PING discovery is not resolving peers. Recreate the `pingfederate-cluster-config` ConfigMap with the exact release name and namespace, then restart the pods.

* **Engine pods never become ready in clustered mode.** Set `RUN_PF_OPERATIONAL_MODE` on the engine container so the flex liveness script selects the engine heartbeat port.

* **A drop-in artifact fails to import.** Mount the drop-in-deployer directory rather than the `data.zip` file, which PingFederate renames after import.

* **Configuration files appear to be missing after an image upgrade.** It is possible a directory mount is shadowing image-supplied files; replace it with individual file mounts.

## Support boundaries

* The example values are demonstrations and may need modification before production use. Confirm the sample image tag (`13.1.4-alpine-flex` at the time of writing), the chart-version floor, and the OpenShift overlay instructions against the [current released examples](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/30-helm/pingfederate-flex) and the chart release notes before adopting them.

* Product-version-specific guidance about where supported settings belong — and which files must remain in the profile — follows the PingFederate product documentation for your version.

* Distinguish image behavior changes from deployment misconfiguration when requesting support: hook absence, probe paths, and profile staging are image model changes; split-brain, mount shadowing, and probe budget mismatches are configuration issues addressed above.

* This guidance describes a general migration pattern. It does not promise specific vulnerability reductions or universal compatibility for every deployment.

## Cleaning up

```shell
helm uninstall pf-flex -n ping
```

Deleting the namespace also deletes the Secrets, ConfigMap, and (subject to the StorageClass reclaim policy) the PVC created during the walkthrough.

---

---
title: Ping Identity DevOps <code>apache-jmeter</code> Hook - <code>04-check-variables.sh</code>
description: This document is auto-generated from apache-jmeter/opt/staging/hooks/04-check-variables.sh
component: devops
page_id: devops::docker-images/apache-jmeter/hooks/04-check-variables.sh
canonical_url: https://developer.pingidentity.com/devops/docker-images/apache-jmeter/hooks/04-check-variables.sh.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `apache-jmeter` Hook - `04-check-variables.sh`

***

This document is auto-generated from *[apache-jmeter/opt/staging/hooks/04-check-variables.sh](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/apache-jmeter/opt/staging/hooks/04-check-variables.sh)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>apache-jmeter</code> Hook - <code>17-check-license.sh</code>
description: This document is auto-generated from apache-jmeter/opt/staging/hooks/17-check-license.sh
component: devops
page_id: devops::docker-images/apache-jmeter/hooks/17-check-license.sh
canonical_url: https://developer.pingidentity.com/devops/docker-images/apache-jmeter/hooks/17-check-license.sh.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `apache-jmeter` Hook - `17-check-license.sh`

***

This document is auto-generated from *[apache-jmeter/opt/staging/hooks/17-check-license.sh](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/apache-jmeter/opt/staging/hooks/17-check-license.sh)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>apache-jmeter</code> Hook - <code>LICENSE</code>
description: This document is auto-generated from apache-jmeter/opt/staging/hooks/LICENSE
component: devops
page_id: devops::docker-images/apache-jmeter/hooks/LICENSE
canonical_url: https://developer.pingidentity.com/devops/docker-images/apache-jmeter/hooks/LICENSE.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `apache-jmeter` Hook - `LICENSE`

***

This document is auto-generated from *[apache-jmeter/opt/staging/hooks/LICENSE](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/apache-jmeter/opt/staging/hooks/LICENSE)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>apache-jmeter</code> Hooks
description: List of available hooks:
component: devops
page_id: devops::docker-images/apache-jmeter/hooks/README
canonical_url: https://developer.pingidentity.com/devops/docker-images/apache-jmeter/hooks/README.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `apache-jmeter` Hooks

List of available hooks:

* [04-check-variables.sh](04-check-variables.sh.html)

* [17-check-license.sh](17-check-license.sh.html)

* [LICENSE](LICENSE.html)

***

This document is auto-generated from *[apache-jmeter/opt/staging/hooks](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/apache-jmeter/opt/staging/hooks)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>ldap-sdk-tools</code> Hooks
description: There are no default hooks defined for the ldap-sdk-tools image.
component: devops
page_id: devops::docker-images/ldap-sdk-tools/hooks/README
canonical_url: https://developer.pingidentity.com/devops/docker-images/ldap-sdk-tools/hooks/README.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `ldap-sdk-tools` Hooks

There are no default hooks defined for the `ldap-sdk-tools` image.

***

This document is auto-generated from *[ldap-sdk-tools/Dockerfile](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/ldap-sdk-tools/Dockerfile)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>04-check-variables.sh.pre</code>
description: This document is auto-generated from pingaccess/opt/staging/hooks/04-check-variables.sh.pre
component: devops
page_id: devops::docker-images/pingaccess/hooks/04-check-variables.sh.pre
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/04-check-variables.sh.pre.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `04-check-variables.sh.pre`

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/04-check-variables.sh.pre](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/04-check-variables.sh.pre)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>20-restart-sequence.sh.pre</code>
description: This document is auto-generated from pingaccess/opt/staging/hooks/20-restart-sequence.sh.pre
component: devops
page_id: devops::docker-images/pingaccess/hooks/20-restart-sequence.sh.pre
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/20-restart-sequence.sh.pre.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `20-restart-sequence.sh.pre`

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/20-restart-sequence.sh.pre](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/20-restart-sequence.sh.pre)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>50-before-post-start.sh</code>
description: This is called after the start or restart sequence has finished and before the server within the container starts
component: devops
page_id: devops::docker-images/pingaccess/hooks/50-before-post-start.sh
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/50-before-post-start.sh.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `50-before-post-start.sh`

This is called after the start or restart sequence has finished and before the server within the container starts

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/50-before-post-start.sh](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/50-before-post-start.sh)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>51-add-engine.sh</code>
description: This script is started in the background immediately before the server within the container is started
component: devops
page_id: devops::docker-images/pingaccess/hooks/51-add-engine.sh
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/51-add-engine.sh.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `51-add-engine.sh`

This script is started in the background immediately before the server within the container is started

This is useful to implement any logic that needs to occur after the server is up and running

For example, enabling replication in PingDirectory, initializing Sync Pipes in PingDataSync or issuing admin API calls to PingFederate or PingAccess

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/51-add-engine.sh](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/51-add-engine.sh)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>80-post-start.sh</code>
description: This script is used to import any configurations that are needed after PingAccess starts
component: devops
page_id: devops::docker-images/pingaccess/hooks/80-post-start.sh
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/80-post-start.sh.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `80-post-start.sh`

This script is used to import any configurations that are needed after PingAccess starts

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/80-post-start.sh](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/80-post-start.sh)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>81-after-start-process.sh</code>
description: This document is auto-generated from pingaccess/opt/staging/hooks/81-after-start-process.sh
component: devops
page_id: devops::docker-images/pingaccess/hooks/81-after-start-process.sh
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/81-after-start-process.sh.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `81-after-start-process.sh`

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/81-after-start-process.sh](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/81-after-start-process.sh)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>83-change-password.sh</code>
description: This document is auto-generated from pingaccess/opt/staging/hooks/83-change-password.sh
component: devops
page_id: devops::docker-images/pingaccess/hooks/83-change-password.sh
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/83-change-password.sh.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `83-change-password.sh`

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/83-change-password.sh](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/83-change-password.sh)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>85-import-configuration.sh</code>
description: This script is started in the background immediately before the server within the container is started
component: devops
page_id: devops::docker-images/pingaccess/hooks/85-import-configuration.sh
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/85-import-configuration.sh.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `85-import-configuration.sh`

This script is started in the background immediately before the server within the container is started

This is useful to implement any logic that needs to occur after the server is up and running

For example, enabling replication in PingDirectory, initializing Sync Pipes in PingDataSync or issuing admin API calls to PingFederate or PingAccess

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/85-import-configuration.sh](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/85-import-configuration.sh)*

Copyright © 2026 Ping Identity Corporation

---

---
title: Ping Identity DevOps <code>pingaccess</code> Hook - <code>LICENSE</code>
description: This document is auto-generated from pingaccess/opt/staging/hooks/LICENSE
component: devops
page_id: devops::docker-images/pingaccess/hooks/LICENSE
canonical_url: https://developer.pingidentity.com/devops/docker-images/pingaccess/hooks/LICENSE.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Ping Identity DevOps `pingaccess` Hook - `LICENSE`

***

This document is auto-generated from *[pingaccess/opt/staging/hooks/LICENSE](https://github.com/pingidentity/pingidentity-docker-builds/blob/master/pingaccess/opt/staging/hooks/LICENSE)*

Copyright © 2026 Ping Identity Corporation