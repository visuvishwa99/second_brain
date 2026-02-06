# Data Engineering Knowledge Pipeline Rules

## 1. Folder Structure & Tag Rules

### Folder Taxonomy

| Folder | Purpose | Mandatory Tag | Keywords (for auto-classification) |
|--------|---------|---------------|-------------------------------------|
| `01_Concepts` | Theory, foundational ideas | `#concepts` | ACID, CAP, normalization, RAG, LLM |
| `02_Compute` | Processing engines | `#compute` | Spark, Databricks, Hadoop |
| `03_Streaming` | Real-time data | `#streaming` | Kafka, Flink, real-time, PubSub |
| `04_Cloud` | Cloud platforms & services | `#cloud` | AWS, Azure, GCP, IAM, S3 |
| `05_Warehousing` | Data warehouses & modeling | `#warehousing` | Snowflake, dbt, SQL, BigQuery, Iceberg |
| `06_Ingestion` | ETL/ELT tools | `#ingestion` | Airbyte, Fivetran, APIs |
| `07_Languages` | Programming | `#languages` | Python, Scala, Bash |
| `08_Architecture` | Patterns & design | `#architecture` | Medallion, Lakehouse, Mesh |
| `09_AI` | Artificial Intelligence | `#ai` | LLM, RAG, Agents, OpenAI |
| `99_Misc` | Uncategorized (review later) | `#misc` | Anything else |

### Tagging Rules (One Folder = One Tag)
> [!IMPORTANT]
> **Rule 1**: Use **ONLY** the high-level tag corresponding to the folder (e.g., `#streaming` for `03_Streaming`).
> **Rule 2**: Do NOT use sub-tags like "kafka" or "spark_streaming". Use the file name for specificity.
> **Rule 3**: This ensures the Obsidian Graph is clean and clustered by domain.

### 99_Misc Special Rules
> [!NOTE]
> - Files in `99_Misc` should have **NO tags** (or only `#misc` if required for tracking).
> - This ensures `99_Misc` files do NOT appear in the Obsidian Graph View.
> - These files are for temporary storage and manual review only.

---

## 2. Journal-to-Brain Workflow (The Librarian)

### Core Principle
Organize knowledge by topic files, not by creating scattered individual files for each question. **Search First, Create Later.**

### Trigger
Command: `Process my notes` or `Analyze my latest journal`

### Workflow Steps
1. **Scan**: User points to a journal file in `./01_Raw/`.
2. **Search Existing Files**:
   - Check `02_Brain` for an existing file matching the topic.
3. **Process & Move (Direct)**:
   - If `move_journal_to_brain: true` -> Append/Create in `02_Brain/<Folder>/<Topic>.md`.
   - If `move_brain_to_mart: true` -> Generate cards in `03_Mart/<Folder>/<Topic>_cards.md`.
   - Delete source file from `01_Raw`.
   - Log action to `automation/movement_log.md`.

### Post-Publish Checklist (CRITICAL)
After publishing, Antigravity MUST complete these steps:
- [ ] Write/Append content to `02_Brain/<Category>/<File>.md`
- [ ] If `move_brain_to_mart: true`, generate cards to `03_Mart/<Category>/<File>_cards.md`
- [ ] Delete source file from `01_Raw` using `rm` (NOT `del`)
- [ ] Update source journal frontmatter: `processed: true`
- [ ] Log action to `automation/movement_log.md` (see Logging Rules below)

### Logging Rules

**Purpose**: Track knowledge lineage (where content came from, where it went).

**Log Schema**:
```
| Timestamp | Operation | Source | Destination | Status | Notes |
```

**Operations to Log**:
| Operation | When to Log |
|-----------|-------------|
| `CREATE` | New file created in Brain or Mart |
| `UPDATE` | Significant changes to a Brain note (new sections, major rewrites) |
| `DELETE` | File removed from any folder |
| `BULK_GEN` | Multiple files generated/regenerated |

**Do NOT Log**: Reads, minor typo fixes, failed operations.

**Example Entries**:
```markdown
| 2026-02-06 09:59 | CREATE | 2026-02-06_09-55-40.md | 09_AI/sandboxed_ai.md | Success | Deep dive on Monty |
| 2026-02-06 10:15 | CREATE | - | 09_AI/sandboxed_ai_cards.md | Success | 5 cards |
| 2026-02-06 11:00 | UPDATE | - | 05_Warehousing/scd.md | Success | Added SCD Type 2 |
| 2026-02-06 12:00 | DELETE | - | 99_Misc/temp_note.md | Success | Duplicate |
| 2026-02-05 16:30 | BULK_GEN | - | 03_Mart/ | Success | 22 cards regenerated |
```

> [!IMPORTANT]
> **Folder Creation is NOT Allowed**: All folders are pre-established. If a note doesn't fit, use `99_Misc`.

---

## 2.5 Rules for 03_Mart (Anki Cards)

### Folder Structure
Mirror `02_Brain` folder structure:
- `03_Mart/01_Concepts`
- `03_Mart/02_Compute`
- `03_Mart/03_Streaming`
- `03_Mart/04_Cloud`
- `03_Mart/05_Warehousing`
- `03_Mart/06_Ingestion`
- `03_Mart/07_Languages`
- `03_Mart/08_Architecture`
- `03_Mart/09_AI`
- `03_Mart/99_Misc`

