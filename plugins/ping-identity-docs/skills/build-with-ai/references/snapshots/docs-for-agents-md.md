---
title: Docs for Agents
description: How AI agents can discover, navigate, and ingest Ping Identity documentation, including AI-friendly Markdown alternates and llms.txt endpoints.
component: build-with-ai
page_id: build-with-ai::docs-for-agents
canonical_url: https://developer.pingidentity.com/build-with-ai/docs-for-agents.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
keywords: ["AI", "agents", "LLM", "markdown", "llms.txt", "documentation", "RAG", "context"]
section_ids:
  documentation-domains: Documentation domains
  markdown-alternates: Markdown alternates
  how-to-access-a-markdown-alternate: How to access a Markdown alternate
  llms-txt-endpoints: llms.txt endpoints
  site-wide-endpoints: Site-wide endpoints
  per-docset-endpoints: Per-docset endpoints
  llms-txt-format: llms.txt format
  recommended-usage-patterns: Recommended usage patterns
  loading-context-for-a-specific-product: Loading context for a specific product
  loading-selectively-from-a-docset: Loading selectively from a docset
  discovery-across-all-products: Discovery across all products
  summary: Summary
---

# Docs for Agents

Ping Identity documentation supports both human readers and AI agents. Every documentation page has a machine-readable Markdown alternate, and every domain and product docset exposes an `llms.txt` index so agents can efficiently discover and load the right content.

## Documentation domains

Ping Identity documentation is served from two domains:

| Domain                                                           | What it covers                                                                                                      |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [developer.pingidentity.com](https://developer.pingidentity.com) | Developer-focused content: Model Context Protocol (MCP) servers, agent skills, SDKs, and AI-first identity tooling. |
| [docs.pingidentity.com](https://docs.pingidentity.com)           | Product documentation for all Ping Identity products: PingAM, PingFederate, PingDirectory, and more.                |

## Markdown alternates

Every documentation page has a Markdown alternate, which is a clean, token-efficient version of the same content, stripped of HTML, navigation chrome, and other rendering artifacts. Markdown alternates reduce token usage compared to raw HTML and improve accuracy when used as agent context.

### How to access a Markdown alternate

You can retrieve the Markdown alternate for any page using one of the following methods:

| Method                         | How to use it                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL extension swap             | Replace `.html` with `.md` in any documentation page URL.Example: `https://docs.pingidentity.com/pingam/8/setup/am-admin-interface-tools.html` becomes: `https://docs.pingidentity.com/pingam/8/setup/am-admin-interface-tools.md`                                                                                                                                                                                         |
| HTML `<link>` alternate        | Every page includes a `<link rel="alternate" type="text/markdown">` element in its `<head>`, pointing to the canonical URL of the Markdown alternate. Agents and scrapers can extract this to reliably locate the markdown version without constructing the URL manually.Example:```html
<link rel="alternate" type="text/markdown" href="https://docs.pingidentity.com/pingam/8.1/setup/am-admin-interface-tools.md">
``` |
| llms.txt                       | Each product docset's `llms.txt` file lists the Markdown alternate URL for every page in that docset. Learn more in [llms.txt endpoints](#llms-txt-endpoints).                                                                                                                                                                                                                                                             |
| `Accept: text/markdown` header | Send `Accept: text/markdown` in the HTTP request for any documentation page URL to receive the Markdown alternate directly, without constructing a `.md` URL.Example:```curl
curl -H "Accept: text/markdown" https://docs.pingidentity.com/pingam/8/setup/am-admin-interface-tools.html
```This is useful when you already have a page URL and want to retrieve its Markdown content without manipulating the URL.         |
| View Markdown link             | On any documentation page, a **View Markdown** link opens the Markdown alternate directly. This is primarily for human use. The previous methods are more suitable for programmatic access.                                                                                                                                                                                                                                |

## llms.txt endpoints

Ping Identity documentation exposes `llms.txt` files following the [llms.txt standard](https://llmstxt.org). These files provide a structured index of documentation that agents and large language models (LLMs) can use to discover relevant content without crawling the full site.

### Site-wide endpoints

| URL                                                                                | What it contains                                                                                |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [developer.pingidentity.com/llms.txt](https://developer.pingidentity.com/llms.txt) | Index of all developer-facing content on developer.pingidentity.com, organized by product area. |
| [docs.pingidentity.com/llms.txt](https://docs.pingidentity.com/llms.txt)           | Index of all product documentation on docs.pingidentity.com, organized by product docset.       |

### Per-docset endpoints

Each product docset also exposes its own scoped `llms.txt`, so an agent focused on a specific product can load only what it needs.

| URL pattern                                             | Example                                                                                                        |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `https://docs.pingidentity.com/{product}/llms.txt`      | [docs.pingidentity.com/pingam/llms.txt](https://docs.pingidentity.com/pingam/llms.txt)                         |
| `https://developer.pingidentity.com/{product}/llms.txt` | [developer.pingidentity.com/build-with-ai/llms.txt](https://developer.pingidentity.com/build-with-ai/llms.txt) |

Replace `{product}` with the docset identifier for the product you are targeting. Valid product identifiers are listed in the site-wide `llms.txt` for each domain.

Each per-docset `llms.txt` covers all available versions of that product's documentation.

### llms.txt format

Each `llms.txt` file is a Markdown document structured as follows:

* A top-level heading (`#`) with the domain name.

* One or more second-level headings (`##`) grouping pages, typically by product version for per-docset files, or by product for site-wide files.

* Under each heading, a bulleted list of links in standard Markdown format: `- [Page title](https://…​page.md)`

All URLs in `llms.txt` point directly to the `.md` markdown alternate for each page, with absolute URLs.

Example entries from `docs.pingidentity.com/pingam/llms.txt`:

```none
# Documentation

## Pingam 8.1

- [/.well-known/webfinger](https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oidc-discovery-webfinger.md)
- [AI agents](https://docs.pingidentity.com/pingam/8.1/am-oauth2/ai-agents.md)
- [Account lockout](https://docs.pingidentity.com/pingam/8.1/security/account-lockout.md)
```

## Recommended usage patterns

### Loading context for a specific product

To give an agent focused context on a single product, point it at the product's `llms.txt`:

```none
https://docs.pingidentity.com/pingam/llms.txt
```

The agent can then fetch individual page Markdown alternates for the pages most relevant to the task.

### Loading selectively from a docset

Use the page titles and URLs in a product's `llms.txt` to identify which pages are relevant to the current task, then fetch only those Markdown alternates. Avoid loading every page in a large docset at once. `llms.txt` exists to make targeted retrieval possible.

### Discovery across all products

To discover which products and docsets are available, start with the site-wide `llms.txt` for the relevant domain:

```none
https://docs.pingidentity.com/llms.txt
https://developer.pingidentity.com/llms.txt
```

## Summary

| Resource                           | URL                                                                                                                                                                                                 |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Developer docs index               | [developer.pingidentity.com/llms.txt](https://developer.pingidentity.com/llms.txt)                                                                                                                  |
| Product docs index                 | [docs.pingidentity.com/llms.txt](https://docs.pingidentity.com/llms.txt)                                                                                                                            |
| Per-docset index (example: PingAM) | [docs.pingidentity.com/pingam/llms.txt](https://docs.pingidentity.com/pingam/llms.txt)                                                                                                              |
| Markdown alternate for any page    | Replace `.html` with `.md` in the page URL, send `Accept: text/markdown` with any page URL, or extract the URL from the `<link rel="alternate" type="text/markdown">` element in the page `<head>`. |
