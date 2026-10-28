import json, os, sys, time, traceback
sys.path.insert(0, "/Users/chervov/analysis1"); os.chdir("/Users/chervov/analysis1")
import pipe, report

T = pipe.T
done = {}
if os.path.exists("results.json"):
    done = json.load(open("results.json"))
order = sorted(T.items(), key=lambda kv: (kv[1]["kind"] != "reference", kv[1]["gene"]))
for i, (acc, e) in enumerate(order, 1):
    if acc in done and os.path.exists(f"out/{e['gene']}.md"):
        print(f"[{i:>2}/{len(order)}] {e['gene']:<10} cached", flush=True); continue
    try:
        gn, err = pipe.gnomad(e["gene"])
        if gn is None:
            time.sleep(8); gn, err = pipe.gnomad(e["gene"])
        r = pipe.analyse(acc, e, gn or {})
        if r is None:
            print(f"[{i:>2}/{len(order)}] {e['gene']:<10} NO FEATURES", flush=True); continue
        r["gnomad_err"] = err
        open(f"out/{e['gene']}.md", "w").write(report.md(r))
        done[acc] = {k: v for k, v in r.items() if k not in ("domains",)}
        json.dump(done, open("results.json", "w"))
        c = r.get("cluster") or {}
        gf = c.get("gnomad_frac")
        print(f"[{i:>2}/{len(order)}] {e['gene']:<10} vars {r['n_variants']:>6,} | "
              f"iface {(r.get('iface') or {}).get('n', 0):>3} | clusters "
              f"{c.get('sizes', ['—','—'])} | gnomAD {r.get('gnomad_n',0):>5,}"
              f"{f' | depletion {gf[0]/gf[1]:.1f}x' if gf and gf[1] > 0 else ''}"
              f"{' | PG ' + str(len(r.get('proteingym') or [])) if r.get('proteingym') else ''}", flush=True)
    except Exception:
        print(f"[{i:>2}/{len(order)}] {e['gene']:<10} ERROR\n{traceback.format_exc()[:400]}", flush=True)
    time.sleep(1.5)
print(f"\nDONE {len(done)}/{len(order)}", flush=True)
