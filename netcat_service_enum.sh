# netcat_service_enum.sh
#!/bin/bash

read -p "Enter target IP: " target
ports=(21 22 23 25 53 80 110 139 143 443 445 3389)

for port in "${ports[@]}"
do
    echo "Scanning port $port..."
    nc -zv $target $port
done
