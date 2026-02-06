TARGET DECK: SecondBrain::09_AI

START
Cloze
{AI Sandboxing} is the practice of executing AI-generated code in a restricted environment to prevent unauthorized access to {Network}, {Connectors}, or {File System}.
END

START
Cloze
{Pydantic Monty} is a Rust-based Python interpreter designed for strict sandboxing, allowing {pure computation} but blocking I/O and builtins.
END

START
Cloze
Executing LLM code with standard Python `{exec()}` is dangerous because it inherits the {permissions} of the host machine (access to env vars, secrets).
END

START
Cloze
Compared to running code in a Docker container, **Monty** provides {faster} execution (milliseconds vs seconds) but has {lower} capability (no external libraries/network).
END

START
Cloze
In a **Zero Trust** AI pipeline, the LLM should generate code that is executed by a {Sandbox} (like Monty/WASM) before the results touch the production database.
END
