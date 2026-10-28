# Review of the three ΔΔG documents in `external_data/`, and which to read for what

*Written 28 October 2026. Three documents on overlapping topics now sit in `external_data/`, written
by different sessions within about 20 hours. This reviews all three, records the corrections each
needs, and says which is authoritative for what. No document is superseded — they answer different
questions, and two of them contain findings the others lack.*

---

## 1. Index — read this first

| document | size | what it is actually about | authoritative for |
|---|--:|---|---|
[`ddg_precomputed.md`](ddg_precomputed.md) | 4.9 KB | **labelled training/benchmark datasets** — ThermoMPNN's `data_all/` splits | where to get ΔΔG **labels** for training and evaluation |
[`ddg_computations_survey_gpt.md`](ddg_computations_survey_gpt.md) | 36.5 KB | **the method and resource landscape** — 12 packages, 5 precomputed human sets, benchmarks, open questions | **method selection, the literature, and the question list before scaling** |
[`ddg_study.md`](ddg_study.md) | 26.7 KB | **one resource obtained and tested** — ProtVar FoldX downloaded, verified, measured against our own data | **what we actually have on disk, and how well it performs** |

**The titles mislead.** `ddg_precomputed.md` sounds like it covers precomputed *predictions*; it covers
precomputed *measurements and splits*. Nothing in it overlaps `ddg_study.md` in substance.

**If you read one thing:** `ddg_computations_survey_gpt.md` §8 (the question list) and §10 (the
workflow). They are the best-structured part of the three and they frame the decisions.

---

## 2. `ddg_precomputed.md` — accurate, narrow, keep as is

Covers `github.com/Kuhlman-Lab/ThermoMPNN → data_all/`, 94.6 MB, ~280,000 ΔΔG labels pre-split by
the published Dieckhaus 2024 partitions.

**Strengths.** Row counts verified by download, not quoted. The distinction between the minimal
mega-scale columns and the rich FireProtDB columns (`uniprot_id`, `interpro_families` — joinable to
`more_proteins/`) is exactly the practical detail that matters. The point that **the splits are not
ours to re-draw** if comparing to published numbers is correct and easy to get wrong.

**The best catch in any of the three documents:** `myoglobin_clean.csv` is misnamed — all 42 rows
carry `#SET = TEST_P53` with a p53 sequence, and the file's `PDB` is 2OCJA while 2AC0A is the
cluster id. That is the kind of error that silently corrupts a benchmark. It was then corrected
again in commit `963e5e89` after an initial column misread. Good process.

**One gap.** It does not mention **Human Domainome 1** (>500,000 variants, >500 human domains),
which `ddg_computations_survey_gpt.md` §5 identifies as the most relevant *human* benchmark. For a
project targeting human genes that is a more important evaluation set than S669 or Ssym. Worth
adding one row.

**Verdict: no changes needed beyond that.** Scope is honest, numbers are checked.

---

## 3. `ddg_computations_survey_gpt.md` — the strongest of the three, with one hole

This is a better survey than mine. It is broader, better organised, properly hedged, and it found
five resources I missed entirely. The hedging discipline is notably good — it consistently separates
"published timing" from "measured here", and Appendix B lists what was *not* verified.

### 3.1 What it found that `ddg_study.md` missed — all three checked and confirmed

**① Liao & Lehner 2026 — a proteome-wide ThermoMPNN resource. This may be the single most useful
item across all three documents, and I had not found it.**

Verified live:

```
Zenodo 18386427 · "Allostery is a widespread cause of loss-of-function variant pathogenicity"
  zenodo_final_jan2026.tar.gz   5.72 GB   CC-BY-4.0   deposited 2026-01-27
  "proteome-wide predictions of protein stability changes and corresponding
   ESM-1v scores for all variants"
Paper: Liao & Lehner, Nat Commun 2026, doi:10.1038/s41467-026-74517-8
```

**Why this likely beats ProtVar FoldX for our purpose.** On Human Domainome 1, ThermoMPNN reaches
median Spearman **≈0.50** (0.57 excluding zinc fingers). FoldX against DMS averages **≈0.26**
(Gerasimavicius 2023), and I measured ProtVar FoldX at **0.275** on the TYK2 abundance arm. If
ThermoMPNN's advantage holds on full-length proteins, this resource is roughly **twice as
informative per variant** as what I downloaded — and it ships **ESM-1v in the same table**, which is
a second, independent channel.

