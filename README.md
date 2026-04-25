# Argument Reconstruction Skill Pack

Evaluate a belief, position, argument, or construct one with Argument Reconstruction to improve pragmatic and epistemic reasoning. Use cases: Evaluate a news article, a point someone made that you disagree with, or a point you made that you agree with but want to improve, and so on. You can quickly get a sense of the Argument Reconstruction Skill [here](https://chatgpt.com/g/g-69ebcf01f7dc819188dbb0c0161268ef-argument-reconstruction).

Pragmatics and epistemic reasoning are key critical thinking skills we should all leverage.

This repo contains one full workflow skill plus modular skills for each phase of argument reconstruction.

<img width="552" height="556" alt="images" src="https://github.com/user-attachments/assets/052a909d-9d3d-4697-999c-9f9e877c81da" />

## Source

These skills were produced from my Argument Reconstruction Cheat Sheet Google Sheet:
https://docs.google.com/spreadsheets/d/1eRLUrRjX30EiagfuRe9iI6Hkbqf2VmcZxADdAhir1rk/edit?usp=sharing

## Recommended use

Use `argument_reconstruction_full/SKILL.md` when you want one comprehensive skill. Use the modular skills when you want a GPT or agent to call a narrower procedure for a specific step.

## Skills included

1. `argument_reconstruction_full`
2. `reconstruct_charity`
3. `reconstruct_conclusion`
4. `reconstruct_premises`
5. `reconstruct_hidden_bridge`
6. `reconstruct_linkage`
7. `reconstruct_removal_test`
8. `reconstruct_counterexample`
9. `reconstruct_fallacy_check`
10. `reconstruct_reality_check`

## Supporting files

- `custom_gpt_instruction_block.md` — reusable instruction block for Custom GPTs or agent prompts.
- `manifest.json` — relative file manifest for developers and tool routing.
- `examples/` — example input and expected output for regression-style testing.

## Default input

A user may provide a belief, claim, position, policy proposal, paragraph, debate statement, comment, or rough argument.

## Default output

The full skill returns:

- Charitable restatement
- Conclusion
- Explicit premises
- Hidden bridge
- Argument linkage
- Removal test
- Counterexample
- Shortcut or fallacy check
- Validity, strength, cogency, or soundness assessment
- Best next questions or evidence needed

## Example theme used in the source sheet

School should start later because students are tired, later start times may increase teen sleep, and improved sleep may improve attention, learning, mental health, or driving safety.
