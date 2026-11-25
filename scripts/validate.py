"""Check the structure and referential integrity of the released catalogue."""
import csv
import json
import collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def load(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))

rows = load("Australian_Window_Manufacturer_Catalogue.csv")
sources = load("sources.csv")
index = {s["source_id"]: s for s in sources}
snapshot = json.loads((DATA / "snapshot.json").read_text())
assert len(index) == len(sources), "Duplicate source IDs"
assert len({r["record_id"] for r in rows}) == len(rows), "Duplicate record IDs"
allowed = {"standard_size", "size_review", "chart_group_size", "example_size",
           "corner_wing", "corner_pair", "dimensional_limit", "chart_axes",
           "product_option", "directory_lead"}
for row in rows:
    rid = row["record_id"]
    assert row["record_type"] in allowed, rid
    assert row["manufacturer"] and row["source_url"], rid
    assert row["source_id"] in index, rid
    assert row["source_url"] == index[row["source_id"]]["source_url"], rid
    if row["record_type"] == "standard_size":
        assert float(row["width_mm"]) > 0 and float(row["height_mm"]) > 0, rid
        assert row["dimension_basis"], rid
    for key, val in row.items():
        if key.endswith("_mm") and "_axis_" not in key and val:
            assert float(val) > 0, (rid, key)
assert len(rows) == snapshot["total_records"]
counts = collections.Counter(r["record_type"] for r in rows)
assert counts["standard_size"] == snapshot["standard"]
assert len(sources) == snapshot["sources"]
print(f"OK: {len(rows):,} records, {len(sources):,} sources.")
print(dict(counts))
