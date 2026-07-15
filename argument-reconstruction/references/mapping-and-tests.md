# Mapping and inference tests

Use this reference when the argument's bridges, topology, or stress tests require more precision.

## Faithful reconstruction versus strengthening

A faithful reconstruction makes the supplied reasoning explicit. It may clarify wording and identify implicit commitments, but it must not silently add evidence or a more defensible conclusion.

A strengthened reconstruction is an editorial proposal. Label every new premise, qualification, or evidential requirement so it is not attributed to the original speaker.

## Explicit and implicit material

- `Explicit premise`: a reason the speaker actually states.
- `Implicit premise or warrant`: an unstated claim required for the intended inference.
- `Background assumption`: a presupposition that frames the discussion but may not perform direct inferential work.
- `Intermediate conclusion`: a claim supported by earlier premises and then used to support another conclusion.

Prefer several precise implicit premises over one vague bridge when the inference contains distinct causal, normative, or feasibility steps. Add only what the intended inference actually needs.

Reject a bridge that merely says, `If P, then C`, when it has no substantive content beyond encoding the desired conclusion. State the general causal, classificatory, evidential, or normative rule and evaluate it independently.

## Support topology

### Linked

Treat premises as linked when they function as co-premises and neither supplies the intended support without the other.

```text
P1 + P2 -> C
```

### Convergent

Treat premises as convergent when each supplies its own line of support for the same conclusion, even if neither is decisive by itself.

```text
P1 -> C
P2 -> C
```

### Serial

Treat support as serial when a premise supports an intermediate conclusion that becomes a premise in a later inference.

```text
P1 -> IC1
IC1 + P2 -> C
```

### Mixed

Map each local relationship rather than assigning one vague label to a complex argument.

## Two removal tests

Do not conflate topology with strength.

1. `Structural removal test`: Remove one premise and ask whether the remaining premise still offers its own intended direct support. Use this to distinguish linked from convergent support.
2. `Robustness removal test`: Remove one premise and ask whether the remaining case still crosses the relevant justificatory threshold. Use this to assess dependence and resilience, not topology.

A convergent premise may independently support a conclusion without being sufficient to justify it. A linked premise may be essential to one inference while the conclusion still has another independent line of support elsewhere in the map.

## Countermodels and stress tests

### Deductive countermodel

To show invalidity, describe a possible interpretation or situation in which every premise is true and the conclusion is false. Verify that the countermodel preserves the original meanings of the terms.

Do not infer validity merely from an unsuccessful search for a countermodel.

### Non-deductive stress tests

Choose the test that matches the inference:

- Induction: atypical cases, base rates, selection effects, or sensitivity to sample assumptions.
- Causation: confounding, reverse causation, measurement artifacts, or a missing counterfactual.
- Explanation: a rival explanation that fits the same evidence with fewer unsupported commitments.
- Policy: a case in which stated benefits occur but are outweighed by costs, risks, rights, or better alternatives.
- Analogy: a material disanalogy that breaks the transfer of support.

Treat these as defeaters or strength tests. A single possible exception does not automatically refute a probabilistic inference.
