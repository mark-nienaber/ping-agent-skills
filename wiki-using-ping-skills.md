# Using Ping Agent Skills

This page explains how to use this repo with AI coding agents.

## What To Install

Install `pingidentity/agent-plugins` when you want broad Ping platform routing and high-level solution guidance. Install this repo when you want deep access to every generated Ping documentation docset.

Most users should install both:

```bash
/plugin marketplace add https://github.com/pingidentity/agent-plugins
/plugin marketplace add https://github.com/mark-nienaber/ping-agent-skills
```

For local development before marketplace publishing:

```bash
./setup-claude.sh pingam pingoneaic pingone-api
./setup-codex.sh pingam pingoneaic pingone-api
```

## How The Skills Work

Each skill contains:

- `SKILL.md` with activation metadata and routing instructions.
- `references/llms.txt` copied from Ping's per-docset `llms.txt`.
- `references/snapshots/*.md` for offline fallback.
- `references/MANIFEST.md` with sync date, source URLs, source type, and checksums.

Agents should load `SKILL.md`, use the routing table and `llms.txt` to choose exact live `.md` pages, and fetch live Ping docs first. Snapshots are fallback only.

## Example Prompts

- "Use PingAM docs to configure OAuth2 token exchange for an AI agent."
- "Find the PingOne API page for creating a worker application and explain the required scopes."
- "Use PingGateway docs to build a route that protects an MCP server."
- "Compare PingOne Verify and PingOne Protect docs for a risk-based identity proofing flow."
- "Use the PingDirectory developer docs to find the SCIM API pattern for user lookup."

## Known Gap

`pingcli` is not generated yet. Ping's developer root index advertises `https://developer.pingidentity.com/pingcli/llms.txt`, but that endpoint redirects to `/pingcli/1.1/llms.txt`, which returns 404. The registry disables this docset until https://github.com/mark-nienaber/ping-agent-skills/issues/2 is resolved.
