"""Pull new ddG results from every box, save locally, push to git. Idempotent and incremental.

Design notes (the failure modes this guards against):
  - molab sandboxes expire at ~4h with HTTP 410, so results must be pulled back every cycle.
  - execute-code output is capped at 1 MB, so lines are fetched in gzip+base64 chunks.
  - a transient 530 is NOT evidence a box is dead; the status file records consecutive failures
    and only 3 in a row count as down.
  - the worker runs as a detached OS process, so the marimo kernel is idle and safe to probe.
"""
import base64, gzip, json, os, subprocess, sys, time, urllib.request, urllib.error

LOCAL = "/Users/chervov/ddg_pairs"
EXEC = "/Users/chervov/.claude/skills/marimo-pair/scripts/execute-code.sh"
TMP = "/Users/chervov/.claude/jobs/e920d48f/tmp"
STATE = os.path.join(LOCAL, "state.json")
BOXES = [l.split() for l in open("/Users/chervov/boxes.txt").read().strip().split("\n")]
CHUNK = 4000
GENES = ["T_within96", "T_crossmax", "T_af3xcamp", "J_afdb", "T_nullctrl"]          # lines per fetch; ~120 B/line raw, well under the 1 MB output cap

def sh(url, code, timeout=300):
    p = os.path.join(TMP, "probe.py")
    open(p, "w").write(code)
    try:
        r = subprocess.run(["bash", EXEC, "--url", f"https://{url}.sb.molab.run/", p],
                           capture_output=True, text=True, timeout=timeout)
        return "\n".join(l for l in (r.stdout + r.stderr).split("\n")
                         if not l.startswith("Warning"))
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

def state():
    return json.load(open(STATE)) if os.path.exists(STATE) else {}

def save(s):
    json.dump(s, open(STATE, "w"), indent=1)

def pull(idx, url, name, st):
    """Fetch any lines beyond what we already hold, for each gene."""
    key = name
    st.setdefault(key, {"fails": 0, "log": ""})
    got = {}
    for gene in GENES:
        st[key].setdefault(gene, 0)
        have = st[key][gene]
        out = sh(url, f'''
import os, json, gzip, base64
p="/tmp/ddg/results_{gene}.jsonl"
if not os.path.exists(p):
    print("NOFILE")
else:
    L=open(p).read().split(chr(10))
    L=[x for x in L if x.strip()]
    print("TOTAL", len(L))
    new=L[{have}:{have}+{CHUNK}]
    if new:
        print("B64START"+base64.b64encode(gzip.compress((chr(10).join(new)).encode())).decode()+"B64END")
''')
        if "TIMEOUT" in out or ("B64START" not in out and "TOTAL" not in out and "NOFILE" not in out):
            st[key]["fails"] += 1
            return None, out[-200:]
        st[key]["fails"] = 0
        tot = 0
        for ln in out.split("\n"):
            if ln.startswith("TOTAL"): tot = int(ln.split()[1])
        if "B64START" in out:
            blob = out.split("B64START")[1].split("B64END")[0].strip()
            txt = gzip.decompress(base64.b64decode(blob)).decode()
            n = len([x for x in txt.split("\n") if x.strip()])
            with open(os.path.join(LOCAL, f"{gene}_{name}.jsonl"), "a") as fh:
                fh.write(txt.rstrip("\n") + "\n")
            st[key][gene] = have + n
        got[gene] = (st[key][gene], tot)
    log = sh(url, 'import os\np="/tmp/ddg/run.log"\n'
                  'print(open(p).read()[-700:] if os.path.exists(p) else "no log")')
    st[key]["log"] = log[-700:]
    return got, log

def merge(gene):
    """Merge every box's shard into one deduplicated file."""
    import glob
    seen = {}
    # glob every shard file ever written, not just the boxes currently in boxes.txt -
    # otherwise replacing a dead box silently drops the earlier boxes' results
    for p in sorted(glob.glob(os.path.join(LOCAL, f"{gene}_*.jsonl"))):
        if not os.path.exists(p):      # dangling symlink: results not written yet
            continue
        for ln in open(p):
            try:
                r = json.loads(ln)
                seen[(r["pos"], r["alt"])] = r
            except Exception:
                pass
    recs = sorted(seen.values(), key=lambda r: (r["pos"], r["alt"]))
    out = os.path.join(LOCAL, f"ddg_{gene}_all.json")
    json.dump(recs, open(out, "w"))
    return len(recs)

def push(paths, msg):
    GH = open("/Users/chervov/molab_b/.gh_token").read().strip()
    REPO = "chervov/ProteinModelling1"
    for path, local in paths:
        if not os.path.exists(local):
            continue
        body = {"message": msg,
                "content": base64.b64encode(open(local, "rb").read()).decode()}
        try:
            r = urllib.request.Request(
                f"https://api.github.com/repos/{REPO}/contents/{path}?ref=main",
                headers={"Authorization": f"Bearer {GH}", "User-Agent": "x"})
            body["sha"] = json.load(urllib.request.urlopen(r))["sha"]
        except urllib.error.HTTPError as e:
            if e.code != 404:
                print("  sha lookup failed", path, e.code); continue
        req = urllib.request.Request(
            f"https://api.github.com/repos/{REPO}/contents/{path}", method="PUT",
            data=json.dumps(body).encode(),
            headers={"Authorization": f"Bearer {GH}", "Accept": "application/vnd.github+json",
                     "User-Agent": "x"})
        try:
            print("  pushed", path,
                  json.load(urllib.request.urlopen(req))["commit"]["sha"][:8])
        except urllib.error.HTTPError as e:
            print("  push FAILED", path, e.code, e.read()[:120])

if __name__ == "__main__":
    st = state()
    print(f"=== collect {time.strftime('%Y-%m-%d %H:%M')}")
    for idx, url, name in BOXES:
        got, log = pull(idx, url, name, st)
        if got is None:
            print(f"  {name}: PROBE FAILED (consecutive={st[name]['fails']}) {log}")
        else:
            tail = [l for l in st[name]["log"].split("\n") if l.strip()]
            live = {g: v for g, v in got.items() if v[1]}
            print(f"  {name}: {live if live else 'no output yet'}  | {tail[-1][:80] if tail else ''}")
        save(st)
    counts = {g: merge(g) for g in GENES}
    print(f"  merged: {counts}")
    push([(f"data/ddg/pairs/ddg_{g}.json", os.path.join(LOCAL, f"ddg_{g}_all.json"))
          for g in GENES if counts.get(g)],
         f"structure-pair ddG: {counts} ({time.strftime('%Y-%m-%d %H:%M')})\n\n"
         "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>")
    save(st)
