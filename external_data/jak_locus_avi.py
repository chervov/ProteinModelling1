"""AVI for every possible SNV across a JAK-family locus, strand-aware.

Usage:  python jak_locus_avi.py JAK1 JAK3 TYK2

Per gene: Ensembl canonical transcript -> region classes -> Atlas query_interval over the
gene span plus 2 kb of promoter -> ag/<gene>_locus_avi.csv.gz plus a high-AVI shortlist.

Strand matters. In genomic coordinates the 5' splice donor of an intron is at its LOW end
for a + strand gene and at its HIGH end for a - strand gene; labelling by genomic order
alone silently swaps donor and acceptor on JAK1 and JAK3.
"""
import pathlib
import sys
import time

import pandas as pd
import requests
from alphagenome.atlas import atlas
from alphagenome.data import genome

ENS = "https://rest.ensembl.org"
UPSTREAM = 2000
WINDOW = 10_000
OUT = pathlib.Path("ag")
OUT.mkdir(exist_ok=True)
LOG = []


def say(m):
    print(m, flush=True)
    LOG.append(str(m))


def ensembl(path, tries=5):
    """Ensembl REST returns a sporadic 500; a single failure must not lose the run."""
    for attempt in range(1, tries + 1):
        try:
            r = requests.get(f"{ENS}{path}",
                             headers={"Content-Type": "application/json"}, timeout=180)
            r.raise_for_status()
            return r.json()
        except Exception as exc:                     # noqa: BLE001
            if attempt == tries:
                raise
            say(f"    ensembl {path.split('?')[0]} attempt {attempt}: "
                f"{type(exc).__name__}, retrying in {4 * attempt}s")
            time.sleep(4 * attempt)


def build(gene):
    g = ensembl(f"/lookup/symbol/homo_sapiens/{gene}?expand=1")
    tid = next(t["id"] for t in g["Transcript"] if t.get("is_canonical") == 1)
    tr = ensembl(f"/lookup/id/{tid}?expand=1")
    strand = tr["strand"]
    chrom = "chr" + tr["seq_region_name"]
    cds_lo, cds_hi = tr["Translation"]["start"], tr["Translation"]["end"]
    exons = sorted([(e["start"], e["end"]) for e in tr["Exon"]])
    tx_lo, tx_hi = exons[0][0], exons[-1][1]
    aa = tr["Translation"]["length"]

    exonic = set()
    for a, b in exons:
        exonic.update(range(a, b + 1))
    introns = [(exons[i][1] + 1, exons[i + 1][0] - 1) for i in range(len(exons) - 1)]
    introns = [(a, b) for a, b in introns if a <= b]

    donor, acceptor, region = set(), set(), set()
    acc_dist = {}                       # position -> nt into the intron from the acceptor end
    for a, b in introns:
        if strand == 1:
            d_end, a_end = (a, a + 1), (b - 1, b)
            for k in range(0, min(30, b - a + 1)):
                acc_dist[b - k] = k + 1
        else:
            d_end, a_end = (b, b - 1), (a, a + 1)
            for k in range(0, min(30, b - a + 1)):
                acc_dist[a + k] = k + 1
        donor.update(p for p in d_end if a <= p <= b)
        acceptor.update(p for p in a_end if a <= p <= b)
        region.update(range(a, min(a + 7, b) + 1))
        region.update(range(max(b - 7, a), b + 1))
    for a, b in exons:
        region.update(range(a, min(a + 2, b) + 1))
        region.update(range(max(b - 2, a), b + 1))

    def classify(p):
        if p in donor:
            return "splice_donor"
        if p in acceptor:
            return "splice_acceptor"
        if p in exonic:
            if cds_lo <= p <= cds_hi:
                return "CDS_splice_region" if p in region else "CDS"
            utr = "5UTR" if (p < cds_lo) == (strand == 1) else "3UTR"
            return f"{utr}_splice_region" if p in region else utr
        if p in region:
            return "splice_region"
        if tx_lo <= p <= tx_hi:
            return "intron"
        return "upstream"

    lo = tx_lo - UPSTREAM if strand == 1 else tx_lo
    hi = tx_hi if strand == 1 else tx_hi + UPSTREAM
    say(f"\n=== {gene} {tid} {chrom}:{tx_lo}-{tx_hi} strand {strand:+d}, "
        f"{len(exons)} exons, {aa} aa")
    say(f"    region {lo}-{hi} = {hi - lo + 1:,} bp -> {(hi - lo + 1) * 3:,} SNVs")
    return dict(gene=gene, tid=tid, chrom=chrom, strand=strand, lo=lo, hi=hi,
                classify=classify, acc_dist=acc_dist, n_exons=len(exons), aa=aa)


