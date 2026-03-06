# Antigravity User Guide

This guide explains how to interact with your AI agent (Antigravity) to manage your Second Brain.

```bash
second_brain/
├── .agent/workflows/     # Antigravity system (slash commands)
├── automation/           # Your automation docs & logs
│   ├── auditor.md
│   ├── audit_report.md
│   ├── movement_log.md
│   └── skills.md
├── 01_Raw/
├── 02_Brain/
├── 03_Mart/
└── scripts/
```

> [!TIP]
> **Guide vs. Walkthrough**: 
> - **Guides** (like this one) are **permanent** project manuals meant for long-term reference. 
> - **Walkthroughs** (AI artifacts) are **temporary** "change logs" or summary reports generated for a specific task. Once you've reviewed a walkthrough, you can rely on the permanent Guides.

## The Personas

### 1. The Librarian (Agent)
* **Role**: Organizer, categorizer, cleaner.
* **Goal**: Move notes from `01_Raw` to `02_Brain` without adding heavy content.
* **Trigger Condition**: `Explain: false` in your note.

### 2. The Principal Engineer (Agent)
* **Role**: Senior Architect, Mentor.
* **Goal**: Deeply analyze a concept, provide real-world Data Engineering examples, write code, and draw diagrams.
* **Trigger Condition**: `Explain: true` in your note.

### 3. The Auditor (Maintenance Agent)
* **Role**: Quality Control, consistency checker.
* **Goal**: Scan for duplicates, missing tags, and rule violations.
* **Trigger Condition**: Manual run using `bash scripts/run_audit.sh`.

---

## Command Triggers

Since Antigravity is a natural language agent, you can talk to it normally. Use these phrases to trigger specific workflows:

### Option 1: The "Librarian" Trigger (Batch Processing)
Use this when you have written notes and just want them filed away.
* **Say**: *"Process my notes"* or *"Organize my journals"*
* **Action**:
 * Scans `01_Raw` for files with `processed: false`.
 * Proposes a folder in `02_Brain` (e.g., `01_Concepts`, `04_Cloud`).
 * Moves them upon approval.

### Option 2: The "Principal Engineer" Trigger (Deep Dive)
Use this when you want to learn.
* **Say**: *"Deep dive this"* or *"Analyze my latest note"*
* **Action**:
 * Finds the latest journal entry.
 * **If `Explain: true`**: Generates a full technical analysis (Concepts + Realtime Examples + Code + Diagrams).
 * **If `Explain: false`**: Summarizes it concisely.

### Option 3: Specific Pointer
Use this to target a specific file.
* **Say**: *"Process 2026-02-04.md"*
* **Action**: Runs the workflow on that specific file only.

### Option 4: Maintenance Audit
Use this to check the health of your Second Brain.
* **Command**: `bash scripts/run_audit.sh`
* **Action**:
 * Scans for duplicates and rule violations.
 * Generates a report in `automation/audit_report.md`.

---

## The Journal Template Rules

Your journal template controls the AI's behavior.

```yaml
---
processed: false # false = Agent will look at it. true = Agent ignores it.
Explain: false # false = Just file it. true = DEEP DIVE it.
examples: 2 # Number of code/syntax examples to include.
Realtime: true # Add a production-grade scenario.
diagram: true # Generate a Mermaid diagram.
extract_info: true # Extract info from attachments. true = discard originals. false = keep them.
move_journal_to_brain: true # Append/Create in 02_Brain.
move_brain_to_mart: true # Generate Anki cards in 03_Mart.
---
```

### The `extract_info` Rule
Controls how the agent handles attachments (PDFs, images, links) in your journal entries.

| Value | Behavior |
|-------|----------|
| `true` | Extract the relevant information from attachments, then **discard** the original files/links from the final Brain note. |
| `false` | Extract the relevant information **and** append the original documents, images, or links at the end of the Brain note. |

---

## Logging & Knowledge Lineage

