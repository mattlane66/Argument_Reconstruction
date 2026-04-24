---
name: reconstruct_linkage
description: Use when the structure of support in an argument needs to be classified as linked, serial, independent, convergent, mixed, or insufficient.
---

# Reconstruct Linkage

Use this skill to map how premises support the conclusion.

## Categories

- `Linked`: premises must work together. Removing one breaks the argument.
- `Serial`: premises form a chain where one supports the next.
- `Independent / Convergent`: each reason can support the conclusion separately.
- `Insufficient support`: the premise is relevant but too narrow or weak for the conclusion.
- `Mixed`: the argument uses multiple structures.

## Procedure

1. List the conclusion.
2. List the premises.
3. Ask whether each premise supports the conclusion by itself or only with others.
4. Identify chains where one claim depends on a prior claim.
5. Name the structure and explain briefly.

## Output format

```markdown
## Linkage
Structure: ...

Reason:
...
```

## Example

Input:
1. `Later starts increase teen sleep.`
2. `More sleep improves attention and learning.`
3. `Better learning improves academic performance.`
Conclusion: `School should start later.`

Output:
`Serial: later start -> more sleep -> better attention and learning -> better academic performance -> school should start later.`
