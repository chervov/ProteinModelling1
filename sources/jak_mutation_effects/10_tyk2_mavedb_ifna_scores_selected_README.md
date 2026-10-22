# Selected TYK2 MaveDB DMS values

This table contains raw score values fetched on 2026-10-22 from the public MaveDB CSV downloads for ten TYK2 variants already represented in the curated literature table.

## Source and conditions

- `urn:mavedb:00001270-a` — Howard et al. TYK2 IFN-alpha signalling experiment: 10 score sets. The columns are labelled by IFN-alpha concentration and inhibitor condition.
- `urn:mavedb:00001271-a-1` — TYK2-VampDMS protein-abundance score set.
- The scores are from the 2025 Howard et al. bioRxiv preprint dataset deposited in MaveDB in 2026. They are raw assay scores, not calibrated clinical pathogenicity probabilities and not universal GOF/LOF calls.

## Exact retrieval endpoints

```text
https://api.mavedb.org/api/v1/experiments/urn:mavedb:00001270-a/score-sets
https://api.mavedb.org/api/v1/score-sets/urn:mavedb:00001270-a-N/scores
https://api.mavedb.org/api/v1/score-sets/urn:mavedb:00001271-a-1/scores
```

The complete score sets contain approximately 23,700 variants each. The compact file here is intentionally limited to variants for which the primary literature table gives independent functional context.
