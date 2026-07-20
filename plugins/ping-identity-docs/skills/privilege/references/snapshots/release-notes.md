---
title: PingOne Privilege Release Notes
description: Learn about changes to PingOne Privilege.
component: privilege
page_id: privilege:release-notes:index
canonical_url: https://docs.pingidentity.com/privilege/release-notes/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 13, 2026
section_ids:
  version-general-availability: "Version: General Availability"
  release-date-july-13-2026: "Release date: July 13, 2026"
  version-identity-for-ai: "Version: Identity for AI"
  release-date-may-5-2026: "Release date: May 5, 2026"
  version-controlled-release: "Version: Controlled release"
  release-date-february-25-2026: "Release date: February 25, 2026"
---

# PingOne Privilege Release Notes

New features and improvements in PingOne Privilege.

Subscribe to get automatic updates: [icon: rss-square, set=fa][PingOne Privilege Release Notes RSS feed](index.xml)

## Version: General Availability

### Release date: July 13, 2026

New

PingOne Privilege is now generally available. This release marks the official launch of our cloud-based privileged access management (PAM) solution, designed to provide secure, frictionless access for developers and DevOps teams to cloud infrastructure and applications.

## Version: Identity for AI

### Release date: May 5, 2026

New

This release introduces a new suite of features focused on providing secure, just-in-time access for artificial intelligence (AI) agents and developers using AI-powered tools.

* **MCP Gateway**: PingOne Privilege can now act as a security gateway for any service that uses the Model Context Protocol (MCP). This allows organizations to enforce just-in-time, least-privilege access policies for AI agents interacting with sensitive backend services and APIs. Administrators can audit all MCP activity and apply fine-grained access control to individual tools, prompts, and resources.

* **Git Server Integration**: You can now secure access to GitHub and GitLab repositories for both human and AI-driven development. This feature uses the PingOne Privilege SSH Certificate Authority (CA) to mint short-lived certificates, enabling passwordless Git operations. Policies can be configured to map commits to the correct user identity and to optionally block code pushes initiated by AI agents, ensuring that all activity is attributable and secure.

## Version: Controlled release

### Release date: February 25, 2026

New

This is a controlled release of PingOne Privilege that's subject to change.