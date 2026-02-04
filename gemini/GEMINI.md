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
2. **Analyze**: Antigravity reads the content and generates:
   - **Concept Definition**: High-level explanation.
   - **Real-time DE Example**: Specific implementation.
   - **Syntax**: Code snippets.
   - **Mermaid Diagram** (if applicable).
   - **Flashcard**: Q/A for Anki.
3. **Propose Destination**:
   - Antigravity tells the user: *"I plan to append this to `02_Brain/pages/<Category>/<Filename>.md`"*
   - If classification is uncertain → `99_Misc` (no tag).
4. **User Approval**: User says "OK" or corrects the destination.
5. **Append**: Antigravity appends the content to the target file.
6. **Log**: Flashcard appended to `./03_Mart/anki_imports.md`.

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

### Step 3: Output Structure
1. **Concept Definition**: High-level explanation.
2. **Real-time Example**: Specific DE implementation.
3. **Syntax**: Code snippets.
4. **Visuals**: Mermaid diagram (if `diagram: mermaid` requested).
5. **Flashcard**: Appended to `03_Mart/anki_imports.md`.

### Step 4: Propose & Confirm
Before appending, Antigravity MUST:
1. **State the target file**: e.g., *"I will append to `02_Brain/pages/01_Concepts/LangChain.md`"*
2. **Wait for user confirmation** ("OK" or correction).
3. Only then write to the file.

### Status Updates
- Change `Explain: T` → `Explain: F`
- Change `status: seed` → `status: sapling`
