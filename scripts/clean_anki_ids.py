import os
import re
import sys

def clean_ids(target_path):
    """
    Recursively removes <!--ID: ...--> tags from Markdown files in target_path.
    """
    id_pattern = re.compile(r'<!--ID: \d+-->\s*$')
    
    # Determine if it's a file or directory
    files_to_process = []
    if os.path.isfile(target_path):
        files_to_process.append(target_path)
    elif os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith('.md'):
                    files_to_process.append(os.path.join(root, file))
    
    count = 0
    for filepath in files_to_process:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = [line for line in lines if not id_pattern.search(line)]
        
        if len(lines) != len(new_lines):
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"Cleaned {len(lines) - len(new_lines)} IDs from: {filepath}")
            count += 1
            
    if count == 0:
        print("No IDs found to clean.")
    else:
        print(f"Finished cleaning {count} files.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_anki_ids.py <path_to_file_or_folder>")
    else:
        clean_ids(sys.argv[1])
