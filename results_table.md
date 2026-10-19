# Live results table (regenerated 2026-10-19 18:47)

Produced by `analysis/all_results.py`, which pulls every run folder from this repository, parses the
per-seed tables out of each `conclusions.md`, groups by (variant, MSA depth, template) and compares each
mutant against the wild type at the same depth.

**Metric:** JH1 RMSD against the closed reference after superposing JH2 (see
[conclusions_selected_20261019_131543.md](conclusions_selected_20261019_131543.md) section 0).
`closed<25` counts seeds that reach the closed arrangement. **Fisher** tests that count; **rank** is
Mann-Whitney on the full distribution. For bimodal data the Fisher count test is the robust one.

**Deduplication:** several duplicate run folders exist, created when the supervisor relaunched a
controller that had already finished its queue (19 Oct, 18:00-18:13). They contain re-derived analyses of
the same inference. The script keys on seed number within each group, so duplicates are not double
counted - without this, R657Q appeared as n=24 and TYK2 V678F at 96/384 as n=24.

```

======================================================================================
JAK3
======================================================================================
variant      MSA         tmpl           n closed<25  median  spread    Fisher     rank  runs
A572V        128/512     none          16    1/16      84.3    75.6    0.0373   0.0348  2
A573V        128/512     none          16   12/16       2.7    78.6    0.1489   0.0024  1
M511I        128/512     none          16    7/16      84.8    90.1    1.0000   0.8210  2
M592F        128/512     none          16    1/16      64.0    68.8    0.0373   0.2912  1
R657Q        128/512     none          16    4/16      89.0    90.3    0.4578   0.1315  3
WT           128/512     none          16    7/16      61.5    75.3                     1
Y581C        128/512     none          16    0/16      88.4     8.6    0.0068   0.0005  2
WT           256/1024    none          16    1/16      82.4    67.1                     1
WT           512/8192    none           8    0/8       82.3     0.7                     1
WT           None/None   none           8    4/8       43.6    87.6                     1

======================================================================================
TYK2
======================================================================================
variant      MSA         tmpl           n closed<25  median  spread    Fisher     rank  runs
P982A        128/512     none           8    0/8       82.2     0.8    1.0000   0.5932  1
WT           128/512     pdb:4OLI:A    16   16/16       1.0     1.6                     1
WT           128/512     none           8    0/8       82.1     0.6                     1
P982A        32/64       none          31    0/31      44.7    29.1    1.0000   0.1367  3
V678F        32/64       none          16    0/16      51.6    40.5    1.0000   0.3326  2
WT           32/64       none          15    0/15      46.4    57.4                     2
P982A        64/256      none          16    0/16      88.8    59.1    1.0000   0.3363  2
V678F        64/256      none          16    0/16      93.0    10.5    1.0000   0.0001  2
WT           64/256      none          16    0/16      84.5    50.8                     2
P982A        96/384      none           8    0/8       82.7    13.2    1.0000   0.7912  3
V678F        96/384      none           8    0/8       82.0     0.5    1.0000   0.0149  3
WT           96/384      none           8    0/8       82.5     8.8                     1

```

## Reading the table

- **TYK2 V678F at 64/256, rank p = 0.0001** is the strongest result in the project. Note `closed<25` is
  0/16 for both wild type and V678F - TYK2 never reaches the closed state - so the effect is visible only
  in the distribution: wild type spreads 50.8 A (reaching down to 41 A, partial approaches) while V678F
  spans 10.5 A and never drops below 85.6 A. **Here the rank test is the meaningful one and Fisher is blind.**
- **JAK3 Y581C, Fisher p = 0.0068**, 0/16 against wild type's 7/16 - the cleanest count-based effect.
- **TYK2 wild type with the 4OLI template, 16/16 closed at median 1.0 A** - the template assay has no
  dynamic range, which is why it was abandoned.
- **TYK2 P982A is null at all four depths** (0.59, 0.79, 0.34, 0.14) despite being the only one of the
  seven variants at a genuine domain interface.
