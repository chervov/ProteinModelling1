"""Inventory every full-length JAK2 structure we have and measure its conformational state.

Answers one question: do we have a CLOSED full-length JAK2, and if so which file is it?

Filenames cannot be trusted. The guided-recycling runs selected "open" and "closed" using the
JH2-JH1 centroid distance, which open_close.md shows is a weak discriminator (46 A open vs
38-41 A closed - the transition is mostly a rotation of JH1, so the centroid barely moves).
Many files called selected_open.pdb are closed and vice versa. So every structure is re-measured
here and the filename is ignored.

Three measures, in increasing order of trustworthiness:
  FERM-JH1 centroid distance  - ~93 A open, ~42 A closed. Strong, needs no reference.
  JH2-JH1 centroid distance   - the weak one. Reported only to show why it misled the selection.
  JH1 RMSD to Shan 2014 JAK2 after superposing JH2 - says WHICH closed state, not just "compact".

That last one is what separates a real closed model from a differently-collapsed one.
"""
import glob, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SHAN = os.path.join(ROOT, "Shan2014JAK1JAK2",
                    "NIHMS704086-supplement-PDB_coordinates_for_JAK2_model.pdb")
DOM = {"FERM": (37, 380), "SH2": (401, 482), "JH2": (545, 809), "JH1": (849, 1124)}


def ca(path, chain=None):
    out = {}
    for l in open(path):
        if l.startswith("ATOM") and l[12:16].strip() == "CA" and (chain is None or l[21] == chain):
            out[int(l[22:26])] = (np.array([float(l[30 + 8 * i:38 + 8 * i]) for i in range(3)]),
                                  float(l[60:66]))
    return out


def centroids(c):
    return {d: (np.mean([c[r][0] for r in range(a, b + 1) if r in c], axis=0)
                if any(r in c for r in range(a, b + 1)) else None) for d, (a, b) in DOM.items()}


def kabsch_fit(P, Q):
    """Return a function mapping P's frame onto Q's."""
    pm, qm = P.mean(0), Q.mean(0)
    V, _, W = np.linalg.svd((P - pm).T @ (Q - qm))
    R = V @ np.diag([1, 1, np.sign(np.linalg.det(V @ W))]) @ W
    return lambda X: (X - pm) @ R + qm


def jh1_rmsd_to_shan(c, ref):
    s2 = [r for r in range(*DOM["JH2"]) if r in c and r in ref]
    s1 = [r for r in range(*DOM["JH1"]) if r in c and r in ref]
    if len(s2) < 50 or len(s1) < 50:
        return None
    fit = kabsch_fit(np.array([c[r][0] for r in s2]), np.array([ref[r][0] for r in s2]))
    P1, Q1 = np.array([c[r][0] for r in s1]), np.array([ref[r][0] for r in s1])
    return float(np.sqrt(((fit(P1) - Q1) ** 2).sum(1).mean()))


def deep(o, key):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key:
                return v
            r = deep(v, key)
            if r is not None:
                return r
    return None


def rmsd_txt(r):
    v = r["jh1_rmsd_to_shan"]
    return "     -" if v is None else f"{v:.1f}"


def classify(ferm_jh1, jh1_rmsd):
    """CLOSED only when it is compact AND in Shan's closed state."""
    if ferm_jh1 is None:
        return "partial"
    if ferm_jh1 > 80:
        return "open"
    if ferm_jh1 > 60:
        return "intermediate"
    if jh1_rmsd is not None and jh1_rmsd > 15:
        return "compact, NOT Shan"
    return "closed"


def main():
    ref = ca(SHAN, "X")
    rows = []
    paths = sorted(glob.glob(os.path.join(ROOT, "JAK2", "runs", "*", "selected_*.pdb")))
    paths += [os.path.join(ROOT, p) for p in (
        "JAK2/af3_template/jak2_af3_template_open_model0.pdb",
        "JAK2/af3_notemplate/jak2_af3_notemplate_open_model0.pdb",
        "AFDB/JAK2_afdb_O60674.pdb")]
    for p in paths:
        if not os.path.exists(p):
            continue
        c = ca(p)
        cen = centroids(c)
        d = lambda a, b: (float(np.linalg.norm(cen[a] - cen[b]))
                          if cen[a] is not None and cen[b] is not None else None)
        run = os.path.basename(os.path.dirname(p))
        cfg = next((x for x in (os.path.join(os.path.dirname(p), f)
                                for f in ("run_config.json", "experiment_config.json"))
                    if os.path.exists(x)), None)
        conf = json.load(open(cfg)) if cfg else {}
        muts = deep(conf, "mutations")
        tmpl = deep(conf, "template_source") or deep(conf, "template_cif")
        fj, rm = d("FERM", "JH1"), jh1_rmsd_to_shan(c, ref)
        rows.append({"run": run, "file": os.path.basename(p),
                     "label_in_filename": "closed" if "closed" in os.path.basename(p) else "open",
                     "template": (os.path.basename(str(tmpl)) if tmpl else "none"),
                     "wt": not muts, "mutations": muts or [],
                     "ferm_jh1": fj, "jh2_jh1": d("JH2", "JH1"),
                     "plddt": float(np.mean([v[1] for v in c.values()])),
                     "jh1_rmsd_to_shan": rm, "state": classify(fj, rm)})
    out = os.path.join(HERE, "jak2_state_inventory.json")
    json.dump(rows, open(out, "w"), indent=1)

    print(f"{'run':<28}{'file':<8}{'template':<18}{'WT':<4}{'FERM-JH1':>9}{'JH2-JH1':>8}"
          f"{'pLDDT':>7}{'JH1 vs Shan':>12}  state  (filename said)")
    for r in rows:
        mis = "" if r["state"].startswith(r["label_in_filename"]) else f"  <- said {r['label_in_filename']}"
        print(f"{r['run'][:27]:<28}{r['label_in_filename']:<8}{r['template'][:17]:<18}"
              f"{'y' if r['wt'] else 'n':<4}{r['ferm_jh1']:9.1f}{r['jh2_jh1']:8.1f}{r['plddt']:7.1f}"
              f"{rmsd_txt(r):>12}"
              f"  {r['state']}{mis}")
    n = sum(1 for r in rows if r["state"] == "closed")
    nwt = sum(1 for r in rows if r["state"] == "closed" and r["wt"])
    nmis = sum(1 for r in rows if not r["state"].startswith(r["label_in_filename"]))
    print(f"\n{len(rows)} structures: {n} genuinely closed ({nwt} wild-type), "
          f"{sum(1 for r in rows if r['state']=='open')} open, "
          f"{sum(1 for r in rows if r['state']=='intermediate')} intermediate, "
          f"{sum(1 for r in rows if r['state']=='compact, NOT Shan')} compact but not Shan's state.")
    print(f"{nmis} of {len(rows)} filenames disagree with the measurement.")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
