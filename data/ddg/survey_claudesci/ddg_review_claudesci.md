# ΔΔG for the 24 selected JAK2 variants — six methods, where each ran, and what to distrust

*Written 6 November 2026. A companion to [`../survey/DDG_METHODS_SURVEY.md`](../survey/DDG_METHODS_SURVEY.md),
not a replacement: that one is proteome-wide over all four JAK kinases; this one is the 24 variants
supplied for JAK2, scored by **six** methods including three the other survey does not have
(mCSM-Stability, DDMut, RSALOR) and an **independent** Rosetta `cartesian_ddg` run that is a different
computation from the dual-state one in `data/ddg/`.*

Interactive version with figures: **[`ddg_review_claudesci.html`](ddg_review_claudesci.html)**.
All numbers below were recomputed from saved data for this document; nothing is quoted from memory.

---

## 1. Findings, shortest form

1. **Only 2 of 23 variants exceed the error bar of the method that produced them.** I1065T (+2.32)
   and Y317H (+1.68) against ThermoMPNN's measured RMSE of ±1.47 kcal/mol on held-out human data.
2. **The six methods agree with each other only moderately** — Spearman 0.47–0.70 on the full JAK2
   saturation scan. Force-field methods cluster together (FoldX↔ThermoMPNN 0.70), and RSALOR sits
   apart from them but close to AlphaMissense (0.71).
3. **The selected variants are *less* destabilising than a typical JAK2 substitution** — median 33rd
   percentile of JAK2's own distribution. For a gain-of-function set this is the expected result:
   these release JH2 autoinhibition rather than unfold the protein.
4. **The proline outlier tail is a Rosetta artefact and it is enormous.** For X→P substitutions the
   dual-state Rosetta median is **−215 REU**, against **+3.41** for FoldX and **+2.03** for
   ThermoMPNN. 92.5% of X→P fall below −10 in Rosetta, 2.4% above +10 in FoldX, **0.0%** in
   ThermoMPNN. This reproduces finding 3 of the companion survey exactly.
5. **`rosetta_delta` is noise.** Spearman |ρ| ≤ 0.02 against every other method, and the two
   independent JAK2 runs agree on *sign* only 55.2% of the time — a coin flip is 50%.
6. **My own `cartesian_ddg` reimplementation has the same disease in miniature.** For V625F,
   `cart_bonded` — bond-geometry strain, not stability — contributed +48.67 of +58.55 REU (83%).

---

## 2. What ran where

Three quite different execution modes. This matters for reproducibility: only the first group is
under your control.

| method | n | mode | where |
|---|--:|---|---|
| **ThermoMPNN** | 23/23 | local, CPU | this machine (8 cores, 16 GiB) |
| **Rosetta `cartesian_ddg`** | 21/23 usable | local, CPU | PyRosetta 2026.39, this machine |
| **RSALOR** | 23/23 | local | pip package + MAFFT alignment built here |
| **mCSM-Stability** | 23/23 | remote web server | biosig.lab.uq.edu.au (Queensland) |
| **DDMut** | 23/23 | remote JSON API | biosig.lab.uq.edu.au |
| **FoldX 5.0** | 22/23 | **downloaded precomputed** | EBI ProtVar — no FoldX binary was run here |

### Attempted and abandoned, with the reason

| method | outcome |
|---|---|
| **DUET**, **SDM** | server fault — `POST /duet/stability_prediction` returns HTTP 500 for *any* uploaded PDB, including DUET's own example protein 2OCJ with its own example mutation R282W chain A, while the hardcoded demo at `/duet/run_example_stability` works. Not a client problem. |
| **PoPMuSiC 3.1** | host `soluble.db.ulb.ac.be` unreachable *and* requires a registered account. Allowlisting alone would not have helped. |
| **DDGun** | all three score terms need a ~25 GB hhblits/uniclust profile. A single-sequence profile would reduce it to a substitution matrix, so it was reported as not run rather than approximated. |
| **molab** | not registered under Customize → Compute, so no dispatch target. The URL serves a marimo frontend (`/health`, `/api/status` respond; `/api/kernels` 404s). Sandboxes expire ~4 h, so migrating a 3 h job mid-run would have been slower. Everything ran locally. |

