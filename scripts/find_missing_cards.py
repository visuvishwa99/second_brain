import os
import sys

# Add scripts directory to path for shared imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from log_action import log_action

brain_dir = r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain"
mart_dir = r"c:\Misc\Dataengineering\Projects\build_second_brain\03_Mart"

skip_folders = ["99_Misc", "00_DATAENG", "assets"]
skip_suffixes = ["_MOC.md"]

missing_cards = []

for root, dirs, files in os.walk(brain_dir):
    # Filter directories
    dirs[:] = [d for d in dirs if d not in skip_folders and not d.startswith(".")]
    
    for file in files:
        if not file.endswith(".md"):
            continue
        if any(file.endswith(s) for s in skip_suffixes):
            continue
            
        # Calc relative path to mirror structure
        rel_path = os.path.relpath(root, brain_dir)
        brain_file_path = os.path.join(root, file)
        
        # Expected Mart path
        card_filename = file.replace(".md", "_cards.md")
        mart_file_path = os.path.join(mart_dir, rel_path, card_filename)
        
        if not os.path.exists(mart_file_path):
            missing_cards.append(brain_file_path)

print("Files needing cards:")
for p in missing_cards:
    print(p)

log_action("AUDIT", "-", "-", "Success",
           f"Missing cards scan: {len(missing_cards)} Brain notes without cards")
