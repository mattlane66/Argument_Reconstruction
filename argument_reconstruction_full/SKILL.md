---
name: argument_reconstruction_full
description: Use when a user provides a belief, position, claim, argument, or debate statement and wants it reconstructed, strengthened, mapped, or evaluated for pragmatic and epistemic quality.
---

# Argument Reconstruction Full Workflow

Use this skill to reconstruct an argument before evaluating it. The goal is to make the reasoning clear enough that the speaker would recognize it, critics can test it fairly, and the user can see where the support is strong, weak, missing, or fact-dependent.


## Core principles

- Be charitable: reconstruct the argument in the strongest reasonable form the speaker could accept.
- Do not add claims the speaker did not make; mark any necessary assumption as a hidden bridge.
- Separate the conclusion from the premises before evaluating truth.
- Distinguish logical structure from factual truth.
- For real-world policy, moral, practical, or causal arguments, usually evaluate cogency: premise truth plus strength of support.
- For deductive arguments, evaluate validity first, then soundness.
- Prefer precise, testable claims over vague summaries.
- State uncertainty and missing evidence instead of pretending the reconstruction is complete.


## Workflow

### 1. Set up charity

Restate the argument in its strongest reasonable form. The speaker should be able to say, "Yes, that is exactly what I mean."

Do:
- Preserve the speaker's central point.
- Define technical or ambiguous terms.
- Make the argument coherent where the intended meaning is clear.

Do not:
- Add evidence or claims the speaker did not provide.
- Make the argument easier to attack.
- Treat a vague slogan as stronger than the speaker could plausibly defend.

Output label: `Charitable reconstruction`

### 2. Blueprint the conclusion

Write one sentence beginning with:

`They are trying to prove that...`

The conclusion should be the claim the argument is meant to establish, not merely a topic.

Output label: `Conclusion`

### 3. List the explicit premises

List only the reasons actually given. Do not add missing logic yet.

Output label: `Explicit premises`

### 4. Identify the hidden bridge

Ask:

`What unstated assumption must be true for these premises to connect to this conclusion?`

Then complete:

`For that to follow, you would also have to assume that...`

If the argument already contains the bridge, say so and identify the real pressure point, such as a false premise, vague term, or weak evidence.

Output label: `Hidden bridge`

### 5. Classify the linkage

Classify the support structure:

- `Linked`: premises must work together; removing one breaks the support.
- `Serial`: one premise supports another in a chain.
- `Independent / Convergent`: separate reasons each support the conclusion on their own.
- `Insufficient support`: the reason is relevant but too narrow or weak for the conclusion.
- `Mixed`: different parts use different structures.

Output label: `Linkage`

### 6. Apply the removal test

Ask:

`If I take this reason away, does the conclusion still have enough support?`

Use the answer to test whether a premise is necessary, independently supportive, redundant, or part of a linked chain.

Output label: `Removal test`

### 7. Generate a counterexample

Ask:

`Can I imagine a world where these reasons are true, but the conclusion is still false?`

If yes, explain the leak in the logic. If no, say whether the structure appears valid and shift attention to premise truth.

Output label: `Counterexample`

### 8. Check for shortcuts, equivocation, or fallacies

Look for:
- Term shifts
- Circular reasoning
- False dichotomies
- Hasty generalizations
- Overbroad policy jumps
- Confusing correlation with causation
- Treating a narrow case as a universal rule
- Sliding between similar but non-identical terms

Output label: `Shortcut / fallacy check`

### 9. Evaluate validity, strength, cogency, or soundness

Choose the right standard:

- Deductive argument: valid or invalid; if valid and premises true, sound.
- Inductive, abductive, causal, policy, moral, or practical argument: strong or weak; if strong and premises true, cogent.
- Explanation: ask whether it is hard-to-vary or whether small edits could make it support many incompatible conclusions.

Ask:
- What evidence, if true, would weaken or override the argument?
- Is the support hard-to-vary?
- Are key terms measurable?
- Could the same evidence easily support a different conclusion?

Output label: `Reality check`

## Default response format

Use this structure unless the user requests something else:

```markdown
## Charitable reconstruction
...

## Conclusion
They are trying to prove that...

## Explicit premises
1. ...
2. ...

## Hidden bridge
For that to follow, you would also have to assume that...

## Linkage
...

## Removal test
...

## Counterexample
...

## Shortcut / fallacy check
...

## Reality check
...

## Better version of the argument
...

## What would change my mind
...
```

## Example

Input:

`School should start later because students are tired in first period.`

Output:

```markdown
## Charitable reconstruction
They are arguing that the school should start later because some students are tired in first period.

## Conclusion
They are trying to prove that the school should start later.

## Explicit premises
1. Some students are tired in first period.

## Hidden bridge
For that to follow, you would also have to assume that first-period tiredness is caused mainly by the school start time, that it is a significant school-wide problem, that a later start would meaningfully solve it, and that the benefits outweigh the tradeoffs.

## Linkage
Insufficient support. The premise is relevant, but too narrow on its own to justify a broad policy conclusion.

## Removal test
If we remove the only premise, nothing is left. Even with it, the argument remains too weak unless supported by broader evidence.

## Counterexample
Some students might be tired for reasons unrelated to school start time, such as work schedules, sleep habits, health issues, or extracurricular demands.

## Shortcut / fallacy check
The argument may slide from "some students are tired" to "the whole school schedule is harmful."

## Reality check
This is a real-world policy argument, so the main standard is cogency. Evidence about sleep duration, academic outcomes, transportation, family schedules, and offsetting harms would determine whether the argument is strong.
```
