# subdomain_enum.py
import requests

def subdomain_enum(domain, wordlist):
    discovered = []
    with open(wordlist, 'r') as f:
        subdomains = f.read().splitlines()
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code < 400:
                print(f"Discovered: {sub}.{domain}")
                discovered.append(f"{sub}.{domain}")
        except requests.ConnectionError:
            pass
    return discovered

if __name__ == "__main__":
    target_domain = input("Enter target domain (e.g., example.com): ")
    wordlist_path = input("Enter path to subdomains wordlist: ")
    found_subdomains = subdomain_enum(target_domain, wordlist_path)
    print(f"Discovered subdomains for {target_domain}:")
    for sub in found_subdomains:
        print(sub)
