#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
DOCSET_SKILLS_ROOT="${REPO_ROOT}/plugins/ping-identity-docs/skills"
RUNTIME_SKILLS_ROOT="${REPO_ROOT}/plugins/ping-identity-docs/runtime-skills"

usage() {
  cat <<'USAGE'
Usage:
  scripts/setup-claude.sh [skill-slug ...]
  scripts/setup-claude.sh --all-docsets
  scripts/setup-claude.sh --push <project-dir> [skill-slug ...]
  scripts/setup-claude.sh --copy [skill-slug ...]

With no skill slugs, installs the single consolidated ping-docs skill.
Named slugs install only those legacy per-docset skills.
--all-docsets installs every per-docset skill for compatibility testing.
--copy copies selected skills instead of symlinking.
--push installs selected skills into <project-dir>/.claude/skills/.
USAGE
}

copy_mode=0
target_root="${HOME}/.claude/skills"
slugs=()
all_docsets=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --copy)
      copy_mode=1
      shift
      ;;
    --all-docsets)
      all_docsets=1
      shift
      ;;
    --push)
      if [[ $# -lt 2 ]]; then
        echo "--push requires a project directory" >&2
        exit 2
      fi
      target_root="$2/.claude/skills"
      copy_mode=1
      shift 2
      ;;
    --)
      shift
      while [[ $# -gt 0 ]]; do
        slugs+=("$1")
        shift
      done
      ;;
    -*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      slugs+=("$1")
      shift
      ;;
  esac
done

if [[ "${all_docsets}" -eq 1 ]]; then
  while IFS= read -r path; do
    slugs+=("$(basename "$path")")
  done < <(find "${DOCSET_SKILLS_ROOT}" -mindepth 1 -maxdepth 1 -type d | sort)
elif [[ ${#slugs[@]} -eq 0 ]]; then
  slugs=("ping-docs")
fi

mkdir -p "${target_root}"

for slug in "${slugs[@]}"; do
  if [[ "${slug}" == "ping-docs" ]]; then
    source_dir="${RUNTIME_SKILLS_ROOT}/${slug}"
  else
    source_dir="${DOCSET_SKILLS_ROOT}/${slug}"
  fi
  target_dir="${target_root}/${slug}"
  if [[ ! -f "${source_dir}/SKILL.md" ]]; then
    echo "Unknown or unsynced skill slug: ${slug}" >&2
    exit 1
  fi
  rm -rf "${target_dir}"
  if [[ "${copy_mode}" -eq 1 ]]; then
    cp -R "${source_dir}" "${target_dir}"
    if [[ "${slug}" == "ping-docs" ]]; then
      mkdir -p "${target_dir}/references"
      cp -R "${DOCSET_SKILLS_ROOT}" "${target_dir}/references/docsets"
    fi
    echo "Copied ${slug} -> ${target_dir}"
  else
    ln -s "${source_dir}" "${target_dir}"
    echo "Linked ${slug} -> ${target_dir}"
  fi
done
