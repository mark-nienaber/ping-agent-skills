# Ping Skills → Agentskills-Compliant Live-Docs Plan

**Date:** 2026-07-03
**Owner:** Mark Nienaber
**Executor:** Codex
**Reviewer:** Claude

## Goal

Replace the current 302-file, hand-curated Ping skill repo with **agentskills-spec-compliant** skills that route to Ping's official live `.md` documentation via `llms.txt`. Cover **every docset** on `docs.pingidentity.com` and `developer.pingidentity.com` — no gaps.

## Why

- Ping now publishes MD alternates for every doc page (`.html` → `.md`), plus per-product `llms.txt` indexes, plus per-guide `single-page.md` files. Official agent guidance: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
- Current static skills stale, cover ~15% of surface area, duplicate what Ping now serves canonically.
- Agentskills format (https://agentskills.io) is the open standard adopted by Claude Code, Cursor, Copilot, Gemini CLI, OpenCode. Same format `pingidentity/agent-plugins` uses.
- Combined: thin routers → live Ping MD + monthly snapshot fallback + agentskills packaging = always current, cross-agent portable, offline-safe.

## Non-goals

- Rewriting or re-authoring Ping documentation content. All prose comes from Ping's MD endpoints.
- Replacing `pingidentity/agent-plugins`. That set stays; this repo composes with it (their umbrella skills route; this repo provides deep per-docset coverage).
- Supporting doc versions older than the latest published version per product.

## Scope: all docsets

Total docsets from root `llms.txt` files:

### docs.pingidentity.com (41)
auth-node-ref, autonomous-identity, configuration_guides, connectors, davinci, developer-resources, enterprise-connect, forgeops, glossary, identity-governance, identity-reporting, integrations, java-agents, licensing-guide, openicf, pgic, pingaccess, pingam, pingauthorize, pingcentral, pingdirectory, pingds, pingfederate, pinggateway, pingid, pingid-user-guide, pingidm, pingintelligence, pingone, pingone-admin-mfa-faq, pingone-solutions, pingoneadvancedservices, pingoneaic, pingoneforenterprise, platform, privilege, recognize, sdks, solution-guides, web-agents

### developer.pingidentity.com (18)
build-with-ai, config-automation-management-sdks, config-automation-promotion, devops, helm, identity-for-ai, login-widget, orchsdks, p14e-directory-api, pingauthorize (dev), pingcli, pingdirectory (dev), pingid-api, pingone-api, pingone-api-ea, pingoneaic-api, terraform

**Total: 59 docsets → 59 skills.**

Note: overlapping product names between docs and developer sites (e.g. `pingauthorize`, `pingdirectory`) split into two skills — one for admin docs (`pingauthorize`), one for developer/API docs (`pingauthorize-dev`).

## Deliverable format: agentskills spec

Ref: https://agentskills.io/specification

**Each skill:**
```
skills/<docset-slug>/
  SKILL.md                          # required, spec frontmatter
  references/
    llms.txt                        # snapshot of product's llms.txt
    snapshots/                      # per-guide single-page.md caches
      <guide-slug>.md
      ...
    MANIFEST.md                     # sync date, version, source URLs, checksums
  scripts/
    fetch.sh                        # helper: WebFetch <url>.md wrapper
```

**SKILL.md frontmatter (required):**
```yaml
---
name: <docset-slug>
description: Use when <task list>. Routes to live Ping docs at <base-url>; falls back to bundled snapshots offline.
license: MIT
version: 1.0.0
keywords: [ping, <product>, <domain-tags>]
---
```

**SKILL.md body:**
- 1-paragraph product overview
- Live source URL (llms.txt)
- Fetch strategy (live → snapshot fallback)
- Task→URL routing table (top 10-30 task categories per product)
- Common patterns (how to combine with other Ping skills)
- Composition notes (works alongside `pingidentity/agent-plugins`)

## Repo structure after migration

```
claudeskills/
  README.md                              # rewritten
  CLAUDE.md                              # updated for new structure
  LICENSE                                # MIT
  .claude-plugin/
    plugin.json                          # marketplace manifest for Claude Code
    marketplace.json                     # if publishing
  plugins/
    ping-identity-docs/
      .claude-plugin/plugin.json
      skills/
        <59 skill directories>
  scripts/
    sync-all.sh                          # cron entry point
    sync-docset.sh                       # per-docset sync
    generate-skill.sh                    # scaffold SKILL.md from llms.txt
    validate.sh                          # URL health check, freshness gate
    lib/
      parse-llms-txt.py
      fetch-md.py
      manifest.py
  setup-claude.sh                        # rewritten for new layout
  setup-codex.sh                         # rewritten for new layout
  archive/                               # (optional) old 302 files, tagged and preserved on branch
  docs/
    superpowers/specs/                   # this doc + future specs
    migration-notes.md
```

## Component detail

### 1. sync-docset.sh

Input: docset slug (e.g. `pingam`), base URL (docs or developer).
Behavior:
1. `curl -sL <base>/<slug>/llms.txt` → `skills/<slug>/references/llms.txt`
2. Parse `.md` URLs from llms.txt; group by guide path prefix (e.g. all `/pingam/8.1/auth-nodes/*.md` → guide `auth-nodes`)
3. For each guide, attempt `curl <base>/<slug>/<version>/<guide>/single-page.md`
   - If 200: save to `skills/<slug>/references/snapshots/<guide>.md`
   - If 404: skip (some guides have no single-page.md)
4. Write `MANIFEST.md`:
   ```markdown
   # Snapshot Manifest — <slug>
   - Version: <detected from llms.txt or URL path>
   - Sync date: YYYY-MM-DD
   - Source: <llms.txt URL>
   - Guides captured: N
   - Total pages indexed: N
   - Checksums: sha256 per file
   ```

Exit code: 0 on success, non-zero if llms.txt itself fetch fails (loud fail — schema break).

### 2. generate-skill.sh

Input: docset slug.
Behavior:
1. Parse `references/llms.txt`
2. Cluster page URLs by guide/section prefix
3. Extract task keywords from page descriptions (right side of ` - ` in llms.txt entries)
4. Emit `SKILL.md` scaffold:
   - Frontmatter with generated `description` (top task categories, joined)
   - Routing table (guide slug → base URL glob)
   - Snapshot fallback pointer
5. Human review pass to tighten description (this is what triggers activation)

### 3. sync-all.sh

Reads a docset registry file (`docsets.yaml` — 59 entries with slug + base URL + preferred version). Calls `sync-docset.sh` per entry, in parallel batches of 5. Emits summary report.

Cron: monthly. Manual: on-demand for URL scheme changes.

### 4. validate.sh

Checks:
- Every SKILL.md has valid frontmatter with `name` and `description`
- Every `references/llms.txt` exists and parses
- Every URL in llms.txt returns 200 (sampled 5% per run to avoid hammering)
- Snapshot MANIFEST.md < 60 days old (warn), < 90 days (fail)
- No dead links in SKILL.md routing tables

Run in CI on PR + weekly cron.

### 5. plugin.json (Claude Code plugin manifest)

```json
{
  "name": "ping-identity-docs",
  "version": "1.0.0",
  "description": "Live-docs router skills for every Ping Identity product",
  "author": {"name": "Mark Nienaber"},
  "license": "MIT",
  "skills": "./skills",
  "keywords": ["ping-identity", "identity", "iam", "sso", "oauth"]
}
```

### 6. setup-claude.sh (rewritten)

Two modes:
- `./setup-claude.sh` — install as Claude Code plugin from local path via `/plugin` mechanism, or symlink `plugins/ping-identity-docs/skills/*` into `~/.claude/skills/`
- `./setup-claude.sh --push <dir>` — copy skills tree into `<dir>/.claude/skills/`

Old positional-product-name syntax (`./setup-claude.sh pingam pingone-aic`) preserved: takes docset slugs, only symlinks those skills.

### 7. setup-codex.sh (rewritten)

Symlink `plugins/ping-identity-docs/skills/*` into `~/.codex/skills/`. Same slug filtering as Claude.

## Content in each SKILL.md

### Frontmatter description rules

The `description` field is what the agent uses at load time to decide relevance. Rules:
- Start with "Use when..."
- List 3-8 concrete task types
- Name the product explicitly (helps triage)
- Mention key products/protocols by name (OAuth2, SAML, WebAuthn, etc.)
- Under 500 chars
- End with fetch behavior note ("Routes to live docs; snapshots fallback")

### Body template

```markdown
# <Product Name>

<1-paragraph product summary — what it is, primary use cases>

## Live source of truth
- Product docs: https://docs.pingidentity.com/<slug>/
- llms.txt index: https://docs.pingidentity.com/<slug>/llms.txt
- Snapshot version: <version>, synced <date>

## Fetch strategy
1. Read `references/llms.txt` (bundled, always available)
2. Match task keywords to page description; pick one or more .md URLs
3. `WebFetch <url>` for that page's content
4. Offline / fetch fails → read `references/snapshots/<guide>.md`

## Task routing

| Task category | Guide slug | Live URL pattern |
|---|---|---|
| <task 1> | <guide> | https://.../<version>/<guide>/... |
| ... | | |

## Composition

- Cloud task on PingOne/AIC + DaVinci → invoke alongside `pingidentity/agent-plugins` `ping-quickstart` for platform routing, then this skill for depth.
- Mixed on-prem + cloud → check `platform` skill first, then per-product.
- SDK integration → invoke `sdks` or `login-widget` with this skill for backend config.

## Snapshots

See `references/MANIFEST.md`.
```

## Migration steps (execution order)

1. **Branch prep**
   - Create branch `agentskills-migration`
   - Tag current main as `legacy-static-v1` for archival
   - Move current `claude-skills/` and `codex-skills/` to `archive/legacy-static/` (not deleted — historical reference)

2. **Registry**
   - Write `scripts/docsets.yaml` listing all 59 docsets, base URLs, preferred versions
   - Include an `enabled` flag per docset (staged rollout)

3. **Sync tooling**
   - Implement `scripts/sync-docset.sh` (parse llms.txt + fetch single-page.md per guide)
   - Implement `scripts/sync-all.sh` (parallel wrapper)
   - Implement `scripts/generate-skill.sh` (SKILL.md scaffold from llms.txt)
   - Implement `scripts/validate.sh`
   - Unit test each with pingam as fixture

4. **First 3 skills — validate pattern**
   - Generate + hand-tune SKILL.md for `pingam`, `pingone`, `pingoneaic`
   - Run `sync-docset.sh` for each
   - Confirm frontmatter passes agentskills validator (npx skills validate or equivalent)
   - Manually test in Claude Code: does description trigger correctly? Does routing table find right page? Does snapshot fallback work when offline?

5. **Bulk generation — remaining 56**
   - Run `sync-all.sh` — pulls all llms.txt + snapshots
   - Run `generate-skill.sh` per slug — produces scaffold SKILL.md files
   - Human review pass on each `description` field (this is the activation trigger; auto-generated descriptions won't be tight enough)

6. **Plugin packaging**
   - Write `.claude-plugin/plugin.json` + `plugins/ping-identity-docs/.claude-plugin/plugin.json`
   - Write marketplace manifest if publishing

7. **Setup scripts**
   - Rewrite `setup-claude.sh` and `setup-codex.sh`
   - Test both on a fresh install

8. **Docs**
   - Rewrite `README.md`: describe new structure, install methods, composition with `pingidentity/agent-plugins`
   - Rewrite `CLAUDE.md`: list all 59 skills, when to use each
   - Update `wiki-using-ping-skills.md`
   - Write `docs/migration-notes.md` explaining before/after and rationale

9. **CI**
   - GitHub Actions workflow: run `validate.sh` on every PR
   - Weekly scheduled workflow: `sync-all.sh` + commit if snapshots changed

10. **Cutover**
    - Merge `agentskills-migration` to `main`
    - Announce to users of prior version
    - Keep `legacy-static-v1` tag available

## Acceptance criteria

- [ ] All 59 docsets have a skill directory with valid SKILL.md
- [ ] Every SKILL.md passes agentskills spec validator (frontmatter fields present, description well-formed)
- [ ] Every skill has `references/llms.txt` cached
- [ ] At least one snapshot per skill (single-page.md for primary guide)
- [ ] `MANIFEST.md` present in every `references/` dir with sync date
- [ ] `validate.sh` passes with zero errors
- [ ] `setup-claude.sh` installs and skills activate correctly in Claude Code on a test task
- [ ] `setup-codex.sh` installs and skills activate correctly in Codex
- [ ] Live fetch works: agent invokes a skill, `WebFetch`es the `.md` URL from the routing table, gets content
- [ ] Snapshot fallback works: with network disabled, agent reads `snapshots/<guide>.md` and produces useful answer
- [ ] `plugin.json` marketplace-installable in Claude Code via `/plugin marketplace add`
- [ ] Composition works: invoking a task alongside `pingidentity/agent-plugins` correctly delegates depth to this repo's skills
- [ ] Old 302 static files preserved in `archive/legacy-static/` under a git tag
- [ ] README + CLAUDE.md fully rewritten
- [ ] CI: PR validation green; weekly sync cron committed

## Risks + mitigations

| Risk | Mitigation |
|---|---|
| Ping restructures URLs mid-migration | `sync-docset.sh` fails loud; validate.sh CI catches; llms.txt is contract, treat schema break as high-priority repair |
| `.md` alternates dropped for some pages | Fall back to `Accept: text/markdown` header via WebFetch, then HTML→MD conversion in helper script |
| Version drift when Ping ships PingAM 8.2, etc. | `docsets.yaml` pins preferred version; quarterly review; automated PR from sync cron flags version changes |
| Snapshots grow repo size unacceptably | Configurable: `snapshots/` gitignored by default, only fetched live; opt-in commit for offline environments |
| Rate limits on docs.pingidentity.com during sync | Sync cron monthly not per-request; polite delays between fetches in sync-docset.sh; User-Agent identifying this project |
| Agentskills spec evolves | Pin to spec version in plugin.json metadata; watch spec repo; validator run in CI catches breaking changes |
| Auto-generated descriptions too vague to trigger correctly | Human review pass on descriptions before bulk merge; test each on 3-5 real prompts |
| Overlap with `pingidentity/agent-plugins` confuses users | README explicitly documents composition; their skills route, ours depth; no duplication of umbrella coverage |

## Open questions for user

1. **Commit snapshots to repo, or fetch-on-demand only?** Recommend: commit (offline safety, versioned drift visible). Downside: ~50-200MB repo growth.
2. **Publish to Claude Code plugin marketplace and npx skills registry?** Recommend: yes, once first-pass ships. Increases reach.
3. **Deprecate current 302 files immediately or leave both formats live during transition?** Recommend: archive immediately under git tag, single active path.
4. **Version pinning strategy — always pin (`/8.1/`) or track latest (`/latest/`)?** Recommend: pin, with quarterly bump PRs. Predictable, breaks visible in git diff.
5. **Codex distribution:** current repo generates codex-skills/ from claude-skills/ source. Under agentskills spec, both platforms should read the same skills directory directly. Drop the codex-skills/ generation step and symlink instead — confirm this is fine.

## Estimated effort

- Sync tooling + validators: 1.5 days
- First 3 skills validated: 1 day
- Bulk generation + human description review pass: 2 days
- Plugin packaging + setup scripts: 0.5 day
- Docs + CI: 1 day
- Testing (live + offline + composition): 1 day
- **Total: ~7 days for a competent executor**

## Handoff to Codex

Codex should:
1. Read this spec end-to-end.
2. Implement in the migration steps order above.
3. Commit per step (branch `agentskills-migration`) with clear commit messages.
4. Open PR when acceptance criteria checked.
5. Flag questions or ambiguities in PR description rather than guessing on core design decisions.
6. Do not modify or delete legacy content before archive step.
