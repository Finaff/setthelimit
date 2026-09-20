#!/bin/sh
# Copies site/ into the session scratchpad so the Artifact tool can publish it
# (it only reads files under the working directory or the scratchpad).
set -e
DEST="${1:-/tmp/stl-staging/stl-site}"
rm -rf "$DEST" && mkdir -p "$DEST" && cp -R "$(dirname "$0")/../site/." "$DEST/"
echo "staged to $DEST"; ls "$DEST"
