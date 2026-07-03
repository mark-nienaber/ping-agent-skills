# Ping Agent Skills

Agent Skills for Ping Identity documentation. Each generated skill is a thin router to Ping's official Markdown docs: it reads a cached `llms.txt`, selects the right live `.md` URL, and falls back to committed snapshots when offline.

This repo complements [`pingidentity/agent-plugins`](https://github.com/pingidentity/agent-plugins). Use their six umbrella skills when you need product routing across PingOne, AIC, DaVinci, PingFederate, PingAccess, and app integration. Use this repo when you already know the docset and need deeper per-product documentation coverage.

## Status

- 57 docsets are registered in `scripts/docsets.yaml`.
- 56 skills are generated under `plugins/ping-identity-docs/skills/`.
- `pingcli` is blocked: Ping's root developer `llms.txt` links to `https://developer.pingidentity.com/pingcli/llms.txt`, but that redirects to `/pingcli/1.1/llms.txt`, which returns 404. The sync script fails loudly as required by the migration spec.
- Snapshot size is about 19 MB, below the 200 MB threshold for proposing fetch-on-demand mode.

## Install

Claude Code marketplace install, once published:

```bash
/plugin marketplace add https://github.com/mark-nienaber/ping-agent-skills
```

Local Claude Code skill install:

```bash
./setup-claude.sh
./setup-claude.sh pingam pingoneaic pingfederate
./setup-claude.sh --push /path/to/project pingam pingone
```

Local Codex skill install:

```bash
./setup-codex.sh
./setup-codex.sh pingam pingoneaic pingfederate
./setup-codex.sh --push /path/to/project pingam pingone
```

The setup scripts preserve the legacy positional slug filtering style. With no slugs, they install every generated skill. With slugs, they install only those skills.

## Repository Layout

```text
.claude-plugin/
  plugin.json
  marketplace.json
plugins/
  ping-identity-docs/
    .claude-plugin/plugin.json
    skills/<docset-slug>/
      SKILL.md
      references/
        llms.txt
        MANIFEST.md
        snapshots/*.md
scripts/
  docsets.yaml
  sync-docset.sh
  sync-all.sh
  generate-skill.sh
  validate.sh
  lib/
```

## Workflow

Sync one docset:

```bash
scripts/sync-docset.sh pingam
```

Sync all enabled docsets:

```bash
scripts/sync-all.sh
```

Generate a skill after syncing:

```bash
scripts/generate-skill.sh pingam
```

Validate generated skills:

```bash
scripts/validate.sh
scripts/validate.sh --skip-url-check
scripts/validate.sh --require-all-enabled
```

`--require-all-enabled` currently fails until Ping fixes the `pingcli` per-docset `llms.txt` endpoint or the registry explicitly disables that docset.

## Snapshot Policy

Snapshots are committed by default for offline safety and visible documentation drift. The sync script attempts each guide's `single-page.md` URL first. Current Ping docs return 404 for those guide-level `single-page.md` URLs, so the script falls back to the first official Ping `.md` page in each guide and records the source type in `references/MANIFEST.md`.

## License

MIT. See `LICENSE`.
