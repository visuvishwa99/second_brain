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

## Trigger
Command: `Process my notes` or `Analyze my latest journal`

### Workflow Steps
1. **Scan**: User points to a journal file in `./01_Raw/`.
2. **Search Existing Files**:
   - Check `02_Brain` for an existing file matching the topic (e.g., if topic is "Snowflake Time Travel", look for `Snowflake.md`).
3. **Draft (Staging)**: 
   - **If Existing File Found**: Prepare an **Append Entry** (see format below).
   - **If No Match**: Prepare a **New File**.
   - Save the draft to `./01_Raw/stage/<Topic>.md` for review.
4. **Review**: User checks the file in `stage`.
5. **Publish**: 
   - User says "Approve" or "Move to Brain".
   - Antigravity appends/moves content to the target file in `02_Brain`.
   - Appends flashcard to `./03_Mart/anki_imports.md`.
   - Marks source journal as `processed: true`.

### Post-Publish Checklist (CRITICAL)
After publishing, Antigravity MUST complete these steps:
- [ ] Write/Append content to `02_Brain/pages/<Category>/<File>.md`
- [ ] Delete staged file from `01_Raw/stage/` using `rm` (NOT `del`)
- [ ] Update source journal frontmatter: `processed: true`
- [ ] Append flashcard to `03_Mart/anki_imports.md`
- [ ] Log to `agents/movement_log.md` using this format:
      `| YYYY-MM-DD HH:MM:SS | <SourceFile> | <DestinationFolder> | Success |`

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
1. **State the target file**: e.g., *"I will append to `02_Brain/pages/05_Warehousing/Snowflake.md`"*
2. **Wait for user confirmation**.

### Global Rules
1. **No Emojis**: Use plain text (e.g., "X", "Note", "tip").
2. **Detailed Explanations**: Provide comprehensive, actionable content.

---

## 5. Technical Notes for Antigravity

### Shell Commands
- The user's terminal runs **Bash** (even on Windows).
- Use `rm` to delete files, NOT `del`.
- Use `mv` to move files, NOT `move`.

### File Operations
- Prefer using `write_to_file` with `Overwrite: true` to move content (avoids shell issues).
- After writing to destination, use `rm` to clean up staged files.

### Frontmatter Formatting
- Always ensure a newline before the closing `---` delimiter.
- Use `false`/`true` (lowercase) for boolean properties, not `F`/`T`.

### File Naming Conventions
- **MOC Files**: Must be ALL CAPS with MOC suffix (e.g., `CONCEPT_MOC.md`, `WAREHOUSING_MOC.md`).
- **Standard Notes**: Must be **lowercase** with **underscores** (e.g., `snowflake_cortex.md`, `delta_lake.md`).
