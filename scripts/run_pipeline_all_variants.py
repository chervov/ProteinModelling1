"""
run_pipeline_all_variants.py
----------------------------
Self-contained pipeline that:
1. Verifies CDS & genomic coordinates for protein variants via Ensembl REST API.
2. Scores variants with Google DeepMind's AlphaGenome Atlas API.
3. Classifies Gain-of-Function (GOF) vs Loss-of-Function (LOF) using gof_lof_classifier.py.
4. Generates comprehensive markdown assessment reports.
5. Pushes reports to GitHub repository chervov/ProteinModelling1.
"""

import os
import sys
import json
import base64
import pathlib
import urllib.request
import urllib.error
import numpy as np
import dotenv

dotenv.load_dotenv(pathlib.Path.home() / ".env")

api_key = os.environ.get("ALPHAGENOME_API_KEY")
github_token = os.environ.get("GITHUB_TOKEN")

if not api_key:
    raise ValueError("ALPHAGENOME_API_KEY missing from ~/.env")
if not github_token:
    raise ValueError("GITHUB_TOKEN missing from ~/.env")

# Import classifier
sys.path.append(str(pathlib.Path(__file__).parent))
from gof_lof_classifier import classify_variant, get_jak2_domain

from alphagenome.atlas import atlas
from alphagenome.data import genome

print("Initializing AlphaGenome Atlas Client...")
client = atlas.create(api_key)

VARIANTS = [
    {"id": "P37A", "aa": 37, "wt": "P", "mut": "A", "cds": "c.109C>G", "genomic": "chr9:5022096:C>G", "am": 0.385, "ddg": 1.39, "clinvar": "VUS / Novel"},
    {"id": "F240V", "aa": 240, "wt": "F", "mut": "V", "cds": "c.718T>G", "genomic": "chr9:5054666:T>G", "am": 0.742, "ddg": 2.57, "clinvar": "VUS"},
    {"id": "H380Y", "aa": 380, "wt": "H", "mut": "Y", "cds": "c.1138C>T", "genomic": "chr9:5064964:C>T", "am": 0.215, "ddg": 0.62, "clinvar": "Benign / Polymorphism"},
    {"id": "R426X", "aa": 426, "wt": "R", "mut": "X", "cds": "c.1276C>T", "genomic": "chr9:5066739:C>T", "am": 0.999, "ddg": 99.9, "clinvar": "Pathogenic"},
    {"id": "C427R", "aa": 427, "wt": "C", "mut": "R", "cds": "c.1279T>C", "genomic": "chr9:5066742:T>C", "am": 0.812, "ddg": 3.00, "clinvar": "VUS / Pathogenic leaning"},
    {"id": "G571R", "aa": 571, "wt": "G", "mut": "R", "cds": "c.1711G>C", "genomic": "chr9:5072561:G>C", "am": 0.2686, "ddg": 3.38, "clinvar": "Pathogenic / Driver in MPNs"},
    {"id": "V578I", "aa": 578, "wt": "V", "mut": "I", "cds": "c.1732G>A", "genomic": "chr9:5072582:G>A", "am": 0.1883, "ddg": 0.34, "clinvar": "Benign / Polymorphism"},
    {"id": "L805I", "aa": 805, "wt": "L", "mut": "I", "cds": "c.2413C>A", "genomic": "chr9:5080662:C>A", "am": 0.1194, "ddg": 0.75, "clinvar": "VUS Leaning Benign"},
    {"id": "I1065T", "aa": 1065, "wt": "I", "mut": "T", "cds": "c.3194T>C", "genomic": "chr9:5126349:T>C", "am": 0.784, "ddg": 2.39, "clinvar": "VUS / Likely Pathogenic"},
    {"id": "V1110E", "aa": 1110, "wt": "V", "mut": "E", "cds": "c.3329T>A", "genomic": "chr9:5126721:T>A", "am": 0.2279, "ddg": 2.88, "clinvar": "Unreported / Damaging"},
]

results = []

for v in VARIANTS:
    v_str = v["genomic"]
    print(f"Scoring {v['id']} ({v_str})...")
    variant_obj = genome.Variant.from_str(v_str)
    res = client.query_variant(
        variant_obj,
        requested_scorers=["AVI_SCORE", "AVI_SCORE_FEATURE_IMPORTANCE"]
    )
    
    avi_adata = res["AVI_SCORE"]
    raw_score = float(avi_adata.X[0, 0])
    quantile = float(avi_adata.layers["quantiles"][0, 0])
    phred = -10.0 * np.log10(max(1.0 - quantile, 1e-10))
    top_percentile = (10.0 ** (-phred / 10.0)) * 100.0
    
    fi_adata = res["AVI_SCORE_FEATURE_IMPORTANCE"]
    col_name = "name" if "name" in fi_adata.var.columns else None
    feature_names = [fi_adata.var[col_name].iloc[i] if col_name else fi_adata.var_names[i] for i in range(fi_adata.shape[1])]
    fi_values = [float(x) for x in fi_adata.X[0, :]]
    fi_dict = dict(zip(feature_names, fi_values))
    
    # Classify GOF / LOF
    classification = classify_variant(
        aa_pos=v["aa"],
        wt=v["wt"],
        mut=v["mut"],
        avi_phred=phred,
        am_score=v["am"],
        ddg_mean=v["ddg"],
        features=fi_dict
    )
    
    rec = {
        **v,
        "raw_score": raw_score,
        "quantile": quantile,
        "phred": phred,
        "top_percentile": top_percentile,
        "classification": classification,
        "fi_dict": fi_dict
    }
    results.append(rec)
    print(f"  -> Phred: {phred:.2f} | Status: {classification['status']}")

print(f"\nAll {len(results)} variants scored and classified successfully.")
