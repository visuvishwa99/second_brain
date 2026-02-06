# Antigravity User Guide

This guide explains how to interact with your AI agent (Antigravity) to manage your Second Brain.

> [!TIP]
> **Guide vs. Walkthrough**: 
> - **Guides** (like this one) are **permanent** project manuals meant for long-term reference. 
> - **Walkthroughs** (AI artifacts) are **temporary** "change logs" or summary reports generated for a specific task. Once you've reviewed a walkthrough, you can rely on the permanent Guides.

## The Personas

### 1. The Librarian
* **Role**: Organizer, categorizer, cleaner.
* **Goal**: Move notes from `01_Raw` to `02_Brain` without adding heavy content.
* **Trigger Condition**: `Explain: false` in your note.

### 2. The Principal Engineer
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
 * Generates a report in `agents/audit_report.md`.

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
move_journal_to_brain: true # Append/Create in 02_Brain.
move_brain_to_mart: true # Generate Anki cards in 03_Mart.
---
```

---

## Logging & Knowledge Lineage

Every movement from `01_Raw` to `02_Brain` is logged in [movement_log.md](file:///c:/Misc/Dataengineering/Projects/build_second_brain/agents/movement_log.md) for auditability.

**Log Format**:
`| Timestamp | Operation | Source | Destination | Status | Notes |`

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
* **Automated**: Run `bash scripts/clean_anki_ids.sh`.
* **Manual**: In VS Code, use Regex find/replace: `<!--ID: \d+-->\n?`

---

## Mobile Sync (iPhone)

To sync your Second Brain between your PC and iPhone without iCloud:

### Prerequisites
1. **Working Copy** (Git client for iOS) - Download from App Store.
2. Clone your `build_second_brain` repo in Working Copy.
3. **Obsidian Mobile** - Open the vault from the Working Copy folder.

### Create a "Sync Brain" Shortcut
1. Open the **Shortcuts** app on your iPhone.
2. Tap **+** to create a new shortcut. Name it **"Sync Brain"**.
3. Add these actions (search for "Working Copy"):
 * **Commit Repository**: Repo = `build_second_brain`, Message = "Mobile sync".
 * **Pull Repository**: Repo = `build_second_brain`.
 * **Push Repository**: Repo = `build_second_brain`.
 * **Open App**: App = Obsidian.
4. Add shortcut to Home Screen.

### Usage
* **Before working on mobile**: Tap "Sync Brain" to pull latest from PC.
* **After working on mobile**: Tap "Sync Brain" to push your changes so the PC can see them.
