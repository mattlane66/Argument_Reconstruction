---
name: reconstruct_reality_check
description: Use when an argument needs to be evaluated against the right epistemic standard: validity, soundness, strength, cogency, or explanatory quality.
---

# Reconstruct Reality Check

Use this skill after reconstructing the argument's conclusion, premises, hidden bridge, and linkage.

## Choose the right standard

- Deductive argument: valid or invalid; if valid and premises are true, sound.
- Inductive argument: strong or weak; if strong and premises are true, cogent.
- Causal, policy, moral, or practical argument: usually assess cogency, tradeoffs, and evidence quality.
- Explanation: ask whether it is hard-to-vary or whether small edits could make it support many incompatible conclusions.

## Procedure

1. Identify the argument type.
2. Name the evaluation standard.
3. Separate structural quality from factual truth.
4. Identify what evidence would strengthen or weaken the argument.
5. State the current confidence level.

## Output format

```markdown
## Reality check
Argument type: ...
Standard: ...
Assessment: ...

## What would change my mind
- ...
```

## Example

Input:
`School should start later because later starts increase teen sleep, improve learning, improve mental health, and reduce teen driving accidents.`

Output:
`This is a real-world policy argument, so the standard is cogency rather than deductive validity. The argument becomes strong if the causal premises are supported by evidence and if the benefits outweigh implementation tradeoffs such as transportation, childcare, work schedules, and extracurriculars.`
