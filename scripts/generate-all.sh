#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

while IFS= read -r slug; do
  python3 "${SCRIPT_DIR}/lib/generate_skill.py" \
    --repo-root "${REPO_ROOT}" \
    "${slug}"
done < <(
  PYTHONPATH="${SCRIPT_DIR}/lib" python3 -c \
    'from ping_docsets import load_docsets; print("\n".join(d.skill_slug for d in load_docsets("scripts/docsets.yaml") if d.enabled))'
)
