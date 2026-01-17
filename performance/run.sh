#!/usr/bin/env bash

set -euo pipefail

JMETER_TEST="performance/smoke_api.jmx"
RESULTS="performance/results.jtl"
REPORT_DIR="performace/report"

rm -f "$RESULTS"
rm -rf "$REPOST_DIR"

jmeter -n -t "$JMETER_TEST" -l "$RESULTS" -e -o "$REPORT_DIR"

echo "Done. Report generated and available in $REPORT_DIR"