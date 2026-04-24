---
name: reconstruct_premises
description: Use when the explicit reasons in an argument need to be extracted without adding missing assumptions or new support.
---

# Reconstruct Premises

Use this skill to list the stated reasons for the conclusion.

## Procedure

1. Find claims offered as support.
2. Separate each reason into its own numbered premise.
3. Do not add hidden assumptions yet.
4. Preserve the user's level of certainty.
5. Mark vague or ambiguous premises for later clarification.

## Output format

```markdown
## Explicit premises
1. ...
2. ...

## Ambiguous premises
- ...
```

## Quality checks

- Premises should be statements that can be true or false.
- Avoid smuggling in bridges such as "therefore we should..." unless the user stated them.
- Separate evidence claims from value claims.

## Example

Input: `Later start times increase teen sleep, more sleep improves attention, and better attention improves learning.`

Output:
```markdown
## Explicit premises
1. Later start times increase teen sleep.
2. More sleep improves attention.
3. Better attention improves learning.
```
