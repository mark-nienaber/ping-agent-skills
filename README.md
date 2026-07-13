# Ping Agent Skills

An efficient deep-documentation layer for Ping Identity Agent Skills. The default plugin exposes one `ping-docs` skill, which searches the local documentation indexes deterministically and returns only the best matching official live Markdown pages. Dated snapshots remain available when live documentation cannot be reached.

Use [`pingidentity/agent-plugins`](https://github.com/pingidentity/agent-plugins) for intent, platform, and product routing. Use this repository after the product is known and exact API, policy, version, SDK, troubleshooting, or citation detail is required.

## Coverage

- 57 docsets registered in `scripts/docsets.yaml`; 56 enabled.
- One consolidated runtime skill under `plugins/ping-identity-docs/runtime-skills/ping-docs/`.
- 56 generated docset packages under `plugins/ping-identity-docs/skills/`, used as searchable data and optional product-specific installs.
- `pingcli` disabled: `https://developer.pingidentity.com/pingcli/llms.txt` redirects to a 404. Tracking: https://github.com/mark-nienaber/ping-agent-skills/issues/2.
- Snapshot footprint ~39 MB; indexes add ~8 MB.
- Numeric-version docsets pinned via `preferred_version` in `scripts/docsets.yaml`.

Each generated docset package contains:

- `SKILL.md`: an optional product-specific router for selective installation.
- `references/llms.txt`: cached copy of the official Ping `llms.txt` index.
- `references/snapshots/*.md`: local fallback Markdown snapshots.
- `references/MANIFEST.md`: sync date, source URLs, source type, and checksums.

## Install

### Claude Code Marketplace

```bash
/plugin marketplace add mark-nienaber/ping-agent-skills
/plugin install ping-identity-docs@ping-agent-skills
```

The marketplace plugin exposes only `ping-docs`, so installing it does not add 56 docset descriptions to every turn.

### Claude Code Local

```bash
scripts/setup-claude.sh                          # install consolidated ping-docs
scripts/setup-claude.sh pingam pingoneaic        # install selected docset skills instead
scripts/setup-claude.sh --all-docsets            # compatibility/testing only
scripts/setup-claude.sh --copy pingam            # copy instead of symlink
scripts/setup-claude.sh --push /path/to/project  # copy into <project>/.claude/skills/
```

Symlinks are the default so local syncs and regenerated skills are visible immediately. Use `--copy` or `--push` for remote machines or environments where symlinks are not suitable.

### Codex

```bash
scripts/setup-codex.sh                          # install consolidated ping-docs
scripts/setup-codex.sh pingam pingoneaic        # install selected docset skills instead
scripts/setup-codex.sh --all-docsets            # compatibility/testing only
scripts/setup-codex.sh --copy pingam            # copy instead of symlink
scripts/setup-codex.sh --push /path/to/project  # copy into <project>/.codex/skills/
```

### Other Agentskills-Compatible Tools

Point the tool at `plugins/ping-identity-docs/runtime-skills/` for the consolidated skill. Point it at a named directory under `plugins/ping-identity-docs/skills/` only when installing one product-specific docset.

## How `ping-docs` Resolves Docs

1. The official umbrella skills establish the Ping product and intent.
2. `ping-docs` runs `scripts/search_docs.py`, which scans the cached indexes in code rather than loading them into model context.
3. Answer-context mode returns at most three ranked pages, exact live Markdown URLs, exact-page snapshot status, and bounded excerpts for pages actually captured.
4. The agent uses the returned excerpt directly. It fetches a selected live page only when the exact page is absent from the snapshot or current behavior must be verified.
5. Unrelated queries and low-confidence searches abstain instead of selecting an arbitrary Ping docset.

Try the retriever directly:

```bash
scripts/search-docs.sh --answer-context --product pingam \
  "cache a risk value between scripted decision nodes"
scripts/search-docs.sh --json --answer-context "PingAuthorize policy response redaction"
```

The search command performs no network requests. Live Ping Markdown remains the source of truth; snapshots are an explicit offline fallback.

## How Activation Works

The default plugin contributes one agentskills-compliant trigger:

```yaml
---
name: ping-docs
description: Find exact, detailed, version-specific Ping Identity documentation pages and offline snapshots. Use after Ping product or intent routing when implementation, configuration, API, policy, troubleshooting, release, or citation detail is needed across Ping products; also use when live documentation access is unavailable. Do not use for unrelated requests or initial product selection.
---
```

The `description` field is the activation trigger. Product-specific prompts produce better retrieval:

- Good: "Using PingAM docs, configure OAuth2 client authentication."
- Weaker: "Set up auth."

The 56 generated docset skills remain available for deliberate selective installs, but they are no longer the default plugin surface. Their descriptions require an explicitly named product, and their bodies instruct the agent to search at most 20 index matches rather than read an entire `llms.txt`.

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

Install both when you want product routing plus exact documentation depth:

```text
/plugin marketplace add pingidentity/agent-plugins
/plugin marketplace add mark-nienaber/ping-agent-skills
```

| Task type | Umbrella skill | Deep layer |
|---|---|---|
| Product unknown | `ping-quickstart` | Clarify first; do not invoke docs blindly |
| Authentication flow design | `ping-orchestration` | `ping-docs` with the selected product |
| Headless app integration | `ping-app-integration` | `ping-docs` for exact SDK/API pages |
| Shared Ping service configuration | `ping-universal-services` | `ping-docs` for policy and API detail |
| AI-agent identity | `ping-identity-for-ai` | `ping-docs` for exact implementation references |
| Platform administration | `ping-foundation` | `ping-docs` for version-specific procedures |

## Maintenance

Sync one docset:

```bash
scripts/sync-docset.sh pingam
```

Sync all enabled docsets:

```bash
scripts/sync-all.sh
```

Every successful docset sync now regenerates its `SKILL.md`, so route metadata cannot silently drift from the refreshed index.

Regenerate a `SKILL.md` from cached `llms.txt`:

```bash
scripts/generate-skill.sh pingam
```

Regenerate every enabled docset without downloading documentation:

```bash
scripts/generate-all.sh
```

Legacy manifests can be migrated once, without changing their original sync dates or snapshot content:

```bash
scripts/migrate-manifests.sh
scripts/migrate-manifests.sh --check
```

## Validation And Proof

Validate structure, manifests, snapshots, and route tables:

```bash
scripts/validate.sh
scripts/validate.sh --skip-url-check
scripts/validate.sh --require-all-enabled
```

`--require-all-enabled` checks that every enabled registry entry has a generated skill. When URL checks are enabled, validation also samples live Markdown URLs and checks each live `llms.txt` endpoint.

Validation now recomputes manifest checksums, rejects duplicate or missing entries, checks captured-versus-indexed page counts, and reports retained snapshots with unknown current provenance as warnings. The consolidated search has focused tests for exact retrieval, version handling, standalone copies, offline fallback, and out-of-domain abstention:

```bash
scripts/test.sh
```

Prove routing for every installed docset skill plus curated complex cases:

```bash
scripts/routing-proof.sh
```

The legacy proof command generates one deterministic route sample for every optional docset skill and adds curated complex routing cases. It is a routing unit test, not evidence that an LLM answer improved.

Useful options:

```bash
scripts/routing-proof.sh --no-report
scripts/routing-proof.sh --include-live-validation
scripts/routing-proof.sh --output reports/custom-routing-proof.html
```

The report includes validation output, route diagrams, selected live URLs, and fallback snapshot paths. Live URL validation is optional so the default proof remains deterministic and works offline.

## A/B Pilot

`evals/` contains a provider-neutral pilot comparing exactly two conditions:

- A: the six official Ping umbrella Agent Skills.
- B: the same six skills plus `ping-docs`.

There is no MCP condition. The suite contains 15 natural TC prompts, randomized repetitions, isolated skill roots, exact staged-skill and filesystem-sandbox protocol checks, gold documentation URLs, deterministic citation/fact metrics, latency/tool/token/cost capture with coverage rates, provider built-in skill inventory comparison, ambiguity and out-of-domain controls, and a blinded SME rubric. A clean-room Claude Code adapter is included for reproducible runs without user skills or MCP servers. See [`evals/README.md`](evals/README.md) for staging, dry-run, execution, and scoring commands.

## Layout

```text
.claude-plugin/
  plugin.json
  marketplace.json
plugins/
  ping-identity-docs/
    runtime-skills/
      ping-docs/
        SKILL.md
        scripts/search_docs.py
    skills/<docset-slug>/
      SKILL.md
      references/
        llms.txt
        MANIFEST.md
        snapshots/*.md
reports/
  routing-proof.html
evals/
  adapters/claude_code.py
  pilot.json
  cases.json
  run.py
  score.py
  validate_sources.py
  SME_RUBRIC.md
scripts/
  docsets.yaml
  sync-docset.sh
  sync-all.sh
  generate-skill.sh
  generate-all.sh
  migrate-manifests.sh
  search-docs.sh
  validate.sh
  routing-proof.sh
  render-proof-report.sh
  lib/
```

## Snapshot Policy

Snapshots are committed for offline safety. Sync tries versioned `single-page.md`, then unversioned `single-page.md`, then assembles at most 20 guide pages, and finally tries the first official Markdown page. Manifests record pages indexed, pages actually captured, full/partial coverage, source type, sync date, and checksums. `ping-docs` exposes a snapshot only when the exact selected page is present; a partial guide is never presented as an offline copy of a page it did not capture. Retained files omitted from the current manifest are also ignored because their current age and provenance are unknown.

## Troubleshooting

- **Skill not triggering:** ask for exact product documentation or invoke `ping-docs` explicitly after naming the product.
- **No search results:** add the Ping product, version, error, endpoint, or policy term. The retriever deliberately abstains on unrelated or underspecified requests.
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
