---
title: Auditing and Reviewing Changes
description: The audit and review process before accepting and deploying changes provide a gate for human interaction and validation of new features. This stage should provide a view of the differences between the current and desired configurations. To do this effectively, engineers should have a clear format to interpret configuration exports and determine the functional intention of changes. The audit and review process should enforce protection against users pushing through unverified changes and encourage the reviewer to check and revalidate compliance with all other areas mentioned in previous sections.
component: config-automation-promotion
page_id: config-automation-promotion:concepts:auditing_and_reviewing_changes
canonical_url: https://developer.pingidentity.com/config-automation-promotion/concepts/auditing_and_reviewing_changes.html
revdate: March 24, 2025
---

# Auditing and Reviewing Changes

The audit and review process before accepting and deploying changes provide a gate for human interaction and validation of new features. This stage should provide a view of the differences between the current and desired configurations. To do this effectively, engineers should have a clear format to interpret configuration exports and determine the functional intention of changes. The audit and review process should enforce protection against users pushing through unverified changes and encourage the reviewer to check and revalidate compliance with all other areas mentioned in previous sections.

Forms of auditing and review of changes include:

* GitHub pull request (PR) with reviewers.

* QA engineer reviewing configuration within the UI of an automatically deployed Ping Identity solution.
