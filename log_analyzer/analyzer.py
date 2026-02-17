from log_analyzer.models import LogStats
from log_analyzer.models import LogRecord
from typing import Any, Generator
from collections import defaultdict

def analyze(records: Generator[LogRecord, Any, None]):
    stats = _count_stats(records)
    error_by_status = {
        s: c for s, c in stats.status_count.items() if s >= 400
    }
    error_by_status = dict(
        sorted(error_by_status.items(), key=lambda item: item[1], reverse=True)
    )
    top_ip_count = dict(
        sorted(stats.ip_count.items(), key=lambda item: item[1], reverse=True)[:10]
    )
    requests_per_hour = dict(
        sorted(stats.hour_count.items(), key=lambda item: item[0], reverse=True)
    )

    return {
        "errors_by_status": error_by_status,
        "top_ip_count": top_ip_count,
        "requests_per_hour": requests_per_hour,
    }

def _count_stats(records: Generator[LogRecord, Any, None]) -> LogStats:
    status_count = defaultdict(int)
    ip_count = defaultdict(int)
    hour_count = defaultdict(int)

    for record in records:
        status_count[record.status] += 1
        ip_count[record.ip] += 1
        hour = record.timestamp.replace(minute=0, second=0, microsecond=0)
        hour_count[hour] += 1

    return LogStats(status_count, ip_count, hour_count)
