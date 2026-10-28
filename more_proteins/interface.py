#!/usr/bin/env python3
"""Does the compact state of a domain pair have a real interface, or are the domains floppy?

For each (protein, domain pair) with >=2 structures, count inter-domain heavy-atom contacts
within 5 A in EVERY structure. The two-state signature (JAK-like) is: many contacts in the
compact structure AND few in the extended one. A flexible-linker protein is mobile but has
few contacts in every structure - no defined closed form.

Reference values from this project (mutation_analysis.md section 3, on 4OLI):
  TYK2 P982 (at the JH2-JH1 interface): 28 cross-domain contacts <5 A
  TYK2 V678 (not at the interface)    :  0
and the whole TYK2 JH2-JH1 interface buries 1147 A^2 over 21 residues.
"""
import os, glob, json, itertools, collections, csv
import numpy as np
from scipy.spatial import cKDTree

STRUCT_DIR = "/Users/chervov/mp_structs"
CACHE = "/Users/chervov/mp_review/domains_cache.json"
CUT = 5.0

def read_heavy(path):
    """residue number -> list of heavy-atom coords, first chain only."""
    out = collections.defaultdict(list); chain = None
    for L in open(path, errors="replace"):
        if not L.startswith("ATOM"): continue
        el = L[76:78].strip() or L[12:16].strip()[0]
        if el == "H": continue
        ch = L[21]
        if chain is None: chain = ch
        if ch != chain: continue
        try: r = int(L[22:26])
        except ValueError: continue
        out[r].append((float(L[30:38]), float(L[38:46]), float(L[46:54])))
    return out

def contacts(hv, ra, rb):
    A = [c for r in ra if r in hv for c in hv[r]]
    B = [c for r in rb if r in hv for c in hv[r]]
    if not A or not B: return None, None
    A = np.array(A); B = np.array(B)
    pairs = cKDTree(A).query_ball_tree(cKDTree(B), CUT)
    n_at = sum(len(x) for x in pairs)
    # distinct residue pairs in contact, a less atom-count-dependent measure
    ia = [r for r in ra if r in hv for _ in hv[r]]
    ib = [r for r in rb if r in hv for _ in hv[r]]
    rp = {(ia[i], ib[j]) for i, js in enumerate(pairs) for j in js}
    return n_at, len(rp)

def main():
    cache = json.load(open(CACHE))
    files = collections.defaultdict(list)
    for p in sorted(glob.glob(os.path.join(STRUCT_DIR, "*.pdb"))):
        b = os.path.basename(p).split("_"); files[(b[0], b[1])].append(p)
    rows = []
    for (gene, acc), paths in sorted(files.items()):
        if len(paths) < 2: continue
        doms = cache.get(acc, [])
        if len(doms) < 2: continue
        hvs = {p: read_heavy(p) for p in paths}
        for (na, sa, ea), (nb, sb, eb) in itertools.combinations(doms, 2):
            ra = list(range(sa, ea + 1)); rb = list(range(sb, eb + 1))
            per = {}
            for p in paths:
                hv = hvs[p]
                if sum(1 for r in ra if r in hv) < 0.5 * len(ra): continue
                if sum(1 for r in rb if r in hv) < 0.5 * len(rb): continue
                A = np.array([c for r in ra if r in hv for c in hv[r]]).mean(0)
                B = np.array([c for r in rb if r in hv for c in hv[r]]).mean(0)
                n_at, n_rp = contacts(hv, ra, rb)
                per[p] = (float(np.linalg.norm(A - B)), n_at or 0, n_rp or 0)
            if len(per) < 2: continue
            d = {p: v[0] for p, v in per.items()}
            comp = min(d, key=d.get); ext = max(d, key=d.get)
            rows.append(dict(gene=gene, acc=acc, pair=f"{na}|{nb}", n=len(per),
                             d_compact=round(per[comp][0], 1), d_extended=round(per[ext][0], 1),
                             contacts_compact=per[comp][2], contacts_extended=per[ext][2],
                             contacts_max=max(v[2] for v in per.values()),
                             contacts_min=min(v[2] for v in per.values())))
    out = "/Users/chervov/mp_review/interface_contacts.csv"
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} rows -> {out}")

if __name__ == "__main__":
    main()
