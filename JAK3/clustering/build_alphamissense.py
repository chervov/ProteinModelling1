"""AlphaMissense pathogenicity for JAK3, fetched from source.

Source: Cheng et al., "Accurate proteome-wide missense variant effect prediction with
AlphaMissense", Science 2023. DeepMind publish the full predictions on Zenodo under
CC BY-NC-SA 4.0:

    https://zenodo.org/records/10813168
    AlphaMissense_aa_substitutions.tsv.gz   1.21 GB   (71 M substitutions, all human canonical)

Columns: `uniprot_id, protein_variant, am_pathogenicity, am_class`, keyed exactly as we need.

**The whole file is not downloaded.** gzip has no random access, so a range request cannot jump
to one protein the way it can inside the ESM-1b zip. But the file is **sorted by accession**, so
this script streams it and stops as soon as it reads past the target - for JAK3 (P52333) that is
roughly half the archive, and it never touches disk. For an accession late in the alphabet the
stream is longer; for one early in it, much shorter.

Output is in the directory's canonical order: **by position, then substituted-in residue**.

Writes jak3_alphamissense.csv.
"""
import csv
import gzip
import pathlib
import sys
import time
import urllib.request

HERE = pathlib.Path(__file__).parent
ACC = "P52333"
URL = ("https://zenodo.org/records/10813168/files/"
       "AlphaMissense_aa_substitutions.tsv.gz?download=1")


def stream_accession(acc):
    """Stream the sorted archive, keep rows for `acc`, stop once past it."""
    req = urllib.request.Request(URL, headers={"User-Agent": "research-script"})
    found, scanned, t0 = {}, 0, time.time()
    with urllib.request.urlopen(req, timeout=600) as fh:
        for line in gzip.GzipFile(fileobj=fh):
            s = line.decode(errors="replace")
            if s.startswith("#") or s.startswith("uniprot_id"):
                continue
            scanned += 1
            uid, variant, score, klass = s.rstrip("\n").split("\t")
            if uid == acc:
                found[variant] = (float(score), klass)
            elif found:
                break                      # sorted, so the block has ended
            if scanned % 20_000_000 == 0:
                print(f"    scanned {scanned/1e6:.0f} M rows, {time.time()-t0:.0f}s ...",
                      flush=True)
    print(f"  scanned {scanned:,} rows in {time.time()-t0:.0f}s, "
          f"stopped early once past {acc}")
    return found


def main():
    seq_file = HERE / f"JAK3_{ACC}_1124aa.txt"
    seq = seq_file.read_text().splitlines()[1]
    print(f"JAK3 {ACC}, {len(seq)} aa")
    print("streaming AlphaMissense from Zenodo (1.21 GB, sorted by accession)")

    am = stream_accession(ACC)
    if not am:
        sys.exit(f"{ACC} not found in the archive")
    print(f"  {len(am):,} AlphaMissense rows for {ACC}")

    bad = [v for v in am if not (1 <= int(v[1:-1]) <= len(seq))
           or seq[int(v[1:-1]) - 1] != v[0]]
    if bad:
        sys.exit(f"wild-type mismatch on {len(bad)} rows, first {bad[:3]}")
    print(f"  wild type agrees with {seq_file.name} on all of them")

    universe = [r["variant"] for r in csv.DictReader(open(HERE / "jak3_variant_universe.csv"))]
    out = HERE / "jak3_alphamissense.csv"
    n = 0
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["index", "variant", "wt", "pos", "alt",
                    "alphamissense", "am_class"])
        for i, v in enumerate(universe, 1):
            hit = am.get(v)
            n += hit is not None
            w.writerow([i, v, v[0], v[1:-1], v[-1],
                        "" if hit is None else f"{hit[0]:.4f}",
                        "" if hit is None else hit[1]])
    print(f"\nwrote {out.name}: {len(universe):,} rows in universe order, "
          f"{n:,} populated ({100 * n / len(universe):.2f}%)")
    vals = [s for s, _ in am.values()]
    import collections
    cl = collections.Counter(k for _, k in am.values())
    print(f"  range {min(vals):.4f} .. {max(vals):.4f}; higher = more pathogenic")
    print(f"  classes: {dict(cl)}")


if __name__ == "__main__":
    main()
