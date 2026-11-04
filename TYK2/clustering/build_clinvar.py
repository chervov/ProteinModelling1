"""ClinVar germline classifications for TYK2.

Not a clustering feature - **no feature sees this**. With AlphaMissense's and ESM-1b's training
data in mind this is the weaker of the two external criteria, but TYK2 is far richer in ClinVar
than JAK1 thanks to V617F and the myeloproliferative-neoplasm literature, so it is worth having
beside gnomAD.

Source: NCBI E-utilities against the `clinvar` database. The bulk alternative,
`https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz` (458 MB), is
reachable from here and would also work; E-utilities is used because one gene is a few hundred
records and needs no 458 MB download. For a gene with thousands of entries the bulk file becomes
the better choice.

**Position disambiguation.** The `protein_change` field lists every isoform's numbering at once -
`I218V, I474V, I623V` for one variant - so it cannot be used directly. The record `title` carries
the canonical transcript instead:

    NM_003331.4(TYK2):c.1867A>G (p.Ile623Val)

NM_003331 is the MANE Select transcript and its protein NP_004963.1 is byte-identical to UniProt
P29597, verified in `TYK2/variant_panel_24/README.md`. The parse therefore requires NM_003331 and
then checks the wild-type residue against the pinned sequence anyway.

Writes tyk2_clinvar.csv.
"""
import csv
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).parent
ACC, GENE, TRANSCRIPT = "P29597", "TYK2", "NM_003331"
E = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
AA3 = {"Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E",
       "Gly": "G", "His": "H", "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F",
       "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V"}
TITLE = re.compile(r"\((p\.([A-Z][a-z]{2})(\d+)([A-Z][a-z]{2}))\)")
# 1 to 4 gold stars, as ClinVar assigns them
STARS = {"practice guideline": 4,
         "reviewed by expert panel": 3,
         "criteria provided, multiple submitters, no conflicts": 2,
         "criteria provided, conflicting classifications": 1,
         "criteria provided, conflicting interpretations": 1,
         "criteria provided, single submitter": 1,
         "no assertion criteria provided": 0,
         "no classification provided": 0,
         "no classifications from unflagged records": 0}


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


def main():
    seq = (HERE / f"TYK2_{ACC}_1187aa.txt").read_text().splitlines()[1]
    print(f"TYK2 {ACC}, {len(seq)} aa")

    term = f'{GENE}[gene] AND "missense variant"[molecular consequence]'
    q = urllib.parse.quote(term)
    total = get(f"{E}esearch.fcgi?db=clinvar&retmode=json&retmax=0&term={q}")
    n = int(total["esearchresult"]["count"])
    print(f"  ClinVar: {n:,} missense records for {GENE}")

    ids = []
    while len(ids) < n:
        d = get(f"{E}esearch.fcgi?db=clinvar&retmode=json&retmax=500&retstart={len(ids)}&term={q}")
        got = d["esearchresult"]["idlist"]
        if not got:
            break
        ids += got
    print(f"  collected {len(ids):,} record ids")

    recs, other_tx, mismatch = {}, 0, 0
    for i in range(0, len(ids), 200):
        d = get(f"{E}esummary.fcgi?db=clinvar&retmode=json&id={','.join(ids[i:i+200])}")["result"]
        for u in d.get("uids", []):
            x = d[u]
            title = x.get("title", "")
            if TRANSCRIPT not in title:
                other_tx += 1
                continue
            m = TITLE.search(title)
            if not m:
                continue
            wt3, pos, alt3 = m.group(2), int(m.group(3)), m.group(4)
            if wt3 not in AA3 or alt3 not in AA3:
                continue
            wt, alt = AA3[wt3], AA3[alt3]
            if not (1 <= pos <= len(seq)) or seq[pos - 1] != wt:
                mismatch += 1
                continue
            g = x.get("germline_classification", {}) or {}
            sig = (g.get("description") or "").strip()
            rev = (g.get("review_status") or "").strip()
            traits = "; ".join(sorted({t.get("trait_name", "") for t in g.get("trait_set", [])
                                       if t.get("trait_name")}))
            key = f"{wt}{pos}{alt}"
            cand = (STARS.get(rev.lower(), 0), x.get("accession", ""), sig, rev, traits)
            # keep the best-reviewed record per substitution
            if key not in recs or cand[0] > recs[key][0]:
                recs[key] = cand
        print(f"    summarised {min(i+200, len(ids)):,}/{len(ids):,}", flush=True)

    print(f"  {len(recs):,} distinct substitutions on {TRANSCRIPT}; "
          f"{other_tx} records on another transcript, {mismatch} wild-type mismatches")

    universe = [r["variant"] for r in csv.DictReader(open(HERE / "tyk2_variant_universe.csv"))]
    out = HERE / "tyk2_clinvar.csv"
    k = 0
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["index", "variant", "wt", "pos", "alt", "clinvar_accession",
                    "clinvar_significance", "clinvar_review_status", "clinvar_stars",
                    "clinvar_conditions"])
        for i, v in enumerate(universe, 1):
            r = recs.get(v)
            k += r is not None
            w.writerow([i, v, v[0], v[1:-1], v[-1],
                        "" if not r else r[1], "" if not r else r[2],
                        "" if not r else r[3], "" if not r else r[0],
                        "" if not r else r[4]])
    print(f"\nwrote {out.name}: {len(universe):,} rows, {k:,} with a ClinVar record "
          f"({100 * k / len(universe):.2f}%)")
    import collections
    sig = collections.Counter(r[2] for r in recs.values())
    st = collections.Counter(r[0] for r in recs.values())
    print("  classifications: " + ", ".join(f"{s}={c}" for s, c in sig.most_common()))
    print("  review stars:    " + ", ".join(f"{s}*={c}" for s, c in sorted(st.items(), reverse=True)))


if __name__ == "__main__":
    main()
