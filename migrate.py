import os
import re

def transform_logseq_to_obsidian(directory):
    print(f"Processing directory: {directory}")
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # 1. Convert Logseq properties (key:: value) to YAML (key: value)
                    # This finds properties at the top of the file.
                    # Simple heuristic: property block is at the very beginning.
                    if '::' in content:
                        lines = content.split('\n')
                        new_lines = ["---"]
                        body = []
                        in_frontmatter = True
                        has_frontmatter = False
                        
                        # Check if the first line looks like a property or empty
                        # Some logseq files have specific frontmatter already? No, typically property:: value
                        # We need to be careful not to consume normal text as frontmatter.
                        # Logseq properties are usually the first block.
                        
                        # Refined logic: traverse lines until a non-property line is found.
                        # BUT, blank lines can exist between properties.
                        # Let's stick to the user's logic but maybe wrap it to be safe.
                        
                        # Actually, looking at the user's provided script logic:
                        # It assumes that once `in_frontmatter` becomes False, it stays False.
                        # And `in_frontmatter` starts True.
                        
                        processed_lines = []
                        
                        # Optimization: Don't rewrite if no changes
                        original_content = content
                        
                        for line in lines:
                            if in_frontmatter:
                                if '::' in line:
                                    kv = line.split('::', 1) # Split only on first ::
                                    key = kv[0].strip()
                                    value = kv[1].strip()
                                    new_lines.append(f"{key}: {value}")
                                    has_frontmatter = True
                                elif line.strip() == "":
                                    # specific Logseq behavior: empty lines might separate properties? 
                                    # Usually not in the strict block, but if we encounter a blank line *before* any text, maybe ignore or keep?
                                    # User script dropped everything else into body once in_frontmatter matched else.
                                    # A blank line usually ends the property block in visual mode, but let's be strict:
                                    # properties are continuous.
                                    pass # Skip blank lines in frontmatter block? Or does that end it?
                                    # Let's assume blank line ends frontmatter for safety if we found some properties
                                    if has_frontmatter:
                                         in_frontmatter = False
                                         body.append(line)
                                    else:
                                        # If we haven't found any properties yet and it's blank, just keep executing?
                                        # Logseq files often start with properties.
                                        pass
                                else:
                                    in_frontmatter = False
                                    body.append(line)
                            else:
                                body.append(line)
                        
                        if has_frontmatter:
                            new_lines.append("---")
                            # Add a newline after yaml
                            content = "\n".join(new_lines) + "\n" + "\n".join(body)
                        
                        # only write if changed
                        if content != original_content:
                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            print(f"Transformed: {file}")

                except Exception as e:
                    print(f"Error processing {path}: {e}")

transform_logseq_to_obsidian('./pages')
transform_logseq_to_obsidian('./journals')
print("Transformation Complete!")
