# finalPoster

This file explains what is inside the plasticity zip and how it maps to the poster.

## What you get in the zip

One folder named plasticity that you can upload as a GitHub repository.

Inside it there are three layers.

Layer 1 is a minimal README at the repo root  
It is designed to be the first page people see after they click from your welcome repository.

Layer 2 is a set of linked markdown pages in docs/content  
These pages start light and become more detailed as readers click deeper.

Layer 3 is an optional GitHub Pages and PWA style site in docs  
It is built from the same text and contains an offline cache via a service worker.

No poster figures are included.

## Mapping to the poster

The poster text contains three visible questions and one forward looking line.

Do wearables distinguish Parkinson’s  
This is explained in docs/content/parkinsons_wearables.md

Quantum-like models test order effects in neuroplasticity  
This is explained in docs/content/core_question.md and docs/content/two_timescale_model.md

A flat gap signals stability and gap peaks signal transitions  
This is explained in docs/content/methods_summary.md with the spectral gap interpretation

If unlearning is rewiring not deletion can we steer neuroplasticity to resist pathological drift  
This is the focus of docs/content/discussion_future_work.md

The thesis quote on the poster appears once in docs/content/poster_guide.md and is not repeated elsewhere.

## How to use this with two repositories

You said you will have a separate repository called welcome that holds the QR landing page.

Put this link in welcome so visitors reach this repository  
https://github.com/YOUR_GITHUB_USERNAME/plasticity

If you publish the optional site, you can instead link to the Pages address  
https://YOUR_GITHUB_USERNAME.github.io/plasticity

## How to publish the optional site

1  Create the GitHub repository named plasticity  
2  Upload the contents of the plasticity folder  
3  In GitHub repository settings, enable Pages and set source to the docs folder  
4  After deployment, open the Pages URL and optionally add it to the welcome repository

## What to edit

Update the author line and affiliations if needed in docs/content/poster_overview.md  
Replace YOUR_GITHUB_USERNAME in links once you know the account name  
If you have a DOI, preprint, or OSF record later, add it to docs/content/references.md

## If you want me to refine the references

Tell me any specific papers or datasets you want featured, and whether you want more emphasis on neuroplasticity, graph spectral methods, quantum-like cognition, or Parkinson wearables.
