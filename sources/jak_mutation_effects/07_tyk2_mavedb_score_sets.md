# Howard et al. TYK2 DMS: MaveDB score-set inventory

## Provenance correction

The primary study is **Howard et al., 2025, bioRxiv preprint**: *Deep mutational scanning reveals pharmacologically relevant insights into TYK2 signaling and disease*, DOI [10.1101/2025.10.11.681520](https://doi.org/10.1101/2025.10.11.681520). It is **not peer-reviewed**. Do not cite the later 2026 database deposit as if it were an independent peer-reviewed article.

- Raw sequencing accession: `PRJNA1291213`.
- Analysis/data archive: [Zenodo 10.5281/zenodo.15347448](https://doi.org/10.5281/zenodo.15347448).
- Analysis code: [octantbio/bms-dms](https://github.com/octantbio/bms-dms).
- Target: human TYK2 / UniProt `P29597`; all score-set records use the preprint DOI as their primary publication.
- MaveDB publication date: 2026-03-03; this is a database-record date, not the preprint publication date.

## Experiment `urn:mavedb:00001270-a`: IFN-alpha signalling (10 score sets)

Each score set measures nearly all 23,740 possible single amino-acid substitutions (23,719–23,723 variants per set) in TYK2-knockout, STAT2/IRF9-reconstituted HEK293T cells with an ISRE barcoded-luciferase reporter. Scores are condition contrasts from a negative-binomial GLMM; they must not be pooled without a stated analysis plan.

| Score set | Variants | Condition |
|---|---:|---|
| `urn:mavedb:00001270-a-1` | 23,723 | IFN-alpha, 1 U/mL |
| `urn:mavedb:00001270-a-4` | 23,723 | IFN-alpha, 10 U/mL |
| `urn:mavedb:00001270-a-6` | 23,723 | IFN-alpha, 100 U/mL |
| `urn:mavedb:00001270-a-9` | 23,719 | IFN-alpha, 100 U/mL, duplicate assay |
| `urn:mavedb:00001270-a-5` | 23,720 | IFN-alpha, 100 U/mL + BMS-986202, 20 nM |
| `urn:mavedb:00001270-a-7` | 23,719 | IFN-alpha, 100 U/mL + BMS-986202, 20 nM, duplicate assay |
| `urn:mavedb:00001270-a-8` | 23,720 | IFN-alpha, 100 U/mL + BMS-986202, 1 uM |
| `urn:mavedb:00001270-a-2` | 23,723 | IFN-alpha, 100 U/mL + BMS-986202, 10 uM |
| `urn:mavedb:00001270-a-3` | 23,719 | IFN-alpha, 100 U/mL + NDI-034858, 7 nM |
| `urn:mavedb:00001270-a-10` | 23,720 | IFN-alpha, 100 U/mL + NDI-034858, 1 uM |

## Experiment `urn:mavedb:00001271-a`: protein abundance (one score set)

| Score set | Variants | Assay |
|---|---:|---|
| `urn:mavedb:00001271-a-1` | 23,698 | TYK2-VampDMS: VAMP-seq-adapted N-terminal GFP-TYK2 abundance, normalized with BFP, four FACS bins |

## Correct analytical use

1. Match the question to the score set: basal cytokine response, dose dependence, BMS-986202 response, NDI-034858 response, or abundance.
2. Keep the duplicate 100 U/mL and BMS 20 nM score sets for reproducibility/variance checks; do not silently average them.
3. Use `score` and `se` together; a point score without its uncertainty is incomplete.
4. Do not convert a condition-specific DMS score directly into a clinical pathogenicity, GOF, or LOF label.
5. For the preprint citation, explicitly state that it is not peer-reviewed; separately cite the exact MaveDB score-set URN used.

## API retrieval

MaveDB’s public API requires no credentials for published records:

```text
https://api.mavedb.org/api/v1/experiments/urn:mavedb:00001270-a/score-sets
https://api.mavedb.org/api/v1/experiments/urn:mavedb:00001271-a/score-sets
https://api.mavedb.org/api/v1/score-sets/urn:mavedb:00001270-a-1/scores
```

The first two endpoints return metadata; the final pattern downloads the chosen score table. MaveDB documents the API and score-set hierarchy at [API Quickstart](https://mavedb.org/docs/mavedb/programmatic-access/api-quickstart.html).
