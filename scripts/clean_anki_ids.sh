#!/bin/bash
# Clean Anki IDs from all card files in 03_Mart
# Usage: ./clean_anki_ids.sh

MART_DIR="./03_Mart"

echo "=== Cleaning Anki IDs from 03_Mart ==="

# Find all .md files and remove ID comments
find "$MART_DIR" -name "*.md" -type f | while read -r file; do
    # Check if file contains IDs
    if grep -q '<!--ID: [0-9]*-->' "$file"; then
        echo "Cleaning: $file"
        # Remove ID lines and fix line endings
        sed -i 's/<!--ID: [0-9]*-->\n\?//g' "$file"
        sed -i 's/\r$//' "$file"
    fi
done

echo "=== Done! Run Obsidian_to_Anki scan to resync ==="
