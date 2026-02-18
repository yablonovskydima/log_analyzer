import argparse
from datetime import datetime, timezone
from log_analyzer.parser import parse_log
from log_analyzer.analyzer import analyze
from log_analyzer.report import cli_report, save_to_csv


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
        "--out",
        default="report.csv",
        help="Output CSV file"
    )

    parser.add_argument(
        "--from-date",
        type=parse_date,
        help="Start date filter"
    )

    parser.add_argument(
        "--to-date",
        type=parse_date,
        help="End date filter"
    )

    args = parser.parse_args()

    records = parse_log(args.file)
    sorted_stats = analyze(records, args.from_date, args.to_date)
    cli_report(sorted_stats)

    if args.out:
        save_to_csv(sorted_stats, args.out)
        print(f"\nReport saved to {args.out}")

if __name__ == "__main__":
    main()