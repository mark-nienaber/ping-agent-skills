# Ping Agent Skills

Agent Skills for Ping Identity documentation. Each skill is a thin router to Ping's official Markdown docs: it reads a cached `llms.txt`, selects the right live `.md` URL, and falls back to committed snapshots when offline.

Complements [`pingidentity/agent-plugins`](https://github.com/pingidentity/agent-plugins). Use their umbrella skills for cross-product routing; use this repo for per-docset depth.

## Coverage

- 57 docsets registered in `scripts/docsets.yaml`; 56 enabled.
- 56 skills generated under `plugins/ping-identity-docs/skills/`.
- `pingcli` disabled: `https://developer.pingidentity.com/pingcli/llms.txt` redirects to a 404. Tracking: https://github.com/mark-nienaber/ping-agent-skills/issues/2.
- Snapshot footprint ~19 MB.
- Numeric-version docsets pinned via `preferred_version` in `scripts/docsets.yaml`.

## Install

### Claude Code (recommended)

Marketplace install:

```bash
/plugin marketplace add mark-nienaber/ping-agent-skills
/plugin install ping-identity-docs@ping-agent-skills
```

### Codex

No marketplace. Use the setup script to symlink skills into `~/.codex/skills/`:

```bash
scripts/setup-codex.sh                          # all skills
scripts/setup-codex.sh pingam pingoneaic        # selective
scripts/setup-codex.sh --push /path/to/project  # into <project>/.codex/skills/
```

### Local Claude Code (pre-marketplace or selective)

Use `setup-claude.sh` when you want to install without the marketplace, install into a specific project, or install only a subset of skills:

```bash
scripts/setup-claude.sh                          # symlink all into ~/.claude/skills/
scripts/setup-claude.sh pingam pingoneaic        # selective
scripts/setup-claude.sh --push /path/to/project  # into <project>/.claude/skills/
```

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
scripts/
  docsets.yaml
  sync-docset.sh
  sync-all.sh
  generate-skill.sh
  validate.sh
  lib/
```

## How Skills Resolve Docs

1. Agent loads `SKILL.md`.
2. `SKILL.md` routing table + bundled `references/llms.txt` pick exact live `.md` URL.
3. Agent `WebFetch`es the URL.
4. Offline or fetch fails → agent reads `references/snapshots/<guide>.md`.

## Maintenance

Sync one docset:

```bash
scripts/sync-docset.sh pingam
```

Sync all enabled:

```bash
scripts/sync-all.sh
```

Regenerate a `SKILL.md` from cached `llms.txt`:

```bash
scripts/generate-skill.sh pingam
```

Validate:

```bash
scripts/validate.sh
scripts/validate.sh --skip-url-check
scripts/validate.sh --require-all-enabled
```

`--require-all-enabled` checks that every enabled registry entry has a generated skill.

## Snapshot Policy

Snapshots committed for offline safety and visible doc drift. Sync tries versioned `single-page.md`, then unversioned `single-page.md`, then first official `.md` page in the guide. Source type recorded in `references/MANIFEST.md`.

## License

MIT. See `LICENSE`.
