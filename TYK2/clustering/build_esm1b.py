"""ESM-1b log-likelihood ratios for TYK2, fetched from source.

Source: Brandes, Goldman, Wang, Ye & Ntranos, "Genome-wide prediction of disease variant
effects with a deep protein language model", Nature Genetics 2023 (doi 10.1038/s41588-023-01465-0).
The authors publish precomputed LLRs for every human protein isoform as a single
**1.34 GB zip** hosted with their HuggingFace Space:

    https://huggingface.co/spaces/ntranoslab/esm_variants
    .../resolve/main/ALL_hum_isoforms_ESM1b_LLR.zip

**It is not downloaded.** The zip holds 42,289 members, one per isoform, named by UniProt
accession (`P29597_LLR.csv`). HuggingFace honours HTTP range requests, so this script reads the
zip's central directory remotely and pulls out only the member it needs - about 175 KB and ~3
seconds for TYK2, against 1.34 GB for the archive. That is what makes this usable for an
arbitrary protein rather than only for ones we have already cached.

The per-isoform file is a MATRIX, not a variant list: 20 rows (one per substituted-in residue),
one column per position, headed `"<wt> <pos>"`. It is transposed here into the directory's
canonical row order - **by position, then by substituted-in residue alphabetically**.

Writes tyk2_esm1b.csv.
"""
import csv
import io
import pathlib
import sys
import urllib.request
import zipfile

HERE = pathlib.Path(__file__).parent
ACC = "P29597"
ZIP_URL = ("https://huggingface.co/spaces/ntranoslab/esm_variants/resolve/main/"
           "ALL_hum_isoforms_ESM1b_LLR.zip")
MEMBER = "content/ALL_hum_isoforms_ESM1b_LLR/{acc}_LLR.csv"


class HttpFile(io.RawIOBase):
    """A seekable read-only file over HTTP range requests, so zipfile can work remotely."""

    def __init__(self, url):
        self.url, self.pos = url, 0
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=120) as fh:
            self.size = int(fh.headers["Content-Length"])
            if fh.headers.get("Accept-Ranges") != "bytes":
                raise RuntimeError("server does not advertise range support")

    def seek(self, off, whence=0):
        self.pos = {0: off, 1: self.pos + off, 2: self.size + off}[whence]
        return self.pos

    def tell(self):      return self.pos
    def seekable(self):  return True
    def readable(self):  return True

    def read(self, n=-1):
        if n < 0:
            n = self.size - self.pos
        if n == 0:
            return b""
        hi = min(self.pos + n, self.size) - 1
        req = urllib.request.Request(self.url, headers={"Range": f"bytes={self.pos}-{hi}"})
        with urllib.request.urlopen(req, timeout=180) as fh:
            data = fh.read()
        self.pos += len(data)
        return data


def fetch_llr_matrix(acc):
    remote = HttpFile(ZIP_URL)
    zf = zipfile.ZipFile(remote)
    name = MEMBER.format(acc=acc)
    if name not in zf.namelist():
        sys.exit(f"{acc} not in the archive; {len(zf.namelist()):,} members present")
    raw = zf.read(name)
    print(f"  pulled {name.split('/')[-1]} - {len(raw):,} bytes "
          f"out of a {remote.size / 1e9:.2f} GB archive")
    return list(csv.reader(io.StringIO(raw.decode())))


def main():
    seq_file = HERE / f"TYK2_{ACC}_1187aa.txt"
    seq = seq_file.read_text().splitlines()[1]
    print(f"TYK2 {ACC}, {len(seq)} aa")

    print(f"fetching ESM-1b from the HuggingFace Space by range request")
    rows = fetch_llr_matrix(ACC)
    header = rows[0][1:]                       # "M 1", "G 2", ...
    positions = []
    for h in header:
        wt, pos = h.split()
        positions.append((wt, int(pos)))
    print(f"  matrix: {len(rows) - 1} alternate residues x {len(positions)} positions")

    # the check that matters: does the file's own wild type agree with our sequence?
    bad = [(p, w, seq[p - 1]) for w, p in positions if seq[p - 1] != w]
    if bad:
        sys.exit(f"wild-type mismatch at {len(bad)} positions, first {bad[:3]}")
    if len(positions) != len(seq):
        sys.exit(f"matrix covers {len(positions)} positions, sequence has {len(seq)}")
    print(f"  wild type agrees with {seq_file.name} at all {len(positions):,} positions")

    llr = {}
    for row in rows[1:]:
        alt = row[0].strip()
        for (wt, pos), val in zip(positions, row[1:]):
            if alt == wt or val == "":
                continue
            llr[f"{wt}{pos}{alt}"] = float(val)

    universe = [r["variant"] for r in csv.DictReader(open(HERE / "tyk2_variant_universe.csv"))]
    out = HERE / "tyk2_esm1b.csv"
    n = 0
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["index", "variant", "wt", "pos", "alt", "esm1b"])
        for i, v in enumerate(universe, 1):
            val = llr.get(v)
            n += val is not None
            w.writerow([i, v, v[0], v[1:-1], v[-1], "" if val is None else f"{val:.4f}"])
    print(f"\nwrote {out.name}: {len(universe):,} rows in universe order "
          f"(position, then substituted-in residue), {n:,} populated "
          f"({100 * n / len(universe):.2f}%)")
    vals = list(llr.values())
    print(f"  range {min(vals):.3f} .. {max(vals):.3f}; "
          f"lower = more damaging (log-likelihood ratio vs wild type)")
    print(f"  first 3 rows: " + ", ".join(
        f"{v}={llr[v]:.3f}" for v in universe[:3] if v in llr))


if __name__ == "__main__":
    main()
