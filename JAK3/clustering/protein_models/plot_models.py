"""Static PNG views of the five JAK3 models - no browser, no WebGL, no vendor file.

matplotlib 3D line plots of the Ca backbone. These are the fallback for the interactive
viewer and the figures the markdown embeds.
"""
import json, os, pathlib
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = pathlib.Path(__file__).parent
S = json.load(open(HERE / "model_analysis.json"))
FIG = HERE / "figs"; FIG.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 8, "figure.dpi": 150, "savefig.bbox": "tight"})

DOM = S["domains"]
DCOL = {"FERM": "#4878d0", "SH2": "#6acc64", "JH2": "#ee854a", "JH1": "#d65f5f",
        "linker": "#c0c0c0"}
LAB = {m["key"]: m["label"] for m in S["models"]}
ORDER = ["af3_closed", "openfold_open", "afdb"]


def dom_of(r):
    for d, (a, b) in DOM.items():
        if a <= r <= b:
            return d
    return "linker"


def xyz(key, fitted=False):
    t = S["traces"][key]
    return np.array(t["xyz"], float), t["res"], np.array(t["plddt"], float)


def draw(ax, X, res, colors=None, lw=0.8, alpha=1.0, single=None):
    """Draw the backbone as per-domain segments so colour changes at the boundaries."""
    cur, start = dom_of(res[0]), 0
    for i in range(1, len(res) + 1):
        d = dom_of(res[i]) if i < len(res) else None
        if d != cur:
            seg = X[start:i + (1 if i < len(res) else 0)]
            ax.plot(seg[:, 0], seg[:, 1], seg[:, 2],
                    color=single or DCOL[cur], lw=lw, alpha=alpha, solid_capstyle="round")
            cur, start = d, i


def style(ax, title=None):
    ax.set_axis_off()
    ax.set_box_aspect((1, 1, 1))
    if title:
        ax.set_title(title, fontsize=8.5, pad=2)


# One radius for every panel. Scaling each model to its own extent would make the open
# and closed states look the same size, which is the single thing these figures exist to show.
GLOBAL_R = max(np.abs(np.array(S["traces"][k]["xyz"], float)
                      - np.array(S["traces"][k]["xyz"], float).mean(0)).max()
               for k in ORDER) * 0.60


def equalise(ax, X, r=None):
    c = X.mean(0); r = r or GLOBAL_R
    ax.set_xlim(c[0] - r, c[0] + r); ax.set_ylim(c[1] - r, c[1] + r); ax.set_zlim(c[2] - r, c[2] + r)


LEG = [Line2D([], [], color=DCOL[d], lw=2.4, label=d) for d in DCOL]

# ---- 1. all five models, two viewing angles each ----
fig = plt.figure(figsize=(8.6, 5.4))
for j, k in enumerate(ORDER):
    X, res, _ = xyz(k)
    for row, (elev, azim) in enumerate([(18, -60), (18, 30)]):
        ax = fig.add_subplot(2, 3, row * 3 + j + 1, projection="3d")
        draw(ax, X, res, lw=0.65)
        equalise(ax, X); ax.view_init(elev, azim)
        style(ax, f"{LAB[k]}\nFERM-JH1 {S['centroids'][k]['FERM-JH1']:.0f} A" if row == 0 else None)
fig.legend(handles=LEG, loc="lower center", ncol=5, frameon=False, fontsize=8.5,
           bbox_to_anchor=(.5, -.015))
fig.suptitle("The three JAK3 models, two viewing angles each", fontsize=10)
fig.subplots_adjust(left=.01,right=.99,top=.88,bottom=.06,wspace=-.25,hspace=-.18)
fig.savefig(FIG / "models_overview.png"); plt.close(fig); print("  figs/models_overview.png")

# ---- 2. pair 1 closed vs open, superposed on JH2 ----
A, resA, _ = xyz("af3_closed")
B, resB, _ = xyz("openfold_open")
Af = np.array(S["traces"]["af3_closed_fitted"], float) if "af3_closed_fitted" in S["traces"] \
     else None
if Af is None:   # recompute the JH2 fit here so this script stands alone
    bi = {r: i for i, r in enumerate(resB)}
    lo, hi = DOM["JH2"]
    sh = [(i, bi[r]) for i, r in enumerate(resA) if lo <= r <= hi and r in bi]
    P = A[[i for i, _ in sh]]; Q = B[[j for _, j in sh]]
    pm, qm = P.mean(0), Q.mean(0)
    V, _, W = np.linalg.svd((P - pm).T @ (Q - qm))
    R = V @ np.diag([1, 1, np.sign(np.linalg.det(V @ W))]) @ W
    Af = (A - pm) @ R + qm

