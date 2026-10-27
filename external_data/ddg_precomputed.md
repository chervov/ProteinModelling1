# Precomputed ΔΔG data — where to get it

*Compiled 27 October 2026. Row counts and columns verified by direct download, not quoted from papers.*

## Short answer

Everything needed for training and benchmarking is in **one already-public GitHub repository**,
pre-split, no registration and no bulk-download forms:

```
github.com/Kuhlman-Lab/ThermoMPNN  →  data_all/
```

94.6 MB total. The original databases are only needed for metadata those splits drop.

## What is in `data_all/`

| file | rows | size | source dataset |
|---|--:|--:|---|
| `training/mega_train.csv` | 216,919 | 36.4 MB | Tsuboyama mega-scale, train |
| `training/mega_val.csv` | 27,481 | 26.1 MB | mega-scale, validation |
| `testing/mega_test.csv` | 28,312 | 27.4 MB | mega-scale, test |
| `training/fireprot_train.csv` | 2,669 | 2.07 MB | FireProtDB, train |
| `training/fireprot_val.csv` | 387 | 0.28 MB | FireProtDB, validation |
| `testing/fireprot_HF.csv` | 2,578 | 1.87 MB | FireProtDB, homology-filtered |
| `testing/fireprot_test.csv` | 348 | 0.26 MB | FireProtDB, test |
| `testing/s669_clean_dir.csv` | 669 | 14 kB | S669 benchmark |
| `testing/ssym-5fold_clean_dir.csv` | 342 | 67 kB | Ssym, forward |
| `testing/ssym-5fold_clean_inv.csv` | 342 | 67 kB | Ssym, inverse mutations |
| `testing/myoglobin_clean.csv` | 42 | 10 kB | small held-out set — see note |

**Total ≈ 280,000 ΔΔG values**, dominated by the mega-scale set.

### Columns

Mega-scale files are minimal — `name, ddG_ML, mut_type, WT_name, aa_seq, wt_seq`, where `name` is a
PDB-style domain identifier and `mut_type` is `wt` for the reference rows (1,188 in train, 153 in
val, 140 in test). There is no UniProt accession.

FireProtDB files are rich and **joinable to our work**: `experiment_id, protein_name, uniprot_id,
pdb_id, chain, position, wild_type, mutation, ddG, dTm, is_curated, type, derived_type,
interpro_families, cons`. The `uniprot_id` and `interpro_families` columns mean these rows can be
matched directly against the kinase and non-kinase sets in `more_proteins/`.

S669 / Ssym / myoglobin are compact benchmark tables: `PDB, MUT, DDG` plus pH, temperature and
sequence for Ssym.

## Notes and gotchas

**Scope limit on the mega-scale data.** Tsuboyama et al. measured domains of **40–72 residues**
([10.1038/s41586-023-06328-6](https://doi.org/10.1038/s41586-023-06328-6)) — around 776,000 curated
stabilities over 331 natural and 148 de novo domains. Excellent for training; **not** directly
comparable to ΔΔG in the large multi-domain proteins analysed in `more_proteins/`, where the mutated
site may sit in an inter-domain interface that no 40–72 aa domain can represent.

**`myoglobin_clean.csv` is misnamed.** All 42 rows carry `#SET = TEST_P53`, `CLUID = 2AC0A` and
`PDB = 2OCJA`, with a p53 sequence — not myoglobin. (Both 2AC0A and 2OCJA are p53 structures; the
file's columns are `#SET, CLUID, PDB, MUT, DDG, SEQ`, so the PDB identifier is 2OCJA and 2AC0A is
the cluster id.) Check its provenance before using it as a held-out set.

**Ssym comes in forward and inverse pairs** (342 rows each). The inverse set exists to expose
antisymmetry bias — a predictor should give ΔΔG(A→B) = −ΔΔG(B→A). Report both or the evaluation is
incomplete.

**The splits are not ours to re-draw.** These files carry the published partitions from
[Dieckhaus et al. 2024 PNAS](https://doi.org/10.1073/pnas.2314853121); `dataset_splits/` in the same
repo holds the cluster assignments (`megascale_clusters.tsv`, `mega_splits.pkl`) and the homology
cross-checks (`s669_vs_megascale_homologues.m8`). Reuse them if comparing against published numbers.

## Original sources — only if the extra metadata is needed

| resource | reference | why you would go there |
|---|---|---|
| Zenodo `10.5281/zenodo.7992926` | Tsuboyama 2023 | mega-scale data unsplit, with full experimental metadata and both ΔG and ΔΔG |
| FireProtDB | [10.1093/nar/gkaa981](https://doi.org/10.1093/nar/gkaa981), [2.0](https://doi.org/10.1093/nar/gkaf1211) | literature provenance per measurement, buffer/pH conditions |
| ThermoMutDB | [10.1093/nar/gkaa925](https://doi.org/10.1093/nar/gkaa925) | additional curated missense thermodynamics |
| ProThermDB | [10.1093/nar/gkaa1035](https://doi.org/10.1093/nar/gkaa1035) | the long-standing ProTherm lineage |

Analysis code for the mega-scale paper: `github.com/Rocklin-Lab/cdna-display-proteolysis-pipeline`.

## Method papers worth reading alongside

- [Dieckhaus et al. 2024, PNAS](https://doi.org/10.1073/pnas.2314853121) — transfer learning from
  mega-scale to the small curated sets; the source of these splits.
- [Blaabjerg et al. 2023, eLife](https://doi.org/10.7554/elife.82593) — RaSP, rapid prediction from
  deep learning representations.
- [Pak et al. 2023, PLoS ONE](https://doi.org/10.1371/journal.pone.0282689) — whether AlphaFold
  models are adequate inputs for ΔΔG prediction, which bears directly on using modelled structures.
