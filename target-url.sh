#!/bin/bash

read -p "Enter target URL: " target
zap-cli start
zap-cli open-url $target
zap-cli spider $target
zap-cli active-scan $target
zap-cli report -o zap_report.html -f html
echo "Scan completed. Report saved as zap_report.html"
zap-cli shutdown
