---
description: Trigger the Principal Engineer for a deep dive analysis of the latest journal.
---

1. **Identify Target**:
   - If user specifies a file path (e.g., `/deep-dive 02_Brain/05_Warehousing/snowflake.md`), use that file.
   - If no path specified, default to the most recent journal in `01_Raw/journals`.

2. **Determine Source Type**:
   - `01_Raw` → New journal, prepare full analysis and move to Brain.
   - `02_Brain` → Existing note, propose improvements or expansions.
   - `03_Mart` → Card file, review quality and suggest new cards.

3. **Perform Deep Dive**:
   - Detailed concept explanation.
   - Production-grade code examples (count based on `examples: X` or default 2).
   - Mermaid diagram (if relevant or `diagram: true`).

4. **Prepare Output**:
   - For `01_Raw`: Create/append to `02_Brain`, generate cards if requested.
   - For `02_Brain`: Propose inline improvements or new sections.
   - For `03_Mart`: Suggest additional cards or flag low-quality cards.

5. **Ask for user confirmation** before writing any changes.

6. **Execute**: Apply changes and update `movement_log.md` if applicable.
