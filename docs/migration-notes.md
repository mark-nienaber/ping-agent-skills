# Migration Notes

## Before

The legacy Ping skill set was a hand-curated static collection in `mark-nienaber_pingcorp/ping_skills`, tagged `v1.0-legacy-static`. That format duplicated Ping documentation content and required manual refresh work.

## After

This repo uses Agent Skills as the shared source for Claude Code, Codex, and other agents. Each skill is a lightweight router:

1. Read bundled `references/llms.txt`.
2. Select exact Ping `.md` pages from live documentation.
3. Fetch live content when available.
4. Fall back to committed snapshots when offline.

## Current Coverage

- Registered docsets: 57
- Generated skills: 56
- Blocked docsets: `pingcli`
- Snapshot footprint: about 19 MB

## Deviations To Review

Guide-level `single-page.md` endpoints returned 404 during migration. The sync tool still attempts `single-page.md` first, then falls back to the first official Ping `.md` page in each guide and records that source type in `MANIFEST.md`.

`pingcli` is not generated because the advertised per-docset `llms.txt` endpoint redirects to a 404. This should remain an explicit PR blocker until Ping fixes the endpoint or the registry intentionally disables the docset.

## Distribution

The old `claude-skills/` to `codex-skills/` generation model is dropped. Both Claude Code and Codex install from `plugins/ping-identity-docs/skills/` directly.

Use:

```bash
./setup-claude.sh [skill-slug ...]
./setup-codex.sh [skill-slug ...]
```

The scripts preserve positional slug filtering for selective installs.
