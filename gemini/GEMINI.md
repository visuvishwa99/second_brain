# Data Engineering Knowledge Pipeline Rules

## 1️⃣ Folder Structure & Tag Rules

### Folder Taxonomy

| Folder            | Purpose                      | Mandatory Tag   | Keywords (for auto-classification)     |
| ----------------- | ---------------------------- | --------------- | -------------------------------------- |
| `01_Concepts`     | Theory, foundational ideas   | `#concepts`     | ACID, CAP, normalization, RAG, LLM     |
| `02_Compute`      | Processing engines           | `#compute`      | Spark, Databricks, Hadoop              |
| `03_Streaming`    | Real-time data               | `#streaming`    | Kafka, Flink, real-time, PubSub        |
| `04_Cloud`        | Cloud platforms & services   | `#cloud`        | AWS, Azure, GCP, IAM, S3               |
| `05_Warehousing`  | Data warehouses & modeling   | `#warehousing`  | Snowflake, dbt, SQL, BigQuery, Iceberg |
| `06_Ingestion`    | ETL/ELT tools                | `#ingestion`    | Airbyte, Fivetran, APIs                |
| `07_Languages`    | Programming                  | `#languages`    | Python, Scala, Bash                    |
| `08_Architecture` | Patterns & design            | `#architecture` | Medallion, Lakehouse, Mesh             |
| `99_Misc`         | Uncategorized (review later) | #default        | Anything else                          |

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

## 2️⃣ Journal-to-Brain Workflow (The Librarian)

### Trigger
Command: `Process my notes` or `Analyze my latest journal`

### Workflow Steps
1. **Scan**: User points to a journal file in `./01_Raw/`.
2. **Check**: If `processed: true` in frontmatter, skip.
3. **Draft (Staging)**: 
   - Antigravity generates the deep dive content.
   - Saves the file to `./01_Raw/stage/<Filename>.md`.
   - *Note*: The flashcard is temporarily held here or in memory.
4. **Review**: User checks the file in `stage`.
5. **Publish**: 
   - User says "Approve" or "Move to Brain".
   - Antigravity moves the file from `stage` to `./02_Brain/pages/<Category>/`.
   - Appends flashcard to `./03_Mart/anki_imports.md`.
   - Marks source journal as `processed: true`.

---

## 3️⃣ Node Identification Parameters

To make the Obsidian Graph View useful, every note must have these properties:

```yaml
---
created_at: "YYYY-MM-DD HH:MM"
tags: [mandatory_tag, specific_tech]
Explain: F                         # T = Needs explanation, F = Done
examples: 2                        # Count of examples
Realtime: NA                       # NA/Yes/Partial
diagram: mermaid                   # If a diagram is present
status: seed | sapling | evergreen # Note maturity
---
```

### Obsidian Graph Groups (Copy to Settings)
- `tag:#concepts`     → 🔴 Red
- `tag:#compute`      → 🟠 Orange
- `tag:#streaming`    → 🔵 Blue
- `tag:#cloud`        → 🟢 Green
- `tag:#warehousing`  → 🟣 Purple
- `tag:#architecture` → 🟡 Yellow

> **Note**: `99_Misc` is intentionally NOT in this list. Files there will not appear in the Graph.

---

## 4️⃣ LLM Integration (Principal Engineer)

### Step 1: Note Identification
User points to a journal entry in `01_Raw/` and asks for analysis.

### Step 2: Invoke
Command: **"Deep dive this"** or **"Analyze my latest journal"**

### Step 3: Analysis (The Realtime Rule)
**Criterion**: At least ONE example must be a practical "Realtime" implementation.

1.  **Concept**: Define what the user asked about.
2.  **The Realtime Example**:
    - **Default**: Data Engineering implementation.
    - **Specific**: If the user asks about a specific tool (e.g., Tableau), show the implementation there *if relevant*. If not, fallback to DE.
    - **How-To**: Show code, configuration, or specific steps.
3.  **Syntax/Code**: Python, SQL, YAML, etc.
4.  **Visuals**: Mermaid diagram (if relevant).
5.  **Flashcard**: Q/A for Anki.

### Step 4: Propose & Confirm
Before appending, Antigravity MUST:
1. **State the target file**: e.g., *"I will append to `02_Brain/pages/01_Concepts/LangChain.md`"*
2. **Wait for user confirmation** ("OK" or correction).
3. Only then write to the file.

### Status Updates
- Change `Explain: T` → `Explain: F`
- Change `status: seed` → `status: sapling`
- Change `examples: <count>` → `examples: dataengineering[1]` (or appropriate tool)
- Change `diagram: <bool>` → `diagram: F` (if no diagram) or `mermaid`

