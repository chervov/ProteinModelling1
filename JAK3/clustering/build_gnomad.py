"""gnomAD r4 population frequencies for JAK3.

Not a clustering feature - **no feature sees this**. It is one of the two external criteria that
have to substitute for the Dataset EV1 target JAK3 does not have: if an unsupervised split of
predictor scores is biologically meaningful, variants the population tolerates should fall
preferentially in one cluster.

Source: the public gnomAD GraphQL endpoint, queried by gene symbol against GRCh38. No key.

Two things are done deliberately, both learned from the JAK1 run
(`JAK1/clustering/build_gnomad_jak1_info.md`):

  1. The wild-type residue from gnomAD's HGVSp is **verified against the pinned sequence**.
     Matching on (position, alt) alone silently admitted 45 JAK1 records from a different
     transcript.

  2. "Observed" means **allele count > 0, tested explicitly**. The obvious idiom
     `ex.get("af") or ge.get("af")` appears to exclude zero-frequency sites only because 0.0 is
     falsy, and it leaks the genome-only cases. On JAK1 that admitted 5 sites that had been
     sequenced at ~1.46 M alleles and never observed.

Writes jak3_gnomad.csv.
"""
import csv
import json
import pathlib
import urllib.request

HERE = pathlib.Path(__file__).parent
ACC, GENE = "P52333", "JAK3"
AA3 = {"Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E",
       "Gly": "G", "His": "H", "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F",
       "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V", "Ter": "*"}
QUERY = ("query($g:String!){gene(gene_symbol:$g,reference_genome:GRCh38){"
         "variants(dataset:gnomad_r4){consequence hgvsp exome{af ac an} genome{af ac an}}}}")


def main():
    seq = (HERE / f"JAK3_{ACC}_1124aa.txt").read_text().splitlines()[1]
    print(f"JAK3 {ACC}, {len(seq)} aa")

    body = json.dumps({"query": QUERY, "variables": {"g": GENE}}).encode()
    req = urllib.request.Request("https://gnomad.broadinstitute.org/api", data=body,
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "research-script"})
    with urllib.request.urlopen(req, timeout=600) as fh:
        variants = json.load(fh)["data"]["gene"]["variants"] or []
    print(f"  gnomAD r4 returned {len(variants):,} variants for {GENE}, all classes")

    best, mismatch, zero_ac, nonmis = {}, [], 0, 0
    for v in variants:
        if v.get("consequence") != "missense_variant":
            nonmis += 1
            continue
        h = v.get("hgvsp") or ""
        if not h.startswith("p."):
            continue
        b = h[2:]
        wt3, rest = b[:3], b[3:]
        digits = "".join(c for c in rest if c.isdigit())
        alt3 = rest[len(digits):]
        if not digits or wt3 not in AA3 or alt3 not in AA3:
            continue
        pos, wt, alt = int(digits), AA3[wt3], AA3[alt3]
        if not (1 <= pos <= len(seq)) or seq[pos - 1] != wt:
            mismatch.append(pos)
            continue
        ex, ge = v.get("exome") or {}, v.get("genome") or {}
        ac = (ex.get("ac") or 0) + (ge.get("ac") or 0)
        an = max(ex.get("an") or 0, ge.get("an") or 0)
        afs = [x.get("af") for x in (ex, ge) if x.get("af") is not None]
        af = max(afs) if afs else None
        if af is None or ac == 0:
            zero_ac += 1
            continue
        k = f"{wt}{pos}{alt}"
        if k not in best or af > best[k][0]:
            best[k] = (af, ac, an)

    print(f"  missense {len(variants) - nonmis:,}; excluded {len(mismatch)} on wild-type "
          f"mismatch, {zero_ac} on allele count 0 (sequenced, never observed)")
    if mismatch:
        print(f"    mismatches at positions {min(mismatch)}-{max(mismatch)}")
    print(f"  accepted {len(best):,} distinct substitutions")

    universe = [r["variant"] for r in csv.DictReader(open(HERE / "jak3_variant_universe.csv"))]
    out = HERE / "jak3_gnomad.csv"
    n = 0
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["index", "variant", "wt", "pos", "alt",
                    "gnomad_af", "gnomad_ac", "gnomad_an", "in_gnomad"])
        for i, v in enumerate(universe, 1):
            hit = best.get(v)
            n += hit is not None
            w.writerow([i, v, v[0], v[1:-1], v[-1],
                        "" if not hit else f"{hit[0]:.3E}",
                        "" if not hit else hit[1], "" if not hit else hit[2],
                        1 if hit else 0])
    print(f"\nwrote {out.name}: {len(universe):,} rows, {n:,} observed in gnomAD "
          f"({100 * n / len(universe):.2f}%)")
    afs = [h[0] for h in best.values()]
    import statistics
    print(f"  allele frequency {min(afs):.2E} .. {max(afs):.2E}, median {statistics.median(afs):.2E}")
    common = sum(1 for a in afs if a > 1e-4)
    print(f"  {common} above AF 1e-4; {sum(1 for a in afs if a > 1e-3)} above 1e-3")


if __name__ == "__main__":
    main()
