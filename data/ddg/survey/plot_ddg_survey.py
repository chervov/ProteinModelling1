"""Figures for the ddG method survey."""
import json, pathlib
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

H = pathlib.Path(__file__).parent
S = json.load(open(H / "ddg_survey.json"))
FIG = H / "figs"; FIG.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 8.5, "figure.dpi": 150, "savefig.bbox": "tight",
                     "axes.spines.top": False, "axes.spines.right": False})
SH = {"rosetta_closed": "Rosetta closed", "rosetta_open": "Rosetta open",
      "rosetta_delta": "Rosetta delta", "thermompnn": "ThermoMPNN", "foldx": "FoldX",
      "rsa": "RSA", "alphamissense": "AlphaMissense", "polyphen2": "PolyPhen-2",
      "esm1b": "ESM-1b", "cadd": "CADD"}
J = pd.read_csv(H / "jak2_methods.csv", index_col=0)

# 1 histograms of the ddG-like methods, JAK2
MET = ["rosetta_closed", "rosetta_open", "rosetta_delta", "thermompnn", "foldx", "rsa"]
fig, axes = plt.subplots(2, 3, figsize=(11, 5.4))
for ax, m in zip(axes.flat, MET):
    v = J[m].dropna()
    lo, hi = np.percentile(v, [0.5, 99.5])
    ax.hist(np.clip(v, lo, hi), bins=70, color="#4878d0", alpha=.85)
    ax.set_title(f"{SH[m]}   n={len(v):,}", fontsize=9)
    ax.set_yscale("log")
    ax.axvline(float(v.median()), color="#c0152f", lw=1, ls="--")
    ax.text(.98, .93, f"median {v.median():.2f}\n1–99% {np.percentile(v,1):.1f} … {np.percentile(v,99):.1f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=7, color="#555")
fig.suptitle("JAK2: distribution of each ΔΔG-like method (log y, clipped at 0.5–99.5%)", fontsize=10)
fig.tight_layout(); fig.savefig(FIG / "histograms.png"); plt.close(fig)

# 2 correlation heatmaps, all four proteins
cmap = LinearSegmentedColormap.from_list("bwr2", ["#2166ac", "#f7f7f7", "#b2182b"])
fig, axes = plt.subplots(1, 4, figsize=(19, 4.6))
for ax, (p, v) in zip(axes, S["proteins"].items()):
    cols = v["corr_cols"]; C = v["corr_spearman"]
    M = np.array([[C[a][b] if C[a][b] is not None else np.nan for b in cols] for a in cols])
    im = ax.imshow(M, cmap=cmap, vmin=-1, vmax=1)
    for i in range(len(cols)):
        for j in range(len(cols)):
            if not np.isnan(M[i, j]):
                ax.text(j, i, f"{M[i,j]:.2f}", ha="center", va="center", fontsize=6,
                        color="white" if abs(M[i, j]) > .55 else "#333")
    ax.set_xticks(range(len(cols))); ax.set_xticklabels([SH[c] for c in cols], rotation=55, ha="right", fontsize=7)
    ax.set_yticks(range(len(cols))); ax.set_yticklabels([SH[c] for c in cols], fontsize=7)
    ax.set_title(p, fontsize=10); ax.grid(False)
fig.colorbar(im, ax=axes, shrink=.7, label="Spearman ρ (all oriented: + = more damaging)")
fig.suptitle("Method correlations — the same picture in all four proteins", fontsize=11)
fig.savefig(FIG / "correlations.png"); plt.close(fig)

# 3 THE OUTLIER FIGURE: % extreme by target residue, per method
fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), sharey=False)
B = S["proteins"]["JAK2"]["by_target_aa"]
for ax, (m, thr) in zip(axes, [("rosetta_closed", "ΔΔG < −10"), ("foldx", "ΔΔG > +10"),
                               ("thermompnn", "ΔΔG > +10")]):
    g = B.get(m, {})
    aas = sorted(g, key=lambda a: -g[a]["pct_extreme"])
    vals = [g[a]["pct_extreme"] for a in aas]
    cols = ["#c0152f" if a in "FPWY" else "#9aa0a8" for a in aas]
    ax.bar(range(len(aas)), vals, color=cols)
    ax.set_xticks(range(len(aas))); ax.set_xticklabels(aas, fontsize=8)
    ax.set_ylabel("% of substitutions beyond threshold")
    ax.set_title(f"{SH[m]}   ({thr})", fontsize=10)
    ax.set_ylim(0, max(100 if m == "rosetta_closed" else 20, max(vals + [1]) * 1.15))
