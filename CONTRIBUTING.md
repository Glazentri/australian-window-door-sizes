# Contributing

Thank you for helping improve Australia's open window and door reference data.

1. Open a catalogue correction or new manufacturer request with a direct, official source URL, edition/date, page number and state/region.
2. Identify the exact product series, product type, configuration, handing (if documented), and whether dimensions are frame, reveal, stud opening or panel size.
3. Transcribe only published combinations. Record independent dimensions as limits or separate chart axes. If a source contradicts itself, flag it for review rather than making an assumption.
4. Keep dimensions numeric in millimetres and leave unknowns empty. Preserve the original source ID and URL. Never upload manufacturer PDFs, images, CAD families, pricing files or other assets without appropriate permission.
5. Add the source to `data/sources.csv`, update the coverage index when needed, and run `python scripts/validate.py`. Update the snapshot statistics and workbook when publishing a coordinated release.

Contributors should confirm they have authority to contribute their original material and should not represent third-party material as their own. Data derived from manufacturer sources must retain attribution and relevant limitations. See DATA_TERMS.md.

Use a pull request for data changes and document the reason, edition and affected records. Suspected incorrect values or ambiguous dimension bases can also be reported as issues.
