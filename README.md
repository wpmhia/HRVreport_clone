# HRVreport_clone

A simple Heart Rate Variability (HRV) report generator with built-in debugging support.

## Features

- Calculate RMSSD (Root Mean Square of Successive Differences)
- Calculate SDNN (Standard Deviation of NN intervals)
- Comprehensive logging for debugging
- Easy-to-use API

## Usage

### Basic Usage

```python
from hrv_report import HRVAnalyzer

# Sample RR intervals in milliseconds
rr_intervals = [800, 810, 790, 805, 795, 808, 812, 798, 802, 807]

# Create analyzer with debug mode
analyzer = HRVAnalyzer(debug=True)

# Generate report
report = analyzer.generate_report(rr_intervals)
print(report)
```

### Running the Example

```bash
python hrv_report.py
```

## Debugging

The module includes comprehensive logging support for debugging:

- **Debug Mode**: Enable with `HRVAnalyzer(debug=True)` for verbose logging
- **Log Levels**: Automatically configured to show INFO and DEBUG messages
- **Detailed Output**: Each calculation step is logged for troubleshooting

### Debug Output Example

When debug mode is enabled, you'll see detailed logs like:
```
2024-01-01 12:00:00 - __main__ - DEBUG - HRVAnalyzer initialized with debug=True
2024-01-01 12:00:00 - __main__ - DEBUG - Calculating RMSSD for 10 intervals
2024-01-01 12:00:00 - __main__ - DEBUG - Successive differences calculated: [10, 20, 15, 10, 13]
2024-01-01 12:00:00 - __main__ - DEBUG - RMSSD calculated: 13.42 ms
```

## Requirements

Python 3.6 or higher (no external dependencies required)

