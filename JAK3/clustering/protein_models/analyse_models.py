"""Geometry and superposition analysis of the five JAK3 full-length models.

Writes model_analysis.json, consumed by the markdown and the HTML viewer.

Measures, in order of what they are good for:
  - domain centroid distances, all 6 pairs, which describe the domain arrangement
  - global Ca RMSD between every pair of models, which is dominated by that arrangement
  - per-domain RMSD after fitting that domain alone, which shows the domains themselves
    are near-identical and only their placement differs
  - JH1 RMSD after superposing JH2, the open/closed measure used throughout this project
  - inter-domain PAE, available only for the AlphaFold DB model
"""
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
# JAK3 P52333 boundaries from UniProt: FERM 26-431, SH2 450-529,
# protein kinase 1 (JH2) 589-875, protein kinase 2 (JH1) 897-1176
# JAK3 P52333: FERM 24-356, SH2 378-482, JH2 521-781, JH1 822-1111
DOM = {"FERM": (24, 356), "SH2": (378, 482), "JH2": (521, 781), "JH1": (822, 1111)}
MODELS = [
    ("af3_closed", "af3_closed/jak3_af3_notemplate_closed_model0.pdb", "AF3 closed",
     "AF3, no template"),
    ("openfold_open", "openfold_open/jak3_openfold_open.pdb", "OpenFold open",
     "OpenFold JAK3_20261016_172413, no template"),
    ("afdb", "AFmodel/AF-P52333-F1-model_v6.pdb", "AlphaFold DB v6", "n/a (AFDB)"),
]
# JAK3 has NO experimental closed structure. The AFDB model is itself closed (FERM-JH1 41.5 A),
# so it serves as the reference arrangement - weaker than TYK2, which has the 4OLI crystal.
SHAN = os.path.join(HERE, "AFmodel", "AF-P52333-F1-model_v6.pdb")
def ca(path, chain=None):
    out = {}
    for l in open(path):
        if l.startswith("ATOM") and l[12:16].strip() == "CA" and (chain is None or l[21] == chain):
            out[int(l[22:26])] = (np.array([float(l[30 + 8 * i:38 + 8 * i]) for i in range(3)]),
                                  float(l[60:66]))
    return out


def fit(P, Q):
    """Kabsch: returns a transform taking P's frame onto Q's, and the fit RMSD."""
    pm, qm = P.mean(0), Q.mean(0)
    V, _, W = np.linalg.svd((P - pm).T @ (Q - qm))
    R = V @ np.diag([1, 1, np.sign(np.linalg.det(V @ W))]) @ W
    T = lambda X: (X - pm) @ R + qm
    return T, float(np.sqrt(((T(P) - Q) ** 2).sum(1).mean()))


def rng(d):
    return range(DOM[d][0], DOM[d][1] + 1)


