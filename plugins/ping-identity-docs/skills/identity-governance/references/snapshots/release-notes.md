---
title: Getting Support
description: Ping Identity provides support services, professional services, training through Ping Identity University, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, see https://www.pingidentity.com.
component: identity-governance
version: 7.1.2
page_id: identity-governance:release-notes:appendix-getting-support
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/appendix-getting-support.html
---

# Getting Support

Ping Identity provides support services, professional services, training through Ping Identity University, and partner services to assist you in setting up and maintaining your deployments. For a general overview of these services, see <https://www.pingidentity.com>.

Ping Identity has staff members around the globe who support our international customers and partners. For details on Ping Identity's support offering, including support plans and service level agreements (SLAs), visit <https://www.pingidentity.com/support>.

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://backstage.pingidentity.com/knowledge/kb) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Identity software.

  While many articles are visible to community members, Ping Identity customers have access to much more, including advanced information for customers using Ping Identity software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

---

---
title: Known Issues
description: There are no known issues in this release.
component: identity-governance
version: 7.1.2
page_id: identity-governance:release-notes:chap-known-issues
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/chap-known-issues.html
---

# Known Issues

There are no known issues in this release.

---

---
title: Release Levels and Interface Stability
description: Ping Identity defines Major, Minor, and Patch product release levels. The release level is reflected in the version number. The release level tells you what sort of compatibility changes to expect.
component: identity-governance
version: 7.1.2
page_id: identity-governance:release-notes:appendix-interface-stability
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/appendix-interface-stability.html
section_ids:
  interface-stability: Ping Identity Product Stability Labels
---

# Release Levels and Interface Stability

Ping Identity defines Major, Minor, and Patch product release levels. The release level is reflected in the version number. The release level tells you what sort of compatibility changes to expect.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Identity Governance uses a different version numbering system from other Ping Identity products. The version number use the following format: `Major.Minor.Patch`, where *Major* is the year of the release, *Minor* is the month of the release, *Patch* is the number beginning with 0, and increases for each patch release.Thus, for this release of Identity Governance, the version number is **7.1.2**. |

**Release Level Definitions**

| Release Label | Version Numbers   | Characteristics                                                                                                                                                                                                                     |
| ------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Major         | Version: x\[.0.0] | \* Bring major new features, minor features, and bug fixes\* Can include changes even to Stable interfaces\* Major indicates the version, for example, `7`.                                                                         |
| Minor         | Version: x.y\[.0] | \* Bring minor features, and bug fixes\* Can include backwards-compatibile changes to Stable interfaces in the same Major release, and incompatible changes to Evolving interfaces\* Minor indicates the version, for example, `1`. |
| Patch         | Version: x.y.z    | \* Bring bug fixes\* Are intended to be fully compatible with previous versions from the same Minor release\* Patch starts with `0` and increases for each bug fix release                                                          |

## Ping Identity Product Stability Labels

Ping Identity products support many features, protocols, APIs, GUIs, and command-line interfaces. Some of these are standard and very stable. Others offer new functionality that is continuing to evolve.

Ping Identity acknowledges that you invest in these features and interfaces, and therefore must know when and how Ping Identity expects them to change. For that reason, Ping Identity defines stability labels and uses these definitions in Ping Identity products.

**Ping Identity Stability Label Definitions**

| Stability Label       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stable                | This documented feature or interface is expected to undergo backwards-compatible changes only for major releases. Changes may be announced at least one minor release before they take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Evolving              | This documented feature or interface is continuing to evolve and so is expected to change, potentially in backwards-incompatible ways even in a minor release. Changes are documented at the time of product release.While new protocols and APIs are still in the process of standardization, they are Evolving. This applies for example to recent Internet-Draft implementations, and also to newly developed functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Legacy                | This feature or interface has been replaced with an improved version, and is no longer receiving development effort from Ping Identity.You should migrate to the newer version, however the existing functionality will remain.Legacy features or interfaces will be marked as *Deprecated* if they are scheduled to be removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Deprecated            | This feature or interface is deprecated and likely to be removed in a future release. For previously stable features or interfaces, the change was likely announced in a previous release. Deprecated features or interfaces will be removed from Ping Identity products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Removed               | This feature or interface was deprecated in a previous release and has now been removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Technology Preview    | Technology previews provide access to new features that are considered as new technology that is not yet supported. Technology preview features may be functionally incomplete and the function as implemented is subject to change without notice. DO NOT DEPLOY A TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.Customers are encouraged to test drive the technology preview features in a non-production environment and are welcome to make comments and suggestions about the features in the associated forums.Ping Identity does not guarantee that a technology preview feature will be present in future releases, the final complete version of the feature is liable to change between preview and the final version. Once a technology preview moves into the completed version, said feature will become part of the Ping Identity platform. Technology previews are provided on an "AS-IS" basis for evaluation purposes only and Ping Identity accepts no liability or obligations for the use thereof. |
| Internal/Undocumented | Internal and undocumented features or interfaces can change without notice. If you depend on one of these features or interfaces, contact Ping Identity support or email link:mailto:info\@Ping Identity.com\[info\@Ping Identity.com] to discuss your needs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

