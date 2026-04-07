# Plasticity - The Technicality

## Scope

This page gives the mathematical spine of our new work.

## Minimal state-update view

Let $\(\rho_t\)$ denote the system state at step $\(t\)$. Let $\(\theta_t\)$ denote slower plasticity parameters, and let $\(u_t\)$ and $\(h_t\)$ denote current input and history.

A compact open-system update is

$$\rho_{t+1}=\sum_k K_k(\theta_t,u_t,h_t)\,\rho_t\,K_k^\dagger(\theta_t,u_t,h_t),$$

with the usual normalization condition chosen according to the exact modeling setup.

The point is not quantum mystique. The point is that this form makes it natural to encode:

- noisy updates,
- context dependence,
- non-commuting order effects,
- and history-sensitive transition bias.

## Slow plasticity update

The slower rule can be written schematically as

\[
\theta_{t+1}=\theta_t+\eta\,G(\rho_t,\theta_t,u_t,h_t),
\]

where \(G\) is a plasticity rule and \(\eta\) is a slow learning rate.

This separates:

- **fast state evolution**, from
- **slower rewiring / retuning**.

That separation is already aligned with the existing repository note on the two-timescale picture.

## Multilayer interpretation

A useful decomposition is:

- **structural layer**: which edges or channels are available;
- **functional layer**: which flows are active now;
- **modulatory layer**: which contextual variables bias the update.

The layers are not independent. They are coupled, but they play different roles.

## Path dependence

In this framework, plasticity is not just a function of how often an edge was used.

It can depend on the **sequence** of uses. That makes order itself a dynamical object.

Examples:

- A → B → D may strengthen a path that B → A → D would not.
- Repeated immediate revisits can be penalized.
- Previously visited motifs can change the next transition probabilities.

## Non-backtracking and self-avoidance

Two simple trajectory constraints are especially useful as first probes:

### Non-backtracking
The process is discouraged or prevented from immediately returning to the node it just left.

### Self-avoidance
The process is discouraged or prevented from revisiting recently occupied states or motifs.

These are not claims about literal neural trajectories. They are testable computational constraints that can stand in for adaptation, repetition suppression, or exploration pressure.

## What can be measured

Natural outputs include:

- transition asymmetry,
- path dependence scores,
- revisit and backtrack rates,
- spectral summaries,
- hysteresis under repeated cues,
- motif occupancy changes across experience order.


See also:
- [Multilayer graph-state models](multilayer_graph_state_models.md)

