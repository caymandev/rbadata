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

## Advanced Usage

### Inflation Calculator

```python
# Calculate inflation-adjusted values
calc = rbapy.InflationCalculator()

# How much was $100 in 2000 worth in 2023?
value_2023 = calc.calculate_value(100, "2000", "2023")

# Calculate inflation rate
inflation_rate = calc.calculate_inflation_rate("2020", "2023")

# Quick calculation
adjusted_value = rbapy.inflation_calculator(1000, "2010", "2023")
```

### Chart Pack

```python
# Access RBA Chart Pack
chart_pack = rbapy.get_chart_pack()

# Get available categories
categories = chart_pack.get_categories()

# Get charts by category
inflation_charts = chart_pack.get_charts_by_category("inflation")

# Download the full Chart Pack PDF
chart_pack.download_chart_pack()
```

### Economic Snapshots

```python
# Get economic indicators snapshot
indicators = rbapy.get_economic_indicators()

# Access snapshots
snapshots = rbapy.get_snapshots()
snapshots.download_snapshot("economic-indicators")
```

### Glossary

```python
# Look up term definitions
definition = rbapy.define("CPI")

# Search for terms
glossary = rbapy.get_glossary()
inflation_terms = glossary.search("inflation")
```

## Features

### Core Features
- Download current and historical RBA statistical tables
- Access RBA economic forecasts since 1990
- Search and browse available data series
- Automatic data tidying into pandas DataFrames
- Robust error handling and retry logic

### Additional Features
- **Inflation Calculator**: Calculate inflation-adjusted values and inflation rates
- **Chart Pack Access**: Download and explore RBA Chart Pack data
- **Economic Snapshots**: Access key economic indicators and visualizations
- **Statistical Alerts**: Set up notifications for new data releases
- **Glossary**: Look up definitions of economic and financial terms

## License

MIT License

## Disclaimer

This package is not affiliated with or endorsed by the Reserve Bank of Australia. All data is provided subject to any conditions and restrictions set out on the RBA website.