#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "${SCRIPT_DIR}/../plugins/ping-identity-docs/runtime-skills/ping-docs/scripts/search_docs.py" "$@"
