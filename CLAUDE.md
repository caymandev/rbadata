# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

rbadata is a Python package for downloading and tidying data from the Reserve Bank of Australia (RBA). It provides a Python implementation inspired by the R package `readrba`, with comprehensive functionality for accessing RBA statistical tables, economic forecasts, and other economic data.

## Key Commands

### Development Setup
```bash
make dev-install    # Install with all development dependencies
```

### Testing
```bash
make test           # Run all tests
make coverage       # Run tests with coverage report
pytest tests/test_core.py::test_read_rba_single_table  # Run a single test
```

### Code Quality
```bash
make lint           # Run linting checks (flake8, black, isort)
make format         # Auto-format code with black and isort
make check          # Run all checks (lint + test + coverage)
```

### Building & Publishing
```bash
make build          # Build distribution packages
make upload-test    # Upload to TestPyPI
make upload         # Upload to PyPI
```

## Architecture Overview

### Core Data Pipeline
The main entry point is `read_rba()` in `core.py`, which implements a data pipeline:
1. **Download**: Fetches Excel files from RBA's statistical tables
2. **Tidy**: Processes raw data into clean pandas DataFrames
3. **Return**: Provides consistent DataFrame output with proper typing

### Module Organization
- **Data Access**: `core.py`, `download.py`, `tidy.py` - Main functionality
- **Data Discovery**: `browse.py` - Search and browse available data
- **Specialized Features**: Each feature (forecasts, cash_rate, calculator, etc.) is self-contained
- **Metadata**: JSON files in `data/` contain series and table information
- **Utilities**: `utils.py` provides shared functionality like URL generation

### Key Patterns
- Factory functions for creating instances (e.g., `get_chart_pack()`)
- Custom exceptions in `exceptions.py` for proper error handling
- Consistent API design across all modules
- Mocking external API calls in tests for reliability

## Testing Strategy

- Test files mirror the module structure (e.g., `rbadata/core.py` → `tests/test_core.py`)
- External API calls are mocked to ensure tests run offline
- Current coverage target: 97%
- Tests serve as usage examples

## Important Considerations

### Code Style
- Black formatter with line length 88
- Flake8 with exceptions for E203, W503
- isort for import organization
- Type hints are used throughout

### API Design
- All public functions are exported in `__init__.py` via `__all__`
- Functions return pandas DataFrames for consistency
- Error messages are user-friendly and actionable

### Performance
- Some modules implement caching for frequently accessed data
- Bulk operations are supported for efficiency
- Connection pooling is used for multiple requests