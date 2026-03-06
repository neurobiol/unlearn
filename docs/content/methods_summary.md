# Methods summary

This section explains the technical details behind the poster.


## Wearable embedding and clustering

A typical pipeline is

1.  segment raw sensor streams into windows  
2.  extract features per window  
3.  build a representation that supports similarity comparisons  
4.  embed into two dimensions for visual inspection  
5.  quantify separation and clustering with held out evaluation

The embedding axes themselves are not physically meaningful. Neighborhood structure is the point.

See the Parkinson wearables note [here](parkinsons_wearables.md).

## Similarity network panel

The dense network panel acts as a visual reminder that a system can be represented by relationships among states, features, or motifs.

Similarity can be defined by correlation, cosine similarity, mutual information, distance metrics, or graph kernels. Different choices change what structure becomes visible.

## Gap panel and interpretation

The poster states

- gap peaks signal transitions  
- a flat gap signals stability

This is a high level spectral interpretation.

A gap here means a difference between two spectral summary curves, labelled in the original figure as gmax (blue) and gmin (orange).

If gmax rises while gmin stays near baseline, the gap widens and forms a peak. Peaks often align with switches between stages and can indicate a regime shift.

If both curves become approximately stationary, the gap becomes flat and suggests a stable regime.

## The staged protocol

- Past exposure and initial learning  
- Rest and consolidation  
- New learning or unlearning  
- Rest  
- Reactivation of past learning

The key idea is to align spectral changes with stage boundaries, then test whether those alignments replicate across seeds, subjects, or datasets.

## Beyond the poster

To make the gap claim rigorous, a full report would specify

- the operator whose spectrum is used  
- how gmax and gmin are defined  
- how uncertainty is estimated  
- how peaks are detected  
- how stage alignment is quantified

These details will be made available in the methods section of the upcoming manuscript.
