"""AVI for every possible SNV across the whole JAK2 locus, annotated by region class.

Gene span plus 2 kb upstream (promoter), pulled in windows via the Atlas, then each
position is labelled CDS / 5'UTR / 3'UTR / splice_donor / splice_acceptor /
splice_region / intron / upstream from the canonical transcript's exon structure.

Writes ag/jak2_locus_avi.csv.gz (all of it) and ag/jak2_locus_summary.txt.
The API key is read from a file and never printed.
"""
import pathlib
import time

import pandas as pd
import requests
from alphagenome.atlas import atlas
from alphagenome.data import genome

ENS = "https://rest.ensembl.org"
TRANSCRIPT = "ENST00000381652"
UPSTREAM = 2000
WINDOW = 10_000            # per query_interval call
OUT = pathlib.Path("ag")
LOG = []


def say(msg):
    print(msg, flush=True)
    LOG.append(str(msg))


def ensembl(path):
    r = requests.get(f"{ENS}{path}", headers={"Content-Type": "application/json"},
                     timeout=180)
    r.raise_for_status()
    return r.json()


tr = ensembl(f"/lookup/id/{TRANSCRIPT}?expand=1")
chrom = "chr" + tr["seq_region_name"]
strand = tr["strand"]
cds_lo, cds_hi = tr["Translation"]["start"], tr["Translation"]["end"]
exons = sorted([(e["start"], e["end"]) for e in tr["Exon"]])
tx_lo, tx_hi = exons[0][0], exons[-1][1]
say(f"{TRANSCRIPT} {chrom}:{tx_lo}-{tx_hi} strand {strand}, {len(exons)} exons, "
    f"CDS {cds_lo}-{cds_hi}")

lo = tx_lo - UPSTREAM if strand == 1 else tx_lo
hi = tx_hi if strand == 1 else tx_hi + UPSTREAM
say(f"region {chrom}:{lo}-{hi} = {hi - lo + 1:,} bp -> {(hi - lo + 1) * 3:,} possible SNVs")

# ---- position -> region class ------------------------------------------------
exonic = set()
for a, b in exons:
    exonic.update(range(a, b + 1))
introns = [(exons[i][1] + 1, exons[i + 1][0] - 1) for i in range(len(exons) - 1)]

donor, acceptor, splice_region = set(), set(), set()
for a, b in introns:
    donor.update(range(a, min(a + 1, b) + 1))          # first 2 intronic bases
    acceptor.update(range(max(b - 1, a), b + 1))       # last 2 intronic bases
    splice_region.update(range(a, min(a + 7, b) + 1))  # 3-8 intronic
    splice_region.update(range(max(b - 7, a), b + 1))
for a, b in exons:                                     # 1-3 exonic bases each side
    splice_region.update(range(a, min(a + 2, b) + 1))
    splice_region.update(range(max(b - 2, a), b + 1))


def classify(p):
    if p in donor:
        return "splice_donor"
    if p in acceptor:
        return "splice_acceptor"
    if p in exonic:
        if cds_lo <= p <= cds_hi:
            return "CDS_splice_region" if p in splice_region else "CDS"
        utr = "5UTR" if (p < cds_lo) == (strand == 1) else "3UTR"
        return f"{utr}_splice_region" if p in splice_region else utr
    if p in splice_region:
        return "splice_region"
    if tx_lo <= p <= tx_hi:
        return "intron"
    return "upstream"


# ---- pull --------------------------------------------------------------------
client = atlas.create(pathlib.Path("alphagenome_token.txt").read_text("utf-8").strip())
frames, t0 = [], time.time()
starts = list(range(lo, hi + 1, WINDOW))
for n, s in enumerate(starts, 1):
    e = min(s + WINDOW - 1, hi)
    iv = genome.Interval(chromosome=chrom, start=s - 1, end=e)
    for attempt in (1, 2, 3):
        try:
            ad = client.query_interval(interval=iv, requested_scorers=["AVI_SCORE"],
                                       progress_bar=False)["AVI_SCORE"]
            break
        except Exception as exc:                        # noqa: BLE001
            if attempt == 3:
                raise
            say(f"  window {n} attempt {attempt} failed ({type(exc).__name__}), retrying")
            time.sleep(5)
    frames.append(pd.DataFrame({
        "pos": [int(v.position) for v in ad.obs["variant"]],
        "ref": [v.reference_bases for v in ad.obs["variant"]],
        "alt": [v.alternate_bases for v in ad.obs["variant"]],
        "avi_raw": ad.X[:, 0].astype(float)}))
    done = sum(len(f) for f in frames)
    say(f"  window {n:2d}/{len(starts)} {s}-{e}: {ad.shape[0]:6d} variants "
        f"({done:,} total, {done / (time.time() - t0):.0f}/s)")

df = pd.concat(frames, ignore_index=True).drop_duplicates(["pos", "ref", "alt"])
df = df[(df.pos >= lo) & (df.pos <= hi)]
say(f"\n{len(df):,} SNVs in {time.time() - t0:.1f}s")

df["region"] = [classify(p) for p in df.pos]
df["variant_dna"] = chrom + ":" + df.pos.astype(str) + ":" + df.ref + ">" + df.alt
df = df[["variant_dna", "pos", "ref", "alt", "region", "avi_raw"]]
df.to_csv(OUT / "jak2_locus_avi.csv.gz", index=False, compression="gzip")

say("\nAVI by region class:")
g = (df.groupby("region").avi_raw
       .agg(n="size", mean="mean", median="median", p99=lambda x: x.quantile(0.99), max="max")
       .sort_values("mean", ascending=False))
say(g.to_string(float_format=lambda v: f"{v:.3f}"))

say("\ntop 25 non-coding SNVs:")
nc = df[~df.region.isin(["CDS", "CDS_splice_region"])]
say(nc.nlargest(25, "avi_raw")[["variant_dna", "region", "avi_raw"]].to_string(index=False))

hi_nc = nc[nc.avi_raw > 1.5]
say(f"\n{len(hi_nc):,} non-coding SNVs score above 1.5 "
    f"({len(hi_nc) / len(nc):.2%} of {len(nc):,})")
say(hi_nc.region.value_counts().to_string())
hi_nc.sort_values("avi_raw", ascending=False).to_csv(
    OUT / "jak2_locus_noncoding_high_avi.csv", index=False)

(OUT / "jak2_locus_summary.txt").write_text("\n".join(LOG), encoding="utf-8")
say("\nwrote jak2_locus_avi.csv.gz, jak2_locus_noncoding_high_avi.csv, jak2_locus_summary.txt")
