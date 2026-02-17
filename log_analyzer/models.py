from datetime import datetime
from dataclasses import dataclass


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