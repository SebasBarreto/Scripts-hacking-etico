# concurrent_port_scanner.py
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        print(f"Port {port} is open")
    except:
        pass
    finally:
        s.close()

def main():
    target = input("Enter target IP: ")
    ports = range(1, 1025)
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)

if __name__ == "__main__":
    main()
