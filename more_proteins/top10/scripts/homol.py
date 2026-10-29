"""Parse phmmer output: per-target bit score, E-value, identity over aligned columns, coverage."""
import re, json, os, sys

ORDER = ["P29597","P23458","Q06124","P12931","P00519","Q06187","Q5S007","P13569","P08183","O00571"]
META = json.load(open("/Users/chervov/top10/meta.json"))
SEQS = json.load(open("/Users/chervov/top10/seqs.json"))

qline = re.compile(r"^(\s+\S+\s+\d+\s+)(\S+)\s+\d+\s*$")

def parse(acc):
    txt = open(f"{acc}.out").read().splitlines()
    # 1. full-sequence score table
    full = {}
    i = next(k for k,l in enumerate(txt) if l.startswith("Scores for complete sequences"))
    for l in txt[i+3:]:
        if not l.strip() or l.startswith("  ---"): continue
        if l.lstrip().startswith("Domain annotation") or l.startswith(">>"): break
        f = l.split()
        if len(f) < 9 or not f[0][0].isdigit(): continue
        m = re.match(r"sp\|(\w+)\|(\S+)$", f[8])
        if not m: continue
        full[m.group(1)] = dict(acc=m.group(1), name=m.group(2),
                                evalue=float(f[0]), score=float(f[1]),
                                ndom=int(f[7]), desc=" ".join(f[9:]))
    # 2. alignment identity, summed over reported domains
    cur = None; aln = {}
    k = 0
    while k < len(txt):
        l = txt[k]
        if l.startswith(">>"):
            m = re.match(r">> sp\|(\w+)\|", l); cur = m.group(1) if m else None
            k += 1; continue
        if cur and (mm := qline.match(l)) and l.split()[0].startswith(acc):
            off, qs = len(mm.group(1)), mm.group(2)
            match = txt[k+1][off:off+len(qs)] if k+1 < len(txt) else ""
            a = aln.setdefault(cur, [0,0,0])
            for c, q in zip(match, qs):
                if q == ".": continue          # insertion relative to the query
                a[1] += 1                      # aligned query column
                if c.isalpha(): a[0] += 1      # identical residue
                elif c == "+": a[2] += 1       # positive, not identical
            k += 4; continue
        k += 1
    rows = []
    for a, d in full.items():
        if a == acc: continue
        idn, cols, pos = aln.get(a, [0,0,0])
        if not cols: continue
        d.update(ident=100.0*idn/cols, simil=100.0*(idn+pos)/cols,
                 cols=cols, qcov=100.0*cols/len(SEQS[acc]))
        rows.append(d)
    rows.sort(key=lambda r: -r["score"])
    return rows

out = {}
for acc in ORDER:
    r = parse(acc)
    out[acc] = r[:10]
    g = META[acc]["gene"]
    print(f"\n=== {g} ({acc}), {len(SEQS[acc])} aa — {len(r)} human homologs at E<1e-3 ===")
    print(f"{'#':>2} {'gene/entry':<16}{'acc':<9}{'bits':>8}{'E-value':>11}{'%id':>7}{'%sim':>7}{'cols':>6}{'%qcov':>7}  description")
    for i, d in enumerate(r[:10], 1):
        print(f"{i:>2} {d['name'].replace('_HUMAN',''):<16}{d['acc']:<9}{d['score']:>8.1f}{d['evalue']:>11.1e}"
              f"{d['ident']:>7.1f}{d['simil']:>7.1f}{d['cols']:>6}{d['qcov']:>7.1f}  {d['desc'][:46]}")
json.dump(out, open("homologs.json","w"), indent=1)
print("\nhomologs.json written")
