"""PolyPhen-2 for JAK3 at full coverage, by running the tool rather than reading dbNSFP.

dbNSFP caps PolyPhen-2 at ~31% because it is indexed on *genomic* variants, so substitutions
needing two or three nucleotide changes have no row. PolyPhen-2 itself is **protein-level**: its
batch query takes `P52333 617 V F` directly and has no such limit. JAK1 reached 21,926 of 21,926
this way; JAK3 should reach 21,356 of 21,356.

The server has no API. This drives the same web form a person would use, documented in
`JAK1/clustering/build_polyphen_jak1_info.md`:

    submit / status   https://genetics.bwh.harvard.edu/ggi/cgi-bin/ggi2.cgi   (POST, multipart)
    results           https://genetics.bwh.harvard.edu/ggi/pph2/<session>/<batch>/pph2-short.txt

Both classifiers are run. The paper says only "PolyPhen2 pathogenicity score" without naming a
model, and on JAK1 the two disagreed on 25.7% of variants - the single most consequential
ambiguity in reproducing it - so both are kept and the choice is made explicitly downstream.

    python3 build_polyphen.py            # submit both models, poll, parse
    python3 build_polyphen.py --parse    # re-parse already-downloaded output

Writes pph2_input_jak3.txt, pph2_sessions_jak3.txt, pph2_{hvar,hdiv}/pph2-short.txt,
jak3_polyphen2_humvar.csv, jak3_polyphen2_humdiv.csv.
"""
import csv
import pathlib
import re
import sys
import time

import requests

HERE = pathlib.Path(__file__).parent
ACC = "P52333"
SUBMIT = "https://genetics.bwh.harvard.edu/ggi/cgi-bin/ggi2.cgi"
RESULTS = "https://genetics.bwh.harvard.edu/ggi/pph2/{sess}/{batch}/pph2-short.txt"
UA = {"User-Agent": "research script, one protein (JAK3), see build_polyphen_jak3_info.md"}
MODELS = [("HumVar", "humvar"), ("HumDiv", "humdiv")]


def write_input():
    universe = [r["variant"] for r in csv.DictReader(open(HERE / "jak3_variant_universe.csv"))]
    path = HERE / "pph2_input_jak3.txt"
    with open(path, "w") as fh:
        for v in universe:
            fh.write(f"{ACC} {v[1:-1]} {v[0]} {v[-1]}\n")
    print(f"  wrote {path.name}: {len(universe):,} substitutions "
          f"({len(universe)/150000:.0%} of the 150,000 batch limit)")
    return path, universe


def submit(path, model):
    s = requests.Session()
    s.headers.update(UA)
    with open(path, "rb") as fh:
        r = s.post(SUBMIT, timeout=600,
                   data={"_ggi_project": "PPHWeb2", "_ggi_origin": "query",
                         "description": f"JAK3 {ACC} saturation {model}",
                         "NOTIFYME": "", "MODELNAME": model, "UCSCDB": "hg19",
                         "SNPFILTER": "1", "SNPFUNC": "m",
                         "_ggi_target_pipeline": "Submit Batch"},
                   files={"_ggi_batch_file": ("pph2_input_jak3.txt", fh, "text/plain")})
    r.raise_for_status()
    sess = s.cookies.get("polyphenweb2")
    job = re.search(r'lastJobSubmitted"?\s+value="?(\d+)', r.text)
    if not sess:
        sys.exit(f"{model}: no polyphenweb2 session cookie returned; "
                 f"response began {r.text[:200]!r}")
    print(f"  {model}: session {sess}  job {job.group(1) if job else '?'}")
    return sess


def poll(sess, model, tag, minutes=40):
    """Results appear at a fixed URL once the pipeline finishes; batch is 1 for a fresh session."""
    url = RESULTS.format(sess=sess, batch=1)
    t0 = time.time()
    while time.time() - t0 < minutes * 60:
        r = requests.get(url, headers=UA, timeout=180)
        if r.status_code == 200 and r.text.lstrip().startswith("#"):
            out = HERE / f"pph2_{tag}"
            out.mkdir(exist_ok=True)
            (out / "pph2-short.txt").write_text(r.text)
            print(f"  {model}: results after {time.time()-t0:.0f}s, "
                  f"{len(r.text)/1e6:.2f} MB -> pph2_{tag}/pph2-short.txt")
            return True
        time.sleep(60)
        print(f"    {model}: waiting, {time.time()-t0:.0f}s", flush=True)
    print(f"  {model}: TIMED OUT after {minutes} min; session {sess} stays valid for "
          f"months, re-run with --parse once {url} is populated")
    return False


def parse(tag, model):
    src = HERE / f"pph2_{tag}" / "pph2-short.txt"
    if not src.exists():
        print(f"  {model}: {src} absent, skipping")
        return
    got = {}
    for line in src.read_text(errors="replace").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        f = [c.strip() for c in line.split("\t")]
        if len(f) < 12:
            continue
        try:
            got[f"{f[2]}{int(f[1])}{f[3]}"] = (f[9], float(f[10]) if f[10] else None)
        except ValueError:
            continue
    universe = [r["variant"] for r in csv.DictReader(open(HERE / "jak3_variant_universe.csv"))]
    out = HERE / f"jak3_polyphen2_{tag}.csv"
    n = 0
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["index", "variant", "wt", "pos", "alt",
                    f"polyphen2_{tag}", f"polyphen2_{tag}_pred"])
        for i, v in enumerate(universe, 1):
            hit = got.get(v)
            n += hit is not None and hit[1] is not None
            w.writerow([i, v, v[0], v[1:-1], v[-1],
                        "" if not hit or hit[1] is None else f"{hit[1]:.3f}",
                        "" if not hit else hit[0]])
    print(f"  wrote {out.name}: {n:,} of {len(universe):,} scored "
          f"({100*n/len(universe):.2f}%)")


def main():
    if "--parse" in sys.argv:
        for model, tag in MODELS:
            parse(tag, model)
        return
    print(f"PolyPhen-2 for JAK3 {ACC}")
    path, _ = write_input()
    sessions = []
    for model, tag in MODELS:
        print(f"submitting {model}")
        sess = submit(path, model)
        sessions.append((sess, model))
        if poll(sess, model, tag):
            parse(tag, model)
    (HERE / "pph2_sessions_jak3.txt").write_text(
        "".join(f"{s} {m} batch1\n" for s, m in sessions))
    print(f"\nsessions recorded in pph2_sessions_jak3.txt (valid for months)")


if __name__ == "__main__":
    main()
