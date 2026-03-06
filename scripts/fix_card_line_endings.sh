#!/bin/bash
# Fix line endings (CRLF -> LF) for all card files in 03_Mart
# Usage: ./fix_card_line_endings.sh
# Run this AFTER Antigravity generates new cards

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/log_action.sh"

MART_DIR="./03_Mart"

echo "=== Fixing line endings in 03_Mart (CRLF -> LF) ==="

file_count=$(find "$MART_DIR" -name "*.md" -type f | wc -l)
find "$MART_DIR" -name "*.md" -type f -exec sed -i 's/\r$//' {} \;

echo "=== Done! All card files now have LF line endings ==="
echo "Run Obsidian_to_Anki: Scan vault to sync"

log_action "MAINTENANCE" "-" "03_Mart/" "Success" "Fixed CRLF -> LF in ${file_count} card files"
