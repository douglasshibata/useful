#!/bin/bash
set -euo pipefail

if [ -z "${1:-}" ]; then
    echo "Uso: $0 <string>" >&2
    exit 1
fi

printf '%s' "$1" | md5sum | awk '{print $1}'
