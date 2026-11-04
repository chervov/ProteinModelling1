# JAK3 clustering

Variant clustering for JAK3 (UniProt P52333, 1,124 aa), by the same pipeline as
[`../../JAK2/clustering/`](../../JAK2/clustering/) and
[`../../TYK2/clustering/`](../../TYK2/clustering/). 4 November 2026.

**Start here:** [`jak3_clustering_report.md`](jak3_clustering_report.md) ·
[`jak3_clustering_report.html`](jak3_clustering_report.html) ·
[`protein_models/jak3_models_3d.html`](protein_models/jak3_models_3d.html)

## What is different about JAK3

**The pathogenic variants are loss of function, not gain.** JAK3 Pathogenic/Likely-pathogenic
alleles cause SCID. For JAK2 they cause myeloproliferative neoplasms and are *activating*. So
"damaging" means the opposite thing here, and the clustering is not being asked to find
activating variants — which is the task every predictor in the set is worst at.

**ClinVar is the best of the three proteins.** 23 Pathogenic/Likely-pathogenic missense records,
most 3-star ("reviewed by expert panel"), against TYK2's two 0-star ones. The seeds are therefore
the full 5 + 5, as the JAK2 rule specifies.

**No deep mutational scan**, unlike TYK2. Validation rests on gnomAD and ClinVar.

**No experimental closed structure.** The reference arrangement is the AlphaFold DB model, which
is itself closed — weaker than TYK2's 4OLI crystal. (The AFDB model being *closed* is itself
notable: it is open for JAK2. Two of three in this family.)

**ΔΔG computed fresh**, locally with PyRosetta, on a closed/open pair that is confounded across
predictors (AF3 closed, OpenFold open) but only mildly: every per-domain RMSD between the two
states is 0.31–0.93 Å, against 5.47 Å for TYK2's FERM domain.

## Structure selection — the part that needed care

**14 of JAK3's 30 `selected_*.pdb` files are mislabelled**, and three OpenFold runs produced
*compact* models that sit **15–16 Å from the autoinhibited arrangement** — collapsed into some
other state rather than closed. FERM–JH1 distance alone would have accepted all of them; it took
a JH1 RMSD after superposing JH2 to separate them. Full measurements in `protein_models/`.

## Features

| feature | source |
|---|---|
| ESM-1b, AlphaMissense, PolyPhen-2, BLOSUM62 | 100% coverage |
| ΔΔG closed / open / delta | fresh PyRosetta run, see `build_ddg.py` |
| FoldX | ProtVar committed extract |
| CADD / SIFT / ClinPred | dbNSFP via myvariant.info (~31%, its structural ceiling) |

## Reproduce

```bash
python3 build_universe.py
for f in esm1b alphamissense blosum62 dbnsfp polyphen foldx gnomad clinvar; do python3 build_$f.py; done
python3 collect_jak3.py && python3 build_ddg.py
python3 cluster_jak3.py && python3 analyse_jak3.py && python3 plots_jak3.py && python3 build_html_jak3.py
cd protein_models && python3 analyse_models.py && python3 plot_models.py && python3 build_3d.py
```
