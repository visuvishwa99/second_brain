TARGET DECK: SecondBrain::09_AI

START
Cloze
The core principle for reliable AI agents is the separation of {Intelligence (Probabilistic)} and {Enforcement (Deterministic)}.
END

START
Cloze
The {Intelligence} layer, typically an LLM, is {Probabilistic} and focuses on {Reasoning, Planning, and generating options}.
END

START
Cloze
The {Enforcement} layer, which is {Deterministic}, handles {Validation, Permissioning, and Execution}.
END

START
Cloze
{Prompt Engineering} for safety is considered {advisory} because it relies on model alignment and can be bypassed.
END

START
Cloze
Effective agentic harnesses, like strict implementations of Claude Code, involve the model {proposing an action block} which the harness {intercepts, validates against a whitelist/blacklist}, and then {executes only if validation passes}.
END

START
Cloze
A safe workflow involves defining scope with {deterministic code for permissions}, running destructive actions in {isolated sandboxes}, and inspecting logical plans with {lifecycle hooks}.
END
