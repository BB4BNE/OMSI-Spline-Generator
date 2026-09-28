# OMSI Spline Generator

Generate OMSI `.sli` spline files from the road templates in this repository
and definitions in the configured Excel workbook.

## Run locally

The tool requires Python 3.10 or newer. Its configuration currently lives
in `tool/config.py` and points to the local Excel workbook and
OMSI output directory.

```powershell
.\venv\Scripts\python.exe .\tool\main.py
```

`main.py` remains a convenience launcher, so `.\venv\Scripts\python.exe .\main.py` also works.

## Layout

- `tool/main.py` contains the generation workflow.
- `tool/formatting.py` contains OMSI output formatting.
- `tool/templates/` contains spline, surface, piece, and
  decoration definitions.
- `tool/config.py` holds runtime paths and Excel table names.
