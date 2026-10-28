# Computing ΔΔG for large numbers of human variants: a practical study

> **Three documents in this folder cover ΔΔG.** See
> [`ddg_docs_review.md`](ddg_docs_review.md) for which to read for what, and for the
> corrections each one needs.

*Written 28 October 2026. Research done for the question "how should we compute ΔΔG at scale for
human genes?" — covering precomputed databases, best practices, software, speed, support, and the
benchmark literature. All numbers in §2, §7 and §8 were measured here, not quoted.*

---

## 0. The short answer

**For human genes, do not compute ΔΔG. Download it.**

The EBI hosts **208,792,558 precomputed FoldX ΔΔG values** covering essentially every missense
substitution in the human proteome, free, CC-BY-4.0, with per-position AlphaFold confidence. I
downloaded the whole thing (1.5 GB gzipped) in six minutes and verified the row count.

Then I tested it against our own month of PyRosetta compute on TYK2. On the 20,162 variants both
cover:

| | Spearman vs Howard DMS abundance | Spearman vs IFN-α 100 U |
|---|--:|--:|
| **ProtVar FoldX** (a download) | **+0.275** | **+0.275** |
| our PyRosetta ddg_closed (weeks of compute) | +0.244 | +0.236 |
| AlphaMissense, for scale | +0.417 | +0.362 |

**The free download is slightly better than what we computed ourselves.** That is the single most
important finding in this document.

Compute your own ΔΔG only when one of these holds: the protein is non-human; you need a specific
conformational state (as we do for open/closed JAK); you need a complex/interface ΔΔG; or you need
a method other than FoldX. Otherwise the marginal value of compute is negative.

---

## 1. Decision tree

```
Is the protein human, and do you want monomer folding ΔΔG?
├─ YES → download ProtVar FoldX (§2.1). Done. 208M values, free.
│        Want a second opinion? Add RaSP (§2.2), trained on Rosetta cartesian_ddg.
└─ NO ──┬─ non-human, or need a specific conformation/state?
        │   └─ compute. ThermoMPNN first (fast, GPU, best benchmarked);
        │      Rosetta cartesian_ddg if you need the physics (§4).
        ├─ no usable structure?
        │   └─ ABYSSAL or DDGun — sequence-only (§4).
        └─ need ΔΔG of *binding* at an interface?
            └─ different problem; FoldX/Rosetta on the complex, or STAB-DDG. ProtVar
               has 486,099 AF2-Multimer models but no binding ΔΔG (§6).
```

---

## 2. Precomputed databases for human variants

### 2.1 ProtVar / FoldX — the main resource ⭐

