# Additional external data sources: what exists, what we got, what is out of reach

*Written 27 October 2026. A survey of public resources for variant effect prediction and protein
stability, done while looking for precomputed ΔΔG we could use instead of computing our own.
Records what was downloaded, what was checked and found wanting, and two corrections to claims made
during the search.*

---

## 1. Summary

| resource | what it holds | covers our proteins? | status |
|---|---|---|---|
| **Tsuboyama 2023 (Zenodo)** | **experimental** folding ΔG / ΔΔG, 776,298 rows | SRC SH3 only | **downloaded** |
| **RaSP (Zenodo)** | predicted ΔΔG, 1,345 proteins | **SRC only — no JAKs** | downloaded, limited |
| **RaSP (ERDA)** | predicted ΔΔG, 23,391 human proteins | yes, all four | **network-blocked here** |
| **MissenseDB (Zenodo)** | AlphaMissense + VESM-3B + VESPA + DSSP + pLDDT, 19,436 proteins | yes, all four | identified, not downloaded |
| **MaveDB** | experimental MAVE data | TYK2, JAK1, SRC — **not JAK2/JAK3** | API queried |
| **AVE VEP catalogue** | predictor *metadata* only, 115 coding VEPs | n/a | downloaded |
| ProThermDB / ThermoMutDB / FireProtDB | curated experimental ΔΔG | unlikely | not pursued |

**The one thing that does not exist anywhere:** a precomputed **dual-state** ΔΔG. Every public
resource is single-structure. The open-minus-closed difference feature remains ours alone — which,
given it came out as noise (`conclusions_ddG_difference_feature.md`), is a small loss.

---

## 2. Tsuboyama 2023 — experimental folding stability (downloaded)

