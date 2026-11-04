"""CADD, SIFT and ClinPred for TYK2, from dbNSFP via the myvariant.info API.

Three of the paper's eleven features come from dbNSFP. The full dbNSFP release is tens of
gigabytes; myvariant.info is its standard programmatic interface and serves the same records by
gene, which is what makes this usable for an arbitrary protein.

**Expect ~31% coverage, and it is not a fetching problem.** dbNSFP is built from all possible
*single*-nucleotide changes. Nine SNVs per codon (3 positions x 3 alternates) reach at most ~6 of
the 19 possible amino-acid substitutions, so about 31% is dbNSFP's ceiling by construction and no
query can exceed it. The JAK1 directory established this by comparing a gene-name query with a
genomic-region query and getting identical record sets
(`JAK1/clustering/test_sift_coverage.py`).

**Many-to-one.** Several nucleotide changes can produce the same amino-acid substitution, so a
substitution may appear more than once. Values are aggregated with `max`, and the within-
substitution spread is printed first so the choice is visible rather than silent. For protein-level
scores (SIFT, ClinPred) the spread should be ~0; for CADD, a nucleotide-level score, it genuinely
is not.

Writes tyk2_cadd.csv, tyk2_sift.csv, tyk2_clinpred.csv.
"""
import csv
import json
import pathlib
import time
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).parent
ACC, GENE = "P29597", "TYK2"
FIELDS = ("dbnsfp.aa,dbnsfp.genename,dbnsfp.sift,dbnsfp.sift4g,dbnsfp.clinpred,"
          "dbnsfp.cadd.phred,cadd.phred")


def get(url, tries=4):
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as fh:
                return json.load(fh)
        except Exception as exc:
            if k == tries - 1:
                raise
            print(f"    retry after {exc}")
            time.sleep(3)


def fetch_all():
    q = urllib.parse.quote(f"dbnsfp.genename:{GENE}")
    base = (f"https://myvariant.info/v1/query?q={q}"
            f"&fields={urllib.parse.quote(FIELDS)}&size=1000")
    total = get(base + "&size=0")["total"]
    print(f"  dbnsfp.genename:{GENE} -> {total:,} records")
    hits, start = [], 0
    while start < total:
        d = get(f"{base}&from={start}")
        got = d.get("hits", [])
        if not got:
            break
        hits += got
        start += len(got)
        print(f"    fetched {start:,}/{total:,}", flush=True)
    return hits


def num(x):
    if isinstance(x, list):
        x = next((v for v in x if v is not None), None)
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main():
    seq = (HERE / f"TYK2_{ACC}_1187aa.txt").read_text().splitlines()[1]
    print(f"TYK2 {ACC}, {len(seq)} aa")
    print("fetching dbNSFP records through myvariant.info")
    hits = fetch_all()

    raw = []
    skipped = 0
    for h in hits:
        b = h.get("dbnsfp") or {}
        aa = b.get("aa") or {}
        aas = aa if isinstance(aa, list) else [aa]
        # aa.pos may list several transcript positions; keep the one whose wild type
        # matches the canonical sequence. This is the check that caught a bad join earlier
        # in this project.
        hit = None
        for a in aas:
            for p in (a.get("pos") if isinstance(a.get("pos"), list) else [a.get("pos")]):
                try:
                    p = int(p)
                except (TypeError, ValueError):
                    continue
                if 1 <= p <= len(seq) and seq[p - 1] == a.get("ref") and a.get("alt"):
                    hit = (p, a["ref"], a["alt"])
                    break
            if hit:
                break
        if not hit:
            skipped += 1
            continue
        pos, wt, alt = hit
        if wt == alt:
            continue
        sift = b.get("sift") or {}
        sift4g = b.get("sift4g") or {}
        cp = b.get("clinpred") or {}
        raw.append({
            "variant": f"{wt}{pos}{alt}",
            "cadd": num((h.get("cadd") or {}).get("phred")) or num((b.get("cadd") or {}).get("phred")),
            "sift": num(sift.get("score")) if sift.get("score") is not None else num(sift4g.get("score")),
            "clinpred": num(cp.get("score")),
        })
    print(f"  usable records {len(raw):,}; {skipped:,} skipped "
          f"(no transcript position whose wild type matches the sequence)")

    # within-substitution spread, before aggregating
    by = {}
    for r in raw:
        by.setdefault(r["variant"], []).append(r)
    print("\nwithin-substitution spread across nucleotide routes "
          "(0 expected for a protein-level score):")
    for col in ("clinpred", "sift", "cadd"):
        groups = {v: [r[col] for r in rs if r[col] is not None] for v, rs in by.items()}
        groups = {v: g for v, g in groups.items() if g}
        multi = sum(1 for g in groups.values() if len(g) > 1)
        spread = max((max(g) - min(g) for g in groups.values() if len(g) > 1), default=0.0)
        print(f"   {col:<10} substitutions={len(groups):>6,}  "
              f"reachable by >1 SNV={multi:>4}  max spread={spread:.4f}")

    agg = {v: {c: max([r[c] for r in rs if r[c] is not None], default=None)
               for c in ("cadd", "sift", "clinpred")} for v, rs in by.items()}

    universe = [r["variant"] for r in csv.DictReader(open(HERE / "tyk2_variant_universe.csv"))]
    for col, fname in (("cadd", "tyk2_cadd.csv"),
                       ("sift", "tyk2_sift.csv"),
                       ("clinpred", "tyk2_clinpred.csv")):
        out = HERE / fname
        n = 0
        with open(out, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["index", "variant", "wt", "pos", "alt", col])
            for i, v in enumerate(universe, 1):
                val = (agg.get(v) or {}).get(col)
                n += val is not None
                w.writerow([i, v, v[0], v[1:-1], v[-1], "" if val is None else f"{val:g}"])
        vals = [x for x in ((agg.get(v) or {}).get(col) for v in universe) if x is not None]
        print(f"\nwrote {fname}: {len(universe):,} rows, {n:,} populated "
              f"({100 * n / len(universe):.1f}%)")
        print(f"   range {min(vals):g} .. {max(vals):g}")


if __name__ == "__main__":
    main()
