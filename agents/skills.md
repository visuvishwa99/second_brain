---
name: Librarian
description: A skill that automates the organization of data engineering notes.
---

# Librarian Skill

The Librarian is an automated workflow that organizes notes from `01_Raw` into the `02_Brain` structure.

## Usage

You can trigger the librarian by running the python automation script, or by manually asking the agent to "Process my notes".

You can also use the **Deep Dive** workflow to analyze your latest journal entry: `analyze journal` or `deep dive`.


## Automation Script

The automation is handled by `scripts/librarian.py`. 
This script:
1. Scans `01_Raw` for markdown files.
2. Classifies them based on keywords mapped to `02_Brain` folders.
3. Copies them to the appropriate folder.
4. Logs the action in `agents/movement_log.md`.

## Classification Rules

See `gemini/GEMINI.md` for the authoritative classification rules.