**Mega-scale experimental analysis of protein folding stability in biology and design.**
Zenodo DOI [10.5281/zenodo.7992926](https://doi.org/10.5281/zenodo.7992926), CC-BY-4.0, deposited
2023-04-21. Nine files, 1.93 GB total. We took `Processed_K50_dG_datasets.zip` (1,013.7 MB).

Local: `~/tsuboyama/`. Extracted to `~/tsuboyama/extract/Processed_K50_dG_datasets/`.

### What is in it

| file | size | contents |
|---|--:|---|
| `Tsuboyama2023_Dataset1_20230416.csv` | 1,284 MB | the larger dataset |
| `Tsuboyama2023_Dataset2_Dataset3_20230416.csv` | 698 MB | **776,298 rows, 479 WT constructs** |
| `Single_DMS_list.csv` | 0.4 MB | construct index |
| `Double_DMS_list.csv`, `Triple_DMS_list.csv` | small | multi-mutant indexes |
| `Heat_maps_single_DMS.zip` | 268 MB | per-construct heat maps |
| `Heat_maps_double_DMS.zip` | 89 MB | |

Columns that matter: `deltaG`, `deltaG_95CI_high/low` (with confidence intervals), `dG_ML`,
**`ddG_ML`**, `log10_K50_trypsin_ML`, `log10_K50_chymotrypsin_ML`, `mut_type`, `WT_name`,
`Stabilizing_mut`. Two proteases independently, with fitted unfolded-state baselines — this is a
careful thermodynamic measurement, not a proxy.

### Why it matters to us

**This is real ΔΔG in kcal/mol, with error bars, for ~776k variants.** It is the only thing in this
survey that can tell us whether our PyRosetta ΔΔG magnitudes mean anything. Our own benchmarks —
the Howard DMS and the paper's JAK1 clusters — measure *function* and *abundance*; abundance is a
proxy for stability, never a measurement of it. Everything we have concluded about ΔΔG so far rests
on rank correlation against a phenotype, which is why `conclusions_ddG_difference_feature.md` clips
to ranks rather than trusting magnitudes.

### The SRC SH3 subset

Saved to `~/tsuboyama/src_sh3_ddG.csv` (4.0 MB). Two constructs, `1SRM.pdb` and `5ECA.pdb`:

| | value |
|---|---|
| rows | 4,400 (2,786 from 5ECA, 1,614 from 1SRM) |
| single substitutions | 2,165 |
| with a usable `ddG_ML` | **1,025** |
| ddG_ML median | **−0.79 kcal/mol** |
| ddG_ML range | −4.56 to +1.17 |
| destabilising (< −0.5) | 623 |
| **stabilising (> +0.5)** | **50** |
| dG_ML median (n = 1,943) | +3.22 |

**Note the missing values: 1,140 of 2,165 single substitutions have `ddG_ML = '-'`.** Where the
variant is too destabilised to fit a baseline, there is no number. Any correlation computed on this
subset is therefore conditioned on the variant being measurable — a selection effect that removes
the most destabilising half. This matters for calibration and is easy to miss.

The sign convention here is the opposite of ours: **negative ddG_ML = destabilising** in their
table, matching our convention in `pipeline/ddg/` (ΔΔG = ΔG_WT − ΔG_mut, negative = destabilising).
Confirm per-file before joining anything.

### Honest limit

**Small domains only.** The SRC entry is the **SH3 domain**, 55–59 residues. No large-scale
experimental stability measurement exists for the SRC kinase domain, let alone a JAK. So a
calibration done here is a calibration on small, soluble, fast-folding domains, and its transfer to
a 1,187-residue multi-domain kinase is an assumption, not a result.

---

## 3. RaSP — predicted ΔΔG (partly obtained, and a correction)

**Blaabjerg et al., "Rapid protein stability prediction using deep learning representations",
*eLife* 2023** — [elifesciences.org/articles/82593](https://elifesciences.org/articles/82593).
RaSP predicts ΔΔG for ~230–300 million substitutions across the human proteome on AlphaFold
structures. Method: [github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg).

### Correction: the Zenodo file is not the proteome

During this survey it was stated that the Zenodo deposit would contain all four JAKs. **It does
not.** [`10.5281/zenodo.7409755`](https://doi.org/10.5281/zenodo.7409755) holds one file,
`df_rasp_gnomad_clinvar.csv` (414 MB, 8,770,220 rows) — and it covers only **1,345 UniProt entries
across 1,366 PDB chains**. It is RaSP run on *experimental PDB structures* that overlap
gnomAD/ClinVar, not the AlphaFold proteome.

Checked directly:

| protein | UniProt | in the file? |
|---|---|---|
| JAK1 | P23458 | **absent** |
| JAK2 | O60674 | **absent** |
| JAK3 | P52333 | **absent** |
| TYK2 | P29597 | **absent** |
| **SRC** | **P12931** | **present — 9,000 variants** |

The JAKs have no suitable full-length experimental structure, so they fall outside this subset. The
concept DOI `10.5281/zenodo.6835877` redirects to the same record; there is no Zenodo mirror of the
proteome set.

Local: `~/rasp_dl/df_rasp_gnomad_clinvar.csv`, with the SRC rows at `~/rasp_dl/jaks_src_rasp.csv`
(9,000 variants; 148 carry a gnomAD allele frequency, none carry a ClinVar label).

### The proteome set is network-blocked from this environment

The full AlphaFold-based set (23,391 human proteins, a Vaex dataframe plus a zipped directory)
lives only on the Copenhagen ERDA share: **https://sid.erda.dk/sharelink/fFPJWflLeE**

That host refuses connections here — DNS resolves to 130.225.104.13, then the TLS handshake is
reset (`Recv failure: Connection reset by peer`). A network-level block, not a bad URL. **It has to
be fetched from a normal browser session.**

### Caveats the authors state

RaSP was trained and benchmarked only on **soluble, globular, folded** proteins; predictions for
membrane and disordered regions are less reliable. For a full-length JAK, values near the
interdomain linkers should be treated with caution. RaSP is also **single-structure**, so it gives a
per-state magnitude and no dual-state difference.

---

## 4. MissenseDB — found by accident, not yet downloaded

[**10.5281/zenodo.23396316**](https://doi.org/10.5281/zenodo.23396316), deposited **2026-10-15**
(twelve days before this note):

> precomputed missense variant effect predictions across **19,436 human Swiss-Prot proteins
> (~10.7 million residue positions)**, integrating **AlphaMissense, VESM-3B and VESPA** with
> DSSP-derived secondary structure, ligand proximity, Pfam domain annotations, AlphaFold pLDDT
> confidence scores, and HUMSAVAR clinical variant classifications.

| file | size |
|---|--:|
| `db1_position_summary.sqlite` | 25,171 MB |
| **`db1_position_summary.parquet`** | **3,467 MB** |
| `genomic_coords.sqlite` (MANE Select, 94.1 % proteome coverage) | 2,008 MB |
| `db2_humsavar_dbsnp.sqlite` / `.parquet` | 57 MB / 7 MB |
| `harmonised_scores_200bins.csv` + calibration tables | ~9 MB |

**Not ΔΔG.** What it would add to our 16-feature matrix: **VESM-3B and VESPA**, two predictors we do
not have, plus **per-residue pLDDT and DSSP secondary structure** — structural context we computed
by hand — and calibrated scores for all three predictors. It covers all four JAKs.

**No license is declared on the record.** Check before redistributing anything derived from it.

---

## 5. MaveDB — coverage, and a gap in our own panel

API: `api.mavedb.org/api/v1/`. `POST /score-sets/search` takes `{"text": "..."}`;
`GET /score-sets/<urn>` returns the full record; `GET /target-genes` returns all 3,120 target
records (2 MB).

| | count |
|---|--:|
| score sets, all organisms | **2,942** |
| target-gene records | 3,120 |
| human target records | **1,500** (48 %) |
| **distinct human genes** | **~470–590** |

Distinct-gene count depends on the field: 468 by UniProt accession, 589 by cleaned target name, but
only **79 by MaveDB's own `mappedHgncName`** — most records are not HGNC-mapped, so that field must
not be used for counting. Roughly **2.5 % of the 20,431 reviewed human proteins** have any MAVE
data, and it is concentrated: BRAF 119 target records, KRAS 43, UBC 33, MPL 26.

**Our proteins:** TYK2 present (the Howard data we use), JAK1 present, SRC present,
**JAK2 and JAK3 absent.** Two of our four proteins have no experimental variant data of any kind,
which is why their results rest entirely on the paper's clusters and our own predicted structures.

### SRC — the best-resourced comparator

| dataset | URN | variants | what it measures |
|---|---|--:|---|
| **Ahler et al. 2019**, *Mol Cell*, PMID [30956043](https://pubmed.ncbi.nlm.nih.gov/30956043/) | `urn:mavedb:00000041-a-1` | **3,506** | catalytic-domain **activity** via yeast growth |
| same paper, SH4 domain | `urn:mavedb:00000041-b-1` | 360 | |
| Tsuboyama-derived, WT | `urn:mavedb:00000192-0-1` | 1,576 | SH3 **folding stability** |
| Tsuboyama-derived, WT (5ECA) | `urn:mavedb:00000409-0-1` | 2,631 | |
| Tsuboyama-derived, **P51S** | `urn:mavedb:00000410-0-1` | 1,299 | |
| Tsuboyama-derived, **W37A** | `urn:mavedb:00000411-0-1` | 1,301 | |
| Beltran et al. 2024 domainome | `urn:mavedb:00001079-a-1` | 1,141 | SH3 abundance |

Ahler classifies **403 gain-of-function, 1,288 WT-like, 1,681 loss-of-function**, with replicate
Pearson **R = 0.91** between independent library transformations. For comparison, the Howard TYK2
duplicate arms reach r ≈ 0.55 (see `TYK2/DMS_Howard2026/dms_basic_statistics.md` §2).

Also relevant: [Nguyen et al., *Protein Science* 2023](https://onlinelibrary.wiley.com/doi/abs/10.1002/pro.4656)
on Hsp90 dependence of SRC, and [Profiling drug resistance in Src kinase at scale,
*Cell Chem Biol* 2023](https://www.cell.com/cell-chemical-biology/fulltext/S2451-9456(23)00277-5),
which explicitly couples autoinhibition to catalytic-domain dynamics — our question in SRC form.

**No paper was found benchmarking computational ΔΔG or variant-effect predictors against the Ahler
dataset.** Treat that as "not found", not "does not exist" — ProteinGym has not been checked for SRC.

---

## 6. The AVE variant-effect-predictor catalogue — metadata, no values

[**varianteffect.org/veps/**](https://www.varianteffect.org/veps/) — Atlas of Variant Effects
Alliance, compiled by Ben Livesey and Tesni Walsh (Joe Marsh lab, Edinburgh) with the AVE
Analysis/Modelling/Prediction workstream.

Not a benchmark and not a leaderboard: **a catalogue with no scores**. The content is in two Google
Sheets linked from the page, both public and exportable as CSV
(`docs.google.com/spreadsheets/d/<id>/export?format=csv&gid=0`):

- coding VEPs — [`17Zsqz-VIS8HQ_Rfl135zRozjyEEcvf9sYdBkxoXwWqc`](https://docs.google.com/spreadsheets/d/17Zsqz-VIS8HQ_Rfl135zRozjyEEcvf9sYdBkxoXwWqc/edit) — **115 predictors**
- non-coding VEPs — [`1EW6em90FteT4bSwhnTiCGTn8MYe4rrYJ4KTegP-iS44`](https://docs.google.com/spreadsheets/d/1EW6em90FteT4bSwhnTiCGTn8MYe4rrYJ4KTegP-iS44/edit) — sequence-to-function models

Every row is filled for all six link/metadata columns: online predictor, **pre-calculated results**,
method download, training data, notes, references — plus Methodology, Type, five feature flags, and
the author-recommended pathogenicity threshold. **No prediction values.** Where the precomputed
scores actually live is fragmented: 6 on GitHub, 6 on Zenodo, 2 on HuggingFace, the rest on
individual lab servers.

### Its one real value for us: provenance

| `Type` | n | meaning |
|---|--:|---|
| **Clinical-trained** | **71** | trained on ClinVar/HGMD labels |
| Population-free | 37 | no human label leakage |
| Population-tuned | 7 | calibrated on population frequency |

Feature use: MSA 93/115, sequence 55, structure 44, **built on other predictors 23**.

**This explains why our 16-feature matrix collapsed into one block.** 62 % of published coding VEPs
are trained on clinical labels, and three of our own columns are built from the others:

| our feature | methodology | `Type` | structure | built on other VEPs |
|---|---|---|:---:|:---:|
| SIFT | empirical | Population-free | no | no |
| PROVEAN | empirical | Population-free | no | no |
| MutationAssessor | combinatorial entropy | Population-free | no | no |
| ESM-1b | language model | Population-free | no | no |
| PolyPhen-2 | naive Bayes | Clinical-trained | yes | no |
| VEST4 | random forest | Clinical-trained | yes | no |
| **CADD** | logistic regression | Clinical-trained | no | **yes** |
| **REVEL** | random forest | Clinical-trained | no | **yes** |
| **MetaRNN** | deep RNN | Clinical-trained | no | **yes** |
| PrimateAI | deep residual net | Population-tuned | yes | no |
| AlphaMissense | masked language model | Population-tuned | yes | no |

**CADD, REVEL and MetaRNN are built from the other columns in our own matrix.** Their high
correlations with the rest are definitional, not evidence of independent agreement. This belongs in
`predictor_correlation_matrix.md`.

### Author-recommended thresholds (answers "why these thresholds?")

AlphaMissense > 0.5 · REVEL > 0.5 · PolyPhen-2 > 0.5 · MetaRNN > 0.5 · SIFT < 0.05 ·
PROVEAN < −2.5 · PrimateAI > 0.803 · PrimateAI-3D > 0.821 · MutationAssessor > 3.5 ·
EVE > 0.5 · popEVE < −5.056.

**CADD, ESM-1b, ESM-1v, MSA Transformer and VEST4 have no author-defined threshold** — worth
knowing, since we used CADD phred.

### Ten population-free structural predictors — the fair comparison for our ΔΔG

The only class methodologically comparable to our structural features, with no clinical-label
leakage:

**Envision · CPT (Cross Protein Transfer) · COSMIS (COntact Set MISsense tolerance) · SSEmb ·
SaProt · ProSST · VenusREM · ProtSSN · S3F · RSALOR**

**RSALOR** ("Relative Solvent Accessibility × Log-Odds Ratio", empirical) is close to what we would
build by combining our RSA data with conservation, and it is published with no machine learning.
**COSMIS** is the other direct comparator. **Our matrix contains none of these.** If we want to
claim our structural features add something, this is the comparison set — not AlphaMissense.

---

## 7. Curated experimental ΔΔG databases — identified, not pursued

| resource | size | download |
|---|---|---|
| **ProThermDB** | ~31,500 entries (ΔG, Tm, ΔH, ΔCp), *NAR* 2020 | [web.iitm.ac.in/bioinfo2/prothermdb](https://web.iitm.ac.in/bioinfo2/prothermdb) — form required |
| **ThermoMutDB** | >14,000 experimental entries | [biosig.unimelb.edu.au/thermomutdb/downloads](http://biosig.unimelb.edu.au/thermomutdb/downloads) — CSV, JSON, SQLite, REST API |
| **FireProtDB** | single-point thermostability | own site; a [ThermoMPNN-derived subset](https://zenodo.org/record/8169289) has 3,438 mutations / 100 proteins |

ThermoMutDB is the easiest (direct CSV, no form). None of these is likely to contain a JAK, so they
are useful for protocol calibration rather than for our proteins.

---

## 8. ProteinGym — not checked

[proteingym.org](https://proteingym.org) · [benchmarks and leaderboards](https://proteingym.org/benchmarks) ·
[github.com/OATML-Markslab/ProteinGym](https://github.com/OATML-Markslab/ProteinGym)

Unlike MaveDB (an archive) ProteinGym is a **benchmark**: curated DMS assays plus precomputed
predictions from many models, with fixed evaluation splits. Four leaderboards — DMS substitutions
zero-shot, DMS substitutions supervised (random / **by position** / contiguous splits), DMS indels,
and clinical. The by-position split is the honest one, and the same scheme we applied by hand for
TYK2 with 5-fold CV grouped by position.

Two cautions: it normalises each assay to **one score per variant**, so the 11-arm structure and the
batch effects we found in TYK2 would be flattened; and **it has not been checked whether TYK2, SRC
or any JAK appears among its assays.**

Given the ΔΔG-difference negative result, ProteinGym is the natural place to test whether that
feature fails *generally* or only on JAKs.

---

## 9. What to do next, in order

1. **Calibrate the PyRosetta protocol against Tsuboyama** on the SRC SH3 subset
   (`~/tsuboyama/src_sh3_ddG.csv`, 1,025 measured ΔΔG). Expect rank agreement and poor magnitudes —
   that is the pattern in `conclusions_ddG_difference_feature.md` and in the Sanachai SIE-vs-QM
   comparison (`open_close/open_close_inf.md` §3). Mind the 1,140 missing values: the subset is
   conditioned on measurability.
2. **Fetch the RaSP proteome set** from the ERDA link in a browser, and extract the four JAKs. It is
   the only way to get an independent published ΔΔG for JAK2 and JAK3, which have no experimental
   data at all.
3. **Add the AVE `Type` and "built on other VEPs" columns** to `predictor_correlation_matrix.md`,
   and add the author-recommended thresholds. This is the cheapest improvement on this list.
4. **Consider MissenseDB** (3.5 GB parquet) for VESM-3B, VESPA, pLDDT and DSSP across all four JAKs.
5. **Check ProteinGym** for SRC and the JAKs before planning around it.

## Local files

| path | size | contents |
|---|--:|---|
| `~/tsuboyama/Processed_K50_dG_datasets.zip` | 1,014 MB | the Tsuboyama archive |
| `~/tsuboyama/extract/Processed_K50_dG_datasets/` | ~1.4 GB | the two extracted ΔG tables |
| **`~/tsuboyama/src_sh3_ddG.csv`** | **4.0 MB** | **SRC SH3, 4,400 rows with experimental ΔG/ΔΔG** |
| `~/rasp_dl/df_rasp_gnomad_clinvar.csv` | 414 MB | RaSP, 1,345 proteins |
| `~/rasp_dl/jaks_src_rasp.csv` | small | RaSP SRC rows, 9,000 variants |

These are large and live outside the repository. Only the derived tables are worth committing.
