#!/usr/bin/env python3
"""Lightweight performance metrics tracker for portfolio scripts/services."""

from __future__ import annotations

from dataclasses import dataclass, field
from statistics import mean
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
LOGGER = logging.getLogger("metrics_dashboard")


@dataclass(slots=True)
class MetricsDashboard:
    """Collects runtime metrics with safe defaults and validation."""

    start_time: float = field(default_factory=time.perf_counter)
    request_count: int = 0
    error_count: int = 0
    latencies_ms: list[float] = field(default_factory=list)

    def record_request(self, latency_ms: float, success: bool = True) -> None:
        """Record a request event.

        Args:
            latency_ms: request latency in milliseconds.
            success: whether request completed successfully.
        """
        if latency_ms < 0:
            raise ValueError("latency_ms must be non-negative")

        self.request_count += 1
        self.latencies_ms.append(latency_ms)

        if not success:
            self.error_count += 1
            LOGGER.warning("Recorded failed request latency=%sms", latency_ms)
        else:
            LOGGER.info("Recorded successful request latency=%sms", latency_ms)

    def uptime_seconds(self) -> float:
        return max(time.perf_counter() - self.start_time, 0.0)

    def average_latency_ms(self) -> float:
        return mean(self.latencies_ms) if self.latencies_ms else 0.0

    def throughput_rps(self) -> float:
        uptime = self.uptime_seconds()
        return self.request_count / uptime if uptime > 0 else 0.0

    def error_rate(self) -> float:
        if self.request_count == 0:
            return 0.0
        return self.error_count / self.request_count

    def summary(self) -> dict[str, float]:
        payload = {
            "request_count": float(self.request_count),
            "error_count": float(self.error_count),
            "average_latency_ms": round(self.average_latency_ms(), 2),
            "throughput_rps": round(self.throughput_rps(), 2),
            "uptime_seconds": round(self.uptime_seconds(), 2),
            "error_rate": round(self.error_rate(), 4),
        }
        LOGGER.info("Metrics summary generated: %s", payload)
        return payload


def demo() -> None:
    dashboard = MetricsDashboard()
    for latency, success in [(120.0, True), (95.0, True), (230.0, False), (100.0, True)]:
        dashboard.record_request(latency_ms=latency, success=success)
        time.sleep(0.01)

    print("Metrics Dashboard Summary")
    for key, value in dashboard.summary().items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    demo()
