# Claude Guidance

This repo contains Agent Skills for Ping Identity documentation. Treat `plugins/ping-identity-docs/skills/` as the single source shared by Claude Code, Codex, and other agents.

## Operating Rules

- Do not hand-author Ping documentation prose. Use Ping's live `.md` pages or bundled snapshots.
- `SKILL.md` frontmatter must stay minimal and agentskills-compatible: `name` and `description` are required; `license` is allowed.
- The frontmatter `name` must match the skill directory.
- The frontmatter `description` is the activation trigger. Keep it concrete, product-specific, and under 500 characters.
- Prefer live fetch from the URL selected through `references/llms.txt`; use `references/snapshots/` only when offline or live fetch fails.
- Do not rename `scripts/docsets.yaml` slugs without an explicit migration note.
- `pingcli` is registered but not generated because Ping's per-docset `llms.txt` currently returns 404 after redirect. Do not create a fake `llms.txt`.

## Skill Inventory

Generated skills:

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

- `pingcli` - registry entry exists, but `https://developer.pingidentity.com/pingcli/llms.txt` currently redirects to a 404 endpoint.

## Composition

Use [`pingidentity/agent-plugins`](https://github.com/pingidentity/agent-plugins) for umbrella routing. Use this repo for per-docset depth after the product/docset is known.

Common combinations:

- Product unknown: start with `ping-quickstart`, then load the matching skill here.
- Authentication flow design: use `ping-orchestration`, then `davinci`, `pingoneaic`, `pingam`, or `pingfederate`.
- Application integration: use `ping-app-integration`, then `pingone-api`, `sdks`, `login-widget`, `java-agents`, or `web-agents`.
- AI agent identity: use `ping-identity-for-ai`, then `identity-for-ai`, `pingam`, `pingone-api`, or `pingoneaic-api`.
