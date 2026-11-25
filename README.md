# Australian Window & Door Catalogue

**An open, source-linked reference dataset for Australian window and door sizing, estimating, design and BIM workflows.**

Maintained by Adrian Woolley / [WinMatch by Glazentri](https://winquotes.com.au/). The repository is independent of the WinMatch Revit and Archicad tools; anyone can use the data in a spreadsheet, a window schedule, a custom application or a BIM integration.

[![Data snapshot](https://img.shields.io/badge/snapshot-2026--11--26-126A64)](data/snapshot.json)
[![Records](https://img.shields.io/badge/records-8%2C141-126A64)](data/snapshot.json)
[![Code license](https://img.shields.io/badge/code-MIT-blue)](LICENSE)

## Download

| File | Purpose |
| --- | --- |
| [Excel catalogue (.xlsx)](data/Australian_Window_Manufacturer_Catalogue.xlsx) | Filterable workbook, with nine worksheets and a start page |
| [Master catalogue (.csv)](data/Australian_Window_Manufacturer_Catalogue.csv) | Machine-readable catalogue, with every evidence type explicitly tagged |
| [Manufacturer coverage (.csv)](data/manufacturers.csv) | Coverage by brand and system supplier |
| [Source register (.csv)](data/sources.csv) | Publisher links, editions and retrieval status |
| [Extraction QA (.csv)](data/extraction_qa.csv) | Page-level extraction coverage |
| [Data dictionary](docs/data-dictionary.md) | Field definitions, units and record interpretation |
| [Data rights and attribution](DATA_TERMS.md) | Distinction between project material and third-party catalogue sources |

## Why this exists

Window schedules frequently mix frame dimensions, structural openings, reveal sizes, nominal size codes and manufacturer-specific configurations. This makes like-for-like quoting difficult. The catalogue retains the original dimension basis and the source for each record instead of pretending all products and size grids are interchangeable.

Use it to identify potential standard sizes, compare regional product offerings, review large sliding and stacking doors, populate an estimating library, or build a source-aware BIM product picker. It does not constitute a live stock list, manufacturer quotation, compliance assessment or approved fabrication schedule.

## Initial dataset — v0.1.0

| Coverage | Records |
| --- | ---: |
| Standard-size candidates | 7,029 |
| Other size, review, corner and example records | 399 |
| Dimensional limits | 241 |
| Chart-axis references | 126 |
| Product and option references | 189 |
| Additional directory research leads | 157 |
| **Total catalogue records** | **8,141** |
| Brands and systems with product or size information | 28 |
| Source references | 226 |

Example brands: A&L, Bradnam's, Dowell, G.James, Hanlon, Jason, Southern Star, Stegbar, Suncoast, Trend, Wideline, Rylock, Valley, Paarhammer, Miglas and more. Architectural Window Systems, Alspec and Darley supply systems and are identified accordingly, not counted as a single finished-window manufacturer.

Coverage varies by brand, series, region and catalogue edition. This initial snapshot is deliberately not described as an exhaustive Australian market census. Additional businesses are directory leads rather than verified catalogue entries.

## Matching workflow

1. Select only records with `record_type == standard_size` for standard-size candidate results.
2. Match manufacturer, region, product type, series and configuration before comparing width and height.
3. Compare like with like: only dimensions with the same `dimension_basis` are directly comparable. Do not substitute reveal or rough-opening dimensions for actual frame dimensions.
4. Use separate `dimensional_limit` rows to flag potential custom options, never to guarantee that any combination within the maximum dimensions works.
5. Review the original source and confirm current availability, handing, glazing, performance and exact ordering reference with the manufacturer.

Empty values mean not recorded or unknown, not zero or unavailable. The `chart_axes` records contain separate axes, not a grid of confirmed combinations. Some size numbers are transcribed from sampled or visually checked catalogue cells rather than explicit orderable SKUs. No current pricing is inferred.

## Read the CSV with Python

Python 3.10+; no third-party dependencies required.

```python
import csv

with open("data/Australian_Window_Manufacturer_Catalogue.csv",
          encoding="utf-8-sig", newline="") as file:
    for row in csv.DictReader(file):
        if (row["record_type"] == "standard_size"
                and row["manufacturer"] == "A&L Windows"
                and row["width_mm"] == "1210"
                and row["height_mm"] == "514"):
            print(row["product_type"], row["configuration"],
                  row["dimension_basis"], row["source_url"])
```

This returns candidates, not approval to order.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Manufacturer catalogue corrections, newly published standard sizes, regional differences and official source links are particularly welcome. Preserve distinct product series and dimension bases; never generate every width × height combination without cell-level evidence.

Run the lightweight structural validator:

```sh
python scripts/validate.py
```

The validator checks the data shape and source references, not live product availability or engineering suitability.

## Licence and attribution

Original code and tooling: MIT. Original project documentation and original database-compilation material, **only to the extent the contributor owns the rights**, are offered under CC BY 4.0. Underlying third-party catalogue publications, logos, imagery, software and protected material are not relicensed or included. See [DATA_TERMS.md](DATA_TERMS.md). Check source-specific terms and publication/redistribution rights before public release or reuse.

This is an independent research project; manufacturers named are not necessarily affiliated with or endorsing WinMatch.
