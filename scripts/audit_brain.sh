#!/bin/bash
# audit_brain.sh - Fast file discovery and basic checks
# Part of the Maintenance Agent (The Auditor)
# Usage: bash scripts/audit_brain.sh

BRAIN_DIR="./02_Brain"
MART_DIR="./03_Mart"
RAW_DIR="./01_Raw"
OUTPUT="./automation/audit_raw.txt"

echo "=== Second Brain Audit - $(date '+%Y-%m-%d %H:%M') ===" > "$OUTPUT"
echo "" >> "$OUTPUT"

# --- 1. Stale Journals in 01_Raw ---
echo "## Stale Journals (unprocessed)" >> "$OUTPUT"
find "$RAW_DIR" -name "*.md" -type f 2>/dev/null | while read -r file; do
    if grep -q "processed: false" "$file" 2>/dev/null; then
        echo "- $file" >> "$OUTPUT"
    fi
done
echo "" >> "$OUTPUT"

# --- 2. Brain Notes Missing Tags ---
echo "## Brain Notes Missing Tags" >> "$OUTPUT"
find "$BRAIN_DIR" -name "*.md" -type f ! -name "*_MOC.md" | while read -r file; do
    if ! grep -q "^tags:" "$file" 2>/dev/null; then
        echo "- [NO_TAG] $file" >> "$OUTPUT"
    fi
done
echo "" >> "$OUTPUT"

# --- 3. File Naming Violations ---
echo "## File Naming Violations" >> "$OUTPUT"
# Check for uppercase in non-MOC filenames only
find "$BRAIN_DIR" -name "*.md" -type f ! -name "*_MOC.md" | while read -r file; do
    filename=$(basename "$file")
    # Use grep to check if filename contains uppercase letters
    if echo "$filename" | grep -q '[A-Z]'; then
        echo "- [UPPERCASE] $file (filename should be lowercase)" >> "$OUTPUT"
    fi
done
echo "" >> "$OUTPUT"

# --- 4. Orphan Cards (Mart without Brain) ---
echo "## Orphan Cards (Mart without Brain)" >> "$OUTPUT"
find "$MART_DIR" -name "*_cards.md" -type f | while read -r card_file; do
    # Extract base name (remove _cards.md)
    base=$(basename "$card_file" "_cards.md")
    dir=$(dirname "$card_file" | sed "s|$MART_DIR|$BRAIN_DIR|")
    brain_file="$dir/$base.md"
    if [ ! -f "$brain_file" ]; then
        echo "- [ORPHAN] $card_file (missing: $brain_file)" >> "$OUTPUT"
    fi
done
echo "" >> "$OUTPUT"

# --- 5. Brain without Cards ---
echo "## Brain Notes without Cards" >> "$OUTPUT"
find "$BRAIN_DIR" -name "*.md" -type f ! -name "*_MOC.md" | while read -r brain_file; do
    base=$(basename "$brain_file" ".md")
    dir=$(dirname "$brain_file" | sed "s|$BRAIN_DIR|$MART_DIR|")
    card_file="$dir/${base}_cards.md"
    if [ ! -f "$card_file" ]; then
        echo "- [NO_CARDS] $brain_file" >> "$OUTPUT"
    fi
done
echo "" >> "$OUTPUT"

# --- 6. Summary Counts ---
echo "## Summary" >> "$OUTPUT"
brain_count=$(find "$BRAIN_DIR" -name "*.md" -type f ! -name "*_MOC.md" | wc -l)
mart_count=$(find "$MART_DIR" -name "*.md" -type f | wc -l)
raw_count=$(find "$RAW_DIR" -name "*.md" -type f 2>/dev/null | wc -l)
echo "- Brain Notes: $brain_count" >> "$OUTPUT"
echo "- Mart Cards: $mart_count" >> "$OUTPUT"
echo "- Raw Journals: $raw_count" >> "$OUTPUT"

echo "=== Scan complete. Output: $OUTPUT ==="
cat "$OUTPUT"
