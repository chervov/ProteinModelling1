#!/usr/bin/env python3
"""Score selected TYK2 substitutions with ESM-2 8M zero-shot log likelihood ratios.

This is a research comparison, not a clinical classifier. It downloads UniProt P29597
and the public ESM-2 checkpoint on first run. Scores are model likelihood differences
(mutant minus wild type); they are not ESM-1b or AlphaMissense scores.
"""

import csv
import math
import urllib.request
from pathlib import Path

import esm
import torch


ROOT = Path(__file__).resolve().parent
VARIANTS_PATH = ROOT / "variants.tsv"
UNIPROT_FASTA = "https://rest.uniprot.org/uniprotkb/P29597.fasta"
WINDOW_LENGTH = 1022


def fetch_sequence():
    with urllib.request.urlopen(UNIPROT_FASTA, timeout=60) as response:
        fasta_lines = response.read().decode("utf-8").splitlines()
    return "".join(line.strip() for line in fasta_lines if not line.startswith(">"))


def context_window(sequence, position):
    index = position - 1
    start = max(0, min(index - WINDOW_LENGTH // 2, len(sequence) - WINDOW_LENGTH))
    return sequence[start : start + WINDOW_LENGTH], start


def main():
    sequence = fetch_sequence()
    model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()
    model.eval()
    batch_converter = alphabet.get_batch_converter()

    with VARIANTS_PATH.open() as handle:
        variants = list(csv.DictReader(handle, delimiter="\t"))

    print("variant\tmodel\twindow_start\tesm2_8m_llr_mut_minus_wt")
    for variant in variants:
        position = int(variant["position"])
        expected = variant["wild_type"]
        observed = sequence[position - 1]
        if observed != expected:
            raise ValueError(f"{variant['variant']}: expected {expected}, UniProt has {observed}")
        window, start = context_window(sequence, position)
        _, _, tokens = batch_converter([(variant["variant"], window)])
        with torch.no_grad():
            logits = model(tokens, repr_layers=[])["logits"]
        log_probs = torch.log_softmax(logits[0, position - start], dim=-1)
        mutant_log_probability = log_probs[alphabet.get_idx(variant["mutant"])].item()
        wild_type_log_probability = log_probs[alphabet.get_idx(expected)].item()
        score = mutant_log_probability - wild_type_log_probability
        print(f"{variant['variant']}\tesm2_t6_8M_UR50D\t{start + 1}\t{score:.6f}")


if __name__ == "__main__":
    main()
