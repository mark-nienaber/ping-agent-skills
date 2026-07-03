#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="${SCRIPT_DIR}/plugins/ping-identity-docs/skills"

usage() {
  cat <<'USAGE'
Usage:
  ./setup-codex.sh [skill-slug ...]
  ./setup-codex.sh --push <project-dir> [skill-slug ...]
  ./setup-codex.sh --copy [skill-slug ...]

Default mode symlinks selected skills into ~/.codex/skills/.
--copy copies selected skills instead of symlinking.
--push installs selected skills into <project-dir>/.codex/skills/.
USAGE
}

copy_mode=0
target_root="${HOME}/.codex/skills"
slugs=()

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
    --push)
      if [[ $# -lt 2 ]]; then
        echo "--push requires a project directory" >&2
        exit 2
      fi
      target_root="$2/.codex/skills"
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

if [[ ${#slugs[@]} -eq 0 ]]; then
  while IFS= read -r path; do
    slugs+=("$(basename "$path")")
  done < <(find "${SKILLS_ROOT}" -mindepth 1 -maxdepth 1 -type d | sort)
fi

mkdir -p "${target_root}"

for slug in "${slugs[@]}"; do
  source_dir="${SKILLS_ROOT}/${slug}"
  target_dir="${target_root}/${slug}"
  if [[ ! -f "${source_dir}/SKILL.md" ]]; then
    echo "Unknown or unsynced skill slug: ${slug}" >&2
    exit 1
  fi
  rm -rf "${target_dir}"
  if [[ "${copy_mode}" -eq 1 ]]; then
    cp -R "${source_dir}" "${target_dir}"
    echo "Copied ${slug} -> ${target_dir}"
  else
    ln -s "${source_dir}" "${target_dir}"
    echo "Linked ${slug} -> ${target_dir}"
  fi
done
