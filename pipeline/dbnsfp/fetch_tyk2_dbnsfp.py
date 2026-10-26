"""Fetch dbNSFP predictor scores for every TYK2 missense SNV from myvariant.info.

Ports scripts/dbnsfp_fetch.ps1 (archive 24-25 Oct) to Python. Reduces each record to the canonical
Ensembl transcript so one protein change gets one row, and keeps CADD phred and MetaRNN - the two
features that until now existed only in the curated 2,247-variant file.
"""
import json, time, urllib.request, urllib.parse, csv, sys, os

GENE = "TYK2"
CANON = "ENST00000525621"          # Ensembl canonical, confirmed via REST
OUT = "/Users/chervov/dbnsfp_fetch/tyk2_dbnsfp_genomewide.csv"
FIELDS = ",".join([
    "dbnsfp.aa.ref","dbnsfp.aa.alt","dbnsfp.aa.pos","dbnsfp.ensembl.transcriptid",
    "dbnsfp.revel.score","dbnsfp.sift.score","dbnsfp.polyphen2.hvar.score",
    "dbnsfp.cadd.phred","cadd.phred","dbnsfp.metarnn.score","dbnsfp.esm1b.score",
    "dbnsfp.alphamissense.score","dbnsfp.primateai.score","dbnsfp.vest4.score",
    "dbnsfp.mutationassessor.score","dbnsfp.provean.score","dbnsfp.gerp.91_mammals.score",
])

def get(url, tries=5):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                return json.load(r)
        except Exception as e:
            print(f"  retry {i+1}/{tries}: {e}", flush=True)
            time.sleep(5 * (i + 1))
    raise RuntimeError("giving up on " + url[:120])

def pick(v, i):
    a = v if isinstance(v, list) else ([] if v is None else [v])
    if not a: return None
    return a[i] if 0 <= i < len(a) else a[0]

print(f"querying myvariant.info for {GENE} (canonical {CANON})", flush=True)
base = "https://myvariant.info/v1/query"
url = f"{base}?q=dbnsfp.genename:{GENE}&fields={urllib.parse.quote(FIELDS)}&fetch_all=true"
RAW = "/Users/chervov/dbnsfp_fetch/raw_docs.json"
if os.path.exists(RAW) and os.path.getsize(RAW) > 100000:
    docs = json.load(open(RAW))
    print(f"reusing cached download: {len(docs):,} documents", flush=True)
else:
    docs, r = [], get(url)
    total = r.get("total")
    while r.get("hits"):
        docs.extend(r["hits"])
        print(f"  {len(docs):,} / {total:,} documents", flush=True)
        sid = r.get("_scroll_id")
        if not sid: break
        r = get(f"{base}?scroll_id={sid}")
    json.dump(docs, open(RAW, "w"))
    print(f"fetched {len(docs):,} documents, cached to {RAW}", flush=True)

rows, skipped = {}, 0
for d in docs:
    n = d.get("dbnsfp")
    if not n: skipped += 1; continue
    def flat(obj, key):
        """dbNSFP nests these as dict or list-of-dicts; return a flat list of values."""
        if obj is None: return []
        items = obj if isinstance(obj, list) else [obj]
        out = []
        for it in items:
            if not isinstance(it, dict): continue
            v = it.get(key)
            out.extend(v if isinstance(v, list) else ([] if v is None else [v]))
        return out
    tx = flat(n.get("ensembl"), "transcriptid")
    try: i = tx.index(CANON)
    except ValueError: skipped += 1; continue
    aa = n.get("aa")
    POS, REF, ALT = flat(aa,"pos"), flat(aa,"ref"), flat(aa,"alt")
    pos = POS[i] if i < len(POS) else (POS[0] if POS else None)
    ref = REF[i] if i < len(REF) else (REF[0] if REF else None)
    alt = ALT[i] if i < len(ALT) else (ALT[0] if ALT else None)
    if not pos or alt in (None, ref): continue
    if alt == "X": alt = "*"
    cadd = d.get("cadd", {}).get("phred") or n.get("cadd", {}).get("phred")
    def s(path, idx=i):
        parts = path.split(".")
        cur = n
        for p in parts[:-1]:
            if isinstance(cur, list): cur = cur[0] if cur else None
            cur = (cur or {}).get(p) if isinstance(cur, dict) else None
        vals = flat(cur, parts[-1]) if cur is not None else []
        if not vals: return None
        return vals[idx] if idx < len(vals) else vals[0]
    rows[f"{ref}{pos}{alt}"] = dict(
        variant=f"{ref}{pos}{alt}", pos=pos, wt=ref, alt=alt,
        revel=s("revel.score"), cadd_phred=pick(cadd, 0), sift=s("sift.score"),
        polyphen2_hvar=s("polyphen2.hvar.score"), metarnn=s("metarnn.score"),
        esm1b=s("esm1b.score"), alphamissense=s("alphamissense.score"),
        primateai=s("primateai.score"), vest4=s("vest4.score"),
        mutationassessor=s("mutationassessor.score"), provean=s("provean.score"),
        gerp=s("gerp.91_mammals.score"))
cols = ["variant","pos","wt","alt","revel","cadd_phred","sift","polyphen2_hvar","metarnn",
        "esm1b","alphamissense","primateai","vest4","mutationassessor","provean","gerp"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for k in sorted(rows, key=lambda v: (int(rows[v]["pos"]), rows[v]["alt"])):
        w.writerow(rows[k])
print(f"\nwrote {OUT}: {len(rows):,} unique protein changes ({skipped:,} docs skipped)", flush=True)
for c in cols[4:]:
    n = sum(1 for v in rows.values() if v[c] not in (None, ""))
    print(f"  {c:18s} {n:>7,}  {100*n/max(len(rows),1):>5.1f}%", flush=True)
print("FETCH_DONE", flush=True)
