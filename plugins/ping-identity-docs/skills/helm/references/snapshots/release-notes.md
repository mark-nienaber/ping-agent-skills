---
title: Current Release
description: Updated the default global image tag to 2605
component: helm
page_id: helm::release-notes/index
canonical_url: https://developer.pingidentity.com/helm/release-notes/index.html
page_aliases: ["release-notes:index.adoc"]
section_ids:
  release-0-12-3-june-3-2026: Release 0.12.3 (June 3, 2026)
  features: Features
---

# Current Release

## Release 0.12.3 (June 3, 2026)

### Features

* Updated the default global image tag to `2605`

* (PDI-2270) Added Secrets Store CSI Driver SecretProviderClass support. Charts can now create and mount a SecretProviderClass resource for all Ping products. Controlled via new secretProviderClass.\* values (enabled, create, name, spec). Validates CSI Driver CRDs are present before templating.
