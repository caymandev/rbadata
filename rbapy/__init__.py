"""
rbapy - Download and tidy data from the Reserve Bank of Australia
"""

__version__ = "0.1.0"

from .core import read_rba, read_rba_seriesid
from .browse import browse_rba_series, browse_rba_tables
from .forecasts import rba_forecasts
from .cash_rate import read_cashrate

__all__ = [
    "read_rba",
    "read_rba_seriesid",
    "browse_rba_series",
    "browse_rba_tables",
    "rba_forecasts",
    "read_cashrate",
]