### Card File Naming
`<topic>_cards.md` (e.g., `snowflake_cards.md`)

### Anki Card Syntax (CurlyCloze)
Use **Cloze** style with single `{curly braces}`:
```markdown
TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
Snowflake micro-partitions are between {50 MB} and {500 MB} of uncompressed data.
END

START
Cloze
{Time Travel} allows access to historical data in Snowflake.
END
```

> [!IMPORTANT]
> **Blank Line Required**: There MUST be a blank line between each `END` and the next `START`.
> **Line Endings**: Card files MUST use **LF** (Unix) line endings, NOT CRLF (Windows). After creating card files, run: `sed -i 's/\r$//' <file.md>`

---

## 3. Template Field Definitions

### Journal Template Fields
```yaml
---
created_at: "{{date}} {{time}}"
status: seed
processed: false        # false = Agent will process. true = Skip.
Explain: false          # true = Deep Dive analysis. false = Concise summary.
tags:                   # Folder tag (streaming, warehousing, etc.)
examples: 1             # Number of syntax/code examples to include.
Realtime: false         # true = Add a Production-Grade Scenario.
diagram: false          # true = Generate a Mermaid diagram.
---
```

### Field Logic

| Field | Value | Behavior |
|-------|-------|----------|
| `Explain` | `true` | Full Principal Engineer analysis (concepts, code, diagrams). |
| `Explain` | `false` | Concise Librarian summary (just organize and file). |
| `examples` | `1`, `2`, etc. | Number of small syntax/usage code snippets to include. |
| `Realtime` | `true` | Add a **Production-Grade Scenario** based on `tags` + note content. |
| `Realtime` | `false` | No production scenario, just the standard examples. |
| `diagram` | `true` | Generate a Mermaid diagram for the concept. |

### The "Realtime" Rule (Context-Aware)

When `Realtime: true`:
1.  **Read `tags`**: Determines the domain (e.g., `streaming`, `warehousing`).
2.  **Read note content**: Infers the specific tool (e.g., Kafka, Snowflake).
3.  **Generate**: A complex, **end-to-end Production Scenario** using industry-standard tools.
    *   Example for `streaming`: Kafka Source -> Spark Structured Streaming -> Delta Lake Sink.
    *   Example for `warehousing`: CDC Ingestion -> dbt Transformations -> Snowflake serving layer.
4.  **Fallback**: If no tool can be inferred, default to a generic Data Engineering scenario.

---

## 4. LLM Integration (Principal Engineer)

### Step 1: Note Identification
User points to a journal entry in `01_Raw/` and asks for analysis.

### Step 2: Invoke
Command: **"Deep dive this"** or **"Analyze my latest journal"**

### Step 3: Analysis
1.  **Concept**: Define what the user asked about.
2.  **Code Examples**: Based on `examples` count.
3.  **Realtime Scenario**: If `Realtime: true`, add production-grade implementation.
4.  **Visuals**: Mermaid diagram (if `diagram: true`).
5.  **Flashcard**: Q/A for Anki.

### Step 4: Propose & Confirm
Before appending, Antigravity MUST:
1. **State the target file**: e.g., *"I will append to `02_Brain/05_Warehousing/Snowflake.md`"*
2. **Wait for user confirmation**.

### Global Rules
1. **No Emojis**: Use plain text (e.g., "X", "Note", "tip").
2. **Detailed Explanations**: Provide comprehensive, actionable content.

---

## 4.5 Maintenance & Quality Control (The Auditor)

### Agent Overview
The **Auditor** is a read-only agent that ensures the Second Brain remains high-quality and consistent with these rules.

### Audit Trigger
**Command**: `bash scripts/run_audit.sh`

### Audit Scope
- Identifying duplicate/similar topics (70% threshold).
- Detecting missing tags or incomplete frontmatter.
- Finding orphan Anki cards (Mart cards without a Brain source).
- Identifying naming convention violations.
- Identifying stale unprocessed journals in `01_Raw`.

### Process
1. Run the audit script.
2. Review findings in `automation/audit_report.md`.
3. Inform Antigravity to perform necessary merges or cleanups.

---

## 5. Technical Notes for Antigravity

### Shell Commands
- The user's terminal runs **Bash** (even on Windows).
- Use `rm` to delete files, NOT `del`.
- Use `mv` to move files, NOT `move`.

### File Operations
- Prefer using `write_to_file` with `Overwrite: true` to move content (avoids shell issues).
- After writing to destination, use `rm` to clean up staged files.

### Anki Card Post-Processing (CRITICAL)
- **After generating ANY card files**, Antigravity MUST run: `bash scripts/fix_card_line_endings.sh`
- This converts CRLF (Windows) to LF (Unix) which is required for the Obsidian_to_Anki plugin.

### Frontmatter Formatting
- Always ensure a newline before the closing `---` delimiter.
- Use `false`/`true` (lowercase) for boolean properties, not `F`/`T`.

### File Naming Conventions
- **MOC Files**: Must be ALL CAPS with MOC suffix (e.g., `CONCEPT_MOC.md`, `WAREHOUSING_MOC.md`).
- **Standard Notes**: Must be **lowercase** with **underscores** (e.g., `snowflake_cortex.md`, `delta_lake.md`).
