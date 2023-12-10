# openvas_scanner.py
import os

def run_openvas_scan(target):
    scan_command = f"omp -u admin -w admin --create-target --name {target} --hosts {target}"
    os.system(scan_command)
    print(f"OpenVAS scan initiated for {target}")

if __name__ == "__main__":
    target_ip = input("Enter target IP for OpenVAS scan: ")
    run_openvas_scan(target_ip)
