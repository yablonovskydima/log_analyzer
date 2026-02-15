from datetime import datetime
from dataclasses import dataclass


@dataclass
class LogRecord:
    ip: str
    timestamp: datetime
    method: str
    status: int
    response_size: int