---

## 3. Local installation — exact steps and the traps

### ThermoMPNN
```bash
# do NOT git clone: the repo contains a .idea/ directory which this sandbox's
# filesystem refuses to create; git aborts the checkout but still exits 0
curl -L https://codeload.github.com/Kuhlman-Lab/ThermoMPNN/tar.gz/refs/heads/main -o t.tar.gz
tar tzf t.tar.gz | grep -v '/\.idea/' > keep.txt && tar xzf t.tar.gz -T keep.txt
pip install torch fair-esm omegaconf pytorch-lightning torchmetrics
export PYTHONPATH=$PYTHONPATH:$PWD/ThermoMPNN-main/analysis   # required
# edit local.yaml -> accel: "cpu"
```
Position convention trap: `custom_inference.py` reports
`position = PDB_author_number − min_author_number`, i.e. it indexes from the first observed residue
**including gaps** — it is NOT a dense index.

### PyRosetta (for `cartesian_ddg`)
```bash
# the pyrosetta-installer PyPI package stalls silently; fetch the wheel directly.
# Apple Silicon needs the .m1. build - the .mac. builds are x86_64 only.
D=https://west.rosettacommons.org/pyrosetta/release/release/PyRosetta4.Release.python311.m1.wheel/
W=$(curl -s "$D" | grep -o 'href="pyrosetta-[^"]*\.whl"' | sed 's/href="//;s/"//' | tail -1)
curl -L -o "/tmp/$W" "$D$W"          # 1.4 GB, ~25 min at ~1 MB/s
pip install "/tmp/$W"                # MUST keep the canonical wheel filename:
                                     # a shortened name fails with
                                     # "Invalid wheel filename (wrong number of parts)"
```
Licence: free for academic/non-commercial use, but granted to you/your institution — confirm that
covers automated use.

### RSALOR
```bash
pip install rsalor
conda install -c bioconda mafft      # RSALOR needs an MSA; it does not build one
```
Output-column trap: use **`mutation_pdb`** (format `wt + chain + pos + mt`, e.g. `MA1A`).
`mutation_fasta` uses *untrimmed-alignment* numbering and is not the UniProt position.

### RaSP (benchmarked earlier in the project, not a JAK2 column)
Four 2022-era breakages need patching: `np.int` removed from NumPy, `Bio.SubsMat` removed from
Biopython, `mkdssp` 4.x accepts only mmCIF, and training-only plot imports at module scope.
One real optimisation: `ds_pred` recomputes the cavity model once per ensemble member although it
does not depend on it — hoisting it gave **213.6 s → 23.2 s (9×)** with identical values.


### How to run each one

