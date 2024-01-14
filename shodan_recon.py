# shodan_recon.py
import shodan

def shodan_search(api_key, query):
    api = shodan.Shodan(api_key)
    try:
        results = api.search(query)
        print(f"Results found: {results['total']}")
        for result in results['matches']:
            print(f"IP: {result['ip_str']} | Port: {result['port']} | Data: {result['data']}")
    except shodan.APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    key = input("Enter your Shodan API key: ")
    query = input("Enter your search query: ")
    shodan_search(key, query)
