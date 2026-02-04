import os
import re
import yaml # PyYAML is usually not standard lib, I should use manual regex parsing to be safe and dependency-free if possible, or assume user has it. 
# Antigravity env usually has standard libs. I'll use simple parsing to avoid dependency issues.

ROOT_DIR = r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages"
MISC_DIR = "99_Misc"

# Map folder generic names to mandatory tags
FOLDER_TAG_MAP = {
    "01_Concepts": "concepts",
    "02_Compute": "compute",
    "03_Streaming": "streaming",
    "04_Cloud": "cloud",
    "05_Warehousing": "warehousing",
    "06_Ingestion": "ingestion",
    "07_Languages": "languages",
    "08_Architecture": "architecture",
    "99_Misc": "misc"
}

# High-level allowed tags (Whitelisted for specific folders or global?)
# For now, we allow any single-word tag, but we enforce the folder tag.
# And we clean up format (lowercase).

def parse_frontmatter(content):
    """
    Parses simple YAML frontmatter. 
    Returns (frontmatter_dict, content_body, separator_style)
    """
    if not content.startswith("---"):
        return {}, content, None
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content, None
        
    fm_str = parts[1]
    body = parts[2]
    
    # Simple dictionary parsing for specific keys we care about
    fm = {}
    
    # Extract tags
    # tags: [a, b] or 
    # tags:
    #   - a
    tags = []
    
    # Regex for array style tags: [tag1, tag2]
    match_inline = re.search(r"^tags:\s*\[(.*?)\]", fm_str, re.MULTILINE)
    if match_inline:
        raw_tags = match_inline.group(1).split(",")
        tags.extend([t.strip() for t in raw_tags if t.strip()])
    
    # Regex for list style tags
    # tags:
    #   - tag1
    if not tags:
        # Look for "tags:" followed by lines starting with "  - "
        in_tags = False
        for line in fm_str.split('\n'):
            line = line.strip()
            if line.startswith("tags:"):
                in_tags = True
                continue
            if in_tags:
                if line.startswith("- "):
                    tags.append(line[2:].strip())
                elif ":" in line: # New key start
                    in_tags = False
    
    fm['tags'] = tags
    return fm, body, "---"

def reconstruct_frontmatter(fm_dict, original_fm_str):
    """
    Rebuilds the YAML string.
    We'll do a simple replace of the 'tags' section or rebuild entirely if simple.
    To preserve other keys, it's safer to just replace the 'tags' block.
    """
    # This is tricky with regex. Let's just output a standard block for now 
    # but that might delete other keys (created, area, etc).
    # Better strategy: Read the full frontmatter as a block, remove old tags lines, insert new tags lines.
    
    lines = original_fm_str.split('\n')
    new_lines = []
    skip = False
    tags_written = False
    
    # Check if tags existed
    has_tags = any(line.strip().startswith("tags:") for line in lines)
    
    for line in lines:
        if line.strip().startswith("tags:"):
            skip = True
            # Write new tags here
            new_lines.append("tags:")
            for t in fm_dict.get('tags', []):
                new_lines.append(f"  - {t}")
            tags_written = True
            continue
            
        if skip:
            # We are in the old tag block. 
            # If line starts with "  - " or "- ", it's a tag.
            # If it starts with a key (word:), it's the end of tags.
            if re.match(r"^\s*-\s", line):
                continue
            elif ":" in line and not line.strip().startswith("-"):
                 skip = False
            else:
                # Ambiguous line (comment or whitespace), if we are skipping tags, skip this too if it looks like part of it
                pass
        
        if not skip:
            new_lines.append(line)
            
    if not tags_written:
        # Append to end of keys if not found
        new_lines.append("tags:")
        for t in fm_dict.get('tags', []):
            new_lines.append(f"  - {t}")
            
    return "\n".join(new_lines)


def process_file(filepath, folder_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if not content.startswith("---"):
        # No frontmatter? Add it.
        # But wait, we need to preserve content.
        print(f"Skipping {os.path.basename(filepath)} (No frontmatter)")
        return
        
    parts = content.split("---", 2)
    if len(parts) < 3:
        return
        
    fm_str = parts[1]
    body = parts[2]
    
    fm, _, _ = parse_frontmatter(content)
    current_tags = fm.get('tags', [])
    
    # LOGIC:
    # 1. Mandatory tag
    mandatory_tag = FOLDER_TAG_MAP.get(folder_name)
    
    new_tags = set()
    if mandatory_tag:
        new_tags.add(mandatory_tag)
        
    # 2. Process existing tags
    for t in current_tags:
        # Clean: lowercase, underscore
        clean_t = t.lower().replace(" ", "_").strip()
        # Remove useless tags like "journal", "daily"? Or keep them? User didn't say delete.
        # User said "Use ONLY tags that align... or broad terms"
        # Let's keep existing ones but standardized format. 
        # But filter out 'level2', 'index' if they are noisy?
        # Let's keep them for now, but ensure format is clean.
        if clean_t:
            new_tags.add(clean_t)
            
    # Convert set back to sorted list
    final_tags = sorted(list(new_tags))
    
    # 3. Reconstruct
    fm['tags'] = final_tags
    new_fm_str = reconstruct_frontmatter(fm, fm_str)
    
    new_content = f"---{new_fm_str}---{body}"
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {os.path.basename(filepath)}: {final_tags}")


def main():
    print("Starting Tag Standardization...")
    
    # Iterate over top-level category folders
    for item in os.listdir(ROOT_DIR):
        folder_path = os.path.join(ROOT_DIR, item)
        if os.path.isdir(folder_path):
            folder_name = item # e.g., "03_Streaming"
            
            # Recurse into this folder
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".md"):
                        process_file(os.path.join(root, file), folder_name)

    print("Done.")

if __name__ == "__main__":
    main()
