"""Pick the two extreme conformations per protein for dual-state ddG."""
import json, os, sys
sys.path.insert(0,'/Users/chervov/top10'); os.chdir('/Users/chervov/top10')
M=json.load(open("meta.json"))
sel={}
for acc,rec in M.items():
    mv=rec.get("movement") or {}
    if not mv: continue
    # the pair with the largest spread that actually forms contacts somewhere
    cands=[(k,v) for k,v in mv.items() if v["cmax"]>=8]
    if not cands: cands=list(mv.items())
    k,v=max(cands,key=lambda kv:kv[1]["spread"])
    byl={r["label"]:r for r in rec["geom_all"]}
    # compact = most contacts for that pair; extended = fewest
    have=[r for r in rec["geom_all"] if k in r["pairs"]]
    comp=max(have,key=lambda r:r["pairs"][k]["contacts"])
    ext =min(have,key=lambda r:r["pairs"][k]["contacts"])
    if comp["label"]==ext["label"] and len(have)>1:
        comp=min(have,key=lambda r:r["pairs"][k]["dist"]); ext=max(have,key=lambda r:r["pairs"][k]["dist"])
    fc=next(s for s in rec["structures"] if s["label"]==comp["label"])
    fe=next(s for s in rec["structures"] if s["label"]==ext["label"])
    sel[acc]=dict(gene=rec["gene"],pair=k,
        closed=dict(label=comp["label"],file=fc["file"],chain=fc.get("chain"),
                    dist=comp["pairs"][k]["dist"],contacts=comp["pairs"][k]["contacts"]),
        open=dict(label=ext["label"],file=fe["file"],chain=fe.get("chain"),
                  dist=ext["pairs"][k]["dist"],contacts=ext["pairs"][k]["contacts"]),
        iface=sorted(set(comp["pairs"][k]["resA"])|set(comp["pairs"][k]["resB"])))
    print(f"{rec['gene']:<8}{k.replace('|','↔')[:44]:<46}")
    print(f"         CLOSED  {comp['label'][:40]:<42} d={comp['pairs'][k]['dist']:>6.1f} contacts={comp['pairs'][k]['contacts']:>3}")
    print(f"         OPEN    {ext['label'][:40]:<42} d={ext['pairs'][k]['dist']:>6.1f} contacts={ext['pairs'][k]['contacts']:>3}")
json.dump(sel,open("states.json","w"),indent=1)
print(f"\n{len(sel)} proteins with a state pair")
