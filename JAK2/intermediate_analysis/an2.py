import numpy as np, difflib, glob, os, json
from Bio import Align
from Bio.Align import substitution_matrices
J1, J2 = open("jak1.seq").read().strip(), open("jak2.seq").read().strip()
ONE = {"ALA":"A","ARG":"R","ASN":"N","ASP":"D","CYS":"C","GLN":"Q","GLU":"E","GLY":"G","HIS":"H","ILE":"I","LEU":"L","LYS":"K","MET":"M","PHE":"F","PRO":"P","SER":"S","THR":"T","TRP":"W","TYR":"Y","VAL":"V","SEP":"S","TPO":"T","PTR":"Y","HIE":"H","HID":"H","HIP":"H","CYX":"C"}
DOM = {"FERM": (37, 380), "SH2": (401, 482), "JH2": (545, 809), "JH1": (849, 1124)}
def load(path, seq):
    res = {}
    for l in open(path):
        if not l.startswith(("ATOM", "HETATM")) or l[17:20] not in ONE or l[16] not in " A": continue
        n = int(l[22:26]); r = res.setdefault(n, {"aa": ONE[l[17:20]], "atoms": {}, "b": float(l[60:66] or 0)})
        r["atoms"][l[12:16].strip()] = np.array([float(l[30:38]), float(l[38:46]), float(l[46:54])])
    ks = sorted(res); s = "".join(res[k]["aa"] for k in ks)
    if s == seq: return res
    sm = difflib.SequenceMatcher(None, s, seq, autojunk=False)
    return {b.b + i + 1: res[ks[b.a + i]] for b in sm.get_matching_blocks() for i in range(b.size)}
al = Align.PairwiseAligner(mode="global", open_gap_score=-11, extend_gap_score=-1); al.substitution_matrix = substitution_matrices.load("BLOSUM62")
a = al.align(J1, J2)[0]; j1to2 = {}
for (s1, e1), (s2, e2) in zip(*a.aligned):
    for k in range(e1 - s1): j1to2[s1 + k + 1] = s2 + k + 1
def from_jak1(path):
    X = load(path, J1); return {j1to2[i]: v for i, v in X.items() if i in j1to2}
S = {}
for p in sorted(glob.glob("pdb/*.pdb")):
    k = os.path.basename(p)[:-4]
    S[k] = from_jak1(p) if k.startswith("j1_") else load(p, J2)
rng = lambda d: range(DOM[d][0], DOM[d][1] + 1)
CA = lambda X, R: np.array([X[i]["atoms"]["CA"] for i in R])
common = lambda A, B, R: [i for i in R if i in A and i in B and "CA" in A[i]["atoms"] and "CA" in B[i]["atoms"]]
def kabsch(P, Q):
    pc, qc = P.mean(0), Q.mean(0); u, s, vt = np.linalg.svd((P - pc).T @ (Q - qc)); d = np.sign(np.linalg.det(vt.T @ u.T))
    R = vt.T @ np.diag([1, 1, d]) @ u.T; return R, qc - pc @ R.T
def fit(A, B):
    f, m = common(A, B, rng("JH2")), common(A, B, rng("JH1"))
    R, t = kabsch(CA(A, f), CA(B, f)); d = CA(A, m) @ R.T + t - CA(B, m); return round(float(np.sqrt((d ** 2).sum(1).mean())), 1)
cen = lambda X, d: np.mean([X[i]["atoms"]["CA"] for i in rng(d) if i in X], 0) if sum(i in X for i in rng(d)) > 20 else None
def dist(X, a, b):
    ca, cb = cen(X, a), cen(X, b); return None if ca is None or cb is None else round(float(np.linalg.norm(ca - cb)), 1)
def contacts(X, d1, d2, cut=4.5):
    A = [(i, np.array(list(X[i]["atoms"].values()))) for i in rng(d1) if i in X]; B = [(j, np.array(list(X[j]["atoms"].values()))) for j in rng(d2) if j in X]
    out = set()
    for i, x in A:
        for j, y in B:
            if np.linalg.norm(X[i]["atoms"]["CA"] - X[j]["atoms"]["CA"]) < 20 and np.min(np.linalg.norm(x[:, None] - y[None], axis=2)) < cut: out.add((i, j))
    return out
refs = ["ref_AF2_jak2", "j2_relA_s0", "ref_shan2", "j1_exp_7T6F_A", "j1_ref_ma-l9b1f", "j1_ref_ma-a1sai"]
rows = []
for k in sorted(S):
    X = S[k]
    rows.append({"name": k, "FERM-JH1": dist(X, "FERM", "JH1"), "SH2-JH1": dist(X, "SH2", "JH1"), "JH2-JH1": dist(X, "JH2", "JH1"),
                 **{f"vs_{r}": fit(X, S[r]) for r in refs},
                 "c_JH1-JH2": len(contacts(X, "JH1", "JH2")), "c_JH1-FERM": len(contacts(X, "JH1", "FERM")), "c_JH1-SH2": len(contacts(X, "JH1", "SH2")),
                 "pLDDT_JH1": round(float(np.mean([X[i]["b"] for i in rng("JH1") if i in X])), 1)})
inter = sorted(k for k in S if k.startswith("j2_128") or k.startswith("j2_64"))
M = {a: {b: fit(S[a], S[b]) for b in inter} for a in inter}
IF = {k: sorted({p[1] for p in contacts(S[k], "JH1", "JH2")}) for k in inter + refs}
IF1 = {k: sorted({p[0] for p in contacts(S[k], "JH1", "JH2")}) for k in inter + refs}
json.dump({"rows": rows, "M": M, "IF_JH2": IF, "IF_JH1": IF1, "aln_identity": round(sum(J1[i-1] == J2[j-1] for i, j in j1to2.items()) / len(j1to2), 3)}, open("an2.json", "w"), default=int)
print("done")
