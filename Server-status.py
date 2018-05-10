# Extract IP address from server-status page

import requests
import time
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

while True:

    r = requests.get('https://hostname/server-status', headers=headers)
    resp = re.findall( r'[0-9]+(?:\.[0-9]+){3}', r.text )
    print resp
    with open('ips.txt', 'a') as ff:
        ff.write(str(resp))
    time.sleep(20)
