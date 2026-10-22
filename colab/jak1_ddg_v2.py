"""Dual-state PyRosetta ddG for TYK2 - v2, with the relaxation step the first attempt lacked.

v1 produced ddG values from -692 to +1136 kcal/mol (the paper clips to [-10,10]) and correlated
with nothing. Cause: the input structures were never relaxed into the Rosetta scorefunction.
AlphaFold and OpenFold outputs carry small clashes that ref2015 scores enormously, so each repack
resolved or created them and the score swung by hundreds of kcal/mol. Repack SD reached 11.4
kcal/mol - larger than any real ddG.

v2 changes:
  1. FastRelax both structures first, with coordinate constraints so they stay near the input
     geometry. Both states get the SAME protocol so the open-closed difference is not an artefact
     of one being better optimised.
  2. Report the relaxed baseline scores, so the two states can be checked for comparability.
  3. Keep 3 repacks per variant per state; the SD is now meaningful rather than clash noise.
"""
import json, os, sys, time, urllib.request

SHELL, NREP = 8.0, 3

def af_url(acc="P23458"):
    r = urllib.request.Request(f"https://alphafold.ebi.ac.uk/api/prediction/{acc}",
                               headers={"User-Agent": "Mozilla/5.0"})
    return json.load(urllib.request.urlopen(r, timeout=120))[0]["pdbUrl"]

RAW = "https://raw.githubusercontent.com/chervov/ProteinModelling1/main/"

def grab(url, path):
    if not os.path.exists(path): urllib.request.urlretrieve(url, path)
    return path

def relaxed_pose(path, tag, sfxn):
    """FastRelax with coordinate constraints, cached to disk so shards share the work."""
    import pyrosetta
    from pyrosetta import pose_from_pdb
    from pyrosetta.rosetta.protocols.relax import FastRelax
    out = f"relaxed_{tag}.pdb"
    if os.path.exists(out):
        return pose_from_pdb(out)
    p = pose_from_pdb(path)
    # constrain to starting coordinates: we want the local geometry cleaned, not the fold changed
    from pyrosetta.rosetta.protocols.constraint_generator import (
        CoordinateConstraintGenerator, AddConstraints)
    cg = CoordinateConstraintGenerator(); ac = AddConstraints(); ac.add_generator(cg); ac.apply(p)
    sf = sfxn.clone()
    from pyrosetta.rosetta.core.scoring import ScoreType
    sf.set_weight(ScoreType.coordinate_constraint, 1.0)
    fr = FastRelax(sf, 1)        # 1 round is enough to clear clashes
    fr.apply(p)
    p.dump_pdb(out)
    return p

def main(start=0, end=None, tag="part"):
    import pyrosetta
    from pyrosetta import get_fa_scorefxn, Pose
    pyrosetta.init("-ex1 -ex2aro -ignore_unrecognized_res -mute all")
    sfxn = get_fa_scorefxn()
    srcs = {"closed": (RAW + "JAK1/Jeanpierre2025_Closed_WT_JAK1_best_model.pdb", "jak1_closed.pdb"),
            "open":   (RAW + "JAK1/Jeanpierre2025_Open_WT_JAK1_best_model.pdb", "jak1_open.pdb")}
    poses, base = {}, {}
    for st,(url,path) in srcs.items():
        grab(url, path)
        poses[st] = relaxed_pose(path, st, sfxn)
        base[st]  = sfxn(poses[st])
        print(f"{st}: {poses[st].total_residue()} res, relaxed score {base[st]:.1f} REU", flush=True)
    json.dump(base, open(f"baseline_{tag}.json","w"))

    # CALIBRATION RUN. These are the paper's own JAK1 open/closed models, so the ddG distribution
    # should land near the cluster means it reports: ddG_closed -2.05 (Cluster 1) and -6.36
    # (Cluster 2). Values far outside that mean the protocol is wrong, independently of any
    # question about TYK2 structure quality.
    # The five variants the paper characterises experimentally, plus an even spread for statistics.
    PAPER = [(464,'M'),(815,'S'),(879,'G'),(917,'D'),(1042,'Y')]
    import random; random.seed(0)
    n_res = poses['closed'].total_residue()
    spread = [(p, a) for p in range(20, n_res-20, 23) for a in "ADEFGKLNQRSVWY"]
    random.shuffle(spread)
    jobs = (PAPER + spread)[start:end]
    print(f"{len(jobs)} jobs", flush=True)

    def ddg(pose, pos, alt):
        import statistics
        v = []
        for _ in range(NREP):
            wt = Pose(); wt.assign(pose); mt = Pose(); mt.assign(pose)
            pyrosetta.toolbox.mutate_residue(mt, pos, alt, pack_radius=SHELL)
            pyrosetta.toolbox.mutate_residue(wt, pos, wt.residue(pos).name1(), pack_radius=SHELL)
            v.append(sfxn(mt) - sfxn(wt))
        return statistics.mean(v), (statistics.stdev(v) if len(v) > 1 else 0.0)

    out, t0 = [], time.time()
    for i,(pos,alt) in enumerate(jobs):
        rec = {"pos": pos, "alt": alt}; ok = True
        for st,p in poses.items():
            if pos > p.total_residue(): ok = False; break
            rec["wt"] = p.residue(pos).name1()
            if rec["wt"] == alt: ok = False; break
            m,s = ddg(p, pos, alt)
            rec[f"ddg_{st}"] = -m        # paper's sign: negative = destabilizing
            rec[f"sd_{st}"]  = s
        if not ok: continue
        rec["delta_open_minus_closed"] = rec["ddg_open"] - rec["ddg_closed"]
        out.append(rec)
        if (i+1) % 10 == 0:
            el = time.time()-t0
            print(f"  {i+1}/{len(jobs)} {el/(i+1):.1f}s/var", flush=True)
            json.dump(out, open(f"ddg_{tag}.json","w"), indent=1)
    json.dump(out, open(f"ddg_{tag}.json","w"), indent=1)
    print(f"done {len(out)} -> ddg_{tag}.json")

if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]) if a else 0, int(a[1]) if len(a)>1 else None, a[2] if len(a)>2 else "part")
