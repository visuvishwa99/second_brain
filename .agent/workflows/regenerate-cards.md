---
description: Nuke all Anki cards in 03_Mart and regenerate them from 02_Brain.
---

// turbo-all

## Trigger
Command: `/regenerate-cards` or `Regenerate all cards`

## Steps

1. Run the cleanup script to delete all existing card files:
   ```bash
   bash scripts/regenerate_all_cards.sh
   ```

2. Scan all markdown files in `02_Brain/` (excluding MOC files, `.gitignore`, and `assets/`).

3. For each Brain file found:
   a. Determine the matching `03_Mart` subfolder (same parent folder name).
   b. Determine the card file name: `<brain_filename>_cards.md` (e.g., `snowflake.md` -> `snowflake_cards.md`).
   c. Generate Anki Cloze cards from the Brain file content.
   d. Write the cards to `03_Mart/<folder>/<topic>_cards.md`.
   e. Use `TARGET DECK: SecondBrain::<folder_name>` as the deck header.

4. After ALL card files are generated, run the line ending fix:
   ```bash
   bash scripts/fix_card_line_endings.sh
   ```

5. Log the bulk operation to `automation/movement_log.md` with operation `BULK_GEN`.

## Rules
- This is a FULL regeneration. All previous Anki IDs will be lost. Only use this when cards are known to be corrupted or a fresh start is needed.
- Follow all card syntax rules from GEMINI.md Section 2.5 (CurlyCloze format, blank lines between cards, LF line endings).
- Do NOT generate cards from MOC files or archive files.
- Propose the plan and wait for user confirmation before generating.
