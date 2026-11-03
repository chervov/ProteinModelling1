# JAK2 full-length models: the open/closed pairs for the dual-state ΔΔG

Five full-length JAK2 models (UniProt O60674, 1,132 aa), assembled 3 November 2026 so the
dual-state ΔΔG work has a fixed, documented starting point instead of a path into `JAK2/runs/`.

| directory | contents |
|---|---|
| [`pair1/`](pair1/) | **the recommended pair** — closed and open from one untemplated run, `JAK2_20261015_161033` |
| [`pair2/`](pair2/) | the templated pair — closed from `JAK2_20261015_082903`, open from `JAK2_20261014_095758` |
| [`AFmodel/`](AFmodel/) | AlphaFold DB `AF-O60674-F1` v6, downloaded from EBI, **with its PAE matrix** |

3D views: **[`jak2_models_3d.html`](jak2_models_3d.html)** — one self-contained file, 3.2 MB.
Cα cartoon traces via 3Dmol.js with domain/pLDDT toggles, a JH2-superposed open-vs-closed overlay,
the static figures, and every table below.
All numbers below come from [`analyse_models.py`](analyse_models.py) → `model_analysis.json`.

---

## 1. Why these five, and the one thing to know first

`../../open_close/jak2_open_closed_inventory.md` measured all 71 JAK2 structures in the repo and
found 16 wild-type closed models. **Filenames are unreliable — 41 of 71 are mislabelled**, because
guided-recycling selection used the JH2–JH1 centroid distance, which barely moves between states.
Everything here was re-measured and the filenames in this directory were renamed to match the
measurement, not the original label.

**Pair 1 is recommended** because both states come from a *single untemplated run*: `model_1`,
MSA 512/8192, 15 recycles, seeds 5–15, wild-type, `template_source: null`. Nothing differs between
its two structures except the conformation — not the MSA, not the hyperparameters, not the seed
sweep. And because it had no template, its closed state is something AlphaFold found from
sequence rather than something it was handed.

**Pair 2 is the control.** Its two runs share seeds 0–4, 15 recycles, `model_1` and default MSA
settings, and differ *only* in the template: `ma-l9b1f` (the JAK1 closed model renumbered onto
JAK2) for the closed one, `AF-O60674-F1` for the open one.

---

## 2. Selected centroid distances — the conformational summary

Cα centroid distances in Å. Domain boundaries as used throughout the project:
FERM 37–380, SH2 401–482, JH2 545–809, JH1 849–1124.

| model | JH2–JH1 | **FERM–JH1** | SH2–JH1 | JH1 vs Shan¹ | state |
|---|--:|--:|--:|--:|---|
| Pair 1 closed | 39.3 | 44.8 | 54.2 | 6.8 | **closed** |
| Pair 1 open | 46.4 | 95.3 | 78.9 | 83.3 | **open** |
| Pair 2 closed | 39.0 | 45.0 | 53.6 | 6.0 | **closed** |
| Pair 2 open | 45.8 | 93.6 | 78.0 | 83.3 | **open** |
| AlphaFold DB v6 | 45.9 | 93.8 | 78.3 | 83.5 | **open** |

¹ JH1 Cα RMSD to Shan 2014's JAK2 model after superposing JH2 — the measure that says *which*
closed state, not merely "compact".

**Note how badly JH2–JH1 performs**: 39 Å closed against 46 Å open, a 7 Å spread, while FERM–JH1
separates 45 from 94. That 7 Å gap is the entire reason 41 files in `JAK2/runs/` are mislabelled.

---

## 3. All pairwise domain-centroid distances

All six pairs, Å.

| model | FERM–SH2 | FERM–JH2 | FERM–JH1 | SH2–JH2 | SH2–JH1 | JH2–JH1 |
|---|--:|--:|--:|--:|--:|--:|
| Pair 1 closed | 35.8 | 49.0 | 44.8 | 39.8 | 54.2 | 39.3 |
| Pair 1 open | 35.8 | 49.0 | 95.3 | 39.8 | 78.9 | 46.4 |
| Pair 2 closed | 35.8 | 48.9 | 45.0 | 39.6 | 53.6 | 39.0 |
| Pair 2 open | 35.7 | 47.9 | 93.6 | 39.4 | 78.0 | 45.8 |
| AlphaFold DB v6 | 35.9 | 48.1 | 93.8 | 39.7 | 78.3 | 45.9 |

