# Master results table (regenerated 2026-10-20 12:16)

Produced by `analysis/all_results.py`. Pulls every run folder, parses the per-seed tables, groups by
(variant, MSA depth, template), deduplicates by seed number, and compares each mutant with the wild type
at the same depth.

## Two metrics, deliberately

**FERM–JH1 centroid distance** — uniform across all four JAKs and independent of which reference columns
a run happened to include. From [reference_states.md](reference_states.md): closed 40–45 Å, active dimer
~84 Å, open 92–94 Å. `compact` counts seeds below 60 Å.

**Arrangement metric** — JH1 RMSD against the **closed** reference after superposing JH2. The column
differs per run, and **its polarity is a trap: the AlphaFold model is OPEN for JAK1/JAK2 but CLOSED for
JAK3/TYK2.** An earlier version of this table used "vs AF2" everywhere and therefore reported the
*opposite* quantity for JAK2. The closed reference is now chosen per run and named in the last column;
where a run contains none, the arrangement columns show `-` rather than a misleading number.

`p(cnt)` Fisher on the compact count · `p(rank)` Mann-Whitney on FERM–JH1 · `p(arr)` Mann-Whitney on the
arrangement metric.

```

========================================================================================================
JAK2   (compact = FERM-JH1 < 60 A; closed-ref column named per group)
========================================================================================================
variant      MSA         tmpl         n |  compact  medFERM  p(cnt) p(rank) |  arr<25  medArr  p(arr) | closed ref
V617F        128/512     none        16 |   7/16       61.3  0.7244  0.4891 |    0/16    65.6  0.0086 | vs Shan 2014
WT           128/512     ma-l9b1f     5 |   5/5        45.3                 |     5/5     3.2         | vs template ma-l9b1f
WT           128/512     pdb:4OLI:A   5 |   5/5        42.0                 |     5/5     7.9         | vs Shan 2014
WT           128/512     none        15 |   8/15       59.8                 |    0/15    85.8         | vs Shan 2014
V617F        256/1024    none        16 |   7/16       94.6  0.0068  0.0060 |     3/8    56.3  0.3765 | vs Shan 2014
WT           256/1024    none        16 |   0/16       94.8                 |     0/5    83.5         | vs Shan 2014
WT           32/64       none        10 |  10/10       45.1                 |       -       -         | NONE
WT           32/64       pdb:4OLI:A   5 |   5/5        41.5                 |     5/5     7.1         | vs Shan 2014
G571R        512/8192    none        16 |   4/16       95.0  0.1489  0.0584 |    3/16    83.3  0.0420 | vs Shan 2014
V617F        512/8192    none        16 |   0/16       95.0  0.0008  0.0404 |       -       -         | NONE
WT           512/8192    none        16 |   9/16       49.6                 |     3/5    19.1         | vs Shan 2014
V617F        64/256      none        16 |   5/16       67.8  0.4725  0.0185 |    0/16    96.0  0.0261 | vs Shan 2014
WT           64/256      none        16 |   8/16       59.4                 |    0/16    92.2         | vs Shan 2014
V617F        96/384      none        16 |  13/16       55.7  0.5489  0.1482 |    1/16    85.2         | vs Shan 2014
WT           96/384      none         5 |   5/5        52.1                 |       -       -         | NONE
WT           None/None   ma-l9b1f     5 |   5/5        44.1                 |     5/5     2.9         | vs template ma-l9b1f
WT           None/None   pdb:4OLI:A   5 |   5/5        43.7                 |     5/5     6.9         | vs Shan 2014

========================================================================================================
JAK3   (compact = FERM-JH1 < 60 A; closed-ref column named per group)
========================================================================================================
variant      MSA         tmpl         n |  compact  medFERM  p(cnt) p(rank) |  arr<25  medArr  p(arr) | closed ref
A572V        128/512     none        16 |  15/16       53.4  1.0000  0.1315 |    1/16    84.3  0.0348 | vs AF2
A573V        128/512     none        16 |  16/16       42.7  1.0000  0.0010 |   12/16     2.7  0.0024 | vs AF2
M511I        128/512     none        16 |  16/16       52.9  1.0000  0.4395 |    7/16    84.8  0.8210 | vs AF2
M592F        128/512     none        16 |  11/16       55.5  0.0434  0.0115 |    1/16    64.0  0.2912 | vs AF2
R657Q        128/512     none        16 |  16/16       51.2  1.0000  0.2064 |    4/16    89.0  0.1315 | vs AF2
WT           128/512     none        16 |  16/16       51.9                 |    7/16    61.5         | vs AF2
Y581C        128/512     none        16 |  13/16       51.7  0.2258  0.1363 |    0/16    88.4  0.0005 | vs AF2
WT           256/1024    none        16 |   1/16       94.0                 |    1/16    82.4         | vs AF2
WT           512/8192    none         8 |   0/8        94.2                 |     0/8    82.3         | vs AF2

========================================================================================================
TYK2   (compact = FERM-JH1 < 60 A; closed-ref column named per group)
========================================================================================================
variant      MSA         tmpl         n |  compact  medFERM  p(cnt) p(rank) |  arr<25  medArr  p(arr) | closed ref
P982A        128/512     none         8 |   0/8        93.1  1.0000  0.0110 |     0/8    82.2  0.5932 | vs AF2
WT           128/512     pdb:4OLI:A  16 |  16/16       39.3                 |   16/16     1.0         | vs AF2
WT           128/512     none         8 |   0/8        93.6                 |     0/8    82.1         | vs AF2
P982A        32/64       none        31 |  31/31       42.5  1.0000  0.1367 |    0/31    44.7  0.1367 | vs AF2
V678F        32/64       none        16 |  16/16       49.9  1.0000  0.0631 |    0/16    51.6  0.3326 | vs AF2
WT           32/64       none        15 |  15/15       45.2                 |    0/15    46.4         | vs AF2
P982A        64/256      none        16 |   3/16       89.5  0.2524  0.2744 |    0/16    88.8  0.3363 | vs AF2
V678F        64/256      none        16 |   0/16       92.6  0.0068  0.0135 |    0/16    93.0  0.0001 | vs AF2
WT           64/256      none        16 |   7/16       80.0                 |    0/16    84.5         | vs AF2
P982A        96/384      none         8 |   0/8        88.1  1.0000  0.0097 |     0/8    82.7  0.7912 | vs AF2
V678F        96/384      none         8 |   0/8        93.3  1.0000  0.1233 |     0/8    82.0  0.0149 | vs AF2
WT           96/384      none         8 |   0/8        93.5                 |     0/8    82.5         | vs AF2

```

## What the corrected table shows

- **JAK2 V617F at 512/8192 — p(cnt) = 0.0008.** Compact 0/16 against wild type 9/16: the mutation
  abolishes the compact state at this depth. At **256/1024 it does the reverse** (7/16 against 0/16,
  p = 0.0068), reproducing the depth-dependent direction reversal documented earlier.
- **TYK2 V678F at 64/256 is now significant on both metrics** — compact 0/16 vs 7/16 (p = 0.0068) and
  arrangement p = 0.0001. The earlier table hid the first of these.
- **JAK3 Y581C: FERM–JH1 says nothing (13/16 compact, p = 0.23) while the arrangement metric says
  p = 0.0005.** The clearest single demonstration that one metric is not enough.
- **JAK2 G571R at 512/8192** trends toward less compact (4/16 vs 9/16) with arrangement p = 0.042 —
  suggestive, not established, and its second comparison baseline is now properly matched at n = 16.
- **TYK2 P982A shows p(rank) = 0.011 and 0.0097 on FERM–JH1 at 128/512 and 96/384** — these are the
  collapsed-variance artefacts described in `mutation_analysis.md` section 15, not real effects: both
  arms have seed spreads under 1 Å at those depths.
