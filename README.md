# Second Brain Automation

An Obsidian-based knowledge system for capturing, organizing, and turning technical learning into reusable notes and spaced-repetition cards.

This project is my personal knowledge operations system. It combines Obsidian, markdown conventions, lightweight automation, and AI-assisted workflows to move raw notes into structured technical knowledge.

The goal is simple: reduce the distance between learning something and being able to use it later in interviews, projects, writing, or architecture discussions.

## Why This Repo Exists

Technical learning creates a lot of scattered material:

- quick notes
- screenshots
- article links
- project ideas
- interview concepts
- architecture patterns
- code snippets
- cloud and data engineering references

Without a system, those notes become hard to retrieve. This repo experiments with a workflow that turns raw capture into organized knowledge.

## Core Workflow

```text
01_Raw      -> capture area
02_Brain    -> organized knowledge base
03_Mart     -> Anki-ready learning cards
automation  -> audit logs and maintenance reports
scripts     -> helper scripts for cleanup, logging, and card generation
```

## What The System Does

- Processes raw journal notes into organized markdown files
- Supports deeper technical analysis when a note is marked for explanation
- Generates Anki-style cards for spaced repetition
- Tracks note movement and maintenance activity
- Audits the knowledge base for duplicates, missing tags, and stale files
- Supports Obsidian workflows across desktop and mobile

## Agent Roles

The project uses a few role-based workflows:

| Role | Purpose |
|---|---|
| Librarian | Organizes and files notes without adding unnecessary content |
| Principal Engineer | Expands selected notes into deeper technical explanations, examples, and diagrams |
| Auditor | Checks the vault for consistency, duplicates, and maintenance issues |

## Why This Matters For Data Engineering

Data engineering has a large surface area: Spark, SQL, orchestration, cloud services, lakehouse design, warehouse modeling, cost optimization, reliability, and system design.

This repo helps turn that learning into a reusable body of knowledge instead of a pile of disconnected notes.

It also supports writing and interview preparation by keeping concepts, examples, and project stories easier to retrieve.

## Repository Structure

```text
second_brain/
├── .agent/workflows/
├── .obsidian/
├── 01_Raw/
├── 02_Brain/
├── 03_Mart/
├── Templates/
├── automation/
├── scripts/
├── AGENT.md
└── User_Guide.md
```

## Key Scripts

| Script | Purpose |
|---|---|
| `run_audit.sh` | Runs the full vault audit workflow |
| `audit_brain.sh` | Scans for stale journals, missing tags, naming issues, and consolidation candidates |
| `audit_brain.py` | Performs duplicate detection and generates the final audit report |
| `post_process.sh` | Handles line-ending fixes, deletion, and logging |
| `clean_anki_ids.py` | Removes Anki plugin tracking IDs |
| `clean_yaml_tags.py` | Normalizes tags based on folder rules |
| `find_missing_cards.py` | Finds Brain notes without matching Anki cards |

## Notes

This is a personal productivity and learning system, not a general-purpose product. The value is in the workflow design: raw capture, structured processing, spaced repetition, auditing, and repeatable knowledge maintenance.

## Related Writing Ideas

- How I use Obsidian as a technical learning system for data engineering
- Turning raw notes into interview-ready knowledge
- Building a lightweight audit system for a personal knowledge base
- Using AI-assisted workflows without losing control of the knowledge structure