**Only the three JH1 columns change.** FERM–SH2 is 35.7–35.9 in every model, SH2–JH2 is 39.4–39.8,
FERM–JH2 is 47.9–49.0. The open→closed transition moves JH1 and nothing else: the FERM–SH2–JH2
module is a rigid body in all five structures. This is a useful constraint for the ΔΔG work —
a mutation outside JH1 and outside the JH1 contact surfaces cannot have a ΔΔG difference between
states for any geometric reason, so a large |ΔΔG_open − ΔΔG_closed| at such a position is a
red flag about the calculation, not a discovery.

---

## 4. Mutual superposition — how different are they really?

Cα RMSD in Å. "Global" fits all shared residues; "JH1 | JH2 fit" superposes JH2 only and then
measures JH1, isolating the arrangement; the per-domain columns fit each domain to itself.

| A | B | global | JH1 \| JH2 fit | FERM | SH2 | JH2 | JH1 |
|---|---|--:|--:|--:|--:|--:|--:|
| Pair 1 closed | Pair 1 open | 31.94 | 81.91 | 0.41 | 0.10 | 0.37 | 0.54 |
| Pair 1 closed | Pair 2 closed | **6.90** | **1.53** | 0.21 | 0.10 | 0.29 | 0.21 |
| Pair 1 closed | Pair 2 open | 32.71 | 81.90 | 0.58 | 0.21 | 0.36 | 0.53 |
| Pair 1 closed | AlphaFold DB v6 | 32.79 | 82.10 | 0.56 | 0.21 | 0.34 | 0.54 |
| Pair 1 open | Pair 2 closed | 31.89 | 81.30 | 0.42 | 0.11 | 0.40 | 0.43 |
| Pair 1 open | Pair 2 open | **7.64** | **1.58** | 0.66 | 0.25 | 0.21 | 0.34 |
| Pair 1 open | AlphaFold DB v6 | **7.67** | **1.89** | 0.64 | 0.25 | 0.20 | 0.34 |
| Pair 2 closed | Pair 2 open | 31.57 | 81.30 | 0.59 | 0.22 | 0.37 | 0.47 |
| Pair 2 closed | AlphaFold DB v6 | 31.66 | 81.50 | 0.55 | 0.21 | 0.36 | 0.48 |
| Pair 2 open | AlphaFold DB v6 | **0.33** | **0.50** | 0.20 | 0.11 | 0.13 | 0.18 |

Four things fall out of this table.

**The domains are rigid.** Every per-domain RMSD is **0.10–0.66 Å** — at or below coordinate
noise — across models that differ by 32 Å globally. There is no internal rearrangement anywhere;
the open/closed difference is entirely the placement of JH1. SH2 is the most invariant at
0.10–0.25 Å.

**The two closed models agree: 1.53 Å** JH1 displacement between pair 1 (no template) and pair 2
(built from the mapped JAK1 closed template). An untemplated prediction and a template-driven one
converge on the same closed arrangement to within 1.5 Å. That is the strongest evidence here that
the closed state is real and not an artefact of the template.

**The two open models agree too** — 1.58 Å, and 1.89 Å against AFDB.

**Pair 2's open model is not independent evidence.** It sits **0.33 Å** from the AlphaFold DB
model it was templated on. The run reproduced its own template. Use it as a control on the
*closed* side of pair 2, and do not count it as a second opinion about the open state.

---

## 5. Confidence

| model | template | pLDDT | FERM | SH2 | JH2 | JH1 |
|---|---|--:|--:|--:|--:|--:|
| Pair 1 closed | none (MSA only) | 85.3 | 87.6 | 92.0 | 90.7 | 89.6 |
| Pair 1 open | none (MSA only) | 86.3 | 88.3 | 91.9 | 91.5 | 91.0 |
| Pair 2 closed | ma-l9b1f (JAK1 closed, mapped) | 85.6 | 87.8 | 92.2 | 91.0 | 89.5 |
| Pair 2 open | AF2 AF-O60674-F1 | 94.8 | 95.8 | 97.0 | 97.1 | 95.9 |
| AlphaFold DB v6 | n/a | 86.9 | 88.7 | 93.7 | 92.1 | 91.8 |

Pair 2 open's 94.8 is **not** a sign it is the best model. It is 0.33 Å from its own template, and
15 recycles against a template inflate pLDDT by agreement with that template. The honest reading
is that all five are ~85–93 inside domains, with the whole-chain means dragged down by the
inter-domain linkers.

### The PAE problem, now quantified

Our OpenFold runs use `config_preset: model_1`, which emits no PAE, so there is no direct measure
of confidence in *where JH1 sits* — exactly the quantity the dual-state feature depends on. The
AlphaFold DB download includes PAE, and it is sobering. Mean PAE per block, Å (ceiling 31.0):

