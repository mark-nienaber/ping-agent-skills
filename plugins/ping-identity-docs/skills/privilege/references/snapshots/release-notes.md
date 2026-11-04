---
title: PingOne Privilege Release Notes
description: Release notes for the PingOne Privilege Platform.
component: privilege
page_id: privilege:release-notes:index
canonical_url: https://docs.pingidentity.com/privilege/release-notes/index.html
llms_txt: https://docs.pingidentity.com/privilege/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 13, 2026
section_ids:
  2026: 2026
  july-2026: July 2026
  july-13: July 13
  general-availability: General availability
  may-2026: May 2026
  may-5: May 5
  identity-for-ai: Identity for AI
  mcp-gateway: MCP gateway
  git-server-integration: Git server integration
  february-2026: February 2026
  february-25: February 25
  controlled-release: Controlled release
---

# PingOne Privilege Release Notes

New features and improvements in PingOne Privilege.

Subscribe to get automatic updates: [icon: rss-square, set=fa][PingOne Privilege Release Notes RSS feed](index.xml)

## 2026

### July 2026

#### July 13

##### General availability

New PingOne Privilege

PingOne Privilege is now generally available. This release provides secure, passwordless, just-in-time access to cloud infrastructure and resources for administrators and developers. It includes two complementary products: Human Privilege provides human access to privileged resources, while Agent Privilege secures the AI agents acting on behalf of your users.

### May 2026

#### May 5

##### Identity for AI

New PingOne Privilege

This release introduces a new suite of features focused on providing secure, just-in-time access for artificial intelligence (AI) agents and developers using AI-powered tools.

###### MCP gateway

PingOne Privilege can now act as a security gateway for any service that uses the Model Context Protocol (MCP). This allows organizations to enforce just-in-time, least-privilege access policies for AI agents interacting with sensitive backend services and APIs. Administrators can audit all MCP activity and apply fine-grained access control to individual tools, prompts, and resources.

###### Git server integration

You can now secure access to GitHub and GitLab repositories for both human and AI-driven development. This feature uses the PingOne Privilege SSH Certificate Authority (CA) to mint short-lived certificates, enabling passwordless Git operations. Policies can be configured to map commits to the correct user identity and to optionally block code pushes initiated by AI agents, ensuring that all activity is attributable and secure.

### February 2026

#### February 25

##### Controlled release

New PingOne Privilege

This is a controlled release of PingOne Privilege that's subject to change.