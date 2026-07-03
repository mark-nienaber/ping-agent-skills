# Using Ping Agent Skills

Detailed guide for installing and using the skills in this repo with Claude Code, Codex, and other agentskills-compatible AI coding tools.

## What This Is

56 Agent Skills, one per Ping Identity docset. Each skill is a router — not a rewrite. It ships:

- `SKILL.md` — activation metadata + task→URL routing table.
- `references/llms.txt` — cached copy of the docset's official `llms.txt` index from Ping.
- `references/snapshots/*.md` — offline fallback single-page dumps of each guide.
- `references/MANIFEST.md` — sync date, source URLs, source type per snapshot, checksums.

At runtime the agent loads `SKILL.md`, picks the exact live `.md` URL from `llms.txt`, `WebFetch`es it, and only reads snapshots when live fetch fails.

## When To Use This Repo

- You already know which Ping product/docset the task targets.
- You want depth: exact API pages, guide-level detail, per-version content.
- You want offline safety: snapshots ship in the repo.

For cross-product routing ("which Ping product handles X?") install [`pingidentity/agent-plugins`](https://github.com/pingidentity/agent-plugins) alongside. Their umbrella skills route; this repo goes deep once the docset is known.

## Install

### Claude Code — marketplace (recommended)

```
/plugin marketplace add mark-nienaber/ping-agent-skills
/plugin install ping-identity-docs@ping-agent-skills
```

Installs the whole `ping-identity-docs` plugin (all 56 skills). Marketplace resolves the repo from GitHub.

### Claude Code — local (pre-marketplace, project-scoped, or selective)

Clone this repo, then:

```bash
scripts/setup-claude.sh                          # symlink all skills → ~/.claude/skills/
scripts/setup-claude.sh pingam pingoneaic        # only listed skills
scripts/setup-claude.sh --copy pingam            # copy instead of symlink
scripts/setup-claude.sh --push /path/to/project  # into <project>/.claude/skills/
scripts/setup-claude.sh --push /path/to/project pingam pingfederate
```

Symlinks are the default so `scripts/sync-all.sh` updates propagate immediately. `--copy` and `--push` copy files (needed for remote machines or environments where symlinks aren't allowed).

### Codex

No marketplace. Symlink via the setup script:

```bash
scripts/setup-codex.sh                          # all → ~/.codex/skills/
scripts/setup-codex.sh pingam pingoneaic        # selective
scripts/setup-codex.sh --push /path/to/project  # into <project>/.codex/skills/
```

Same flags as `setup-claude.sh`.

### Other Agentskills-Compatible Tools

Cursor, Copilot workspace, Gemini CLI, OpenCode all follow the agentskills.io spec. Point them at `plugins/ping-identity-docs/skills/` — each subdirectory is a self-contained skill.

## How Activation Works

Every `SKILL.md` starts with agentskills-compliant frontmatter:

```yaml
---
name: pingam
description: Use when working with PingAM (self-managed Access Management) — authentication trees/journeys, OAuth2/OIDC, SAML2, sessions, realms, Amster, and REST APIs. Routes to live docs.pingidentity.com/pingam Markdown; falls back to bundled snapshots.
license: MIT
---
```

The `description` field is the activation trigger. When you prompt the agent with a task, the agent's harness matches your prompt against every installed skill's description. Matches trigger skill load.

Two implications:

- **Be specific in your prompt.** "Configure OAuth2 in PingAM" beats "set up auth" — the product name in your prompt maps directly to a skill description.
- **Skills don't conflict.** A prompt naming a specific product loads that product's skill; a cross-product prompt may load several.

## Routing Flow

Once a skill is active:

1. Agent reads `SKILL.md` body — includes a task→URL routing table (e.g. "OAuth2 client → `/pingam/8.1/oauth2-guide/`").
2. Agent consults `references/llms.txt` for the exact `.md` page URL matching the task.
3. Agent `WebFetch`es the URL. Ping serves the `.md` alternate for every doc page.
4. On failure (offline, 404, timeout), agent reads `references/snapshots/<guide>.md` — a single-page dump captured at last sync.

Sync frequency: monthly via `scripts/sync-all.sh` (or ad-hoc `scripts/sync-docset.sh <slug>`).

## Skill Inventory

56 enabled skills across two source hosts.

**docs.pingidentity.com:** `auth-node-ref`, `autonomous-identity`, `configuration-guides`, `connectors`, `davinci`, `developer-resources`, `enterprise-connect`, `forgeops`, `glossary`, `identity-governance`, `identity-reporting`, `integrations`, `java-agents`, `licensing-guide`, `openicf`, `pgic`, `pingaccess`, `pingam`, `pingauthorize`, `pingcentral`, `pingdirectory`, `pingds`, `pingfederate`, `pinggateway`, `pingid`, `pingid-user-guide`, `pingidm`, `pingintelligence`, `pingone`, `pingone-admin-mfa-faq`, `pingone-solutions`, `pingoneadvancedservices`, `pingoneaic`, `pingoneforenterprise`, `platform`, `privilege`, `recognize`, `sdks`, `solution-guides`, `web-agents`.

**developer.pingidentity.com:** `build-with-ai`, `config-automation-management-sdks`, `config-automation-promotion`, `devops`, `helm`, `identity-for-ai`, `login-widget`, `orchsdks`, `p14e-directory-api`, `pingauthorize-dev`, `pingdirectory-dev`, `pingid-api`, `pingone-api`, `pingone-api-ea`, `pingoneaic-api`, `terraform`.

**Disabled:** `pingcli` — Ping's `llms.txt` endpoint redirects to 404. Tracking: https://github.com/mark-nienaber/ping-agent-skills/issues/2.

## Composition With `pingidentity/agent-plugins`

Install both when you want product routing + docset depth:

```
/plugin marketplace add pingidentity/agent-plugins
/plugin marketplace add mark-nienaber/ping-agent-skills
```

Typical flows:

| Task type | Umbrella skill | Then depth skill |
|---|---|---|
| Product unknown | `ping-quickstart` | matched product skill |
| Authentication flow design | `ping-orchestration` | `davinci`, `pingoneaic`, `pingam`, `pingfederate` |
| App integration | `ping-app-integration` | `pingone-api`, `sdks`, `login-widget`, `java-agents`, `web-agents` |
| AI-agent identity | `ping-identity-for-ai` | `identity-for-ai`, `pingam`, `pingone-api`, `pingoneaic-api` |
| Config-as-code | `ping-orchestration` | `config-automation-promotion`, `config-automation-management-sdks`, `terraform`, `devops` |

## Example Prompts

Prompts that trigger the right skill and produce grounded output:

- "Using PingAM docs, build an authentication tree that requires WebAuthn after risk score > 60."
- "From the PingOne API reference, show me the request body for creating a worker application, including required scopes."
- "Use PingGateway docs to design a route that protects an MCP server with OAuth2 bearer tokens."
- "In PingOneAIC, what's the ESV promotion flow between staging and production tenants?"
- "Using PingDirectory developer docs, find the SCIM 2.0 endpoint pattern for user lookup by external ID."
- "Compare PingOne Verify and PingOne Protect docs for a risk-based identity proofing flow."
- "Show me the PingFederate SP connection JSON schema for a SAML2 partner."

## Local Maintenance

Refresh cached docs and snapshots:

```bash
scripts/sync-docset.sh pingam              # one docset
scripts/sync-all.sh                        # all enabled docsets
```

Regenerate a `SKILL.md` from cached `llms.txt` (used after sync when routing table needs to update):

```bash
scripts/generate-skill.sh pingam
```

Validate:

```bash
scripts/validate.sh                        # frontmatter + snapshot freshness + link sample
scripts/validate.sh --skip-url-check       # skip live URL sampling
scripts/validate.sh --require-all-enabled  # fail if any enabled docset has no generated skill
```

CI runs `validate.sh` on every PR and a weekly `sync-all.sh` cron commits refreshed snapshots.

## Troubleshooting

- **Skill not triggering:** your prompt likely doesn't name the product. Add "Using PingAM docs" or the exact product name. Check the skill's `description` field to see what phrasing it matches.
- **Live fetch returns 404:** Ping may have moved a page. Snapshot fallback kicks in automatically. Run `scripts/sync-docset.sh <slug>` to re-cache.
- **Snapshot missing:** the docset's guide didn't publish a `single-page.md` at sync time. Sync tool falls back to the first `.md` page in the guide. `references/MANIFEST.md` records the source type.
- **`pingcli` skill absent:** disabled by design (Ping endpoint broken). Track upstream issue.

## Source of Truth

Live: https://docs.pingidentity.com/&lt;docset&gt;/ and https://developer.pingidentity.com/&lt;docset&gt;/. Every doc page has a `.md` alternate. Skills route to those directly.

Ping's agent guidance: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md.

## License

MIT.
