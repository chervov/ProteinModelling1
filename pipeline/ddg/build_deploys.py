"""Rebuild per-box deploy payloads, splitting the REMAINING work evenly across boxes.txt.

Recomputes what is missing from the merged results each time, so it is safe to re-run whenever a
box is added or replaced - already-computed variants are never recomputed.
"""
import json, gzip, base64, random, os, sys
OB = "/Users/chervov/orianne_tyk2"
T = "/Users/chervov/.claude/jobs/e920d48f/tmp/"
LOCAL = "/Users/chervov/ddg_overnight"
WORKER = open(T + "worker.py").read()
MODELS = {"TYK2": {"closed": "TYK2/af3/tyk2_af3_closed.pdb",
                   "open": "TYK2/af3/tyk2_af3_open.pdb"},
          "JAK1": {"closed": "JAK1/Jeanpierre2025_Closed_WT_JAK1_best_model.pdb",
                   "open": "JAK1/Jeanpierre2025_Open_WT_JAK1_best_model.pdb"}}
SHARDS = {"JAK1": "jak1_shard%d.json", "TYK2": "shard%d.json"}

boxes = [l.split() for l in open("/Users/chervov/boxes.txt").read().strip().split("\n")]
rem = {}
for gene in ("JAK1", "TYK2"):
    full = {}
    for i in range(4):
        for p, alts in json.load(open(os.path.join(OB, SHARDS[gene] % i))).items():
            full[int(p)] = alts
    done = set()
    f = os.path.join(LOCAL, f"ddg_{gene}_all.json")
    if os.path.exists(f):
        for r in json.load(open(f)):
            done.add((r["pos"], r["alt"]))
    miss = {}
    for p, alts in full.items():
        left = [(w, a) for (w, a) in alts if (p, a) not in done]
        if left:
            miss[str(p)] = left
    rem[gene] = miss
    print(f"{gene}: {len(miss)} positions, {sum(len(v) for v in miss.values())} variants remaining")

order = {}
for gene in rem:
    ks = list(rem[gene]); random.seed(42); random.shuffle(ks); order[gene] = ks

for slot, (idx, url, name) in enumerate(boxes):
    jobs = []
    for gene in ("JAK1", "TYK2"):          # JAK1 first: the bigger gap
        ks = order[gene][slot::len(boxes)]
        if ks:
            jobs.append({"gene": gene, "models": MODELS[gene],
                         "shard": {k: rem[gene][k] for k in ks}})
    payload = base64.b64encode(gzip.compress(json.dumps(jobs).encode())).decode()
    boot = f'''import os, gzip, base64, json, subprocess, sys
W="/tmp/ddg"; os.makedirs(W, exist_ok=True)
open(W+"/worker.py","w").write(base64.b64decode("{base64.b64encode(WORKER.encode()).decode()}").decode())
json.dump(json.loads(gzip.decompress(base64.b64decode("{payload}"))), open(W+"/jobs.json","w"))
alive=[l for l in subprocess.run(["ps","-eo","pid,args"],capture_output=True,text=True).stdout.splitlines()
       if "worker.py" in l and "grep" not in l]
try:
    import pyrosetta; ready=True
except ImportError:
    ready=False
print("pyrosetta ready:", ready)
if alive:
    print("ALREADY RUNNING:", len(alive), "- jobs.json refreshed")
elif ready:
    log=open(W+"/run.log","ab")
    p=subprocess.Popen([sys.executable,"-u",W+"/worker.py"],stdout=log,stderr=subprocess.STDOUT,
                       cwd=W, start_new_session=True)
    print("LAUNCHED pid", p.pid)
else:
    print("NOT LAUNCHED - pyrosetta still installing")
print("jobs:", [(x["gene"], len(x["shard"]), sum(len(v) for v in x["shard"].values()))
               for x in json.load(open(W+"/jobs.json"))])
'''
    open(T + f"deploy{idx}.py", "w").write(boot)
    print(f"  {name} (deploy{idx}): "
          f"{[(j['gene'], sum(len(v) for v in j['shard'].values())) for j in jobs]}")
