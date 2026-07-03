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
- Enabled docsets: 56
- Generated skills: 56
- Disabled docsets: `pingcli`
- Snapshot footprint: about 19 MB

## Deviations To Review

Most versioned guide-level `single-page.md` endpoints returned 404 during migration. The sync tool attempts the versioned `single-page.md` URL first, then the unversioned guide `single-page.md` URL. If both are unavailable, it falls back to the first official Ping `.md` page in each guide and records that source type in `MANIFEST.md`.

`pingcli` is not generated because the advertised per-docset `llms.txt` endpoint redirects to a 404. The registry keeps the docset but sets `enabled: false` until https://github.com/mark-nienaber/ping-agent-skills/issues/2 is resolved.

## Distribution

The old `claude-skills/` to `codex-skills/` generation model is dropped. Both Claude Code and Codex install from `plugins/ping-identity-docs/skills/` directly.

Use:

```bash
./setup-claude.sh [skill-slug ...]
./setup-codex.sh [skill-slug ...]
```

The scripts preserve positional slug filtering for selective installs.
