"""Dual-state ddG worker, driven by a job queue. Detached process; writes JSONL incrementally.

Positions are processed in a pre-shuffled order, so partial output at ANY stopping point is an
unbiased random sample - which matters because molab sandboxes expire at ~4h mid-run.
"""
import os, json, time, sys, traceback, urllib.request
import multiprocessing as mp

W = "/tmp/ddg"
RAW = "https://raw.githubusercontent.com/chervov/ProteinModelling1/main/"
NPROC = max(1, min(18, mp.cpu_count() - 2))
POSE = {}
SF = None

def log(*a):
    print(f"[{time.strftime('%H:%M:%S')}]", *a, flush=True)

def init_rosetta():
    global SF
    import pyrosetta
    from pyrosetta import get_fa_scorefxn
    pyrosetta.init("-mute all -ex1 -ex2aro -ignore_unrecognized_res "
                   "-ignore_zero_occupancy false -detect_disulf false")
    SF = get_fa_scorefxn()

def load_state(job, tag):
    """Fetch + relax (cached) one state. Returns the pose."""
    from pyrosetta import pose_from_pdb
    from pyrosetta.rosetta.protocols.relax import FastRelax
    from pyrosetta.rosetta.protocols.constraint_generator import (
        CoordinateConstraintGenerator, AddConstraints)
    from pyrosetta.rosetta.core.scoring import ScoreType
    gene = job["gene"]
    src = os.path.join(W, f"{gene}_{tag}.pdb")
    if not os.path.exists(src) or os.path.getsize(src) < 50000:
        u = job["models"][tag]
        urllib.request.urlretrieve(u if u.startswith("http") else RAW + u, src)
    chain = job.get("chain")
    if chain:
        keep = [l for l in open(src)
                if (not l.startswith(("ATOM", "HETATM"))) or l[21] == chain]
        open(src, "w").writelines(keep)
    cached = os.path.join(W, f"{gene}_relaxed_{tag}.pdb")
    if os.path.exists(cached) and os.path.getsize(cached) > 100000:
        p = pose_from_pdb(cached); log(f"{gene} {tag}: loaded cached relax")
    else:
        p = pose_from_pdb(src)
        cg = CoordinateConstraintGenerator()
        ac = AddConstraints(); ac.add_generator(cg); ac.apply(p)
        sf = SF.clone(); sf.set_weight(ScoreType.coordinate_constraint, 1.0)
        t0 = time.time(); FastRelax(sf, 1).apply(p)
        log(f"{gene} {tag}: relaxed in {time.time()-t0:.0f}s")
        p.dump_pdb(cached + ".tmp"); os.replace(cached + ".tmp", cached)
    log(f"{gene} {tag}: {p.total_residue()} res, baseline {SF(p):.1f} REU")
    return p

def one_position(args):
    """All variants at one position, both states. The WT repack is computed ONCE per position
    per state and reused across that position's substitutions - a ~19x saving."""
    pos, alts = args
    from pyrosetta.toolbox import mutate_residue
    recs = []
    try:
        wt = alts[0][0]
        base = {}
        for tag in ("closed", "open"):
            seq = POSE[tag].sequence()
            if pos > len(seq) or seq[pos - 1] != wt:
                return []
            p = POSE[tag].clone()
            mutate_residue(p, pos, wt, pack_radius=8.0)
            base[tag] = SF(p)
        for w, alt in alts:
            rec = {"pos": pos, "wt": w, "alt": alt}
            for tag in ("closed", "open"):
                p = POSE[tag].clone()
                mutate_residue(p, pos, alt, pack_radius=8.0)
                # paper convention: ddG = dG_WT - dG_mut, negative = destabilizing
                rec[f"ddg_{tag}"] = round(base[tag] - SF(p), 4)
            rec["delta"] = round(rec["ddg_open"] - rec["ddg_closed"], 4)
            recs.append(rec)
    except Exception:
        log("position", pos, "FAILED\n", traceback.format_exc())
        return []
    return recs

def run_job(job):
    gene = job["gene"]
    out = os.path.join(W, f"results_{gene}.jsonl")
    done_flag = os.path.join(W, f"DONE_{gene}")
    if os.path.exists(done_flag):
        log(f"{gene}: already complete, skipping"); return
    log(f"=== JOB {gene} ===")
    POSE.clear()
    for tag in ("closed", "open"):
        POSE[tag] = load_state(job, tag)
    json.dump({t: SF(POSE[t]) for t in POSE},
              open(os.path.join(W, f"baselines_{gene}.json"), "w"))
    shard = job["shard"]
    done = set()
    if os.path.exists(out):
        for line in open(out):
            try: done.add(int(json.loads(line)["pos"]))
            except Exception: pass
    todo = [(int(p), shard[p]) for p in shard if int(p) not in done]
    log(f"{gene}: {len(shard)} positions in shard, {len(done)} done, {len(todo)} to go, "
        f"{sum(len(v) for _, v in todo)} variants, {NPROC} workers")
    t0 = time.time(); nv = 0
    with open(out, "a") as fh, mp.Pool(NPROC) as pool:
        for i, recs in enumerate(pool.imap_unordered(one_position, todo, chunksize=1), 1):
            for r in recs:
                fh.write(json.dumps(r) + "\n")
            fh.flush(); os.fsync(fh.fileno())
            nv += len(recs)
            if i % 5 == 0 or i == len(todo):
                el = time.time() - t0
                log(f"{gene} progress {i}/{len(todo)} pos, {nv} variants, "
                    f"{el/60:.1f} min, {nv/max(el,1)*3600:.0f} var/h")
    open(done_flag, "w").write(str(nv))
    log(f"{gene}_COMPLETE {nv} variants in {(time.time()-t0)/60:.1f} min")

def main():
    os.makedirs(W, exist_ok=True)
    jobs = json.load(open(os.path.join(W, "jobs.json")))
    init_rosetta()
    for job in jobs:
        try:
            run_job(job)
        except Exception:
            log("JOB FAILED", job.get("gene"), "\n", traceback.format_exc())
    log("ALL_JOBS_FINISHED")

if __name__ == "__main__":
    main()
