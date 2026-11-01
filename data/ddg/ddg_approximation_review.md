# Review of `ddg_approximation.md` — do not use this model for ranking

*1 November 2026. Reviewed [`ddg_approximation.md`](ddg_approximation.md) and
[`ddg_approximator.py`](ddg_approximator.py) by reimplementing `compute_ddg` independently and
testing it against the methods already in this repository. The `.py` and the code block in the
`.md` are substantively identical (same constants, same omissions), so both are covered here.*

**Verdict: the document's validation section is not reproducible, the model cannot express half of
its own defined output range, and it carries no stability information measurable against four
established methods. It should not be used to rank or prioritise variants.**

Nothing in the repository currently depends on it — see §5.

---

## 1. Section 5 was not produced by the code in section 4

§5 states *"When executed, the approximation model yields the following values."* It does not.
Running the logic in §4 with the harness's own arguments from §4's `test_variants`:

| variant | §5 claims | code gives | component breakdown from the code |
|---|--:|--:|---|
| V617F | 3.0 | **3.00** | steric 3.00 — the only match |
| G571R | 3.4 | **8.83** | steric 7.70 + elec 1.14 |
| V1110E | 2.9 | **2.31** | cavity 0.03 + elec 2.28 |
| F240V | 2.6 | **2.24** | cavity 2.24 |
| V578I | 0.3 | **0.40** | steric 0.40 (after the V/I/L clamp) |
| L805I | 0.7 | **0.00** | all terms zero |
| R938Q | 3.2 | **5.06** | cavity 1.66 + elec 3.41 |
| P37A | 1.4 | **1.68** | cavity 0.23 + backbone 1.45 |

**One of eight.** Two cases show the numbers were written rather than computed:

- **G571R.** §5 breaks it down as "ΔΔG_Gly = 2.42, ΔΔG_steric = 0.98". The code computes steric as
  `0.040 × 164.9 × 0.8 = 7.70`, and additionally adds 1.14 kcal/mol of electrostatics for inserting
  an arginine charge at `burial_index = 0.8`, a term the breakdown omits entirely.
- **L805I.** §5 reports +0.7 "mitigated by rotamer repacking". Leu and Ile have identical volumes in
  the parameter table (166.7 Å³ both), so `delta_v = 0`, neither the steric nor the cavity branch
  fires, and the result is exactly 0.00. The V/I/L clamp that the note credits never executes.

A validation section that does not reproduce is worse than no validation section, because it
transfers unearned confidence.

## 2. The model cannot predict a stabilising mutation

§1 defines the sign convention including "ΔΔG < 0: Stabilizing". Every component in the
implementation is non-negative by construction, so the sum cannot be. Enumerating all 380 ordered
substitutions × 5 burial levels:

```
1,900 combinations evaluated -> 0 negative, minimum exactly 0.00
```

Experimentally, a minority but non-trivial fraction of substitutions are stabilising, and both
structural methods already in this repository produce negative values on these very variants
(FoldX: V1110E −0.49; ThermoMPNN: P37A −0.09). A predictor that cannot represent stabilisation is
not approximating ΔΔG; it is scoring "how unusual is this substitution".

## 3. It carries no stability information against four established methods

[`jak2_variants_multimethod.csv`](jak2_variants_multimethod.csv) already holds ThermoMPNN, FoldX,
mCSM-Stability and DDMut values plus `rsa_pct` for a set of JAK2 variants. Setting
`burial_index = 1 − RSA/100` and leaving the hand flags off — the only defensible automated use, as
the flags are not derivable from a structure — over the 23 variants with all five values:

| approximator vs | Spearman |
|---|--:|
| ThermoMPNN | **−0.12** |
| FoldX | **+0.19** |
| mCSM-Stability | **+0.15** |
| DDMut | **−0.06** |

Zero within noise against all four, including the two methods §1 names as what it approximates. For
context, the repulsive-artefact Rosetta values criticised in
[`conclusions_ddG_difference_feature.md`](../../conclusions_ddG_difference_feature.md) §9 still
preserve rank across a protocol change at Spearman 0.904. The approximator's magnitudes are
inflated (range 0–4.9, mean 1.57 on this set) *and* its ordering is uninformative, which removes the
only property that made the Rosetta numbers usable.

## 4. Why it fails

**It never reads a structure.** The signature is
`compute_ddg(wt, mut, burial_index, is_tight_turn, is_salt_bridge, is_catalytic_core, is_autoinhibitory_switch)`
— two letters and five hand-set booleans. No coordinates, no neighbour list, no PDB. Two different
positions with the same substitution and the same flags receive identical scores. And if a structure
is available to set burial honestly, the real terms can be computed instead.

**The flags used in §5 contradict this repository's own RSA values**, consistently in the direction
that inflates the result:

| variant | §4 harness | `rsa_pct` in this repo |
|---|---|---|
| V617F | burial 0.9 | 44.3 % exposed |
| G571R | burial 0.8, `is_tight_turn=True` | **73.9 % exposed** — a surface residue |
| V1110E | burial 0.9, `is_catalytic_core=True` | 40.9 % exposed |
| V578I | burial 0.85 | **0.0 % — fully buried** |
| L805I | burial 0.50 | **0.0 % — fully buried** |

