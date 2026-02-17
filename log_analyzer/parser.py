import re
from datetime import datetime
from typing import Any, Generator

from .models import LogRecord

LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - '
    r'\[(?P<ts>[^\]]+)\] '
    r'"(?P<m>[A-Z]+) [^"]+" '
    r'(?P<s>\d{3}) '
    r'(?P<r>\d+)'
)


def parse_log(path: str) -> Generator[LogRecord, Any, None]:
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            record = _parse_line(line)
            if record:
                yield record


def _parse_line(line: str):
    matching = LOG_PATTERN.match(line)
    if matching:
        return LogRecord(
            ip=matching.group("ip"),
            timestamp=datetime.strptime(matching.group("ts"), "%d/%b/%Y:%H:%M:%S %z"),
            method=matching.group("m"),
            status=int(matching.group("s")),
            response_size=int(matching.group("r"))
        )
    return None
