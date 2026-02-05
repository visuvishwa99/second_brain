
import os
import re

SOURCE_FILE = r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\01_Concepts\data_merging_strategies.md"
OUTPUT_DIR = r"c:\Misc\Dataengineering\Projects\build_second_brain\03_Mart"

def parse_and_generate():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    # Extract Tags
    tags = []
    in_frontmatter = False
    for line in lines:
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
            else:
                break
        if in_frontmatter and line.strip().startswith("- "):
            tags.append(line.strip().replace("- ", "").strip())
            
    # Default to 'misc' if no tags, otherwise take the first one
    main_tag = tags[0] if tags else "misc"
    output_file = os.path.join(OUTPUT_DIR, f"{main_tag}.md")
    
    deck_name = main_tag.capitalize()
    
    output_content = []
    output_content.append(f"# {deck_name} Deck\n\n")
    
    # Simple Heuristic for this test:
    # 1. H2 (##) and H3 (###) are cards. 
    # 2. Add #card tag to them.
    
    current_card = []
    
    for line in lines:
        if line.strip().startswith("---") or line.strip() == "tags:" or line.strip().startswith("  -"):
            continue
            
        # If Header
        if line.startswith("##"):
            # It's a header. Add #card
            # Strip existing #card if present to avoid dupes
            clean_line = line.strip().replace("#card", "")
            output_content.append(f"\n{clean_line} #card\n")
        else:
            output_content.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_content)
        
    print(f"Generated {output_file} from {SOURCE_FILE}")

if __name__ == "__main__":
    parse_and_generate()
