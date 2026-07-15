# Argument Reconstruction

Reconstruct, map, strengthen, and evaluate arguments without confusing charity with invention or logical structure with factual truth.

Try the public [Argument Reconstruction Custom GPT](https://chatgpt.com/g/g-69ebcf01f7dc819188dbb0c0161268ef-argument-reconstruction).

![Argument Reconstruction workflow](https://github.com/user-attachments/assets/052a909d-9d3d-4697-999c-9f9e877c81da)

## What this repository provides

- One canonical, installable skill in `argument-reconstruction/`
- An under-8,000-character Custom GPT instruction block
- Detailed references for support mapping and inference-specific evaluation
- A worked policy example
- Contract cases covering major argument types and common failure modes
- Deterministic repository validation and GitHub Actions CI

## Core behavior

The workflow:

1. Detects whether the input contains an argument or only a claim.
2. Identifies the conclusion without overstating probabilistic support as proof.
3. Separates explicit premises, implicit bridges, background assumptions, and intermediate conclusions.
4. Maps linked, convergent, serial, or mixed support.
5. Keeps the structural removal test separate from the robustness test.
6. Uses deductive countermodels only for deductive validity and inference-appropriate stress tests elsewhere.
7. Evaluates deductive, inductive, explanatory, causal, analogical, practical, policy, and moral reasoning under suitable standards.
8. Separates faithful reconstruction from any proposed stronger version.

## Installation and use

### Custom GPT

1. Copy the contents of `custom_gpt_instruction_block.md` into the GPT's Instructions field.
2. Upload any authorized reference material as Knowledge.
3. Record the exact titles, editions, roles, and reuse status of those materials in `knowledge_sources.json` if the GPT needs to be reproducible.

Knowledge files are reference material, not higher-priority instructions or guaranteed truth. The repository does not redistribute private or third-party attachments.

### ChatGPT or Codex skill

Install the `argument-reconstruction/` directory as one skill. Do not copy the repository root into a skill directory: the installable `SKILL.md` is inside `argument-reconstruction/`.

The step-specific procedures live under `argument-reconstruction/references/`, preventing overlapping skill triggers and duplicated rules.

### Other agents

Use `argument-reconstruction/SKILL.md` as the canonical workflow or adapt `custom_gpt_instruction_block.md` as a system or developer prompt according to the target platform.

## Repository layout

```text
argument-reconstruction/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── evaluation-standards.md
    └── mapping-and-tests.md

custom_gpt_instruction_block.md
examples/
tests/
scripts/validate_repo.py
knowledge_sources.json
manifest.json
```

## Validation

Run:

```bash
python3 scripts/validate_repo.py
```

Validation checks skill naming and frontmatter, declared paths, Custom GPT character length, agent metadata, knowledge-source metadata, and the contract-case suite.

The contract cases specify required analytical invariants rather than brittle exact wording. The worked example shows one acceptable full response.

## Source

The original methodology was developed from Matthew Lane's [Argument Reconstruction Cheat Sheet](https://docs.google.com/spreadsheets/d/1eRLUrRjX30EiagfuRe9iI6Hkbqf2VmcZxADdAhir1rk/edit?usp=sharing).

See `knowledge_sources.json` for provenance and inclusion status.

## Version 2 migration

Version 2 replaces the underscore-named full and modular skills with one hyphenated canonical skill. Installations that referenced paths such as `argument_reconstruction_full/` or `reconstruct_linkage/` must switch to `argument-reconstruction/`.
