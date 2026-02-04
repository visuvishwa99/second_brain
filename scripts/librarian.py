import os
import shutil
import datetime
import re

# Configuration
SOURCE_DIR = r"c:\Misc\Dataengineering\Projects\build_second_brain\01_Raw"
DEST_BASE = r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages"
LOG_FILE = r"c:\Misc\Dataengineering\Projects\build_second_brain\agents\movement_log.md"

# Classification Rules (Keyword -> Target Folder)
# Folder names must match the structure in 02_Brain/pages/
CATEGORIES = {
    "01_Concepts": ["theory", "acid", "cap theorem", "normalization", "database design", "rag", "llm", "generative ai", "langchain"],
    "02_Compute": ["spark", "databricks", "hadoop", "mapreduce", "cluster"],
    "03_Streaming": ["kafka", "flink", "streaming", "real-time", "pubsub"],
    "04_Cloud": ["aws", "azure", "gcp", "iam", "s3", "ec2", "blob storage"],
    "05_Warehousing": ["snowflake", "dbt", "sql", "warehouse", "bigquery", "redshift"],
    "06_Ingestion": ["airbyte", "fivetran", "etl", "elt", "api", "ingestion"],
    "07_Languages": ["python", "scala", "java", "syntax", "bash", "shell"],
    "08_Architecture": ["medallion", "lakehouse", "mesh", "fabric", "architecture"]
}

DEFAULT_CATEGORY = "99_Misc"


def parse_tags(content):
    """
    Extract tags from content formatted as [[tag_name]].
    Returns a list of tags.
    """
    # Regex to find [[tag]] or #tag
    # We focus on [[tag]] as per user example
    wikilink_tags = re.findall(r"\[\[(.*?)\]\]", content)
    
    # Also support hash tags #tag just in case
    hash_tags = re.findall(r"#(\w+)", content)
    
    normalization = [t.lower().replace(" ", "_") for t in wikilink_tags + hash_tags]
    return normalization

def classify_content(content):
    """
    Classify content based on Tags first, then keywords.
    Returns the target folder name.
    """
    tags = parse_tags(content)
    
    # 1. Direct Tag Mapping
    # If the user explicitly provided a tag that matches a known category key or value
    
    # Invert CATEGORIES for easy lookup: keyword -> category
    keyword_map = {}
    for cat, keywords in CATEGORIES.items():
        # Map the category folder name itself
        folder_name_clean = cat.split("_", 1)[1].lower() # 02_Compute -> compute
        keyword_map[folder_name_clean] = cat
        
        # Map specific keywords
        for kw in keywords:
            keyword_map[kw.lower()] = cat

    # Check extracted tags against map
    for tag in tags:
        if tag in keyword_map:
            return keyword_map[tag]
            
    # 2. Key Word Scoring (Fallback)
    content_lower = content.lower()
    scores = {cat: 0 for cat in CATEGORIES}
    
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in content_lower:
                scores[cat] += 1
    
    # Get category with max hits
    best_cat = max(scores, key=scores.get)
    
    if scores[best_cat] > 0:
        return best_cat
    
    return DEFAULT_CATEGORY



# Map folder names to mandatory tags (Reused from tag_standardizer logic if we want consistency)
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

def ensure_frontmatter(content, category):
    """
    Ensure the file has YAML frontmatter AND correct tags.
    """
    import yaml
    
    # helper to parse FM roughly
    def parse_fm(c):
        if not c.startswith("---"): return None, c
        parts = c.split("---", 2)
        if len(parts) < 3: return None, c
        return parts[1], parts[2]
    
    existing_fm_str, body = parse_fm(content)
    
    tags = []
    
    if existing_fm_str:
        # Simple extraction of existing tags
        # We can implement a simple parser or just rebuild it.
        # For robustness, let's just append the new tag if missing to the text if regex fails,
        # or fully rebuild if we can.
        
        # Let's verify if the category tag is present. 
        mandatory_tag = FOLDER_TAG_MAP.get(category, "misc")
        
        # Check if tag exists
        if mandatory_tag not in existing_fm_str.lower():
            # Inject it.
            # Find "tags:" line
            if "tags:" in existing_fm_str:
                 # Add to list
                 lines = existing_fm_str.split('\n')
                 new_lines = []
                 for line in lines:
                     new_lines.append(line)
                     if line.strip().startswith("tags:"):
                         new_lines.append(f"  - {mandatory_tag}")
                 existing_fm_str = "\n".join(new_lines)
            else:
                 # No tags block, add it
                 existing_fm_str += f"\ntags:\n  - {mandatory_tag}\n"
        
        return f"---{existing_fm_str}---{body}"

    else:
        # Create new
        mandatory_tag = FOLDER_TAG_MAP.get(category, "misc")
        frontmatter = f"""---
area: data_engineering
category: {category}
refined: true
created: {datetime.datetime.now().strftime('%Y-%m-%d')}
tags:
  - {mandatory_tag}
---

"""
        return frontmatter + content


def log_movement(filename, destination, status):
    """
    Log the movement to the log file.
    """
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"| {date_str} | {filename} | {destination} | {status} |\n"
    
    # Create log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("| Date | File | Destination | Status |\n")
            f.write("|---|---|---|---|\n")
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

def main():
    print(f"Scanning {SOURCE_DIR} recursively...")
    
    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory {SOURCE_DIR} does not exist.")
        return

    files_moved = 0
    
    # Use os.walk to find files recursively
    for root, dirs, files in os.walk(SOURCE_DIR):
        for filename in files:
            if not filename.endswith(".md"):
                continue
                
            src_path = os.path.join(root, filename)
            
            try:
                with open(src_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Classify
                category = classify_content(content)
                target_dir = os.path.join(DEST_BASE, category)
                
                # Ensure target directory exists
                os.makedirs(target_dir, exist_ok=True)
                
                # Refine (Add frontmatter)
                new_content = ensure_frontmatter(content, category)
                
                dest_path = os.path.join(target_dir, filename)
                
                # Check if file already exists in destination
                if os.path.exists(dest_path):
                    print(f"Skipping {filename} - already exists in {category}")
                    # Optional: Check if content is different? 
                    # For now, safe default is to skip to avoid duplicates/overwrites in a 'Copy' workflow.
                    log_movement(filename, category, "Skipped - Exists")
                    continue
                
                # Write new content to dest
                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                
                # COPY ONLY: Do not remove source
                # os.remove(src_path)
                
                # OPTIONAL: Remove empty directories after move
                # if not os.listdir(root):
                #     os.rmdir(root)
                
                log_movement(filename, category, "Success")
                print(f"Copied {filename} -> {category}")
                files_moved += 1
                
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                log_movement(filename, "Unknown", f"Error: {str(e)}")

    print(f"Processing complete. Moved {files_moved} files.")

if __name__ == "__main__":
    main()
