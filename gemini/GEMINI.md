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
| `99_Misc` | Uncategorized (review later) | #default | Anything else |

### Tagging Rules
> [!IMPORTANT]
> **Rule 1**: Every file MUST have its folder's mandatory tag.
> **Rule 2**: Use ONLY existing tags (from the table above) or broad terms like `#spark`, `#aws`.
> **Rule 3**: If a new, unique tag is needed, the file MUST go to `99_Misc`.

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

---

## 3. Node Identification Parameters

### Append Format (for adding to existing files)
When appending to an existing file, use this separator and header:

```markdown
---
[New Entry]
created_at: "{{date}} {{time}}"
status: seed
processed: false
Explain: false [Full explanation of the concept - detailed and comprehensive]
tags: [relevant, topic, tags]
examples: 
  - dataengineering[1]: [Realtime implementation example with actual code/configuration]
  - [specified-tool][2]: [Realtime implementation OR default to dataengineering if irrelevant]
diagram: NA [or describe if diagram would be helpful]
---

### [Topic Title]
(Content goes here...)
```

### The "Realtime" Rule
**Criterion**: At least ONE example must be a practical "Realtime" implementation.

1.  **Definition**: Realtime = Practical implementation example using actual tools/platforms.
2.  **Default Field**: Data Engineering.
3.  **Selection Logic**:
    - **User specifies tool**: Show implementation in that tool.
    - **Tool not specified**: Default to Data Engineering implementation.
    - **Tool irrelevant**: Fall back to Data Engineering (e.g., if user asks "Iceberg in Tableau", use Data Engineering instead).
4.  **Format**: Show HOW to implement (code/config), not just WHAT it is.

---

## 4. LLM Integration (Principal Engineer)

### Step 1: Note Identification
User points to a journal entry in `01_Raw/` and asks for analysis.

### Step 2: Invoke
Command: **"Deep dive this"** or **"Analyze my latest journal"**

### Step 3: Analysis
1.  **Concept**: Define what the user asked about.
2.  **The Realtime Example** (Strict adherence to Rule above).
3.  **Syntax/Code**: Python, SQL, YAML, etc.
4.  **Visuals**: Mermaid diagram (if relevant).
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
