# ci_security_checks.py
import subprocess

def run_nmap_scan(target):
    result = subprocess.run(['nmap', '-sV', target], stdout=subprocess.PIPE)
    with open('nmap_scan.txt', 'w') as f:
        f.write(result.stdout.decode())
    print("Nmap scan completed. Results saved to nmap_scan.txt.")

def run_clamav_scan(target_dir):
    result = subprocess.run(['clamscan', '-r', target_dir], stdout=subprocess.PIPE)
    with open('clamav_scan.txt', 'w') as f:
        f.write(result.stdout.decode())
    print("ClamAV scan completed. Results saved to clamav_scan.txt.")

if __name__ == "__main__":
    target = input("Enter target for Nmap scan: ")
    run_nmap_scan(target)
    target_dir = input("Enter directory to scan with ClamAV: ")
    run_clamav_scan(target_dir)
