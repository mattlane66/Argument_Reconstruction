---
name: reconstruct_hidden_bridge
description: Use when an argument's missing premise, warrant, or enthymeme needs to be identified.
---

# Reconstruct Hidden Bridge

Use this skill to identify what must be assumed for the explicit premises to support the conclusion.

## Procedure

1. State the explicit premises and conclusion.
2. Ask: `What unstated assumption must be true for these premises to connect to this conclusion?`
3. Complete: `For that to follow, you would also have to assume that...`
4. Distinguish missing logic from disputed factual premises.

## Output format

```markdown
## Hidden bridge
For that to follow, you would also have to assume that...

## Pressure point
The main issue is...
```

## Quality checks

- The hidden bridge should connect premise to conclusion.
- It should not merely repeat the conclusion.
- It should expose the real burden of proof.

## Example

Input:
- Premise: `Some students are tired in first period.`
- Conclusion: `The school should start later.`

Output:
`For that to follow, you would also have to assume that first-period tiredness is caused mainly by the current start time, that the problem is significant enough to justify a school-wide change, that a later start would meaningfully solve it, and that the benefits outweigh the tradeoffs.`
