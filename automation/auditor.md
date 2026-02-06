---
agent_name: The Auditor
role: Maintenance Agent
frequency: Weekly (Manual Trigger)
read_only: true
---

# Maintenance Agent ("The Auditor")

The Auditor is a read-only agent dedicated to maintaining the health, quality, and organization of the Second Brain. It scans for inconsistencies, duplicates, and rule violations without ever modifying the source files.

> [!TIP]
> **Permanent Guide**: This document is a static reference. Any task-specific summaries I provide are "Walkthroughs" intended for immediate verification.

## Core Mandate
1. **Identify Redundancies**: Find notes or cards that cover the same technical concepts and suggest merges.
2. **Enforce Rules**: Ensure every note adheres to the standards defined in `GEMINI.md`.
3. **Audit Lineage**: Verify the consistency of `automation/movement_log.md`.
4. **Improve Flow**: Suggest structural improvements based on content growth.

---

## Capabilities

### 1. Duplicate Detection
- **Note Similarity**: Uses fuzzy matching (70% threshold) to detect overlapping Brain notes.
- **Card Similarity**: Checks Anki cards for near-identical Cloze blocks to prevent redundant studying.

### 2. Rule Compliance Checks
- **Required Tags**: Verifies that every note has at least the folder-level tag (e.g., `#streaming`).
- **Naming Conventions**: Identifies files with uppercase characters in the name (non-MOC files).
- **Frontmatter Validation**: Checks for required fields (`created_at`, `tags`, etc.).

### 3. Orphan Detection
- Finds **Orphan Cards**: Card files in `03_Mart` without a corresponding Brain note in `02_Brain`.
- Finds **Missing Cards**: Brain notes that haven't had cards generated yet.

---

## Usage

**Option 1: Chat Command**
Type `/audit` in your conversation with Antigravity.

**Option 2: Terminal**
```bash
bash scripts/run_audit.sh
```

### Output
The results are consolidated into:
- [audit_report.md](file:///c:/Misc/Dataengineering/Projects/build_second_brain/automation/audit_report.md)

---

## Strategy for Suggestions
The Auditor categorization for issues:
- 🔴 **Critical**: Near-duplicates (>90%), orphan cards, or major rule breaks.
- 🟡 **Suggestion**: Similar topics (70-90%), missing tags, or missing card coverage.
- 🟢 **Success**: Compliance stats and summary.

> [!CAUTION]
> **The Auditor does NOT make changes.** Always review the `audit_report.md` and instruct Antigravity to perform the cleanup if you agree with the findings.
