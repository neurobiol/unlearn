# Parkinson wearables note

## Poster question

Do wearables distinguish Parkinson’s?
Do people with similar movement patterns cluster together?

## What the poster plot supports

A two-dimensional embedding of wearable features can reveal clusters, overlap, and outliers.

If Parkinson’s and control points show separation in some regions, those regions can be traced back to specific movement contexts or sensor channels.

## Avoid over-interpretation

Embedding axes have no direct physical meaning.  
Separation in an embedding is not the same as clinically useful prediction.

That is why downstream evaluation is needed.

## Minimal evaluation checklist

1.  Define the task clearly, for example classification or progression scoring.  
2.  Avoid leakage between train and test splits.  
3.  Report calibration and uncertainty if probabilities are used.  
4.  Run ablations over feature sets and windowing choices.  
5.  Replicate across cohorts when possible.

## How this connects back to unlearning

If neuroplasticity supports compensation early in disease, then drift in wearable signatures might reflect a failure of compensatory rewiring.

The broader question is whether a single modeling language can connect

- plasticity stage transitions  
- network diagnostics  
- wearable derived disease signatures

## Key references

See [References](docs/content/references.md) for primary sources on mPower and smartphone-based Parkinson’s disease testing.


