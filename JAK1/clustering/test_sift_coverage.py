"""Does querying MyVariant by genomic region beat querying by gene name?

The repo's features came from q=dbnsfp.genename:JAK1 and reached 6,873 substitutions with
SIFT (31.3%). The paper reports 56.3%. If the difference is query strategy, a region query
should return more; if it is a different dbNSFP build, it should return the same.

dbNSFP in MyVariant is keyed on hg19, so the region has to be the GRCh37 locus.
"""
import time

import requests

MV = "https://myvariant.info/v1/query"
# the amino-acid fields live under dbnsfp.aa (ref/alt/pos), NOT as top-level aaref/aaalt/aapos
FIELDS = "dbnsfp.genename,dbnsfp.sift,dbnsfp.sift4g,dbnsfp.polyphen2,dbnsfp.clinpred,dbnsfp.aa"


def ens37(path):
    for a in range(1, 5):
        try:
            r = requests.get(f"https://grch37.rest.ensembl.org{path}",
                             headers={"Content-Type": "application/json"}, timeout=120)
            r.raise_for_status()
            return r.json()
        except Exception as exc:                            # noqa: BLE001
            print(f"   ensembl37 attempt {a}: {type(exc).__name__}")
            time.sleep(4 * a)
    raise SystemExit("could not reach GRCh37 Ensembl")


g = ens37("/lookup/symbol/homo_sapiens/JAK1?expand=1")
chrom, lo, hi = g["seq_region_name"], g["start"], g["end"]
print(f"JAK1 GRCh37: chr{chrom}:{lo:,}-{hi:,}  ({hi - lo + 1:,} bp, strand {g['strand']:+d})")


def first(v):
    """dbNSFP packs one value per transcript; take the first."""
    while isinstance(v, list):
        v = v[0] if v else None
    return v


def fetch(q, label):
    """Scroll a MyVariant query; collect unique substitutions per predictor."""
    got = {k: set() for k in ("sift", "sift4g", "polyphen2", "clinpred", "any")}
    seen, total, scroll = 0, None, None
    while True:
        for attempt in (1, 2, 3):
            try:
                # the scroll continuation must still carry `fields`, or later pages
                # come back without the subdocuments we asked for
                p = ({"scroll_id": scroll, "fields": FIELDS} if scroll
                     else {"q": q, "fields": FIELDS, "fetch_all": "true"})
                r = requests.get(MV, params=p, timeout=300)
                r.raise_for_status()
                j = r.json()
                break
            except Exception as exc:                        # noqa: BLE001
                if attempt == 3:
                    raise
                print(f"      retry {attempt}: {type(exc).__name__}")
                time.sleep(5 * attempt)
        if total is None:
            total = j.get("total")
            print(f"   [{label}] total hits reported: {total:,}")
        hits = j.get("hits", [])
        if not hits:
            break
        for h in hits:
            d = h.get("dbnsfp")
            if not d:
                continue
            seen += 1
            aa = d.get("aa") or {}
            ref, alt, pos = first(aa.get("ref")), first(aa.get("alt")), first(aa.get("pos"))
            try:
                pos = int(pos)
            except (TypeError, ValueError):
                continue
            if not (ref and alt and ref != alt and 1 <= pos <= 1154):
                continue
            vid = f"{ref}{pos}{alt}"
            got["any"].add(vid)
            if (d.get("sift") or {}).get("score") is not None:
                got["sift"].add(vid)
            if (d.get("sift4g") or {}).get("score") is not None:
                got["sift4g"].add(vid)
            if ((d.get("polyphen2") or {}).get("hvar") or {}).get("score") is not None:
                got["polyphen2"].add(vid)
            if (d.get("clinpred") or {}).get("score") is not None:
                got["clinpred"].add(vid)
        scroll = j.get("_scroll_id")
        if not scroll:
            break
    print(f"   [{label}] dbNSFP records {seen:,}; any-aa {len(got['any']):,}")
    for k in ("sift", "sift4g", "polyphen2", "clinpred"):
        print(f"      {k:10s} {len(got[k]):6,} ({len(got[k]) / 21926:5.1%})")
    return got["sift"]


by_gene = fetch("dbnsfp.genename:JAK1", "gene name")
by_region = fetch(f"chr{chrom}:{lo}-{hi}", "genomic region")

print(f"\ngene name : {len(by_gene):,}")
print(f"region    : {len(by_region):,}")
print(f"region only: {len(by_region - by_gene):,}   gene only: {len(by_gene - by_region):,}")
print(f"union     : {len(by_gene | by_region):,} ({len(by_gene | by_region) / 21926:.1%})")
print(f"\nrepo's jak1_features.json had 6,873 (31.3%); the paper reports 56.3% (~12,340)")
