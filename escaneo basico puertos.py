import socket

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP: ")
    port_range = range(1, 1025)
    open_ports = scan_ports(target, port_range)
    print(f"Open ports on {target}: {open_ports}")
