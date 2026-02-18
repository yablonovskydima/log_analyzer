import csv
import json
from rich.console import Console
from rich.table import Table
from dataclasses import asdict

from log_analyzer.models import LogStats, SortedStats

console = Console()

def cli_report(stats):
    table_status = Table(title="Errors by Status")
    table_status.add_column("Status code", style="red", justify="right")
    table_status.add_column("Count", style="green", justify="right")

    for status, count in stats.errors_by_status.items():
        table_status.add_row(str(status), str(count))

    console.print(table_status)

    table_ip = Table(title="Top IPs by Requests")
    table_ip.add_column("IP", style="red", justify="right")
    table_ip.add_column("Count", style="green", justify="right")

    for ip, count in stats.top_ip_count.items():
        table_ip.add_row(str(ip), str(count))

    console.print(table_ip)

    for hour, count in stats.requests_per_hour.items():
        bar = "█" * (count // 10)
        print(f"{hour.strftime('%H:%M')} | {bar} ({count})")


def save_to_csv(stats, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["Errors by Status"])
        writer.writerow(["Status", "Count"])
        for status, count in stats.errors_by_status.items():
            writer.writerow([status, count])
        writer.writerow([])

        writer.writerow(["Top IPs By Count"])
        writer.writerow(["IP", "Count"])
        for ip, count in stats.top_ip_count.items():
            writer.writerow([ip, count])
        writer.writerow([])

        writer.writerow(["Requests By Hours"])
        writer.writerow(["Hour", "Count"])
        for hour, count in stats.requests_per_hour.items():
            writer.writerow([hour.strftime('%Y-%m-%d %H:%M'), count])
        writer.writerow([])

def save_to_json(stats, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stats.serialize(), f, indent=4, ensure_ascii=False)