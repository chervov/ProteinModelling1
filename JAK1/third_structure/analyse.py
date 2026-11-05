import numpy as np, difflib, glob, os, json, itertools
SEQ = open("jak1.seq").read().strip()
ONE = {"ALA":"A","ARG":"R","ASN":"N","ASP":"D","CYS":"C","GLN":"Q","GLU":"E","GLY":"G","HIS":"H","ILE":"I","LEU":"L","LYS":"K","MET":"M","PHE":"F","PRO":"P","SER":"S","THR":"T","TRP":"W","TYR":"Y","VAL":"V",
       "SEP":"S","TPO":"T","PTR":"Y","HIE":"H","HID":"H","HIP":"H","CYX":"C"}
DOM = {"FERM": (34, 420), "SH2": (439, 544), "JH2": (583, 855), "JH1": (875, 1153)}
def load(path):
    res = {}                                   # resnum -> {"aa", "atoms": {name: xyz}, "b"}
    for l in open(path):
        if not l.startswith(("ATOM", "HETATM")) or l[17:20] not in ONE: continue
        if l[16] not in " A": continue
        n = int(l[22:26]); r = res.setdefault(n, {"aa": ONE[l[17:20]], "atoms": {}, "b": float(l[60:66] or 0)})
        r["atoms"][l[12:16].strip()] = np.array([float(l[30:38]), float(l[38:46]), float(l[46:54])])
    ks = sorted(res); s = "".join(res[k]["aa"] for k in ks)
    if s == SEQ: return res
    sm = difflib.SequenceMatcher(None, s, SEQ, autojunk=False)   # map to UniProt numbering
    return {b.b + i + 1: res[ks[b.a + i]] for b in sm.get_matching_blocks() for i in range(b.size)}
S = {os.path.basename(p)[:-4]: load(p) for p in sorted(glob.glob("pdb/*.pdb"))}
rng = lambda d: range(DOM[d][0], DOM[d][1] + 1)
CA = lambda X, R: np.array([X[i]["atoms"]["CA"] for i in R])
def common(*Xs, R): return [i for i in R if all(i in X and "CA" in X[i]["atoms"] for X in Xs)]
def kabsch(P, Q):
    pc, qc = P.mean(0), Q.mean(0); u, s, vt = np.linalg.svd((P - pc).T @ (Q - qc))
    d = np.sign(np.linalg.det(vt.T @ u.T)); R = vt.T @ np.diag([1, 1, d]) @ u.T
    return R, qc - pc @ R.T
def jh1_fit_jh2(A, B):          # RMSD of JH1 after superposing JH2 (A onto B)
    f = common(A, B, R=rng("JH2")); m = common(A, B, R=rng("JH1"))
    R, t = kabsch(CA(A, f), CA(B, f)); d = CA(A, m) @ R.T + t - CA(B, m)
    return float(np.sqrt((d ** 2).sum(1).mean()))
def jh1_rot(A, B):              # rotation angle of JH1 between A and B in the JH2 frame
    f = common(A, B, R=rng("JH2")); m = common(A, B, R=rng("JH1"))
    R1, t1 = kabsch(CA(A, f), CA(B, f))               # put A in B's JH2 frame
    Pa = CA(A, m) @ R1.T + t1; R2, _ = kabsch(Pa, CA(B, m))
    return float(np.degrees(np.arccos(np.clip((np.trace(R2) - 1) / 2, -1, 1)))), float(np.linalg.norm(Pa.mean(0) - CA(B, m).mean(0)))
def cen(X, d): return np.mean([X[i]["atoms"]["CA"] for i in rng(d) if i in X], 0) if sum(i in X for i in rng(d)) > 20 else None
def contacts(X, d1, d2, cut=4.5):
    A = [(i, np.array(list(X[i]["atoms"].values()))) for i in rng(d1) if i in X]
    B = [(j, np.array(list(X[j]["atoms"].values()))) for j in rng(d2) if j in X]
    ca = {i: X[i]["atoms"].get("CA") for i, _ in A + B}
    pairs = set()
    for i, a in A:
        for j, b in B:
            if np.linalg.norm(ca[i] - ca[j]) > 20: continue
            if np.min(np.linalg.norm(a[:, None] - b[None], axis=2)) < cut: pairs.add((i, j))
    return pairs
def domain_integrity(X, ref):
    out = {}
    for d in DOM:
        c = common(X, ref, R=rng(d))
        if len(c) < 30: continue
        R, t = kabsch(CA(X, c), CA(ref, c)); out[d] = float(np.sqrt((((CA(X, c) @ R.T + t) - CA(ref, c)) ** 2).sum(1).mean()))
    return out
OPEN, CLOSED, AF2, SHAN = S["ref_ma-a1sai"], S["ref_ma-l9b1f"], S["ref_AF2"], S["ref_shan"]
names = [k for k in S]
rows = []
for k in names:
    X = S[k]; c = {d: cen(X, d) for d in DOM}
    dist = lambda a, b: round(float(np.linalg.norm(c[a] - c[b])), 1) if c[a] is not None and c[b] is not None else None
    ro, to = jh1_rot(X, OPEN); rc, tc = jh1_rot(X, CLOSED)
    pl = {d: round(float(np.mean([X[i]["b"] for i in rng(d) if i in X])), 1) for d in DOM if sum(i in X for i in rng(d)) > 20}
    rows.append({"name": k, "FERM-JH1": dist("FERM", "JH1"), "SH2-JH1": dist("SH2", "JH1"), "JH2-JH1": dist("JH2", "JH1"),
                 "FERM-JH2": dist("FERM", "JH2"), "SH2-JH2": dist("SH2", "JH2"),
                 "vs_open": round(jh1_fit_jh2(X, OPEN), 1), "vs_closed": round(jh1_fit_jh2(X, CLOSED), 1),
                 "vs_shan": round(jh1_fit_jh2(X, SHAN), 1), "rot_vs_open": round(ro), "shift_vs_open": round(to, 1),
                 "rot_vs_closed": round(rc), "shift_vs_closed": round(tc, 1), "pLDDT": pl,
                 "integrity_vs_AF2": {d: round(v, 2) for d, v in domain_integrity(X, AF2).items()}})
third = [k for k in names if k.startswith("third")]
M = {a: {b: round(jh1_fit_jh2(S[a], S[b]), 1) for b in third + ["ref_ma-a1sai", "ref_ma-l9b1f", "ref_shan", "other_96_s0"]} for a in third}
C = {}
for k in names:
    X = S[k]; C[k] = {}
    for d1, d2 in [("JH1", "FERM"), ("JH1", "SH2"), ("JH1", "JH2"), ("JH2", "FERM"), ("JH2", "SH2"), ("FERM", "SH2")]:
        C[k][f"{d1}-{d2}"] = sorted(contacts(X, d1, d2))
json.dump({"rows": rows, "M": M, "C": {k: {p: v for p, v in d.items()} for k, d in C.items()}}, open("analysis.json", "w"), default=int)
print("done", len(rows))
