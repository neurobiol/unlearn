# Self-avoidance

At this stage, our work is a **toy demonstration**, not a biological claim and not a final result.

Its purpose is to show that simple history constraints already produce measurable differences in trajectory summaries.

## Setup

- Graph: 5×5 toy grid
- Trajectory length: 60 steps
- Runs per condition: 300
- Conditions:
  - unconstrained walk,
  - non-backtracking walk,
  - self-avoiding walk with simple restart logic when stuck

The metric summaries reuse the provided transition-summary logic where appropriate, and add simple revisit / coverage summaries.

## What changes qualitatively

Relative to the unconstrained walk:

- **backtrack rate** drops strongly under non-backtracking and self-avoidance;
- **coverage** increases, meaning more unique nodes are visited;
- **trajectory statistics** shift in a direction consistent with history-sensitive routing.

## Why this matters

Even before fitting real neural data, our toy runs show that path-history rules are not just philosophical decoration. They leave quantitative fingerprints.

That makes them useful as first candidate mechanisms for:

- repetition suppression,
- adaptive exploration,
- anti-cycling behavior,
- and order-sensitive plasticity.

![Self-avoidance smoke test](assets/self_avoidance_smoketest.png)


