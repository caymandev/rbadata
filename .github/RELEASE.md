# Release Process

This document describes how to release a new version of rbadata to PyPI.

## Prerequisites

1. Set up PyPI API tokens in GitHub repository secrets:
   - `PYPI_API_TOKEN` - For production PyPI releases
   - `TEST_PYPI_API_TOKEN` - For test PyPI releases (optional)

## Automated Release Process

### Option 1: Tag-based Release (Recommended)

1. Update version in `rbadata/__init__.py`
2. Commit your changes
3. Create and push a version tag:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
4. The `release.yml` workflow will automatically:
   - Run all tests
   - Build the package
   - Create a GitHub release with generated release notes
   - Publish to PyPI

### Option 2: Release-based Publishing

1. Create a new release on GitHub
2. The `publish.yml` workflow will automatically:
   - Run all tests
   - Build and publish to PyPI

### Option 3: Manual Test Publishing

1. Go to Actions → "Publish to PyPI" workflow
2. Click "Run workflow"
3. This will publish to TestPyPI for testing

## Manual Release Process

If you need to release manually:

```bash
# 1. Update version
# Edit rbadata/__init__.py

# 2. Build
make build

# 3. Test upload (optional)
make upload-test

# 4. Production upload
make upload
```

## Version Numbering

Follow semantic versioning (MAJOR.MINOR.PATCH):
- MAJOR: Breaking API changes
- MINOR: New features, backwards compatible
- PATCH: Bug fixes
