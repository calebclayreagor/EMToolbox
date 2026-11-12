#!/usr/bin/env bash
# deposit.sh - relink deposit/ from the live tree, then zip it.
# Run from the repo root. deposit/ is the spec of what ships.
#
# Add to the deposit with:  cp -l --parents [path/to/file] deposit/
# Every file in deposit/ must be a hardlink of a repo file at the same
# relative path; anything else is refused.
set -euo pipefail

[[ -d deposit ]] || { echo "ERROR: no deposit/ here - run from the repo root" >&2; exit 1; }
ZIP=$PWD/deposit.zip        # absolute: the zip step cds into deposit/

mapfile -t FILES < <( cd deposit && find . -type f -printf '%P\n' | sort )
[[ ${#FILES[@]} -gt 0 ]] || { echo "ERROR: deposit/ is empty" >&2; exit 1; }

# relink (--remove-destination repoints the link after a pipeline rerun)
for rel in "${FILES[@]}"; do
  [[ -f $rel ]] || { echo "ERROR: deposit/$rel has no repo counterpart at ./$rel" >&2; exit 1; }
  cp -l --remove-destination --parents "$rel" deposit/
done

# every entry must now point at the current source inode
for rel in "${FILES[@]}"; do
  [[ "$(stat -c %i "$rel")" == "$(stat -c %i "deposit/$rel")" ]] \
    || { echo "ERROR: deposit/$rel is stale" >&2; exit 1; }
done
echo "relinked ${#FILES[@]} files, all current"

# zip from inside deposit/ so members are data/... and mesencoder/...
rm -f "$ZIP"
( cd deposit && zip -r -6 -q "$ZIP" . )
echo "$ZIP  $(du -h "$ZIP" | cut -f1)"
