"""AVI scores for every possible SNV in the JAK2 coding sequence, mapped to protein level.

1. JAK2 canonical transcript (ENST00000381652) CDS exons + CDS sequence from Ensembl
2. one Atlas query_interval per CDS exon -> dense precomputed AVI for all 3 alternates
3. local codon translation -> missense / synonymous / nonsense, and the protein substitution

Writes jak2_cds_avi_snv.csv (one row per SNV) and jak2_cds_avi_protein.csv (one row per
amino-acid substitution, aggregated). The API key is read from a file and never printed.
"""
import pathlib
import time

import pandas as pd
import requests
from alphagenome.atlas import atlas
from alphagenome.data import genome

ENS = "https://rest.ensembl.org"
TRANSCRIPT = "ENST00000381652"
OUT = pathlib.Path("ag")

CODONS = {}
_bases = "TCAG"
_aas = ("FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG")
for _i, _b1 in enumerate(_bases):
    for _j, _b2 in enumerate(_bases):
        for _k, _b3 in enumerate(_bases):
            CODONS[_b1 + _b2 + _b3] = _aas[_i * 16 + _j * 4 + _k]


def ensembl(path):
    r = requests.get(f"{ENS}{path}", headers={"Content-Type": "application/json"},
                     timeout=120)
    r.raise_for_status()
    return r.json()


# ---- 1. transcript structure -------------------------------------------------
tr = ensembl(f"/lookup/id/{TRANSCRIPT}?expand=1")
strand, chrom = tr["strand"], "chr" + tr["seq_region_name"]
cds_lo, cds_hi = tr["Translation"]["start"], tr["Translation"]["end"]
aa_len = tr["Translation"]["length"]
print(f"{TRANSCRIPT} {chrom} strand {strand}, protein {aa_len} aa, "
      f"CDS genomic {cds_lo}-{cds_hi}")
if strand != 1:
    raise SystemExit("this script assumes the + strand, which JAK2 is on")

# CDS portion of each exon, in transcription order
cds_exons = []
for ex in sorted(tr["Exon"], key=lambda e: e["start"]):
    lo, hi = max(ex["start"], cds_lo), min(ex["end"], cds_hi)
    if lo <= hi:
        cds_exons.append((lo, hi))
print(f"{len(cds_exons)} CDS exons, {sum(h - l + 1 for l, h in cds_exons)} nt")

cds_seq = ensembl(f"/sequence/id/{TRANSCRIPT}?type=cds")["seq"].upper()
print(f"CDS sequence {len(cds_seq)} nt, starts {cds_seq[:3]}, ends {cds_seq[-3:]}")

# genomic position -> 0-based CDS index
pos2cds, idx = {}, 0
for lo, hi in cds_exons:
    for p in range(lo, hi + 1):
        pos2cds[p] = idx
        idx += 1
print(f"mapped {len(pos2cds)} genomic positions to CDS indices")

# ---- 2. Atlas, one interval per CDS exon ------------------------------------
client = atlas.create(pathlib.Path("alphagenome_token.txt").read_text("utf-8").strip())
rows, t0 = [], time.time()
for n, (lo, hi) in enumerate(cds_exons, 1):
    iv = genome.Interval(chromosome=chrom, start=lo - 1, end=hi)   # 0-based half-open
    res = client.query_interval(interval=iv, requested_scorers=["AVI_SCORE"],
                                progress_bar=False)
    ad = res["AVI_SCORE"]
    got = 0
    # obs["variant"] holds genome.Variant objects, not strings
    for var, score in zip(ad.obs["variant"], ad.X[:, 0]):
        p = int(var.position)
        ref, alt = var.reference_bases, var.alternate_bases
        if p in pos2cds and len(ref) == 1 and len(alt) == 1:
            rows.append({"variant_dna": f"{chrom}:{p}:{ref}>{alt}", "pos": p,
                         "ref": ref, "alt": alt, "avi_raw": float(score)})
            got += 1
    print(f"  exon {n:2d}/{len(cds_exons)} {lo}-{hi} ({hi - lo + 1:4d} nt): "
          f"{ad.shape[0]:5d} returned, {got:4d} inside CDS")

snv = pd.DataFrame(rows).drop_duplicates("variant_dna")
print(f"\n{len(snv)} CDS SNVs with AVI in {time.time() - t0:.1f}s")

# ---- 3. translate ------------------------------------------------------------
recs = []
for r in snv.itertuples():
    i = pos2cds[r.pos]
    if cds_seq[i] != r.ref:                      # reference sanity check
        recs.append({**r._asdict(), "consequence": "REF_MISMATCH"})
        continue
    cod_n, off = divmod(i, 3)
    wt_cod = cds_seq[cod_n * 3:cod_n * 3 + 3]
    mt_cod = wt_cod[:off] + r.alt + wt_cod[off + 1:]
    wt_aa, mt_aa = CODONS[wt_cod], CODONS[mt_cod]
    if wt_aa == mt_aa:
        cons = "synonymous"
    elif mt_aa == "*":
        cons = "nonsense"
    elif wt_aa == "*":
        cons = "stop_lost"
    else:
        cons = "missense"
    recs.append({"variant_dna": r.variant_dna, "avi_raw": r.avi_raw,
                 "aa_pos": cod_n + 1, "wt_aa": wt_aa, "mut_aa": mt_aa,
                 "codon_change": f"{wt_cod}>{mt_cod}", "consequence": cons,
                 "variant": f"{wt_aa}{cod_n + 1}{mt_aa}" if cons == "missense" else ""})

df = pd.DataFrame(recs)
print(df["consequence"].value_counts().to_string())
OUT.mkdir(exist_ok=True)
df.to_csv(OUT / "jak2_cds_avi_snv.csv", index=False)

mis = df[df.consequence == "missense"]
prot = (mis.groupby(["variant", "aa_pos", "wt_aa", "mut_aa"])["avi_raw"]
          .agg(avi_max="max", avi_mean="mean", n_snv="size")
          .reset_index().sort_values(["aa_pos", "mut_aa"]))
prot.to_csv(OUT / "jak2_cds_avi_protein.csv", index=False)
print(f"\n{len(mis)} missense SNVs -> {len(prot)} distinct protein substitutions "
      f"({len(prot) / (19 * aa_len):.1%} of the 19 x {aa_len} = {19 * aa_len} possible)")
print(f"positions covered: {prot.aa_pos.nunique()} of {aa_len}")
print(f"AVI raw range {prot.avi_max.min():.3f} .. {prot.avi_max.max():.3f}")
print(prot.head(8).to_string(index=False))
