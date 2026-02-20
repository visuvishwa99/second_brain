# Antigravity User Guide

Antigravity is your specialized Data Engineering AI agent (powered by [Gemini CLI](https://github.com/google-gemini/gemini-cli)) designed to manage, process, and audit your Second Brain knowledge base.

## Prerequisites

To interact with Antigravity, you must have the **Gemini CLI** installed:

```bash
# Install globally via npm
npm install -g @google/gemini-cli
```

Ensure your environment variables (e.g., `GOOGLE_API_KEY`) are configured as per the [Gemini CLI documentation](https://github.com/google-gemini/gemini-cli).

## Repository Structure

```text
second_brain/
├── .agent/workflows/     # Agent instruction sets
├── automation/           # Operational logs and audit reports
│   ├── auditor.md        # Auditor persona definition
│   ├── audit_report.md   # Latest audit findings
│   ├── movement_log.md   # Knowledge lineage tracker
│   └── skills.md         # Extended agent capabilities
├── 01_Raw/               # Incoming journals and raw notes
├── 02_Brain/             # Processed, categorized knowledge
├── 03_Mart/              # Generated Anki flashcards
├── scripts/              # Maintenance and utility scripts
└── Templates/            # Standardized Obsidian templates
```

> [!TIP]
> **Permanent Guides**: This README serves as the project manual. 
> **Temporary Walkthroughs**: AI-generated reports are transient logs of specific tasks and should not be relied upon for long-term project configuration.

---

## The Core Personas

Antigravity operates through three distinct personas based on your requirements.

### 1. The Librarian (Organizer)
*   **Role**: Content categorization and filing.
*   **Goal**: Move notes from `01_Raw` to the correct domain folder in `02_Brain` without modifying the core content.
*   **Trigger**: Set `Explain: false` in the journal frontmatter.

### 2. The Mentor 
*   **Role**: Technical deep-dive and analysis.
*   **Goal**: Transform raw notes into comprehensive technical guides with production scenarios, code examples, and Mermaid diagrams.
*   **Trigger**: Set `Explain: true` in the journal frontmatter.

### 3. The Auditor (Quality Control)
*   **Role**: Consistency and compliance checker.
*   **Goal**: Scan the Brain for duplicates, missing tags, naming violations, or orphaned cards.
*   **Trigger**: Execute `bash scripts/run_audit.sh` or request an "Audit".

---

## Knowledge Workflows

### Batch Processing
Use this to organize multiple journals at once.
*   **Trigger**: "Process my notes" or "Organize my journals".
*   **Action**: Antigravity scans `01_Raw/journals` for files where `processed: false`, proposes destinations, and moves them upon your confirmation.

### Targeted Deep Dive
Use this for learning or expanding on a specific topic.
*   **Trigger**: "Deep dive this" or "Analyze my latest note".
*   **Action**: Antigravity processes the most recent journal. If `Explain: true`, it generates a full architectural analysis; otherwise, it provides a concise summary.

---

## Configuration: The Journal Template

The behavior of the agent is controlled via the YAML frontmatter in your journals.

```yaml
---
processed: false             # false = Pending agent action
Explain: true                # true = Invoke Mentor; false = Invoke Librarian
examples: 2                  # Number of code snippets to generate
Realtime: true               # Include a production-grade implementation scenario
diagram: true                # Generate a Mermaid diagram (Mentor mode only)
move_journal_to_brain: true  # Move/Append content to 02_Brain
move_brain_to_mart: true     # Generate flashcards in 03_Mart
---
```

---

## Anki Spaced Repetition (03_Mart)

Flashcards are generated in Cloze style using `{curly braces}` and are stored in the `03_Mart` directory.

### Maintenance Commands
*   **Line Endings**: Card files MUST use LF (Unix) line endings for the `Obsidian_to_Anki` plugin to function.
    *   Command: `bash scripts/fix_card_line_endings.sh`
*   **ID Cleanup**: To remove the `<!--ID: ...-->` tags injected by the plugin:
    *   Command: `bash scripts/clean_anki_ids.sh`

---

## Mobile Sync Strategy (iOS)

To sync your knowledge base between your PC and iPhone without relying on iCloud:

### Setup
1.  **Working Copy**: Install this Git client on iOS and clone your repository.
2.  **Obsidian Mobile**: Open the vault from the Working Copy local directory.
3.  **iOS Shortcut**: Create a "Sync Brain" shortcut with the following actions:
    *   **Commit Repository** (Repo: `second_brain`, Message: "Mobile sync")
    *   **Pull Repository** (Repo: `second_brain`)
    *   **Push Repository** (Repo: `second_brain`)
    *   **Open App** (App: Obsidian)

### Usage
*   **Start Session**: Run "Sync Brain" to pull latest changes.
*   **End Session**: Run "Sync Brain" to push your updates back to the remote.
