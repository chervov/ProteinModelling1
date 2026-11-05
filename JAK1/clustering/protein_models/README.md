# JAK1 structural models

The open and closed JAK1 models behind the dual-state ΔΔG features, with geometry, PAE and an
interactive viewer. Added 5 November 2026 to bring JAK1 in line with
[`../../../JAK2/clustering/protein_models/`](../../../JAK2/clustering/protein_models/),
TYK2 and JAK3.

**[`jak1_models_3d.html`](jak1_models_3d.html)** — one self-contained file, 3.2 MB.

| directory | contents |
|---|---|
| `jeanpierre/` | the paper's own closed and open WT models |
| `shan/` | Shan 2014's JH2–JH1 closed reference |
| `AFmodel/` | AlphaFold DB `AF-P23458-F1` v6, with its PAE matrix |

## JAK1 has the cleanest pair in the project

It is the **only** protein here with a *published* open/closed pair — the two models
Jeanpierre/Debeaupuis built and used for the ΔΔG features in their own clustering. Everywhere
else the pair had to be assembled from our own runs, and every one of those carries a confound:

| protein | pair | confound |
|---|---|---|
| **JAK1** | Jeanpierre closed + open | **none** — same authors, same purpose |
| JAK2 | pair 1, one untemplated run | none (pair 2 is the templated control) |
| TYK2 | AF3 closed + AF3 open | different jobs, seeds **and** template settings |
| JAK3 | AF3 closed + OpenFold open | different predictors |

Per-domain RMSD between the JAK1 states is **0.25–1.39 Å**, so the two structures differ in where
JH1 sits and little else.

## Geometry

Cα centroid distances, Å. Domains: FERM 34–420, SH2 439–544, JH2 583–855, JH1 875–1153.

| model | FERM–SH2 | FERM–JH2 | **FERM–JH1** | SH2–JH2 | SH2–JH1 | JH2–JH1 |
|---|--:|--:|--:|--:|--:|--:|
| Jeanpierre closed | 40.4 | 47.4 | **40.1** | 40.3 | 55.3 | 39.5 |
| Jeanpierre open | 40.4 | 46.6 | **92.5** | 40.2 | 77.7 | 46.0 |
| AlphaFold DB v6 | 40.1 | 46.2 | **92.2** | 40.2 | 78.9 | 46.3 |

As everywhere in this family, **only the three JH1 columns move**: FERM–SH2 is 40.1–40.4 in all
three, SH2–JH2 is 40.2–40.3.

**The AlphaFold DB model is open for JAK1** — 3.44 Å from the Jeanpierre open model after a JH2
fit. It is also open for JAK2, and **closed** for TYK2 and JAK3. The default AlphaFold state
splits two-and-two across this family, so no AFDB model should be reused as a reference for a
particular state without measuring it first.

## Superposition

| A | B | global RMSD | JH1 after JH2 fit | FERM | SH2 | JH2 | JH1 |
|---|---|--:|--:|--:|--:|--:|--:|
| Jeanpierre closed | Jeanpierre open | 31.16 | **81.68** | 1.07 | 0.25 | 1.39 | 0.76 |
| Jeanpierre closed | AFDB | 30.77 | 80.96 | 1.58 | 0.32 | 1.35 | 0.52 |
| Jeanpierre open | AFDB | 4.17 | **3.44** | 1.66 | 0.25 | 0.72 | 0.49 |

Against **Shan 2014**'s independent closed JH2–JH1 model: the Jeanpierre closed model is
**11.70 Å** at JH1 after a JH2 fit, the open model 82.92 Å. So the two closed models agree on the
arrangement but not on the details — looser than TYK2's AF3 model against the 4OLI crystal
(2.02 Å), which is expected, since Shan's is itself a model rather than a structure.

## PAE — the worst in the family

AlphaFold DB inter-domain PAE, Å (ceiling 31.75 for this model):

| block | mean PAE |
|---|--:|
| SH2–SH2 | 4.0 |
| JH1–JH1 | 5.3 |
| JH2–JH2 | 5.7 |
| FERM–FERM | 8.9 |
| FERM–SH2 | 10.6 |
| JH2–JH1 | 19.9 |
| SH2–JH2 | 19.9 |
| FERM–JH2 | 21.3 |
| SH2–JH1 | 26.5 |
| **FERM–JH1** | **25.8** |

Across the family, FERM–JH1 runs JAK3 18.5 → JAK2 21.0 → TYK2 23.1 → **JAK1 25.8**. JAK1 is the
protein where AlphaFold is *least* confident about where JH1 sits — and it is also the protein
with the published pair and the paper's own clustering.

## The point this closes

`ddg_delta` has now scored chance on all four: **JAK1 0.4966**, JAK2 0.499, TYK2 0.502,
JAK3 0.527. JAK1 matters most of the four, because its pair is the clean one — the feature fails
even when the two structures are exactly what the method intends, from the authors who defined
it. On JAK2 the second model pair showed why: `delta` is a difference of two large, strongly
correlated numbers, so it is numerical noise, and noise does not reproduce (r = 0.074).

## Reproduce

```bash
python3 analyse_models.py     # -> model_analysis.json
python3 plot_models.py        # -> figs/*.png
python3 build_3d.py           # -> jak1_models_3d.html
```
