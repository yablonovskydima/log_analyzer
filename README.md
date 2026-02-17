# Python Log Analyzer
LogAnalyzer is a simple Python CLI tool for analyzing web server logs.
It provides quick insights into HTTP errors, top IP addresses, and request counts per hour, directly in the console or as a CSV report.

## Features
- Count HTTP errors by status codes (4xx, 5xx)
- Identify top IP addresses by request count
- Optional CSV report export
- Automatic CLI help and argument validation

## Usage
### Analyze a log file and display results in the console
`python -m log_analyzer.cli --file access.log`

### Analyze and save the report to CSV

`python -m log_analyzer.cli --file access.log --out report.csv`

### Logs format
`0000.0000.0000.0000 - - [00/DEC/2000:00:00:00 +0300] "GET /any/endpoint HTTP/1.0" 404 123456 "http://example/any/resource.php" "Any User Client"`
