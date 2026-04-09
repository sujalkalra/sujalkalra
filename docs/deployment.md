# Deployment Steps

This repository is static + script-driven and can be deployed as a GitHub portfolio.

## Recommended pipeline
1. Run tests (`pytest -q`).
2. Validate scripts (`python sujal.py`, `python scripts/metrics_dashboard.py`).
3. Publish repository with updated README and docs.

## Optional enhancements
- Add CI workflow for automated checks.
- Add Dockerfile for reproducible runtime.
