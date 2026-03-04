# Two-timescale model

We are developing a model that treats brain-like adaptation as network change happening more slowly than moment-to-moment activity.

## Why a two-timescale picture is natural

Plasticity has at least two coupled rates. Some changes happen quickly (seconds–minutes), while learning-related rewiring tends to happen more slowly (minutes–days).

### A fast timescale: state evolution under a fixed effective network.

Short-term activity evolves on a network that is “almost the same” during a brief window.

### A slow timescale: network parameter updates driven by experience, context, and feedback.

Over longer periods, experiences gradually change the network itself.

Treating the network as slowly varying lets us separate dynamics from adaptation. This separation makes it easier to tell “what the system is doing now” from “how the system is being changed by what happened.”

## A minimal two-timescale equation (fast + slow)

### Fast dynamics (state update):

$$\frac{d\rho}{dt} = -i[H(\theta(t)),\rho] + \sum_k \gamma_k \left(L_k \rho L_k^\dagger-\frac{1}{2}\{L_k^\dagger L_k,\rho\}\right).$$

### Slow dynamics (plasticity update):
$$
\frac{d\theta}{dt}
=
\varepsilon\, G(\rho,\theta,u(t)),
\qquad
0<\varepsilon\ll 1.
$$

### Meaning

* $\rho$: the system state (a density matrix) over network modes.

This means a compact “state-of-the-system” object that can represent uncertainty and mixed patterns, not just one activity pattern.

* $t$: time.
  
* $H(\theta(t))$: a graph Hamiltonian parameterized by $\theta$, built from the network (e.g., adjacency, $A$, Laplacian, $L$, or weighted couplings).
  
  This is a matrix that encodes how activity can spread through the network, with knobs, $\theta$, that can slowly change as learning happens.

* $[H,\rho]=H\rho-\rho H$: the commutator generating reversible, order-sensitive evolution.

  This is the part that makes “sequence matters” possible in the model.

* $L_k$: Lindblad (noise/dissipation) operators;

* $L_k^\dagger$ is the conjugate transpose.
  
  These are mathematical tools that represent randomness, leakage, and imperfect memory.

* $\gamma_k\ge 0$: rates (strengths) of each noise/dissipation channel.

  This determines how strong each kind of noise is.

* ${X,Y}=XY+YX$: the anti-commutator.

  This is a symmetrized product used to keep the update mathematically well-behaved. It means we combine $𝑋$ and $𝑌$ in a balanced way that does not depend on their order, which helps the equations stay stable and physically consistent.

* $\theta$: slow parameters controlling network structure or effective couplings (weights, gains, contextual biases, etc.).

  These are the “learning knobs” that change the network over time.

* $u(t)$: external inputs, tasks, cues, or interventions.
  
  This is what we show to the system and when (training, prompts, stimulation, context).

* $G(\rho,\theta,u(t))$: a plasticity rule that updates $\theta$ based on current state, context, and feedback (could be Hebbian-like, error-driven, regularized, etc.).
  
  This is the learning rule that says “given what just happened, how should the network change?”

* $\varepsilon\ll 1$: a small parameter enforcing timescale separation (slow learning vs fast state evolution).

  This is a dial that makes learning much slower than moment-to-moment activity.

## Graph Hamiltonian

A graph Hamiltonian is a structured operator built from a network representation. It encodes how activity or information flows among nodes. It is a network-based matrix that tells us which parts influence which other parts.

In a quantum-like setting, the Hamiltonian can be paired with an environment term that induces noise and dissipation. We explicitly include randomness and loss, because real biological signals are noisy.

This is a modeling choice: we use an operator-based formalism because it provides a compact, principled way to express order-dependent updates and to compute stability diagnostics. It lets us ask clean, testable questions such as whether sequence matters and when the system transitions between regimes, without implying that the brain is a literal quantum computer.

## Unlearning

Unlearning can appear as directed parameter updates that reduce the influence of a previously dominant subspace or pathway. Unlearning is modeled as gradually weakening a once-strong route or pattern.

In spectral language, unlearning can shift eigenvalues, reshape gaps, and change mode occupancy patterns.
Basically, in the model’s “vibration modes,” unlearning changes which modes dominate and how separated they are, which can signal stability vs transition.

## What would make the model compelling

A compelling two-timescale model should

* produce falsifiable predictions about when transitions occur.
  It should predict when changes happen, and be able to be wrong.

* map parameters to interpretable biological or behavioural knobs.
  Each knob should correspond to something we can measure or manipulate.

* predict which perturbations increase resilience versus fragility.
  It should say what makes the system more stable or more likely to tip.

* generalize across datasets and protocols.
  It should not be tuned to only one dataset or one experimental design.

### A minimal spectral unlearning term

Let $W(t)\in\mathbb{R}^{n\times n}$ be symmetric with eigendecomposition $W=V\Lambda V^\top$ where $\Lambda=\mathrm{diag}(\lambda_1\ \lambda_2\ \dots\ \lambda_n)$ and $v_1$ is the dominant mode. A simple unlearning update that weakens that mode is

$$
\frac{dW}{dt}=-\eta v_1 v_1^\top
\qquad \eta>0
$$

Using a first order Rayleigh quotient approximation

$$
\frac{d\lambda_1}{dt}=v_1^\top\frac{dW}{dt}v_1=-\eta
$$

and for other modes

$$
\frac{d\lambda_k}{dt}\approx 0
\qquad k\ne 1
$$

So the spectral gap $\Delta=\lambda_1-\lambda_2$ decreases during unlearning.

Citation:
Goolam Hossen Y H, Gassab L, Craddock T J A. Graph Hamiltonian Model of Plasticity: Two-timescale Quantum-like Unlearning. Manuscript in preparation, 2026.

