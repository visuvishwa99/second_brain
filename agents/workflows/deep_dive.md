---
description: Analyzes the latest journal entry and creates a Principal Engineer deep dive.
---

# Deep Dive Analysis Workflow

1. **Find Latest Journal**:
    - Search for the most recently modified `.md` file in `01_Raw/journals/` (recursively).
    - Read the content of that file.

2. **Principal Engineer Analysis**:
    - Act as the **Principal Engineer** (defined in `GEMINI.md`).
    - Explain the concepts found in the journal.
    - Generate a Mermaid diagram if applicable.
    - Create a Flashcard.

3. **Output Generation**:
    - **Brain**: Determine the correct category in `02_Brain` and create a new file there with the explanation.
    - **Mart**: Append the flashcard to `03_Mart/anki_imports.md`.

4. **Confirmation**:
    - Present the plan to the user.
    - Use `write_to_file` to save the explanation (User will approve this action).
    - Use `run_command` or similar to append to the Anki file.
