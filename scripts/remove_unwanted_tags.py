#!/usr/bin/env python3
"""
Remove unwanted inline tags from all markdown files.
Tags to remove: #card, #Keep, #keeps, #level2, #level3, #daily, #default, #index
"""

import os
import re

VAULT_PATH = r"c:\Misc\Dataengineering\Projects\build_second_brain"

# Tags to remove (case-insensitive)
UNWANTED_TAGS = [
    r'#card',
    r'#Keep',
    r'#keeps',
    r'#level2',
    r'#level3',
    r'#daily',
    r'#default',
    r'#index',
]

def remove_tags_from_file(filepath):
    """Remove unwanted inline tags from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    for tag in UNWANTED_TAGS:
        # Match the tag with optional trailing characters (like block IDs)
        # e.g., #card ^6816857a-c58d-415a-b5c6-43bf23f58593
        pattern = re.escape(tag) + r'(\s*\^[a-f0-9-]+)?'
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)
    
    # Clean up resulting double spaces or trailing whitespace on lines
    content = re.sub(r'  +', ' ', content)
    content = re.sub(r' +$', '', content, flags=re.MULTILINE)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 60)
    print("REMOVING UNWANTED TAGS")
    print("=" * 60)
    print(f"Tags to remove: {UNWANTED_TAGS}")
    print()
    
    total_updated = 0
    
    for root, dirs, files in os.walk(VAULT_PATH):
        # Skip .git and .obsidian folders
        dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian']]
        
        for filename in files:
            if not filename.endswith('.md'):
                continue
            
            filepath = os.path.join(root, filename)
            
            if remove_tags_from_file(filepath):
                rel_path = os.path.relpath(filepath, VAULT_PATH)
                print(f"  [CLEANED] {rel_path}")
                total_updated += 1
    
    print()
    print("=" * 60)
    print(f"DONE. Cleaned: {total_updated} files")
    print("=" * 60)

if __name__ == "__main__":
    main()
