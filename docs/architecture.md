# Architecture Description

## Design Principles
1. **Single responsibility**: profile rendering and metrics tracking are separate concerns.
2. **Safe defaults**: validation and explicit runtime error handling.
3. **Observability first**: logging and metrics summary in critical flows.

## Component Diagram (logical)
- Presentation Layer: `README.md`, docs.
- Application Layer: `sujal.py`, `metrics_dashboard.py`.
- Verification Layer: `tests/`.
- Data Layer: `components/*.json|*.md`.

## Tradeoffs
- Lightweight dependency footprint over heavy framework adoption.
- In-memory metrics over persistent storage (extensible later).