fig = plt.figure(figsize=(13.5, 4.0))
for i, (elev, azim) in enumerate([(14, -70), (14, 10), (78, -60)]):
    ax = fig.add_subplot(1, 3, i + 1, projection="3d")
    draw(ax, B, resB, lw=0.6, alpha=.55, single="#9aa0a6")
    draw(ax, Af, resA, lw=0.85)
    equalise(ax, np.vstack([Af, B])); ax.view_init(elev, azim)
    style(ax, ["side", "rotated 80°", "from above"][i])
fig.legend(handles=LEG + [Line2D([], [], color="#9aa0a6", lw=2.4, label="open (grey)")],
           loc="lower center", ncol=6, frameon=False, fontsize=8.5, bbox_to_anchor=(.5, -.02))
fig.suptitle("JAK3: closed in colour, open in grey, both fitted on JH2",
             fontsize=10)
fig.subplots_adjust(left=.01,right=.99,top=.92,bottom=.04,wspace=-.1)
fig.savefig(FIG / "open_vs_closed.png"); plt.close(fig); print("  figs/open_vs_closed.png")

# ---- 3. coloured by pLDDT ----
fig = plt.figure(figsize=(8.6, 3.2))
for j, k in enumerate(ORDER):
    X, res, pl = xyz(k)
    ax = fig.add_subplot(1, 3, j + 1, projection="3d")
    for i in range(len(X) - 1):
        ax.plot(X[i:i + 2, 0], X[i:i + 2, 1], X[i:i + 2, 2],
                color=plt.cm.RdYlBu((np.clip(pl[i], 50, 100) - 50) / 50), lw=0.75)
    equalise(ax, X); ax.view_init(18, -60)
    style(ax, f"{LAB[k]}\npLDDT {S['models'][j]['plddt']:.1f}")
sm = plt.cm.ScalarMappable(cmap="RdYlBu", norm=plt.Normalize(50, 100))
fig.colorbar(sm, ax=fig.axes, shrink=.6, pad=.015, label="pLDDT")
fig.suptitle("Confidence: high inside domains, collapsing in the linkers", fontsize=10)
fig.subplots_adjust(left=.01,right=.93,top=.84,bottom=.02,wspace=-.2)
fig.savefig(FIG / "plddt.png"); plt.close(fig); print("  figs/plddt.png")

# ---- 4. the numbers, as a figure ----
fig, axes = plt.subplots(1, 3, figsize=(13.5, 3.5))
ax = axes[0]
pairs = S["domain_pairs"]
w = .15
for i, k in enumerate(ORDER):
    ax.bar(np.arange(len(pairs)) + (i - 2) * w, [S["centroids"][k][p] for p in pairs], w,
           label=LAB[k], color=plt.cm.tab10(i))
ax.set_xticks(range(len(pairs))); ax.set_xticklabels(pairs, rotation=40, ha="right", fontsize=7)
ax.set_ylabel("centroid distance (A)"); ax.legend(fontsize=6.5, frameon=False)
ax.set_title("Only the three JH1 pairs change", fontsize=9)
ax = axes[1]
keys = ORDER; n = len(keys)
Mx = np.full((n, n), np.nan)
for i, a in enumerate(keys):
    for j, b in enumerate(keys):
        if i == j: Mx[i, j] = 0
        else:
            v = S["pairwise"].get(f"{a}|{b}") or S["pairwise"].get(f"{b}|{a}")
            Mx[i, j] = v["jh1_after_jh2_fit"]
im = ax.imshow(Mx, cmap="magma_r")
for i in range(n):
    for j in range(n):
        ax.text(j, i, f"{Mx[i,j]:.1f}", ha="center", va="center", fontsize=6.5,
                color="white" if Mx[i, j] > 45 else "#222")
ax.set_xticks(range(n)); ax.set_xticklabels([LAB[k] for k in keys], rotation=40, ha="right", fontsize=6.5)
ax.set_yticks(range(n)); ax.set_yticklabels([LAB[k] for k in keys], fontsize=6.5)
ax.set_title("JH1 RMSD after JH2 fit (A)", fontsize=9)
ax = axes[2]
pae = S["afdb_pae"]
ks = ["SH2-SH2", "JH2-JH2", "JH1-JH1", "FERM-FERM", "FERM-SH2", "SH2-JH2", "FERM-JH2",
      "JH2-JH1", "SH2-JH1", "FERM-JH1"]
