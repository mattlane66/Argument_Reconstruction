# Contract cases

`cases.json` defines behavioral invariants for representative argument types and failure modes. These cases do not require exact prose. A model or agent passes when it performs the required analytical moves and avoids the prohibited ones.

The deterministic repository validator checks the test schema and coverage. Runtime evaluation should feed each `input` to the skill and judge the response against `required_moves` and `prohibited_moves`.

Coverage includes:

- claim-only input
- valid and invalid deduction
- statistical induction
- causal inference
- inference to the best explanation
- practical policy reasoning
- linked, convergent, serial, and mixed support
- equivocation
- analogy
- moral reasoning
- arguments with objections and rebuttals
