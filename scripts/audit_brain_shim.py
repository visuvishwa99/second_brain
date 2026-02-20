import os
import glob
import re

BRAIN_DIR = "./02_Brain"
MART_DIR = "./03_Mart"
RAW_DIR = "./01_Raw/journals"
OUTPUT = "./automation/audit_raw.txt"

def run_audit():
    with open(OUTPUT, "w", encoding="utf-8") as out:
        out.write(f"=== Second Brain Audit - SHIM ===

")

        # --- 1. Stale Journals ---
        out.write("## Stale Journals (unprocessed)
")
        raw_files = glob.glob(os.path.join(RAW_DIR, "*.md"))
        for file in raw_files:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    if "processed: false" in f.read():
                        out.write(f"- {file}
")
            except Exception:
                pass
        out.write("
")

        # --- 2. Brain Notes Missing Tags ---
        out.write("## Brain Notes Missing Tags
")
        brain_files = glob.glob(os.path.join(BRAIN_DIR, "**", "*.md"), recursive=True)
        brain_files = [f for f in brain_files if "_MOC.md" not in f]
        
        for file in brain_files:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    if not re.search(r"^tags:", f.read(), re.MULTILINE):
                        out.write(f"- [NO_TAG] {file}
")
            except Exception:
                pass
        out.write("
")

        # --- 3. File Naming Violations ---
        out.write("## File Naming Violations
")
        for file in brain_files:
            filename = os.path.basename(file)
            if re.search(r"[A-Z]", filename):
                 out.write(f"- [UPPERCASE] {file} (filename should be lowercase)
")
        out.write("
")

        # --- 4. Orphan Cards (Mart without Brain) ---
        out.write("## Orphan Cards (Mart without Brain)
")
        mart_files = glob.glob(os.path.join(MART_DIR, "**", "*_cards.md"), recursive=True)
        for card_file in mart_files:
            base = os.path.basename(card_file).replace("_cards.md", "")
            # Construct expected Brain path
            # Need to handle subdirectories relative to MART_DIR and BRAIN_DIR
            rel_path = os.path.relpath(os.path.dirname(card_file), MART_DIR)
            brain_file = os.path.join(BRAIN_DIR, rel_path, f"{base}.md")
            
            if not os.path.exists(brain_file):
                 out.write(f"- [ORPHAN] {card_file} (missing: {brain_file})
")
        out.write("
")

        # --- 5. Brain Notes without Cards ---
        out.write("## Brain Notes without Cards
")
        for brain_file in brain_files:
            base = os.path.basename(brain_file).replace(".md", "")
            rel_path = os.path.relpath(os.path.dirname(brain_file), BRAIN_DIR)
            card_file = os.path.join(MART_DIR, rel_path, f"{base}_cards.md")
            
            if not os.path.exists(card_file):
                out.write(f"- [NO_CARDS] {brain_file}
")
        out.write("
")

        # --- 7. Consolidation Candidates ---
        out.write("## Consolidation Candidates
")
        for file in brain_files:
            try:
                with open(file, "r", encoding="utf-8") as f:
                    line_count = sum(1 for _ in f)
                if line_count < 15:
                    out.write(f"- [SMALL_FILE] {file} ({line_count} lines) -> Consider merging
")
                
                if re.search(r"\d{4}-\d{2}-\d{2}", os.path.basename(file)):
                     out.write(f"- [DATED_FILE] {file} -> Consider merging
")
            except Exception:
                pass
        out.write("
")

        # --- 6. Summary ---
        out.write("## Summary
")
        out.write(f"- Brain Notes: {len(brain_files)}
")
        out.write(f"- Mart Cards: {len(mart_files)}
")
        out.write(f"- Raw Journals: {len(raw_files)}
")

if __name__ == "__main__":
    run_audit()
