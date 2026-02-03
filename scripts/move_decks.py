import os
import shutil

# Files identified by grep
files_to_move = [
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\08_Architecture\Table Formats.md",
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\08_Architecture\mpp.md",
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\07_Languages\SQL.md",
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\07_Languages\python.md",
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\04_Cloud\aws\Aws.md",
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\03_Streaming\kafka.md",
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\02_Compute\spark_optimization.md",
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\02_Compute\PySpark_Syntax.md",
    r"c:\Misc\Dataengineering\Projects\build_second_brain\02_Brain\pages\02_Compute\PySpark_OOPS.md"
]

DEST_DIR = r"c:\Misc\Dataengineering\Projects\build_second_brain\03_Mart"

if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

for src_path in files_to_move:
    if os.path.exists(src_path):
        filename = os.path.basename(src_path)
        dest_path = os.path.join(DEST_DIR, filename)
        
        # Handle collision logic if needed, but per request "move all... to 03_mart" implies simple move.
        # If destination exists, we will overwrite or rename? 
        # Usually checking is better. Let's rename if exists to be safe.
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            dest_path = os.path.join(DEST_DIR, f"{base}_{timestamp}{ext}")
            
        try:
            shutil.move(src_path, dest_path)
            print(f"Moved: {src_path} -> {dest_path}")
            
            # Since these are Logseq files, they might have associated assets (images).
            # The prompt didn't ask for assets, just the files with "deck::".
            
        except Exception as e:
            print(f"Error moving {src_path}: {e}")
    else:
        print(f"File not found (maybe already moved): {src_path}")
