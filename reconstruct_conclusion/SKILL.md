---
name: reconstruct_conclusion
description: Use when the main conclusion of an argument needs to be identified and separated from premises, background, rhetoric, or examples.
---

# Reconstruct Conclusion

Use this skill to identify what the argument is trying to prove.

## Procedure

1. Ask: what claim would count as the argument's success?
2. Ignore background, examples, emotional framing, and side remarks unless they are the target claim.
3. Write the conclusion as one sentence.
4. Begin with: `They are trying to prove that...`

## Output format

```markdown
## Conclusion
They are trying to prove that...

## Not the conclusion
- ...
```

## Quality checks

- The conclusion should be a claim, not a topic.
- The conclusion should be specific enough to evaluate.
- The conclusion should not include reasons; reasons belong in the premise list.

## Example

Input: `Teen sleep biology makes early school start times harmful, so school should begin later.`

Output: `They are trying to prove that the school should start later.`
