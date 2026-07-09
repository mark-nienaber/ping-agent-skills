---
name: pingid
description: "Use when working with PingID: release notes, pingid service management, pingid integrations, pingid sdk, pingid user life cycle management, introduction to pingid. Routes to live Ping docs; snapshots fallback."
license: MIT
---

# PingID

Overview of legacy PingID FIDO2 platform biometrics, including supported devices and high-level steps to enable passwordless or MFA authentication.

## Live source of truth

- Product docs: https://docs.pingidentity.com/pingid/
- llms.txt index: https://docs.pingidentity.com/pingid/llms.txt
- Snapshot version: current
- Snapshot manifest: references/MANIFEST.md

## Fetch strategy

1. Read references/llms.txt for page discovery.
2. Match the user task to page titles, page descriptions, and the routing table below.
3. Fetch the selected live `.md` URL from Ping documentation.
4. If live fetch is unavailable, read the closest file under references/snapshots/.

## Task routing

| Task category | Guide slug | Live URL pattern | Snapshot |
|---|---|---|---|
| Release Notes: december, app, april | release_notes | https://docs.pingidentity.com/pingid/release_notes/*.md | references/snapshots/release-notes.md |
| Pingid Service Management: authentication, pingid, legacy | pingid_service_management | https://docs.pingidentity.com/pingid/pingid_service_management/*.md | references/snapshots/pingid-service-management.md |
| Pingid Integrations: configuration, example, passwordless | pingid_integrations | https://docs.pingidentity.com/pingid/pingid_integrations/*.md | references/snapshots/pingid-integrations.md |
| Pingid Sdk: pingid, sdk, account | pingid_sdk | https://docs.pingidentity.com/pingid/pingid_sdk/*.md | references/snapshots/pingid-sdk.md |
| Pingid User Life Cycle Management: user, pingid, service | pingid_user_life_cycle_management | https://docs.pingidentity.com/pingid/pingid_user_life_cycle_management/*.md | references/snapshots/pingid-user-life-cycle-management.md |
| Introduction To Pingid: pingid, authentication, pingfederate | introduction_to_pingid | https://docs.pingidentity.com/pingid/introduction_to_pingid/*.md | references/snapshots/introduction-to-pingid.md |
| Pingid Offline Mfa: mfa, offline, pingid | pingid_offline_mfa | https://docs.pingidentity.com/pingid/pingid_offline_mfa/*.md | references/snapshots/pingid-offline-mfa.md |
| Orphan Files Old: untitled | _orphan_files_old | https://docs.pingidentity.com/pingid/_orphan_files_old/*.md | references/snapshots/orphan-files-old.md |
| Pid Landing Page.Md: pingid | pid_landing_page.md | https://docs.pingidentity.com/pingid/pid_landing_page.md | references/snapshots/pid-landing-page-md.md |
| Pid Link To End User Guide.Md: accessing, end, guide | pid_link_to_end_user_guide.md | https://docs.pingidentity.com/pingid/pid_link_to_end_user_guide.md | references/snapshots/pid-link-to-end-user-guide-md.md |

## Composition

- Use alongside pingidentity/agent-plugins umbrella skills when the task needs product routing before deep documentation lookup.
- For cloud workflows involving PingOne, PingOne AIC, or DaVinci, route at the platform level first, then use this docset skill for exact pages.
- For SDK or API implementation work, combine this skill with the relevant developer or SDK docset skill.

## Snapshots

See references/MANIFEST.md for sync date, source URLs, source type, and checksums.
