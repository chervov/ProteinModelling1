"""Is the third arrangement really a distinct state? Measures it against every reference.

Three measures, in increasing order of what they establish:
  domain centroid distances  - describes the arrangement
  JH1 RMSD after superposing JH2 - says WHICH arrangement, the measure used throughout
  JH1 rotation angle in the JH2 frame - says how far JH1 has turned, not just moved
"""
import json, os, pathlib
import numpy as np

HERE = pathlib.Path(__file__).parent
DOM = {"FERM": (34, 420), "SH2": (439, 544), "JH2": (583, 855), "JH1": (875, 1153)}
MODELS = [
    ("third_a",  "jak1_third_64-256_a.pdb", None, "Third arrangement (a)", "ours, MSA 64/256, no template"),
    ("third_b",  "jak1_third_64-256_b.pdb", None, "Third arrangement (b)", "ours, MSA 64/256, no template"),
    ("exp_7t6f", "7T6F.pdb", "A", "7T6F cryo-EM", "EXPERIMENTAL active JAK1 dimer (Glassman 2022)"),
    ("exp_8ewy", "8EWY.pdb", "A", "8EWY cryo-EM", "EXPERIMENTAL JAK1 dimer (Caveney 2023)"),
    ("open",     "jak1_open_ma-a1sai.pdb", None, "Open (ma-a1sai)", "Jeanpierre open model"),
    ("afdb",     "jak1_afdb_open.pdb", None, "AlphaFold DB", "AF-P23458-F1 v6"),
    ("closed",   "jak1_closed_ma-l9b1f.pdb", None, "Closed (ma-l9b1f)", "Jeanpierre closed model"),
]


def ca(path, chain=None):
    out = {}
    for l in open(path):
        if l.startswith("ATOM") and l[12:16].strip() == "CA" and (chain is None or l[21] == chain):
            if l[16] not in " A":
                continue
            out[int(l[22:26])] = np.array([float(l[30 + 8 * i:38 + 8 * i]) for i in range(3)])
    return out


def kabsch(P, Q):
    pm, qm = P.mean(0), Q.mean(0)
    V, _, W = np.linalg.svd((P - pm).T @ (Q - qm))
    R = V @ np.diag([1, 1, np.sign(np.linalg.det(V @ W))]) @ W
    return R, pm, qm


def jh1_after_jh2(A, B):
    """RMSD of JH1 after superposing JH2 - and the rotation JH1 has undergone."""
    f = [r for r in range(*DOM["JH2"]) if r in A and r in B]
    m = [r for r in range(*DOM["JH1"]) if r in A and r in B]
    if len(f) < 50 or len(m) < 50:
        return None, None
    R, pm, qm = kabsch(np.array([A[r] for r in f]), np.array([B[r] for r in f]))
    P1 = (np.array([A[r] for r in m]) - pm) @ R + qm
    Q1 = np.array([B[r] for r in m])
    rmsd = float(np.sqrt(((P1 - Q1) ** 2).sum(1).mean()))
    R2, _, _ = kabsch(P1, Q1)                      # residual rotation of JH1 itself
    ang = float(np.degrees(np.arccos(np.clip((np.trace(R2) - 1) / 2, -1, 1))))
    return rmsd, ang


M = {k: ca(HERE / "structures" / f, ch) for k, f, ch, _, _ in MODELS}
LAB = {k: lab for k, _, _, lab, _ in MODELS}
keys = [k for k, *_ in MODELS]
S = {"labels": LAB, "note": {k: n for k, _, _, _, n in MODELS}}

S["centroids"] = {}
for k in keys:
    c = {d: np.mean([M[k][r] for r in range(a, b + 1) if r in M[k]], axis=0) for d, (a, b) in DOM.items()}
    S["centroids"][k] = {f"{a}-{b}": round(float(np.linalg.norm(c[a] - c[b])), 1)
                         for i, a in enumerate(DOM) for b in list(DOM)[i + 1:]}
    S["centroids"][k]["n_ca"] = len(M[k])

S["jh1_rmsd"] = {a: {} for a in keys}
S["jh1_rot"] = {a: {} for a in keys}
for a in keys:
    for b in keys:
        r, ang = jh1_after_jh2(M[a], M[b])
        S["jh1_rmsd"][a][b] = None if r is None else round(r, 1)
        S["jh1_rot"][a][b] = None if ang is None else round(ang)

S["traces"] = {k: {"res": sorted(M[k]),
                   "xyz": [[round(float(c), 1) for c in M[k][r]] for r in sorted(M[k])]} for k in keys}
S["domains"] = {d: list(DOM[d]) for d in DOM}
json.dump(S, open(HERE / "third_analysis.json", "w"))

P = S["centroids"]["third_a"]
print("== centroid distances (A) ==")
cols = [c for c in P if c != "n_ca"]
print(f"{'model':<24}" + "".join(f"{c:>11}" for c in cols))
for k in keys:
    print(f"{LAB[k]:<24}" + "".join(f"{S['centroids'][k][c]:>11.1f}" for c in cols))
print("\n== JH1 RMSD after superposing JH2 (A) ==")
print(f"{'':<24}" + "".join(f"{LAB[k][:10]:>11}" for k in keys))
for a in keys:
    print(f"{LAB[a]:<24}" + "".join(
        (f"{S['jh1_rmsd'][a][b]:>11.1f}" if S['jh1_rmsd'][a][b] is not None else f"{'-':>11}") for b in keys))
print(f"\nwrote third_analysis.json")
