#!/usr/bin/env python3
"""Superposition-based inter-domain mobility, for comparison with centroid distance.

For each domain pair (A,B) and each pair of structures: superpose on domain A's Ca atoms
(Kabsch), then report the Ca RMSD of domain B. This is the metric used in reference_states.md
(JH1 RMSD after superposing JH2) and is sensitive to hinge rotations that preserve the
centroid distance - the blind spot of the centroid method.
"""
import os, sys, glob, json, urllib.request, collections, itertools
import numpy as np

STRUCT_DIR = "/Users/chervov/mp_structs"
CACHE = "/Users/chervov/mp_review/domains_cache.json"

def uniprot_domains(acc, cache):
    if acc in cache: return cache[acc]
    u = f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=ft_domain"
    try:
        d = json.load(urllib.request.urlopen(u, timeout=60))
    except Exception as e:
        cache[acc] = []; return []
    out = []
    for f in d.get("features", []):
        if f.get("type") != "Domain": continue
        s = f["location"]["start"].get("value"); e = f["location"]["end"].get("value")
        if s and e: out.append((f.get("description", "?"), int(s), int(e)))
    cache[acc] = out
    return out

def read_ca(path):
    """residue number -> Ca coordinate, first chain encountered only."""
    ca = {}; chain = None
    for L in open(path, errors="replace"):
        if not L.startswith("ATOM"): continue
        if L[12:16].strip() != "CA": continue
        ch = L[21]
        if chain is None: chain = ch
        if ch != chain: continue
        try: r = int(L[22:26])
        except ValueError: continue
        ca[r] = (float(L[30:38]), float(L[38:46]), float(L[46:54]))
    return ca

def kabsch(P, Q):
    """rotation+translation aligning P onto Q; returns R, t."""
    pc, qc = P.mean(0), Q.mean(0)
    H = (P - pc).T @ (Q - qc)
    U, S, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    D = np.diag([1, 1, d])
    R = Vt.T @ D @ U.T
    return R, qc - R @ pc

def main():
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    files = collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(STRUCT_DIR, "*.pdb"))):
        b = os.path.basename(p).split("_")
        files[(b[0], b[1])].append(p)

    rows = []
    for (gene, acc), paths in sorted(files.items()):
        if len(paths) < 2: continue
        doms = uniprot_domains(acc, cache)
        if len(doms) < 2: continue
        cas = {p: read_ca(p) for p in paths}
        for (na, sa, ea), (nb, sb, eb) in itertools.combinations(doms, 2):
            ra = list(range(sa, ea + 1)); rb = list(range(sb, eb + 1))
            usable = [p for p in paths
                      if sum(1 for r in ra if r in cas[p]) >= 0.5 * len(ra)
                      and sum(1 for r in rb if r in cas[p]) >= 0.5 * len(rb)]
            if len(usable) < 2: continue
            # centroid distance, for direct comparison
            cent = {}
            for p in usable:
                A = np.array([cas[p][r] for r in ra if r in cas[p]])
                B = np.array([cas[p][r] for r in rb if r in cas[p]])
                cent[p] = float(np.linalg.norm(A.mean(0) - B.mean(0)))
            # superposition RMSD of B after aligning on A, all structure pairs
            sup = []
            for p, q in itertools.combinations(usable, 2):
                ca_shared = [r for r in ra if r in cas[p] and r in cas[q]]
                cb_shared = [r for r in rb if r in cas[p] and r in cas[q]]
                if len(ca_shared) < 20 or len(cb_shared) < 20: continue
                P = np.array([cas[p][r] for r in ca_shared])
                Q = np.array([cas[q][r] for r in ca_shared])
                R, t = kabsch(P, Q)
                Bp = np.array([cas[p][r] for r in cb_shared]) @ R.T + t
                Bq = np.array([cas[q][r] for r in cb_shared])
                sup.append(float(np.sqrt(((Bp - Bq) ** 2).sum(1).mean())))
            if not sup: continue
            cv = list(cent.values())
            rows.append(dict(gene=gene, acc=acc, pair=f"{na}|{nb}", n=len(usable),
                             cent_min=round(min(cv), 1), cent_max=round(max(cv), 1),
                             cent_spread=round(max(cv) - min(cv), 1),
                             sup_max=round(max(sup), 1), sup_med=round(float(np.median(sup)), 1)))
    json.dump(cache, open(CACHE, "w"))
    out = "/Users/chervov/mp_review/superposition_vs_centroid.csv"
    import csv
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} (protein, pair) rows -> {out}")
    return rows

if __name__ == "__main__":
    main()
