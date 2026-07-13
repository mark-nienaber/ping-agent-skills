# Claude Guidance

This repo contains an efficient deep-documentation layer for Ping Identity Agent Skills. Treat `plugins/ping-identity-docs/runtime-skills/ping-docs/` as the default runtime skill and `plugins/ping-identity-docs/skills/` as its generated docset data plus optional product-specific skills.

## Operating Rules

- Do not hand-author Ping documentation prose. Use Ping's live `.md` pages or bundled snapshots.
- `SKILL.md` frontmatter must stay minimal and agentskills-compatible: `name` and `description` are required; `license` is allowed.
- The frontmatter `name` must match the skill directory.
- The frontmatter `description` is the activation trigger. Keep it concrete, product-specific, and under 500 characters.
- Use `search_docs.py --json --answer-context` for bounded top-k discovery. Never load an entire `llms.txt` into model context.
- Use only the returned `snapshot_excerpt` when `snapshot_page_status` is `present`; never open, grep, or read snapshot files directly. If the exact page is absent, the excerpt is null, or current information matters, fetch the exact live Markdown URL returned by the search.
- Keep retrieval proportional: one primary search, at most one narrower retry, and at most two exact live-page fetches before answering or identifying the missing evidence.
- Do not rename `scripts/docsets.yaml` slugs without updating every reference.
- `pingcli` is registered but disabled because Ping's per-docset `llms.txt` currently returns 404 after redirect. Do not create a fake `llms.txt`.

## Skill Inventory

Generated docset data and optional skills:

- `auth-node-ref` - authentication tree node reference across PingOne and AM/self-managed nodes.
- `autonomous-identity` - Ping Autonomous Identity administration and APIs.
- `build-with-ai` - Ping AI docs, MCP servers, Agent Skills, and Docs for Agents.
- `config-automation-management-sdks` - configuration management SDK automation.
- `config-automation-promotion` - configuration promotion and pipeline examples.
- `configuration-guides` - third-party application SSO and provisioning guides.
- `connectors` - Ping connectors, especially DaVinci and PingOne connectors.
- `davinci` - PingOne DaVinci flows, connectors, applications, and UI Studio.
- `developer-resources` - OAuth2, OIDC, SCIM, SAML, JWT, and developer primers.
- `devops` - Ping DevOps images, deployment, and container tooling.
- `enterprise-connect` - Ping Enterprise Connect setup and operations.
- `forgeops` - ForgeOps Kubernetes deployments and operations.
- `glossary` - Ping terminology and IAM vocabulary.
- `helm` - Ping Helm charts and Kubernetes chart configuration.
- `identity-for-ai` - identity patterns for AI agents and agentic workflows.
- `identity-governance` - Ping Identity Governance administration and APIs.
- `identity-reporting` - Ping Identity Reporting.
- `integrations` - third-party Ping integrations.
- `java-agents` - PingAM Java Agents.
- `licensing-guide` - Ping licensing guidance.
- `login-widget` - PingOne login widget.
- `openicf` - OpenICF connector framework and development.
- `orchsdks` - Ping orchestration SDKs.
- `p14e-directory-api` - PingOne for Enterprise Directory API.
- `pgic` - Ping Government Identity Cloud.
- `pingaccess` - PingAccess administration and operations.
- `pingam` - PingAM access management, journeys, OAuth2/OIDC, SAML2, sessions, Amster, and REST.
- `pingauthorize` - PingAuthorize administration and policy.
- `pingauthorize-dev` - PingAuthorize developer/API docs.
- `pingcentral` - PingCentral administration and application owner workflows.
- `pingdirectory` - PingDirectory, PingDirectoryProxy, and PingDataSync administration.
- `pingdirectory-dev` - PingDirectory developer APIs.
- `pingds` - PingDS/ForgeRock DS.
- `pingfederate` - PingFederate federation, OAuth2/OIDC, SAML, adapters, and clustering.
- `pinggateway` - PingGateway routes, filters, handlers, and Studio.
- `pingid` - PingID administration, MFA policies, integrations, and SDKs.
- `pingid-api` - PingID APIs.
- `pingid-user-guide` - PingID end-user support.
- `pingidm` - PingIDM managed objects, sync, scripting, and REST.
- `pingintelligence` - PingIntelligence for APIs.
- `pingone` - PingOne administration across apps, MFA, directory, Protect, Verify, Authorize, Credentials, and DaVinci.
- `pingone-admin-mfa-faq` - PingOne administrator MFA FAQ.
- `pingone-api` - PingOne Platform APIs.
- `pingone-api-ea` - PingOne early access APIs.
- `pingone-solutions` - PingOne solution guides.
- `pingoneadvancedservices` - PingOne Advanced Services.
- `pingoneaic` - PingOne Advanced Identity Cloud administration.
- `pingoneaic-api` - PingOne AIC APIs.
- `pingoneforenterprise` - PingOne for Enterprise.
- `platform` - Ping Platform.
- `privilege` - PingOne Privilege/PAM.
- `recognize` - PingOne Recognize.
- `sdks` - Ping SDKs.
- `solution-guides` - cross-product Ping solution patterns.
- `terraform` - Ping Terraform automation.
- `web-agents` - PingAM Web Agents.

Blocked:

- `pingcli` - registry entry exists but is disabled. `https://developer.pingidentity.com/pingcli/llms.txt` currently redirects to a 404 endpoint. Tracking: https://github.com/mark-nienaber/ping-agent-skills/issues/2.

## Composition

Use [`pingidentity/agent-plugins`](https://github.com/pingidentity/agent-plugins) for umbrella routing. Invoke the single `ping-docs` skill for exact documentation after the product is known. Install an individual generated docset skill only for deliberate compatibility or product-isolated use.

Common combinations:

- Product unknown: start with `ping-quickstart` and clarify the platform before retrieving detailed docs.
- Authentication flow design: use `ping-orchestration`, then `ping-docs` with the selected product and task.
- Application integration: use `ping-app-integration`, then `ping-docs` for exact SDK or API pages.
- AI agent identity: use `ping-identity-for-ai`, then `ping-docs` for exact implementation references.
