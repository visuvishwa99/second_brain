#!/usr/bin/env python3
"""
Remove ALL inline tags from markdown files EXCEPT the 10 approved domain tags.
Approved tags: concepts, compute, streaming, cloud, warehousing, ingestion, languages, architecture, ai, misc
"""

import os
import re

VAULT_PATH = r"c:\Misc\Dataengineering\Projects\build_second_brain"

# Only these tags are allowed (lowercase)
APPROVED_TAGS = {
    'concepts', 'compute', 'streaming', 'cloud', 'warehousing',
    'ingestion', 'languages', 'architecture', 'ai', 'misc'
}

def clean_inline_tags(content):
    """Remove all inline #tags that are NOT in the approved list."""
    
    # Pattern to match hashtags (word boundary, #, then word characters)
    # But NOT inside code blocks or URLs
    def replace_tag(match):
        full_match = match.group(0)
        tag_name = match.group(1).lower()
        
        # Keep approved tags
        if tag_name in APPROVED_TAGS:
            return full_match
        
        # Remove unapproved tags
        return ''
    
    # Match #tag patterns, but be careful with context
    # This pattern matches #word but not ##heading or inside URLs
    pattern = r'(?<![#\w])#([A-Za-z_][A-Za-z0-9_]*)(?:\s*\^[a-f0-9-]+)?'
    
    result = re.sub(pattern, replace_tag, content)
    
    # Clean up multiple spaces
    result = re.sub(r'  +', ' ', result)
    result = re.sub(r' +$', '', result, flags=re.MULTILINE)
    
    return result

def process_file(filepath):
    """Process a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    cleaned = clean_inline_tags(content)
    
    if cleaned != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        return True
    return False

def main():
    print("=" * 60)
    print("AGGRESSIVE TAG CLEANUP")
    print("Keeping only:", APPROVED_TAGS)
    print("=" * 60)
    
    total_updated = 0
    
    # Walk through specific directories
    for subdir in ['02_Brain', '03_Mart', '01_Raw']:
        target_path = os.path.join(VAULT_PATH, subdir)
        if not os.path.exists(target_path):
            continue
            
        for root, dirs, files in os.walk(target_path):
            dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian']]
            
            for filename in files:
                if not filename.endswith('.md'):
                    continue
                
                filepath = os.path.join(root, filename)
                
                if process_file(filepath):
                    rel_path = os.path.relpath(filepath, VAULT_PATH)
                    print(f"  [CLEANED] {rel_path}")
                    total_updated += 1
    
    print()
    print("=" * 60)
    print(f"DONE. Cleaned: {total_updated} files")
    print("=" * 60)

if __name__ == "__main__":
    main()