```bash
# ---- ThermoMPNN: saturation scan of one PDB, CPU
python ThermoMPNN-main/analysis/custom_inference.py \
    --pdb AF-O60674-F1.pdb --chain A --out jak2_thermompnn.csv
# position column = author_number - min_author_number  (NOT a dense index)

# ---- Rosetta cartesian_ddg: two stages, see relax_stage.py / ddg_stage.py one level up
python ../relax_stage.py      # 20x Cartesian relax per construct, keeps lowest-energy model
python ../ddg_stage.py        # per-variant repack + shell minimise, writes rosetta_ddg.json

# ---- RSALOR: needs an MSA you supply
curl -s "https://rest.uniprot.org/uniprotkb/stream?query=uniref_cluster_50:UniRef50_O60674&format=fasta" \
     -o jak2_cluster.fasta                      # repeat for P23458, P52333, P29597 to add paralogues
mafft --auto --thread 2 jak_family_input.fasta > jak_family_msa.fasta
python -c "
from rsalor import MSA
MSA('jak_family_msa.fasta','AF-O60674-F1.pdb','A',num_threads=2).save_scores('rsalor_jak2.csv')"
# target sequence MUST be first in the MSA and match the PDB

# ---- mCSM-Stability: batch endpoint, chain-first mutation list ('A V617F', not 'V617F A')
printf 'A V617F\nA I1065T\n' > mutlist.txt
curl -s -X POST https://biosig.lab.uq.edu.au/mcsm/stability_prediction_list \
     -F wild=@AF-O60674-F1.pdb -F mutation_list=@mutlist.txt
# returns an HTML results page at /mcsm/results_stability_prediction/<job_id>; parse with
# pandas.read_html (needs lxml). Note: mCSM lives at /mcsm/stability, NOT /mcsm_stability (404).

# ---- DDMut: proper JSON API, submit then poll
curl -s -X POST https://biosig.lab.uq.edu.au/ddmut/api/prediction_list \
     -F pdb_file=@AF-O60674-F1.pdb -F mutations_list=@mutlist.txt     # -> {"job_id": "..."}
curl -s -X GET  https://biosig.lab.uq.edu.au/ddmut/api/prediction_list -F job_id=<id>
# status RUNNING until done; ~15 min for 23 variants

# ---- FoldX via ProtVar: download, do not compute
curl -O https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/2025.02.10_foldx_energy.csv.gz
# 1.56 GB; stream it, deduplicate fragment-overlapping positions, filter to your accession
```

**Remember to negate mCSM and DDMut** before merging them with the others.

### Supporting
`gemmi`, `biopython`, `scipy`, `lxml` (needed by `pandas.read_html` for the mCSM result page),
`openmm`, `pdbfixer`, `reduce`, `dssp`.

---

## 4. Execution timings, measured

| job | hardware | time |
|---|---|---|
| ThermoMPNN saturation | 1 CPU core | **336 variants/s** median over 23 proteins (range 198–487); 269,458 variants in 961 s |
| PyRosetta single Cartesian FastRelax | 1 core, 276 residues | 575 s |
| PyRosetta relax stage, full protocol | 8 cores | **170.5 min** — 40 jobs (2 constructs × 20 replicates) |
| `cartesian_ddg`, 23 variants | 8 cores | **0.6 min** (~4 s/variant, both states) |
| *rejected alternative:* shell FastRelax | 8 cores | 340 s/variant — 85× slower **and less accurate** |
| PyRosetta wheel download | — | 1.4 GB at ~1 MB/s ≈ 25 min |
| mCSM-Stability, 23 variants (batch) | remote | returned by the first poll |
| DDMut, 23 variants (batch API) | remote | ~15 min |
| MAFFT, 902 sequences | 2 threads | ~3 min |
| RaSP | 1 core | ~125 variants/s |

Scale implication: a full human proteome saturation scan with ThermoMPNN at 336 var/s is
on the order of **9 days** on one core — tractable. The same with `cartesian_ddg` at 4 s/variant is
**not**: ~25 core-years.

---

## 5. Precomputed ΔΔG you can download instead of computing

| resource | contents | URL | licence |
|---|---|---|---|
| **ProtVar (EBI)** — the one actually used here | **208,792,558 rows**, 20,437 accessions, **76.0% of canonical human residues**, FoldX 5 on AlphaFold models | `ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/2025.02.10_foldx_energy.csv.gz` (1.56 GB) | CC BY 4.0 |
| ProtVar per-gene annotations | `<ACC>-fun-pop-str.csv.zip`, 43 columns incl. FoldX, AlphaMissense, EVE, ESM1b, CADD | `.../ProtVar/.../1048genes_annotations.tar.gz` (538 MB) | CC BY 4.0 |
| ProtVar MaveDB mirror | 1,993 score sets, 1,173 human, 3,423,249 rows, with `uniprotoffset` resolving study numbering to UniProt | `ftp.ebi.ac.uk/pub/databases/ProtVar/mave/` | CC0 |
| AlphaMissense | all human substitutions, precomputed | GCS bucket `dm_alphamissense`; also the Ensembl VEP plug-in | — |
| RaSP precomputed | 23,391 proteins, ~230M values | ERDA | **unverified — the download failed here (TLS handshake reset); counts are from the README/abstract, not measured** |

