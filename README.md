# ProteinModelling1

Structural and variant-effect modelling of the JAK family (JAK1, JAK2, JAK3, TYK2).

## Run in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chervov/ProteinModelling1/blob/main/colab/tyk2_ddg_clash_diagnosis.ipynb)
**TYK2 ddG: are the extreme values real?** — installs PyRosetta, downloads the relaxed structure,
and reproduces the clash diagnosis: pipeline protocol vs mobile backbone vs Rosetta's own
`ddg_monomer`. Run all; no configuration. Write-up:
[`conclusions_ddG_difference_feature.md`](conclusions_ddG_difference_feature.md) sections 8-10.

Other notebooks live in [`colab/`](colab/).

## Where things are

| path | contents |
|---|---|
| [`pipeline/ddg/`](pipeline/ddg/) | the dual-state ddG computation, its supervisor, and how to reproduce it |
| [`data/ddg/`](data/ddg/) | merged ddG results, the clash diagnosis, and the relaxed TYK2 pose |
| [`external_data/`](external_data/) | per-protein variant tables assembled from ClinVar, gnomAD, cBioPortal, OncoKB, LOVD, DECIPHER, OMIM and the main predictors |
| [`colab/`](colab/) | notebooks meant to be opened in Google Colab |
| `conclusions_*.md` | dated analysis write-ups |
