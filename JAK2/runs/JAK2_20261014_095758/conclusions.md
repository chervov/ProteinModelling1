# JAK2_20261014_095758 — full MSA + AF2 template (AF-O60674-F1)

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0–4, full MSA (OpenFold default depth),
custom template = AlphaFold DB AF-O60674-F1 (`--use_custom_template`). Inference took 61 min (RTX PRO 6000).

## References
AF2 (open): JH2–JH1 45.9 Å, FERM–JH1 93.8 Å. Shan 2014 (closed, JH2–JH1 only): JH2–JH1 40.9 Å.
JH1 RMSD after superposing JH2, AF2 vs Shan: 83.5 Å. (ModelArchive has no JAK2 models.)

## Our 75 conformations (5 seeds × 15 recycles)
| | vs AF2 | vs Shan |
|---|---|---|
| closest (Å) | 0.2 | 83.1 |
| selected per seed (Å) | 0.3–0.6 | 83.2–83.4 |
| within 15 Å | 75/75 | 0 |

JH2–JH1 45.7–46.0 Å, FERM–JH1 93.4–94.0 Å, pLDDT 94.3–94.7: **open**.

## What this means
- **With the AF2 model as a template, the output is just the template.** Already at recycle 1 every
  structure matches the AF2 domain arrangement to within 0.2–0.8 Å (JH1 superposed on JH2), with pLDDT ~94.5–94.8.
  It hardly moves over 15 recycles: across all 75 conformations, JH2–JH1 varies by < 0.5 Å and FERM–JH1 by < 1 Å.
- Guided recycling cannot explore anything here: the "open" and "closed" selections are the same structure,
  so open/closed selection is meaningless in this setup.
- No conformation comes anywhere near the closed references (> 80 Å, the same as the AF2-vs-closed distance).
- The template is so strong that this run cannot show what the full MSA alone does.
  Earlier runs (MSA 32/64, no template) gave closed-like, FERM-bound JH1 with lower pLDDT.

## Suggested next steps
1. Full MSA **without** a template, to separate the MSA effect from the template effect.
2. A closed template (ma-l9b1f, or a full-length model built on Shan) as a control: if the
   output copies that too, the template simply dictates the conformation.
3. A partial template (e.g. JH2+JH1 only, or each domain alone without the interdomain geometry),
   or a template only in the first recycles, so recycling can still move the domains.
