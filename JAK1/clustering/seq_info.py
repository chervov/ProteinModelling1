"""Record the sequence identity explicitly: accession, entry name, length, checksums.

The FASTA header carries this too, but as prose on one line. A separate file makes it
checkable by a script, and pins which sequence version the variant numbering refers to.
"""
import hashlib
import json
import pathlib
import time

import requests

HERE = pathlib.Path(__file__).parent
fasta = (HERE / "JAK1_P23458.fasta").read_text(encoding="utf-8").splitlines()
header, seq = fasta[0], "".join(l.strip() for l in fasta[1:])

meta = None
for attempt in range(1, 5):
    try:
        r = requests.get("https://www.ebi.ac.uk/proteins/api/proteins/P23458",
                         headers={"Accept": "application/json"}, timeout=120)
        r.raise_for_status()
        meta = r.json()
        break
    except Exception as exc:                        # noqa: BLE001
        print(f"  attempt {attempt}: {type(exc).__name__}")
        time.sleep(5 * attempt)

info = {
    "uniprot_accession": "P23458",
    "uniprot_entry_name": "JAK1_HUMAN",
    "gene": "JAK1",
    "protein_name": "Tyrosine-protein kinase JAK1",
    "organism": "Homo sapiens (9606)",
    "sequence_length": len(seq),
    "fasta_header": header,
    "md5": hashlib.md5(seq.encode()).hexdigest(),
    "sha256": hashlib.sha256(seq.encode()).hexdigest(),
    "source": "https://rest.uniprot.org/uniprotkb/P23458.fasta",
    "retrieved": "2026-11-02",
    "variant_numbering": "1-based; variant_id in Dataset EV1 refers to this sequence",
    "ev1_rows": 23080,
    "ev1_real_substitutions": 21926,
    "ev1_self_substitutions": 1154,
    "positions_covered_by_ev1": 1154,
    "wt_residues_matching_this_sequence": "23080 of 23080",
}
if meta:
    info["uniprot_entry_version"] = meta.get("info", {}).get("version")
    info["uniprot_last_modified"] = meta.get("info", {}).get("modified")
    info["uniprot_dataset"] = meta.get("info", {}).get("type")
    api_len = (meta.get("sequence") or {}).get("length")
    info["length_agrees_with_uniprot_api"] = (api_len == len(seq))
    info["uniprot_api_length"] = api_len

(HERE / "jak1_sequence_info.json").write_text(
    json.dumps(info, indent=2) + "\n", encoding="utf-8")
print(json.dumps(info, indent=2))