**Three ProtVar traps, all measured:**
1. Sign convention is **positive = destabilising** (verified empirically, not assumed).
2. **The README is stale.** It states a pLDDT-70 filter leaving 34,838,191 rows; the actual file is
   16.7% larger than that implies.
3. **17.3% of positions are fragment duplicates** — the same residue appears under more than one
   AlphaFold fragment. Deduplicate before aggregating.
4. Coverage is worst exactly where multi-domain proteins live: **64.1% for 1,001–2,700 aa**.
   For JAK2 specifically, 20,349 of 21,508 substitutions are present (94.6%); the 61 missing
   positions have median pLDDT 31.8 against 93.1 for present ones.

---

## 6. Descriptive statistics

### 6.1 The 23 computable selected variants

| method | count | mean | std | min | 50% | max |
|---|---|---|---|---|---|---|
| **ThermoMPNN** | 23.000 | 0.583 | 0.681 | -0.397 | 0.344 | 2.321 |
| **FoldX 5.0** | 22.000 | 0.793 | 1.550 | -1.093 | 0.671 | 5.334 |
| **mCSM-Stability** | 23.000 | 0.923 | 0.681 | -1.129 | 0.959 | 2.106 |
| **DDMut** | 23.000 | 0.621 | 0.833 | -0.790 | 0.460 | 2.720 |
| **Rosetta cartesian** | 23.000 | 3.981 | 12.175 | -2.402 | 1.160 | 58.549 |
| **RSALOR** | 23.000 | 4.816 | 3.052 | -0.374 | 3.984 | 11.022 |

Units differ and must not be mixed: ThermoMPNN/FoldX/mCSM/DDMut are kcal/mol, Rosetta is REU,
RSALOR is a log-odds ratio scaled by RSA. The Rosetta mean of 3.98 is inflated by the single
V625F artefact (+58.5); excluding the two flagged variants the median is +1.05.

### 6.2 The complete JAK2 saturation scan, for background

| method | count | mean | std | min | 50% | max |
|---|---|---|---|---|---|---|
| **ThermoMPNN** | 21508.000 | 0.970 | 0.960 | -2.843 | 0.744 | 4.746 |
| **FoldX 5.0** | 20349.000 | 2.166 | 3.658 | -4.487 | 1.198 | 69.533 |
| **Rosetta dual-state (closed)** | 21508.000 | -54.970 | 199.302 | -3495.650 | -4.158 | 45.679 |
| **Rosetta delta** | 21508.000 | 0.253 | 99.619 | -2280.818 | -0.003 | 2633.898 |
| **RSALOR** | 21508.000 | 5.436 | 3.072 | -4.267 | 5.556 | 12.062 |
| **RSA (fraction)** | 21508.000 | 0.314 | 0.291 | 0.000 | 0.230 | 1.000 |

---

## 7. Correlations

Spearman ρ over the complete JAK2 saturation scan, 20,349 rows complete in all methods
(limited by FoldX coverage). RSALOR here is my own full-protein run merged into the companion
survey's table.

| Spearman ρ | ThermoMPNN | FoldX 5.0 | Rosetta dual-state (closed) | Rosetta delta | RSALOR | RSA | AlphaMissense |
|---|---|---|---|---|---|---|---|
| **ThermoMPNN** | 1.000 | 0.697 | 0.533 | 0.001 | 0.547 | -0.569 | 0.530 |
| **FoldX 5.0** | 0.697 | 1.000 | 0.544 | -0.016 | 0.530 | -0.563 | 0.501 |
| **Rosetta dual-state (closed)** | 0.533 | 0.544 | 1.000 | 0.126 | 0.473 | -0.489 | 0.447 |
| **Rosetta delta** | 0.001 | -0.016 | 0.126 | 1.000 | -0.005 | 0.017 | 0.010 |
| **RSALOR** | 0.547 | 0.530 | 0.473 | -0.005 | 1.000 | -0.765 | 0.713 |
| **RSA** | -0.569 | -0.563 | -0.489 | 0.017 | -0.765 | 1.000 | -0.512 |
| **AlphaMissense** | 0.530 | 0.501 | 0.447 | 0.010 | 0.713 | -0.512 | 1.000 |