Every movement from `01_Raw` to `02_Brain`, as well as manual script tools (Maintenance and Audits), is logged in [movement_log.md](file:///c:/Misc/Dataengineering/Projects/second_brain/automation/movement_log.md) for auditability.

> [!IMPORTANT]
> **How to Log (NEVER VIOLATE)**:
> NEVER edit `automation/movement_log.md` manually using file writing tools (`replace_file_content`, `write_to_file`, or echo). 
> **ALWAYS** use the dedicated bash script via the terminal: 
> `bash scripts/log_action.sh "OPERATION" "Source" "Destination" "Status" "Notes"`
> This guarantees there are no empty lines injected that break the Markdown table rendering.

**Log Format**:
`| Timestamp | Operation | Source | Destination | Status | Notes |`

**Tracked Operations**:
- `CREATE` / `UPDATE` / `DELETE` / `BULK_GEN` (Agent actions)
- `MAINTENANCE` / `AUDIT` (Manual script runs)

---

## Anki Spaced Repetition (03_Mart)

We use the Obsidian_to_Anki plugin. 

### Card Syntax
Use the **Cloze** style with `{curly braces}` for simplicity.

```markdown
TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
Snowflake micro-partitions are contiguous units of storage between {50 MB} and {500 MB} of uncompressed data.
<!--ID: 1770331406602-->
END

START
Cloze
{Time Travel} in Snowflake allows you to access historical data.
<!--ID: 1770331406610-->
END
```

> [!IMPORTANT]
> **Line Endings (LF)**: Anki cards MUST use Unix (LF) line endings. After generating cards, you **MUST** run:
> `bash scripts/fix_card_line_endings.sh`

### Cleaning Up IDs
The plugin automatically injects `<!--ID: 12345-->` tags to track cards. To remove them safely:
* **Automated**: Run `python scripts/clean_anki_ids.py 03_Mart`.
* **Manual**: In VS Code, use Regex find/replace: `<!--ID: \d+-->\n?`

---

## Scripts Reference

> [!IMPORTANT]
> **Git Bash Required**: If you are generating cards or running scripts on Windows (e.g., via the Gemini CLI or Obsidian terminal), you **must use Git Bash**. Standard PowerShell or Command Prompt will fail to correctly run the `.sh` files due to differing path formats and missing Unix utilities.

All scripts live in the `scripts/` directory. Here is a summary of each one and when to use it.

| Script | Language | Purpose | Usage |
|--------|----------|---------|-------|
| `run_audit.sh` | Bash | **Orchestrator** -- runs the full audit pipeline (Steps 1 and 2 below) in sequence. | `bash scripts/run_audit.sh` |
| `audit_brain.sh` | Bash | **Step 1 of audit** -- fast file-system scan for stale journals, missing tags, naming violations, orphan cards, Brain notes without cards, and consolidation candidates. Outputs raw findings to `automation/audit_raw.txt`. | Called by `run_audit.sh` |
| `audit_brain.py` | Python | **Step 2 of audit** -- smart duplicate detection using SequenceMatcher (70% similarity threshold for notes, 85% for cards). Reads the raw scan from Step 1, then generates the final `automation/audit_report.md`. | Called by `run_audit.sh` |
| `fix_card_line_endings.sh` | Bash | Converts CRLF (Windows) to LF (Unix) line endings on all `.md` files in `03_Mart`. **Required** after generating Anki cards so the Obsidian_to_Anki plugin can parse them. | `bash scripts/fix_card_line_endings.sh` |
| `clean_anki_ids.py` | Python | Removes `<!--ID: ...-->` tracking tags injected by the Obsidian_to_Anki plugin. Accepts a file or directory path. | `python scripts/clean_anki_ids.py <path>` |
| `clean_yaml_tags.py` | Python | Enforces the "One Folder = One Tag" rule across all `02_Brain` files. Rewrites frontmatter so `tags:` contains only the folder's designated tag. Runs in **dry-run** mode by default. | `python scripts/clean_yaml_tags.py` (preview) or `python scripts/clean_yaml_tags.py --apply` (write) |
| `find_missing_cards.py` | Python | Lists all Brain notes in `02_Brain` that do **not** have a corresponding `_cards.md` file in `03_Mart`. Useful for identifying gaps in Anki coverage. | `python scripts/find_missing_cards.py` |
| `log_action.sh` | Bash | **Shared utility** -- sourced by bash scripts to append standardized log entries to `movement_log.md`. | N/A (Internal use) |
| `log_action.py` | Python | **Shared utility** -- imported by python scripts to append standardized log entries to `movement_log.md`. | N/A (Internal use) |

> [!NOTE]
> All the above tools automatically log their operations (as `MAINTENANCE` or `AUDIT`) to `automation/movement_log.md` when you run them.

---

## Mobile Sync (iPhone)

To sync your Second Brain between your PC and iPhone without iCloud:

### Prerequisites
1. **Working Copy** (Git client for iOS) - Download from App Store.
2. Clone your `second_brain` repo in Working Copy.
3. **Obsidian Mobile** - Open the vault from the Working Copy folder.

### Create a "Sync Brain" Shortcut
1. Open the **Shortcuts** app on your iPhone.
2. Tap **+** to create a new shortcut. Name it **"Sync Brain"**.
3. Add these actions (search for "Working Copy"):
 * **Commit Repository**: Repo = `second_brain`, Message = "Mobile sync".
 * **Pull Repository**: Repo = `second_brain`.
 * **Push Repository**: Repo = `second_brain`.
 * **Open App**: App = Obsidian.
1. Add shortcut to Home Screen.
2. npx @google/gemini-cli  

### Usage
* **Before working on mobile**: Tap "Sync Brain" to pull latest from PC.
* **After working on mobile**: Tap "Sync Brain" to push your changes so the PC can see them.