| block | mean PAE |
|---|--:|
| FERM–FERM | 5.4 |
| SH2–SH2 | 2.4 |
| JH2–JH2 | 4.5 |
| JH1–JH1 | 5.3 |
| FERM–SH2 | 7.4 |
| SH2–JH2 | 8.6 |
| FERM–JH2 | 12.3 |
| JH2–JH1 | 14.6 |
| SH2–JH1 | 19.6 |
| **FERM–JH1** | **21.0** |

Within domains AlphaFold is confident (2.4–5.4 Å). **Between FERM and JH1 it is at 21.0 Å, 68% of
the way to the 31 Å ceiling** — which means the model has essentially no idea where JH1 sits
relative to FERM. The open arrangement in the AFDB model is a low-confidence guess, and the
FERM–SH2–JH2 module being rigid across all five models is consistent with that: the network is
confident about the module and unconfident about the one thing that distinguishes open from
closed.

This does not invalidate the dual-state ΔΔG, because ΔΔG is local (it depends on each residue's
own neighbourhood) and the domains themselves are confidently modelled. It does mean the
**interface** residues — where the ΔΔG difference between states actually comes from — sit in the
least certain part of the model. Interface positions should carry that caveat explicitly.

---

## 6. Recommended use

```
closed : pair1/jak2_pair1_closed_untemplated.pdb
open   : pair1/jak2_pair1_open_untemplated.pdb
control: pair2/jak2_pair2_closed_tmpl_ma-l9b1f.pdb   (1.53 A from pair 1 closed)
```

If ΔΔG_closed shifts materially between `pair1` and `pair2` closed models that are 1.53 Å apart,
the feature is reporting on the model rather than on the protein.

### Known limitations
- **No PAE for pair 1 or pair 2.** `model_1_ptm` would provide it; a re-prediction is the clean fix.
- **One structure per state, not an ensemble.** ΔΔG from a single conformer understates the real
  uncertainty.
- **OpenFold guided-recycling outputs**, selected per recycle, not vanilla predictions.
- **Shan's JAK2 covers only 520–1131** (JH2–JH1), so it validates the JH1 placement but cannot
  confirm the FERM arrangement in the closed models. Nothing experimental does, for full-length JAK2.

## Files

| file | what |
|---|---|
| `analyse_models.py` | all the geometry: centroids, superpositions, PAE blocks → `model_analysis.json` |
| `build_3d.py` | builds the 3Dmol viewer from that JSON |
| `plot_models.py` | the static matplotlib views → `figs/*.png` |
| `jak2_models_3d.html` | the viewer, **3.2 MB, self-contained** |
| `figs/*.png` | the four static figures, also embedded in the html |
| `model_analysis.json` | every number on this page, machine-readable |

### The viewer: 3Dmol.js, inlined

Built on **3Dmol.js**, the same library as `more_proteins/top10/*.html`, so the structural pages
in this repository all behave the same way: cartoon trace, click to toggle domain or pLDDT
colouring, drag to rotate. 3Dmol is **inlined** (0.5 MB), as are all four PNGs — **copy the file
anywhere and it still works**, with no network, no sibling directory and no CDN.

It took three attempts to get there, which is worth recording:

1. **Plotly from cdnjs pinned at `plotly.js/2.35.2`** — a version that *does not exist on cdnjs*
   (their mirror stops earlier). The page rendered blank with nothing but a console error.
2. **A vendored Plotly referenced by relative path** — which broke the moment the html was copied
   somewhere on its own, which is the normal way to share it. A page whose purpose is to be passed
   around must not have a sibling dependency.
3. **3Dmol inlined** — a real molecular cartoon instead of a line plot, a seventh of Plotly's
   bytes, and consistent with the rest of the repository.

The static PNG section stays for a separate reason: WebGL can be unavailable (headless browsers,
remote desktops, locked-down machines), and the figures and numbers should survive that. Build
with `--link-lib` for the small CDN-linked version instead. `vendor/` is only a build-time cache,
fetched on demand and gitignored.

The superposition for panel 2 is computed in `build_3d.py` with numpy and the fitted coordinates
are inlined. An earlier version did the Kabsch fit in JavaScript in the browser; that is exactly
the kind of code that returns a plausible-looking wrong rotation without failing, so it was moved
to where the maths is already verified. The JH2 fit RMSD is 0.37 Å over 265 residues.

## Reproduce

```bash
python3 analyse_models.py     # -> model_analysis.json, prints every table above
python3 build_3d.py           # -> jak2_models_3d.html
open jak2_models_3d.html
```
