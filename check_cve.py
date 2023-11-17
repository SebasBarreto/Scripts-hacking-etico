import requests

def check_cve(service):
    cve_database = {
        "ssh": ["CVE-2020-15778"],
        "http": ["CVE-2019-6340"],
        # Añade más servicios y CVEs según sea necesario
    }
    return cve_database.get(service, [])

if __name__ == "__main__":
    service = input("Enter service name: ").lower()
    cves = check_cve(service)
    if cves:
        print(f"Known CVEs for {service}: {', '.join(cves)}")
    else:
        print(f"No known CVEs found for {service}.")
