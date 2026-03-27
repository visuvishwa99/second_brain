#!/bin/bash
# post_process.sh - Unified post-publish script
# Handles: line-ending fixes, source file cleanup, and logging
# Usage: bash scripts/post_process.sh [--fix-endings] [--delete <file>...] [--log <op> <src> <dest> <status> <notes>]...
#
# Examples:
#   bash scripts/post_process.sh --fix-endings
#   bash scripts/post_process.sh --fix-endings --delete "01_Raw/journals/2026-03-06.md"
#   bash scripts/post_process.sh --fix-endings \
#       --delete "01_Raw/journals/2026-03-06.md" \
#       --delete "01_Raw/journals/2026-03-13.md" \
#       --log "CREATE" "journal1.md" "02_Brain/05_Warehousing/spark.md" "Success" "Added Spark section" \
#       --log "CREATE" "-" "03_Mart/05_Warehousing/spark_cards.md" "Success" "Appended 2 cards"

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/log_action.sh"

do_fix_endings=false
files_to_delete=()
log_entries=()

# ----------------- Argument Parsing -----------------
while [[ $# -gt 0 ]]; do
    case "$1" in
        --fix-endings)
            do_fix_endings=true
            shift
            ;;
        --delete)
            shift
            if [[ -z "$1" ]]; then
                echo "[ERROR] --delete requires a file path argument"
                exit 1
            fi
            files_to_delete+=("$1")
            shift
            ;;
        --log)
            shift
            if [[ $# -lt 5 ]]; then
                echo "[ERROR] --log requires 5 arguments: operation source destination status notes"
                exit 1
            fi
            log_entries+=("$1|$2|$3|$4|$5")
            shift 5
            ;;
        *)
            echo "[WARNING] Unknown argument: $1"
            shift
            ;;
    esac
done

# ----------------- Step 1: Fix Line Endings -----------------
if [ "$do_fix_endings" = true ]; then
    MART_DIR="./03_Mart"
    echo "=== Fixing line endings in 03_Mart (CRLF -> LF) ==="
    file_count=$(find "$MART_DIR" -name "*.md" -type f | wc -l)
    find "$MART_DIR" -name "*.md" -type f -exec sed -i 's/\r$//' {} \;
    echo "=== Done! Fixed ${file_count} card files ==="
fi

# ----------------- Step 2: Delete Source Files -----------------
if [ ${#files_to_delete[@]} -gt 0 ]; then
    echo "=== Deleting source files ==="
    for file in "${files_to_delete[@]}"; do
        if [ -f "$file" ]; then
            rm "$file"
            echo "  Deleted: $file"
        else
            echo "  [SKIP] Not found: $file"
        fi
    done
    echo "=== Deletion complete ==="
fi

# ----------------- Step 3: Log Actions -----------------
if [ ${#log_entries[@]} -gt 0 ]; then
    echo "=== Logging actions ==="
    for entry in "${log_entries[@]}"; do
        IFS='|' read -r op src dest status notes <<< "$entry"
        log_action "$op" "$src" "$dest" "$status" "$notes"
        echo "  Logged: $op -> $dest ($status)"
    done
    echo "=== Logging complete ==="
fi

echo ""
echo "[DONE] Post-processing finished successfully."
