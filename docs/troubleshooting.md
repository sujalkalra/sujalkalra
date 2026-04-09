# Troubleshooting Guide

## `python sujal.py` fails
- Ensure Python 3.11+ is installed.
- Verify script has not been edited with invalid syntax.

## `pytest` command not found
- Install pytest: `pip install pytest`.

## Metrics output seems zeroed
- Ensure requests were recorded before calling `summary()`.
- Validate non-negative latency inputs.
