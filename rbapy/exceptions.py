"""
Custom exceptions for rbapy
"""


class RBAPyError(Exception):
    """Base exception for all rbapy errors."""
    pass


class DownloadError(RBAPyError):
    """Raised when a download fails."""
    pass


class DataError(RBAPyError):
    """Raised when data cannot be parsed or is invalid."""
    pass


class ConnectionError(RBAPyError):
    """Raised when connection to RBA cannot be established."""
    pass