def pull(client, spec):
    frames, t0 = [], time.time()
    starts = list(range(spec["lo"], spec["hi"] + 1, WINDOW))
    for n, s in enumerate(starts, 1):
        e = min(s + WINDOW - 1, spec["hi"])
        iv = genome.Interval(chromosome=spec["chrom"], start=s - 1, end=e)
        for attempt in (1, 2, 3):
            try:
                ad = client.query_interval(interval=iv,
                                           requested_scorers=["AVI_SCORE"],
                                           progress_bar=False)["AVI_SCORE"]
                break
            except Exception as exc:                 # noqa: BLE001
                if attempt == 3:
                    raise
                say(f"    window {n} attempt {attempt}: {type(exc).__name__}, retrying")
                time.sleep(5)
        frames.append(pd.DataFrame({
            "pos": [int(v.position) for v in ad.obs["variant"]],
            "ref": [v.reference_bases for v in ad.obs["variant"]],
            "alt": [v.alternate_bases for v in ad.obs["variant"]],
            "avi_raw": ad.X[:, 0].astype(float)}))
    df = pd.concat(frames, ignore_index=True).drop_duplicates(["pos", "ref", "alt"])
    df = df[(df.pos >= spec["lo"]) & (df.pos <= spec["hi"])].copy()
    df["region"] = [spec["classify"](p) for p in df.pos]
    df["variant_dna"] = (spec["chrom"] + ":" + df.pos.astype(str) + ":"
                         + df.ref + ">" + df.alt)
    say(f"    {len(df):,} SNVs in {time.time() - t0:.1f}s "
        f"({len(df) / (time.time() - t0):.0f}/s)")
    return df[["variant_dna", "pos", "ref", "alt", "region", "avi_raw"]]


client = atlas.create(pathlib.Path("alphagenome_token.txt").read_text("utf-8").strip())
summary = []
for gene in sys.argv[1:]:
    spec = build(gene)
    df = pull(client, spec)
    df.to_csv(OUT / f"{gene}_locus_avi.csv.gz", index=False, compression="gzip")

    g = (df.groupby("region").avi_raw
           .agg(n="size", mean="mean", median="median", max="max")
           .sort_values("mean", ascending=False))
    say(g.to_string(float_format=lambda v: f"{v:.3f}"))
    for region, row in g.iterrows():
        summary.append({"gene": gene, "region": region, "n": int(row["n"]),
                        "mean": row["mean"], "median": row["median"], "max": row["max"]})

    nc = df[~df.region.isin(["CDS", "CDS_splice_region"])]
    hi_nc = nc[nc.avi_raw > 1.5].sort_values("avi_raw", ascending=False)
    hi_nc.to_csv(OUT / f"{gene}_locus_noncoding_high_avi.csv", index=False)
    say(f"    {len(hi_nc)} non-coding SNVs above 1.5 "
        f"({len(hi_nc) / max(len(nc), 1):.3%}): "
        f"{hi_nc.region.value_counts().to_dict()}")

    # polypyrimidine profile, transcript-oriented
    intr = df[df.region == "intron"].copy()
    intr["acc_dist"] = intr.pos.map(spec["acc_dist"])
    near = intr[intr.acc_dist.between(3, 25)]
    far = intr[intr.acc_dist.isna()]
    if len(near) and len(far):
        say(f"    polypyrimidine tract (3-25 nt from acceptor): mean "
            f"{near.avi_raw.mean():.3f} vs deep intron {far.avi_raw.mean():.3f} "
            f"= {near.avi_raw.mean() / max(far.avi_raw.mean(), 1e-9):.1f}x")

pd.DataFrame(summary).to_csv(OUT / "jak_family_avi_by_region.csv", index=False)
(OUT / "jak_family_locus_summary.txt").write_text("\n".join(LOG), encoding="utf-8")
say("\nwrote per-gene csv.gz, shortlists, jak_family_avi_by_region.csv")
