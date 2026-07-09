#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

PYTHONDONTWRITEBYTECODE=1 python3 "${SCRIPT_DIR}/lib/render_proof_report.py" --repo-root "${REPO_ROOT}" "$@"
