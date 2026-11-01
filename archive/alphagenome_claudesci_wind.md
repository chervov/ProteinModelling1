# AlphaGenome on Claude Science (Windows sandbox) — working setup

Record of a session (2026-11-01) in which the AlphaGenome API was connected from a
Claude Science workspace running on native Windows. Hand this file to a fresh session
to skip the dead ends: the connection took ~25 minutes the first time, almost all of
it spent on two non-obvious sandbox issues documented in "Errors hit" below.

Verified working: `alphagenome` 0.10.0, Python 3.11, Windows sandbox, 2026-11-01.

---

## 1. Get the API key

Register at <https://deepmind.google.com/science/alphagenome/> → "Get API Key".
Free for non-commercial use, subject to the terms on that page. The key is a
39-character Google API key.

## 2. Store the key as a credential (do not paste it into chat)

Claude Science UI: **Customize → Credentials → Add**

| field | value |
|---|---|
| Service / name | `ALPHAGENOME` |
| Type | API key / generic secret |
| Environment variable name (if asked) | `ALPHAGENOME_API_KEY` |
| Value | the key |
| URL / username | leave blank |

**Important — reading the key back.** A generic secret is *not* injectable through a
cell's `credentials=[...]` parameter. Declaring `credentials=["ALPHAGENOME"]` fails with

```
No credential named "ALPHAGENOME" — the cell did not run. Available: "GitHub".
```

Read it in-kernel instead:

```python
KEY = host.credentials.get("ALPHAGENOME")["value"]
```

This works in any analysis kernel and the value is redacted from cell output.

## 3. Create a dedicated environment

AlphaGenome pulls in grpcio, protobuf, anndata and jax — keep it out of the shared env:

```
manage_environments(mode="create", name="alphagenome", language="python", python_version="3.11")
manage_packages(environment="alphagenome", mode="install", packages=["alphagenome"], use_pip=True)
```

## 4. Allow the endpoint through the network sandbox

The client dials **`dns:///gdmscience.googleapis.com:443`** over gRPC
(see `src/alphagenome/models/v1/dna_client.py`, the `create()` function).
That host is not on the default allowlist, so request it once:

```
request_network_access(domain="gdmscience.googleapis.com",
                       reason="AlphaGenome API endpoint (gRPC)")
```

## 5. Working snippet

```python
import os
# gRPC does not pick up the sandbox proxy from HTTP_PROXY, and does not use the
# sandbox CA bundle. Both must be set BEFORE the client is created.
os.environ["grpc_proxy"] = os.environ["HTTPS_PROXY"]
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = os.environ["REQUESTS_CA_BUNDLE"]

from alphagenome.data import genome
from alphagenome.models import dna_client, variant_scorers

model = dna_client.create(host.credentials.get("ALPHAGENOME")["value"])

# catalogue of available output tracks
md = model.output_metadata(organism=dna_client.Organism.HOMO_SAPIENS)

# score one variant
variant  = genome.Variant(chromosome="chr22", position=36201698,
                          reference_bases="A", alternate_bases="C")
interval = variant.reference_interval.resize(2**17)          # 131,072 bp
scores   = model.score_variant(
    interval=interval, variant=variant,
    variant_scorers=[variant_scorers.RECOMMENDED_VARIANT_SCORERS["RNA_SEQ"]])
```

With the two environment variables set, calls return in well under a second.

---

## Errors hit, and what they actually were

**1. First call hung for 9 minutes with no error.**
`dna_client.create()` blocks in `grpc.channel_ready_future(channel).result(timeout)`.
The sandbox drops non-allowlisted outbound connections rather than refusing them, so
gRPC waits instead of failing. Cause: `gdmscience.googleapis.com` not yet allowlisted.
Fix: `request_network_access` (step 4).

**2. The hung cell ignored SIGINT.**
`host.exec_interrupt()` reported `{'interrupted': True, 'via': 'sigint'}` twice while
the cell kept running; it only unwound after ~545 s. gRPC's C core does not respond to
Ctrl-C while blocked in a channel wait. Do not wait for it — dispatch work to another
environment, or run a one-shot subprocess with the interpreter at
`...\.claude-science\conda\envs\alphagenome\python.exe` and a real `timeout=`.

