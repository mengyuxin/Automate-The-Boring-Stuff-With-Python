#! python3
# luckySearch.py - opens several Baidu search results.

import requests
import sys
import webbrowser
import bs4

keyword = ' '.join(sys.argv[1:])

print('Searching...... for ' + keyword) # display text while downloading the page.
res = requests.get('http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' + keyword)
res.raise_for_status()

# Retrieve top search result links.
#print(res.text)
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get('href'))
    #webbrowser.open(linkElems[i].get('href'))
