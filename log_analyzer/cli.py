import argparse
from log_analyzer.parser import parse_log
from log_analyzer.analyzer import analyze
from log_analyzer.report import cli_report, save_to_csv


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

    args = parser.parse_args()

    records = parse_log(args.file)
    sorted_stats = analyze(records)
    cli_report(sorted_stats)

    if args.out:
        save_to_csv(sorted_stats, args.out)
        print(f"\nReport saved to {args.out}")

if __name__ == "__main__":
    main()