The three headline values rest on burial assumptions the repository contradicts, and the two
genuinely buried variants were given the lower burial.

**Blind to the physics that decides these cases.** Volume difference cannot see β-branching
(hence L→I = 0), aromatic stacking (one `+1.1` special case aside), hydrogen bonding (see below),
rotamer availability, or conservation.

**Smaller defects**

- The `ddG_hbond` term appears in §2's equation *and in the code's own docstring*, but is never
  implemented. Four terms are summed, not five.
- `total_raw` (line 152 of the `.py`) is computed and discarded.
- The Born expression in §2.3 is decorative. With r ≈ 2 Å it yields tens of kcal/mol, not the quoted
  "+1.2 to +2.0", and the code ignores it regardless, applying a flat 1.42 for any charge and any
  radius.
- The parameter table is headed "Sidechain Volume" but lists Zamyatnin **residue** volumes — glycine
  cannot have a 60.1 Å³ side chain, it has none. Differences remain usable; the label is wrong.
- Volume ordering in that table is scrambled (N = 114.1 after T = 116.1; E = 138.4 after V = 140.0),
  indicating it was not checked.
- `α = 0.040 kcal/mol/Å³` applied to the entire volume difference assumes **zero relaxation**. This
  is the same error, scaled down, that produces the −3000 artefacts diagnosed in
  `conclusions_ddG_difference_feature.md` §§8–10: it treats every added Å³ as overlap.

**Section 6 should be withdrawn.**

- It invokes an "AlphaGenome AVI Phred score". No such output exists. AlphaGenome predicts
  regulatory tracks — expression, splicing, chromatin — from DNA sequence and makes no statement
  about missense effects on a fold. Pairing it with protein ΔΔG for GOF/LOF assignment is a category
  error, whatever the score were called.
- The rule "high ΔΔG in JH2 ⟹ GOF, high ΔΔG in JH1 ⟹ LOF", stated as deterministic, is contradicted
  by measurements already in this repository: in the TYK2 deep mutational scan **every** substitution
  at the JH2 position H667 *reduces* IFN-α signalling, and
  [`external_data/JAK3/jak3_homology_inf.md`](../../external_data/JAK3/jak3_homology_inf.md)
  concludes explicitly that direction cannot be inferred from position plus predicted effect.
  V617F, the archetypal gain of function, is only mildly destabilising by every method here.

**The stated motivation is overstated.** §1 justifies the approximation by "20–45 CPU minutes per
variant for Rosetta". The pipeline in [`../../pipeline/ddg/`](../../pipeline/ddg/) computes the
wild-type repack once per position and reuses it across that position's 19 substitutions, and
completed 22,536 TYK2 variants; the measured cost of Rosetta's own `ddg_monomer` was ~6 min per
variant, and of the repack-only protocol far less.

## 5. Nothing depends on it

Checked every ΔΔG-bearing table in `data/ddg/`:

| file | ΔΔG columns |
|---|---|
| `jak2_variants_ddg.csv` | `thermompnn`, `foldx` |
| `jak2_variants_ddg_inputorder.csv` | `thermompnn`, `foldx` |
| `jak2_variants_multimethod.csv` | `thermompnn`, `foldx`, `mcsm_stability`, `ddmut`, `rsalor_*` |
| `jak2_rosetta_categories.csv` | `thermompnn`, `foldx`, `mcsm_stability`, `ddmut`, `rosetta_category` |
| `ddg_TYK2_all.json`, `ddg_JAK1_all.json` | Rosetta `ddg_closed` / `ddg_open` |

No column anywhere carries approximator output, so no result needs retracting. This review is a
guard against future use, not a correction of past results.

## 6. What is worth keeping

- **The glycine rule is directionally correct**, and independently matches what the Rosetta
  diagnosis found the hard way: buried Gly → bulky is the pathological class.
- **The component decomposition is sound as a teaching frame** — steric, cavity, electrostatic,
  backbone is textbook, and the T4-lysozyme cavity coefficient (~0.024 kcal/mol/Å³, Eriksson &
  Matthews 1992) is a real and correctly cited number.

## 7. Recommendation

1. Keep `ddg_approximation.md` as a record of an approach that was tried and failed its own
   validation. A note at its head points here.
2. Do not use it to rank, prioritise, or assign GOF/LOF. Treat §5 as non-reproducible and §6 as
   withdrawn.
3. For ΔΔG, use what is already here and works: **ThermoMPNN**, **FoldX**, **mCSM-Stability**,
   **DDMut** (free REST API — note the mutation-list format is `<chain> <wt><pos><mut>`, not the
   format its API page documents), and the Rosetta values **as ranks only**.

*Reproduction: the independent reimplementation of `compute_ddg` and the three tests above are in
[`../../pipeline/ddg/check_approximator.ps1`](../../pipeline/ddg/check_approximator.ps1). Run it
with no arguments to print the §5 comparison, the stabilisation enumeration and the four Spearman
coefficients; it needs `jak2_variants_multimethod.csv` and no Python.*
