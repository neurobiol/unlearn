# Core question and claims

## Core question

If plasticity includes unlearning, and unlearning is rewiring rather than deletion, can we model and test it with formalisms that capture order effects.

## What is meant by unlearning?

Unlearning here means reduced expression of a previously learned mapping, coupled with the emergence of a new mapping.  
It can arise from competition, inhibition, pruning, or context dependent retrieval.

See [glossary](glossary.md).

## What is meant by order effects?

An order effect means outcomes differ for A then C versus C then A even when the set of exposures is the same.

Order effects are experimentally testable and can be used to compare model families.

## Why quantum-like?

Quantum-like models are useful when we want a compact mathematical language for contextual updates and order dependence.

The formal move is to represent state with objects that support non-commutative updates, so the composition of updates depends on order.

This is a modelling choice, not a claim that the substrate is quantum coherent at macroscopic scales.

## What should be compared?

A useful comparison is between

1.  Classical probability vector updates such as Markov style models  
2.  Quantum-like open system updates such as density matrix evolution under completely positive maps  
3.  Hybrid families that interpolate between these regimes

The goal is empirical: predict transitions, stability windows, and measurable behavioural outcomes.

## What counts as success?

A quantum-like model is useful if it improves prediction under controlled stress tests such as

- Perturbation  
- order manipulation  
- noise injection  
- missing data  
- domain shift across devices or cohorts

A model is not useful if it adds parameters without improving robustness or interpretability.
