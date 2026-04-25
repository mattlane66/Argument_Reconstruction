---
name: reconstruct_removal_test
description: Use when testing whether a premise is necessary, redundant, independent, or part of a linked support structure.
---

# Reconstruct Removal Test

Use this skill to test how much work each premise is doing.

## Procedure

For each premise, ask:

`If I take this reason away, does the conclusion still have enough support?`

Then classify the result:
- If no, the premise is necessary or part of a linked/serial structure.
- If yes, the premise may be independent, redundant, or supported by other reasons.
- If the conclusion becomes weaker but not unsupported, the premise is contributory.

## Output format

```markdown
## Removal test
- Remove premise 1: ...
- Remove premise 2: ...
- Result: ...
```

## Example

Input:
1. `Later starts improve mental health.`
2. `Later starts reduce teen driving accidents.`
Conclusion: `School should start later.`

Output:
`If we remove the accidents reason, the mental-health reason could still support starting later on its own. The argument is independent/convergent, so each pillar should be tested separately.`
