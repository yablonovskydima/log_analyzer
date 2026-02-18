from datetime import datetime
from dataclasses import dataclass, asdict, field


@dataclass
class LogRecord:
    ip: str
    timestamp: datetime
    method: str
    status: int
    response_size: int

@dataclass
class LogStats:
    status_count: dict[int, int]
    ip_count: dict[str, int]
    hour_count: dict[datetime, int]

@dataclass
class SortedStats:
    errors_by_status: dict[int, int] = field(default_factory=dict)
    top_ip_count: dict[str, int] = field(default_factory=dict)
    requests_per_hour: dict[datetime, int] = field(default_factory=dict)

    def serialize(self):
        data = asdict(self)
        data["requests_per_hour"] = {
            dt.isoformat(): count
            for dt, count in data["requests_per_hour"].items()
        }
        return data