Three things to read off it:

- **Force-field methods cluster.** FoldX↔ThermoMPNN 0.70 is the strongest pair; Rosetta dual-state
  sits at 0.53–0.54 with both.
- **RSALOR is a genuinely different axis.** It correlates 0.55/0.53 with the ΔΔG methods but
  **0.71 with AlphaMissense** — it is behaving as an evolutionary score, which is what it is.
  Its −0.77 with RSA is partly definitional, since RSALOR is RSA-scaled.
- **RSA alone is competitive.** |ρ| 0.49–0.57 against every energy method — one geometric number,
  no energy function, nearly as informative as the methods are about each other.
- **`rosetta_delta` correlates with nothing** (0.00, −0.02, −0.00, 0.01).

On the 23 selected variants the agreement is weaker and noisier, as expected from n=23: pairwise
Pearson r ranges 0.09–0.80, with Rosetta↔FoldX highest (0.80) and DDMut↔RSALOR lowest (0.09).

---

## 8. Suspicious and outlier behaviour

This is the section worth reading twice.

### 8.1 The proline catastrophe in Rosetta — real, large, and method-specific

| target residue | n | Rosetta ΔΔG<−10 (%) | FoldX ΔΔG>+10 (%) | ThermoMPNN ΔΔG>+10 (%) |
|---|---|---|---|---|
| **P** | 1081.0 | 92.5 | 2.4 | 0.0 |
| **W** | 1118.0 | 46.2 | 13.3 | 0.0 |
| **I** | 1056.0 | 45.4 | 1.4 | 0.0 |
| **Y** | 1083.0 | 44.6 | 10.4 | 0.0 |
| **F** | 1078.0 | 43.9 | 6.6 | 0.0 |
| **V** | 1076.0 | 38.6 | 0.8 | 0.0 |
| **R** | 1072.0 | 33.2 | 5.0 | 0.0 |
| **K** | 1053.0 | 32.6 | 2.2 | 0.0 |
| **L** | 1023.0 | 32.3 | 1.1 | 0.0 |
| **H** | 1099.0 | 31.4 | 6.6 | 0.0 |

X→P: Rosetta median **−215.1 REU**, FoldX **+3.41**, ThermoMPNN **+2.03**. Both other methods call
proline substitution mildly destabilising, which is right. Rosetta calls it a two-hundred-unit
collapse. Mutating to proline removes a backbone amide and constrains φ; if the protocol does not
rebuild the backbone, the result is a geometry violation rather than a thermodynamic quantity.

**The aromatic part of the tail is partly shared and therefore partly real.** W (46.2% Rosetta /
13.3% FoldX), Y (44.6 / 10.4) and F (43.9 / 6.6) are elevated in both — burying a large aromatic
genuinely does cost something. Proline is elevated in Rosetta *only*. Treat the aromatic tail as
signal with an inflated scale, and the proline tail as artefact.

### 8.2 `cart_bonded` dominates my own cartesian_ddg at packed positions

| variant | ΔΔG (REU) | Δcart_bonded | fraction |
|---|--:|--:|--:|
| V625F | +58.55 | +48.67 | **83%** |
| V578I | +3.31 | +2.51 | 76% |

Both are flagged and excluded. Cause: `MutateResidue` places a side chain against a
Cartesian-relaxed (hence non-ideal) backbone; if the MoveMap frees backbone DOFs only at i±1 the
strain cannot relax. Widening the minimisation shell to 10 Å with backbone and side-chain DOFs free
fixed it everywhere except V625F — a Val→Phe at **0% RSA**, the most tightly packed site in the set.

