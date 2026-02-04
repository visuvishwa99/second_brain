# Antigravity User Guide

This guide explains how to interact with your AI agent (Antigravity) to manage your Second Brain.

## 🤖 The Personas

### 1. The Librarian 📚
*   **Role**: Organizer, categorizer, cleaner.
*   **Goal**: Move notes from `01_Raw` to `02_Brain` without adding heavy content.
*   **Trigger Condition**: `Explain: false` in your note.

### 2. The Principal Engineer 👷
*   **Role**: Senior Architect, Mentor.
*   **Goal**: Deeply analyze a concept, provide real-world Data Engineering examples, write code, and draw diagrams.
*   **Trigger Condition**: `Explain: true` in your note.

---

## 🗣️ Command Triggers

Since Antigravity is a natural language agent, you can talk to it normally. Use these phrases to trigger specific workflows:

### Option 1: The "Librarian" Trigger (Batch Processing)
Use this when you have written notes and just want them filed away.
*   **Say**: *"Process my notes"* or *"Organize my journals"*
*   **Action**: 
    *   Scans `01_Raw` for files with `processed: false`.
    *   Proposes a folder in `02_Brain` (e.g., `01_Concepts`, `04_Cloud`).
    *   Moves them upon approval.

### Option 2: The "Principal Engineer" Trigger (Deep Dive)
Use this when you want to learn.
*   **Say**: *"Deep dive this"* or *"Analyze my latest note"*
*   **Action**: 
    *   Finds the latest journal entry.
    *   **If `Explain: true`**: Generates a full technical analysis (Concepts + Realtime Examples + Code + Diagrams).
    *   **If `Explain: false`**: summarizing it concisely.

### Option 3: Specific Pointer
Use this to target a specific file.
*   **Say**: *"Process 2026-02-04.md"*
*   **Action**: Runs the workflow on that specific file only.

---

## 📝 The Journal Template Rules

Your journal template controls the AI's behavior.

```yaml
---
processed: false        # false = Agent will look at it. true = Agent ignores it.
Explain: false          # false = Just file it. true = DEEP DIVE it.
examples: dataengineering[1]  # The "Realtime Rule": Must have 1 practical DE example.
diagram: false          # true/mermaid = Agent creates a Mermaid diagram.
---
```
