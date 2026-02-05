#!/usr/bin/env python3
"""
Tag Standardization Script
Ensures each file in 02_Brain has exactly ONE tag matching its folder.
"""

import os
import re

# Define the folder-to-tag mapping
FOLDER_TAG_MAP = {
    "01_Concepts": "concepts",
    "02_Compute": "compute",
    "03_Streaming": "streaming",
    "04_Cloud": "cloud",
    "05_Warehousing": "warehousing",
    "06_Ingestion": "ingestion",
    "07_Languages": "languages",
    "08_Architecture": "architecture",
    "09_AI": "ai",
    "99_Misc": None,  # No tag for Misc
    "00_Map": None,   # Index files, no domain tag
    "00_DATAENG": None,  # Index files, no domain tag
}

BRAIN_PATH = r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages"

def get_tag_for_folder(folder_name):
    """Get the tag for a folder, or None if no tag should be applied."""
    return FOLDER_TAG_MAP.get(folder_name, None)

def update_tags_in_file(filepath, new_tag):
    """Update the tags field in a markdown file's frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has frontmatter
    if not content.startswith('---'):
        print(f"  [SKIP] No frontmatter: {filepath}")
        return False
    
    # Find the frontmatter block
    fm_end = content.find('---', 3)
    if fm_end == -1:
        print(f"  [SKIP] Invalid frontmatter: {filepath}")
        return False
    
    frontmatter = content[3:fm_end]
    body = content[fm_end+3:]
    
    # Pattern to match tags line (handles various formats)
    # tags: [tag1, tag2]
    # tags:
    #   - tag1
    #   - tag2
    # tags: tag1
    
    if new_tag:
        new_tags_line = f"tags:\n  - {new_tag}"
    else:
        new_tags_line = "tags:"
    
    # Replace existing tags line(s)
    # First, try to find multi-line tags block
    multi_line_pattern = r'tags:\s*\n(\s+-\s+\S+\s*\n?)+'
    if re.search(multi_line_pattern, frontmatter):
        frontmatter = re.sub(multi_line_pattern, new_tags_line + "\n", frontmatter)
    else:
        # Try single line tags: [...]
        single_line_pattern = r'tags:\s*\[.*?\]'
        if re.search(single_line_pattern, frontmatter):
            frontmatter = re.sub(single_line_pattern, new_tags_line, frontmatter)
        else:
            # Try tags: value (no brackets)
            simple_pattern = r'tags:\s*\S*'
            if re.search(simple_pattern, frontmatter):
                frontmatter = re.sub(simple_pattern, new_tags_line, frontmatter)
            else:
                # No tags field found, add one
                frontmatter = frontmatter.rstrip() + "\n" + new_tags_line + "\n"
    
    # Reconstruct the file
    new_content = "---" + frontmatter + "---" + body
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    print("=" * 60)
    print("TAG STANDARDIZATION")
    print("=" * 60)
    
    total_updated = 0
    total_skipped = 0
    
    for folder_name in os.listdir(BRAIN_PATH):
        folder_path = os.path.join(BRAIN_PATH, folder_name)
        
        if not os.path.isdir(folder_path):
            continue
        
        new_tag = get_tag_for_folder(folder_name)
        tag_display = f"#{new_tag}" if new_tag else "(no tag)"
        print(f"\n[FOLDER] {folder_name} -> {tag_display}")
        
        for filename in os.listdir(folder_path):
            if not filename.endswith('.md'):
                continue
            
            filepath = os.path.join(folder_path, filename)
            
            if update_tags_in_file(filepath, new_tag):
                print(f"  [OK] {filename}")
                total_updated += 1
            else:
                total_skipped += 1
    
    print("\n" + "=" * 60)
    print(f"DONE. Updated: {total_updated}, Skipped: {total_skipped}")
    print("=" * 60)

if __name__ == "__main__":
    main()
