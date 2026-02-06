---
name: Librarian
description: A skill that automates the organization of data engineering notes.
---

# Librarian Skill

The Librarian is an automated workflow that organizes notes from `01_Raw` into the `02_Brain` structure.

## Triggers
- `Process my notes`
- `Organize my journals`
- `Process <filename.md>` (for a specific file)

---

## Core Principle
**Search First, Create Later.**
Organize knowledge by topic files, not by creating scattered individual files for each question.

---

## Workflow

### 1. Scan
- Search `01_Raw/journals/` for files with `processed: false`.

### 2. Match
- For each file, check if an existing file in `02_Brain` matches the topic.
- If a match is found, prepare to **append** to that file.
- If no match, prepare to **create** a new file.

### 3. Draft (Staging)
- Generate content based on `Explain` flag:
 - `Explain: true` -> Full "Deep Dive" analysis.
 - `Explain: false` -> Concise summary/cleanup.
- Save to `01_Raw/stage/<Topic>.md`.

### 4. Review & Approve
- User reviews the staged file.
- User says "Approve" or "Move to Brain".

### 5. Publish (Checklist)
After approval:
1. [ ] Write/Append to `02_Brain/<Category>/<File>.md`
2. [ ] Delete staged file using `rm` (NOT `del`)
3. [ ] Update source journal: `processed: true`
4. [ ] Append flashcard to `03_Mart/anki_imports.md`
5. [ ] Log to `automation/movement_log.md`:
 `| YYYY-MM-DD HH:MM:SS | <SourceFile> | <DestinationFolder> | Success |`

---

## Classification Rules
See `gemini/GEMINI.md` for the authoritative folder taxonomy and tagging rules.

---

## Technical Notes

### Shell Commands
- Terminal is **Bash**. Use `rm`, NOT `del`. Use `mv`, NOT `move`.

### File Operations
- Prefer `write_to_file` over shell `mv` for moving content.

### Frontmatter
- Use lowercase booleans: `false`, `true`.
