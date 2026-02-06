---
description: Trigger the Librarian to process raw journals from 01_Raw to 02_Brain.
---

1. Scan `01_Raw/journals` for files with `processed: false`.
2. For each file, identify the correct target folder in `02_Brain` based on `tags`.
3. If `move_journal_to_brain: true`, propose the move/append.
4. If `move_brain_to_mart: true`, prepare to generate Anki cards.
5. Ask for user confirmation.
6. execution: Perform moves, generate cards, delete source, and update `movement_log.md`.
