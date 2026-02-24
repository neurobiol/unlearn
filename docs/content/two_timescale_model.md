# Two-timescale model note

This page is a conceptual companion to the line on the poster

Graph Hamiltonian Model of Plasticity: Two-timescale Quantum-like Unlearning. Manuscript in preparation.

## Why a two-timescale picture is natural

Plasticity has at least two coupled rates.

A fast timescale  
state evolution under a fixed effective network

A slow timescale  
network parameter updates driven by experience, context, and feedback

Treating the network as slowly varying lets us separate dynamics from adaptation.

## What a graph Hamiltonian can mean in this context

A graph Hamiltonian is a structured operator built from a network representation. It encodes how activity or information flows among nodes.

In a quantum-like setting, the Hamiltonian can be paired with an environment term that induces noise and dissipation.

The goal is not physics mimicry for its own sake. The goal is a compact operator language that makes order effects and stability diagnostics easy to compute.

## Where unlearning fits

Unlearning can appear as directed parameter updates that reduce the influence of a previously dominant subspace or pathway.

In spectral language, unlearning can shift eigenvalues, reshape gaps, and change mode occupancy patterns.

## What would make the model compelling

A compelling two-timescale model should

produce falsifiable predictions about when transitions occur  
map parameters to interpretable biological or behavioural knobs  
predict which perturbations increase resilience versus fragility  
generalize across datasets and protocols

If you want, we can add a short equation box that matches your manuscript conventions.
