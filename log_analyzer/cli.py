import argparse
from datetime import datetime, timezone
from log_analyzer.parser import parse_log
from log_analyzer.analyzer import analyze
from log_analyzer.report import cli_report, save_to_csv, save_to_json


def parse_date(value: str):
    formats = [
        "%d-%b-%Y",
        "%d-%b-%YT%H:%M",
        "%d-%b-%YT%H:%M:%S",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue

    raise argparse.ArgumentTypeError(
        "Date must be in format YYYY-MM-DD or YYYY-MM-DD HH:MM[:SS]"
    )


def main():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI")

    parser.add_argument(
        "--file",
        required=True,
        help="Path to log file"
    )

    parser.add_argument(
        "--out-csv",
        default="report.csv",
        help="Output CSV file"
    )

    parser.add_argument(
        "--out-json",
        default="report.json",
        help="Output JSON file"
    )

    parser.add_argument(
        "--from-date",
        type=parse_date,
        help="Start date filter"
    )

    parser.add_argument(
        "--method",
        help="Http method filter"
    )

    parser.add_argument(
        "--to-date",
        type=parse_date,
        help="End date filter"
    )

    args = parser.parse_args()

    records = parse_log(args.file)
    sorted_stats = analyze(records, args.from_date, args.to_date, args.method)
    cli_report(sorted_stats)

    if args.out_csv:
        save_to_csv(sorted_stats, args.out_csv)
        print(f"\nReport saved to {args.out_csv}")

    if args.out_json:
        save_to_json(sorted_stats, args.out_json)
        print(f"\nReport saved to {args.out_json}")

if __name__ == "__main__":
    main()