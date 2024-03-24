# security_audit.py
import os
import subprocess

def check_updates():
    print("Checking for system updates...")
    subprocess.run(['sudo', 'apt', 'update'])

def check_firewall():
    print("Checking UFW status...")
    subprocess.run(['sudo', 'ufw', 'status'])

def check_services():
    print("Listing active services...")
    subprocess.run(['systemctl', 'list-units', '--type=service', '--state=running'])

def audit():
    check_updates()
    check_firewall()
    check_services()
    print("Security audit completed.")

if __name__ == "__main__":
    audit()
