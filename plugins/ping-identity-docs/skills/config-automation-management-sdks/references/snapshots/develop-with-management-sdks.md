---
title: Getting support
description: Find community forum, GitHub issues, and Ping Identity Support options for Ping Identity client SDK projects
component: config-automation-management-sdks
page_id: config-automation-management-sdks::develop_with_management_sdks/getting_support
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/develop_with_management_sdks/getting_support.html
llms_txt: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
---

# Getting support

Ping Identity's SDK client projects are delivered as open-source projects and can be found on [Ping Identity's GitHub account](https://github.com/pingidentity). There are multiple ways of getting support when using Ping Identity's SDK client projects:

* Community forum: The Ping Identity [developer community forum](https://support.pingidentity.com/s/community-home) provides a quick and simple way to interact with an active community of subject matter experts, including Ping Identity technical staff, customer, and partner specialists. The community forum is ideal for specific questions on how best to configure Ping Identity products using the SDK client projects to meet use cases.

* GitHub project issues: Each SDK client project has a GitHub repository where open-source provider code is published, and each repository has the GitHub issues feature enabled. With a GitHub account, anyone can create issues on the relevant project by filling in the provided template. Using GitHub project issues is ideal when requesting new features, enhancements, or reporting unexpected errors or provider bugs. The GitHub issues are closely monitored and are a quick and easy way to interact directly with the project team.

* Ping Identity Support: For customers with an active product license using an SDK client project version of 1.0.0 or later, support tickets can be raised according to the normal Ping Identity Support process. Raising a support ticket is ideal when there is a potential issue with the underlying product, or the issue should be tracked with the account team.

---

---
title: Interface stability
description: Learn how Ping Identity applies Semantic Versioning to major, minor, and patch releases of its client SDK projects
component: config-automation-management-sdks
page_id: config-automation-management-sdks::develop_with_management_sdks/interface_stability
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/develop_with_management_sdks/interface_stability.html
llms_txt: https://developer.pingidentity.com/config-automation-management-sdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  breaking-changes: Breaking changes
---

# Interface stability

To provide predictability and stability when developing with Ping Identity's client SDKs, Ping Identity's development practices follow the Semantic Versioning 2.0.0 methodology set out at [Semver.org](https://semver.org).

This includes a regular cadence of major, minor, and patch versions of each client project. Releases are issued on the respective GitHub code repositories using [GitHub's Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) feature. Changelogs are compiled into release notes on each release and provide a list of resolved issues, enhancements, new features, general updates, and any breaking changes that might cause developers to alter their application project code in order to use the update.

High-level descriptions of the release types are:

* Major releases: Typically once every year or couple of years. Major releases are issued when significant changes are made to the client project and typically require customers to change their application project code, otherwise known as breaking changes.

* Minor releases: Typically on a planned schedule, such as every few weeks or aligned with product releases. Minor releases are issued when the providers are enhanced with additional, optional functionality and can also include planned bug fixes.

* Patch releases: Typically ad-hoc, patch releases are issued between minor releases when bug fixes or documentation updates must be released before the next minor release.

Learn more about major, minor, and patch releases at [Semver.org](https://semver.org)

## Breaking changes

Breaking changes to a Ping SDK client project typically require the developer to make changes to the written application code before they can use the update.

Breaking changes could be required periodically to ensure Ping Identity's client projects remain aligned with the product API. Significant breaking changes are typically planned in advance to be released in-bulk in the major release cycle.

As part of Ping Identity's development practices, breaking changes are kept to a minimum and are planned as technical debt in the major release cycle. It's uncommon for breaking changes to occur in minor and patch releases except when a project is not yet released to version 1.0.

Occasionally, breaking changes cannot be included in the major release cycle and must be included in a minor release to ensure that the SDK client project functions correctly. These breaking changes are marked clearly in the release notes.

Some examples of breaking changes are: \* Scheduled removal of previously deprecated functionality. \* Renaming functions, methods, or data structures without following a deprecation path. \* Renaming or removing data-structure fields without following a deprecation path. \* Changing an "Optional" field to be "Required" in a function signature.

When breaking changes are made to an SDK client project, these are highlighted in the release notes. If the change requires significant rework of application project code, the corrective action cannot be included in the release note, or if there are many breaking changes to be handled, then a specific guide might be created and published to assist with the conversion process. Upgrade and migration guides are typically created for major releases.