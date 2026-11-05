#!/usr/bin/env python
"""Regenerate every number and figure in ddg_review_claudesci.{md,html}.

Inputs (all in the repo, nothing local required):
  ../jak2_variants_multimethod.csv   six-method table for the 24 selected variants
  ../jak2_rosetta_cartesian.csv      per-variant Rosetta energies + cart_bonded diagnostics
  ../survey/jak2_methods.csv         full JAK2 saturation (companion survey)
  ../rsalor_jak2_family.csv          full-protein RSALOR run (semicolon-separated)
Outputs: figs/*.png and the statistics tables embedded in the markdown.
"""
import pandas as pd, numpy as np, re, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

V  = pd.read_csv("../jak2_variants_multimethod.csv")
RC = pd.read_csv("../jak2_rosetta_cartesian.csv")
J  = pd.read_csv("../survey/jak2_methods.csv")
RS = pd.read_csv("../rsalor_jak2_family.csv", sep=";")

m = RS.mutation_pdb.str.extract(r"^([A-Z])[A-Za-z0-9]*?(\d+)([A-Z])$")
RS2 = RS.assign(variant=m[0] + m[1] + m[2])[["variant", "LOR", "RSA*LOR"]].rename(
    columns={"RSA*LOR": "rsalor"})
JF = J.merge(RS2, on="variant", how="left")
JF["rosetta_closed_flip"] = -JF.rosetta_closed      # their convention: negative = destabilising
JF["alt"] = JF.variant.str[-1]
D = V.dropna(subset=["thermompnn"])

COLS = ["thermompnn", "foldx", "rosetta_closed_flip", "rosetta_delta", "rsalor", "rsa",
        "alphamissense"]
print("Spearman, full saturation:\n", JF[COLS].dropna().corr(method="spearman").round(3))

out = []
for aa in sorted(JF.alt.dropna().unique()):
    s = JF[JF.alt == aa]
    out.append(dict(alt=aa, n=len(s),
                    rosetta_lt_m10=100 * (s.rosetta_closed < -10).mean(),
                    foldx_gt_10=100 * (s.foldx > 10).mean(),
                    thermompnn_gt_10=100 * (s.thermompnn > 10).mean()))
O = pd.DataFrame(out).sort_values("rosetta_lt_m10", ascending=False)
print("\nOutlier tail by target residue:\n", O.round(1).head(8).to_string(index=False))
print("\nRosetta artefacts (|d_cart_bonded| > 2):\n",
      RC[RC.d_cart_bonded.abs() > 2][["variant", "rosetta_cart_ddg", "d_cart_bonded"]]
      .to_string(index=False))
print("\nSee the markdown for the figure code; this script reproduces the statistics.")
