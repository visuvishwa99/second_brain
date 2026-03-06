import os
import re
import sys

# Add scripts directory to path for shared imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from log_action import log_action

# Configuration
VAULT_PATH = r"c:\Misc\Dataengineering\Projects\build_second_brain"
TARGET_DIRS = ['02_Brain']

DRY_RUN = '--apply' not in sys.argv  # Default to dry-run unless --apply is passed

# Strict Mapping: Folder Name -> Single Allowed Tag
FOLDER_TAG_MAP = {
    '01_Concepts': 'concepts',
    '02_Compute': 'compute',
    '03_Streaming': 'streaming',
    '04_Cloud': 'cloud',
    '05_Warehousing': 'warehousing',
    '06_Ingestion': 'ingestion',
    '07_Languages': 'languages',
    '08_Architecture': 'architecture',
    '09_AI': 'ai',
    '99_Misc': 'misc'
}

APPROVED_TAGS = set(FOLDER_TAG_MAP.values())

def get_expected_tag(filepath):
    """
    Determines the expected tag based on the file path.
    Returns the tag string, or None if no matching folder found.
    """
    # Normalize separators
    parts = filepath.replace('\\', '/').split('/')
    
    # Find the deepest matching folder in the path
    # (In case of nested mapped folders, though unlikely with this taxonomy)
    expected = None
    for part in parts:
        if part in FOLDER_TAG_MAP:
            expected = FOLDER_TAG_MAP[part]
    
    return expected

def clean_yaml_frontmatter(content, expected_tag):
    """
    Enforces that 'tags' contains ONLY the expected_tag.
    """
    if not expected_tag:
        # If the file is not in a mapped folder, we don't enforce strict single tag,
        # but we still filter for APPROVED_TAGS generally?
        # For now, let's strictly enforce ONLY if in mapped folder.
        # But per user request "Restricted tags", we should probably enforce APPROVED_TAGS everywhere?
        # Let's stick to the "One Folder = One Tag" rule for mapped folders.
        return content, False

    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return content, False

    frontmatter_raw = match.group(1)
    rest_of_file = content[match.end():]
    
    lines = frontmatter_raw.split('\n')
    new_lines = []
    
    # We will reconstruct the frontmatter, ensuring 'tags' is set correctly.
    # Strategy: Filter out existing 'tags' lines, and inject the correct one.
    
    # First, separate non-tag lines and finding insertion point
    other_lines = []
    has_tags = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if stripped.startswith('tags:'):
            has_tags = True
            # Skip this line and any subsequent list items
            i += 1
            while i < len(lines):
                next_line = lines[i]
                # If indented list item OR inside [] (handled by main line usually)
                # But YAML list items start with - or are indented.
                # Simplest heuristic: if it looks like a list item '- ' or has leading spaces
                if next_line.strip().startswith('-') or (next_line.startswith(' ') and ':' not in next_line):
                     i += 1
                else:
                    break
            continue
        
        other_lines.append(line)
        i += 1
            
    # Reconstruct
    # We want to place 'tags:' generally near the bottom or where it was?
    # Let's append it to the end of frontmatter for consistency, or keep it if we can preserve order.
    # To correspond with "Concepts" layout, usually tags are near end.
    
    # Let's add the strict tag
    # Format: 
    # tags:
    #   - expected_tag
    
    # Check if we actually changed anything
    # We need to see if the original tags were exactly [expected_tag]
    # It's hard to compare without fully parsing. 
    # So we ALWAYS assume change if we found 'tags:' or if we need to add it.
    
    # Wait, if we rewrite every file, that's noisy. 
    # Let's try to detect if it's already perfect.
    # But for now, ensuring strictness is more important.
    
    final_lines = list(other_lines)
    # Remove empty trailing lines
    while final_lines and final_lines[-1].strip() == '':
        final_lines.pop()
        
    final_lines.append("tags:")
    final_lines.append(f"  - {expected_tag}")
    
    new_frontmatter = "---\n" + "\n".join(final_lines) + "\n---\n"
    
    # Check if content changed semantically (ignoring whitespace/comments is hard)
    # Simple check: if re-generated frontmatter is identical to old (ignoring whitespace?)
    
    if new_frontmatter == match.group(0):
        return content, False
        
    return new_frontmatter + rest_of_file, True

def main():
    mode = "DRY RUN (Preview)" if DRY_RUN else "APPLYING CHANGES"
    print(f"\n{'='*60}")
    print(f"Enforcing folder-based tags in 02_Brain - {mode}")
    print(f"{'='*60}\n")
    
    count = 0
    for subdir in TARGET_DIRS:
        root_path = os.path.join(VAULT_PATH, subdir)
        for root, dirs, files in os.walk(root_path):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    
                    expected_tag = get_expected_tag(filepath)
                    if not expected_tag:
                        continue
                        
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content, changed = clean_yaml_frontmatter(content, expected_tag)
                    
                    if changed and new_content != content:
                        rel = os.path.relpath(filepath, VAULT_PATH)
                        print(f"  {'[WOULD FIX]' if DRY_RUN else '[FIXING]'} {rel} -> #{expected_tag}")
                        
                        if not DRY_RUN:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                        count += 1
    
    print(f"\n{'='*60}")
    if DRY_RUN:
        print(f"PREVIEW: Would update {count} files.")
        print("To apply changes, run: python scripts/clean_yaml_tags.py --apply")
    else:
        print(f"DONE: Updated {count} files.")
        if count > 0:
            log_action("MAINTENANCE", "-", "02_Brain/", "Success",
                       f"Enforced folder-based tags on {count} files")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
