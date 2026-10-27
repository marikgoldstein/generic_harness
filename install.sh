#!/usr/bin/env bash
# install.sh: copy the harness's core files into an existing project folder, then start Claude Code there.
# Usage: bash install.sh /path/to/your/project
# Copies CLAUDE.md, AUTONOMY.md, METHODOLOGY.md, SELF_CHECK.md, RESOURCES.md and the templates folder.
# Never overwrites: a file that already exists in the target is left alone and reported.
set -u
T=${1:?usage: bash install.sh /path/to/your/project}
H=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$T"
for f in CLAUDE.md AUTONOMY.md METHODOLOGY.md SELF_CHECK.md RESOURCES.md; do
  if [ -e "$T/$f" ]; then echo "kept existing $T/$f"; else cp "$H/$f" "$T/$f" && echo "copied $f"; fi
done
if [ -e "$T/templates" ]; then echo "kept existing $T/templates/"; else cp -r "$H/templates" "$T/templates" && echo "copied templates/"; fi
echo
echo "Now: cd \"$T\" && claude    # then type your problem, or: read problem.md"
echo "Optional: copy memory/ into your Claude Code memory dir (see memory/README.md); tools/ and optional/ only if you have the resources."
