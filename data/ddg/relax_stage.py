"""Stage 1 of Frenz et al. 2020 (10.3389/fbioe.2020.558247) cartesian ddG protocol.
Relax the starting model 20x WITHOUT all-atom constraints in Cartesian space;
keep the LOWEST-energy model as input to cartesian_ddg."""
import os, sys, time, json, multiprocessing as mp

CONSTRUCTS = {"FERM_SH2": (20, 497), "JH2_JH1": (545, 1132)}
NSTRUCT, NPROC = 20, 8

def trim(src, lo, hi, out):
    keep = [l for l in open(src) if l.startswith("ATOM") and lo <= int(l[22:26]) <= hi]
    open(out, "w").write("".join(keep) + "TER\nEND\n")
    return len({l[22:26] for l in keep})

def one_relax(args):
    name, pdb, seed = args
    import pyrosetta
    pyrosetta.init(f"-score:weights ref2015_cart -ex1 -ex2 -mute all "
                   f"-fa_max_dis 9.0 -constant_seed -jran {seed}")
    from pyrosetta import pose_from_pdb
    from pyrosetta.rosetta.protocols.relax import FastRelax
    p = pose_from_pdb(pdb)
    sf = pyrosetta.create_score_function("ref2015_cart")
    fr = FastRelax(); fr.set_scorefxn(sf); fr.cartesian(True); fr.max_iter(100)
    t0 = time.time(); fr.apply(p); dt = time.time() - t0
    out = f"relaxed/{name}_{seed}.pdb"; p.dump_pdb(out)
    e = sf(p)
    print(f"{name} seed{seed}: {e:.2f} REU  {dt/60:.1f} min", flush=True)
    return {"construct": name, "seed": seed, "energy": e, "pdb": out, "minutes": dt/60}

if __name__ == "__main__":
    os.makedirs("relaxed", exist_ok=True)
    jobs = []
    for name, (lo, hi) in CONSTRUCTS.items():
        src = f"construct_{name}.pdb"
        n = trim("AF-O60674-F1.pdb", lo, hi, src)
        print(f"{name}: residues {lo}-{hi} ({n} present)", flush=True)
        jobs += [(name, src, s) for s in range(1, NSTRUCT + 1)]
    print(f"{len(jobs)} relax jobs on {NPROC} cores", flush=True)
    t0 = time.time()
    with mp.Pool(NPROC) as pool:
        res = pool.map(one_relax, jobs)
    json.dump(res, open("relax_results.json", "w"), indent=1)
    for name in CONSTRUCTS:
        sub = sorted([r for r in res if r["construct"] == name], key=lambda r: r["energy"])
        print(f"\n{name}: best {sub[0]['energy']:.2f} REU ({sub[0]['pdb']}), "
              f"worst {sub[-1]['energy']:.2f}, spread {sub[-1]['energy']-sub[0]['energy']:.2f}")
        json.dump(sub[0], open(f"best_{name}.json", "w"))
    print(f"\nTOTAL {(time.time()-t0)/60:.1f} min")
