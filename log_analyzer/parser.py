import re
from datetime import datetime
from typing import Any, Generator

from log_analyzer.models import LogRecord
from .models import LogRecord


def parse_log(path: str) -> Generator[LogRecord, Any, None]:
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            record = _parse_line(line)
            if record:
                yield record


def _parse_line(line: str):
    matching = re.match('', line)
    if matching:
        return LogRecord(
            ip=matching.group("ip"),
            timestamp=datetime.strptime(matching.group("ts")),
            method=matching.group("m"),
            status=int(matching.group("s")),
            response_size=int(matching.group("r"))
        )
    return None
