from __future__ import annotations

import time

import pytest

from scripts.metrics_dashboard import MetricsDashboard


def test_metrics_summary_happy_path() -> None:
    dashboard = MetricsDashboard()
    dashboard.record_request(100.0, success=True)
    dashboard.record_request(200.0, success=False)

    summary = dashboard.summary()
    assert summary["request_count"] == 2.0
    assert summary["error_count"] == 1.0
    assert summary["average_latency_ms"] == 150.0
    assert 0.0 <= summary["error_rate"] <= 1.0


def test_negative_latency_rejected() -> None:
    dashboard = MetricsDashboard()
    with pytest.raises(ValueError, match="non-negative"):
        dashboard.record_request(-1.0)


def test_integration_throughput_after_delay() -> None:
    dashboard = MetricsDashboard()
    dashboard.record_request(50.0)
    time.sleep(0.01)
    assert dashboard.throughput_rps() > 0.0


def test_failure_path_increments_error_count() -> None:
    dashboard = MetricsDashboard()
    dashboard.record_request(20.0, success=False)
    assert dashboard.error_count == 1


def test_stress_many_requests() -> None:
    dashboard = MetricsDashboard()
    for _ in range(2_000):
        dashboard.record_request(1.0)
    summary = dashboard.summary()
    assert summary["request_count"] == 2000.0
    assert summary["error_rate"] == 0.0
