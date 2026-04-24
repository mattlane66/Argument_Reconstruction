---
name: reconstruct_counterexample
description: Use when testing whether premises can be true while the conclusion is false.
---

# Reconstruct Counterexample

Use this skill to find leaks in an argument's logic.

## Procedure

Ask:

`Can I imagine a world where these reasons are true, but the conclusion is still false?`

If yes:
1. Describe that world.
2. Explain what it reveals about the missing assumption or weak support.
3. Suggest how the argument would need to be strengthened.

If no:
1. Say the structure may be valid or strongly connected.
2. Shift attention to whether the premises are true.

## Output format

```markdown
## Counterexample
...

## What this shows
...

## Strengthening move
...
```

## Example

Input:
`Later start times increase sleep and improve learning, so school should start later.`

Output:
`A possible counterexample is a district where later starts increase sleep and learning somewhat, but also create larger transportation, childcare, work, or extracurricular harms. This shows the argument needs a bridge saying the benefits outweigh the offsetting costs.`
