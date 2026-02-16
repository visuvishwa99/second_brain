---
created_at: 2026-02-09 09:44
tags:
  - ai
status: sapling
---

# AI Safety: Advisory vs. Deterministic Architecture

> "Please don't delete important files" is a hope.
> A pre-execution hook that blocks `rm -rf` is a guarantee.

This note outlines a core architectural principle for building reliable AI agents: **The separation of Intelligence (Probabilistic) and Enforcement (Deterministic).**

## The Core Distinction

| Layer | Component | Nature | Role | Example |
| :--- | :--- | :--- | :--- | :--- |
| **Intelligence** | The Model (LLM) | Probabilistic | Reasoning, Planning, generating options | "I think I should delete this temp file." |
| **Enforcement** | The Harness (Code) | Deterministic | Validation, Permissioning, Execution | `if cmd == 'rm -rf': raise PermissionError` |

## Why "Prompt Engineering" for Safety Fails
Attempting to secure an agent via system prompts ("You are a safe agent, do not do bad things") is **advisory**. It relies on the model's alignment training, which can be bypassed (jailbroken) or simply fail due to stochasticity.

**Deterministic Code** (if-statements, OS-level permissions, sandboxing) provides a **guarantee**.

## Case Study: Claude Code
Effective agentic harnesses (like strict implementations of Anthropic's `computer-use` or `Claude Code`) follow this pattern:
1.  **The Model Reasons**: It proposes an action block.
2.  **The Harness Intercepts**: Before execution, a script validates the action against a whitelist/blacklist.
3.  **The Harness Executes**: Only if validation passes.

## Implementation Pattern
The User Interface for an AI Engineer isn't just the prompt window; it's the **boundary** definition.

**Safe Workflow**:
1.  **Permissions**: Use deterministic code to define scope.
2.  **Sandboxing**: Run potentially destructive actions in isolated containers (Docker, Firecracker).
3.  **Hooks**: Use lifecycle hooks to inspect logical plans before they become physical actions.

**Conclusion**: The model provides intelligence. The harness provides reliability. One is probabilistic; the other never fails.
