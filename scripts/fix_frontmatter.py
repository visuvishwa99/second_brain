import os

ROOT_DIR = r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages"

def fix_corrupted_frontmatter():
    count_fixed = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Pattern: match anything followed immediately by --- (no newline)
                    # We look for the FIRST non-empty part or just scan the split?
                    # The corruption is specifically at the boundary of FM and body.
                    
                    # If we split by "---" and the second part ends weirdly?
                    # Easier: Regex replace `([^\n])---` with `\1\n---`
                    # But be careful not to break valid things?
                    # The corruption created `  - tag---` or `key: value---`
                    
                    import re
                    # Look for lines ending in --- where --- is NOT the start of the line
                    # Regex: ^(.*[^\n])---$ (multiline?)
                    # or just string find.
                    
                    lines = content.split('\n')
                    new_lines = []
                    modified = False
                    
                    fm_open = False
                    
                    for i, line in enumerate(lines):
                        if i == 0 and line.strip() == "---":
                            new_lines.append(line)
                            fm_open = True
                            continue
                            
                        if fm_open:
                            # We are inside potential FM.
                            # Look for the closing delimiter corruption.
                            if line.endswith("---") and line.strip() != "---":
                                # Found corruption! e.g., "  - level2---"
                                fixed_line = line[:-3] # Remove ---
                                new_lines.append(fixed_line)
                                new_lines.append("---") # Add proper separator
                                modified = True
                                fm_open = False # Closed
                            elif line.strip() == "---":
                                fm_open = False
                                new_lines.append(line)
                            else:
                                new_lines.append(line)
                        else:
                            # Body
                            new_lines.append(line)
                    
                    if modified:
                        new_content = "\n".join(new_lines)
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Fixed corruption in: {file}")
                        count_fixed += 1
                        
                except Exception as e:
                    print(f"Error checking {file}: {e}")
                    
    print(f"Total files fixed: {count_fixed}")

if __name__ == "__main__":
    fix_corrupted_frontmatter()
