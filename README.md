# Ping Agent Skills

Agentskills-compliant skill bundles that route AI coding agents to Ping Identity's official live Markdown documentation.

**Status:** Under construction. See `docs/specs/2026-07-03-agentskills-migration-design.md` for the full plan.

## What this is

- One [Agent Skill](https://agentskills.io) per Ping Identity docset (59 total across `docs.pingidentity.com` and `developer.pingidentity.com`).
- Each skill is a thin router: a `SKILL.md` with an agentskills-spec frontmatter, a task-to-URL routing table, and a bundled `llms.txt` snapshot for offline discovery.
- All actual documentation content is fetched live from Ping's official `.md` endpoints. No hand-authored copies. Never stales.
- Monthly automated sync captures `single-page.md` snapshots per guide as offline fallback.

## What it is not

- Not a replacement for [`pingidentity/agent-plugins`](https://github.com/pingidentity/agent-plugins). That plugin ships umbrella skills that route across products; this repo provides deep per-docset coverage. The two compose.
- Not a rewrite of Ping's docs. Content comes from Ping's canonical `.md` endpoints via their [Docs for Agents](https://developer.pingidentity.com/build-with-ai/docs-for-agents.md) guidance.

## Predecessor

This repo supersedes the hand-curated static skill set at [`mark-nienaber_pingcorp/ping_skills`](https://github.com/mark-nienaber_pingcorp/ping_skills), preserved under the `v1.0-legacy-static` tag.

## Install

Not yet published. Once the first-pass ships:

```
# Claude Code
/plugin marketplace add https://github.com/mark-nienaber/ping-agent-skills

# Cursor / Copilot / Gemini / OpenCode
npx skills add mark-nienaber/ping-agent-skills
```

## License

MIT. See `LICENSE`.
