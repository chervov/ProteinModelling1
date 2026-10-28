import json, os, sys, time, urllib.request, urllib.parse, csv
sys.path.insert(0,"/Users/chervov/analysis1"); os.chdir("/Users/chervov/analysis1")
T=json.load(open("targets.json")); SEQ=json.load(open("seqs.json"))
FIELDS=("dbnsfp.aa,dbnsfp.genename,dbnsfp.revel.score,dbnsfp.cadd.phred,dbnsfp.sift.score,"
        "dbnsfp.polyphen2.hvar.score,dbnsfp.metarnn.score,dbnsfp.vest4.score,dbnsfp.primateai.score,"
        "dbnsfp.mutationassessor.score,dbnsfp.provean.score,dbnsfp.gerp++.rs,dbnsfp.esm1b.score,"
        "dbnsfp.alphamissense.score")
SPEC=[("revel","revel","score"),("cadd","cadd","phred"),("sift","sift","score"),
      ("polyphen","polyphen2","hvar_score"),("metarnn","metarnn","score"),("vest4","vest4","score"),
      ("primateai","primateai","score"),("mutassessor","mutationassessor","score"),
      ("provean","provean","score"),("gerp","gerp++","rs"),("esm1b","esm1b","score"),
      ("am_dbnsfp","alphamissense","score")]
NAMES=[n for n,_,_ in SPEC]
def flat(v):
    if isinstance(v,list):
        for x in v:
            r=flat(x)
            if r is not None: return r
        return None
    return v
def getscore(b,key,path):
    o=b.get(key)
    if not isinstance(o,dict): return None
    if path=="hvar_score":
        h=o.get("hvar")
        return flat(h.get("score")) if isinstance(h,dict) else None
    return flat(o.get(path))
def norm_aa(aa):
    """yield (ref, alt, [candidate positions])"""
    items = aa if isinstance(aa,list) else [aa]
    for it in items:
        if not isinstance(it,dict): continue
        ref, alt = it.get("ref"), it.get("alt")
        pos = it.get("pos")
        pl = pos if isinstance(pos,list) else [pos]
        pl = [p for p in pl if isinstance(p,int)]
        if ref and alt and pl: yield str(ref), str(alt), pl
def fetch(gene, acc):
    seq=SEQ.get(acc,""); out={}; frm=0; skipped=0; total=None
    while True:
        q=urllib.parse.urlencode({"q":f"dbnsfp.genename:{gene}","fields":FIELDS,"size":"1000","from":str(frm)})
        d=None
        for att in range(4):
            try:
                d=json.load(urllib.request.urlopen(f"https://myvariant.info/v1/query?{q}",timeout=240)); break
            except Exception:
                if att==3: return out,skipped,"fetch failed"
                time.sleep(6+6*att)
        total=d.get("total",0); hits=d.get("hits",[])
        if not hits: break
        for h in hits:
            b=h.get("dbnsfp") or {}
            gn=b.get("genename"); gn=gn if isinstance(gn,str) else flat(gn)
            if gn and str(gn).upper()!=gene.upper(): continue
            vals={n:getscore(b,k,p) for n,k,p in SPEC}
            for ref,alt,pl in norm_aa(b.get("aa")):
                if len(alt)!=1 or len(ref)!=1: continue
                # disambiguate the transcript position by matching the canonical sequence
                good=[p for p in pl if 1<=p<=len(seq) and seq[p-1]==ref]
                if not good: skipped+=1; continue
                p=good[0]
                rec=out.setdefault((p,alt),{"wt":ref})
                for n in NAMES:
                    if vals[n] is not None and n not in rec:
                        try: rec[n]=float(vals[n])
                        except (TypeError,ValueError): pass
        frm+=len(hits)
        if len(hits)<1000 or frm>=total: break
        time.sleep(0.35)
    return out,skipped,None
if __name__=="__main__":
    for i,(acc,e) in enumerate(sorted(T.items(),key=lambda kv:kv[1]["gene"]),1):
        p=f"feat/{acc}.dbnsfp.csv"
        if os.path.exists(p) and os.path.getsize(p)>200:
            print(f"[{i:>2}/54] {e['gene']:<10} cached",flush=True); continue
        try: D,sk,err=fetch(e["gene"],acc)
        except Exception as ex:
            print(f"[{i:>2}/54] {e['gene']:<10} ERROR {type(ex).__name__} {str(ex)[:60]}",flush=True); continue
        with open(p,"w",newline="") as fh:
            w=csv.writer(fh); w.writerow(["pos","wt","alt"]+NAMES)
            for (pos,alt),v in sorted(D.items()):
                w.writerow([pos,v.get("wt",""),alt]+[v.get(n,"") for n in NAMES])
        cov={n:sum(1 for v in D.values() if n in v) for n in NAMES}
        print(f"[{i:>2}/54] {e['gene']:<10} {len(D):>6,} vars | skipped(seq mismatch) {sk:>5,} | "
              +" ".join(f"{n[:5]}:{cov[n]}" for n in ('revel','cadd','sift','metarnn','esm1b','gerp'))
              +(f" | {err}" if err else ""),flush=True)
        time.sleep(0.8)
    print("DBNSFP DONE",flush=True)
