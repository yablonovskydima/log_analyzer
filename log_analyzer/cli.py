import argparse
from .parser import parse_log


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

    # execution
    records = parse_log(args.file)


if __name__ == "__main__":
    main()