**EBI ProtVar**, from Jänes, Müller, Selvaraj, Manoel, Stephenson, Gonçalves, Lafita, Polacco,
Obernier, Alasoo, Lemos, Krogan, Martin, Saraiva, Burke & Beltrao, *"Predicted mechanistic impacts
of human protein missense variants"*, bioRxiv 2024, DOI
[10.1101/2024.05.29.596373](https://doi.org/10.1101/2024.05.29.596373) (PMCID PMC11160786).

| | |
|---|---|
| web | https://www.ebi.ac.uk/ProtVar/ |
| bulk FTP | https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/ |
| file | `2025.02.10_foldx_energy.csv.gz` — **1.5 GB gz**, dated 2025-02-10 |
| **rows** | **208,792,558** (verified by decompressing and counting) |
| method | **FoldX v5.0** on AlphaFold2 structures |
| licence | **CC-BY-4.0** |
| code | https://github.com/jurgjn/af2genomics/ |

Schema — exactly what you want, nothing to parse:

```
uniprot_accession,uniprot_position,alphafold_fragment_id,
alphafold_fragment_position,wild_type,mutated_type,foldx_ddg,plddt
```

**Sign convention: positive `foldx_ddg` = destabilising.** Note this is the opposite of ours.

**Download, whole thing:**

```bash
curl -O https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/2025.02.10_foldx_energy.csv.gz
```
Took **6 minutes** here. Extracting one gene is a single `awk` pass (~4 min over 209 M rows):

```bash
gzip -dc 2025.02.10_foldx_energy.csv.gz \
  | awk -F, 'NR==1 || $1=="P29597"' > TYK2_foldx.csv
```

**Coverage of our own proteins — all five present:**

| protein | UniProt | variants | positions | median ΔΔG | median pLDDT | pLDDT<70 |
|---|---|--:|--:|--:|--:|--:|
| JAK1 | P23458 | 20,805 | 1,095 | +1.14 | 92.7 | 8.0% |
| JAK2 | O60674 | 20,349 | 1,071 | +1.20 | 93.1 | 5.3% |
| JAK3 | P52333 | 20,045 | 1,055 | +1.29 | 92.5 | 6.2% |
| TYK2 | P29597 | 20,178 | 1,062 | +1.31 | 91.0 | 8.4% |
| SRC | P12931 | 8,550 | 450 | +1.29 | 94.8 | 4.4% |

**JAK2 and JAK3 — which have no MAVE data and no experimental structure — now have a published
ΔΔG.** That closes the gap recorded in `external_data/more_data.md` §5.

**The API also works, but the published endpoint is wrong.** The README's example
(`/ProtVar/api/foldx/{acc}/{pos}`) 404s. The live route is:

```
GET https://www.ebi.ac.uk/ProtVar/api/prediction/foldx/{accession}/{position}
```
returning all 19 substitutions at that position with `foldxDdg` and `plddt`. The OpenAPI spec is at
`https://www.ebi.ac.uk/ProtVar/api/docs` (not `/v3/api-docs`); 28 endpoints, including
`/prediction/pocket/`, `/prediction/interaction/`, `/score/`, and a batch `POST /download`.

Verified live for TYK2 P982 (ΔΔG P982I = +3.16, P982K = +4.22, pLDDT 79.67), TYK2 V678, JAK2 V617,
JAK3 Y581, JAK1 V658 and SRC Y530.

**Caveat on the pLDDT filter.** The 2024 README says only pLDDT>70 positions are included. The
2025 file does **not** honour that — the sample file's first rows have pLDDT 56.9, and 5–8% of our
proteins' rows are below 70. **Filter yourself.** Low-pLDDT positions are disordered regions where
ΔΔG is not a meaningful quantity.

**Also on that FTP:** `1048genes_annotations.tar.gz` (538 MB), plus pockets (109,599 high-confidence)
and interfaces (486,099 AF2-Multimer models, 126,118 high-confidence pairs).

### 2.2 RaSP — second opinion, trained on Rosetta

Blaabjerg et al., *eLife* 2023, [82593](https://elifesciences.org/articles/82593). Trained to
reproduce Rosetta `cartesian_ddg`, so it's an independent *method family* from FoldX.

| | |
|---|---|
| human proteome | **23,391 proteins**, ~230 M predictions |
| download | ERDA share https://sid.erda.dk/sharelink/fFPJWflLeE (Vaex dataframe + zip) |
| Zenodo subset | [10.5281/zenodo.7409755](https://doi.org/10.5281/zenodo.7409755), 414 MB |

⚠ **Two traps.** The Zenodo file is **not** the proteome — it is 1,345 PDB-backed proteins only, and
**contains none of the JAKs** (only SRC). The real proteome set is ERDA-only, and **ERDA refuses
connections from this environment** (DNS resolves, TLS reset). It needs a browser session.

Authors' caveat: trained and benchmarked only on **soluble, globular, folded** proteins.

### 2.3 Experimental ΔΔG — for calibration, not coverage

| resource | size | notes |
|---|---|---|
| **Tsuboyama 2023** [zenodo 7992926](https://doi.org/10.5281/zenodo.7992926) | 776,298 rows, 479 constructs | the gold standard; ΔG with 95% CIs, two proteases. **Small domains only** |
| **ProThermDB** | ~31,500 entries | ΔG, Tm, ΔH, ΔCp. Form required |
| **ThermoMutDB** | >14,000 | CSV/JSON/SQLite + REST API. Easiest |
| **FireProtDB** | single-point | [ThermoMPNN subset](https://zenodo.org/record/8169289): 3,438 muts / 100 proteins |

Already downloaded: `~/tsuboyama/`, with the SRC SH3 extract committed at
`external_data/SRC/src_sh3_experimental_ddG_Tsuboyama2023.csv` (1,025 measured ΔΔG).

### 2.4 Related but not ΔΔG

- **MissenseDB** [zenodo 23396316](https://doi.org/10.5281/zenodo.23396316), 2026-10-15 — AlphaMissense + VESM-3B + VESPA + DSSP + pLDDT for 19,436 proteins, 10.7 M positions. 3.5 GB parquet. No licence declared.
- **Missense3D** — ~4 M precomputed structural predictions for human missense.
- **SNPeffect 5.0** — structural phenotyping on AlphaFold models.
- **MTR3D-AF2** — spatially derived missense tolerance.
- **COSMIS** — per-residue constraint; already extracted for our five proteins (`external_data/new_predictors/cosmis_jak_src.tsv`).

**What does not exist anywhere: a precomputed *dual-state* ΔΔG.** Every public resource is
single-structure. Our open-minus-closed feature has no external equivalent — and it came out as
noise.

---

## 3. Best practices

### 3.1 Protocol

1. **Repack wild type identically to the mutant.** The commonest error. Scoring a raw input against a repacked mutant measures relaxation, not mutation. Cache the WT repack per position — the 19 substitutions share it (~19× saving).
2. **Constrain coordinates during relaxation.** Unconstrained FastRelax drift exceeds most mutational effects.
3. **Local pack radius, ~8 Å.** Whole-protein repacking adds noise, not signal.
4. **Replicate and average.** Rosetta guidance is ~50 replicates, mean of the lowest few. Single-shot ΔΔG is dominated by packing stochasticity.
5. **Use `cartesian_ddg`, not `ddg_monomer`** (Park et al. 2016).
6. **Write the sign convention in the file header.** Field standard is ΔΔG = ΔG_mut − ΔG_WT, positive = destabilising — FoldX, ProtVar and Tsuboyama's `ddG_ML` all use it. **We use the opposite.** This has already caused confusion in this project.
7. **Filter on pLDDT.** ≥70 minimum, ≥90 for anything load-bearing. ΔΔG in a disordered region is meaningless — there is no folded state to destabilise.
8. **Use each protein's own structure.** Homology-mapping burial failed outright for us: JAK2 V1110 is 8% exposed in a TYK2 mapping and **30%** in JAK2's own structure, at 44–51% identity. That reversed a published prediction.

### 3.2 The tests that catch a broken ΔΔG

**Antisymmetry.** A true ΔΔG satisfies ΔΔG(A→B) = −ΔΔG(B→A). Most predictors fail badly, biased
toward predicting destabilisation in both directions — Usmanova, Bogatyreva, Ariño Bernad, Ferreiro
& Ivankov, *"Self-consistency test reveals systematic bias in programs for prediction change of
stability upon mutation"*, *Bioinformatics* 2018, 34, DOI
[10.1093/bioinformatics/bty340](https://doi.org/10.1093/bioinformatics/bty340). Also Pucci et al.
2018 (Ssym) and Montanucci et al., *PLOS ONE* 2023, DOI
[10.1371/journal.pone.0283727](https://doi.org/10.1371/journal.pone.0283727) on data-imbalance bias.

**Use `Ssym`** — 342 forward/reverse pairs, now at
`external_data/new_predictors/Ssym.tsv`. **We have never run it on our protocol.** It is the
cheapest way to find out whether our ΔΔG is thermodynamic or a position-importance score wearing
kcal/mol.

**A null control.** Run the pipeline on two *identical* structures. We did: AUC **0.491** against
the DMS, indistinguishable from real structure pairs (0.499–0.507). One control settled what a year
of correlation analysis would not have.

**A trivial baseline.** DDGun is untrained, nearly free, and embarrassingly hard to beat. If a
physics-based ΔΔG doesn't beat it, that is the result.

**Homology-filtered test sets.** `S669_411` is S669 minus everything homologous to both common
training sets, via an all-against-all BLAST. Random splits overstate performance.

### 3.3 Don't subtract two correlated noisy estimates

Our main negative result, and it generalises. ddG_closed and ddG_open correlate at **r = 0.82**.
Subtracting cancels shared signal and keeps independent noise: AUC 0.70–0.74 for each state,
**0.50 for the difference**. Check the correlation *before* designing a difference feature.

### 3.4 Treat magnitudes as untrustworthy

End-point free-energy methods **rank acceptably and quantify badly.** The sharpest illustration is
Sanachai et al. 2020: against their own 0.16 kcal/mol measured selectivity, MM-PBSA overshot 23×,
MM-GBSA 32×, QM-corrected up to **73×** — and SIE, the method they featured least, was the only one
within 1×. (`open_close/open_close_inf.md` §3.)

Consequences: use ranks or clip; and **inspect the clipped tail** — our extreme values were
**100% `fa_rep`**, pure steric repulsion, not a free energy. Clipping hides this rather than
fixing it.

Our own scale check against FoldX makes the point: FoldX median +1.30 kcal/mol (IQR +0.19…+3.25),
ours median **+4.52 REU** (IQR +1.54…+13.22). Rosetta REU is nominally ≈ kcal/mol. Ours are
inflated roughly 3–4×.

### 3.5 Validate against ΔG, not phenotype

Everything we have concluded about ΔΔG rests on rank correlation against *function* and
*abundance*. Abundance is a proxy for stability; it is not a measurement of it. Calibrate on
Tsuboyama, ProThermDB or ThermoMutDB.

Two traps there: experimental ΔΔG depends on **pH and temperature** (the ABYSSAL tables carry both
columns), and in Tsuboyama **1,140 of 2,165 SRC SH3 substitutions have no ΔΔG at all** — too
destabilised to fit a baseline. Any correlation is conditioned on measurability, which removes the
most destabilising half.

---

## 4. Packages — speed, support, licence

| package | basis | speed | licence | support | notes |
|---|---|---|---|---|---|
| **FoldX 5.0** | empirical force field | ~seconds/mutation | **academic free, commercial paid** | mature, CRG | top of most benchmarks; what ProtVar used |
| **Rosetta `cartesian_ddg`** | physics | minutes–hours/mutation | free academic | very mature | the reference; expensive |
| **PyRosetta** (ours) | physics | **~100,000 var/h per 8-core box** with cached-WT repack | free academic | mature | our measured throughput; a full cartesian_ddg is orders slower |
| **RaSP** | 3D CNN on Rosetta labels | **480–1,036× Rosetta**; <1 s per residue saturation | NOASSERTION ⚠ | [58★, pushed 2026-04](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg) | proteome-scale screening |
| **ThermoMPNN** | ProteinMPNN embeddings + light head | seconds per structure, GPU | **MIT** | **[279★, pushed 2026-09](https://github.com/Kuhlman-Lab/ThermoMPNN)** — best-supported | **most robust in its own benchmark** vs Rosetta, RaSP, PROSTA-T |
| **ThermoMPNN-D** | extension | as above | MIT | [active](https://github.com/Kuhlman-Lab/ThermoMPNN-D) | double mutants; SCC <0.60 — epistasis is unsolved |
| **DDGun / DDGun3D** | simple, untrained | very fast | none declared ⚠ | [33★, pushed 2024-06](https://github.com/biofold/ddgun) | **the baseline you must beat** |
| **ABYSSAL** | ESM2 + MLP on Tsuboyama | GPU, minutes | **none on repo** ⚠ (model CC-BY-4.0) | 2★, 2023 | **sequence-only — no structure needed** |
| **Stability Oracle** | transformer | GPU | — | [32★](https://github.com/danny305/StabilityOracle) | |
| **RSALOR** | RSA × log-odds, **no ML** | trivial | **MIT** | [42★, pushed 2026-08](https://github.com/3BioCompBio/RSALOR) | interpretable baseline; we already have both inputs for TYK2 |
| others | | | | | PROSTATA, JanusDDG, DDGemb, HERMES, PremPS, DynaMut2, mCSM, INPS3D, PoPMuSiC, MAESTRO, KORPM |

**Licence warning.** FoldX academic licences cover *public-funded academic/education/research
institutions* only and explicitly **prohibit commercial computations**; commercial terms come from
CRG_BusinessInnovation@crg.eu, with a 2-week full-featured trial. **Using the ProtVar download
sidesteps this entirely** — it's CC-BY-4.0 output, not the program.

**If computing from scratch today, I would use ThermoMPNN**: MIT, 279 stars, pushed last month, the
most robust in its own comparison, and fast on GPU. The caveat is that it is trained on Tsuboyama,
so it inherits that data's small-domain bias.

---

## 5. Literature — surveys and benchmarks

### Benchmarks of ΔΔG predictors

- **Pancotti, Benevenuta, Birolo, Alberini, Repetto, Sanavia, Capriotti & Fariselli**, *"Predicting protein stability changes upon single-point mutation: a thorough comparison of the available tools on a new dataset"*, *Briefings in Bioinformatics* 2022, **23**, bbab555 — introduced **S669** (669 variants, 87 proteins, from ThermoMutDB), built specifically because existing tools were trained on overlapping data. The standard reference.
- **Critique of S669**: *Bioinformatics* 2023, **39**, btad011, DOI [10.1093/bioinformatics/btad011](https://doi.org/10.1093/bioinformatics/btad011) — argues S669 has incorrect entries and binding-rather-than-stability mutations; curates **S461**, on which `CartddG` ranks first, then KORPM and PoPMuSiCS.
- **Usmanova et al.**, *Bioinformatics* 2018, 34 — the self-consistency/antisymmetry bias result. Essential.
- **Montanucci et al.**, *PLOS ONE* 2023 — data-imbalance bias.
- **ThermoMPNN**: Dieckhaus, Brocidiacono, Randolph & Kuhlman, *PNAS* 2024, DOI [10.1073/pnas.2314853121](https://doi.org/10.1073/pnas.2314853121).
- **Epistasis failure**: [PMC11659742](https://pmc.ncbi.nlm.nih.gov/articles/PMC11659742/) — *"Protein stability models fail to capture epistatic interactions of double point mutations"*; all top predictors SCC < 0.60 on double mutants.
- **ProDDG** — [ivankovlab.ru/proddg](https://ivankovlab.ru/proddg), a database of ΔΔG *datasets and predictors*, from the ABYSSAL group. More directly relevant than the AVE catalogue (which indexes pathogenicity predictors). Not yet examined.
- **DDGemb datasets** — [ddgemb.biocomp.unibo.it/datasets](https://ddgemb.biocomp.unibo.it/datasets/) reuses Pancotti's 21-method results.

### ΔΔG as a variant-effect predictor — read these before planning anything

This is the literature that actually bears on the user's goal, and the findings are sobering.

**Gerasimavicius, Liu & Marsh**, *"Identification of pathogenic missense mutations using protein
stability predictors"*, *Scientific Reports* 2020, DOI
[10.1038/s41598-020-72404-w](https://doi.org/10.1038/s41598-020-72404-w) —
[PMC7506547](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7506547/):

- 13 structure-based predictors tested; **FoldX best, AUC 0.661** for pathogenic vs benign
- utility is **highly heterogeneous across proteins**
- all were **inferior to the best variant effect predictors**
- attributed to "alternate molecular mechanisms other than protein destabilisation underlying many pathogenic mutations"

**Gerasimavicius, Livesey & Marsh**, *"Correspondence between functional scores from deep mutational
scans and predicted effects on protein stability"*, *Protein Science* 2023, DOI
[10.1002/pro.4688](https://doi.org/10.1002/pro.4688) — preprint
[2023.02.03.527007](https://www.biorxiv.org/content/10.1101/2023.02.03.527007v1.full):

- 9 stability predictors against **45 DMS datasets, 35 proteins, 161,441 variants**
- **average Spearman ≈ 0.26 for ΔΔG, 0.28 for |ΔΔG|**
- **FoldX and Rosetta best**; complex structures improved both; DynaMut2, mCSM, ENCoM worst
- VEPs averaged **≈ 0.35** (0.40 excluding substitution matrices) — i.e. **ΔΔG is systematically worse than sequence VEPs at predicting DMS**
- best agreement on **abundance assays** (VAMP-seq and fluorescence); worst on viral replication and binding
- **dominant-negative and gain-of-function variants poorly captured** — explicitly including **SRC**, CALM1 and TARDBP
- individual highs: Rosetta/FoldX reach 0.66–0.68 on β-lactamase

**Gerasimavicius, Livesey & Marsh**, *Nature Communications* 2022 — LOF vs GOF vs dominant-negative
have "profoundly different effects on protein structure". I could not confirm the specific ΔΔG
numbers from the search and have not read the full text.

**Jänes et al. 2024** (the ProtVar paper) — of predicted destabilising variants, **69% are also
predicted pathogenic; but only 43% of predicted pathogenic variants are predicted destabilising.**
So destabilisation explains under half of pathogenicity.

---

## 6. Questions you did not ask, that matter more than some you did

### 6.1 Is ΔΔG even the right feature?

On the published evidence, **ΔΔG is a mediocre variant-effect predictor and a good mechanistic
annotation.** Average ρ ≈ 0.26 against DMS versus ≈ 0.35–0.40 for sequence VEPs; AUC 0.66 for
pathogenicity; and only 43% of pathogenic variants are destabilising.

Its value is **not** prediction accuracy. It is that ΔΔG says *why* — distinguishing a destabilised,
degraded protein from one that folds fine and fails functionally. That distinction is invisible to
AlphaMissense, and it is what our own TYK2 interface finding rests on. **Frame ΔΔG as a mechanism
channel, not a pathogenicity score.** If you need pathogenicity, AlphaMissense beats it everywhere
(ρ 0.417 vs 0.275 on our own data).

### 6.2 Folding ΔΔG or binding ΔΔG?

Most pathogenic variants in multi-domain and complex-forming proteins act at **interfaces**, not in
the core. Gerasimavicius 2023 found complex structures improved FoldX and Rosetta, and that missing
complex structures were the main reason binding assays correlated badly. Monomer ΔΔG cannot see
this.

ProtVar ships **486,099 AF2-Multimer interface models** and interface residue lists — but **no
binding ΔΔG**. If interfaces matter for your genes, that is a separate computation (FoldX/Rosetta
on the complex, or STAB-DDG).

### 6.3 Which isoform?

ProtVar is keyed to the **UniProt canonical isoform**. dbNSFP is keyed to transcripts. We have
already been burned by this: the dbNSFP join produced impossible values for 2-nucleotide
substitutions, and the fix required the canonical transcript ENST00000525621 and an `nt_changes`
column. **Decide isoform policy before joining anything**, and record it.

### 6.4 Disorder

~30% of the human proteome is intrinsically disordered. ΔΔG there is **undefined** — no folded
state to destabilise. The 2025 ProtVar file includes sub-70 pLDDT rows; filter them. For our five
proteins that is 4–8% of rows, but for a disorder-rich gene it could be most of them.

### 6.5 Stabilising mutations are nearly absent from training data

In the SRC SH3 experimental set: **623 destabilising, 50 stabilising.** Predictors trained on such
data are biased toward destabilisation and are poor at the stabilising tail. If gain-of-function
matters to you — and for JAK2 V617F it does — ΔΔG is the wrong instrument.

### 6.6 How do you know your numbers are any good?

Three cheap checks, in order: **Ssym antisymmetry**; **DDGun baseline**; **experimental ΔG
correlation** on Tsuboyama. None requires new compute infrastructure, and any of them can
invalidate a pipeline.

### 6.7 Multi-domain proteins

AlphaFold places domains relative to each other with low confidence even when each domain is
confident. A full-length JAK is a worked example: the interdomain linker regions have the lowest
pLDDT, and ΔΔG there is unreliable regardless of the per-residue score.

---

## 7. Measured here: how well do two ΔΔG methods agree?

On the **20,162 TYK2 variants** both ProtVar FoldX (AlphaFold2 monomer, FoldX v5) and our PyRosetta
(AF3 pair, cached-WT repack) cover, with signs aligned:

| | Spearman | Pearson |
|---|--:|--:|
| FoldX vs our ddg_closed | **+0.555** | +0.595 |
| FoldX vs our ddg_open | +0.540 | +0.592 |
| FoldX vs ddg_closed, pLDDT ≥ 90 only (n = 11,598) | +0.548 | — |

**Two independent structure-based ΔΔG methods on the same protein agree at ρ ≈ 0.55.** Restricting
to high-confidence positions does not help. So **method choice is a first-order decision**, not a
detail — and a single method's ΔΔG should not be treated as "the" ΔΔG.

Distributions: FoldX 80% positive (destabilising), median +1.30 kcal/mol; ours 89% positive, median
+4.52 REU. Both lean heavily destabilising, as expected from §6.5.

And against the Howard DMS:

| | IFN-α 1 U | IFN-α 100 U | abundance |
|---|--:|--:|--:|
| **ProtVar FoldX** | +0.128 | **+0.275** | **+0.275** |
| our ddg_closed | +0.108 | +0.236 | +0.244 |
| AlphaMissense | **+0.173** | **+0.362** | **+0.417** |

Three things follow:

1. **FoldX modestly beats our PyRosetta on every arm**, for zero compute.
2. **Our ρ = 0.244 on abundance matches the published average** (Gerasimavicius 2023: ≈ 0.26 across 45 DMS datasets). Our pipeline is performing exactly as the field expects — neither broken nor special.
3. **AlphaMissense beats both by ~1.7×.** Consistent with the literature. Use ΔΔG for mechanism, not for ranking.

---

## 8. Recommended plan for computing ΔΔG across many human genes

**Phase 0 — don't compute (1 day).** Download ProtVar once (1.5 GB, 6 min). Build a local index —
SQLite or parquet keyed on `(uniprot_accession, uniprot_position, mutated_type)` — and serve all
gene requests from it. For *n* human genes with monomer ΔΔG, this is the whole job. Already done:
`~/protvar/foldx_energy_2025.02.10.csv.gz`, with our five proteins extracted to
`~/protvar/jak_src_foldx.csv`.

**Phase 1 — a second method (1 day).** Fetch the RaSP proteome from ERDA **in a browser** (blocked
from here). Two independent methods per variant, and their disagreement is a usable confidence
signal — given ρ ≈ 0.55 between FoldX and Rosetta-family methods, that disagreement is large and
informative.

**Phase 2 — validate before trusting (2 days).** Ssym antisymmetry on our protocol; DDGun as
baseline; correlation against the Tsuboyama SRC SH3 ΔΔG we already have. If our protocol fails
these, Phase 3 is moot.

**Phase 3 — compute only the gaps.** Non-human proteins, specific conformational states,
interfaces, or genes where ProtVar's pLDDT is too low. Use **ThermoMPNN** (MIT, GPU, fast) for bulk
and Rosetta `cartesian_ddg` where physics is required. Our measured PyRosetta throughput is
**~100,000 variants/hour per 8-core box** with the cached-WT repack protocol — adequate for tens of
genes, not for a proteome.

**Phase 4 — frame it correctly.** Report ΔΔG beside AlphaMissense as a *mechanism* channel, never
as a competing pathogenicity score. The published numbers (ρ 0.26 vs 0.35–0.40; 43% of pathogenic
variants destabilising) make the stronger claim the honest one.

---

## 9. Local files

| path | size | contents |
|---|--:|---|
`~/protvar/foldx_energy_2025.02.10.csv.gz` | 1.5 GB | **208,792,558 FoldX ΔΔG, human proteome** |
`~/protvar/jak_src_foldx.csv` | 5.4 MB | the five proteins, 89,927 variants |
`~/tsuboyama/` | ~2.4 GB | experimental ΔG, 776,298 rows |
`~/rasp_dl/` | 414 MB | RaSP, 1,345 proteins (no JAKs) |
`~/cosmis_dl/` | 81 MB | COSMIS all three structure sources |
`~/abyssal_dl/`, `~/newpred/` | 4 MB | ABYSSAL benchmark suite |

Committed to the repository: `external_data/new_predictors/` (COSMIS + ABYSSAL benchmarks),
`external_data/SRC/src_sh3_experimental_ddG_Tsuboyama2023.csv`, `external_data/more_data.md`.

## 10. Open items

- RaSP proteome set needs a browser fetch (ERDA blocked here)
- ProDDG not yet examined
- Gerasimavicius 2022 *Nat Commun* LOF/GOF paper not read in full
- No 2025–2026 comparative review of ΔΔG predictors was found; Pancotti 2022 + the S461 critique remain the standard
- ThermoMPNN vs Stability Oracle throughput: no published head-to-head; would need benchmarking ourselves
- Whether ProtVar's 2025 file includes any methodological change from 2024 beyond dropping the pLDDT filter — the README was not updated
