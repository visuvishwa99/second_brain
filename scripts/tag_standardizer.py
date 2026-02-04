import os
import re

ROOT_DIR = r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages"

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

def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}, content, None
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content, None
        
    fm_str = parts[1]
    body = parts[2]
    
    fm = {}
    tags = []
    
    # Regex for array style tags: [tag1, tag2]
    match_inline = re.search(r"^tags:\s*\[(.*?)\]", fm_str, re.MULTILINE)
    if match_inline:
        raw_tags = match_inline.group(1).split(",")
        tags.extend([t.strip() for t in raw_tags if t.strip()])
    
    # Regex for list style tags
    if not tags:
        in_tags = False
        for line in fm_str.split('\n'):
            line = line.strip()
            if line.startswith("tags:"):
                in_tags = True
                continue
            if in_tags:
                if line.startswith("- "):
                    tags.append(line[2:].strip())
                elif ":" in line:
                    in_tags = False
    
    fm['tags'] = tags
    return fm, body, "---"

def reconstruct_frontmatter(fm_dict, original_fm_str):
    lines = original_fm_str.split('\n')
    new_lines = []
    skip = False
    tags_written = False
    
    for line in lines:
        if line.strip().startswith("tags:"):
            skip = True
            new_lines.append("tags:")
            for t in fm_dict.get('tags', []):
                new_lines.append(f"  - {t}")
            tags_written = True
            continue
            
        if skip:
            if re.match(r"^\s*-\s", line):
                continue
            elif ":" in line and not line.strip().startswith("-"):
                 skip = False
            else:
                pass
        
        if not skip:
            new_lines.append(line)
            
    if not tags_written:
        new_lines.append("tags:")
        for t in fm_dict.get('tags', []):
            new_lines.append(f"  - {t}")
            
    return "\n".join(new_lines)

def process_file(filepath, folder_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if not content.startswith("---"):
        print(f"Skipping {os.path.basename(filepath)} (No frontmatter)")
        return
        
    parts = content.split("---", 2)
    if len(parts) < 3:
        return
        
    fm_str = parts[1]
    body = parts[2]
    
    fm, _, _ = parse_frontmatter(content)
    current_tags = fm.get('tags', [])
    
    mandatory_tag = FOLDER_TAG_MAP.get(folder_name)
    
    new_tags = set()
    if mandatory_tag:
        new_tags.add(mandatory_tag)
        
    for t in current_tags:
        clean_t = t.lower().replace(" ", "_").strip()
        if clean_t:
            new_tags.add(clean_t)
            
    final_tags = sorted(list(new_tags))
    
    fm['tags'] = final_tags
    new_fm_str = reconstruct_frontmatter(fm, fm_str)
    
    if not new_fm_str.endswith('\n'):
        new_fm_str += '\n'
        
    new_content = f"---{new_fm_str}---{body}"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {os.path.basename(filepath)}: {final_tags}")

def main():
    print("Starting Tag Standardization...")
    for item in os.listdir(ROOT_DIR):
        folder_path = os.path.join(ROOT_DIR, item)
        if os.path.isdir(folder_path):
            folder_name = item
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(".md"):
                        process_file(os.path.join(root, file), folder_name)

    print("Done.")

if __name__ == "__main__":
    main()
