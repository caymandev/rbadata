# rbapy

A Python package to download and tidy data from the Reserve Bank of Australia (RBA).

This package is a Python implementation inspired by the R package `readrba`, providing similar functionality for accessing RBA statistical tables and economic forecasts.

## Installation

```bash
pip install rbapy
```

## Quick Start

```python
import rbapy

# Read a single RBA table
cpi_table = rbapy.read_rba(table_no="g1")

# Read multiple tables
data = rbapy.read_rba(table_no=["a1", "g1"])

# Read by series ID
cpi_series = rbapy.read_rba(series_id="GCPIAG")

# Get RBA forecasts
forecasts = rbapy.rba_forecasts()

# Browse available tables and series
tables = rbapy.browse_rba_tables()
series = rbapy.browse_rba_series("inflation")
```

## Features

- Download current and historical RBA statistical tables
- Access RBA economic forecasts since 1990
- Search and browse available data series
- Automatic data tidying into pandas DataFrames
- Robust error handling and retry logic

## License

MIT License

## Disclaimer

This package is not affiliated with or endorsed by the Reserve Bank of Australia. All data is provided subject to any conditions and restrictions set out on the RBA website.