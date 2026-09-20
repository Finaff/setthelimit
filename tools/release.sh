#!/bin/sh
# Rebuilds generated files, validates, and stages BOTH published builds (db build and public build)
# into the session scratchpad so the Artifact tool can publish them. Run before every release.
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"
SP="${STL_SCRATCH:-/tmp/stl-staging}"
node "$HERE/tools/build-content.js"
node "$HERE/tools/check-figures.js" | tail -1
node "$HERE/tools/check-fr.js" | tail -1
for d in stl-site stl-public; do rm -rf "$SP/$d"; mkdir -p "$SP/$d"; cp -R "$HERE/site/." "$SP/$d/"; done
echo "staged: $SP/stl-site (db build → JH9TKPk8tdqZBgHbrQvk49) and $SP/stl-public (public → Ht3wU2oi9HGC2vTBCXa1oz)"
