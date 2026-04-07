# Multilayer graph-state models of plasticity and adaptation

## Core hypothesis

Plasticity can be represented as an **irreversible, path-dependent update rule on a graph state**.

That means future transitions depend not only on how often a route was used, but also on the order in which prior transitions occurred.

## Three linked layers

### 1. Structural connectivity
The edges that are available in principle.

### 2. Functional coupling
The routes that are currently carrying flow or occupancy.

### 3. Modulatory context
Task, cue, gain, or environmental bias that can reshape transition choice.

## Why

A single graph often mixes together several very different things:

- anatomy,
- momentary activity,
- and context.

A multilayer representation lets those pieces be separated without pretending they are independent.

## Repetition suppression and adaptation

In this picture, adaptation can be implemented as a trajectory constraint.

Two simple examples are:

- **non-backtracking**: reduce immediate reversals;
- **self-avoidance**: reduce rapid revisits and short cycles.

These constraints are computationally attractive because they produce directly measurable changes in trajectory statistics.

## What signatures would support the model

- temporal asymmetry in transition counts;
- hysteresis when the same stimulation is repeated in a different sequence;
- motif-level changes that depend on order of exposure;
- reduction of short loops or immediate revisits after learning.

## Caution

This is not claiming that every biological process is literally quantum.

It is using a quantum-inspired state-update language because it naturally handles:

- context,
- order sensitivity,
- uncertainty,
- and open-system noise.


This page is an extension of:
- [Core question and claims](core_question.md)
- [Two-timescale model note](two_timescale_model.md)
- [Discussion and next steps](discussion_future_work.md)
