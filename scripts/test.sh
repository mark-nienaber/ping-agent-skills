#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

python3 -m unittest discover -s tests -v
scripts/migrate-manifests.sh --check
scripts/validate.sh --skip-url-check --require-all-enabled
scripts/routing-proof.sh --no-report