---

---
title: Release Notes
description: These release notes are intended to provide information to administrators and evaluators of the ForgeRock Identity Governance. All information is accurate at the time of publication and updates will be provided by ForgeRock with subsequent software releases.
component: identity-governance
version: 7.1.2
page_id: identity-governance:release-notes:preface
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/preface.html
page_aliases: ["index.adoc", "_@identity-governance::index.adoc"]
---

# Release Notes

These release notes are intended to provide information to administrators and evaluators of the ForgeRock Identity Governance. All information is accurate at the time of publication and updates will be provided by ForgeRock with subsequent software releases.

[icon: newspaper, set=fas, size=3x]

#### [What's New](chap-whats-new.html)

Learn about what's new in this release.

[icon: cogs, set=fas, size=3x]

#### [Before You Start](chap-before-you-install.html)

Learn about the requirements for running Identity Governance software in production.

[icon: asterisk, set=fas, size=3x]

#### [Fixes, Limitations, Known Issues](chap-key-fixes.html)

Learn about the fixes, limitations, and known issues in this release.

[icon: sync, set=fas, size=3x]

#### [Compatibility](chap-compatibility.html)

Learn about major and minor changes to existing, deprecated, and removed functionality.

[icon: book, set=fas, size=3x]

#### [Check Doc Updates](chap-doc-updates.html)

Track important changes to the documentation.

[icon: life-ring, set=fas, size=3x]

#### [Get Support](appendix-getting-support.html)

Find out where to get professional support and training.

---

---
title: What&#8217;s New in 7.1.2
description: Ping® Identity Governance 7.1.2 is a major self-managed software release that centralized management of access requests, certifications, segregation of duties, and other important compliance and security tasks.
component: identity-governance
version: 7.1.2
page_id: identity-governance:release-notes:chap-whats-new
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/release-notes/chap-whats-new.html
section_ids:
  whats_new_in_7_1_1: What's New in 7.1.1
---

# What's New in 7.1.2

Ping® Identity Governance 7.1.2 is a major self-managed software release that centralized management of access requests, certifications, segregation of duties, and other important compliance and security tasks.

Identity Governance 7.1.2 doesn't introduce any new features, only [fixes](chap-changelog.html).

## What's New in 7.1.1

The following new major features and functionality were introduced in Identity Governance 7.1.1:

* **Reassign tasks in access review**: In previous versions of IGA, only administrator users were able to reassign campaign events from one certifier to another. In patch release 7.1.1, end users can run reassignments on their own if the system settings are configured to allow them. Configure as an administrator to view this access as a certifier.

* **Enhanced certification filtering**: Users can now filter on multiple columns at once in their access review line-items.

Other important features are as follows:

* **Unified user interface**. Both Identity Governance and Access Request components now exist within the same UI context.

* **Custom request form fields**. Administrators can define custom request fields using multiple input types and assign them to requestable objects to dynamically create custom request forms.

* **Custom request workflow support**. In addition to the standard request process, administrators can assign custom BPMN workflows or Javascript scripts to requestable objects to control the request process for individual items.

* **Requests for removal of access**. End users can now create requests for the removal of a given requestable item.

* **Expanded requestable item options**.In addition to IDM managed objects, administrators can now set generic IDM attributes as well as disconnected system entitlements to be requestable by users.

* **Add consults to tasks**. Approvers can reach out to another user or group to ask them for additional insight or information in order to help make their approval decision.

* **Manual provisioning tasks**. For any requestable item that requires manual provisioning steps, such as disconnected system entitlements, a manual provisioner can be assigned as a final step of the process to complete provisioning of any item.

* **File attachments**. End users have the ability to attach file uploads to an in-flight request either as a requirement to create the request or as supplemental information from the requester, requestee, approver, or consult.

* **End user task reassignment**. When enabled, approvers will be able to reassign a given approval task to another end user or group of their choosing. In addition, approval tasks will now follow the same delegation pattern introduced in Identity Governance 3.0 when configured by administrators.

* **Pre-request and provisioning script hooks**. Administrators can define automated scripts to run any pre-processing logic on a request for access, as well as to automate any additional logic or steps to the provisioning process.

* **Policy validations against requests**. When enabled, any request that would violate an existing policy as defined in Identity Governance if approved, will be not allowed to be submitted. End users will be informed of what potential policy violation would occur and a description of the policy, so that their request can be adjusted if need be.

* **Autonomous Identity integration**. Administrators can configure system settings to allow Identity Governance to work in conjunction with Ping Identity Autonomous Identity to provide additional insights to certifiers and approvers within certifications and requests. Items that have recommendations available from AutoID will be marked with a recommendation to approve/certify or reject/revoke, as well as a confidence score for that suggestion.

* **Scripted certification and policy remediation**. In addition to being able to use the IDM BPMN workflow functionality to remediate revoked access or policy violations, administrators now also have the option to use a scripted remediation process.