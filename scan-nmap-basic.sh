#!/bin/bash

read -p "Enter target IP: " target
mkdir -p nmap_results
nmap -sV -O -Pn $target -oN nmap_results/$target_scan.txt
echo "Scan completed. Results saved in nmap_results/$target_scan.txt"
