"""One overnight cycle: ensure each box's worker is alive, pull results, push, maybe analyse."""
import json, os, subprocess, sys, time
sys.path.insert(0, "/Users/chervov")
import collect as C

TMP = "/Users/chervov/.claude/jobs/e920d48f/tmp"

def alive(url):
    """Is a worker process running? Returns True/False/None (None = probe failed)."""
    out = C.sh(url, '''
import subprocess, os, json
ps=subprocess.run(["ps","-eo","pid,etimes,args"],capture_output=True,text=True).stdout
w=[l for l in ps.splitlines() if "worker.py" in l and "grep" not in l]
print("WORKERS", len(w))
jp="/tmp/ddg/jobs.json"
genes=[j["gene"] for j in json.load(open(jp))] if os.path.exists(jp) else []
print("GENES", ",".join(genes))
for g in genes:
    print("DONE_"+g, os.path.exists(f"/tmp/ddg/DONE_{g}"))
''')
    if "WORKERS" not in out:
        return None, out[-150:]
    lines = out.split("\n")
    n = int([l for l in lines if l.startswith("WORKERS")][0].split()[1])
    gl = [l for l in lines if l.startswith("GENES")]
    genes = [g for g in (gl[0].split(" ", 1)[1].split(",") if gl and " " in gl[0] else []) if g]
    done = {}
    for g in genes:
        r = [l for l in lines if l.startswith("DONE_" + g + " ")]
        done[g] = bool(r) and "True" in r[0]
    return (n > 0, done)

def redeploy(idx, url, name):
    p = os.path.join(TMP, f"deploy{idx}.py")
    out = C.sh(url, open(p).read(), timeout=300)
    print(f"  {name}: REDEPLOY -> {[l for l in out.split(chr(10)) if 'LAUNCH' in l or 'ALREADY' in l]}")

if __name__ == "__main__":
    st = C.state()
    print(f"=== cycle {time.strftime('%Y-%m-%d %H:%M')}")
    for idx, url, name in C.BOXES:
        a = alive(url)
        if a[0] is None:
            st.setdefault(name, {}).setdefault("fails", 0)
            st[name]["fails"] = st[name].get("fails", 0) + 1
            # 3 consecutive failures, not 1 - molab returns transient 530s
            flag = "DEAD (needs a new sandbox URL)" if st[name]["fails"] >= 3 else "transient"
            print(f"  {name}: probe failed ({st[name]['fails']}x) {flag}")
            C.save(st)
            continue
        running, done = a
        if not running and not (done and all(done.values())):
            print(f"  {name}: worker not running, shard incomplete -> relaunching")
            redeploy(idx, url, name)
        elif not running:
            print(f"  {name}: all jobs complete")
    # ESCALATE: if every box is dead and work remains, say so out loud instead of spinning.
    # The overnight run of 2026-10-22 lost ~8h because this was only written to a log.
    ndead = sum(1 for _, _, n in C.BOXES if st.get(n, {}).get("fails", 0) >= 3)
    if ndead == len(C.BOXES):
        st["_dead_cycles"] = st.get("_dead_cycles", 0) + 1
        if not st.get("_escalated"):
            msg = (f"All {ndead} molab boxes expired (410). ddG run stalled - "
                   f"need new sandbox URLs to resume.")
            open("/Users/chervov/ddg_overnight/STALLED.txt", "w").write(
                f"{time.strftime('%Y-%m-%d %H:%M')} {msg}\n")
            print(f"  *** ESCALATION: {msg}")
            st["_escalated"] = True
            C.save(st)
        # stop burning cycles on dead boxes after 3 confirmations
        if st.get("_dead_cycles", 0) >= 3:
            print("  *** all boxes dead for 3 cycles - exiting loop rather than spinning")
            C.save(st)
            subprocess.run([sys.executable, "/Users/chervov/collect.py"])
            sys.exit(42)
    else:
        st["_dead_cycles"] = 0; st["_escalated"] = False
    C.save(st)
    print("--- pulling results")
    subprocess.run([sys.executable, "/Users/chervov/collect.py"])
    # analyse + regenerate the report whenever the merged set has grown by >=200 variants
    n = 0
    for g in C.GENES:
        f = f"/Users/chervov/ddg_pairs/ddg_{g}_all.json"
        if os.path.exists(f):
            n += len(json.load(open(f)))
    last = st.get("_analysed", 0)
    if n - last >= 200:
        print(f"--- analysing ({n} variants merged, last analysed at {last})")
        subprocess.run([sys.executable, "/Users/chervov/analyse_pairs.py"])
        st["_analysed"] = n
        C.save(st)
    else:
        print(f"--- {n} variants merged; no analysis yet (need +200 over {last})")
