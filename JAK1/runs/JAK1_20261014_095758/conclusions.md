# JAK1_20261014_095758 — full MSA + AF2 template (AF-P23458-F1)

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0–4, full MSA (OpenFold default depth),
custom template = AlphaFold DB AF-P23458-F1 (`--use_custom_template`). Inference took 69 min (RTX PRO 6000).

## References (JH1 RMSD after superposing JH2, Å)
| | AF2 | ma-a1sai (open) | ma-l9b1f (closed) | Shan 2014 |
|---|---|---|---|---|
| JH2–JH1 / FERM–JH1 (Å) | 46.3 / 92.2 | 46.1 / 92.5 | 39.5 / 40.1 | 38.0 / – |
| vs AF2 | 0 | 3.4 | 81.0 | 82.5 |
| vs ma-a1sai | | 0 | 81.7 | 82.9 |
| vs ma-l9b1f | | | 0 | 11.7 |

AF2 and ma-a1sai are both open and nearly the same (3.4 Å); ma-l9b1f and Shan are both closed (11.7 Å apart).

## Our 75 conformations (5 seeds × 15 recycles)
| | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan |
|---|---|---|---|---|
| closest (Å) | 0.2 | 2.7 | 80.5 | 82.2 |
| selected per seed (Å) | 0.6–0.8 | 3.1–4.0 | 80.7–81.0 | 82.3–82.5 |
| within 15 Å | 75/75 | 75/75 | 0 | 0 |

JH2–JH1 46.1–46.5 Å, FERM–JH1 91.8–92.4 Å, pLDDT 94.5–94.8: **open**.

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
