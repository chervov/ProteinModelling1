"""gnomAD r4 population frequencies for JAK1, in EV1 order.

Fetches every missense variant gnomAD holds for JAK1 through the GraphQL API, parses the
HGVSp protein change, and **verifies the wild-type residue against UniProt P23458** before
accepting a match. Records that disagree are excluded, not silently mapped: 45 of them do,
all in positions 665-708, where gnomAD evidently annotates a different transcript.

Output follows this directory's conventions: all 23,080 Dataset EV1 rows in EV1 order, so
the file joins to every other feature file by row position as well as by variant_id.
Variants gnomAD has never observed get EMPTY fields, not 0 - an allele frequency of 0 and
"not observed" are different statements, and 0 is a legitimate value elsewhere.

Writes jak1_gnomad.csv.
"""
import json
import pathlib
import urllib.request

import pandas as pd

HERE = pathlib.Path(__file__).parent
AA3 = {"Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E",
       "Gly": "G", "His": "H", "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F",
       "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V", "Ter": "*"}
QUERY = ("query($g:String!){gene(gene_symbol:$g,reference_genome:GRCh38){"
         "variants(dataset:gnomad_r4){consequence hgvsp exome{af ac an} genome{af ac an}}}}")


def canonical_sequence():
    fa = (HERE / "JAK1_P23458.fasta").read_text().splitlines()
    return "".join(l.strip() for l in fa if not l.startswith(">"))


def fetch(gene="JAK1"):
    body = json.dumps({"query": QUERY, "variables": {"g": gene}}).encode()
    req = urllib.request.Request("https://gnomad.broadinstitute.org/api", data=body,
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "research-script"})
    with urllib.request.urlopen(req, timeout=600) as fh:
        return json.load(fh)["data"]["gene"]["variants"] or []


def main():
    seq = canonical_sequence()
    variants = fetch()
    print(f"gnomAD r4 returned {len(variants):,} variants for JAK1")

    best, mismatched, n_zero_ac = {}, [], 0
    for v in variants:
        if v.get("consequence") != "missense_variant":
            continue
        h = v.get("hgvsp") or ""
        if not h.startswith("p."):
            continue
        body_, wt3 = h[2:], h[2:5]
        rest = body_[3:]
        digits = "".join(c for c in rest if c.isdigit())
        alt3 = rest[len(digits):]
        if not digits or wt3 not in AA3 or alt3 not in AA3:
            continue
        pos, wt, alt = int(digits), AA3[wt3], AA3[alt3]

        # the check that matters: does gnomAD's wild type agree with P23458?
        if not (1 <= pos <= len(seq)) or seq[pos - 1] != wt:
            mismatched.append((pos, wt, seq[pos - 1] if 1 <= pos <= len(seq) else "?"))
            continue

        ex, ge = v.get("exome") or {}, v.get("genome") or {}
        ac = (ex.get("ac") or 0) + (ge.get("ac") or 0)
        an = max(ex.get("an") or 0, ge.get("an") or 0)
        afs = [x.get("af") for x in (ex, ge) if x.get("af") is not None]
        af = max(afs) if afs else None

        # "observed" means ALLELE COUNT > 0, tested explicitly. gnomAD lists ~100 JAK1
        # missense sites with af == 0.0 and ac == 0: the position was sequenced (an is
        # about 1.46 M) but no copy of the alternate allele was seen. Those are not
        # observed variants and are excluded. Note the trap: `ex.get("af") or ge.get("af")`
        # would drop them too, but only because 0.0 is falsy - an accident, not a decision,
        # and it would equally drop a genuine af of 0.0 if one ever existed.
        if af is None or ac == 0:
            n_zero_ac += 1
            continue
        key = (pos, alt)
        if key not in best or af > best[key]["gnomad_af"]:
            best[key] = {"gnomad_af": af, "gnomad_ac": ac, "gnomad_an": an}

    print(f"  missense with a usable HGVSp and matching wild type, allele count > 0: "
          f"{len(best):,}")
    print(f"  excluded on allele count == 0 (sequenced, never observed): {n_zero_ac}")
    if mismatched:
        pp = sorted({p for p, _, _ in mismatched})
        print(f"  EXCLUDED {len(mismatched)} records on wild-type mismatch, "
              f"positions {min(pp)}-{max(pp)}")
        print("    gnomAD annotates a different transcript there; no constant offset "
              "reconciles them, so they are dropped rather than remapped.")

    ev1 = pd.read_csv(HERE / "jak1_ev1_clusters.csv")
    ev1["wt"] = ev1.variant_id.str[0]
    ev1["pos"] = ev1.variant_id.str[1:-1].astype(int)
    ev1["alt"] = ev1.variant_id.str[-1]
    df = ev1[["variant_id", "wt", "pos", "alt", "cluster"]].copy()
    for col in ("gnomad_af", "gnomad_ac", "gnomad_an"):
        df[col] = [best.get((p, a), {}).get(col) for p, a in zip(df.pos, df.alt)]
    df["in_gnomad"] = df.gnomad_af.notna().astype(int)

    out = HERE / "jak1_gnomad.csv"
    df.to_csv(out, index=False)
    obs = int(df.in_gnomad.sum())
    print(f"\nwrote {out.name}: {len(df):,} rows in EV1 order, {obs:,} observed in gnomAD "
          f"({100 * obs / len(df):.2f}%), {len(df) - obs:,} left blank")
    real = df[df.wt != df.alt]
    print(f"  excluding self-substitutions: {int(real.in_gnomad.sum()):,} of {len(real):,}")
    for c in (1, 2):
        sub = real[real.cluster == c]
        print(f"  EV1 cluster {c}: {100 * sub.in_gnomad.mean():.2f}% observed "
              f"({int(sub.in_gnomad.sum()):,} of {len(sub):,})")
    print(df.head(4).to_string(index=False))


if __name__ == "__main__":
    main()