cols = ["#6acc64" if "-" in k and k.split("-")[0] == k.split("-")[1] else "#d65f5f" for k in ks]
ax.barh(range(len(ks)), [pae[k] for k in ks], color=cols)
ax.axvline(S["afdb_pae_max"], color="#555", ls="--", lw=1)
ax.text(S["afdb_pae_max"], -.8, f" ceiling {S['afdb_pae_max']}", fontsize=6.5, va="top")
ax.set_yticks(range(len(ks))); ax.set_yticklabels(ks, fontsize=6.5); ax.invert_yaxis()
ax.set_xlabel("mean PAE (A)"); ax.set_title("AlphaFold DB PAE: confident within,\nnot between", fontsize=9)
fig.tight_layout(); fig.savefig(FIG / "metrics.png"); plt.close(fig); print("  figs/metrics.png")

# ---- 5. the full AlphaFold DB PAE matrix ----
pae_f = HERE / "AFmodel" / "AF-P52333-F1-predicted_aligned_error_v6.json"
if pae_f.exists():
    raw = json.load(open(pae_f))
    P = np.array((raw[0] if isinstance(raw, list) else raw)["predicted_aligned_error"], float)
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.9),
                             gridspec_kw={"width_ratios": [1.12, 1]})
    ax = axes[0]
    im = ax.imshow(P, cmap="Greens_r", vmin=0, vmax=P.max(), origin="upper",
                   extent=[1, P.shape[0], P.shape[0], 1])
    for d, (a, b) in DOM.items():
        for v in (a, b):
            ax.axhline(v, color="#333", lw=.4, alpha=.6); ax.axvline(v, color="#333", lw=.4, alpha=.6)
        ax.add_patch(plt.Rectangle((a, a), b - a, b - a, fill=False, ec=DCOL[d], lw=1.6))
        ax.text(b + 8, (a + b) / 2, d, color=DCOL[d], fontsize=7.5, va="center", rotation=90)
    # mark the block that matters
    fa, fb = DOM["FERM"]; ja, jb = DOM["JH1"]
    ax.add_patch(plt.Rectangle((ja, fa), jb - ja, fb - fa, fill=False, ec="#c0152f", lw=1.6, ls="--"))
    ax.text((ja + jb) / 2, fa - 14, "FERM-JH1", color="#c0152f", fontsize=7.5, ha="center")
    ax.set_xlabel("scored residue"); ax.set_ylabel("aligned residue")
    ax.set_title("AlphaFold DB PAE, AF-P52333-F1 v6", fontsize=9.5)
    fig.colorbar(im, ax=ax, shrink=.82, label="expected position error (A)")

    ax = axes[1]
    blocks = ["SH2-SH2", "JH2-JH2", "JH1-JH1", "FERM-FERM", "FERM-SH2", "SH2-JH2",
              "FERM-JH2", "JH2-JH1", "SH2-JH1", "FERM-JH1"]
    vals = [S["afdb_pae"][b] for b in blocks]
    cols = ["#6acc64" if b.split("-")[0] == b.split("-")[1] else
            ("#c0152f" if b == "FERM-JH1" else "#ee854a") for b in blocks]
    ax.barh(range(len(blocks)), vals, color=cols)
    ax.axvline(S["afdb_pae_max"], color="#555", ls="--", lw=1)
    ax.text(S["afdb_pae_max"] - .4, len(blocks) - .4, f"ceiling {S['afdb_pae_max']} A",
            fontsize=7, ha="right", va="center")
    for i, v in enumerate(vals):
        ax.text(v + .4, i, f"{v:.1f}", fontsize=7, va="center")
    ax.set_yticks(range(len(blocks))); ax.set_yticklabels(blocks, fontsize=8); ax.invert_yaxis()
    ax.set_xlim(0, S["afdb_pae_max"] * 1.12); ax.set_xlabel("mean PAE (A)")
    ax.set_title("Mean PAE per block: confident within domains,\nnot between FERM and JH1",
                 fontsize=9.5)
    fig.tight_layout(); fig.savefig(FIG / "pae.png"); plt.close(fig); print("  figs/pae.png")
else:
    print("  (no PAE json, skipping figs/pae.png)")
print("done")
