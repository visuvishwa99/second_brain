#!/bin/bash
# Regenerate All Cards: Step 1 - Delete all existing card files from 03_Mart
# Usage: bash scripts/regenerate_all_cards.sh
#
# This script ONLY handles deletion. The agent (Antigravity or Gemini CLI)
# handles Step 2: scanning 02_Brain and generating fresh cards.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/log_action.sh"

MART_DIR="./03_Mart"

echo "=== Bulk Card Regeneration: Step 1 - Cleanup ==="

# Count existing card files
card_count=$(find "$MART_DIR" -name "*_cards.md" -type f | wc -l)
echo "Found ${card_count} card files in 03_Mart"

if [ "$card_count" -eq 0 ]; then
    echo "No card files found. Nothing to delete."
    exit 0
fi

# List what will be deleted
echo ""
echo "The following card files will be deleted:"
find "$MART_DIR" -name "*_cards.md" -type f | sort
echo ""

# Delete all card files (but preserve directory structure and non-card files)
find "$MART_DIR" -name "*_cards.md" -type f -delete

remaining=$(find "$MART_DIR" -name "*_cards.md" -type f | wc -l)
if [ "$remaining" -eq 0 ]; then
    echo "=== Cleanup complete: ${card_count} card files deleted ==="
    echo "=== Step 2: Agent will now scan 02_Brain and generate fresh cards ==="
    log_action "BULK_GEN" "-" "03_Mart/" "Success" "Deleted ${card_count} card files for bulk regeneration"
else
    echo "[ERROR] ${remaining} card files could not be deleted"
    log_action "BULK_GEN" "-" "03_Mart/" "Failed" "Deletion incomplete: ${remaining} files remain"
    exit 1
fi
