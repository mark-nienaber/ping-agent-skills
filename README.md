# Ping Agent Skills

Agent Skills for Ping Identity documentation. Each skill is a thin router to Ping's official Markdown docs: it reads a cached `llms.txt`, selects the right live `.md` URL, and falls back to committed snapshots when offline.

Use this repo when you want docset-level depth: exact API pages, guide-level detail, per-version content, and offline safety. For cross-product "which Ping product do I need?" routing, use [`pingidentity/agent-plugins`](https://github.com/pingidentity/agent-plugins) alongside this repo.

## Coverage

- 57 docsets registered in `scripts/docsets.yaml`; 56 enabled.
- 56 skills generated under `plugins/ping-identity-docs/skills/`.
- `pingcli` disabled: `https://developer.pingidentity.com/pingcli/llms.txt` redirects to a 404. Tracking: https://github.com/mark-nienaber/ping-agent-skills/issues/2.
- Snapshot footprint ~19 MB.
- Numeric-version docsets pinned via `preferred_version` in `scripts/docsets.yaml`.

Each generated skill contains:

- `SKILL.md`: activation metadata, fetch strategy, and task-to-route table.
- `references/llms.txt`: cached copy of the official Ping `llms.txt` index.
- `references/snapshots/*.md`: local fallback Markdown snapshots.
- `references/MANIFEST.md`: sync date, source URLs, source type, and checksums.

## Install

### Claude Code Marketplace

```bash
/plugin marketplace add mark-nienaber/ping-agent-skills
/plugin install ping-identity-docs@ping-agent-skills
```

### Claude Code Local

```bash
scripts/setup-claude.sh                          # symlink all skills to ~/.claude/skills/
scripts/setup-claude.sh pingam pingoneaic        # symlink selected skills
scripts/setup-claude.sh --copy pingam            # copy instead of symlink
scripts/setup-claude.sh --push /path/to/project  # copy into <project>/.claude/skills/
```

Symlinks are the default so local syncs and regenerated skills are visible immediately. Use `--copy` or `--push` for remote machines or environments where symlinks are not suitable.

### Codex

```bash
scripts/setup-codex.sh                          # symlink all skills to ~/.codex/skills/
scripts/setup-codex.sh pingam pingoneaic        # symlink selected skills
scripts/setup-codex.sh --copy pingam            # copy instead of symlink
scripts/setup-codex.sh --push /path/to/project  # copy into <project>/.codex/skills/
```

### Other Agentskills-Compatible Tools

Point the tool at `plugins/ping-identity-docs/skills/`. Each subdirectory is a self-contained skill.

## How Skills Resolve Docs

1. The agent loads the matching product skill from `SKILL.md`.
2. The skill's routing table and bundled `references/llms.txt` identify the official live `.md` page.
3. The agent fetches the live Ping Markdown URL.
4. If live fetch is unavailable, the agent reads the closest `references/snapshots/<guide>.md` fallback.

The live documentation is the source of truth. Snapshots are committed for offline safety and visible doc drift.

## How Activation Works

Every `SKILL.md` starts with agentskills-compliant frontmatter:

```yaml
---
name: pingam
description: "Use when configuring PingAM access management, authentication journeys, OAuth2/OIDC, SAML2 federation, sessions, security, Amster, REST APIs, or upgrade and install work. Routes to live docs; snapshots fallback."
license: MIT
---
```

The `description` field is the activation trigger. Product-specific prompts produce better routing:

- Good: "Using PingAM docs, configure OAuth2 client authentication."
- Weaker: "Set up auth."

Cross-product prompts may load multiple Ping skills. Use `pingidentity/agent-plugins` first when the product is unknown, then use this repo for product-specific depth.

## Headless Alignment

This repo supports Ping's headless approach, but it is not limited to pure headless implementation work. The skills are deliberately UI-neutral: they route an agent to API, SDK, orchestration, policy, and product documentation instead of assuming hosted sign-on pages, embedded widgets, or any specific application framework.

For headless app work, the most relevant docsets are:

- `orchsdks`: Journey, DaVinci, and OIDC orchestration SDK concepts.
- `sdks`: Ping SDK entry points and release guidance.
- `pingone-api`: PingOne platform, application, OAuth, MFA, and authorization APIs.
- `pingoneaic-api`: PingOne AIC authentication, OAuth2/OIDC, IDM REST, CREST, and scripting APIs.
- `davinci`, `pingoneaic`, and `pingam`: flow, journey, tree, node, and scripting behavior needed behind the API or SDK integration.

The repo intentionally goes beyond a pure headless-only scope because real Ping deployments usually need more than app-side SDK calls. A headless login or registration experience still depends on correct tenant setup, OAuth client configuration, journey or flow design, policy decisions, identity store behavior, connector trust, promotion, observability, and troubleshooting. Keeping those docsets available lets an agent answer the whole implementation problem without forcing every issue through an SDK-only lens.

Use the broader scope when a question crosses layers, for example:

- A custom mobile app using the Journey SDK fails because the AIC journey script returns the wrong callback shape.
- A DaVinci-powered registration flow needs PingOne Verify, MFA enrollment, and custom OAuth scopes.
- A headless app integration is blocked by LDAP connector trust, DS certificates, RCS configuration, or OpenICF connector behavior.
- A production rollout needs Terraform, configuration promotion, environment variables, and rollback guidance.

## Example Prompts

- "Using PingAM docs, build an authentication tree that requires WebAuthn after a risk score is high."
- "From the PingOne API reference, show the request body for creating a worker application and required scopes."
- "Using the Ping orchestration SDK docs, design a custom React login that renders AIC journey callbacks without the hosted UI."
- "Create a DaVinci-backed mobile sign-in flow with OIDC token handling, MFA enrollment, and custom app claims."
- "Use PingGateway docs to design a route that protects an MCP server with OAuth2 bearer tokens."
- "In PingOne AIC, what is the ESV promotion flow between staging and production tenants?"
- "Using PingDirectory developer docs, find the SCIM 2.0 endpoint pattern for user lookup by external ID."
- "Compare PingOne Verify and PingOne Protect docs for a risk-based identity proofing flow."
- "Show the PingFederate SDK docs for a custom authentication adapter."

## Skill Inventory

**docs.pingidentity.com:** `auth-node-ref`, `autonomous-identity`, `configuration-guides`, `connectors`, `davinci`, `developer-resources`, `enterprise-connect`, `forgeops`, `glossary`, `identity-governance`, `identity-reporting`, `integrations`, `java-agents`, `licensing-guide`, `openicf`, `pgic`, `pingaccess`, `pingam`, `pingauthorize`, `pingcentral`, `pingdirectory`, `pingds`, `pingfederate`, `pinggateway`, `pingid`, `pingid-user-guide`, `pingidm`, `pingintelligence`, `pingone`, `pingone-admin-mfa-faq`, `pingone-solutions`, `pingoneadvancedservices`, `pingoneaic`, `pingoneforenterprise`, `platform`, `privilege`, `recognize`, `sdks`, `solution-guides`, `web-agents`.

**developer.pingidentity.com:** `build-with-ai`, `config-automation-management-sdks`, `config-automation-promotion`, `devops`, `helm`, `identity-for-ai`, `login-widget`, `orchsdks`, `p14e-directory-api`, `pingauthorize-dev`, `pingdirectory-dev`, `pingid-api`, `pingone-api`, `pingone-api-ea`, `pingoneaic-api`, `terraform`.

**Disabled:** `pingcli`, because the upstream `llms.txt` endpoint redirects to 404.

## Composition With `pingidentity/agent-plugins`

Install both when you want product routing plus docset depth:

```text
/plugin marketplace add pingidentity/agent-plugins
/plugin marketplace add mark-nienaber/ping-agent-skills
```

| Task type | Umbrella skill | Then depth skill |
|---|---|---|
| Product unknown | `ping-quickstart` | matched product skill |
| Authentication flow design | `ping-orchestration` | `davinci`, `pingoneaic`, `pingam`, `pingfederate` |
| Headless app integration | `ping-app-integration` | `orchsdks`, `sdks`, `pingone-api`, `pingoneaic-api`, `davinci`, `pingoneaic` |
| Hosted, widget, agent, or gateway integration | `ping-app-integration` | `login-widget`, `java-agents`, `web-agents`, `pingaccess`, `pinggateway` |
| AI-agent identity | `ping-identity-for-ai` | `identity-for-ai`, `pingam`, `pingone-api`, `pingoneaic-api` |
| Config-as-code | `ping-orchestration` | `config-automation-promotion`, `config-automation-management-sdks`, `terraform`, `devops` |

## Maintenance

Sync one docset:

```bash
scripts/sync-docset.sh pingam
```

Sync all enabled docsets:

```bash
scripts/sync-all.sh
```

Regenerate a `SKILL.md` from cached `llms.txt`:

```bash
scripts/generate-skill.sh pingam
```

## Validation And Proof

Validate structure, manifests, snapshots, and route tables:

```bash
scripts/validate.sh
scripts/validate.sh --skip-url-check
scripts/validate.sh --require-all-enabled
```

`--require-all-enabled` checks that every enabled registry entry has a generated skill. When URL checks are enabled, validation also samples live Markdown URLs and checks each live `llms.txt` endpoint.

Prove representative routing decisions:

```bash
scripts/routing-proof.sh --assert-defaults
```

The proof samples cover PingAM, DaVinci, PingFederate, PingDirectory, PingAccess, PingOne application policy configuration, PingOne Authorize OAuth/API policy configuration, PingOne AIC journey scripting, and an AIC/RCS LDAP truststore troubleshooting case that routes to OpenICF connector documentation.

Render a visual HTML proof report:

```bash
scripts/render-proof-report.sh
open reports/routing-proof.html
```

The report includes validation output, route diagrams, selected live URLs, and fallback snapshot paths.

## Layout

```text
.claude-plugin/
  plugin.json
  marketplace.json
plugins/
  ping-identity-docs/
    skills/<docset-slug>/
      SKILL.md
      references/
        llms.txt
        MANIFEST.md
        snapshots/*.md
reports/
  routing-proof.html
scripts/
  docsets.yaml
  sync-docset.sh
  sync-all.sh
  generate-skill.sh
  validate.sh
  routing-proof.sh
  render-proof-report.sh
  lib/
```

## Snapshot Policy

Snapshots are committed for offline safety. Sync tries versioned `single-page.md`, then unversioned `single-page.md`, then assembled guide pages, then the first official `.md` page in the guide. Source type is recorded in `references/MANIFEST.md`.

## Troubleshooting

- **Skill not triggering:** name the product in the prompt, such as "Using PingAM docs" or "From the PingOne API reference."
- **Live fetch returns 404:** Ping may have moved a page. Snapshot fallback should still provide local context. Run `scripts/sync-docset.sh <slug>` to refresh.
- **Snapshot missing:** check `references/MANIFEST.md` for the captured source type and run `scripts/sync-docset.sh <slug>`.
- **`pingcli` skill absent:** disabled by design because the upstream endpoint currently redirects to 404.

## Source Of Truth

- Ping docs: `https://docs.pingidentity.com/<docset>/`
- Ping developer docs: `https://developer.pingidentity.com/<docset>/`
- Ping agent guidance: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md

Every supported doc page has a Markdown alternate. The generated skills route to those live Markdown pages first.

## License

MIT. See `LICENSE`.
