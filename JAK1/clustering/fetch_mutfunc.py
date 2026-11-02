"""Query mutfunc.com programmatically through its Dash callback endpoint.

mutfunc has no public API: /about 404s and there is no download page. It is a Dash app, so
the only backend is POST /_dash-update-component. The callback graph from /_dash-dependencies
gives two steps:

    go-btn.n_clicks  + state user-input.value  ->  redirect.href + variant-list.data
    variant-list.data                          ->  variants.rowData + variants.selectedRows

So: submit the variant text, take variant-list.data from the response, feed it to the second
callback, read the table. This is an undocumented internal interface on an academic server -
batches are kept small and spaced.
"""
import json
import sys
import time

import requests

BASE = "http://www.mutfunc.com"
EP = f"{BASE}/_dash-update-component"
HDRS = {"Content-Type": "application/json", "Accept": "application/json",
        "User-Agent": "claude-code research script (one protein, JAK1)"}


def post(payload, tries=3):
    for a in range(1, tries + 1):
        try:
            r = requests.post(EP, json=payload, headers=HDRS, timeout=300)
            r.raise_for_status()
            return r.json()
        except Exception as exc:                            # noqa: BLE001
            if a == tries:
                raise
            print(f"      retry {a}: {type(exc).__name__}: {str(exc)[:120]}")
            time.sleep(5 * a)


def submit(text):
    """Step 1: hand the variant text to the Parse Variants callback."""
    return post({
        "output": "..redirect.href...variant-list.data..",
        "outputs": [{"id": "redirect", "property": "href"},
                    {"id": "variant-list", "property": "data"}],
        "inputs": [{"id": "go-btn", "property": "n_clicks", "value": 1}],
        "changedPropIds": ["go-btn.n_clicks"],
        "state": [{"id": "user-input", "property": "value", "value": text}],
    })


def table(variant_list):
    """Step 2: turn variant-list.data into the results table."""
    return post({
        "output": "..variants.rowData...variants.selectedRows..",
        "outputs": [{"id": "variants", "property": "rowData"},
                    {"id": "variants", "property": "selectedRows"}],
        "inputs": [{"id": "variant-list", "property": "data", "value": variant_list}],
        "changedPropIds": ["variant-list.data"],
        "state": [],
    })


if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else "P23458 A1005E\nP23458 I617T\nP23458 A1005D"
    print(f"submitting {len(text.splitlines())} variants")

    r1 = submit(text)
    print("\n--- step 1 response ---")
    print(json.dumps(r1, indent=2)[:1200])

    rv = (r1.get("response") or {}).get("variant-list", {}).get("data")
    if rv is None:
        print("\nno variant-list.data in the response; stopping")
        sys.exit(1)
    print(f"\nvariant-list.data: {json.dumps(rv)[:400]}")

    r2 = table(rv)
    rows = (r2.get("response") or {}).get("variants", {}).get("rowData")
    print("\n--- step 2: table ---")
    if rows:
        print(f"{len(rows)} rows; keys of the first: {sorted(rows[0].keys())}")
        for row in rows:
            print("   " + json.dumps(row))
    else:
        print(json.dumps(r2, indent=2)[:1500])
