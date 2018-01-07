#! python3
# testRequests.py
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as err:
    print('There was a problem: %s ' % (err))

if res.status_code == requests.codes.ok:
    print('Size: ' + str(len(res.text)))
    #print(res.text[:253])

    playFile = open('.\\#temp\\RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)

    