**What not to do about it:** substituting a ramped-repulsion FastRelax makes it *worse*, because
FastRelax is stochastic and relaxes wild type and mutant into different local minima. V617F went
from +3.22 to +31.75 REU, at 340 s/variant instead of 4 s. The pack+minimise protocol as reported is
**deterministic — SD = 0.00 REU over 6 repeats with free random seeds** — so its errors are
systematic and diagnosable rather than noise. That is a better property than a smaller error.

### 8.3 `rosetta_delta` does not reproduce between two runs of the same protein

`ddg_JAK2P1_all.json` and `ddg_JAK2P2_all.json` are both complete JAK2 saturation scans
(21,508 = 19 × 1,132), so they compare variant by variant:

| set | n | Pearson r | Spearman ρ | median abs diff | **sign agreement** |
|---|--:|--:|--:|--:|--:|
| all paired rows | 21,508 | +0.074 | +0.155 | 1.39 | **55.4%** |
| after \|single-state\| < 15 filter | 15,396 | +0.295 | +0.172 | 0.78 | **55.2%** |

Filtering improves the correlation but **not the sign agreement at all**. Per-variant `delta` values
are not usable. The mean difference is near zero (−0.005 filtered), so aggregate statistics over
thousands of variants may still carry signal.

*Unresolved:* this directory does not document what P1 and P2 denote. If they are two different
open/closed structure pairs, `delta` is acutely pair-sensitive; if they are repeats of the same
pair, it is irreproducible. Both argue against per-variant use but imply different fixes.

### 8.4 Sign conventions are the most common error in this field, including mine

Three conventions are in play in this repository simultaneously:

| source | convention |
|---|---|
| ThermoMPNN, FoldX/ProtVar, my `cartesian_ddg` | **positive = destabilising** |
| mCSM-Stability, DDMut | **negative = destabilising** (negated on import here) |
| the dual-state Rosetta files in `data/ddg/` | **negative = destabilising** (ΔΔG = ΔG_WT − ΔG_mut) |

`DDG_COMPUTATION_REPORT.md` records that scoring with the wrong sign flips AUC against the JAK1
clusters from 0.26 to 0.74, and that the mistake had been made twice. I then made it a third time in
the opposite direction, briefly mis-reading the correct negative median of the dual-state files as
evidence of contamination; corrected in [`../rosetta_dualstate_qc.md`](../rosetta_dualstate_qc.md).
**Always fix the convention empirically** — check that buried hydrophobic→charged substitutions and
helix prolines come out destabilising — rather than trusting documentation.

### 8.5 Antisymmetry: both learned methods fail it, in the same direction

Thermodynamics requires ΔΔG(A→B) = −ΔΔG(B→A). Measured on Ssym's 341 matched pairs:

| method | mean δ | SD | median \|δ\| | direct → inverse Pearson |
|---|--:|--:|--:|---|
| experimental control | 0.000 | — | — | r = **−1.000** (exact) |
| ThermoMPNN | **+0.689** | 0.667 | 0.497 | 0.729 → 0.603 |
| RaSP | **+1.626** | 1.507 | 1.314 | 0.649 → **0.189** (collapses) |

Both predict "destabilising" in *both* directions. Below ±0.69 kcal/mol the **sign** of a ThermoMPNN
prediction carries no information. RaSP's inverse-direction correlation collapsing to 0.189 is the
more serious failure.

### 8.6 Consensus averaging makes things worse

On 386 held-out human measurements (FireProtDB, homology-filtered, 23 proteins):
ThermoMPNN alone **r = 0.517** > ThermoMPNN+FoldX 0.509 > all three 0.489. The predictors agree with
each other (r 0.583–0.702) more than any of them agrees with experiment (mean 0.424), so averaging
reinforces shared bias. **A "Cross-Tool Mean" column would be worse than its best member** — which
is why this survey does not provide one.

### 8.7 Things that look like outliers but are not

- **ThermoMPNN's range is genuinely narrow**, −2.84 to +4.75, with **zero** values beyond |10|.
  Apparent spikes at the edges of the histogram are an artefact of my 0.5/99.5-percentile clipping,
  not a model ceiling. Checked explicitly before writing this.