axes[0].text(.5, .88, "F, P, W, Y in red", transform=axes[0].transAxes, color="#c0152f", fontsize=9)
fig.suptitle("The outlier tail is a PyRosetta problem: fraction of extreme ΔΔG by substituted-in residue (JAK2)",
             fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "outliers_by_residue.png"); plt.close(fig)

# 4 RSA vs the ddG methods
fig, axes = plt.subplots(1, 3, figsize=(12.5, 4))
for ax, m in zip(axes, ["thermompnn", "foldx", "rosetta_closed"]):
    d = J[["rsa", m]].dropna()
    ax.hexbin(d.rsa, np.clip(d[m], *np.percentile(d[m], [1, 99])), gridsize=45, cmap="Blues",
              bins="log", mincnt=1)
    r = d.rsa.corr(d[m], method="spearman")
    ax.set_xlabel("RSA (relative solvent accessibility, 0–1)"); ax.set_ylabel(SH[m])
    ax.set_title(f"{SH[m]}  vs RSA   ρ = {r:+.2f}", fontsize=10)
fig.suptitle("A single geometric number tracks ΔΔG nearly as well as the methods track each other",
             fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "rsa_vs_ddg.png"); plt.close(fig)

# 5 TYK2 against experimental DMS
fig, ax = plt.subplots(figsize=(8.6, 4.2))
D = S["tyk2_dms"]
ms = sorted(D, key=lambda m: -abs(D[m].get("abundance", {}).get("spearman", 0)))
x = np.arange(len(ms)); w = .38
ab = [abs(D[m].get("abundance", {}).get("spearman", 0)) for m in ms]
ifn = [abs(D[m].get("ifn_100U", {}).get("spearman", 0)) for m in ms]
ax.bar(x - w/2, ab, w, label="abundance (stability)", color="#4878d0")
ax.bar(x + w/2, ifn, w, label="IFN 100 U (function)", color="#ee854a")
for i, m in enumerate(ms):
    if m.startswith(("rosetta", "foldx", "thermompnn", "rsa")):
        ax.get_xticklabels()
ax.set_xticks(x); ax.set_xticklabels([SH[m] for m in ms], rotation=35, ha="right")
ax.set_ylabel("|Spearman ρ| vs DMS"); ax.legend(frameon=False)
ax.set_title("TYK2: every method against the deep mutational scan (22,516 variants)", fontsize=10)
fig.tight_layout(); fig.savefig(FIG / "tyk2_dms.png"); plt.close(fig)

# 6 per-cluster separation
fig, axes = plt.subplots(1, 4, figsize=(17, 3.8), sharey=True)
for ax, (p, v) in zip(axes, S["proteins"].items()):
    bc = v.get("by_cluster", {})
    ms2 = sorted(bc, key=lambda m: -bc[m]["auc"])
    ax.barh(range(len(ms2)), [bc[m]["auc"] for m in ms2],
            color=["#c0152f" if m.startswith(("rosetta", "foldx", "thermompnn", "rsa")) else "#9aa0a8"
                   for m in ms2])
    ax.axvline(.5, color="#555", ls="--", lw=1)
    ax.set_yticks(range(len(ms2))); ax.set_yticklabels([SH[m] for m in ms2], fontsize=7.5)
    ax.invert_yaxis(); ax.set_xlim(.45, 1); ax.set_title(p, fontsize=10); ax.set_xlabel("AUC vs the clustering")
fig.suptitle("Separation of the two clusters — stability methods in red, predictors in grey", fontsize=11)
fig.tight_layout(); fig.savefig(FIG / "by_cluster.png"); plt.close(fig)
print("wrote", len(list(FIG.glob("*.png"))), "figures")
