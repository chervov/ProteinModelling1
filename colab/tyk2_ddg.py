# Dual-state PyRosetta ddG for TYK2, reproducing Jeanpierre/Debeaupuis (EMBO Mol Med 2025).
#
# Their convention (Appendix S3): ddG_m = dG_WT - dG_m, so NEGATIVE = destabilizing.
# Rosetta's native convention is the opposite, so the sign is flipped at the end.
# The key feature is ddG_open - ddG_closed: positive means the mutation favours the open
# state, which the paper reads as "more open configurations in mutants" = gain of function.
import os, sys, json, time, urllib.request

SHELL = 8.0          # repack neighbours within this radius of the mutated residue
NREP  = 3            # independent repacks per variant per state, for an error bar the paper lacks

def install():
    try:
        import pyrosetta; return
    except ImportError:
        pass
    os.system(f"{sys.executable} -m pip install -q pyrosetta-installer")
    import pyrosetta_installer; pyrosetta_installer.install_pyrosetta()

def grab(url, path):
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)
    return path

RAW = "https://raw.githubusercontent.com/chervov/ProteinModelling1/main/"
def af_url(acc="P29597"):
    """AlphaFold bumps its model version (v4 -> v6 ...) and old URLs start returning 403,
    so resolve the current one from the API rather than hardcoding it."""
    import json
    req = urllib.request.Request(f"https://alphafold.ebi.ac.uk/api/prediction/{acc}",
                                 headers={"User-Agent": "Mozilla/5.0"})
    return json.load(urllib.request.urlopen(req, timeout=120))[0]["pdbUrl"]

STRUCTS = {
    # closed/compact: the AlphaFold TYK2 model, FERM-JH1 39.7 A
    "closed": (af_url(), "tyk2_closed.pdb"),
    # open: a wild-type template-free prediction at 512/8192, FERM-JH1 93.4 A, 4.8 A from
    # Jeanpierre's open JAK1 model - the TYK2 equivalent of their open state
    "open":   (RAW + "TYK2/runs/TYK2_20261022_010154/selected_open.pdb", "tyk2_open.pdb"),
}

def main(start=0, end=None, tag="part"):
    install()
    import pyrosetta
    from pyrosetta import pose_from_pdb, get_fa_scorefxn, Pose
    from pyrosetta.rosetta.core.pack.task import TaskFactory
    from pyrosetta.rosetta.protocols.minimization_packing import PackRotamersMover
    pyrosetta.init("-ex1 -ex2aro -ignore_unrecognized_res -mute all")
    sfxn = get_fa_scorefxn()

    poses = {}
    for state,(url,path) in STRUCTS.items():
        grab(url, path)
        p = pose_from_pdb(path)
        print(f"{state}: {p.total_residue()} residues", flush=True)
        poses[state] = p

    # the 26 residues of the 4OLI JH2-JH1 interface (section 26 of mutation_analysis.md)
    IFACE = [579,580,582,610,637,663,664,666,672,674,728,743,744,756,
             900,901,921,922,923,926,980,982,983,992,993,1033]
    AAS = "ACDEFGHIKLMNPQRSTVWY"
    jobs = [(pos,alt) for pos in IFACE for alt in AAS]
    jobs = jobs[start:end]
    print(f"{len(jobs)} (position, substitution) jobs", flush=True)

    def ddg(pose, pos, alt):
        """Rosetta-convention ddG = score(mut) - score(wt); positive = destabilizing."""
        import pyrosetta
        from pyrosetta.rosetta.core.pack.task import operation
        vals = []
        for rep in range(NREP):
            wt = Pose(); wt.assign(pose)
            mt = Pose(); mt.assign(pose)
            pyrosetta.toolbox.mutate_residue(mt, pos, alt, pack_radius=SHELL)
            # repack the same shell in the WT so both sides get equal treatment
            pyrosetta.toolbox.mutate_residue(wt, pos, wt.residue(pos).name1(), pack_radius=SHELL)
            vals.append(sfxn(mt) - sfxn(wt))
        import statistics
        return statistics.mean(vals), (statistics.stdev(vals) if len(vals) > 1 else 0.0)

    out = []
    t0 = time.time()
    for i,(pos,alt) in enumerate(jobs):
        rec = {"pos": pos, "alt": alt}
        ok = True
        for state,p in poses.items():
            if pos > p.total_residue():
                ok = False; break
            wt_name = p.residue(pos).name1()
            rec["wt"] = wt_name
            if wt_name == alt: ok = False; break
            m,s = ddg(p, pos, alt)
            rec[f"ddg_{state}"] = -m          # flip to the paper's sign: negative = destabilizing
            rec[f"sd_{state}"]  = s
        if not ok: continue
        rec["delta_open_minus_closed"] = rec["ddg_open"] - rec["ddg_closed"]
        out.append(rec)
        if (i+1) % 10 == 0:
            el = time.time()-t0
            print(f"  {i+1}/{len(jobs)}  {el/ (i+1):.1f}s/variant  eta {el/(i+1)*(len(jobs)-i-1)/60:.0f} min", flush=True)
            json.dump(out, open(f"ddg_{tag}.json","w"), indent=1)
    json.dump(out, open(f"ddg_{tag}.json","w"), indent=1)
    print(f"done: {len(out)} variants -> ddg_{tag}.json")

if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]) if a else 0, int(a[1]) if len(a)>1 else None, a[2] if len(a)>2 else "part")
