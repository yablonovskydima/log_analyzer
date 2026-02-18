from log_analyzer.models import LogStats, SortedStats
from log_analyzer.models import LogRecord
from typing import Any, Generator
from collections import defaultdict

def analyze(records: Generator[LogRecord, Any, None], from_date=None, to_date=None, method=None):
    if from_date:
        records = [r for r in records if r.timestamp >= from_date]
    if to_date:
        records = [r for r in records if r.timestamp <= to_date]
    if method:
        records = [r for r in records if r.method == method]

    stats = _count_stats(records)
    sorted_stats = SortedStats()
    sorted_stats.errors_by_status = dict(
        sorted({s: c for s, c in stats.status_count.items() if s >= 400}.items(), key=lambda item: item[1], reverse=True)
    )
    sorted_stats.top_ip_count = dict(
        sorted(stats.ip_count.items(), key=lambda item: item[1], reverse=True)[:10]
    )
    sorted_stats.requests_per_hour = dict(
        sorted(stats.hour_count.items(), key=lambda item: item[0], reverse=True)
    )

    return sorted_stats

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