- **FoldX's long right tail is real but small**: max +69.53, 157 of 20,349 rows above +20 (0.77%).
- **RSALOR's bimodality** reflects the RSA scaling, not a bug: buried positions get a weight near 1
  and exposed positions near 0, so the distribution piles up at both ends.

---

## 9. Known limitations of this survey

1. **The RSALOR alignment is shallow.** 902 sequences from the UniRef50 clusters of all four JAK
   kinases, but **Neff = 30.2** — the clusters are nearly all vertebrate orthologues above 80%
   identity. Adding the three paralogues raised Neff only from 23.9 to 30.2. The EBI HMMER service
   returns 405 to POST, and a proper jackhmmer/HHblits run needs a ~25 GB database not available
   here. Treat LOR values as indicative.
2. **Rosetta used two constructs, not the full protein.** FERM-SH2 (20–497) and JH2-JH1 (545–1132);
   full-length 20× relax was not affordable. The other five methods used the full-length AlphaFold
   model, so Rosetta's structural context differs.
3. **FoldX was not run here** — those are EBI's precomputed values on AlphaFold models.
4. **n = 23** for everything variant-specific. Correlations on that set have wide intervals.
5. **No experimental ΔΔG exists for these variants**, so none of this is validated against ground
   truth for JAK2 specifically. The ±1.47 RMSE is transferred from 386 held-out human measurements
   on *other* proteins.

---

## 10. Interpretation floors — which threshold answers which question

| threshold | value | use it to decide | flags |
|---|--:|---|--:|
| experimental noise floor | ±0.50 kcal/mol | is the value distinguishable from no effect? | 16/23 on ≥1 method |
| ThermoMPNN antisymmetry bias | ±0.69 kcal/mol | does the **sign** mean anything? | 15/23 |
| per-variant random error (RMSE) | ±1.47 kcal/mol | is a **difference between two variants** real? | 21/23 |

The accuracy ceiling is not a tooling problem: the theoretical limit from experimental noise is
r ≈ 0.70–0.80, and the best independent assessments reach 0.22–0.53 on genuinely unseen mutations.
ThermoMPNN's 0.517 here is near the top of that observed band.

**ΔΔG is a weak pathogenicity classifier** (best reported AUC ≈ 0.66) and is *characteristically*
mild for gain-of-function and dominant-negative variants — which is exactly this set. These numbers
describe folding stability only and must not be used to rank pathogenicity.

---

## 11. The variant table

