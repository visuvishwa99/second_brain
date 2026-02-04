---
description: Analyzes the latest journal entry and creates a Principal Engineer deep dive.
---

# Deep Dive Analysis Workflow

## Trigger
- `Deep dive this`
- `Analyze my latest journal`
- `Process my notes`

---

## Workflow Steps

### 1. Find & Read Journal
- Search for the most recently modified `.md` file in `01_Raw/journals/` (recursively).
- Read the file's content and frontmatter.
- **Check**: If `processed: true`, skip this file and find the next unprocessed one.

### 2. Search Existing Brain Files
- Before creating a new file, **search `02_Brain`** for an existing file matching the topic.
- Example: If the journal is about "Snowflake Time Travel", search for `Snowflake.md`.

### 3. Determine Action
| Condition | Action |
|-----------|--------|
| `Explain: true` | Run **Principal Engineer Analysis** (Deep Dive). |
| `Explain: false` | Run **Librarian Cleanup** (Summarize & File). |

### 4. Generate Content
**If `Explain: true` (Deep Dive)**:
1.  **Concept Definition**: Explain the topic.
2.  **Realtime Example**: At least one practical Data Engineering implementation.
3.  **Syntax/Code**: Python, SQL, YAML, etc.
4.  **Mermaid Diagram**: If `diagram: true` or relevant.
5.  **Flashcard**: Q/A for Anki.

**If `Explain: false` (Librarian)**:
1.  Clean up markdown and formatting.
2.  Summarize content concisely.
3.  Do NOT add extra analysis.

### 5. Draft to Staging
- Save the generated content to `./01_Raw/stage/<TopicName>.md`.
- Present the plan to the user:
  - *"I will append to `02_Brain/pages/05_Warehousing/Snowflake.md`"*
- Wait for user confirmation ("Approve" or "OK").

### 6. Publish (Post-Approval Checklist)
After user approval, execute these steps **in order**:

1.  **Write to Brain**:
    - Use `write_to_file` with `Overwrite: true` to write/append content to the target file in `02_Brain`.
2.  **Delete Staged File**:
    - Use `rm` command (NOT `del`) to remove the file from `01_Raw/stage/`.
3.  **Update Source Journal**:
    - Use `replace_file_content` to change `processed: false` to `processed: true` in the source journal file.
4.  **Append Flashcard**:
    - Use `replace_file_content` or `write_to_file` to append the flashcard to `03_Mart/anki_imports.md`.

---

## Technical Notes (CRITICAL)

### Shell Environment
- The user's terminal is **Bash** (even on Windows).
- Use `rm` to delete files, NOT `del`.
- Use `mv` to move files, NOT `move`.

### File Operations
- Prefer `write_to_file` over shell `move` commands for reliability.
- Always verify file deletion with `list_dir` if unsure.

### Frontmatter
- Use `false`/`true` (lowercase), not `F`/`T`.
- Ensure a newline exists before the closing `---` delimiter.
