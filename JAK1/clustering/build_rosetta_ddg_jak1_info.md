# The paper's three dual-state PyRosetta ΔΔG features for JAK1 — complete, 100%

Covers [`jak1_ddg_rosetta_dualstate.csv`](jak1_ddg_rosetta_dualstate.csv). Written 2 November 2026.

> Where the numbers came from: [`ddg_rosetta_computations.md`](ddg_rosetta_computations.md), and in full
> [`data/ddg/DDG_COMPUTATION_REPORT.md`](../../data/ddg/DDG_COMPUTATION_REPORT.md).

**Correction first.** Earlier notes in this directory said these features existed for only 500
variants (2.3%). That was wrong: it described the *test subset* in
`data/orianne/jak1_cluster_ddg.json`, used for the section-56 comparison against the paper's
clusters. The complete saturation has been in the repository since 22 October.

---

## 1. Source and provenance

| | |
|---|---|
| file | [`../../data/ddg/ddg_JAK1_all.json`](../../data/ddg/ddg_JAK1_all.json) |
| contents | **21,926 variants, all 1,154 positions — complete JAK1 saturation** |
| records | `{pos, wt, alt, ddg_closed, ddg_open, delta}` |
| computed | overnight run **2026-10-22**, four molab CPU boxes (20 cores, 172 GB each) |
| **structures** | **Jeanpierre's own open and closed JAK1 models** (`RUNBOOK.md`) |
| method | PyRosetta, FastRelax with coordinate constraints per structure, `mutate_residue(pack_radius=8.0)`, wild-type repacked identically |

So this is **the paper's own quantity computed on the paper's own structures** — the most faithful
feature in this directory, and the only one that did not have to be substituted or approximated.

The protocol was verified against PyRosetta's published ddG tutorial (PagP set) to four decimals:
0.3590 against their 0.3590768, and 0.6712 against their 0.6720891 excluding proline
(`pipeline/ddg/README.md`).

## 2. Sign convention — and `delta` is not a stability measure

**ΔΔG = ΔG_WT − ΔG_mut, so negative = destabilising.** This is the *opposite* of FoldX in
[`jak1_ddg_foldx_precomputed.csv`](jak1_ddg_foldx_precomputed.csv), where positive = destabilising.
Two stability features on opposite axes is invisible to a Gower distance and will quietly degrade
it.

From the paper's Appendix S3:

> ddG_open,m > ddG_closed,m corresponds to stronger stabilization (or weaker destabilization) of the
> open versus closed state, **leading to more open configurations in mutants**.

So **`delta = ddg_open − ddg_closed` is a conformational-preference estimate, not a stability
change.** It asks "does this mutation favour the open state?" — arguably the better question for a
gain-of-function hypothesis, and the distinctive component of the paper's pipeline. It must **not**
be pooled with FoldX or ThermoMPNN single-state ΔΔG.

## 3. The values are contaminated by steric clashes — read `within_15`

| | |
|---|--:|
| median `ddg_closed` | **−3.79** |
| \|ddG\| > 10 | **27.8%** |
| \|ddG\| > 100 | **11.0%** |
| minimum | **−2,935.51** |

A median of −3.79 is wrong on its face: most random substitutions destabilise, so under this sign
convention the median should sit near −1 at most, and −2,935 kcal/mol is not an energy at all.

The cause is established, not suspected. `clash_diagnosis.json` shows `frac_rep ≈ 1.0` — essentially
the entire difference is `fa_rep`, repulsive van der Waals from a side chain inserted without
backbone relaxation. `kellogg_ddg_monomer.json` confirms it with Rosetta's own `ddg_monomer`, which
returns the same magnitudes. **40% of JAK1 Gly→{W,F,Y,R,K} substitutions exceed 100 kcal/mol**, while
ordinary substitutions come out textbook. Full diagnosis:
[`../../conclusions_ddG_difference_feature.md`](../../conclusions_ddG_difference_feature.md) §§8–10.

**`within_15` is 1 where both single-state values satisfy |ΔΔG| < 15**, the window
`data/ddg/rosetta_dualstate_qc.md` uses. **16,298 of 21,926 (74.3%)** qualify — matching the QC
note's 74.3% exactly, an independent check that this file reproduces it.

| | full set | `within_15 == 1` |
|---|--:|--:|
| `ddg_closed` median | −3.786 | **−2.497** (SD 3.733) |
| `ddg_open` median | −3.979 | **−2.611** (SD 3.561) |
| `delta` median | −0.014 | **−0.011** (SD 2.420) |

Even restricted, the median of −2.5 is more destabilising than a relaxed protocol would give, so
**rank these values; do not read them as kcal/mol.** That is what the project concluded and what
`pipeline/ddg/README.md` already said: *"only the ordering is meaningful."*

## 4. What `delta` is worth — tested, and the answer is nothing

`data/orianne/jak1_cluster_auc.json` scores each feature against the paper's EV1 clusters:

| feature | AUC | p |
|---|--:|--:|
| ddg_closed | 0.770 | 6e−26 |
| ddg_open | 0.767 | 2e−25 |
| **`delta` (ddg_open − ddg_closed)** | **0.5035** | **0.89** |

AUC 0.50 at p = 0.89 is a coin flip. The two single states carry real signal; **their difference —
the paper's distinctive feature — carries none.** Consistent with the two states correlating at
Spearman 0.855: they are nearly the same measurement, so differencing them leaves mostly noise.

Keep the column, because reproducing the paper means including it. But it should not be expected to
contribute, and if the rebuilt clustering diverges from the paper's, this is one of the first places
to look.

## 5. The file

```csv
variant_id,wt,pos,alt,cluster,ddg_closed,ddg_open,delta,within_15
```

23,080 rows, EV1 order, conventions as in the [README](README.md).

| | n |
|---|--:|
| populated | **21,926 (100% of real substitutions)** |
| `within_15 = 1` | **16,298 (74.3%)** |
| `within_15 = 0` | 5,628 |
| blank | 1,154 (the self-substitutions) |

The paper clipped these values to **[−10, 10]**; `within_15` is a slightly wider window, so clipping
to the paper's range is still available from the raw columns. Clipping was the right instinct —
unclipped, three features reaching −2,935 would dominate any distance that included them.
