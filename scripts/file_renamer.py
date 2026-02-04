import os

ROOT_DIR = r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages"
VAULT_ROOT = r"c:\Misc\Dataengineering\Projects\build_second_brain"

def rename_files():
    renamed_map = {} # Old Name -> New Name
    
    # 1. Rename files
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".md"):
                if " " in file:
                    old_path = os.path.join(root, file)
                    new_name = file.replace(" ", "_")
                    new_path = os.path.join(root, new_name)
                    
                    try:
                        os.rename(old_path, new_path)
                        renamed_map[file.replace(".md", "")] = new_name.replace(".md", "")
                        print(f"Renamed: {file} -> {new_name}")
                    except Exception as e:
                        print(f"Error renaming {file}: {e}")

    # 2. Update Wikilinks
    if renamed_map:
        print(f"Updating wikilinks for {len(renamed_map)} renamed files...")
        update_wikilinks(renamed_map)
    else:
        print("No files renamed.")

def update_wikilinks(rename_map):
    # Walk existing vault to find references
    # We scan 01_Raw, 02_Brain, 03_Mart to be safe.
    
    files_updated = 0
    
    for root, dirs, files in os.walk(VAULT_ROOT):
        # Skip .git, .obsidian
        if ".git" in root or ".obsidian" in root:
            continue
            
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    changes = False
                    
                    for old_name, new_name in rename_map.items():
                        # Regex or simple replace?
                        # [[Old Name]] -> [[New_Name]]
                        # [[Old Name|Alias]] -> [[New_Name|Alias]]
                        
                        # Simple replace might be risky if "Old Name" is common text, 
                        # but wikilinks are usually specific.
                        # Let's target [[...]]
                        
                        if f"[[{old_name}]]" in new_content:
                            new_content = new_content.replace(f"[[{old_name}]]", f"[[{new_name}]]")
                            changes = True
                            
                        if f"[[{old_name}|" in new_content:
                            new_content = new_content.replace(f"[[{old_name}|", f"[[{new_name}|")
                            changes = True
                    
                    if changes:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        # print(f"Updated links in {file}")
                        files_updated += 1
                        
                except Exception as e:
                    print(f"Error updating links in {file}: {e}")
                    
    print(f"Updated links in {files_updated} files.")

if __name__ == "__main__":
    rename_files()
