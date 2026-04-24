---
name: reconstruct_fallacy_check
description: Use when an argument needs to be checked for equivocation, shortcuts, term shifts, or common fallacies.
---

# Reconstruct Fallacy Check

Use this skill after mapping the conclusion, premises, and hidden bridge.

## Common checks

- Equivocation: Does a key term shift meanings?
- Hasty generalization: Is a broad claim based on too little evidence?
- False dichotomy: Are alternatives excluded without reason?
- Circular reasoning: Does the premise assume the conclusion?
- Correlation/causation shortcut: Is causation inferred too quickly?
- Scope shift: Does the argument move from some cases to all cases?
- Metric shift: Does it treat related but distinct outcomes as identical?
- Burden shift: Does it demand disproof instead of providing support?

## Output format

```markdown
## Shortcut / fallacy check
Possible issue: ...

## Why it matters
...

## Repair
...
```

## Example

Input:
`Some students are tired in first period, so the whole school should start later.`

Output:
`The argument may slide from "some students are tired" to "the whole school schedule is harmful." To repair it, show that the tiredness is widespread, caused by the schedule, and better solved by later start times than by alternatives.`
