# Data dictionary

Master CSV: UTF-8 with BOM, comma-delimited, one record per evidence item. Numeric fields are millimetres unless the suffix explicitly indicates another unit. Blank means unknown, unrecorded or not applicable; never assume zero.

## Record types

| Type | Meaning |
| --- | --- |
| standard_size | Published size pair or checked catalogue cell; candidate only, not necessarily complete SKU |
| size_review | Pair with a subtype ambiguity or conflict with a limit; resolve before matching |
| chart_group_size | Published size pair in a chart group, with precise configuration to check |
| example_size | Published illustrative size, not proof of a full standard range |
| corner_wing | Individual wing width option; not an approved pair of wings |
| corner_pair | Explicit paired corner assembly; use both wing values and height |
| dimensional_limit | Independent overall or sash/panel bounds; not all combinations guaranteed |
| chart_axes | Separately published width and height axes; no cell-level implication |
| product_option | Product/series, configurations and documented option information |
| directory_lead | Unverified supplier or business research lead; no dimensional guarantee |

## Field definitions

| Field | Definition |
| --- | --- |
| record_id | Unique snapshot record identifier; retain during updates |
| record_type | Evidence class listed above |
| manufacturer | Brand, system provider or directory-listed company |
| region | Region or state stated or captured for the source; not a geographic availability guarantee |
| series | Published series, suite, system or chart grouping |
| product_type | Product category; categories are not yet a fully harmonised ontology |
| configuration | Panel or opening arrangement as published or described |
| catalogue_code | Printed catalogue identifier or chart-derived reference; verify suffix and full order code |
| width_mm, height_mm | Published size pair, interpreted using dimension_basis |
| dimension_basis | Frame, reveal, stud opening, panel or source-specific dimensional reference |
| stud_opening_width_mm, stud_opening_height_mm | Stud opening dimensions only when present in the source |
| min_width_mm, max_width_mm, min_height_mm, max_height_mm | Independent dimensional bounds for a product, per dimension_basis |
| max_sash_panel_width_mm, max_sash_panel_height_mm | Sash or panel maximums, not assembly widths/heights |
| wing1_width_mm, wing2_width_mm | Corner wing dimensions, as recorded in the source |
| max_area_m2 | Area limit, square metres |
| max_panel_weight_kg | Panel weight limit in kilograms |
| panel_count | Number of panels when stated |
| code_prefix | Code family for chart axes |
| width_axis_mm, height_axis_mm | Semicolon-separated published axis values, **not combinations** |
| frame_material | Material where captured |
| glazing | Published glazing options or specification |
| handing | Handing only where captured; do not infer external view |
| availability | Size evidence status, not actual stock |
| record_status | Evidence/review status |
| custom_availability | Published custom availability or confirmation requirement |
| options | Additional published product option summary |
| restriction | Relevant qualification or constraint |
| notes | Context, evidence interpretation and review reminders |
| website | Website associated with a research lead |
| source_id | Foreign key to data/sources.csv |
| source_page | PDF page number where captured; blank for web pages |
| source_url | Publisher or directory reference URL |

## Integration guidance

Preserve raw source values and map to canonical project fields in a separate layer. A matching engine should first enforce the product class, region and dimension basis; a close dimensional match is not a compatible product match when any of those differ. Model rough opening, frame, sill, subsill and reveal as separate properties. Do not derive missing values from unrelated brands. For pricing, add independently supplied price-book and effective-date records, not invented prices.

The Excel workbook separates the evidence classes on filterable sheets. CSV data is the canonical machine-readable snapshot; neither is a substitute for a confirmed manufacturer quote.
