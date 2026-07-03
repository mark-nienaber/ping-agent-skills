---
title: Computer-Using Agents (CUAs)
description: A computer-using agent (CUA) is an AI agent that operates computers through human interfaces like GUIs or CLIs, rather than structured APIs.
component: identity-for-ai
page_id: identity-for-ai:agents:idai-computer-using-agents
canonical_url: https://developer.pingidentity.com/identity-for-ai/agents/idai-computer-using-agents.html
revdate: October 9, 2025
keywords: ["computer-using agents", "AI agent", "GUI automation", "CLI automation", "browser automation"]
section_ids:
  how-cuas-differ-from-api-driven-agents: How CUAs differ from API-driven agents
---

# Computer-Using Agents (CUAs)

A computer-using agent (CUA) is an agent that operates a computer like a human would, interacting with graphical user interfaces (GUIs) and command-line interfaces (CLIs) instead of structured APIs.

Using techniques like computer vision and accessibility hooks to navigate screens, CUAs can simulate mouse clicks, keystrokes, or terminal commands to perform tasks.

## How CUAs differ from API-driven agents

The following table highlights key differences between API-driven agents and CUAs across identity, security, and operational categories. This comparison shows why CUAs introduce unique security challenges compared to API-based approaches.

| Category                     | API-driven agents                                                     | CUAs                                                                  |
| ---------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Interface type               | Structured, machine-readable APIs                                     | Human-facing GUIs and CLIs                                            |
| Stability and resilience     | Predictable, versioned, and contract-based                            | Minor UI changes can easily break workflows                           |
| Authentication model         | Modern standards such as OAuth 2.0, OIDC, or workload identities      | Human-style logins (usernames, passwords, shared bot accounts)        |
| Authorization model          | Fine-grained, least-privilege policies enforceable at the API layer   | Broad access after sign-on; difficult to constrain privileges         |
| Auditability and attribution | Actions tied to unique workload identities or service principals      | Shared accounts reduce accountability and audit clarity               |
| Execution environment        | Cloud-native or service-based runtimes                                | Local desktops, VMs, or RDP sessions                                  |
| Security posture             | Supports IAM-native controls (short-lived tokens, conditional access) | Often relies on long-lived sessions vulnerable to hijacking or replay |
| Best suited for              | Modern systems with robust API coverage                               | Legacy, desktop, or closed-source applications without APIs           |