def main():
    M = {k: ca(os.path.join(HERE, p)) for k, p, _, _ in MODELS}
    shan = ca(SHAN)
    keys = [k for k, *_ in MODELS]
    S = {"models": [{"key": k, "label": lab, "template": t, "file": p,
                     "n_res": len(M[k]),
                     "plddt": round(float(np.mean([v[1] for v in M[k].values()])), 2),
                     "plddt_by_domain": {d: round(float(np.mean(
                         [M[k][r][1] for r in rng(d) if r in M[k]])), 1) for d in DOM}}
                    for k, p, lab, t in MODELS]}

    # ---- centroid distances, all 6 domain pairs ----
    pairs = [(a, b) for i, a in enumerate(DOM) for b in list(DOM)[i + 1:]]
    S["domain_pairs"] = ["%s-%s" % p for p in pairs]
    S["centroids"] = {}
    for k in keys:
        cen = {d: np.mean([M[k][r][0] for r in rng(d) if r in M[k]], axis=0) for d in DOM}
        S["centroids"][k] = {f"{a}-{b}": round(float(np.linalg.norm(cen[a] - cen[b])), 1)
                             for a, b in pairs}

    # ---- pairwise model comparison ----
    S["pairwise"] = {}
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            sh = sorted(set(M[a]) & set(M[b]))
            A = np.array([M[a][r][0] for r in sh]); B = np.array([M[b][r][0] for r in sh])
            _, glob = fit(A, B)
            per = {}
            for d in DOM:
                s = [r for r in rng(d) if r in M[a] and r in M[b]]
                _, per[d] = fit(np.array([M[a][r][0] for r in s]),
                                np.array([M[b][r][0] for r in s]))
                per[d] = round(per[d], 2)
            # JH1 displacement after fitting on JH2 - the conformational difference
            s2 = [r for r in rng("JH2") if r in M[a] and r in M[b]]
            s1 = [r for r in rng("JH1") if r in M[a] and r in M[b]]
            T, _ = fit(np.array([M[a][r][0] for r in s2]), np.array([M[b][r][0] for r in s2]))
            P1 = np.array([M[a][r][0] for r in s1]); Q1 = np.array([M[b][r][0] for r in s1])
            jh1 = float(np.sqrt(((T(P1) - Q1) ** 2).sum(1).mean()))
            S["pairwise"][f"{a}|{b}"] = {"n": len(sh), "global_rmsd": round(glob, 2),
                                         "per_domain_rmsd": per, "jh1_after_jh2_fit": round(jh1, 2)}

    # ---- each model against Shan's JAK3 (JH2-JH1 only, 520-1131) ----
    S["vs_shan"] = {}
    for k in keys:
        s2 = [r for r in rng("JH2") if r in M[k] and r in shan]
        s1 = [r for r in rng("JH1") if r in M[k] and r in shan]
        T, r2 = fit(np.array([M[k][r][0] for r in s2]), np.array([shan[r][0] for r in s2]))
        P1 = np.array([M[k][r][0] for r in s1]); Q1 = np.array([shan[r][0] for r in s1])
        S["vs_shan"][k] = {"jh2_fit_rmsd": round(r2, 2), "n_jh1": len(s1),
                           "jh1_rmsd": round(float(np.sqrt(((T(P1) - Q1) ** 2).sum(1).mean())), 2)}

    # ---- inter-domain PAE, AFDB only ----
    pae_f = os.path.join(HERE, "AFmodel", "AF-P52333-F1-predicted_aligned_error_v6.json")
    if os.path.exists(pae_f):
        raw = json.load(open(pae_f))
        P = np.array((raw[0] if isinstance(raw, list) else raw)["predicted_aligned_error"], float)
        idx = {d: np.array([r - 1 for r in rng(d) if r - 1 < P.shape[0]]) for d in DOM}
        S["afdb_pae"] = {f"{a}-{b}": round(float(P[np.ix_(idx[a], idx[b])].mean()), 1)
                         for a, b in pairs}
        S["afdb_pae"].update({f"{d}-{d}": round(float(P[np.ix_(idx[d], idx[d])].mean()), 1)
                              for d in DOM})
        S["afdb_pae_max"] = round(float(P.max()), 1)

    # ---- backbone traces for the 3D viewer, 1 decimal is plenty ----
    S["traces"] = {k: {"res": sorted(M[k]),
                       "xyz": [[round(float(c), 1) for c in M[k][r][0]] for r in sorted(M[k])],
                       "plddt": [round(M[k][r][1], 1) for r in sorted(M[k])]} for k in keys}
    S["domains"] = {d: list(DOM[d]) for d in DOM}
    json.dump(S, open(os.path.join(HERE, "model_analysis.json"), "w"))

    w = lambda *a: print(*a)
    w("\n== centroid distances (A) ==")
    w(f"{'model':<16}" + "".join(f"{p:>12}" for p in S["domain_pairs"]))
    for k in keys:
        w(f"{k:<16}" + "".join(f"{S['centroids'][k][p]:>12.1f}" for p in S["domain_pairs"]))
    w("\n== pairwise: global RMSD / JH1 after JH2 fit ==")
    for kk, v in S["pairwise"].items():
        a, b = kk.split("|")
        w(f"{a:<14}{b:<14}global {v['global_rmsd']:6.2f}   JH1|JH2fit {v['jh1_after_jh2_fit']:6.2f}"
          f"   per-domain " + " ".join(f"{d} {v['per_domain_rmsd'][d]:.2f}" for d in DOM))
    w("\n== vs Shan 2014 JAK3 ==")
    for k in keys:
        w(f"{k:<16}JH2 fit {S['vs_shan'][k]['jh2_fit_rmsd']:5.2f}   JH1 {S['vs_shan'][k]['jh1_rmsd']:7.2f}")
    if "afdb_pae" in S:
        w("\n== AFDB inter-domain PAE (A) ==")
        for p, v in S["afdb_pae"].items():
            w(f"   {p:<12}{v:5.1f}")
    w(f"\nwrote model_analysis.json "
      f"({os.path.getsize(os.path.join(HERE,'model_analysis.json'))/1e6:.2f} MB)")


if __name__ == "__main__":
    main()