| variant | # | group | domain | RSA% | ThermoMPNN | FoldX | mCSM | DDMut | Rosetta | RSALOR |
|---|--:|---|---|--:|--:|--:|--:|--:|--:|--:|
| **T108A** | 1 | GOF | FERM | 47.1 | +0.33 | +0.32 | +0.62 | +0.45 | +0.52 | -0.37 |
| **Y317H** | 2 | GOF | FERM | 12.6 | +1.68 | +2.61 | +1.19 | +2.72 | +3.47 | +3.81 |
| **H345L** | 3 | GOF | FERM | 9.5 | +0.32 | -1.09 | +0.43 | +1.28 | -2.40 | +5.65 |
| **H608N** | 4 | GOF | Protein kinase 1 | 1.5 | +0.96 | +1.33 | +2.11 | +1.46 | +1.05 | +10.40 |
| **L611S** | 5 | GOF | Protein kinase 1 | 60.0 | +0.20 | +1.00 | +1.48 | +1.07 | +3.31 | +5.98 |
| **V617I** | 6 | GOF | Protein kinase 1 | 44.3 | -0.07 | -0.95 | +0.55 | +0.05 | +0.10 | +2.79 |
| **V617F** | 7 | GOF | Protein kinase 1 | 44.3 | +0.43 | +0.64 | +1.05 | +0.09 | +3.22 | +5.14 |
| **V625F** | 8 | GOF | Protein kinase 1 | 0.0 | +1.42 | +5.33 | +1.43 | +2.24 | +58.55 | +10.69 |
| **E846D** | 9 | GOF | - | 21.1 | +1.39 | -0.76 | +1.15 | +0.29 | -0.42 | +7.42 |
| **R867Q** | 10 | GOF | Protein kinase 2 | 30.6 | +0.47 | +0.64 | +1.37 | -0.44 | -1.58 | +7.58 |
| **T875N** | 11 | GOF | Protein kinase 2 | 79.8 | +0.34 | -0.30 | +0.10 | -0.02 | +1.16 | +3.78 |
| **S755R** | 13 | GOF | Protein kinase 1 | 41.1 | -0.25 | -0.82 | +0.25 | -0.06 | +0.30 | +3.66 |
| **R938Q** | 14 | GOF | Protein kinase 2 | 48.8 | +0.17 | +1.15 | +0.84 | +0.11 | +1.67 | +4.87 |
| **R1063H** | 15 | GOF | Protein kinase 2 | 70.8 | +0.99 | +1.04 | +0.96 | +0.65 | +2.08 | +2.03 |
| **P37A** | 16 | this study | FERM | 30.9 | -0.09 | — | +0.93 | +0.13 | -0.83 | +0.43 |
| **F240V** | 17 | this study | FERM | 55.2 | +0.68 | +0.98 | +1.32 | +1.62 | +0.98 | +2.61 |
| **H380Y** | 18 | this study | FERM | 17.7 | -0.07 | -0.91 | -1.13 | -0.79 | -1.94 | +3.98 |
| **C427R** | 20 | this study | SH2; atypical | 19.4 | -0.40 | +0.70 | +1.44 | +0.71 | +1.70 | +1.62 |
| **G571R** | 21 | this study | Protein kinase 1 | 73.9 | +1.15 | +2.44 | +0.35 | -0.05 | +3.65 | +3.79 |
| **V578I** | 22 | this study | Protein kinase 1 | 0.0 | +1.03 | +0.94 | +0.76 | +0.51 | +3.31 | +11.02 |
| **L805I** | 23 | this study | Protein kinase 1 | 0.0 | +0.19 | +0.50 | +0.92 | +0.46 | +3.28 | +4.28 |
| **I1065T** | 24 | this study | Protein kinase 2 | 3.8 | +2.32 | +3.15 | +2.06 | +0.82 | +10.13 | +6.46 |
| **V1110E** | 25 | this study | Protein kinase 2 | 40.9 | +0.21 | -0.49 | +1.07 | +0.98 | +0.26 | +3.16 |


`R426X` is a nonsense variant — no folded mutant state, ΔΔG undefined. `R755S` has a wild-type
mismatch: position 755 is **S** in O60674, not R (nearest Arg at 761/769, no isoform shifts the
numbering, and PubMed has 0 hits for "JAK2 R755S" against 1 for "S755R", PMID 24398328). The
transposed reading S755R is scored and both are kept.

---

## 12. Files here

| file | what |
|---|---|
| `ddg_review_claudesci.md` | this document |
| `ddg_review_claudesci.html` | same content with the four figures inline |
| `figs/histograms.png` | distribution of each method over the full saturation scan |
| `figs/correlations.png` | Spearman matrix, 20,349 complete rows |
| `figs/outliers_by_residue.png` | the proline/aromatic tail by target residue |
| `figs/selected_percentile.png` | where the 24 variants sit in JAK2's own distribution |
| `build_survey.py` | regenerates every number and figure above |

Source data, all elsewhere in the repo: [`../jak2_variants_multimethod.csv`](../jak2_variants_multimethod.csv)
(the six-method table), [`../jak2_rosetta_cartesian.csv`](../jak2_rosetta_cartesian.csv) (per-variant
energies with `cart_bonded` diagnostics), [`../survey/jak2_methods.csv`](../survey/jak2_methods.csv)
(full saturation), [`../rosetta_dualstate_qc.md`](../rosetta_dualstate_qc.md) (the dual-state audit).