**3. Allowlisting alone was not enough.**
After the grant, a raw socket test still failed instantly:

```
socket.create_connection(("gdmscience.googleapis.com", 443)) -> gaierror 11001 getaddrinfo failed
```

There is no direct DNS in the sandbox; everything goes through an HTTP CONNECT proxy
(`HTTP_PROXY` / `HTTPS_PROXY`, e.g. `http://127.0.0.1:<port>`), with TLS interception
using the bundle at `REQUESTS_CA_BUNDLE`. `requests.get()` worked (HTTP 404 from the
Google frontend = reachable) because requests honours those variables. gRPC does not:
it needs lowercase `grpc_proxy`, and it ignores `SSL_CERT_FILE` in favour of its own
root store unless `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` is set. Setting both fixed it.

**4. Misread the result shape.**
`score_variant` with the RNA-seq scorer returns an `AnnData` of shape
**(genes x tracks)** — here 12 x 371. `obs` carries `gene_id`, `gene_name`, `strand`,
`gene_type`; `var` carries `name`, `biosample_name`, `ontology_curie`, `gtex_tissue`.
It is not tracks-by-outputs; indexing it that way raises
`IndexError: positional indexers are out-of-bounds`.

---

## Verification performed

`output_metadata(HOMO_SAPIENS)` returned the full human catalogue:

| output | tracks |
|---|---|
| chip_tf | 1617 |
| chip_histone | 1116 |
| splice_site_usage | 734 |
| rna_seq | 667 |
| cage | 546 |
| splice_junctions | 367 |
| dnase | 305 |
| atac | 167 |
| contact_maps | 28 |
| procap | 12 |
| splice_sites | 4 |

End-to-end prediction, `chr22:36201698:A>C`, 131,072 bp window, RNA-seq scorer:
12 genes x 371 tracks returned; strongest effect on **APOL4**, -3.06 in K562,
followed by cardiac ventricle fibroblast -2.89, cardiac atrium fibroblast -2.81,
pericardium fibroblast -2.76. (A smoke test, not a biological claim.)

---

## Links

- AlphaGenome API & key registration — <https://deepmind.google.com/science/alphagenome/api>
- Client source (endpoint constant lives here) — <https://github.com/google-deepmind/alphagenome>
- Docs / quick start — <https://www.alphagenomedocs.com/colabs/quick_start.html>
- PyPI package — <https://pypi.org/project/alphagenome/>

### DeepMind science skills

<https://github.com/google-deepmind/science-skills> — 40 agent skills for scientific
databases and tools (3,374 stars as of 2026-10-23). AlphaGenome-relevant ones:

- `skills/alphagenome_single_variant_analysis/SKILL.md` — variant effects on expression,
  accessibility, histone marks, TF binding; tissue/cell-type ontology resolution
- `skills/alphagenome_variant_impact_score/SKILL.md`
- `skills/alphagenome_atlas_website_links/SKILL.md`
- `skills/credentials/SKILL.md` — their safe-credentials protocol. Note it assumes a
  `~/.env` file checked with `grep -sq`; on Claude Science the credential store plus
  `host.credentials.get(...)` replaces that, and `grep` does not exist on the Windows host.

Related: `skills/clinvar_database`, `skills/gnomad_database`, `skills/gtex_database`,
`skills/ensembl_database`, `skills/encode_ccres_database`, `skills/jaspar_database`,
`skills/alphafold_database_fetch_and_analyze`, `skills/pdb_database`,
`skills/uniprot_database`, `skills/foldseek_structural_search`, `skills/pymol`.

---

## Checklist for a new session

1. `host.credentials.list()` shows `ALPHAGENOME` (generic) — if not, re-add it (step 2).
2. Environment `alphagenome` exists with the package — else step 3.
3. `gdmscience.googleapis.com` allowlisted — else step 4.
4. Set `grpc_proxy` and `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` before creating the client.
5. Smoke test with `output_metadata`; a hang means step 4 or the proxy vars, not the key.
