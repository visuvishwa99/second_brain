#!/usr/bin/env python3
"""
audit_brain.py - Smart analysis for duplicate detection and report generation
Part of the Maintenance Agent (The Auditor)
Usage: python scripts/audit_brain.py
"""

import os
import re
import sys
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

# Add scripts directory to path for shared imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from log_action import log_action

BRAIN_DIR = "./02_Brain"
MART_DIR = "./03_Mart"
RAW_INPUT = "./automation/audit_raw.txt"
REPORT_OUTPUT = "./automation/audit_report.md"
SIMILARITY_THRESHOLD = 0.70  # 70%

def get_text_content(filepath):
    """Extract text content, skipping frontmatter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Remove YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]
        return content.strip()
    except Exception:
        return ""

def similarity(text1, text2):
    """Calculate similarity ratio between two texts."""
    return SequenceMatcher(None, text1, text2).ratio()

def find_duplicates():
    """Find similar notes in Brain directory."""
    duplicates = []
    files = list(Path(BRAIN_DIR).rglob("*.md"))
    files = [f for f in files if "_MOC" not in f.name]
    
    contents = {}
    for f in files:
        contents[str(f)] = get_text_content(f)
    
    checked = set()
    for path1, text1 in contents.items():
        for path2, text2 in contents.items():
            if path1 >= path2 or (path1, path2) in checked:
                continue
            checked.add((path1, path2))
            
            if len(text1) < 100 or len(text2) < 100:
                continue  # Skip very short files
            
            sim = similarity(text1, text2)
            if sim >= SIMILARITY_THRESHOLD:
                level = "[DUPLICATE]" if sim >= 0.90 else "[SIMILAR]"
                duplicates.append((level, sim, path1, path2))
    
    return sorted(duplicates, key=lambda x: -x[1])

def find_duplicate_cards():
    """Find similar cards in Mart directory."""
    duplicates = []
    files = list(Path(MART_DIR).rglob("*_cards.md"))
    
    # Extract individual cards
    cards = {}
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            # Split by START/END blocks
            blocks = re.findall(r'START\nCloze\n(.+?)\nEND', content, re.DOTALL)
            for i, block in enumerate(blocks):
                cards[f"{f}::{i}"] = block.strip()
        except Exception:
            continue
    
    checked = set()
    for id1, text1 in cards.items():
        for id2, text2 in cards.items():
            if id1 >= id2 or (id1, id2) in checked:
                continue
            checked.add((id1, id2))
            
            sim = similarity(text1, text2)
            if sim >= 0.85:  # Stricter for cards
                duplicates.append((sim, id1, id2))
    
    return sorted(duplicates, key=lambda x: -x[0])[:10]  # Top 10

def generate_report():
    """Generate the final audit report."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Read bash scan results
    raw_content = ""
    if os.path.exists(RAW_INPUT):
        with open(RAW_INPUT, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    
    # Run duplicate detection
    note_dups = find_duplicates()
    card_dups = find_duplicate_cards()
    
    # Build report
    report = f"""# Audit Report - {timestamp}

## Critical Issues

### Duplicate/Similar Notes
"""
    if note_dups:
        for level, sim, p1, p2 in note_dups[:10]:
            report += f"- {level} ({sim:.0%}): `{Path(p1).name}` ↔ `{Path(p2).name}`\n"
    else:
        report += "- None found\n"
    
    report += """
### Duplicate Cards
"""
    if card_dups:
        for sim, id1, id2 in card_dups:
            report += f"- ({sim:.0%}): `{id1.split('::')[0]}` card {id1.split('::')[1]}\n"
    else:
        report += "- None found\n"
    
    report += f"""
---

## Compliance Issues

{raw_content}

---

## Next Steps
1. Review flagged duplicates and merge if appropriate
2. Add missing tags to Brain notes
3. Generate cards for Brain notes without them
4. Process stale journals in 01_Raw

> This report is **read-only**. No files were modified.
"""
    
    with open(REPORT_OUTPUT, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"[DONE] Report generated: {REPORT_OUTPUT}")

    dup_count = len(note_dups) + len(card_dups)
    log_action("AUDIT", "-", "automation/audit_report.md", "Success",
               f"Duplicate detection completed ({dup_count} issues found)")

if __name__ == "__main__":
    generate_report()