Caveat the survey correctly notes: that analysis retained **19,288 proteins**, excluding anything
under 16 or over 2,700 residues and anything without matching ESM-1v. And Domainome correlations
are *abundance* correlations, not kcal/mol accuracy.

**② SPURS** — verified: [luo-group/SPURS](https://github.com/luo-group/SPURS), **100★, MIT, pushed
2026-07-15**. Reports median per-protein Spearman 0.83 vs ThermoMPNN's 0.77 on Megascale, and 0.54
vs 0.49 on Domainome. Developer-run evaluation, and there is a **March 2026 correction replacing
Figure 5** — use the corrected release. The survey is right to call it "pilot first".

**③ The ProtVar journal citation.** `ddg_study.md` cites only the Jänes et al. bioRxiv preprint
(PMC11160786). There is also a peer-reviewed web-server paper:

> Stephenson, Totoo, Burke, Jänes, Beltrao & Martin, *"ProtVar: mapping and contextualizing human
> missense variation"*, **Nucleic Acids Research 2024, 52:W140–W147**, doi:10.1093/nar/gkae413

**But a small correction to the survey here:** it cites gkae413 as the paper that "documents the
FoldX calculation". gkae413 is the *web server* paper; the 208 M FoldX computation and its
methodology are in **Jänes et al.** (the preprint). Both are real and should both be cited, for
different things.

Also missed by me and worth having: **StabilitySort** (human proteome, **MAESTRO**-based — *not*
FoldX, and the survey is right to flag that its Z-scores are not kcal/mol), **MutateX** (GPL-3.0
orchestration around FoldX saturation mutagenesis), **GeoStab/GeoDDG**, **DDGemb**, **PROSTATA**,
**DDMut**, **VenusMutHub** (905 small experimental datasets, 527 proteins, 23 models), and the two
recent reviews (Qiu 2024; Peccati 2025).

### 3.2 The hole: it could not get the bulk data, and concluded from a single API call

Appendix B records:

> ProtVar bulk FTP / StabilitySort / direct RaSP archive access — **HTTP errors during direct requests**

and §2 marks its ProtVar verification as a **single lookup** (TP53 R175H, 4.88 s), explicitly
labelled "a database lookup, not a new calculation".

That is honest, but it leaves the practical question unanswered: *does the bulk resource work, how
big is it, and does it cover our genes?* **It does, and I have it.** From `ddg_study.md`:

| | |
|---|---|
| file | `2025.02.10_foldx_energy.csv.gz`, **1.5 GB**, downloaded in **6 minutes** |
| rows | **208,792,558** — decompressed and counted |
| coverage | **all four JAKs and SRC**, ~20,000 variants each |
| licence | CC-BY-4.0 |
| committed | `external_data/protvar_foldx_jak_src.csv`, 89,927 variants |

So the survey's "First source for empirical energy-function predictions" recommendation is right,
and the route is confirmed working end to end. The earlier FTP failure was transient or
environment-specific.

### 3.3 Two things only measurement could settle

The survey says, correctly, that there is "no defensible single ranking". Two numbers from
`ddg_study.md` §7 put limits on that, measured on **20,162 TYK2 variants**:

**Two structure-based ΔΔG methods agree at only ρ = 0.555.** ProtVar FoldX vs our PyRosetta,
unchanged at ρ = 0.548 when restricted to pLDDT ≥ 90. This supports the survey's warning that
method errors are **not independent enough to treat agreement as a confidence interval** — but it
also shows the disagreement is large enough to be a usable signal.

**The free download beat our own compute.** Against the Howard DMS: FoldX +0.275 vs our PyRosetta
+0.244 on abundance, both far below AlphaMissense's +0.417. This is the empirical justification for
the survey's top-line recommendation — retrieve before computing — and neither of the other two
documents contains it.

### 3.4 Smaller points

- **The RaSP Table 4 timings are the most useful concrete numbers in any of the three** (GCK, 434 residues: RaSP 11 s prep + 173 s predict; Rosetta 7,996 + 118,361 s; FoldX 728 + 309,762 s). The survey is right to warn against generalising "FoldX is slower than Rosetta" from one protocol. `ddg_study.md`'s own figure — ~100,000 variants/hour per 8-core box — is from our cached-WT repack protocol and is not comparable to a full `cartesian_ddg`; that caveat is in the file but deserves more emphasis.
- **"Preserve missingness"** (§7) is a point neither other document makes and it matters here: the ProtVar 2025 file silently dropped the pLDDT>70 filter its 2024 README describes, so 4–8% of rows for our proteins are low-confidence. Missing ≠ neutral, and low-confidence ≠ missing.
- **The §8 question list is the best single section across all three.** The items `ddg_study.md` §6 does not raise: haplotypes/epistasis, within-gene vs cross-gene calibration, whether excessive *stabilisation* can cause disease, and whether the protein's baseline stability margin is known at all (ΔΔG alone does not give folded fraction).
- Appendix B notes **no PyTorch and no GPU** in that session. Still true here. Anything using ThermoMPNN or SPURS needs molab, per the project's GPU rule.

---

## 4. Where the three disagree, and what is correct

| point | resolution |
|---|---|
| Does the ProtVar bulk download work? | **Yes** — 1.5 GB, 208,792,558 rows, 6 min. The survey's HTTP error was transient. |
| Which ProtVar paper to cite? | **Both.** Jänes et al. (PMC11160786) for the 208 M FoldX computation; Stephenson et al. NAR 52:W140–W147 for the server/API. |
| Is the pLDDT>70 filter applied? | **In the 2024 file, per its README. Not in the 2025 file** — filter yourself. |
| Best precomputed source for human genes? | **Unresolved, and this is the open question.** `ddg_study.md` says ProtVar FoldX (obtained, tested, ρ 0.275 on our data). The survey says Liao & Lehner ThermoMPNN (ρ ≈0.50 on Domainome, not obtained). **The ThermoMPNN resource is probably better and has not been tested.** |
| RaSP proteome coverage | Survey is more precise: 23,391 **AlphaFold structure files**, not 23,391 distinct genes. Both documents agree the ERDA route fails from here. |
| Is ΔΔG a good variant-effect predictor? | Both agree: no. ρ ≈0.26 vs ≈0.35–0.40 for sequence VEPs; FoldX AUC 0.661 for pathogenicity; only 43% of predicted-pathogenic variants predicted destabilising. Use it for **mechanism**, not ranking. |

---

## 5. What I would do next, given all three

1. **Download and test the Liao & Lehner ThermoMPNN proteome set** (5.72 GB, CC-BY-4.0). This is the highest-value open action across all three documents. Then repeat the §7 measurement — ThermoMPNN vs the Howard DMS on TYK2 — against the FoldX ρ = 0.275 baseline. If it reaches ~0.4–0.5 it becomes the primary source and no computation is needed for human genes at all.
2. **Then** build the lookup index over whichever wins, keyed on `(accession, position, mutated_type)`, with one column per method and the pLDDT/confidence retained — per the survey's "one column per method, do not collapse to an average".
3. **Add Human Domainome 1** to `ddg_precomputed.md` as the primary human evaluation set.
4. **Run the Ssym antisymmetry test** on our own PyRosetta protocol before extending it. Both documents flag antisymmetry; neither has run it. Data already in `external_data/new_predictors/Ssym.tsv`.
5. Treat SPURS as a pilot, not a dependency — developer-run benchmarks plus a figure correction.

## 6. Verification record for this review

| claim checked | result |
|---|---|
| Zenodo 18386427 exists, size, licence, contents | ✅ 5.72 GB, CC-BY-4.0, 2026-01-27, ThermoMPNN + ESM-1v proteome predictions |
| `10.1093/nar/gkae413` is a real ProtVar paper | ✅ NAR 2024, 52:W140–W147, Stephenson et al. |
| SPURS repository status | ✅ 100★, MIT, pushed 2026-07-15 |
| ProtVar bulk file row count | ✅ 208,792,558 (counted locally) |
| ProtVar covers JAK1/2/3, TYK2, SRC | ✅ 89,927 variants extracted |
| FoldX vs our PyRosetta agreement | ✅ ρ = 0.555 on 20,162 shared TYK2 variants |

Not checked: the Liao & Lehner archive contents (metadata only), Human Domainome 1 figures, the
SPURS and StabilitySort numbers, and every published timing quoted in the survey.
