# api_security_tester.py
import requests

def test_api_endpoint(url):
    # Prueba de inyección SQL
    sql_payload = {"query": "' OR '1'='1"}
    response = requests.post(url, data=sql_payload)
    if "error" not in response.text.lower():
        print(f"Potential SQL Injection vulnerability detected at {url}")

    # Prueba de XSS
    xss_payload = {"input": "<script>alert('XSS')</script>"}
    response = requests.post(url, data=xss_payload)
    if "<script>alert('XSS')</script>" in response.text:
        print(f"Potential XSS vulnerability detected at {url}")

if __name__ == "__main__":
    api_url = input("Enter the API endpoint URL: ")
    test_api_endpoint(api_url)
